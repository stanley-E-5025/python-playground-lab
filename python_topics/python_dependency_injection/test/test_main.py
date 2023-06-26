import pytest

from python_topics.python_dependency_injection.main import TextEditor, show_text


def test_handle_text():
    text_editor = TextEditor()
    assert text_editor.handle_text("This is a text") == "This is a text"


def test_show_text():
    text_editor = TextEditor()
    assert show_text("note:", text_editor) == "note: This is dependency injection"
