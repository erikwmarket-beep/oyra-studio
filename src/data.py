# Contenuti del sito OYRA. I progetti e gli articoli sono esempi da sostituire con quelli reali.
STAR = '<svg viewBox="0 0 500 564" aria-hidden="true"><use href="#oyra-star"/></svg>'

PROJECTS = [
  dict(slug='yagiu', name='Yagiu', client='Community di viaggiatori', place='Online · 5 lingue', year='2026',
       cats='brand web', tags=['Branding','Web design','Sviluppo'], cv='cv-photo',
       cover='<img src="assets/img/yagiu/brand-notebook.jpg" alt="Taccuino da viaggio giallo con il logotipo Yagiu, su una mappa al sole" loading="lazy">',
       colors=('#FFF4E9','#F7B32B','#562D2A'),
       palette=[('Crema','#FFF4E9'),('Giallo','#F7B32B'),('Teal','#3295A0'),('Azzurro','#6197C5'),('Corallo','#E8895E'),('Verde','#43A574'),('Marrone','#562D2A')],
       fonts='Cabinet Grotesk · Satoshi',
       mark='<svg style="height:56%;width:auto" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 182 253"><path fill="currentColor" fill-rule="evenodd" d="M81.33 247.99C68.37 247.38 53.26 242.06 41.31 233.90C22.33 220.94 9.71 201.82 5.76 180.04C5.22 177.05 5.22 176.92 5.82 176.32C6.31 175.83 6.31 175.83 28.08 175.83C51.78 175.83 50.59 175.79 51.29 176.77C51.47 177.04 51.93 178.04 52.31 179.00C52.96 180.65 54.90 184.42 56.06 186.25C59.27 191.36 67.12 197.56 73.62 200.15C78.95 202.27 83.04 202.92 91.00 202.92C99.27 202.92 103.26 202.23 109.03 199.82C117.86 196.13 125.80 188.13 129.59 179.11C130.53 176.89 130.81 176.46 131.56 176.10C132.08 175.86 134.15 175.83 153.78 175.84C177.11 175.84 176.03 175.80 176.47 176.72C177.01 177.84 174.59 188.10 172.45 193.75C166.73 208.88 157.75 220.65 143.52 231.68C131.72 240.84 114.58 247.29 100.17 248.00C96.62 248.18 85.15 248.17 81.33 247.99ZM84.42 171.06C82.11 170.96 78.62 170.66 77.91 170.50C77.53 170.41 76.29 170.22 75.15 170.08C73.02 169.80 68.91 169.00 65.83 168.27C54.91 165.64 41.53 158.13 31.68 149.11C24.80 142.79 20.09 137.01 15.08 128.75C4.94 112.00 1.69 87.85 6.76 67.00C11.79 46.34 25.88 27.49 45.16 15.61C53.53 10.45 66.66 5.85 75.42 5.00C76.42 4.90 77.74 4.75 78.33 4.67C82.49 4.10 84.19 4.08 130.60 4.08C180.76 4.08 177.08 4.01 177.53 5.06C177.85 5.82 177.85 87.31 177.54 92.25C176.21 112.81 169.30 129.06 155.62 143.79C145.68 154.49 134.37 162.02 121.30 166.64C117.02 168.16 111.36 169.52 107.42 169.99C106.59 170.09 105.32 170.28 104.58 170.42C101.73 170.94 90.01 171.31 84.42 171.06ZM99.58 125.46C106.99 124.23 112.28 121.95 117.33 117.82C124.89 111.65 128.83 105.58 131.17 96.53C131.65 94.66 131.83 93.30 132.16 89.12C132.46 85.46 132.39 50.79 132.09 50.07C131.61 48.92 133.15 48.98 108.12 49.05C80.65 49.12 82.27 49.00 74.33 51.54C69.58 53.06 62.89 57.87 58.74 62.75C56.31 65.60 55.83 66.30 54.01 69.58C49.77 77.22 48.55 84.90 50.02 94.66C50.11 95.26 50.56 96.96 51.01 98.45C53.35 106.14 57.09 111.75 63.36 117.00C66.78 119.87 67.21 120.16 70.15 121.65C74.76 123.99 79.25 125.19 86.67 126.06C89.12 126.35 96.18 126.02 99.58 125.46Z"/></svg>',
       mark_cap='Il simbolo · la «g» con la coda che diventa strada',
       url='https://yagiu.com/', url_label='yagiu.com',
       summary="Identità, brand book e sito di una community di viaggiatori: una mappa del mondo raccontata da chi i luoghi li conosce davvero.",
       challenge="Le piattaforme di viaggio sono piene di classifiche, recensioni e cartoline tutte uguali. Yagiu voleva il contrario: guide personali scritte da chi un luogo l'ha vissuto, con rispetto per chi ci abita. Serviva un marchio caldo e un sito che facesse venire voglia di esplorare.",
       idea="Il marchio nasce dalla «g», la lettera con la coda che diventa strada: da lì vengono il simbolo, le forme e le icone. Il sito parte da una mappa reale ricolorata con la palette. Le guide si scelgono per esperienza (ammirare, rallentare, assaggiare), i paesi si sfogliano come un mazzo di carte e un test di 20 affermazioni dice che viaggiatore sei. Tutto in cinque lingue.",
       deliv=['Logo, simbolo «g», palette e caratteri','Brand book','Icone proprietarie e forme del marchio','UX e UI del sito','Sviluppo: mappa, guide, profili, storie e test','Sito in 5 lingue'],
       photos=[('brand-g','w7',''),('brand-tote','w5',''),
               ('brand-logo','w12',''),
               ('brand-tag','w4',''),('shapes','w4',''),('palette','w4',''),
               ('bookduo','w12',''),
               ('site-hero','w12',''),
               ('experiences','w7',''),('test','w5',''),
               ('wall','w12',''),('phones','w12','')],
       quote="Incontra i luoghi attraverso chi li conosce.",
       note="Taccuino, borsa e cartellino sono visualizzazioni del marchio. Profili, guide e numeri visibili nelle schermate sono contenuti dimostrativi del sito, in attesa dei contenuti reali della community.",
       mock='card'),
  dict(slug='immobiliare-sociale', name='Immobiliare Sociale', client='Pellicciotta Immobili', place='Milano', year='2026',
       cats='web', tags=['Web design','Sviluppo','Motion'], cv='cv-photo',
       cover='<img src="assets/img/immobiliare-sociale/mock-hero.jpg" alt="Il sito Immobiliare Sociale su laptop e smartphone" loading="lazy">',
       colors=('#E4DFC3','#E11A45','#1B0A10'),
       url='https://immobiliaresociale.it/', url_label='immobiliaresociale.it',
       summary="Il sito di un'agenzia immobiliare milanese che dona in beneficenza metà della sua provvigione netta. Un'idea etica, raccontata in modo chiaro e credibile.",
       challenge="Pellicciotta Immobili, agenzia di famiglia attiva a Milano da oltre 35 anni, lanciava Immobiliare Sociale: per ogni casa venduta o affittata, il 50% della provvigione netta va a un ente scelto da chi vende. Un'idea forte, ma facile da fraintendere: il sito doveva spiegarla in modo semplice, senza retorica, e renderla credibile.",
       idea="Abbiamo messo al centro il meccanismo e le persone. Tre passaggi chiari, i vantaggi concreti (provvigione più bassa, risparmio fiscale, beneficenza a costo zero), gli enti sostenuti e le donazioni già fatte, con importi e foto. Le storie di Fabio e Giulia danno un volto all'agenzia. Tema chiaro e scuro, animazioni leggere, tutto pensato per leggersi bene anche da telefono.",
       deliv=['Architettura dei contenuti e testi','UX e UI design','Tema chiaro e scuro','Sviluppo e animazioni','Pagine enti, donazioni e interviste','SEO di base'],
       photos=[('mock-phone','w4',''),('mock-scroll','w4',''),('mock-mix','w4',''),
               ('mock-wall','w12',''),('mock-phones','w12',''),('mock-browser','w12',''),('mock-duo','w12','')],
       mock='card'),
  dict(slug='alori', name='Alori', client='Progetto di brand indipendente', place='Italia', year='2026',
       cats='brand web', tags=['Branding','Web','Art direction'], cv='cv-photo',
       cover='<img src="assets/img/alori/hero-wide.jpg" alt="Bottiglia di Alori su un tavolo all\'aperto" loading="lazy">',
       colors=('#F3ECDF','#CFD86A','#1E2620'),
       palette=[('Panna','#F3ECDF'),('Travertino','#E4D6C1'),('Notte','#1E2620'),('Oliva','#47502F'),('Bergamotto','#CFD86A'),('Pompelmo','#E98E7B')],
       fonts='Instrument Serif · Instrument Sans · DM Mono',
       summary="Un aperitivo botanico 0.0% da miscelare: nome, segno, gamma, rito e sito, ideati da OYRA come progetto di marca indipendente.",
       challenge="Gli analcolici per l'aperitivo sembrano spesso un ripiego: bevande pronte, dolci, con un'immagine da succo di frutta. Volevamo immaginare una base da miscelare che avesse il carattere di un bitter e il tono di un prodotto adulto.",
       idea="Alori si versa, si allunga con soda e si condivide: 50 ml e 100 ml di soda, con una scorza di pompelmo. Il segno è un'orbita aperta con un punto di luce, come un cerchio di persone attorno a un tavolo sempre pronto ad accogliere qualcuno in più. Colori presi dalla carta delle etichette, dalla pietra e dagli agrumi.",
       deliv=['Nome, posizionamento e tono di voce','Segno "orbita" e logotipo','Palette, caratteri e brand book','Gamma di cinque profili ed etichette','Art direction e visualizzazioni di concept','Sito bilingue IT / EN con animazioni'],
       url='https://alori.uno/', url_label='alori.uno',
       photos=[('site-home','w12','Il sito · alori.uno'),('bottle-citrus','w4','Citrus · profilo firma'),('bottle-apricot','w4','Apricot & Sage'),('bottle-fig','w4','Green Fig'),
               ('pour','w5','Il rito: 50 ml'),('botanicals','w7','Le botaniche'),('table','w12','Prima di cena, con chi vuoi'),
               ('bottle-quince','w4','Quince & Cardamom · in sviluppo'),('bottle-cherry','w4','Sour Cherry · in sviluppo'),('peel-macro','w4','Scorza di pompelmo')],
       quote="Apri il momento.",
       note="Prodotto, bottiglia e fotografie sono visualizzazioni di concept: Alori è un progetto di marca indipendente di OYRA, il prodotto è in sviluppo.",
       mock='card'),
  dict(slug='forno-di-brera', name='Forno di Brera', client='Panificio di quartiere', place='Milano', year='2026',
       cats='brand', tags=['Branding','Packaging'], cv='cv-1',
       cover='<div class="loaf"></div><div class="t">Forno<em>di Brera</em></div>',
       colors=('#F7C6CE','#FF6A2B','#7D0A2A'),
       summary="Un forno di quartiere con quarant'anni di storia, ridisegnato per restare quello di sempre e farsi notare dalla via.",
       challenge="Il forno aveva clienti affezionati ma un'immagine ferma agli anni '90: insegna sbiadita, sacchetti anonimi, nessuna presenza online. Accanto aprivano catene con vetrine curatissime.",
       idea="Siamo partiti dalla forma della pagnotta, diventata il segno del marchio. Colori caldi da cartoleria, un timbro per i sacchetti di carta e un'insegna dipinta a mano: moderno, ma con l'odore del forno.",
       deliv=['Logo e sistema di identità','Sacchetti, scatole e timbri','Insegna e vetrine','Menu, cartellini e listino','Profilo Instagram e modelli post'],
       mock='card'),
  dict(slug='lido-aurora', name='Lido Aurora', client='Stabilimento balneare', place='Liguria', year='2026',
       cats='web motion', tags=['Web','Motion'], cv='cv-2',
       cover='<div class="sun">Lido<br>Aurora</div>',
       colors=('#FF6A2B','#E11A45','#1B0A10'),
       summary="Un sito con le prenotazioni online e un'identità in movimento per uno stabilimento che si prenotava solo al telefono.",
       challenge="La stagione dura quattro mesi e le prenotazioni passavano tutte dal telefono del bar. Il sito era una pagina statica con orari vecchi di due anni.",
       idea="Abbiamo costruito un sito leggero con la mappa degli ombrelloni prenotabile in tre tocchi. Il sole che sorge è diventato un'animazione ricorrente: sul sito, nelle storie e sullo schermo del bar.",
       deliv=['Sito web e prenotazioni','Mappa interattiva degli ombrelloni','Logo animato','Kit di storie e reel','Segnaletica in spiaggia'],
       mock='phone'),
  dict(slug='vespertina', name='Vespertina', client='Cantina', place='Langhe', year='2025',
       cats='brand', tags=['Branding','Etichette'], cv='cv-3',
       cover='<div class="halo"></div><div class="bottle"><span>'+STAR+'</span></div>',
       colors=('#1B0A10','#E11A45','#EFECD7'),
       summary="Nome, etichette e materiali per la prima linea di vini di una giovane cantina delle Langhe.",
       challenge="Due fratelli, quattro ettari e la prima vendemmia imbottigliata. Volevano distinguersi sugli scaffali senza imitare le etichette classiche della zona.",
       idea="Il nome viene dall'ora in cui si lavora in vigna d'estate, la sera. Ogni etichetta ha un sole basso stampato a caldo e un colore diverso per vitigno: si riconoscono da lontano, anche al buio di un'enoteca.",
       deliv=['Naming della linea','Etichette e controetichette','Casse e carta velina','Schede tecniche','Stand per fiere'],
       mock='card'),
  dict(slug='studio-salvi', name='Studio Salvi', client='Studio di architettura', place='Milano', year='2025',
       cats='web', tags=['Web','Art direction'], cv='cv-4',
       cover='<div class="blk"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>',
       colors=('#E4DFC3','#E11A45','#1B0A10'),
       summary="Un portfolio online facile da aggiornare, con una griglia modulare che ricorda una pianta d'architetto.",
       challenge="Lo studio pubblicava i progetti una volta l'anno perché aggiornare il sito richiedeva uno sviluppatore. Le foto erano disomogenee e i progetti migliori restavano nascosti.",
       idea="Una griglia a moduli quadrati, come la carta millimetrata, che si compone da sola a ogni nuovo progetto. Abbiamo curato anche il nuovo servizio fotografico, così ogni progetto ha luce e inquadrature coerenti.",
       deliv=['Sito web e CMS','Art direction fotografica','Archivio progetti','Modelli per presentazioni'],
       mock='phone'),
  dict(slug='ciclo', name='Ciclo', client='Biciclette urbane', place='Torino', year='2025',
       cats='brand motion', tags=['Branding','Motion'], cv='cv-5',
       cover='<div class="lines"></div><div class="t">Ciclo</div>',
       colors=('#E11A45','#EFECD7','#1B0A10'),
       summary="Il lancio di un nuovo marchio di biciclette da città: logo, logo animato e video di presentazione.",
       challenge="Un mercato pieno di marchi che si somigliano, tutti grigi e tecnici. Ciclo voleva parlare a chi usa la bici per andare al lavoro, non a chi fa gare.",
       idea="Un logotipo inclinato in avanti, come se fosse già in movimento, e un rosso pieno su ogni telaio. Il logo animato riprende il giro di una ruota e chiude ogni video e ogni pagina del sito.",
       deliv=['Logo e logo animato','Video di lancio','Grafiche per e-commerce','Decalcomanie dei telai','Linee guida del marchio'],
       mock='card'),
  dict(slug='mare-nostro', name='Mare Nostro', client='Festival musicale', place='Puglia', year='2024',
       cats='brand web', tags=['Identità','Web'], cv='cv-6',
       cover='<div class="disc"><span>Mare<em>Nostro</em>Festival</span></div>',
       colors=('#7D0A2A','#E11A45','#F7C6CE'),
       summary="L'identità di un festival estivo che cambia ogni anno senza perdere la sua faccia.",
       challenge="Ogni edizione aveva un grafico diverso e un'immagine diversa. Il pubblico non collegava i manifesti al festival e gli sponsor chiedevano più riconoscibilità.",
       idea="Un sistema fatto di retino e cerchio: le forme restano, i colori e le composizioni cambiano a ogni edizione. Abbiamo disegnato i manifesti, il sito con il programma e il merchandising.",
       deliv=['Identità del festival','Manifesti e affissioni','Sito e programma','Merchandising','Grafiche per il palco'],
       mock='phone'),
]

