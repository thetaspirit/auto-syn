# auto-syn
Automatically grabs a digest of grades from Synergy and emails to some recipient(s)

## Variables you need to change
* `USERNAME`: Synergy username, change this in the code
* `PASSWORD`: This is linked to the __system environment variable `PY_PASS`__, which is your Synergy password.  You will need to set this environment variable.
* `EMAIL_PASS`: This is linked to the __system environment variable `PY_EMAIL_PASS`__, which is the password to the email account you're having this program send from.  You will need to set this environment variable.
* `SENDER`: The email address that this program is using to send the emails.
* `RECEIVER`: The email address you want this program to send reports to.

## Running the program
The program can be run with `python3 auto.py`.

You can set an anacron job to run this every once in a while if you wish.

## Dependencies
Remember to `pip3 install selenium` and `pip3 install bs4`.

If using FireFox, get Mozilla geckodriver from here: https://github.com/mozilla/geckodriver/releases.  Put the binary into the `PATH`.  I recommend the `/usr/bin` directory.

## Sidenote
This isn't intended to be "good" code, but it should work, and does its job as a utility script decently well 
