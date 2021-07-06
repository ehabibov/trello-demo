# Trello UI/API tests Demo

Requirements:\
`Python 3.7.4`

Install dependencies:\
`python3 -m pip install -r requirements.txt`

Tests execution:\
`python -m pytest tests -s` from project root dir

Test files executed in natiral order:
1. test_api.py
2. test_ui.py

### Some notes
This is my the very first test suite on Python. Before this task only requests library was a bit familiar to me and 
selenium (java impl, not pythonic).  
There are a lot of thing that could be better (logging, additional layers for objects/functions, syntax sugar) 
and there are some things that I still do not understand fully (TypeVar, typed function return statement static type check).

Comments left on tests which are failing due some library/trello issues. I haven't much time to resolve that.

Also, tests were implemented strictly to objectives without additional checks/bonus tasks as, again,
Python/selenium/requests are new for me.