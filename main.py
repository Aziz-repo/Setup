import typer
import os
from utils.utils import build_hiarchy
from utils.utils import create_main
from enums.prog_lang import ProgLang

app = typer.Typer()

# TODO: write the docs for every componenent in the app
@app.command("create")
def make_structure(name: str, verbose: bool=False) -> int:
    dir = os.getcwd()
    subdirs_to_create = ["src", "bin", "obj"]
    file_to_create = "Makefile"
    project_directory = os.path.join(dir,name)
    # build hiarchy
    if build_hiarchy(project_directory, subdirs_to_create, file_to_create, verbose) == 0:
        return 0
    print("exit code 1")
    return 1

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

