from script import Canvas, Temp
from pathlib import Path


class TestCanvas:

    def test_generate_final(self):
        canvas = Canvas("Temp.canvas")
        Path("final.md").write_text(canvas.concatenated_text)
