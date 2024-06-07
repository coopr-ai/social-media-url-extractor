import hrequests
from bs4 import BeautifulSoup
import yaml
import re
import logging

class SocialMediaURLExtractor:
    def __init__(self, config_path='src/social_media_url_extractor/config.yaml', debug=False):
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
            self.patterns = config['patterns']
        
        # Set up logging
        self.logger = logging.getLogger(__name__)
        if debug:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)

    def extract_urls(self, url):
        self.logger.info(f"Extracting URLs from: {url}")
        response = hrequests.get(url)
        if response.status_code != 200:
            self.logger.error(f"Failed to retrieve the page: {response.status_code}")
            return {}
        
        soup = BeautifulSoup(response.text, 'html.parser')
        urls = {platform: [] for platform in self.patterns}

        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            self.logger.debug(f"Found link: {href}")
            for platform, patterns in self.patterns.items():
                for pattern in patterns:
                    if re.match(pattern, href):
                        self.logger.debug(f"Match found: {href} for platform {platform}")
                        urls[platform].append(href)
        
        # Create a beautiful report
        report = self._create_report(urls)
        self.logger.info("\n" + report)
        return urls
    
    def _create_report(self, urls):
        report_lines = ["Social Media URLs found:"]
        for platform, links in urls.items():
            if links:
                report_lines.append(f"\n{platform.capitalize()}:")
                for link in links:
                    report_lines.append(f"  - {link}")
        return "\n".join(report_lines)

