"""
Gestion de la base de données SQLite
"""
import sqlite3

SCHEMA = '''
CREATE TABLE IF NOT EXISTS prps (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    nom             TEXT NOT NULL,
    categorie       TEXT DEFAULT 'Hygiène',
    responsable     TEXT NOT NULL,
    frequence       TEXT DEFAULT 'Mensuel',
    score_t1        INTEGER DEFAULT 0,
    score_t2        INTEGER DEFAULT 0,
    statut          TEXT DEFAULT 'Non évalué',
    prochain_audit  TEXT DEFAULT ''
);

CREATE TABLE IF NOT EXISTS verifications (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    prp_id          INTEGER,
    prp_nom         TEXT,
    date_verif      TEXT,
    resultat        TEXT,
    verificateur    TEXT,
    observations    TEXT DEFAULT '',
    FOREIGN KEY(prp_id) REFERENCES prps(id)
);

CREATE TABLE IF NOT EXISTS non_conformites (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    prp_id          INTEGER,
    prp_nom         TEXT,
    description     TEXT,
    gravite         TEXT DEFAULT 'Mineure',
    responsable     TEXT,
    echeance        TEXT,
    statut_action   TEXT DEFAULT 'En cours',
    avancement      INTEGER DEFAULT 0,
    FOREIGN KEY(prp_id) REFERENCES prps(id)
);

CREATE TABLE IF NOT EXISTS actions_capa (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    prp_nom     TEXT,
    action      TEXT,
    responsable TEXT,
    echeance    TEXT,
    avancement  INTEGER DEFAULT 0,
    statut      TEXT DEFAULT 'En cours'
);
'''

SEED_PRPS = [
    ('Nettoyage & Désinfection', 'Hygiène', 'M. Koné', 'Mensuel', 80, 92, 'Conforme', '15/06/2026'),
    ('Lutte contre les nuisibles', 'Hygiène', 'Mme Diabaté', 'Mensuel', 78, 88, 'Conforme', '20/06/2026'),
    ('Hygiène du personnel', 'Hygiène', 'M. Touré', 'Hebdomadaire', 38, 45, 'Non-Conforme', '30/05/2026'),
    ('Qualité de l\'eau', 'Qualité', 'Mme Coulibaly', 'Trimestriel', 90, 95, 'Conforme', '01/07/2026'),
    ('Gestion des déchets', 'Environnement', 'M. Bamba', 'Mensuel', 70, 78, 'Conforme', '10/06/2026'),
    ('Maintenance préventive', 'Infrastructure', 'M. Sylla', 'Mensuel', 32, 40, 'Non-Conforme', '28/05/2026'),
    ('Formation du personnel', 'RH', 'Mme Traoré', 'Semestriel', 55, 70, 'En cours', '05/06/2026'),
    ('Maîtrise des allergènes', 'Qualité', 'M. Diallo', 'Mensuel', 78, 85, 'Conforme', '15/06/2026'),
    ('Traçabilité & rappel', 'Qualité', 'M. Konaté', 'Mensuel', 85, 90, 'Conforme', '01/07/2026'),
]

SEED_NCS = [
    (3, 'Hygiène du personnel', 'Non-respect des EPI sur 3 agents', 'Critique', 'M. Touré', '10/06/2026', 'En cours', 30),
    (6, 'Maintenance préventive', '4 équipements sans révision depuis 6 mois', 'Majeure', 'M. Sylla', '05/06/2026', 'En cours', 15),
    (7, 'Formation du personnel', '30% du personnel non formé T2', 'Mineure', 'Mme Traoré', '05/06/2026', 'En cours', 40),
]

SEED_CAPAS = [
    ('Hygiène du personnel', 'Formation obligatoire + contrôle quotidien EPI', 'M. Touré', '10/06/2026', 30, 'En cours'),
    ('Maintenance préventive', 'Révision 4 équipements + mise à jour planning', 'M. Sylla', '05/06/2026', 15, 'En cours'),
    ('Formation du personnel', 'Planifier sessions formation mai-juin 2026', 'Mme Traoré', '05/06/2026', 40, 'En cours'),
]

SEED_VERIFS = [
    (1, 'Nettoyage & Désinfection', '2026-05-02', 'Conforme', 'M. Koné', 'RAS'),
    (3, 'Hygiène du personnel', '2026-04-28', 'Non-Conforme', 'M. Touré', '3 agents sans EPI'),
    (4, 'Qualité de l\'eau', '2026-05-01', 'Conforme', 'Mme Coulibaly', 'Analyses microbiologiques OK'),
]


def get_db(app):
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def init_db(app):
    conn = get_db(app)
    conn.executescript(SCHEMA)
    conn.commit()
    conn.close()


def seed_db(app):
    conn = get_db(app)
    count = conn.execute('SELECT COUNT(*) FROM prps').fetchone()[0]
    if count == 0:
        conn.executemany(
            'INSERT INTO prps (nom,categorie,responsable,frequence,score_t1,score_t2,statut,prochain_audit) VALUES (?,?,?,?,?,?,?,?)',
            SEED_PRPS)
        conn.executemany(
            'INSERT INTO non_conformites (prp_id,prp_nom,description,gravite,responsable,echeance,statut_action,avancement) VALUES (?,?,?,?,?,?,?,?)',
            SEED_NCS)
        conn.executemany(
            'INSERT INTO actions_capa (prp_nom,action,responsable,echeance,avancement,statut) VALUES (?,?,?,?,?,?)',
            SEED_CAPAS)
        conn.executemany(
            'INSERT INTO verifications (prp_id,prp_nom,date_verif,resultat,verificateur,observations) VALUES (?,?,?,?,?,?)',
            SEED_VERIFS)
        conn.commit()
    conn.close()
