import os
import traceback
from utils.utils_hks import *

def main():
    all_fns = os.listdir(in_dir)
    normalize_all_hks(all_fns)
    _, _ = merge_all_hks(all_fns)

if __name__ == "__main__":
    try: main()
    except Exception as e: traceback.print_exc()
    finally: input("\nPress Enter to exit...")
