[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

# Elden Ring HKS Merger

**ER-HKSMerger** is a modding tool for Elden Ring that automates and simplifies the HKS merging procedure, particularly the cumbersome task of correctly locating and placing changed lines within the thousands of lines in HKS files. The tool is built upon the **Merge3 algorithm**.

- [NexusMods Page](https://www.nexusmods.com/eldenring/mods/7660)

## Installation
1. Download the latest release of the tool.
2. Extract the tool folder from the downloaded file.
3. Place the extracted folder in a directory, such as the `Users\<your-windows-username>`, where file read/write permissions are unrestricted.

## Configuration
- Place all your HKS files into the `inputs` folder.
- Make sure each file is named in the format `c0000_<tag>.hks`, where `<tag>` contains only letters and digits. For example: `c0000_clever.hks`, `c0000_wings.hks`, or `c0000_1.hks`.

## Usage
1. Ensure that the steps outlined in the **Configuration** section are completed.
2. Launch the `ER-HKSMerger.exe`.
3. The merged HKS file is generated in the `outputs` folder as `c0000_merged.hks`.

## Notes
- Tested on **v1.16**.
- This is not a mod but a tool that allows you to create mods.
- Specifically designed to operate on the **Windows** platform.
- Currently supports only HKS files of the player character, which is **c0000**.
- The tool automatically upgrades older HKS files to the latest supported version, which is **version 17**.
- You can merge as many HKS files as you want at once; however, as the number of files increases and the extent of their differences grows, the chance of merge conflicts also increases. Therefore, it's recommended to test the merged files, as manual adjustments may occasionally be necessary.
- The 6th line of `c0000.hks` files must contain version information, which is usually present. However, some mod creators intentionally remove this and similar metadata. In such cases, the tool cannot merge these files.

## Additional Information
- To uninstall, simply delete the tool's folder.

## Contributing
Feedback and contributions are highly valued. Issues or suggestions for improvements can be reported by opening an issue on the [GitHub page](https://github.com/tfb-sv/ER-HKSMerger.git), or by creating a post or posting a bug on [NexusMods page](https://www.nexusmods.com/eldenring/mods/7660). Please report any anomalies in the terminal.

## License
© 2025 [ineedthetail](https://github.com/tfb-sv).

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

**ER-HKSMerger** uses the following open-source work:
- [EldenRingHKS](https://github.com/ividyon/EldenRingHKS.git) by [ividyon](https://github.com/ividyon)

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
