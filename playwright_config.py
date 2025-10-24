import os
import re

from dotenv import load_dotenv

# Load .env file only if present (for local development)
load_dotenv()

ENV_TYPE = os.getenv("ENV_TYPE", "local")

# Headless mode: always True in CI, configurable locally
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

# Timeout settings
DEFAULT_TIMEOUT = 10_000  # in milliseconds

# Browsers to run tests on
BROWSERS = ["chromium", "firefox", "webkit"]

# Folder paths
TESTS_DIR = "tests"
REPORTS_DIR = "test-results"

# Clean API base from dashboard URL
def derive_graphql_url(base_url: str) -> str:
    api_base = str.replace(r"-dashboard", "", base_url.rstrip("/"))
    return api_base + "/graphql/"


# Base URL
BASE_URL = os.getenv("BASE_URL") or "https://saleor-dashboard-228462058101.europe-central2.run.app/"
GRAPHQL_URL = os.getenv("GRAPHQL_URL") or "https://saleor-228462058101.europe-central2.run.app/graphql/"

config = {
    "env_type": ENV_TYPE,
    "headless": HEADLESS,
    "browsers": BROWSERS,
    "timeout": DEFAULT_TIMEOUT,
    "tests_dir": TESTS_DIR,
    "reports_dir": REPORTS_DIR,
    "base_url": BASE_URL,
    "graphql_url": GRAPHQL_URL,
    "admin_name": os.getenv("ADMIN_NAME"),
    "admin_passw": os.getenv("ADMIN_PASSW"),
}


