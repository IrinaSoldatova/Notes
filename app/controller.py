class NoteController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        self.model.load_notes()

        while True:
            self.view.display_menu()
            choice = self.view.get_input("Enter your choice: ")

            if choice == '1':
                title = self.view.get_input("Enter the title of the note: ")
                body = self.view.get_input("Enter the body of the note: ")
                self.model.add_note(title, body)
            elif choice == '2':
                self.model.list_notes()