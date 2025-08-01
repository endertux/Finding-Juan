label pizza2:
    scene pizza_place
    felipe " Hey uh, I ordered this pizza with no vegetables… and there’s vegetables."

    show guy stand
    c "Sorry about that! We’ll get you another one right away!" 

    hide guy stand
    with dissolve

    "Felipe waits for the new pizza, he looks around and notices that there aren’t many employees working today…"

    show guy pizza
    with fade

    "After about 15 minutes, the new pizza is ready. The cashier also hands Felipe a coupon."

    scene black bg
    with dissolve

    "Felipe leaves the pizza place and returns to the apartment."

    scene apt bg

    felipe "Juan! I’m back with the pizza!"

    show buan
    with fade

    "Juan appears..."

    b "Sup dude!"

    b "Alright! Pizza!"

    felipe "Juan?"

    b "Yeah? What’s wrong?"
    hide buan

    show felipe at left
    felipe "Did you… do something with your hair?"

    show buan at right
    b "Huh? Oh yeah! Just got a new haircut! I did it myself!"

    felipe "That quickly?"

    b "Yup!"

    "Felipe starts to get suspicious of “Juan”… he doesn’t usually act like this."

    felipe "…What’s your favorite kind of pizza, Juan?"

    b "Oh…uh…"

    "“Juan” seems nervous, as if he doesn’t know the answer."

    b "My favorite would have to be veggie pizza!, I mean, how else would I stay in shape!"

    hide buan
    hide felipe

    scene black bg

    "Felipe suddenly lunges at this burglar that has broken into his home. He grabs some duct tape and tapes him around a chair."

    felipe "You're not Juan! Who are you!?"

    show buan
    b "What’s gotten into you man! It’s obviously me! Juan!"
    felipe "No you’re not! Look at you! You have a weird haircut, you’re all floppy and lumpy, and you like veggie pizza! Juan HATES veggie pizza!"

    "The burglar starts sweating profusely, then he’s pressured into telling Felipe his real identity…"

    buan "M-my name is Buan! I only wanted to be friends!"

    felipe "Buan? Where’s Juan!!!"

    buan "I’ll never tell you! Besides, I’m a way better friend than he is!"

    buan "I’m smarter, more handsome, and I’m not a lazy bum!"

    buan "You’ll never find him…"

    "Felipe thinks to himself (I must get to the bottom of this, if it’s the last thing I do!)"

    "Felipe glances at the coupon and notices something. The bottom of the coupon had two numbers written upside down, 8 and 5."

    "He believes that these numbers belong to some kind of code."

    felipe "Do you know anything about this?"

    buan "uh, no?"

    menu:
        "Threat":
            felipe "If you don’t tell me right now I’m gonna beat you to a pulp!"
            buan "Okay, okay! It’s half of a secret password! But I ain’t tellin you the other half!"
            jump info

        "Bargain":
            felipe "if you tell me I’ll give you five goober dollars…"
            buan "It’s half a secret password! But I don’t know the other half I swear! Please give me the goober dollars, I want icecream!"
            jump info
label info:
    scene black bg
    "With the information gathered, Felipe decides to go outside and look for more clues. Leaving Buan tied up in the apartment."

    jump findHim