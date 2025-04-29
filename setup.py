from setuptools import setup

package_name = 'bridge_cf21'

setup(
name=package_name,
version='0.1.0',
packages=[package_name],
data_files=[
('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
('share/' + package_name, ['package.xml']),
],
install_requires=['setuptools'],
zip_safe=True,
maintainer='dahui',
maintainer_email='dahuilinyang@uma.es',
description='ROS2 python template',
license='Apache License 2.0',
entry_points={
                'console_scripts': [
                        'python_template = python_template.main:main',
                ],
        },
)