import pytest
from app import app as dash_app
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture
def app():
    return dash_app

def test_header_is_present(dash_duo):
    dash_duo.start_server(dash_app)
    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales Visualiser"

def test_graph_is_present(dash_duo):
    dash_duo.start_server(dash_app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

def test_radio_items_present(dash_duo):
    dash_duo.start_server(dash_app)
    radio = dash_duo.find_element("#region-selector")
    assert radio is not None
