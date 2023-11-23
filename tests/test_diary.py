from lib.diary import *
from lib.diary_entry import *
from lib.todo import *

def test_diary_exists():
    diary = Diary()

def test_diary_list_of_entries_is_initially_empty():
    diary = Diary()
    actual = diary.list_of_entries
    expected = []
    assert actual == expected

def test_diary_list_of_entries_can_be_added_to():
    diary = Diary()
    diary_entry = DiaryEntry("First ENtry", "This is the first time I write")
    actual = diary.list_of_entries
    expected = []
    assert actual == expected
    diary.add(diary_entry)
    actual = diary.list_of_entries
    expected = [diary_entry]
    assert actual == expected

# Would that just be the contents?

# "These are your entries:
# - "Title": "contents"
# - "Title 2": "contents again"
# "

def test_diary_has_report_function_for_viewing():
    diary = Diary()
    diary_entry = DiaryEntry("First Entry", "This is the first")
    second_diary_entry = DiaryEntry("Second Entry", "This is the second")

    diary.add(diary_entry)
    diary.add(second_diary_entry)

    actual = diary.report_entries()
    expected = "These are your entries:\n-First Entry: This is the first\n-Second Entry: This is the second"
    assert actual == expected

def test_diary_reports_when_no_entries():
    diary = Diary()
    diary_entry = DiaryEntry("First Entry", "This is the first")
    second_diary_entry = DiaryEntry("Second Entry", "This is the second")

    actual = diary.report_entries()
    expected = "No entries added yet"
    assert actual == expected

def test_diary_has_report_function_for_viewing_specific_entry():
    diary = Diary()
    diary_entry = DiaryEntry("First Entry", "This is the first")
    second_diary_entry = DiaryEntry("Second Entry", "This is the second")
    third_diary_entry = DiaryEntry("Third Entry", "This is the third")

    diary.add(diary_entry)
    diary.add(second_diary_entry)
    diary.add(third_diary_entry)

    actual = diary.report_("Third Entry")
    expected = "This is Third Entry entry:\nThis is the third"
    assert actual == expected

def test_diary_has_report_function_for_no_found_entry_by_that_title():
    diary = Diary()
    diary_entry = DiaryEntry("First Entry", "This is the first")
    second_diary_entry = DiaryEntry("Second Entry", "This is the second")

    diary.add(diary_entry)
    diary.add(second_diary_entry)

    actual = diary.report_("Third Entry")
    expected = "No entry found with the title 'Third Entry'"
    assert actual == expected

# > As a user
# > So that I can reflect on my experiences in my busy day
# > I want to select diary entries to read based on how much time I have and my
# > reading speed

# parameters given: wpm, minutes
# returns: diary entry that matches the reading parameters the closest

one_hundred_words = "one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one"
two_hundred_words = "one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one"
fifty_words = "one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one"

def test_diary_can_select_optimal_diary_entry_example_1():
    diary = Diary()
    diary_entry = DiaryEntry("First Entry", one_hundred_words)

    diary.add(diary_entry)

    actual = diary.find_entry_for_reading_time(100, 1)
    expected = diary_entry
    assert actual == expected


def test_diary_can_select_optimal_diary_entry_example_2():
    diary = Diary()
    diary_entry_2 = DiaryEntry("First Entry", two_hundred_words)
    diary_entry = DiaryEntry("First Entry", one_hundred_words)

    diary.add(diary_entry)
    diary.add(diary_entry_2)

    actual = diary.find_entry_for_reading_time(100, 1)
    expected = diary_entry
    assert actual == expected


def test_diary_can_select_optimal_diary_entry_example_3():
    diary = Diary()

    diary_entry = DiaryEntry("First Entry", one_hundred_words)
    diary_entry_2 = DiaryEntry("First Entry", two_hundred_words)
    diary_entry_3 = DiaryEntry("First Entry", fifty_words)

    diary.add(diary_entry)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)

    actual = diary.find_entry_for_reading_time(25, 2)
    expected = diary_entry_3
    assert actual == expected

# > As a user
# > So that I can reflect on my experiences in my busy day
# > I want to select diary entries to read based on how much time I have and my
# > reading speed

def test_diary_can_select_optimal_diary_entry_example_4():
    diary = Diary()

    diary_entry = DiaryEntry("First Entry", one_hundred_words)

    diary_entry_2 = DiaryEntry("Second Entry", two_hundred_words)
#    diary_entry_3 = DiaryEntry("Third Entry", fifty_words)

    diary.add(diary_entry)
    diary.add(diary_entry_2)
#    diary.add(diary_entry_3)

    actual = diary.find_entry_for_reading_time(50, 2)

    expected = diary_entry
    assert actual == expected


def test_diary_can_select_optimal_diary_entry_example_4():
    diary = Diary()

    diary_entry = DiaryEntry("First Entry", one_hundred_words)
    diary_entry_2 = DiaryEntry("Second Entry", two_hundred_words)
    diary.add(diary_entry)
    diary.add(diary_entry_2)

    actual = diary.find_entry_for_reading_time(50, 1)

    expected = "No entries found that match those specifications"

    assert actual == expected


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
# Todo integratino tests
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

    # NOTE: having it default to the next best is user friendly, but perhaps not
    # expected for an MVP?

    # the user should be told that there aren't any options that adher to those specifications


def tests_diary_can_create_todos():
    diary = Diary()
    diary_entry = DiaryEntry("Todo: Exercise", "Go for a walk")

    #todo = Todo(diary_entry.title, diary_entry.content)

    diary.add(diary_entry)
    actual = diary.todos[0].name

    expected = "Todo: Exercise"
    assert actual == expected

def tests_diary_can_only_adds_todos_to_todos():
    diary = Diary()
    diary_entry = DiaryEntry("Todo: Exercise", "Go for a walk")
    diary_entry_2 = DiaryEntry("Exercise", "Go for a walk")

    #todo = Todo(diary_entry.title, diary_entry.content)

    diary.add(diary_entry)
    diary.add(diary_entry_2)
    actual = len(diary.todos)

    expected = 1
    assert actual == expected

# > As a user
# > So that I can keep track of my tasks
# > I want to keep a todo list along with my diary
#


# ```
# NOTES:

# - How would this actually be implemented? Would it be that if the word
# todo appears inside an entry it automatically gets added to my todo
# list?
#
# The way I can think of is to have a constructor attribute that calls a
# method to check whether any of the entries have the word "todo" inside
# of them, if they do, then a Todo class instance is created and that
# entry is added to it. That is all that I can think of in regards the
# following questions.
#
# - What is meant by "along with my diary"?
#
# - If this is the case, an instance of a todo would be created if there
#   is the word todo prefixed somewhere. The todo class has its own
# functions:
#
# reading_time.
# mark_complete

# PSEUDO code:

# class Diary:
#
#     def __init__(self)
#
#         self.list_of_entries = []

#         self.todos = find_todos(self.list_of_entries)
#
#         # the return would be either: "currently no todos" or a list of todos
#         self.list_of_numbers = find_any_numbers(self.list_of_entries)
#         # the return would be either "currently no numbers" or a list of
#           numbers
#         # there isn't anything about attributing a name to each number, the
#         # phone number would have to be input in a very particular format in order
#         # for that to work
#
#     def parse_todos(self):
#         list_of_todos = []
#         given a list of entries:
#            if any of the entries.title or the entry.content include the word "todo":
#             then create an instance of Todo class called todo
#                 then list_of_todos.append(that todo entry)
#         if list_of_todos is empty:
#             return "currently no todos"
#
#         else:
#             return list_of_todos
#
#
#
#
