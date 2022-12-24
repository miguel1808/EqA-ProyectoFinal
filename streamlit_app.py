import streamlit as st
from multiapp import MultiApp
from apps import home,EDA,transformacion,knn  # import your app modules here


app = MultiApp()

st.title("""  #Inteligencia de negocios - Equipo A """)

# Add all your application here


app.add_app('Home',home.app)
app.add_app('Análisis Exploratorio de Datos',EDA.app)
app.add_app('Transformación de datos',transformacion.app)
app.add_app('KNN',knn.app)



# The main app
app.run()