import subprocess
import tempfile
import os
import uuid

def get_docker_commands(tmp_dir_name, container_name):
    """
    Creates temporary docker container and runs python script
    Also add limits of memory and cpu
    :param tmp_dir_name:
    :return:
    """
    return [
        "docker", "run", "--rm", "--name", container_name,
        "-v", f"{tmp_dir_name}:/code",
        "--network", "none",
        "--memory", "128m",
        "--cpus", "0.5",
        "python:3.12-slim",
        "python", "/code/script.py"
    ]

def save_to_temp_folder(tmp_dir_name, code):
    code_path = os.path.join(tmp_dir_name, "script.py")

    with open(code_path, "w") as f:
        f.write(code)


async def run_code(code):
    os.makedirs("/tmp", exist_ok=True)

    with tempfile.TemporaryDirectory(dir="/tmp") as tmp_dir_name:
        save_to_temp_folder(tmp_dir_name, code)

        container_name = f"python-runner-{uuid.uuid4().hex[:12]}"
        try:
            result = subprocess.run(
                get_docker_commands(tmp_dir_name, container_name),
                capture_output=True,
                text=True,
                timeout=10
            )

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
