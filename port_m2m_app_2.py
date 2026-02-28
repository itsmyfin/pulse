# app.py
# Portfolio Monitor · Dark Theme · Streamlit


# ---------- Segment mapping by name ----------

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
        'units': 14762.9,
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
        'units': 32776.499,
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
        'units': 3652.901,
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
        'units': 4071.214,
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




# ── Config & Constants ──────────────────────────────────────────────────────

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
        'threshold_pct': 1.0,
        'multipliers': {-1.0:10000,-1.5:12000,-2:15000,-2.5:17000,-3.0:20000,-3.5:25000,-4.0:30000},
    },
    'None': {
        'threshold_pct': 0.5,
        'multipliers': {-1:5000,-2:7000},
    },
}

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

def seg_color(seg):
    return _color_for(f"seg:{seg}")

def fund_color(fund):
    return _color_for(f"fund:{fund}")

C_BG        = "#020617"
C_SURFACE   = "#0b1220"
C_SURFACE2  = "#111827"
C_SURFACE_H = "#1f2937"
C_BORDER    = "rgba(148,163,184,0.28)"
C_BORDER_H  = "rgba(148,163,184,0.42)"
C_TEXT      = "#e5e7eb"
C_TEXT2     = "#cbd5f5"
C_MUTED     = "#9ca3af"
C_DIM       = "#6b7280"
C_TH_BG     = "#020617"
C_TH_COL    = "#9ca3af"
C_ROW_HOV   = "#020617"
C_GREEN     = "#22c55e"
C_RED       = "#f97373"
C_GOLD      = "#fbbf24"
C_BLUE      = "#3b82f6"
C_PURPLE    = "#a855f7"
C_TOPBAR    = "rgba(2,6,23,0.92)"

import requests, time, numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Portfolio Monitor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

for k, v in {"run_mtm": False, "df_disp": None, "totals": None, "last_updated": None}.items():
    if k not in st.session_state:
        st.session_state[k] = v

st.html(f"""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=DM+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<style>
html, body, [class*="stApp"], [class*="block-container"] * {{
  font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
  color: {C_TEXT};
  font-size: 15px;
}}
thead th {{
  font-size: 13.5px !important;
}}
tbody td {{
  font-size: 14px !important;
}}
[class*="stApp"] {{
  background: radial-gradient(circle at top, #0b1120 0, {C_BG} 55%) !important;
}}
[class*="block-container"] {{
  padding-top: 0 !important;
  max-width: 1300px !important;
}}
#MainMenu, footer {{ visibility: hidden; }}
header[data-testid="stHeader"] {{ display: none; }}
::-webkit-scrollbar {{ width: 6px; height: 6px; }}
::-webkit-scrollbar-track {{ background: transparent; }}
::-webkit-scrollbar-thumb {{
  background: rgba(148,163,184,0.5);
  border-radius: 999px;
}}
[data-testid="stButton"] > button {{
  font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
  font-size: 14px !important;
  font-weight: 500 !important;
  color: #e5e7eb !important;
  background: linear-gradient(135deg, {C_BLUE}, #{hex(int(C_BLUE[1:],16) ^ 0x111111)[2:]:s}) !important;
  border-radius: 999px !important;
  border: 1px solid rgba(59,130,246,0.3) !important;
  padding: 8px 20px !important;
  box-shadow: 0 10px 30px rgba(15,23,42,0.9) !important;
  display: inline-flex !important;
  align-items: center;
  justify-content: center;
  gap: 6px;
  transition: transform 0.15s ease, box-shadow 0.15s ease, background 0.15s ease !important;
}}
[data-testid="stButton"] > button:hover {{
  transform: translateY(-1px) scale(1.01) !important;
  box-shadow: 0 18px 45px rgba(15,23,42,0.95) !important;
}}
[data-testid="stButton"] > button:active {{
  transform: translateY(0) scale(0.99) !important;
  box-shadow: 0 4px 18px rgba(15,23,42,0.9) !important;
}}
table {{
  border-collapse: collapse;
}}
tbody tr:nth-child(even) {{
  background-color: rgba(15,23,42,0.55);
}}
tbody tr:nth-child(odd) {{
  background-color: rgba(15,23,42,0.2);
}}
tbody tr:hover {{
  background-color: {C_SURFACE_H} !important;
}}
@keyframes pm-pulse-dot {{
  0%,100% {{ opacity:1; transform:scale(1); }}
  50% {{ opacity:0.4; transform:scale(0.8); }}
}}
@keyframes fadeUp {{
  0% {{ opacity:0; transform:translateY(6px); }}
  100% {{ opacity:1; transform:translateY(0); }}
}}
</style>
""")

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
            if attempt == retries - 1:
                raise
            time.sleep(delay)

