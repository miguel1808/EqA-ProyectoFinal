import streamlit as st
import pandas as pd
import seaborn as sns
import statistics as stats
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches

plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler 
from sklearn.metrics import accuracy_score



def app():
    # Import Dataset
    st.title('K-Nearest Neighbors (KNN)')
    st.subheader('Import Dataset')
    url='https://drive.google.com/file/d/1uDdI0Uh7DBa-1OTywteqoz6MLjpboD-t/view?usp=sharing'
    url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    df = pd.read_csv(url)
    st.write(df.head())

    st.subheader('Dropeamos la columna Unnamed: 0')
    df = df.drop(labels='Unnamed: 0', axis=1)
    st.write(df.columns)
    st.write(df.dtypes)

    st.subheader('Division en conjunto de entrenamiento y prueba')

    target="MEDIO"
    x = df.drop(target, axis=1)
    y = df[target]
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size = 0.2, random_state = 42)
    st.write("Valores de y_train:")
    st.write(y_train.value_counts())
    # check the shape of X_train and X_test
    st.subheader('Dimensiones de los conjuntos de x_train y x_test')
    st.write("X_train shape:", x_train.shape)
    st.write("X_test shape:", x_test.shape)

    fig=plt.figure(figsize=(16, 9))
    sns.countplot(y=y_train,data=df,palette='mako_r')
    plt.ylabel('MEDIO')
    plt.xlabel('Total')
    plt.title('Distribucion de los datos de entrenamiento')
    st.pyplot(plt.gcf())

    st.header('Entrenamiento')
    # Crear una instancia del modelo KNN
    knn = KNeighborsClassifier(n_neighbors=6)

    # Entrenar el modelo con el conjunto de datos de entrenamiento
    knn.fit(x_train, y_train)

    # Hacer predicciones con el conjunto de datos de prueba
    y_pred = knn.predict(x_test)

    # Calcular el rendimiento del modelo
    st.subheader('Reporte de clasificación para el modelo KNN con k=6:')
    st.write(classification_report(y_test, y_pred))
    st.subheader('Matriz de confusión para el modelo KNN con k=6:')
    st.write(confusion_matrix(y_test, y_pred))


    RFAcc = accuracy_score(y_pred,y_test)
    st.subheader('Accuracy del modelo KNN con k=6:')
    st.write('El accuracy del modelo KNN es : {:.2f}%'.format(RFAcc*100))

    st.subheader('Grafico de la matriz de confusión para el modelo KNN con k=6:')
    fig=plt.figure(figsize=(16, 9))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='g')
    st.pyplot(plt.gcf())







