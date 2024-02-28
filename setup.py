from setuptools import setup, find_packages

import glob
import os

# curr_path = os.path.dirname(os.path.realpath(__file__))
# select all folders in the current directory
# folders = [f for f in glob.glob(f"{curr_path}/")]

setup(
    name='stable_kp',
    version='0.1.0',
    description='Description of your package',
    include_package_data=False,
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        # "tcl.sclip": ["*.txt.gz"]
    },
    install_requires=[
        # List your project dependencies here
    ],
    packages=find_packages(),
    package_dir={'skey':"unsupervised_keypoints"},
)