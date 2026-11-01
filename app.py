"""공공 대여자전거 수요 관측소 — Streamlit에서 웹앱(ddareungi.html)을 그대로 띄운다.

실행: streamlit run app.py
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="공공 대여자전거 수요 관측소", page_icon="🚲", layout="wide")

# Streamlit 기본 머리글·메뉴·여백을 숨겨서 웹앱이 화면을 꽉 채우게 한다
st.markdown(
    """
    <style>
      header, [data-testid="stHeader"], [data-testid="stToolbar"], #MainMenu, footer { display: none !important; }
      .block-container, [data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
      [data-testid="stAppViewContainer"] iframe { display: block; border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "ddareungi.html").read_text(encoding="utf-8")

# 웹앱이 들어가는 상자(iframe)의 높이를 브라우저 창 높이에 맞춘다.
# 이렇게 하면 상자 안에서 스크롤되어, ③의 왼쪽 달 목록처럼 화면에 붙어 있는 부분도 원래대로 동작한다.
FIT = """
<script>
(function () {
  try {
    var f = window.frameElement; if (!f) return;
    var fit = function () { f.style.height = window.parent.innerHeight + 'px'; };
    fit(); window.parent.addEventListener('resize', fit);
  } catch (e) { /* 막히면 아래 height 값이 그대로 쓰인다 */ }
})();
</script>
"""

components.html(html + FIT, height=900, scrolling=True)
