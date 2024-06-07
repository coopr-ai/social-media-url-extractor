import click
from .extractor import SocialMediaURLExtractor

@click.command()
@click.argument('url')
@click.option('--config', default='src/social_media_url_extractor/config.yaml', help='Path to the config file.')
@click.option('--debug', is_flag=True, help='Enable debug mode for detailed logging.')
def extract(url, config, debug):
    extractor = SocialMediaURLExtractor(config_path=config, debug=debug)
    urls = extractor.extract_urls(url)
    for platform, links in urls.items():
        if links:
            click.echo(f'{platform.capitalize()}:')
            for link in links:
                click.echo(f'  - {link}')

if __name__ == '__main__':
    extract()
