import cv2
import os
import face_detection

print(face_detection.available_detectors)
detector = face_detection.build_detector("DSFDDetector")

def access_files_from_subdirectory(root_dir, target_subdir):
    for root, dirs, files in os.walk(root_dir):
        if target_subdir in dirs:
            subdir_path = os.path.join(root, target_subdir)

            for new_root, new_dirs, new_files in os.walk(subdir_path):
                for file in new_files:
                    if not file.endswith('.png'):
                        continue
                    im = cv2.imread(os.path.join(new_root, file))[:, :, ::-1]
                    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

                    detections = detector.detect(im)
                    for det in detections[:1]:            
                        if len(det) < 5:
                            continue

                        xmin = det[0]
                        ymin = det[1]
                        xmax = det[2]
                        ymax = det[3]
                        score = det[4]

                        xmin, ymin, xmax, ymax = round(xmin), round(ymin), round(xmax), round(ymax)
                        frame = im[ymin:ymax, xmin:xmax]
                        frame = cv2.resize(frame, (224, 224))
                        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                    frame_path = os.path.join(new_root, file)
                    cv2.imwrite(frame_path, frame)

directory = '/DATA1/MultiModalDeepfake/FakeAVCeleb_Data'
target_subdirectory = 'extracted_frames'
access_files_from_subdirectory(directory, target_subdirectory)
