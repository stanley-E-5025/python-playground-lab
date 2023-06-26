class TextEditor:
    def handle_text(self, text: str) -> str:
        if not isinstance(text, str):
            raise TypeError("text should be of type str")
        return text


def show_text(title: str, text: TextEditor) -> None:

    result = ""
    try:
        note = text.handle_text("This is dependency injection")
        result = f"{title} {note}"
    except Exception as e:
        print(f"An error occurred: {e}")

    return result


def main() -> None:
    text = TextEditor()
    show_text(title="note:", text=text)


if __name__ == "__main__":
    main()
