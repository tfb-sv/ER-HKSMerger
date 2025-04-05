import os
import re
from merge3 import Merge3

in_dir = "inputs"
out_dir = "outputs"
ref_dir = "refs"

no_file_text = (
    "\n\nUnable to find HKS files!\n"
    'There should be at least 2 HKS files in the "inputs" folder.'
)

no_v_text = (
    "\n\nUnable to determine version!\n"
    "Make sure the file contains version info on line 6."
)

wrong_v_text = (
    "\n\nVersion incompatibility!\n"
    "Supported reference versions are from 11 to 17, inclusive."
)
wrong_fn_text = (
    "\n\nInvalid filename format!\n"
    'Must follow the format "c0000_<tag>.hks", where "<tag>" contains only letters and digits.'
)

last_version = 17
supported_vers = list(range(11, last_version + 1))

char_id = "c0000"
last_ref_fp = f"{ref_dir}/{char_id}_ref_v{last_version}.hks"
out_fn = f"{char_id}_merged.hks"

in_fns = [fn for fn in os.listdir(in_dir) if fn != ".gitkeep"]

def read_file(fp):
    with open(fp, 'r', encoding="utf8") as f: lines = f.readlines()
    return lines

def write_file(fp, lines):
    with open(fp, 'w', encoding="utf8") as f: f.writelines(lines)

def check_fn(fn):
    print(f'File "{fn}":\n\t> Checking the filename format..')
    pattern = r"^c0000_[a-zA-Z0-9]+\.hks$"
    if not re.match(pattern, fn): raise ValueError(wrong_fn_text)
    print("\t> Filename format is correct.")

def get_hks_version(fn):
    fp = f"{in_dir}/{fn}"
    print("\t> Checking the file version..")
    lines = read_file(fp)
    match = re.search(r"-- Version (\d+)", lines[5])
    if match: hks_version = int(match.group(1))
    else: hks_version = None
    print(f"\t> File version is checked. Version: {hks_version}")
    return hks_version

def normalize_all_hks():
    if not os.path.exists(in_dir): raise ValueError(no_file_text)
    for fn in in_fns:
        check_fn(fn)
        hks_version = get_hks_version(fn)
        if hks_version is None: raise ValueError(no_v_text)
        elif hks_version not in supported_vers: raise ValueError(wrong_v_text)
        elif hks_version == last_version:
            print(f"\t> Version is already {last_version}.\n")
            continue
        else: normalize_hks(fn, hks_version)

def normalize_hks(hks_fn, hks_version):
    ref_fp = f"{ref_dir}/{char_id}_ref_v{hks_version}.hks"
    ref_lines = read_file(ref_fp)
    last_ref_lines = read_file(last_ref_fp)
    hks_fp = f"{in_dir}/{hks_fn}"
    hks_lines = read_file(hks_fp)
    merged_lines = merger_core(ref_lines, last_ref_lines, hks_lines)
    write_file(hks_fp, merged_lines)
    print(f"\t> File version is updated to {last_version}.\n")

def merger_core(ref, a, b):
    merger = Merge3(ref, a, b)
    merged = list(merger.merge_lines())
    return merged

