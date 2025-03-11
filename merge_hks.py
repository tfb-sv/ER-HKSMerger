import os
from utils_hks import *

def main():
    data_dir = "inputs"
    ref_fp = "refs/c0000_refv17.hks"
    in_fns = os.listdir(data_dir)
    # in_fns = ["c0000_refv17.hks", "c0000_lord.hks"]   # normalization
    out_fp = "outputs/c0000_merged.hks"
    final_lines, final_name = merge_hks_scripts(data_dir, ref_fp, in_fns, out_fp)

if __name__ == "__main__": main()
