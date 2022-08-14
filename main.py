import typer
from commands import create_command, lang_command
app = typer.Typer()

app.add_typer(typer_instance=create_command, name="create")
app.add_typer(typer_instance=lang_command, name="lang")

# TODO: add a callback to the CLI indicate what's going on!!!


if __name__== "__main__":
    app()
