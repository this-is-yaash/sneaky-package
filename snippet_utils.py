import os
import subprocess
import sys

def display(snippet_name):
    """
    Displays the source code/information of the files in the console output.
    
    Args:
        snippet_name (str): The name of the snippet to display.
    """
    snippet_path = os.path.join(
        os.path.dirname(__file__), "code_snippets", f"{snippet_name}.py"
    )

    with open(snippet_path, "r") as file:
        source_code = file.read()
        print(source_code)


def graph(snippet_name):
    """
    Copies the source code/information to the system's clipboard.
    
    Args:
        snippet_name (str): The name of the snippet to copy.
    """
    snippet_path = os.path.join(
        os.path.dirname(__file__), "code_snippets", f"{snippet_name}.py"
    )

    with open(snippet_path, "r") as file:
        source_code = file.read()

    # Function to copy text to clipboard based on platform
    if "linux" in sys.platform:
        subprocess.run(
            ["/usr/bin/xclip", "-selection", "clipboard"],
            input=source_code.strip().encode(),
            check=True,
        )

    elif "win32" in sys.platform:
        subprocess.run(
            ["C:\\Windows\\System32\\clip.exe"],
            input=source_code.strip().encode(),
            check=True,
        )

    else:
        raise OSError("Unsupported operating system")


def piechart(snippet_name):
    """
    Writes the file to the root directory of execution.
    
    Args:
        snippet_name (str): The name of the snippet to write.
    """
    snippet_path = os.path.join(
        os.path.dirname(__file__), "code_snippets", f"{snippet_name}.py"
    )

    with open(snippet_path, "r") as file:
        source_code = file.read()

    with open(snippet_name + ".py", "w") as file:
        file.write(source_code)


# ---------for working with above function -------
#  from package_name.snippet_utils import display, copy_to_clipboard, write_to_root
# display('filename')
# copy_to_clipboard('filename')
# write_to_root('filename')

# --------example for how to use-------------
# from package_name.snippet_utils import display, copy_to_clipboard, write_to_root

# def main():
#     filename = 'example'  # replace with your filename
#     display(filename)
#     copy_to_clipboard(filename)
#     write_to_root(filename)

# if __name__ == "__main__":
#     main()