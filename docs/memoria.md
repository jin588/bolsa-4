En este proyecto de ML hemos entrenado 6 modelos, 5 supervisados y 1 semisupervisado. En algunos hemos predicho el precio que tendrá una accion un día en cuestion basandonos en patrones que el modelo haya podido detectar basandose en la evolucion que ha tenido el precio de la accion en cuestion. En otros, los de clasificacion, hemos creado una nueva columna llamada "buy signal" lo cual es un indicador de compra y la hemos definado como el momento en que la ema5 corta con la ema20 , lo cual es señal de compra o de venta. Por simplificar nos hemos centrado solo en la señal de compra pero mas adelante se puede ampliar tambíén para que pronostique cuando hay que vender.
En todos los modelos he realizado un EDA  en los de clasificacion ha sido mas minucioso al tener que crear mas columnas y definir los indiciadores para comprar. En todos hemos tenido que trabajar con la fecha para facilitar los analisis y borrar algunas columnas que contaminaban la prediccion como high o low , además en los de clasificacion  hemos tenido que seleccionar las columnas mas determinantes para trabajar solo con ellas y hacer un modelo lo más preciso posible. A continuacion describo un poco los modelos que hemos entrenado:

ARIMA: El modelo ARIMA es un modelo de series temporales que combina los modelos de Autoregresión (AR), Integración (I) y Media Móvil (MA). Los parámetros utilizados para este modelo se guardaron en el archivo params.yaml.

PCA y RandomForest: PCA (Principal Component Analysis) es una técnica de reducción de dimensionalidad que se utiliza para transformar variables correlacionadas en un conjunto más pequeño de variables no correlacionadas llamadas componentes principales. RandomForest es un algoritmo de aprendizaje supervisado que utiliza múltiples árboles de decisión para realizar tareas de clasificación o regresión. Los parámetros utilizados para estos modelos se guardaron en el archivo params.yaml.

Regresión Lineal: Este es un modelo de aprendizaje supervisado que se utiliza para predecir una variable continua (y) basándose en una o más variables predictoras (X). Los parámetros utilizados para este modelo se guardaron en el archivo params.yaml.

Regresión Logística: Este es un modelo de aprendizaje supervisado que se utiliza para predecir una variable categórica basándose en una o más variables predictoras. Los parámetros utilizados para este modelo se guardaron en el archivo params.yaml.

Red Neuronal: Este es un modelo de aprendizaje profundo que se inspira en el funcionamiento del cerebro humano. Se utiliza para realizar tareas de clasificación, regresión, agrupación, entre otras. Los parámetros utilizados para este modelo se guardaron en el archivo params.yaml.

Gradient Boosting: Este es un algoritmo de aprendizaje supervisado que construye un modelo predictivo en forma de un conjunto de modelos de predicción débiles, normalmente árboles de decisión. Los parámetros utilizados para este modelo se guardaron en el archivo params.yaml.

Cada uno de estos modelos tiene sus propias fortalezas y debilidades, y la elección del modelo depende del tipo de datos y del problema que se esté tratando de resolver. Los archivos params.yaml contienen los parámetros específicos utilizados para cada modelo, lo que permite una fácil replicación y comparación de los resultados.

Además hemos graficado todos los modelos, hemos hehco un yaml de todos ellos y un .pkl.

El modelo ganador ha sido el PCA y random forest aunque por muy poquito y le hemos hecho una app en streamlit para poder verificar que el modelo funciona y que predice lo que se le pide.
También he realizado un pptx para analistas de datos y otro para vender el proyecto como negocio. he desglosado todo el trabajo y todos los modelos en varios .ipynb.

Los modelos de regresion se han evaluado con MAE, MSE, MPE, etc y los de clasificacion con accuracy, recall, presicion y score

No he podido realizar los pipelina que me hubiese gustado debido al gran tamaño de los datos que me llevaba horas hasta que me daba un resultado.

En el modelo ganador se ha analizado la importancia de las caracteristicas, sirviendo ademas de mejora para los otros modelos clasificatorios.

He validado la amyoria de ellos con validacion cruzada

En el futuro todos tienen margen de mejora, sobre todo el LSTM que al dominar menos la materia, esta un poco verde aun.

