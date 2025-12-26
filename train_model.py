from DataLoader import load_data

TRAINING_DATA_PATH = "../huruf_data/train"
LABEL_PATTERN = r"id_\d+_label_(\d+)\.png"

data = load_data(TRAINING_DATA_PATH, LABEL_PATTERN)
for img in data:
    print(img)
