import os

def write_file(working_directory, file_path, content):
    try:
        path = os.path.abspath(working_directory)
        joined = os.path.join(path, file_path)
        target_dir = os.path.normpath(joined)

        # Prevent directory traversal
        if os.path.commonpath([path, target_dir]) != path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # If path is an existing directory
        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # Create parent directory if needed
        parent_dir = os.path.dirname(target_dir)
        os.makedirs(parent_dir, exist_ok=True)

        with open(target_dir, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
