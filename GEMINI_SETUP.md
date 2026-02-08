# 🚀 Using Google Gemini with DISHA (FREE!)

## ✨ Why Gemini?

**Google Gemini is RECOMMENDED because:**
- ✅ **100% FREE** with generous limits
- ✅ Very powerful (compares to GPT-4)
- ✅ Fast responses
- ✅ No credit card required
- ✅ 60 requests per minute (free tier)
- ✅ Great for natural conversations

---

## 📝 Step-by-Step Setup (5 Minutes)

### Step 1: Get Your FREE Gemini API Key

1. **Go to:** https://makersuite.google.com/app/apikey
   - Or: https://aistudio.google.com/app/apikey

2. **Sign in** with your Google account (Gmail)

3. **Click:** "Create API Key"

4. **Select:** "Create API key in new project" (or use existing)

5. **Copy** the API key
   - It looks like: `AIzaSy...` (about 39 characters)
   - Store it safely!

### Step 2: Add to DISHA

In your `DISHA_Enhanced` folder, create/edit the `.env` file:

**Windows - Using Notepad:**
```bash
notepad .env
```

**Add this line:**
```
GEMINI_API_KEY=AIzaSy-your-actual-key-here
```

**Save** the file (Ctrl+S)

### Step 3: Install Gemini Library

```bash
pip install google-generativeai
```

Or install all dependencies:
```bash
pip install -r requirements_enhanced.txt
```

### Step 4: Run DISHA

```bash
python main_enhanced.py
```

You should see:
```
[AI] Multi-AI Brain: Online mode activated with Google Gemini ✨
[AI] Provider: Gemini 1.5 Flash (FREE tier available)
```

---

## 🎯 Complete `.env` Example

```env
# Google Gemini API Key (FREE - Recommended!)
GEMINI_API_KEY=AIzaSyYour-Actual-Key-Here

# Optional: OpenAI (if you want to use GPT instead)
# OPENAI_API_KEY=sk-proj-your-key-here

# Optional: Premium Voice
# ELEVENLABS_API_KEY=your-elevenlabs-key

# AI Provider Selection (auto tries Gemini first, then OpenAI)
AI_PROVIDER=auto
```

---

## 🆚 Gemini vs OpenAI Comparison

| Feature | Google Gemini | OpenAI GPT |
|---------|---------------|------------|
| **Cost** | 🟢 FREE | 🟡 Paid ($5 free trial) |
| **Speed** | 🟢 Very Fast | 🟢 Fast |
| **Quality** | 🟢 Excellent | 🟢 Excellent |
| **Limit (Free)** | 60 requests/min | 3 requests/min |
| **Credit Card** | ❌ Not needed | ⚠️ After trial |
| **Best For** | Most users | Advanced use cases |

**Recommendation:** Start with Gemini (FREE), switch to OpenAI only if needed.

---

## 🔧 Advanced Configuration

### Choose Specific Provider

Edit `config_enhanced.py`:

```python
# Force Gemini only
AI_PROVIDER = "gemini"

# Force OpenAI only
AI_PROVIDER = "openai"

# Auto (tries Gemini first, then OpenAI)
AI_PROVIDER = "auto"
```

### Or use `.env`:

```env
AI_PROVIDER=gemini
```

---

## 🎤 Test Gemini

Once running, try:

```
"Hey DISHA, tell me about artificial intelligence"
"Hey DISHA, what's quantum computing?"
"Hey DISHA, search for latest tech news"
"Hey DISHA, explain how neural networks work"
```

Gemini will provide intelligent, detailed responses!

---

## 💡 Usage Limits (Free Tier)

**Gemini 1.5 Flash (FREE):**
- 15 requests per minute
- 1,500 requests per day
- 1 million requests per month

**More than enough for:**
- ✅ Daily personal assistant use
- ✅ Hundreds of conversations per day
- ✅ Extended development/testing

---

## 🔄 Using Both Gemini AND OpenAI

You can have both configured! DISHA will:

