from distutils.core import setup

requires = ['geocoder', 'pyowm', 'Adafruit_CharLCD']
setup(
  name = 'iwPiWeather',
  packages = ['iwPiWeather'],
  version = '0.1',
  license = 'gpl-3.0',
  description = 'Gets your weather data for a 16x2 display on raspberry pi',
  author = 'Dejan Roshkovski',
  author_email = 'dejan.roshkovski@interworks.com.mk',
  url = 'https://github.com/dejanr92/iwPyWeather',
  download_url = 'https://github.com/dejanr92/iwPyWeather/archive/v_01.tar.gz',
  keywords = ['RaspberryPi', 'LCD display', '16x2', 'Pi'],   # Keywords that define your package best
  install_requires=[
          'geocoder',
          'pyowm',
          'Adafruit_CharLCD'
      ],
  package_dir={'iwPiWeather': 'iwPiWeather'},
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3.0',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)