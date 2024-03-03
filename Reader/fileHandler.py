import os
import logging
LOGGER = logging.getLogger(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'doc', 'docx', 'pdf'}



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def handle_files(request_files):

    uploaded_files = {'resumes': [], 'job_descriptions': []}

    # Create the 'uploads' directory if it doesn't exist
    if not os.path.exists(os.path.join(UPLOAD_FOLDER)):
        os.makedirs(os.path.join(UPLOAD_FOLDER))

    for file_type, files in request_files.items():
        folder_path = os.path.join(UPLOAD_FOLDER, file_type)

        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for file in files:
            if file and allowed_file(file.filename):
                filename = os.path.join(folder_path, file.filename)
                file.save(filename)
                uploaded_files[file_type].append(file.filename)
    LOGGER.info("All files saved successfully.")
    return uploaded_files['job_descriptions'], uploaded_files['resumes']

def delete_files_in_folder(folder_path):

    try:
        LOGGER.info(f"Deleting files from path {folder_path}")
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
        LOGGER.info(f"All files in {folder_path} deleted successfully.")
    except Exception as e:
        LOGGER.warning(f"Error deleting files: {e}")
