import os
import subprocess

def run_python_file(working_directory,file_path,args=None):
    try:
        path = os.path.abspath(working_directory)
        joined = os.path.join(path,file_path)
        target_dir = os.path.normpath(joined)
        valid_target_dir = os.path.commonpath([path, target_dir]) == path
        if valid_target_dir == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'
        if not os.path.isfile(file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        command = ["python", target_dir]
        if args != None:
            command.extend(args)
        message = ""
        CompletedProcess = subprocess.run(command,timeout=30,text=True,cwd=working_directory,capture_output=True)
        if CompletedProcess.returncode != 0:
            message += f"Process exited with code {CompletedProcess.returncode}"
        if CompletedProcess.stderr == "" and CompletedProcess.stdout == "":
            message += "No output produced"
        else:
            message += f"STDOUT: {CompletedProcess.stdout}"
            message += f"STDERR: {CompletedProcess.stderr}"
        return message
    except Exception as e:
        return f"Error: executing Python file: {e}"
        
