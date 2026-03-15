# 🫁 Pneumonia Detection from Chest X-Rays

A deep learning project using Convolutional Neural Networks (CNNs) to detect pneumonia from chest X-ray images. Achieved **91.3% accuracy**, **92.56% precision**, and **93.55% recall** — deployed as a real-time Streamlit web app.

-----

## 📌 Problem Statement

Pneumonia is one of the leading causes of mortality worldwide, especially in children under 5. Early and accurate diagnosis from chest X-rays is critical but requires expert radiologists. This project automates that detection using deep learning, making it accessible and fast.

-----

## 🎯 Results

|Metric   |Score     |
|---------|----------|
|Accuracy |**91.3%** |
|Precision|**92.56%**|
|Recall   |**93.55%**|


> High recall is prioritized — in medical diagnosis, missing a true positive (false negative) is far more dangerous than a false alarm.

-----

## 🛠️ Tech Stack

|Tool                |Purpose                      |
|--------------------|-----------------------------|
|Python              |Core language                |
|TensorFlow & Keras  |CNN model building & training|
|NumPy & Pandas      |Data handling                |
|Matplotlib & Seaborn|Training curve visualization |
|Streamlit           |Web app deployment           |
|Jupyter Notebook    |Model development            |

-----

## 🧠 Model Architecture

- **Base:** Custom CNN with multiple Conv2D + MaxPooling layers
- **Regularization:** Dropout layers to prevent overfitting
- **Activation:** ReLU (hidden layers), Sigmoid (output — binary classification)
- **Loss:** Binary Crossentropy
- **Optimizer:** Adam

-----

## 📊 Workflow

1. **Data Loading** — Chest X-ray dataset (Normal vs Pneumonia)
1. **Preprocessing** — Resizing, normalization, data augmentation (rotation, flipping, zoom)
1. **Model Training** — CNN with early stopping based on validation loss
1. **Evaluation** — Accuracy, Precision, Recall, Confusion Matrix, AUC-ROC
1. **Learning Curve Analysis** — Training vs validation accuracy & loss monitored to detect overfitting
1. **Deployment** — Streamlit app for real-time X-ray upload and prediction

-----

## 📂 Project Structure

```
Chest_XRay-Pneumonia/
├── Chest_XRay_Pneumonia.ipynb   # Full training & evaluation notebook
└── README.md
```

-----

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/somendrew/Chest_XRay-Pneumonia-.git
cd Chest_XRay-Pneumonia-

# Install dependencies
pip install tensorflow keras numpy pandas matplotlib seaborn streamlit

# Run the notebook
jupyter notebook Chest_XRay_Pneumonia.ipynb
```

-----

## 💡 Key Learnings

- Data augmentation is crucial when working with limited medical imaging datasets
- Recall > Precision in medical diagnosis contexts — tuning the classification threshold matters
- Monitoring training vs validation curves early prevents overfitting and wasted compute
- Deploying ML models as Streamlit apps makes results tangible and demonstrable

-----

## 🗂️ Dataset

The dataset used is the [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) dataset from Kaggle, containing 5,863 X-ray images across two categories: **NORMAL** and **PNEUMONIA**.

-----

## 👤 Author

**Somendra Singh**

- 🔗 [LinkedIn](https://linkedin.com/in/somendrew)
- 🐙 [GitHub](https://github.com/somendrew)
- 📊 [Kaggle](https://kaggle.com/somendrew)