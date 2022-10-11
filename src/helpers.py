import inquirer


def show_input_choices(choices: list) -> str:
    questions = [
        inquirer.List("profile",
                      message="Select aws profile",
                      choices=choices
                      ),
    ]

    return inquirer.prompt(questions)["profile"]
