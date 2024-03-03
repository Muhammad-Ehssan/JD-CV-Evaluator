import csv
from datetime import datetime
from config import configure_logger
LOGGER = configure_logger()

def add_to_csv(data_list):
    path = "./ResultFiles/"
    try:
        # Check if the CSV file exists
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        csv_filename = f"scores_{timestamp}.csv"
        path = path + csv_filename
        # Opening the CSV file in append mode or creating a new one
        with open(path, 'a', newline='', encoding='utf-8') as csvfile:
            # Creating a CSV writer object
            csv_writer = csv.writer(csvfile)
            
            # Write header if the file is newly created
            if csvfile.tell() == 0:
                csv_writer.writerow(["Score", "Reason"])
            
            # Iterating over the list of strings
            for entry in data_list:
                # Extracting score and reason from each entry
                score_start = entry.find('=') + 1
                score_end = entry.find('\n')
                score = entry[score_start:score_end].strip()
                
                reason_start = entry.find('Reason:') + len('Reason:')
                reason = entry[reason_start:].strip()
                
                # Writing the score and reason to the CSV file
                csv_writer.writerow([score, reason])
                
        LOGGER.info(f"Data successfully added to {csv_filename}")
        return csv_filename , path
    
    except Exception as e:
        print(f"Error: {e}")


