# 🤖 DISHA — Digital Intelligent System for Human Assistant

A **full-featured Python voice assistant** that lives on your PC. Talk to her naturally — she controls your apps, files, browser, system settings, and more. Speaks back every response in real time.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        main.py                              │
│   (event loop · dispatcher · undo handler)                  │
└────┬─────────────┬──────────────┬───────────────────┬──────┘
     │             │              │                   │
┌────▼────┐  ┌────▼────┐  ┌─────▼─────┐  ┌──────────▼──────┐
│  VOICE  │  │   AI    │  │ SECURITY  │  │   ACTION MODULES │
│  INPUT  │  │  BRAIN  │  │   GATE    │  │                  │
│  Layer  │  │  (LLM)  │  │ PIN/Confirm│  │ pc_control       │
│         │  │         │  │           │  │ file_manager     │
│ wake    │  │ OpenAI  │  │ dangerous │  │ web_services     │
│ word    │  │   +     │  │ action    │  │ automation       │
│ detect  │  │ offline │  │ guard     │  │ writing_assistant│
│ mic →   │  │ fallback│  │           │  │ screen_reader    │
│ text    │  │         │  │           │  │ smart_home       │
└─────────┘  └────┬────┘  └───────────┘  └──────────────────┘
                  │
           ┌──────▼──────┐
           │  CONTEXT    │
           │  MANAGER    │
           │  (memory,   │
           │  pronouns,  │
           │  follow-ups)│
           └─────────────┘
```

**Data flow:**
```
Voice / Keyboard  →  Context resolve  →  AI Brain  →  Security gate  →  Dispatcher  →  Module
                                                                                        ↓
                                          ← speak() ← ─ ─ ─ ─ ─ ─ ─ ─ ─ result ← ─ ─ ┘
```

---

## 📂 Project Structure

```
DISHA/
├── main.py                   ← Entry point. Run this!
├── config.py                 ← All settings (wake words, app map, security PIN …)
├── requirements.txt
├── .env.example              ← Copy to .env, add your API keys
│
├── core/
│   ├── voice_input.py        ← Mic listener + wake-word detection (background thread)
│   ├── voice_output.py       ← TTS: pyttsx3 (offline) + ElevenLabs (optional)
│   ├── ai_brain.py           ← LLM integration + offline rule-based fallback
│   ├── context_manager.py    ← Conversation memory, pronoun resolution
│   └── security.py           ← Permission gates, PIN, emergency stop
│
├── modules/
│   ├── pc_control.py         ← Open/close apps, volume, brightness, Wi-Fi, power
│   ├── file_manager.py       ← Find, create, delete, compress, organise, clean
│   ├── web_services.py       ← Google, YouTube, Wikipedia, news, downloads
│   ├── automation.py         ← Trigger & scheduled automations, multi-step runner
│   ├── writing_assistant.py  ← Notes, reminders, PDF summarisation
│   ├── screen_reader.py      ← Screenshot + OCR screen reading
│   └── smart_home.py         ← IoT device stubs (light, fan, AC, TV)
│
├── utils/
│   ├── logger.py             ← Activity log with undo support
│   └── helpers.py            ← Shared utilities, memory I/O, speak shortcut
│
└── data/
    ├── memory.json           ← Persistent user profile & preferences
    ├── automations.json      ← Saved automation routines
    └── activity_log.json     ← Full action history
