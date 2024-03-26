import datetime
import json
import random


class NoteModel:
    def __init__(self):
        self.notes = []

    def load_notes(self):
        try:
            with open('notes.json', 'r') as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            self.notes = []

    def save_notes(self):
        with open('notes.json', 'w') as file:
            json.dump(self.notes, file, indent=4)

    def add_note(self, title, body):
        note_id = random.randint(1, 100000)
        while any(note['id'] == note_id for note in self.notes):
            note_id = random.randint(1, 100000)

        new_note = {
            'id': note_id,
            'title': title,
            'body': body,
            'date and time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.notes.append(new_note)
        self.save_notes()
        print("Note saved")