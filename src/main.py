import subprocess
import configparser

import helpers as h
import constants as c

def get_profile_credentials()-> dict:
    config = configparser.RawConfigParser()
    config.read(c.AWS_CONFIG_FILE_PATH)

    selected_profile = h.show_input_choices(config.sections())

    credentials = {
        "key_id": config.get(selected_profile, 'aws_access_key_id'),
        "secret_id": config.get(selected_profile, 'aws_access_key_id')
    }

    return credentials

def run_aws_configure(aws_key: str, aws_secret: str):
    subprocess.run(f"aws configure set aws_access_key_id {aws_key}", stderr=subprocess.PIPE, shell=True, check=True, text=True)
    subprocess.run(f"aws configure set aws_secret_access_key {aws_secret}", stderr=subprocess.PIPE, shell=True, check=True, text=True)


def main():
    credentials = get_profile_credentials()
    print(credentials)
    

if __name__ == "__main__":
    main()