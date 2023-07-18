import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



# Use the application default credentials
# if not firebase_admin._apps:
#     cred = credentials.Certificate('reneud-80109-firebase-adminsdk-qvjw8-a1a4d6315a.json')
#    firebase_admin.initialize_app(cred)
#db = firestore.client()


st.set_page_config(page_title='E-learning', layout = 'wide', page_icon = '📖', initial_sidebar_state = 'auto')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if True:
    def add_bg_from_url():
            st.markdown(
                f"""
                <style>
                .stApp {{
                    background-image: url("https://www.atulhost.com/wp-content/uploads/2017/11/elearning.jpg");
                    background-attachment: fixed;
                    background-size: cover
                }}
                </style>
                """,
                unsafe_allow_html=True
            )

    add_bg_from_url()



st.markdown('''
    <div style="display: flex; width: 100%; height: 100vh; flex-direction: column; align-items: flex-start; ">
        <h1 style="color: #F0F0F0;">Bentornat* _________ </h1>
        <p style="margin-left: 0px;">
            Questa è la tua piattaforma di e-learning, qui potrai trovare tutti i corsi Jesap disponibili.
        </p>
    </div>
''', unsafe_allow_html=True)

