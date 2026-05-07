"""
PRP Manager — MMCI
Backend Flask + SQLite
"""
from flask import Flask, jsonify, request, render_template, abort
from database import init_db, get_db, seed_db
import sqlite3, os

app = Flask(__name__)
app.config['DATABASE'] = os.path.join(app.root_path, 'mmci_prp.db')

# ── Init DB au démarrage ──
with app.app_context():
    init_db(app)
    seed_db(app)

# ─────────────────────────────────────────
# PAGE PRINCIPALE
# ─────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')

# ─────────────────────────────────────────
# API PRP
# ─────────────────────────────────────────
@app.route('/api/prps', methods=['GET'])
def get_prps():
    db = get_db(app)
    prps = db.execute('SELECT * FROM prps ORDER BY id').fetchall()
    return jsonify([dict(p) for p in prps])

@app.route('/api/prps', methods=['POST'])
def add_prp():
    data = request.get_json()
    required = ['nom', 'categorie', 'responsable']
    if not all(k in data for k in required):
        abort(400, 'Champs manquants')
    db = get_db(app)
    db.execute('''INSERT INTO prps (nom, categorie, responsable, frequence, score_t1, score_t2, statut, prochain_audit)
                  VALUES (?,?,?,?,?,?,?,?)''',
        (data['nom'], data['categorie'], data['responsable'],
         data.get('frequence','Mensuel'),
         data.get('score_t1', 0), data.get('score_t2', 0),
         data.get('statut','Non évalué'),
         data.get('prochain_audit','')))
    db.commit()
    return jsonify({'message': 'PRP ajouté'}), 201

@app.route('/api/prps/<int:prp_id>', methods=['PUT'])
def update_prp(prp_id):
    data = request.get_json()
    db = get_db(app)
    db.execute('''UPDATE prps SET nom=?, categorie=?, responsable=?, frequence=?,
                  score_t1=?, score_t2=?, statut=?, prochain_audit=? WHERE id=?''',
        (data['nom'], data['categorie'], data['responsable'], data['frequence'],
         data['score_t1'], data['score_t2'], data['statut'], data['prochain_audit'], prp_id))
    db.commit()
    return jsonify({'message': 'PRP mis à jour'})

@app.route('/api/prps/<int:prp_id>', methods=['DELETE'])
def delete_prp(prp_id):
    db = get_db(app)
    db.execute('DELETE FROM prps WHERE id=?', (prp_id,))
    db.commit()
    return jsonify({'message': 'PRP supprimé'})

# ─────────────────────────────────────────
# API VÉRIFICATIONS
# ─────────────────────────────────────────
@app.route('/api/verifications', methods=['GET'])
def get_verifications():
    db = get_db(app)
    rows = db.execute('SELECT * FROM verifications ORDER BY date_verif DESC').fetchall()
    return jsonify([dict(r) for r in rows])

@app.route('/api/verifications', methods=['POST'])
def add_verification():
    data = request.get_json()
    db = get_db(app)
    db.execute('''INSERT INTO verifications (prp_id, prp_nom, date_verif, resultat, verificateur, observations)
                  VALUES (?,?,?,?,?,?)''',
        (data.get('prp_id'), data['prp_nom'], data['date_verif'],
         data['resultat'], data['verificateur'], data.get('observations','')))
    # Mettre à jour le statut du PRP
    db.execute('UPDATE prps SET statut=? WHERE id=?', (data['resultat'], data.get('prp_id')))
    db.commit()
    return jsonify({'message': 'Vérification enregistrée'}), 201

# ─────────────────────────────────────────
# API NON-CONFORMITÉS
# ─────────────────────────────────────────
@app.route('/api/ncs', methods=['GET'])
def get_ncs():
    db = get_db(app)
    rows = db.execute('SELECT * FROM non_conformites ORDER BY id DESC').fetchall()
    return jsonify([dict(r) for r in rows])

@app.route('/api/ncs', methods=['POST'])
def add_nc():
    data = request.get_json()
    db = get_db(app)
    db.execute('''INSERT INTO non_conformites (prp_id, prp_nom, description, gravite, responsable, echeance, statut_action)
                  VALUES (?,?,?,?,?,?,?)''',
        (data.get('prp_id'), data['prp_nom'], data['description'],
         data['gravite'], data['responsable'], data['echeance'], 'En cours'))
    db.execute('UPDATE prps SET statut="Non-Conforme" WHERE id=?', (data.get('prp_id'),))
    db.commit()
    return jsonify({'message': 'NC enregistrée'}), 201

@app.route('/api/ncs/<int:nc_id>', methods=['PUT'])
def update_nc(nc_id):
    data = request.get_json()
    db = get_db(app)
    db.execute('UPDATE non_conformites SET statut_action=?, avancement=? WHERE id=?',
               (data.get('statut_action','En cours'), data.get('avancement',0), nc_id))
    db.commit()
    return jsonify({'message': 'NC mise à jour'})

# ─────────────────────────────────────────
# API ACTIONS CAPA
# ─────────────────────────────────────────
@app.route('/api/capas', methods=['GET'])
def get_capas():
    db = get_db(app)
    rows = db.execute('SELECT * FROM actions_capa ORDER BY id').fetchall()
    return jsonify([dict(r) for r in rows])

@app.route('/api/capas', methods=['POST'])
def add_capa():
    data = request.get_json()
    db = get_db(app)
    db.execute('''INSERT INTO actions_capa (prp_nom, action, responsable, echeance, avancement, statut)
                  VALUES (?,?,?,?,?,?)''',
        (data['prp_nom'], data['action'], data['responsable'],
         data['echeance'], data.get('avancement',0), 'En cours'))
    db.commit()
    return jsonify({'message': 'CAPA ajoutée'}), 201

@app.route('/api/capas/<int:capa_id>', methods=['PUT'])
def update_capa(capa_id):
    data = request.get_json()
    db = get_db(app)
    db.execute('UPDATE actions_capa SET avancement=?, statut=? WHERE id=?',
               (data.get('avancement',0), data.get('statut','En cours'), capa_id))
    db.commit()
    return jsonify({'message': 'CAPA mise à jour'})

# ─────────────────────────────────────────
# API STATISTIQUES (pour dashboard + rapport)
# ─────────────────────────────────────────
@app.route('/api/stats', methods=['GET'])
def get_stats():
    db = get_db(app)
    prps = db.execute('SELECT * FROM prps').fetchall()
    total = len(prps)
    conf  = sum(1 for p in prps if p['statut'] == 'Conforme')
    nc    = sum(1 for p in prps if p['statut'] == 'Non-Conforme')
    ec    = sum(1 for p in prps if p['statut'] == 'En cours')
    pct   = round(conf/total*100) if total else 0
    avg   = round(sum(p['score_t2'] for p in prps)/total) if total else 0
    nc_count = db.execute('SELECT COUNT(*) FROM non_conformites WHERE statut_action != "Clôturée"').fetchone()[0]
    verif_count = db.execute('SELECT COUNT(*) FROM verifications').fetchone()[0]
    return jsonify({
        'total': total, 'conformes': conf, 'non_conformes': nc,
        'en_cours': ec, 'taux_conformite': pct, 'score_moyen': avg,
        'nc_actives': nc_count, 'total_verifications': verif_count
    })

# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
