"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser
from models.github_page import github_page


def test_github_desktop(driver_setup):
    if browser.config.window_width < 1000:
        pytest.skip('Mobile version')
    github_page.open()
    github_page.desktop_sign_in()
    github_page.should_have_text_sign_in()


def test_github_mobile(driver_setup):
    if browser.config.window_width > 1000:
        pytest.skip('Desktop version')
    github_page.open()
    github_page.mobile_sign_in()
    github_page.should_have_text_sign_in()
