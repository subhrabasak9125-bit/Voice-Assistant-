# DISHA Enhanced - Quick Setup Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Install Python
1. Download Python 3.8+ from https://www.python.org/downloads/
2. **IMPORTANT**: Check "Add Python to PATH" during installation
3. Verify: Open Command Prompt and type `python --version`

### Step 2: Install Dependencies
Open Command Prompt in the DISHA folder and run:
```bash
pip install -r requirements_enhanced.txt
```

This will install:
- Speech recognition
- Text-to-speech
- OpenAI integration
- System control libraries
- And more...

### Step 3: Configure (Optional but Recommended)

#### For Full Intelligence (Recommended)
Create a file named `.env` in the DISHA folder:
```
OPENAI_API_KEY=sk-your-key-here
```

Get your free API key:
1. Go to https://platform.openai.com/api-keys
2. Sign up / Log in
3. Create a new secret key
4. Copy and paste into `.env`

**Cost**: ~$0.002 per conversation (very cheap!)

#### For Premium Voice (Optional)
Add to `.env`:
```
ELEVENLABS_API_KEY=your-elevenlabs-key
```

Get from: https://elevenlabs.io

### Step 4: Run DISHA

#### Windows (Easy Way)
Double-click: `run_enhanced.bat`

#### Any OS (Command Line)
```bash
python main_enhanced.py
```

### Step 5: Start Using

1. Wait for "DISHA systems are now online"
2. Say: **"Hey DISHA"**
3. Give a command: **"Open Chrome"**
4. Or ask a question: **"What can you do?"**

---

## 🎤 Your First Commands

Try these to get started:

### Test Voice Recognition
```
"Hey DISHA, what time is it?"
"Hey DISHA, tell me a joke"
"Hey DISHA, who are you?"
```

### Test System Control
```
"Hey DISHA, open calculator"
"Hey DISHA, volume up"
"Hey DISHA, take a screenshot"
```

### Test Intelligence (Needs API Key)
```
"Hey DISHA, search for best Python tutorials"
"Hey DISHA, what's happening in tech news?"
"Hey DISHA, explain quantum computing"
```

---

## 🔧 Common Issues & Fixes

### ❌ "Module not found" error
**Fix**: Run `pip install -r requirements_enhanced.txt` again

### ❌ No voice output
**Fix 1**: Check speakers are working
**Fix 2**: Run as Administrator
**Fix 3**: Edit `config_enhanced.py`, change `TTS_VOICE_INDEX = 0`

### ❌ Not hearing wake word
**Fix 1**: Speak clearly: "Hey DISHA" (pause) "command"
**Fix 2**: Check microphone in Windows Settings
**Fix 3**: Edit `config_enhanced.py`, increase `AMBIENT_TIMEOUT = 3`

### ❌ AI not working
**Fix 1**: Check `.env` file has your OpenAI API key
**Fix 2**: Check internet connection
**Fix 3**: Don't worry - DISHA works offline too (just less smart)

---

## 📚 Learn More

- **Full Documentation**: `README_ENHANCED.md`
- **Configuration**: `config_enhanced.py`
- **Add Commands**: Edit `core/ai_brain_enhanced.py`
- **Customize Voice**: Edit `core/voice_output_enhanced.py`

---

## 🎯 Pro Tips

1. **Better Recognition**: Use a good quality microphone
2. **Faster Response**: Use GPT-4 API key (costs more but worth it)
3. **Natural Voice**: Get ElevenLabs key for human-like speech
4. **Customize**: Edit `data/memory.json` to teach DISHA about you
5. **Automate**: Create custom routines in `data/automations.json`

---

## 🆘 Need Help?

1. Check this guide
2. Read `README_ENHANCED.md`
3. Review error messages
4. Check all files are in correct folder
5. Ensure Python is in PATH

---

## ✨ Make DISHA Yours

### Change Name
Edit `config_enhanced.py`:
```python
# In memory.json
"user_name": "Your Name Here"
```

### Add Apps
Edit `config_enhanced.py`, add to `APP_MAP`:
```python
APP_MAP = {
    "your app": "executable_name",
}
```

### Custom Wake Word
Edit `config_enhanced.py`:
```python
WAKE_WORDS = ["hey disha", "hey jarvis", "computer"]
```

---

## 🎉 You're Ready!

DISHA Enhanced is now set up and ready to be your AI assistant.

**Remember**:
- Speak clearly after wake word
- Online mode needs API key (but works offline too)
- Customize everything in config files
- Have fun! 🚀

---

**Quick Command**: Just run `python main_enhanced.py` and start talking!
