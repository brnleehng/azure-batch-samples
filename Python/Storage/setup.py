import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('blobxfer.py', 'r') as fd:
    version = re.search(
        r'^_SCRIPT_VERSION\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(), re.MULTILINE).group(1)

with open('README.rst') as readme:
    long_description = ''.join(readme).strip()

setup(
    name='blobxfer',
    version=version,
    author='Microsoft Corporation, Azure Batch and HPC Team',
    author_email='',
    description='Azure Blob storage transfer tool with AzCopy-like features',
    long_description=long_description,
    platforms='any',
    url='https://github.com/Azure/azure-batch-samples/Python/Storage',
    license='MIT',
    py_modules=['blobxfer'],
    entry_points={
        'console_scripts': 'blobxfer=blobxfer:main',
    },
    install_requires=[
        'azure-common==1.1.1',
        'azure-storage==0.30.0',
        'azure-servicemanagement-legacy==0.20.2',
        'cryptography>=1.3',
        'requests==2.9.1'
    ],
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ],
    keywords='azcopy azure storage blob transfer copy',
)
