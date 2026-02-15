import os


def get_files_info(working_directory, directory="."):
    try:
        path = os.path.abspath(working_directory)
        joined = os.path.join(path,directory)
        target_dir = os.path.normpath(joined)
        valid_target_dir = os.path.commonpath([path, target_dir]) == path
        if valid_target_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
            f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
                    )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error: {e}"
