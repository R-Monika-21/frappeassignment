import click
@click.command("hello_app")
def hello_app():
    click.echo("Hello from the custom command")
commands = [hello_app]
