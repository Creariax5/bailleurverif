#!/bin/bash
# Watchdog server.py BailleurVérif — restart si HTTP non-200 OU process dead
# Run via cron: */2 * * * *
set -u
LOG=/home/deploy/saas-florian/wedge-tool/watchdog.log
LOCK=/tmp/bv-watchdog.lock
SERVER_DIR=/home/deploy/saas-florian/wedge-tool
PORT=8102

# Prevent overlap
exec 9>"$LOCK"
flock -n 9 || exit 0

now() { date -u +%FT%TZ; }

# Probe 3s timeout
HTTP=$(curl -s -o /dev/null -w "%{http_code}" --max-time 3 "http://127.0.0.1:$PORT/" 2>/dev/null || echo "000")

if [ "$HTTP" = "200" ]; then
    exit 0
fi

# Down. Check process state.
PIDS=$(pgrep -f "python3 server.py" || true)

echo "[$(now)] DOWN http=$HTTP pids='$PIDS' — restarting" >> "$LOG"

# Kill any straggler (defensive)
if [ -n "$PIDS" ]; then
    kill -TERM $PIDS 2>/dev/null || true
    sleep 1
    pgrep -f "python3 server.py" | xargs -r kill -KILL 2>/dev/null || true
fi

# Restart
cd "$SERVER_DIR"
LOGFILE="server.log.watchdog-$(date -u +%FT%TZ).log"
nohup python3 server.py > "$LOGFILE" 2>&1 &
NEWPID=$!
sleep 3

# Verify
HTTP2=$(curl -s -o /dev/null -w "%{http_code}" --max-time 3 "http://127.0.0.1:$PORT/" 2>/dev/null || echo "000")
echo "[$(now)] RESTART pid=$NEWPID http_post=$HTTP2 logfile=$LOGFILE" >> "$LOG"
