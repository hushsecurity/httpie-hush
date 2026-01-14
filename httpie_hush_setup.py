#!/usr/bin/env python3
import getpass
import json
import os
import sys

IS_WINDOWS = "win32" in str(sys.platform).lower()
CONF_DIR = str(
    os.getenv(
        "HTTPIE_CONFIG_DIR",
        os.path.expanduser("~/.httpie" if not IS_WINDOWS else r"%APPDATA%\\httpie"),
    )
)
CONF_PATH = os.path.join(CONF_DIR, "config.json")
PROMPT = ">> "


def main():
    print("Welcome to Hush's HTTPie setup")

    print("Please enter your Hush API Key ID:")
    api_key_id = input(PROMPT)
    if not api_key_id.startswith("key-"):
        print("httpie-hush error: invalid API Key ID format (should start with 'key-')")
        sys.exit(1)

    print("Please enter your Hush API Key Secret:")
    api_key_secret = getpass.getpass(PROMPT)

    conf = {"default_options": [f"--auth={api_key_id}:{api_key_secret}"]}
    if not os.path.exists(CONF_DIR):
        os.makedirs(CONF_DIR)
    with open(CONF_PATH, "w") as f:
        json.dump(conf, f, indent=4)
        f.write("\n")

    print("Updated %s successfully" % CONF_PATH)


if __name__ == "__main__":
    main()
