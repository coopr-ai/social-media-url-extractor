from setuptools import setup, find_packages

setup(
    name='social-media-url-extractor',
    version='0.1.0',
    description='A module to extract social media URLs from HTML',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/social-media-url-extractor',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'beautifulsoup4',
        'pyyaml',
        'click'
    ],
    entry_points={
        'console_scripts': [
            'extract-social-media-urls=social_media_url_extractor.cli:extract',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
