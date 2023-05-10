import os
import subprocess
import sys

success_count = 0
failure_count = 0
results = []

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <directory>")
    sys.exit(1)

directory = sys.argv[1]

# Scan the specified directory for Python files
for filename in os.listdir(directory):
    if filename.endswith(".py"):
        full_path = os.path.join(directory, filename)
        print(f"Running {full_path}...")
        # Invoke the Python file and capture its output
        process = subprocess.Popen(["python", full_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        result = process.returncode
        results.append((full_path, result, output, error))
        # Check if the Python file executed successfully
        if result == 0:
            success_count += 1
        else:
            failure_count += 1

# Print the summary of execution results
print(f"Executed {success_count} Python files successfully and {failure_count} with errors.\n")

# Print the output and error of each Python file
for filename, result, output, error in results:
    print(f"Results for {filename}:\n")
    print(f"Return code: {result}\n")
    if output:
        print("Standard output:")
        print(output.decode())
    if error:
        print("Standard error:")
        print(error.decode())
    print("-" * 80)
