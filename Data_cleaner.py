import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def clean_data(df):
    # clean the data
    print("\nCleaning data...")
    print("Initial shape:", df.shape)

    # Show missing values before cleaning
    print("\nMissing values before cleaning:")
    print(df.isnull().sum())

    # Handle missing values
    print("\nHandling missing values...")
    df = df.dropna()
    print("Shape after dropping missing values:", df.shape)

    # Remove duplicates
    print("\nRemoving duplicates...")
    df = df.drop_duplicates()
    print("Shape after removing duplicates:", df.shape)

    return df

def save_data(df, output_path):
    try:
        df.to_csv(output_path, index=False)
        print(f"\nData saved successfully to {output_path}.")
    except Exception as e:
        print(f"An error occurred while saving: {e}")

def main():
    print("Welcome to the Data Cleaner!")

    # input file path
    file_path = input("Enter the path to your CSV file: ")

    df = load_data(file_path)

    if df is None:
        return

    # show initial data
    print("\nInitial Data Shape:")
    print(df.shape)

    print("\nInitial Data:")
    print(df.head(16))

    # clean the data
    cleaned_df = clean_data(df)

    # show cleaned data
    # show cleaned data
    print("\nCleaned Data Shape:")
    print(cleaned_df.shape)

    print("\nCleaned Data:")
    print(cleaned_df.to_string())

    # save cleaned data
    output_path = input("\nEnter the path to save the cleaned CSV file: ")
    save_data(cleaned_df, output_path)

main()