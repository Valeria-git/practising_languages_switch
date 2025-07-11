from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



def test_basket_button_exists(browser, request):
    language = request.config.getoption("language")
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)

    #time.sleep(30)
    basket_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")

    assert basket_button.is_displayed()
