import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px




def app():
    st.title('Análisis Exploratorio de Datos')

    archivo='result.xlsx'
    df=pd.read_excel(archivo,sheet_name='sheet1')
    st.write(df.head())

    st.subheader('Recopilacion de casos por dias de la semana')
    inc=pd.value_counts(df['DIA INCIDENCIA'])
    st.write(inc)
    st.write(type(inc))

    st.subheader('Frecuencia absoluta y relativa de casos por dia de la semana')
    inc = pd.DataFrame(inc)
    inc.columns = ["Frec_abs"]
    inc["Frec_rel_%"] = 100*inc["Frec_abs"] / len(df)
    valor_ac=0

    Frec_rel_val=inc["Frec_rel_%"].values

    for i in Frec_rel_val:
        valor_ac=valor_ac+i
    st.write(inc)

    fig=px.pie(inc,values='Frec_rel_%',names=inc.index,title='Frecuencia absoluta de casos por dia de la semana')
    st.plotly_chart(fig)

    st.subheader('Recuento de casos por modalidad')
    medio = pd.value_counts(df['MEDIO'])

    st.write(medio)
    st.write(type(medio))

    st.subheader('Frecuencia absoluta y relativa de casos por modalidad')
    medio = pd.DataFrame(medio)
    medio.columns = ["Frec_abs"]
    medio["Frec_rel_%"] = 100*medio["Frec_abs"]/len(df)
    valor_ac=0

    Frec_rel_val=inc["Frec_rel_%"].values

    for i in Frec_rel_val:
        valor_ac=valor_ac+i
    st.write(medio)

    st.write("Grafico tipo pie")
    fig=px.pie(medio,values='Frec_rel_%',names=medio.index,title='Registros por modalidad de Incidencia')

    st.plotly_chart(fig)

    st.subheader('Recuento de casos por Zona')
    inc = pd.value_counts(df['ZONA'])
    st.write(inc)

    st.write(type(inc))

    inc=pd.DataFrame(inc)
    inc.columns = ["Frec_abs"]
    inc["Frec_rel_%"] = 100*inc["Frec_abs"] / len(df)
    valor_ac=0

    Frec_rel_val = inc["Frec_rel_%"].values

    for i in Frec_rel_val:
        valor_ac = valor_ac+i
    st.write(inc)

    fig=px.pie(inc,values='Frec_rel_%',names=inc.index,title='Frecuencia absoluta de casos por zona')
    st.plotly_chart(fig)


    st.subheader('Recuento de casos por tipo de delito')
    case = pd.value_counts(df['CASO'])
    st.write(case)
    st.write(type(case))

    st.write("Grafico de barras")
    plt.figure(figsize=(10,5))
    fig=px.bar(case,x=case.index,y=case.values,title='Registros por tipo de delito')
    st.plotly_chart(fig)

    st.write("Grafico tipo displote")
    fx=plt.figure(figsize=(10,5))
    sns.displot(df['SUB ZONA'])
    st.pyplot(plt.gcf())

    fx1=plt.figure(figsize=(10,5))
    sns.lmplot(x='LONGITUD',y='SUB ZONA',data=df)
    st.pyplot(plt.gcf())

    st.subheader('Grafico de barras de casos por situacion')
    fx2=plt.figure(figsize=(10,5))
    sns.displot(df['SITUACION'],bins=1)
    st.pyplot(plt.gcf())



    