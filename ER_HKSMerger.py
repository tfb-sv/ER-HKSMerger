import traceback
from utils.utils_hks import *

def main():
    normalize_all_hks()
    _, _ = merge_all_hks()

if __name__ == "__main__":
    try: main()
    except Exception as e: traceback.print_exc()
    finally: input("\nPress Enter to exit...")
