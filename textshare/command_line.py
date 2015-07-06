import click, textshare, sys

@click.command()
@click.option('--input', '-i', help='uses stdin as input', is_flag=True, default=False)
@click.option('--map', help='returns output as a map of filepaths and url', is_flag=True, default=False)
@click.argument('filepaths', type=click.Path(exists=True), nargs=-1)
def cli(input, map, filepaths):
    if input:
        text = sys.stdin.readlines()
        click.echo(textshare.uploadtext(''.join(text)))
    else:
        if len(filepaths) != 0:
            for fpath in filepaths:
                map_fpath = fpath;
                if not map:
                    map_fpath = ""
                click.echo(map_fpath+" : "+textshare.uploadfile(click.format_filename(fpath)))
        else:
            click.echo('pass atleast one filepath as argument or use -i/--input as an option')
