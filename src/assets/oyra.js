/* OYRA Studio — script condiviso da tutte le pagine.
   Ogni funzione parte solo se trova i suoi elementi nella pagina. */
(function(){
  var root = document.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var finePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var hasGsap = !!(window.gsap && window.ScrollTrigger && window.SplitText);
  var $ = function(s,c){return (c||document).querySelector(s)};
  var $$ = function(s,c){return [].slice.call((c||document).querySelectorAll(s))};
  var entering = root.classList.contains('entering');
  if (!hasGsap) root.classList.add('js-off');
  if (!hasGsap || reduce) { root.classList.remove('entering'); entering = false; }
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  if (!location.hash) window.scrollTo(0,0);
  addEventListener('beforeunload',function(){window.scrollTo(0,0)});

  /* ---- grana + maschera asterisco ---- */
  (function(){var c=document.createElement('canvas');c.width=c.height=180;var x=c.getContext('2d'),d=x.createImageData(180,180);
    for(var i=0;i<d.data.length;i+=4){var v=Math.random()*255;d.data[i]=d.data[i+1]=d.data[i+2]=v;d.data[i+3]=255}
    x.putImageData(d,0,0);root.style.setProperty('--noise','url('+c.toDataURL()+')');
    var sp=$('#oyra-star path');if(sp)root.style.setProperty('--star-mask','url("data:image/svg+xml,'+encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 564"><path d="'+sp.getAttribute('d')+'"/></svg>')+'")');
  })();

  /* ---- orologio di Milano ---- */
  $$('[data-clock]').forEach(function(el){
    function tick(){try{el.textContent=new Intl.DateTimeFormat('it-IT',{hour:'2-digit',minute:'2-digit',timeZone:'Europe/Rome'}).format(new Date())}catch(e){}}
    tick();setInterval(tick,15000);
  });

  /* ---- toast + copia ---- */
  var toast=$('#toast'),tt;
  function say(t){if(!toast)return;toast.textContent=t;toast.classList.add('on');clearTimeout(tt);tt=setTimeout(function(){toast.classList.remove('on')},2200)}
  $$('[data-copy]').forEach(function(b){b.addEventListener('click',function(){
    var v=b.dataset.copy==='url'?location.href:b.dataset.copy,msg=b.dataset.copyMsg||'Copiato';
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(v).then(function(){say(msg)},function(){say(v)})}else say(v);
  })});

  /* ---- menu mobile ---- */
  var menu=$('#menu'),mb=$('#menu-btn'),hdr=$('#hdr');
  function setMenu(open){if(!menu)return;menu.classList.toggle('open',open);hdr.classList.toggle('menu-open',open);$('#menu-ico').setAttribute('href',open?'#i-close':'#i-menu');if(open)hdr.classList.remove('hide');
    menu.setAttribute('aria-hidden',!open);mb.setAttribute('aria-expanded',open);mb.setAttribute('aria-label',open?'Chiudi il menu':'Apri il menu');if(window.__lenis){open?window.__lenis.stop():window.__lenis.start()}}
  if(menu){
    mb.addEventListener('click',function(){setMenu(!menu.classList.contains('open'))});
    $$('a',menu).forEach(function(a){a.addEventListener('click',function(){setMenu(false)})});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&menu.classList.contains('open')){setMenu(false);mb.focus()}});
    addEventListener('resize',function(){if(innerWidth>900&&menu.classList.contains('open'))setMenu(false)});
  }

  /* ---- testo rotante (stile React Bits RotatingText) ---- */
  var rot=$('#rot');
  if(rot&&hasGsap&&!reduce){
    var rw=[].slice.call(rot.children),ri=0;
    gsap.set(rw.slice(1),{yPercent:110,opacity:1});gsap.set(rw[0],{yPercent:0});
    var fit=function(el,d){var cs=getComputedStyle(rot);gsap.to(rot,{width:el.offsetWidth+parseFloat(cs.paddingLeft)+parseFloat(cs.paddingRight),duration:d,ease:'expo.inOut'})};
    setInterval(function(){var a=rw[ri];ri=(ri+1)%rw.length;var b=rw[ri];
      gsap.to(a,{yPercent:-110,duration:.7,ease:'expo.inOut'});gsap.fromTo(b,{yPercent:110},{yPercent:0,duration:.7,ease:'expo.inOut'});fit(b,.7)},2400);
    if(document.fonts)document.fonts.ready.then(function(){fit(rw[ri],0)});addEventListener('resize',function(){fit(rw[ri],0)});
  }

  /* ---- scintille al clic (React Bits ClickSpark) ---- */
  var cv=$('#sparks');
  function onRed(el){var s=el&&el.closest&&el.closest('[data-header]');return !!(s&&s.dataset.header==='light')}
  if(cv&&!reduce){
    var cx=cv.getContext('2d'),sparks=[],dpr=Math.min(2,window.devicePixelRatio||1);
    var size=function(){cv.width=innerWidth*dpr;cv.height=innerHeight*dpr;cv.style.width=innerWidth+'px';cv.style.height=innerHeight+'px'};
    size();addEventListener('resize',size);
    var draw=function(now){cx.setTransform(dpr,0,0,dpr,0,0);cx.clearRect(0,0,innerWidth,innerHeight);
      sparks=sparks.filter(function(s){var p=(now-s.t)/450;if(p>=1)return false;var e=p*(2-p),d=e*28,l=10*(1-e);
        cx.strokeStyle=s.c;cx.lineWidth=2.2;cx.lineCap='round';cx.beginPath();
        cx.moveTo(s.x+d*Math.cos(s.a),s.y+d*Math.sin(s.a));cx.lineTo(s.x+(d+l)*Math.cos(s.a),s.y+(d+l)*Math.sin(s.a));cx.stroke();return true});
      if(sparks.length)requestAnimationFrame(draw)};
    document.addEventListener('click',function(e){var col=onRed(e.target)?'#EFECD7':'#E11A45',t=performance.now(),was=sparks.length;
      for(var i=0;i<8;i++)sparks.push({x:e.clientX,y:e.clientY,a:i*Math.PI/4,t:t,c:col});if(!was)requestAnimationFrame(draw)});
  }

  /* ---- testo "scramble" sui link del menu ---- */
  var glyphs='OYRA✱#*+/<>01';
  $$('[data-scramble] span').forEach(function(s){var orig=s.textContent,run=null;
    s.parentElement.addEventListener('mouseenter',function(){if(reduce)return;var f=0;cancelAnimationFrame(run);
      (function step(){f++;s.textContent=orig.split('').map(function(ch,i){return i<f/2?ch:glyphs[Math.floor(Math.random()*glyphs.length)]}).join('');
        if(f/2<orig.length)run=requestAnimationFrame(step);else s.textContent=orig})()})});

  /* ---- vista griglia / elenco (pagina progetti) ---- */
  $$('[data-view]').forEach(function(b){b.addEventListener('click',function(){
    $$('[data-view]').forEach(function(o){o.setAttribute('aria-pressed',o===b)});
    $$('.pview').forEach(function(v){v.hidden=v.dataset.pview!==b.dataset.view});
    try{localStorage.setItem('oyra-view',b.dataset.view)}catch(e){}
    if(window.ScrollTrigger)ScrollTrigger.refresh();
  })});
  try{var sv=localStorage.getItem('oyra-view');var vb=sv&&$('[data-view="'+sv+'"]');if(vb&&vb.getAttribute('aria-pressed')!=='true')vb.click()}catch(e){}

  /* ---- moduli (contatti, newsletter) ----
     Se il form ha data-endpoint invia i dati lì (es. Formspree, Netlify Forms, API propria);
     senza endpoint mostra comunque la conferma, così il flusso si può provare. */
  $$('form[data-form]').forEach(function(form){
    form.setAttribute('novalidate','');
    function check(fld){var i=$('input,textarea',fld);if(!i||!i.required&&i.type!=='email')return true;
      var v=i.type==='checkbox'?i.checked:i.value.trim(),ok=!!v,msg=i.dataset.msg||'Campo obbligatorio';
      if(ok&&i.type==='email'&&!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(i.value.trim())){ok=false;msg='Controlla l\'indirizzo email'}
      if(!i.required&&!i.value.trim())ok=true;
      fld.classList.toggle('bad',!ok);var e=$('.err',fld);if(e)e.textContent=ok?'':msg;return ok}
    $$('.fld',form).forEach(function(f){var i=$('input,textarea',f);if(i)i.addEventListener('blur',function(){if(f.classList.contains('bad')||i.value)check(f)})});
    form.addEventListener('submit',function(e){
      e.preventDefault();
      var flds=$$('.fld',form),bad=flds.filter(function(f){return !check(f)});
      if(bad.length){var i=$('input,textarea',bad[0]);if(i)i.focus();say('Controlla i campi evidenziati');return}
      var btn=$('button[type="submit"]',form),label=btn?btn.innerHTML:'';
      function done(){var ok=$(form.dataset.ok);if(ok){form.hidden=true;ok.hidden=false;ok.setAttribute('tabindex','-1');ok.focus();if(window.__lenis)window.__lenis.scrollTo(ok,{offset:-120})}else{say(form.dataset.okMsg||'Fatto, grazie!');form.reset()}}
      var ep=form.dataset.endpoint;
      if(!ep){done();return}
      if(btn){btn.disabled=true;btn.textContent='Invio…'}
      fetch(ep,{method:'POST',body:new FormData(form),headers:{Accept:'application/json'}}).then(function(r){if(!r.ok)throw 0;done()})
        .catch(function(){say('Invio non riuscito: scrivici a ciao@oyra.studio')}).finally(function(){if(btn){btn.disabled=false;btn.innerHTML=label}});
    });
  });

  /* ---- filtri journal (senza GSAP) ---- */
  $$('[data-jfilter]').forEach(function(b){b.addEventListener('click',function(){
    $$('[data-jfilter]').forEach(function(o){o.setAttribute('aria-pressed',o===b)});
    var f=b.dataset.jfilter,n=0;
    $$('.j-grid .j-card').forEach(function(c){var show=f==='all'||c.dataset.cat===f;c.hidden=!show;if(show)n++});
    var em=$('.j-empty');if(em)em.hidden=n>0;
    if(window.ScrollTrigger)ScrollTrigger.refresh();
  })});

  var curtain=$('#curtain');
  if(!hasGsap){var l0=$('#loader');if(l0)l0.remove();return}

  gsap.registerPlugin(ScrollTrigger,SplitText);
  ScrollTrigger.config({ignoreMobileResize:true});
  var fontsReady=Promise.race([document.fonts?document.fonts.ready:Promise.resolve(),new Promise(function(r){setTimeout(r,2500)})]);

  /* ---- Lenis + ScrollTrigger ---- */
  var lenis=null;
  if(window.Lenis&&!reduce){
    lenis=new Lenis({lerp:.1,smoothWheel:true});window.__lenis=lenis;
    lenis.on('scroll',ScrollTrigger.update);
    gsap.ticker.add(function(t){lenis.raf(t*1000)});gsap.ticker.lagSmoothing(0);
  }
  $$('a[href^="#"]').forEach(function(a){a.addEventListener('click',function(e){var id=a.getAttribute('href');if(id.length<2)return;var el=id==='#top'?0:document.querySelector(id);if(el===null)return;e.preventDefault();
    if(lenis)lenis.scrollTo(el,{duration:1.4,offset:el===0?0:-90,easing:function(t){return 1-Math.pow(1-t,4)}});else if(el===0)window.scrollTo(0,0);else el.scrollIntoView()})});

  /* ---- transizione tra pagine ---- */
  if(curtain){
    gsap.set(curtain,{y:0,yPercent:entering?0:100});
    $$('a[href]').forEach(function(a){
      var h=a.getAttribute('href');
      if(!h||h.charAt(0)==='#'||/^(mailto:|tel:|https?:|\/\/)/i.test(h)||a.target||a.hasAttribute('download')||!/\.html(#|$)/.test(h))return;
      a.addEventListener('click',function(e){
        if(e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||e.button)return;
        e.preventDefault();
        try{sessionStorage.setItem('oyra-enter','1')}catch(err){}
        if(reduce){location.href=h;return}
        gsap.fromTo(curtain,{yPercent:100},{yPercent:0,duration:.75,ease:'expo.inOut',onComplete:function(){location.href=h}});
      });
    });
    addEventListener('pageshow',function(e){if(e.persisted){gsap.set(curtain,{yPercent:100});root.classList.remove('entering')}});
  }
  function revealCurtain(cb){
    if(!curtain||!entering){cb&&cb();return}
    curtain.style.animation='none';gsap.set(curtain,{yPercent:0});
    gsap.to(curtain,{yPercent:-100,duration:.9,ease:'expo.inOut',delay:.1,onComplete:function(){root.classList.remove('entering');gsap.set(curtain,{yPercent:100})}});
    gsap.delayedCall(.45,function(){cb&&cb()});
  }

  /* ---- cursore ---- */
  var cursor=$('#cursor');
  if(cursor&&finePointer&&!reduce){
    var qx=gsap.quickTo(cursor,'x',{duration:.35,ease:'power3'}),qy=gsap.quickTo(cursor,'y',{duration:.35,ease:'power3'});
    root.addEventListener('mouseleave',function(){cursor.style.opacity=0});
    addEventListener('pointermove',function(e){cursor.style.opacity=1;qx(e.clientX);qy(e.clientY);cursor.classList.toggle('on-red',onRed(e.target))});
    $$('[data-cursor]').forEach(function(el){
      el.addEventListener('mouseenter',function(){$('#cursor-label').textContent=el.dataset.cursor;cursor.classList.add('big')});
      el.addEventListener('mouseleave',function(){cursor.classList.remove('big')})});
  }

  /* ---- bottoni magnetici (React Bits Magnet) ---- */
  if(finePointer&&!reduce){
    $$('.magnet').forEach(function(el){
      var xT=gsap.quickTo(el,'x',{duration:.6,ease:'elastic.out(1,.4)'}),yT=gsap.quickTo(el,'y',{duration:.6,ease:'elastic.out(1,.4)'});
      el.addEventListener('pointermove',function(e){var r=el.getBoundingClientRect();xT((e.clientX-r.left-r.width/2)*.35);yT((e.clientY-r.top-r.height/2)*.35)});
      el.addEventListener('pointerleave',function(){xT(0);yT(0)})});
  }

  /* ---- card inclinate (React Bits TiltedCard) ---- */
  if(finePointer&&!reduce){
    $$('.card').forEach(function(card){var c=$('.cover',card);
      var rx=gsap.quickTo(c,'rotationX',{duration:.6,ease:'power3'}),ry=gsap.quickTo(c,'rotationY',{duration:.6,ease:'power3'});
      card.addEventListener('pointermove',function(e){var r=c.getBoundingClientRect();ry(((e.clientX-r.left)/r.width-.5)*10);rx(-((e.clientY-r.top)/r.height-.5)*10)});
      card.addEventListener('pointerleave',function(){rx(0);ry(0)})});
  }

  /* ---- anteprima che segue il mouse negli elenchi (stile zajno) ---- */
  var prev=$('#preview'),slot=$('#preview-slot');
  if(prev&&finePointer){
    var covers=$$('.card .cover');
    var px=gsap.quickTo(prev,'x',{duration:.6,ease:'power3'}),py=gsap.quickTo(prev,'y',{duration:.6,ease:'power3'});
    $$('.index').forEach(function(idx){
      idx.addEventListener('pointermove',function(e){px(e.clientX+24);py(e.clientY-prev.offsetHeight/2)});
      $$('.row',idx).forEach(function(row){row.addEventListener('mouseenter',function(){
        var src=covers[+row.dataset.cover];if(!src)return;
        var cl=src.cloneNode(true),w=src.offsetWidth||640,h=src.offsetHeight||496;
        cl.removeAttribute('style');cl.style.width=w+'px';cl.style.height=h+'px';cl.style.transform='scale('+(prev.offsetWidth/w)+')';
        slot.innerHTML='';slot.appendChild(cl);
        gsap.to(prev,{opacity:1,scale:1,rotation:gsap.utils.random(-6,6),duration:.5,ease:'expo.out'})})});
      idx.addEventListener('mouseleave',function(){gsap.to(prev,{opacity:0,scale:.6,duration:.4,ease:'expo.out'})});
    });
  }

  /* ---- filtri progetti: uscita, nuovo layout, entrata ---- */
  var grid=$('#grid'),cards=grid?[].slice.call(grid.children):[],entrances=[],filtering=null;
  function applyFilter(f){
    var vis=0;
    cards.forEach(function(c){var show=f==='all'||c.dataset.cat.split(' ').indexOf(f)>=0;c.classList.toggle('is-hidden',!show);c.classList.toggle('offset',show&&(vis++%2===1))});
    $$('.index .row').forEach(function(r){var c=cards[+r.dataset.cover];r.hidden=!!(c&&c.classList.contains('is-hidden'))});
    $$('[data-count]').forEach(function(n){n.textContent='('+String(vis).padStart(2,'0')+')'});
    ScrollTrigger.refresh();
  }
  $$('.filters button[data-filter]').forEach(function(b){b.addEventListener('click',function(){
    if(b.getAttribute('aria-pressed')==='true')return;
    $$('.filters button[data-filter]').forEach(function(o){o.setAttribute('aria-pressed',o===b)});
    entrances.forEach(function(t){if(t.scrollTrigger)t.scrollTrigger.kill();t.progress(1).kill()});entrances=[];
    if(filtering)filtering.kill();
    var f=b.dataset.filter,shown=cards.filter(function(c){return !c.classList.contains('is-hidden')});
    if(reduce){applyFilter(f);return}
    filtering=gsap.timeline()
      .to(shown,{opacity:0,y:30,duration:.35,ease:'power2.in',stagger:.04})
      .add(function(){applyFilter(f);
        gsap.fromTo(cards.filter(function(c){return !c.classList.contains('is-hidden')}),{opacity:0,y:50},{opacity:1,y:0,duration:.8,ease:'expo.out',stagger:.08,overwrite:true});
      });
  })});

  /* ---- header: colore secondo la sezione, si nasconde scendendo (creato dopo i pin) ---- */
  function setupHeader(){
    var foot=$('.foot');
    $$('[data-header]').forEach(function(sec){
      if(sec.id==='hero'){ScrollTrigger.create({start:-1,end:function(){return innerHeight-40},onToggle:function(s){hdr.classList.toggle('dark',!s.isActive)}});return}
      if(sec===foot){ScrollTrigger.create({trigger:$('main').lastElementChild,start:'bottom 40px',end:'max',onToggle:function(s){if(s.isActive)hdr.classList.toggle('dark',false)}});return}
      ScrollTrigger.create({trigger:sec,start:'top 40px',end:'bottom 40px',onToggle:function(s){if(s.isActive)hdr.classList.toggle('dark',sec.dataset.header==='dark')}});
    });
    var lastY=0;ScrollTrigger.create({start:0,end:'max',onUpdate:function(s){var y=s.scroll();hdr.classList.toggle('hide',y>lastY&&y>400&&!(menu&&menu.classList.contains('open')));lastY=y}});
    ScrollTrigger.sort();
  }
  function setupFooter(){
    var foot=$('.foot');if(!foot)return;
    var mode=function(){foot.classList.toggle('tall',foot.offsetHeight>innerHeight-24)};
    mode();fontsReady.then(function(){mode();ScrollTrigger.refresh()});addEventListener('resize',mode);
  }
  setupFooter();

  if(reduce){var l1=$('#loader');if(l1)l1.remove();setupHeader();return}

  /* ---- scroll velocity marquee (React Bits ScrollVelocity) ---- */
  $$('.v-row').forEach(function(row){
    var span=row.firstElementChild;for(var i=0;i<5;i++)row.appendChild(span.cloneNode(true));
    var dir=+row.dataset.dir,x=0,w=1,meas=function(){w=span.offsetWidth||1};meas();fontsReady.then(meas);addEventListener('resize',meas);
    gsap.ticker.add(function(t,dt){var v=lenis?lenis.velocity:0;var speed=(1+Math.min(Math.abs(v)*.25,8))*(v<0?-1:1);
      x+=dir*speed*dt*.06;if(x<=-w)x+=w;if(x>0)x-=w;gsap.set(row,{x:x})});
  });

  /* ---- titoli e testi ---- */
  fontsReady.then(function(){
    $$('.split').forEach(function(el){
      SplitText.create(el,{type:'lines',mask:'lines',linesClass:'split-line',autoSplit:true,onSplit:function(self){
        if(el.dataset.shown)return;
        return gsap.from(self.lines,{yPercent:110,duration:1.1,ease:'expo.out',stagger:.08,scrollTrigger:{trigger:el,start:'top 88%',once:true,onEnter:function(){el.dataset.shown=1}}})}});
    });
    var man=$('#manifesto-text');
    if(man){
      var sp=SplitText.create(man,{type:'words',wordsClass:'w'});
      gsap.to(sp.words,{opacity:1,ease:'none',stagger:.1,scrollTrigger:{trigger:man,start:'top 80%',end:'bottom 45%',scrub:true}});
      $$('.manifesto .chip').forEach(function(c){gsap.fromTo(c,{scaleX:0},{scaleX:1,ease:'expo.out',duration:1,scrollTrigger:{trigger:c,start:'top 75%'}})});
    }
    ScrollTrigger.refresh();
  });

  /* entrate generiche: data-reveal (gruppi con data-stagger) */
  $$('[data-reveal]').forEach(function(el){
    var kids=el.hasAttribute('data-stagger')?el.children:el;
    gsap.from(kids,{y:60,opacity:0,duration:1.1,ease:'expo.out',stagger:.09,scrollTrigger:{trigger:el,start:'top 88%',once:true}});
  });
  /* asterischi che ruotano con lo scroll */
  $$('[data-spin]').forEach(function(el){
    gsap.to(el,{rotation:+el.dataset.spin||180,ease:'none',scrollTrigger:{trigger:el.closest('section')||el,start:'top bottom',end:'bottom top',scrub:true}});
  });
  /* parallasse leggera */
  $$('[data-speed]').forEach(function(el){
    gsap.to(el,{yPercent:-(+el.dataset.speed||10),ease:'none',scrollTrigger:{trigger:el,start:'top bottom',end:'bottom top',scrub:true}});
  });

  /* ---- home: hero che si chiude in una pillola ---- */
  var mm=gsap.matchMedia();
  if($('#hero')){
    gsap.set('#hero-card',{clipPath:'inset(0% 0% 0% 0% round 0px 0px 0px 0px)'});
    gsap.timeline({scrollTrigger:{trigger:'#hero',start:'top top',end:'bottom top',scrub:true}})
      .to('#hero-card',{clipPath:'inset(0% 3% 9% 3% round 0px 0px 48px 48px)',ease:'none'},0)
      .to('#hero-star',{rotation:180,ease:'none'},0)
      .to('#hero-logo',{yPercent:-18,scale:.94,ease:'none'},0)
      .to('.hero-mid',{yPercent:-30,opacity:.2,ease:'none'},0);
    ScrollTrigger.create({trigger:'#hero',start:'top top',end:'bottom top',pin:true,pinSpacing:false});
  }

  /* ---- home: servizi in scorrimento orizzontale (desktop) ---- */
  if($('#h-wrap')){
    mm.add('(min-width: 701px)',function(){
      var track=$('#h-track'),dist=function(){return track.scrollWidth-innerWidth};
      gsap.to(track,{x:function(){return -dist()},ease:'none',scrollTrigger:{trigger:'#h-wrap',start:'top top',end:function(){return '+='+dist()},pin:true,scrub:1,invalidateOnRefresh:true}});
      $$('.svc .deco').forEach(function(d){gsap.to(d,{rotation:360,ease:'none',scrollTrigger:{trigger:'#h-wrap',start:'top top',end:function(){return '+='+dist()},scrub:true}})});
    });
  }

  /* ---- metodo: carte impilate ---- */
  var steps=$$('.step');
  steps.forEach(function(s,i){if(i===steps.length-1)return;
    gsap.to(s,{scale:.93,ease:'none',scrollTrigger:{trigger:steps[i+1],start:'top bottom',end:'top 100px',scrub:true}})});

  /* ---- entrate di card e righe ---- */
  cards.forEach(function(c){entrances.push(gsap.from(c,{y:80,opacity:0,duration:1.1,ease:'expo.out',scrollTrigger:{trigger:c,start:'top 92%',once:true}}))});
  $$('.row').forEach(function(r){gsap.from(r,{y:30,opacity:0,duration:.9,ease:'expo.out',scrollTrigger:{trigger:r,start:'top 95%',once:true}})});

  /* ---- footer: il logotipo sale ---- */
  var footEl=$('.foot');
  if(footEl){gsap.from('.foot-mark',{yPercent:40,ease:'none',scrollTrigger:{trigger:$('main').lastElementChild,start:'bottom bottom',end:function(){return '+='+footEl.offsetHeight},scrub:true,invalidateOnRefresh:true}})}

  setupHeader();

  /* ---- entrata della pagina ---- */
  var loader=$('#loader');
  if($('#hero')){
    var ht=$('#hero-title .ht');gsap.set(ht,{opacity:0});
    gsap.set('#rot',{scale:0,transformOrigin:'0% 50%'});
    gsap.set('#hero-word',{yPercent:100});gsap.set('#hero-star-in',{scale:0,rotation:-180});
    if(lenis)lenis.stop();
    var intro=function(){
      var hs=SplitText.create(ht,{type:'words',mask:'words'});gsap.set(hs.words,{yPercent:110});gsap.set(ht,{opacity:1});
      return gsap.timeline({defaults:{ease:'expo.out'}})
        .to('#hero-word',{yPercent:0,duration:1.4})
        .to('#hero-star-in',{scale:1,rotation:0,duration:1.6,ease:'elastic.out(1,.55)'},'-=1.2')
        .to(hs.words,{yPercent:0,duration:1.1,stagger:.05},'-=1.4')
        .to('#rot',{scale:1,duration:.9},'-=.8')
        .add(function(){if(lenis)lenis.start();ScrollTrigger.refresh()});
    };
    if(loader&&!entering){
      var o={v:0},count=$('#count');
      var counting=new Promise(function(res){gsap.to(o,{v:100,duration:1.3,ease:'power2.inOut',onUpdate:function(){count.textContent=String(Math.round(o.v)).padStart(3,'0')},onComplete:res})});
      Promise.all([counting,fontsReady]).then(function(){
        gsap.to(loader,{clipPath:'inset(0 0 100% 0)',duration:1,ease:'expo.inOut',onComplete:function(){loader.remove()}});
        gsap.delayedCall(.5,intro);
      });
    }else{
      if(loader)loader.remove();
      fontsReady.then(function(){revealCurtain(intro)});
    }
  }else{
    if(loader)loader.remove();
    var ph=$('.page-title');
    if(ph)gsap.set(ph,{opacity:0});
    fontsReady.then(function(){
      revealCurtain(function(){
        if(ph){var s=SplitText.create(ph,{type:'lines',mask:'lines',linesClass:'split-line'});gsap.set(ph,{opacity:1});
          gsap.from(s.lines,{yPercent:110,duration:1.2,ease:'expo.out',stagger:.09});}
        gsap.from('.page-in',{y:40,opacity:0,duration:1.1,ease:'expo.out',stagger:.08,delay:.25});
        ScrollTrigger.refresh();
      });
    });
  }
})();
