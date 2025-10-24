import allure

from playwright.sync_api import Page, expect
from .base_page import BasePage
from playwright_config import config


class SignInPage(BasePage):
    """Page Object for Saleor Sign In page."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.logo = page.locator("svg.jss4")
        self.sign_in_title = page.get_by_text("Sign In", exact=True)
        self.email_input = page.locator("[data-test-id='email']")
        self.email_label = page.get_by_text("Email address")
        self.password_input = page.locator("[data-test-id='password']")
        self.password_label =page.get_by_text("Password", exact=True)
        self.show_pass_button = page.locator('[data-macaw-ui-component="Button"]:not([data-test-id="submit"])')
        self.forgot_password_link = page.get_by_role("link", name="Forgot password?")
        self.sign_in_button = page.locator("[data-test-id=\"submit\"]")

    # --- Actions ---
    @allure.step("Open TRG home page")
    def open_signin_page(self):
        self.open(config["base_url"])

    def sign_in(self, username: str, password: str):
        with allure.step("Sign in with provided credentials"):
            self.email_input.fill(username)
            self.password_input.fill(password)
            self.sign_in_button.click()


    # --- Asserts ---
    @allure.step("Validate all critical elements on Sign In page")
    def assert_page_elements(self):
        self.soft_check("Logo", lambda: expect(self.logo).to_be_visible(timeout=3000))
        self.soft_check("Title 'Sign In'", lambda: expect(self.sign_in_title).to_be_visible())
        self.soft_check("Email input", lambda: expect(self.email_input).to_be_visible())
        self.soft_check("Email label", lambda: expect(self.email_label).to_be_visible())
        self.soft_check("Password input", lambda: expect(self.password_input).to_be_visible())
        self.soft_check("Password label", lambda: expect(self.password_label).to_be_visible())
        self.soft_check("Show password button", lambda: expect(self.show_pass_button).to_be_visible())
        self.soft_check("Forgot password link", lambda: expect(self.forgot_password_link).to_be_visible())
        self.soft_check("Sign In button", lambda: expect(self.sign_in_button).to_be_visible())

        self.verify_soft_assertions()