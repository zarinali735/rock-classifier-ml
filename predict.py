import sys
import pandas as pd
import joblib

def main():
    # Check if user provided a CSV file
    if len(sys.argv) < 2:
        print("Usage: python predict.py <your_input_file.csv>")
        return

    input_file = sys.argv[1]

    try:
        # Load the saved model
        model = joblib.load("output/rock_classifier_model.joblib")
    except FileNotFoundError:
        print("Error: Trained model file not found in 'output/' directory.")
        return

    try:
        # Load user data
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error reading input file: {e}")
        return

    # Check required columns
    required_columns = ["SIO2", "FEO", "AL2O3"]
    if not all(col in df.columns for col in required_columns):
        print(f"Error: Input file must contain columns: {', '.join(required_columns)}")
        return

    # Predict
    features = df[required_columns]
    predictions = model.predict(features)

    # Append results
    df["Predicted_RockType"] = predictions

    # Save output
    output_file = "output/predicted_rock_types.csv"
    df.to_csv(output_file, index=False)
    print(f"✅ Predictions saved to: {output_file}")

if __name__ == "__main__":
    main()