@st.cache_data(show_spinner=False, ttl=300)
def build_snapshot():
    r_idx = requests.get(URL_JSON, headers=HEADERS_NSE, timeout=5)
    r_idx.raise_for_status()
    raw = r_idx.json()
    df_idx = pd.json_normalize(raw.get("data") or raw.get("indices") or raw)
    idx_cols = [c for c in ["index", "indexSymbol", "percentChange"] if c in df_idx.columns]
    df_idx = df_idx[idx_cols].rename(columns={
        "index": "Benchmark Name", "indexSymbol": "benchmark_ticker", "percentChange": "PctChg"
    })

    r_etf = requests.get(URL_ETF, headers=HEADERS_NSE, timeout=5)
    r_etf.raise_for_status()
    raw_e = r_etf.json()
    df_etf = pd.json_normalize(raw_e.get("data") or raw_e.get("etfData") or raw_e)
    etf_cols = [c for c in ["assets", "symbol", "per"] if c in df_etf.columns]
    df_etf = df_etf[etf_cols].rename(columns={
        "assets": "Benchmark Name", "symbol": "benchmark_ticker", "per": "PctChg"
    })

    bmk = pd.concat(
        [df_idx[["Benchmark Name", "benchmark_ticker", "PctChg"]],
         df_etf[["Benchmark Name", "benchmark_ticker", "PctChg"]]],
        ignore_index=True,
    ).dropna(subset=["benchmark_ticker"])

    pct_eq   = pd.to_numeric(str(bmk.loc[bmk["benchmark_ticker"] == "NIFTY 500",   "PctChg"].iloc[0]).replace("%", ""), errors="coerce")
    pct_debt = pd.to_numeric(str(bmk.loc[bmk["benchmark_ticker"] == "LTGILTBEES",  "PctChg"].iloc[0]).replace("%", ""), errors="coerce")
    bmk = pd.concat([bmk, pd.DataFrame([{
        "Benchmark Name": "Custom Multi-Asset",
        "benchmark_ticker": "CUSTMULT01",
        "PctChg": 0.75 * pct_eq + 0.25 * pct_debt,
    }])], ignore_index=True)

    port = pd.DataFrame([{
        "Scheme Code": sc, "Scheme Name": v["Scheme Name"],
        "Benchmark Name": v["Benchmark Name"],
        "benchmark_ticker": v["benchmark_ticker"],
        "units": v["units"],
    } for sc, v in FUNDS.items()])

    port = port.merge(bmk[["Benchmark Name", "benchmark_ticker", "PctChg"]],
                      on=["Benchmark Name", "benchmark_ticker"], how="left")
    port["PctChg"]     = pd.to_numeric(port["PctChg"].astype(str).str.replace("%", ""), errors="coerce")
    port["Last NAV"]   = port["Scheme Code"].apply(get_latest_nav)
    port["Last Value"] = port["Last NAV"] * port["units"]
    port["iNAV"]       = port["Last NAV"] * (1 + port["PctChg"] / 100.0)
    port["MTM Value"]  = port["iNAV"] * port["units"]
    port["1D P&L"]     = port["MTM Value"] - port["Last Value"]
    port["1D Chg Num"] = port["1D P&L"] / port["Last Value"] * 100.0

    df_disp = port[[
        "Scheme Code", "Scheme Name", "Benchmark Name",
        "Last NAV", "iNAV", "Last Value", "MTM Value", "1D P&L", "1D Chg Num",
    ]].reset_index(drop=True)

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
        sname  = row["Scheme Name"]
        chg    = float(row["1D Chg Num"])
        t      = THRESHOLDS.get(sname, THRESHOLDS["default"])
        thr    = -t["threshold_pct"]  # e.g. -1.0 for 1%

        if chg <= thr:
            avail = sorted(t["multipliers"].keys())  # e.g. [-4.0,-3.5,-3.0,...,-1.0]

            # choose the highest threshold that is still >= chg (less negative)
            # example: chg = -1.2 -> picks -1.0, chg = -1.6 -> picks -1.5
            eligible = [k for k in avail if k >= chg and k <= thr]
            if not eligible:
                chosen = min(avail)  # fallback to most negative if something odd
            else:
                chosen = max(eligible)

            recs.append({
                "name":      sname,
                "chg":       chg,
                "threshold": t["threshold_pct"],
                "buy_amt":   t["multipliers"].get(chosen, 25000),
            })
    return recs



