import os
from dataclasses import dataclass

EXTENSIONS = [".mp4", ".mkv", ".avi"]
SUB_EXTENSIONS = [".srt", ".sub"]

ROOT = "/Volumes/maxone/Films"


@dataclass
class Film:
    year: int
    title: str
    director: str
    country: str
    continent: str
    original_path: str

    @property
    def proper_path(self):
        return os.path.join(
            ROOT,
            self.continent,
            self.country,
            self.director,
            f"{self.title} ({self.year})",
            f"{self.title} ({self.year}).{self.extension}",
        )

    @property
    def proper_sub_path(self):
        return os.path.join(
            self.continent,
            self.country,
            self.director,
            f"{self.title} ({self.year})",
            f"{self.title} ({self.year}).srt",
        )

    @property
    def extension(self):
        return self.video_file.split(".")[-1]

    @property
    def video_file(self):
        try:
            video_file = next(
                x
                for x in os.listdir(self.original_path)
                if any(x.endswith(ext) for ext in EXTENSIONS)
            )
            return os.path.join(self.original_path, video_file)
        except StopIteration:
            return

    @property
    def subtitles_file(self):
        try:
            video_file = next(
                x
                for x in os.listdir(self.original_path)
                if any(x.endswith(ext) for ext in SUB_EXTENSIONS)
            )
            return os.path.join(self.original_path, video_file)
        except StopIteration:
            return

    def rename(self):
        os.makedirs(os.path.dirname(self.proper_path), exist_ok=True)
        os.rename(self.video_file, self.proper_path)
        if self.subtitles_file:
            os.rename(self.subtitles_file, self.proper_sub_path)


def interactive():
    year = input("Year: ")
    title = input("Title: ")
    director = input("Director: ")
    country = input("Country: ")
    continent = input("Continent: ")
    original_path = input("Original path: ")

    film = Film(
        year=year,
        title=title,
        director=director,
        country=country,
        continent=continent,
        original_path=original_path,
    )
    film.rename()
