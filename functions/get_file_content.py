import os

def get_file_content(working_directory, file_path):
    try:
        path = os.path.abspath(working_directory)
        joined = os.path.join(path,file_path)
        target_dir = os.path.normpath(joined)
        valid_target_dir = os.path.commonpath([path, target_dir]) == path
        if valid_target_dir == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(target_dir,"r") as f:
            file_contents = f.read(10000)
            if f.read(1):
                file_contents += f'[...File "{file_path}" truncated at 10000 characters]'
            return file_contents
    except Exception as e:
        return f"Error: {e}"
