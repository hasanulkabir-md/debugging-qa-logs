import requests

BASE = "http://127.0.0.1:5000"

def safe_request(method, url, **kwargs):
    try:
        resp = requests.request(method, url, **kwargs)
        print(f"{method.upper()} {url} → {resp.status_code}")
        try:
            print(resp.json())
        except Exception:
            print("❌ Response not JSON:", resp.text[:100])
    except requests.exceptions.ConnectionError:
        print(f"❌ Could not connect to {url} (Is the server running?)")

print("GET /products")
safe_request("get", f"{BASE}/products")

print("\nPOST /cart")
safe_request("post", f"{BASE}/cart")

print("\nPOST /checkout")
safe_request("post", f"{BASE}/checkout", json={"total": 100, "discount": 0})
