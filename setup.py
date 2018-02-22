from distutils.core import setup

setup(
    name = 'ohbotWin',
    packages = ['ohbotWin'],
    package_data={'': ['MotorDefinitionsv21.omd','Silence1.wav']},
    include_package_data=True,
    version = '1.11',  
    description = 'description',
    author = 'ohbot',
    author_email = 'info@ohbot.co.uk',
    url = 'https://github.com/ohbot/ohbotWin-python',
    download_url = 'https://github.com/ohbot/ohbotWin-python/archive/1.11.tar.gz',
    keywords = ['ohbot', 'robot'],
    classifiers = [],
    install_requires=[
          'pyserial','comtypes',
      ],
)
