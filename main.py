# ============================================================
# DISHA  -  Digital Intelligent System for Human Assistant
# main.py  -  Central entry point & action dispatcher
#
# Usage:   python main.py   OR   double-click run.bat
# Deps:    pip install -r requirements.txt
# ============================================================

# --- Force UTF-8 stdout on Windows (MUST run before any print) --
import sys, os, io
if sys.platform == "win32":
    os.environ["PYTHONIOENCODING"] = "utf-8"
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "buffer"):
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

import time, threading
from pathlib import Path

# --- Lock CWD + sys.path so imports & data/ paths always resolve --
_THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS_DIR))
os.chdir(_THIS_DIR)

from config import MEMORY_FILE
from utils.helpers import (print_banner, time_greeting, speak as _speak_stub,
                           set_speak_fn, load_memory)
from utils.logger import log_action, pop_last_action, get_history

# --- Core modules ------------------------------------------------
from core.voice_input  import VoiceInput
from core.voice_output import VoiceOutput
from core.context_manager import ContextManager
from core.ai_brain     import AIBrain
from core.security     import request_permission, emergency_stop, is_stopped, reset_emergency

# --- Feature modules ---------------------------------------------
from modules import pc_control, file_manager, web_services
from modules import automation as automation_mod
from modules import writing_assistant, screen_reader, smart_home


# ===========================================================================
# GLOBAL INSTANCES  (created once at startup)
# ===========================================================================
voice_in  : VoiceInput      = None   # type: ignore
voice_out : VoiceOutput     = None   # type: ignore
context   : ContextManager  = None   # type: ignore
brain     : AIBrain         = None   # type: ignore


def speak(text: str):
    """Central speak function - routes to VoiceOutput."""
    if voice_out:
        voice_out.speak(text)
    else:
        print(f"  [DISHA] DISHA: {text}")


# ===========================================================================
# ACTION DISPATCHER
# ===========================================================================
# This is the single routing table.  The AI brain returns an action name;
# this function calls the correct module and returns (success, message).

def dispatch(action: str, params: dict) -> tuple[bool, str]:
    """Route an action to the appropriate module. Returns (ok, message)."""

    # --- Emergency / control --------------------------------------
    if action == "emergency_stop":
        emergency_stop()
        return True, "Emergency stop activated. All tasks halted."

    if action == "quit":
        speak("Goodbye, Subhra! See you next time. [BYE]")
        log_action("quit", status="success", detail="User requested exit.")
        sys.exit(0)

    if action == "undo":
        return handle_undo()

    # --- Security gate - dangerous actions need confirmation ------
    if not request_permission(action, params):
        return False, "Action cancelled."

    # --- PC Control -----------------------------------------------
    if action == "open_app":
        app = params.get("app", "")
        ok, msg = pc_control.open_app(app)
        if ok:
            context.set_last_app(app)
        return ok, msg

    if action == "close_app":
        app = params.get("app", "")
        ok, msg = pc_control.close_app(app)
        return ok, msg

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

    # --- File Management ------------------------------------------
    if action == "find_file":
        ok, msg = file_manager.find_file(params.get("name", ""))
        return ok, msg

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

    # --- Web Services ---------------------------------------------
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
        return web_services.download_file(params.get("url", ""),
                                          params.get("filename"))

    if action == "open_spotify":
        return web_services.open_spotify()

    if action == "open_whatsapp":
        return web_services.open_whatsapp()

    if action == "open_gmail":
        return web_services.open_gmail()

    # --- Automation -----------------------------------------------
    if action == "run_automation":
        name = params.get("name", "")
        return automation_mod.run_automation(name, dispatch)

    if action == "schedule_automation":
        return automation_mod.schedule_automation(
            params.get("time", "09:00"),
            params.get("name", ""),
            dispatch
        )

    if action == "multi_step":
        return automation_mod.execute_multi_step(params.get("steps", []), dispatch)

    # --- Writing & Notes ------------------------------------------
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

    # --- Screen ---------------------------------------------------
    if action == "take_screenshot":
        return screen_reader.take_screenshot()

    if action == "read_screen":
        return screen_reader.read_screen()

    if action == "find_element":
        return screen_reader.find_element(params.get("description", ""))

    # --- Smart Home -----------------------------------------------
    if action == "smart_home_light":
        return smart_home.control_light(params.get("action","on"), params.get("room","living room"))

    if action == "smart_home_fan":
        return smart_home.control_fan(params.get("action","on"), params.get("room","bedroom"))

    if action == "smart_home_ac":
        return smart_home.control_ac(params.get("action","on"), params.get("temp"))

    # --- Fallback -------------------------------------------------
    log_action(action, params, status="failed", detail="Unknown action.")
    return False, f"I don't know how to perform \"{action}\" yet."


# ===========================================================================
# UNDO HANDLER
# ===========================================================================

