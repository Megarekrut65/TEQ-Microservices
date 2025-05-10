import subprocess
import tempfile
import os
import uuid

def get_docker_commands(tmp_dir_name, container_name):
    """
    Creates temporary docker container and runs c++ script
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
        "kost13/cpp-gtest:latest",
        "bash", "-c",
        "g++ /code/script.cpp -lgtest -lgtest_main -lpthread -o /tmp/script.out && chmod +x /tmp/script.out && /tmp/script.out"
    ]

def save_to_temp_folder(tmp_dir_name, code):
    code_path = os.path.join(tmp_dir_name, "script.cpp")

    with open(code_path, "w") as f:
        f.write(code)


async def run_code(code):
    os.makedirs("/tmp", exist_ok=True)

    with tempfile.TemporaryDirectory(dir="/tmp") as tmp_dir_name:
        save_to_temp_folder(tmp_dir_name, code)

        container_name = f"cpp-runner-{uuid.uuid4().hex[:12]}"
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
