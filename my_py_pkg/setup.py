from setuptools import find_packages, setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='drwnnns',
    maintainer_email='drwnnns@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_first_node = my_py_pkg.my_first_node:main',
            'my_second_node = my_py_pkg.my_second_node:main',
            'templete = my_py_pkg.templete:main',
            'string_publisher_node1 = my_py_pkg.string_publisher_node1:main',
            'string_publisher_node2 = my_py_pkg.string_publisher_node2:main',
            'twist_pub_node = my_py_pkg.twist_pub_node:main',
            'string_subscriber_node1 = my_py_pkg.string_subscriber_node1:main',
            'string_subscriber_node2 = my_py_pkg.string_subscriber_node2:main',
            'joy_subscriber_node = my_py_pkg.joy_subscriber_node:main',
            'twist_joy_node1 = my_py_pkg.twist_joy_node1:main',
            'twist_joy_node2 = my_py_pkg.twist_joy_node2:main',
            'twist_joy_node3 = my_py_pkg.twist_joy_node3:main',
            'add_two_ints_server = my_py_pkg.add_two_ints_server:main',
            'add_two_ints_client_no_oop = my_py_pkg.add_two_ints_client_no_oop:main',
            'add_two_ints_client = my_py_pkg.add_two_ints_client:main',
            'number_publisher = my_py_pkg.number_publisher:main',
            'number_counter = my_py_pkg.number_counter:main',
            'hw_status_publisher = my_py_pkg.hw_status_publisher:main',
            'led_panel = my_py_pkg.led_panel:main',
            'battery = my_py_pkg.battery:main',
            'joy2twist_node = my_py_pkg.joy2twist_node:main',
            
        ],
    },
)
