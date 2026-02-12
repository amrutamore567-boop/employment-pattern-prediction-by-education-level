# employment_percentage_by_education.py

import pandas as pd

def main():
    try:
        # Load cleaned dataset (Make sure cleaned_data.csv is in same folder)
        df = pd.read_csv("cleaned_data.csv")

        # Check required columns
        required_columns = ["Education_Level", "Employment_Status"]
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"Column '{col}' not found in dataset.")

        # Calculate percentage of Employment Status by Education Level
        result = (
            df.groupby("Education_Level")["Employment_Status"]
            .value_counts(normalize=True)
            .mul(100)
            .rename("Percentage")
            .reset_index()
        )

        # Round percentage to 2 decimal places
        result["Percentage"] = result["Percentage"].round(2)

        print("\nEmployment Percentage by Education Level:\n")
        print(result)

        # Optional: Save result to CSV
        result.to_csv("employment_percentage_by_education_output.csv", index=False)
        print("\nOutput saved as 'employment_percentage_by_education_output.csv'")

    except FileNotFoundError:
        print("Error: 'cleaned_data.csv' file not found.")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
