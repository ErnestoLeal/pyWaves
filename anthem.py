from playNote import playNote
from setupSource import setupSource

def play_melody():
    #Main Melody:
    melody = [

    #Main verses:
    ("B4", 1),  # "You"
    ("A4", 1),  # "will"
    ("A4", 1),  # "kn"
    ("G4", 1),  # "ow"
    ("G4", 1),  # "Youll"
    
    ("D5", 1),  # "re-"
    ("G4", 2),  # "born"
    ("F#4", 1), # "to"
    ("G4", 8),  # "night"
    
    ("B4", 1),  # "Must"
    ("A4", 1),  # "be"
    ("A4", 1),  # "ra"
    ("G4", 1),  # "ged"
    ("G4", 1),  # "Il"
    
    ("D5", 1),  # "stay-"
    ("A4", 2),  # "by"
    ("B4", 1),  # "your"
    ("G4", 8),  # "side"
    
    ("B4", 1),  # "E"
    ("A4", 1),  # "ven"
    ("A4", 1),  # "if"
    ("G4", 1),  # "my"
    ("G4", 1),  # "body"

    ("D5", 1),  # "is-"
    ("D5", 1),  # "bleached"
    ("D5", 1),  # "to"
    ("A4", 1),  # "the"
    ("G4", 8),  # "bones"

    ("E4", 1),  # "I"
    ("G4", 1),  # "Dont"
    ("A4", 2),  # "Want"
    ("A4", 1),  # "Go"
    ("G4", 1),  # "Through"
    ("A4", 1),  # "That"
    ("B4", 1),  # "Ever"
    ("A4", 1),  # "A"
    ("A4", 1),  # "ga"
    ("G4", 4),  # "in"
    ]
    
    
    piece_speed = 128 
    waveform_function = "sine" 

    # Setup the waveform generator connection once
    resource, rm = setupSource("USB0::0x0957::0x2607::MY59003077::0::INSTR")
    if resource is None:
        print("Failed to connect to waveform generator.")
        return
    
    try:
        # Loop through each note in the melody and play it
        for note, duration in melody:
            playNote(note, duration, piece_speed, waveform_function, resource=resource)
            print(f"Playing {note} for {duration} beat(s)")
    finally:
        # Close the connection after the melody is played
        resource.close()
        rm.close()

# Main function to call play_melody
if __name__ == "__main__":
    play_melody()
