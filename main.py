from fastapi import FastAPI, Form, Request
from utils import send_message, download_audio
from model import response_from_gemini
import os

app = FastAPI()

@app.post("/message")
async def reply(request: Request):
	twilio_request = await request.form()
	print(twilio_request)
	text_message = twilio_request.get("Body", "").strip()
	number = twilio_request.get("From").replace("whatsapp:","")
	print(number, text_message)
	audio_url = twilio_request.get("MediaUrl0", "")

	if text_message:
		response = response_from_gemini(text_message)
		send_message(number, response)
		print(response)

	if audio_url:
		audio_message = download_audio(audio_url)
		text = audio_to_text(audio_message)
		response = response_from_gemini(text)
		send_message(number, response)

		if os.path.exists(audio_message):
			os.remove(audio_message)

	return ""

# if __name__ == "__main__":
# 	import uvicorn
# 	uvicorn.run(app, host='127.0.0.1', port=12745, reload=True)