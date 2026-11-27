"""Entry script for the Production Database Apology competition.

This module reads the apology line from line.txt and writes it to entry.txt
in the output directory specified by the MAKEFUN_OUTPUT_DIR environment variable.
Defaults to /output if not set.
"""

import os


def main():
    """Read line.txt and write its contents to entry.txt in the output directory."""
    # Read the line from line.txt
    with open('line.txt', 'r', encoding='utf-8') as f:
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