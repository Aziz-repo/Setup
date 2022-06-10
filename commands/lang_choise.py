from typing import Set
import typer
import os
from make_structure import global_name # importing the name of the project as a global variable
from enums.cflags import Cflags
from utils.utils import create_main, write_to_makefile
from enums.prog_lang import ProgLang


lang_command = typer.Typer()


@lang_command.command("set")
def language_choise(lang: ProgLang =typer.Option(ProgLang.c.value, "--lang", "-l")):
    if global_name not in os.listdir(): # clause guard
        typer.echo("Project isn't created!! Please create project first!!")
        return 2
    if lang.value == "c":
        # Create the main file in /src directory and write to it
        lang_code = 0
        if create_main(lang_code) != 0:
            print("exit code 2")
            return 2
        # Changing to the project directory
        os.chdir(global_name)
        if "Makefile"  not in os.listdir():
            typer.echo("Makefile is not created!! Please retry or try to create it manually!!")
            return 2
        if write_to_makefile(lang_code) != 0:
            return 2
    else:
        # Create the main file in /src directory and write to it
        lang_code = 1
        if (create_main(lang_code) != 0):
            print("exit code 2")
            return 2
        # Write in the makefile
        if write_to_makefile(lang_code) != 0:
            return 2
    return 0


        
if __name__ == "__main__":
    lang_command()