def seg_pill(seg):
    c = seg_color(seg)
    r, g, b = int(c[1:3], 16), int(c[3:5], 16), int(c[5:7], 16)
    return (
        f"<span style=\"display:inline-flex;align-items:center;"
        f"font-size:12px;font-weight:500;letter-spacing:0.01em;"
        f"padding:4px 10px;border-radius:999px;white-space:nowrap;"
        f"color:{c};background:rgba({r},{g},{b},0.12);"
        f"border:1px solid rgba({r},{g},{b},0.45);\">"
        f"{seg}</span>"
    )

def sign(v):
    return "+" if v > 0 else ""

def topbar(ts):
    live_badge = (
        f"<span style=\"display:inline-flex;align-items:center;gap:6px;"
        f"padding:2px 10px;border-radius:999px;"
        f"background:rgba(34,197,94,0.08);border:1px solid rgba(34,197,94,0.4);"
        f"font-size:11px;font-weight:500;color:{C_GREEN};\">"
        f"<span style=\"width:7px;height:7px;border-radius:999px;"
        f"background:{C_GREEN};box-shadow:0 0 12px rgba(34,197,94,0.9);"
        f"animation:pm-pulse-dot 2s ease-in-out infinite;\"></span>"
        f"Live"
        f"</span>"
    )
    updated_dot = (
        f"<span style=\"width:6px;height:6px;border-radius:999px;"
        f"background:{C_GREEN};margin-right:6px;\"></span>"
        if ts not in ["&#8212;", "—"] else ""
    )
    return (
        f"<div style=\"position:sticky;top:0;z-index:999;background:{C_TOPBAR};"
        f"backdrop-filter:blur(20px) saturate(1.6);"
        f"-webkit-backdrop-filter:blur(20px) saturate(1.6);"
        f"border-bottom:1px solid {C_BORDER};margin-bottom:20px;\">"
        f"<div style=\"max-width:1300px;margin:0 auto;"
        f"display:flex;align-items:center;justify-content:space-between;"
        f"height:64px;padding:10px 8px 8px;\">"

        # LEFT: icon + title / subtitle (subtitle starts roughly under icon)
        f"<div style=\"display:flex;align-items:flex-start;gap:10px;\">"
        f"<div style=\"width:30px;height:30px;border-radius:10px;"
        f"background:radial-gradient(circle at 10% 0%,rgba(56,189,248,0.9),rgba(59,130,246,0.15));"
        f"display:flex;align-items:center;justify-content:center;"
        f"font-size:18px;box-shadow:0 8px 30px rgba(15,23,42,0.8);"
        f"transform: translateY(-4px);\">&#128202;</div>"
        f"<div style=\"display:flex;flex-direction:column;gap:2px;\">"
        f"<div style=\"font-size:20px;font-weight:600;letter-spacing:-0.02em;color:{C_TEXT};\">"
        f"Portfolio Monitor</div>"
        # small negative margin to pull the Live/subtitle left under the icon
        f"<div style=\"display:flex;align-items:center;gap:8px;margin-left:-40  px;\">"
        f"{live_badge}"
        f"<span style=\"font-size:11px;color:{C_DIM};\">Daily NAV and MTM overview</span>"
        f"</div>"
        f"</div>"
        f"</div>"

        # RIGHT: last-updated pill (top-right, smaller font)
        f"<div style=\"display:flex;align-items:flex-start;\">"
        f"<div style=\"display:inline-flex;align-items:center;gap:6px;"
        f"padding:3px 12px;border-radius:999px;background:rgba(15,23,42,0.9);"
        f"border:1px solid {C_BORDER};font-size:11px;color:{C_DIM};"
        f"font-family:'DM Mono',monospace;\">"
        f"{updated_dot}"
        f"<span style=\"opacity:0.85;font-size:11px;\">Last updated</span>"
        f"<span style=\"color:{C_TEXT2};font-size:11px;\">{ts}</span>"
        f"</div>"

        f"</div>"

        f"</div>"
        f"</div>"
    )




