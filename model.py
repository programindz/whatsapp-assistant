import google.generativeai as genai 
import whisper
import os
from dotenv import load_dotenv

load_dotenv()

###################################################
# Setting up the configuration for gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

generation_config = {
	"temperature": 1,
	"top_k": 1,
	"top_p": 1,
	"max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]
####################################################


####################################################
# Model for Gemini and Chat History

model_gemini = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

chat = model_gemini.start_chat(history=[
])
#####################################################

#####################################################
# Model for Audio to Text using Whisper

model_whisper = whisper.load_model("base", in_memory=True)

def audio_to_text(audio):
	result = model_whisper.transcribe(audio)
	return result['text']

#####################################################


# Gemini Response
def response_from_gemini(text):
	response = chat.send_message(text, stream=True)
	response.resolve()
	return response.text