ARTICLES = [
  dict(slug='perche-un-asterisco', title='Perché un asterisco', cat='Brand', date='12 novembre 2026', mins='3',
       jc='jc-1', jinner=STAR,
       excerpt="La storia del nostro marchio, e cosa c'entra una nota a margine con il lavoro di uno studio.",
       body="""<p>Quando abbiamo ridisegnato OYRA cercavamo un segno che dicesse cosa facciamo senza spiegarlo. L'abbiamo trovato in fondo a una pagina.</p>
<h2>Una nota che cambia la frase</h2>
<p>L'asterisco è il segno delle note: rimanda a un dettaglio che sta fuori dal testo ma ne cambia il senso. Per noi un brand funziona così. La differenza tra due caffè, due studi di architettura o due festival spesso sta in un dettaglio che il cliente nota anche senza saperlo.</p>
<blockquote>Il nostro lavoro è trovare quel dettaglio e renderlo impossibile da ignorare.</blockquote>
<h2>Sopra la Y</h2>
<p>Nel logo l'asterisco sta sopra la Y, come un accento. Lo usiamo anche da solo: come favicon, come cursore sul sito, come punto elenco, come sigillo sui materiali. Ruota quando qualcosa si muove, e segna quello che conta.</p>
<h2>Rosso e crema</h2>
<p>I colori vengono dalla stessa idea: un rosso pieno che si vede da lontano, e un crema caldo che ricorda la carta. Niente sfumature, niente effetti. Se un'identità funziona con due colori, funziona ovunque.</p>
<p>Il resto lo trovate nel nostro brand book, che usiamo ogni giorno come facciamo con quelli dei nostri clienti.</p>"""),
  dict(slug='prima-di-rifare-il-logo', title='Cinque domande prima di rifare il logo', cat='Guide', date='28 ottobre 2026', mins='4',
       jc='jc-2', jinner='<b>5<em>?</em></b>',
       excerpt="Prima di chiamare uno studio (anche noi), vale la pena rispondere a queste domande. Ti fanno risparmiare tempo e budget.",
       body="""<p>Ci scrivono spesso aziende convinte di aver bisogno di un logo nuovo. A volte è vero, a volte serve altro. Queste sono le domande che facciamo al primo incontro.</p>
<h2>Le domande</h2>
<ol>
<li><b>Cosa non funziona oggi?</b> "È vecchio" non basta. Non si legge sul telefono? Somiglia a un concorrente? Non racconta più cosa fate?</li>
<li><b>Chi deve sceglierti?</b> Un logo piace o non piace a qualcuno in particolare. Descrivi il cliente ideale in tre righe.</li>
<li><b>Dove vivrà il marchio?</b> Insegna, packaging, sito, divise, social. Ogni luogo ha esigenze diverse.</li>
<li><b>Cosa vuoi tenere?</b> Colori, nome, un simbolo amato dai clienti. Rinnovare non vuol dire cancellare.</li>
<li><b>Chi decide?</b> Un progetto con troppi decisori finisce in un compromesso. Meglio due persone che si fidano.</li>
</ol>
<blockquote>Spesso il problema non è il logo, ma come viene usato.</blockquote>
<h2>E se il logo va bene?</h2>
<p>Succede. In quel caso lavoriamo sul sistema intorno: colori, caratteri, regole, fotografie. Costa meno di un rebranding e a volte cambia di più.</p>
<p>Se hai risposto a tutte e cinque, sei pronto per una prima chiamata.</p>"""),
  dict(slug='siti-animati-veloci', title='Animati, ma veloci', cat='Web', date='9 ottobre 2026', mins='4',
       jc='jc-3', jinner='<b>0.9s</b>',
       excerpt="Come facciamo siti con animazioni e scroll fluido senza farli diventare lenti. Qualche regola che seguiamo sempre.",
       body="""<p>Ci piacciono i siti che si muovono. Non ci piacciono quelli che fanno aspettare. Ecco come teniamo insieme le due cose.</p>
<h2>Prima il contenuto, poi il movimento</h2>
<p>Ogni pagina deve essere leggibile anche se le animazioni non partono. Testi e immagini sono nel codice dall'inizio: il movimento arriva dopo, come un livello in più, mai come condizione per vedere qualcosa.</p>
<h2>Poche librerie, scelte bene</h2>
<p>Usiamo GSAP per le animazioni e Lenis per lo scroll fluido. Sono leggere, stabili e ben documentate. Niente framework pesanti per una pagina che deve solo raccontare un brand.</p>
<blockquote>Un'animazione deve aiutare a capire, non a far passare il tempo.</blockquote>
<h2>Rispetto per chi guarda</h2>
<p>Se una persona ha attivato "riduci movimento" sul proprio telefono o computer, il sito lo rispetta e mostra tutto subito. Controlliamo anche i telefoni meno recenti e le connessioni lente, non solo i monitor dello studio.</p>
<h2>Misurare</h2>
<p>Prima di ogni consegna misuriamo i tempi di caricamento e correggiamo quello che rallenta. Un sito bello che fa aspettare perde visitatori prima ancora di mostrarsi.</p>"""),
]
