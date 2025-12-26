from pathlib import Path
import numpy as np
import cv2
import re

def load_data(data_path, label_pattern):
    data_path = Path(data_path)
    data = []
    for file in data_path.rglob('*'):
        img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        label = re.search(label_pattern, file.name).group(1)
        flattened = img.flatten() / 255.0
        flattened = np.insert(flattened, 0, int(label) - 1)
        data.append(flattened)
    return np.array(data)
