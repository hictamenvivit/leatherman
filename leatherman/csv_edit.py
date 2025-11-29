from typer import Typer
from pathlib import Path


app = Typer()


@app.command()
def goodbye(name: str):
    print(f"Goodbye {name}")


@app.command()
def remove(filepath: str, sep=";", delete=None):
    if delete is None:
        return
    delete = delete.split(",")
    path = Path(filepath)
    content = path.read_text()
    lines = content.strip().split("\n")
    splitted = [line.split(sep) for line in lines]
    translated = [
        line
        for line in zip(*splitted)
        if line[0] not in delete
    ]
    path.write_text("\n".join([sep.join(line) for line in zip(*translated)]))


if __name__ == "__main__":
    app()
