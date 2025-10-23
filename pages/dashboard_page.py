import allure
from playwright.sync_api import Page, expect
from .base_page import BasePage

import time


class DashboardPage(BasePage):
    """Page Object for the Saleor Dashboard after successful login."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_title = page.title()
        self.dashboard_title = page.get_by_text("Saleor Dashboard", exact=True)
        self.sidebar = page.get_by_role("complementary")
        self.admin_email_label = page.get_by_text("admin@example.com", exact=True)

    # --- Asserts ---
    @allure.step("Assert Dashboard page title is correct")
    def assert_page_title(self):
        """Verify that browser tab title matches expected Saleor Dashboard title."""
        title = self.page.title()
        assert "Dashboard | Saleor e-commerce" in title, \
            f"Unexpected page title: {title}"

    @allure.step("Validate all critical elements on Dashboard page for signed-in admin")
    def assert_dashboard_loaded_for_signed_in_admin(self, admin_email: str):
        """Run soft checks on all key elements to verify the Dashboard loaded correctly."""
        self.soft_check("Dashboard title visible",
                        lambda: expect(self.dashboard_title).to_be_visible(timeout=5000))
        self.soft_check("Sidebar visible",
                        lambda: expect(self.sidebar).to_be_visible())
        self.soft_check("Sidebar contains 'Saleor Dashboard' text",
                        lambda: expect(self.sidebar).to_contain_text("Saleor Dashboard"))
        self.soft_check(f"Logged-in admin email '{admin_email}' visible",
                        lambda: expect(self.page.get_by_text(admin_email, exact=True)).to_be_visible())

        # Final verification of all collected assertions
        self.verify_soft_assertions()
