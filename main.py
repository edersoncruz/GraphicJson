from pathlib import Path
import json
import os
import matplotlib.pyplot as plt
from datetime import datetime

JSON_PATH = Path('files') / 'habits.json'

def load_json():
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

data = load_json()
data_formatted = {}

for key, _list in data.items():
    count = 0
    if key == "_habits_list":
        continue
    else: 
        data_formatted[key] = count
        key_formatted = datetime.strptime(key, "%Y-%m-%d").date()
        data_hoje = datetime.now().date()
        
        if key_formatted > data_hoje:
            data_formatted.pop(key, None)
            continue
        for value in _list.values():
            if value == True:
                count += 1
                data_formatted[key] = count

datas = list(data_formatted.keys())
values = list(data_formatted.values())

plt.figure(figsize=(10,5))
plt.plot(datas, values, marker='o', linestyle='-', color='blue')

plt.title("Hábitos ao longo do tempo")
plt.xlabel("Data")
plt.ylabel("Valor")
plt.grid(True)
plt.tight_layout()

plt.show()
