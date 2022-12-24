import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.model_selection import train_test_split


def app():
    st.title('Support Vector Classifier (SVC)')


    # Para carga rapida
    url='https://drive.google.com/file/d/1uDdI0Uh7DBa-1OTywteqoz6MLjpboD-t/view?usp=sharing'
    url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    df = pd.read_csv(url)
    df = df.drop(labels='Unnamed: 0', axis=1)

    st.write(df.head())

    st.subheader('Division en conjunto de entrenamiento y prueba')
    st.code("""X = df[['UNIDAD', 'CASO', 'MEDIO', 'ZONA', 'SUB ZONA', 'TIPO OPERADOR']]
    y = df['MEDIO']""", language='python')
    X = df[['UNIDAD', 'CASO', 'MEDIO', 'ZONA', 'SUB ZONA', 'TIPO OPERADOR']]
    y = df['MEDIO']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    st.code("""X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)""", language='python')


    st.subheader('Entrenamiento del modelo')
    SVC_model = SVC(max_iter=55)
    SVC_model.fit(X_train,y_train)
    st.code("""SVC_model = SVC(max_iter=55)""", language='python')
    st.code("""SVC_model.fit(X_train,y_train)""", language='python')
    st.write('Modelo entrenado:' ,SVC_model)


    st.subheader('Predicciones y evaluacion')
    y_pred = SVC_model.predict(X_test)
    st.write('matriz de confusion')
    st.write(confusion_matrix(y_test, y_pred))
    st.write('Reporte de clasificacion')
    st.write(classification_report(y_test, y_pred))