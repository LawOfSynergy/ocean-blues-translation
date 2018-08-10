label TrueEnd:
    scene bg_black
    with fade
    
    centered "{size=+30}Five years later.{/size}"
    
    scene bg_beach
    with dissolve
    
    play sfx1 ("OB_sound/Seashore.ogg")
    
    mc "Mmmmm..."
    mc "Aaahhh..."
    "Here at last."
    "I couldn't believe it took me a whole week to get here."
    mc "... ... ..."
    
    show aIdle
    with dissolve
    
    play Sound1 ("OB_music/Everyday.ogg") fadein 3.0
    
    "Well I guess it wasn't all that bad."
    "For once I made the right choice by borrowing dad's yacht."
    "Was such a pain trying to convince him."
    
    stop sfx1 fadeout 2.0
    
    mc "Now then..."
    extend " let's see if I can remember how to get there."
    
    scene bg_forest1
    with dissolve
    
    play sfx1 "OB_sound/Cicada.ogg" fadein 2.0
    play sfx2 "OB_sound/Birds.ogg" fadein 2.0
    
    show aIdle
    with dissolve
    
    mc "... ... ..."
    "Five years...\n"
    extend "Only five whole years I've been away...\n"
    extend "And..."
    
    hide aIdle
    with dissolve
    show aSigh
    with dissolve
    
    mc "I can't believe I'm lost..."
    
    play sfx3 ("OB_sound/Clothes.ogg")
    
    hide aSigh
    with dissolve
    show aIdle
    with dissolve
    
    mc "Hm?"
    
    g "Did someone say they got lost?"
    
    show gIdle at right
    with moveinright
    show aIdle at left
    with moveoutleft
    
    mc "GORO!"
    "I ran up to him and gave him the biggest hug in five years."
    
    hide gIdle
    hide aIdle
    show gShock at Shake ((0.72, 1.0, 0.5, 1.0), 1.0, dist=5)
    show aCry at Shake((0.55, 1.0, 0.5, 1.0), 1.0, dist=5)
    
    mc "I've missed you so much!"
    
    hide gShock
    with dissolve
    show gHappy at right
    with dissolve
    
    g "I've missed you too."
    
    hide aCry
    with dissolve
    show aHappy at left2
    with dissolve
    
    mc "I see you haven't changed much."
    
    hide gHappy
    with dissolve
    show gBlush at right2
    with dissolve
    
    g "And you've changed a lot."
    
    mc "Hehehe."
    mc "I have so much to tell you."
    
    hide gBlush
    with dissolve
    show gHappy at right2
    with dissolve
    
    g "Heh."
    g "I'm sure you do."
    
    hide gHappy
    with dissolve
    show gPoint at right2 behind aHappy
    with dissolve
    
    g "Let's go. I'll lead the way."
    mc "Okay."
    
    hide gPoint
    hide aHappy
    with dissolve
    
    "As we walked futher into the forest. I was reminded of the time when I first met him."
    "He told me to follow him while we kept our distance from each other."
    "Always walking behind him..."
    mc "... ... ..."
    "Feels like I'm doing exaclty the same thing as back then."
    "I rushed over to Goro until we were walking side by side."
    g "What's wrong?"
    g "!"
    "I placed my hand in his hoping it was okay for me to walk with him like this." 
    mc "Is that bad?"
    g "N-No..."
    mc "Heheh."
    g "... ... ..."
    g "Welcome back [povname]."
    
    stop Sound1 fadeout 2.0
    stop sfx2 fadeout 2.0
    stop sfx1 fadeout 2.0
    
    mc "Thank you Goro."
    mc "It's good to be home."
    scene bg_black
    with fade
    
    centered "{size=+30}FIN{/size}"
    with Pause (2.0)
    
    play Sound1 ("OB_music/Twinkle.ogg")
    
    scene bg_tEnd1
    with Dissolve(0.5)
    $renpy.pause(10.0, hard=True)
    
    scene bg_tEnd2
    with Dissolve(0.5)
    $renpy.pause(10.0, hard=True)
    
    scene bg_tEnd3
    with Dissolve(0.5)
    $renpy.pause(10.0, hard=True)
    
    scene bg_tEnd4
    with Dissolve(0.5)
    $renpy.pause(10.0, hard=True)
    
    scene bg_tEnd5
    with Dissolve(0.5)
    $renpy.pause(10.0, hard=True)
    
    scene bg_tEnd6
    with Dissolve(0.5)
    $renpy.pause(10.0, hard=True)
    
    scene bg_tEnd7
    with Dissolve(0.5)
    $renpy.pause(10.0, hard=True)
    
    scene bg_tEnd8
    with Dissolve(0.5)
    $renpy.pause(10.0, hard=True)
    
    stop Sound1 fadeout 3.0
    
    scene credits
    with fade
    with Pause (10.0)