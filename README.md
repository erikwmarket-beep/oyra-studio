# OYRA Studio — sito e brand book

## Struttura
- `brand/index.html` — brand book
- `site/` — sito pronto per il deploy (carica la cartella così com'è)
  - `index.html` home · `studio.html` · `servizi.html` · `progetti.html` · `contatti.html` · `journal.html`
  - `progetto-*.html` (6 case study) · `journal-*.html` (3 articoli)
  - `assets/oyra.css`, `assets/oyra.js`, `assets/favicon.svg`
- `src/` — sorgenti: modifica qui, poi `python3 build.py`
  - `src/pages/*.html` contenuto delle pagine principali
  - `src/data.py` progetti e articoli (aggiungi un dizionario = nuova pagina generata)
  - `src/assets/` CSS e JS condivisi
- `assets/` — logo vettoriale

## Da completare prima di andare online
- Progetti e articoli sono esempi: sostituiscili in `src/data.py`
- Email, indirizzo, P.IVA, link social, orari
- Form contatti e newsletter: imposta `data-endpoint` (es. Formspree, Netlify Forms) in
  `src/pages/contatti.html` e in `NEWSLETTER` dentro `build.py`. Senza endpoint mostrano la conferma ma non inviano nulla.
- Informativa privacy (il form la cita)
- Verifica tempi, revisioni e formule in `servizi.html`

## Pubblicazione automatica su Hostinger
Ogni push sul branch `main` avvia `.github/workflows/deploy.yml`:
GitHub ricostruisce il sito con `build.py` e carica `site/` su Hostinger via FTP (solo i file cambiati).
Lo stato di ogni pubblicazione si vede nella scheda **Actions** del repository.

Configurazione una tantum (GitHub → Settings → Secrets and variables → Actions):
| Tipo | Nome | Dove lo trovi in Hostinger (hPanel → Siti web → Gestisci → File → Account FTP) |
|---|---|---|
| Secret | `FTP_SERVER` | "Host FTP" (es. `ftp.nomesito.hostingersite.com` o un IP) |
| Secret | `FTP_USERNAME` | "Nome utente FTP" (es. `u123456789`) |
| Secret | `FTP_PASSWORD` | la password FTP (puoi reimpostarla lì) |
| Variable | `FTP_SERVER_DIR` | cartella del sito, con `/` finale. Con l'utente FTP principale di solito `public_html/` o `domains/NOME-DOMINIO/public_html/` |
| Variable (facoltativa) | `FTP_PROTOCOL` | `ftp` se l'invio con `ftps` fallisce |

Per pubblicare a mano: Actions → "Deploy su Hostinger" → Run workflow.
Quando passi al dominio definitivo aggiorna `src/static/robots.txt` (ora blocca l'indicizzazione).
