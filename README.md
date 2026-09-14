# Cryptix File Expander (CRYPTIX SHADOW KERNEL HEX)

A simple, interactive Python tool to expand a file by appending null bytes up to a target size (max 4GB). Built for educational and testing purposes only.

Important — Legal & safety
- Use this tool only on machines and files you own or where you have explicit permission.
- Expanding files can consume large amounts of disk space and may cause system instability or data loss if disk becomes full. Always verify available free space before use.
- The author and repository maintainers are not responsible for misuse.

Features
- Interactive CLI with colorful banner and progress bar
- Input validation for sizes (supports `1`, `0.5`, `2GB`, etc.)
- Creates a copy of the original file named `<name>_expanded<ext>`
- Maximum allowed expansion: 4GB

Requirements
- Python 3.7+ (tested)
- No external dependencies required, but for improved CLI experience you can optionally install `tqdm` or `colorama`.

Quick start (interactive)
1. Clone the repo:
   git clone https://github.com/basimstore-com/cryptix-file-expander.git
2. Run:
   python3 index.py
3. Follow interactive prompts:
   - Enter path to file
   - Enter target size (GB) up to 4
   - Confirm to proceed

Example
```
$ python3 index.py
[?] Enter path to file: ./sample.bin
[?] Enter target size (GB, max 4GB): 0.5GB
[?] Proceed? (yes/no): yes
... progress ...
```

Recommended improvements
- Add a non-interactive CLI using argparse: `--input`, `--size`, `--output`, `--yes` (for auto-confirm).
- Use sparse file allocation (os.truncate / posix_fallocate / fallocate) where available to avoid heavy IO.
- Add a pre-check for available free disk space and abort if insufficient.
- Add unit tests and a CI workflow (.github/workflows/ci.yml).
- Consider adding logging (to a file) with an option to be verbose or quiet.

Security & abuse mitigation
- Validate that the path is writable and on expected filesystem.
- Limit max size (already set to 4GB) and consider making this configurable with caution.
- Add rate-limiting or other checks if integrating into any automated systems.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
- Fork, make changes, open a PR.
- Add tests for parsing and size calculations.

Contact / Author
Project by Cryptix Security (as shown in file header). For issues or questions, open an issue on GitHub.
