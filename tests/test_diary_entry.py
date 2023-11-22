from lib.diary_entry import *

# > As a user
# > So that I can record my experiences
# > I want to keep a regular diary

#
# > As a user
# > So that I can reflect on my experiences
# > I want to read my past diary entries


def test_diary_entry():
    diary = DiaryEntry("Title", "A first entry")

    title_attribute = diary.title
    content_attribute = diary.content

    expected_title = "Title"
    expected_content = "A first entry"

    assert title_attribute == expected_title
    assert content_attribute == expected_content
