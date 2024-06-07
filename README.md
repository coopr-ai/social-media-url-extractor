# Social Media URL Extractor

## Overview

The Social Media URL Extractor is a Python module that extracts social media URLs from a given webpage. It supports multiple social media platforms and can be used both as a module in your Python projects or as a command-line tool.

## Features

- Extracts URLs for various social media platforms such as Facebook, Twitter, LinkedIn, Instagram, YouTube, Pinterest, TikTok, Reddit, Snapchat, Tumblr, Medium, GitHub, Flickr, VK, Vimeo, Dailymotion, and Quora.
- Configurable patterns through a YAML file.
- Can be used as a Python module or a command-line tool.
- Optional debug mode for detailed logging.

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/social-media-url-extractor.git
   cd social-media-url-extractor

2. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the dependencies:
    pip install -r requirements.txt

4. Install the package in editable mode:
    pip install -e .

## Usage

As a Command-Line Tool
Run the tool with a URL and an optional configuration file:

extract-social-media-urls https://www.example.com --config=src/social_media_url_extractor/config.yaml
Enable debug mode for detailed logging:
extract-social-media-urls https://www.example.com --config=src/social_media_url_extractor/config.yaml --debug

# As a Python Module
Import the module and create an instance of SocialMediaURLExtractor:

from social_media_url_extractor import SocialMediaURLExtractor
extractor = SocialMediaURLExtractor(config_path='src/social_media_url_extractor/config.yaml')
urls = extractor.extract_urls('https://www.example.com')
for platform, links in urls.items():
    if links:
        print(f'{platform.capitalize()}:')
        for link in links:
            print(f'  - {link}')

# Configuration
The URL patterns for different social media platforms are specified in a YAML configuration file. Here is an example config.yaml:

patterns:
  facebook:
    - "https?://(www\\.)?facebook\\.com/profile\\.php\\?id=[0-9]+/?"
    - "https?://(www\\.)?facebook\\.com/[a-zA-Z0-9_\\-\\.]+/?"
    - "https?://(www\\.)?fb\\.com/[a-zA-Z0-9_\\-\\.]+/?"
  twitter:
    - "https?://(www\\.)?twitter\\.com/[a-zA-Z0-9_\\-]+/?"
    - "https?://(www\\.)?x\\.com/[a-zA-Z0-9_\\-]+/?"
  linkedin:
    - "https?://(www\\.)?linkedin\\.com/in/[a-zA-Z0-9_\\-]+/?"
    - "https?://(www\\.)?linkedin\\.com/company/[a-zA-Z0-9_\\-]+/?"
    - "https?://(www\\.)?linkedin\\.com/school/[a-zA-Z0-9_\\-]+/?"
  instagram:
    - "https?://(www\\.)?instagram\\.com/[a-zA-Z0-9_\\-\\.]+/?"
  youtube:
    - "https?://(www\\.)?youtube\\.com/[a-zA-Z0-9_\\-]+/?"
    - "https?://(www\\.)?youtube\\.com/c/[a-zA-Z0-9_\\-]+/?"
    - "https?://(www\\.)?youtube\\.com/@[a-zA-Z0-9_\\-]+/?"
  pinterest:
    - "https?://(www\\.)?pinterest\\.com/[a-zA-Z0-9_\\-]+/?"
    - "https?://in\\.pinterest\\.com/[a-zA-Z0-9_\\-]+/?"
  tiktok:
    - "https?://(www\\.)?tiktok\\.com/@[a-zA-Z0-9_\\-\\.]+/?"
  reddit:
    - "https?://(www\\.)?reddit\\.com/user/[a-zA-Z0-9_\\-]+/?"
    - "https?://(www\\.)?reddit\\.com/r/[a-zA-Z0-9_\\-]+/?"
  snapchat:
    - "https?://(www\\.)?snapchat\\.com/add/[a-zA-Z0-9_\\-\\.]+/?"
  tumblr:
    - "https?://(www\\.)?[a-zA-Z0-9_\\-]+\\.tumblr\\.com/?"
  medium:
    - "https?://(www\\.)?medium\\.com/@[a-zA-Z0-9_\\-\\.]+/?"
  github:
    - "https?://(www\\.)?github\\.com/[a-zA-Z0-9_\\-\\.]+/?"
  flickr:
    - "https?://(www\\.)?flickr\\.com/photos/[a-zA-Z0-9_\\-]+/?"
  vk:
    - "https?://(www\\.)?vk\\.com/[a-zA-Z0-9_\\-]+/?"
  vimeo:
    - "https?://(www\\.)?vimeo\\.com/[a-zA-Z0-9_\\-]+/?"
  dailymotion:
    - "https?://(www\\.)?dailymotion\\.com/[a-zA-Z0-9_\\-]+/?"
  quora:
    - "https?://(www\\.)?quora\\.com/profile/[a-zA-Z0-9_\\-]+/?"

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Contributing
Contributions are welcome! Please feel free to submit a Pull Request.




