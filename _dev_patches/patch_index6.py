import io

path = "index.html"
with io.open(path, "r", encoding="utf-8") as f:
    html = f.read()

def do_replace(text, old, new, label):
    n = text.count(old)
    assert n == 1, "anchor not unique (%d matches) for %s" % (n, label)
    return text.replace(old, new, 1)

# 1. new icon symbols
html = do_replace(
    html,
    '''    <g id="i-play"><path d="M5 3.5 19 12 5 20.5V3.5Z"/></g>''',
    '''    <g id="i-play"><path d="M5 3.5 19 12 5 20.5V3.5Z"/></g>
    <g id="i-chat"><path d="M4 5h16v11H9l-5 4V5Z"/><path d="M8 10h8M8 13h5"/></g>
    <g id="i-box"><path d="M3 8l9-5 9 5-9 5-9-5Z"/><path d="M3 8v9l9 5 9-5V8"/><path d="M12 13v9"/></g>
    <g id="i-paw"><circle cx="7" cy="9" r="2"/><circle cx="12" cy="6.5" r="2"/><circle cx="17" cy="9" r="2"/><path d="M12 12c-4 0-6 2.5-6 5.5S8.5 21 12 21s6-1.5 6-3.5S16 12 12 12Z"/></g>
    <g id="i-wheelchair"><circle cx="9" cy="17" r="4.5"/><path d="M9 17V9h7M9 12h6l4 6"/><circle cx="17" cy="5" r="1.6" fill="currentColor" stroke="none"/></g>
    <g id="i-lock"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></g>
    <g id="i-crown"><path d="M4 18h16l-1-9-4 4-3-6-3 6-4-4-1 9Z"/></g>''',
    "icons"
)

# 2. package tab button
html = do_replace(
    html,
    '''        <button class="tab" data-tab="later"><svg class="ic"><use href="#i-calendar"/></svg> <span class="i18n" data-de="Vorbestellung" data-en="Schedule">Vorbestellung</span></button>''',
    '''        <button class="tab" data-tab="later"><svg class="ic"><use href="#i-calendar"/></svg> <span class="i18n" data-de="Vorbestellung" data-en="Schedule">Vorbestellung</span></button>
        <button class="tab" data-tab="package"><svg class="ic"><use href="#i-box"/></svg> <span class="i18n" data-de="Paket senden" data-en="Send package">Paket senden</span></button>''',
    "package-tab"
)

# 3. green vehicle option
html = do_replace(
    html,
    '''              <option value="business" class="i18n" data-de="Business-Taxi (Mercedes E-Klasse)" data-en="Business Taxi (Mercedes E-Class)">Business-Taxi (Mercedes E-Klasse)</option>
              <option value="van" class="i18n" data-de="Großraum-Taxi (ab 5 Pers.)" data-en="Large Capacity Taxi (5+ pax)">Großraum-Taxi (ab 5 Pers.)</option>''',
    '''              <option value="business" class="i18n" data-de="Business-Taxi (Mercedes E-Klasse)" data-en="Business Taxi (Mercedes E-Class)">Business-Taxi (Mercedes E-Klasse)</option>
              <option value="green" class="i18n" data-de="Öko-Taxi (Elektro, bis 4 Pers.)" data-en="Eco Taxi (Electric, up to 4 pax)">Öko-Taxi (Elektro, bis 4 Pers.)</option>
              <option value="van" class="i18n" data-de="Großraum-Taxi (ab 5 Pers.)" data-en="Large Capacity Taxi (5+ pax)">Großraum-Taxi (ab 5 Pers.)</option>''',
    "green-option"
)

