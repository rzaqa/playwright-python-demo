import os
import allure
import pytest
from pages.signin_page import SignInPage
from pages.dashboard_page import DashboardPage

@allure.feature("Admin SignIn")
@allure.title("E2E: Successful admin login with valid credentials")
@allure.tag("AUTH-ADMIN-LOGIN-001")
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.e2e
def test_admin_login_success(page):
    """Verifies that an admin can log in successfully and reach the Dashboard."""
    # --- Test Data ---
    admin_name = os.getenv("ADMIN_NAME")
    admin_passw = os.getenv("ADMIN_PASSW")

    signin_page = SignInPage(page)

    with allure.step("Open Saleor Sign In page"):
        signin_page.open_signin_page()

    with allure.step("Fill in login credentials and sign in"):
        signin_page.sign_in(admin_name, admin_passw)

    dashboard_page = DashboardPage(page)

    with allure.step("Verify dashboard loads successfully and admin email is displayed in the dashboard menu"):
        dashboard_page.assert_dashboard_loaded_for_signed_in_admin(admin_name)
        dashboard_page.assert_page_title()

