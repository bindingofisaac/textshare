import click, textshare, os

@click.command()
@click.option('--input', '-i', help='uses stdin as input', is_flag=True, default=False)
@click.argument('filepaths', type=click.Path(exists=True), nargs=-1)
def cli(input, filepaths):
    if input:
        pass
    else:
        if len(filepaths) != 0:
            for fpath in filepaths:
                click.echo(textshare.uploadfile(click.format_filename(fpath)))
        else:
            click.echo('pass atleast one filepath as argument or use -i/--input as an option')
