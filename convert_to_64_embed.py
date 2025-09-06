# encode_sounds.py
# This script reads specified .wav files, encodes their contents in base64,
# and writes the encoded strings to new .txt files.
# which you can replace in timer_app.py 
import base64

for filename in ["mario_bros.wav"]:
    with open(filename, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    with open(filename + ".txt", "w") as out:
        out.write(encoded)

print("Done. Check half.wav.txt and end.wav.txt")
