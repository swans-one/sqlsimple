import re
from setuptools import setup, find_packages


def get_version():
    """
    Extracts the version number from the version.py file.
    """
    VERSION_FILE = '{{ project_name }}/version.py'
    mo = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', open(VERSION_FILE, 'rt').read(), re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError('Unable to find version string in {0}.'.format(VERSION_FILE))

install_requires = [
]
tests_require = [
    'coverage>=4.0',
    'flake8>=2.2.0',
    'mock>=1.0.1',
    'nose>=1.3.0'
]
extras_require = {
    'test': tests_require,
    'packaging': ['wheel'],
}

everything = set(install_requires)
for deps in extras_require.values():
    everything.update(deps)
extras_require['all'] = list(everything)

setup(
    name='sqlsimple',
    version=get_version(),
    description='Manage a project with a database, by just writing SQL.',
    long_description=open('README.rst').read(),
    url='https://github.com/Wilduck/sqlsimple',
    author='Erik Swanson',
    author_email='theerikswanson@gmail.comcom',
    keywords='',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license='MIT',
    include_package_data=True,
    test_suite='nose.collector',
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    zip_safe=False,
)
