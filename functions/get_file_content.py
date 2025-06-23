import os


def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(
            os.path.join(working_directory, file_path))

        # Check if file_path is within working_directory
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check if file_path is a regular file
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        MAX_CHARS = 10000

        with open(abs_file_path, "r") as f:
            content = f.read(MAX_CHARS)
            # tyr reading one more char to check if file is longer
            rest = f.read(1)

            if rest:
                # If file is longer, append truncation message
                content += f'\n[...File "{file_path}" truncated at 10000 characters]'
            return content
    except Exception as e:
        return f"Error: {e}"


# Here are some standard library functions you'll find helpful:

# os.path.abspath(): Get an absolute path from a relative path
# os.path.join(): Join two paths together safely (handles slashes)
# .startswith(): Check if a string starts with a substring
# os.path.isdir(): Check if a path is a directory
# os.listdir(): List the contents of a directory
# os.path.getsize(): Get the size of a file
# os.path.isfile(): Check if a path is a file
# .join(): Join a list of strings together with a separator
