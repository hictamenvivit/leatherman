from pathlib import Path

from dataclasses import dataclass


@dataclass
class Folder:
    letter: str
    destination: Path


SOURCE = Path("/Users/maximebettinelli/Desktop")
TARGET = Path("/Users/maximebettinelli/Desktop")

FOLDERS = [
    Folder(letter, SOURCE / destination)
    for (letter, destination) in [
        ("p", "projs"),
        ("o", "other"),
        ("i", "investigate"),
        ("d", "trash"),
    ]
]


for file in SOURCE.iterdir():
    letter = input(file.name + "\n")
    for f in FOLDERS:
        if f.letter == letter:
            file.rename(f.destination / file.name)
            break
