import requests
import time

SERVICES = {
    "api": "http://127.0.0.1:18080/health",
    "ai": "http://127.0.0.1:17877/health",
}

def check_services():
    print("EndCosmos health check\n")

    for name, url in SERVICES.items():
        try:
            r = requests.get(url, timeout=3)

            if r.status_code == 200:
                print(f"{name} : OK")
            else:
                print(f"{name} : ERROR {r.status_code}")

        except Exception as e:
            print(f"{name} : DOWN ({e})")

if __name__ == "__main__":
    while True:
        check_services()
        time.sleep(30)
