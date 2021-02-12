import os
import time
import subprocess
import datetime

def  main():
    wait_time = os.environ.get("INPUT_SECONDS", 10)
    print(f"Waiting {wait_time} seconds ...")
    time.sleep(int(wait_time))
    print("Done.")

    now = datetime.datetime.now()
    args = ["echo", "::set-output", f"name=time::{now.isoformat()}"]
    subprocess.call(args)


if __name__ == "__main__":
    main()
