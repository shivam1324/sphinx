from flask import Flask, render_template, request,flash, redirect, url_for, send_file,flash, make_response,Response
import os
import datetime
import requests
import io
import random
import csv
import json
import librosa
import torch
import soundfile as sf
import numpy as np
from transformers import pipeline
from gtts import gTTS
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import torch
import spacy
import random
import datetime
import datefinder
import re
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


app = Flask(__name__)
app.secret_key = 'dc9a0187c5297e94c26cdd32ffb3266eda502bc49a2874cb77961707ecda021f'
app.debug = True
pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    if 'audio' in request.files:
        audio_file = request.files['audio']
        if audio_file:
            audio_file.save("static/music/recorded_audio.wav")
            text="hello shivam"
            tts=gTTS(text=text,lang="en",tld="co.in")
            tts.save("static/music/text.mp3")  
            audio_path = "static/music/recorded_audio.wav"
            sample_rate = 16000
            audio_input, sample_rate = librosa.load(audio_path, sr=sample_rate)
            transcribe = pipe(audio_input)
            print(transcribe['text'])
            
        

if __name__ == '__main__':
  app.run(port=5000)