# 4. extras-row-2 + package box, inserted between extras-row close and contactRow
html = do_replace(
    html,
    '''            <div class="split-detail" id="splitDetail">
              <div class="counter"><button type="button" id="splitMinus">−</button><span id="splitCount">2</span><button type="button" id="splitPlus">+</button></div>
              <span class="per-person" id="splitPerPerson">≈ – € / Person</span>
            </div>
          </div>
        </div>
        <div class="brow contact-row" id="contactRow">''',
    '''            <div class="split-detail" id="splitDetail">
              <div class="counter"><button type="button" id="splitMinus">−</button><span id="splitCount">2</span><button type="button" id="splitPlus">+</button></div>
              <span class="per-person" id="splitPerPerson">≈ – € / Person</span>
            </div>
          </div>
        </div>
        <div class="extras-row-2">
          <div class="prefs-box">
            <div class="prefs-title i18n" data-de="Ausstattung &amp; Präferenzen" data-en="Equipment &amp; preferences">Ausstattung &amp; Präferenzen</div>
            <div class="pref-row">
              <span class="pref-label"><svg class="ic" style="width:15px;height:15px;"><use href="#i-wheelchair"/></svg> <span class="i18n" data-de="Rollstuhlgerechtes Fahrzeug" data-en="Wheelchair-accessible vehicle">Rollstuhlgerechtes Fahrzeug</span></span>
              <label class="switch"><input type="checkbox" id="accessWheelchair"><span class="slider"></span></label>
            </div>
            <div class="pref-row">
              <span class="pref-label"><svg class="ic" style="width:15px;height:15px;"><use href="#i-users"/></svg> <span class="i18n" data-de="Kindersitz" data-en="Child seat">Kindersitz</span></span>
              <label class="switch"><input type="checkbox" id="accessChildSeat"><span class="slider"></span></label>
            </div>
            <div class="pref-row">
              <span class="pref-label"><svg class="ic" style="width:15px;height:15px;"><use href="#i-paw"/></svg> <span class="i18n" data-de="Haustier willkommen" data-en="Pet friendly">Haustier willkommen</span></span>
              <label class="switch"><input type="checkbox" id="accessPet"><span class="slider"></span></label>
            </div>
            <div class="pref-row">
              <span class="pref-label"><svg class="ic" style="width:15px;height:15px;"><use href="#i-star"/></svg> <span class="i18n" data-de="Weibliche Fahrerin bevorzugen" data-en="Prefer female driver">Weibliche Fahrerin bevorzugen</span></span>
              <label class="switch"><input type="checkbox" id="prefFemaleDriver"><span class="slider"></span></label>
            </div>
          </div>
          <div class="flight-box">
            <div class="prefs-title i18n" data-de="Flugnummer (optional)" data-en="Flight number (optional)">Flugnummer (optional)</div>
            <div class="promo-box">
              <input type="text" id="flightNo" placeholder="z. B. LH2036" maxlength="10">
              <button type="button" class="btn btn-ghost" id="flightCheckBtn"><span class="i18n" data-de="Status prüfen" data-en="Check status">Status prüfen</span></button>
            </div>
            <div class="promo-msg" id="flightStatus"></div>
            <p class="flight-hint i18n" data-de="Wir gleichen Ihre Abholzeit automatisch mit dem Landezeitpunkt ab." data-en="We automatically align your pickup time with your landing time.">Wir gleichen Ihre Abholzeit automatisch mit dem Landezeitpunkt ab.</p>
          </div>
        </div>
        <div class="package-box" id="packageBox">
          <div class="prefs-title i18n" data-de="Paketdetails" data-en="Package details">Paketdetails</div>
          <div class="brow">
            <div class="field">
              <label class="i18n" data-de="Paketgröße" data-en="Package size">Paketgröße</label>
              <select id="packageSize">
                <option value="s" class="i18n" data-de="Klein (bis 5 kg)" data-en="Small (up to 5 kg)">Klein (bis 5 kg)</option>
                <option value="m" class="i18n" data-de="Mittel (bis 15 kg)" data-en="Medium (up to 15 kg)">Mittel (bis 15 kg)</option>
                <option value="l" class="i18n" data-de="Groß (bis 30 kg)" data-en="Large (up to 30 kg)">Groß (bis 30 kg)</option>
              </select>
            </div>
            <div class="field">
              <label class="i18n" data-de="Empfänger-Telefon" data-en="Recipient phone">Empfänger-Telefon</label>
              <input id="packageRecipient" type="tel" placeholder="+49 1XX XXX XXXX">
            </div>
          </div>
          <p class="flight-hint i18n" data-de="Ihr Fahrer holt das Paket ab und liefert es direkt beim Empfänger." data-en="Your driver picks up the package and delivers it directly to the recipient.">Ihr Fahrer holt das Paket ab und liefert es direkt beim Empfänger.</p>
        </div>
        <div class="brow contact-row" id="contactRow">''',
    "extras-row-2"
)