```

---

## ⚡ Quick Setup (Windows)

### 1. Install Python 3.10+
Download from [python.org](https://www.python.org/downloads/).

### 2. Install dependencies
```bash
cd DISHA
pip install -r requirements.txt
```

### 3. (Optional) Install Tesseract OCR
For screen-reading features. Download from:
[https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

Add `tesseract.exe` to your system PATH.

### 4. (Optional) Add API keys
Copy `.env.example` → `.env` and paste your keys:
- **OPENAI_API_KEY** — gives DISHA a full AI brain (GPT-4o-mini). Without it, she uses the built-in offline rule engine.
- **ELEVENLABS_API_KEY** — ultra-realistic female voice (optional; pyttsx3 works fine offline).

### 5. Run DISHA
```bash
python main.py
```

---

## 🗣️ How to Use

### Voice mode
1. DISHA starts listening in the background.
2. Say **"Hey DISHA"** to wake her up.
3. Speak your command naturally.
4. She speaks the response back to you.

### Keyboard mode
Just type your command at the `>` prompt — same AI brain processes it.

---

## 📋 Command Reference

| Category | Say… | What happens |
|----------|------|--------------|
| **Apps** | "Open Chrome" | Launches Chrome |
| | "Close VS Code" | Kills VS Code |
| **Search** | "Search Python tutorials" | Opens Google |
| | "YouTube lo-fi music" | Opens YouTube search |
| | "Wikipedia black holes" | Opens Wikipedia |
| **Files** | "Find my resume" | Searches common folders |
| | "Create folder Projects" | Creates on Desktop |
| | "Delete old_file.txt" | Moves to Recycle Bin (with confirmation) |
| | "Compress my Documents" | Zips the folder |
| | "Organise my Downloads" | Sorts by file type |
| | "Clean junk files" | Deletes .tmp, .log, .bak … |
| **System** | "Volume up / down" | Adjusts system volume |
| | "Brightness to 70" | Sets screen brightness |
| | "Wi-Fi off" | Disables Wi-Fi |
| | "Bluetooth on" | Enables Bluetooth |
| | "Shutdown" | Shuts down PC (asks PIN) |
| | "Restart" | Restarts PC (asks PIN) |
| | "Sleep" | Puts PC to sleep (asks PIN) |
| **Automation** | "Good morning" | Wi-Fi on → News → Chrome |
| | "Good night" | Wi-Fi off → Sleep |
| | "Start work" | Chrome + VS Code |
| **Notes** | "Remind me to buy milk" | Saves a reminder |
| | "What are my reminders" | Lists active reminders |
| **Screen** | "Take a screenshot" | Captures screen |
| | "What's on my screen" | OCR reads visible text |
| **Smart Home** | "Turn on the light" | Controls light (stub) |
| | "Set AC to 24" | Controls AC (stub) |
| **Meta** | "Undo" | Reverses last action |
| | "Stop everything" | Emergency kill-switch |
| | "Help" | Lists capabilities |
| | "Quit" | Exits DISHA |

---

## 🔐 Security

- **Dangerous actions** (shutdown, delete, send email) always ask **yes/no** confirmation.
- **Admin actions** (shutdown, restart, delete) additionally require your **PIN** (default: `1234` — change in `config.py`).
- **Emergency stop** ("Stop everything") halts all pending tasks instantly.
- **Activity log** records every action DISHA takes. Reviewable via `data/activity_log.json`.
- **Undo** reverses the last action where possible (e.g. open↔close app, Wi-Fi toggle).

---

## 🧠 How the AI Brain Works

```
User speech
    │
    ▼
Context Manager          ← resolves "it", "that", remembers last app/file/query
    │
    ▼
AI Brain (OpenAI)        ← understands intent, returns JSON action OR text reply
    │  (fallback: offline rule engine if no API key)
    ▼
Security Gate            ← confirms dangerous actions, checks PIN
    │
    ▼
Dispatcher               ← routes to the right module
    │
    ▼
Module executes          ← pc_control, file_manager, web_services …
    │
    ▼
Result spoken back       ← pyttsx3 / ElevenLabs TTS
```

---

## 🚀 Extending DISHA

1. **Add a new app** — edit `APP_MAP` in `config.py`.
2. **Add a new automation** — edit `DEFAULT_AUTOMATIONS` in `config.py` or say "create automation…".
3. **Add a new module** — create a file in `modules/`, import it in `main.py`, add routes to `dispatch()`.
4. **Change wake word** — edit `WAKE_WORDS` in `config.py`.
5. **Change PIN** — edit `SECURITY_PIN` in `config.py`.
6. **Switch to ElevenLabs voice** — set `TTS_ENGINE = "elevenlabs"` in `config.py` and add your key to `.env`.

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `SpeechRecognition` | Mic input + Google Speech API |
| `pyaudio` | Microphone access |
| `pyttsx3` | Offline text-to-speech |
| `openai` | GPT-4o-mini AI brain |
| `pyautogui` | Mouse, keyboard, screenshots |
| `Pillow` | Image processing |
| `pytesseract` | OCR (needs Tesseract installed) |
| `psutil` | System info |
| `schedule` | Scheduled automations |
| `requests` | Web downloads |
| `python-dotenv` | .env file loading |
| `PyPDF2` | PDF text extraction |

---

*Built with ❤️ — DISHA is ready to help you, Subhra!*
