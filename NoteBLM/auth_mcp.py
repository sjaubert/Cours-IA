import os
import sys
import time
import subprocess
from pathlib import Path

def get_chrome_path():
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")
    ]
    for path in chrome_paths:
        if Path(path).exists():
            return path
    return None

def kill_chrome():
    print("Stopping existing Chrome processes gracefully...")
    # Attempt gentle kill first
    result = subprocess.run(["taskkill", "/IM", "chrome.exe"], capture_output=True, text=True)
    # Check if there was any chrome process found and terminated
    if "SUCCESS" in result.stdout or result.returncode == 0:
        print("Waiting for Chrome to fully close...")
        time.sleep(3)
        # Force kill any lingering processes
        subprocess.run(["taskkill", "/IM", "chrome.exe", "/F"], capture_output=True, text=True)
        time.sleep(1)

def launch_chrome_with_debugging(executable):
    profile_dir = Path.home() / ".notebooklm-mcp" / "chrome-profile"
    profile_dir.mkdir(parents=True, exist_ok=True)
    args = [
        executable,
        "--remote-debugging-port=9222",
        "--no-first-run",
        "--no-default-browser-check",
        f"--user-data-dir={profile_dir}",
        "--remote-allow-origins=*",
    ]
    print(f"Launching Chrome on port 9222...")
    # Launch totally detached
    subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)

def run_notebooklm_auth():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    auth_exe = os.path.join(script_dir, "env_mcp", "Scripts", "notebooklm-mcp-auth.exe")
    if not os.path.exists(auth_exe):
        auth_exe = os.path.join(script_dir, "env_mcp", "Scripts", "notebooklm-mcp-auth")
        if not os.path.exists(auth_exe):
            print("Error: Cannot find notebooklm-mcp-auth executable.", file=sys.stderr)
            return 1
    
    print("\nRunning notebooklm-mcp-auth...")
    print("Please follow the instructions on the newly opened Chrome browser if prompted.")
    process = subprocess.Popen([auth_exe, "--port", "9222"])
    process.wait()
    return process.returncode

def main():
    chrome_exe = get_chrome_path()
    if not chrome_exe:
        print("Error: Could not find chrome.exe on this system.", file=sys.stderr)
        sys.exit(1)
        
    kill_chrome()
    launch_chrome_with_debugging(chrome_exe)
    
    code = run_notebooklm_auth()
    if code == 0:
        print("\n=== Authentication flow finished successfully! ===")
        print("Your tokens have been captured. Note that you may need to re-run this script when they expire.")
    else:
        print("\n=== Authentication flow ended with an error. ===", file=sys.stderr)
        
    sys.exit(code)

if __name__ == "__main__":
    main()