# 5. CO2 badge in history header
html = do_replace(
    html,
    '''<h4><span class="i18n" data-de="Meine letzten Fahrten" data-en="My recent rides">Meine letzten Fahrten</span> <span class="hcount" id="historyCount">(3)</span></h4>''',
    '''<h4><span class="i18n" data-de="Meine letzten Fahrten" data-en="My recent rides">Meine letzten Fahrten</span> <span class="hcount" id="historyCount">(3)</span> <span class="hco2" id="historyCo2"></span></h4>''',
    "co2-badge"
)

# 6. loyalty section, inserted after #preise closes and before #gebiet
html = do_replace(
    html,
    '''      <div class="pays reveal">
        <span class="lbl i18n" data-de="Zahlung" data-en="Payment">Zahlung</span>
        <div class="chip">Visa</div><div class="chip">Mastercard</div><div class="chip">Amex</div><div class="chip">PayPal</div><div class="chip">Apple Pay</div><div class="chip">Google Pay</div><div class="chip i18n" data-de="Rechnung" data-en="Invoice">Rechnung</div>
      </div>
    </div>
  </section>

  <section id="gebiet">''',
    '''      <div class="pays reveal">
        <span class="lbl i18n" data-de="Zahlung" data-en="Payment">Zahlung</span>
        <div class="chip">Visa</div><div class="chip">Mastercard</div><div class="chip">Amex</div><div class="chip">PayPal</div><div class="chip">Apple Pay</div><div class="chip">Google Pay</div><div class="chip i18n" data-de="Rechnung" data-en="Invoice">Rechnung</div>
      </div>
    </div>
  </section>

  <section id="loyalty">
    <div class="wrap">
      <div class="sec-head reveal">
        <div class="eyebrow i18n" data-de="Mitgliedschaft" data-en="Membership">Mitgliedschaft</div>
        <h2 class="i18n" data-de="Blitz Plus — mehr Vorteile bei jeder Fahrt" data-en="Blitz Plus — more value on every ride">Blitz Plus — mehr Vorteile bei jeder Fahrt</h2>
      </div>
      <div class="loyalty-card reveal">
        <div class="loyalty-left">
          <div class="loyalty-icon"><svg class="ic" style="width:28px;height:28px;"><use href="#i-crown"/></svg></div>
          <h3 class="i18n" data-de="Blitz Plus Mitgliedschaft" data-en="Blitz Plus membership">Blitz Plus Mitgliedschaft</h3>
          <p class="i18n" data-de="9,99 € / Monat — jederzeit kündbar. Für Vielfahrer, Pendler und Firmenkunden." data-en="€9.99 / month — cancel anytime. For frequent riders, commuters and business clients.">9,99 € / Monat — jederzeit kündbar. Für Vielfahrer, Pendler und Firmenkunden.</p>
          <ul class="loyalty-perks">
            <li><svg class="ic"><use href="#i-check"/></svg><span class="i18n" data-de="5% Rabatt auf jede Fahrt" data-en="5% off every ride">5% Rabatt auf jede Fahrt</span></li>
            <li><svg class="ic"><use href="#i-check"/></svg><span class="i18n" data-de="Bevorzugte Fahrervermittlung" data-en="Priority driver matching">Bevorzugte Fahrervermittlung</span></li>
            <li><svg class="ic"><use href="#i-check"/></svg><span class="i18n" data-de="Kostenlose Stornierung bis 5 Min. vorher" data-en="Free cancellation up to 5 min before">Kostenlose Stornierung bis 5 Min. vorher</span></li>
            <li><svg class="ic"><use href="#i-check"/></svg><span class="i18n" data-de="Exklusive Monatsangebote" data-en="Exclusive monthly deals">Exklusive Monatsangebote</span></li>
          </ul>
          <button class="btn btn-gold" id="loyaltyJoinBtn" type="button"><span class="i18n" id="loyaltyBtnLabel" data-de="Blitz Plus beitreten" data-en="Join Blitz Plus">Blitz Plus beitreten</span> <svg class="ic ar"><use href="#i-arrow"/></svg></button>
        </div>
        <div class="loyalty-right">
          <div class="loyalty-tier-badge" id="loyaltyBadge">
            <span class="i18n" data-de="Noch kein Mitglied" data-en="Not a member yet">Noch kein Mitglied</span>
          </div>
          <div class="loyalty-stat"><b id="loyaltySaved">0,00 €</b><span class="i18n" data-de="gespart mit Blitz Plus" data-en="saved with Blitz Plus">gespart mit Blitz Plus</span></div>
        </div>
      </div>
    </div>
  </section>

  <section id="gebiet">''',
    "loyalty-section"
)

