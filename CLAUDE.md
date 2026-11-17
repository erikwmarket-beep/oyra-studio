# OYRA Studio — istruzioni per Claude

Sito dello studio creativo OYRA (Milano). Lingua del sito e delle risposte: **italiano**.
Il proprietario considera stile e tono attuali definitivi: ogni nuovo lavoro li **conserva**.

## Pubblicazione (importante)
- Si modifica **solo `src/`** (più `build.py` e `assets/`). `site/`, `brand/`, `dist-artifact/` sono generati e ignorati da git.
- Dopo ogni modifica: `python3 build.py`, controlla le pagine, poi commit e `git push origin main`.
- Il push su `main` avvia `.github/workflows/deploy.yml`: build → branch `deploy` → Hostinger (Git, deploy automatico)
  pubblica su https://good-whitesmoke-panther-86.hostingersite.com/ in 1–2 minuti. Non modificare il branch `deploy` a mano.
- Modifiche grandi o rischiose: proponi prima un branch di anteprima e chiedi conferma prima del merge su `main`.

## Struttura
- `src/pages/*.html` contenuto delle pagine (home, studio, servizi, progetti, contatti, journal, 404).
  Segnaposto riempiti da `build.py`: `{{PROJECT_CARDS}}`, `{{PROJECT_ROWS}}`, `{{CTA}}`, `{{JOURNAL_*}}`, `{{N_PROJECTS}}`.
- `src/data.py` → `PROJECTS` (una voce = card + pagina `progetto-<slug>.html`) e `ARTICLES` (`journal-<slug>.html`).
  Progetti con foto reali: campi `photos`, `palette`, `fonts`, `quote`, `note` (vedi `alori`); immagini in `src/img/<slug>/`,
  JPEG max 1800 px, qualità ~80.
- `src/assets/oyra.css` e `oyra.js` condivisi da tutte le pagine; ogni funzione JS parte solo se trova i suoi elementi.
- Brand book: `src/brand.html` (fonte di verità per colori, caratteri, regole del logo).

## Stile da conservare
- **Direzione:** "retro-futuro mediterraneo". Audace, caldo, preciso, giocoso.
- **Colori:** Rosso OYRA `#E11A45` (grandi superfici), Crema `#EFECD7` / `#E4DFC3`, Inchiostro `#1B0A10`,
  Bordeaux `#7D0A2A`, Cipria `#F7C6CE`, Mandarino `#FF6A2B` solo come accento (max ~5%). Niente gradienti lucidi, vetro o neon.
- **Caratteri:** Unbounded (titoli, maiuscolo, spaziatura stretta), Archivo (testo), Instrument Serif corsivo
  solo per 1–2 parole d'accento nei titoli, Geist Mono per etichette maiuscole.
- **Segno:** l'asterisco (✱) dal logo: eyebrow, punti elenco, cursore, rotazione allo scroll. Logo mai deformato o ricolorato fuori palette.
- **Forme:** fasce piene alternate rosso / crema / inchiostro, pillole a raggio pieno, card con raggio ~20 px, grana leggera.
- **Movimento:** Lenis + GSAP (ScrollTrigger, SplitText); easing `cubic-bezier(.22,1,.36,1)`; titoli rivelati riga per riga,
  transizione a tendina rossa tra pagine. Rispettare sempre "riduci movimento". I contenuti devono essere leggibili anche senza JS.
- **Componenti esistenti da riusare** prima di crearne di nuovi: `phero`, `sec-title`, `cta`, `card`, `index/row`, `faq`, `plan`, `gal`, `j-card`.

## Tono di voce
Diretto, caldo, un po' ironico. Frasi corte, verbi attivi, niente gergo da agenzia ("soluzioni olistiche", "sinergie").
Copy breve: racconta il brand senza dilungarti. Non inventare numeri, clienti, testimonianze o risultati:
se mancano dati reali, chiedili o lascia un segnaposto evidente.

## Controlli prima del push
- `python3 build.py` senza errori; pagine nuove a 1440 px e 390 px senza scroll orizzontale e senza errori in console.
- Contrasto: crema su rosso solo per testi ≥ 24 px.

## Ancora da completare
Progetti diversi da Alori e articoli sono esempi; email, indirizzo, P.IVA, social; endpoint dei form (`data-endpoint`); informativa privacy.
