#######################
### Player Movement ###
#######################

# walking code: https://youtu.be/j9R97yKecF4
    # https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=53333#p502719

init python:
    import math

image semi stand = "FelipeWalk/felipe1.png"


image semi walk:
    "FelipeWalk/felipe1.png"
    0.3
    "FelipeWalk/felipe2.png"
    0.3
    "FelipeWalk/felipe3.png"
    0.3
    "FelipeWalk/felipe4.png"
    0.3
    repeat


default sX= 310
default sY=470
default mX=0
default mY=0
default dist=0
default standWalk=0

screen checkMouse():
    if standWalk==0:
        key "mousedown_1" action Jump("checkDist")


label start:
    scene bg town
    show screen checkMouse
    show screen dogTalk1
    show screen pizzaTalk1
    show screen aptTalk1

    play music "587437__clameria__chinese-loop2.mp3"

label standRight:
    $ standWalk=0

    show semi stand:
        xpos sX-37
        ypos sY-150
        xzoom 1.0

    $ renpy.pause(hard=True)

label standLeft:
    $ standWalk=0

    show semi stand:
        xpos sX-37
        ypos sY-150
        xzoom -1.0

    $ renpy.pause(hard=True)

label walkRight:
    $ standWalk=1

    show semi walk:
        xpos sX-37
        ypos sY-150
        xzoom 1.0
        linear dist/100.0 xpos mX-37 ypos mY-150

    $ renpy.pause(delay=dist/100.0, hard=True)
    $ sX=mX
    $ sY=mY
    jump standRight

label walkLeft:
    $ standWalk=1

    show semi walk:
        xpos sX-37
        ypos sY-150
        xzoom -1.0
        linear dist/100.0 xpos mX-37 ypos mY-150

    $ renpy.pause(delay=dist/100.0, hard=True)
    $ sX=mX
    $ sY=mY
    jump standLeft

label checkDist:
    python:
        mX=renpy.get_mouse_pos()[0]
        mY=renpy.get_mouse_pos()[1]

        if mY<118:
            mY=118

        if mX<164:
            mX=164

        elif mX>2080:
            mX=2080

        xD = sX-mX
        yD = sY-mY
        dist = (xD**2)+(yD**2)
        dist= math.sqrt(dist)


    if mX>sX:
        jump walkRight

    else:
        jump walkLeft

##################
### Game Start ###
##################

# define sprites
image dog = "dog_sprite.png"
image felipe = "felipe_sprite.png"
image juan = "juan_sprite.png"
image delipe = "delipe_sprite.png"
image buan = "buan_sprite.png"

define dog = Character("Deigo", color = "#88b790" )
define felipe = Character("Felipe", color = "#ac88b7" )
define juan = Character("Juan", color = "#ac6161" )
define delipe = Character("Delipe", color = "#b7b088" )
define buan = Character("Buan", color = "#b7b088" )
define b = Character("Juan?", color = "#b7b088" )
define c = Character("Cashier")

define unk = Character("???")

### Dog button ###
screen dogTalk1():
    
    imagebutton:
        idle "/images/DogButton/dog_idle.png"
        hover "/images/DogButton/dog_hover.png"
        action Jump("dog1")
        pos (501, 807)

label dog1:
    window hide

    show dim
    show dog
    dog "..."
    
    hide dog
    with dissolve

    hide dim
    jump checkDist

### Pizza Place Button ###
screen pizzaTalk1():
    
    imagebutton:
        idle "/images/PizzaButton/pizza_idle.png"
        hover "/images/PizzaButton/pizza_hover.png"
        action Jump("pizza1")
        pos (53, 0)

label pizza1:
    window hide

    "This is the Pizza Place"
    
    jump checkDist

### Apt Button ###
screen aptTalk1():
    
    imagebutton:
        idle "/images/AptButton/apt_idle.png"
        hover "/images/AptButton/apt_hover.png"
        action Jump("apt1")
        pos (1315, 715)

label apt1:
    window hide
    
    jump theStart

label theStart:
    hide screen dogTalk1
    hide screen pizzaTalk1
    hide screen aptTalk1
    hide screen checkMouse

    scene black bg
    with fade

    show apt bg
    with dissolve
    play music "650939__beetlemuse__numskull.wav"
    "Felipe and Juan are chilling in their apartment,"

    "Suddenly, Juan’s stomach rumbles."

    show juan
    juan "Man, I’m so hungry I could eat a whole horse…"
    hide juan

    show felipe at left
    felipe "Wanna just order some pizza today?"

    show juan at right
    juan "Well, I kinda want to eat Italian food instead…"

    felipe "Pizza is Italian, Juan…"

    juan "Oh! Well in that case…"

    juan "I want a large stuffed crust pizza, only cheese and ZERO VEGETABLES!"

    felipe "That sounds pretty good. Alright I’ll give them a call."

    "Felipe calls the pizza place."

    scene black bg with fade
    hide atp bg
    hide juan
    hide felipe

    play sound "371782__iamgiorgio__g6_doorbell.mp3"
    centered "20 minutes later the doorbell rings, it’s the pizza guy."
    centered "Felipe pays the pizza guy and closes the door."

    show apt bg
    show juan
    with fade

    juan "Pizza time!"

    show black bg with fade
    "Felipe and Juan open the pizza box, only to discover…"

    show veggie cg

    juan "What! Why are there VEGETABLES on my pizza!"

    felipe "I told the guy no vegetables! This is outrageous!"

    hide veggie cg
    hide juan

    show apt bg
    with fade

    felipe "The pizza place is across the street, I guess I’ll go over there myself."

    show juan
    juan "Okay, I’ll wait here and uh, guard our castle."

    "Felipe leaves the building and heads to the pizza place."

    show black bg
    with fade

    jump pizza2


