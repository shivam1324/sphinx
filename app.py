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
from transformers import WhisperProcessor, WhisperForConditionalGeneration
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
asr_processor = WhisperProcessor.from_pretrained("openai/whisper-small")
asr_model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")
asr_model.config.forced_decoder_ids = None
nlp = spacy.load("/static/ner_model")
ner = nlp.get_pipe("ner")

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
            
            
        

if __name__ == '__main__':
  app.run(port=5000)