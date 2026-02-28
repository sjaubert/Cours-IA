import sys
import os

# Ensure the virtual environment's site-packages is in the path
script_dir = os.path.dirname(os.path.abspath(__file__))
site_packages = os.path.join(script_dir, "env_mcp", "Lib", "site-packages")
sys.path.insert(0, site_packages)

try:
    from notebooklm_mcp.api_client import NotebookLMClient
    from notebooklm_mcp.auth import load_cached_tokens
except ImportError as e:
    print(f"Error: Could not import NotebookLM modules ({e}).", file=sys.stderr)
    print("Ensure notebooklm-mcp-server is installed in env_mcp.", file=sys.stderr)
    sys.exit(1)

def main():
    print("Testing connection to NotebookLM...")
    
    # Load authentication tokens from the cache
    tokens = load_cached_tokens()
    if not tokens or not tokens.cookies:
        print("\nError: No valid authentication tokens found.")
        print("Please run the authentication script first:")
        print(f"  python {os.path.join(script_dir, 'auth_mcp.py')}")
        sys.exit(1)
        
    try:
        # Initialize the API client
        client = NotebookLMClient(
            cookies=tokens.cookies,
            csrf_token=tokens.csrf_token,
            session_id=tokens.session_id
        )
        
        # Test connection by listing notebooks
        notebooks = client.list_notebooks()
        
        if not notebooks:
            print("\nSuccess: Authenticated properly, but no notebooks were found in your account.")
        else:
            print("\nSuccess! Here are your NotebookLM notebooks:")
            for nb in notebooks[:10]: # Limit to 10 for display purposes
                print(f" - {nb.title} (ID: {nb.id})")
            
            if len(notebooks) > 10:
                print(f"   ... and {len(notebooks) - 10} more.")
                
    except Exception as e:
        error_msg = str(e).lower()
        if "auth" in error_msg or "expire" in error_msg or "cookie" in error_msg:
            print(f"\nError: Authentication Expired or Invalid.")
            print(f"Details: {e}")
            print("\nPlease run the authentication script to renew your tokens:")
            print(f"  python {os.path.join(script_dir, 'auth_mcp.py')}")
        else:
            print(f"\nAn error occurred while communicating with NotebookLM: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
