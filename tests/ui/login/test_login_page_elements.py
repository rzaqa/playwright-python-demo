import pytest
import allure
from pages.signin_page import SignInPage

@allure.feature("Login Page")
@allure.title("UI-LOGIN-001: Login page contains all critical elements")
@allure.tag("UI-LOGIN-001")
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.component
def test_signin_page_elements(page):
    """
    Verifies that the Sign-In page displays all essential elements correctly.
    """
    signin_page = SignInPage(page)

    with allure.step("Open Saleor Sign In page"):
        signin_page.open_signin_page()

    with allure.step("Verify that all critical elements are visible and labeled correctly"):
        signin_page.assert_page_elements()
