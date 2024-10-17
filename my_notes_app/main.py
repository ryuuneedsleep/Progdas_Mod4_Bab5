from notes_manager import NotesManager

def menu():
    manager = NotesManager()
    
    while True:
        print("\n1. Add Note")
        print("2. View All Notes")
        print("3. View Note Details")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            manager.add_note(title, content)
        elif choice == '2':
            manager.view_notes()
        elif choice == '3':
            manager.view_notes()
            index = int(input("Enter the index of the note to view: "))
            manager.view_note_detail(index)
        elif choice == '4':
            manager.view_notes()
            index = int(input("Enter the index of the note to edit: "))
            new_title = input("Enter new title: ")
            new_content = input("Enter new content: ")
            manager.edit_note(index, new_title, new_content)
        elif choice == '5':
            manager.view_notes()
            index = int(input("Enter the index of the note to delete: "))
            manager.delete_note(index)
        elif choice == '6':
            print("Exiting the notes manager.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()