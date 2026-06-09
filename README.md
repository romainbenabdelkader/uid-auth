# UID_AUTH

Standard ouvert d'identification, de preuve d'origine et de tracabilite des oeuvres creatives.

UID_AUTH definit un identifiant souverain, verifiable et interoperable pour les oeuvres creatives. Il fournit une couche minimale permettant de relier une oeuvre a une declaration d'origine, un horodatage, un hash d'integrite et des signaux lisibles par machine.

> UID_AUTH identifie et structure une declaration. Il ne decide pas la propriete juridique, la contrefacon ou la responsabilite.

## Objectif

UID_AUTH fournit trois garanties techniques:

- preuve d'origine declarative
- integrite cryptographique via hash `sha256`
- signaux de transparence pour l'IA et le TDM opt-out

Le standard peut etre utilise par:

- societes de gestion collective
- institutions culturelles
- DSP et plateformes de distribution
- plateformes IA
- editeurs, producteurs et labels
- createurs independants

## Format Officiel

Format UID_AUTH v1.0:

```text
COUNTRY-YEAR-AUTH-CATEGORY-SEQUENCE
```

Exemple:

```text
FR-2025-AUTH-MUS-000001
```

Segments:

| Segment | Description |
| --- | --- |
| `COUNTRY` | Code pays ISO alpha-2, ex. `FR`, `US`, `CA` |
| `YEAR` | Annee de declaration |
| `AUTH` | Prefixe fixe du standard |
| `CATEGORY` | Categorie creative, ex. `MUS`, `VID`, `IMG`, `TXT` |
| `SEQUENCE` | Sequence numerique a 6 chiffres |

UID_AUTH ne remplace pas ISRC, ISWC, UPC, EAN, DDEX ou EIDR. Il ajoute une couche d'identification, d'origine et d'integrite.

## Manifeste JSON

Exemple minimal:

```json
{
  "uid_auth": "FR-2025-AUTH-MUS-000001",
  "spec_version": "1.0",
  "issued_at": "2025-11-11T10:30:00Z",
  "media_type": "audio/wav",
  "name": "Example Audio Work",
  "creator": "Anonymous",
  "origin": "human",
  "rights": {
    "ai_training": "prohibited",
    "tdm_opt_out": true,
    "jurisdiction": "EU"
  },
  "hash": {
    "algorithm": "sha256",
    "value": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  },
  "issuer": {
    "name": "AUTHENTICA",
    "type": "IdentityAuthority"
  }
}
```

Fichier de reference:

```text
examples/uid_auth_example.json
```

## Manifeste JSON-LD

Un manifeste JSON-LD peut ajouter un contexte machine-readable pour les droits IA et TDM.

Fichier de reference:

```text
examples/manifest_example.jsonld
```

Contexte JSON-LD:

```text
context/schema/ai-rights-context.jsonld
```

## Schema

Le schema JSON officiel est disponible ici:

```text
schema/uid_auth_schema.json
```

Il verifie notamment:

- le format `uid_auth`
- l'origine declaree: `human`, `ai`, `hybrid`
- l'horodatage ISO 8601
- l'autorite emettrice
- les droits IA/TDM
- le hash `sha256`

## Validation Locale

Une validation minimale des exemples est fournie:

```bash
python scripts/validate_examples.py
```

ou:

```bash
python3 scripts/validate_examples.py
```

Lorsque la bibliotheque optionnelle `jsonschema` est installee (`pip install jsonschema`), les exemples sont valides directement contre `schema/uid_auth_schema.json`, qui fait foi. Sinon, un controle equivalent en pure bibliotheque standard est utilise. Cette validation sert a verifier que les exemples du depot restent coherents avec le format UID_AUTH v1.0.

## Interoperabilite

UID_AUTH coexiste avec les identifiants existants:

- ISRC
- ISWC
- UPC / EAN
- DDEX
- EIDR

Il complete ces standards avec:

- un identifiant d'origine
- une preuve d'integrite
- des signaux de transparence IA/TDM

## Architecture

Les roles sont separes:

- AURA fournit une preuve technique neutre d'origine, d'integrite et de verification. AURA peut verifier un manifeste, un hash ou une signature, sans imposer de registre, d'identifiant ou de profil de droits.
- UID_AUTH fournit l'identifiant souverain de l'oeuvre ou de l'actif. C'est le role de ce depot: definir le format, le schema et les exemples de l'identifiant.
- AUTHENTICA fournit un profil de droits et de reserve IA/TDM. Un manifeste AUTHENTICA peut contenir un `uid_auth` et peut etre reference ou verifie par AURA, mais il reste un profil applicatif distinct.

UID_AUTH peut donc etre utilise dans un manifeste AURA ou AUTHENTICA, sans dependance obligatoire entre les trois couches.

Exemple de combinaison:

```json
{
  "uid_auth": "FR-2025-AUTH-MUS-000001",
  "aura_id": "AURA-LOCAL-2026-000001-TEST",
  "asset_hash": "..."
}
```

Dans ce modele:

- `uid_auth` identifie l'oeuvre
- `aura_id` identifie la preuve AURA
- `asset_hash` verifie l'integrite du fichier
- la signature AURA verifie l'integrite du manifeste

## Ce Que UID_AUTH Ne Fait Pas

UID_AUTH ne fournit pas:

- preuve juridique absolue de propriete
- decision automatique de contrefacon
- surveillance d'usage
- sanction automatique
- DRM
- watermarking
- reconnaissance de contenu

UID_AUTH fournit un artefact technique verifiable. La qualification juridique releve du droit, d'un audit, d'un regulateur ou d'une juridiction competente.

## Arborescence

```text
uid-auth/
├── README.md
├── README_EN.md
├── README.US.md
├── LICENSE
├── CHANGELOG.md
├── version.txt
├── schema/
│   └── uid_auth_schema.json
├── context/
│   ├── context.jsonld
│   └── schema/
│       └── ai-rights-context.jsonld
├── examples/
│   ├── uid_auth_example.json
│   ├── manifest_example.jsonld
│   └── manifest_us_example.jsonld
└── scripts/
    └── validate_examples.py
```

## Statut

UID_AUTH v1.0 est publie comme standard ouvert minimal. Les implementations de reference peuvent evoluer separement.

## Licence

Apache License 2.0
