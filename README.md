Delta VFD EL Control with Raspberry Pi and Modbus
This project demonstrates how to control a Delta VFD EL (Variable Frequency Drive) using a Raspberry Pi through RJ45 using the Modbus communication protocol. By leveraging the MinimalModbus library in Python, this code allows for seamless communication and control between the Raspberry Pi and the VFD.

Features
Control motor speed and direction
Establish communication between Raspberry Pi and Delta VFD EL
Utilize Modbus protocol for reliable communication
Easily adaptable for various VFD configurations and setups
Getting Started
To get started with this project, follow these steps:

Connect your Raspberry Pi to the Delta VFD EL using an RJ45 cable.
Ensure that the necessary dependencies are installed on your Raspberry Pi. You can install MinimalModbus library using pip:
Copy code
pip install minimalmodbus
Clone or download this repository to your Raspberry Pi.
Open the control_vfd.py file and customize the settings according to your VFD configuration (such as slave address, register mappings, etc.).
Run the control_vfd.py script on your Raspberry Pi.
Contributing
Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Special thanks to the developers of MinimalModbus for providing a simple and efficient way to communicate with Modbus devices using Python.
