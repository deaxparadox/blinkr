"""
Remove unncessary files (not required for deployment).

1. Test files.
2. Docker files if not required.
3. Asgi if not required
"""


from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_dirs = ['.vnev', '.env', 'venv', 'env']
remove_dirs = ['.tests', 'tests','.test', 'test', 'docs', 'script', "ui", "env", ".env"]
remove_files = ['.python-version', 'README.md']
SIZE: int = 0

# Files to remove
REMOVE:list[str] = []


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def check_env_dir(_path: str = None):
    
    # Env dirs name list
    
    # If any path contains the env dir name,
    # return True
    if any(p in _path.split("\\") for p in env_dirs):
        return True
    
    return False


def list_files():
    """
    This function remove uncessary files,
    not required during deployment.
    """
    
    
    global SIZE
    for root, dirs, files in os.walk(BASE_DIR):
        
        # Don't search if the path include "venv", ".venv", "env", or ".env".
        if check_env_dir(root):
            continue
    
        # Iterate through every directory,
        # remove the paths ending with name in `remove_dirs`.
        for d in dirs:    
            if d in remove_dirs:
                print(os.path.join(root, d))
                REMOVE.append(os.path.join(root, d))
                SIZE += os.stat(os.path.join(root, d)).st_size
                
        # Iterate through every file,
        # remove the paths ending with name in `remove_files`.
        for f in files:    
            if f in remove_files:
                print(os.path.join(root, f))
                REMOVE.append(os.path.join(root, f))
                SIZE += os.stat(os.path.join(root, f)).st_size
                
if __name__ == "__main__":
    list_files()
    print(f"\nFollowing files are going to be removed.\nTotal: {convert_bytes(SIZE)}")
    
    
    if input(r"Enter [y\n] : ").lower() == 'y':
        for f in REMOVE:
            print(f"{f} : Removed")
    else:
        print("No files removed.")
            
    
    
    