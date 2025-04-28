import subprocess
import tempfile
import os


async def run_code(code):
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        code_path = os.path.join(tmp_dir_name, "script.cpp")

        with open(code_path, "w") as f:
            f.write(code)

        try:
            result = subprocess.run(
                [
                    "docker", "run", "--rm",
                    "-v", f"{tmp_dir_name}:/app",
                    "--network", "none",
                    "--memory", "128m",
                    "--cpus", "0.5",
                    "gcc:latest",
                    "g++", "/app/script.cpp", "-o", "/app/script.out"
                ],
                capture_output=True,
                text=True,
            )

            if result.returncode != 0:
                return {"output": "", "error": result.stderr}

            result = subprocess.run(
                [
                    "docker", "run", "--rm",
                    "-v", f"{tmp_dir_name}:/app",
                    "--network", "none",
                    "--memory", "128m",
                    "--cpus", "0.5",
                    "gcc:latest",
                    "/app/script.out"
                ],
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
