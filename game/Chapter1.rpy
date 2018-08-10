label Chapter1:

    scene bg_beach
    with dissolve
    hide bg_ship1
    hide bg_ship2
    with Pause (1.0)

    play sfx1 ("OB_sound/Seashore.ogg") fadein 1.0

    "... ... ...!"

    show mSigh at left
    with dissolve

    "Ugh..."
    "Ow... My head hurts..."
    "Everything around me is spinning..."

    hide mSigh
    with dissolve
    show mIdle
    with dissolve

    "Where...\n{w=1.0}{nw}"
    extend "Am I?"

    with Pause (1.0)
    "It doesn't look like there's anyone else around."
    "Could it be that I'm the only survivor from that incident?"

    hide mIdle
    with dissolve
    show mSigh
    with dissolve

    "No..."
    "This can't be happening..."
    "Mom... Dad..."
    "I'm...\n{w=1.0}{nw}"
    extend "all alone again..."
    "Just like..."
    "... ... ..."

    hide mSigh
    with dissolve
    show mPumped
    with dissolve

    "No!"
    "I've got to keep it together."
    "Yeah that's right."
    "I'm sure news has already gotten out about the incident. I just have to believe they'll send help out."
    "Right now I'll do everything I can to survive."

    hide mPumped
    with dissolve
    show mIdle
    with dissolve

    "... ... ..."
    "Maybe I should take a look around."
    "There's a chance that someone else besides me could have ended up here."

    hide mIdle
    with dissolve
    scene bg_beach
    with fade

    show mSigh
    with dissolve
    "... ... ..."
    "Not a single soul to be seen..."

    hide mSigh
    with dissolve
    show mSad
    with dissolve

    "Am I going to die here?"
    "There's no water or food for that matter... Just sand everywhere and a big ocean in front of me..."
    "What am I to do now?"
    "I've looked everywhere... Everywhere except for..."

    hide mSad
    with dissolve
    show mIdle
    with dissolve
    "The forest behind me."
    "I mean I want to take a look in there but what if I run into a wild animal, I'll be nothing but a pile of bones in seconds."
    "... ... ..."
    "As I stood there with the sun beaming down on me. My mind became lost in thought. I started to despair over the thoughts of what will become of me."
    "Staying here won't help and the place where I'll most likely find food would be in there..."

    hide mIdle
    with dissolve
    show mSad
    with dissolve

    "I guess I don't have a choice... it's do or die."

    stop sfx1 fadeout (1.0)

    hide mSad
    with dissolve
#----------------------------------------------------------------########################
    scene bg_forest1
    with fade
    with Pause (1.0)
    hide bg_beach

    play Sound1 ("OB_music/StrangeForest.ogg") fadein 3.0

    show mIdle
    with moveinleft

    "This forest is really something... I've never seen anything like this. Then again I've never been to a forest before..."
    "All this greenery reminds me of home somehow. Especially the time when I was little... "
    "I remember sitting in the garden on a sunny day, watching mum tending to the flowers and watering the plants. "
    "The garden would always look impressive because mum would spend every available hour pruning the leaves from the bushes and keeping the place prim and proper. "
    "But, this place is different. Everything here feels natural. Big leaves growing everywhere, green vines hanging from trees, huge tree trunks with fungus growing around them."

    stop Sound1 fadeout 3.0

    "The sound of birds chirping and cicadas mixed into the atmosphere. A carving that looks like a dragon's head..."
    "... ... ..."

    play Sound1 ("OB_music/Creepy.ogg") fadein 3.0

    "Ah ha ha... dragon..."
    "What a funny looking piece of wood."
    "I stared at the miniature piece that sat on top of a moss covered rock."
    "I think I'm starting to lose the plot here."
    "B-But..."
    extend " could this be..."
    extend "man-made?"
    "If so then..."
    extend " there's definitely someone that lives here!"

    hide mIdle
    with moveoutright

    scene bg_forest1
    with fade

    stop Sound1 fadeout 2.0
    play Sound1 ("OB_music/StrangeForest.ogg") fadein 3.0

    show mSad
    with dissolve

    "How long have I been walking?\n"
    extend "What time is it?\n"
    extend "What day's today?"

    hide mSad
    with dissolve
    show mSigh
    with dissolve

    "I just can't seem to find anything or anyone..."

    hide mSigh
    with dissolve
    show mIdle
    with dissolve

    "Wait..."
    "Which way did I come from?"

    hide mIdle
    with dissolve
    show mSad
    with dissolve

    "Sigh..."
    "Now I'm lost too...\n"
    extend "And on top of that..."
    "I'm really thirsty and hungry.\n"
    extend "I wish I could have something cold, thirst quenching and filling to eat..."
    "It's no good... I'm really tired.\n"
    extend "Maybe this is it for me..."
    hide mSad
    with dissolve
    show mSigh
    with dissolve
    "Mum..."
    extend "Dad...\n"

    stop Sound1 fadeout 1.0

    extend"I'm sorry..."

    hide mSigh
    with dissolve

    scene bg_black
    with dissolve
    hide bg_forest1
    with dissolve


    "... ... ..."
    sub "..ey... Wa... up..."
    sub "Wha.. a... doing.. ere..."
    "Hmm... Who's there?"
    sub "Wake up..."
    "Oh I know, I must be on my way to heaven..."
    "Someone up there is calling out to me..."
    sub "I SAID WAKE UP!!"

    scene bg_forest1
    with dissolve

    show mShock at Shake((0.16, 1.0, 0.5, 1.0), 1.0, dist=5)
    show gAngry at right

    play Sound1 ("OB_music/TreadingCarefully.ogg") fadein 3.0

    msub "Wah!!!"

    #show mShock at left
    #with dissolve


    sub "Grrr..."

    msub "A-a-a talking dragon!!!"
    msub "P-p-please don't eat me, I'm not tasty at all!"

    hide gAngry
    with dissolve
    show gSigh at right
    with dissolve

    sub "Hmph! You humans never change!"
    sub "Especially for one who's trespassing my territory!"

    hide mShock
    with dissolve
    show mSad at left
    with dissolve

    msub "I'm... I'm sorry... I-I didn't know..."
    msub "I'll l-leave right away..."
    sub "Hey!"

    hide mSad
    with dissolve
    show mShock at left
    with dissolve

    msub "Y-yes?"

    hide gSigh
    with dissolve
    show gPoint at right
    with dissolve

    stop Sound1 fadeout 3.0

    sub "It's that way!"

    hide mShock
    with dissolve
    show mFidget at left
    with dissolve

    msub "O-oh... T-Thank you."

    hide mFidget
    with moveoutleft
    hide gPoint
    with dissolve


    scene bg_forest1
    with fade

    play Sound1 ("OB_music/StrangeForest.ogg") fadein 3.0

    show mIdle at left
    with moveinleft

    "What... was that just now?"
    "I'm sure that was a dragon but don't dragons normally have wings..."
    "It didn't seem like it had any on its back though..."

    hide mIdle
    with dissolve
    show mSigh at left
    with dissolve

    "But that was shocking..."
    "A dragon in this day and age..."
    "I bet my mind was playing tricks on me..."

    hide mSigh
    with dissolve
    show mSad at left
    with dissolve

    "Yup. There's no other explanation.\n"
    extend "I'm so exhausted that I've started hallucinating."
    "... ... ..."
    "... which way do I go now?"
    "I'm completely lost again..."

    hide mSad
    with dissolve
    show mIdle at left
    with dissolve

    msub "Maybe it's that way?"

    jump mMaze

    label gCont:

    sub "Hey!"

    hide mIdle
    show mShock at Shake((0.16, 1.0, 0.5, 1.0), 1.0, dist=5)

    "!"

    show gIdle at right
    with moveinright

    "Oh crap!\n"
    extend "What does it want now?"
    msub "U-umm, y-yes?"
    "So it wasn't an illusion, it really is a dragon!"

    hide gIdle
    with dissolve
    show gAnnoyed at right
    with dissolve

    sub "Tch..."
    sub "Is your pathetic human brain made out of beetle dung or something?"
    sub "I told you it's that way!"

    hide mShock
    with dissolve
    show mSad at left
    with dissolve

    msub "O-oh, sorry..."
    msub "It's just that everywhere looks the same to me..."

    hide gAnnoyed
    with dissolve
    show gSigh at right
    with dissolve
    sub "Sigh..."
    sub "For a mere human you're not very capable."
    sub "... ... ..."
    sub "Tsk..."

    hide gSigh
    with dissolve
    show gPoint at right
    with dissolve

    sub "Come!"

    hide mSad
    with dissolve
    show mShock at left
    with dissolve

    "What?"
    "It wants me to follow?"
    "This is bad... it's going to eat me alive!"

    hide gPoint
    with dissolve
    show gSigh at right
    with dissolve

    sub "Hurry up human or I'll leave you behind!"

    "I don't have a choice... If I run now things could turn bad...."

    hide mShock
    with dissolve
    show mSigh at left
    with dissolve

    "O-Okay..."
    "What should I do... I knew going into the forest was a bad idea..."
    "I've got to find a way to get out of this..."

    hide mSigh
    hide gSigh
    with dissolve

    scene bg_forest1
    with fade

    "As we walked further into the forest I couldn't help but take my eyes off from what I'm seeing in front of me."
    "In fact I'm completely overwhelmed by the beast's presence that I'm starting to shiver in fear. It could turn around and eat me alive anytime it wants."
    "Honestly I don't know what to expect but even so I can't let my guard down. Not even for a second."

    show gSigh at right
    with dissolve

    sub "Hey human!"

    show mShock at left
    with dissolve

    msub "Y-Yes?"

    sub "Your name."

    "It wants to know my name?\n"
    extend "Why does it want to know?\n"
    extend "Don't tell me it's planning to put a curse on me?"

    sub "Well?"

    hide mShock
    hide gSigh
    with dissolve

