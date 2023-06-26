from flask import render_template
from steps.extract import extract_all_notes
from steps.transform import transform_all_notes

# JUST LOAD THE OUTPUT OF TRANSFORM TO USE IT IN FLASK RENDER


def load_notes():
    notes = transform_all_notes()
    return render_template("index.html", data=notes, raw_data=extract_all_notes())