# 7. req-package-note before driver card
html = do_replace(
    html,
    '''      <div class="req-badge-ok i18n" data-de="✓ Fahrer gefunden" data-en="✓ Driver found">✓ Fahrer gefunden</div>
      <div class="req-driver-card">''',
    '''      <div class="req-badge-ok i18n" data-de="✓ Fahrer gefunden" data-en="✓ Driver found">✓ Fahrer gefunden</div>
      <div class="req-package-note" id="reqPackageNote"><svg class="ic" style="width:14px;height:14px;"><use href="#i-box"/></svg> <span class="i18n" data-de="Paketzustellung" data-en="Package delivery">Paketzustellung</span></div>
      <div class="req-driver-card">''',
    "package-note"
)

# 8. favorite button inside driver card
html = do_replace(
    html,
    '''        <div class="req-eta"><span id="reqEtaVal">4</span><small class="i18n" data-de="Min." data-en="min">Min.</small></div>
      </div>
      <div class="req-livemap" id="reqLiveMap">''',
    '''        <div class="req-eta"><span id="reqEtaVal">4</span><small class="i18n" data-de="Min." data-en="min">Min.</small></div>
        <button type="button" class="req-fav-btn" id="reqFavBtn" aria-label="Favorit"><svg class="ic"><use href="#i-star"/></svg></button>
      </div>
      <div class="req-livemap" id="reqLiveMap">''',
    "fav-button"
)

# 9. extras note between livemap and tools
html = do_replace(
    html,
    '''        <div class="rlm-eta"><span class="i18n" data-de="Ankunft in" data-en="Arrives in">Ankunft in</span> <b id="reqLiveEta">4 Min.</b></div>
      </div>
      <div class="req-tools">''',
    '''        <div class="rlm-eta"><span class="i18n" data-de="Ankunft in" data-en="Arrives in">Ankunft in</span> <b id="reqLiveEta">4 Min.</b></div>
      </div>
      <div class="req-extras-note" id="reqExtrasNote"></div>
      <div class="req-tools">''',
    "extras-note"
)

# 10. chat button + chat panel
html = do_replace(
    html,
    '''        <button class="btn btn-ghost" id="reqSafetyBtn" type="button"><svg class="ic" style="width:15px;height:15px;"><use href="#i-shield"/></svg> <span class="i18n" data-de="Sicherheit" data-en="Safety">Sicherheit</span></button>
      </div>
      <div class="req-safety-panel" id="reqSafetyPanel">''',
    '''        <button class="btn btn-ghost" id="reqSafetyBtn" type="button"><svg class="ic" style="width:15px;height:15px;"><use href="#i-shield"/></svg> <span class="i18n" data-de="Sicherheit" data-en="Safety">Sicherheit</span></button>
        <button class="btn btn-ghost" id="reqChatBtn" type="button"><svg class="ic" style="width:15px;height:15px;"><use href="#i-chat"/></svg> <span class="i18n" data-de="Chat" data-en="Chat">Chat</span></button>
      </div>
      <div class="req-chat-panel" id="reqChatPanel">
        <div class="req-chat-log" id="reqChatLog"></div>
        <div class="req-chat-quick">
          <button type="button" data-msg-de="Ich bin unten." data-msg-en="I'm downstairs."><span class="i18n" data-de="Ich bin unten" data-en="I'm downstairs">Ich bin unten</span></button>
          <button type="button" data-msg-de="Bin in 5 Minuten da." data-msg-en="I'll be there in 5 minutes."><span class="i18n" data-de="5 Min. noch" data-en="5 min more">5 Min. noch</span></button>
          <button type="button" data-msg-de="Bitte kurz hupen." data-msg-en="Please honk briefly."><span class="i18n" data-de="Bitte hupen" data-en="Please honk">Bitte hupen</span></button>
        </div>
      </div>
      <div class="req-safety-panel" id="reqSafetyPanel">''',
    "chat-panel"
)

