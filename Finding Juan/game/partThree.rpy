
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
    show dog
    dog "lalala"
    dog "i love my swing..."
    
    hide dog
    with dissolve

    hide dim
    jump checkDist

### Pizza Place Button ###
screen pizzaTalk3():
    
    imagebutton:
        idle "/images/PizzaButton/pizza_idle.png"
        hover "/images/PizzaButton/pizza_hover.png"
        action Jump("pizza3")
        pos (53, 0)

label pizza3:
    window hide

    "Could he be here?"
    
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