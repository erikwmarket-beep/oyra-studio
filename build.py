#!/usr/bin/env python3
"""Assembla il brand book e il sito multi-pagina di OYRA.

Sorgenti:  src/brand.html, src/pages/*.html, src/assets/oyra.css|js, src/data.py
Uscita:    brand/index.html, site/*.html + site/assets/  (pronti per il deploy)
           dist-artifact/  (versioni per l'anteprima su claude.ai)
Uso:       python3 build.py
"""
import pathlib, shutil, sys, html, hashlib
root = pathlib.Path(__file__).parent
sys.path.insert(0, str(root / 'src'))
from data import PROJECTS, ARTICLES, STAR  # noqa: E402

SYM = (root / 'assets/symbols.html').read_text()
# versione dei file per evitare che il browser mostri CSS/JS vecchi dopo un aggiornamento
V = {f: hashlib.md5((root / 'src/assets' / f).read_bytes()).hexdigest()[:8] for f in ('oyra.css', 'oyra.js')}
ICONS = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 19 19 5M8 5h11v11" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></symbol>
  <symbol id="i-down" viewBox="0 0 24 24"><path d="M12 3v18M5 14l7 7 7-7" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></symbol>
  <symbol id="i-menu" viewBox="0 0 24 24"><path d="M3 8h18M3 16h18" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></symbol>
  <symbol id="i-close" viewBox="0 0 24 24"><path d="M5 5l14 14M19 5 5 19" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></symbol>
</defs></svg>'''
FONTS = 'https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900&family=Geist+Mono:wght@400;500&family=Instrument+Serif:ital@0;1&family=Unbounded:wght@300..900&display=swap'
SCRIPTS = '''<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/ScrollTrigger.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/SplitText.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.3.4/dist/lenis.min.js"></script>
<script src="assets/oyra.js?v={V_JS}"></script>'''.replace('{V_JS}', V['oyra.js'])
S = STAR
ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true"><use href="#i-arrow"/></svg>'
NAV = [('progetti', 'progetti.html', 'Progetti'), ('servizi', 'servizi.html', 'Servizi'),
       ('studio', 'studio.html', 'Studio'), ('journal', 'journal.html', 'Journal')]


def head(title, desc, extra=''):
    return f'''<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="theme-color" content="#E11A45">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="assets/oyra.css?v={V["oyra.css"]}">
<script>try{{if(sessionStorage.getItem('oyra-enter')){{document.documentElement.classList.add('entering');sessionStorage.removeItem('oyra-enter')}}}}catch(e){{}}</script>
<style>{extra}</style>'''


def chrome(active, home=False):
    nav = ''.join(f'<a href="{h}" data-scramble{" aria-current=\"page\"" if k == active else ""}><span>{t}</span></a>' for k, h, t in NAV)
    mitems = [('home', 'index.html', 'Home')] + NAV + [('contatti', 'contatti.html', 'Contatti')]
    mnav = ''.join(f'<li><a href="{h}"{" aria-current=\"page\"" if k == active else ""}>{t} <span>{i:02d}</span></a></li>' for i, (k, h, t) in enumerate(mitems))
    loader = (root / 'src/pages/_loader.html').read_text() if home else ''
    return f'''{SYM}
{ICONS}
<div class="curtain" id="curtain" aria-hidden="true">{S}</div>
{loader}<div class="grain" aria-hidden="true"></div>
<div class="cursor" id="cursor" aria-hidden="true"><span id="cursor-label">Guarda</span></div>
<canvas class="sparks" id="sparks" aria-hidden="true"></canvas>
<div class="preview" id="preview" aria-hidden="true"><div class="slot" id="preview-slot"></div></div>

