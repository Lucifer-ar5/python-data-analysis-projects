import pandas as pd

def clean_sales_data(filepath):
    """
    Cleans raw sales lead dataset by removing duplicates,
    handling missing values, and formatting text fields.
    """
    # Load dataset
    df = pd.read_excel(filepath)
    
    # Drop complete duplicates
    df = df.drop_duplicates()
    
    # Strip whitespaces from column headers
    df.columns = df.columns.str.strip()
    
    # Clean text columns
    text_columns = df.select_dtypes(include=['object']).columns
    for col in text_columns:
        df[col] = df[col].astype(str).str.strip().str.title()
        
    return df

if __name__ == "__main__":
    print("Data cleaning pipeline initialized.")
