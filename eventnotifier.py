import requests
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# Get today's date in the required format
date = datetime.now().strftime("%d.%m.%Y.")

# Send a GET request to the URL
response = requests.get('https://starkarena.co.rs/lat/')

# Parse the HTML response
soup = BeautifulSoup(response.text, 'html.parser')

# Flag to indicate whether a link with today's date was found
found = False

# Iterate over all links on the page
for link in soup.find_all('a'):
    # Check if the entire HTML structure of the link contains today's date
    if date in str(link):
        # Print the link and the date
        print(f'Link: {link["href"]}, Date: {date}')
        found = True

        # Extract all text up to "Detalji"
        subject_extra = link["href"].replace("lat/", "").replace("-", " ")
        print(subject_extra)

        # Prepare the email
        msg = MIMEText(f'Link: {link["href"]}, Date: {date}')
        msg['Subject'] = f'Arena - {subject_extra}'
        msg['From'] = 'Arena Alert sendermailaddress@gmail.com'
        msg['To'] = 'receivermailaddress@gmail.com'

        # Send the email
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('sendermailaddress@gmail.com', 'password')
        s.send_message(msg)
        s.quit()

# If no link with today's date was found, print a message
if not found:
    print(f'There are no events on {date}')

# Clear the requests file
with open('requests', 'w') as file:
    pass
