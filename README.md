# auto-syn
Automatically grabs a digest of grades from Synergy and emails to some recipient(s)

## Setup
Things to be edited (sending/receiving email, etc) can be found by searching for `#CHANGE HERE` comments.

2 environment variables can be set: `PY_PASS` and `PY_EMAIL_PASS`

The program can be run with `python3 auto.py`

Remember to `pip3 install selenium` and `pip3 install bs4`.

If using FireFox, get Mozilla geckodriver from here: https://github.com/mozilla/geckodriver/releases

You can set an anacron job to run this every once in a while if you wish.

## Sidenote
This isn't intended to be "good" code, but it should work, and does its job as a utility script decently well 
