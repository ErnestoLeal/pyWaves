from playNote import playNote
from setupSource import setupSource

def play_scale():
    scale_notes = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]
    
    note_duration = 1  
    piece_speed = 100  
    waveform_function = "sine"  
    resource, rm = setupSource("USB0::0x0957::0x2607::MY59003077::0::INSTR")
    if resource is None:
        print("Failed to connect to waveform generator.")
        return
    
    try:

        for note in scale_notes:
            playNote(note, note_duration, piece_speed, waveform_function, resource=resource)
            print(f"Playing {note}")
    finally:

        resource.close()
        rm.close()

# Main function to call play_scale
if __name__ == "__main__":
    play_scale()
