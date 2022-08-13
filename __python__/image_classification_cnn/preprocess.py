import os
import pickle
import numpy as np

DATASET_DIR = "cifar-10-batches-py"


def unpickle(file):
	with open(f"{DATASET_DIR}/{file}", "rb") as fo:
		dict = pickle.load(fo, encoding="bytes")
	return dict

if __name__ == "__main__":
	for dir, folder, files in list(os.walk(DATASET_DIR)):
		for file in files:
			if file.startswith("data"): print(unpickle(file)) 