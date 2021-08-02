from setuptools import setup, find_packages

setup(
    name='app',
    entry_points={
        'console_scripts': ['app=app.app:main']
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)