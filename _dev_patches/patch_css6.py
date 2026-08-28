import io

path = "css/style.css"
with io.open(path, "r", encoding="utf-8") as f:
    css = f.read()

MARKER = ".chatbot-fab{"
assert MARKER not in css, "CSS6 already applied"

NEW_BLOCK = """

/* ===== Phase 2 competitor-inspired features (chatbot, loyalty, driver prefs, accessibility, flight, package, PIN, in-ride chat, CO2) ===== */

.prefs-box{background:var(--bg);border:1px solid var(--line-2);border-radius:9px;padding:12px 14px;display:flex;flex-direction:column;gap:2px;}
.prefs-title{font-size:12.5px;color:var(--text-2);font-weight:600;margin-bottom:6px;}
.pref-row{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:6px 0;border-bottom:1px dashed var(--line-2);}
.pref-row:last-child{border-bottom:none;}
.pref-label{display:flex;align-items:center;gap:8px;font-size:12.5px;color:var(--text-2);}
.pref-label svg{color:var(--text-3);flex:0 0 auto;}

.flight-box{background:var(--bg);border:1px solid var(--line-2);border-radius:9px;padding:12px 14px;display:flex;flex-direction:column;gap:2px;}
.flight-hint{font-size:.72rem;color:var(--text-3);margin-top:7px;line-height:1.5;}

.extras-row-2{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:14px;}
@media(max-width:640px){.extras-row-2{grid-template-columns:1fr;}}

.package-box{display:none;background:var(--bg);border:1px solid var(--line-2);border-radius:9px;padding:14px 16px;margin-top:14px;}
.package-box.show{display:block;}
.package-box .brow{display:grid;grid-template-columns:1fr 1fr;gap:12px;}
@media(max-width:640px){.package-box .brow{grid-template-columns:1fr;}}

.req-fav-btn{background:none;border:none;color:var(--line-2);cursor:pointer;padding:4px;flex:0 0 auto;display:flex;align-items:center;margin-right:0;margin-left:auto;}
.req-fav-btn svg{width:19px;height:19px;transition:color .15s,transform .15s;}
.req-fav-btn:hover svg{color:var(--amber-2);}
.req-fav-btn.active svg{color:var(--amber);fill:var(--amber);transform:scale(1.1);}

.req-pin-code{font-family:var(--mono);font-size:1.05rem;font-weight:700;letter-spacing:.14em;color:var(--amber-2);background:rgba(242,179,75,.08);border:1px solid rgba(242,179,75,.28);border-radius:8px;padding:5px 12px;}

.req-extras-note{display:flex;flex-wrap:wrap;gap:7px;margin-top:12px;}
.req-extras-chip{display:inline-flex;align-items:center;gap:5px;background:var(--bg);border:1px solid var(--line-2);border-radius:20px;padding:5px 11px;font-size:11px;color:var(--text-2);font-family:var(--mono);}
.req-extras-chip svg{width:12px;height:12px;color:var(--volt-2);}

.req-package-note{display:none;align-items:center;gap:7px;font-family:var(--mono);font-size:.76rem;color:var(--amber-2);background:rgba(242,179,75,.08);border:1px solid rgba(242,179,75,.28);border-radius:20px;padding:6px 13px;margin-bottom:14px;}
.req-package-note.show{display:inline-flex;}

.req-chat-panel{display:none;margin-top:12px;background:var(--bg);border:1px solid var(--line-2);border-radius:12px;padding:12px;text-align:left;}
.req-chat-panel.open{display:block;}
.req-chat-log{max-height:150px;overflow-y:auto;display:flex;flex-direction:column;gap:7px;margin-bottom:10px;padding-right:2px;}
.req-chat-msg{max-width:80%;padding:7px 11px;border-radius:12px;font-size:12.5px;line-height:1.5;}
.req-chat-msg.me{align-self:flex-end;background:var(--amber);color:#191100;border-bottom-right-radius:3px;}
.req-chat-msg.driver{align-self:flex-start;background:var(--bg-2);border:1px solid var(--line-2);color:var(--text-2);border-bottom-left-radius:3px;}
.req-chat-quick{display:flex;flex-wrap:wrap;gap:6px;}
.req-chat-quick button{background:var(--bg-2);border:1px solid var(--line-2);color:var(--text-2);border-radius:20px;padding:6px 12px;font-size:11.5px;cursor:pointer;font-family:var(--body);transition:border-color .15s,color .15s;}
.req-chat-quick button:hover{border-color:var(--amber);color:var(--amber-2);}

#loyalty .loyalty-card{display:grid;grid-template-columns:1.6fr 1fr;gap:0;background:var(--bg-2);border:1px solid var(--line-2);border-radius:22px;overflow:hidden;margin-top:30px;}
.loyalty-left{padding:38px 40px;}
.loyalty-left h3{font-family:var(--sora);font-size:22px;margin:14px 0 8px;}
.loyalty-left > p{color:var(--text-2);font-size:14px;line-height:1.7;max-width:44ch;}
.loyalty-icon{width:52px;height:52px;border-radius:14px;background:rgba(242,179,75,.12);border:1px solid rgba(242,179,75,.3);display:flex;align-items:center;justify-content:center;color:var(--amber);}
.loyalty-perks{list-style:none;margin:20px 0 26px;padding:0;display:flex;flex-direction:column;gap:10px;}
.loyalty-perks li{display:flex;align-items:center;gap:10px;font-size:13.5px;color:var(--text-2);}
.loyalty-perks li svg{color:var(--amber);flex:0 0 auto;width:17px;height:17px;}
.loyalty-right{background:linear-gradient(160deg,rgba(242,179,75,.1),rgba(55,210,230,.06));border-right:1px solid var(--line-2);padding:38px 34px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;gap:20px;}
.loyalty-tier-badge{font-family:var(--mono);font-size:12px;color:var(--text-3);border:1px solid var(--line-2);border-radius:20px;padding:8px 16px;background:var(--bg);}
.loyalty-tier-badge.active{color:var(--amber-2);border-color:rgba(242,179,75,.4);background:rgba(242,179,75,.08);}
.loyalty-stat{display:flex;flex-direction:column;gap:4px;}
.loyalty-stat b{font-family:var(--mono);font-size:1.8rem;color:var(--volt-2);}
.loyalty-stat span{font-size:11.5px;color:var(--text-3);}
@media(max-width:820px){#loyalty .loyalty-card{grid-template-columns:1fr;}.loyalty-right{border-right:none;border-top:1px solid var(--line-2);}}
@media(max-width:560px){.loyalty-left{padding:28px 24px;}.loyalty-right{padding:28px 24px;}}

.history-head .hco2{font-family:var(--mono);font-size:11px;color:#5FD68A;font-weight:400;margin-right:8px;}

.chatbot-fab{position:fixed;bottom:22px;left:22px;z-index:80;width:56px;height:56px;border-radius:50%;background:var(--amber);color:#191100;border:none;box-shadow:0 8px 24px rgba(242,179,75,.35);cursor:pointer;display:flex;align-items:center;justify-content:center;transition:transform .18s;}
.chatbot-fab:hover{transform:scale(1.06);}
.chatbot-fab svg{width:24px;height:24px;}
.chatbot-fab .cb-dot{position:absolute;top:6px;right:6px;width:10px;height:10px;border-radius:50%;background:#4CAF50;border:2px solid var(--bg);}
.chatbot-panel{position:fixed;bottom:90px;left:22px;z-index:80;width:min(340px,88vw);max-height:min(480px,70vh);background:var(--bg-2);border:1px solid var(--line-2);border-radius:18px;box-shadow:0 20px 60px rgba(0,0,0,.45);display:none;flex-direction:column;overflow:hidden;}
.chatbot-panel.open{display:flex;}
.chatbot-head{display:flex;align-items:center;gap:10px;padding:14px 16px;background:var(--bg-1);border-bottom:1px solid var(--line-2);}
.chatbot-head .cb-avatar{width:32px;height:32px;border-radius:50%;background:rgba(242,179,75,.14);display:flex;align-items:center;justify-content:center;color:var(--amber);flex:0 0 auto;}
.chatbot-head b{font-family:var(--sora);font-size:13.5px;display:block;}
.chatbot-head small{font-family:var(--mono);font-size:10.5px;color:#5FD68A;}
.chatbot-close{margin-right:auto;background:none;border:none;color:var(--text-3);font-size:20px;cursor:pointer;line-height:1;padding:2px 6px;}
.chatbot-log{flex:1;overflow-y:auto;padding:14px 16px;display:flex;flex-direction:column;gap:9px;}
.cb-msg{max-width:82%;padding:9px 12px;border-radius:13px;font-size:12.8px;line-height:1.55;}
.cb-msg.bot{align-self:flex-start;background:var(--bg);border:1px solid var(--line-2);color:var(--text-2);border-bottom-left-radius:3px;}
.cb-msg.user{align-self:flex-end;background:var(--amber);color:#191100;border-bottom-right-radius:3px;}
.chatbot-suggest{display:flex;flex-wrap:wrap;gap:6px;padding:0 16px 12px;}
.chatbot-suggest button{background:var(--bg);border:1px solid var(--line-2);color:var(--text-2);border-radius:20px;padding:6px 11px;font-size:11px;cursor:pointer;font-family:var(--body);transition:border-color .15s,color .15s;}
.chatbot-suggest button:hover{border-color:var(--amber);color:var(--amber-2);}
.chatbot-input-row{display:flex;gap:8px;padding:12px;border-top:1px solid var(--line-2);}
.chatbot-input-row input{flex:1;background:var(--bg);border:1px solid var(--line-2);border-radius:20px;padding:9px 15px;color:var(--text);font-family:var(--body);font-size:12.8px;}
.chatbot-input-row input:focus{outline:none;border-color:var(--amber);}
.chatbot-send{width:36px;height:36px;border-radius:50%;background:var(--amber);border:none;color:#191100;cursor:pointer;display:flex;align-items:center;justify-content:center;flex:0 0 auto;}
.chatbot-send svg{width:16px;height:16px;}
@media(max-width:480px){.chatbot-fab{left:14px;bottom:14px;}.chatbot-panel{left:14px;right:14px;width:auto;bottom:82px;}}
"""

css = css + NEW_BLOCK

with io.open(path, "w", encoding="utf-8") as f:
    f.write(css)

print("CSS6_PATCH_OK", len(css))
