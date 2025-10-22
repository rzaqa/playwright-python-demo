import requests
import json
import time
import allure
from playwright_config import config

PING_QUERY = {
    "query": "{ shop { name domain { host } __typename } }"
}

@allure.step("Pre-check: Verify backend GraphQL service is available")
def test_verify_backend_alive(timeout: int = 10, retries: int = 3, delay: int = 3):
    """
    Check if backend GraphQL API responds and schema is valid.
    Retries a few times before failing.
    """
    url = config.get("graphql_url")
    last_error = None

    for attempt in range(1, retries + 1):
        try:
            response = requests.post(url, json=PING_QUERY, timeout=timeout)
            if response.status_code != 200:
                raise AssertionError(
                    f"Unexpected status code {response.status_code}: {response.text}"
                )

            data = response.json()
            if "data" not in data or "shop" not in data["data"]:
                raise AssertionError(f"Unexpected data format: {data}")

            print(f"✅ Backend GraphQL service is available at: {url}")
            return True

        except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
            last_error = str(e)
            print(f"⚠️ Attempt {attempt}/{retries} failed: {last_error}")
            if attempt < retries:
                time.sleep(delay)
            else:
                raise AssertionError(
                    f"❌ Backend pre-check failed for {url} after {retries} attempts: {last_error}"
                )
