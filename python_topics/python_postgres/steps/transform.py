import random

from steps.extract import extract_all_notes


# TAKE EXTRACT AS AN INPUT AND TRANSFORM THE ARRAY ADDING EMOJIS
def transform_all_notes():

    notes: str = extract_all_notes()
    parsed_notes = []

    emojis_list = ["🚀", "💡", "💻", "🏚", "🔨", "🐍", "🚧", "📟", "🔥", "💰", "🍗", "🗑", "📓", "🔐"]

    for items in notes:
        tuple_to_list = list(items)

        tuple_to_list.append(emojis_list[random.choice([*range(5)])])
        parsed_notes.append(tuple_to_list)
    return parsed_notes
