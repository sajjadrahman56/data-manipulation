import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'id': [1, 2, None, 4, 5, 6, 7, 8, 9, None],
    'score': [10, 20, 30, None, None, 70, 80, None, None, None],
}
df = pd.DataFrame(data)

def display_menu():
    print("\nData Manipulation Menu:")
    print("1. Identify Null Values")
    print("2. Fill Missing Data with Mean")
    print("3. Fill Missing Data with Median")
    print("4. Forward Fill Missing Data")
    print("5. Backward Fill Missing Data")
    print("6. Apply ffill bfill mean")
    print("7. Drop Columns with More than 49% Missing Data")
    print("8. Drop Rows with Missing Data")
    print("9. Exit")

def identify_null_values():
    df_copy = df.copy()
    print("\nOriginal DataFrame:")
    print(df_copy)

    print("\nFind Null Values in the DataFrame:")
    print(df_copy.isnull())  

def fill_with_mean():
    df_copy = df.copy()
    print("\nOriginal DataFrame:")
    print(df_copy)
    
    df_copy['score'] = df_copy['score'].fillna(df_copy['score'].mean())  
    print("\nFilling Missing 'score' Values with the Mean:")
    print(df_copy)

def fill_with_median():
    df_copy = df.copy()
    print("\nOriginal DataFrame:")
    print(df_copy)
    
    df_copy['score'] = df_copy['score'].fillna(df_copy['score'].median())  
    print("\nFilling Missing 'score' Values with the Median:")
    print(df_copy)

def forward_fill():
    df_copy = df.copy()
    print("\nOriginal DataFrame:")
    print(df_copy)
    
    df_copy = df_copy.ffill() 
    print("\nForward Fill (ffill):")
    print(df_copy)

def backward_fill():
    
    df_copy = df.copy()
    print("\nOriginal DataFrame:")
    print(df_copy)
    
    df_copy = df_copy.bfill() 
    print("\nBackward Fill (bfill):")
    print(df_copy)

def ffill_bfill_mean():
    
    df_copy = df.copy()
    print("\nOriginal DataFrame:")
    print(df_copy)
    
    for col in df_copy.columns:
        for idx in df_copy[df_copy[col].isnull()].index:
            prev_values = df_copy[col].iloc[max(0, idx - 3):idx].dropna()  
            if idx == 0:
                df_copy.at[idx, col] = df_copy[col].bfill().iloc[idx]
            elif len(prev_values) >= 3:
                df_copy.at[idx, col] = prev_values.mean() 
            else:
                df_copy.at[idx, col] = df_copy[col].ffill().iloc[idx]
    
    print("\nApplying ffill, bfill, and Mean Imputation:")
    print(df_copy)

def drop_columns_with_missing_data():
    df_copy = df.copy()
    print("\nOriginal DataFrame:")
    print(df_copy)
    
    def percent_missing(col):
        missing_percentage = (col.isnull().sum() / len(col)) * 100
        if missing_percentage >= 49:
            return True
        return False
    
    columns_to_drop = [col for col in df_copy.columns if percent_missing(df_copy[col])]
    df_copy = df_copy.drop(columns=columns_to_drop)
    print("\nDropping Columns with More than 49% Missing Values:")
    print(df_copy)

def drop_rows_with_missing_data():
    df_copy = df.copy()
    print("\nOriginal DataFrame:")
    print(df_copy)
    
    df_copy = df_copy.dropna(axis=0)  
    print("\nDataFrame After Dropping Rows with Missing Values:")
    print(df_copy)

def main():
    while True:
        display_menu()
        choice = input("\nEnter the number of your choice: ")

        if choice == "1":
            identify_null_values()
        elif choice == "2":
            fill_with_mean()
        elif choice == "3":
            fill_with_median()
        elif choice == "4":
            forward_fill()
        elif choice == "5":
            backward_fill()
        elif choice == "6":
            ffill_bfill_mean()
        elif choice == "7":
            drop_columns_with_missing_data()
        elif choice == "8":
            drop_rows_with_missing_data()
        elif choice == "9":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
