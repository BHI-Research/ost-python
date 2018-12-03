import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ost-python",
    version="0.0.9",
    autaor="UTN-FRBB",
    author_email="balmacedalm@gmail.com",
    description="Evaluation framework for video summarizations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leanbalma/ost-python",
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': ['ost-python=ost.evaluator_cli:main'],
    },
    install_requires=[
        'opencv-python',
        'h5py',
        'numpy'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
