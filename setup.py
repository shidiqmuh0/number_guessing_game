from setuptools import setup, find_packages

setup(
    name='game_tebak_angka',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'number-guessing-game = number_guessing_game.game:guess_number',
        ],
    },
    author='shidiq',
    author_email='shidiqmuh0@gmail.com',
    description='A simple number guessing game package',
    url='https://github.com/shidiqmuh0/number_guessing_game.git',
)