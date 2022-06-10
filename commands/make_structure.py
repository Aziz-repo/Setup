from typing import Optional, Tuple
import typer
import os
from utils.utils import *

create_command = typer.Typer()

# TODO: write the docs for every componenent in the app
@create_command.command("project")
def make_struct(name: str = typer.Option("project","--name", "-n",help="project name"),
                header_file: Optional[Tuple[str,str,str]] = typer.Option(Tuple[None], "--headers", "-o", help="add header files. Maximum 3"),
                verbose: bool=typer.Option(False, "--verbose", "-v")) -> int:
    global project_name
    project_name = name
    dir = os.getcwd()
    subdirs_to_create = ["src", "bin", "obj"]
    file_to_create = "Makefile"
    project_directory = os.path.join(dir,name)
    # build hiarchy
    if build_hiarchy(project_directory, subdirs_to_create, file_to_create, verbose) == 0:
        return 0
    typer.echo("exit code 1")

    # create source and header files if provided
    if header_file != Tuple[None]:
        if add_header_file(project_directory, header_file) != 0:
            typer.echo("Error: Header files couldn't be created!")

    return 1

if __name__ == "__main__":
    create_command()




