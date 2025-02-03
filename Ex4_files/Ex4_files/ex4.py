import deepspeech
import wave
import numpy as np
import noisereduce as nr

# Function to load the DeepSpeech model
def load_model(model_path, scorer_path):
    model = deepspeech.Model(model_path)
    model.enableExternalScorer(scorer_path)
    return model

# Function to read and preprocess an audio file
def read_process_audio(filename):
    with wave.open(filename, 'rb') as w:
        rate = w.getframerate()
        frames = w.getnframes()
        buffer = w.readframes(frames)
        audio_data = np.frombuffer(buffer, dtype=np.int16)

        # Noise reduction
        reduced_noise_audio = nr.reduce_noise(y=audio_data, sr=rate)

    return reduced_noise_audio, rate

# Function to transcribe audio using a given model
def transcribe(model, audio_data):
    return model.stt(audio_data)

# Paths to the models and scorers for each language
models = {
    'english': (C:\Users\user\Desktop\INTELIGENT SIGNAL\Ex4_files\Ex4_audio_files \english_model.pbmm', C:\Users\user\Desktop\INTELIGENT SIGNAL\Ex4_files\Ex4_audio_files \english_scorer.scorer'),
'italian': (C:\Users\user\Desktop\INTELIGENT SIGNAL\Ex4_files\Ex4_audio_files \italian_model.pbmm', C:\Users\user\Desktop\INTELIGENT SIGNAL\Ex4_files\Ex4_audio_files \italian_scorer.scorer'),
'spanish': (C:\Users\user\Desktop\INTELIGENT SIGNAL\Ex4_files\Ex4_audio_files \spanish_model.pbmm', C:\Users\user\Desktop\INTELIGENT SIGNAL\Ex4_files\Ex4_audio_files \spanish_scorer.scorer'),}

# Load models for each language
loaded_models = {lang: load_model(*paths) for lang, paths in models.items()}

# Transcribe an example audio file for each language
for lang in loaded_models:
    audio_file = f'path_to_your_{lang}_audio.wav'
    audio_data, rate = read_process_audio(audio_file)
    transcription = transcribe(loaded_models[lang], audio_data)
    print(f"{lang.capitalize()} Transcription:", transcription)