# 11. PIN row as first row inside safety panel
html = do_replace(
    html,
    '''      <div class="req-safety-panel" id="reqSafetyPanel">
        <div class="req-safety-row">
          <div class="rs-label"><svg class="ic" style="width:16px;height:16px;color:#4CAF50;"><use href="#i-check"/></svg> <span class="i18n" data-de="Fahrzeug &amp; Kennzeichen geprüft" data-en="Vehicle &amp; plate verified">Fahrzeug &amp; Kennzeichen geprüft</span></div>
          <span class="rs-ok">✓ <span class="i18n" data-de="Stimmt überein" data-en="Matches">Stimmt überein</span></span>
        </div>''',
    '''      <div class="req-safety-panel" id="reqSafetyPanel">
        <div class="req-safety-row">
          <div class="rs-label"><svg class="ic" style="width:16px;height:16px;"><use href="#i-lock"/></svg> <b class="i18n" data-de="Ihr Fahrt-PIN" data-en="Your ride PIN">Ihr Fahrt-PIN</b></div>
          <span class="req-pin-code" id="reqPinCode">– – – –</span>
        </div>
        <div class="req-safety-row">
          <div class="rs-label"><svg class="ic" style="width:16px;height:16px;color:#4CAF50;"><use href="#i-check"/></svg> <span class="i18n" data-de="Fahrzeug &amp; Kennzeichen geprüft" data-en="Vehicle &amp; plate verified">Fahrzeug &amp; Kennzeichen geprüft</span></div>
          <span class="rs-ok">✓ <span class="i18n" data-de="Stimmt überein" data-en="Matches">Stimmt überein</span></span>
        </div>''',
    "pin-row"
)

# 12. chatbot widget markup, before the req-overlay
html = do_replace(
    html,
    '''<div class="req-overlay" id="reqOverlay" role="dialog" aria-modal="true" aria-hidden="true">''',
    '''<button class="chatbot-fab" id="chatbotFab" type="button" aria-label="Support-Chat öffnen"><svg class="ic" style="width:24px;height:24px;"><use href="#i-chat"/></svg><span class="cb-dot"></span></button>
<div class="chatbot-panel" id="chatbotPanel" role="dialog" aria-label="Support-Chat">
  <div class="chatbot-head">
    <div class="cb-avatar"><svg class="ic" style="width:17px;height:17px;"><use href="#i-bolt"/></svg></div>
    <div>
      <b>Blitz Assistent</b><br>
      <small class="i18n" data-de="● Online" data-en="● Online">● Online</small>
    </div>
    <button class="chatbot-close" id="chatbotClose" type="button" aria-label="Schließen">&times;</button>
  </div>
  <div class="chatbot-log" id="chatbotLog"></div>
  <div class="chatbot-suggest" id="chatbotSuggest">
    <button type="button" data-q="preis"><span class="i18n" data-de="Preise" data-en="Prices">Preise</span></button>
    <button type="button" data-q="gepaeck"><span class="i18n" data-de="Gepäck" data-en="Luggage">Gepäck</span></button>
    <button type="button" data-q="kindersitz"><span class="i18n" data-de="Kindersitz" data-en="Child seat">Kindersitz</span></button>
    <button type="button" data-q="wartezeit"><span class="i18n" data-de="Wartezeit" data-en="Wait time">Wartezeit</span></button>
  </div>
  <div class="chatbot-input-row">
    <input type="text" id="chatbotInput" placeholder="Nachricht schreiben…" maxlength="200">
    <button class="chatbot-send" id="chatbotSend" type="button" aria-label="Senden"><svg class="ic" style="width:15px;height:15px;color:#191100;"><use href="#i-arrow"/></svg></button>
  </div>
</div>

<div class="req-overlay" id="reqOverlay" role="dialog" aria-modal="true" aria-hidden="true">''',
    "chatbot-widget"
)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("INDEX6_PATCH_OK", len(html))
