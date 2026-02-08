# ============================================================
# DISHA  -  Digital Intelligent System for Human Assistant
# main_enhanced.py - Enhanced version with JARVIS-like capabilities
#
# Features:
# - Advanced AI with internet capabilities
# - Natural, proactive conversation
# - Hybrid online/offline mode
# - Enhanced voice output
# - Sophisticated command processing
# ============================================================

import sys
import os
import io

# Force UTF-8 stdout on Windows
if sys.platform == "win32":
    os.environ["PYTHONIOENCODING"] = "utf-8"
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(
            sys.stdout.buffer, encoding="utf-8", errors="replace"
        )
    if hasattr(sys.stderr, "buffer"):
        sys.stderr = io.TextIOWrapper(
            sys.stderr.buffer, encoding="utf-8", errors="replace"
        )

import time
import threading
from pathlib import Path
from datetime import datetime

# Lock CWD and sys.path
_THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS_DIR))
os.chdir(_THIS_DIR)

from config import MEMORY_FILE, OPENAI_API_KEY
from utils.helpers import (
    print_banner,
    time_greeting,
    set_speak_fn,
    load_memory,
)
from utils.logger import log_action, pop_last_action

# Core modules - Enhanced versions
from core.voice_input import VoiceInput
from core.voice_output_enhanced import EnhancedVoiceOutput
from core.context_manager import ContextManager
from core.ai_brain_multi import MultiAIBrain  # Multi-provider AI support
from core.security import (
    request_permission,
    emergency_stop,
    is_stopped,
    reset_emergency,
)

# Feature modules
from modules import (
    pc_control,
    file_manager,
    web_services,
)
from modules import automation as automation_mod
from modules import writing_assistant, screen_reader, smart_home


# ===========================================================================
# GLOBAL INSTANCES
# ===========================================================================
voice_in: VoiceInput = None  # type: ignore
voice_out: EnhancedVoiceOutput = None  # type: ignore
context: ContextManager = None  # type: ignore
brain: MultiAIBrain = None  # type: ignore


def speak(text: str, priority: bool = False):
    """Central speak function with priority support"""
    if voice_out:
        voice_out.speak(text, priority=priority)
    else:
        print(f"  [DISHA] {text}")


