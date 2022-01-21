import os, json

files = [file.replace(".json", "") for file in os.listdir("shortkuts/")]

files.remove("shortkut-list")

with open("shortkuts/shortkut-list.json", "w+") as f:
    f.write(json.dumps(files))
