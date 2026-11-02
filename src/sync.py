"""Sync availability and bookings between the channel manager and the reservation gateway."""
import os
import time

import requests

BASE_URL = os.environ["RSV_GATEWAY_BASE_URL"]
HEADERS = {
    "X-Client-Id": os.environ["RSV_GATEWAY_CLIENT_ID"],
    "X-Api-Key": os.environ["RSV_GATEWAY_API_KEY"],
}


def pull_availability(session):
    response = session.get(f"{BASE_URL}/availability", headers=HEADERS, timeout=30)
    response.raise_for_status()
    return response.json()


def main():
    session = requests.Session()
    while True:
        rooms = pull_availability(session)
        print(f"synced {len(rooms)} room types")
        time.sleep(int(os.environ.get("SYNC_INTERVAL_SECONDS", "300")))


if __name__ == "__main__":
    main()