# ===========================================================================
# ACTION DISPATCHER
# ===========================================================================
def dispatch(action: str, params: dict, explanation: str = "") -> tuple[bool, str]:
    """
    Route an action to the appropriate module.
    
    Args:
        action: Action name
        params: Action parameters
        explanation: Optional explanation to speak before action
    
    Returns:
        (success, message) tuple
    """
    # Announce action if explanation provided
    if explanation:
        speak(explanation)
    
    # Emergency / control
    if action == "emergency_stop":
        emergency_stop()
        return True, "Emergency stop activated. All operations halted."
    
    if action == "quit":
        speak("DISHA systems shutting down. Goodbye, Subhra.")
        log_action("quit", status="success", detail="User requested exit.")
        time.sleep(1)
        sys.exit(0)
    
    if action == "undo":
        return handle_undo()
    
    # Security gate
    if not request_permission(action, params):
        return False, "Action cancelled."
    
    # PC Control
    if action == "open_app":
        app = params.get("app", "")
        ok, msg = pc_control.open_app(app)
        if ok:
            context.set_last_app(app)
        return ok, msg
    
    if action == "close_app":
        app = params.get("app", "")
        return pc_control.close_app(app)
    
    if action == "set_volume":
        return pc_control.set_volume(params.get("direction", "up"))
    
    if action == "set_brightness":
        return pc_control.set_brightness(params.get("direction", "up"))
    
    if action == "wifi_toggle":
        return pc_control.wifi_toggle(params.get("state", True))
    
    if action == "bluetooth_toggle":
        return pc_control.bluetooth_toggle(params.get("state", True))
    
    if action == "shutdown":
        return pc_control.shutdown()
    
    if action == "restart":
        return pc_control.restart()
    
    if action == "sleep":
        return pc_control.sleep()
    
    # File Management
    if action == "find_file":
        return file_manager.find_file(params.get("name", ""))
    
    if action == "create_folder":
        return file_manager.create_folder(params.get("name", ""))
    
    if action == "delete_file":
        return file_manager.delete_file(params.get("path", ""))
    
    if action == "compress_folder":
        return file_manager.compress_folder(params.get("folder", ""))
    
    if action == "organize_downloads":
        return file_manager.organize_downloads()
    
    if action == "clean_junk":
        return file_manager.clean_junk()
    
    # Web Services
    if action == "search_google":
        query = params.get("query", "")
        context.set_last_query(query)
        return web_services.search_google(query)
    
    if action == "play_youtube":
        query = params.get("query", "")
        context.set_last_query(query)
        return web_services.play_youtube(query)
    
    if action == "search_wikipedia":
        query = params.get("query", "")
        return web_services.search_wikipedia(query)
    
    if action == "open_url":
        url = params.get("url", "")
        context.set_last_url(url)
        return web_services.open_url(url)
    
    if action == "open_news":
        return web_services.open_news()
    
    if action == "download_file":
        return web_services.download_file(
            params.get("url", ""), params.get("filename")
        )
    
    if action == "open_spotify":
        return web_services.open_spotify()
    
    if action == "open_whatsapp":
        return web_services.open_whatsapp()
    
    if action == "open_gmail":
        return web_services.open_gmail()
    
    # Automation
    if action == "run_automation":
        name = params.get("name", "")
        return automation_mod.run_automation(name, dispatch)
    
    if action == "schedule_automation":
        return automation_mod.schedule_automation(
            params.get("time", "09:00"), params.get("name", ""), dispatch
        )
    
    if action == "multi_step":
        return automation_mod.execute_multi_step(params.get("steps", []), dispatch)
    
    # Writing & Notes
    if action == "write_note":
        note_type = params.get("type", "note")
        text = params.get("text", "")
        if note_type == "reminder":
            return writing_assistant.save_reminder(text, params.get("time"))
        return writing_assistant.write_note(text, params.get("title"))
    
    if action == "get_reminders":
        _, msg = writing_assistant.get_reminders()
        return True, msg
    
    if action == "summarize":
        return writing_assistant.summarize_file(params.get("file", ""))
    
    # Screen
    if action == "take_screenshot":
        return screen_reader.take_screenshot()
    
    if action == "read_screen":
        return screen_reader.read_screen()
    
    if action == "find_element":
        return screen_reader.find_element(params.get("description", ""))
    
    # Smart Home
    if action == "smart_home_light":
        return smart_home.control_light(
            params.get("action", "on"), params.get("room", "living room")
        )
    
    if action == "smart_home_fan":
        return smart_home.control_fan(
            params.get("action", "on"), params.get("room", "bedroom")
        )
    
    if action == "smart_home_ac":
        return smart_home.control_ac(params.get("action", "on"), params.get("temp"))
    
    # Fallback
    log_action(action, params, status="failed", detail="Unknown action.")
    return False, f"I don't have the capability to perform '{action}' yet."


# ===========================================================================
# UNDO HANDLER
# ===========================================================================
def handle_undo() -> tuple[bool, str]:
    """Undo the last action"""
    last = pop_last_action()
    if last is None:
        return False, "There's nothing to undo at the moment."
    
    action = last.get("action", "")
    params = last.get("params", {})
    
    # Reversible pairs
    reverse_map = {
        "open_app": ("close_app", params),
        "close_app": ("open_app", params),
        "wifi_toggle": (
            "wifi_toggle",
            {"state": not params.get("state", True)},
        ),
        "bluetooth_toggle": (
            "bluetooth_toggle",
            {"state": not params.get("state", True)},
        ),
    }
    
    if action in reverse_map:
        rev_action, rev_params = reverse_map[action]
        print(f"  [UND] Reversing {action} -> {rev_action}")
        log_action(
            "undo", {"original": action}, status="pending", detail=f"Reversing {action}"
        )
        ok, msg = dispatch(rev_action, rev_params, explanation=f"Undoing {action}")
        return ok, f"Done. I've reversed the last action."
    
    # Non-reversible
    log_action(
        "undo",
        {"original": action},
        status="success",
        detail="Noted but not reversible",
    )
    return (
        True,
        f"The last action was '{action}'. "
        "This can't be automatically reversed, but I've noted it.",
    )


# ===========================================================================
# PROACTIVE SUGGESTIONS
# ===========================================================================
def check_proactive_suggestions():
    """Check if DISHA should offer proactive suggestions"""
    hour = datetime.now().hour
    
    # Morning suggestions
    if hour == 9 and datetime.now().minute == 0:
        speak("Good morning, Subhra. Would you like me to run your morning routine?")
    
    # Evening suggestions
    elif hour == 20 and datetime.now().minute == 0:
        speak("It's getting late. Should I dim the screen and prepare for evening mode?")