<header class="hdr wrap" id="hdr">
  <a class="brand" href="index.html" aria-label="OYRA Studio, home"><svg viewBox="0 0 3192 644" aria-hidden="true"><use href="#oyra-word"/></svg></a>
  <nav aria-label="Principale">{nav}</nav>
  <div class="right">
    <span class="status mono"><i></i>Disponibili da gennaio</span>
    <a class="btn magnet" href="contatti.html">Parliamone {S}</a>
    <button class="menu-btn" id="menu-btn" type="button" aria-expanded="false" aria-controls="menu" aria-label="Apri il menu"><svg viewBox="0 0 24 24" aria-hidden="true"><use id="menu-ico" href="#i-menu"/></svg></button>
  </div>
</header>

<div class="menu wrap" id="menu" aria-hidden="true">
  <ul>{mnav}</ul>
  <div class="mono" style="display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap"><span>ciao@oyra.studio</span><span>Milano, IT</span></div>
</div>
'''


FOOTER = f'''<footer class="foot wrap" data-header="light">
  <div class="foot-cols">
    <div style="display:grid;gap:18px;align-content:start"><p class="lead">Studio creativo indipendente, Milano.</p><a class="mono link-u" href="contatti.html" style="justify-self:start">Inizia un progetto →</a></div>
    <div><h4>Menu</h4><ul><li><a href="progetti.html">Progetti</a></li><li><a href="servizi.html">Servizi</a></li><li><a href="studio.html">Studio</a></li><li><a href="journal.html">Journal</a></li><li><a href="contatti.html">Contatti</a></li></ul></div>
    <div><h4>Social</h4><ul><li><a href="https://www.instagram.com/" rel="noopener">Instagram</a></li><li><a href="https://www.behance.net/" rel="noopener">Behance</a></li><li><a href="https://www.linkedin.com/" rel="noopener">LinkedIn</a></li></ul></div>
    <div><h4>Studio</h4><ul><li><a href="mailto:ciao@oyra.studio">ciao@oyra.studio</a></li><li><span style="font:500 17px/1.4 var(--f-text)">Milano, Italia</span></li><li><span style="font:500 17px/1.4 var(--f-text)">P.IVA da inserire</span></li></ul></div>
  </div>
  <svg class="logo foot-mark" viewBox="0 0 3192 644" role="img" aria-label="OYRA"><use href="#oyra-word"/></svg>
  <div class="foot-base mono"><span>© 2026 OYRA Studio</span><span>Fatto con cura a Milano ✱</span><a href="#top" style="text-decoration:none">Torna su ↑</a></div>
