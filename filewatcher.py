#!/usr/bin/env python3
import argparse
import os
import time
from datetime import datetime
VERSION = "1.0.0"

def watch_directory(path, callback=None):
    initial = set(os.listdir(path)) if os.path.exists(path) else set()
    print(f"Watching {path}... Press Ctrl+C to stop")
    try:
        while True:
            time.sleep(1)
            current = set(os.listdir(path)) if os.path.exists(path) else set()
            added = current - initial
            removed = initial - current
            if added or removed:
                for f in added:
                    print(f"[{datetime.now().isoformat()}] Created: {f}")
                for f in removed:
                    print(f"[{datetime.now().isoformat()}] Deleted: {f}")
                initial = current
    except KeyboardInterrupt:
        print("Stopped watching")

def main():
    parser = argparse.ArgumentParser(description='File Watcher Pro - Real-time file monitoring')
    parser.add_argument('path', nargs='?', default='.', help='Directory to watch')
    args = parser.parse_args()
    watch_directory(args.path)
if __name__ == '__main__':
    main()
