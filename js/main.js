  const btnDe=document.getElementById('btn-de'),btnEn=document.getElementById('btn-en'),els=document.querySelectorAll('.i18n');
  function setLang(l){document.documentElement.lang=l;els.forEach(e=>{const v=e.getAttribute('data-'+l);if(v!==null)e.innerHTML=v;});if(btnDe)btnDe.classList.toggle('active',l==='de');if(btnEn)btnEn.classList.toggle('active',l==='en');}
  if(btnDe)btnDe.onclick=()=>setLang('de');
  if(btnEn)btnEn.onclick=()=>setLang('en');

  // meter ticker
  const meterEl=document.getElementById('meter-val');let base=8.40;
  if(meterEl)setInterval(()=>{base+=0.10;if(base>24)base=8.40;meterEl.textContent=base.toFixed(2).replace('.',',')+'\u00A0\u20AC';},900);

  // stars
  const s=document.getElementById('stars');if(s)for(let i=0;i<44;i++){const d=document.createElement('span');d.style.left=Math.random()*100+'%';d.style.top=Math.random()*72+'%';d.style.animationDelay=Math.random()*3+'s';s.appendChild(d);}

  // reveal
  const io=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:0.12});
  document.querySelectorAll('.reveal').forEach(e=>io.observe(e));

  // counters
  function fmt(n,el){const suf=el.dataset.suffix||'';if(el.dataset.fmt==='mio')return(n/1000000).toFixed(1).replace('.',',')+' Mio.';return Math.round(n).toLocaleString('de-DE')+suf;}
  const cio=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){const el=e.target,end=+el.dataset.count,t0=performance.now(),dur=1400;function tick(t){const p=Math.min((t-t0)/dur,1);el.textContent=fmt(end*(0.5-Math.cos(p*Math.PI)/2),el);if(p<1)requestAnimationFrame(tick);}requestAnimationFrame(tick);cio.unobserve(el);}});},{threshold:0.5});
  document.querySelectorAll('[data-count]').forEach(e=>cio.observe(e));

  // faq
  document.querySelectorAll('.fq').forEach(q=>{q.onclick=()=>{const a=q.nextElementSibling,open=q.classList.contains('open');document.querySelectorAll('.fq').forEach(o=>{o.classList.remove('open');o.nextElementSibling.style.maxHeight=null;});if(!open){q.classList.add('open');a.style.maxHeight=a.scrollHeight+'px';}};});

  // booking tabs
  document.querySelectorAll('.tab').forEach(t=>{t.onclick=()=>{document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));t.classList.add('active');const w=document.getElementById('when');if(t.dataset.tab==='later'){w.classList.add('show');}else{w.classList.remove('show');}};});

  // swap
  const swapBtn=document.getElementById('swap');
  if(swapBtn)swapBtn.onclick=()=>{const f=document.getElementById('from'),tt=document.getElementById('to'),tmp=f.value;f.value=tt.value;tt.value=tmp;};

  // passengers
  let pax=2;const paxEl=document.getElementById('pax');
  const minusBtn=document.getElementById('minus'),plusBtn=document.getElementById('plus');
  if(minusBtn)minusBtn.onclick=()=>{if(pax>1)pax--;paxEl.textContent=pax;};
  if(plusBtn)plusBtn.onclick=()=>{if(pax<8)pax++;paxEl.textContent=pax;};

  // fare calc (real Hamburg 2025 tariff)
  const calcBtn=document.getElementById('calc');
  if(calcBtn)calcBtn.onclick=()=>{
    const cls=document.getElementById('cls').value;
    const isVan = cls === 'van';
    const isBiz = cls === 'business';
    const baseFare = 4.50 + (isVan ? 8.00 : (isBiz ? 3.50 : 0));
    const km=14+Math.round(Math.random()*4); // Simulate 14-18 km ride
    
    // Calculate accurate taximeter price
    const kmRate = isBiz ? 1.3 : 1;
    let kmPrice = 0;
    if (km <= 9) {
      kmPrice = km * 2.70 * kmRate;
    } else {
      kmPrice = ((9 * 2.70) + ((km - 9) * 2.00)) * kmRate;
    }
    const taximeterPrice = baseFare + kmPrice;
    
    // Price corridor (-20% to +20%) for App Festpreis
    const low = taximeterPrice * 0.80;
    const high = taximeterPrice * 1.20;
    
    const f=n=>n.toFixed(2).replace('.',',')+' €';
    const fareAmtEl = document.getElementById('fare-amt');
    fareAmtEl.textContent=f(low)+' – '+f(high);
    fareAmtEl.dataset.low = low.toFixed(2);
    fareAmtEl.dataset.high = high.toFixed(2);
    document.getElementById('mfare').textContent='ab '+f(low);
    const a=document.querySelector('.fare .amt');a.style.transition='none';a.style.opacity='.3';requestAnimationFrame(()=>{a.style.transition='opacity .5s';a.style.opacity='1';});
    if(typeof applyLoyaltyDiscount === 'function') applyLoyaltyDiscount();
    if(typeof resetPromo === 'function') resetPromo();
    if(typeof updateSplitDisplay === 'function') updateSplitDisplay();
  };

  // ===== Saved places, promo code, fare split, ride history (competitor-inspired) =====
  document.querySelectorAll('.chip-place').forEach(function(chip){
    chip.addEventListener('click', function(){
      const toEl = document.getElementById('to');
      if(toEl) toEl.value = chip.dataset.fill;
      document.querySelectorAll('.chip-place').forEach(function(c){ c.style.borderColor=''; c.style.color=''; });
      chip.style.borderColor = 'var(--amber)';
      chip.style.color = 'var(--amber-2)';
    });
  });

  function currentFareValues(){
    const el = document.getElementById('fare-amt');
    if(!el) return {low:0, high:0};
    return { low: parseFloat(el.dataset.low)||0, high: parseFloat(el.dataset.high)||0 };
  }
  function resetPromo(){
    const input = document.getElementById('promoInput'), btn = document.getElementById('promoBtn'), msg = document.getElementById('promoMsg');
    if(input){ input.disabled = false; input.value=''; }
    if(btn){ btn.disabled = false; }
    if(msg){ msg.textContent=''; msg.className='promo-msg'; }
  }
  const promoBtn = document.getElementById('promoBtn');
  if(promoBtn) promoBtn.onclick = function(){
    const input = document.getElementById('promoInput'), msg = document.getElementById('promoMsg');
    const code = (input.value || '').trim().toUpperCase();
    if(!code) return;
    if(code === 'BLITZ10'){
      const fv = currentFareValues();
      if(fv.high > 0){
        const newLow = fv.low * 0.9, newHigh = fv.high * 0.9;
        const f2=n=>n.toFixed(2).replace('.',',')+' €';
        const el = document.getElementById('fare-amt');
        el.textContent = f2(newLow)+' – '+f2(newHigh);
        el.dataset.low = newLow.toFixed(2);
        el.dataset.high = newHigh.toFixed(2);
        document.getElementById('mfare').textContent = 'ab '+f2(newLow);
      }
      msg.textContent = (document.documentElement.lang === 'en' ? '✓ 10% discount applied' : '✓ 10% Rabatt angewendet');
      msg.className = 'promo-msg ok';
      input.disabled = true;
      promoBtn.disabled = true;
      updateSplitDisplay();
    } else {
      msg.textContent = (document.documentElement.lang === 'en' ? 'Invalid code' : 'Code ungültig');
      msg.className = 'promo-msg err';
    }
  };

  let splitCount = 2;
  function updateSplitDisplay(){
    const per = document.getElementById('splitPerPerson');
    if(!per) return;
    const fv = currentFareValues();
    const total = fv.high || 0;
    const perPerson = splitCount > 0 ? total / splitCount : total;
    per.textContent = '≈ '+perPerson.toFixed(2).replace('.',',')+' € / '+(document.documentElement.lang==='en' ? 'person' : 'Person');
  }
  const splitToggle = document.getElementById('splitToggle');
  const splitDetailEl = document.getElementById('splitDetail');
  if(splitToggle) splitToggle.onchange = function(){
    if(splitDetailEl) splitDetailEl.classList.toggle('show', splitToggle.checked);
    updateSplitDisplay();
  };
  const splitCountEl = document.getElementById('splitCount');
  const splitMinus = document.getElementById('splitMinus'), splitPlus = document.getElementById('splitPlus');
  if(splitMinus) splitMinus.onclick = function(){ if(splitCount>2){ splitCount--; splitCountEl.textContent=splitCount; updateSplitDisplay(); } };
  if(splitPlus) splitPlus.onclick = function(){ if(splitCount<6){ splitCount++; splitCountEl.textContent=splitCount; updateSplitDisplay(); } };

  const historyToggle = document.getElementById('historyToggle');
  const historyPanel = document.getElementById('historyPanel');
  if(historyToggle) historyToggle.onclick = function(){ historyPanel.classList.toggle('open'); };

  function addHistoryEntry(from, to, priceText, rating){
    const list = document.getElementById('historyList');
    const countEl = document.getElementById('historyCount');
    if(!list) return;
    const item = document.createElement('div');
    item.className = 'history-item';
    const stars = rating > 0 ? '★'.repeat(rating) + '☆'.repeat(5-rating) : '—';
    const now = new Date();
    const dateStr = now.toLocaleDateString('de-DE') + ' · ' + now.toLocaleTimeString('de-DE', {hour:'2-digit', minute:'2-digit'});
    item.innerHTML = '<div class="hroute"><b>'+from+' → '+to+'</b><span class="hmeta">'+dateStr+'</span></div><span class="hstars">'+stars+'</span><span class="hprice">'+priceText+'</span>';
    list.insertBefore(item, list.firstChild);
    if(countEl){
      const n = list.querySelectorAll('.history-item').length;
      countEl.textContent = '(' + n + ')';
    }
  }

  // ===== 90-day advance booking window =====
  (function(){
    const whenInput = document.querySelector('#when input[type="datetime-local"]');
    if(whenInput){
      const maxD = new Date();
      maxD.setDate(maxD.getDate() + 90);
      whenInput.max = maxD.toISOString().slice(0,16);
    }
  })();

  // ===== Package tab toggle =====
  document.querySelectorAll('.tab').forEach(function(t){
    t.addEventListener('click', function(){
      const packageBox = document.getElementById('packageBox');
      if(packageBox) packageBox.classList.toggle('show', t.dataset.tab === 'package');
    });
  });

  // ===== Flight status check (mock) =====
  const flightCheckBtn = document.getElementById('flightCheckBtn');
  if(flightCheckBtn) flightCheckBtn.onclick = function(){
    const input = document.getElementById('flightNo'), msg = document.getElementById('flightStatus');
    const code = (input.value || '').trim().toUpperCase();
    if(!code) return;
    const lang = document.documentElement.lang;
    const onTime = Math.random() > 0.3;
    if(onTime){
      msg.textContent = lang === 'en' ? 'On time — pickup planned accordingly' : 'Pünktlich — Abholung entsprechend geplant';
      msg.className = 'promo-msg ok';
    } else {
      const delay = 10 + Math.floor(Math.random()*35);
      msg.textContent = (lang === 'en' ? 'Delayed by ~' : 'Verspätung von ca. ') + delay + (lang === 'en' ? ' min — we adjust automatically' : ' Min. — wir passen automatisch an');
      msg.className = 'promo-msg';
      msg.style.color = 'var(--amber-2)';
    }
  };

  // ===== Blitz Plus loyalty club =====
  let loyaltyActive = false;
  let loyaltyTotalSaved = 0;
  function updateLoyaltyUI(){
    const badge = document.getElementById('loyaltyBadge');
    const btnLbl = document.getElementById('loyaltyBtnLabel');
    const savedEl = document.getElementById('loyaltySaved');
    const lang = document.documentElement.lang;
    if(badge){
      badge.classList.toggle('active', loyaltyActive);
      const span = badge.querySelector('span');
      if(span){
        span.setAttribute('data-de', loyaltyActive ? '✓ Blitz Plus Mitglied' : 'Noch kein Mitglied');
        span.setAttribute('data-en', loyaltyActive ? '✓ Blitz Plus member' : 'Not a member yet');
        span.textContent = span.getAttribute('data-' + lang) || span.getAttribute('data-de');
      }
    }
    if(btnLbl){
      btnLbl.setAttribute('data-de', loyaltyActive ? 'Mitgliedschaft aktiv' : 'Blitz Plus beitreten');
      btnLbl.setAttribute('data-en', loyaltyActive ? 'Membership active' : 'Join Blitz Plus');
      btnLbl.textContent = btnLbl.getAttribute('data-' + lang) || btnLbl.getAttribute('data-de');
    }
    if(savedEl) savedEl.textContent = loyaltyTotalSaved.toFixed(2).replace('.',',') + ' €';
  }
  const loyaltyJoinBtn = document.getElementById('loyaltyJoinBtn');
  if(loyaltyJoinBtn) loyaltyJoinBtn.onclick = function(){
    loyaltyActive = !loyaltyActive;
    updateLoyaltyUI();
  };
  function applyLoyaltyDiscount(){
    if(!loyaltyActive) return;
    const el = document.getElementById('fare-amt');
    if(!el) return;
    const low = parseFloat(el.dataset.low)||0, high = parseFloat(el.dataset.high)||0;
    if(!high) return;
    const newLow = low*0.95, newHigh = high*0.95;
    loyaltyTotalSaved += (high-newHigh);
    const f2=n=>n.toFixed(2).replace('.',',')+' €';
    el.textContent = f2(newLow)+' – '+f2(newHigh);
    el.dataset.low = newLow.toFixed(2);
    el.dataset.high = newHigh.toFixed(2);
    document.getElementById('mfare').textContent = 'ab '+f2(newLow);
    updateLoyaltyUI();
  }

  // ===== CO2 savings dashboard (all-electric fleet) =====
  let co2SavedTotal = 0;
  function addCo2Saving(){
    co2SavedTotal += 1.8 + Math.random()*1.4;
    const el = document.getElementById('historyCo2');
    if(el){
      const lang = document.documentElement.lang;
      const label = lang === 'en' ? 'CO₂ saved: ' : 'CO₂ gespart: ';
      el.textContent = label + co2SavedTotal.toFixed(1).replace('.',',') + ' kg';
    }
  }

  // ===== AI support chatbot (canned demo responses) =====
  (function(){
    const fab = document.getElementById('chatbotFab');
    const panel = document.getElementById('chatbotPanel');
    const log = document.getElementById('chatbotLog');
    const input = document.getElementById('chatbotInput');
    const sendBtn = document.getElementById('chatbotSend');
    const closeBtn = document.getElementById('chatbotClose');
    if(!fab || !panel || !log) return;

    const REPLIES = {
      preis: {de:'Unsere Preise sind transparent: Standard-Taxi ab 4,50 € Grundpreis plus 2,70 €/km. Nutzen Sie den Preisrechner oben für Ihre genaue Strecke.', en:'Our prices are transparent: standard taxi from a €4.50 base fare plus €2.70/km. Use the calculator above for your exact route.'},
      gepaeck: {de:'Normales Gepäck ist kostenlos. Für viel Gepäck empfehlen wir unser Großraum-Taxi — einfach bei der Buchung auswählen.', en:'Regular luggage is free. For lots of luggage, we recommend our large-capacity taxi — just select it when booking.'},
      kindersitz: {de:'Klar! Aktivieren Sie „Kindersitz“ bei den Ausstattungsoptionen im Buchungsformular, dann bringt Ihr Fahrer einen mit.', en:'Sure! Enable "Child seat" in the equipment options in the booking form and your driver will bring one.'},
      wartezeit: {de:'Die ersten 3 Minuten Wartezeit sind kostenlos, danach werden 38,00 €/Stunde berechnet.', en:'The first 3 minutes of waiting are free, after that €38.00/hour is charged.'},
      fallback: {de:'Danke für Ihre Nachricht! Für alles rund um Buchung, Preise oder Sonderwünsche helfen wir gerne — nutzen Sie auch gern die Vorschläge unten.', en:'Thanks for your message! We are happy to help with anything about booking, pricing or special requests — feel free to use the suggestions below too.'}
    };

    function addMsg(text, who){
      const div = document.createElement('div');
      div.className = 'cb-msg ' + who;
      div.textContent = text;
      log.appendChild(div);
      log.scrollTop = log.scrollHeight;
    }

    let greeted = false;
    function openPanel(){
      panel.classList.add('open');
      if(!greeted){
        greeted = true;
        const lang = document.documentElement.lang;
        addMsg(lang === 'en' ? "Hi! I'm the Blitz Assistant. Ask me about prices, luggage, child seats or wait times." : 'Hallo! Ich bin der Blitz Assistent. Fragen Sie mich zu Preisen, Gepäck, Kindersitzen oder Wartezeiten.', 'bot');
      }
    }
    fab.onclick = function(){
      if(panel.classList.contains('open')){ panel.classList.remove('open'); } else { openPanel(); }
    };
    if(closeBtn) closeBtn.onclick = function(){ panel.classList.remove('open'); };

    function reply(key){
      const lang = document.documentElement.lang === 'en' ? 'en' : 'de';
      const r = REPLIES[key] || REPLIES.fallback;
      setTimeout(function(){ addMsg(r[lang], 'bot'); }, 550);
    }

    function matchKey(text){
      const t = text.toLowerCase();
      if(/preis|kost|euro|€|price|cost/.test(t)) return 'preis';
      if(/gepäck|gepaeck|koffer|luggage|bag/.test(t)) return 'gepaeck';
      if(/kind|kindersitz|child|seat/.test(t)) return 'kindersitz';
      if(/warte|wait/.test(t)) return 'wartezeit';
      return 'fallback';
    }

    document.querySelectorAll('#chatbotSuggest button').forEach(function(btn){
      btn.addEventListener('click', function(){
        const q = btn.dataset.q;
        const span = btn.querySelector('span');
        addMsg(span ? span.textContent : btn.textContent, 'user');
        reply(q);
      });
    });

    function sendFromInput(){
      const text = (input.value || '').trim();
      if(!text) return;
      addMsg(text, 'user');
      reply(matchKey(text));
      input.value = '';
    }
    if(sendBtn) sendBtn.onclick = sendFromInput;
    if(input) input.addEventListener('keydown', function(e){ if(e.key === 'Enter') sendFromInput(); });
  })();

  // cursor glow (desktop only)
  const glow=document.getElementById('glow');
  if(glow){if(matchMedia('(pointer:fine)').matches){window.addEventListener('mousemove',e=>{glow.style.left=e.clientX+'px';glow.style.top=e.clientY+'px';});}else{glow.style.display='none';}}

  // scroll progress
  const prog=document.getElementById('progress');
  if(prog)window.addEventListener('scroll',()=>{const h=document.documentElement,sc=(h.scrollTop)/(h.scrollHeight-h.clientHeight)*100;prog.style.width=sc+'%';},{passive:true});


  // ===== Hero ambient particle system =====
  (function(){
    const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
    const canvas = document.getElementById('heroParticles');
    const scene = document.querySelector('.scene');
    if(!canvas || !scene || reduceMotion) return;
    const ctx = canvas.getContext('2d');
    let w=0,h=0,dpr=Math.min(window.devicePixelRatio||1,2);
    let particles=[];
    let running=false;
    let raf=null;
    let mouseX=0.5, mouseY=0.35;

    function resize(){
      const r = scene.getBoundingClientRect();
      w = Math.max(r.width,1); h = Math.max(r.height,1);
      canvas.width = Math.round(w*dpr); canvas.height = Math.round(h*dpr);
      canvas.style.width = w+'px'; canvas.style.height = h+'px';
      ctx.setTransform(dpr,0,0,dpr,0,0);
    }

    function spawn(y){
      const gold = Math.random() < 0.62;
      return {
        x: Math.random()*w,
        y: y===undefined ? Math.random()*h : y,
        r: 0.6+Math.random()*1.7,
        vy: -(0.10+Math.random()*0.26),
        vx: (Math.random()-0.5)*0.14,
        a: 0.15+Math.random()*0.5,
        tw: Math.random()*Math.PI*2,
        twSpeed: 0.01+Math.random()*0.02,
        color: gold ? '242,179,75' : '127,230,241'
      };
    }

    function makeParticles(){
      const count = w<560 ? 16 : 30;
      particles = Array.from({length:count}, () => spawn());
    }

    function tick(){
      ctx.clearRect(0,0,w,h);
      const px = mouseX*w;
      for(const p of particles){
        p.tw += p.twSpeed;
        const flick = 0.55+Math.sin(p.tw)*0.45;
        const pull = (px-p.x)*0.00004;
        p.x += p.vx+pull;
        p.y += p.vy;
        if(p.y < -6){ Object.assign(p, spawn(h+6)); }
        if(p.x < -6) p.x = w+6;
        if(p.x > w+6) p.x = -6;
        ctx.beginPath();
        ctx.fillStyle = 'rgba('+p.color+','+(p.a*flick).toFixed(3)+')';
        ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
        ctx.fill();
      }
      raf = requestAnimationFrame(tick);
    }

    function start(){ if(running) return; running=true; raf=requestAnimationFrame(tick); }
    function stop(){ running=false; if(raf) cancelAnimationFrame(raf); raf=null; }

    resize(); makeParticles();

    if(window.ResizeObserver){
      const ro = new ResizeObserver(()=>{ resize(); makeParticles(); });
      ro.observe(scene);
    } else {
      window.addEventListener('resize', ()=>{ resize(); makeParticles(); });
    }

    scene.addEventListener('mousemove', e=>{
      const r = scene.getBoundingClientRect();
      mouseX = (e.clientX-r.left)/r.width;
      mouseY = (e.clientY-r.top)/r.height;
    });

    const vio = new IntersectionObserver(es=>{
      es.forEach(e => e.isIntersecting ? start() : stop());
    }, {threshold:0.05});
    vio.observe(scene);
  })();

  // ===== Click particle burst (CTA buttons) =====
  (function(){
    const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
    const canvas = document.getElementById('burstCanvas');
    if(!canvas || reduceMotion) return;
    const ctx = canvas.getContext('2d');
    let dpr = Math.min(window.devicePixelRatio||1,2);
    let particles = [];
    let raf = null;

    function resize(){
      canvas.width = Math.round(innerWidth*dpr);
      canvas.height = Math.round(innerHeight*dpr);
      canvas.style.width = innerWidth+'px';
      canvas.style.height = innerHeight+'px';
      ctx.setTransform(dpr,0,0,dpr,0,0);
    }
    resize();
    window.addEventListener('resize', resize);

    function burst(x,y,color){
      const n = 16;
      for(let i=0;i<n;i++){
        const ang = (Math.PI*2*i)/n + Math.random()*0.4;
        const sp = 1.6+Math.random()*2.6;
        particles.push({
          x, y,
          vx: Math.cos(ang)*sp,
          vy: Math.sin(ang)*sp - 1.1,
          r: 1.4+Math.random()*2.2,
          life: 1,
          decay: 0.018+Math.random()*0.014,
          color
        });
      }
      if(!raf) raf = requestAnimationFrame(tick);
    }

    function tick(){
      ctx.clearRect(0,0,innerWidth,innerHeight);
      particles.forEach(p=>{
        p.vy += 0.055;
        p.x += p.vx; p.y += p.vy;
        p.life -= p.decay;
        const l = Math.max(p.life,0);
        ctx.beginPath();
        ctx.fillStyle = 'rgba('+p.color+','+l.toFixed(3)+')';
        ctx.arc(p.x,p.y,p.r*l,0,Math.PI*2);
        ctx.fill();
      });
      particles = particles.filter(p=>p.life>0);
      if(particles.length){ raf = requestAnimationFrame(tick); } else { raf = null; }
    }

    document.addEventListener('click', e=>{
      const btn = e.target.closest('.btn-gold, .btn-volt');
      if(!btn) return;
      const color = btn.classList.contains('btn-volt') ? '55,210,230' : '242,179,75';
      burst(e.clientX, e.clientY, color);
    });
  })();

  // ===== Cookie consent banner =====
  (function(){
    const banner = document.getElementById('cookieBanner');
    if(!banner) return;
    let consent = null;
    try{ consent = localStorage.getItem('blitzTaxiCookieConsent'); }catch(e){}
    if(!consent){ setTimeout(()=>banner.classList.add('show'), 900); }
    const acceptBtn = document.getElementById('cookieAcceptAll');
    const essentialBtn = document.getElementById('cookieEssentialOnly');
    function hide(choice){
      banner.classList.remove('show');
      try{ localStorage.setItem('blitzTaxiCookieConsent', choice); }catch(e){}
    }
    if(acceptBtn) acceptBtn.onclick=()=>hide('all');
    if(essentialBtn) essentialBtn.onclick=()=>hide('essential');
  })();

  // ===== Ride request flow (customer booking -> driver dispatch demo) =====
  (function(){
    const reqBtn = document.getElementById('requestBtn');
    const overlay = document.getElementById('reqOverlay');
    if(!reqBtn || !overlay) return;

    const nameField = document.getElementById('fieldName');
    const phoneField = document.getElementById('fieldPhone');
    const nameInput = document.getElementById('custName');
    const phoneInput = document.getElementById('custPhone');

    const stageSearch = document.getElementById('reqStageSearch');
    const stageFound = document.getElementById('reqStageFound');
    const stageScheduled = document.getElementById('reqStageScheduled');
    const stageRating = document.getElementById('reqStageRating');

    let currentFrom = '', currentTo = '', currentDriverName = '';
    let selectedRating = 0;

    const DRIVERS = [
      {name:'Mustafa Yilmaz', car:'NIO ET7 · HH-BT 2026', rating:'4.9', gender:'m'},
      {name:'Sven Brandt', car:'NIO ET7 · HH-BT 3350', rating:'4.8', gender:'m'},
      {name:'Elif Kaya', car:'NIO ET7 · HH-BT 4410', rating:'5.0', gender:'f'}
    ];
    const favoriteDrivers = new Set();
    function pickDriver(){
      const femaleToggle = document.getElementById('prefFemaleDriver');
      const wantFemale = !!(femaleToggle && femaleToggle.checked);
      let pool = DRIVERS.slice();
      if(wantFemale){
        const females = pool.filter(function(d){ return d.gender === 'f'; });
        if(females.length) pool = females;
      }
      if(favoriteDrivers.size){
        const favs = pool.filter(function(d){ return favoriteDrivers.has(d.name); });
        if(favs.length) pool = favs;
      }
      return pool[Math.floor(Math.random()*pool.length)];
    }
    function pinCode(){
      return String(Math.floor(1000 + Math.random()*9000));
    }

    function initials(n){ return n.split(' ').map(function(p){ return p.charAt(0); }).join('').toUpperCase(); }
    function refNo(){ return 'BTX-' + Math.floor(100000 + Math.random()*900000); }

    function showStage(el){
      [stageSearch, stageFound, stageScheduled, stageRating].forEach(function(s){ if(s) s.style.display = 'none'; });
      if(el) el.style.display = 'block';
    }

    function isLaterTab(){
      const activeTab = document.querySelector('.tab.active');
      return !!(activeTab && activeTab.dataset.tab === 'later');
    }

    function isPackageTab(){
      const activeTab = document.querySelector('.tab.active');
      return !!(activeTab && activeTab.dataset.tab === 'package');
    }

    function closeOverlay(){
      overlay.classList.remove('open');
      overlay.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }

    let progressTimer = null;
    function animateProgress(){
      const fill = document.getElementById('reqProgressFill');
      if(!fill) return;
      fill.style.width = '0%';
      let pct = 0;
      clearInterval(progressTimer);
      progressTimer = setInterval(function(){
        pct = Math.min(pct + 8, 100);
        fill.style.width = pct + '%';
        if(pct >= 100) clearInterval(progressTimer);
      }, 900);
    }

    let etaTimer = null;
    function animateEta(initialMinutes){
      const liveEta = document.getElementById('reqLiveEta');
      const etaVal = document.getElementById('reqEtaVal');
      if(!liveEta) return;
      let pct = 0;
      clearInterval(etaTimer);
      const unit = document.documentElement.lang === 'en' ? 'min' : 'Min.';
      const arrivedTxt = document.documentElement.lang === 'en' ? 'Arriving now' : 'Kommt jetzt an';
      etaTimer = setInterval(function(){
        pct = Math.min(pct + 8, 100);
        const remaining = Math.max(0, Math.round(initialMinutes * (1 - pct/100)));
        if(pct >= 100){
          liveEta.textContent = arrivedTxt;
          clearInterval(etaTimer);
        } else {
          liveEta.textContent = remaining + ' ' + unit;
          if(etaVal) etaVal.textContent = remaining;
        }
      }, 900);
    }

    reqBtn.onclick = function(){
      let valid = true;
      if(!nameInput.value.trim()){ nameField.classList.add('invalid'); valid = false; } else { nameField.classList.remove('invalid'); }
      if(!phoneInput.value.trim() || phoneInput.value.trim().length < 6){ phoneField.classList.add('invalid'); valid = false; } else { phoneField.classList.remove('invalid'); }
      if(!valid) return;

      const fromEl = document.getElementById('from'), toEl = document.getElementById('to');
      const from = (fromEl && fromEl.value) || 'Abholort';
      const to = (toEl && toEl.value) || 'Zielort';
      currentFrom = from; currentTo = to;
      const fromMini = document.getElementById('reqFromMini'), toMini = document.getElementById('reqToMini');
      if(fromMini) fromMini.textContent = from;
      if(toMini) toMini.textContent = to;

      overlay.classList.add('open');
      overlay.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';

      if(isLaterTab()){
        const whenInput = document.querySelector('#when input[type=\"datetime-local\"]');
        let label = document.documentElement.lang === 'en' ? 'your requested time' : 'Ihrem gewünschten Termin';
        if(whenInput && whenInput.value){
          const d = new Date(whenInput.value);
          if(!isNaN(d)) label = d.toLocaleString('de-DE', {day:'2-digit', month:'2-digit', hour:'2-digit', minute:'2-digit'}) + ' Uhr';
        }
        const schedTime = document.getElementById('reqSchedTime');
        if(schedTime) schedTime.textContent = label;
        const ref2 = document.getElementById('reqRefNo2');
        if(ref2) ref2.textContent = refNo();
        showStage(stageScheduled);
        return;
      }

      showStage(stageSearch);
      const sub = document.getElementById('reqSearchSub');
      setTimeout(function(){
        if(sub) sub.textContent = document.documentElement.lang === 'en' ? '2 drivers nearby notified…' : '2 Fahrer in der Nähe benachrichtigt…';
      }, 1400);

      setTimeout(function(){
        const d = pickDriver();
        currentDriverName = d.name;
        const elInit = document.getElementById('reqDriverInitials');
        const elName = document.getElementById('reqDriverName');
        const elCar = document.getElementById('reqDriverCar');
        const elRating = document.querySelector('#reqStageFound .req-rating');
        const elEta = document.getElementById('reqEtaVal');
        const elRef = document.getElementById('reqRefNo');
        const etaMinutes = 3 + Math.floor(Math.random()*4);
        if(elInit) elInit.textContent = initials(d.name);
        if(elName) elName.textContent = d.name;
        if(elCar) elCar.textContent = d.car;
        if(elRating) elRating.textContent = d.rating + ' ★';
        if(elEta) elEta.textContent = etaMinutes;
        if(elRef) elRef.textContent = refNo();
        const pinEl = document.getElementById('reqPinCode');
        if(pinEl) pinEl.textContent = pinCode();
        const favBtn = document.getElementById('reqFavBtn');
        if(favBtn) favBtn.classList.toggle('active', favoriteDrivers.has(d.name));
        const extrasNote = document.getElementById('reqExtrasNote');
        if(extrasNote){
          extrasNote.innerHTML = '';
          const lang = document.documentElement.lang;
          const chips = [];
          const wc = document.getElementById('accessWheelchair');
          const cs = document.getElementById('accessChildSeat');
          const pt = document.getElementById('accessPet');
          if(wc && wc.checked) chips.push([lang==='en'?'Wheelchair-accessible':'Rollstuhlgerecht','i-wheelchair']);
          if(cs && cs.checked) chips.push([lang==='en'?'Child seat':'Kindersitz','i-users']);
          if(pt && pt.checked) chips.push([lang==='en'?'Pet friendly':'Haustier','i-paw']);
          chips.forEach(function(c){
            const span = document.createElement('span');
            span.className = 'req-extras-chip';
            span.innerHTML = '<svg class="ic"><use href="#'+c[1]+'"/></svg>'+c[0];
            extrasNote.appendChild(span);
          });
        }
        const pkgNote = document.getElementById('reqPackageNote');
        if(pkgNote) pkgNote.classList.toggle('show', isPackageTab());
        showStage(stageFound);
        animateProgress();
        animateEta(etaMinutes);
        const safetyPanel = document.getElementById('reqSafetyPanel');
        if(safetyPanel) safetyPanel.classList.remove('open');
        const chatPanelReset = document.getElementById('reqChatPanel');
        if(chatPanelReset) chatPanelReset.classList.remove('open');
        const chatLogReset = document.getElementById('reqChatLog');
        if(chatLogReset) chatLogReset.innerHTML = '';
      }, 3400);
    };

    const reqClose = document.getElementById('reqClose');
    const reqDoneBtn = document.getElementById('reqDoneBtn');
    const reqDoneBtn2 = document.getElementById('reqDoneBtn2');
    const reqNewBtn = document.getElementById('reqNewBtn');
    const reqNewBtn2 = document.getElementById('reqNewBtn2');
    if(reqClose) reqClose.onclick = closeOverlay;
    if(reqDoneBtn) reqDoneBtn.onclick = function(){
      const title = document.getElementById('reqRatingTitle');
      if(title && currentDriverName){
        const withTxt = document.documentElement.lang === 'en' ? 'How was your ride with ' : 'Wie war Ihre Fahrt mit ';
        title.textContent = withTxt + currentDriverName + '?';
      }
      selectedRating = 0;
      document.querySelectorAll('#reqStars .rstar').forEach(function(s){ s.classList.remove('filled'); });
      const comment = document.getElementById('reqComment');
      if(comment) comment.value = '';
      showStage(stageRating);
    };
    if(reqDoneBtn2) reqDoneBtn2.onclick = closeOverlay;
    if(reqNewBtn) reqNewBtn.onclick = function(){ closeOverlay(); const f = document.getElementById('from'); if(f) f.focus(); };
    if(reqNewBtn2) reqNewBtn2.onclick = function(){ closeOverlay(); const f = document.getElementById('from'); if(f) f.focus(); };

    document.querySelectorAll('#reqStars .rstar').forEach(function(star){
      star.addEventListener('click', function(){
        selectedRating = parseInt(star.dataset.val, 10) || 0;
        document.querySelectorAll('#reqStars .rstar').forEach(function(s){
          s.classList.toggle('filled', parseInt(s.dataset.val,10) <= selectedRating);
        });
      });
    });

    function finishRating(rating){
      const fv = currentFareValues();
      const priceText = fv.high ? fv.high.toFixed(2).replace('.',',') + ' €' : '—';
      addHistoryEntry(currentFrom || 'Abholort', currentTo || 'Zielort', priceText, rating);
      if(typeof addCo2Saving === 'function') addCo2Saving();
      closeOverlay();
    }
    const reqRatingSendBtn = document.getElementById('reqRatingSendBtn');
    const reqRatingSkipBtn = document.getElementById('reqRatingSkipBtn');
    if(reqRatingSendBtn) reqRatingSendBtn.onclick = function(){ finishRating(selectedRating || 5); };
    if(reqRatingSkipBtn) reqRatingSkipBtn.onclick = function(){ finishRating(0); };

    const reqShareBtn = document.getElementById('reqShareBtn');
    if(reqShareBtn) reqShareBtn.onclick = function(){
      const refEl = document.getElementById('reqRefNo');
      const ref = (refEl && refEl.textContent) || 'BTX-000000';
      const link = 'https://blitztaxi-yildirim.de/live/' + ref;
      const done = function(){
        const lbl = reqShareBtn.querySelector('span');
        const original = lbl ? lbl.textContent : '';
        if(lbl){
          lbl.textContent = document.documentElement.lang === 'en' ? 'Link copied!' : 'Link kopiert!';
          setTimeout(function(){ lbl.textContent = original; }, 2200);
        }
      };
      if(navigator.clipboard && navigator.clipboard.writeText){
        navigator.clipboard.writeText(link).then(done).catch(done);
      } else {
        done();
      }
    };

    const reqSafetyBtn = document.getElementById('reqSafetyBtn');
    const reqSafetyPanel = document.getElementById('reqSafetyPanel');
    if(reqSafetyBtn) reqSafetyBtn.onclick = function(){
      if(reqSafetyPanel) reqSafetyPanel.classList.toggle('open');
    };

    const reqFavBtn = document.getElementById('reqFavBtn');
    if(reqFavBtn) reqFavBtn.onclick = function(){
      if(!currentDriverName) return;
      if(favoriteDrivers.has(currentDriverName)){ favoriteDrivers.delete(currentDriverName); }
      else { favoriteDrivers.add(currentDriverName); }
      reqFavBtn.classList.toggle('active', favoriteDrivers.has(currentDriverName));
    };

    const reqChatBtn = document.getElementById('reqChatBtn');
    const reqChatPanel = document.getElementById('reqChatPanel');
    const reqChatLog = document.getElementById('reqChatLog');
    function addChatMsg(text, who){
      if(!reqChatLog) return;
      const div = document.createElement('div');
      div.className = 'req-chat-msg ' + who;
      div.textContent = text;
      reqChatLog.appendChild(div);
      reqChatLog.scrollTop = reqChatLog.scrollHeight;
    }
    if(reqChatBtn) reqChatBtn.onclick = function(){
      if(reqChatPanel) reqChatPanel.classList.toggle('open');
    };
    document.querySelectorAll('#reqChatPanel .req-chat-quick button').forEach(function(btn){
      btn.addEventListener('click', function(){
        const lang = document.documentElement.lang;
        const msg = lang === 'en' ? btn.dataset.msgEn : btn.dataset.msgDe;
        addChatMsg(msg, 'me');
        setTimeout(function(){
          const driverReplies = lang === 'en'
            ? ['Got it, thanks!', 'On my way!', 'Sure, no problem.']
            : ['Alles klar, danke!', 'Bin unterwegs!', 'Kein Problem.'];
          addChatMsg(driverReplies[Math.floor(Math.random()*driverReplies.length)], 'driver');
        }, 900);
      });
    });
    const reqCallBtn = document.getElementById('reqCallBtn');
    if(reqCallBtn) reqCallBtn.onclick = function(){
      const lbl = reqCallBtn.querySelector('span') || reqCallBtn;
      const original = lbl.textContent;
      lbl.textContent = document.documentElement.lang === 'en' ? 'Calling…' : 'Rufe an…';
      setTimeout(function(){ lbl.textContent = original; }, 1800);
    };
    const reqSosBtn = document.getElementById('reqSosBtn');
    if(reqSosBtn) reqSosBtn.onclick = function(){
      const original = reqSosBtn.textContent;
      reqSosBtn.textContent = document.documentElement.lang === 'en' ? 'Alert sent (demo)' : 'Alarm gesendet (Demo)';
      setTimeout(function(){ reqSosBtn.textContent = original; }, 2600);
    };

    // Swap the CTA label between "request now" and "send advance booking" per active tab
    document.querySelectorAll('.tab').forEach(function(t){
      t.addEventListener('click', function(){
        const lbl = document.getElementById('requestBtnLabel');
        if(!lbl) return;
        if(t.dataset.tab === 'later'){ lbl.setAttribute('data-de','Vorbestellung senden'); lbl.setAttribute('data-en','Send advance booking'); }
        else if(t.dataset.tab === 'package'){ lbl.setAttribute('data-de','Paketversand anfragen'); lbl.setAttribute('data-en','Request package pickup'); }
        else { lbl.setAttribute('data-de','Fahrt jetzt anfragen'); lbl.setAttribute('data-en','Request ride now'); }
        lbl.textContent = lbl.getAttribute('data-' + document.documentElement.lang) || lbl.getAttribute('data-de');
      });
    });
  })();
