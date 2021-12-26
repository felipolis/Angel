import speech_recognition as sr
import random
import webbrowser
import pyttsx3
import os
import datetime
import wikipedia
import pywhatkit
import gtts
import playsound


class VirtualAssist:
    def __init__(self, assist_name, person):
        self.assist_name = assist_name
        self.person = person

        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()

        self.voice_data = ""

    def engine_speak(self, audio_string):
        """
        Fala da assistente virtual
        """
        audio_string = str(audio_string)
        tts = gtts.gTTS(text=audio_string, lang='en')
        r = random.randint(1, 20000)
        audio_file = 'audio-' + str(r) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(self.assist_name + ':', audio_string)
        os.remove(audio_file)

    def there_exists(self, terms):
        """
        Verifica se existe algo no que o usuário disse
        """
        for term in terms:
            if term in self.voice_data:
                return True

    def record_audio(self, ask=''):
        """
        Gera um audio de voz
        """
        with sr.Microphone() as source:
            if ask:
                print('Recording...')

            audio = self.r.listen(source)

            try:
                self.voice_data = self.r.recognize_google(audio)
                self.voice_data = self.voice_data.lower()
            except sr.UnknownValueError:
                print(f'Sorry {self.person}, I did not understand what you said. Please try again.')
            except sr.RequestError:
                print(f'Sorry {self.person}, my speech service is down. Please try again later.')

            if 'angel' in self.voice_data:
                print('You said: ' + self.voice_data)
                self.voice_data = self.voice_data.replace('angel', '')
                print('Looking at the data base...')
            else:
                self.voice_data = ''

    def respond(self, voice_data):
        """
        Responde ao usuário
        """
        self.record_audio('Listenin...')

        if self.there_exists(['hey', 'hi', 'hello']):
            greetings = [f'Hi {self.person}, what are you doing today?',
                         f'Hello {self.person}, how can I help you?',
                         f'Hey {self.person}, what can I do for you today?']

            greet = random.choice(greetings)
            self.engine_speak(greet)

        if self.there_exists(['who are you', 'who made you', 'who created you']):
            self.engine_speak('I am a virtual assistant. Created by Felipe Archanjo da Cunha Mendes.')

        if self.there_exists(['how are you', 'how is everything', 'how is life']):
            self.engine_speak('I am fine, thank you. How are you?')

        if self.there_exists(['search for']) and 'youtube' not in voice_data:
            search_term = self.voice_data.split('for')[-1]
            url = 'https://google.com/search?q=' + search_term
            webbrowser.get().open(url)
            self.engine_speak('Here is what I found for ' + search_term)

        if self.there_exists(['search on youtube for']):
            search_term = self.voice_data.split('for')[-1]
            url = 'https://www.youtube.com/results?search_query=' + search_term
            webbrowser.get().open(url)
            self.engine_speak('Here is what I found for ' + search_term)

        if self.there_exists(['what time is it', 'what is the time', 'tell me the time']):
            horas = datetime.datetime.now().hour
            minutos = datetime.datetime.now().minute
            segundos = datetime.datetime.now().second
            self.engine_speak(f"It is {horas} hours {minutos} minutes {segundos} seconds")

        if self.there_exists(['open google']):
            webbrowser.get().open('https://google.com')
            self.engine_speak('Here is your google.')

        if self.there_exists(['open youtube']):
            webbrowser.get().open('https://youtube.com')
            self.engine_speak('Here is your youtube.')

        if self.there_exists(['open facebook']):
            webbrowser.get().open('https://facebook.com')
            self.engine_speak('Here is your facebook.')

        if self.there_exists(['open instagram']):
            webbrowser.get().open('https://instagram.com')
            self.engine_speak('Here is your instagram.')

        if self.there_exists(['open twitter']):
            webbrowser.get().open('https://twitter.com')
            self.engine_speak('Here is your twitter.')

        if self.there_exists(['open spotify']):
            webbrowser.get().open('https://spotify.com')
            self.engine_speak('Here is your spotify.')

        if self.there_exists(['open netflix']):
            webbrowser.get().open('https://netflix.com')
            self.engine_speak('Here is your netflix.')

        if self.there_exists(['open twitch']):
            webbrowser.get().open('https://twitch.com')
            self.engine_speak('Here is your twitch.')

        if self.there_exists(['what is']):
            term = voice_data.split('is')[-1]
            wikipedia.set_lang('en')
            try:
                summary = wikipedia.summary(term, 2)
                self.engine_speak('According to Wikipedia, ' + summary)
            except:
                self.engine_speak('Sorry, I could not find what you are looking for.')

        if self.there_exists(['expecto patronum']):
            self.engine_speak(
                'you need to think of a memory. not just any memory, but a very happy memory, a very powerful memory')

        if self.there_exists(['play']):
            term = voice_data.replace('play', '')
            pywhatkit.playonyt(term)
            self.engine_speak(f'Playing {term}')

        if self.there_exists(['what\'s the weather in']):
            term = voice_data.split('in')[-1]
            url = 'https://www.google.com/search?q=weather+' + term
            webbrowser.get().open(url)
            self.engine_speak('Here is what I found for ' + term)

        if self.there_exists(['find location']):
            term = voice_data.replace('find location', '')
            url = 'https://www.google.com/maps/place/' + term
            webbrowser.get().open(url)
            self.engine_speak('Here is what I found for ' + term)

        if self.there_exists(['goodbye', 'bye', 'see you later', 'see you', 'goodbye']):
            self.engine_speak(f'Goodbye {self.person}, have a nice day!')
            exit()


assistent = VirtualAssist('Angel', 'Felipe')
while True:
    assistent.respond(assistent.voice_data)
