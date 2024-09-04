# Maintenance_Prediction_Rest_API

The work is done using a synthetic dataset obtained from [Kaggle](https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification). The dataset consists of 10 000 data points stored as rows with 14 features in columns

# Interface 
<img width="685" alt="Screenshot 2024-09-05 at 2 14 39 AM" src="https://github.com/user-attachments/assets/affc1df0-7c46-489c-bb7f-4cd20f53504b">

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

# Maintenance Failure Prediction Application

This application predicts potential maintenance failures based on machine parameters using a trained machine learning model. It includes a FastAPI backend and a Streamlit frontend for interaction.

## Features
- **FastAPI Backend**: Handles prediction requests.
- **Streamlit Frontend**: Provides a user-friendly interface to input parameters and view predictions.
- **Docker Support**: Easily run the entire application in containers using Docker Compose.

## Setup Instructions

### Prerequisites
- [Python 3.8+](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.pypa.io/en/latest/) or [pip](https://pip.pypa.io/en/stable/)
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

### Local Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/maintenance-failure-prediction.git
    cd maintenance-failure-prediction
    ```

2. **Install dependencies:**
   If using `pipenv`:
    ```bash
    pipenv install
    pipenv shell
    ```
   If using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

3. **Start FastAPI backend:**
    ```bash
    uvicorn main:app --reload
    ```

4. **Start Streamlit frontend:**
    ```bash
    streamlit run app.py
    ```

### Running with Docker

1. **Build and run the containers:**
    ```bash
    docker-compose up --build
    ```

2. **Access the application:**
   - FastAPI backend will be available at [http://localhost:8000](http://localhost:8000)
   - Streamlit frontend will be available at [http://localhost:8501](http://localhost:8501)

### Stopping the Application
To stop the application when running with Docker, use:
```bash
docker-compose down


## File Structure
maintenance-failure-prediction/
│
├── main.py               # FastAPI backend
├── app.py                # Streamlit frontend
├── Dockerfile            # Dockerfile for the application
├── docker-compose.yml    # Docker Compose configuration
├── requirements.txt      # Python dependencies
├── model/                # Directory containing the model and encoder files
│   ├── maintenance-failure-model.pkl
│   └── encoder.pkl
└── README.md             # This readme file

