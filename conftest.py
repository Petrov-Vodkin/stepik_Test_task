import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# добавляем праметр к тестам "--browser_name" & "--user_language"
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="default",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, fr,......")


@pytest.fixture(scope="function")
def browser(request):
    # с помощью ф-ии request получаем browser_name, browser_lang заданные в командной строке при запуске теста
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    print(f"\nstart {browser_name} browser for test..")
    if browser_name == "default":
        print("\nChrome browser selected by DEFAULT ")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()