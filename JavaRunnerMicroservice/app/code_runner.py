import subprocess
import tempfile
import os

def get_docker_commands(tmp_dir_name, java_command):
    """
    Creates temporary docker container and runs python script
    Also add limits of memory and cpu
    :param tmp_dir_name:
    :return:
    """
    return [
        "docker", "run", "--rm",
        "-v", f"{tmp_dir_name}:/app",
        "--network", "none",
        "--memory", "128m",
        "--cpus", "0.5",
        "java-junit-image",
        "sh", "-c",
        java_command
    ]

def get_java_command(code):
    command = "javac Script.java && java Script"
    if "@Test" in code:
        command = ("javac -cp /libs/junit4.jar:/libs/hamcrest.jar:/libs/hamcrest-all.jar Script.java && "
                   "java -cp .:/libs/junit4.jar:/libs/hamcrest.jar:/libs/hamcrest-all.jar Script")

    return command

def save_to_temp_folder(tmp_dir_name, code):
    code_path = os.path.join(tmp_dir_name, "Script.java")

    with open(code_path, "w") as f:
        f.write(code)


async def run_code(code):
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        save_to_temp_folder(tmp_dir_name, code)

        try:
            result = subprocess.run(
                get_docker_commands(tmp_dir_name, get_java_command(code)),
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                return {"output": "", "error": result.stderr}

            output = result.stdout
            error = result.stderr

        except subprocess.TimeoutExpired:
            output = ""
            error = "Execution timed out."

        return {"output": output, "error": error}
