import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn import linear_model, metrics, model_selection
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import Ridge
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from dateutil.relativedelta import relativedelta
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

df_Tata = pd.read_csv("TATAMOTORS_with_indicators_.csv")
data_daily = df_Tata['close'].resample('T').mean()

size = int(len(data_daily)*0.8)
train = data_daily[:size]
test = data_daily[size:]
arima_model = auto_arima(train, 
                         start_p=1, 
                         d=0, 
                         start_q=0, 
                         max_p=5, 
                         max_d=5, 
                         max_q=5,
                         start_P=0, 
                         D=1, 
                         start_Q=0, 
                         max_P=5, 
                         max_D=5, 
                         max_Q=5,  
                         m=1,
                         seasonal=True, # que considere modelos estacionales.
                         error_action='warn', # que emita un warning si encuentra un error.
                         trace=True, # que imprima informacion mientras busca el modelo optimo
                         suppress_warnings=True,# que suprima las adverencias  durante el ajuste del modelo.
                         stepwise=True, # que un algoritmo buscara paso a paso el modelo optimo
                         random_state=20, 
                         n_fits=50
)


y_forec, conf_int  = arima_model.predict(len(test),return_conf_int=True,alpha=0.05)
pred = pd.Series(y_forec, index=test.index)
pred.columns = ['predicted']
confidence = pd.DataFrame(conf_int, columns=['lower', 'upper'])

plt.figure(figsize=(15,4))
plt.plot(train, c='green', label='train data')
plt.plot(test, c='blue', label='test data')
plt.plot(pred, c='red', label='predictions')
plt.legend()
plt.grid(), plt.margins(x=0)
plt.title('Results on test data'), plt.xticks(rotation=45)
plt.fill_between(test.index, confidence['lower'],
                 confidence['upper'], color='k', alpha=.15)


from sklearn.metrics import r2_score
print('Actual values: ', np.around(test[:10].tolist(),3))
print('Predictions:   ', np.around(pred[:10].tolist(),3))
print('RMSE: %.3f' % np.sqrt(mean_squared_error(test, pred)))
MAE = mean_absolute_error(test, pred)
MAPE = np.mean(np.abs(pred - test)/np.abs(test))
MASE = np.mean(np.abs(test - pred ))/(np.abs(np.diff(train)).sum()/(len(train)-1))
print('MAE: %.3f' % MAE)
print('MAPE: %.3f' %MAPE)
print('MASE: %.3f' %MASE)
print('R^2 score: %.3f' % r2_score(test, pred))
              