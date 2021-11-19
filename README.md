# auto-syn
Automatically grabs a digest of grades from Synergy and emails to some recipient(s)

## Variables you need to change
Things to be edited (sending/receiving email, etc) can be found by searching for `#CHANGE HERE` comments.

2 environment variables can be set: `PY_PASS` and `PY_EMAIL_PASS`

## Running the program
The program can be run with `python3 auto.py`.

You can set an anacron job to run this every once in a while if you wish.

## Dependencies
Remember to `pip3 install selenium` and `pip3 install bs4`.

If using FireFox, get Mozilla geckodriver from here: https://github.com/mozilla/geckodriver/releases.  Put the binary into the `PATH`.  I recommend the `/usr/bin` directory.

## Sidenote
This isn't intended to be "good" code, but it should work, and does its job as a utility script decently well 
