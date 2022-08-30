from setuptools import setup
import re

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

version = ''
with open('azauthpy/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

readme = ''
with open('README.MD') as f:
    readme = f.read()

setup(
    name='azauthpy',
    version=version,    
    author='AktiCube',
    author_email='contact@akticube.fr',
    license='MIT',
    description='A python library for your Azuriom website authentication  API',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/AktiCube/AzAuthPY',
    packages=['azauthpy'],
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.8",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
      ]
)