import speech_recognition as sr
from pydub import AudioSegment

class AudioTranscriber:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        
    def process_audio(self, audio_file_path):
        audio = AudioSegment.from_file(audio_file_path)
        audio.export("temp.wav", format="wav")
        
        with sr.AudioFile("temp.wav") as source:
            audio_data = self.recognizer.record(source)
            try:
                text = self.recognizer.recognize_google(audio_data, show_all=True)
                return self._process_transcription(text)
            except sr.UnknownValueError:
                return {"error": "Could not understand audio"}
            except sr.RequestError as e:
                return {"error": f"Service error: {e}"}
    
    def _process_transcription(self, transcription_data):
        if not transcription_data or 'alternative' not in transcription_data:
            return {"text": "", "speakers": []}
        text = transcription_data['alternative'][0]['transcript']
        return {"text": text, "speakers": [{"speaker": "Speaker 1", "text": text}]}