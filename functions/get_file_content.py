import os
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(abs_file_path, "r") as f:
            content = f.read(10000)
            if f.read(1):
                content += (
                    f'[...File "{file_path}" truncated at 10000 characters]'
                )
        return content
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
    
schema_get_files_content = types.FunctionDeclaration(
            name="get_file_content",
            description="returns contents of a file in a specified directory relative to the working directory",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="Path to the file whose contents should be returned, relative to the working directory.",
            ),
        },
        required=["file_path"]
    ),
)