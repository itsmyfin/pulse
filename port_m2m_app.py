
import requests
import pandas as pd
import streamlit as st
from datetime import datetime

# ----------------- Streamlit page config -----------------
# st.set_page_config(page_title="MF MTM Dashboard", layout="wide")
st.set_page_config(
    page_title="Portfolio Monitor",
    page_icon="📊",
    layout="wide",
)

st.markdown(
    """
    <style>
    /* Global app font */
    html, body, [class*="stApp"] * {
        font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont,
                     "Segoe UI", sans-serif !important;
    }

    /* Force st.dataframe to use same font */
    [data-testid="stDataFrame"] table,
    [data-testid="stDataFrame"] tbody,
    [data-testid="stDataFrame"] th,
    [data-testid="stDataFrame"] td,
    [data-testid="stDataFrame"] div {
        font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont,
                     "Segoe UI", sans-serif !important;
        font-size: 13px;  /* tweak if you want */
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ----------------- Session state -----------------
if "run_mtm" not in st.session_state:
    st.session_state.run_mtm = False

if "df_disp" not in st.session_state:
    st.session_state.df_disp = None

if "totals" not in st.session_state:
    st.session_state.totals = None

if "last_updated" not in st.session_state:      # ✅ NEW
    st.session_state.last_updated = None        # ✅ NEW


# ---------- Constants ----------
URL_JSON = "https://www.nseindia.com/api/allIndices"
URL_ETF = "https://www.nseindia.com/api/etf"

HEADERS_NSE = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json,text/plain,*/*",
}

FUNDS = {
   ########### LARGE CAPS #############

    '112877': {
        'Scheme Name': 'Bandhan Nifty 50 - Regular ',
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

# ---------- Helpers ----------
def color_pnl(val):
    try:
        v = float(str(val).replace("₹", "").replace(",", "").replace("%", ""))
    except Exception:
        return ""
    if v > 0:
        return "color: green;"
    if v < 0:
        return "color: red;"
    return ""

# def get_latest_nav(scheme_code):
#     data = requests.get(f"https://api.mfapi.in/mf/{scheme_code}", timeout=5).json()
#     return float(data["data"][0]["nav"])

import requests, time

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (MF App)'})

def get_latest_nav(scheme_code, max_retries=2, delay=0.5):
    url = f"https://api.mfapi.in/mf/{scheme_code}"

    for attempt in range(max_retries):
        try:
            resp = session.get(url, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            return float(data["data"][0]["nav"])
        except Exception:
            if attempt == max_retries - 1:
                raise
            time.sleep(delay)

# ---------- Snapshot builder ----------
@st.cache_data(show_spinner=False, ttl=300)
def build_snapshot():
    # 1) NSE indices
    r_idx = requests.get(URL_JSON, headers=HEADERS_NSE, timeout=5)
    r_idx.raise_for_status()
    data_idx = r_idx.json()
    df_idx_raw = pd.json_normalize(
        data_idx.get("data") or data_idx.get("indices") or data_idx
    )
    idx_cols = [c for c in ["index", "indexSymbol", "percentChange"] if c in df_idx_raw.columns]
    df_idx = df_idx_raw[idx_cols].copy()
    df_idx = df_idx.rename(
        columns={
            "index": "Benchmark Name",
            "indexSymbol": "benchmark_ticker",
            "percentChange": "PctChg",
        }
    )

    # 2) NSE ETFs
    r_etf = requests.get(URL_ETF, headers=HEADERS_NSE, timeout=5)
    r_etf.raise_for_status()
    data_etf = r_etf.json()
    df_etf_raw = pd.json_normalize(
        data_etf.get("data") or data_etf.get("etfData") or data_etf
    )
    etf_cols = [c for c in ["assets", "symbol", "per"] if c in df_etf_raw.columns]
    df_etf = df_etf_raw[etf_cols].copy()
    df_etf = df_etf.rename(
        columns={
            "assets": "Benchmark Name",
            "symbol": "benchmark_ticker",
            "per": "PctChg",
        }
    )

    # 3) Combine indices + ETFs
    df_idx = df_idx[["Benchmark Name", "benchmark_ticker", "PctChg"]]
    df_etf = df_etf[["Benchmark Name", "benchmark_ticker", "PctChg"]]
    bmk_info = pd.concat([df_idx, df_etf], ignore_index=True).dropna(
        subset=["Benchmark Name", "benchmark_ticker"]
    )

    # 4) Custom multi-asset benchmark (0.75 * NIFTY 500 + 0.25 * LTGILTBEES)
    w_eq = 0.75
    w_debt = 0.25

    pct_eq = bmk_info.loc[
        bmk_info["benchmark_ticker"] == "NIFTY 500", "PctChg"
    ].iloc[0]
    pct_debt = bmk_info.loc[
        bmk_info["benchmark_ticker"] == "LTGILTBEES", "PctChg"
    ].iloc[0]

    pct_eq = pd.to_numeric(str(pct_eq).replace("%", ""), errors="coerce")
    pct_debt = pd.to_numeric(str(pct_debt).replace("%", ""), errors="coerce")

    cust_pctchg = w_eq * pct_eq + w_debt * pct_debt

    new_row = {
        "Benchmark Name": "Custom Multi-Asset",
        "benchmark_ticker": "CUSTMULT01",
        "PctChg": cust_pctchg,
    }

    bmk_info = pd.concat(
        [bmk_info, pd.DataFrame([new_row])],
        ignore_index=True,
    )

    # 5) Build portfolio
    portfolio = pd.DataFrame(
        [
            {
                "Scheme Code": sc,
                "Scheme Name": info["Scheme Name"],
                "Benchmark Name": info["Benchmark Name"],
                "benchmark_ticker": info["benchmark_ticker"],
                "units": info["units"],
            }
            for sc, info in FUNDS.items()
        ]
    )

    portfolio = portfolio.merge(
        bmk_info[["Benchmark Name", "benchmark_ticker", "PctChg"]],
        on=["Benchmark Name", "benchmark_ticker"],
        how="left",
    )

    # 6) MTM calculations
    portfolio["PctChg"] = pd.to_numeric(
        portfolio["PctChg"].astype(str).str.replace("%", "", regex=False),
        errors="coerce",
    )

    portfolio["Last NAV"] = portfolio["Scheme Code"].apply(get_latest_nav)
    portfolio["Last Value"] = portfolio["Last NAV"] * portfolio["units"]
    portfolio["iNAV"] = portfolio["Last NAV"] * (1 + portfolio["PctChg"] / 100)
    portfolio["MTM Value"] = portfolio["iNAV"] * portfolio["units"]

    portfolio["1D P&L"] = portfolio["MTM Value"] - portfolio["Last Value"]
    portfolio["1D Return"] = portfolio["PctChg"].round(2).astype(str) + "%"

    df_disp = portfolio[
        [
            "Scheme Code",
            "Scheme Name",
            "Benchmark Name",
            "Last NAV",
            "iNAV",
            "Last Value",
            "MTM Value",
            "1D P&L",
            "1D Return",
        ]
    ].reset_index(drop=True)

    totals = pd.DataFrame(
        [{
            "Σ Portfolio Value": portfolio["Last Value"].sum(),
            "Σ MTM Value": portfolio["MTM Value"].sum(),
            "Σ 1D P&L": portfolio["1D P&L"].sum(),
            "Σ 1D Return": (portfolio["1D P&L"].sum()/portfolio["Last Value"].sum())*100,
        }]
    )

    return df_disp, totals

# ---------- UI ----------
st.title("📊 Portfolio Monitor")
st.caption("Captures real-time gains, losses, and Net Value")


if st.button("Refresh P&L"):
    with st.spinner("Getting latest data and updating P&L"):
        df_disp, totals = build_snapshot()
    st.session_state.run_mtm = True
    st.session_state.df_disp = df_disp
    st.session_state.totals = totals
    st.session_state.last_updated = datetime.now().strftime(  # ✅ NEW
        "%d-%b-%Y %H:%M:%S IST"
    )

# st.space("small")

# ✅ NEW: timestamp caption just below button
if st.session_state.last_updated is not None:
    # st.caption(f"*Last updated at {st.session_state.last_updated}*")
    st.caption(
    f"<span style='font-size:12px;'>Last updated on {st.session_state.last_updated}</span>",
    unsafe_allow_html=True,
)


st.space("small")


if st.session_state.run_mtm and st.session_state.df_disp is not None:
    totals = st.session_state.totals.iloc[0]

    port_val = float(totals["Σ Portfolio Value"])
    mtm_val  = float(totals["Σ MTM Value"])
    pnl_val  = float(totals["Σ 1D P&L"])
    ret_val  = float(totals["Σ 1D Return"])

    def color_hex(val: float) -> str:
        return "#16a34a" if val >= 0 else "#dc2626"  # green / red

    col1, col2, col3, col4 = st.columns(4)

    # Σ Portfolio Value (neutral)
    with col1:
        st.markdown(
            f"""
            <div style="
                padding:10px 14px;
                border-radius:10px;
                border:1px solid #1f2933;
                background-color:#020617;">
              <div style="font-size:13px;color:#9ca3af;">Σ Portfolio Value</div>
              <div style="font-size:24px;font-weight:600;color:#e5e7eb;">
                ₹{port_val:,.0f}
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Σ MTM Value (neutral)
    with col2:
        st.markdown(
            f"""
            <div style="
                padding:10px 14px;
                border-radius:10px;
                border:1px solid #1f2933;
                background-color:#020617;">
              <div style="font-size:13px;color:#9ca3af;">Σ MTM Value</div>
              <div style="font-size:24px;font-weight:600;color:#e5e7eb;">
                ₹{mtm_val:,.0f}
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Σ 1D P&L (colored)
    with col3:
        st.markdown(
            f"""
            <div style="
                padding:10px 14px;
                border-radius:10px;
                border:1px solid #1f2933;
                background-color:#020617;">
              <div style="font-size:13px;color:#9ca3af;">Σ 1D P&L</div>
              <div style="font-size:24px;font-weight:600;color:{color_hex(pnl_val)};">
                ₹{pnl_val:,.0f}
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Σ 1D Return (colored)
    with col4:
        st.markdown(
            f"""
            <div style="
                padding:10px 14px;
                border-radius:10px;
                border:1px solid #1f2933;
                background-color:#020617;">
              <div style="font-size:13px;color:#9ca3af;">Σ 1D Return</div>
              <div style="font-size:24px;font-weight:600;color:{color_hex(ret_val)};">
                {ret_val:.2f}%
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


    st.space("small")

    st.subheader("Scheme-wise Market Value & P&L")
    st.dataframe(
        st.session_state.df_disp.style
        .format({
            "Last NAV": "{:.2f}",
            "iNAV": "{:.2f}",
            "Last Value": "{:,.0f}",
            "MTM Value": "{:,.0f}",
            "1D P&L": "{:,.0f}",
        })
        .applymap(color_pnl, subset=["1D P&L", "1D Return"]),
        use_container_width=True,
        hide_index=True,
    )
else:
    st.info("Click to compute portfolio change")
