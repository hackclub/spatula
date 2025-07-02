import time
import schedule
import httpx

print("This is a spatula project")

def main():
    text = "We've been trying to reach you about your car's extended warranty"
    httpx.post(
        "https://ntfy.sh/your-unique-channel",
        data=text,
        headers={
            "Title": "This is totally really important",
            "Tags": "rotating_light",
        },
    )
    print(
        f'Posted: "{text}" to https://ntfy.sh/your-unique-channel'
    )


if __name__ == "__main__":
    main()
    schedule.every(10).minutes.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)