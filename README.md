![Logo of the project](https://stepik.org/static/frontend/topbar_logo.svg)

# Автоматизация тестирования с помощью Selenium и Python
> Stepik cources automation

A test project for the code review

## Installing / Getting started

A quick introduction of the minimal setup you need to get a result of project running.
1. Download and install the python from here https://www.python.org/downloads/
2. Download and install the Git-client from here https://git-scm.com/downloads
3. Open the shell in folder, where you want to clone the project, and type next commands

```shell
git clone git@github.com:Mikelyangello/finally_test_project_auto.git .
python -m venv /myvenv
./myvenv/Scripts/activate
pip install -r requirements.txt
```

You need to have an actual version of browsers Google Chrome and Mozilla Firefox,
and their web-drivers with correct PATH registration
Google Chrome browser - https://www.google.com/intl/en_ph/chrome/
Chromedriver - https://googlechromelabs.github.io/chrome-for-testing/

Mozilla Firefox browser - https://www.mozilla.org/en-US/firefox/new/
Mozilla geckodriver - https://github.com/mozilla/geckodriver/releases

## Code-review

You can check the code working process by use this commands 
in shell in project directory and activated virtual environment with installed packets
for example:
```shell
pytest -v --tb=line --language=en -m need_review
pytest -v --tb=line --language=en --delay=5 -m login_guest
pytest -v --tb=line --language=ru -m add_to_basket_user
pytest -v --tb=line --browser_name=firefox --language=en -m need_review
pytest
```

## Links

- Course homepage: https://stepik.org/course/575/info
- Useful pytest commands: https://gist.github.com/amatellanes/12136508b816469678c2
- Git course (russian language): https://youtu.be/W4hoc24K93E?si=9bT43zPhc_N_lURX
- About README - https://habr.com/ru/articles/810537/


## Licensing

"The code in this project is free software."

