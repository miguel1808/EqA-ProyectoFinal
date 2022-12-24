import streamlit as st
import pandas as pd
import numpy as np


def app():
    st.title('Transformacion de datos')
    st.code('''df = pd.read_excel("./result.xlsx", sheet_name='sheet1') ''', language='python')
    df = pd.read_excel("./result.xlsx", sheet_name='sheet1')
    st.write(df.head())

    

    st.header('Transformacion de atributos categoricos')
    st.subheader("a. Categoria Medio de reporte")
    labels_medio = df['MEDIO'].astype('category').cat.categories.tolist()
    map_medio = {'MEDIO' : {k: v for k,v in zip(labels_medio,list(range(0,len(labels_medio)+1)))}}
    st.write(map_medio)

    st.write("Resultado:")
    df.replace(map_medio,inplace=True) 
    st.write(df.head())

    st.subheader("b. Categoría Zona de Incidencia")
    labels_zona = df['ZONA'].astype('category').cat.categories.tolist()
    map_zona = {'ZONA' : {k: v for k,v in zip(labels_zona,list(range(0,len(labels_zona)+1)))}}
    st.write(map_zona)

    st.write("Resultado:")
    df.replace(map_zona,inplace=True)
    st.write(df.head())

    st.subheader("c. Categoría Caso")
    labels_caso = df['CASO'].astype('category').cat.categories.tolist()
    map_caso = {'CASO' : {k: v for k,v in zip(labels_caso,list(range(0,len(labels_caso)+1)))}}
    st.write(map_caso)

    st.write("Resultado:")
    df.replace(map_caso,inplace=True)
    st.write(df.head())

    st.subheader("d. Categoría Subcaso")
    labels_subcaso = df['SUBCASO'].astype('category').cat.categories.tolist()
    map_subcaso = {'SUBCASO' : {k: v for k,v in zip(labels_subcaso,list(range(0,len(labels_subcaso)+1)))}}
    st.write(map_subcaso)
    
    st.write("Resultado:")
    df.replace(map_subcaso,inplace=True)
    st.write(df.head())

    st.subheader("e. Categoría Severidad")
    labels_severidad = df['SEVERIDAD'].astype('category').cat.categories.tolist()
    map_severidad = {'SEVERIDAD' : {k: v for k,v in zip(labels_severidad,list(range(0,len(labels_severidad)+1)))}}
    st.write(map_severidad)

    st.write("Resultado:")
    df.replace(map_severidad,inplace=True)
    st.write(df.head())

    st.subheader("f. Categoría Unidad")
    labels_unidad = df['UNIDAD'].astype('category').cat.categories.tolist()
    map_unidad = {'UNIDAD' : {k: v for k,v in zip(labels_unidad,list(range(0,len(labels_unidad)+1)))}}
    st.write(map_unidad)

    st.write("Resultado:")
    df.replace(map_unidad,inplace=True)
    st.write(df.head())

    st.subheader("g. Categoría Modalidad")
    labels_mod = df['MODALIDAD'].astype('category').cat.categories.tolist()
    map_mod = {'MODALIDAD' : {k: v for k,v in zip(labels_mod,list(range(0,len(labels_mod)+1)))}}
    st.write(map_mod)

    st.write("Resultado:")
    df.replace(map_mod,inplace=True)
    st.write(df.head())

    st.subheader("h. Categoría día de incidencia")
    labels_dia = df['DIA INCIDENCIA'].astype('category').cat.categories.tolist()
    map_dia = {'DIA INCIDENCIA' : {k: v for k,v in zip(labels_dia,list(range(0,len(labels_dia)+1)))}}
    st.write(map_dia)

    st.write("Resultado:")
    df.replace(map_dia,inplace=True)
    st.write(df.head())


    