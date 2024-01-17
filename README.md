# Event Notifier

This Python script checks the Stark Arena website for events happening on the current day and sends an email alert with the event details. Each event on this specific website is within it's own link and script checks links from the main page for dates. If there is event with today's date then the link for the event is parsed for email subject.
You can modify it to check custom websites.

## Requirements

- Python 3
- pip

## Installation

1. Clone this repository.
2. Install the required Python packages using pip:


```bash
pip install -r requirements.txt
```

## Usage

1. Open eventnotifier.py and replace 'sendermailaddress@gmail.com' and 'password' with your Gmail address and password.
2. Run the script:

```bash
python eventnotifier.py
```

The script will check the Stark Arena website for events happening on the current day. If it finds an event, it will send an email with the event details.

## Note

This script uses Gmail's SMTP server to send the email. If you're using 2-Step Verification, you'll need to generate and use an App Password. If you're not using 2-Step Verification, you'll need to allow less secure apps to access your account.

This script could be best utilized by configuring cron job to run it daily.

## Disclaimer

This script is for educational purposes only. Always respect the terms of use of the website you're scraping.
