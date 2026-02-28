import os
import sys
import json
import threading
import subprocess

def forward_stderr(process):
    """Forward the stderr of the subprocess to our own stderr."""
    for line in process.stderr:
        print(line, end='', file=sys.stderr, flush=True)

def main():
    # Resolve the path to the executable inside our env_mcp
    script_dir = os.path.dirname(os.path.abspath(__file__))
    executable = os.path.join(script_dir, "env_mcp", "Scripts", "notebooklm-mcp.exe")
    
    if not os.path.exists(executable):
        executable = os.path.join(script_dir, "env_mcp", "Scripts", "notebooklm-mcp")
        if not os.path.exists(executable):
            print(f"Error: Cannot find notebooklm-mcp executable in env_mcp/Scripts", file=sys.stderr)
            sys.exit(1)
            
    # Launch the mcp server
    # We must not buffer the stdout so we can process lines as they arrive
    process = subprocess.Popen(
        [executable],
        stdin=sys.stdin,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,  # Line buffered
        env=os.environ.copy()
    )
    
    # Thread to handle stderr continuously
    stderr_thread = threading.Thread(target=forward_stderr, args=(process,), daemon=True)
    stderr_thread.start()
    
    # Read stdout line by line and filter
    for line in process.stdout:
        line_stripped = line.strip()
        if not line_stripped:
            continue
            
        try:
            # Check if this line is a valid JSON object
            json.loads(line_stripped)
            # Valid JSON - this is likely a JSON-RPC message, pass it through
            print(line, end='', flush=True)
        except json.JSONDecodeError:
            # Not valid JSON - this is probably some rogue log output or banner
            # Redirect it to stderr so it doesn't break the MCP client
            print(f"[notebooklm-mcp guard] {line}", end='', file=sys.stderr, flush=True)

    process.wait()
    sys.exit(process.returncode)

if __name__ == "__main__":
    main()
