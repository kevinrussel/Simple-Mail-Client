# Simple Mail Client (Python)

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

Important: Many email providers (like Gmail) require an App Password instead of your normal password if you have 2FA enabled.