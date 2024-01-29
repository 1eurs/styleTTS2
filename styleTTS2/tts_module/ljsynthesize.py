import styleTTS2jspeech.tts_module.ljspeechimportable as ljspeechimportable

import torch
from tortoise.utils.text import split_and_recombine_text
import numpy as np
import soundfile as sf

def ljsynthesize(text, steps):
    noise = torch.randn(1, 1, 256).to('cuda' if torch.cuda.is_available() else 'cpu')
    texts = split_and_recombine_text(text)
    audios = []
    for t in texts:
        audios.append(ljspeechimportable.inference(t, noise, diffusion_steps=steps, embedding_scale=1))
    return (24000, np.concatenate(audios))


