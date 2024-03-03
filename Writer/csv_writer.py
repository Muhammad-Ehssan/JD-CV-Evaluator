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
                csv_writer.writerow(["Filename","Score", "Reason"])
            
            # Iterating over the list of strings
            for entry in data_list:
                # Extracting score and reason from each entry
                filename = entry['filename']
                result = entry['result']
                score_start = result.find('=') + 1
                score_end = result.lower().find('reason')
                score = result[score_start:score_end].strip()
                
                reason_start = result.lower().find('reason')
                reason = result[reason_start:].strip()
                
                # Writing the score and reason to the CSV file
                csv_writer.writerow([filename, score, reason])
                
        LOGGER.info(f"Data successfully added to {csv_filename}")
        return csv_filename , path
    
    except Exception as e:
        print(f"Error: {e}")