</footer>
<div class="toast mono" id="toast" role="status" aria-live="polite"></div>
'''


def cta(label='Contatti'):
    return f'''  <section class="cta wrap" data-header="dark">
    <div class="lbl mono" style="display:flex;justify-content:space-between;margin-bottom:clamp(32px,5vw,56px)"><span class="eyebrow">{S}{label}</span><span>Risposta in 24h</span></div>
    <h2 class="split">Hai un'idea? <span class="serif">Parliamone*</span></h2>
    <div class="cta-row">
      <p>Raccontaci il progetto in due righe: tempi, budget indicativo, cosa ti serve. Rispondiamo entro un giorno lavorativo.</p>
      <div class="mail">
        <span class="mono" style="opacity:.6">Scrivici</span>
        <a class="addr" href="mailto:ciao@oyra.studio">ciao@oyra.studio</a>
        <button class="copy" type="button" data-copy="ciao@oyra.studio" data-copy-msg="Indirizzo copiato">Copia indirizzo</button>
      </div>
      <a class="big-btn magnet" href="contatti.html"><svg viewBox="0 0 160 160" aria-hidden="true"><defs><path id="circ2" d="M80 80m-70 0a70 70 0 1 1 140 0a70 70 0 1 1-140 0"/></defs><text><textPath href="#circ2">Nuovo progetto ✱ Nuovo progetto ✱ </textPath></text></svg>Scrivici</a>
    </div>
  </section>'''


def card(p, i):
    tags = ''.join(f'<span>{t}</span>' for t in p['tags'])
    off = ' offset' if i % 2 else ''
    return f'''      <a class="card{off}" href="progetto-{p['slug']}.html" data-cat="{p['cats']}" data-cursor="Guarda">
        <div class="cover {p['cv']}"><div class="inner">{p['cover']}</div></div>
        <div class="meta"><h3>{p['name']}</h3><div class="tags">{tags}</div></div>
      </a>'''


def cards():
    return '    <div class="grid" id="grid">\n' + '\n'.join(card(p, i) for i, p in enumerate(PROJECTS)) + '\n    </div>'


def rows(top=True):
    r = ''.join(f'''
      <a class="row" href="progetto-{p['slug']}.html" data-cover="{i}"><span class="n">{p['name']}</span><span class="c mono">{p['client']}, {p['place']}</span><span class="y mono">{p['year']}</span><span class="ar">{ARROW}</span></a>''' for i, p in enumerate(PROJECTS))
    style = '' if top else ' style="margin-top:0"'
    return f'''    <div class="index"{style}>
      <div class="index-head mono"><span>Progetto</span><span>Cliente</span><span>Anno</span><span></span></div>{r}
    </div>'''


def jcard(a):
    return f'''      <a class="j-card" href="journal-{a['slug']}.html" data-cat="{a['cat']}">
        <div class="jc {a['jc']}">{a['jinner']}</div>
        <div class="jmeta"><span class="cat">{a['cat']}</span><span>{a['date']}</span><span>· {a['mins']} min</span></div>
        <h3>{a['title']}</h3><p>{a['excerpt']}</p>
      </a>'''


def jfeatured(a):
    return f'''    <a class="j-feat" href="journal-{a['slug']}.html" data-cursor="Leggi" data-reveal>
      <div class="jc {a['jc']}">{a['jinner']}</div>
      <div class="txt"><div class="jmeta"><span class="cat">{a['cat']}</span><span>{a['date']}</span><span>· {a['mins']} min</span></div>
        <h2>{a['title']}</h2><p class="body-t">{a['excerpt']}</p><span class="more" style="justify-self:start">Leggi l'articolo {ARROW}</span></div>
    </a>'''


NEWSLETTER = f'''    <div class="news" data-reveal>
      <h2>Una lettera <em>al mese</em></h2>
      <form data-form data-ok-msg="Iscrizione registrata, grazie!" data-endpoint="" aria-label="Iscrizione alla newsletter">
        <p class="body-t" style="color:inherit">Un articolo, un progetto, una cosa che ci è piaciuta. Niente spam, ti cancelli con un clic.</p>
        <div class="fld" style="gap:6px"><label for="n-mail" class="sr">Email</label><div class="row-f"><input id="n-mail" name="email" type="email" required placeholder="La tua email" autocomplete="email" data-msg="Inserisci la tua email"><button type="submit">Iscriviti</button></div><span class="err" aria-live="polite" style="color:var(--crema)"></span></div>
        <small>Iscrivendoti accetti di ricevere la newsletter di OYRA Studio.</small>
      </form>
    </div>'''


def journal_teaser():
    return f'''  <section class="sec bg-crema2 wrap" data-header="dark">
    <div class="sec-top">
      <h2 class="sec-title split">Dal <span class="serif">journal</span></h2>
      <a class="more" href="journal.html">Tutti gli articoli {ARROW}</a>
    </div>
    <div class="j-grid" data-reveal data-stagger>
{chr(10).join(jcard(a) for a in ARTICLES)}
    </div>
  </section>'''


def fill(s):
    return (s.replace('{{N_PROJECTS}}', f'({len(PROJECTS):02d})').replace('{{PROJECT_CARDS}}', cards()).replace('{{PROJECT_ROWS_FLAT}}', rows(False)).replace('{{PROJECT_ROWS}}', rows())
             .replace('{{CTA}}', cta()).replace('{{JOURNAL_TEASER}}', journal_teaser())
             .replace('{{JOURNAL_FEATURED}}', jfeatured(ARTICLES[0]))
             .replace('{{JOURNAL_CARDS}}', '\n'.join(jcard(a) for a in ARTICLES[1:]) if len(ARTICLES) > 1 else '')
             .replace('{{NEWSLETTER}}', NEWSLETTER))


def txt(c):
    r, g, b = (int(c[i:i + 2], 16) for i in (1, 3, 5))
    return '#1B0A10' if (0.299 * r + 0.587 * g + 0.114 * b) > 150 else '#EFECD7'


ORBIT = ('<svg viewBox="0 0 128 128" aria-hidden="true"><path d="M91 22c-9-7-20-11-32-11C30 11 7 35 7 64s23 53 52 53 52-24 52-53c0-8-2-16-5-23M87 31c9 7 15 19 15 33 0 24-19 43-43 43S16 88 16 64s19-43 43-43c10 0 20 4 28 10" '
         'fill="none" stroke="currentColor" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="94" cy="20" r="5" fill="currentColor"/></svg>')


def photo_gallery(p):
    tiles = ''.join(f'<figure class="g ph {w}"><img src="assets/img/{p["slug"]}/{f}.jpg" alt="{html.escape(c)}" loading="lazy"><figcaption class="cap">{c}</figcaption></figure>' for f, w, c in p['photos'])
    pal = ''.join(f'<span style="background:{h};color:{txt(h)}"><b>{n}</b>{h}</span>' for n, h in p['palette'])
    bg, ac, ink = p['colors']
    return f'''  <section class="sec bg-crema wrap" data-header="dark" style="padding-top:0">
    <div class="gal" data-reveal data-stagger>{tiles}</div>
  </section>

  <section class="sec wrap brand-sys" data-header="dark" style="background:{bg};color:{ink}">
    <div class="sec-top"><h2 class="sec-title split" style="font-size:clamp(40px,6vw,100px)">Il <span class="serif">sistema</span></h2><span class="mono" style="opacity:.7">Dal brand book</span></div>
    <div class="gal" data-reveal data-stagger>
      <div class="g w5 g-mark" style="background:{ink};color:{bg}">{p.get('mark', ORBIT)}<span class="cap">{p.get('mark_cap', 'Il segno · un cerchio aperto, un punto di luce')}</span></div>
      <div class="g w7 g-quote" style="background:{ac};color:{ink}"><p>{p['quote']}</p><span class="cap">{p['fonts']}</span></div>
      <div class="g w12 g-pal6">{pal}</div>
    </div>
  </section>
