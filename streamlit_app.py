import streamlit as st
from multiapp import MultiApp
from apps import home


app = MultiApp()

st.markdown("""  #Inteligencia de negocios - Equipo A """)

# Add all your application here


app.add_app('Home',home.app)




# The main app
app.run()