import requests
import json
import allure
from playwright_config import config

PING_QUERY = {
    "query": "{ shop { name domain { host } __typename } }"
}


@allure.step("Pre-check: Verify backend GraphQL service is available")
def test_verify_backend_alive(timeout: int = 5):
    """Check if backend GraphQL API responds and schema is valid."""
    url = config.get("graphql_url")

    try:
        response = requests.post(url, json=PING_QUERY, timeout=timeout)
        if response.status_code != 200:
            raise AssertionError(f"Unexpected status code {response.status_code}: {response.text}")

        data = response.json()
        if "data" not in data or "shop" not in data["data"]:
            raise AssertionError(f"Unexpected data: {data}")

        print(f"✅ Backend GraphQL service is available at: {url}")
        return True

    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        raise AssertionError(f"❌ Backend pre-check failed for {url}: {str(e)}")
