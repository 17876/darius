import setuptools

setuptools.setup(
    name="dash",
    version="1.0",
    author="Anton Wassiljew",
    author_email="anton@hwassiljew.online",
    description="tools for composing time-based objects",
    url="https://github.com/17876/dash.git",
    packages=setuptools.find_packages(),
    install_requires=['setuptools==49.2.0'
                      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
