from setuptools import setup
import os
from glob import glob

package_name = 'turtle_shapes'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='your@email.com',
    description='Draws square, triangle, and star using turtlesim',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'shapes = turtle_shapes.shape_drawer:main',
        ],
    },
)
