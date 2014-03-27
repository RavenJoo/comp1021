'''
COMP 1021 Assignment 1

Written by: JOO, Minhyung
Student ID: 20173164
Email: mjoo@stu.ust.hk   OR   melody10511@gmail.com
'''

import pygame.midi  # Import the midi module for playing music
import time         # Import the time module for the time.sleep function
import turtle       # Import the turtle module for the music display option

##### Initialize the modules

# Initialize the MIDI (playing music) module
pygame.midi.init()

# Create an output to play music
output = pygame.midi.Output(pygame.midi.get_default_output_id())

# Initialize the music list
music = []

# Initialize the note colour list
colors = ['HotPink1', 'HotPink2', 'HotPink3', 'HotPink4']

# Initialize the instrument list
instruments = [
    'Acoustic Grand Piano', 'Bright Acoustic Piano', 'Electric Grand Piano',
    'Honky-tonk Piano', 'Electric Piano 1', 'Electric Piano 2', 'Harpsichord',
    'Clavinet', 'Celesta', 'Glockenspiel', 'Music Box', 'Vibraphone',
    'Marimba', 'Xylophone', 'Tubular Bells', 'Dulcimer', 'Drawbar Organ',
    'Percussive Organ', 'Rock Organ', 'Church Organ', 'Reed Organ',
    'Accordion', 'Harmonica', 'Tango Accordion', 'Acoustic Guitar (nylon)',
    'Acoustic Guitar (steel)', 'Electric Guitar (jazz)',
    'Electric Guitar (clean)', 'Electric Guitar (muted)', 'Overdriven Guitar',
    'Distortion Guitar', 'Guitar Harmonics', 'Acoustic Bass',
    'Electric Bass (finger)', 'Electric Bass (pick)', 'Fretless Bass',
    'Slap Bass 1', 'Slap Bass 2', 'Synth Bass 1', 'Synth Bass 2', 'Violin',
    'Viola', 'Cello', 'Contrabass', 'Tremolo Strings', 'Pizzicato Strings',
    'Orchestral Harp', 'Timpani', 'String Ensemble 1', 'String Ensemble 2',
    'Synth Strings 1', 'Synth Strings 2', 'Choir Aahs', 'Voice Oohs',
    'Synth Choir', 'Orchestra Hit', 'Trumpet', 'Trombone', 'Tuba',
    'Muted Trumpet', 'French Horn', 'Brass Section', 'Synth Brass 1',
    'Synth Brass 2', 'Soprano Sax', 'Alto Sax', 'Tenor Sax', 'Baritone Sax',
    'Oboe', 'English Horn', 'Bassoon', 'Clarinet', 'Piccolo', 'Flute',
    'Recorder', 'Pan Flute', 'Blown Bottle', 'Shakuhachi', 'Whistle',
    'Ocarina', 'Lead 1 (square)', 'Lead 2 (sawtooth)', 'Lead 3 (calliope)',
    'Lead 4 (chiff)', 'Lead 5 (charang)', 'Lead 6 (voice)', 'Lead 7 (fifths)',
    'Lead 8 (bass + lead)', 'Pad 1 (new age)', 'Pad 2 (warm)',
    'Pad 3 (polysynth)', 'Pad 4 (choir)', 'Pad 5 (bowed)', 'Pad 6 (metallic)',
    'Pad 7 (halo)', 'Pad 8 (sweep)', 'FX 1 (rain)', 'FX 2 (soundtrack)',
    'FX 3 (crystal)', 'FX 4 (atmosphere)', 'FX 5 (brightness)',
    'FX 6 (goblins)', 'FX 7 (echoes)', 'FX 8 (sci-fi)', 'Sitar', 'Banjo',
    'Shamisen', 'Koto', 'Kalimba', 'Bagpipe', 'Fiddle', 'Shanai',
    'Tinkle Bell', 'Agogo', 'Steel Drums', 'Woodblock', 'Taiko Drum',
    'Melodic Tom', 'Synth Drum', 'Reverse Cymbal', 'Guitar Fret Noise',
    'Breath Noise', 'Seashore', 'Bird Tweet', 'Telephone Ring', 'Helicopter',
    'Applause', 'Gunshot']

# Display music function for the turtle display option
def displaymusic():
    # Initialize turtle
    turtle.mode('world')
    turtle.reset()

    turtle.pensize(5)       # Set the pensize before hiding
    turtle.hideturtle()     # Do not display the turtle
    turtle.tracer(False)    # Disable any turtle animation

    # Find the maximum and the minimum pitches of the music
    maxpitch = music[0][1]
    minpitch = music[0][1]
    offset = 0

    for event in music:
        if event[1] > maxpitch:
            maxpitch = event[1]
        elif event[1] < minpitch:
            minpitch = event[1]

    # Set the offset according to the difference between the maxpitch and the minpitch
    offset = int((maxpitch - minpitch) * 0.05)

    # Set up the coordinate system
    duration = music[-1][0]
    rightoffset = duration * 0.01
    turtle.setworldcoordinates(0, minpitch - offset, duration + rightoffset, maxpitch + offset)

    # Draw the notes
    for i in range(len(music)):
        event = music[i]
        if event[2] == 'On':
            if event[3] >= 96:
                turtle.color(colors[0])
            elif event[3] >= 64:
                turtle.color(colors[1])
            elif event[3] >= 32:
                turtle.color(colors[2])
            elif event[3] < 32:
                turtle.color(colors[3])
            turtle.up()
            turtle.goto(event[0], event[1])
            turtle.down()

            for j in range(i + 1, len(music)):
                nextevent = music[j]
                if (event[1] == nextevent[1]) and (nextevent[2] == 'Off'):
                    turtle.goto(nextevent[0], nextevent[1])
                    break
            
    turtle.update()

    # Call done() to keep the window alive
    turtle.done()
    

