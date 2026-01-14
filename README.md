# Simple Mail Client (Python)


<img src="images/mail.webp" width="400" alt="Demo Screenshot">


A small command-line Python script that sends an email through an SMTP server.  
It supports:

- Custom subject + message body
- Using a premade message from `message.txt`
- Optionally embedding an inline image (from an `images/` folder)

---

## Features

- **Interactive CLI prompts** for subject, message, recipient, and image choice
- **Plain text email body** (always attached)
- **Optional HTML part** that displays an embedded inline image using a `Content-ID` (`cid:image1`)
- **Credentials loaded from JSON** (`password.json`)

---

## Project Structure

Recommended structure:
.
├── main.py # your script (rename as you like)
├── password.json # SMTP config + credentials (not committed)
├── message.txt # premade message (optional)
└── images/
└── cat.png # example image to embed


## Requirements

- Python 3.8+ recommended (should work on most 3.x versions)
- No extra packages required (uses Python standard library)

---

## Setup

### 1) Create `password.json`

Create a file named `password.json` in the same folder as the script:

```json
{
  "server": "smtp.gmail.com",
  "port": 587,
  "sender_email": "you@example.com",
  "password": "YOUR_PASSWORD_OR_APP_PASSWORD"
}
```

Important: Many email providers (like Gmail) require an App Password instead of your normal password if you have 2FA enabled.

### 2) (Optional) Create message.txt

If you want the premade message option to work, add a message.txt file:

Hello!

This is a premade message sent from my Python mail client.

### 3) (Optional) Add images

Put images inside the images/ folder.
When prompted, you’ll type the image file name (example: cat.png), and the script will look for:

images/cat.png

Run

From the project folder:

python main.py


You’ll be prompted for:

Recipient email

Subject line

Whether to write your own message (yes) or use message.txt (no)

Whether to embed an inline image (yes/no)

If yes, the image filename inside images/

How the embedded image works

If you choose to embed an image, the script:

Adds an HTML part that references the image using:

src="cid:image1"

Attaches the image with:

Content-ID: <image1>

Content-Disposition: inline

Some email clients display inline images differently. If you don’t see it inline, check the email’s “attachments” area.

### Notes / Known Limitations

No error handling yet (there’s a #TODO in the code)

Assumes the image exists inside images/

Assumes password.json exists and contains all required keys

Sends using STARTTLS (server.starttls()), which works for most SMTP providers on port 587

Security Tips

Do not commit password.json to GitHub.

Add this to a .gitignore:

password.json

Future Improvements (ideas)

Add validation + error handling for missing files and bad SMTP login

Support attachments (not just inline images)

Support multiple recipients

Add a non-interactive mode using CLI arguments (argparse)

Store secrets in environment variables instead of JSON