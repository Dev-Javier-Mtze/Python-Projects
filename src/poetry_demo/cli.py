import typer

app = typer.Typer(help="CLI para gestionar Orders")

@app.command()
def list_orders():
    """Listar órdenes"""
    typer.echo("Hello world")
