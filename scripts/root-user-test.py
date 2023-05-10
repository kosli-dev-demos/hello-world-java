import re
import sys

def check_dockerfile(filename):
    # Regular expression to match a non-root user declaration
    USER_REGEX = r'^\s*USER\s+([^\s0-9][^\s]*)\s*$'

    with open(filename, 'r') as f:
        content = f.read()
        # Find all instances of USER declaration in the Dockerfile
        user_declarations = re.findall(USER_REGEX, content, flags=re.MULTILINE)
        if not user_declarations:
            print(f"Error: {filename} does not declare a non-root user")
            return False
        else:
            # Check if the declared user is not root
            if "root" in user_declarations:
                print(f"Error: {filename} declares root as the user")
                return False
            else:
                print(f"{filename} declares a non-root user: {user_declarations[0]}")
                return True

# Example usage
if __name__ == "__main__":
    if not check_dockerfile("Dockerfile"):
        sys.exit(1)
    else:
        sys.exit(0)