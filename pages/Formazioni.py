import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

st.set_page_config(page_title='E-learning', layout = 'wide', page_icon = '📖', initial_sidebar_state = 'auto')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.title('📖 E-learning')


st.sidebar.title("Elenco formazioni")

option = ''
with st.sidebar:
    opt = ('', 'Gestione interna', 'Streamlit', 'Analisi finanziaria', 'Analisi di mercato')
    option = st.selectbox('Scegli la formazione', opt)
    if option != '':
        st.write('You selected:', option)

if option != '':
    st.subheader('Stai vedendo la formazione di: ' + str(option))
else:
    st.subheader('Scegli la formazione che vuoi seguire')

    