def section_hdr(title, badge=""):
    b = (
        f"<div style=\"font-size:12px;color:{C_DIM};padding:3px 10px;"
        f"border-radius:999px;border:1px solid {C_BORDER};"
        f"background:rgba(15,23,42,0.8);white-space:nowrap;\">{badge}</div>"
    ) if badge else ""
    return (
        f"<div style=\"display:flex;align-items:center;gap:12px;"
        f"margin:22px 0 6px;\">"
        f"<div style=\"font-size:15px;font-weight:600;letter-spacing:0.03em;"
        f"text-transform:none;color:{C_MUTED};white-space:nowrap;\">{title}</div>"
        f"<div style=\"flex:1;height:1px;background:linear-gradient(90deg,rgba(148,163,184,0.45),transparent);\"></div>"
        f"{b}"
        f"</div>"
    )

def kpi_card(label, value, accent, val_color):
    return (
        f"<div style=\"background:radial-gradient(circle at top,rgba(15,23,42,0.9),{C_SURFACE2});"
        f"border-radius:14px;border:1px solid rgba(148,163,184,0.35);"
        f"padding:16px 18px;display:flex;flex-direction:column;gap:8px;"
        f"box-shadow:0 18px 45px rgba(15,23,42,0.9);animation:fadeUp 0.35s ease both;\">"
        f"<div style=\"display:flex;align-items:center;justify-content:space-between;\">"
        f"<span style=\"font-size:13px;font-weight:500;color:{C_DIM};\">{label}</span>"
        f"<span style=\"width:8px;height:8px;border-radius:999px;"
        f"background:{accent};box-shadow:0 0 12px rgba(59,130,246,0.7);\"></span>"
        f"</div>"
        f"<div style=\"font-family:'DM Mono',monospace;font-size:24px;"
        f"font-weight:500;color:{val_color};letter-spacing:-0.04em;\">{value}</div>"
        f"</div>"
    )

def sep():
    return (
        "<div style=\"height:1px;margin:24px 0;"
        "background:linear-gradient(90deg,rgba(15,23,42,0.1),rgba(148,163,184,0.4),rgba(15,23,42,0.1));\"></div>"
    )

def signal_ok():
    return (
        f"<div style=\"background:linear-gradient(135deg,rgba(22,163,74,0.16),rgba(15,23,42,0.9));"
        f"border:1px solid rgba(34,197,94,0.45);border-radius:14px;"
        f"padding:16px 18px;display:flex;align-items:flex-start;gap:10px;"
        f"color:{C_GREEN};font-size:14px;font-weight:500;\">"
        f"<span style=\"font-size:20px;\">&#9989;</span>"
        f"<div>"
        f"<div>No buy signals today</div>"
        f"<div style=\"margin-top:2px;font-size:13px;font-weight:400;color:{C_TEXT2};\">"
        f"All schemes are within their configured thresholds."
        f"</div>"
        f"</div>"
        f"</div>"
    )

