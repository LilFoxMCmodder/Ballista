import time

play_again = "yes"

while play_again.lower() == "yes":
    print('''
                                                                         
88                     88 88 88                               
88                     88 88 ""             ,d                
88                     88 88                88                
88,dPPYba,  ,adPPYYba, 88 88 88 ,adPPYba, MM88MMM ,adPPYYba,  
88P'    "8a ""     `Y8 88 88 88 I8[    ""   88    ""     `Y8  
88       d8 ,adPPPPP88 88 88 88  `"Y8ba,    88    ,adPPPPP88  
88b,   ,a8" 88,    ,88 88 88 88 aa    ]8I   88,   88,    ,88  
8Y"Ybbd8"'  `"8bbdP"Y8 88 88 88 `"YbbdP"'   "Y888 `"8bbdP"Y8  
                                                             
''')

    print("Hello! Welcome to Treasure Island! Get ready for this absolute amazing adventure of a story!")
    print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")

    time.sleep(1.5)

    print('''In the path, the air crackling with unseen energy. Before him, three paths unwound from the gnarled, bioluminescent trees of Treasure Island: one veered left towards
a shimmering, opal-like lagoon; straight ahead, a path of pure, solidified moonlight stretched into the distance; and to the right, a path wound through a grove of trees that 
seemed to whisper secrets in a language only the wind understood. His companion, Jim Hawkins, (a young cartographer with uncanny abilities to manipulate time) –
a boy who could subtly alter the flow of time around him with a mere thought, his skin perpetually dusted with the golden shimmer of temporal energy –
nervously adjusted his spectacles, his gaze flickering between the paths. The usual treasure map was useless; this was no ordinary island''')
    print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")

    time.sleep(1.5)

    path = input("What path may the choose? Path 1: The Opal Lagoon, Path 2: The Moonlight Road, Path 3: The Whispering Grove? ") 
    print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")

    time.sleep(1.5)

    if path == '1':
        print('''You point left, and Jim nods, his temporal shimmer intensifying slightly as you step onto the path leading to the shimmering, opal-like lagoon. The air here 
is thick with the scent of salt and strange, sweet-smelling blossoms. The bioluminescent trees give way to giant, luminous coral formations, casting an ethereal glow over your 
surroundings.

Soon, the path opens onto the edge of the lagoon. The water itself pulses with soft, shifting colors, and in its center, a small, rocky islet rises. On this islet, three ancient,
moss-covered magical doors stand, each radiating a different aura:''')
        print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")
    
        time.sleep(1.5)
        
        door_path_1 = input("Jim clutches your arm, his eyes wide. Which one, Captain? They feel... ancient? ")
        print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")
            #need to add 3 door options plus stories.
        time.sleep(1.5)
        play_again = input("Wanna play again? (yes/no) ") #take this out later
        
    elif path == '2':
        print('''You choose the path straight ahead, the one of pure, solidified moonlight. As you walk, the ground beneath your feet feels cool and smooth, like polished glass, 
reflecting the strange, alien sky above. The gnarled trees recede, replaced by towering crystals that hum with a low, resonant frequency. The light here is stark and clear, 
revealing intricate patterns in the crystalline landscape.

After a long walk, the path widens into a vast, open clearing, bathed in the moon-like glow. In the center, a single, colossal archway stands, shimmering with the same 
solidified moonlight. Within this arch, three magical doors are embedded, each distinct:

Door of Stars: A door that appears to be made of pure night sky, with tiny, swirling constellations embedded within it.

Door of Silence: A door of obsidian, absorbing all light and sound, creating an unnerving void around it.

Door of Growth: A door woven from living vines and strange, glowing fungi, constantly shifting and subtly expanding.''')
        print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")
    
        time.sleep(1.5)
    
        door_path_2 = input("Incredible, Jim breathes, adjusting his spectacles. These doors... they feel like they've been here since the island's creation which one? ")
        print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")
            #need to add 3 door options plus stories.
        time.sleep(1.5)
        play_again = input("Wanna play again? (yes/no) ") #take this out later
        
    else:
        print('''You decide on the path to the right, winding through the grove of trees that seem to whisper secrets. As you step under their canopy, the whispers grow louder, 
twisting into unsettling murmurs that seem to come from all directions at once. Jim visibly shivers, his temporal shimmer flickering erratically. 
The air grows heavy, oppressive, and the bioluminescent light dims, replaced by an eerie, sickly green glow.

The path becomes overgrown, thorny vines snagging at your clothes. The whispers turn into a cacophony of voices, not speaking words, but sounds of despair, regret, and ancient 
sorrow. You feel an immense, crushing weight descend upon you, as if the very air is trying to push you down. Jim cries out, his temporal energy failing, and he collapses to 
his knees.

Suddenly, the trees around you seem to lean in, their gnarled branches reaching like skeletal fingers. The ground beneath your feet turns soft, then gives way. You tumble into 
an unseen chasm, the whispering voices rising to a deafening shriek as darkness engulfs you. There's no escape, no magical door, only the cold embrace of the island's ancient 
secrets.

GAME OVER...''')
        print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")
        time.sleep(1.5)
        play_again = input("Wanna play again? (yes/no) ")