print('Welcome to the Python music player!')

# The following while loop shows the menu options
# to the user, gets the response from the user,
# and does the appropriate action

# Initialize the option to empty so we can
# do the while loop the first time
option = ''

while option != 'q': # While the option is not 'q'
    print()
    print('Please choose one of the following options:')
    print()
    print('l - Load a music file')
    print('p - Play the music')
    print('i - Change the musical instrument')
    print('t - Transpose the music')
    print('s - Adjust the speed of the music')
    print('d - Display the music')
    print('f - Fade in/out the music')
    print('r - Print the music')
    print('q - Quit the program')
    print()

    option = input('Please input your option: ')

    '''
    The following code loads the music information
    into the event data structure.
    You aren't expected to understand exactly how it
    works, so don't worry about it!
    '''
    ##### Handle the load option
    if option == 'l':
        print()

        # Ask the user for the music file
        musicfile = input('Please give me a music file: ')

        # Open the file for reading
        f = open(musicfile, 'r')

        # Read the data into the music list
        music = []
        for line in f:
            # Read each line as a music event
            event = line.rstrip().split("\t")

            # Convert the data to the right data type
            event[0] = float(event[0])  # Time
            event[1] = int(event[1])    # Pitch
            event.append(127)           # Volume

            # Add the event at the end of the music
            music.append(event)

        # Close the file
        f.close()
    '''
    End of the scary code
    '''

    ##### Handle the play option
    if option == 'p':
        print()

        # Initialize the time sequence
        timeline = 0.0
        
        # Loop for playing each note
        for i in range(len(music)):
            # Get the note and play it
            event = music[i]
            time.sleep(event[0] - timeline)
            timeline = event[0]

            # Play the notes
            if event[2] == 'On':
                if event[1] > 127:
                    output.note_on(127, event[3])
                elif event[1] < 0:
                    output.note_on(0, event[3])
                else:
                    output.note_on(event[1], event[3])
            elif event[2] == 'Off':
                if event[1] > 127:
                    output.note_off(127, event[3])
                elif event[1] < 0:
                    output.note_off(0, event[3])
                else:
                    output.note_off(event[1], event[3])
                
    ##### Handle the instrument option
    if option == 'i':
        print()

        # Get the instrument number
        inst = input("Please enter the instrument (instrument number of name): ")

        # Change the instrument
        for i in range(len(instruments)):
            if inst == instruments[i]:
                output.set_instrument(i)
                break
            elif i == 127:
                output.set_instrument(int(inst))

    ##### Handle the transpose option
    if option == 't':
        print()

        # Ask the user for the transposition value
        trans = input("Please enter the transposition: ")
        trans = int(trans)

        # Loop for transposing the notes
        for event in music:
            event[1] = event[1] + trans

    ##### Handle the speed option
    if option == 's':
        print()

        # Ask the user for the new speed
        speed = input("Please enter the new speed, in percentage: ")
        speed = float(speed) / 100

        # Adjust the speed
        for event in music:
            event[0] = event[0] / speed

    ##### Handle the display option
    if option == 'd':
        print()

        print('Please switch to the turtle window to see the music display')

        # Draw the music
        displaymusic()

    ##### Handle the fade in/out option
    if option == 'f':
        print()

        fade = int(input('Please enter 1 for fade in and 2 for fade out: '))
        length = float(input('Please enter the length in seconds for the fading in/out: '))

        
        
        # Pick out the notes for the fade in and change volumes
        if fade == 1:
            for i in range(len(music)):
                event = music[i]
                if (event[0] < length) and (event[2] == "On"):
                    event[3] = int(event[0]/length * event[3])
                    for j in range(1, len(music) - i):
                        nextevent = music[i+j]
                        if (event[1] == nextevent[1]) and (nextevent[2] == "Off"):
                            nextevent[3] = event[3]
                            break
        elif fade == 2:
            duration = music[-1][0]
            for i in reversed(range(len(music))):
                event = music[i]
                if (event[0] <= duration) and (event[0] > (duration - length)) and (event[2] == "On"):
                    event[3] = int(((duration - event[0]) / length) * event[3])
                    for j in range(1, len(music) - i):
                        nextevent = music[i+j]
                        if (event[1] == nextevent[1]) and (nextevent[2] == "Off"):
                            nextevent[3] = event[3]
                            break
        
    ##### Handle the print option
    if option == 'r':
        print()

        # Print a note in each line
        for event in music:
            print('[', event[0], ', ', event[1], ", '", event[2], "', ", event[3], ']', sep='')

# Close the music output
output.close()

# Close the MIDI module
pygame.midi.quit()