def splash():
    return (
        f"<div style=\"background:radial-gradient(circle at top,rgba(15,23,42,0.85),{C_SURFACE});"
        f"border-radius:18px;border:1px dashed {C_BORDER};padding:52px 24px;"
        f"text-align:center;margin-top:40px;max-width:520px;margin-left:auto;margin-right:auto;\">"
        f"<div style=\"width:56px;height:56px;border-radius:18px;"
        f"margin:0 auto 16px;display:flex;align-items:center;justify-content:center;"
        f"background:rgba(15,23,42,0.85);border:1px solid rgba(148,163,184,0.45);"
        f"box-shadow:0 18px 40px rgba(15,23,42,0.9);font-size:28px;\">&#128200;</div>"
        f"<div style=\"font-size:18px;font-weight:600;color:{C_TEXT};margin-bottom:6px;\">"
        f"No data yet</div>"
        f"<div style=\"font-size:14px;color:{C_DIM};margin-bottom:12px;\">"
        f"Refresh your portfolio to see today&apos;s market move.</div>"
        f"<div style=\"font-size:13px;color:{C_MUTED};\">"
        f"Use the <strong>Refresh P&amp;L</strong> button in the top bar."
        f"</div>"
        f"</div>"
    )

def tbl_start(cols):
    ths = "".join(
        f"<th style=\"font-size:13px;font-weight:500;letter-spacing:0.03em;"
        f"text-transform:none;color:{C_TH_COL};"
        f"padding:9px 10px;white-space:nowrap;text-align:{a};"
        f"background:{C_TH_BG};border-bottom:1px solid {C_BORDER};\">"
        f"{h}</th>"
        for h, a in cols
    )
    return (
        # outer scroll wrapper
        f"<div style=\"width:100%;overflow-x:auto;\">"
        f"<div style=\"background:{C_SURFACE2};border:1px solid {C_BORDER};"
        f"border-radius:14px;overflow:hidden;animation:fadeUp 0.35s ease 0.05s both;"
        f"box-shadow:0 18px 45px rgba(15,23,42,0.9);\">"
        f"<table style=\"width:100%;border-collapse:collapse;"
        f"font-family:'DM Mono',monospace;font-size:13.5px;line-height:1.6;\">"
        f"<thead><tr>{ths}</tr></thead><tbody>"
    )


def tbl_end():
    return "</tbody></table></div></div>"


def td(val, align="right", color=None, bold=False):
    col   = f"color:{color};" if color else f"color:{C_TEXT2};"
    wgt   = "font-weight:600;" if bold else ""
    fam   = "font-family:'Inter',system-ui,sans-serif;" if bold else ""
    return (
        f"<td style=\"padding:8px 10px;white-space:nowrap;text-align:{align};{col}{wgt}{fam}\">"
        f"{val}</td>"
    )

def buy_table(recs):
    cols = [("Scheme", "left"),("1D change %","right"),("Threshold","right"),("Recommended buy","right")]
    rows = ""
    for r in recs:
        cc = C_GREEN if r["chg"] > 0 else C_RED
        rows += (
            "<tr>"
            + td(r["name"], "left", C_TEXT, bold=True)
            + td(f"{sign(r['chg'])}{r['chg']:.2f}%", color=cc)
            + td(f"{r['threshold']}%", color=C_MUTED)
            + td(f"&#8377;{r['buy_amt']:,.0f}", color=C_GOLD)
            + "</tr>"
        )
    return tbl_start(cols) + rows + tbl_end()

def scheme_table(df_in, total_mtm):
    cols = [
        ("Scheme", "left"), ("Segment", "left"),
        ("Last NAV", "right"), ("iNAV", "right"),
        ("Last value", "right"), ("MTM value", "right"),
        ("Weight %", "right"), ("1D P&L", "right"), ("1D change %", "right"),
    ]
    rows = ""
    for _, row in df_in.iterrows():
        pnl  = row["1D P&L"]
        chg  = row["1D Chg Num"]
        wt   = row["MTM Value"] / total_mtm * 100 if total_mtm else 0
        pc   = C_GREEN if pnl > 0 else (C_RED if pnl < 0 else C_MUTED)
        cc   = C_GREEN if chg > 0 else (C_RED if chg < 0 else C_MUTED)
        rows += (
            "<tr>"
            + td(row["Scheme Name"], "left", C_TEXT, bold=True)
            + td(seg_pill(row["Segment"]), "left")
            + td(f"{row['Last NAV']:.2f}", color=C_TEXT2)
            + td(f"{row['iNAV']:.2f}", color=C_TEXT2)
            + td(f"&#8377;{row['Last Value']:,.0f}", color=C_TEXT2)
            + td(f"&#8377;{row['MTM Value']:,.0f}", color=C_TEXT2)
            + td(f"{wt:.1f}%", color=C_MUTED)
            + td(f"{sign(pnl)}&#8377;{abs(pnl):,.0f}", color=pc)
            + td(f"{sign(chg)}{chg:.2f}%", color=cc)
            + "</tr>"
        )
    return tbl_start(cols) + rows + tbl_end()

