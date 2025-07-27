# https://www.youtube.com/watch?v=8Y98Nm2yYxQ&ab_channel=PerKGrok
# https://www.youtube.com/watch?v=d2BhDSVfmDU&ab_channel=PerKGrok


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

define sX= 310
define sY=335
default mX=0
default dist=0
default standWalk=0
default rX= -1000

screen checkMouse():
    if standWalk==0:
        key "mousedown_1" action Jump("checkDist")


# The game starts here.
label start:
    scene bg town:
        xpos rX
    show screen checkMouse

label standRight:
    $ standWalk=0

    show semi stand:
        xpos sX
        ypos sY
        xzoom 1.0

    $ renpy.pause(hard=True)

label standLeft:
    $ standWalk=0

    show semi stand:
        xpos sX
        ypos sY
        xzoom -1.0

    $ renpy.pause(hard=True)

label walkRight:
    $ standWalk=1
    scene bg town:
        xpos rX
        linear dist/200.0 xpos rX-dist

    show semi walk:
        xpos sX
        ypos sY
        xzoom 1.0

    $ renpy.pause(delay=dist/200.0, hard=True)
    $ rX -= dist
    jump standRight

label walkLeft:
    $ standWalk=1

    scene bg town:
        xpos rX
        linear dist/200.0 xpos rX+dist

    show semi walk:
        xpos sX
        ypos sY
        xzoom -1.0

    $ renpy.pause(delay=dist/200.0, hard=True)
    $ rX += dist
    jump standLeft

label checkDist:
    $ mX=renpy.get_mouse_pos()[0]

    if mX>320:
        $ dist = mX-320
        if rX-dist<-4067:
            $ dist= 4067 + rX
        jump walkRight

    else:
        $ dist = 320-mX
        if rX+dist>-351:
            $ dist= -(351 + rX)
        jump walkLeft