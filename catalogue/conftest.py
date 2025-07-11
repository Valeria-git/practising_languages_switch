import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption(
        '--language', 
        action='store', 
        default='en',
        help='Choose language: en, ru, es, fr or de'
    )

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print(f"\nStarting Chrome browser with language: {language}")

    if language not in ['en', 'ru', 'es', 'fr', 'de']:
        raise pytest.UsageError("--language should be one of: en, ru, es, fr, de")

    options = Options()
    options.add_argument("--incognito")
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    options.add_argument(f"--lang={language}")

    driver = webdriver.Chrome(options=options)

    yield driver

    print("\nQuitting browser..")
    driver.quit()