# Rock Type Classifier using Decision Trees

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15673394.svg)](https://doi.org/10.5281/zenodo.15673394)

This project uses a Decision Tree Classifier to classify igneous rocks (**Basalt**, **Andesite**, **Rhyolite**, **Other**) based on major oxide geochemical data: **SiO₂**, **FeO**, and **Al₂O₃**.

It’s a simple but effective tool for geologists, students, or researchers wanting quick insights from geochemical datasets.

---

## How It Works

The classifier uses:

- **SiO₂ (Silicon Dioxide)**
- **FeO (Iron(II) Oxide)**
- **Al₂O₃ (Aluminum Oxide)**

to predict rock types based on geochemical thresholds and patterns learned during training.

---

## 📁 Project Structure
rock-classifier-ml/
├── rock_classifier_script.py # Training + plotting script
├── predict.py # Run predictions on new CSV data
├── sample_data.csv # Sample input data
├── output.zip # Zipped folder containing model + prediction results
├── requirements.txt # Dependencies
├── README.md # Project overview
└── LICENSE # MIT License

---

## How to Use

### Download or clone the repository
git clone https://github.com/zarinali735/rock-classifier-ml.git
cd rock-classifier-ml

### Install the requirements
pip install -r requirements.txt

### Prepare your input CSV
SIO2,FEO,AL2O3

### Run the prediction script
python predict.py sample_data.csv
## This will create a file named:
output/predicted_rock_types.csv
## Note: In this repository, the output/ folder is compressed as output.zip
## Output Contents
Download and extract output.zip to access:
rock_classifier_model.joblib → Trained Decision Tree model
predicted_rock_types.csv → Output predictions from predict.py
The training script also generates:
A scatter plot of SiO₂ vs FeO, color-coded by rock type
A confusion matrix and classification report for model performance

## Data Source
Original data downloaded from the https://search.earthchem.org  , exported as:
earthchem_download_46477_csv.csv

## 👤 Author
Zarin Ali
Geologist | Researcher
2025
