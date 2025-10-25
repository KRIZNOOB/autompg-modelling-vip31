# Auto MPG Linear Regression Modelling

Proyek machine learning untuk memprediksi konsumsi bahan bakar kendaraan (MPG) menggunakan Linear Regression pada dataset Auto MPG dari UCI Machine Learning Repository.

## 📊 Deskripsi Project

Project ini melakukan analisis dan pemodelan prediktif terhadap efisiensi bahan bakar kendaraan (Miles Per Gallon/MPG) berdasarkan berbagai fitur kendaraan seperti displacement, cylinders, horsepower, weight, acceleration, model year, dan origin.

## 🛠️ Teknologi

- **Pandas**: Library untuk manipulasi dan analisis data
- **NumPy**: Library untuk komputasi numerik
- **Matplotlib**: Library untuk visualisasi data (plotting)
- **Seaborn**: Library untuk visualisasi statistik
- **Scikit-learn**: Library untuk machine learning (Linear Regression, metrics)
- **Jupyter Notebook**: Environment untuk pengembangan interaktif
- **ucimlrepo**: Library untuk mengakses dataset dari UCI ML Repository

## 📦 Installation

1. Clone repository ini:
```bash
git clone https://github.com/KRIZNOOB/autompg-modelling-vip31.git
cd autompg-modelling-vip31
```

2. Buat virtual environment:
```bash
python -m venv .venv
```

3. Aktifkan virtual environment:
```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

Jalankan Jupyter Notebook:

```bash
jupyter notebook
```

Kemudian buka file `src/modelling.ipynb` dan jalankan cell secara berurutan.

Atau jalankan di VS Code dengan Jupyter extension.

## 📁 Struktur Project

```
autompg-modelling-vip31/
├── src/
│   ├── modelling.ipynb    # Main notebook untuk analisis dan modelling
│   └── dataset.py         # Module untuk loading dataset dari UCI
├── data/
│   └── auto-mpg.csv      # Dataset (optional, jika disimpan lokal)
├── .venv/                 # Virtual environment
├── .gitignore            # Git ignore file
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 📊 Dataset

Dataset yang digunakan adalah **Auto MPG** dari UCI Machine Learning Repository:
- **ID**: 9
- **Total Records**: 398
- **Features**: 
  - `displacement`: Engine displacement (cu. inches)
  - `cylinders`: Number of cylinders
  - `horsepower`: Horsepower
  - `weight`: Vehicle weight (lbs)
  - `acceleration`: Time to accelerate 0-60 mph (sec)
  - `model_year`: Model year (19XX)
  - `origin`: Origin of car (1=USA, 2=Europe, 3=Japan)
- **Target**: `mpg` (miles per gallon)

### Data Preprocessing

1. **Missing Values**: Mengisi nilai missing pada kolom `horsepower` dengan mean
2. **Reset Index**: Menata ulang index setelah cleaning
3. **Feature Selection**: Menggunakan semua fitur numerik untuk prediksi

## 📈 Pipeline Analisis

### 1. Data Loading & Info
- Load dataset dari UCI ML Repository
- Cek informasi dataset (tipe data, ukuran, dll)

### 2. Data Preprocessing
- Identifikasi missing values
- Handle missing values dengan mean imputation
- Reset index

### 3. Exploratory Data Analysis (EDA)
- Statistical summary
- Data distribution
- Correlation matrix
- Distribution of MPG (Histogram & Boxplot)

### 4. Modelling
- Prepare features (X) dan target (y)
- Split data (80% training, 20% testing)
- Train Linear Regression model
- Make predictions

### 5. Evaluation
- Calculate R² Score
- Calculate RMSE (Root Mean Squared Error)
- Interpret model performance

## 📊 Hasil Model

Model Linear Regression yang dibangun memiliki performa:
- **R² Score**: ~0.8476 (84.76%)
- **RMSE**: ~2.86 MPG

### Interpretasi:
- Model dapat menjelaskan **84.76%** variasi dalam data MPG
- Rata-rata kesalahan prediksi sebesar **±2.86 MPG**

### Fitur Paling Berpengaruh:
1. **Origin** (+1.31): Mobil dari negara tertentu lebih hemat
2. **Model Year** (+0.80): Teknologi lebih baru lebih efisien
3. **Weight** (-0.007): Mobil lebih berat lebih boros
4. **Cylinders** (-0.15): Lebih banyak silinder lebih boros

## 📝 Requirements

```
pandas==2.1.4
numpy==1.26.2
matplotlib==3.8.2
seaborn==0.13.0
scikit-learn==1.3.2
ucimlrepo>=0.0.3
jupyter==1.0.0
ipykernel==6.27.1
```

## 🔗 Links

- [UCI ML Repository](https://archive.ics.uci.edu/ml/index.php)
- [Auto MPG Dataset](https://archive.ics.uci.edu/dataset/9/auto+mpg)