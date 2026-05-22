# Metodología CRISP-ML: Clasificación de Especies de Iris mediante Árbol de Decisión ID3

Este documento detalla la aplicación rigurosa de la metodología **CRISP-ML** (Cross-Industry Standard Process for Machine Learning) sobre el proyecto desarrollado a partir del notebook `Arbol_ID3_Estudiante_Iris.ipynb`. CRISP-ML proporciona un marco de trabajo sistemático y de calidad para guiar el desarrollo de soluciones de Machine Learning desde la concepción del problema hasta el mantenimiento en producción.

---

## 1. Comprensión del Problema y del Negocio (Business & Problem Understanding)

### Contexto y Motivación
La clasificación taxonómica manual de especies de plantas es una labor que requiere la presencia de botánicos expertos y un consumo considerable de tiempo. En entornos académicos, agrícolas o de conservación forestal, existe la necesidad de automatizar y agilizar la identificación de especies vegetales a partir de medidas morfológicas básicas y fácilmente recolectables en campo.

### Objetivos del Proyecto
*   **Objetivo de Negocio:** Desarrollar un sistema de asistencia botánica digital que reduzca el tiempo de catalogación de especies del género Iris en más de un 90% con una fiabilidad mínima del 95%.
*   **Objetivo de Machine Learning:** Entrenar un modelo de clasificación multiclase capaz de predecir la especie de una flor de Iris a partir de sus dimensiones anatómicas.
*   **Requisito de Interpretabilidad:** Al ser un entorno científico, el modelo debe ser una "caja blanca" (White-Box Model). Los expertos deben ser capaces de extraer, auditar y entender las reglas lógicas que conducen a cada predicción. Por ello, se selecciona el **Árbol de Decisión basado en el Algoritmo ID3** (Entropía y Ganancia de Información).

---

## 2. Comprensión de los Datos (Data Understanding)

### Origen del Dataset
El conjunto de datos utilizado es el famoso **Iris Dataset**, publicado originalmente por el eminente estadístico británico Ronald Fisher en 1936. Los datos han sido cargados de forma transparente desde el repositorio público de OpenML.

### Estructura y Características
El conjunto de datos consta de **150 instancias (muestras)** y está perfectamente **balanceado**, con exactamente 50 instancias para cada una de las tres especies. Contiene 4 variables predictoras numéricas continuas (medidas en centímetros) y 1 variable objetivo categórica:

| Variable | Tipo de Dato | Unidad | Descripción |
| :--- | :--- | :--- | :--- |
| `sepallength` | Numérica (Continuo) | cm | Longitud del sépalo de la flor. |
| `sepalwidth` | Numérica (Continuo) | cm | Ancho del sépalo de la flor. |
| `petallength` | Numérica (Continuo) | cm | Longitud del pétalo de la flor. |
| `petalwidth` | Numérica (Continuo) | cm | Ancho del pétalo de la flor. |
| `class` (Objetivo) | Categórica (Nominal) | - | Especie de Iris: `Iris-setosa`, `Iris-versicolor`, `Iris-virginica`. |

### Análisis de Calidad y Exploración Inicial
*   **Datos Faltantes:** El dataset cuenta con el 100% de integridad (no existen valores nulos ni `NaN`).
*   **Distribución:** Al estar balanceado a nivel de clase (33.3% para cada una), no se requieren técnicas de sobremuestreo (SMOTE) o submuestreo.
*   **Separabilidad:** La clase `Iris-setosa` es linealmente separable de las otras dos especies a partir de características del pétalo. En cambio, `Iris-versicolor` e `Iris-virginica` presentan un leve solapamiento en sus fronteras morfológicas, lo cual representa el principal reto de clasificación para el árbol.

---

## 3. Preparación de los Datos (Data Preparation)

La fase de preparación de datos se diseñó para ser directa y limpia, manteniendo la fidelidad del notebook original:

1.  **Ingeniería de Características:** Las 4 variables morfológicas originales se seleccionan directamente como variables de entrada ($X$), y la columna `class` se define como la variable objetivo a predecir ($y$). No se realiza normalización ni escalado dado que los árboles de decisión son insensibles a la escala de las variables.
2.  **Partición del Dataset (Data Splitting):** Para evaluar la capacidad de generalización del modelo ante datos no vistos, el conjunto de datos se divide de manera aleatoria en:
    *   **Conjunto de Entrenamiento (Training Set):** 80% de las instancias (120 muestras), utilizado para que el algoritmo aprenda los patrones morfológicos y construya las reglas del árbol.
    *   **Conjunto de Prueba (Test Set):** 20% de las instancias (30 muestras), reservado estrictamente para la evaluación final del rendimiento.
3.  **Reproducibilidad:** Se fija la semilla de aleatorización en `random_state=1` al momento de realizar la partición con `train_test_split`. Esto asegura que cada ejecución genere exactamente los mismos conjuntos de entrenamiento y prueba.

---

## 4. Modelado (Modeling)

