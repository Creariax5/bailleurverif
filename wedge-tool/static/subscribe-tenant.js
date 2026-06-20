// Shared subscribe handler for locataire SEO city pages — backprop /api/subscribe + intent_signal.
// Form contract: #subscribe-form / #sub-email / #sub-intent (select 6 options) / #sub-msg.
// Topic forced 'loyer-legal'. Source = location.pathname. Consent implicit via submit.
(function(){
  var f=document.getElementById('subscribe-form');if(!f)return;
  var em=document.getElementById('sub-email');var msg=document.getElementById('sub-msg');
  f.addEventListener('submit',async function(e){
    e.preventDefault();msg.textContent='Envoi…';msg.style.color='#64748b';
    try{
      try{fetch('/api/funnel/event',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({sessionId:null,event_type:'email_submitted',path:location.pathname,meta:{kind:'inline_subscribe_tenant',has_at:(em.value||'').indexOf('@')>=0}})}).catch(function(){});}catch(_){}
      var intent_signal=(document.getElementById('sub-intent')||{}).value||'';
      var r=await fetch('/api/subscribe',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email:em.value,topic:'loyer-legal',source:location.pathname,consent:true,intent_signal:intent_signal})});
      var j=await r.json();
      if(r.ok&&j.ok){msg.textContent='✓ Inscrit. Confirmez via l\'email envoyé.';msg.style.color='#065f46';em.value='';}
      else{msg.textContent='Erreur : '+(j.error||'inconnue');msg.style.color='#b91c1c';}
    }catch(err){msg.textContent='Erreur réseau, réessayez.';msg.style.color='#b91c1c';}
  });
})();
