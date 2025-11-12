#!/usr/bin/env python3

from datetime import datetime
import time


def main():
    try:
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Текущее время: {current_time}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nУзел остановлен")

if __name__ == "__main__":
    main()
