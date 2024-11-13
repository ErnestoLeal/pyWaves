import pyvisa

def setupSource(address):
    """
    Sets up the connection to the waveform generator.

    Parameters:
        address (str): The VISA address of the waveform generator.

    Returns:
        tuple: (resource, rm) if successful, where `resource` is the device connection
               and `rm` is the ResourceManager. Returns (None, None) if the setup fails.
    """
    rm = pyvisa.ResourceManager()
    try:
        # Open the resource
        resource = rm.open_resource(address)
        resource.write("OUTP1:LOAD 33")  # Set output load to 33Ω
        resource.timeout = 5000  # Set communication timeout
        print("Resource successfully connected and configured.")
        return resource, rm
    except pyvisa.VisaIOError as e:
        print(f"Could not open resource. Check connection and address. Error: {e}")
        # Ensure ResourceManager is closed if resource setup fails
        rm.close()
        return None, None
    except Exception as e:
        print(f"Unexpected error during setup: {e}")
        rm.close()
        return None, None
