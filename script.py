import os
import json

music_folder = "docs"
base_url = "https://yourusername.github.io/MyMusicFiles/"
playlist = {"songs": []}

for filename in os.listdir(music_folder):
    if filename.endswith(".mp3") or filename.endswith(".wav"):
        playlist["songs"].append(base_url + filename)

with open("docs/playlist.json", "w") as f:
    json.dump(playlist, f, indent=4)
