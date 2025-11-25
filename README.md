UID_AUTH Universal Identity for Creative Works

Standard ouvert de preuve d’origine et de traçabilité des œuvres (v1.0)

UID_AUTH est un identifiant souverain, vérifiable et interopérable conçu pour fournir une preuve d’origine, une intégrité cryptographique et une traçabilité fiable des œuvres créatives à l’ère de l’IA.

Ce protocole peut être utilisé par :

•	les sociétés de gestion collective (SACEM, SOCAN, PRS, GEMA, ASCAP…)

•	les institutions culturelles

•	les DSP (Spotify, Apple Music, YouTube…)

•	les plateformes IA

•	les éditeurs et producteurs

•	les créateurs individuels

UID_AUTH est un standard ouvert, neutre, sans dépendance commerciale, conçu pour être intégré dans tout écosystème


1. Objectifs du standard

UID_AUTH fournit trois garanties essentielles :

Preuve d’origine

Un identifiant unique, horodaté et vérifiable, associé à une œuvre

Intégrité cryptographique

Un hash indépendant, permettant de vérifier qu’une œuvre n’a pas été modifiée.

Transparence AI Act

Un manifeste JSON-LD indiquant les conditions d’usage, notamment pour l’entraînement IA et le TDM opt-out.


2. Structure du protocole UID_AUTH

Le format est le suivant :

AUTH.TIMESTAMP.ALGO.VERSION.RANDOM.CHECKSUM

Détail des segments

Segment	Description
AUTH	Préfixe du standard
TIMESTAMP	Horodatage ISO 8601 (UTC)
ALGO	Algorithme cryptographique (sha3-256)
VERSION	Version du protocole UID_AUTH (v1)
RANDOM	Aléa Base58 (8+ caractères)
CHECKSUM	Contrôle d’intégrité (6+ caractères Base58)

Exemple

AUTH.2025-11-11T00:40:07Z.sha3-256.v1.89fT1kZa.Qp9eD4

3. Exemple complet (UID_AUTH)

{
  "uid_auth": "AUTH.2025-11-11T00:40:07Z.sha3-256.v1.89fT1kZa.Qp9eD4",
  "spec_version": "1.0",
  "media_type": "audio/wav",
  "hash": {
    "algorithm": "sha256",
    "value": "EXAMPLE-AUDIO-HASH"
  },
  "issued_at": "2025-11-11T00:40:07Z",
  "issuer": {
    "name": "AUTHENTICA",
    "type": "IdentityAuthority"
  }
}

4. Manifeste JSON-LD (AI Act-ready)

Chaque œuvre peut être accompagnée d’un manifeste conforme au vocabulaire JSON-LD

Exemple (audio)

{
  "@context": "https://raw.githubusercontent.com/romainbenabdelkader/authentica-ai-rights/main/schema/ai_rights_context.json",
  "@type": "CreativeWork",

  "uid_auth": "FR-2025-AUTH-MUS-000001",
  "spec_version": "1.0",
  "media_type": "audio/wav",

  "name": "Example Audio Work",
  "creator": "Anonymous",
  "origin": "human",

  "rights": {
    "ai_training_prohibited": true,
    "tdm_opt_out": true,
    "derivative_generation_prohibited": true
  },

  "provenance": {
    "generated_by": "AUTHENTICA",
    "generation_timestamp": "2025-01-12T14:21:53Z"
  }
}

5. Interopérabilité

UID_AUTH est conçu pour coexister avec les identifiants existants :

	•	ISRC (enregistrements)

	•	ISWC (œuvres)

	•	UPC/EAN

	•	DDEX

	•	EIDR (audiovisuel)

Le standard n’entre pas en concurrence :

il fournit la couche de preuve d’origine qui manque à tous ces systèmes


6. Gouvernance du standard

UID_AUTH est un standard évolutif, maintenu sous gouvernance institutionnelle :

•	évolutions basées sur un processus de RFC (Request for Comments)

•	consultation des OGC, DSP et institutions culturelles

•	comité technique multi-acteurs

•	compatibilité ascendante garantie


7. Conformité réglementaire

RGPD

•	aucune donnée personnelle nécessaire

•	traitement anonymisé

•	vérification hors-ligne possible


AI Act

Le manifeste AI Rights fournit les informations exigées :
	
•	origine humaine / générée

•	conditions d’usage

•	TDM opt-out

•	transparence machine readable

8. Arborescence du repos

uid-auth/
│
├── README.md
├── LICENSE
│
├── context/
│   └── context.jsonld
│
├── schema/
│   └── uid_auth_schema.json
│
├── examples/
│   ├── uid_auth_example.json
│   ├── manifest_example.jsonld
│   └── manifest_us_example.jsonld
│
└── version.txt

9. Statut du standard

Statut	Description

🟢 Stable	UID_AUTH v1.0 publié

🟡 Implémentation	librairies de référence en cours

🔵 Pilotes institutionnels	OGC & institutions culturelles

10. Licence

Ce standard est publié sous licence Apache 2.0, permettant :

•	usage libre

•	implémentation libre 
(commerciale ou publique)

•	contributions ouvertes


11. Contact

Pour toute question institutionnelle ou collaboration :
romain@lockdna.tech