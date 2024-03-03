from octoai.client import Client
from dotenv import load_dotenv
import os
import time
from config import configure_logger
load_dotenv()
OCTOAPI_TOKEN = os.getenv("OCTOAPI_TOKEN")
client = Client(token=OCTOAPI_TOKEN)
LOGGER=configure_logger()

def calculate_score(message_dict,index):
    message = message_dict['message']
    filename = message_dict['filename']
    LOGGER.info(f"Request initiated for id {index} ")
    try:
        start_time = time.time()
        completion = client.chat.completions.create(
        messages=message,
            model="mixtral-8x7b-instruct",
            max_tokens=200,
            presence_penalty=0,
            temperature=0.5,
            top_p=0.9
        )
        stop_time = time.time()
        response = {"result":completion.choices[0].message.content, "filename":filename}
        time_taken = stop_time - start_time
        LOGGER.info(f"Total time taken by request ID  {index +1} is  {time_taken}" )
    except Exception as e:
        LOGGER.info (f"{e}")
        response = {'result':"Score = 0 , Reason = Some Error occured","filename":"filename"}
    finally:
        return response