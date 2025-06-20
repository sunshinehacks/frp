import subprocess
import os
import time

# Path to the frps binary and config file
frps_path = "./frps"
config_path = "./frps.toml"

# Make sure the binary is executable
os.chmod(frps_path, 0o755)

print("🚀 Starting FRP server...")

try:
    while True:
        process = subprocess.Popen([frps_path, "-c", config_path])
        print("✅ frps started. Waiting for it to exit...")
        process.wait()
        print("⚠️ frps exited. Restarting in 3 seconds...")
        time.sleep(3)
except KeyboardInterrupt:
    print("🛑 Exiting on user interrupt.")