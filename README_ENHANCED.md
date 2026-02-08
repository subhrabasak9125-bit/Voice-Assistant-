# DISHA Enhanced - Digital Intelligent System for Human Assistant

<div align="center">

![DISHA Logo](https://img.shields.io/badge/DISHA-Enhanced-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![AI](https://img.shields.io/badge/AI-Powered-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**Your Personal JARVIS-Like AI Assistant**

</div>

---

## 🌟 Overview

DISHA Enhanced is an advanced AI assistant inspired by JARVIS, featuring:

- 🧠 **Intelligent AI** - Powered by GPT-4 for natural conversations
- 🌐 **Internet Capabilities** - Real-time web search and information retrieval
- 🎯 **Hybrid Mode** - Works offline with basic features, enhanced online
- 🗣️ **Natural Voice** - JARVIS-like speech with female voice
- ⚡ **Proactive Assistance** - Anticipates your needs and offers suggestions
- 🔧 **Full PC Control** - Manage apps, files, and system settings
- 🤖 **Automation** - Schedule tasks and create custom workflows

---

## 📋 Features

### Core Capabilities

#### 🎤 Voice Interaction
- Wake word detection ("Hey DISHA")
- Natural language understanding
- Continuous listening mode
- Multiple language support (English, Hindi, Bengali)

#### 🧠 Advanced AI
- **Online Mode**: Full GPT-4 intelligence with internet access
- **Offline Mode**: Smart fallback with pattern-based recognition
- Contextual awareness and memory
- Proactive suggestions based on time and usage patterns

#### 💻 System Control
- Open/close applications
- Adjust volume and brightness
- Control WiFi and Bluetooth
- Shutdown, restart, sleep modes
- Take screenshots
- File management (find, create, delete, organize)

#### 🌐 Web Services
- Google search
- YouTube playback
- Wikipedia lookups
- Open custom URLs
- Real-time news
- Weather information (with API key)
- Download files

#### 🤖 Automation
- Pre-configured routines (morning, evening, work mode)
- Custom automation sequences
- Task scheduling
- Multi-step operations

#### 🏠 Smart Home (Extensible)
- Light control
- Fan control
- AC control
- Easily add more devices

---

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+** installed
2. **Microphone** for voice input
3. **Internet connection** (for enhanced features)
4. **Windows OS** (currently optimized for Windows)

### Installation

1. **Clone or Extract** the DISHA folder

2. **Install Dependencies**
   ```bash
   pip install -r requirements_enhanced.txt
   ```

3. **Configure Environment** (Optional but recommended)
   
   Create a `.env` file in the DISHA folder:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ELEVENLABS_API_KEY=your_elevenlabs_key_here
   WEATHER_API_KEY=your_openweather_key_here
   ```

   > **Getting API Keys:**
   > - OpenAI: https://platform.openai.com/api-keys
   > - ElevenLabs: https://elevenlabs.io (for premium voice)
   > - Weather: https://openweathermap.org/api (free tier available)

4. **Run DISHA Enhanced**
   ```bash
   python main_enhanced.py
   ```
   
   Or use the batch file (Windows):
   ```bash
   run_enhanced.bat
   ```

---

## 🎯 Usage Guide

### Voice Commands

#### Basic Interactions
```
"Hey DISHA"                    # Wake up DISHA
"Hi" / "Hello"                 # Greet DISHA
"What can you do?"             # List capabilities
"Help"                         # Get help
```

#### System Control
```
"Open Chrome"                  # Open applications
"Close Notepad"                # Close applications
"Volume up"                    # Increase volume
"Brightness down"              # Decrease brightness
"Take a screenshot"            # Capture screen
```

#### Web & Information
```
"Search for Python tutorials"  # Google search
"Play lofi music on YouTube"   # YouTube playback
"What's the weather?"          # Weather info (needs API key)
"Tell me about quantum computing"  # Information query
"Open news"                    # Latest news
```

#### File Management
```
"Find my resume"               # Locate files
"Create folder Projects"       # Create folder
"Organize downloads"           # Auto-organize downloads folder
"Clean junk files"             # Remove temporary files
```

#### Automation
```
"Good morning"                 # Morning routine
"Start work"                   # Work mode setup
"Good night"                   # Evening routine
"Focus mode"                   # Minimize distractions
```

#### Advanced
```
"Undo"                         # Reverse last action
"Stop everything"              # Emergency stop
"Quit"                         # Exit DISHA
```

---

## 🎨 JARVIS-Like Features

### Proactive Assistance
DISHA doesn't just respond - she anticipates:
- Morning routine suggestions at 9 AM
- Evening mode at 8 PM
- Work mode reminders
- Context-aware recommendations

### Natural Conversation
DISHA speaks like JARVIS:
```
❌ "Sure! I will open Chrome for you right now!"
✅ "Initiating Chrome. Your browser is ready."

❌ "OK! Searching Google now!"
✅ "Searching for quantum computing. Here's what I found..."
```

### Intelligent Actions
DISHA explains reasoning when helpful:
```
User: "I need to focus"
DISHA: "Activating focus mode. I'm closing Discord and WhatsApp 
        to minimize distractions, and starting Spotify for 
        background music."
```

---

## ⚙️ Configuration

### Voice Settings

Edit `config_enhanced.py`:

```python
# Speech rate (words per minute)
TTS_RATE = 170  # 150-200 recommended

# Voice selection (0=male, 1=female)
TTS_VOICE_INDEX = 1

# Enhanced features
TTS_ENHANCED_MODE = True
TTS_ADD_PAUSES = True
```

### AI Settings

```python
# AI Model
OPENAI_MODEL = "gpt-4o-mini"  # or "gpt-4" for maximum capability

# Temperature (0.0 = precise, 1.0 = creative)
AI_TEMPERATURE = 0.7

# Enable features
AI_WEB_SEARCH_ENABLED = True
AI_PROACTIVE_SUGGESTIONS = True
```

### Custom Applications

Add your favorite apps to `APP_MAP`:

```python
APP_MAP = {
    "pycharm": "pycharm64",
    "slack": "slack",
    "photoshop": "photoshop",
    # Add more...
}
```

### Custom Automations

Edit `data/automations.json`:

```json
{
  "study mode": [
    {"action": "open_app", "params": {"app": "notion"}},
    {"action": "open_app", "params": {"app": "spotify"}},
    {"action": "set_brightness", "params": {"direction": "to 60"}}
  ]
}
```

---

## 🌐 Online vs Offline Mode

### Online Mode (Recommended)
**Requires**: OpenAI API key

**Features**:
- Natural language understanding
- Web search and information retrieval
- Context-aware responses
- Proactive suggestions
- Complex multi-step reasoning

**Setup**: Add OpenAI API key to `.env`

### Offline Mode (Fallback)
**Requires**: Nothing (works out of the box)

**Features**:
- Basic command recognition
- Pattern-based understanding
- Core system control
- File operations
- Pre-defined automations

**Limitations**:
- No web search
- Limited conversation ability
- No proactive features

---

## 📁 Project Structure

```
DISHA/
├── core/
│   ├── ai_brain_enhanced.py      # Enhanced AI with internet
│   ├── voice_input.py             # Speech recognition
│   ├── voice_output_enhanced.py   # JARVIS-like TTS
│   ├── context_manager.py         # Context tracking
│   └── security.py                # Permission system
├── modules/
│   ├── pc_control.py              # System control
│   ├── file_manager.py            # File operations
│   ├── web_services.py            # Web interactions
│   ├── automation.py              # Task automation
│   ├── writing_assistant.py       # Notes & reminders
│   ├── screen_reader.py           # Screen capture
│   └── smart_home.py              # IoT control
├── utils/
│   ├── helpers.py                 # Utility functions
│   └── logger.py                  # Activity logging
├── data/
│   ├── memory.json                # User preferences
│   ├── automations.json           # Custom routines
│   └── activity_log.json          # Action history
├── main_enhanced.py               # Enhanced entry point
├── config_enhanced.py             # Enhanced settings
├── requirements_enhanced.txt      # Dependencies
└── README_ENHANCED.md            # This file
```

---

## 🔧 Troubleshooting

### Voice Recognition Issues

**Problem**: DISHA doesn't hear commands
**Solutions**:
1. Check microphone is working
2. Adjust `AMBIENT_TIMEOUT` in config
3. Speak clearly after "Hey DISHA"
4. Check microphone permissions

### Voice Output Issues

**Problem**: No speech output
**Solutions**:
1. Check system audio is working
2. Try different voice index: `TTS_VOICE_INDEX = 0` or `1`
3. Reinstall pyttsx3: `pip install --force-reinstall pyttsx3`

### API Connection Issues

**Problem**: Online mode not working
**Solutions**:
1. Verify API key in `.env` file
2. Check internet connection
3. Ensure OpenAI account has credits
4. DISHA will auto-fallback to offline mode

### Application Control Issues

**Problem**: Can't open/close apps
**Solutions**:
1. Check app name in `APP_MAP` (config_enhanced.py)
2. Ensure application is installed
3. Try full executable name

---

## 🎓 Advanced Usage

### Creating Custom Commands

Edit `core/ai_brain_enhanced.py` to add custom patterns:

```python
# Add to _enhanced_offline_fallback method
if "custom command" in t:
    return {
        "type": "action",
        "action": "your_action",
        "params": {"key": "value"},
        "explanation": "Executing custom command"
    }
```

### Adding New Actions

1. Create function in appropriate module
2. Add action handler in `main_enhanced.py` dispatch function
3. Document in help text

### Integrating Smart Home Devices

Edit `modules/smart_home.py`:

```python
def control_custom_device(action: str) -> tuple[bool, str]:
    # Your device control code
    return True, f"Device {action}"
```

---

## 🔒 Security & Privacy

- **Offline Mode**: No data sent externally
- **Online Mode**: Only sends necessary data to OpenAI
- **Local Storage**: All data stored locally in `data/` folder
- **No Telemetry**: DISHA doesn't collect or send usage data
- **API Keys**: Stored locally in `.env` (never committed to git)

### Security PIN

For sensitive operations, DISHA requires a PIN:

```python
# In config_enhanced.py
SECURITY_PIN = "1234"  # CHANGE THIS!
```

---

## 🛠️ Development

### Running in Development Mode

```bash
# With verbose logging
python main_enhanced.py --verbose

# Testing specific features
python -m pytest tests/  # If tests are added
```

### Code Style

The project follows Python best practices:
- Type hints where beneficial
- Clear function documentation
- Modular architecture
- Separation of concerns

---

## 📝 Changelog

### Version 2.0 - Enhanced (Current)
- ✨ JARVIS-like AI and voice
- 🌐 Internet search capabilities
- 🧠 GPT-4 integration
- 🎯 Proactive assistance
- ⚡ Enhanced performance
- 📊 Better logging and debugging

### Version 1.0 - Original
- Basic voice assistant
- Offline pattern matching
- Simple system control
- File management

---

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- [ ] Mac/Linux support
- [ ] Mobile app integration
- [ ] More smart home integrations
- [ ] Voice command customization UI
- [ ] Cloud sync for settings
- [ ] Multi-user support

---

## 📄 License

This project is for educational and personal use.

---

## 🙏 Acknowledgments

- Inspired by JARVIS from Iron Man
- Built with Python and love
- Powered by OpenAI's GPT models
- Community feedback and testing

---

## 📧 Support

For issues, questions, or suggestions:
1. Check troubleshooting section
2. Review configuration guide
3. Ensure all dependencies installed
4. Check API keys are valid

---

## 🚀 Future Roadmap

- [ ] Mobile companion app
- [ ] Web dashboard
- [ ] Skill marketplace
- [ ] Multi-language support expansion
- [ ] Video call integration
- [ ] Calendar and email management
- [ ] Advanced home automation
- [ ] Learning from user behavior

---

<div align="center">

**Made with ❤️ for Subhra**

*"Sometimes you gotta run before you can walk." - Tony Stark*

</div>
