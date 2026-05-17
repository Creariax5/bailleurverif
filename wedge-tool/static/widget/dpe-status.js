/*! BailleurVerif Widget v1 — script-injection embed (vanilla JS, 0 dep) */
(function(){
"use strict";
var BASE="https://bailleurverif.fr";
var s=document.currentScript;
if(!s){var all=document.getElementsByTagName("script");for(var i=all.length-1;i>=0;i--){if(/dpe-status\.js(\?|$)/.test(all[i].src||"")){s=all[i];break;}}}
if(!s)return;
function attr(k,d){var v=s.getAttribute("data-"+k);return v===null||v===""?d:v;}
var ville=attr("ville","").trim();
var dpe=(attr("dpe","")||"").trim().toUpperCase();
var theme=attr("theme","light");
var compact=attr("compact","false")==="true";
var DPE={A:{c:"ok",t:"Conforme location"},B:{c:"ok",t:"Conforme location"},C:{c:"ok",t:"Conforme location"},D:{c:"ok",t:"Conforme location"},E:{c:"warn",t:"Interdit location dès 2034"},F:{c:"warn",t:"Interdit nouvelle location dès 2028"},G:{c:"danger",t:"Interdit location depuis 2025"}};
function esc(x){return String(x==null?"":x).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[c];});}
function norm(x){return (x||"").toLowerCase().trim().normalize("NFD").replace(/[̀-ͯ]/g,"").replace(/\s+/g,"-").replace(/[^a-z0-9-]/g,"");}
var villeSlug=norm(ville);
var info=DPE[dpe]||null;
var utm="?utm_source=embed&utm_medium=widget&utm_campaign=dpe-status";
var href=BASE+"/"+(villeSlug?villeSlug+"-dpe-f-g-interdit-location.html":"")+utm;
if(!villeSlug)href=BASE+"/"+utm.substring(1);
var palette=(theme==="dark")?{bg:"#0f172a",fg:"#f1f5f9",muted:"#94a3b8",link:"#a5b4fc",border:"#1e293b",ok:"#10b981",warn:"#f59e0b",danger:"#ef4444"}:{bg:"#ffffff",fg:"#0f172a",muted:"#64748b",link:"#4338ca",border:"#e2e8f0",ok:"#059669",warn:"#d97706",danger:"#dc2626"};
var color=info?palette[info.c]:palette.muted;
var label=info?info.t:"Diagnostic bailleur DPE";
var sub=(ville?esc(ville)+" · ":"")+"Source officielle : Loi Climat & Résilience";
var html;
if(compact){
  html='<a href="'+esc(href)+'" target="_blank" rel="noopener nofollow" style="display:inline-flex;align-items:center;gap:6px;padding:4px 10px;border:1px solid '+palette.border+';border-radius:999px;background:'+palette.bg+';color:'+palette.fg+';font:600 12px/1 -apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif;text-decoration:none;vertical-align:middle"><span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:'+color+'"></span>DPE '+esc(dpe||"?")+' · '+esc(label)+'<span style="opacity:.6;font-weight:400">→ bailleurverif.fr</span></a>';
}else{
  html='<div style="display:block;max-width:380px;margin:12px 0;padding:14px 16px;border:1px solid '+palette.border+';border-radius:10px;background:'+palette.bg+';color:'+palette.fg+';font:14px/1.45 -apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif;box-sizing:border-box">'+
    '<div style="display:flex;align-items:center;gap:8px;font-size:11px;color:'+palette.muted+';text-transform:uppercase;letter-spacing:.05em;margin-bottom:6px"><span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:'+color+'"></span>BailleurVérif · DPE '+esc(dpe||"?")+'</div>'+
    '<div style="font-size:16px;font-weight:700;margin-bottom:4px;color:'+palette.fg+'">'+esc(label)+'</div>'+
    '<div style="font-size:12px;color:'+palette.muted+';margin-bottom:10px">'+sub+'</div>'+
    '<a href="'+esc(href)+'" target="_blank" rel="noopener nofollow" style="display:inline-block;padding:7px 12px;background:'+palette.link+';color:#fff;text-decoration:none;border-radius:6px;font-size:12px;font-weight:600">Vérifier conformité gratuitement →</a>'+
    '<div style="font-size:10px;color:'+palette.muted+';margin-top:8px"><a href="'+BASE+utm+'" target="_blank" rel="noopener nofollow" style="color:'+palette.muted+';text-decoration:none">bailleurverif.fr</a> · MAJ 2026</div>'+
  '</div>';
}
var holder=document.createElement("span");
holder.setAttribute("data-bvw","dpe-status");
holder.innerHTML=html;
s.parentNode.insertBefore(holder,s.nextSibling);
try{
  var img=new Image(1,1);
  img.referrerPolicy="no-referrer-when-downgrade";
  img.src=BASE+"/api/embed/view?w=dpe-status&v="+encodeURIComponent(villeSlug||"-")+"&d="+encodeURIComponent(dpe||"-")+"&t="+Date.now();
}catch(e){}
})();
