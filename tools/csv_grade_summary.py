import csv
import os

AUTHOR = "Suleman Saddet"
APP_NAME = "CSV Grade Summary Tool"

def run():
    print (f"=== {APP_NAME} by {AUTHOR} ===")

    # Prompt the user to type in the file path of their CSV file and strip extra whitespace
    file_path = input("Enter the path to the CSV file (e.g., tests/fixtures/grades.csv): ").strip()

    # Check if the file actually exists on the computer before attempting to open it
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist. Please check the path and try again.")
        return # Exits the function early if the file is missing

    try:
        # Open the CSV file in read mode ('r') using UTF-8 text encoding
        with open(file_path, mode='r', encoding='utf-8') as file:
            # csv.DictReader reads rows as dictionaries where keys are column header names
            reader = csv.DictReader(file)
            
            # Verify that the CSV file actually contains column headers
            if not reader.fieldnames:
                print("Error: The CSV file is empty or missing headers.")
                return

            # Print out the detected column names to the user
            print(f"\nFound columns: {', '.join(reader.fieldnames)}")
            
            # Initialize an empty list to store valid scores and a counter for rows
            scores = []
            row_count = 0
            
            # Iterate through every row in the CSV file sequentially
            for row in reader:
                row_count += 1
                score_val = None
                
                # Loop through each column header in the current row dictionary
                for key in row:
                    # Check if the column name contains 'score' or 'grade' (case-insensitive)
                    if 'score' in key.lower() or 'grade' in key.lower():
                        try:
                            # Try converting the text value found in that cell into a decimal number (float)
                            score_val = float(row[key])
                        except ValueError:
                            # If conversion fails (e.g., text instead of a number), ignore and move on
                            pass
                
                # If a valid numeric score was successfully extracted, add it to our scores list
                if score_val is not None:
                    scores.append(score_val)

            # If no valid numbers were found in any score/grade columns, notify the user and exit
            if not scores:
                print("Warning: No numeric scores found in the grade/score columns.")
                return

            # Compute statistical metrics using built-in Python math operations
            total_students = len(scores)                    # Count how many scores were collected
            average_score = sum(scores) / total_students    # Calculate the mathematical average
            highest_score = max(scores)                     # Find the maximum score value
            lowest_score = min(scores)                      # Find the minimum score value

            # Print out a nicely formatted summary report of the calculations
            print("\n--- Grade Summary Report ---")
            print(f"Total Records Processed: {row_count}")
            print(f"Average Score: {average_score:.2f}")     # Formats the float to 2 decimal places
            print(f"Highest Score: {highest_score}")
            print(f"Lowest Score: {lowest_score}")
            print("----------------------------\n")

    except Exception as e:
        # Catch any unexpected technical errors (like permission issues or bad encodings) and display them safely
        print(f"An unexpected error occurred while reading the file: {e}")

# Standard Python check to ensure the run() function executes when called from the main launcher
if __name__ == "__main__":
    run()