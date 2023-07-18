import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from streamlit.components.v1 import html
from bokeh.models.widgets import Div

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
    opt = ('', 'Gestione interna', 'Streamlit', 'Analisi finanziaria')
    option = st.selectbox('Scegli la formazione', opt)
    if option != '':
        st.write('You selected:', option)

if option != '':
    st.subheader('Stai vedendo la formazione di: ' + str(option))

    if option == 'Streamlit':
        if st.button('Vedi formazione'):
            js = "window.open('https://www.youtube.com/watch?v=RzyD08-w-tk&ab_channel=annalisaufficiale')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    
    if option == 'Gestione interna':
        if st.button('Vedi formazione'):
            js = "window.open('https://www.youtube.com/watch?v=RzyD08-w-tk&ab_channel=annalisaufficiale')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
        
     
    if option == 'Analisi finanziaria':
        if st.button('Vedi formazione'):
            js = "window.open('https://www.youtube.com/watch?v=RzyD08-w-tk&ab_channel=annalisaufficiale')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

    
else:
    st.subheader('Scegli la formazione che vuoi seguire')

