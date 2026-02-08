"""
DISHA - Digital Intelligent System for Human Assistant
========================================================
config.py - Central configuration. Edit values here to customize behaviour.
"""

import os, sys, json
from pathlib import Path
from dotenv import load_dotenv

# --- Paths -------------------------------------------------------------------
BASE_DIR          = Path(__file__).resolve().parent
DATA_DIR          = BASE_DIR / "data"
LOGS_DIR          = BASE_DIR / "logs"
MEMORY_FILE       = DATA_DIR / "memory.json"
AUTOMATIONS_FILE  = DATA_DIR / "automations.json"
ACTIVITY_LOG_FILE = DATA_DIR / "activity_log.json"

# --- Environment / API Keys --------------------------------------------------
load_dotenv(BASE_DIR / ".env")                          # create .env with your keys
OPENAI_API_KEY    = os.getenv("OPENAI_API_KEY", "")     # paste your key here or in .env
ELEVENLABS_KEY    = os.getenv("ELEVENLABS_API_KEY", "")

# --- Wake Word ---------------------------------------------------------------
WAKE_WORDS = ["hey disha", "hey d i s h a", "disha"]    # recognized triggers

# --- Voice Input -------------------------------------------------------------
RECOGNITION_LANGUAGE  = "en-IN"       # en-US, en-IN, hi-IN, bn-IN ...
AMBIENT_TIMEOUT       = 2             # seconds of silence before ambient phase ends
PHRASE_TIMEOUT        = 8             # max seconds to wait for a phrase after wake
PHRASE_TIME_LIMIT     = 10            # hard cap on one utterance (seconds)

# --- Voice Output (pyttsx3) -------------------------------------------------
TTS_ENGINE            = "pyttsx3"     # "pyttsx3" | "elevenlabs"
TTS_RATE              = 165           # words per minute  (pyttsx3)
TTS_VOLUME            = 1.0           # 0.0 - 1.0         (pyttsx3)
TTS_VOICE_INDEX       = 1             # 0 = male, 1 = female (OS-dependent; check list)

# --- AI Brain ----------------------------------------------------------------
OPENAI_MODEL          = "gpt-4o-mini" # lightweight but capable
AI_MAX_TOKENS         = 1024
AI_TEMPERATURE        = 0.4
# system prompt that gives DISHA her personality
AI_SYSTEM_PROMPT      = (
    "You are DISHA (Digital Intelligent System for Human Assistant), a smart, polite, "
    "friendly female PC voice assistant. You run directly on the user's Windows computer "
    "and can control apps, files, the browser, and more.\n\n"
    "Rules:\n"
    "- Be concise. Respond in 1-3 short sentences unless detail is asked.\n"
    "- If the user's intent maps to a PC action, reply with ONLY a JSON block like:\n"
    '  {"action":"<action_name>","params":{...}}\n'
    "  Available actions: open_app, close_app, search_google, open_url, play_youtube,\n"
    "  set_volume, set_brightness, wifi_toggle, bluetooth_toggle, find_file,\n"
    "  create_folder, delete_file, compress_folder, shutdown, restart, sleep,\n"
    "  take_screenshot, run_automation, write_note, summarize, send_email.\n"
    "- If it's a conversation, just reply naturally.\n"
    "- Always remember the user's name: Subhra.\n"
    "- Be warm, encouraging, slightly humorous.\n"
)

# --- Security ----------------------------------------------------------------
SECURITY_PIN          = "1234"        # change this!
DANGEROUS_ACTIONS     = [             # these always need confirmation
    "shutdown", "restart", "sleep", "delete_file", "send_email",
    "compress_folder", "run_automation"
]
ADMIN_ACTIONS         = ["shutdown", "restart", "sleep", "delete_file"]

# --- PC Control --------------------------------------------------------------
# Map friendly names -> executable paths (Windows).  Add your own.
APP_MAP = {
    "chrome":           "chrome",
    "google chrome":    "chrome",
    "browser":          "chrome",
    "firefox":          "firefox",
    "edge":             "msedge",
    "vs code":          "code",
    "visual studio code":"code",
    "notepad":          "notepad",
    "calculator":       "calc",
    "file explorer":    "explorer",
    "explorer":         "explorer",
    "task manager":     "taskmgr",
    "discord":          "discord",
    "spotify":          "spotify",
    "whatsapp":         "whatsapp",
    "vlc":              "vlc",
    "google drive":     "googledrive",
    "cmd":              "cmd",
    "powershell":       "powershell",
    "paint":            "mspaint",
    "word":             "winword",
    "excel":            "excel",
    "powerpoint":       "powerpnt",
}

# --- File Management ---------------------------------------------------------
JUNK_EXTENSIONS  = {".tmp",".log",".bak","~",".swp",".swo",".dmp"}
SEARCH_ROOTS     = [Path.home(), Path.home()/"Documents", Path.home()/"Downloads",
                    Path.home()/"Desktop", Path.home()/"Pictures"]
ORGANIZE_RULES   = {                  # extension -> target subfolder in Downloads
    ".pdf":  "PDFs",
    ".doc":  "Documents", ".docx":"Documents",
    ".xls":  "Spreadsheets", ".xlsx":"Spreadsheets",
    ".jpg":  "Images", ".jpeg":"Images", ".png":"Images", ".gif":"Images",
    ".mp4":  "Videos", ".avi":"Videos", ".mkv":"Videos",
    ".mp3":  "Music", ".wav":"Music",
    ".zip":  "Archives", ".rar":"Archives", ".7z":"Archives",
    ".exe":  "Installers",
    ".py":   "Code", ".js":"Code", ".html":"Code", ".css":"Code",
}

# --- Automation --------------------------------------------------------------
# Pre-loaded automation routines  (trigger_phrase -> list of action dicts)
DEFAULT_AUTOMATIONS = {
    "good morning": [
        {"action": "wifi_toggle",   "params": {"state": True}},
        {"action": "open_url",      "params": {"url": "https://news.google.com"}},
        {"action": "open_app",      "params": {"app": "chrome"}},
    ],
    "good night": [
        {"action": "wifi_toggle",   "params": {"state": False}},
        {"action": "sleep",         "params": {}},
    ],
    "start work": [
        {"action": "open_app",      "params": {"app": "chrome"}},
        {"action": "open_app",      "params": {"app": "vs code"}},
    ],
    "backup files": [
        {"action": "compress_folder","params": {"folder": str(Path.home()/"Documents")}},
    ],
}

# --- Ensure data files exist -------------------------------------------------
def _init_data():
    DATA_DIR.mkdir(exist_ok=True)
    LOGS_DIR.mkdir(exist_ok=True)
    if not MEMORY_FILE.exists():
        MEMORY_FILE.write_text(json.dumps({
            "user_name": "Subhra",
            "location": "Kolkata, West Bengal",
            "preferences": {"language": "en-IN", "music_genre": "Hindi/Bengali"},
            "habits": [],
            "last_commands": []
        }, indent=2))
    if not AUTOMATIONS_FILE.exists():
        AUTOMATIONS_FILE.write_text(json.dumps(DEFAULT_AUTOMATIONS, indent=2))
    if not ACTIVITY_LOG_FILE.exists():
        ACTIVITY_LOG_FILE.write_text("[]")

_init_data()
