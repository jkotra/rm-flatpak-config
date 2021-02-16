#!/usr/bin/env python

import os
import time
from typing import List
import argparse
import shutil
import subprocess

parser = argparse.ArgumentParser(
    description='rm-flatpak-config - Remove config files of flatpak applications!')

parser.add_argument('--debug','-D', action='store_true', dest="debug")
parser.add_argument('--version','-v', action='store_true', dest="version")

args = parser.parse_args()

FLATPAK_USER_CONFIG_PATH = os.path.expanduser("~") + "/.var/app/"

def show_version():
    print("rm-flatpak-config v0.3")
    flatpak_v = subprocess.run(["flatpak", "--version"])
    exit(flatpak_v.returncode)

def list_configs() -> List:
    config_files = []
    config_files += [(FLATPAK_USER_CONFIG_PATH, path, "user")
                     for path in os.listdir(FLATPAK_USER_CONFIG_PATH)]

    return config_files


def delete(config_dir):
    if args.debug:
        print("[DEBUG] Deleting", config_dir)
        shutil.rmtree(config_dir)


if __name__ == "__main__":

    if args.version:
        show_version()

    conf_files = list_configs()

    index = 0
    BOLD = '\033[1m'
    END = '\033[0m'

    print(BOLD, 'SNO\t', "Application ID", END)
    for _, d, t in conf_files:
        print(index, '\t', d.center(10), "({})".format(t))
        index += 1
    prompt = "\nChoose [0-{}]:".format(len(conf_files))
    user_choice = input(prompt)
    if args.debug:
        print("[DEBUG] user_choice = ", user_choice)

    try:
        user_choice = conf_files[int(user_choice)]
    except IndexError:
        print("no such thing exists!")
        exit(1)

    delete(os.path.join(user_choice[0], user_choice[1]))