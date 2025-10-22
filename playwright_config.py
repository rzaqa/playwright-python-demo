import os

from dotenv import load_dotenv

# Load .env file only if present (for local development)
load_dotenv()

ENV_TYPE = os.getenv("ENV_TYPE", "local")

# Headless mode: always True in CI, configurable locally
HEADLESS = True if ENV_TYPE == "CI" else False

# Timeout settings
DEFAULT_TIMEOUT = 10_000  # in milliseconds

# Browsers to run tests on
# BROWSERS = ["chromium", "firefox", "webkit"]
BROWSERS = ["chromium"]

# Folder paths
TESTS_DIR = "tests"
REPORTS_DIR = "test-results"

config = {
    "env_type": ENV_TYPE,
    "headless": HEADLESS,
    "browsers": BROWSERS,
    "timeout": DEFAULT_TIMEOUT,
    "tests_dir": TESTS_DIR,
    "reports_dir": REPORTS_DIR,
    "base_url": os.getenv("BASE_URL", "https://saleor-dashboard-228462058101.europe-central2.run.app/"),
}