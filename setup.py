from setuptools import setup


_readme = 'README.md'

with open('.env', 'r') as f:
    line = f.readline()
    if line.startswith('PACKAGE='):
        _package = line.splitlines()[0].split('=')[1].lower()

with open(_readme, 'r') as f:
    long_description = f.read()

required = []
with open(_package+'/requirements.txt', 'r') as f:
    required = [line.splitlines()[0] for line in f]
# hack to handle diff between pip and conda 'redis' package name
if any('redis' in s for s in required):
    from sys import argv as sys_argv
    if 'bdist_conda' in sys_argv:
        for i,elt in enumerate(required):
            if 'redis' in elt:
                required[i] = required[i].replace('redis', 'redis-py')


_release = 'RELEASE'
# extra_files={
#     'release': (_package, [_package+'/doc/'+_release])
# }

# with open(extra_files['release'][1][0], 'r') as f:
with open(_release, 'r') as f:
    _version = f.readline().split()[0]

setup(
    name=_package,
    version=_version,
    author='Melchior du Lac, Joan Hérisson',
    author_email='joan.herisson@univ-evry.fr',
    description='BRSynth Utilities',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/brsynth/CRedisDict',
    packages=[_package],
    # package_dir={_package: _package},
    install_requires=required,
    tests_require=required,
    test_suite='pytest',
    package_data={_package: ['requirements.txt']},
#    include_package_data=True,
#    data_files=[v for v in extra_files.values()],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
)
