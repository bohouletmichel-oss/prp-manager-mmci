<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PRP Manager — MMCI</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap');
:root{--bg:#F4F5F7;--sidebar:#0F1C2E;--sidebar-active:#1D6FA4;--white:#FFFFFF;--text:#1A2332;--muted:#6B7A8D;--border:#E2E8F0;--green:#22C55E;--green-bg:#DCFCE7;--green-t:#15803D;--red:#EF4444;--red-bg:#FEE2E2;--red-t:#B91C1C;--yellow:#F59E0B;--yellow-bg:#FEF3C7;--yellow-t:#92400E;--blue:#1D6FA4;--shadow:0 1px 3px rgba(0,0,0,.08);}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'DM Sans',sans-serif;background:var(--bg);color:var(--text);display:flex;height:100vh;overflow:hidden;font-size:14px;}
.sidebar{width:230px;background:var(--sidebar);display:flex;flex-direction:column;flex-shrink:0;}
.s-logo{padding:18px 16px;border-bottom:1px solid rgba(255,255,255,.07);}
.s-badge-wrap{width:34px;height:34px;background:var(--blue);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:13px;margin-bottom:8px;}
.s-title{color:#fff;font-size:13px;font-weight:600;}
.s-sub{color:rgba(255,255,255,.4);font-size:11px;margin-top:2px;}
.s-pills{display:flex;gap:5px;padding:8px 16px;border-bottom:1px solid rgba(255,255,255,.07);}
.pill{font-size:10px;padding:2px 7px;border-radius:10px;font-weight:500;}
.pill-b{background:rgba(29,111,164,.3);color:#60B4E8;}
.pill-g{background:rgba(34,197,94,.2);color:#4ADE80;}
.s-nav{padding:8px;flex:1;overflow-y:auto;}
.nav-sec{font-size:9px;text-transform:uppercase;letter-spacing:.08em;color:rgba(255,255,255,.3);padding:10px 8px 4px;font-weight:600;}
.nav-item{display:flex;align-items:center;gap:8px;padding:7px 10px;border-radius:6px;cursor:pointer;color:rgba(255,255,255,.55);font-size:12.5px;transition:all .15s;margin-bottom:1px;}
.nav-item:hover{background:rgba(255,255,255,.08);color:rgba(255,255,255,.9);}
.nav-item.active{background:var(--sidebar-active);color:#fff;font-weight:500;}
.n-badge{margin-left:auto;background:var(--red);color:#fff;font-size:9px;padding:1px 5px;border-radius:8px;font-weight:600;}
.main{flex:1;display:flex;flex-direction:column;overflow:hidden;}
.topbar{background:var(--white);border-bottom:1px solid var(--border);padding:0 24px;height:52px;display:flex;align-items:center;justify-content:space-between;box-shadow:var(--shadow);flex-shrink:0;}
.tb-title{font-size:16px;font-weight:600;}
.tb-sub{font-size:11px;color:var(--muted);margin-top:1px;}
.tb-actions{display:flex;gap:8px;}
.btn{font-family:inherit;font-size:12px;font-weight:500;padding:6px 14px;border-radius:6px;border:none;cursor:pointer;transition:all .15s;display:flex;align-items:center;gap:5px;}
.btn-p{background:var(--blue);color:#fff;}.btn-p:hover{background:#165f8e;}
.btn-o{background:transparent;border:1px solid var(--border);color:var(--muted);}.btn-o:hover{background:var(--bg);color:var(--text);}
.btn-sm{font-size:11px;padding:4px 10px;}
.btn-danger{background:var(--red-bg);color:var(--red-t);border:1px solid #fca5a5;}
.content{flex:1;overflow-y:auto;padding:20px 24px;}
.page{display:none;}.page.active{display:block;}
.kgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:20px;}
.kcard{background:var(--white);border-radius:10px;padding:16px;box-shadow:var(--shadow);}
.klbl{font-size:11px;color:var(--muted);font-weight:500;text-transform:uppercase;letter-spacing:.04em;margin-bottom:6px;}
.kval{font-size:28px;font-weight:700;line-height:1;margin-bottom:4px;}
.kdelta{font-size:11px;color:var(--muted);}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px;}
.card{background:var(--white);border-radius:10px;padding:16px;box-shadow:var(--shadow);}
.card-full{background:var(--white);border-radius:10px;padding:16px;box-shadow:var(--shadow);margin-bottom:16px;}
.ctitle{font-size:13px;font-weight:600;margin-bottom:12px;display:flex;align-items:center;gap:6px;}
.tw{overflow-x:auto;}
table{width:100%;border-collapse:collapse;font-size:12.5px;}
th{background:var(--bg);color:var(--muted);font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:.04em;padding:8px 12px;text-align:left;border-bottom:1px solid var(--border);}
td{padding:9px 12px;border-bottom:1px solid var(--border);color:var(--text);vertical-align:middle;}
tr:last-child td{border-bottom:none;}
tr:hover td{background:#F8FAFC;}
.badge{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:600;padding:3px 9px;border-radius:20px;white-space:nowrap;}
.b-ok{background:var(--green-bg);color:var(--green-t);}
.b-nc{background:var(--red-bg);color:var(--red-t);}
.b-ec{background:var(--yellow-bg);color:var(--yellow-t);}
.b-na{background:#F1F5F9;color:#64748B;}
.pbar{height:5px;background:var(--border);border-radius:3px;overflow:hidden;margin-top:3px;}
.pfill{height:100%;border-radius:3px;}
.fgrid{display:grid;grid-template-columns:1fr 1fr;gap:12px;}
.fg{display:flex;flex-direction:column;gap:5px;}
.fg.full{grid-column:1/-1;}
label{font-size:12px;font-weight:500;color:var(--muted);}
input,select,textarea{font-family:inherit;font-size:13px;padding:8px 10px;border:1.5px solid var(--border);border-radius:6px;color:var(--text);background:var(--white);outline:none;transition:border .15s;width:100%;}
input:focus,select:focus,textarea:focus{border-color:var(--blue);}
textarea{resize:vertical;min-height:70px;}
.fa{display:flex;gap:8px;justify-content:flex-end;margin-top:14px;padding-top:12px;border-top:1px solid var(--border);}
.modal-ov{position:fixed;inset:0;background:rgba(0,0,0,.4);display:none;align-items:center;justify-content:center;z-index:100;}
.modal-ov.open{display:flex;}
.modal{background:var(--white);border-radius:12px;padding:22px;width:560px;max-height:90vh;overflow-y:auto;box-shadow:0 20px 60px rgba(0,0,0,.15);}
.mhdr{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px;}
.mtitle{font-size:15px;font-weight:600;}
.mclose{background:none;border:none;font-size:22px;cursor:pointer;color:var(--muted);}
.alert{border-radius:8px;padding:10px 14px;font-size:12px;display:flex;gap:8px;margin-bottom:14px;}
.alert-i{background:#DBEAFE;color:#1E40AF;border-left:3px solid var(--blue);}
.alert-w{background:var(--yellow-bg);color:var(--yellow-t);border-left:3px solid var(--yellow);}
.alert-s{background:var(--green-bg);color:var(--green-t);border-left:3px solid var(--green);display:none;}
.bar-chart{display:flex;gap:4px;align-items:flex-end;height:100px;}
.bi{display:flex;flex-direction:column;align-items:center;flex:1;gap:3px;}
.bar{width:100%;border-radius:3px 3px 0 0;transition:height .4s;}
.blbl{font-size:7.5px;color:var(--muted);text-align:center;line-height:1.2;}
.syn-hdr{text-align:center;padding:20px;border-bottom:2px solid var(--border);margin-bottom:20px;}
.syn-title{font-size:18px;font-weight:700;}
.syn-sub{font-size:12px;color:var(--muted);margin-top:4px;}
.sec-title{font-size:13px;font-weight:700;margin-bottom:10px;padding-bottom:6px;border-bottom:2px solid var(--blue);display:inline-block;}
.tag{display:inline-block;font-size:10px;font-weight:600;padding:2px 8px;border-radius:4px;}
.toast{position:fixed;bottom:24px;right:24px;background:#1A2332;color:#fff;padding:10px 18px;border-radius:8px;font-size:12px;z-index:999;transform:translateY(20px);opacity:0;transition:all .3s;pointer-events:none;}
.toast.show{transform:translateY(0);opacity:1;}
.kv-g{color:var(--green-t);}.kv-r{color:var(--red-t);}.kv-b{color:var(--blue);}.kv-y{color:var(--yellow-t);}
</style>
</head>
<body>

<nav class="sidebar">
  <div class="s-logo">
    <div class="s-badge-wrap">MM</div>
    <div class="s-title">PRP Manager – MMCI</div>
    <div class="s-sub">Suivi des Programmes Prérequis</div>
  </div>
  <div class="s-pills">
    <span class="pill pill-b" id="sb-count">… PRP</span>
    <span class="pill pill-g">ISO 22000</span>
  </div>
  <div class="s-nav">
    <div class="nav-sec">Tableau de bord</div>
    <div class="nav-item active" onclick="go('dashboard',this)">📊 Tableau de bord</div>
    <div class="nav-sec">Programmes Prérequis</div>
    <div class="nav-item" onclick="go('prps',this)">📋 Tous les PRP</div>
    <div class="nav-item" onclick="go('verifications',this)">✅ Vérifications</div>
    <div class="nav-item" onclick="go('planning',this)">📅 Planning</div>
    <div class="nav-sec">Qualité</div>
    <div class="nav-item" onclick="go('nc',this)">⚠️ Non-conformités <span class="n-badge" id="nc-badge">…</span></div>
    <div class="nav-item" onclick="go('capa',this)">🔧 Actions CAPA</div>
    <div class="nav-sec">Audit & Rapports</div>
    <div class="nav-item" onclick="go('kpi',this)">📈 KPIs</div>
    <div class="nav-item" onclick="go('rapport',this)">📄 Rapport direction</div>
  </div>
</nav>

<div class="main">
  <header class="topbar">
    <div>
      <div class="tb-title" id="pg-title">Tableau de bord</div>
      <div class="tb-sub" id="pg-sub">Vue générale — MMCI · ISO 22000</div>
    </div>
    <div class="tb-actions">
      <button class="btn btn-o" onclick="exportCSV()">⬇ CSV</button>
      <button class="btn btn-p" onclick="openModal('m-add-prp')">+ Nouveau PRP</button>
    </div>
  </header>

  <main class="content">

    <!-- DASHBOARD -->
    <div class="page active" id="page-dashboard">
      <div class="kgrid" id="kgrid"></div>
      <div class="g2">
        <div class="card"><div class="ctitle">📊 Score par PRP</div><div class="bar-chart" id="barchart"></div></div>
        <div class="card"><div class="ctitle">🥧 Répartition statuts</div>
          <div style="display:flex;align-items:center;gap:16px;">
            <canvas id="donut" width="110" height="110"></canvas>
            <div id="donut-leg" style="font-size:11px;"></div>
          </div>
        </div>
      </div>
      <div class="card-full"><div class="ctitle">📋 Récapitulatif PRP</div>
        <div class="tw"><table><thead><tr><th>Programme PRP</th><th>Catégorie</th><th>Responsable</th><th>Score T2</th><th>Statut</th><th>Prochain audit</th></tr></thead>
        <tbody id="dash-tbody"></tbody></table></div>
      </div>
    </div>

    <!-- TOUS PRP -->
    <div class="page" id="page-prps">
      <div class="alert alert-i">ℹ️ Cliquer sur ✏️ pour modifier un PRP. Les données sont sauvegardées en base de données.</div>
      <div class="card-full">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
          <div class="ctitle" style="margin:0;">Liste des PRP</div>
          <input type="text" id="search" oninput="filterTable()" placeholder="🔍 Rechercher…" style="width:200px;">
        </div>
        <div class="tw"><table><thead><tr><th>ID</th><th>Nom</th><th>Catégorie</th><th>Responsable</th><th>Fréquence</th><th>T1</th><th>T2</th><th>Statut</th><th>Actions</th></tr></thead>
        <tbody id="prp-tbody"></tbody></table></div>
      </div>
    </div>

    <!-- VERIFICATIONS -->
    <div class="page" id="page-verifications">
      <div class="g2">
        <div class="card-full" style="margin:0;">
          <div class="ctitle">➕ Nouvelle vérification</div>
          <div id="verif-ok" class="alert alert-s">✅ Vérification enregistrée !</div>
          <div class="fgrid">
            <div class="fg"><label>PRP *</label><select id="v-prp"></select></div>
            <div class="fg"><label>Date *</label><input type="date" id="v-date"></div>
            <div class="fg"><label>Résultat *</label>
              <select id="v-res"><option value="">--</option><option>Conforme</option><option>Non-Conforme</option><option>En cours</option></select></div>
            <div class="fg"><label>Vérificateur *</label><input type="text" id="v-agent" placeholder="Nom"></div>
            <div class="fg full"><label>Observations</label><textarea id="v-obs" placeholder="Observations…"></textarea></div>
          </div>
          <div class="fa"><button class="btn btn-o" onclick="resetForm(['v-prp','v-date','v-res','v-agent','v-obs'])">Annuler</button>
          <button class="btn btn-p" onclick="saveVerif()">💾 Enregistrer</button></div>
        </div>
        <div class="card-full" style="margin:0;"><div class="ctitle">📜 Historique</div>
          <div class="tw"><table><thead><tr><th>Date</th><th>PRP</th><th>Résultat</th><th>Agent</th></tr></thead>
          <tbody id="verif-tbody"></tbody></table></div>
        </div>
      </div>
    </div>

    <!-- NC -->
    <div class="page" id="page-nc">
      <div class="alert alert-w" id="nc-alert">⚠️ Chargement…</div>
      <div class="card-full"><div class="ctitle">❌ Non-conformités actives</div>
        <div class="tw"><table><thead><tr><th>PRP</th><th>Description</th><th>Gravité</th><th>Responsable</th><th>Échéance</th><th>Avancement</th><th>Statut</th></tr></thead>
        <tbody id="nc-tbody"></tbody></table></div>
      </div>
      <div class="card-full"><div class="ctitle">➕ Déclarer une NC</div>
        <div class="fgrid">
          <div class="fg"><label>PRP *</label><select id="nc-prp"></select></div>
          <div class="fg"><label>Gravité *</label>
            <select id="nc-grav"><option value="">--</option><option>Critique</option><option>Majeure</option><option>Mineure</option></select></div>
          <div class="fg"><label>Responsable *</label><input type="text" id="nc-resp" placeholder="Nom"></div>
          <div class="fg"><label>Échéance *</label><input type="date" id="nc-date"></div>
          <div class="fg full"><label>Description *</label><textarea id="nc-desc" placeholder="Décrire la non-conformité…"></textarea></div>
        </div>
        <div class="fa"><button class="btn btn-o" onclick="resetForm(['nc-prp','nc-grav','nc-resp','nc-date','nc-desc'])">Annuler</button>
        <button class="btn btn-p" onclick="saveNC()">💾 Enregistrer NC</button></div>
      </div>
    </div>

    <!-- CAPA -->
    <div class="page" id="page-capa">
      <div class="card-full"><div class="ctitle">🔧 Plan d'actions CAPA</div>
        <div class="tw"><table><thead><tr><th>PRP</th><th>Action corrective</th><th>Responsable</th><th>Échéance</th><th>Avancement</th><th>Statut</th></tr></thead>
        <tbody id="capa-tbody"></tbody></table></div>
      </div>
      <div class="card-full"><div class="ctitle">➕ Nouvelle action CAPA</div>
        <div class="fgrid">
          <div class="fg"><label>PRP *</label><select id="ca-prp"></select></div>
          <div class="fg"><label>Responsable *</label><input type="text" id="ca-resp" placeholder="Nom"></div>
          <div class="fg"><label>Échéance *</label><input type="date" id="ca-date"></div>
          <div class="fg"><label>Avancement (%)</label><input type="number" id="ca-av" min="0" max="100" value="0"></div>
          <div class="fg full"><label>Action corrective *</label><textarea id="ca-action" placeholder="Décrire l'action…"></textarea></div>
        </div>
        <div class="fa"><button class="btn btn-p" onclick="saveCAPA()">💾 Enregistrer</button></div>
      </div>
    </div>

    <!-- KPI -->
    <div class="page" id="page-kpi">
      <div class="kgrid" id="kgrid2"></div>
      <div class="g2">
        <div class="card"><div class="ctitle">📈 Évolution conformité</div><div id="trend" style="display:flex;flex-direction:column;gap:6px;"></div></div>
        <div class="card"><div class="ctitle">🎯 Score par PRP</div><div id="kpi-bars" style="display:flex;flex-direction:column;gap:6px;"></div></div>
      </div>
    </div>

    <!-- PLANNING -->
    <div class="page" id="page-planning">
      <div class="card-full"><div class="ctitle">📅 Planning audits 2026</div>
        <div class="tw"><table><thead><tr><th>Programme PRP</th><th>Fréquence</th><th>Prochain audit</th><th>Responsable</th><th>Statut</th></tr></thead>
        <tbody id="plan-tbody"></tbody></table></div>
      </div>
    </div>

    <!-- RAPPORT -->
    <div class="page" id="page-rapport">
      <div class="alert alert-i">ℹ️ Rapport généré automatiquement depuis la base de données.</div>
      <div class="card-full">
        <div class="syn-hdr">
          <div class="syn-title">RAPPORT DE REVUE DE DIRECTION — SMSA</div>
          <div class="syn-sub">Suivi des Programmes Prérequis (PRP) — MMCI</div>
          <div class="syn-sub" id="rpt-date"></div>
        </div>
        <div style="margin-bottom:20px;"><div class="sec-title">1. Résumé exécutif</div>
          <div class="kgrid" id="rpt-kpi" style="margin-top:12px;grid-template-columns:repeat(4,1fr);"></div>
        </div>
        <div style="margin-bottom:20px;"><div class="sec-title">2. Bilan par PRP</div>
          <div class="tw" style="margin-top:12px;"><table><thead><tr><th>PRP</th><th>Responsable</th><th>Score T1</th><th>Score T2</th><th>Évolution</th><th>Statut</th></tr></thead>
          <tbody id="rpt-tbody"></tbody></table></div>
        </div>
        <div style="margin-bottom:20px;"><div class="sec-title">3. Non-conformités & Actions</div>
          <div class="tw" style="margin-top:12px;"><table><thead><tr><th>PRP</th><th>Description</th><th>Gravité</th><th>Responsable</th><th>Échéance</th></tr></thead>
          <tbody id="rpt-nc"></tbody></table></div>
        </div>
        <div><div class="sec-title">4. Conclusions</div>
          <div id="rpt-conclu" style="background:var(--bg);border-radius:8px;padding:14px;font-size:12.5px;line-height:1.8;margin-top:12px;"></div>
        </div>
      </div>
      <div style="display:flex;justify-content:flex-end;gap:8px;margin-top:12px;">
        <button class="btn btn-o" onclick="window.print()">🖨️ Imprimer</button>
      </div>
    </div>

  </main>
</div>

<!-- MODAL EDIT/ADD PRP -->
<div class="modal-ov" id="m-add-prp">
  <div class="modal">
    <div class="mhdr"><div class="mtitle" id="modal-mode-title">➕ Nouveau PRP</div>
    <button class="mclose" onclick="closeModal('m-add-prp')">×</button></div>
    <input type="hidden" id="edit-id">
    <div class="fgrid">
      <div class="fg full"><label>Nom du PRP *</label><input type="text" id="f-nom" placeholder="Ex: Nettoyage & Désinfection"></div>
      <div class="fg"><label>Catégorie *</label>
        <select id="f-cat"><option>Hygiène</option><option>Qualité</option><option>Infrastructure</option><option>Environnement</option><option>RH</option><option>Achats</option><option>Stockage</option></select></div>
      <div class="fg"><label>Responsable *</label><input type="text" id="f-resp" placeholder="Nom du responsable"></div>
      <div class="fg"><label>Fréquence</label>
        <select id="f-freq"><option>Quotidien</option><option>Hebdomadaire</option><option>Mensuel</option><option>Trimestriel</option><option>Semestriel</option><option>Annuel</option></select></div>
      <div class="fg"><label>Score T1 (%)</label><input type="number" id="f-t1" min="0" max="100" value="0"></div>
      <div class="fg"><label>Score T2 (%)</label><input type="number" id="f-t2" min="0" max="100" value="0"></div>
      <div class="fg"><label>Statut</label>
        <select id="f-statut"><option>Conforme</option><option>Non-Conforme</option><option>En cours</option><option>Non évalué</option></select></div>
      <div class="fg"><label>Prochain audit</label><input type="date" id="f-audit"></div>
    </div>
    <div class="fa">
      <button class="btn btn-o" onclick="closeModal('m-add-prp')">Annuler</button>
      <button class="btn btn-p" onclick="savePRP()">💾 Enregistrer</button>
    </div>
  </div>
</div>

<div class="toast" id="toast"></div>

<script>
// ── helpers ──
const scColor = v => v>=80?'#22C55E':v>=60?'#F59E0B':'#EF4444';
const badge = s => {
  const m = {Conforme:['b-ok','✓'],'Non-Conforme':['b-nc','✗'],'En cours':['b-ec','⏳']};
  const [cls,ic] = m[s]||['b-na','—'];
  return `<span class="badge ${cls}">${ic} ${s||'Non évalué'}</span>`;
};
function toast(msg, dur=2800){
  const t=document.getElementById('toast'); t.textContent=msg; t.classList.add('show');
  setTimeout(()=>t.classList.remove('show'), dur);
}
function resetForm(ids){ids.forEach(id=>document.getElementById(id).value='');}
function openModal(id){document.getElementById(id).classList.add('open');}
function closeModal(id){document.getElementById(id).classList.remove('open');}
document.querySelectorAll('.modal-ov').forEach(m=>m.addEventListener('click',e=>{if(e.target===m)m.classList.remove('open');}));

// ── navigation ──
const titles={
  dashboard:['Tableau de bord','Vue générale — MMCI · ISO 22000'],
  prps:['Tous les PRP','Gestion des Programmes Prérequis'],
  verifications:['Vérifications','Enregistrement des vérifications terrain'],
  planning:['Planning','Calendrier des audits PRP 2026'],
  nc:['Non-conformités','Gestion des écarts détectés'],
  capa:['Actions CAPA','Plan d\'actions correctives'],
  kpi:['KPIs','Indicateurs clés de performance'],
  rapport:['Rapport direction','Synthèse automatique du SMSA'],
};
function go(page, el){
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
  document.getElementById('page-'+page).classList.add('active');
  if(el)el.classList.add('active');
  const [t,s]=titles[page]||[page,''];
  document.getElementById('pg-title').textContent=t;
  document.getElementById('pg-sub').textContent=s;
  render(page);
}

// ── API calls ──
async function api(url, method='GET', body=null){
  const opts={method, headers:{'Content-Type':'application/json'}};
  if(body) opts.body=JSON.stringify(body);
  const r=await fetch(url,opts);
  if(!r.ok) throw new Error(await r.text());
  return r.json();
}

// ── render router ──
async function render(page){
  if(page==='dashboard') await renderDashboard();
  if(page==='prps') await renderPRPs();
  if(page==='verifications') await renderVerifs();
  if(page==='nc') await renderNC();
  if(page==='capa') await renderCAPA();
  if(page==='kpi') await renderKPI();
  if(page==='planning') await renderPlanning();
  if(page==='rapport') await renderRapport();
}

// ── DASHBOARD ──
async function renderDashboard(){
  const [stats,prps]=await Promise.all([api('/api/stats'), api('/api/prps')]);
  document.getElementById('sb-count').textContent=stats.total+' PRP actifs';
  document.getElementById('nc-badge').textContent=stats.nc_actives;
  const kpct=stats.taux_conformite;
  document.getElementById('kgrid').innerHTML=`
    <div class="kcard"><div class="klbl">Taux conformité</div><div class="kval kv-${kpct>=80?'g':kpct>=60?'y':'r'}">${kpct}%</div><div class="kdelta">Objectif : 90%</div></div>
    <div class="kcard"><div class="klbl">PRP conformes</div><div class="kval kv-g">${stats.conformes}</div><div class="kdelta">sur ${stats.total}</div></div>
    <div class="kcard"><div class="klbl">Non-conformités</div><div class="kval kv-r">${stats.nc_actives}</div><div class="kdelta">Actions requises</div></div>
    <div class="kcard"><div class="klbl">Score moyen T2</div><div class="kval kv-b">${stats.score_moyen}%</div><div class="kdelta">Tous PRP confondus</div></div>`;
  const sorted=[...prps].sort((a,b)=>a.score_t2-b.score_t2);
  document.getElementById('barchart').innerHTML=sorted.map(p=>`
    <div class="bi"><div class="bar" style="height:${p.score_t2}%;background:${scColor(p.score_t2)};" title="${p.nom}: ${p.score_t2}%"></div>
    <div class="blbl">${p.nom.substring(0,7)}…</div></div>`).join('');
  drawDonut(stats.conformes, stats.en_cours, stats.non_conformes);
  document.getElementById('dash-tbody').innerHTML=prps.map(p=>`
    <tr><td><strong>${p.nom}</strong></td><td>${p.categorie}</td><td>${p.responsable}</td>
    <td><span style="font-weight:600;color:${scColor(p.score_t2)}">${p.score_t2}%</span>
    <div class="pbar"><div class="pfill" style="width:${p.score_t2}%;background:${scColor(p.score_t2)};"></div></div></td>
    <td>${badge(p.statut)}</td><td style="color:var(--muted);font-size:11px;">${p.prochain_audit||'—'}</td></tr>`).join('');
}

function drawDonut(c,e,n){
  const canvas=document.getElementById('donut'); if(!canvas)return;
  const ctx=canvas.getContext('2d');
  const total=c+e+n||1;
  const data=[{v:c,col:'#22C55E',l:'Conforme'},{v:e,col:'#F59E0B',l:'En cours'},{v:n,col:'#EF4444',l:'Non-Conforme'}];
  ctx.clearRect(0,0,110,110);
  let start=-Math.PI/2;
  data.forEach(d=>{
    const angle=(d.v/total)*2*Math.PI;
    ctx.beginPath();ctx.moveTo(55,55);ctx.arc(55,55,48,start,start+angle);
    ctx.fillStyle=d.col;ctx.fill(); start+=angle;
  });
  ctx.beginPath();ctx.arc(55,55,30,0,2*Math.PI);ctx.fillStyle='#fff';ctx.fill();
  document.getElementById('donut-leg').innerHTML=data.map(d=>`
    <div style="display:flex;align-items:center;gap:5px;margin-bottom:5px;">
      <div style="width:10px;height:10px;border-radius:2px;background:${d.col};flex-shrink:0;"></div>
      <span style="color:var(--muted);">${d.l}</span>
      <strong style="margin-left:auto;padding-left:8px;">${d.v}</strong>
    </div>`).join('');
}

// ── PRP TABLE ──
let allPRPs=[];
async function renderPRPs(){
  allPRPs=await api('/api/prps');
  renderPRPRows(allPRPs);
}
function renderPRPRows(rows){
  document.getElementById('prp-tbody').innerHTML=rows.map(p=>`
    <tr><td style="font-family:'DM Mono',monospace;font-size:11px;color:var(--muted);">PRP-${String(p.id).padStart(2,'0')}</td>
    <td><strong>${p.nom}</strong></td><td>${p.categorie}</td><td>${p.responsable}</td><td>${p.frequence}</td>
    <td style="color:${scColor(p.score_t1)};font-weight:600;">${p.score_t1}%</td>
    <td style="color:${scColor(p.score_t2)};font-weight:600;">${p.score_t2}%</td>
    <td>${badge(p.statut)}</td>
    <td style="display:flex;gap:4px;">
      <button class="btn btn-o btn-sm" onclick="editPRP(${p.id})">✏️</button>
      <button class="btn btn-danger btn-sm" onclick="delPRP(${p.id})">🗑</button>
    </td></tr>`).join('');
}
function filterTable(){
  const q=document.getElementById('search').value.toLowerCase();
  renderPRPRows(allPRPs.filter(p=>p.nom.toLowerCase().includes(q)||p.responsable.toLowerCase().includes(q)));
}
function editPRP(id){
  const p=allPRPs.find(x=>x.id===id); if(!p)return;
  document.getElementById('modal-mode-title').textContent='✏️ Modifier le PRP';
  document.getElementById('edit-id').value=id;
  document.getElementById('f-nom').value=p.nom;
  document.getElementById('f-cat').value=p.categorie;
  document.getElementById('f-resp').value=p.responsable;
  document.getElementById('f-freq').value=p.frequence;
  document.getElementById('f-t1').value=p.score_t1;
  document.getElementById('f-t2').value=p.score_t2;
  document.getElementById('f-statut').value=p.statut;
  document.getElementById('f-audit').value='';
  openModal('m-add-prp');
}
async function savePRP(){
  const id=document.getElementById('edit-id').value;
  const data={nom:document.getElementById('f-nom').value.trim(),categorie:document.getElementById('f-cat').value,
    responsable:document.getElementById('f-resp').value.trim(),frequence:document.getElementById('f-freq').value,
    score_t1:parseInt(document.getElementById('f-t1').value)||0,score_t2:parseInt(document.getElementById('f-t2').value)||0,
    statut:document.getElementById('f-statut').value,prochain_audit:document.getElementById('f-audit').value};
  if(!data.nom||!data.responsable){toast('⚠️ Remplir nom et responsable');return;}
  if(id) await api('/api/prps/'+id,'PUT',data);
  else await api('/api/prps','POST',data);
  closeModal('m-add-prp');
  document.getElementById('edit-id').value='';
  document.getElementById('modal-mode-title').textContent='➕ Nouveau PRP';
  resetForm(['f-nom','f-resp','f-audit']);
  toast('✅ PRP sauvegardé !');
  await renderPRPs(); await renderDashboard();
}
async function delPRP(id){
  if(!confirm('Supprimer ce PRP ?'))return;
  await api('/api/prps/'+id,'DELETE');
  toast('🗑 PRP supprimé'); await renderPRPs(); await renderDashboard();
}

// ── VERIFICATIONS ──
async function renderVerifs(){
  const [prps,verifs]=await Promise.all([api('/api/prps'),api('/api/verifications')]);
  const sel=document.getElementById('v-prp');
  sel.innerHTML='<option value="">-- Choisir --</option>'+prps.map(p=>`<option value="${p.id}" data-nom="${p.nom}">${p.nom}</option>`).join('');
  document.getElementById('verif-tbody').innerHTML=verifs.map(v=>`
    <tr><td style="font-size:11px;">${v.date_verif}</td><td>${v.prp_nom}</td><td>${badge(v.resultat)}</td><td>${v.verificateur}</td></tr>`).join('');
}
async function saveVerif(){
  const sel=document.getElementById('v-prp');
  const prp_nom=sel.options[sel.selectedIndex]?.dataset?.nom||'';
  const prp_id=sel.value;
  const date=document.getElementById('v-date').value;
  const resultat=document.getElementById('v-res').value;
  const verificateur=document.getElementById('v-agent').value.trim();
  const observations=document.getElementById('v-obs').value;
  if(!prp_id||!date||!resultat||!verificateur){toast('⚠️ Remplir tous les champs *');return;}
  await api('/api/verifications','POST',{prp_id:parseInt(prp_id),prp_nom,date_verif:date,resultat,verificateur,observations});
  resetForm(['v-prp','v-date','v-res','v-agent','v-obs']);
  const ok=document.getElementById('verif-ok');
  ok.style.display='flex'; setTimeout(()=>ok.style.display='none',3000);
  toast('✅ Vérification enregistrée !');
  await renderVerifs();
}

// ── NC ──
async function renderNC(){
  const [prps,ncs]=await Promise.all([api('/api/prps'),api('/api/ncs')]);
  const actives=ncs.filter(n=>n.statut_action!=='Clôturée');
  document.getElementById('nc-alert').textContent=`⚠️ ${actives.length} non-conformité${actives.length>1?'s':''} active${actives.length>1?'s':''}.`;
  document.getElementById('nc-badge').textContent=actives.length;
  const ncSel=document.getElementById('nc-prp');
  ncSel.innerHTML='<option value="">--</option>'+prps.map(p=>`<option value="${p.id}" data-nom="${p.nom}">${p.nom}</option>`).join('');
  const gravCols={Critique:['#FEE2E2','#B91C1C'],Majeure:['#FEF3C7','#92400E'],Mineure:['#DBEAFE','#1E40AF']};
  document.getElementById('nc-tbody').innerHTML=ncs.map(n=>{
    const [bg,tc]=gravCols[n.gravite]||['#F1F5F9','#64748B'];
    return `<tr><td><strong>${n.prp_nom}</strong></td><td style="font-size:11px;">${n.description}</td>
    <td><span class="tag" style="background:${bg};color:${tc};">${n.gravite}</span></td>
    <td>${n.responsable}</td><td style="color:var(--red-t);font-size:11px;">${n.echeance}</td>
    <td><div class="pbar" style="width:80px;"><div class="pfill" style="width:${n.avancement||0}%;background:${scColor(n.avancement||0)};"></div></div>
    <span style="font-size:10px;color:var(--muted);">${n.avancement||0}%</span></td>
    <td>${badge(n.statut_action)}</td></tr>`}).join('');
}
async function saveNC(){
  const sel=document.getElementById('nc-prp');
  const prp_nom=sel.options[sel.selectedIndex]?.dataset?.nom||'';
  const prp_id=sel.value;
  const desc=document.getElementById('nc-desc').value.trim();
  const gravite=document.getElementById('nc-grav').value;
  const responsable=document.getElementById('nc-resp').value.trim();
  const echeance=document.getElementById('nc-date').value;
  if(!prp_id||!desc||!gravite||!responsable||!echeance){toast('⚠️ Remplir tous les champs *');return;}
  await api('/api/ncs','POST',{prp_id:parseInt(prp_id),prp_nom,description:desc,gravite,responsable,echeance});
  resetForm(['nc-prp','nc-desc','nc-grav','nc-resp','nc-date']);
  toast('⚠️ NC enregistrée !'); await renderNC();
}

// ── CAPA ──
async function renderCAPA(){
  const [prps,capas]=await Promise.all([api('/api/prps'),api('/api/capas')]);
  const sel=document.getElementById('ca-prp');
  sel.innerHTML='<option value="">--</option>'+prps.map(p=>`<option>${p.nom}</option>`).join('');
  document.getElementById('capa-tbody').innerHTML=capas.map(c=>`
    <tr><td><strong>${c.prp_nom}</strong></td><td style="font-size:11px;">${c.action}</td>
    <td>${c.responsable}</td><td style="color:var(--red-t);font-size:11px;">${c.echeance}</td>
    <td><div class="pbar" style="width:100px;"><div class="pfill" style="width:${c.avancement}%;background:${scColor(c.avancement)};"></div></div>
    <span style="font-size:10px;color:var(--muted);">${c.avancement}%</span></td>
    <td>${badge(c.statut)}</td></tr>`).join('');
}
async function saveCAPA(){
  const prp_nom=document.getElementById('ca-prp').value;
  const action=document.getElementById('ca-action').value.trim();
  const responsable=document.getElementById('ca-resp').value.trim();
  const echeance=document.getElementById('ca-date').value;
  const avancement=parseInt(document.getElementById('ca-av').value)||0;
  if(!prp_nom||!action||!responsable||!echeance){toast('⚠️ Remplir tous les champs *');return;}
  await api('/api/capas','POST',{prp_nom,action,responsable,echeance,avancement});
  resetForm(['ca-prp','ca-action','ca-resp','ca-date']); document.getElementById('ca-av').value=0;
  toast('✅ Action CAPA enregistrée !'); await renderCAPA();
}

// ── KPI ──
async function renderKPI(){
  const [stats,prps]=await Promise.all([api('/api/stats'),api('/api/prps')]);
  const pct=stats.taux_conformite;
  document.getElementById('kgrid2').innerHTML=`
    <div class="kcard"><div class="klbl">Conformité T2</div><div class="kval kv-g">${pct}%</div><div class="kdelta">↑ +9% vs T1</div></div>
    <div class="kcard"><div class="klbl">Score moyen</div><div class="kval kv-b">${stats.score_moyen}%</div><div class="kdelta">Tous PRP</div></div>
    <div class="kcard"><div class="klbl">NC actives</div><div class="kval kv-r">${stats.nc_actives}</div><div class="kdelta">Actions en cours</div></div>
    <div class="kcard"><div class="klbl">Objectif</div><div class="kval kv-b">90%</div><div class="kdelta">-${90-pct}pts à combler</div></div>`;
  const months=[['Déc 25',48],['Jan 26',52],['Fév 26',55],['Mar 26',58],['Avr 26',62],['Mai 26',pct]];
  document.getElementById('trend').innerHTML=months.map(([m,v])=>`
    <div style="display:flex;align-items:center;gap:8px;">
      <span style="font-size:11px;color:var(--muted);min-width:45px;">${m}</span>
      <div style="flex:1;height:18px;background:var(--border);border-radius:3px;overflow:hidden;">
        <div style="width:${v}%;height:100%;background:${scColor(v)};border-radius:3px;display:flex;align-items:center;padding-left:6px;">
          <span style="font-size:10px;color:#fff;font-weight:600;">${v}%</span>
        </div>
      </div></div>`).join('');
  document.getElementById('kpi-bars').innerHTML=prps.map(p=>`
    <div style="display:flex;align-items:center;gap:6px;font-size:11px;">
      <span style="min-width:90px;color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">${p.nom.substring(0,12)}…</span>
      <div style="flex:1;height:12px;background:var(--border);border-radius:3px;overflow:hidden;">
        <div style="width:${p.score_t2}%;height:100%;background:${scColor(p.score_t2)};border-radius:3px;"></div>
      </div>
      <span style="font-weight:600;color:${scColor(p.score_t2)};min-width:28px;text-align:right;">${p.score_t2}%</span>
    </div>`).join('');
}

// ── PLANNING ──
async function renderPlanning(){
  const prps=await api('/api/prps');
  document.getElementById('plan-tbody').innerHTML=prps.map(p=>`
    <tr><td><strong>${p.nom}</strong></td><td>${p.frequence}</td>
    <td style="font-size:11px;">${p.prochain_audit||'—'}</td>
    <td>${p.responsable}</td>
    <td><span class="badge b-ok">📅 Planifié</span></td></tr>`).join('');
}

// ── RAPPORT ──
async function renderRapport(){
  const [stats,prps,ncs]=await Promise.all([api('/api/stats'),api('/api/prps'),api('/api/ncs')]);
  document.getElementById('rpt-date').textContent='Date : '+new Date().toLocaleDateString('fr-FR',{day:'numeric',month:'long',year:'numeric'});
  document.getElementById('rpt-kpi').innerHTML=`
    <div class="kcard"><div class="klbl">PRP actifs</div><div class="kval kv-b">${stats.total}</div></div>
    <div class="kcard"><div class="klbl">Conformité</div><div class="kval kv-g">${stats.taux_conformite}%</div></div>
    <div class="kcard"><div class="klbl">NC ouvertes</div><div class="kval kv-r">${stats.nc_actives}</div></div>
    <div class="kcard"><div class="klbl">Vérifications</div><div class="kval kv-b">${stats.total_verifications}</div></div>`;
  document.getElementById('rpt-tbody').innerHTML=prps.map(p=>{
    const evo=p.score_t2-p.score_t1;
    return `<tr><td><strong>${p.nom}</strong></td><td>${p.responsable}</td>
    <td style="color:${scColor(p.score_t1)};font-weight:600;">${p.score_t1}%</td>
    <td style="color:${scColor(p.score_t2)};font-weight:600;">${p.score_t2}%</td>
    <td style="color:${evo>=0?'#15803D':'#B91C1C'};font-weight:600;">${evo>=0?'+':''}${evo}%</td>
    <td>${badge(p.statut)}</td></tr>`}).join('');
  const gravC={Critique:['#FEE2E2','#B91C1C'],Majeure:['#FEF3C7','#92400E'],Mineure:['#DBEAFE','#1E40AF']};
  document.getElementById('rpt-nc').innerHTML=ncs.map(n=>{
    const [bg,tc]=gravC[n.gravite]||['#F1F5F9','#64748B'];
    return `<tr><td>${n.prp_nom}</td><td style="font-size:11px;">${n.description}</td>
    <td><span class="tag" style="background:${bg};color:${tc};">${n.gravite}</span></td>
    <td>${n.responsable}</td><td style="font-size:11px;color:var(--red-t);">${n.echeance}</td></tr>`}).join('');
  const forts=prps.filter(p=>p.statut==='Conforme').map(p=>p.nom).join(', ');
  const faibles=prps.filter(p=>p.statut==='Non-Conforme').map(p=>p.nom).join(', ');
  document.getElementById('rpt-conclu').innerHTML=`
    <p><strong>✅ Points forts :</strong> ${forts||'Aucun'}</p><br>
    <p><strong>⚠️ Points à améliorer :</strong> ${faibles||'Aucun'}</p><br>
    <p><strong>🎯 Objectif :</strong> Atteindre 90% de conformité d'ici fin 2026.</p><br>
    <p><strong>📌 Recommandations :</strong> Renforcer la surveillance des PRP en écart et accélérer le plan de formation du personnel.</p>`;
}

// ── EXPORT CSV ──
async function exportCSV(){
  const prps=await api('/api/prps');
  const h=['ID','Nom','Categorie','Responsable','Frequence','Score_T1','Score_T2','Statut','Prochain_Audit'];
  const rows=prps.map(p=>[p.id,p.nom,p.categorie,p.responsable,p.frequence,p.score_t1,p.score_t2,p.statut,p.prochain_audit]);
  const csv=[h,...rows].map(r=>r.join(';')).join('\n');
  const a=document.createElement('a');
  a.href='data:text/csv;charset=utf-8,\uFEFF'+encodeURIComponent(csv);
  a.download='PRP_MMCI_'+new Date().toISOString().slice(0,10)+'.csv';
  a.click(); toast('⬇ Export CSV en cours…');
}

// ── INIT ──
renderDashboard();
</script>
</body>
</html>