def recursive_merge(recursive_input):
    [in_fns, in_names, ref_lines, stage_cnt, ref_name] = recursive_input  # , cnt
    in_groups = [in_fns[i:i + 2] for i in range(0, len(in_fns), 2)]
    name_groups = [in_names[i:i + 2] for i in range(0, len(in_names), 2)]
    if len(in_groups[0]) == 1: return in_groups[0][0], name_groups[0][0]  # , cnt
    print(f"\nStage {stage_cnt+1}:")
    print(f"\t{name_groups} =")
    new_in_groups = []
    new_name_groups = []
    for cnt, sub_groups in enumerate(in_groups):
        sub_names = name_groups[cnt]
        if len(sub_groups) == 2:
            [a, b] = sub_groups
            [a_name, b_name] = sub_names
        else:
            [a] = sub_groups
            [a_name] = sub_names
            b = ref_lines
            b_name = ref_name
        if stage_cnt == 0:
            a = read_file(f"{in_dir}/{a}") if isinstance(a, str) else a
            b = read_file(f"{in_dir}/{b}") if isinstance(b, str) else b
        merged_lines = merger_core(ref_lines, a, b)
        # merged_lines, cnt1 = deal_with_merge_conflicts(merged_lines, a_name, b_name, stage_cnt)
        merged_names = f"{a_name}-{b_name}"
        print(f"\t\t({ref_name}, {a_name}, {b_name})")
        # if cnt1 > 0: print(f"\t\t{cnt1} merge conflict(s) occurred between the {a_name.capitalize()} and {b_name.capitalize()} mods!")
        # cnt += cnt1
        new_in_groups.append(merged_lines)
        new_name_groups.append(merged_names)
    recursive_output = [new_in_groups, new_name_groups, ref_lines, stage_cnt+1, ref_name]  # , cnt
    return recursive_merge(recursive_output)

# def deal_with_merge_conflicts(merged_lines, a_n, b_n, stage_cnt):
    # c_s = "<<<<<<<"
    # c_m = "======="
    # c_e = ">>>>>>>"
    # new_merged_lines = []
    # cnt = 0
    # for line in merged_lines:
        # if c_s in line:
            # cnt += 1
            # line = line.replace(c_s, f"-- {c_s} - Start of the Conflict {cnt} > {a_n.capitalize()} Code")
        # elif c_m in line:
            # line = line.replace(c_m, f"-- {c_m} - Middle of the Conflict {cnt} > {b_n.capitalize()} Code")
        # elif c_e in line:
            # line = line.replace(c_e, f"-- {c_e} - End of the Conflict {cnt}")
        # new_merged_lines.append(line)
    # return new_merged_lines, cnt

def comment_merge_conflicts(final_lines):
    c_s = "<<<<<<<"
    c_m = "======="
    c_e = ">>>>>>>"
    new_final_lines = []
    cnt_s = cnt_m = cnt_e = 0
    for line in final_lines:
        if c_s in line:
            cnt_s += 1
            line = line.replace(c_s, f"-- {c_s} - MERGE CONFLICT #{cnt_s} START")
        elif c_m in line:
            cnt_m += 1
            line = line.replace(c_m, f"-- {c_m} - MERGE CONFLICT #{cnt_m} MIDDLE")
        elif c_e in line:
            cnt_e += 1
            line = line.replace(c_e, f"-- {c_e} - MERGE CONFLICT #{cnt_e} END")
        new_final_lines.append(line)
    assert cnt_s == cnt_m == cnt_e, "Conflict counters are not same!"
    return new_final_lines, cnt_s

def merge_all_hks():
    if len(in_fns) < 2: raise ValueError(no_file_text)
    ref_lines = read_file(last_ref_fp)
    ref_fn = last_ref_fp.split("/")[1]
    ref_name = ref_fn[:-4].split("_")[1]
    in_names = [in_fn[:-4].split("_")[1] for in_fn in in_fns]
    stage_cnt = 0
    recursive_input = [in_fns, in_names, ref_lines, stage_cnt, ref_name]  # , 0
    final_lines, final_name = recursive_merge(recursive_input)  # , cnt
    final_lines, cnt = comment_merge_conflicts(final_lines)
    if not os.path.exists(out_dir): os.mkdir(out_dir)
    out_fp = f"{out_dir}/{out_fn}"
    write_file(out_fp, final_lines)
    if cnt > 0: print(f"\n> All {len(in_fns)} files were merged, but {cnt} merge conflict(s) occurred, which need to be resolved manually!\n")
    else: print(f"\n> All {len(in_fns)} files were merged successfully!\n")
    return final_lines, final_name
