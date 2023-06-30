import os
import random
import shutil
import csv

class AudioDatasetSplitter:
    def __init__(self, root_dir, output_dir, train_ratio, test_ratio):
        self.data_dir = root_dir
        self.output_dir = output_dir

        self.train_ratio = train_ratio
        self.test_ratio = test_ratio

        self.classes = ['RealVideo-RealAudio', 'RealVideo-FakeAudio0', 'FakeVideo-RealAudio', 'FakeVideo-FakeAudio', ]
        self.ethnicities = ['Caucasian (American)', 'Caucasian (European)', 'African', 'Asian (East)', 'Asian (South)']
        self.set_names = ['train', 'test']

        
        self.audio_output_dir = os.path.join(output_dir, 'audio')
        self.csv_file = os.path.join(self.audio_output_dir, 'audio_dataset.csv')
        self.file_data = []

    def create_directories(self):
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.audio_output_dir, exist_ok=True)

        for set_name in self.set_names:
            os.makedirs(os.path.join(self.audio_output_dir, set_name), exist_ok=True)

    def split_dataset(self):
        self.create_directories()
        self.file_data = []

        for class_name in self.classes:
            class_dir = os.path.join(self.data_dir, class_name)
            for ethnicity in self.ethnicities:
                ethnicity_dir = os.path.join(class_dir, ethnicity)
                men_dir = os.path.join(ethnicity_dir, 'men')
                women_dir = os.path.join(ethnicity_dir, 'women')

                men_ids = self.get_person_ids(men_dir)
                women_ids = self.get_person_ids(women_dir)

                men_train, men_test = self.split_person_ids(men_ids)
                women_train, women_test = self.split_person_ids(women_ids)

                self.copy_files(men_dir, men_train, men_test)
                self.copy_files(women_dir, women_train, women_test)

        self.write_csv_file()

    def get_person_ids(self, dir_path):
        person_ids = []
        if os.path.exists(dir_path):
            person_ids = [d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d))]

        return person_ids

    def split_person_ids(self, person_ids):
        random.shuffle(person_ids)
        total_ids = len(person_ids)
        train_count = int(total_ids * self.train_ratio)
        test_count = total_ids - train_count

        train_ids = person_ids[:train_count]
        test_ids = person_ids[train_count:]

        return train_ids, test_ids

    def copy_files(self, source_dir, train_ids, test_ids):
        for set_name, ids in zip(self.set_names, [train_ids, test_ids]):
            set_dir = os.path.join(self.audio_output_dir, set_name)
            real_dir = os.path.join(set_dir, 'real')
            fake_dir = os.path.join(set_dir, 'fake')
            os.makedirs(real_dir, exist_ok=True)
            os.makedirs(fake_dir, exist_ok=True)

            for person_id in ids:
                person_dir = os.path.join(source_dir, person_id)
                wav_files = [file for file in os.listdir(person_dir) if file.endswith('.jpg')]
                for wav_file in wav_files:
                    source_path = os.path.join(person_dir, wav_file)
                    if self.get_label(source_path) == 'Real':
                        dest_path = os.path.join(real_dir, wav_file)
                    elif self.get_label(source_path) == 'Fake':
                        dest_path = os.path.join(fake_dir, wav_file)
                    else:
                        continue
                    shutil.copyfile(source_path, dest_path)
                    file_info = (wav_file, person_id, set_name, self.get_label(source_path), self.get_ethnicity(source_path), self.get_sex(source_path), dest_path)
                    self.file_data.append(file_info)


    def get_sex(self, dir_path):
        if 'men' in dir_path:
            return 'Men'
        elif 'women' in dir_path:
            return 'Women'
        else:
            return ''

    def get_ethnicity(self, dir_path):
        for ethnicity in self.ethnicities:
            if ethnicity in dir_path:
                return ethnicity
        return ''
    
    def get_label(self, dir_path):
        if 'RealAudio' in dir_path:
            return 'Real'
        elif 'FakeAudio' in dir_path:
            return 'Fake'
        else:
            return ''

    def write_csv_file(self):
        with open(self.csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['File Name', 'Person ID', 'Set Name', 'Label', 'Ethnicity', 'Sex', 'File Path'])
            writer.writerows(self.file_data)

root_dir = '/DATA1/MultiModalDeepfake/FakeAVCeleb_Data'
output_dir = '/DATA1/MultiModalDeepfake/akanksha/fakeavceleb/dataset'
train_ratio = 0.8
test_ratio = 0.2

splitter = AudioDatasetSplitter(root_dir, output_dir, train_ratio, test_ratio)
splitter.split_dataset()
