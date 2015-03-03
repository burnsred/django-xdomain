import os
from distutils.core import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}

setup(
    name='django-xdomain',
    version='0.0.3',
    packages=['xdomain',],
    include_package_data=True,
	package_data=get_package_data('xdomain'),
    license='MIT License',
    author='Michael Bertolacci',
    author_email='michael@burnsred.com.au',
    url='',
    long_description=open('README.md').read(),
)