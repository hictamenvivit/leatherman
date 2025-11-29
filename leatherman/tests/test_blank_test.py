from teach_french.blank_text import add_blanks_to_line, add_blanks_to_song


SAMPLE_LINE = "Je suis un cheval blanc"
SAMPLE_SONG = """
Je suis un cheval blanc
Il mange des sushis noirs

"""


class TestBlankTest:

    def test_add_blank_to_line(self):
        assert add_blanks_to_line(SAMPLE_LINE) == "Je ____ un ______ _____"

    def test_add_blanks_to_song(self):
        assert (
            add_blanks_to_song(SAMPLE_SONG)
            == """Je ____ un ______ _____
Il _____ des ______ _____"""
        )