'''


def project_page(i, p):
    nx = PROJECTS[(i + 1) % len(PROJECTS)]
    bg, ac, ink = p['colors']
    tags = ' · '.join(p['tags'])
    deliv = ''.join(f'<div>{d}</div>' for d in p['deliv'])
    if p['mock'] == 'card':
        mock = f'<div><div class="mock-card"><b>{p["name"]}</b><span class="mono" style="display:flex;justify-content:space-between"><span>{p["place"]}</span><span>{p["year"]}</span></span></div><div class="mock-card b2"><span class="mono">{p["client"]}</span><span class="mono">✱</span></div></div>'
    else:
        mock = f'<div class="mock-phone"><div class="scr"><span class="mono" style="font-size:9px">{p["name"]} ✱</span><b>{p["name"]}</b><i></i></div></div>'
    extra = f':root{{--p-bg:{bg};--p-ac:{ac};--p-ink:{ink}}}'
    hdr_mode = 'light' if bg in ('#1B0A10', '#7D0A2A', '#E11A45') else 'dark'
    main = f'''  <section class="case-hero wrap" data-header="{hdr_mode}">
    <div class="top mono page-in" style="display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-bottom:clamp(20px,3vw,40px)"><a class="link-u" href="progetti.html">← Tutti i progetti</a><span>{tags} · {p['year']}</span></div>
    <h1 class="page-title">{p['name']}</h1>
    <p class="sum page-in">{p['summary']}</p>
  </section>
  <section class="case-cover wrap" data-header="{hdr_mode}">
    <div class="cover {p['cv']} page-in"><div class="inner" data-speed="6">{p['cover']}</div></div>
    <div class="case-meta page-in" style="color:var(--p-ink)">
      <div><span class="mono">Cliente</span><b>{p['client']}</b></div>
      <div><span class="mono">Luogo</span><b>{p['place']}</b></div>
      <div><span class="mono">Anno</span><b>{p['year']}</b></div>
      <div><span class="mono">Servizi</span><b>{', '.join(p['tags'])}</b></div>
    </div>
    {f'<a class="btn magnet case-visit" href="{p["url"]}" target="_blank" rel="noopener">Visita {p.get("url_label", "il sito")} {ARROW}</a>' if p.get('url') else ''}
  </section>

  <section class="sec bg-crema wrap" data-header="dark">
    <div class="case-two" data-reveal data-stagger>
      <div><span class="mono">01 — La sfida</span><h2>Il <em>punto</em> di partenza</h2><p class="body-t">{p['challenge']}</p></div>
      <div><span class="mono">02 — L'idea</span><h2>La nostra <em>risposta</em></h2><p class="body-t">{p['idea']}</p></div>
    </div>
  </section>

