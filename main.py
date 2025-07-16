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
    else:
        print(f"JSON file not found at {JSON_PATH}. Please ensure the file exists.")
        return None

data = load_json()
data_formatted = {}

if not data:
    print("No data found in the JSON file.")
    exit()
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

ordened_data = {key: data_formatted[key] for key in sorted(data_formatted)}

datas = list(ordened_data.keys())
values = list(ordened_data.values())
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))  # 1 linha, 2 colunas

# Gráfico de linha
ax1.plot(datas, values, marker='o', linestyle='-', color='blue')
ax1.axhline(y=11, color='red', linestyle='--', label='Meta (11)')
ax1.set_title("Hábitos ao longo do tempo (Linha)")
ax1.set_xlabel("Data")
ax1.set_ylabel("Valor")
ax1.grid(True)
ax1.legend()

# Gráfico de barras
ax2.bar(datas, values, color='blue')
ax2.axhline(y=11, color='red', linestyle='--', label='Meta (11)')
ax2.set_title("Hábitos ao longo do tempo (Barras)")
ax2.set_xlabel("Data")
ax2.set_ylabel("Valor")
ax2.set_xticklabels(datas, rotation=45)
ax2.grid(axis='y')
ax2.legend()

plt.tight_layout()
plt.show()
