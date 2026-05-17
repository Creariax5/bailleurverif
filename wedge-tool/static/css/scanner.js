(function(){
  var btn = document.getElementById('scan-btn');
  var inp = document.getElementById('scan-input');
  if (!btn || !inp) return;
  var box = document.getElementById('scan-result');
  var badge = document.getElementById('scan-badge');
  var verdict = document.getElementById('scan-verdict');
  var marker = document.getElementById('scan-marker');
  var lbl = document.getElementById('scan-score-label');
  var flagsEl = document.getElementById('scan-flags');
  var flagsBlock = document.getElementById('scan-flags-block');
  var adviceEl = document.getElementById('scan-advice');
  var adviceBlock = document.getElementById('scan-advice-block');
  var disc = document.getElementById('scan-disclaimer');

  function render(r){
    box.classList.remove('hidden');
    var sev = r.severity || 'safe';
    badge.textContent = sev === 'high' ? 'Risque élevé' : sev === 'medium' ? 'Vigilance' : sev === 'low' ? 'Attention' : 'Aucun signal';
    badge.className = 'badge badge-' + sev;
    verdict.textContent = r.verdict || '';
    marker.style.left = (r.score || 0) + '%';
    lbl.textContent = 'Score : ' + (r.score || 0) + '/100';
    flagsEl.innerHTML = '';
    if (r.flags && r.flags.length){
      flagsBlock.classList.remove('hidden');
      r.flags.forEach(function(f){
        var div = document.createElement('div');
        div.className = 'flag flag-' + (f.severity || 'low');
        div.innerHTML = '<span class="badge badge-' + (f.severity || 'low') + '">' + (f.severity || 'low').toUpperCase() + '</span><span>' + f.label + '</span>';
        flagsEl.appendChild(div);
      });
    } else {
      flagsBlock.classList.add('hidden');
    }
    adviceEl.innerHTML = '';
    if (r.advice && r.advice.length){
      adviceBlock.classList.remove('hidden');
      r.advice.forEach(function(a){
        var li = document.createElement('li'); li.textContent = a; adviceEl.appendChild(li);
      });
    } else {
      adviceBlock.classList.add('hidden');
    }
    disc.textContent = r.disclaimer || '';
    box.scrollIntoView({behavior:'smooth', block:'start'});
  }

  btn.addEventListener('click', async function(){
    var text = (inp.value || '').trim();
    if (text.length < 20){
      alert('Collez au moins quelques phrases de l’annonce (minimum 20 caractères).');
      return;
    }
    btn.disabled = true; btn.textContent = 'Analyse en cours…';
    try {
      var res = await fetch('/api/scan-annonce', {
        method: 'POST', headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({text: text.slice(0, 8000)})
      });
      var data = await res.json();
      if (data.ok){ render(data); }
      else { alert('Erreur : ' + (data.error || 'analyse impossible')); }
    } catch (e) {
      alert('Erreur réseau : ' + e.message);
    } finally {
      btn.disabled = false; btn.textContent = 'Analyser l’annonce';
    }
  });
})();
