from datetime import datetime
def log_to_file(message):
    file_name = "output.py"
    with open(file_name, "a") as f1:
        f1.write(f"{message}\n")

log_to_file(f"Session started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")