
label findHim:
    scene bg town
    show screen checkMouse
    show screen dogTalk2
    show screen pizzaTalk3
    show screen aptTalk2
    play music "789664__madgravitystudio__shady.wav"

##################
### Game Start ###
##################

### Dog button ###
screen dogTalk2():
    
    imagebutton:
        idle "/images/DogButton/dog_idle.png"
        hover "/images/DogButton/dog_hover.png"
        action Jump("dog2")
        pos (501, 807)

label dog2:
    window hide

    show dim
    felipe "Excuse me?"

    show dog
    dog "What do you want? Can’t you see I'm busy?"

    hide dog
    show felipe
    felipe "Have you seen my friend around here? He looks just like me but…wider."

    hide felipe
    show dog
    dog "Hey wait a minute?! Aren’t you the guy that stole my ice cream!"

    felipe "What?"

    dog "Yeah you! How dare you show your face here again!"

    felipe "What are you talking about? You must've mistaken me for someone else."

    felipe "I’m just looking for my friend, he's missing! His name is Juan."

    dog "Well, I did see a guy like you but more round. And he was with someone that looks exactly like you…"

    dog "Now that I think about it, the guy that looks like you had this weird lifeless stare…"

    dog "So it was definitely him that stole my ice cream!"

    felipe "Where did they go! Please tell me!"

    dog "They were walking towards that red warehouse over there. Next to the pizza place."

    dog "But you'll need a code to access that place."

    felipe "Thanks a lot!"

    hide juan
    hide dog

    hide screen checkMouse
    hide screen dogTalk2
    hide screen pizzaTalk3
    hide screen aptTalk2

    scene black bg
    with fade

    centered "Felipe leaves the park and searches the area around for more clues."
    centered "Felipe finds a hopscotch game on the sidewalk. The numbers 8 and 5 are missing! Could this be a clue?"

    jump partFour
    with fade

### Pizza Place Button ###
screen pizzaTalk3():
    
    imagebutton:
        idle "/images/PizzaButton/pizza_idle.png"
        hover "/images/PizzaButton/pizza_hover.png"
        action Jump("pizza3")
        pos (53, 0)

label pizza3:
    window hide

    "Now is not the time, I gotta find Juan."
    
    jump checkDist

### Apt Button ###
screen aptTalk2():
    
    imagebutton:
        idle "/images/AptButton/apt_idle.png"
        hover "/images/AptButton/apt_hover.png"
        action Jump("apt2")
        pos (1315, 715)

label apt2:
    window hide

    "I gotta find Juan..."
    "But where could he be?"
    "Think Felipe think!"
    
    jump checkDist