'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple
simple functions. They could be as simple as add and subtract or more complex
such as functions that read and write to files.

Instead of writing out the functions, only provide the tests.
Think about how the functions might fail and write tests that will
check and prevent failure.

You do not need to implement the actual functions after writing the
tests but you may.

'''
import pytest


# Defining empty functions for future:
def file_reader():
    """Function reads .txt file with text.
    Returns variable containing text from the file."""
    pass


def search_count():
    """Function searches through text to count specsific words.
    Prints out a dictionary with words count."""
    pass


# Test block:
class TestTDD:

    def test_IOerror(self):
        self.pytest.raises(IOError, file_reader, "file.txt")

    def test_is_txt(self):
        self.pytest.raises("CustomException", file_reader, "file.py")

    def test_empty():
        assert file_reader("file.txt") != ""

    def test_have_word():
        assert "word" in file_reader("file.txt")

    def test_found_something():
        some_text = file_reader("file.txt")
        assert len(search_count(some_text)) > 0
