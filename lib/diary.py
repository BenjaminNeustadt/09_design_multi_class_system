from lib.todo import *
import pdb

class Diary:

    def __init__(self):
        self.list_of_entries = []
        self.todos = []
        self.numbers = []

    def validate_if_todos(self, entry):
        if entry.title.lower().startswith("todo"):
            new_todo = Todo(entry.title, entry.content)
            self.todos.append(new_todo)

    def check_if_number(self, entry):
        word_elements = entry.content.split()
        for word in word_elements:
            if word.isdigit() and len(word) == 11:
                self.numbers.append(word)

    def add(self, entry):
        self.check_if_number(entry)
        self.validate_if_todos(entry)
        self.list_of_entries.append(entry)

    #=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
    # report functions and helpers +=+=+=+=
    #=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

    def report_numbers(self):
        list_of_numbers = []
        report_statement = "These are your numbers:"

        for number in self.numbers:
           list_of_numbers.append(f"\n-{number}")
        report_of_numbers = ''.join(list_of_numbers)
        final_report = f"{report_statement}{report_of_numbers}"
        return final_report


    def report_todos(self):
        list_of_todos = []
        report_statement = "These are your todos:"

        if len(self.todos) == 0:
            return "No todos added yet"

        for todo in self.todos:
           todo_name_without_prefix = todo.name.replace("Todo:", "").strip()
           list_of_todos.append(f"\n-{todo_name_without_prefix}: {todo.entry}")
        report_of_todos = ''.join(list_of_todos)
        final_report = f"{report_statement}{report_of_todos}"

        return final_report

    def find_entry(self, entry_title):
        for entry in self.list_of_entries:
            if entry.title == entry_title:
                return entry

    def report_(self, entry_title):
        if self.find_entry(entry_title):
            specific_entry = self.find_entry(entry_title)
            return f"This is {specific_entry.title} entry:\n{specific_entry.content}"
        else:
            return f"No entry found with the title '{entry_title}'"

    def report_entries(self):
        list_of_entry_reports = []
        report_statement = "These are your entries:"

        if len(self.list_of_entries) == 0:
            return "No entries added yet"

        for entry in self.list_of_entries:
           list_of_entry_reports.append(f"\n-{entry.title}: {entry.content}")

        report_of_entries = ''.join(list_of_entry_reports)
        final_report = f"{report_statement}{report_of_entries}"

        return final_report

    #=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
    # best reading time
    #=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

    def find_entry_for_reading_time(self, wpm, minutes):
        best_entry = None
        best_reading_time = float('inf')

        for entry in self.list_of_entries:
            entry_reading_time = entry.reading_time(wpm)
            if entry_reading_time <= minutes:
                if minutes - entry_reading_time < best_reading_time:
                     best_entry = entry
                     best_reading_time = minutes - entry_reading_time
        if best_entry:
            return best_entry
        else:
            return "No entries found that match those specifications"
