import pytest

@pytest.fixture
def web_browser(selenium):

    browser = selenium
    browser.set_window_size(2000, 1500)