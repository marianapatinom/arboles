# Ecosistema Profesional de Clasificación Botánica: Árbol de Decisión ID3 (Dataset Iris)

Este repositorio contiene la transformación integral de un notebook educativo de Machine Learning en un **entorno empresarial estructurado, documentado y de alto rendimiento**, alineado bajo la metodología internacional **CRISP-ML**.

La solución incluye un portal web de presentación (landing page) con diseño de noche tecnológica, una memoria técnica académica de nivel universitario autogenerada en Word (.docx) y una aplicación interactiva premium basada en Streamlit con explicabilidad visual.

---

## 🌟 Características Principales

*   **Lógica de Caja Blanca (ID3):** Implementación de un clasificador de árbol de decisión interpretable por expertos botánicos basado en entropía y ganancia de información.
*   **Exactitud Científica de Élite (96.67%):** Desempeño sobresaliente trazable en su totalidad con los resultados originales del notebook.
*   **Generador Automático de Word (.docx):** Script de compilación premium en Python utilizando `python-docx` para renderizar el informe académico formateado, con portadas, tablas elegantes y gráficos integrados de forma automática.
*   **Dashboard Interactivo en Streamlit:** Herramienta analítica con carga inteligente de datos, gráficos EDA dinámicos, modificación interactiva de hiperparámetros en tiempo real, métricas KPI y una consola de predicción espacial 2D explicable.
*   **Landing Page de Noche Tecnológica:** Portal de difusión web estático responsivo, implementado en HTML5, CSS3 y JS, con efectos de *glassmorphism*, menú lateral activo flotante y contadores animados de KPIs.

---

## 📁 Estructura del Ecosistema

```text
Seguimiento3/
├── .venv/                         # Entorno virtual de Python (local)
├── Imágenes/                      # Recursos gráficos y diagramas del proyecto
│   ├── GraficoBarras.png          # Gráfico de balance de clases
│   ├── MatrizConfusion.png        # Evidencia de validación científica
│   ├── VisualizaacionArbol.png    # Estructura del árbol aprendido
│   └── Infog.png                  # Infografía de apoyo y banner principal
├── Proyecto/
│   ├── Material_1_Proyecto_IA_Talento_Tech.docx  # Reporte de Word premium compilado
│   ├── Memoria_Tecnica.md         # Memoria técnica académica de alta calidad
│   └── generate_docx.py           # Script automatizado de renderizado de Word
├── landing/                       # Portal Web Corporativo (SPA)
│   ├── index.html                 # Estructura de landing page responsiva
│   ├── styles.css                 # Diseño oscuro con glassmorphism y Google Fonts
│   └── script.js                  # Control de scroll spy y contadores dinámicos
├── app.py                         # Dashboard interactivo en Streamlit
├── CRISP-ML.md                    # Documentación exhaustiva del ciclo de vida de ML
├── Tutorial.md                    # Guía de reproducción paso a paso para usuarios
└── requirements.txt               # Paquetes requeridos en el entorno
```

---

## 🛠️ Tecnologías Utilizadas

*   **Análisis y Manipulación de Datos:** Python 3, Pandas, NumPy.
*   **Machine Learning y Modelado:** Scikit-Learn (`DecisionTreeClassifier`).
*   **Gráficos Científicos:** Matplotlib, Seaborn (pairplots, heatmaps, boxplots).
*   **Despliegue y Dashboard:** Streamlit.
*   **Generación de Documentos:** Python-Docx (estructuras y bordes XML personalizados).
*   **Aesthetics de la Web:** HTML5 Semántico, CSS3 Vanilla (Glassmorphism, Flexbox, Grids, Google Fonts: Outfit/Inter), JS nativo (Intersection Observer, requestAnimationFrame).

---

## 🚀 Instalación y Puesta en Marcha

### 1. Clonación y Entorno Virtual
Se recomienda la creación de un entorno virtual limpio para evitar conflictos de librerías:

```bash
# Crear entorno virtual en Windows
python -m venv .venv

# Activar el entorno virtual
.venv\Scripts\activate
```

### 2. Instalar Dependencias
Instale los paquetes especificados en el manifiesto de requerimientos:

```bash
pip install -r requirements.txt
```

---

## 💻 Instrucciones de Ejecución

### A. Ejecutar el Dashboard en Streamlit (Producción)
Abra una consola en la raíz de la carpeta y ejecute:

```bash
streamlit run app.py
```
*Se abrirá automáticamente una ventana en su navegador predeterminado (por defecto en `http://localhost:8501`).*

### B. Compilar el Reporte Word Premium (.docx)
Para renderizar y actualizar el documento de Word final directamente a partir de la memoria técnica en Markdown, ejecute:

```bash
# Asegúrese de tener Microsoft Word cerrado antes de ejecutar
.venv\Scripts\python.exe Proyecto/generate_docx.py
```
*Esto actualizará el archivo `Proyecto/Material_1_Proyecto_IA_Talento_Tech.docx` insertando textos estilizados, tablas y los diagramas gráficos.*

### C. Visualizar la Landing Page Web
Para explorar el portal interactivo corporativo, simplemente navegue a la carpeta `landing/` y abra el archivo `index.html` en cualquier navegador web moderno (Chrome, Edge, Firefox, Safari). *No requiere servidores ni dependencias externas.*

---

## 🎯 Resumen de Métricas del Modelo

*   **Exactitud en Prueba (Accuracy):** **96.67%** (29/30 aciertos).
*   **Rendimiento en Iris-setosa:** 100% Precision, 100% Recall.
*   **Rendimiento en Iris-versicolor:** 100% Precision, 92% Recall (1 error).
*   **Rendimiento en Iris-virginica:** 90% Precision, 100% Recall.
*   **Diagnóstico del Error:** Muestra de test número 77 (Real: *versicolor*, Predicho: *virginica*) debido a que sus pétalos excedieron el umbral físico regular de 1.75 cm aprendido por el árbol de decisión.
