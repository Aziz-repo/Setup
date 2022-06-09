import typer

import commands

app = typer.Typer()

app.add_typer(typer_instance=commands.make_structure.app, name="create", help="Create the project structure")
app.add_typer(typer_instance=commands.lang_choise.app, name="lang", help="Pick C or Cpp language")

# TODO: add a callback to the CLI indicate what's going on!!!


if __name__== "__main__":
    app()