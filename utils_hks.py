from merge3 import Merge3

def read_file(fp):
    with open(fp, 'r') as f: lines = f.readlines()
    return lines

def write_file(fp, lines):
    with open(fp, 'w') as f: f.writelines(lines)
    print(f"\n{len(lines)} lines are written to the {fp} file.")

def recursive_merge(recursive_input):
    [in_fns, in_names, ref_lines, stage_cnt, ref_name, data_dir] = recursive_input
    in_groups = [in_fns[i:i + 2] for i in range(0, len(in_fns), 2)]
    name_groups = [in_names[i:i + 2] for i in range(0, len(in_names), 2)]
    print(f"\nStage {stage_cnt+1}:")
    print(name_groups, "=")
    if len(in_groups[0]) == 1: return in_groups[0][0], name_groups[0][0]
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
            a = read_file(f"{data_dir}/{a}") if isinstance(a, str) else a
            b = read_file(f"{data_dir}/{b}") if isinstance(b, str) else b
        merger = Merge3(ref_lines, a, b)
        merged_lines = list(merger.merge_lines())
        merged_names = f"{a_name}-{b_name}"
        print(f"({ref_name}, {a_name}, {b_name})")
        new_in_groups.append(merged_lines)
        new_name_groups.append(merged_names)
    recursive_output = [new_in_groups, new_name_groups, ref_lines, stage_cnt+1, ref_name, data_dir]
    return recursive_merge(recursive_output)

def merge_hks_scripts(data_dir, ref_fp, in_fns, out_fp):
    ref_lines = read_file(ref_fp)
    ref_fn = ref_fp.split("/")[1]
    ref_name = ref_fn[:-4].split("_")[1]
    in_names = [in_fn[:-4].split("_")[1] for in_fn in in_fns]
    stage_cnt = 0
    recursive_input = [in_fns, in_names, ref_lines, stage_cnt, ref_name, data_dir]
    final_lines, final_name = recursive_merge(recursive_input)
    write_file(out_fp, final_lines)
    print("Merging completed.")
    return final_lines, final_name
