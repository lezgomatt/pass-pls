import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="pass-pls",
    version="0.0.1",
    description="A simple ssh-askpass implementation using GTK",
    url="https://github.com/undecidabot/pass-pls",
    author="Matt",
    author_email="undecidabot@gmail.com",
    license="Zlib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Environment :: X11 Applications :: GTK",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: zlib/libpng License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Security",
        "Topic :: System :: Networking",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    py_modules=["pass_pls"],
    python_requires=">=3.6",
    install_requires=[
        "PyGObject",
    ],
    entry_points = {
        'console_scripts': ['pass-pls=pass_pls:main'],
    },
)
