import os
# import librosa
# from statistics import mean

VIDEOS_PATH = '/DATA1/MultiModalDeepfake/FakeAVCeleb_Data'
VIDEOS_EXTENSION = '.mp4'
AUDIO_EXT = 'wav'

# -y: overwrites, -ar: sampling rate, -f: format, -vn: no video
EXTRACT_VIDEO_COMMAND = ('ffmpeg -i "{from_video_path}" -f {audio_ext} -ar 16000 -vn "{to_audio_path}" -y')

for root, dirs, files in os.walk(VIDEOS_PATH):
    for file in files:
        if not file.endswith(VIDEOS_EXTENSION):
            continue
        video_file_name = os.path.splitext(file)[0] # saves the file name and removes extension
        audio_file_name = '{}.{}'.format(video_file_name, AUDIO_EXT)
        command = EXTRACT_VIDEO_COMMAND.format(from_video_path= (os.path.join(root, file)), 
                                                audio_ext=AUDIO_EXT, 
                                                to_audio_path = (os.path.join(root, audio_file_name)))

        os.system(command)

### Average audio length ###

# AUDIO_PATH = '/DATA1/MultiModalDeepfake/FakeAVCeleb_Data'
# AUDIO_EXTENSION = '.wav'
# duration_list = []

# for root, dirs, files in os.walk(AUDIO_PATH):
#     for file in files:
#         if not file.endswith(AUDIO_EXTENSION):
#             continue
#         duration = librosa.get_duration(path = (os.path.join(root, file)))
#         duration_list.append(duration)

# mean_duration = mean(duration_list)
# print("Average duration of audio is %f"%(mean_duration))
