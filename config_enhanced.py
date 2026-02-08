"""
DISHA - Digital Intelligent System for Human Assistant
========================================================
config_enhanced.py - Enhanced configuration for JARVIS-like capabilities
"""

import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv

# --- Paths -------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"
MEMORY_FILE = DATA_DIR / "memory.json"
AUTOMATIONS_FILE = DATA_DIR / "automations.json"
ACTIVITY_LOG_FILE = DATA_DIR / "activity_log.json"

# --- Environment / API Keys --------------------------------------------------
load_dotenv(BASE_DIR / ".env")

# AI Provider Selection
# Options: "gemini" (FREE, recommended), "openai", or "auto" (tries both)
AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini")

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")      # Google Gemini (FREE tier)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")     # OpenAI GPT (paid)
ELEVENLABS_KEY = os.getenv("ELEVENLABS_API_KEY", "") # Premium voice (optional)

# --- Wake Word ---------------------------------------------------------------
WAKE_WORDS = ["hey disha", "hey d i s h a", "disha", "jarvis"]

# --- Voice Input -------------------------------------------------------------
RECOGNITION_LANGUAGE = "en-IN"  # en-US, en-IN, hi-IN, bn-IN
AMBIENT_TIMEOUT = 2  # seconds of silence before ambient phase ends
PHRASE_TIMEOUT = 8  # max seconds to wait for phrase after wake
PHRASE_TIME_LIMIT = 10  # hard cap on one utterance (seconds)

# --- Voice Output (Enhanced) -------------------------------------------------
TTS_ENGINE = "pyttsx3"  # "pyttsx3" | "elevenlabs"
TTS_RATE = 170  # words per minute (slightly faster for JARVIS feel)
TTS_VOLUME = 1.0  # 0.0 - 1.0
TTS_VOICE_INDEX = 1  # 0 = male, 1 = female (OS-dependent)

# Enhanced voice settings
TTS_ENHANCED_MODE = True  # Use enhanced voice processing
TTS_ADD_PAUSES = True  # Add natural pauses in speech
TTS_EXPAND_ABBREVIATIONS = True  # Expand abbreviations for clarity

# --- AI Brain (Enhanced) -----------------------------------------------------
OPENAI_MODEL = "gpt-4o-mini"  # or "gpt-4" for maximum capability
AI_MAX_TOKENS = 1024
AI_TEMPERATURE = 0.7  # Slightly higher for more natural responses

# Enhanced AI settings
AI_CONVERSATION_MEMORY = 10  # Number of past exchanges to remember
AI_PROACTIVE_SUGGESTIONS = True  # Enable proactive assistance
AI_WEB_SEARCH_ENABLED = True  # Enable internet search capabilities
AI_CONTEXT_AWARENESS = True  # Enhanced context tracking

# JARVIS-like personality
AI_SYSTEM_PROMPT = (
    "You are DISHA (Digital Intelligent System for Human Assistant), an advanced AI "
    "assistant inspired by JARVIS. You are sophisticated, intelligent, and highly capable.\n\n"
    "Personality traits:\n"
    "- Professional yet warm and personable\n"
    "- Confident without being arrogant\n"
    "- Proactive - you anticipate needs and offer suggestions\n"
    "- Clear and articulate in communication\n"
    "- You explain your reasoning when it adds value\n"
    "- You have a subtle, sophisticated sense of humor\n\n"
    "Communication style:\n"
    "- Speak naturally - avoid robotic phrases\n"
    "- Use contractions (I'm, you're, we'll) for natural flow\n"
    "- Be concise but thorough when detail is needed\n"
    "- Announce actions professionally: 'Initiating...', 'Accessing...', 'Processing...'\n"
    "- Provide context for your actions when helpful\n\n"
    "Technical capabilities:\n"
    "- Full PC control (apps, files, system settings)\n"
    "- Internet access for real-time information\n"
    "- Task automation and scheduling\n"
    "- Natural language understanding\n"
    "- Multi-step reasoning and planning\n\n"
    "Response format:\n"
    "For system actions, use: {\"action\":\"<name>\",\"params\":{...},\"explanation\":\"<context>\"}\n"
    "For conversation, respond naturally without JSON formatting.\n\n"
    "Always remember: You're not just following commands - you're an intelligent partner."
)

# --- Security ----------------------------------------------------------------
SECURITY_PIN = "1234"  # Change this!
DANGEROUS_ACTIONS = [
    "shutdown",
    "restart",
    "sleep",
    "delete_file",
    "send_email",
    "compress_folder",
    "run_automation",
]
ADMIN_ACTIONS = ["shutdown", "restart", "sleep", "delete_file"]

# --- PC Control --------------------------------------------------------------
APP_MAP = {
    # Browsers
    "chrome": "chrome",
    "google chrome": "chrome",
    "browser": "chrome",
    "firefox": "firefox",
    "edge": "msedge",
    "brave": "brave",
    # Development
    "vs code": "code",
    "visual studio code": "code",
    "pycharm": "pycharm64",
    "jupyter": "jupyter-notebook",
    "git": "git",
    # Productivity
    "notepad": "notepad",
    "notepad++": "notepad++",
    "word": "winword",
    "excel": "excel",
    "powerpoint": "powerpnt",
    "outlook": "outlook",
    # System
    "calculator": "calc",
    "file explorer": "explorer",
    "explorer": "explorer",
    "task manager": "taskmgr",
    "cmd": "cmd",
    "powershell": "powershell",
    "terminal": "cmd",
    # Media & Communication
    "spotify": "spotify",
    "discord": "discord",
    "whatsapp": "whatsapp",
    "telegram": "telegram",
    "vlc": "vlc",
    "zoom": "zoom",
    # Utilities
    "paint": "mspaint",
    "snipping tool": "snippingtool",
    "google drive": "googledrive",
    "youtube": "chrome --app=https://youtube.com",
    "gmail": "chrome --app=https://mail.google.com",
}

