import minimalmodbus

# Configure the serial connection
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 2, debug=True)  # Port name, slave address
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 2
instrument.serial.timeout = 0.5
instrument.clear_buffers_before_each_transaction = True
instrument.close_port_after_each_call = True
instrument.mode = minimalmodbus.MODE_RTU

def wf(speed):
    write_start = 8193
    speed = (speed*100)
    send_list = [speed]
    instrument.write_registers(write_start, send_list)
    #print((write_start, send_list))
    instrument.serial.close()

def forward_motor(fqc):
    # Set bit 1 for run and bit 4 for forward
    direction = 18  # 18 in decimal is 0b00010010 in binary (bit 1 and bit 4 set)
    
    instrument.write_register(8192, direction)
    wf(fqc)
    
    

    
def stop_motor(fqc):
    # Set bit 0 for run and bit 4 for forward
    direction = 1  # 18 in decimal is 0b00010010 in binary (bit 1 and bit 4 set)
    wf(fqc)
    instrument.write_register(8192, direction)
    
def usr_ip():
     
     starter = (input("Enter 'run' to start the treadmil: "))
     
     freq = int(input("Enter the frequency: "))
     if(starter == 'run'):
          forward_motor(freq)
     else:
          print("oops")
def halt():
     halt = (input("Enter 'stop' to halt the treadmil: "))
     if(halt == "stop"):
          stop_motor(1)
usr_ip()
halt()