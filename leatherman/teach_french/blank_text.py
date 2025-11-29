from random import sample


def make_blank(word):
    return "_" * len(word)


def choose_indexes(sline, n=3):
    try:
        return sample([i for (i, e) in enumerate(sline) if len(e) > 3], n)
    except ValueError:
        return choose_indexes(sline, n - 1)


def add_blanks_to_line(line):
    sline = line.split(" ")
    indexes = choose_indexes(sline)
    return " ".join(
        [make_blank(x) if i in indexes else x for (i, x) in enumerate(sline)]
    )


def add_blanks_to_song(song):
    lines = song.strip().split("\n")
    return "\n".join([add_blanks_to_line(x) for x in lines])
