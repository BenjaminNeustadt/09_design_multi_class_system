class DiaryEntry:

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def reading_time(self, wpm):
        list_of_words = self.content.split()
        number_of_words = len(list_of_words)
        return number_of_words / wpm