####---------------------------------------------EnterName
    scene ui_firstn
    with fade
    $ povname = renpy.input(_("First Name:")) or _("Kyle")

    $ povname = povname.strip()

    if povname == "":
        $ povname ="Kyle"

    scene ui_lastn
    with fade
    $ povlast = renpy.input(_("Last Name:")) or _("Romford")

    $ povlast = povlast.strip()

    if povlast == "":
        $ povlast ="Romford"
####----------------------------------------------------------

    scene bg_forest1
    with fade

    show mSad at left
    with dissolve

    msub "It's [povname] [povlast]..."

    hide gSigh
    with dissolve
    show gIdle at right
    with dissolve

    sub "... ... ..."

    hide mSad
    with dissolve
    show mIdle at left
    with dissolve

    "Did I say something wrong?"

    hide gIdle
    with dissolve
    show gSigh at right
    with dissolve

    sub "Goro..."

    "What was that?\n"
    extend "I didn't catch that at all..."

    hide mIdle
    with dissolve
    show mFidget at left
    with dissolve

    mc "Um...\n"
    extend "I'm sorry...\n"
    extend "What was-"

    hide gSigh
    with dissolve
    show gAngry at right

    sub "My name!"
    sub "It's Goro!"

    hide mFidget
    show mShock at left

    mc "O-okay..."

    hide gAngry
    with dissolve
    show gSigh at right
    with dissolve

    g "Hmph...\n"
    extend "You do your best to remember the owner of this island, human!"

    mc "I-I will..."

    hide mShock
    with dissolve
    show mIdle at left
    with dissolve

    hide mIdle
    hide gSigh
    with dissolve


    "As I treaded carefully past a tree trunk branching out of the ground.\n"
    extend "I noticed how Goro seems to avoid these ever so casually."
    "I tried to keep up, following, yet keeping my distance.\n"
    extend "My eye's adverted to its back from time to time."
    "I couldn't help but notice its large tail swinging from side to side as it walks."
    "Still, I kept my guard up, being ever so cautious around this creature."
    "No one in this whole world would ever believe such a beast exists.\n"
    extend "And judging by its looks I'm pretty sure it's a male.\n"
    "There were many questions that I wanted to ask, the general stuff."
    "What's your favourite food, colour, weather and have you ever been anywhere else besides here?"
    "It would be interesting and fun to find out more about him.\n"
    extend "But...\n"
    extend "Something just tells me, it's best to keep my mouth shut."

    show mSad at left
    with dissolve
    mc "I wonder why he's all alone on this island?"

    show gAnnoyed at right
    with dissolve

    g "For a pathetic human to ask such a dumb question."
    g "I don't know whether you're just brave or stupid."

    hide mSad
    with dissolve
    show mShock at left
    with dissolve

    "H-he heard me!"
    mc "I-I didn't mean to... I'm sorry I was just talking to myself..."

    hide gAnnoyed
    with dissolve
    show gSigh at right
    with dissolve

    g "Hmph..."
    extend "whatever..."
    g "Just hurry up and leave this island once I take you back to the beach!"

    hide mShock
    with dissolve
    show mFidget at left
    with dissolve

    mc "Oh... Um...\n"
    extend "The thing is...\n"
    extend "I drifted here from an incident that I had on a boat..."

    hide mFidget
    with dissolve
    show mSad at left
    with dissolve

    mc "So I can't really leave the island..."
    "Although I would love to get out of here more than anything at this moment."

    hide gSigh
    with dissolve
    show gAnnoyed at right
    with dissolve

    g "That's none of my concern!"

    "His words were harsh like a sharp knife chipping away at me."
    "I knew for sure that there won't be anyone or anything on this island that can help me."
    "Not knowing the first thing about survival, I was guaranteed my death on this island sooner or later."

    hide mSad
    with dissolve
    show mSigh at left
    with dissolve

    mc "But...\n"
    extend "I won't be able to leave...\n"
    extend "I don't know where I am... "
    mc "Or what to do...\n"
    extend "... ... ...\n"
    extend "I'll definitely die out here without your help..."

    g "Tsk..."

    hide gAnnoyed
    with dissolve
    show gSigh at right
    with dissolve

    g "Useless human."
    g "It's none my concern if you die here too!"

    "Those words came down like an axe. Tearing at me causing a certain memory to resurface."

    hide mSigh
    with dissolve
    show mSad at left
    with dissolve

    mc "P-Please...\n"
    extend "Don't take me back there...\n"
    extend "I can't die here! People out there might be searching for me!"

    "I can't die.\n"
    extend "Not here...\n"
    extend "Not yet..."

    hide mSad
    with dissolve
    show mHurt at left
    with dissolve

    mc "Please... I'll do anything!"
    mc "... So please..."
    mc "... ... ..."

    hide gSigh
    with dissolve
    show gAnnoyed at right
    with dissolve

    g "... Grrr..."
    g "Fine!"
    g "Do what you want human!"
    g "Your death here would cause me more problems!"

    "Even though he says it like that I couldn't help but feel relief."
    "Relief of not having to be left alone. Relief for a chance of surviving."
    "But even so it doesn't make me any happier."

    hide mHurt
    with dissolve
    show mSad at left
    with dissolve

    mc "T-Thank you!"

    hide gAnnoyed
    with dissolve
    show gSigh at right
    with dissolve

    g "Hmph..."

    "I don't really know much about dragons but...\n"
    extend "Do they all hate humans this much?"

    hide mSad
    hide gSigh
    with dissolve
    scene bg_forest1
    with fade

    show mSad at left
    with dissolve

    "My legs are going to fall off..."
    "Just how much longer are we going to walk?"
    "I want to stop and rest already..."

    show gSigh at right
    with dissolve

    g "... ... ...\n"
    extend "You're slowing down!\n"
    extend "Keep walking human!"

    hide mSad
    with dissolve
    show mSigh at left
    with dissolve

    "Keep walking!?"
    "We must've been walking for at least an hour or two on these uneven paths!"
    "I can barely stand let alone walk."
    "On top of that my throat is really dry and the word hungry doesn't even come close to how I feel."

    hide mSigh
    with dissolve
    show mIdle at left
    with dissolve

    mc "Oh berries!\n"
    extend "They look really tasty, these white ones especially!"


    g "Hmph!\n"
    extend "You must be a real fool to eat those, human!"

    hide mIdle
    with dissolve
    show mSad at left
    with dissolve

    "Well, I can't help it if I'm hungry..."
    "You've been dragging me around in this forest for hours..."
    "I'm really tired, thirsty and hungry!"

    mc "Just because you don't want to eat these doesn't mean I can't."

    hide gSigh
    with dissolve
    show gAnnoyed at right
    with dissolve

    g "... ... ...\n"
    extend "If you want to eat and poison yourself be my guest."

    hide mSad
    with dissolve
    show mShock at left
    with dissolve

    mc "P-Poison!?"

    hide gAnnoyed
    with dissolve
    show gSigh at right
    with dissolve

    g "Also, feel free to eat those mushrooms while you're at it. You'll be dead in no time."

    hide mShock
    with dissolve
    show mSad at left
    with dissolve

    "... ... ...\n"
    extend "On second thought. I think I can deal with not having food for a little while longer..."

    g "... ... ..."

    hide mSad
    hide gSigh
    with dissolve

