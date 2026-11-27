"""Entry script for the Production Database Apology competition.

This module reads the apology line from line.txt and writes it to entry.txt
in the output directory specified by the MAKEFUN_OUTPUT_DIR environment variable.
Defaults to /output if not set.
"""

import os
from pathlib import Path


def main():
    """Read line.txt and write its contents to entry.txt in the output directory."""
    # Locate line.txt relative to this script's own file location so it works
    # regardless of the current working directory.
    line_path = Path(__file__).resolve().parent / "line.txt"

    # Read the line from line.txt
    with open(line_path, 'r', encoding='utf-8') as f:
        line = f.read()

    # Get the output directory from the environment variable or default to /output
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Write the line to entry.txt in the output directory
    output_path = os.path.join(output_dir, 'entry.txt')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(line)

    # Set the file mode to 0644 (readable by everyone)
    os.chmod(output_path, 0o644)


if __name__ == '__main__':
    main()