def seg_card(seg, mtm, chg, wt):
    col     = seg_color(seg)
    chg_col = C_GREEN if chg >= 0 else C_RED
    s       = "+" if chg >= 0 else ""
    return (
        f"<div style=\"background:{C_SURFACE2};border-radius:14px;"
        f"border:1px solid {C_BORDER};padding:12px 14px 13px;"
        f"box-shadow:0 16px 32px rgba(15,23,42,0.85);position:relative;overflow:hidden;\">"
        f"<div style=\"position:absolute;top:0;left:0;right:0;height:3px;"
        f"background:linear-gradient(90deg,{col},rgba(15,23,42,0.9));opacity:0.9;\"></div>"
        f"<div style=\"display:flex;align-items:center;justify-content:space-between;margin-top:6px;\">"
        f"<div style=\"font-size:13px;font-weight:600;color:{C_TEXT};"
        f"overflow:hidden;text-overflow:ellipsis;white-space:nowrap;\">{seg}</div>"
        f"<span style=\"width:9px;height:9px;border-radius:999px;background:{col};\"></span>"
        f"</div>"
        f"<div style=\"margin-top:8px;font-family:'DM Mono',monospace;font-size:15px;"
        f"color:{C_TEXT};\">&#8377;{mtm:,.0f}</div>"
        f"<div style=\"display:flex;align-items:center;gap:10px;margin-top:4px;"
        f"font-family:'DM Mono',monospace;font-size:12px;\">"
        f"<span style=\"color:{chg_col};\">{s}{chg:.2f}%</span>"
        f"<span style=\"color:{C_DIM};\">{wt:.1f}% weight</span>"
        f"</div>"
        f"</div>"
    )

def _with_alpha(hex_color, alpha=0.85):
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    return f"rgba({r},{g},{b},{alpha})"


