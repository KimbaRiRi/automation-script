import os
import csv

def consolidate_csv_files(input_folder, output_file):
    # Get a list of all CSV files in the input folder
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
    
    # Set to store unique items from original descriptions
    unique_items = set()
    
import os
import csv

def consolidate_csv_files(input_folder, output_file):
    # Get a list of all CSV files in the input folder
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
    
    # Set to store unique items from original descriptions
    unique_items = set()
    
    # Open the output CSV file in write mode
    with open(output_file, 'w', newline='', encoding='utf-8') as output_csv:
        csv_writer = csv.writer(output_csv)
        
        # Write header row
        csv_writer.writerow(["Date", "Debit", "Original Description"])
        
        # Iterate over each CSV file
        for csv_file in csv_files:
            with open(os.path.join(input_folder, csv_file), 'r', newline='', encoding='utf-8') as input_csv:
                csv_reader = csv.reader(input_csv)
                
                # Check if the CSV file has a header row
                has_header = csv.Sniffer().has_header(input_csv.read(1024))
                input_csv.seek(0)  # Reset file pointer
                
                # Skip header row if present
                if has_header:
                    next(csv_reader)
                
                # Identify the index of the column for "Original Description"
                if csv_file == "CSV3.csv":
                    description_index = -1  # Last column
                else:
                    description_index = 2  # Third column
                
                # Iterate over each row in the CSV file
                for row in csv_reader:
                    # Check if the transaction is a debit
                    if len(row) >= 2 and row[1].startswith('-'):
                        # Write selected columns to the output CSV file
                        csv_writer.writerow([row[0], row[1][1:], row[description_index]])
                        
                        # Extract and add items from the description to the set
                        items = [item.strip() for item in row[description_index].split("-")]
                        unique_items.update(items)

    # Print the unique items
    print("Unique items:", list(unique_items))

# Specify the input folder containing CSV files and the output consolidated CSV file
input_folder = "/Volumes/ADATA/Documents/ATO/Tax22-23/CSV/CSV_Process"
output_file = "_Processed/consolidated.csv"

# Call the function to consolidate CSV files
consolidate_csv_files(input_folder, output_file)
