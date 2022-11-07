from env import export_passwd
import time

if __name__ == "__main__":
    print(f"For Testing docker build First!")
    passwd = export_passwd()
    print(f"Your passwd is \"{passwd}\"")
    print(f"For Testing docker build First!")
    