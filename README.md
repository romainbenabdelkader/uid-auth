📘 UID_AUTH 
Universal Identity for Creative Works

Standard ouvert, souverain, compatible AI Act & RGPD


Version 1.0 — Novembre 2025



🔹 1. Introduction

UID_AUTH est l’identifiant universel souverain développé par AUTHENTICA, conçu pour fournir :

	•	une identité unique,

	•	non ambiguë,

	•	horodatée,

	•	vérifiable,

	•	indépendante des métadonnées,

	•	conforme au RGPD et à l’AI Act.

UID_AUTH donne à chaque œuvre (audio, image, vidéo, texte) une identité native, lisible par les systèmes juridiques, culturels et techniques.

⸻

🔹 2. Structure d’un UID_AUTH

Format général :

CC-YYYY-AUTH-XXXXX

Exemple :

FR-2025-AUTH-000001

🔹 3. Spécification JSON

Le schéma complet est disponible ici :

➡️ /schema/uid_auth_schema.json

Exemple d’UID_AUTH :

  "uid_auth": "FR-2025-AUTH-000001",
  
  "issued_at": "2025-11-11T00:40:07Z",
  
  "issuer": "AUTHENTICA",
  
  "hash": 
    "algorithm": "sha256",
	
    "value": "EXAMPLE-UID-AUTH-000001"

🔹 4. Manifeste TRINITY Light (JSON-LD)

Le manifeste associé (machine-readable, compatible IA et DDEX) se trouve dans :

➡️ /examples/manifest_example.jsonld

Exemple :

  "@type": "CreativeWork",
  
  "uid_auth": "FR-2025-AUTH-000001",
  
  "origin": "human",
  
  "rights": 
    "ai_training": "prohibited",
    "tdm_opt_out": true
	
  
  "hash": 
    "algorithm": "sha256",
    "value": "EXAMPLE-HASH"
	


🔹 5. Compatibilité & Objectifs

UID_AUTH est çoncu pour s'integrer naturellemnt avec :

✔ SACEM / ADAMI / SPEDIADAM / SCPP / SPPF / SCAM / SGDL/ SACD /PRS / GEMA /SIAE ETC...

✔ AI Act (transparence + traçabilité IA)

✔ RGPD (aucune donnée personnelle)

✔ Systèmes de gestion collective

✔ Formats culturels (audio, vidéo, texte, image)

✔ Standards JSON-LD / DDEX / W3C

⸻

🔹 6. Licence

Ce standard est publié sous licence Apache 2.0, permettant :

	•	usage libre

	•	implémentations commerciales

	•	interopérabilité ouverte

⸻

✨ UID_AUTH est un standard souverain ouvert, conçu pour protéger la création humaine et assurer la traçabilité culturelle à l’ère de l’IA.






UID_AUTH est une brique technique de conformité,

mais ne garantit pas la conformité RGPD ou AI Act à lui seul.

Il doit être intégré dans un système conforme.
