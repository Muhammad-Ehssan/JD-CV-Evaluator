from flask import Flask, render_template, request, send_file
from Reader.fileHandler import handle_files, delete_files_in_folder
from Mixtral.mixtral import calculate_score
from Mixtral.messageMaker import create_evaluation_message,extract_text
from concurrent.futures import ThreadPoolExecutor
from Writer.csv_writer import add_to_csv
from config import app_configure_logger
from dotenv import load_dotenv
import os
import logging
from flask_cors import CORS
logging.getLogger().addHandler(app_configure_logger())

load_dotenv()
PORT = os.getenv("PORT")

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB


@app.route('/', methods=['GET'])
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload():
    messages_list=[]
    file_types = ['resumes', 'job_descriptions']
    delete_files_in_folder("./ResultFiles/")
    request_files = {file_type: request.files.getlist(file_type + '[]') for file_type in file_types}
    job_desc_paths, resume_paths  = handle_files(request_files)
    extracted_JD = extract_text("./"+ UPLOAD_FOLDER +"/job_descriptions/"+job_desc_paths[0])
    for path in resume_paths:
        extracted_resume = extract_text("./"+ UPLOAD_FOLDER +"/resumes/"+path)
        message = create_evaluation_message(extracted_resume,extracted_JD)
        messages_list.append(message)

        # Create a ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=len(messages_list)) as executor:
        # Submit the tasks to the executor
        completion_futures = [executor.submit(calculate_score, message,index) for index,message in enumerate(messages_list)]
    # Retrieve the results
    results = [future.result() for future in completion_futures]
    csv_filename , path = add_to_csv(results)
    delete_files_in_folder("./"+ UPLOAD_FOLDER+"/job_descriptions")
    delete_files_in_folder("./"+ UPLOAD_FOLDER+"/resumes")

    return send_file(path, as_attachment=True, download_name=csv_filename)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)