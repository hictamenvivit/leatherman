# coding: utf-8
import os
import re


class File:
    def __init__(self, path):
        self.scene, self.shot, self.take = None, None, None
        self.path = path
        self.title = path.split(".zprj")[0].replace(" ", "")
        # if "AMB" in self.title:
        self.amb = "AMB" in self.title or "SS" in self.title
        if not self.amb:
            regex = r"^S(.*)P(.*)T(.*)"
            assert re.match(regex, self.title), self.title
            self.scene, self.shot, self.take = re.findall(regex, self.title)[0]
        self.files = [
            os.path.join(self.path, x)
            for x in os.listdir(self.path)
            if x.endswith(".WAV")
        ]


ffiles = [File(x) for x in os.listdir(".") if x != ".DS_Store"]

scenes = {x.scene for x in ffiles if x.scene}

for scene in scenes:
    shots = {x.shot for x in ffiles if x.scene == scene}
    print(f"shots for scene {scene} : {shots}")
    for shot in shots:
        files = {x for x in ffiles if x.shot == shot and x.scene == scene}
        for file in files:
            for trackfile in file.files:
                name = trackfile.split("/")[-1]
                os.renames(
                    trackfile, os.path.join("0" + scene, shot, file.take + "_" + name)
                )
