import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_interface_languages(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    button = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
# assert button == true
    assert button, "button not found"
    time.sleep(11)