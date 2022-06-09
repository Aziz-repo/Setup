import typer
from utils.utils import create_main
from enums.prog_lang import ProgLang


app = typer.Typer()


@app.command("lang")
def language_choise(lang: ProgLang = ProgLang.c.value):
    # set the directory to work with
    
    if lang.value == "C":
        # TODO: create the main file in /src directory and write to it
        lang_code = 0
        if create_main(lang_code) != 0:
            print("exit code 2")
            return 2
        # TODO: Write in the makefile
        pass
    else:
        # TODO: create the main file in /src directory and write to it
        lang_code = 1
        if (create_main(lang_code) != 0):
            print("exit code 2")
            return 2
        # TODO: write in the makefile
        pass

if __name__ == "__main__":
    app()