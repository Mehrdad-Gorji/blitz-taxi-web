  const btnDe=document.getElementById('btn-de'),btnEn=document.getElementById('btn-en'),els=document.querySelectorAll('.i18n');
  function setLang(l){document.documentElement.lang=l;els.forEach(e=>{const v=e.getAttribute('data-'+l);if(v!==null)e.innerHTML=v;});btnDe.classList.toggle('active',l==='de');btnEn.classList.toggle('active',l==='en');}
  btnDe.onclick=()=>setLang('de');btnEn.onclick=()=>setLang('en');

  // meter ticker
  const meterEl=document.getElementById('meter-val');let base=8.40;
  setInterval(()=>{base+=0.10;if(base>24)base=8.40;meterEl.textContent=base.toFixed(2).replace('.',',')+'\u00A0\u20AC';},900);

  // stars
  const s=document.getElementById('stars');for(let i=0;i<44;i++){const d=document.createElement('span');d.style.left=Math.random()*100+'%';d.style.top=Math.random()*72+'%';d.style.animationDelay=Math.random()*3+'s';s.appendChild(d);}

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
  document.getElementById('swap').onclick=()=>{const f=document.getElementById('from'),tt=document.getElementById('to'),tmp=f.value;f.value=tt.value;tt.value=tmp;};

  // passengers
  let pax=2;const paxEl=document.getElementById('pax');
  document.getElementById('minus').onclick=()=>{if(pax>1)pax--;paxEl.textContent=pax;};
  document.getElementById('plus').onclick=()=>{if(pax<8)pax++;paxEl.textContent=pax;};

  // fare calc (real Hamburg 2025 tariff)
  document.getElementById('calc').onclick=()=>{
    const cls=document.getElementById('cls').value;
    const isVan = cls === 'van';
    const baseFare = 4.50 + (isVan ? 8.00 : 0);
    const km=14+Math.round(Math.random()*4); // Simulate 14-18 km ride
    
    // Calculate accurate taximeter price
    let kmPrice = 0;
    if (km <= 9) {
      kmPrice = km * 2.70;
    } else {
      kmPrice = (9 * 2.70) + ((km - 9) * 2.00);
    }
    const taximeterPrice = baseFare + kmPrice;
    
    // Price corridor (-20% to +20%) for App Festpreis
    const low = taximeterPrice * 0.80;
    const high = taximeterPrice * 1.20;
    
    const f=n=>n.toFixed(2).replace('.',',')+' €';
    document.getElementById('fare-amt').textContent=f(low)+' – '+f(high);
    document.getElementById('mfare').textContent='ab '+f(low);
    const a=document.querySelector('.fare .amt');a.style.transition='none';a.style.opacity='.3';requestAnimationFrame(()=>{a.style.transition='opacity .5s';a.style.opacity='1';});
  };

  // cursor glow (desktop only)
  const glow=document.getElementById('glow');
  if(matchMedia('(pointer:fine)').matches){window.addEventListener('mousemove',e=>{glow.style.left=e.clientX+'px';glow.style.top=e.clientY+'px';});}else{glow.style.display='none';}

  // scroll progress
  const prog=document.getElementById('progress');
  window.addEventListener('scroll',()=>{const h=document.documentElement,sc=(h.scrollTop)/(h.scrollHeight-h.clientHeight)*100;prog.style.width=sc+'%';},{passive:true});