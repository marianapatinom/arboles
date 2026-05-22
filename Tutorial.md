# Tutorial Reproducible Paso a Paso: Árbol de Decisión ID3 sobre el Dataset Iris

Este tutorial didáctico está diseñado para guiar a estudiantes, botánicos y científicos de datos en la reproducción completa y paso a paso del proyecto, partiendo desde el notebook científico original hasta el despliegue e integración en producción.

---

## Prerrequisitos

Para completar este tutorial, asegúrese de tener instalado:
*   **Python 3.8 o superior**
*   Consola de comandos (PowerShell en Windows, Terminal en Linux/macOS)
*   Editor de código (VS Code, Jupyter Notebook o Google Colab)

---

## Paso 1: Configuración del Entorno de Trabajo

Es una buena práctica aislar el proyecto en un entorno virtual propio:

```bash
# 1. Crear el entorno virtual en el directorio raíz
python -m venv .venv

# 2. Activar el entorno en Windows
.venv\Scripts\activate

# Activar en Linux/macOS
source .venv/bin/activate

# 3. Instalar todas las librerías necesarias
pip install pandas numpy scikit-learn matplotlib seaborn streamlit python-docx
```

---

## Paso 2: Importación de Librerías Científicas

Cree un archivo de script Python (`main.py` o ejecute una celda en su notebook) e importe las dependencias fundamentales:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Componentes de modelado de Scikit-Learn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
```

---

## Paso 3: Carga y Exploración Inicial de Datos

Cargaremos el conjunto de datos clásico "Iris" directamente desde su repositorio oficial en OpenML y realizaremos una inspección de sus dimensiones:

```python
# Definición de la URL del dataset en formato CSV
url = "https://www.openml.org/data/get_csv/61/dataset_61_iris.arff"

# Carga de datos con Pandas
dt = pd.read_csv(url)

# Inspección de las dimensiones (filas, columnas)
print("Dimensiones del dataset:", dt.shape)  # Debe imprimir (150, 5)

# Visualización de las primeras 5 instancias
print(dt.head())
```

---

## Paso 4: Preparación y División del Dataset

Para validar que nuestro modelo sea robusto ante datos nuevos, debemos separar los datos en dos subconjuntos: uno para el entrenamiento (80%) y otro para la validación (20%):

```python
# Separación de características predictoras (X) y etiqueta de especie (y)
X = dt.drop('class', axis=1)
y = dt['class']

# Partición aleatoria reproducible (random_state=1)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=1
)

print(f"Muestras de entrenamiento: {len(X_train)} | Muestras de prueba: {len(X_test)}")
```

---

## Paso 5: Entrenamiento del Árbol de Decisión (Algoritmo ID3)

Instanciaremos la clase `DecisionTreeClassifier` configurando el criterio en `'entropy'`. Esto emula el comportamiento de partición basado en **Entropía de Shannon** y **Ganancia de Información** del algoritmo clásico **ID3**:

```python
# Instanciación del clasificador
algorithm = DecisionTreeClassifier(criterion='entropy')

# Entrenamiento / Ajuste del modelo sobre el conjunto de entrenamiento
algorithm.fit(X_train, y_train)

print("¡Modelo ID3 entrenado con éxito!")
```

---

## Paso 6: Realización de Predicciones y Evaluación Científica

Evaluaremos la capacidad predictiva del modelo con el conjunto de prueba que este no ha visto durante el entrenamiento:

```python
# Realizar predicciones lógicas
y_pred = algorithm.predict(X_test)

# 1. Exactitud General (Accuracy)
acc = accuracy_score(y_test, y_pred)
print(f"Exactitud (Accuracy): {acc * 100:.2f}%")  # Debe reportar 96.67%

# 2. Matriz de Confusión
cm = confusion_matrix(y_test, y_pred)
print("\nMatriz de Confusión:")
print(cm)

# 3. Reporte de Clasificación Detallado
print("\nReporte de Clasificación Académico:")
print(classification_report(y_test, y_pred))
```

### 🔍 Diagnóstico Clínico del Error Singular
Al analizar la comparación entre `y_test` (valores reales) e `y_pred` (predichos por el árbol), se identifica un único error (acierto de 29/30):
*   La muestra con **índice de prueba 77** era realmente una ***Iris-versicolor***, pero fue predicha como ***Iris-virginica***.
*   **Justificación:** Esto se debe a que las variables morfológicas de este espécimen excedían los rangos típicos de su especie, cruzando el límite lógico de $1.75$ cm de ancho de pétalo establecido por el clasificador.

---

## Paso 7: Visualización Gráfica de las Reglas del Árbol

Una de las grandes virtudes de este clasificador es su interpretabilidad. Podemos exportar visualmente las reglas jerárquicas con el siguiente código:

```python
# Configuración del lienzo de Matplotlib
plt.figure(figsize=(10, 8))

# Graficar la estructura lógica aprendida
plot_tree(
    algorithm, 
    filled=True, 
    rounded=True, 
    feature_names=X.columns, 
    class_names=algorithm.classes_
)

# Guardar la imagen en el directorio
plt.savefig("Imágenes/VisualizacionArbol_reproducido.png", dpi=300)
plt.show()
```

---

## Paso 8: Despliegue del Entorno Interactivo (Streamlit)

Para poner a disposición de los usuarios botánicos nuestro modelo de forma interactiva:

1.  Asegúrese de contar con el archivo `app.py` configurado con la biblioteca Streamlit.
2.  Abra su terminal y ejecute el comando:
    ```bash
    streamlit run app.py
    ```
3.  Utilice los controles deslizantes para ingresar dimensiones personalizadas y compruebe la predicción espacial inmediata.

---

## Paso 9: Generación Automatizada del Reporte Word Premium

Para generar la memoria técnica académica en formato Word (.docx), sincronizada con las imágenes y tablas descriptivas:

1.  Cierre Microsoft Word en su sistema.
2.  Ejecute en la terminal:
    ```bash
    .venv\Scripts\python.exe Proyecto/generate_docx.py
    ```
3.  Abra el archivo `Proyecto/Material_1_Proyecto_IA_Talento_Tech.docx` resultante para ver la memoria técnica terminada con diseño corporativo premium.