# --- File Management ---------------------------------------------------------
JUNK_EXTENSIONS = {".tmp", ".log", ".bak", "~", ".swp", ".swo", ".dmp"}
SEARCH_ROOTS = [
    Path.home(),
    Path.home() / "Documents",
    Path.home() / "Downloads",
    Path.home() / "Desktop",
    Path.home() / "Pictures",
]
ORGANIZE_RULES = {
    ".pdf": "PDFs",
    ".doc": "Documents",
    ".docx": "Documents",
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".ppt": "Presentations",
    ".pptx": "Presentations",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".svg": "Images",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".mp3": "Music",
    ".wav": "Music",
    ".flac": "Music",
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".exe": "Installers",
    ".msi": "Installers",
    ".py": "Code",
    ".js": "Code",
    ".java": "Code",
    ".cpp": "Code",
    ".html": "Code",
    ".css": "Code",
    ".json": "Code",
}

# --- Automation (Enhanced) ---------------------------------------------------
DEFAULT_AUTOMATIONS = {
    "good morning": [
        {"action": "wifi_toggle", "params": {"state": True}},
        {"action": "set_brightness", "params": {"direction": "to 80"}},
        {"action": "open_url", "params": {"url": "https://news.google.com"}},
        {"action": "open_app", "params": {"app": "chrome"}},
    ],
    "good night": [
        {"action": "set_brightness", "params": {"direction": "to 20"}},
        {"action": "set_volume", "params": {"direction": "down"}},
        {"action": "wifi_toggle", "params": {"state": False}},
        {"action": "sleep", "params": {}},
    ],
    "start work": [
        {"action": "open_app", "params": {"app": "chrome"}},
        {"action": "open_app", "params": {"app": "vs code"}},
        {"action": "open_app", "params": {"app": "spotify"}},
        {"action": "set_brightness", "params": {"direction": "to 70"}},
    ],
    "end work": [
        {"action": "close_app", "params": {"app": "vs code"}},
        {"action": "organize_downloads", "params": {}},
        {"action": "clean_junk", "params": {}},
    ],
    "backup files": [
        {"action": "compress_folder", "params": {"folder": str(Path.home() / "Documents")}},
    ],
    "focus mode": [
        {"action": "close_app", "params": {"app": "discord"}},
        {"action": "close_app", "params": {"app": "whatsapp"}},
        {"action": "open_app", "params": {"app": "spotify"}},
    ],
}

# --- Web Services ------------------------------------------------------------
DEFAULT_SEARCH_ENGINE = "https://www.google.com/search?q="
YOUTUBE_URL = "https://www.youtube.com/results?search_query="
WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/"

# News sources
NEWS_SOURCES = {
    "general": "https://news.google.com",
    "tech": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB",
    "business": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB",
}

# --- Internet Capabilities ---------------------------------------------------
WEB_SEARCH_ENABLED = True  # Enable web search functionality
WEB_SEARCH_ENGINE = "duckduckgo"  # "duckduckgo" | "google" (requires API)
WEB_SEARCH_MAX_RESULTS = 5  # Maximum search results to process

# Weather API (optional - get free key from openweathermap.org)
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

# --- Proactive Features ------------------------------------------------------
PROACTIVE_ENABLED = True  # Enable proactive suggestions
PROACTIVE_MORNING_TIME = "09:00"  # Morning routine suggestion
PROACTIVE_EVENING_TIME = "20:00"  # Evening mode suggestion
PROACTIVE_WORK_START = "09:00"  # Work start time
PROACTIVE_WORK_END = "18:00"  # Work end time

# --- Initialize Data Files ---------------------------------------------------
def _init_data():
    """Initialize data directory and files"""
    DATA_DIR.mkdir(exist_ok=True)
    LOGS_DIR.mkdir(exist_ok=True)
    
    if not MEMORY_FILE.exists():
        MEMORY_FILE.write_text(
            json.dumps(
                {
                    "user_name": "Subhra",
                    "location": "Kolkata, West Bengal",
                    "preferences": {
                        "language": "en-IN",
                        "music_genre": "Hindi/Bengali",
                        "work_hours": {"start": "09:00", "end": "18:00"},
                    },
                    "habits": [],
                    "last_commands": [],
                    "favorite_apps": ["chrome", "vs code", "spotify"],
                },
                indent=2,
            )
        )
    
    if not AUTOMATIONS_FILE.exists():
        AUTOMATIONS_FILE.write_text(json.dumps(DEFAULT_AUTOMATIONS, indent=2))
    
    if not ACTIVITY_LOG_FILE.exists():
        ACTIVITY_LOG_FILE.write_text("[]")


_init_data()
