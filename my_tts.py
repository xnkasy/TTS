import subprocess
from pathlib import Path
def tts_call(input_file, tts_model_name, vocoder_model_name, output_path):
    txt = Path(input_file).read_text()
    if(tts_model_name==""):
        tts_model_name = "tts_models/en/ljspeech/tacotron2-DDC"
    if(vocoder_model_name==""):
        vocoder_model_name = "vocoder_models/en/ljspeech/hifigan_v2"
    subprocess.run(["tts","--text", txt, "--model_name", tts_model_name, "--vocoder_name", vocoder_model_name, "--out_path", output_path])