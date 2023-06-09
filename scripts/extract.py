#!/usr/bin/env bash

import argparse
import os
import re

def parse_arguments():
    parser = argparse.ArgumentParser(description='Find all unique java or jdk modules in a .dot file generated by jdeps.')
    parser.add_argument('filename', help='Path to input file (.dot). The "summary.dot" file is the recommended file.')
    return parser.parse_args()

def extract_java_strings(filename):
    # Check that the filename ends with ".dot"
    if not filename.endswith('.dot'):
        print('Error: input file must have ".dot" extension')
        return None

    # Check that the file exists and is not empty
    if not os.path.exists(filename):
        print(f'Error: file "{filename}" does not exist')
        return None

    if os.path.getsize(filename) == 0:
        print(f'Error: file "{filename}" is empty')
        return None

    # Open the file and read in the contents
    with open(filename, 'r') as file:
        contents = file.readlines()

    # Define a regular expression to match Java/JDK strings
    java_regex = re.compile(r'"(.+?)"\s+->\s+"(.+?)\s+\(')

    # Create an empty set to store unique Java/JDK strings
    unique_java_strings = set()

    # Loop through each line in the file
    for line in contents:
        # Search for Java/JDK strings in the line
        java_strings = java_regex.findall(line)

        # Add any found Java/JDK strings to the set
        for java_string in java_strings:
            unique_java_strings.add(java_string[1].split()[0])

    # Return the set of unique Java/JDK strings
    return unique_java_strings

def main():
    # Parse command-line arguments
    args = parse_arguments()

    # Extract Java/JDK strings from input file
    java_strings = extract_java_strings(args.filename)

    # Print the unique Java/JDK strings
    if java_strings is not None:
        print(java_strings)

if __name__ == '__main__':
    main()