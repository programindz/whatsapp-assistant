from twilio.rest import Client
from dotenv import load_dotenv
import os
import requests
import uuid

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)


def send_message(number, text):
  try:
    message = client.messages.create(
      from_='whatsapp:+14155238886',
      body=f"{text}",
      to=f"whatsapp:{number}"
      )
  except Exception as e:
    print("Exception: ", e)


def download_audio(media_url):
    response = requests.get(media_url, auth=(account_sid, auth_token))
    
    if response.status_code == 200:
        unique_filename = f"{uuid.uuid4().hex}.wav"
        audio_file_path = os.path.join(os.getcwd() + "\\audios\\", unique_filename) 
        
        with open(audio_file_path, "wb") as audio_file:
            audio_file.write(response.content)
        
        return audio_file_path
    else:
        print("Failed to download audio file:", response.status_code)
        return None