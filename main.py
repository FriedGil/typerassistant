import typer
from datetime import datetime
from typing import List

app = typer.Typer()

@app.command()
def note(text:str):
    with open('/home/gilfr/assistant/notes.txt', 'a+') as f:
        f.write( f"{text} || Date: {datetime.now()} \n")

@app.command()
def rnotes():
    with open('/home/gilfr/assistant/notes.txt', 'r') as f:
        color = None
        for line in f.readlines():
            color = typer.colors.MAGENTA if color != typer.colors.MAGENTA else typer.colors.YELLOW
            typer.secho(line,fg=color)

@app.command()
def cnotes():
    with open('/home/gilfr/assistant/notes.txt','w') as f:
        f.close()

@app.command()
def dnotes(indices: List[int]):
    with open("/home/gilfr/assistant/notes.txt", 'r') as f:
        lines = f.readlines()
    with open("/home/gilfr/assistant/notes.txt", "w") as f:
        for number, line in enumerate(lines):
            if number not in indices:
                f.write(line)

@app.command()
def time():
    typer.echo(datetime.now())

if __name__ == "__main__":
    app()