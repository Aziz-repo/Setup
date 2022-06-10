from typing import Set
import typer
import click
from enums.cflags import Cflags
from utils.utils import create_main, write_to_makefile
from enums.prog_lang import ProgLang
from enums.compiler import Compiler


lang_command = typer.Typer()


@lang_command.command("lang")
@click.option("--lang", "-l", help="development language")
@click.option("--compiler", "-c", help="compiler to be used")
def language_choise(lang: ProgLang = ProgLang.c.value, compiler: Compiler=typer.Option(...,"--compiler", "-c")):
    # TODO: verify if the project is created

    if lang.value == "c":
        # Create the main file in /src directory and write to it
        lang_code = 0
        if create_main(lang_code) != 0:
            print("exit code 2")
            return 2
        # Write in the makefile
        write_to_makefile(lang_code, compiler.value)
        pass
    else:
        # Create the main file in /src directory and write to it
        lang_code = 1
        if (create_main(lang_code) != 0):
            print("exit code 2")
            return 2
        # Write in the makefile
        write_to_makefile(lang_code, compiler.value)
        
if __name__ == "__main__":
    lang_command()