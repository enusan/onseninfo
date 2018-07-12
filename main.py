import click
import onsenInfo

@click.group()
def main():
    """onsen.ag tool"""

@main.command()
def list():
    """
    Show the list of radio id
    """
    onsenInfo.get_id_list()

@main.command()
@click.argument('radio_id')
def info(radio_id):
    """
    Show the information of radio
    """
    onsenInfo.get_radio_info(radio_id)

@main.command()
@click.argument('radio_id')
def down(radio_id):
    """
    Download radio mp3 file
    """
    onsenInfo.get_mp3(radio_id)



if __name__ == '__main__':
    main()