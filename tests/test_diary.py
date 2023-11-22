from lib.diary import *
from lib.diary_entry import *

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