{photo_gallery(p) if p.get('photos') else f'''  <section class="sec bg-crema wrap" data-header="dark" style="padding-top:0">
    <div class="gal" data-reveal data-stagger>
      <div class="g w7 cover {p['cv']}" style="border-radius:22px"><div class="inner" style="transform:scale(1.15)">{p['cover']}</div></div>
      <div class="g w5 g-type"><span class="aa">Aa<em>a</em></span><span class="cap">Tipografia</span></div>
      <div class="g w5 g-pal"><span style="background:{bg};color:{txt(bg)}">{bg}</span><span style="background:{ac};color:{txt(ac)}">{ac}</span><span style="background:{ink};color:{txt(ink)}">{ink}</span></div>
      <div class="g w7 g-mock">{mock}<span class="cap">Applicazioni</span></div>
    </div>
  </section>
'''}
  <section class="sec bg-crema2 wrap" data-header="dark">
    <div class="deliv"><h2 class="split">Cosa <span class="serif" style="color:var(--rosso)">abbiamo fatto</span></h2><div class="dl" data-reveal>{deliv}</div></div>
    {f'<p class="case-note mono">{p["note"]}</p>' if p.get('note') else ''}
  </section>

  <a class="next wrap end-round" href="progetto-{nx['slug']}.html" data-header="light" data-cursor="Apri">
    <span class="mono">Prossimo progetto</span>
    <span class="nt">{nx['name']} {S}</span>
  </a>
'''
    return head(f"{p['name']} — OYRA Studio", p['summary'], extra), main


def article_page(i, a):
    others = [x for x in ARTICLES if x is not a][:2]
    rel = '\n'.join(jcard(x) for x in others)
    main = f'''  <section class="art-hero wrap" data-header="dark">
    <div class="top mono page-in" style="display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap"><a class="link-u" href="journal.html">← Journal</a><span>{a['date']}</span></div>
    <div class="jmeta page-in" style="margin-top:clamp(24px,3vw,40px)"><span class="cat">{a['cat']}</span><span>{a['mins']} minuti di lettura</span></div>
    <h1 class="page-title">{a['title']}</h1>
    <div class="jc {a['jc']} page-in"><div data-speed="8">{a['jinner']}</div></div>
  </section>
  <article class="art wrap" data-header="dark">
    <div class="art-body">
{a['body']}
    </div>
    <div class="art-foot"><span class="mono">OYRA Studio · {a['date']}</span><button class="copy" type="button" data-copy="url" data-copy-msg="Link copiato">Copia il link</button></div>
  </article>
  <section class="sec bg-crema2 wrap end-round" data-header="dark">
    <div class="sec-top"><h2 class="sec-title split" style="font-size:clamp(36px,5vw,80px)">Da leggere <span class="serif">anche</span></h2><a class="more" href="journal.html">Journal {ARROW}</a></div>
    <div class="j-grid">
{rel}
    </div>
{NEWSLETTER}
  </section>
