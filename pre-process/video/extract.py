import os
import argparse

# VIDEOS_PATH = '/DATA1/MultiModalDeepfake/FakeAVCeleb_Data/FakeVideo-FakeAudio'    # frames = 1
VIDEOS_PATH = '/DATA1/MultiModalDeepfake/FakeAVCeleb_Data/RealVideo-RealAudio'  # frames = 40

parser = argparse.ArgumentParser(description='Extract frames from video')
parser.add_argument('-f', '--frames', type=int, required = True, help='Number of frames to be extracted')
args = parser.parse_args()

EXTRACT_VIDEO_COMMAND = ('ffmpeg -i "{from_video_path}" -vf "select=eq(n\,{num_frames})" "{to_frames_path}" -f png  -y')

for root, dirs, files in os.walk(VIDEOS_PATH):
    for file in files:
        if not file.endswith('.mp4'):
            continue
        
        video_file_name = os.path.splitext(file)[0]
        # frames_path = os.path.join(root, 'extracted_frames/', video_file_name)  # fake videos
        frames_path = os.path.join(root, 'extracted_frames')  # real videos
        if not os.path.exists(frames_path): 
            os.makedirs(frames_path)
        
        command = EXTRACT_VIDEO_COMMAND.format(from_video_path= (os.path.join(root, file)),
                                               num_frames = args.frames-1 ,
                                                to_frames_path = (os.path.join(frames_path, "frame%03d.png")))
        os.system(command)
