
segment_mapping_dict = {

'Bandhan Nifty 50 - Regular':'Equity: UltraLarge',
'Bandhan Nifty 50':'Equity: UltraLarge',
'HDFC Mid-Cap':'Equity: Midcap',
'HDFC NIFTY Next50':'Equity: Largecap',
'ICICI Prudential Value':'Equity: Value', 
'HDFC Small Cap':'Equity: Smallcap',
'HDFC NIFTY200 Momentum 30':'Equity: Momentum',
# 'SBI Gilt':'Debt: Gilt',
'DSP Nifty 50 Equal Weight':'Equity: UltraLarge',
# 'Nippon India Tax Saver (ELSS)':'Old Inv.',
'Motilal Oswal Nifty Smallcap 250':'Equity: Smallcap',
'Motilal Oswal Nifty Midcap 150':'Equity: Midcap',
# 'SBI Long Term Equity':'Old Inv.',
'Parag Parikh Flexi Cap':'Equity: Flexi/Multi',
'JM Flexicap':'Equity: Flexi/Multi',
'DSP Nifty Top 10 Equal Weight':'Equity: UltraLarge',
# 'Franklin India Focused Equity':'Old Inv.',
'Edelweiss Nifty Midcap150 Momentum 50':'Equity: Momentum',
'UTI Nifty 500 Value 50':'Equity: Value',
'Nippon India Multi Cap':'Equity: Flexi/Multi',
'ICICI Prudential Multi-Asset':'Equity: Hybrid',
# 'Bandhan Nifty Alpha 50':'Equity: Alpha',
'SBI Gold':'Commo: Gold/Silver',
'SBI Contra':'Equity: Value',
'HDFC Balanced Advantage':'Equity: Hybrid',
# 'ICICI Prudential Equity & Debt':'Eq.Hybrid',
# 'Bandhan Small Cap':'Equity:Smallcap',
'SBI Silver':'Commo: Gold/Silver',
'HDFC Silver':'Commo: Gold/Silver',
# 'Navi Nifty Bank':'Sector/Bank',
'Kotak Arbitrage':'Equity: Liquid',
'Franklin US Opportunities':'Equity: US',
'Kotak Nifty Next 50': 'Equity: Largecap',
'Total':'Total'
}
FUNDS = {
   ########### LARGE CAPS #############

    '112877': {
        'Scheme Name': 'Bandhan Nifty 50 - Regular',
        'benchmark_ticker': 'NIFTY 50',
        'Benchmark Name': 'NIFTY 50',
        'units': 10095.428,
    },
    '118482': {
        'Scheme Name': 'Bandhan Nifty 50',
        'benchmark_ticker': 'NIFTY 50',
        'Benchmark Name': 'NIFTY 50',
        'units': 7675.45,
    },
    '148745': {
        'Scheme Name': 'Kotak Nifty Next 50',
        'benchmark_ticker': 'NIFTY NEXT 50',
        'Benchmark Name': 'NIFTY NEXT 50',
        'units': 14271.526,
    },
    '141877': {
        'Scheme Name': 'DSP Nifty 50 Equal Weight',
        'benchmark_ticker': 'NIFTY50 EQL WGT',
        'Benchmark Name': 'NIFTY50 EQUAL WEIGHT',
        'units': 11720.387,
    },
    '152814': {
        'Scheme Name': 'DSP Nifty Top 10 Equal Weight',
        'benchmark_ticker': 'NIFTY TOP 10 EW',
        'Benchmark Name': 'NIFTY TOP 10 EQUAL WEIGHT',
        'units': 30714.276,
    },

########## MID & SMALL CAPS ##########

    '147622': {
        'Scheme Name': 'Motilal Oswal Nifty Midcap 150',
        'benchmark_ticker': 'NIFTY MIDCAP 150',
        'Benchmark Name': 'NIFTY MIDCAP 150',
        'units': 5040.272,
    },
    '147623': {
        'Scheme Name': 'Motilal Oswal Nifty Smallcap 250',
        'benchmark_ticker': 'NIFTY SMLCAP 250',
        'Benchmark Name': 'NIFTY SMALLCAP 250',
        'units': 5546.078,
    },
    '118989': {
        'Scheme Name': 'HDFC Mid-Cap',
        'benchmark_ticker': 'NIFTY MIDCAP 150',
        'Benchmark Name': 'NIFTY MIDCAP 150',
        'units': 1627.281,
    },
    '130503': {
        'Scheme Name': 'HDFC Small Cap',
        'benchmark_ticker': 'NIFTY SMLCAP 250',
        'Benchmark Name': 'NIFTY SMALLCAP 250',
        'units': 1939.401,
    },

########### MOMENTUM ###########

    '152430': {
        'Scheme Name': 'HDFC NIFTY200 Momentum 30',
        'benchmark_ticker': 'NIFTY200MOMENTM30',
        'Benchmark Name': 'NIFTY200 MOMENTUM 30',
        'units': 22669.6530842006,#22190.8230842006 + 478.83/
    },
    '150902': {
        'Scheme Name': 'Edelweiss Nifty Midcap150 Momentum 50',
        'benchmark_ticker': 'NIFTYM150MOMNTM50',
        'Benchmark Name': 'NIFTY MIDCAP150 MOMENTUM 50',
        'units': 5553.464,
    },

########## VALUE  ##########

    '119835': {
        'Scheme Name': 'SBI Contra',
        'benchmark_ticker': 'NIFTY500 VALUE 50',
        'Benchmark Name': 'NIFTY500 VALUE 50',
        'units': 368.852,
    },
    '120323': {
        'Scheme Name': 'ICICI Prudential Value',
        'benchmark_ticker': 'NIFTY500 VALUE 50',
        'Benchmark Name': 'NIFTY500 VALUE 50',
        'units': 393.475,
    },
    '151739': {
        'Scheme Name': 'UTI Nifty 500 Value 50',
        'benchmark_ticker': 'NIFTY500 VALUE 50',
        'Benchmark Name': 'NIFTY500 VALUE 50',
        'units': 9756.788,
    },

######## FLEXI/MULTI CAP  #######

    '118650': {
        'Scheme Name': 'Nippon India Multi Cap',
        'benchmark_ticker': 'NIFTY500 MULTICAP',
        'Benchmark Name': 'NIFTY500 MULTICAP 50:25:25',
        'units': 815.721,
    },
    '122639': {
        'Scheme Name': 'Parag Parikh Flexi Cap',
        'benchmark_ticker': 'CUSTMULT01',
        'Benchmark Name': 'Custom Multi-Asset',
        'units': 3490.444,#3382.352
    },
    '120492': {
        'Scheme Name': 'JM Flexicap',
        'benchmark_ticker': 'NIFTY 500',
        'Benchmark Name': 'NIFTY 500',
        'units': 1684.449,
    },

###### GOLD/SILVER ##########

    '119788': {
        'Scheme Name': 'SBI Gold',
        'benchmark_ticker': 'SETFGOLD',
        'Benchmark Name': 'Gold',
        'units': 11924.354,
    },
    '152735': {
        'Scheme Name': 'SBI Silver',
        'benchmark_ticker': 'SBISILVER',
        'Benchmark Name': 'SBI SILVER ETF',
        'units': 15814.738,
    },
    '150737': {
        'Scheme Name': 'HDFC Silver',
        'benchmark_ticker': 'HDFCSILVER',
        'Benchmark Name': 'HDFC Silver ETF',
        'units': 3249.967,
    },

###### ARBITRAGE ##########

    '119771': {
        'Scheme Name': 'Kotak Arbitrage',
        'benchmark_ticker': 'GROWWLIQID',
        'Benchmark Name': 'Nifty 1D Rate Index',
        'units': 15203.98,
    },

###### GILT ##########

    # '119707': {
    #     'Scheme Name': 'SBI Gilt',
    #     'benchmark_ticker': 'LTGILTBEES',
    #     'Benchmark Name': 'NIFTY 8-13 yr G-Sec Index',
    #     'units': 1513.943,
    # },

###### USA ##########

    '118551': {
        'Scheme Name': 'Franklin US Opportunities',
        'benchmark_ticker': 'LIQUIDBEES',
        'Benchmark Name': 'Government Securities',
        'units': 3959.751,
    },

###### Multi-Asset ##########

    '120334': {
        'Scheme Name': 'ICICI Prudential Multi-Asset',
        'benchmark_ticker': 'CUSTMULT01',
        'Benchmark Name': 'Custom Multi-Asset',
        'units': 367.132,
    },
    '118968': {
        'Scheme Name': 'HDFC Balanced Advantage',
        'benchmark_ticker': 'CUSTMULT01',
        'Benchmark Name': 'Custom Multi-Asset',
        'units': 388.471,
    },
}




