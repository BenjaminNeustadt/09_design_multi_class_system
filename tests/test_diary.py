from lib.diary import *
from lib.diary_entry import *

# > As a user
# > So that I can record my experiences
# > I want to keep a regular diary




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

# > As a user
# > So that I can reflect on my experiences
# > I want to read my past diary entries

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

def test_diary_can_select_optimal_diary_entry_example_1():
    diary = Diary()
    diary_entry = DiaryEntry("First Entry", one_hundred_words)

    diary.add(diary_entry)

    actual = diary.find_best_entry_for_reading_time(100, 1)
    expected = diary_entry
    assert actual == expected


def test_diary_can_select_optimal_diary_entry_example_2():
    diary = Diary()
    diary_entry_2 = DiaryEntry("First Entry", two_hundred_words)
    diary_entry = DiaryEntry("First Entry", one_hundred_words)

    diary.add(diary_entry)
    diary.add(diary_entry_2)

    actual = diary.find_best_entry_for_reading_time(100, 1)
    expected = diary_entry
    assert actual == expected


