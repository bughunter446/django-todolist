from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest


target_url = "http://test-server/"

print("########## Running the Selenium Script ##########")

@pytest.fixture(scope="session")
def get_driver():
    global driver
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    yield
    driver.close()

@pytest.mark.usefixtures("get_driver")
def test_data():
    driver.get(target_url)
    element = driver.find_element_by_class_name("title")
    print("########## Checking for title on the page ##########")
    assert element.text == "Dead simple Todolists."

@pytest.mark.usefixtures("get_driver")
def test_body():
    element = driver.find_element_by_class_name("navbar-link")
    print("########## Checking for Content on page ##########")
    assert element.text == "DJODOLIST"