###--------------------------------------------###########################
    stop Sound1 fadeout 3.0

    scene bg_forest2
    with fade

    play sfx1 ("OB_sound/Cicada.ogg") fadein 3.0
    play sfx2 ("OB_sound/Birds.ogg") fadein 3.0

    show gSigh at right
    with dissolve

    "Stop!"
    "We're here."

    show mSad at left
    with dissolve

    mc "*huff* *pant*"

    "Finally, my legs gave in. I fell to the floor with my backside colliding onto the soft grass."
    "We're here at last!\n"
    extend "I think I'm about to pass out."

    hide gSigh
    with dissolve
    show gAnnoyed at right
    with dissolve

    g "Tch..."
    g "Wait here!"

    hide mSad
    with dissolve
    show mSigh at left
    with dissolve

    "I mustered the remaining energy I had left and replied before he left."
    mc "O-okay..."

    hide gAnnoyed
    with moveoutright

    "At this moment I don't care what he does, he could eat me for all I care."
    "I'm just so tired that I don't even want to move or think."

    hide mSigh
    with dissolve
    show mIdle
    with dissolve

    "Hmm?"
    "Now that I take a closer look. This place is really different from the rest of the forest..."

    hide mIdle
    with dissolve
    show mRelax
    with dissolve

    "It's so relaxing here...\n"
    extend "... ... ..."
    mc "Ahhh...."
    "The occasional breeze passing by and the warm sun seeping through the tree leaves...\n"
    extend "Feels like I'm being wrapped up in a blanket."
    "I feel so calm and at ease...\n"
    extend "If only I could close my eyes for eternity."

    hide mRelax
    with dissolve

    scene bg_black
    with fade

    mc "zzz...\n"
    extend"zzz..."

    #show gSigh at right
    #with moveinright

    g "Hey!"
    g "Human! Get up!"

    #show mShock at left
    #with dissolve

    scene bg_Goro1
    with fade

    mc "Ah!"

    #hide mShock
    #with dissolve
    #show mIdle at left
    #with dissolve

    "I must of drifted off for a moment there."

    #hide mIdle
    #with dissolve
    #show mSigh at left
    #with dissolve

    mc "S-Sorry... I just..."

    g "Hmph..."

    #hide gSigh
    #with dissolve
    #show gIdle at right
    #with dissolve

    g "Here!"

    show bg_Goro1a at right
    with moveinbottom

    #hide mSigh
    #with dissolve
    #show mIdle at left
    #with dissolve

    "I watched as he held out his hand while holding a large fruit."

    #hide gIdle
    #with dissolve
    #show gSigh at right
    #with dissolve

    g "Be glad that I'm giving this to you human!"
    "A watermelon?"

    #hide gSigh
    #with dissolve
    #show gIdle at right
    #with dissolve

    "I held out my hands to receive the large fruit."

    hide bg_Goro1a
    with moveoutbottom

    "It was rather heavy for me to hold onto, so I placed it beside me."

    #hide mIdle
    #with dissolve
    #show mFidget at left
    #with dissolve

    mc "Oh, err... thank you...\n"
    extend "... ... ..."

    scene bg_forest2
    with dissolve

    hide gIdle
    with dissolve
    show gSigh at right
    with dissolve

    g "What?"
    g "Not good enough for you human!?"

    hide mFidget
    with dissolve
    show mShock at left
    with dissolve

    mc "N-No that's not it!"

    hide mShock
    with dissolve
    show mFidget at left
    with dissolve

    mc "... It's just that...\n"
    mc "I can't eat it like this..."

    hide gSigh
    with dissolve
    show gAnnoyed at right
    with dissolve

    g "Tsk..."

    hide gAnnoyed
    with dissolve
    show gPoint at right
    with dissolve

    g "Give it here!"

    hide mFidget
    with dissolve
    show mShock at left
    with dissolve

    "I flinched as he reached out and swiped up the watermelon."

    hide mShock
    with dissolve
    show mIdle at left
    with dissolve

    "What's he going to do with it?"

    hide gPoint
    with dissolve
    show gSigh at right
    with dissolve

    "You human beings are completely useless!"

    hide mIdle
    with dissolve
    show mSad at left
    with dissolve

    "... ... ..."
    "Well sorry for being completely useless."
    "Unlike you, it's not like I have claws to open this or anything."
    "As I sat there staring at the tall grass beside my feet. I couldn't help but wallow in despair."

    play sfx3 ("OB_sound/HeavyPunch.ogg")

    "A loud crack sounded from the watermelon."

    hide mSad
    hide gSigh
    with dissolve

    show mShock at left
    show gAngry at right
    with dissolve

    "I watched in awe as he split the fruit in half with his big lizard like hands."

    hide gAngry
    with dissolve
    show gSigh at right
    with dissolve

    g "Here!"
    mc "... ... ..."
    "The once perfectly round fruit has now been forcefully ripped into smaller pieces."

    hide mShock
    with dissolve
    show mSigh at left
    with dissolve

    "I better be careful not to say anything to upset him...\n"
    extend "Otherwise it'll be my head he'll be ripping off next."
    "As that thought crossed my mind. He began piling the pieces of the melon in front of me."
    "Without hesitation I began tucking into the fruit."

    hide mSigh
    with dissolve
    show mShock at left
    with dissolve

    "Wow...\n"
    extend "This is really good, it's so cold and full of juice!"

    hide mShock
    with dissolve
    show mRelax at left
    with dissolve

    mc "... So refreshing..."

    hide gSigh
    with dissolve
    show gShy at right
    with dissolve

    g "Hmph!"
    g "Stay here and don't move human!"
    mc "Y-Yes..."

    hide gShy
    with moveoutright

    hide mRelax
    with dissolve
    show mIdle
    with dissolve

    "I wonder where he's going...?"
    "He's not planning to eat me, is he!?"
    "Maybe I should run while I can!"
    "But if I did... where should I run to?"
    mc "... ... ..."
    "I guess, if he did plan on eating me he could've done that a long time ago."
    mc "Ah!"
    "Now that I think about it..."
    "Is it considered normal for a Dragon to give someone food?"
    "From what I've seen and read in novels they eat humans.\n"
    extend "I think..."

    hide mIdle
    with dissolve
    show mSad
    with dissolve

    "If that was the case then I could be wrong about him. Maybe he's not as bad as I thought."

    hide mSad
    with dissolve
    show mIdle
    with dissolve

    stop sfx1 fadeout 3.0
    stop sfx2 fadeout 3.0

    mc "hmm..."
    "I wonder if he's been living here for a long time?"
    "Whatever, that's not my priority to worry about..."
    "Right now, I should try and figure out a way to get off this island."
    "... But for now..."
    "I'll try and get some rest while I can..."

    hide mIdle
    with dissolve

