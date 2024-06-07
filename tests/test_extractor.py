import unittest
from social_media_url_extractor import SocialMediaURLExtractor

class TestSocialMediaURLExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = SocialMediaURLExtractor(config_path='src/social_media_url_extractor/config.yaml')
    
    def test_extract_urls(self):
        url = 'https://example.com'
        result = self.extractor.extract_urls(url)
        self.assertIsInstance(result, dict)
        for platform in result:
            self.assertIsInstance(result[platform], list)

if __name__ == '__main__':
    unittest.main()
