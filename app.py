import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# Configuración premium de la página de Streamlit
st.set_page_config(
    page_title="ID3 Iris Project Builder",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inyección de estilos CSS premium
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
    
    /* Configuración de fuentes y fondo */
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    /* Estilos personalizados para tarjetas de KPis y contenedores */
    .metric-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(11, 59, 58, 0.15);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        text-align: center;
        margin-bottom: 20px;
    }
    
    .metric-value {
        font-size: 2.2rem;
        font-weight: 700;
        color: #0B3B3A;
        margin: 5px 0;
    }
    
    .metric-label {
        font-size: 0.95rem;
        color: #666666;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Estilos para tarjetas de predicción */
    .pred-card-setosa {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        border-left: 6px solid #28a745;
        border-radius: 8px;
        padding: 15px 25px;
        color: #155724;
        font-weight: 600;
        font-size: 1.4rem;
        box-shadow: 0 4px 10px rgba(40, 167, 69, 0.15);
    }
    .pred-card-versicolor {
        background: linear-gradient(135deg, #fff3cd 0%, #ffeeba 100%);
        border-left: 6px solid #ffc107;
        border-radius: 8px;
        padding: 15px 25px;
        color: #856404;
        font-weight: 600;
        font-size: 1.4rem;
        box-shadow: 0 4px 10px rgba(255, 193, 7, 0.15);
    }
    .pred-card-virginica {
        background: linear-gradient(135deg, #cce5ff 0%, #b8daff 100%);
        border-left: 6px solid #007bff;
        border-radius: 8px;
        padding: 15px 25px;
        color: #004085;
        font-weight: 600;
        font-size: 1.4rem;
        box-shadow: 0 4px 10px rgba(0, 123, 255, 0.15);
    }

    /* Estilo de botones */
    .stButton>button {
        background: linear-gradient(135deg, #0B3B3A 0%, #2B7A78 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(11, 59, 58, 0.25) !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(11, 59, 58, 0.35) !important;
    }
</style>
""", unsafe_allow_html=True)

# Configuración del estilo de gráficos en Seaborn
sns.set_theme(style="white")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = '#333333'
plt.rcParams['axes.labelcolor'] = '#333333'
plt.rcParams['xtick.color'] = '#333333'
plt.rcParams['ytick.color'] = '#333333'

# Carga de datos con caché
@st.cache_data
def load_data():
    url = "https://www.openml.org/data/get_csv/61/dataset_61_iris.arff"
    dt = pd.read_csv(url)
    return dt

def main():
    dt = load_data()
    X = dt.drop('class', axis=1)
    y = dt['class']
    
    # División fija e inalterable del conjunto para trazabilidad con el notebook
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
    
    # SIDEBAR: Cabecera y Menú
    st.sidebar.markdown(
        "<div style='text-align: center; padding-bottom: 20px;'>"
        "<h2 style='color:#0B3B3A; font-weight:700; margin:0;'>🌸 Iris ID3 Builder</h2>"
        "<p style='color:#666; font-size:0.85rem;'>Ecosistema de ML Profesional</p>"
        "</div>", 
        unsafe_allow_html=True
    )
    
    menu = st.sidebar.radio(
        "Navegación del Ecosistema",
        [
            "✨ Presentación General", 
            "📊 Exploración de Datos", 
            "📈 Análisis Exploratorio (EDA)", 
            "🌳 Modelado e Interpretabilidad", 
            "🎯 Evaluación Científica", 
            "🔮 Predicción e Inteligencia"
        ]
    )
    
    # ------------------ PESTAÑA 1: PRESENTACIÓN GENERAL ------------------
    if menu == "✨ Presentación General":
        st.markdown("<h1 style='color:#0B3B3A; font-weight:700;'>Presentación del Proyecto</h1>", unsafe_allow_html=True)
        st.markdown("---")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("""
            ### Asistente Botánico Automatizado
            Este ecosistema transforma un notebook educativo de Machine Learning en un **entorno empresarial interactivo y documentado de nivel académico superior**, fundamentado en la metodología estructurada **CRISP-ML**.
            
            El corazón del proyecto es el algoritmo de **Árbol de Decisión ID3** (Iterative Dichotomiser 3), implementado mediante entropía y ganancia de información. A diferencia de las complejas 'cajas negras', este modelo de 'caja blanca' genera reglas de negocio explícitas y auditables para botánicos e investigadores.
            
            #### Objetivos Clave:
            *   **Automatización:** Reducir el tiempo de catalogación botánica en más de un 90%.
            *   **Fiabilidad:** Garantizar una exactitud superior al 95% (Métricas reales: **96.67%**).
            *   **Interpretabilidad:** Extraer de forma transparente las reglas morfológicas divisorias de especies del género *Iris*.
            """)
            
            st.info(
                "💡 **Dato Histórico:** El dataset Iris fue publicado originalmente en 1936 por el célebre genetista y estadístico británico **Ronald Fisher** y es, hasta el día de hoy, el conjunto de referencia académica más popular de clasificación de datos morfológicos."
            )
            
        with col2:
            st.image('Imágenes/Infog.png', caption='Especies de flores de Iris (Setosa, Versicolor, Virginica)', use_container_width=True)
            
        st.markdown("### Ciclo del Proyecto (CRISP-ML)")
        
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">1. Comprensión</div>
                <div style="font-size: 1.1rem; font-weight:600; color:#0B3B3A; margin-top:8px;">Definición del Problema</div>
                <p style="font-size:0.85rem; color:#666;">Clasificar especies de Iris basándose en variables morfológicas interpretables.</p>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">2. Preparación</div>
                <div style="font-size: 1.1rem; font-weight:600; color:#0B3B3A; margin-top:8px;">Calidad y Partición</div>
                <p style="font-size:0.85rem; color:#666;">150 muestras balanceadas sin nulos. Partición 80/20 reproducible (random_state=1).</p>
            </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">3. Modelado</div>
                <div style="font-size: 1.1rem; font-weight:600; color:#0B3B3A; margin-top:8px;">ID3 por Entropía</div>
                <p style="font-size:0.85rem; color:#666;">Entrenamiento de árboles de decisión basados en ganancia de información.</p>
            </div>
            """, unsafe_allow_html=True)
        with c4:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">4. Evaluación</div>
                <div style="font-size: 1.1rem; font-weight:600; color:#0B3B3A; margin-top:8px;">Rendimiento del 96.67%</div>
                <p style="font-size:0.85rem; color:#666;">Un único error de validación debido a solapamiento morfológico natural.</p>
            </div>
            """, unsafe_allow_html=True)

    # ------------------ PESTAÑA 2: EXPLORACIÓN DE DATOS ------------------
    elif menu == "📊 Exploración de Datos":
        st.markdown("<h1 style='color:#0B3B3A; font-weight:700;'>Exploración General del Dataset</h1>", unsafe_allow_html=True)
        st.markdown("---")
        
        st.write("El conjunto de datos cargado contiene **150 instancias** distribuidas de forma balanceada con **50 muestras por especie**.")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.subheader("Visualización del Dataset (Muestra de Filas)")
            # Slider para ver cuántas filas mostrar
            rows_to_show = st.slider("Filas a visualizar", min_value=5, max_value=150, value=15)
            st.dataframe(dt.head(rows_to_show), use_container_width=True)
            
            # Botón para descargar el dataset
            csv = dt.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Descargar Dataset Completo en CSV",
                data=csv,
                file_name='iris_dataset.csv',
                mime='text/csv',
            )
            
        with col2:
            st.subheader("Estadísticas Descriptivas Generales")
            st.dataframe(dt.describe().T, use_container_width=True)
            
            st.subheader("Balanceo de Clases")
            # Gráfico de barras de balance de clases
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.countplot(data=dt, x='class', palette=['#0B3B3A', '#2B7A78', '#3A6073'], ax=ax)
            ax.set_title("Cantidad de Instancias por Especie", fontsize=11, fontweight='bold', pad=10)
            ax.set_xlabel("Especie", fontsize=9)
            ax.set_ylabel("Muestras", fontsize=9)
            sns.despine()
            st.pyplot(fig)

    # ------------------ PESTAÑA 3: ANÁLISIS EXPLORATORIO (EDA) ------------------
    elif menu == "📈 Análisis Exploratorio (EDA)":
        st.markdown("<h1 style='color:#0B3B3A; font-weight:700;'>Análisis Exploratorio de Datos (EDA)</h1>", unsafe_allow_html=True)
        st.markdown("---")
        
        st.write("Visualice las relaciones físicas y morfológicas entre las variables predictoras del pétalo y del sépalo agrupadas por clase botánica.")
        
        eda_menu = st.tabs(["📊 Distribución y Densidad", "📦 Boxplots y Outliers", "📌 Gráfico de Dispersión 2D"])
        
        # Sub-pestaña 1: Densidades e histogramas
        with eda_menu[0]:
            st.subheader("Distribución de Densidad de Características")
            feature_selected = st.selectbox("Seleccione la variable a analizar", list(X.columns))
            
            fig, ax = plt.subplots(figsize=(8, 4))
            sns.kdeplot(data=dt, x=feature_selected, hue='class', fill=True, alpha=0.4, palette=['#0B3B3A', '#2B7A78', '#d9534f'], ax=ax)
            ax.set_title(f"Función de Densidad para: {feature_selected}", fontsize=11, fontweight='bold')
            ax.set_xlabel(feature_selected + " (cm)")
            ax.set_ylabel("Densidad")
            sns.despine()
            st.pyplot(fig)
            
        # Sub-pestaña 2: Boxplots
        with eda_menu[1]:
            st.subheader("Comparación de Rangos y Valores Atípicos")
            box_feature = st.selectbox("Seleccione la característica para Boxplot", list(X.columns), key="box")
            
            fig, ax = plt.subplots(figsize=(8, 4.5))
            sns.boxplot(data=dt, x='class', y=box_feature, palette=['#0B3B3A', '#2B7A78', '#3A6073'], width=0.5, ax=ax)
            sns.stripplot(data=dt, x='class', y=box_feature, color='black', alpha=0.3, size=4, jitter=0.1, ax=ax)
            ax.set_title(f"Distribución Morfológica: {box_feature} por Especie", fontsize=11, fontweight='bold')
            ax.set_xlabel("Clase")
            ax.set_ylabel(box_feature + " (cm)")
            sns.despine()
            st.pyplot(fig)
            
        # Sub-pestaña 3: Dispersión 2D
        with eda_menu[2]:
            st.subheader("Fronteras de Decisión en Espacio Bidimensional")
            x_feat = st.selectbox("Variable del eje X", list(X.columns), index=2)
            y_feat = st.selectbox("Variable del eje Y", list(X.columns), index=3)
            
            fig, ax = plt.subplots(figsize=(8, 4.5))
            sns.scatterplot(data=dt, x=x_feat, y=y_feat, hue='class', palette=['#0B3B3A', '#2B7A78', '#d9534f'], s=80, alpha=0.8, ax=ax)
            ax.set_title(f"Dispersión: {y_feat} vs {x_feat}", fontsize=11, fontweight='bold')
            ax.set_xlabel(x_feat + " (cm)")
            ax.set_ylabel(y_feat + " (cm)")
            sns.despine()
            st.pyplot(fig)
            st.markdown(
                "💡 **Observación:** Al graficar el largo vs ancho del pétalo se aprecia una **separación lineal limpia y perfecta** para la especie *Setosa*, mientras que *Versicolor* y *Virginica* comparten fronteras de dispersión cercanas en la zona de transición."
            )

    # ------------------ PESTAÑA 4: MODELADO E INTERPRETABILIDAD ------------------
    elif menu == "🌳 Modelado e Interpretabilidad":
        st.markdown("<h1 style='color:#0B3B3A; font-weight:700;'>Entrenamiento e Interpretabilidad (ID3)</h1>", unsafe_allow_html=True)
        st.markdown("---")
        
        st.write("Configure los parámetros lógicos del clasificador y observe cómo se entrena y ramifica el árbol de decisión en tiempo real.")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("Configuración de Hiperparámetros")
            max_depth = st.slider("Profundidad Máxima del Árbol (max_depth)", min_value=1, max_value=10, value=4)
            min_samples_split = st.slider("Muestras Mínimas por División (min_samples_split)", min_value=2, max_value=10, value=2)
            
            # Modelo dinámico según los parámetros ingresados por el usuario
            clf = DecisionTreeClassifier(
                criterion='entropy', 
                max_depth=max_depth, 
                min_samples_split=min_samples_split, 
                random_state=1
            )
            clf.fit(X_train, y_train)
            
            st.success("✅ Modelo entrenado exitosamente.")
            
            st.subheader("Importancia de Variables (ID3)")
            # Importancia de variables calculada
            fi = pd.Series(clf.feature_importances_, index=X.columns).sort_values(ascending=True)
            
            fig, ax = plt.subplots(figsize=(5, 3.5))
            fi.plot(kind='barh', color='#2B7A78', ax=ax)
            ax.set_title("Ganancia de Información Relativa", fontsize=10, fontweight='bold')
            ax.set_xlabel("Peso de Importancia")
            sns.despine()
            st.pyplot(fig)
            st.markdown("<p style='font-size:0.85rem; color:#666;'>El **ancho del pétalo (petalwidth)** concentra la mayor ganancia de información.</p>", unsafe_allow_html=True)
            
        with col2:
            st.subheader("Estructura de Reglas Lógicas del Árbol")
            # Graficar el árbol
            fig2, ax2 = plt.subplots(figsize=(10, 8.5))
            plot_tree(
                clf, 
                filled=True, 
                rounded=True, 
                feature_names=X.columns, 
                class_names=clf.classes_, 
                ax=ax2,
                fontsize=8
            )
            st.pyplot(fig2)
            st.caption("Visualización interactiva de la estructura de nodos divisores, entropía interna y clases resultantes del modelo ID3.")

    # ------------------ PESTAÑA 5: EVALUACIÓN CIENTÍFICA ------------------
    elif menu == "🎯 Evaluación Científica":
        st.markdown("<h1 style='color:#0B3B3A; font-weight:700;'>Evaluación Científica de Resultados</h1>", unsafe_allow_html=True)
        st.markdown("---")
        
        # Entrenamiento fijo e inalterable (reproducibilidad estricta con el notebook original)
        clf_fixed = DecisionTreeClassifier(criterion='entropy', random_state=1)
        clf_fixed.fit(X_train, y_train)
        y_pred = clf_fixed.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Exactitud en Test</div>
                <div class="metric-value">{acc*100:.2f}%</div>
                <p style="font-size:0.8rem; color:#28a745; font-weight:600;">29 de 30 Aciertos</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">Muestras Entrenadas</div>
                <div class="metric-value">120</div>
                <p style="font-size:0.8rem; color:#666;">80% del Dataset Total</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">Impureza Promedio</div>
                <div class="metric-value">0.0</div>
                <p style="font-size:0.8rem; color:#007bff; font-weight:600;">Hojas Entropía Cero</p>
            </div>
            """, unsafe_allow_html=True)
            
        c1, c2 = st.columns(2)
        
        with c1:
            st.subheader("Matriz de Confusión en Validación")
            cm = confusion_matrix(y_test, y_pred)
            
            fig, ax = plt.subplots(figsize=(6, 4.5))
            sns.heatmap(cm, annot=True, fmt='d', cmap='crest', xticklabels=clf_fixed.classes_, yticklabels=clf_fixed.classes_, ax=ax, cbar=False)
            ax.set_title("Mapeo de Aciertos vs Predicciones", fontsize=11, fontweight='bold', pad=12)
            ax.set_ylabel("Clase Real")
            ax.set_xlabel("Clase Predicha")
            st.pyplot(fig)
            
            st.warning(
                "🔍 **Diagnóstico del Error:** Existe un único error de validación. Una flor clasificada realmente como **Iris-versicolor** fue predicha como **Iris-virginica** (índice 77 del notebook) debido a que su ancho de pétalo superaba la frontera lógica natural."
            )
            
        with c2:
            st.subheader("Reporte de Clasificación Académico")
            
            # Obtener el reporte formateado como DataFrame
            report_dict = classification_report(y_test, y_pred, output_dict=True)
            report_df = pd.DataFrame(report_dict).T
            # Formatear números
            st.dataframe(report_df.style.format(precision=2), use_container_width=True)
            
            st.subheader("Trazabilidad con Imágenes del Notebook")
            st.image('Imágenes/MatrizConfusion.png', caption='Evidencia: Matriz de confusión e informe original extraídos del notebook', width=400)

    # ------------------ PESTAÑA 6: PREDICCIÓN E INTELIGENCIA ------------------
    elif menu == "🔮 Predicción e Inteligencia":
        st.markdown("<h1 style='color:#0B3B3A; font-weight:700;'>Predicción Botánica Explicable</h1>", unsafe_allow_html=True)
        st.markdown("---")
        
        # Modelo fijo e inalterable para predecir
        clf_pred = DecisionTreeClassifier(criterion='entropy', random_state=1)
        clf_pred.fit(X_train, y_train)
        
        st.write("Ingrese las dimensiones morfológicas recolectadas y descubra la especie correspondiente con justificación espacial en tiempo real.")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("Entrada de Mediciones Anatómicas")
            
            sepallength = st.slider("Longitud del Sépalo (sepallength) [cm]", min_value=4.0, max_value=8.0, value=5.8, step=0.1)
            sepalwidth = st.slider("Ancho del Sépalo (sepalwidth) [cm]", min_value=2.0, max_value=4.5, value=3.0, step=0.1)
            petallength = st.slider("Longitud del Pétalo (petallength) [cm]", min_value=1.0, max_value=7.0, value=3.8, step=0.1)
            petalwidth = st.slider("Ancho del Pétalo (petalwidth) [cm]", min_value=0.1, max_value=2.5, value=1.2, step=0.1)
            
            input_data = pd.DataFrame(
                [[sepallength, sepalwidth, petallength, petalwidth]], 
                columns=['sepallength', 'sepalwidth', 'petallength', 'petalwidth']
            )
            
            st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
            
        with col2:
            st.subheader("Diagnóstico y Explicabilidad Espacial")
            
            # Predecir de inmediato
            prediction = clf_pred.predict(input_data)[0]
            
            # Mostrar tarjeta de color premium según la clase
            if prediction == "Iris-setosa":
                st.markdown('<div class="pred-card-setosa">🌸 Especie Predicha: <b>Iris-setosa</b></div>', unsafe_allow_html=True)
            elif prediction == "Iris-versicolor":
                st.markdown('<div class="pred-card-versicolor">🌸 Especie Predicha: <b>Iris-versicolor</b></div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="pred-card-virginica">🌸 Especie Predicha: <b>Iris-virginica</b></div>', unsafe_allow_html=True)
                
            st.write("")
            st.write("A continuación, se representa el **espacio bidimensional de características del dataset** (Petal Length vs Petal Width). La estrella de color rojo indica la **posición exacta** del ejemplar que acaba de ingresar, demostrando a qué clúster espacial pertenece:")
            
            # Graficar posición del punto ingresado por el usuario
            fig, ax = plt.subplots(figsize=(7, 4))
            sns.scatterplot(
                data=dt, 
                x='petallength', 
                y='petalwidth', 
                hue='class', 
                palette=['#0B3B3A', '#2B7A78', '#d9534f'], 
                alpha=0.6, 
                s=40, 
                ax=ax
            )
            # Agregar el punto ingresado por el usuario
            ax.scatter(petallength, petalwidth, color='red', marker='*', s=300, edgecolor='black', label='Tu Muestra')
            ax.set_xlabel("Longitud del Pétalo (cm)")
            ax.set_ylabel("Ancho del Pétalo (cm)")
            ax.set_title("Ubicación de tu Muestra en el Espacio de Características", fontsize=10, fontweight='bold')
            ax.legend()
            sns.despine()
            st.pyplot(fig)

if __name__ == '__main__':
    main()
