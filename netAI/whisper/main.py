import sys
import whisper
import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

print("Running on python version:", sys.version)
print("Using device:", DEVICE)

print("Loading model base")
model = whisper.load_model("base", device=DEVICE)

