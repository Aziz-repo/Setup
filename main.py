import typer

import make_structure
import lang_choise


app = typer.Typer()

app.add_typer(make_structure.app, name="create")
app.add_typer(lang_choise.app, name="lang")


if __name__=="__main__":
    app()