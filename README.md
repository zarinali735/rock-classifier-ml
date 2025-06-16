# Rock Type Classifier using Decision Trees 

This project uses a Decision Tree Classifier to classify igneous rocks (Basalt, Andesite, Rhyolite, Other) based on major oxide geochemical data (SiO₂, FeO, Al₂O₃).

It’s a simple but effective tool for geologists, students, or researchers wanting quick insights from geochemical datasets.

---

## How It Works

The classifier uses:

- **SiO₂ (Silicon Dioxide)**
- **FeO (Iron(II) Oxide)**
- **Al₂O₃ (Aluminum Oxide)**

to predict the rock type based on thresholds and patterns learned during training.

---

## Project Structure

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
### download the folder
```bash
git clone https://github.com/zarinali735/rock-classifier-ml.git
cd rock-classifier-ml

### Install the requirements
pip install -r requirements.txt

### Prediction should have these columns/ Prepare your own input .csv
SIO2,FEO,AL2O3

### Run predictions
predict.py sample_data.csv
### This will create a file named 
output/predicted_rock_types.csv
### Note that in this repository, the output/ folder has been compressed for download as output.zip


### Download and extract output.zip to access:
### rock_classifier_model.joblib → Trained Decision Tree model
### predicted_rock_types.csv → Output predictions from predict.py
### The training script also includes scatter plots and a confusion matrix for visual performance insights.

### Data Source : Original data from EarthChem Portal https://www.earthchem.org/, exported as: earthchem_download_46477_csv.csv
### 
👤 Author
Zarin Ali
Geologist | Researcher
2025
