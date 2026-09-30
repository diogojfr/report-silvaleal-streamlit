import base64
import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

# ── Authentication ───────────────────────────────────────────────────────
load_dotenv()


def _get_app_password():
    """Senha vem do st.secrets (Streamlit Cloud) ou do .env/variável de ambiente (local)."""
    try:
        if "APP_PASSWORD" in st.secrets:
            return st.secrets["APP_PASSWORD"]
    except Exception:
        # Nenhum arquivo de secrets configurado (ex.: rodando localmente)
        pass
    return os.getenv("APP_PASSWORD")


APP_PASSWORD = _get_app_password()

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔒 Acesso Restrito")
    password = st.text_input("Digite a senha", type="password")
    if st.button("Entrar"):
        if APP_PASSWORD and password == APP_PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Senha incorreta")
    st.stop()

# ── Main App ─────────────────────────────────────────────────────────────
# Faixa branca ocupando toda a largura do conteudo, com o logo centralizado.
# O logo usado e' o de texto preto, porque o fundo da faixa e' branco.
_logo_b64 = base64.b64encode(
    (Path(__file__).parent / "logo-silvaleal-preto.png").read_bytes()
).decode()

st.markdown(
    f"""
    <style>
      .sl-logo-band {{
          width: 100%;
          background: #ffffff;
          border-radius: 8px;
          padding: 1.25rem 0;
          margin-bottom: 1rem;
          text-align: center;
      }}
      .sl-logo-band img {{ height: 130px; }}
    </style>
    <div class="sl-logo-band">
      <img src="data:image/png;base64,{_logo_b64}" alt="Silva Leal Distribuidora">
    </div>
    """,
    unsafe_allow_html=True,
)

st.set_page_config(
    page_title="Easy Pallet – Silva Leal Dashboard",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded",
)


image_url_sidebar = "https://easypallet.com.br/assets/imgs/logos/logo_easypallet.png"
st.sidebar.image(image_url_sidebar, caption=' ', width=250)



# define navigation pages explicitly
pages = [
    st.Page("pages/painel_geral.py", title="📊  Painel Geral"),
    st.Page("pages/painel_montagem.py", title="🔧  Painel Montagem"),
    st.Page("pages/painel_conferencia.py", title="✅  Painel Conferência"),
    st.Page("pages/painel_erros.py", title="⚠️  Painel Erros"),
    st.Page("pages/painel_operacoes.py", title="⏱️  Painel Operações"),
]

current = st.navigation(pages)
current.run()