# Portfolio Monitor · Dark Theme · Streamlit

# segment_mapping_dict = {
#     'Bandhan Nifty 50':               'Equity: UltraLarge',
#     'HDFC Mid-Cap':                   'Equity: Midcap',
#     'Kotak Nifty Next 50':            'Equity: Largecap',
#     'Parag Parikh Flexi Cap':         'Equity: Flexi/Multi',
#     'Nippon India Multi Cap':         'Equity: Flexi/Multi',
#     'ICICI Prudential Multi-Asset':   'Equity: Hybrid',
#     'HDFC Balanced Advantage':        'Equity: Hybrid',
# }

# FUNDS = {
#     '118482': {'Scheme Name': 'Bandhan Nifty 50',             'benchmark_ticker': 'NIFTY 50',          'Benchmark Name': 'NIFTY 50',                   'units': 500},
#     '148745': {'Scheme Name': 'Kotak Nifty Next 50',          'benchmark_ticker': 'NIFTY NEXT 50',     'Benchmark Name': 'NIFTY NEXT 50',              'units': 500},
#     '118989': {'Scheme Name': 'HDFC Mid-Cap',                 'benchmark_ticker': 'NIFTY MIDCAP 150',  'Benchmark Name': 'NIFTY MIDCAP 150',           'units': 500},
#     '118650': {'Scheme Name': 'Nippon India Multi Cap',       'benchmark_ticker': 'NIFTY500 MULTICAP', 'Benchmark Name': 'NIFTY500 MULTICAP 50:25:25', 'units': 500},
#     '122639': {'Scheme Name': 'Parag Parikh Flexi Cap',       'benchmark_ticker': 'CUSTMULT01',        'Benchmark Name': 'Custom Multi-Asset',         'units': 500},
#     '120334': {'Scheme Name': 'ICICI Prudential Multi-Asset', 'benchmark_ticker': 'CUSTMULT01',        'Benchmark Name': 'Custom Multi-Asset',         'units': 400},
#     '118968': {'Scheme Name': 'HDFC Balanced Advantage',      'benchmark_ticker': 'CUSTMULT01',        'Benchmark Name': 'Custom Multi-Asset',         'units': 300},
# }

