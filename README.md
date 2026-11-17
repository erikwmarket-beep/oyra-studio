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
Ogni push sul branch `main` avvia `.github/workflows/deploy.yml`: GitHub ricostruisce il sito con
`build.py` e pubblica la cartella `site/` sul branch **`deploy`**. Lo stato si vede nella scheda **Actions**.

### Metodo consigliato: Git di Hostinger (nessuna password da salvare)
1. hPanel → Siti web → Gestisci → **Avanzate → GIT**
2. Repository: `https://github.com/UTENTE/REPO.git` (repo privato: usa l'indirizzo SSH `git@github.com:UTENTE/REPO.git`
   e aggiungi la chiave SSH mostrata da Hostinger in GitHub → Settings → Deploy keys)
3. Branch: `deploy` · Cartella: lasciala vuota (la cartella `public_html` deve essere vuota) → **Crea**
4. Clicca **Distribuisci** una volta, poi **Deploy automatico**: copia l'URL del webhook
5. GitHub → Settings → Webhooks → Add webhook → incolla l'URL, evento "Just the push event" → Add

### Alternativa: FTP
Se il Git di Hostinger non è disponibile nel piano, aggiungi in GitHub → Settings → Secrets and variables → Actions:
| Tipo | Nome | Dove lo trovi (hPanel → File → Account FTP) |
|---|---|---|
| Secret | `FTP_SERVER` | Host FTP |
| Secret | `FTP_USERNAME` | Nome utente FTP |
| Secret | `FTP_PASSWORD` | Password FTP |
| Variable | `FTP_SERVER_DIR` | cartella del sito con `/` finale, di solito `public_html/` |
| Variable (facoltativa) | `FTP_PROTOCOL` | `ftp` se `ftps` fallisce |

Con `FTP_SERVER` impostato, il workflow carica anche via FTP. Per ripubblicare a mano: Actions → "Deploy su Hostinger" → Run workflow.

Quando passi al dominio definitivo aggiorna `src/static/robots.txt` (ora blocca l'indicizzazione).
