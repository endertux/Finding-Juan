label partFour:
    scene apt bg
    play music "529008__danjfilms__short-pizzicato-song.wav"

    "Buan is still there… watching soap operas while stuck to the chair."

    show buan
    buan "Hey pal! Could you hand me some pizza? I’m starving!"

    hide buan
    show felipe at left
    felipe "What's with the missing numbers on that hopscotch game? Why are the numbers 8 and 5 missing?"
    
    show buan at right
    buan "Hopscotch? I don’t know anything about that…"

    buan "I do know that my cousin Delipe loves that game!"

    felipe "Delipe…?"

    buan "Uh… who’s Delipe?"
label ask:
    show dim
    menu:
        "Bargain":
            hide dim
            hide felipe
            show buan at center
            felipe "If you tell me who the Delipe guy is, I’ll give you the whole box of pizza!"
            buan "Uhhhh..."
            "Buan starts getting nervous…"
            buan "H-hes my c-cousin…"
            felipe "And?"
            buan "That's all im sayin!"

            jump ask

        "Threat":
            hide dim
            hide felipe
            show buan at center
            felipe "Who is this Delipe guy! Tell me now or else you're gonna starve to death!"
            buan "He's..."
            buan "He has Juan! He’s held up in that warehouse! I’m the one that’s supposed to replace him!"
            felipe "Why are you going to replace him? What's your guy's motive?!"
            buan "Because we’ve seen how awesome the two of you are! And me and Delipe are just…nobodies! We thought that since we look alike, we could replace you easily and take all the fame!"
            felipe "Fame? We’re not famous…"
            buan "You both have lots of friends and get all the ladies! While me and Delipe live in an old dusty warehouse and work at the pizza place."
            felipe "If you give me the code to the warehouse…I’ll tell you all the secrets to getting friends and the ladies…"
            buan "r-really?"
            buan "“sighs” it’s 5 and 8 plus the two numbers between them…"

            hide buan
            scene black bg
            with fade

            jump cont

label cont:
    centered "With this information, Felipe heads to the red warehouse…"

    play music "813193__annabax01q__mysterious-song-loop.mp3"
    "There is a keypad on the door, the code is…"

    jump code

label code:
    menu:
        "5468":
            play sound "237712__hydranos__beepd.mp3"
            jump doorOpen
        "8645":
            "error"
            jump code
        "0023":
            "error"
            jump code
        "6485":
            "error"
            jump code

label doorOpen:

    play sound "700681__mathewhenry__metal-door-squeaking-12-medium.wav"

    centered "Felipe gets the door open…"

    "There…in the middle of the dark warehouse is Juan."
    "Juan is being held hostage by Delipe, who is standing behind him."

    scene warehouse
    show delipe
    with dissolve
    delipe "Good evening, Felipe."
    felipe "You must be Delipe…"
    felipe "I’m here for Juan."

    hide delipe
    show juan
    juan "Felipe! Oh thank goodness you're here!"

    hide juan
    show delipe

    delipe "As expected, Buan wouldn’t keep his filthy mouth shut…"
    delipe "But you’re too late Felipe… My plan is almost complete…"

    hide delipe
    scene black bg
    with fade

    centered "Delipe walks over to a large structure covered by a table cloth…"
    centered "He reveals what's underneath. It's a giant pizza oven."

    show delipe at right
    delipe "Behold!"
    show felipe at left
    felipe "What the heck is that? A…pizza oven?"
    delipe "Yes Felipe and now you and Juan will become the secret ingredient to our world famous pizza…"

    hide delipe
    hide felipe
    scene warehouse
    with dissolve

    z "WHAT?!"

    show delipe
    delipe "Once you two become the secret ingredient, me and Buan will replace the both of you and our pizza place will take over the world!"
    delipe "Muahahahaha!!!"
    hide delipe

    show juan at right
    juan "Man, I could go for some pizza right now."
    show felipe at left
    felipe "Juan!"
    felipe "Wait a minute…"

    "Felipe notices something strange about the pizza oven. It smells like pizza, and it’s…crispy?"

    "As Felipe inspects further, he realizes that the pizza oven…"

    "is made out of pizza!"

    "This gives Felipe an idea!"

    hide juan
    felipe "Hey, is that an ice cream truck I see outside?"
    show delipe at right
    delipe "What? Where?"
    felipe "Woah, looks like they're just giving it away for free!"

    hide felipe
    hide delipe
    scene black bg
    with dissolve

    play sound "448004__kneeling__break-window.mp3"

    centered "Delipe bursts through the glass window, he simply cannot resist free ice cream…"
    centered "Felipe quickly unties Juan and tells him that the pizza oven is made out of pizza!"
    centered "And within 5 seconds the pizza oven is gone and Juan seems stuffed…"
    centered "Felipe and Juan make their grand escape!"

    show delipe
    delipe "You pathetic liar! There's no ice cream truck!"
    delipe "huh? What happened to my pizza oven… and where did you guys go!"
    hide delipe
    "Suddenly, Buan appears and then the two just stand there…for a while. Not knowing what to do next."

    show buan at left
    buan "I managed to escape, boss! …but uh now what."
    show delipe at right
    delipe "I guess we're back to square one again…"

    stop music

    jump gameOver
    with fade

label gameOver:
    show thanks
    with fade
    pause 4.2

    return

