import subprocess
import configparser

import helpers as h
import constants as c


def get_profile_credentials() -> dict:
    config = configparser.RawConfigParser()
    config.read(c.AWS_CONFIG_FILE_PATH)

    if len(config.sections()) == 0:
        raise Exception("No profiles found, ensure correct file path is given")
    else:
        selected_profile = h.show_input_choices(config.sections())

    credentials = {
        "key_id": config.get(selected_profile, "aws_access_key_id"),
        "secret_id": config.get(selected_profile, "aws_secret_access_key")
    }

    return credentials


def run_aws_configure(key_id: str, secret_id: str):
    subprocess.run(f"aws configure set aws_access_key_id {key_id}",
                   stderr=subprocess.PIPE, 
                   shell=True, 
                   check=True, 
                   text=True)
    subprocess.run(f"aws configure set aws_secret_access_key {secret_id}",
                   stderr=subprocess.PIPE,
                   shell=True,
                   check=True,
                   text=True)


def main():
    if c.AWS_CONFIG_FILE_PATH == "":
        raise Exception("Config path cannot be empty")

    credentials = get_profile_credentials()
    run_aws_configure(credentials["key_id"], credentials["secret_id"])


if __name__ == "__main__":
    main()