THRESHOLDS = {
    'default': {
        'threshold_pct': 5.0,
        'multipliers': {-1.0:10000,-1.5:12000,-2:15000,-2.5:17000,-3.0:20000,-3.5:25000,-4.0:30000},
    },
    'None': {
        'threshold_pct': 0.5,
        'multipliers': {-1:5000,-2:7000},
    },
}

# ── Dynamic colour palette ───────────────────────────────────────────────────
_PALETTE = [
    '#3b82f6','#10b981','#f59e0b','#8b5cf6','#f43f5e','#06b6d4',
    '#84cc16','#f97316','#ec4899','#14b8a6','#a855f7','#eab308',
    '#6366f1','#22c55e','#fb923c','#e879f9','#38bdf8','#4ade80',
    '#fbbf24','#c084fc','#f87171','#34d399','#60a5fa','#a78bfa',
]

def _color_for(name, cache={}):
    if name not in cache:
        cache[name] = _PALETTE[len(cache) % len(_PALETTE)]
    return cache[name]

def seg_color(seg):   return _color_for(f"seg:{seg}")
def fund_color(fund): return _color_for(f"fund:{fund}")

# ── Dark palette constants ───────────────────────────────────────────────────
C_BG      = "#030712"
C_SURFACE = "#0f1923"
C_BORDER  = "rgba(255,255,255,0.07)"
C_BORDER_H= "rgba(255,255,255,0.15)"
C_TEXT    = "#f0f4f8"
C_TEXT2   = "#c4cdd8"
C_MUTED   = "#8b9ab0"
C_DIM     = "#4a5568"
C_TH_BG   = "#111827"
C_TH_COL  = "#5a6a82"
C_GREEN   = "#10b981"
C_RED     = "#f43f5e"
C_GOLD    = "#f59e0b"
C_BLUE    = "#3b82f6"
C_PURPLE  = "#8b5cf6"
C_TOPBAR  = "rgba(3,7,18,0.92)"

# ── Imports ──────────────────────────────────────────────────────────────────
import requests, time, numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Portfolio Monitor", page_icon="📊",
                   layout="wide", initial_sidebar_state="collapsed")