'''
    return head(f"{a['title']} — Journal OYRA", a['excerpt']), main


PAGES = {
    'index':    ('OYRA Studio', 'OYRA è uno studio creativo di Milano: identità di marca, siti web e motion design per brand che si fanno ricordare.', 'home'),
    'studio':   ('Studio — OYRA Studio', "Chi siamo: uno studio creativo indipendente di Milano, piccolo di proposito. Valori, metodo e squadra.", 'studio'),
    'servizi':  ('Servizi — OYRA Studio', 'Brand identity, siti web, motion design e art direction. Tempi, formule e domande frequenti.', 'servizi'),
    'progetti': ('Progetti — OYRA Studio', 'Una selezione di progetti di identità, siti web e motion design firmati OYRA.', 'progetti'),
    'contatti': ('Contatti — OYRA Studio', 'Raccontaci il tuo progetto: rispondiamo entro un giorno lavorativo.', 'contatti'),
    '404':      ('Pagina non trovata — OYRA Studio', 'La pagina che cerchi non esiste.', ''),
    'journal':  ('Journal — OYRA Studio', 'Idee, guide e retroscena dallo studio: brand, siti web e motion design.', 'journal'),
}


def doc(headpart, body):
    return ('<!doctype html>\n<html lang="it">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + headpart + '\n</head>\n<body>\n' + body + '\n</body>\n</html>\n')


def build_site():
    out = root / 'site'; art = root / 'dist-artifact/site'
    for d in (out, art):
        if d.exists(): shutil.rmtree(d)
        (d / 'assets').mkdir(parents=True)
    for f in ('oyra.css', 'oyra.js'):
        for d in (out, art): shutil.copy(root / 'src/assets' / f, d / 'assets' / f)
    star = (root / 'assets/oyra-star.svg').read_text()
    for d in (out, art): (d / 'assets/favicon.svg').write_text(star)
    if (root / 'src/img').exists():
        for d in (out, art): shutil.copytree(root / 'src/img', d / 'assets/img')
    for f in ('.htaccess', 'robots.txt', '404.html'):
        src = root / 'src/static' / f
        if src.exists(): shutil.copy(src, out / f)
    pages = {}
    for name, (title, desc, active) in PAGES.items():
        main = fill((root / f'src/pages/{name}.html').read_text())
        pages[name] = (head(title, desc), chrome(active, home=(name == 'index')), main)
    for i, p in enumerate(PROJECTS):
        h, m = project_page(i, p); pages['progetto-' + p['slug']] = (h, chrome('progetti'), m)
    for i, a in enumerate(ARTICLES):
        h, m = article_page(i, a); pages['journal-' + a['slug']] = (h, chrome('journal'), m)
    for name, (h, c, m) in pages.items():
        body = f'{c}\n<main id="top">\n{m}\n</main>\n\n{FOOTER}\n{SCRIPTS}\n'
        full = doc(h, body)
        if name == '404':
            full = full.replace('<head>\n', '<head>\n<base href="/">\n<meta name="robots" content="noindex">\n', 1)
        (out / f'{name}.html').write_text(full)
        # nell'anteprima la pagina principale viene avvolta dal visualizzatore: niente doctype
        (art / f'{name}.html').write_text(h + '\n' + body if name == 'index' else full)
    print('site:', len(pages), 'pagine ->', ', '.join(pages))


def build_brand():
    p = root / 'src/brand.html'
    s = p.read_text().replace('<!--SYMBOLS-->', SYM)
    h, b = s.split('<!--BODY-->', 1)
    (root / 'brand').mkdir(exist_ok=True)
    (root / 'brand/index.html').write_text(doc(h, b))
    (root / 'dist-artifact').mkdir(exist_ok=True)
    (root / 'dist-artifact/brand.html').write_text(h + '\n' + b)
    print('brand: ok')


if __name__ == '__main__':
    build_brand(); build_site()
