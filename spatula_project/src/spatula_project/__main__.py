from datetime import datetime
import random
import time
import httpx
import schedule

print("This is a spatula project")

NTFY_TOPIC = "well-hi-there"


def get_event() -> str:
    date_today = datetime.now().strftime("%m/%d")
    r = httpx.get(
        f"https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/holidays/{date_today}",
    )
    data = r.json()
    event_summaries = [e["text"] for e in data["holidays"]]
    # Pick a random
    random_event_summary = random.choice(event_summaries)
    return random_event_summary


def main():
    text = get_event()
    httpx.post(
        f"https://ntfy.sh/{NTFY_TOPIC}",
        data=text,
        headers={
            "Title": "Random Holiday Occuring Today",
            # https://docs.ntfy.sh/publish/#message-priority
            # "Priority": "default",
            "Tags": "rewind",
        },
    )
    print(
        f'Posted: "{text}" to https://ntfy.sh/{NTFY_TOPIC}'
    )


if __name__ == "__main__":
    main()
    schedule.every(10).minutes.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)