for k, v in {"run_mtm": False, "df_disp": None, "totals": None, "last_updated": None}.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── Global CSS via st.html (never stripped) ──────────────────────────────────
st.html("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
html, body, [class*="stApp"], [class*="block-container"] * {
  font-family: 'DM Sans', sans-serif !important;
  font-size: 15px;
}
[class*="stApp"] { background: #030712 !important; }
[class*="block-container"] { padding-top: 0 !important; max-width: 1300px !important; }
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { display: none; }
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #4a5568; border-radius: 3px; }
[data-testid="stButton"] > button {
  font-family: 'DM Sans', sans-serif !important;
  font-size: 15px !important; font-weight: 600 !important;
  color: white !important;
  background: linear-gradient(135deg, #3b82f6, #6366f1) !important;
  border: none !important; border-radius: 10px !important;
  padding: 9px 22px !important;
  box-shadow: 0 2px 12px rgba(59,130,246,0.3) !important;
  transition: all 0.2s !important;
}
[data-testid="stButton"] > button:hover {
  transform: translateY(-1px) !important;
  box-shadow: 0 4px 22px rgba(59,130,246,0.5) !important;
}
</style>
""")

# ── Data helpers ─────────────────────────────────────────────────────────────
URL_JSON    = "https://www.nseindia.com/api/allIndices"
URL_ETF     = "https://www.nseindia.com/api/etf"
HEADERS_NSE = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json,text/plain,*/*",
}
_session = requests.Session()
_session.headers.update({"User-Agent": "Mozilla/5.0"})


def get_latest_nav(code, retries=2, delay=0.5):
    for attempt in range(retries):
        try:
            r = _session.get(f"https://api.mfapi.in/mf/{code}", timeout=5)
            r.raise_for_status()
            return float(r.json()["data"][0]["nav"])
        except Exception:
            if attempt == retries - 1: raise
            time.sleep(delay)


@st.cache_data(show_spinner=False, ttl=300)
def build_snapshot():
    r_idx = requests.get(URL_JSON, headers=HEADERS_NSE, timeout=5); r_idx.raise_for_status()
    raw = r_idx.json()
    df_idx = pd.json_normalize(raw.get("data") or raw.get("indices") or raw)
    idx_cols = [c for c in ["index","indexSymbol","percentChange"] if c in df_idx.columns]
    df_idx = df_idx[idx_cols].rename(columns={
        "index":"Benchmark Name","indexSymbol":"benchmark_ticker","percentChange":"PctChg"})

    r_etf = requests.get(URL_ETF, headers=HEADERS_NSE, timeout=5); r_etf.raise_for_status()
    raw_e = r_etf.json()
    df_etf = pd.json_normalize(raw_e.get("data") or raw_e.get("etfData") or raw_e)
    etf_cols = [c for c in ["assets","symbol","per"] if c in df_etf.columns]
    df_etf = df_etf[etf_cols].rename(columns={
        "assets":"Benchmark Name","symbol":"benchmark_ticker","per":"PctChg"})

    bmk = pd.concat([df_idx[["Benchmark Name","benchmark_ticker","PctChg"]],
                     df_etf[["Benchmark Name","benchmark_ticker","PctChg"]]],
                    ignore_index=True).dropna(subset=["benchmark_ticker"])

    pct_eq   = pd.to_numeric(str(bmk.loc[bmk["benchmark_ticker"]=="NIFTY 500","PctChg"].iloc[0]).replace("%",""), errors="coerce")
    pct_debt = pd.to_numeric(str(bmk.loc[bmk["benchmark_ticker"]=="LTGILTBEES","PctChg"].iloc[0]).replace("%",""), errors="coerce")
    bmk = pd.concat([bmk, pd.DataFrame([{"Benchmark Name":"Custom Multi-Asset",
        "benchmark_ticker":"CUSTMULT01","PctChg":0.75*pct_eq+0.25*pct_debt}])], ignore_index=True)

    port = pd.DataFrame([{"Scheme Code":sc,"Scheme Name":v["Scheme Name"],
        "Benchmark Name":v["Benchmark Name"],"benchmark_ticker":v["benchmark_ticker"],
        "units":v["units"]} for sc,v in FUNDS.items()])
    port = port.merge(bmk[["Benchmark Name","benchmark_ticker","PctChg"]],
                      on=["Benchmark Name","benchmark_ticker"], how="left")
    port["PctChg"]     = pd.to_numeric(port["PctChg"].astype(str).str.replace("%",""), errors="coerce")
    port["Last NAV"]   = port["Scheme Code"].apply(get_latest_nav)
    port["Last Value"] = port["Last NAV"] * port["units"]
    port["iNAV"]       = port["Last NAV"] * (1 + port["PctChg"]/100.0)
    port["MTM Value"]  = port["iNAV"] * port["units"]
    port["1D P&L"]     = port["MTM Value"] - port["Last Value"]
    port["1D Chg Num"] = port["1D P&L"] / port["Last Value"] * 100.0

    df_disp = port[["Scheme Code","Scheme Name","Benchmark Name",
                    "Last NAV","iNAV","Last Value","MTM Value","1D P&L","1D Chg Num"]].reset_index(drop=True)
    totals = {
        "pv":  float(port["Last Value"].sum()),
        "mtm": float(port["MTM Value"].sum()),
        "pnl": float(port["1D P&L"].sum()),
        "ret": float(port["1D P&L"].sum() / port["Last Value"].sum() * 100),
    }
    return df_disp, totals


def calc_buy_recs(df):
    recs = []
    for _, row in df.iterrows():
        sname = row["Scheme Name"]
        chg   = float(row["1D Chg Num"])
        t     = THRESHOLDS.get(sname, THRESHOLDS["default"])
        if chg <= -t["threshold_pct"]:
            step   = float(np.floor(chg * 2) / 2)   # half-step floors for 0.5-step keys
            avail  = sorted(t["multipliers"].keys())
            chosen = max([k for k in avail if k <= step], default=min(avail))
            recs.append({"name":sname,"chg":chg,"threshold":t["threshold_pct"],
                         "buy_amt":t["multipliers"].get(chosen, 25000)})
    return recs


# ── HTML helpers ─────────────────────────────────────────────────────────────

def sign(v): return "+" if v > 0 else ""


def seg_pill(seg):
    c = seg_color(seg)
    r, g, b = int(c[1:3],16), int(c[3:5],16), int(c[5:7],16)
    return (
        f'<span style="display:inline-flex;align-items:center;font-family:DM Sans,sans-serif;'
        f'font-size:12px;font-weight:600;letter-spacing:0.3px;padding:4px 10px;'
        f'border-radius:20px;white-space:nowrap;color:{c};'
        f'background:rgba({r},{g},{b},0.14);border:1px solid rgba({r},{g},{b},0.38);">{seg}</span>'
    )


def topbar(ts):
    dot = (
        f'<div style="width:8px;height:8px;border-radius:50%;flex-shrink:0;'
        f'background:{C_GREEN};box-shadow:0 0 8px {C_GREEN};'
        f'animation:pm-pulse 2s ease-in-out infinite;"></div>'
    ) if ts not in ("—", "&#8212;") else ""
    return (
        f'<div style="position:sticky;top:0;z-index:999;background:{C_TOPBAR};'
        f'backdrop-filter:blur(20px) saturate(1.8);-webkit-backdrop-filter:blur(20px) saturate(1.8);'
        f'border-bottom:1px solid {C_BORDER};margin-bottom:28px;">'
        f'<style>@keyframes pm-pulse{{0%,100%{{opacity:1;transform:scale(1)}}'
        f'50%{{opacity:0.4;transform:scale(0.75)}}}}</style>'
        f'<div style="max-width:1300px;margin:0 auto;display:flex;align-items:center;'
        f'justify-content:space-between;height:64px;padding:0 14px;">'
        f'<div style="display:flex;align-items:center;gap:11px;font-family:Syne,sans-serif;'
        f'font-size:19px;font-weight:800;letter-spacing:-0.4px;color:{C_TEXT};">'
        f'<div style="width:32px;height:32px;background:linear-gradient(135deg,#3b82f6,#8b5cf6);'
        f'border-radius:8px;display:flex;align-items:center;justify-content:center;'
        f'font-size:15px;box-shadow:0 0 18px rgba(59,130,246,0.38);">&#128202;</div>'
        f'Portfolio Monitor</div>'
        f'<div style="display:flex;align-items:center;gap:8px;font-family:DM Mono,monospace;'
        f'font-size:13px;color:{C_DIM};background:{C_SURFACE};border:1px solid {C_BORDER};'
        f'border-radius:20px;padding:5px 14px;">{dot}Updated: {ts}</div>'
        f'</div></div>'
    )


def section_hdr(title, badge=""):
    b = (f'<div style="font-family:DM Mono,monospace;font-size:12px;color:{C_DIM};'
         f'background:{C_SURFACE};border:1px solid {C_BORDER};'
         f'padding:3px 10px;border-radius:20px;">{badge}</div>') if badge else ""
    return (
        f'<div style="display:flex;align-items:center;gap:14px;margin:38px 0 18px;">'
        f'<div style="font-family:Syne,sans-serif;font-size:13px;font-weight:700;'
        f'text-transform:uppercase;letter-spacing:1.5px;color:{C_MUTED};'
        f'white-space:nowrap;line-height:1.4;">{title}</div>'
        f'<div style="flex:1;height:1px;background:linear-gradient(90deg,{C_BORDER},transparent);"></div>'
        f'{b}</div>'
    )


def kpi_card(label, value, accent, val_color):
    return (
        f'<div style="background:{C_SURFACE};border:1px solid {C_BORDER};border-radius:14px;'
        f'padding:24px 26px 22px;position:relative;overflow:hidden;transition:border-color 0.2s;">'
        f'<div style="position:absolute;top:0;left:0;right:0;height:2px;'
        f'background:linear-gradient(90deg,transparent,{accent},transparent);opacity:0.85;"></div>'
        f'<div style="position:absolute;bottom:-26px;right:-26px;width:96px;height:96px;'
        f'border-radius:50%;background:{accent};opacity:0.06;"></div>'
        f'<div style="font-family:DM Sans,sans-serif;font-size:12px;font-weight:600;'
        f'text-transform:uppercase;letter-spacing:1.2px;color:{C_DIM};margin-bottom:12px;">{label}</div>'
        f'<div style="font-family:DM Mono,monospace;font-size:28px;font-weight:500;'
        f'letter-spacing:-0.8px;line-height:1;color:{val_color};">{value}</div>'
        f'</div>'
    )


def sep():
    return (f'<div style="height:1px;margin:28px 0;'
            f'background:linear-gradient(90deg,{C_BORDER},rgba(59,130,246,0.2),{C_BORDER});"></div>')


def signal_ok():
    return (
        f'<div style="background:{C_SURFACE};border:1px solid rgba(16,185,129,0.28);'
        f'border-radius:14px;padding:20px 24px;display:flex;align-items:center;gap:12px;'
        f'color:{C_GREEN};font-size:16px;font-weight:500;">'
        f'&#9989;&nbsp; No buy signals triggered today — all schemes within threshold bounds.</div>'
    )


def splash():
    return (
        f'<div style="background:{C_SURFACE};border:1px solid {C_BORDER};border-radius:14px;'
        f'padding:70px 20px;text-align:center;margin-top:40px;">'
        f'<div style="font-size:50px;margin-bottom:16px;opacity:0.35;">&#128200;</div>'
        f'<div style="font-family:Syne,sans-serif;font-size:22px;font-weight:700;'
        f'color:{C_MUTED};margin-bottom:10px;">No data loaded</div>'
        f'<div style="font-size:16px;color:{C_DIM};">Click <strong>&#8635; Refresh P&amp;L</strong>'
        f' to compute portfolio change</div></div>'
    )


def tbl_start(cols):
    ths = "".join(
        f'<th style="font-family:Syne,sans-serif;font-size:11px;font-weight:700;'
        f'text-transform:uppercase;letter-spacing:1.1px;color:{C_TH_COL};'
        f'padding:13px 18px;white-space:nowrap;text-align:{a};background:{C_TH_BG};">{h}</th>'
        for h, a in cols
    )
    return (
        f'<div style="background:{C_SURFACE};border:1px solid {C_BORDER};'
        f'border-radius:14px;overflow:hidden;">'
        f'<table style="width:100%;border-collapse:collapse;font-family:DM Mono,monospace;font-size:14px;">'
        f'<thead><tr style="border-bottom:1px solid {C_BORDER};">{ths}</tr></thead><tbody>'
    )


def tbl_end():
    return "</tbody></table></div>"


def td(val, align="right", color=None, bold=False, wrap=False):
    col = f"color:{color};" if color else f"color:{C_TEXT2};"
    wgt = "font-weight:600;" if bold else ""
    fam = "font-family:DM Sans,sans-serif;" if bold else ""
    # wrap=True allows text to wrap (used for fund names so long names aren't truncated)
    ws  = "white-space:normal;word-break:break-word;min-width:160px;max-width:260px;" if wrap \
          else "white-space:nowrap;"
    return (
        f'<td style="padding:13px 18px;{ws}text-align:{align};{col}{wgt}{fam}">{val}</td>'
    )


def buy_table(recs):
    cols = [("Scheme Name","left"),("1D Change %","right"),
            ("Threshold","right"),("Recommended Buy","right")]
    rows = ""
    for r in recs:
        cc = C_GREEN if r["chg"] > 0 else C_RED
        rows += (
            f'<tr style="border-bottom:1px solid {C_BORDER};">'
            + td(r["name"], "left", C_TEXT, bold=True, wrap=True)
            + td(f'{sign(r["chg"])}{r["chg"]:.2f}%', color=cc)
            + td(f'{r["threshold"]}%', color=C_MUTED)
            + td(f'&#8377;{r["buy_amt"]:,.0f}', color=C_GOLD)
            + "</tr>"
        )
    return tbl_start(cols) + rows + tbl_end()


def scheme_table(df_in, total_mtm):
    cols = [
        ("Scheme","left"),("Segment","left"),
        ("Last NAV","right"),("iNAV","right"),
        ("Last Value","right"),("MTM Value","right"),
        ("Weight %","right"),("1D P&L","right"),("1D Change %","right"),
    ]
    rows = ""
    for _, row in df_in.iterrows():
        pnl = row["1D P&L"]
        chg = row["1D Chg Num"]
        wt  = row["MTM Value"] / total_mtm * 100 if total_mtm else 0
        pc  = C_GREEN if pnl > 0 else (C_RED if pnl < 0 else C_MUTED)
        cc  = C_GREEN if chg > 0 else (C_RED if chg < 0 else C_MUTED)
        rows += (
            f'<tr style="border-bottom:1px solid {C_BORDER};">'
            + td(row["Scheme Name"], "left", C_TEXT, bold=True, wrap=True)
            + td(seg_pill(row["Segment"]), "left")
            + td(f'{row["Last NAV"]:.2f}', color=C_TEXT2)
            + td(f'{row["iNAV"]:.2f}', color=C_TEXT2)
            + td(f'&#8377;{row["Last Value"]:,.0f}', color=C_TEXT2)
            + td(f'&#8377;{row["MTM Value"]:,.0f}', color=C_TEXT2)
            + td(f'{wt:.1f}%', color=C_MUTED)
            + td(f'{sign(pnl)}&#8377;{abs(pnl):,.0f}', color=pc)
            + td(f'{sign(chg)}{chg:.2f}%', color=cc)
            + "</tr>"
        )
    return tbl_start(cols) + rows + tbl_end()


def seg_card(seg, mtm, chg, wt):
    col     = seg_color(seg)
    chg_col = C_GREEN if chg >= 0 else C_RED
    s       = "+" if chg >= 0 else ""
    return (
        f'<div style="background:{C_SURFACE};border:1px solid {C_BORDER};'
        f'border-top:3px solid {col};border-radius:10px;padding:14px 16px;" title="{seg}">'
        f'<div style="font-size:11px;color:{C_DIM};font-weight:700;text-transform:uppercase;'
        f'letter-spacing:0.8px;margin-bottom:7px;font-family:Syne,sans-serif;'
        f'overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">{seg}</div>'
        f'<div style="font-family:DM Mono,monospace;font-size:16px;font-weight:500;color:{C_TEXT};">'
        f'&#8377;{mtm:,.0f}</div>'
        f'<div style="display:flex;align-items:center;gap:10px;margin-top:5px;">'
        f'<span style="font-family:DM Mono,monospace;font-size:14px;color:{chg_col};">{s}{chg:.2f}%</span>'
        f'<span style="font-family:DM Mono,monospace;font-size:12px;color:{C_DIM};">{wt:.1f}% wt</span>'
        f'</div></div>'
    )


def build_sunburst(df):
    seg_agg = (df.groupby("Segment")
                 .agg({"Last Value":"sum","MTM Value":"sum","1D P&L":"sum"})
                 .reset_index())
    seg_agg["chg"] = (seg_agg["1D P&L"] / seg_agg["Last Value"] * 100).round(2)
    total_mtm      = seg_agg["MTM Value"].sum()
    seg_agg["wt"]  = (seg_agg["MTM Value"] / total_mtm * 100).round(1)

    ids, labels, parents, values, customdata, colors = [], [], [], [], [], []
    t_pnl = float(seg_agg["1D P&L"].sum())
    t_lv  = float(seg_agg["Last Value"].sum())

    ids.append("__root__"); labels.append("Portfolio"); parents.append("")
    values.append(float(total_mtm)); colors.append("#1e3a5f")
    customdata.append((float(total_mtm), t_pnl, t_pnl/t_lv*100 if t_lv else 0, 100.0))

    for _, sr in seg_agg.iterrows():
        seg = sr["Segment"]
        ids.append(seg); labels.append(seg); parents.append("__root__")
        values.append(float(sr["MTM Value"])); colors.append(seg_color(seg))
        customdata.append((float(sr["MTM Value"]),float(sr["1D P&L"]),
                           float(sr["chg"]),float(sr["wt"])))

    fund_tot = float(df["MTM Value"].sum())
    for _, row in df.iterrows():
        fc = fund_color(row["Scheme Name"])
        r_, g_, b_ = int(fc[1:3],16), int(fc[3:5],16), int(fc[5:7],16)
        w = float(row["MTM Value"]) / fund_tot * 100 if fund_tot else 0
        ids.append(row["Scheme Name"]); labels.append(row["Scheme Name"])
        parents.append(row["Segment"]); values.append(float(row["MTM Value"]))
        colors.append(f"rgba({r_},{g_},{b_},0.82)")
        customdata.append((float(row["MTM Value"]),float(row["1D P&L"]),
                           float(row["1D Chg Num"]),round(w,1)))

    fig = go.Figure(go.Sunburst(
        ids=ids, labels=labels, parents=parents, values=values,
        marker=dict(colors=colors, line=dict(color="#030712", width=2)),
        customdata=customdata,
        hovertemplate=(
            "<b>%{label}</b><br>"
            "MTM: \u20b9%{customdata[0]:,.0f}<br>"
            "Weight: %{customdata[3]:.1f}%<br>"
            "1D P&L: \u20b9%{customdata[1]:,.0f}<br>"
            "1D Chg: %{customdata[2]:.2f}%<extra></extra>"
        ),
        texttemplate="%{label}<br>%{customdata[3]:.1f}%",
        textfont=dict(family="DM Sans, sans-serif", size=12, color="#f0f4f8"),
        insidetextorientation="auto",
        maxdepth=2, branchvalues="total",
    ))
    fig.update_layout(
        margin=dict(t=10,b=10,l=10,r=10),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="DM Sans, sans-serif", color="#f0f4f8",size=11),
        height=580,#540
    )
    return fig


# ── RENDER ───────────────────────────────────────────────────────────────────

ts = st.session_state.last_updated or "—"
st.markdown(topbar(ts), unsafe_allow_html=True)

col_btn, _ = st.columns([2, 6])
with col_btn:
    refresh_clicked = st.button("↻  Refresh P&L", use_container_width=True)

if refresh_clicked:
    with st.spinner("Fetching NAVs & benchmarks…"):
        df_disp, totals = build_snapshot()
    st.session_state.run_mtm      = True
    st.session_state.df_disp      = df_disp
    st.session_state.totals       = totals
    st.session_state.last_updated = datetime.now().strftime("%d-%b-%Y %H:%M:%S IST")
    st.rerun()

st.markdown(sep(), unsafe_allow_html=True)

# ── Main content ─────────────────────────────────────────────────────────────
if st.session_state.run_mtm and st.session_state.df_disp is not None:

    df   = st.session_state.df_disp.copy()
    tots = st.session_state.totals
    df["Segment"] = df["Scheme Name"].map(segment_mapping_dict).fillna("Other")

    pv, mtm, pnl, ret = tots["pv"], tots["mtm"], tots["pnl"], tots["ret"]

    # ── KPI tiles ──
    st.markdown(section_hdr("Portfolio Overview", "Live"), unsafe_allow_html=True)
    k1, k2, k3, k4 = st.columns(4)
    with k1: st.markdown(kpi_card("&Sigma; Portfolio Value", f"&#8377;{pv:,.0f}",  C_BLUE,   C_TEXT), unsafe_allow_html=True)
    with k2: st.markdown(kpi_card("&Sigma; MTM Value",       f"&#8377;{mtm:,.0f}", C_PURPLE, C_TEXT), unsafe_allow_html=True)
    with k3:
        pc = C_GREEN if pnl >= 0 else C_RED
        st.markdown(kpi_card("&Sigma; 1D P&amp;L", f"&#8377;{pnl:,.0f}", pc, pc), unsafe_allow_html=True)
    with k4:
        rc = C_GREEN if ret >= 0 else C_RED
        st.markdown(kpi_card("&Sigma; 1D Change %", f"{ret:.2f}%", rc, rc), unsafe_allow_html=True)

    st.markdown(sep(), unsafe_allow_html=True)

    # ── Exhibit 1: Buy Recommendations ──
    st.markdown(section_hdr("Exhibit 1 &nbsp;&middot;&nbsp; Buy Recommendations", "Threshold-based"), unsafe_allow_html=True)
    recs = calc_buy_recs(df)
    if not recs:
        st.markdown(signal_ok(), unsafe_allow_html=True)
    else:
        st.markdown(buy_table(recs), unsafe_allow_html=True)

    st.markdown(sep(), unsafe_allow_html=True)

    # ── Exhibit 2: Scheme-wise table ──
    st.markdown(section_hdr("Exhibit 2 &nbsp;&middot;&nbsp; Scheme-wise Market Value &amp; P&amp;L"), unsafe_allow_html=True)
    df_scheme = (df[["Scheme Name","Segment","Last NAV","iNAV","Last Value","MTM Value","1D P&L","1D Chg Num"]]
                 .copy().sort_values("1D P&L", ascending=False))
    st.markdown(scheme_table(df_scheme, mtm), unsafe_allow_html=True)

    st.markdown(sep(), unsafe_allow_html=True)

    # ── Exhibit 3: Sunburst ──
    st.markdown(section_hdr("Exhibit 3 &nbsp;&middot;&nbsp; Portfolio Breakdown", "Click segment to drill down"), unsafe_allow_html=True)
    st.plotly_chart(build_sunburst(df), use_container_width=True, config={"displayModeBar": False})

    # ── Segment legend cards — sorted by MTM desc, chunked 3 then 4s ──
    seg_leg = (df.groupby("Segment")
                 .agg({"Last Value":"sum","MTM Value":"sum","1D P&L":"sum"})
                 .reset_index())
    seg_leg["chg"] = (seg_leg["1D P&L"] / seg_leg["Last Value"] * 100).round(2)
    seg_leg["wt"]  = (seg_leg["MTM Value"] / seg_leg["MTM Value"].sum() * 100).round(1)
    seg_leg        = seg_leg.sort_values("MTM Value", ascending=False).reset_index(drop=True)

    n_total = len(seg_leg)
    # Build chunk sizes: first chunk is 3 (or less if fewer cards), rest are 4
    if n_total <= 3:
        chunks = [n_total]
    else:
        chunks = [3] + [4] * ((n_total - 3 + 3) // 4)
        # trim last chunk to actual remainder
        last = n_total - 3
        chunks = [3] + [4] * (last // 4) + ([last % 4] if last % 4 else [])

    idx = 0
    for chunk_size in chunks:
        if idx >= n_total:
            break
        row_df   = seg_leg.iloc[idx:idx+chunk_size]
        leg_cols = st.columns(chunk_size)
        for ci, (_, sr) in enumerate(row_df.iterrows()):
            with leg_cols[ci]:
                st.markdown(
                    seg_card(sr["Segment"], float(sr["MTM Value"]),
                             float(sr["chg"]), float(sr["wt"])),
                    unsafe_allow_html=True,
                )
        idx += chunk_size

else:
    st.markdown(splash(), unsafe_allow_html=True)

