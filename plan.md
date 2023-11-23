# Plan for multi class design

> As a user
> So that I can record my experiences
> I want to keep a regular diary

> As a user
> So that I can reflect on my experiences
> I want to read my past diary entries

--> Should be an option for viewing all of the entries, and then viewing
particular entries.

/// DONE

--> One class Diary
functions = add(), view()

/// DONE

individually? or all of them.

/// DONE


STILL TO DO:

> As a user
> So that I can reflect on my experiences in my busy day
> I want to select diary entries to read based on how much time I have and my
> reading speed

should it select the closest one to the parameters given?
What if there are two given?

- Here we can re-use some of the logic we have for the past challenges
  and exercises

> As a user
> So that I can keep track of my tasks
> I want to keep a todo list along with my diary

- How would this actually be implemented? Would it be that if the word
todo appears inside an entry it automatically gets added to my todo
list?

The way I can think of is to have a constructor attribute that calls a
method to check whether any of the entries have the word "todo" inside
of them, if they do, then a Todo class instance is created and that
entry is added to it. That is all that I can think of in regards the
following questions.

- What is meant by "along with my diary"?

- If this is the case, an instance of a todo would be created if there
  is the word todo prefixed somewhere. The todo class has its own
functions:

reading_time.
mark_complete

# Todo class attributes and behaviour

## functions:
There is a todolist class, which has a few functions:

* give_up() (or mark_all_as_complete).
* mark_complete()

## attributes:

Show those which are complete: True
Show those which are incomplete: False

# Phone numbers

> As a user
> So that I can keep track of my contacts
> I want to see a list of all of the mobile phone numbers in all my diary
> entries

If there is a number in a diary entry, should it be prefixed by the word
"number"? Or should it contain the correct length of numbers? For
instance:

so it could look something like this:

```
class Diary:

    def __init__(self)
        self.list_of_entries = []
        self.todos = find_todos(self.list_of_entries)
        # the return would be either: "currently no todos" or a list of todos
        self.list_of_numbers = find_any_numbers(self.list_of_entries)
        # the return would be either "currently no numbers" or a list of
          numbers
        # there isn't anything about attributing a name to each number, the
        # phone number would have to be input in a very particular format in order
        # for that to work

    def parse_todos(self):
        list_of_todos = []
        given a list of entries:
           if any of the entries.title or the entry.content include the word "todo":
            then create an instance of Todo class called todo
                then list_of_todos.append(that todo entry)
        if list_of_todos is empty:
            return "currently no todos"

        else:
            return list_of_todos


# for phone numbers:

class PhoneNumber:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def change_name(self, new_name):
        self.name = new_name
```

02072814097 is correct
0207281409 is incorrect

Or should it have the correct prefix. How to define it?

