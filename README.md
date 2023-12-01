Proyecto de Machine Learning
Este proyecto de Machine Learning se centra en la predicción del precio de las acciones y la generación de señales de compra basadas en indicadores técnicos. Se han entrenado seis modelos, cinco supervisados y uno semisupervisado, utilizando diferentes técnicas y algoritmos.

Modelos entrenados
ARIMA: Un modelo de series temporales que combina los modelos de Autoregresión (AR), Integración (I) y Media Móvil (MA).

PCA y RandomForest: PCA (Principal Component Analysis) es una técnica de reducción de dimensionalidad. RandomForest es un algoritmo de aprendizaje supervisado que utiliza múltiples árboles de decisión.

Regresión Lineal: Un modelo de aprendizaje supervisado que se utiliza para predecir una variable continua.

Regresión Logística: Un modelo de aprendizaje supervisado que se utiliza para predecir una variable categórica.

Red Neuronal: Un modelo de aprendizaje profundo que se inspira en el funcionamiento del cerebro humano.

Gradient Boosting: Un algoritmo de aprendizaje supervisado que construye un modelo predictivo en forma de un conjunto de modelos de predicción débiles, normalmente árboles de decisión.

Los parámetros utilizados para cada modelo se guardaron en archivos params.yaml para permitir una fácil replicación y comparación de los resultados.

Análisis de datos
Se realizó un Análisis Exploratorio de Datos (EDA) en todos los modelos. En los modelos de clasificación, se crearon columnas adicionales y se definieron indicadores para las señales de compra. Se trabajó con la fecha para facilitar los análisis y se eliminaron algunas columnas que contaminaban la predicción.

Evaluación del modelo
Se evaluaron todos los modelos y se graficaron los resultados. Se crearon archivos .pkl para cada modelo. El modelo ganador fue el PCA y RandomForest.

Implementación del modelo
Se creó una aplicación en Streamlit para verificar que el modelo funciona y que predice lo que se le pide. También se realizaron presentaciones para analistas de datos y para vender el proyecto como negocio.

Trabajo futuro
En el futuro, se podría ampliar el modelo para que también pronostique cuándo vender. Además, se podrían explorar otros modelos o técnicas para mejorar aún más los resultados.