# 🔒 Invisible Watermark Tool

Secure your images like a digital creator should.  
This tool embeds an **invisible, encrypted watermark** into images using:

- 🧠 SHA-256 hashing (for unique creator ID)
- 🔐 AES-256 encryption (for watermark confidentiality)
- 🧾 Logging system (to track embed/verify events)
- ⏱️ Timestamp ledger (to prove when a file was watermarked)

> Built modularly and transparently using Python + OpenAI guidance.

---

## 👤 Creator Note

This project was built in real-time through hands-on testing, terminal navigation, and guided iteration with ChatGPT (OpenAI). It represents both technical functionality and a philosophy:  
**Digital sovereignty + creative authorship = protection + power.**

---

## 🛠️ Features

- ✅ Embed invisible encrypted watermark into PNG images
- ✅ Extract and verify watermark for creator validation
- ✅ Log every embed/verify event (with UTC timestamps)
- ✅ Maintain a local SHA-256 hash ledger for future proof
- ✅ Built with modular, scalable file structure

---

## 💾 Project Structure

invisible_watermark_tool/
├── main.py # Embeds watermark
├── config.py # Loads .env config
├── .env # Contains CREATOR_ID and SECRET_KEY (not pushed)
├── utils/
│ ├── hasher.py # SHA-256 hash creator ID
│ ├── aes_cipher.py # AES encrypt/decrypt watermark
│ ├── logger.py # Logs events
│ └── timestamping.py # Logs file hashes + time
├── verify/
│ └── extract.py # Extracts + verifies watermark
├── logs/ # Watermark event logs
├── data/ # Hash ledger
├── assets/ # Original + watermarked images
├── requirements.txt # Dependencies
├── README.md


---

## ⚙️ Setup Instructions

1. **Clone the repo**  
```bash

Create virtual environment

python3 -m venv .venv
source .venv/bin/activate
Install dependencies

pip install -r requirements.txt
Create your .env

CREATOR_ID=YourUniqueName
SECRET_KEY=your-super-secret-key
🧪 Usage
Embed watermark into image

python3 main.py
Add your image to assets/original/test_image.png, and it’ll output to assets/watermarked/.

Verify watermark

python3 verify/extract.py
Checks if the embedded watermark matches your creator ID.
----------------------------------------------------------------------------------------------------------------------------


🧠 Philosophy
This tool isn’t just about hiding a message—it’s about proof of origin in a world where digital content is easily stolen, remixed, and misattributed.

It’s built for creators who believe:

In protecting their voice, art, and authorship

That digital ownership shouldn’t be an afterthought

That AI can be used with intention, not just automation

📜 License
MIT (or add one of your choice)

✨ Credits
Built by nellx-io
In collaboration with OpenAI's ChatGPT
Documented + structured through real-time co-piloting

“Code is magic with logic. And this one whispers your name in the pixels.”








