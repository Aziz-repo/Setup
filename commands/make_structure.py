from typing import Optional
import typer
import os
from utils.utils import build_hiarchy

app = typer.Typer()

# TODO: write the docs for every componenent in the app
@app.command("create")
def make_struct(name: str = typer.Option("project","--name", "-n"), verbose: bool=typer.Option(False, "--verbose", "-v")) -> int:
    dir = os.getcwd()
    subdirs_to_create = ["src", "bin", "obj"]
    file_to_create = "Makefile"
    project_directory = os.path.join(dir,name)
    # build hiarchy
    if build_hiarchy(project_directory, subdirs_to_create, file_to_create, verbose) == 0:
        return 0
    typer.echo("exit code 1")
    return 1




