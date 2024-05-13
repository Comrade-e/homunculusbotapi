import torch
import os
from pydub import AudioSegment
from pydub.playback import play


def turn_on():
    if 'model' not in globals():
        device = torch.device('cpu')
        torch.set_num_threads(9)
        local_file = 'model.pt'

        if not os.path.isfile(local_file):
            torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v4_ru.pt',
                                           local_file)
        global model
        model = (torch.package.PackageImporter(local_file).load_pickle("tts_models", "model"))
        model.to(device)
    for i in range(2):
        audio_paths = model.save_wav(text='амогус',
                                     speaker='aidar',
                                     sample_rate=48000)
    if os.path.exists('test.wav'):
        os.remove('test.wav')

def say(what, s='aidar'):
    if 'model' not in globals():
        device = torch.device('cpu')
        torch.set_num_threads(9)
        local_file = 'model.pt'

        if not os.path.isfile(local_file):
            torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v4_ru.pt',
                                           local_file)
        global model
        model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
        model.to(device)
    audio_paths = model.save_wav(text=what,
                                     speaker=s,
                                     sample_rate=48000)

    play(AudioSegment.from_wav("test.wav"))
    if os.path.exists('test.wav'):
        os.remove('test.wav')