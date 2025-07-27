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
