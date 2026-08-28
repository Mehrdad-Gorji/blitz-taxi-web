import io

path = "js/main.js"
with io.open(path, "r", encoding="utf-8") as f:
    js = f.read()

def do_replace(text, old, new, label):
    n = text.count(old)
    assert n == 1, "anchor not unique (%d matches) for %s" % (n, label)
    return text.replace(old, new, 1)

# 1. Top-level: 90-day booking window, package tab toggle, flight status, loyalty club, CO2 tracking, AI chatbot
js = do_replace(
    js,
    "  // cursor glow (desktop only)",
    '''  // ===== 90-day advance booking window =====
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

  // cursor glow (desktop only)''',
    "top-level-phase2"
)

# 2. calc(): apply loyalty discount before promo/split refresh
js = do_replace(
    js,
    '''    if(typeof resetPromo === 'function') resetPromo();
    if(typeof updateSplitDisplay === 'function') updateSplitDisplay();
  };''',
    '''    if(typeof applyLoyaltyDiscount === 'function') applyLoyaltyDiscount();
    if(typeof resetPromo === 'function') resetPromo();
    if(typeof updateSplitDisplay === 'function') updateSplitDisplay();
  };''',
    "calc-loyalty"
)

# 3. DRIVERS array -> add gender, third driver, favoriteDrivers set, pickDriver(), pinCode()
js = do_replace(
    js,
    '''    const DRIVERS = [
      {name:'Mustafa Yilmaz', car:'NIO ET7 · HH-BT 2026', rating:'4.9'},
      {name:'Sven Brandt', car:'NIO ET7 · HH-BT 3350', rating:'4.8'}
    ];''',
    '''    const DRIVERS = [
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
    }''',
    "drivers-array"
)

# 4. isLaterTab -> add isPackageTab
js = do_replace(
    js,
    '''    function isLaterTab(){
      const activeTab = document.querySelector('.tab.active');
      return !!(activeTab && activeTab.dataset.tab === 'later');
    }''',
    '''    function isLaterTab(){
      const activeTab = document.querySelector('.tab.active');
      return !!(activeTab && activeTab.dataset.tab === 'later');
    }

    function isPackageTab(){
      const activeTab = document.querySelector('.tab.active');
      return !!(activeTab && activeTab.dataset.tab === 'package');
    }''',
    "is-package-tab"
)

# 5. driver match callback: use pickDriver(), set PIN/fav/extras/package badge
js = do_replace(
    js,
    '''      setTimeout(function(){
        const d = DRIVERS[Math.floor(Math.random()*DRIVERS.length)];
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
        showStage(stageFound);
        animateProgress();
        animateEta(etaMinutes);
        const safetyPanel = document.getElementById('reqSafetyPanel');
        if(safetyPanel) safetyPanel.classList.remove('open');
      }, 3400);''',
    '''      setTimeout(function(){
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
      }, 3400);''',
    "driver-match"
)

# 6. finishRating: add CO2 tracking
js = do_replace(
    js,
    '''    function finishRating(rating){
      const fv = currentFareValues();
      const priceText = fv.high ? fv.high.toFixed(2).replace('.',',') + ' €' : '—';
      addHistoryEntry(currentFrom || 'Abholort', currentTo || 'Zielort', priceText, rating);
      closeOverlay();
    }''',
    '''    function finishRating(rating){
      const fv = currentFareValues();
      const priceText = fv.high ? fv.high.toFixed(2).replace('.',',') + ' €' : '—';
      addHistoryEntry(currentFrom || 'Abholort', currentTo || 'Zielort', priceText, rating);
      if(typeof addCo2Saving === 'function') addCo2Saving();
      closeOverlay();
    }''',
    "finish-rating-co2"
)

# 7. favorite + chat button wiring, after safety button wiring
js = do_replace(
    js,
    '''    const reqSafetyBtn = document.getElementById('reqSafetyBtn');
    const reqSafetyPanel = document.getElementById('reqSafetyPanel');
    if(reqSafetyBtn) reqSafetyBtn.onclick = function(){
      if(reqSafetyPanel) reqSafetyPanel.classList.toggle('open');
    };''',
    '''    const reqSafetyBtn = document.getElementById('reqSafetyBtn');
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
    });''',
    "fav-chat-wiring"
)

# 8. CTA label swap: add package tab branch
js = do_replace(
    js,
    '''        if(t.dataset.tab === 'later'){ lbl.setAttribute('data-de','Vorbestellung senden'); lbl.setAttribute('data-en','Send advance booking'); }
        else { lbl.setAttribute('data-de','Fahrt jetzt anfragen'); lbl.setAttribute('data-en','Request ride now'); }''',
    '''        if(t.dataset.tab === 'later'){ lbl.setAttribute('data-de','Vorbestellung senden'); lbl.setAttribute('data-en','Send advance booking'); }
        else if(t.dataset.tab === 'package'){ lbl.setAttribute('data-de','Paketversand anfragen'); lbl.setAttribute('data-en','Request package pickup'); }
        else { lbl.setAttribute('data-de','Fahrt jetzt anfragen'); lbl.setAttribute('data-en','Request ride now'); }''',
    "cta-label-package"
)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(js)

print("MAINJS6_PATCH_OK", len(js))