#--------------------------------------------########################
    scene bg_forest3
    with fade

    play sfx1 ("OB_sound/Fireplace.ogg") fadein 3.0
    play sfx2 ("OB_sound/Crickets.ogg") fadein 3.0

    "... ... ..."
    mc "Uuhhgn..."

    "The night enveloped the forest leaving the woods feeling dark and eerie."
    "As I opened my eyes I noticed a large figure had sat beside a small camp fire."
    "Flames flickered and crackled as the large figure threw in more wood to fuel the flames."

    show gIdle at right
    with dissolve

    g "So... finally awake human?"

    show mIdle at left
    with dissolve

    mc "... ... ..."
    "Something smells really good."
    "Is that fish he's cooking over by the fire?"
    "That reminds me, I completely forgot to thank him."

    hide mIdle
    with dissolve
    show mFidget at left
    with dissolve

    mc "I umm...\n"
    extend "Thank you..."

    hide gIdle
    with dissolve
    show gSigh at right
    with dissolve

    g "What?"

    mc "The watermelon earlier. It was really good..."
    mc "so..."
    mc "Thank you."

    hide gSigh
    with dissolve
    show gShy at right
    with dissolve

    g "... ... ..."
    g "It gets cold at night."

    hide mFidget
    with dissolve
    show mIdle at left
    with dissolve

    mc "Huh?"

    hide gShy
    with dissolve
    show gSigh at right
    with dissolve

    g "Unless you prefer the cold human.\n"
    extend "You can stay where you are!"

    "Is that his way of trying to be nice?"
    "Still, beats sitting here and away from the fire.\n"
    extend "Besides, it's kind of creepy here at night, I don't think anyone wants to be alone in the dark."

    hide mIdle
    with dissolve
    show mFidget at left
    with dissolve

    mc "W-Well if you don't mind then...\n"
    extend "I'll sit beside the fire..."

    hide mFidget
    with moveoutleft

    "I got up from and soft patch of grass I was lying on and started walking towards the camp fire."
    "I sat myself down on the opposite side of where he is."

    show mRelax at left
    with moveinleft

    hide gSigh
    with dissolve
    show gIdle at right
    with dissolve

    "Ahhh... it's so warm..."
    "I didn't think it could get this cold at night."
    "That smell..."

    hide mRelax
    with dissolve
    show mIdle at left
    with dissolve

    "Those fishes he's grilling, they look so delicious..."
    "My mouth is watering just from the smell..."
    "I watched as he plucked one of the fishes impaled by a stick off the ground.\n"
    extend "He examined the slightly burnt fish by pinching several places."
    "I tried not to look as he began to eat but the temptation was too much for me."
    "Each bite would be bigger than the last until nothing remained.\n"
    extend "Not even the bones from the fish."

    hide gIdle
    with dissolve
    show gSigh at right
    with dissolve

    g "... ... ..."
    g "You're making my meal taste bad, human."

    hide mIdle
    with dissolve
    show mSad at left
    with dissolve

    mc "S-Sorry... I didn't mean to stare."

    hide gSigh
    with dissolve
    show gIdle at right
    with dissolve

    g "... ... ..."
    g "Here..."

    hide mSad
    with dissolve
    show mShock at left
    with dissolve

    mc "But...\n"

    hide mShock
    with dissolve
    show mIdle at left
    with dissolve

    extend "Isn't that yours..."

    hide gIdle
    with dissolve
    show gSigh at right
    with dissolve

    g "Hmph."
    g "Unless you prefer finding your own food during the night?"
    g "Be my guest. Not that I care."

    hide mIdle
    with dissolve
    show mSigh at left
    with dissolve

    mc "N-No... I guess not..."
    mc "I-I'll gladly accept your offer..."

    hide mSigh
    with dissolve
    show mIdle at left
    with dissolve

    mc "Thank you..."

    hide mIdle
    hide gSigh
    with dissolve

    "Even though the warm heat and soft light emitting from the fire puts my mind at ease."
    "It wasn't enough to melt the ice between us as we sat there in a very uncomfortable silence eating our meal."
    "I thought it was best if I should say something and maybe even try to become friends."
    "He might be a bit scary on the outside but that doesn't mean he has no emotions or feelings."


    show mFidget at left
    with dissolve

    mc "So...\n"
    extend "Err...\n"
    extend "Have you been living here for a long time?"

    show gAnnoyed at right
    with dissolve

    g "... ... ..."

    hide mFidget
    with dissolve
    show mShock at left
    with dissolve

    mc "I-I mean it's none of my business. You can ignore what I said...\n"
    extend "Um... "

    hide mShock
    with dissolve
    show mSigh at left
    with dissolve

    extend "s-sorry for asking..."

    hide gAnnoyed
    with dissolve
    show gSigh at right
    with dissolve

    g "For a puny human, you do ask a lot of inconsiderate questions..."

    hide mSigh
    with dissolve
    show mSad at left
    with dissolve

    "I was only trying to be nice and start a conversation."
    "It's better than sitting here in silence."

    g "Fifty or sixty years."

    hide mSad
    with dissolve
    show mShock at left
    with dissolve

    "Fifty or Sixty years!?"

    hide mShock
    with dissolve
    show mIdle at left
    with dissolve

    "Wait... fifty or sixty..."
    "That makes it sound like he's not sure. Then could it be that he's been here much longer than fifty or sixty years?"
    "Even so living for that long..."

    hide mIdle
    with dissolve
    show mSad at left
    with dissolve

    mc "Aren't you sad...?"

    hide gSigh
    with dissolve
    show gAnnoyed at right
    with dissolve

    g "Huh?"
    mc "Aren't you sad being alone on this island all by yourself?"

    play Sound1 ("OB_music/A Void.ogg") fadein 3.0

    "Because if I were to be in his position.\n"
    extend "I would've broken down a long time ago..."
    "But that's because it would be something that I won't be able cope with..."

    hide gAnnoyed
    with dissolve
    show gSigh at right
    with dissolve

    g "Hmph... Don't compare yourself to me human."
    g "Unlike you lesser beings I've no need for any petty emotions including pathetic things such as sadness."

    mc "Then..."

    hide mSad
    with dissolve
    show mPumped at left
    with dissolve

    mc "Why did you help me?\n"
    extend "Why did you give me food?\n"
    extend "You could of left me to die out there and-"

    hide gSigh
    with dissolve
    show gAngry at right
    with dissolve

    g "Don't think too highly of yourself human!"
    g "If you died on this island you'll cause me problems!"

    hide mPumped
    with dissolve
    show mIdle at left
    with dissolve

    mc "Problems?"
    mc "Like what?"

    hide gAngry
    with dissolve
    show gSigh at right
    with dissolve

    g "Hmph... You wouldn't understand human!"

    hide mIdle
    with dissolve
    show mSad at left
    with dissolve

    mc "... ... ..."
    "Giving me food and bringing me to this place was only to help himself..."
    "I'm such a fool to think for a minute that he actually has a heart."
    mc "Well sorry... for not understanding..."
    g "As long as you know human."

    hide gSigh
    with moveoutright

    "As soon as the conversation ended, he got up and began walking away from where he was sitting."
    "After a few paces he laid down facing the woods."
    "His back was the only visible part that remained as the fire carried on burning."

    "It wasn't long before I fell asleep after eating. To be honest I was quite upset, mainly at myself for being so gullible."
    "I tried believing for a moment that he was helping me for good intentions but it seems like I was wrong."
    "He only helped me to prevent further problems from arising. That is to protect himself, whatever the problem may be."

    stop Sound1 fadeout 3.0
    stop sfx1 fadeout 3.0
    stop sfx2 fadeout 3.0

    mc "Whatever..."
    mc "I don't care...."

    hide mSad
    with dissolve

    scene bg_forest2
    with fade

    play sfx1 ("OB_sound/Cicada.ogg") fadein 3.0
    play sfx2 ("OB_sound/Birds.ogg") fadein 3.0

    mc "Yawn... "
    " I've slept pretty well considering it's out in the open."
    "As I rubbed my sleepy eyes to adjust my sight, I noticed Goro was nowhere to be seen."

    show mIdle
    with dissolve

    mc " Hmm?"
    mc " Where did he go?"
    mc "... ... ..."
    "Maybe he wanted to be alone..."
    "Or..."

    hide mIdle
    with dissolve
    show mSigh
    with dissolve

    "Could it be that he's angry about what I said last night?"
    "I guess that makes sense, he only brought me here so that I wouldn't go and die on his island."
    "... ... ..."

    hide mSigh
    with dissolve
    show mIdle
    with dissolve

    "What should I do now?"
    "... ... ..."
    "I'm getting restless just sitting here..."

    hide mIdle
    with dissolve
    show mSad
    with dissolve

    mc "... And hungry...."

    hide mSad
    with dissolve
    show mPumped
    with dissolve

    jump mForest

    label mContinue:

    hide mPumped
    with dissolve
    show mSigh
    with dissolve

    "Although, that might be a bad idea. Going into the forest alone..."
    "But... there's also no guarantee I'll be getting food from him all the time."
    "... ... ..."

    hide mSigh
    with dissolve
    show mIdle
    with dissolve

    "I guess the answer is quite obvious..."
    "This time I better leave tracks behind so I can find my way back."
    "Well... I better get started..."

    hide mIdle
    with moveoutright

    "As I began walking into the forest, I noticed a rock with a sharp end to it. A thought struck me as I picked it up from a nearby tree."
    "I could use this to create markings on some of the trees. That way I won't get lost."
    "I walked up to the nearest tree and began scratching the surface of the trunk with the stone."
    "For now I'll just try and make an arrow pointing to the camp area."
    mc "... ... ..."
    "Alright, that's done. Onto the next."

