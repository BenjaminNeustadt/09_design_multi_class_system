# Plan for multi class design

> As a user
> So that I can record my experiences
> I want to keep a regular diary

> As a user
> So that I can reflect on my experiences
> I want to read my past diary entries

--> Should be an option for viewing all of the entries, and then viewing
particular entries.

--> One class Diary
functions = add(), view()

individually? or all of them.

> As a user
> So that I can reflect on my experiences in my busy day
> I want to select diary entries to read based on how much time I have and my
> reading speed

- Here we can re-use some of the logic we have for the past challenges
  and exercises

> As a user
> So that I can keep track of my tasks
> I want to keep a todo list along with my diary

- How would this actually be implemented? Would it be that if the word
todo appears inside an entry it automatically gets added to my todo
list?

- What is meant by "along with my diary"?

- If this is the case, an instance of a todo would be created if there
  is the word todo prefixed somewhere. The todo class has its own
functions:

reading_time.
mark_complete

there is a todolist class, which has a few functions:
give_up (or mark_all_as_complete).

Show those which are complete: True
Show those which are incomplete: False

> As a user
> So that I can keep track of my contacts
> I want to see a list of all of the mobile phone numbers in all my diary
> entries

If there is a number in a diary entry, should it be prefixed by the word
"number"? Or should it contain the correct length of numbers? For
instance:

02072814097 is correct
0207281409 is incorrect

Or should it have the correct prefix. How to define it?

