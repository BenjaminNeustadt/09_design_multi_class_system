from lib.diary_entry import *

def test_diary_entry():
    diary = DiaryEntry("Title", "A first entry")

    title_attribute = diary.title
    content_attribute = diary.content

    expected_title = "Title"
    expected_content = "A first entry"

    assert title_attribute == expected_title
    assert content_attribute == expected_content