def build_treemap(df):
    seg_agg = (
        df.groupby("Segment")
          .agg({"Last Value": "sum", "MTM Value": "sum", "1D P&L": "sum"})
          .reset_index()
    )
    seg_agg["chg"] = (seg_agg["1D P&L"] / seg_agg["Last Value"] * 100).round(2)
    total_mtm       = seg_agg["MTM Value"].sum()
    seg_agg["wt"]  = (seg_agg["MTM Value"] / total_mtm * 100).round(1)

    ids, labels, parents, values, customdata, colors = [], [], [], [], [], []

    t_pnl = float(seg_agg["1D P&L"].sum())
    t_lv  = float(seg_agg["Last Value"].sum())
    t_ret = t_pnl / t_lv * 100 if t_lv else 0

    # root node (portfolio)
    ids.append("__root__")
    labels.append("Portfolio")
    parents.append("")
    values.append(float(total_mtm))
    colors.append("rgba(2,6,23,0.9)")
    customdata.append((float(total_mtm), t_pnl, t_ret, 100.0))

    # segment level
    for _, sr in seg_agg.iterrows():
        seg = sr["Segment"]
        short_label = seg.replace("Equity: ", "")
        ids.append(seg)
        labels.append(short_label)
        parents.append("__root__")
        values.append(float(sr["MTM Value"]))
        colors.append(_with_alpha(seg_color(seg), alpha=0.85))
        customdata.append(
            (float(sr["MTM Value"]), float(sr["1D P&L"]),
             float(sr["chg"]), float(sr["wt"]))
        )

    # fund level – each fund gets its own (slightly transparent) color
    fund_tot = float(df["MTM Value"].sum())
    for _, row in df.iterrows():
        seg  = row["Segment"]
        w    = float(row["MTM Value"]) / fund_tot * 100 if fund_tot else 0

        ids.append(row["Scheme Name"])
        labels.append(row["Scheme Name"])
        parents.append(seg)
        values.append(float(row["MTM Value"]))
        colors.append(_with_alpha(fund_color(row["Scheme Name"]), alpha=0.85))
        customdata.append(
            (float(row["MTM Value"]), float(row["1D P&L"]),
             float(row["1D Chg Num"]), round(w, 1))
        )

    fig = go.Figure(go.Treemap(
        ids=ids,
        labels=labels,
        parents=parents,
        values=values,
        marker=dict(
            colors=colors,
            line=dict(width=1, color="#020617"),
        ),
        customdata=customdata,
        branchvalues="total",
        maxdepth=2,
        hovertemplate=(
            "<b>%{label}</b><br>"
            "MTM value: ₹%{customdata[0]:,.0f}<br>"
            "Weight: %{customdata[3]:.1f}%<br>"
            "1D P&L: ₹%{customdata[1]:,.0f}<br>"
            "1D change: %{customdata[2]:.2f}%"
            "<extra></extra>"
        ),
        texttemplate="<b>%{label}</b><br>%{customdata[3]:.1f}%",
        textfont=dict(
            family="Inter, system-ui, sans-serif",
            size=14,
            color="#e5e7eb",
        ),
        tiling=dict(
            pad=2,
            squarifyratio=1.1,
        ),
    ))

    # global transparency for a more modern look
    fig.update_traces(
        opacity=0.8,
        selector=dict(type="treemap"),
    )

    fig.update_layout(
        margin=dict(t=20, b=8, l=8, r=8),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="Inter, system-ui, sans-serif",
            color="#e5e7eb",
            size=14,
        ),
        hoverlabel=dict(
            font_size=14,
            font_family="Inter, system-ui, sans-serif",
        ),
        height=540,
    )

    fig.add_annotation(
        text=(
            f"<span style='font-size:13px;color:#94a3b8;'>Portfolio MTM</span><br>"
            f"<span style='font-size:20px;font-weight:600;'>₹{total_mtm:,.0f}</span> "
            f"<span style='font-size:12px;color:{'#22c55e' if t_ret >= 0 else '#f97373'};'>"
            f"{t_ret:+.2f}%</span>"
        ),
        showarrow=False,
        x=0, y=1.18,
        xref="paper", yref="paper",
        align="left",
    )

    return fig


ts = st.session_state.last_updated or "—"
st.markdown(topbar(ts), unsafe_allow_html=True)

# Three columns: left spacer, narrow center (button), right spacer
left, col_btn, right = st.columns([2, 1, 2])

with col_btn:
    refresh_clicked = st.button("↻  Refresh P&L", use_container_width=True)


if refresh_clicked:
    with st.spinner("Fetching NAVs and benchmarks…"):
        df_disp, totals = build_snapshot()
    st.session_state.run_mtm      = True
    st.session_state.df_disp      = df_disp
    st.session_state.totals       = totals
    st.session_state.last_updated = datetime.now().strftime("%d-%b-%Y %H:%M:%S IST")
    st.rerun()

st.markdown(sep(), unsafe_allow_html=True)

