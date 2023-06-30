import os
import time
import librosa
import numpy as np
import skimage.io

AUDIO_PATH = '/DATA1/MultiModalDeepfake/FakeAVCeleb_Data'
AUDIO_EXTENSION = '.wav'

sample_rate=16000

# preprocessing parameters
frame_length = int(0.025 * sample_rate)  # 25ms frame length
frame_shift = int(0.01 * sample_rate)  # 10ms frame shift
num_mfcc = 80  # number of MFCC coefficients

def scale_minmax(X, min=0.0, max=1.0):
    X_std = (X - X.min()) / (X.max() - X.min())
    X_scaled = X_std * (max - min) + min
    return X_scaled

for root, dirs, files in os.walk(AUDIO_PATH):
    for file in files:
        if not file.endswith(AUDIO_EXTENSION):
            continue

        audio_path = os.path.join(root, file)
        y, sr = librosa.load(audio_path, sr= sample_rate, duration = 7)
        mfcc_features = librosa.feature.mfcc(y = y,
                                            sr=sample_rate,
                                            n_fft=512,
                                            hop_length=frame_shift,
                                            win_length = frame_length,
                                            n_mfcc=num_mfcc,
                                            window='hann')
        
        # spec= torchaudio.compliance.kaldi.mfcc(waveform, sample_frequency=sr, window_type= 'hanning' ,num_ceps=80, num_mel_bins=512)

        mfcc_features = mfcc_features.T # transpose the MFCC features to have frames as rows and coefficients as columns
        spectogram = np.stack([mfcc_features] * 3, axis=-1)
        print('MFCC features shape:', spectogram.shape)

        audio_file_name = os.path.splitext(file)[0] # saves the file name and removes extension
        image_file_name = '{}.{}'.format(audio_file_name, 'jpg')
        img = scale_minmax(mfcc_features, 0, 255).astype(np.uint8)
        image_path = (os.path.join(root, image_file_name))
        skimage.io.imsave(image_path, img)
