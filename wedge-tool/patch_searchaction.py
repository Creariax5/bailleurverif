#!/usr/bin/env python3
"""run-157: inject SearchAction into all pages declaring WebSite JSON-LD.
Handles both compact (no-space) and spaced JSON variants.
Idempotent: skip if SearchAction marker already present in the WebSite block."""
import os, re

STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

# Marker to detect already-patched WebSite blocks (both variants)
SEARCHACTION_MARKER = '"SearchAction"'

# Compact variant
COMPACT_OLD = '{"@type":"WebSite","@id":"https://bailleurverif.fr/#website","url":"https://bailleurverif.fr","name":"BailleurVérif","inLanguage":"fr-FR","publisher":{"@id":"https://bailleurverif.fr/#organization"}}'
COMPACT_NEW = '{"@type":"WebSite","@id":"https://bailleurverif.fr/#website","url":"https://bailleurverif.fr","name":"BailleurVérif","inLanguage":"fr-FR","publisher":{"@id":"https://bailleurverif.fr/#organization"},"potentialAction":{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://bailleurverif.fr/?q={search_term_string}"},"query-input":"required name=search_term_string"}}'

# Spaced variant
SPACED_OLD = '{"@type": "WebSite", "@id": "https://bailleurverif.fr/#website", "url": "https://bailleurverif.fr", "name": "BailleurVérif", "inLanguage": "fr-FR", "publisher": {"@id": "https://bailleurverif.fr/#organization"}}'
SPACED_NEW = '{"@type": "WebSite", "@id": "https://bailleurverif.fr/#website", "url": "https://bailleurverif.fr", "name": "BailleurVérif", "inLanguage": "fr-FR", "publisher": {"@id": "https://bailleurverif.fr/#organization"}, "potentialAction": {"@type": "SearchAction", "target": {"@type": "EntryPoint", "urlTemplate": "https://bailleurverif.fr/?q={search_term_string}"}, "query-input": "required name=search_term_string"}}'

patched_compact, patched_spaced, already, no_match = 0, 0, 0, 0
for name in sorted(os.listdir(STATIC_DIR)):
    if not name.endswith(".html"):
        continue
    path = os.path.join(STATIC_DIR, name)
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    # Skip if SearchAction already present
    if SEARCHACTION_MARKER in src:
        already += 1
        continue
    if COMPACT_OLD in src:
        src = src.replace(COMPACT_OLD, COMPACT_NEW)
        patched_compact += 1
    elif SPACED_OLD in src:
        src = src.replace(SPACED_OLD, SPACED_NEW)
        patched_spaced += 1
    else:
        no_match += 1
        continue
    with open(path, "w", encoding="utf-8") as f:
        f.write(src)

print(f"patched_compact={patched_compact} patched_spaced={patched_spaced} already_present={already} no_match={no_match}")
