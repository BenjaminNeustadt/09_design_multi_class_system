class Diary:

    def __init__(self):
        self.list_of_entries = []

    def add(self, entry):
        self.list_of_entries.append(entry)

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
