import subprocess
import tempfile
import os

def get_docker_commands(tmp_dir_name):
    """
    Creates temporary docker container and runs c++ script
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
        "kost13/cpp-gtest:latest",
        "bash", "-c",
        "g++ /app/script.cpp -lgtest -lgtest_main -lpthread -o /app/script.out && /app/script.out"
    ]

def save_to_temp_folder(tmp_dir_name, code):
    code_path = os.path.join(tmp_dir_name, "script.cpp")

    with open(code_path, "w") as f:
        f.write(code)


async def run_code(code):
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        save_to_temp_folder(tmp_dir_name, code)

        try:
            result = subprocess.run(
                get_docker_commands(tmp_dir_name),
                capture_output=True,
                text=True,
                timeout=5
            )

            output = result.stdout
            error = result.stderr

        except subprocess.TimeoutExpired:
            output = ""
            error = "Execution timed out."

        return {"output": output, "error": error}
