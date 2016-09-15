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
        'sqlalchemy >=1.0,<1.1',
        'python-dateutil >=2.5,<2.6',
        'psycopg2 <=2.6',
        'flask',
        'Flask-SQLAlchemy',
        'bumpversion',
        'uwsgi <=2.0',
        'factual-api',
        'requests',
        'pytest',
        'pytest-cov',
        'pytest-mock',
        'pytest-capturelog',
    ],
    tests_require=[
        'mock',
    ],
    classifiers=[],
)
