import sys
import subprocess
import re
from datetime import datetime

FIO = "KVN"

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <command> [arg]")
    sys.exit(1)

cmd = sys.argv[1]

if cmd == '-ping':
    if len(sys.argv) < 3:
        print("Usage: ./script.py -ping <host>")
        sys.exit(1)
    try:
        result = subprocess.check_output(
            ['ping', '-c', '1', sys.argv[2]], 
            text=True, 
            stderr=subprocess.STDOUT,
            timeout=10  # Защита от зависания
        )
        match = re.search(r'time=(.*?) ms', result)
        if match:
            print(match.group(1).strip())
        else:
            print("Ping failed or no time")
    except subprocess.TimeoutExpired:
        print("Ping timeout")
    except subprocess.CalledProcessError:
        print("Ping failed")
    except Exception:
        print("Ping error")

elif cmd == '-simple_print':
    if len(sys.argv) < 3:
        print("Usage: ./script.py -simple_print <text>")
        sys.exit(1)
    print(sys.argv[2])

elif cmd == '-1':
    print(FIO)

elif cmd == '-2':
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

else:
    print(f"unknown input: {cmd}")