#-----------------------------------------------###############
    scene bg_forest1
    with fade

    play Sound1 ("OB_music/StrangeForest.ogg") fadein 3.0

    show mSigh
    with dissolve

    "It's been a long walk just to find something that's edible and not poisonous at the same time."
    "I've made sure to mark enough trees along the way so I'll be okay going back."

    hide mSigh
    with dissolve
    show mSad
    with dissolve

    "I wonder if word has gotten out about the boat incident."
    "I hope mum and dad has received news that I'm missing..."
    "Guess it's no use thinking about it and the bigger question is how would I be able to get off this island..."

    hide mSad
    with dissolve
    show mIdle
    with dissolve

    "Anyway, food. Need to find food..."
    mc "Hmm..."

    hide mIdle
    with dissolve
    show mPumped
    with dissolve

    mc "Ah!"
    mc "I see a few nests up there!"
    "It might be a bit dangerous but if I'm careful I'll be fine."
    "Alright! Time to get myself some eggs!"

    hide mPumped
    with moveoutright

    "I started to scale the tree by jumping and grabbing hold of the thick branches."
    "It's a good thing these branches are sturdy."
    "With each branch I climbed onto, I made sure that my footing was in the correct place before going onto the next one."

    mc "... ... ..."
    mc "*huff* *pant*"
    mc "Phew... made it at last."
    "I've somehow managed to get up here."
    mc "Woah..."
    "I'm so far from the ground. I don't think anyone could survive if they fall from here..."
    "And the eggs are right there in front of me."
    "I reached out with one hand trying to grab the eggs and the other hand held firmly onto the trunk."
    "Three eggs here in total and they look kind of large too."
    "I grabbed the first egg that was closest and placed it in my pocket."
    "And then the second."
    "That third one is a bit far but I should be able to get it."
    "I stretched out as much as I can, trying my best not to lose my footing."

    stop sfx1 fadeout 1.0
    stop sfx2 fadeout 1.0
    stop Sound1 fadeout 1.0

    mc "... Hng... Eh..."
    mc "... Just a bit more..."
    mc "... Almost there...."
    mc "... Yes! Got it!"
    mc "Ah!"

    play Sound1 ("OB_music/Thrill.ogg")

    "In an instant my hand slipped from the trunk causing my body to fall."
    "UWaaaaaaaah!!!"



    show bg_black
    with fade

    "As I fell from the tree I couldn't help but close my eyes. A few branches and leaves brushed pass me as I continued."
    "My mind went blank, I couldn't think of anything else except for my dead body lying beneath the tree."

    stop Sound1
    play sfx3 ("OB_sound/HeavyPunch.ogg")
    with Pause (1.0)
    mc"... "
    extend "... "
    extend "..."
    mc "Mm...?"
    "Did I break my fall on something?"
    "It doesn't hurt..."
    "I opened my eyes slowly only to find myself being stared down by a familiar face."

    show bg_Goro2
    with fade

    play Sound1 ("OB_music/TreadingCarefully.ogg") fadein 3.0

    mc "Ah!"

    "My heart was pumping really fast and my body was shaking.\n"
    extend "The cause was because of the sudden fall from the tree but now..."
    "Just looking at him glaring at me screams dangerous!"
    "He looks like he's about to bury me six feet under!"

    g "What the hell are you playing at human!?"
    mc "I... I..."
    mc "I-It's not what you think..."
    mc "I-I wasn't trying to jump off that tree or-"

    g "Then what!?"

    mc "I was... I-I..."

    "This isn't good..."
    g "I've told you before!!\n"
    extend "Your death would cause me a lot of problems!"
    g "If you want to die that badly!\n"
    extend "I'll gladly end your life here!"
    mc "I'm sorry, I'm really, really sorry..."
    g "Save your words Human!"
    mc "P-Please listen!"
    g "Nothing you say can-"
    mc "I-I was only trying to get these..."
    "I held out the egg in my hand and pulled out the rest from my pockets."
    "It's a good thing that none of them are damaged."
    mc "... ... ..."
    g "Eggs?"
    mc "I... I just wanted to repay you somehow."
    mc "For the food that you shared with me yesterday. I didn't want you to think I'm a burden or anything. "
    extend "I just... "
    extend "just wanted to help..."
    g "... ... ..."

    stop Sound1 fadeout 2.0

    g "Hmph, whatever..."


    scene bg_forest1
    with dissolve

    show mSigh at left
    show gSigh at right
    with dissolve

    "As he dropped me to the ground I felt a sense of relief. His anger had started to subside."
    g "Instead of doing something so troublesome. You should have waited back there!"
    mc "... I didn't mean to..."
    "I honestly did thought to myself that I could be a little helpful if I tried."
    "Even if it's just finding something to eat."

    play sfx1 ("OB_sound/Cicada.ogg") fadein 3.0
    play sfx2 ("OB_sound/Birds.ogg") fadein 3.0

    g "And?"
    g "What do you plan on doing with just three eggs?"

    hide mSigh
    with dissolve
    show mFidget at left
    with dissolve

    mc "I... I guess I could cook it..."
    g "With what human?"
    mc "I, umm... "

    hide mFidget
    with dissolve
    show mSad at left
    with dissolve

    extend "I don't know..."
    "Now that I think about it, there's nothing here I could use to cook these."

    hide gSigh
    with dissolve
    show gAnnoyed at right
    with dissolve

    g "Tch..."
    g "Should've thought about it before climbing up a damn tree!"

    mc "... ... ... "

    hide gAnnoyed
    with dissolve
    show gAngry at right
    with dissolve

    g "Next time you pull some stupid shit like that. I'll personally break your legs!"

    hide mSad
    show mShock at Shake((0.16, 1.0, 0.5, 1.0), 1.0, dist=5)
    "!"
    mc "I'm sorry..."

    hide mShock
    with dissolve
    show mSad at left
    with dissolve

    mc "It won't happen again..."

    hide gAngry
    with dissolve
    show gSigh at right
    with dissolve

    g "Hmph..."
    "I feel so ashamed of myself for not being able to do anything..."
    "I don't care how...\n"
    extend "Someone... anyone..."
    "Please find me and take me home..."

    scene bg_forest2
    with fade

    "Ever since I fell from the tree he hasn't said a single word..."
    "I can't tell if he's still angry, upset, agitated or just ignoring me."

    show gPoint at right
    with dissolve

    g "Sit over there and give me those!"

    show mSad at left
    with dissolve

    mc "Yes..."

    hide gPoint
    with dissolve
    show gIdle at right
    with dissolve

    "I watched him take the eggs from me and planted them next to the already extinguished camp fire."
    "I followed his instruction and sat down on a patch of grass just a few feet behind him.\n"
    extend "In silence."
    mc "... ... ...\n"
    extend "... ... ...\n"
    extend "... ... ..."

    hide gIdle
    with dissolve
    show gSigh at right
    with dissolve

    g "Sigh..."
    g "If you want to be helpful human!"
    g "Go and gather some firewood."
    g "... ... ..."

    hide mSad
    with dissolve
    show mIdle at left
    with dissolve

    mc "Y-Yes..."

    hide gSigh
    with dissolve
    show gShy at right
    with dissolve

    g "Just..."
    g "Stay away from trees."

    hide mIdle
    with dissolve
    show mPumped at left
    with dissolve

    mc "I-I will.."

    hide mPumped
    with dissolve
    show mIdle at left
    with dissolve

    "I'm so stupid..."

    stop sfx1 fadeout 3.0
    stop sfx2 fadeout 3.0

    "There was no need to get so upset.\n"
    extend "He had every right to be angry with me."
    "For now I'll do my best to gather as many firewood as I can!"

    hide mIdle
    hide gShy
    with dissolve

    scene bg_forest4
    with fade

    play Sound1 ("OB_music/TwilightMoment.ogg") fadein (2.0)

    show mSigh
    with dissolve

    mc "Phew..."
    "I don't know much about firewood but I got the ones that looked dry enough to burn."
    "Given this is my first time, I think I did a pretty good job."
    "Collecting firewood that is..."
    "Not that it's anything to brag about..."

    hide mSigh
    with dissolve
    show mIdle
    with dissolve

    mc "I hope this is enough..."
    g "Hey human! Bring those over here!"

    hide mIdle
    show mShock

    mc "C-Coming..."

    hide mShock
    with moveoutright

    "I walked up to him and left a bunch of dry branches next to the camp fire."

    show gIdle at right
    with dissolve
    show mIdle at left
    with moveinleft

    mc "... ... ..."
    g "... ... ..."

    hide gIdle
    with dissolve
    show gSigh at right
    with dissolve

    g "You know how to start a fire human?"

    hide mIdle
    with dissolve
    show mSad at left
    with dissolve

    mc "N-No, I don't."
    g "Good!"
    g "It's best if you didn't."
    mc "... ... ..."

    hide gSigh
    hide mSad
    with dissolve
    show gIdle at right
    show mIdle at left
    with dissolve

    g "Don't want you burning the whole forest down."
    "I've never actually seen anyone setting up a camp fire before."
    "I watched carefully as he began by picking up one of the branches.\n"
    extend "He then starts rubbing the stick frantically on his palm back and forth on a tree bark."
    "The tip of the stick begins to chip away at the bark."

    hide mIdle
    with dissolve
    show mSad at left
    with dissolve

    "I can't really see how this is going to..."

    hide mSad
    with dissolve
    show mShock at left
    with dissolve

    "!"
    "Smoke is coming out..."

    hide mShock
    with dissolve
    show mIdle at left
    with dissolve

    "He's putting something on top of the smoke..."
    "Looks like shaved bits of wood."
    "He planted his face closer to the smoke and began blowing gently while making sure none of the shaved wood gets blown away."
    "... ... ..."

    hide mIdle
    with dissolve
    show mShock at left
    with dissolve

    "!"
    "It sparked up a tiny flame..."

    hide mShock
    with dissolve
    show mPumped at left
    with dissolve

    "Now he's throwing in some firewood bit by bit."
    "The fire is gradually getting bigger."