def handle_undo() -> tuple[bool, str]:
    """
    Undo the last action.  For most actions this just logs the reversal.
    For open_app -> close_app, and vice versa.
    """
    last = pop_last_action()
    if last is None:
        return False, "There's nothing to undo."

    action = last.get("action", "")
    params = last.get("params", {})

    # - Reversible pairs ------------------------------------------
    reverse_map = {
        "open_app":        ("close_app",  params),
        "close_app":       ("open_app",   params),
        "wifi_toggle":     ("wifi_toggle",{"state": not params.get("state", True)}),
        "bluetooth_toggle":("bluetooth_toggle",{"state": not params.get("state", True)}),
    }

    if action in reverse_map:
        rev_action, rev_params = reverse_map[action]
        print(f"  [UND]  Undoing {action} -> {rev_action}")
        log_action("undo", {"original": action}, status="pending", detail=f"Reversing {action}.")
        ok, msg = dispatch(rev_action, rev_params)
        return ok, f"Undone! I reversed the last action: {msg}"

    # - Non-reversible: just report -------------------------------
    log_action("undo", {"original": action}, status="success",
               detail="Action noted but not automatically reversible.")
    return True, (f"The last action was \"{action}\". "
                  "This one can't be automatically undone, but I've noted it.")


# ===========================================================================
# MAIN LOOP
# ===========================================================================

def main():
    global voice_in, voice_out, context, brain

    # --- Banner ----------------------------------------------------
    print_banner()

    # --- Init subsystems ------------------------------------------
    print("  Initialising DISHA...\n")

    voice_out = VoiceOutput()
    set_speak_fn(speak)                        # wire speak() everywhere

    context = ContextManager()
    brain   = AIBrain(context)
    voice_in = VoiceInput()

    # --- Startup greeting -----------------------------------------
    mem = load_memory(MEMORY_FILE)
    name = mem.get("user_name", "Subhra")
    greeting = f"{time_greeting()}, {name}! I'm DISHA, your personal assistant. " \
               f"I'm listening for you. Say 'Hey DISHA' to wake me up, " \
               f"or just type a command here."
    speak(greeting)

    # --- Start background voice listener --------------------------
    voice_in.start()

    # --- Main event loop ------------------------------------------
    print("\n  " + "-" * 58)
    print("  Type a command below, or speak after the wake word.\n")

    while True:
        try:
            # -- Check for emergency stop -------------------------
            if is_stopped():
                print("\n  [!!!] Emergency stop is active. Type 'reset' to resume.")
                typed = input("  > ").strip()
                if typed.lower() == "reset":
                    reset_emergency()
                    speak("Emergency stop cleared. I'm ready again.")
                    voice_in.start()
                continue

            # -- Get input: voice queue OR keyboard ---------------
            user_text = None

            # non-blocking check on voice queue
            if voice_in.has_command():
                user_text = voice_in.get_command(timeout=0.1)
            else:
                # offer keyboard input with a short timeout so we keep
                # polling the voice queue
                import select, sys as _sys
                # On Windows select doesn't work on stdin; use threading trick
                typed_holder = [None]
                def read_line():
                    try:
                        typed_holder[0] = input("  > ")
                    except (EOFError, KeyboardInterrupt):
                        typed_holder[0] = "quit"

                t = threading.Thread(target=read_line, daemon=True)
                t.start()
                t.join(timeout=2.0)            # wait 2s for keyboard

                if typed_holder[0] is not None:
                    user_text = typed_holder[0].strip()

            if not user_text:
                continue                       # loop back, keep listening

            # -- Process the input --------------------------------
            print(f"\n  [SAY]  Input: \"{user_text}\"\n")
            context.add_user(user_text)

            # Pronoun resolution (local, fast)
            resolved = context.resolve_pronouns(user_text)
            if resolved != user_text:
                print(f"  [LNK] Resolved to: \"{resolved}\"")

            # AI brain decides: action or conversation
            result = brain.process(resolved)
            context.set_last_action(result)

            if result["type"] == "conversation":
                # -- Just talk back -----------------------------
                reply = result["reply"]
                speak(reply)
                context.add_disha(reply)

            elif result["type"] == "action":
                # -- Execute the action -------------------------
                action = result["action"]
                params = result.get("params", {})

                # Update context anchors
                if action == "open_app":
                    context.set_last_app(params.get("app", ""))
                if action in ("search_google", "play_youtube"):
                    context.set_last_query(params.get("query", ""))
                if action == "open_url":
                    context.set_last_url(params.get("url", ""))

                ok, msg = dispatch(action, params)
                speak(msg)
                context.add_disha(msg)

            print()  # spacing

        except KeyboardInterrupt:
            print("\n\n  [BYE] Interrupted. Type 'quit' to exit or press Ctrl+C again.")
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                speak("Goodbye!")
                break

        except Exception as e:
            print(f"\n  [!]  Unexpected error: {e}")
            log_action("error", {}, status="failed", detail=str(e))
            time.sleep(1)

    # --- Cleanup --------------------------------------------------
    if voice_in:
        voice_in.stop()
    print("\n  [BYE] DISHA has been shut down. Goodbye!\n")


# ===========================================================================
if __name__ == "__main__":
    main()
