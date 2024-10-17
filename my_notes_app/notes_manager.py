from note import Note

class NotesManager:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        new_note = Note(title, content)
        self.notes.append(new_note)
        print(f"Note'{title}' added!")

    def view_notes(self):
        if not self.notes:
            print("No notes available.")
            return
        for i, note in enumerate(self.notes):
            print(f"[{i}] {note.title}")

    def view_note_detail(self, index):
        if 0 <= index < len(self.notes):
            note = self.notes[index]
            print(f"Title: {note.title}\nContent: {note.content}")
        else:
            print("Invalid index!")

    def edit_note(self, index, new_title, new_content):
        if 0 <= index < len(self.notes):
            self.notes[index].title = new_title
            self.notes[index].content = new_content
            print(f"Note [{index}] updated!")
        else:
            print("Invalid index!")

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            deleted_note = self.notes.pop(index)
            print(f"Note '{deleted_note.title}' deleted!")
        else:
            print("Invalid index!")