import serial.tools.list_ports

def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    available_ports = []

    for port, desc, hwid in sorted(ports):
        available_ports.append(port)

    return available_ports

if __name__ == "__main__":
    ports = list_serial_ports()
    if ports:
        print("Available serial ports:")
        for port in ports:
            print(port)
    else:
        print("No serial ports available.")