if st.session_state.run_mtm and st.session_state.df_disp is not None:

    df   = st.session_state.df_disp.copy()
    tots = st.session_state.totals
    df["Segment"] = df["Scheme Name"].map(segment_mapping_dict).fillna("Other")

    pv  = tots["pv"]
    mtm = tots["mtm"]
    pnl = tots["pnl"]
    ret = tots["ret"]

    st.markdown(section_hdr("Portfolio overview", "Live snapshot"), unsafe_allow_html=True)
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown(kpi_card("Portfolio value", f"&#8377;{pv:,.0f}", C_BLUE, C_TEXT), unsafe_allow_html=True)
    with k2:
        st.markdown(kpi_card("MTM value", f"&#8377;{mtm:,.0f}", C_PURPLE, C_TEXT), unsafe_allow_html=True)
    with k3:
        pc = C_GREEN if pnl >= 0 else C_RED
        st.markdown(kpi_card("1D P&amp;L", f"&#8377;{pnl:,.0f}", pc, pc), unsafe_allow_html=True)
    with k4:
        rc = C_GREEN if ret >= 0 else C_RED
        st.markdown(kpi_card("1D change", f"{ret:.2f}%", rc, rc), unsafe_allow_html=True)

    st.markdown(sep(), unsafe_allow_html=True)

    st.markdown(section_hdr("Exhibit 1 · Buy recommendations", "Threshold-based"), unsafe_allow_html=True)
    recs = calc_buy_recs(df)
    if not recs:
        st.markdown(signal_ok(), unsafe_allow_html=True)
    else:
        st.markdown(buy_table(recs), unsafe_allow_html=True)

    st.markdown(sep(), unsafe_allow_html=True)

        # Exhibit 2 with sort controls
    st.markdown(
        section_hdr("Exhibit 2 · Scheme-wise market value and P&L", "Sortable table"),
        unsafe_allow_html=True,
    )

    sort_col_map = {
        "Scheme": "Scheme Name",
        "Segment": "Segment",
        # "Last NAV": "Last NAV",
        # "iNAV": "iNAV",
        "Last value": "Last Value",
        "MTM value": "MTM Value",
        "Weight %": "MTM Value",  # sort by MTM, weight is derived
        "1D P&L": "1D P&L",
        "1D change %": "1D Chg Num",
        
    }

    # single row: dropdown + radio
    c_sort, c_order, _ = st.columns([2.2, 1.8, 3])

    with c_sort:
        sort_label = st.selectbox(
            "Sort by",
            list(sort_col_map.keys()),
            index=list(sort_col_map.keys()).index("1D P&L"),
        )

    with c_order:
        sort_order_label = st.radio(
            "Order",
            ["Descending", "Ascending"],
            index=0,
            horizontal=True,
            key="sort_order_radio",
        )

    sort_col = sort_col_map[sort_label]
    ascending = sort_order_label == "Ascending"

    df_scheme = (
        df[["Scheme Name", "Segment", "Last NAV", "iNAV",
            "Last Value", "MTM Value", "1D P&L", "1D Chg Num"]]
        .copy()
        .sort_values(sort_col, ascending=ascending)
    )

    st.markdown(scheme_table(df_scheme, mtm), unsafe_allow_html=True)



    st.markdown(sep(), unsafe_allow_html=True)

    st.markdown(
        section_hdr("Exhibit 3 · Portfolio breakdown", "Segment and scheme treemap"),
        unsafe_allow_html=True
    )
    st.plotly_chart(build_treemap(df), use_container_width=True, config={"displayModeBar": False})

    seg_leg = (
        df.groupby("Segment")
          .agg({"Last Value": "sum", "MTM Value": "sum", "1D P&L": "sum"})
          .reset_index()
    )
    seg_leg["chg"] = (seg_leg["1D P&L"] / seg_leg["Last Value"] * 100).round(2)
    seg_leg["wt"]  = (seg_leg["MTM Value"] / seg_leg["MTM Value"].sum() * 100).round(1)
    seg_leg        = seg_leg.sort_values("MTM Value", ascending=False)

    cards = list(seg_leg.itertuples(index=False))

    rows_cfg = [3, 4]
    rows = []
    idx = 0

    for wanted in rows_cfg:
        if idx >= len(cards):
            break
        rows.append(cards[idx:idx + wanted])
        idx += wanted

    while idx < len(cards):
        rows.append(cards[idx:idx + 5])
        idx += 5

    for row_cards in rows:
        n = len(row_cards)
        cols = st.columns(n)
        for i, sr in enumerate(row_cards):
            seg_name = sr[0]
            mtm_val  = float(sr[2])
            chg_val  = float(sr[4])
            wt_val   = float(sr[5])
            with cols[i]:
                st.markdown(
                    seg_card(seg_name, mtm_val, chg_val, wt_val),
                    unsafe_allow_html=True,
                )

else:
    st.markdown(splash(), unsafe_allow_html=True)