####-----------------------------------------------------------------########################
    scene bg_forest5
    with fade

    play sfx1 ("OB_sound/Fireplace.ogg")

    hide mPumped
    with dissolve
    show mShock at left
    with dissolve

    mc "So that's how a camp fire is done."
    mc "That was amazing!"

    hide gIdle
    with dissolve
    show gShy at right
    with dissolve

    g "... ... ..."
    g "You think that was amazing?"

    hide mShock
    with dissolve
    show mSad at left
    with dissolve

    mc "It is for me."
    mc "I mean, I've never been camping before."
    mc "Well not like I had the chance.\n"

    hide mSad
    with dissolve
    show mHappy at left
    with dissolve

    extend "So to see how it's done in front of me for the very first time.\n"
    extend "Is really amazing!"
    mc "It's kind of like magic!"

    hide gShy
    with dissolve
    show gHappy at right
    with dissolve

    g "Heh..."

    hide mHappy
    with dissolve
    show mIdle at left
    with dissolve

    mc "Hmm?"
    "Did he just...\n"
    extend "Smile?"

    hide gHappy
    with dissolve
    show gIdle at right
    with dissolve

    "I watched as he takes a bunch of firewood and places it on the edge of the camp fire."
    "Making sure that it doesn't come in contact with the large flame that's currently burning."
    "He takes a few more sticks and sets the tip on fire."
    "I waited in anticipation to see what he was going to do next."
    "He then drops the sticks held in his hand with the bunch up firewood and sets the rest on fire."
    "A small flame was set up, completely separate from the big one in the centre of the camp fire."

    hide gIdle
    with dissolve
    show gPoint at right
    with dissolve

    g "Bring me that rock over there."
    "I looked around to where he was pointing at."
    "This big, flat looking rock?"
    "I took hold of the odd looking rock and struggled to lift it off from the ground."

    hide mIdle
    with dissolve
    show mSigh at left
    with dissolve

    mc "Unnngh ..."
    mc "It's really heavy..."
    "What's he planning to do with this?"

    hide mSigh
    hide gPoint
    with dissolve
    show mIdle at left
    show gIdle at right
    with dissolve

    mc "Umm h-here..."
    "He grabbed the large rock with one hand as if to say it's light as a feather."
    "And placed it over on the small flames he made on the side."
    mc "... ... ..."
    "What is he waiting for?"
    "After a short time he reached out for the eggs."
    "Does he plan to cook those?"
    "But there's no frying pan how is he going to cook it?"

    hide mIdle
    with dissolve
    show mShock at left
    with dissolve

    "He cracks open the first egg and pours the contents onto the heated stone."

    play sfx2 ("OB_sound/Frying.ogg")

    "Oh I see..."

    hide mShock
    with dissolve
    show mIdle at left
    with dissolve

    "He heated up the rock and waited when it was hot enough to cook the egg on top of it."
    "Kind of like a hot plate!"
    "As I stood there watching him cook the eggs."
    "I could tell this wasn't his first time doing something like this."
    "Once the eggs are fully cooked he took a large looking leaf he had prepared and began scraping the bottom of the eggs."

    stop sfx2 fadeout 1.0

    hide gIdle
    with dissolve
    show gSigh at right
    with dissolve

    g "Here."

    hide mIdle
    with dissolve
    show mHappy at left
    with dissolve

    mc "T-Thank you..."
    "It smells really good..."
    "He even wrapped it up with a big leaf."

    hide gSigh
    hide mHappy
    with dissolve
    show gIdle at right
    show mIdle at left
    with dissolve

    g "There's some fruits over there."
    "Is that his was of saying, if the egg isn't enough have something else over there?"

    hide mIdle
    with dissolve
    show mHappy at left
    with dissolve

    mc "...Hehe...\n"
    extend "It's strange..."

    hide gIdle
    with dissolve
    show gSigh at right
    with dissolve

    g "What is?"

    hide mHappy
    with dissolve
    show mIdle at left
    with dissolve

    mc "Oh it's just that...\n"

    hide mIdle
    with dissolve
    show mSad at left
    with dissolve

    extend "This reminds me of home a little..."

    hide gSigh
    with dissolve
    show gIdle at right
    with dissolve

    g "Your... home?"

    hide mSad
    with dissolve
    show mHappy at left
    with dissolve

    mc "Yes..."
    mc "It feels a little nostalgic..."

    hide mHappy
    with dissolve
    show mSad at left
    with dissolve

    mc "I'd wake up every morning to find these on the table. They'll normally be warm like this and on a plate."
    mc "But still, I would always sit there and eat these by myself and occasionally there would be a note beside them..."
    g "... ... ..."

    hide mSad
    with dissolve
    show mHappy at left
    with dissolve

    mc "But somehow, eating them like this feels strange."

    hide mHappy
    with dissolve
    show mShock at left
    with dissolve

    mc "Oh!"

    hide mShock
    with dissolve
    show mIdle at left
    with dissolve

    mc "I didn't mean strange as in it's bad or anything."
    mc "It's more like this is how it should have been."

    hide mIdle
    with dissolve
    show mHappy at left
    with dissolve

    mc "Ahaha..."

    hide mHappy
    with dissolve
    show mSigh at left
    with dissolve

    mc "Sorry...\n"
    extend "I'm not making any sense am I?"
    g "... ... ..."

    hide gIdle
    with dissolve
    show gShy at right
    with dissolve

    g "Hmph...\n"
    extend "For a human you can talk a lot."

    hide mSigh
    with dissolve
    show mHappy at left
    with dissolve

    mc "Ahehe..."

    hide gShy
    with dissolve
    show gSigh at right
    with dissolve

    g "There's always enough food here...\n"
    extend "Warm or not."

    hide mHappy
    with dissolve
    show mIdle at left
    with dissolve

    mc "... ... ..."

    hide mIdle
    with dissolve
    show mHappy at left
    with dissolve

    mc "Thank you, "
    extend "Goro..."

    hide gSigh
    with dissolve
    show gShock at right
    with dissolve

    g "!"

    hide gShock
    with dissolve
    show gShy at right
    with dissolve

    "... ... ..."

    stop Sound1 fadeout 2.0

    jump Chapter2

    return
