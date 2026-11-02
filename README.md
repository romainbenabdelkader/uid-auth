# UID_AUTH

Format ouvert d'identification et de declarations sur les oeuvres creatives.

UID_AUTH definit un format d'identifiant accompagne de metadonnees : origine
declaree, date declaree, empreinte et signaux de droits lisibles par machine.
Le schema verifie leur structure ; l'identifiant seul ne certifie ni l'origine,
ni l'identite du declarant, ni l'integrite d'un fichier.

[English documentation](README_EN.md) · [U.S. profile](README.US.md)

> UID_AUTH identifie et structure une declaration. Il ne decide pas la propriete juridique, la contrefacon ou la responsabilite.

## Objectif

UID_AUTH structure trois types d'informations:

- declaration d'origine
- empreinte declaree `sha256`, a comparer separement aux octets du fichier
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

UID_AUTH ne remplace pas les identifiants ISRC, ISWC, UPC, EAN ou EIDR, ni les
formats d'echange DDEX. La forme de l'identifiant n'etablit pas son unicite
globale : l'attribution des sequences et la prevention des collisions restent
a organiser par les implementations. Le schema verifie la forme des segments,
pas l'attribution effective d'un code pays ou d'une categorie.

## Manifeste JSON

Exemple minimal:

Les exemples sont fictifs. L'empreinte `e3b0c442...b855` ci-dessous et dans les
trois fichiers d'exemple est le SHA-256 d'une suite d'octets vide ; elle ne
constitue pas la preuve d'integrite d'un fichier audio. Aucun fichier audio ni
signature n'est fourni avec ces exemples.

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

Il impose notamment des contraintes de structure sur:

- le format `uid_auth`
- l'origine declaree: `human`, `ai`, `hybrid`
- le champ de date declaree `issued_at`
- les champs d'emetteur declares
- les droits IA/TDM
- l'algorithme `sha256` et la forme hexadecimale de son empreinte

## Validation Locale

Installer la dependance, puis valider les exemples contre le schema publie:

```bash
python3 -m pip install 'jsonschema>=4,<5'
python3 scripts/validate_examples.py
```

Le script utilise `schema/uid_auth_schema.json` avec la bibliotheque requise
`jsonschema`, sans activer les controles de format des dates et URI. Si la
bibliotheque ne peut pas etre importee, il s'arrete avec le code 2 et ne valide
aucun exemple. Il renvoie 0 si tous les exemples respectent le schema, ou 1 si
un exemple est invalide. Il ne recalcule pas les empreintes de fichiers, ne
verifie aucune signature et n'authentifie pas l'autorite emettrice.

Tests de regression (dependance installee):

```bash
python3 -m unittest discover -s tests -v
```

## Interoperabilite

Les integrations peuvent referencer les identifiants ou formats existants:

- ISRC
- ISWC
- UPC / EAN
- DDEX
- EIDR

Le profil ajoute des declarations structurees:

- un identifiant d'oeuvre declare
- une empreinte de fichier declaree
- des signaux de transparence IA/TDM

Cette coexistence ne demontre pas un echange DDEX, une integration C2PA ou une
conversion sans perte. Les regles de correspondance doivent etre specifiees et
testees. Voir les [differences entre formats et versions](ARCHITECTURE.md).

## Architecture

Les roles sont separes:

- AURA definit des declarations signees et des preuves d'integrite des fichiers. Son identifiant obligatoire est `aura_uid` ; UID_AUTH et les identifiants institutionnels restent facultatifs dans son socle.
- UID_AUTH definit le format d'un identifiant d'oeuvre declare et les metadonnees publiees ici.
- AUTHENTICA AI Rights publie un profil JSON-LD distinct, dont le schema exige `uid_auth`. Un document conforme a ce profil n'est pas automatiquement un manifeste AURA signe.

Un identifiant UID_AUTH peut etre porte dans une extension AURA, sans dependance
obligatoire du socle AURA a ce format. Le chemin d'extension et son sens doivent
etre documentes par l'integration ; le verificateur AURA ne les certifie pas.

Les objets identifies restent distincts:

| Element | Portee |
| --- | --- |
| `uid_auth` | Identifiant declare d'une oeuvre dans ce profil |
| `aura_uid` | Identifiant obligatoire d'une declaration AURA 1.0/1.1 |
| `asset.hash` | Empreinte des octets du fichier dans un manifeste AURA |
| Signature AURA | Lien entre la declaration signee et une cle publique |

Le champ AURA `aura_id` est optionnel et ne remplace pas `aura_uid`. Une
signature valide ne demontre pas la veracite des informations declarees.

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
