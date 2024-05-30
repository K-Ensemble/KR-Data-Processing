import os
import json

def find_wav_files(directory):
    wav_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".wav"):
                wav_files.append(os.path.join(root, file))
    return wav_files

def create_json_data(wav_files):
    json_data = []
    for wav_file in wav_files:
        data = {
            "wav": wav_file,
            "seg_label": "",
            "labels": "/m/0818ms,/m/0918jw,/m/1105jh,/m/04szw,/m/028sqc,/m/02p0sh1",
            "caption": "Korean traditional music"
        }
        json_data.append(data)
    return json_data

def save_json_data(json_data, output_file):
    with open(output_file, "w") as file:
        json.dump(json_data, file, indent=4)

directory = "C:\\Users\\wise-temp-1\\kr-data"  # 탐색할 디렉토리 경로 설정
output_file = "C:\\Users\\wise-temp-1\\kr-data\\output.json"  # 출력 JSON 파일 이름 설정

wav_files = find_wav_files(directory)
json_data = create_json_data(wav_files)
save_json_data(json_data, output_file)