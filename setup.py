from setuptools import setup

setup(
    name="prompt-injection",
    version="1.0",
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "play = main:main",
        ],
    },
)
