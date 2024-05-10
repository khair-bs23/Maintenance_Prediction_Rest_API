# Maintenance_Prediction_Rest_API

The work is done using a synthetic dataset obtained from [Kaggle](https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification). The dataset consists of 10 000 data points stored as rows with 14 features in columns


# Technology Used
* Python
* Jupyter Notebook
* Fast API
* Docker


In this work the classification algorithm predicted the Failure Type using LGBM classifier. The following results shows the performance of the model:


           Clases                    precision    recall  f1-score   support

    'Heat Dissipation Failure'         1.00      1.00      1.00        32
          'No Failure'                 0.99      0.98      0.99      3196
      'Overstrain Failure'             0.81      0.86      0.83        29
        'Power Failure'                0.85      0.85      0.85        26
       'Random Failures'               0.00      0.00      0.00         5
      'Tool Wear Failure'              0.06      0.17      0.09        12
    
        accuracy                           0.98      3300
       macro avg       0.62      0.64      0.63      3300
    weighted avg       0.99      0.98      0.98      3300
    
    Predicted labels:  [1 1 1 ... 1 1 1]
    accuracy score:  0.9754545454545455
    precision score:  0.618412319129165
    recall score:  0.6427902989553328
    F1-score:  0.6266798797885839


# Project Architecture 

![Drawing](https://github.com/khair-bs23/Maintenance_Prediction_Rest_API/assets/167753101/3f140e33-207c-48da-b18a-8268ad7942b3)




# API View
![image](https://github.com/khair-bs23/Maintenance_Prediction_Rest_API/assets/167753101/d387cdea-b85c-4444-a623-85c09c0934f9)