### Configuración del Algoritmo
Se entrena un clasificador de árbol de decisión utilizando la implementación `DecisionTreeClassifier` de la biblioteca `scikit-learn`.
*   **Criterio de Partición:** Se define explícitamente `criterion='entropy'`. Esto instruye al clasificador a emular la lógica del algoritmo clásico **ID3 (Iterative Dichotomiser 3)** de Ross Quinlan, utilizando la **Entropía** como medida de impureza y la **Ganancia de Información** como métrica para seleccionar la variable idónea en cada nodo divisor:

$$\text{Entropía}(S) = - \sum_{i=1}^{c} p_i \log_2(p_i)$$

$$\text{Ganancia}(S, A) = \text{Entropía}(S) - \sum_{v \in \text{Valores}(A)} \frac{|S_v|}{|S|} \text{Entropía}(S_v)$$

### Proceso de Entrenamiento
El modelo se ajusta sobre el conjunto de entrenamiento ($X_{\text{train}}$, $y_{\text{train}}$) sin aplicar restricciones de profundidad inicial (`max_depth=None`). El árbol aprende a subdividir recursivamente el espacio tridimensional de características hasta obtener hojas completamente puras (entropía = 0.0).

---

## 5. Evaluación (Evaluation)

La evaluación se realiza sobre el conjunto de prueba de 30 muestras. Los resultados reflejan un rendimiento sobresaliente que valida el uso práctico del modelo:

### Métricas de Rendimiento Clave
*   **Exactitud General (Accuracy):** **96.67%** (29 aciertos de 30 predicciones).
*   **Desempeño por Clase:**
    *   `Iris-setosa`: **100% de precisión y exhaustividad (recall)**. Es clasificada a la perfección gracias al umbral de ancho de pétalo.
    *   `Iris-versicolor`: **100% de precisión y 92% de recall** (debido a la única muestra mal clasificada).
    *   `Iris-virginica`: **90% de precisión y 100% de recall**.

### Análisis Detallado del Error Singular (Análisis de Errores)
De las 30 muestras del conjunto de prueba, existió una sola equivocación (Traceabilidad directa con el Notebook, Línea 859):
*   **Instancia de Test Índice 77:** La especie **real** era `Iris-versicolor`, pero el modelo entrenado la **predijo** como `Iris-virginica`.
*   **Causa:** Esta flor en particular presentaba dimensiones de pétalo inusualmente grandes para su especie, cruzando el umbral de decisión lógico aprendido por el árbol divisor, lo que la situó en la hoja de `Iris-virginica`. Este comportamiento es esperado dada la leve intersección física entre estas dos especies en la naturaleza.

---

## 6. Despliegue (Deployment)

Para transformar la lógica del backend científico en herramientas interactivas y profesionales orientadas al usuario final, se diseñaron dos componentes clave de despliegue:

1.  **Dashboard Interactivo en Streamlit (`app.py`):**
    *   Desplegado como un prototipo funcional en tiempo real para laboratorios botánicos.
    *   Permite a los investigadores ingresar de forma manual o mediante deslizadores las 4 dimensiones físicas y obtener de inmediato la especie predicha.
    *   Proporciona explicabilidad en tiempo real a través de la visualización del árbol de decisión y mapas de calor interactivos.
2.  **Landing Page Web Premium (`landing/`):**
    *   Creada como portal de difusión corporativa y presentación del proyecto.
    *   Implementa una interfaz fluida, interactiva y responsiva con animaciones de KPIs dinámicas, resumiendo los aspectos clave de CRISP-ML para inversionistas o partes interesadas.

---

## 7. Monitorización y Mantenimiento (Monitoring & Maintenance)

Para garantizar que el modelo no se degrade una vez puesto en producción, se proponen las siguientes prácticas recomendadas:

### Detección de Desviación de Concepto y Datos (Data & Concept Drift)
*   **Data Drift (Desviación de Datos):** Si los botánicos comienzan a utilizar la app con flores recolectadas en condiciones de sequía o de una región geográfica distinta, es probable que las dimensiones promedio cambien sustancialmente, reduciendo la efectividad del modelo. Se debe monitorizar periódicamente la distribución de las variables de entrada utilizando métricas estadísticas (como la prueba de Kolmogorov-Smirnov).
*   **Concept Drift (Desviación de Concepto):** Ocurre si la relación biológica entre las medidas y la especie cambia por mutaciones evolutivas (un escenario a muy largo plazo) o por cambios en la taxonomía botánica oficial.

### Estrategia de Reentrenamiento y Retroalimentación
*   **Módulo de Muestreo de Control:** Guardar las predicciones realizadas en la app interactiva junto con las dimensiones físicas ingresadas por los usuarios.
*   **Validación Humana:** Diseñar un flujo donde botánicos expertos etiqueten manualmente una submuestra (ej: 5%) de las predicciones guardadas en la base de datos.
*   **Reentrenamiento Programado:** Si se acumulan más de 50 muestras validadas manualmente y se observa que la precisión en producción cae por debajo del 93%, se debe programar un pipeline automático de reentrenamiento para ajustar los umbrales de decisión del árbol ID3.
