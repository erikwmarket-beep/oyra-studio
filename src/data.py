# Contenuti del sito OYRA. I progetti e gli articoli sono esempi da sostituire con quelli reali.
STAR = '<svg viewBox="0 0 500 564" aria-hidden="true"><use href="#oyra-star"/></svg>'

PROJECTS = [
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
