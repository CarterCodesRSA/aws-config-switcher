# aws-config-switcher

Python script used to read/select/change the users current terminal sessions `aws profile`.

## Background

There are situations where an AWS Programmatic user is required to be the "owner" of a given AWS resource.

Prime example being AWS EKS:
>When an Amazon EKS cluster is created, the IAM entity (user or role) that creates the cluster is permanently added to the Kubernetes RBAC authorization table as the administrator. This entity has system:masters permissions.

This script allows for the users `~/.aws/config` file to read as an input, from there, the user can select a listed profile.

# How to run
Simply install the required packages
```bash
pip3 install -r requirements.txt 
```

Update the file path to your aws config file:
```bash
AWS_CONFIG_FILE_PATH="/Users/my-computer/.aws/config"
```

Then run the script:
```bash
python3 ./src/main.py
```