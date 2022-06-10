from typing import Optional
import typer
import os
from utils.utils import build_hiarchy

create_command = typer.Typer()

# TODO: write the docs for every componenent in the app
@create_command.command("project")
def make_struct(name: str = typer.Option("project","--name", "-n"), verbose: bool=typer.Option(False, "--verbose", "-v")) -> int:
    global global_name
    global_name = name
    dir = os.getcwd()
    subdirs_to_create = ["src", "bin", "obj"]
    file_to_create = "Makefile"
    project_directory = os.path.join(dir,name)
    # build hiarchy
    if build_hiarchy(project_directory, subdirs_to_create, file_to_create, verbose) == 0:
        return 0
    typer.echo("exit code 1")
    return 1

if __name__ == "__main__":
    create_command()




