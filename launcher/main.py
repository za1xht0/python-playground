import subprocess
import sys

projects = {
    "1": {
        "name": "Calculator",
        "path": "./beginner/calc/calculator.py"
    },
    "2": {
        "name": "Dice Roll",
        "path": "./beginner/dice_roll/dice_roll.py"
    },
    "3": {
        "name": "Guess the Number",
        "path": "./beginner/guess_number/guess.py"
    },
    "4": {
        "name": "Magic Ball",
        "path": "./beginner/magic_ball/magic.py"
    },
    "5": {
        "name": "Paper Rock Scissors",
        "path": "./beginner/paper_rock_scissors/prc.py"
    },
    "6": {
        "name": "Password Generator",
        "path": "./beginner/password_generator/pass.py"
    },
    "7": {
        "name": "To-Do List",
        "path": "./beginner/to-do-list/todo.py"
    },
    "8": {
        "name": "Unit Converter",
        "path": "./beginner/unit_converter/unit_con.py"
    },
    "9": {
        "name": "Username Generator",
        "path": "./beginner/username_generator/username.py"
    },
    "10": {
        "name": "Configuration Validator",
        "path": "./devops/conf_valid/conf_valid.py"
    },
    "11": {
        "name": "Server Health Checker",
        "path": "./devops/server_health_checker/shc.py"
    },
    "12": {
        "name": "Server Diff",
        "path": "./devops/server_diff/server_diff.py"
    }
}

def get_choose():
    choose = input('Select project:')
    if choose in projects:
        return choose
    elif choose == '0':
        return choose
    else:
        return None

def menu():
    print('\n╔══════════════════════════════════════╗\n║          PYTHON PLAYGROUND           ║\n╚══════════════════════════════════════╝\n')
    print('[Beginner]\n\n1. Calculator\n2. Dice roll\n3. Guess the number\n4. Magic ball\n5. Paper-Rock-Scissors\n6. Password generator\n7. To-Do List\n8. Unit converter\n9. Username generator\n\n[DevOps]\n\n10. Server Health Checker\n11. Configuration Validator\n12. Server diff\n\n0. Exit')
    choose = get_choose()
    if choose == '0':
        return False
    elif choose is None:
        print('Invalid option')
        return True
    else:
        project = projects[choose]["path"]
        subprocess.run([sys.executable, project])
        return True
while True:
    if not menu():
        break


