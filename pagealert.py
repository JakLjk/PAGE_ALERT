import sys

from page_alert.pagealert import initialize_webapp_and_backed

args_passed_by_user = [arg.lower() for arg in sys.argv[1:]]

expectad_args = {"-init":"Initializes webapp and scripts which check if there are webpages to parse",
                 "-h":"Displays help."}


if __name__ == "__main__":
    if len(args_passed_by_user) == 0:
        print(f"No arguments were passed, [-h for help].")

    if "-h" in args_passed_by_user:
        arg_string ="\n" +"\n".join([f"{key}: {val}" for key, val in expectad_args.items()])
        print(f"""Arguments that can be utilized in this script: {arg_string}""")

    if "-init" in args_passed_by_user:
        initialize_webapp_and_backed()

