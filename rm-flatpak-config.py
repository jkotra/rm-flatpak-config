import os
import tarfile
import time
from typing import List

FLATPAK_SYSTEM_CONFIG_PATH = ""
FLATPAK_USER_CONFIG_PATH = ""

def list_configs() -> List[str]:
    user_configs = [path for path in os.listdir(FLATPAK_USER_CONFIG_PATH)]
    return user_configs

def delete() -> bool:
    pass

def backup() -> bool:
    pass

if __name__ == "__main__":
    pass