from setuptools import setup

setup(
   name='snowflake',
   version='1.0',
   description='Draws snowflakes in random colours and on random positions',
   author='Quirin von Rekowski',
   author_email='quirin.von.rekowski@fau.de',
   packages=['snowflake'],  # would be the same as name
   install_requires=['turtle', 'numpy'], #external packages acting as dependencies
)
