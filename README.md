UID_AUTH Open AI-Origin & Rights Manifest (JSON-LD Standard)

Version 1.0  Open, Neutral, Interoperable

UID_AUTH est un standard ouvert pour déclarer l’origine, les droits et les restrictions d’usage d’une œuvre (audio, vidéo, image, 

texte) à l’ère de l’IA générative.

Il fournit un manifest JSON-LD, lisible par les humains, les IA, les DSPs (Spotify/YouTube/Deezer) et les sociétés de gestion 

collective (SACEM, STIM, GEMA, PRS, etc.).


Ce manifest permet :

	•	de déclarer l’origine humaine,
	
	•	de signaler les restrictions IA (AI Act),
	
	•	d’associer un identifiant souverain (UID_AUTH),
	
	•	de fournir une preuve d’intégrité (hash),
	
	•	d’assurer l’interopérabilité avec les workflows existants (DDEX, ISWC, ISRC, etc.).

Le standard est entièrement ouvert, gratuit, neutre toute organisation peut l’adopter dès maintenant.

AUTHENTICA propose une implémentation de référence, mais le standard fonctionne indépendamment de toute technologie propriétaire.


🎯 Objectifs
	1.	Fournir un format universel pour déclarer l’origine des œuvres.
	
	2.	Être AI Act Ready (articles 52, 53, 54 — transparence et TDM opt-out).
	
	3.	Rendre les œuvres lisibles par les IA, les plateformes et les institutions.
	
	4.	Offrir un socle neutre que les sociétés de gestion collective peuvent intégrer immédiatement.
	
	5.	Permettre une interopérabilité mondiale sans dépendance à une infrastructure unique.

📦 Structure du Manifest

Chaque fichier JSON-LD doit suivre cette structure : 
{
 "@context": "https://raw.githubusercontent.com/romainbenabdelkader/uid-auth/main/context/context.jsonld
 
  "@type": "CreativeWork",

  "uid_auth": "FR-2025-AUTH-000001",
  "name": "Example Work",
  "creator": "Anonymous",
  "origin": "human",

  "issued_at": "2025-11-11T00:40:07Z",
  "issuer": {
    "name": "AUTHENTICA",
    "type": "IdentityAuthority"
  },

  "rights": {
    "ai_training": "prohibited",
    "tdm_opt_out": true
  },

  "hash": {
    "algorithm": "sha256",
    "value": "EXAMPLE-HASH"
  }
}

🔒 Champs Obligatoires

Champ	Description

uid_auth	Identifiant souverain unique de l’œuvre

origin	“human” ou “ai”

issued_at	Date ISO 8601

hash	Preuve d’intégrité du fichier

rights.ai_training	Indique si l’œuvre peut être utilisée pour entraîner une IA

rights.tdm_opt_out	Conformité TDM Directive EU


✨ Extensions Optionnelles (v1.1)

Pour les institutions ou workflows avancés :

	•	provenance_chain (transformations successives)
	
	•	signature (future cryptographic signing)`

	•	work_code (ISWC, ISRC, UPC)
	
	•	rightsSociety (SACEM, STIM, PRS…)
	
	•	creator_id (pseudonymisé)

Ces champs ne sont pas obligatoires mais déjà prévus pour l’AI Act long terme.


📁 Dossiers du Référentiel

uid-auth/
├── README.md                 # Ce document
├── context.jsonld            # @context officiel du standard
├── schema.json               # JSON Schema (validation automatique)
├── examples/
│   └── manifest_example.jsonld
└── LICENSE                   # Licence open source (MIT ou CC0)


🧪 Exemple de Manifest Complet

Voir

👉 examples/manifest_example.jsonld


🏛️ Interopérabilité et Adoptions Cibles

UID_AUTH est conçu pour s’intégrer dans :

Collecting Societies

	•	SACEM
	
	•	STIM
	
	•	GEMA
	
	•	PRS
	
	•	SIAE


DSPs
	•	Spotify
	
	•	YouTube
	
	•	TikTok
	
	•	Deezer


AI Providers
	•	OpenAI
	
	•	Google
	
	•	Anthropic
	
	•	Stability


Labels & Éditeurs

	•	Universal
	
	•	Warner
	
	•	Sony
	
	•	Believe

Ces acteurs sont mentionnés uniquement à titre d’exemple d’intégration potentielle.  
Aucun partenariat ou adoption n’est annoncé à ce stade.

🌍 Pourquoi JSON-LD ?

Le JSON-LD :
	•	est déjà utilisé par Google & Schema.org,
	
	•	est compatible IA Act,
	
	•	permet une validation automatique,
	
	•	crée une base pour un futur standard W3C.

UID_AUTH s’inscrit donc dans une logique web-native.


🤝 Licence & Contribution
	•	Le standard est publié sous licence MIT (open, permissive).
	
	•	Les contributions sont les bienvenues.
	
	•	Les organisations peuvent proposer extensions, champs, versions…
	

📬 Contact

Pour rejoindre le groupe de travail, ou proposer une adoption institutionnelle :

romain@lockdna.tech
