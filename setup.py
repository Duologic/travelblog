from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession

import os


# Lists of requirements and dependency links which are needed during runtime, testing and setup
install_requires = []
tests_require = []
setup_requires = []
dependency_links = []
#
# Inject requirements from requirements.txt into setup.py
requirements_file = parse_requirements(os.path.join('deployment', 'requirements.txt'), session=PipSession())
for req in requirements_file:
    install_requires.append(str(req.req))
    if req.link:
        dependency_links.append(str(req.link))

## Inject test requirements from requirements_test.txt into setup.py
#requirements_test_file = parse_requirements(os.path.join('deployment', 'requirements_test.txt'), session=PipSession())
#for req in requirements_test_file:
#    tests_require.append(str(req.req))
#    if req.link:
#        dependency_links.append(str(req.link))
#
## Inject setup requirements from requirements_setup.txt into setup.py
#requirements_setup_file = parse_requirements(os.path.join('deployment', 'requirements_setup.txt'), session=PipSession())
#for req in requirements_setup_file:
#    setup_requires.append(str(req.req))
#    if req.link:
#        dependency_links.append(str(req.link))


setup(
    name='travelblog',
    version='0.0.1',
    url='',
    license='commercial',
    description='',
    long_description=open('README.md', 'r').read(),
    author='Jeroen Op \'t Eynde',
    packages=find_packages('.'),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=setup_requires,
    dependency_links=dependency_links,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
