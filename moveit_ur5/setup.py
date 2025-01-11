from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'moveit_ur5'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (
            os.path.join("share", package_name, "urdf"),
            glob(os.path.join("urdf", "*.urdf*")),
        ),
        (
            os.path.join("share", package_name, "urdf"),
            glob(os.path.join("urdf","*.xacro*")),
        ),
  	(
            os.path.join("share", package_name, "launch"),
            glob(os.path.join("launch", "*.launch*")),
        ),
        (
            os.path.join("share", package_name, "meshes"),
            glob(os.path.join("meshes","*.*")),
        ),
        (
            os.path.join("share", package_name, "rviz"),
            glob(os.path.join("meshes","*.*")),
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kira',
    maintainer_email='kirubel.s.tadesse@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
