from setuptools import setup, find_packages

setup(
    name='embrace',
    version='0.0.2',
    url='',
    license='PROPRIETARY',
    author='Sathish Kumar',
    author_email='sathish.cres07@gmail.com',
    description='handle customized API',
    long_description="None",
    packages=find_packages(),
    package_dir={
        'embrace_app': 'embrace_app'
    },
    install_requires=[
        'flask >=0.10',
        'Flask-SQLAlchemy',
        'bumpversion',
        'factual-api',
        'requests',
        'pytest',
        'flask-restful',
    ],
    tests_require=[
        'mock',
    ],
    classifiers=[],
)