1. Try Gemini first (it's free!)
2. Fall back to OpenAI if Gemini fails
3. Fall back to offline mode if both fail

**Setup:**
```env
GEMINI_API_KEY=your-gemini-key
OPENAI_API_KEY=your-openai-key
AI_PROVIDER=auto
```

---

## ⚙️ Gemini Models Available

DISHA uses **Gemini 1.5 Flash** by default (best balance):

| Model | Speed | Quality | Best For |
|-------|-------|---------|----------|
| Gemini 1.5 Flash | ⚡ Fastest | 🟢 Great | DISHA (default) |
| Gemini 1.5 Pro | 🐢 Slower | 🟢🟢 Better | Complex tasks |
| Gemini 1.0 Pro | ⚡ Fast | 🟢 Good | Legacy |

**To change model**, edit `core/ai_brain_multi.py` line 75:
```python
self._client = genai.GenerativeModel('gemini-1.5-pro')  # For Pro model
```

---

## 🆘 Troubleshooting

### "Module not found: google.generativeai"
**Fix:**
```bash
pip install google-generativeai
```

### "API key not valid"
**Fixes:**
1. Check key is correct (starts with `AIzaSy`)
2. Ensure no spaces in `.env` file
3. Regenerate key at Google AI Studio
4. Make sure key is enabled

### "Quota exceeded"
**Fix:**
- Wait a minute (rate limit)
- Free tier: 15 requests/minute
- Unlikely to hit daily limit for normal use

### "Gemini not working"
**Fix:**
1. Check internet connection
2. Verify API key in `.env`
3. DISHA will auto-fallback to offline mode

---

## 🎁 Benefits of Gemini for DISHA

1. **Cost Effective**
   - Completely free for personal use
   - No billing required

2. **Great Performance**
   - Fast responses
   - High quality answers
   - Natural conversations

3. **Generous Limits**
   - More than enough for daily use
   - Rarely hit limits

4. **Easy Setup**
   - No credit card
   - Quick registration
   - Simple API key

5. **Reliable**
   - Google infrastructure
   - High uptime
   - Good support

---

## 🚀 Quick Commands After Setup

```bash
# Install dependencies
pip install -r requirements_enhanced.txt

# Verify Gemini is installed
python -c "import google.generativeai; print('Gemini ready!')"

# Run DISHA
python main_enhanced.py
```

---

## 📊 What Gemini Enables in DISHA

With Gemini, DISHA can:

✅ Understand natural language perfectly
✅ Answer complex questions intelligently
✅ Search and summarize web information
✅ Maintain context across conversations
✅ Provide proactive suggestions
✅ Explain reasoning and provide details
✅ Handle ambiguous commands
✅ Learn from conversation flow

**All for FREE!** 🎉

---

## 🌟 Recommended Setup

**Best Configuration:**
```env
# .env file
GEMINI_API_KEY=your-gemini-key-here
AI_PROVIDER=gemini
```

**Why:**
- ✅ FREE forever
- ✅ Best quality/cost ratio
- ✅ Fast and reliable
- ✅ No billing surprises

---

## 📚 Additional Resources

- **Get API Key:** https://aistudio.google.com/app/apikey
- **Gemini Docs:** https://ai.google.dev/docs
- **Rate Limits:** https://ai.google.dev/pricing
- **Examples:** https://ai.google.dev/examples

---

## 💬 Support

**Having issues?**

1. Check API key is correct
2. Verify internet connection
3. Ensure `google-generativeai` is installed
4. Check `.env` file format
5. Try regenerating API key

**Still stuck?**
- Review error messages
- Check DISHA falls back to offline mode
- Verify Python version (3.8+)

---

## 🎉 You're Ready!

With Gemini configured, DISHA now has:
- 🧠 Advanced intelligence
- 🌐 Internet knowledge
- 💬 Natural conversations
- 🎯 JARVIS-like capabilities

**All completely FREE!**

Enjoy your powerful AI assistant! 🚀

---

*Last updated: February 2026*
*Gemini API is free at time of writing - check Google AI for current pricing*
