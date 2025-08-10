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

    time.sleep(1)

    print('''In the path, the air crackling with unseen energy. Before him, three paths unwound from the gnarled, bioluminescent trees of Treasure Island: one veered left towards
a shimmering, opal-like lagoon; straight ahead, a path of pure, solidified moonlight stretched into the distance; and to the right, a path wound through a grove of trees that 
seemed to whisper secrets in a language only the wind understood. His companion, Jim Hawkins, (a young cartographer with uncanny abilities to manipulate time) –
a boy who could subtly alter the flow of time around him with a mere thought, his skin perpetually dusted with the golden shimmer of temporal energy –
nervously adjusted his spectacles, his gaze flickering between the paths. The usual treasure map was useless; this was no ordinary island''')
    print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")

    time.sleep(1)

    path = input("What path may the choose? Path 1: The Opal Lagoon, Path 2: The Moonlight Road, Path 3: The Whispering Grove? ") 
    print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")

    time.sleep(1)

    if path == '1':
        print('''You point left, and Jim nods, his temporal shimmer intensifying slightly as you step onto the path leading to the shimmering, opal-like lagoon. The air here 
is thick with the scent of salt and strange, sweet-smelling blossoms. The bioluminescent trees give way to giant, luminous coral formations, casting an ethereal glow over your 
surroundings.

Soon, the path opens onto the edge of the lagoon. The water itself pulses with soft, shifting colors, and in its center, a small, rocky islet rises. On this islet, three ancient,
moss-covered magical doors stand, each radiating a different aura:

Option 1: Door of Whispers: A door carved from dark, twisted wood, from which faint, alluring whispers seem to emanate.

Option 2: Door of Light: A door made of smooth, pearlescent stone, glowing with a soft, steady light.

option 3: Door of Echoes: A door of tarnished silver, reflecting distorted images of the lagoon and the sky.''')
        print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")
    
        time.sleep(1)
        
        opal_lagoon_doors = input("Jim clutches your arm, his eyes wide. Which one, Captain? They feel... ancient? ")
        print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")
        if opal_lagoon_doors == '1':
            print('''You decide to brave the Door of Whispers, drawn by its faint, alluring sounds. As you push it open, a gust of warm, sweet-smsmelling air washes over you, 
carrying with it a thousand indistinct voices. Jim hesitates, his temporal shimmer flickering wildly, but you step through.

The other side is a cavern of shimmering, bioluminescent fungi. The whispers intensify, no longer alluring but a chaotic chorus of forgotten memories and sorrowful secrets. 
You feel an overwhelming sense of loss and regret, not your own, but an ancient, collective grief. The air grows heavy, pressing in on you. The ground beneath your feet becomes 
soft, then dissolves into a swirling vortex of light and sound. Jim's distant cry is the last thing you hear before you are utterly consumed by the island's sorrow... ''')
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("GAME OVER...")
            print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")
            time.sleep(1.5)
            play_again = input("Wanna play again? (yes/no) ") 
            
        elif opal_lagoon_doors == '2':
            print('''You choose the Door of Light, drawn to its steady, comforting glow. As you touch the smooth, pearlescent stone, the door swings inward silently, revealing 
not another cavern, but a blinding flash of pure, golden energy. Jim shields his eyes, but you step forward, feeling an inexplicable pull.

You emerge onto a vast, sun-drenched plateau, high above the clouds. The air is crisp and clean, and below you, the entire Treasure Island stretches out, vibrant and clear, its 
secrets laid bare. In the center of the plateau, a magnificent, crystalline chest rests, glowing with an inner light. As you approach, the chest opens, revealing not gold or 
jewels, but a single, perfectly formed Orb of True Sight.

As you pick up the orb, a voice, clear as a bell, echoes in your mind: "The island's truth is yours. Its magic bows to your will. The treasure is knowledge, and with it, 
mastery." Jim appears beside you, his eyes wide with awe. "Captain... we've done it. We've truly won!" The island's mysteries are now yours to command. ''')
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...YOU WIN!!!...")
            print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")
            time.sleep(1.5)
            play_again = input("Wanna play again? (yes/no) ")
            
        else:
            print('''You opt for the Door of Echoes, intrigued by its tarnished silver surface reflecting distorted images. As you push it open, a cold, damp breeze sweeps past 
you, carrying the faint, distant sound of crashing waves. You step through, and Jim follows cautiously.

You find yourselves in a vast, echoing chamber carved from black, volcanic rock. The air is still and silent, save for the faint, lingering echoes of your own footsteps and 
breathing. There's nothing else here no treasure, no monsters, no further paths. The chamber is empty, stretching into the darkness in every direction. The door behind you 
has vanished, leaving only a smooth, featureless rock wall.

Jim looks around, confused. "Captain? Where... where are we? What was the point of this door?" You are left with an unsettling sense of anticlimax, stranded in an endless, 
echoing void with no clear way forward or back. The island's secrets remain elusive, and this path has led to a perplexing, empty stillness...''')
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1.5)
            play_again = input("Wanna play again? (yes/no) ") 
            
    elif path == '2':
        print('''You choose the path straight ahead, the one of pure, solidified moonlight. As you walk, the ground beneath your feet feels cool and smooth, like polished glass, 
reflecting the strange, alien sky above. The gnarled trees recede, replaced by towering crystals that hum with a low, resonant frequency. The light here is stark and clear, 
revealing intricate patterns in the crystalline landscape.

After a long walk, the path widens into a vast, open clearing, bathed in the moon-like glow. In the center, a single, colossal archway stands, shimmering with the same 
solidified moonlight. Within this arch, three magical doors are embedded, each distinct:

Option 1: Door of Stars: A door that appears to be made of pure night sky, with tiny, swirling constellations embedded within it.

Option 2: Door of Silence: A door of obsidian, absorbing all light and sound, creating an unnerving void around it.

Option 3: Door of Growth: A door woven from living vines and strange, glowing fungi, constantly shifting and subtly expanding.''')
        print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")
    
        time.sleep(1)
    
        moonlight_doors = input("Incredible, Jim breathes, adjusting his spectacles. These doors... they feel like they've been here since the island's creation which one should we choose? ")
        print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")
        if moonlight_doors == '1':
            print('''You reach out and touch the Door of Stars, feeling a faint thrumming beneath your fingertips. It swings open silently, revealing not a room, but a 
boundless void filled with swirling nebulae and distant, glittering galaxies. Jim gasps, his temporal shimmer flaring with awe. You step through, feeling weightless, as if 
suspended in the cosmos itself.

Suddenly, a single, brilliant star detaches from the swirling expanse and streaks towards you, growing larger and brighter until it envelops you in a warm, comforting light. 
You feel a surge of ancient power, a connection to the very fabric of the universe. When the light fades, you find yourself back on the Moonlight Road, but something has 
changed. In your hand rests a Celestial Compass, its needle spinning wildly before settling on a point far beyond the island. A voice, clear and resonant, fills your mind: 
"The true treasure lies not on this island, but in the journey beyond. Your destiny awaits among the stars." Jim looks at you, his eyes wide with understanding. "Captain, 
we're not just adventurers anymore. We're... explorers of the cosmos!"''')
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...YOU WIN!!!...")
            print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")
            time.sleep(1.5)
            play_again = input("Wanna play again? (yes/no) ")
        elif moonlight_doors == '2':
            print('''You approach the Door of Silence, its obsidian surface unnervingly dark and still. As you push it open, the world outside seems to vanish. All sound, 
all light, all sensation is swallowed by an absolute void. Jim's temporal shimmer flickers and dies, and he lets out a choked cry before he, too, becomes 
utterly silent and still. You feel an immense, crushing pressure, not physical, but existential. Your thoughts, your memories, your very being begin to unravel, 
absorbed into the suffocating nothingness. There is no pain, only the terrifying, inevitable cessation of everything.''')   
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("GAME OVER...")
            print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")
            time.sleep(1.5)
            play_again = input("Wanna play again? (yes/no) ") 
        else:
            print('''You choose the Door of Growth, intrigued by its living, shifting form. As you touch the woven vines, they part, and you step into a chamber that seems to 
breathe. The walls are alive with glowing fungi and slowly unfurling fronds. The air is warm and humid, carrying the scent of rich earth and new life.

However, there's nothing else here. No treasure, no further path, no immediate danger. The chamber simply is, a living, growing space that slowly expands and contracts around 
you. Jim looks around, perplexed. "It's... just growth, Captain. Endless, slow growth." The door behind you has sealed itself, the vines weaving back into an impenetrable wall. 
You are left in a vibrant, yet ultimately stagnant, living chamber, a place of perpetual, aimless expansion with no clear exit or purpose.''')
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")
            time.sleep(1.5)
            play_again = input("Wanna play again? (yes/no) ") 
    else:
        print('''You decide on the path to the right, winding through the grove of trees that seem to whisper secrets. As you step under their canopy, the whispers grow louder, 
twisting into unsettling murmurs that seem to come from all directions at once. Jim visibly shivers, his temporal shimmer flickering erratically. 
The air grows heavy, oppressive, and the bioluminescent light dims, replaced by an eerie, sickly green glow.

The path becomes overgrown, thorny vines snagging at your clothes. The whispers turn into a cacophony of voices, not speaking words, but sounds of despair, regret, and ancient 
sorrow. You feel an immense, crushing weight descend upon you, as if the very air is trying to push you down. Jim cries out, his temporal energy failing, and he collapses to 
his knees.

Suddenly, the trees around you seem to lean in, their gnarled branches reaching like skeletal fingers. The ground beneath your feet turns soft, then gives way. You tumble into 
an unseen chasm, the whispering voices rising to a deafening shriek as darkness engulfs you. There's no escape, no magical door, only the cold embrace of the island's ancient 
secrets. ''')
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("GAME OVER...")
        print("────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────────── ⋆⋅☆⋅⋆ ──────")
        time.sleep(1.5)
        play_again = input("Wanna play again? (yes/no) ") 