# ===========================================================================
# MAIN LOOP
# ===========================================================================
def main():
    global voice_in, voice_out, context, brain
    
    # Print banner
    print_banner()
    
    # Initialize subsystems
    print("  \033[96mInitializing DISHA Enhanced Systems...\033[0m\n")
    
    # Voice output first
    voice_out = EnhancedVoiceOutput()
    set_speak_fn(speak)
    
    # Context manager
    context = ContextManager()
    
    # Multi-AI brain (supports Gemini, OpenAI, or offline)
    brain = MultiAIBrain(context, ai_provider="auto")
    
    # Voice input
    voice_in = VoiceInput()
    
    # Load memory
    mem = load_memory(MEMORY_FILE)
    name = mem.get("user_name", "Subhra")
    
    # Startup greeting - JARVIS style
    ai_provider = brain.get_provider()
    if ai_provider == "gemini":
        mode_status = "Online mode with Google Gemini"
    elif ai_provider == "openai":
        mode_status = "Online mode with OpenAI GPT"
    else:
        mode_status = "Offline mode"
    
    greeting = (
        f"{time_greeting()}, {name}. DISHA systems are now online. "
        f"{mode_status}. I'm ready to assist you. "
        f"Say 'Hey DISHA' to wake me, or type your command."
    )
    
    voice_out.announce_system_event("startup", greeting)
    
    # Start voice listener
    voice_in.start()
    
    # Main event loop
    print("\n  " + "-" * 70)
    print("  Enhanced DISHA is active. Listening for your commands.\n")
    
    last_suggestion_check = time.time()
    
    while True:
        try:
            # Check for emergency stop
            if is_stopped():
                print("\n  [!!!] Emergency stop is active. Type 'reset' to resume.")
                typed = input("  > ").strip()
                if typed.lower() == "reset":
                    reset_emergency()
                    speak("Emergency protocols disengaged. I'm operational again.")
                    voice_in.start()
                continue
            
            # Periodic proactive suggestions (every 5 minutes)
            if time.time() - last_suggestion_check > 300:
                check_proactive_suggestions()
                last_suggestion_check = time.time()
            
            # Get input from voice or keyboard
            user_text = None
            
            # Check voice queue
            if voice_in.has_command():
                user_text = voice_in.get_command(timeout=0.1)
            else:
                # Keyboard input with timeout
                typed_holder = [None]
                
                def read_line():
                    try:
                        typed_holder[0] = input("  > ")
                    except (EOFError, KeyboardInterrupt):
                        typed_holder[0] = "quit"
                
                t = threading.Thread(target=read_line, daemon=True)
                t.start()
                t.join(timeout=2.0)
                
                if typed_holder[0] is not None:
                    user_text = typed_holder[0].strip()
            
            if not user_text:
                continue
            
            # Process input
            print(f"\n  \033[93m[USER]\033[0m {user_text}")
            context.add_user(user_text)
            
            # Resolve pronouns
            resolved = context.resolve_pronouns(user_text)
            if resolved != user_text:
                print(f"  \033[90m[Resolved to: {resolved}]\033[0m")
            
            # Process with enhanced AI brain
            result = brain.process(resolved)
            context.set_last_action(result)
            
            if result["type"] == "conversation":
                # Conversational reply
                reply = result["reply"]
                speak(reply)
                context.add_disha(reply)
            
            elif result["type"] == "action":
                # Execute action
                action = result["action"]
                params = result.get("params", {})
                explanation = result.get("explanation", "")
                
                # Update context anchors
                if action == "open_app":
                    context.set_last_app(params.get("app", ""))
                if action in ("search_google", "play_youtube"):
                    context.set_last_query(params.get("query", ""))
                if action == "open_url":
                    context.set_last_url(params.get("url", ""))
                
                ok, msg = dispatch(action, params, explanation)
                
                if ok:
                    speak(msg)
                else:
                    speak(f"I encountered an issue: {msg}")
                
                context.add_disha(msg)
            
            print()  # spacing
        
        except KeyboardInterrupt:
            print("\n\n  [!] Interrupted. Type 'quit' to exit or Ctrl+C again to force.")
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                speak("Emergency shutdown initiated.")
                break
        
        except Exception as e:
            print(f"\n  \033[91m[ERROR]\033[0m Unexpected error: {e}")
            log_action("error", {}, status="failed", detail=str(e))
            speak("I encountered an unexpected error. Please try again.")
            time.sleep(1)
    
    # Cleanup
    if voice_in:
        voice_in.stop()
    if voice_out:
        voice_out.stop()
    
    print("\n  \033[96m[SHUTDOWN]\033[0m DISHA systems offline. Goodbye!\n")


# ===========================================================================
if __name__ == "__main__":
    main()
