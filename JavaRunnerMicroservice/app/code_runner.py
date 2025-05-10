import subprocess
import tempfile
import os
import uuid


def get_docker_commands(tmp_dir_name, java_command, container_name):
    """
    Creates temporary docker container and runs python script
    Also add limits of memory and cpu
    :param tmp_dir_name:
    :return:
    """
    return [
        "docker", "run", "--rm", "--name", container_name,
        "-v", f"{tmp_dir_name}:/app",
        "--network", "none",
        "--memory", "128m",
        "--cpus", "0.5",
        "megarekrut65/java-junit",
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
    os.makedirs("/tmp", exist_ok=True)

    with tempfile.TemporaryDirectory(dir="/tmp") as tmp_dir_name:
        save_to_temp_folder(tmp_dir_name, code)

        container_name = f"java-runner-{uuid.uuid4().hex[:12]}"

        try:
            result = subprocess.run(
                get_docker_commands(tmp_dir_name, get_java_command(code), container_name),
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode != 0:
                return {"output": "", "error": result.stderr}

            output = result.stdout
            error = result.stderr

        except subprocess.TimeoutExpired:
            output = ""
            error = "Execution timed out."
            subprocess.run(
                ["docker", "rm", "-f", container_name],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL)

        return {"output": output, "error": error}
