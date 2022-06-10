from typing import Optional, Set, Tuple
import typer
import os
from commands import make_structure
from enums.cflags import Cflags
from utils.utils import add_source_file, create_main, write_to_makefile, makefile_debug
from enums.prog_lang import ProgLang
from enums.cflags import Cflags
from enums.compiler import Compiler


lang_command = typer.Typer()

# FIXME fix the glabal variable project_name

@lang_command.command("set")
def language_choise(lang: ProgLang =typer.Option(ProgLang.c.value, "--lang", "-l", help="development language used"),
                    source_file :Optional[Tuple[str,str,str]] = typer.Option(Tuple[None], "--source", "-s", help="add source file. Maximum 3"),
                    verbose:bool=typer.Option(False, "--verbose","-v")) -> int:

    if make_structure.make_struct.project_name not in os.listdir(): # clause guard
        typer.echo("Project isn't created!! Please create project first!!")
        return 2
    # TODO: change the hole structure to one function
    if lang.value == "c":
        # Create the main file in /src directory and write to it
        lang_code = 0
        if create_main(lang_code) != 0:
            print("Error: couldn't create main file")
            return 2
        if verbose:
            typer.echo("main file is created!!")
        # Changing to the project directory
        os.chdir(make_structure.make_struct.project_name)
        if "Makefile"  not in os.listdir():
            typer.echo("Makefile is not created!! Please retry or try to create it manually!!")
            return 2
        if write_to_makefile(lang_code) != 0:
            typer.echo("Error: Couldn't create Makefile")
            return 2
        if verbose:
            typer.echo(f"Makefile is created under /{make_structure.make_struct.project_name}")
        if source_file != Tuple[None]:
            if add_source_file(make_structure.make_struct.project_name, source_file, lang_code) != 0 :
                typer.echo("Error: Couldn't create source files!")
                return 2
            if verbose:
                typer.echo("Source files is created")
    else:
        # Create the main file in /src directory and write to it
        lang_code = 1
        if create_main(lang_code) != 0:
            print("exit code 2")
            return 2
        if verbose:
            typer.echo(f"main file is created under /{make_structure.make_struct.project_name}/src")
        # Write in the makefile
        os.chdir(make_structure.make_struct.project_name)
        if "Makefile"  not in os.listdir():
            typer.echo("Makefile is not created!! Please retry or try to create it manually!!")
            return 2
        if write_to_makefile(lang_code) != 0:
            return 2
        if verbose:
            typer.echo(f"Makefile is created under /{make_structure.make_struct.project_name}")
        if source_file != Tuple[None]:
            if add_source_file(make_structure.make_struct.project_name, source_file, lang_code) != 0 :
                typer.echo("Error: Couldn't create source files!")
                return 2
            if verbose:
                typer.echo("Source files is created")
    return 0

@lang_command.command("debug")
# TODO: tweaking the compiling flag -> set a list of flags
def compilation(compiler: Compiler=typer.Option(...,"--compiler", "-c", help="compiler to use"), 
                debuger: Cflags=typer.Option(..., "--debuger", "-d", help= "flags passed to the compiler"),
                verbose: bool=typer.Option(False, "--verbose", "-v")
                ) -> int:
    os.chdir(make_structure.make_struct.project_name)
    if "Makefile" not in os.listdir():
        typer.print("Makefile doesn't exist!!")
        return 1
    if (makefile_debug(compiler, debuger)) == 0 and verbose:
        typer.echo("Makefile variables is done setting...")
    
         



        
if __name__ == "__main__":
    lang_command()