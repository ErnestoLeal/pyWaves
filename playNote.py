import time
import pyvisa  # type: ignore
import logging
from noteDictionary import note_dictionary
from functionDictionary import function_dictionary
from setupSource import setupSource

# Configure logging
logging.basicConfig(level=logging.INFO)

def playNote(note, noteDuration, pieceSpeed, waveform_function, amplitude=0.03, offset=0.0, resource=None, rm=None):

    # Validate parameters
    if not isinstance(noteDuration, (int, float)) or noteDuration <= 0:
        logging.error("Invalid note duration. Must be a positive number.")
        return
    if not isinstance(pieceSpeed, (int, float)) or pieceSpeed <= 0:
        logging.error("Invalid piece speed. Must be a positive number.")
        return
    if not (0.0 <= amplitude <= 10.0):  # Example amplitude range
        logging.error("Amplitude out of range. Must be between 0.0 and 10.0.")
        return

    frequency = note_dictionary.get(note)
    if frequency is None:
        logging.error(f"Note {note} not found in note dictionary.")
        return

    # Calculate duration in seconds
    duration_in_seconds = (noteDuration / pieceSpeed) * 60

    # Get waveform command from function dictionary
    waveform_command = function_dictionary.get(waveform_function)
    if waveform_command is None:
        logging.error(f"Waveform function {waveform_function} not found in function dictionary.")
        return

    # Set up the resource if not provided
    close_after_use = False  # Track if resource needs to be closed
    if resource is None or rm is None:
        resource, rm = setupSource("USB0::0x0957::0x2607::MY59003077::0::INSTR")
        if resource is None:
            return
        close_after_use = True

    try:
        # Channel 2
        command = f"{waveform_command} {frequency}, {amplitude}, {offset}"
        logging.info(f"Sending command to Both Channels: {command}")
        resource.write(command)

        # Turn on the output channels and play the note
        logging.info(f"Turning output ON for {duration_in_seconds:.2f} seconds")
        resource.write("OUTP1 ON")
        resource.write("OUTP2 ON")
        time.sleep(duration_in_seconds)

        # Turn off the output channels after the duration
        resource.write("OUTP1 OFF")
        resource.write("OUTP2 OFF")
        logging.info("Output turned OFF")

    except Exception as e:
        logging.error(f"Error during playNote execution: {e}")

    finally:
        # Close resources if they were created in this function
        if close_after_use:
            try:
                resource.close()
                rm.close()
            except Exception as e:
                logging.error(f"Error closing resource or ResourceManager: {e}")

# Example usage:
# playNote("A4", noteDuration=1, pieceSpeed=100, waveform_function="sine")
