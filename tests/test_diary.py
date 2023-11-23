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

    diary.add(diary_entry)
    actual = diary.todos[0].name

    expected = "Todo: Exercise"
    assert actual == expected

def tests_diary_can_only_adds_todos_to_todos():
    diary = Diary()
    diary_entry = DiaryEntry("Todo: Exercise", "Go for a walk")
    diary_entry_2 = DiaryEntry("Exercise", "Go for a walk")

    diary.add(diary_entry)
    diary.add(diary_entry_2)
    actual = len(diary.todos)

    expected = 1
    assert actual == expected

def tests_diary_can_report_todos():
    diary = Diary()
    diary_entry = DiaryEntry("Todo: Exercise", "Go for a walk")
    diary_entry_2 = DiaryEntry("Todo: Housecleaning", "Scrub the windows")

    diary.add(diary_entry)
    diary.add(diary_entry_2)

    actual = len(diary.todos)
    expected = 2
    assert actual == expected

    actual = diary.report_todos()
    expected = "These are your todos:\n-Exercise: Go for a walk\n-Housecleaning: Scrub the windows"
    assert actual == expected

# > As a user
# > So that I can keep track of my contacts
# > I want to see a list of all of the mobile phone numbers in all my diary
# > entries

def tests_diary_has_numbers_attribute():
    diary = Diary()
    diary_entry = DiaryEntry("Christmas day", "Go for a walk")

    diary.add(diary_entry)
    actual = diary.numbers
    expected = []
    assert actual == expected

def tests_diary_can_parse_numbers():
    diary = Diary()
    diary_entry = DiaryEntry("Numbers of friends", "I met an old friend who gave their number: 07596802695 alfie ")

    diary.add(diary_entry)
    actual = diary.numbers
    expected = ['07596802695']
    assert actual == expected

def tests_diary_can_parse_numbers_multiple():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Numbers of friends", "I met an old friend who gave their number: 02072804108 Jordan ")
    diary_entry = DiaryEntry("Numbers of friends", "I met an old friend who gave their number: 07596802695 alfie ")

    diary.add(diary_entry)
    diary.add(diary_entry_1)
    actual = diary.numbers
    expected = ['07596802695', '02072804108']
    assert actual == expected

def tests_diary_find_numbers_ignores_invalid():
    diary = Diary()
    diary_entry = DiaryEntry("Numbers of friends", "I met an old friend who gave their number: 07596802695 alfie ")
    diary_entry_1 = DiaryEntry("Numbers of friends", "I met an old friend who gave their number: 02072804108 Jordan ")
    diary_entry_2 = DiaryEntry("Numbers of friends", "I met an old friend who gave their number: 07596695 alfie ")

    diary.add(diary_entry)
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    actual = diary.numbers
    expected = ['07596802695', '02072804108']
    assert actual == expected

