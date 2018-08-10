label gWakeUp:
    stop Sound1 fadeout 1.0
    stop sfx1 fadeout 1.0
    stop sfx2 fadeout 1.0
    
    scene bg_forest2
    with fade
    
    play sfx1 ("OB_sound/Birds.ogg") fadein 3.0
    
    mc "... Mmmng..."
    g "Zzzz..."
    "The bright sunlight beaming down on my face woke me from my sleep."
    "I rubbed my eyes, yawning while strecthing my arms and legs like a cat had finished taking its nap."
    "It's morning already?"
    mc "Hmm?"
    "I turned to look beside me and saw Goro still fast asleep."
    
    scene bg_Goro12
    with dissolve
    
    "That's right. Last night..."
    "After he kissed me...\n"
    extend "We came back to the campsite and fell asleep together."
    "He's still got me wrapped up in his arms..."
    "I can't believe we were asleep like this the whole night."
    mc "Ehehe..."
    g "Zzzz..."
    "That's a cute snore for a big dragon."
    g "Ugmmh..."
    mc "... ... ..."
    g "Yawn..."
    
    scene bg_Goro13
    with Dissolve(1.5)
    
    "He looked at me while blushing slightly."
    g "O-Oh.... err..."
    extend " morning..."
    mc "M-Morning..."
    "I still feel a little embarrass and nervous looking into his eyes."
    g "Did you..."
    extend " sleep well?" 
    "I didn't just sleep well. I slept like a baby."
    "The way you embraced me last night made me feel safe and secure. If only I could sleep like that every night..."
    mc "Yeah... I slept really well."
    mc "Thanks Goro."
    
    play sfx3 ("OB_sound/Clothes.ogg")
    
    "He released me from his arms and got up from the ground."
    
    jump Chapter6
    
#####################################################################

label WakeUp:
    
    scene bg_forest2
    with fade
    
    mc "Mnggh..."
    mc "Yawn..."
    "Morning already?"
    
    show gIdle at right
    with dissolve
    
    g "Morning..."
    mc "O-Oh, good morning."
    
    show mFidget at left
    with dissolve
    
    "Goro was sitting by the extinguished campfire prodding at the ashes with a stick."
    
    jump Chapter6

#####################################################################


label Chapter6:
    
    scene bg_forest2
    with fade
    
    show gIdle at right
    with dissolve
    
    g "We're going to get a few things today. To prepare you for your journey."
    
    show mIdle at left
    with dissolve
    
    mc "Okay..."
    "That's right. The day is nearing for me to leave this island."
    g "We'll be gathering some provisions for you."
    mc "How much do we need?"
    
    hide gIdle
    with dissolve
    show gSigh at right
    with dissolve
    
    
    g "Enough for three to four days."
    
    hide mIdle
    with dissolve
    show mShock at left
    with dissolve
    
    mc "T-That much!?"
    g "You need at least that much if you want to survive."
    
    hide mShock
    with dissolve
    show mIdle at left
    with dissolve
    
    mc "Three to four days on a boat, at sea..."
    
    hide mIdle
    with dissolve
    show mSigh at left
    with dissolve
    
    mc "What if another storm comes along?"
    
    hide gSigh
    with dissolve
    show gIdle at right
    with dissolve
    
    g "That won't happen."
    
    hide mSigh
    with dissolve
    show mIdle at left
    with dissolve
    
    mc "?"
    
    hide gIdle
    with dissolve
    show gSigh at right
    with dissolve
    
    g "It's very unlikely for another one to appear."
    g "I know this because of the previous storms."
    
    hide mIdle
    with dissolve
    show mSigh at left
    with dissolve
    
    mc "That's a relief..."
    
    hide gSigh
    with dissolve
    show gPoint at right
    with dissolve
    
    g "We'll get a move on once you're ready."
    
    hide mSigh
    with dissolve
    show mHappy at left
    with dissolve
    
    mc "Okay."
    
    hide mHappy
    hide gPoint
    with dissolve
    
    scene bg_forest6
    with fade
    
    play sfx2 ("OB_sound/Cicada.ogg")
    
    play Sound1 ("OB_music/StrangeForest.ogg") fadein 3.0
    
    "It's so humid today."
    extend " The weather is really unpredictable on this island."
    "I wish it could rain a little right about now..."
    extend " just so I can cool down a bit."
    g "Here should be fine..."
    
    show mIdle at left
    with dissolve
    
    mc "Hm?"
    
    show gPoint at right
    with dissolve
    
    g "Let's take a break here [povname]." 
    "I didn't think we'd be stopping so early."
    
    hide mIdle
    with dissolve
    show mHappy at left
    with dissolve
    
    mc "I can carry on walking Goro. I'm not really tired or anything."
    
    hide gPoint
    with dissolve
    show gSigh at right
    with dissolve
    
    g "No..."
    
    hide gSigh
    with dissolve
    show gIdle at right
    with dissolve
    
    g "We'll stop here."
    "Maybe he's the one feeling tired?"
    mc  "Well alright then. Guess I'll take it easy for now."
    
    hide mHappy
    with dissolve
    
    "I planted myself on the ground and stretched out my legs."
    mc "Mmmngh... aaaah... "
    
    show mSigh at left
    with dissolve
    
    mc "Still, it's really hot today..." 
    
    hide gIdle
    with dissolve
    show gSigh at right
    with dissolve
    
    "Goro settled down by leaning next to a tree with the sun beaming down on him."
    
    hide mSigh
    with dissolve
    show mIdle at left
    with dissolve 
    
    mc "Aren't you hot Goro?"
    "He looked around aimlessly as he answered."
    
    hide gSigh
    with dissolve
    show gIdle at right
    with dissolve
    
    g "Hm?"
    g "Oh..."
    extend  " yeah... it's good."
    "What's wrong with him?\n"
    extend "Is something on his mind?"
    
    hide mIdle
    with dissolve
    show mDuh at left
    with dissolve
    
    mc "Hmm..."
    "Maybe he's just hungry."
    
    hide mDuh
    with dissolve
    show mIdle at left
    with dissolve
    
    mc "Do you want me to go and find something for you to eat while you rest."
    
    hide gIdle
    with dissolve
    show gShock at right
    with dissolve
    
    g "What!?"
    g "N-No, just stay there."    
    mc "You sure you're okay?"
    "I looked at him with concern as he was acting a little different than usual."
    
    hide gShock
    with dissolve
    show gShy at right
    with dissolve
    
    g "I'm fine."
    g "I'm going to head off for a little bit."
    g "Promise me you'll stay here."
    "What's gotten into him all of a sudden?"
    
    hide mIdle
    with dissolve
    show mSad at left
    with dissolve
    
    mc "You're acting really strange Goro...\n"
    extend "What's-"
    
    hide gShy
    with dissolve
    show gAngry at right
    with dissolve
    
    g "Just promise me [povname]!"
    
    hide mSad
    with dissolve 
    show mSigh at left
    with dissolve
    
    "He looks really serious. The way he stares into my eyes forces me to nod my head in return."
    "That scared me a little bit especially with the way he reacted."
    
    hide gAngry
    with dissolve
    show gIdle at right
    with dissolve
    
    g "I'll be back soon. Don't go anywhere."
    
    hide mSigh
    with dissolve
    show mPumped at left
    with dissolve
    
    hide gIdle
    with moveoutright
    
    mc "W-Wait Goro!"
    "I watched him as he hurried off into the woods, brushing pass the tall grass and leaves."
    
    hide mPumped
    with dissolve
    show mSad at left
    with dissolve
    
    mc "What was..."
    extend " that all about?"
    "Something just doesn't feel right..."
    "He looked quite nervous or maybe a little on edge?\n"
    "Everything was fine up until we came into the woods..."
    
    hide mSad
    with dissolve
    
    scene bg_forest6
    with fade
    #scene repeat with fade 
    
    show mSad
    with dissolve
    
    mc "Goro..."
    "Why hasn't he come back yet?" 
    "I feel like I've been sitting here for a long time."
    
    hide mSad
    with dissolve
    show mSigh
    with dissolve
    
    "I'm starting to get a bit worried...\n"
    extend "Maybe I should go look for him..."
    "But what if he comes by when I leave here?"
    "Also I kind of promised him not to move from this spot..."
    mc "Sigh..."
    "What am I to do now..."
    "I lowered my head down in frustration, feeling restless and unable to think of what I should be doing."
    mc "And here I thought we'd be spending the last day or two together gathering some food..."
    "The thought of food made my stomach growl."
    
    stop Sound1 fadeout 2.0
    
    mc "I'm so hungry..."
    
    hide mSigh
    with dissolve
    show mIdle
    with dissolve
    
    mc "Hm?"
    
    play sfx3 ("OB_sound/Clothes.ogg")
    
    "A sudden rustling from a bush in the distance caught my attention."
    mc "Goro?\n"
    extend "Is that you?"
    "A chill ran down my spine. I got scared because there were no responses when I called out."
    
    play Sound1 ("OB_music/Creepy.ogg")
    
    hide mIdle
    with dissolve
    show mShock
    with dissolve
    
    mc "Goro, you there?"
    "Sweat began to form on my skin from the uncertainty in front of me."
    "I stood up slowly as I looked around, observing and listening to my surrounding."
    
    hide mShock
    with dissolve
    show mFidget
    with dissolve
    
    mc "G-Goro, if you're there please answer me."
    
    stop Sound1 fadeout 2.0
    
    mc "... ... ..."
    "Silence took over with nothing but the sound of chirping birds and buzzing cicadas in the forest."
    
    hide mFidget
    with dissolve
    show mSigh
    with dissolve
    
    mc "Phew..."
    
    play sfx3 ("OB_sound/Clothes.ogg")
    stop sfx2 fadeout 2.0
    stop sfx1 fadeout 2.0
    
    "The bushes from a distant rustled again and this time..."
    
    hide mSigh
    with dissolve
    show mShock at left
    with dissolve
    
    play Sound1 ("OB_music/Thrill.ogg")
    
    mc "WAH!!"
    
    show tiger_flip at right
    with moveinright
    
    "It's a tiger!\n"
    extend "A-And it's huge too!"
    t "Grr..."
    "Th-That size isn't normal!\n"
    extend "Wh-What should I do. It's snarling at me!\n"
    extend "Does it think I'm its prey!?"
    "I-Im scared..."
    extend " my legs won't move..."
    "I watched in terror as the large feline circulated around me from a distance."
    "Tears began to form as I imagined the worst case scenario."
    "My body became stiff, my heart was beating extremely fast and my breathing got heavier by the second."
    t "Grrr..."
    t "Growl!!!"
    "I flinched as it bared its fangs and leapt towards me."
    mc "H-Help!!"
    "...Goro..."
    
    scene bg_black
    with fade
    
    "I shut my eyes in fear and curled up into a ball."
    "My body wasn't ready to face the impact of the moment where the wild beast would sink its deadly teeth into me."
    mc "... ... ..."
    
    scene bg_black
    with fade
    
    "The sound of my heartbeat was ringing loudly in my ear.\n" 
    extend "It was the only thing left that I could hear."
    g "WHAT ARE YOU DOING!?\n"
    extend "GET UP!"
    
    scene bg_forest6
    with dissolve

    "I opened my eyes to find Goro on the floor and the ferocious tiger on top of him."
    "He struggled continuously, trying to hold back the giant feline from its deadly claws."  
    
    show mShock at left    
    show gAngry_flip
    show tiger_flip at right
    with dissolve
    
    hide mShock
    with dissolve
    show mAngry at left
    with dissolve
    
    mc "Goro!"
    g "RUN!"
    "His voice echoed loudly as I stood there watching helplessly."
    mc "B-But-"
    g "I SAID RUN!"
    g "GET OUT OF HERE!"
    "I fumbled as I began to run but got back on my feet."
    "W-What should I do?"
    "At this rate... Goro will..."

    menu:
        "Get up and run for it.":
            g "GET OUT OF HERE!"
            "I turned on my heels and began running away. I felt awful, powerless, pathetic and useless."
            
            hide mAngry
            with moveoutleft
            
            hide gAngry_flip
            hide tiger_flip
            with dissolve 
            
            stop Sound1 fadeout 3.0
            
            scene bg_forest6
            with fade
            
            "A mixture of feelings began to well up inside me. Teardrops began to form and roll off from my face while I ran."
            
            scene bg_Goro14
            with Dissolve (1.0)
            
            play Sound1 ("OB_music/A Void.ogg") fadein 3.0
            
                        
            "I don't even know where I should run to."
            "My mind was completely overwhelmed by the tiger and bad things that might happen to Goro."
            "I began to worry for Goro's safety and started to slow down..."
            mc "... ... ..."            
            "I'm such a coward for leaving him behind..."
            "All this time I've been running..."
            "Running away..."
            extend " from my past because I was scared to face it..."
            "Running away"
            extend " from my parents because I didn't have the courage to talk to them properly..." 
            "And now..."
            extend " from Goro."
            "Everything. All of it."
            "I'm always trying to find the easiest way out when it comes to things that matter..."
            mc "I..."
            "I don't want to run anymore."
            mc "... ... ..."
            
            stop Sound1 fadeout 3.0
            
            "I'm tired of running!"
            
            scene bg_forest6
            with fade
            
            play sfx1 ("OB_sound/Birds.ogg")
            play sfx2 ("OB_sound/Cicada.ogg")
            
            "I began sprinting towards the campsite."
            "It's not far but I can make it there and back!"
            "I ran like I've never ran before and arrived there sweating and breathing hard."
            
            scene bg_forest2
            with dissolve
            
            mc "Huff... huff..."
            "It should be here somewhere!"
            "I shuffled around near the campfire looking for a certain item."
            mc "Got it!"
            
            show bg_Goro15
            with moveinbottom
            
            "It was the rock that Goro had sharpened that I'd use for cooking."
            mc "This should do!"
            "I held onto the object and ran back at the scene as quick as I can."
            
            hide bg_Goro15
            with moveoutright
            
            scene bg_forest6
            with fade
            
            "The thought of Goro being attacked and covered in blood pushed my body to move even quicker."
            "Running through the forest, ignoring my surrounding, cutting and bruising myself. I didn't care. At this precise moment whatever happens to me are unimportant."
            "Right now I've got to go back and save Goro!"
            
            
            stop sfx2 fadeout 3.0
            stop sfx1 fadeout 3.0
            
            play Sound1 ("OB_music/Creepy.ogg")

            "Goro!"
            g "Huff... Nghh..."
            
            show gBlood at right
            show tiger at left
            with dissolve
            
            "I came into view with the tiger at a distance. Goro was backed up onto a tree with his left arm dripping with blood."
            "The tiger seems to be on its guard as it circled around Goro."
            "This is my chance."
            "Goro kept his watch on the tiger for any sudden movement."
            "They both snarled at each other. Like a predator on it's prey."
            "I gripped onto the weapon tightly trying to muster up the courage and crept up to the nearest tree."
            "The tiger didn't seem like it had noticed my presence.\n"
            extend "I waited until it was close enough for me to reach."
            "My heart throbbed all the way up to my throat. I swallowed hard."
            
            stop Sound1 fadeout 3.0
            
            "Almost there..."
            "The tiger's gaze was fixed onto Goro. Its back became visible to me."
            
            play Sound1 ("OB_music/Thrill.ogg")
            
            "Here!"
            
            show bg_Goro15 at right
            with moveinright
            
            "I leapt out at the tiger with the weapon ready to strike."
            
            hide bg_Goro15 
            with moveoutleft
            
            g "[povname]!?"
            "It was sudden but the tiger leapt to the side and almost avoided my attempt to attack it."
            
            hide tiger
            hide gBlood
            with dissolve
            
            t "Grrrowl!!"
            "The tiger growled in pain. Seems like I just manage to graze it on its side."
            "I fell onto the ground, face first, as the weapon flew out of my hand."
            g "[povname]!\n"
            extend "IDIOT!"
            g "WHAT ARE YOU DOING HERE!?"
            "I turned over to look at the tiger. It's focus was now on me."
            g "GET UP!"
            "Those blood thirsty feline eyes staring down at me gave me shivers."
            g "MOVE!"
            mc "I-I... I c-c-can't..."
            g "GRR..."
            "The ferocious tiger leapt towards me, claws ready and fangs covered in blood."
            t "GROWL!"
            mc "AAHHHH!!!"
            g "[povname]!!!"  
            g "GRRRRR!"
            "Goro picked up the weapon on the floor and thrust it at the tigers head with extreme force."
            
            stop Sound1 
            
            play sfx3 ("OB_sound/HeavyPunch.ogg")
            
            "The wild animal fell onto the ground, laying on its side and completely still. Blood was now oozing out of its head" 
            "I sat there trembling as I looked up to Goro with his left arm dripping in his own blood."
            
            show gBlood at right
            with dissolve
            
            show mSad at left
            with dissolve
            
            g "... ... ..."
            g "Why did you come back?"
            mc "A... a.. I-I-"
            "I wasn't able to find the words that I wanted to say. In fact I couldn't, my mind was still in shock from all that's happened."
            g "WHAT HELL WERE YOU THINKING!?\n"
            extend "YOU COULD OF DIED THERE!"
            mc "Bu-But... I-I..."
            g "I TOLD YOU TO RUN!"
            g "NOT COME BACK AND GET YOURSELF KILLED!"
            g "YOU HUMANS WILL NEVER LEARN!"
            
            hide mSad
            with dissolve
            show mAngry at left
            with dissolve
            
            play Sound1 ("OB_music/A Void.ogg") fadein 2.0
            
            mc "YOU'RE WRONG!"
            g "!"
            mc "I-I can't blame you for getting angry and..."
            extend " I-I'm sorry I came back..."
            mc "I'm sorry I tried doing something so dangerous without thinking it through properly."
            mc "But!\n"
            extend "I'm tired of running!"
            mc "I don't want to run any more. Not now. Not ever.\n"
            extend "I want to face things head on!"
            "He looked at me, took a deep breath and sighed."
            g "Tch..."
            g "Don't do anything like that ever again."
            g "Otherwise..."
            extend " I won't be able to stop worrying..."
            
            hide mAngry
            with dissolve
            show mHurt at left
            with dissolve
            
            mc "I could say the same thing to you..."
            mc "You told me to run away and I did it without thinking."
            mc "But all that time while I was running away. I was thinking of you."
            
            hide mHurt
            with dissolve
            show mSad at left
            with dissolve
            
            mc "I couldn't stand the thought of something bad had happened to you."
            "My heart called out to him, my feelings poured out and everything else that was bottled up inside of me."
            "I don't think I could hold it all in anymore, I've come to like him a lot."
            "And everything that's happened proved it to me today."    
            "That I..."
            mc "I..."
            extend "I really like you Goro!"
            mc "If something ever happens to you..."
            "I was so caught up confessing my personal feelings towards him that I began to cry."
            
            hide mSad
            with dissolve
            show mCry at left
            with dissolve
            
            mc " I don't know what I'll do without you..."
            g "Don't be stupid..."
            "I know for certain that my feelings and words had reached him because..."
            
            
            hide mCry
            hide gBlood
            with dissolve
            
            scene bg_Goro16
            with fade
            
            g "I like you too [povname]."
            "I'm so happy just hearing those words..."
            g "If anything happens to you." 
            extend " I don't think I can ever forgive myself."
            mc "I'm sorry... I'm so sorry..."
            g "It's alright. I'm not angry at you..."
            g "You don't need to apologise..."
            "I gave a faint nod while I wiped my tears off my face."
            g "For now... let's go back to camp..."
            
            scene bg_forest6
            with dissolve
            
            show gBlood at right2
            show mSad at left2
            with dissolve
            
            mc "W-Wait, aren't you hurt?"
            g "It's only a scratch..."
            "Those wounds doesn't look like a minor scratch to me."
            
            hide mSad
            with dissolve
            show mPumped at left2
            with dissolve
            
            mc "Let me see ..."
            "He didn't hesitate while I moved over to inspect his arm."
            "I watched in pain, even though I wasn't the one with a wounded arm. I still felt hurt inside seeing him like this."
            
            hide mPumped
            with dissolve
            show mSad at left2
            with dissolve
            
            mc "This looks painful..."
            "I planted my palm gently on his arm where his wounds were visible."
            
            show gBlood at Shake((0.67, 1.0, 0.5, 1.0), 1.0, dist=5) 
            
            
            "He flinched as I touched him."
            g "... Ugh..."
            mc "This looks bad. We need to get this treated."
            g "I'm okay. No need to-"
            
            hide mSad
            with dissolve
            show mPumped at left2
            with dissolve
            
            mc "NO!"
            g "!"
            
            hide mPumped
            with dissolve
            show mSad at left2
            with dissolve
            
            mc "I won't stand by and do nothing..."
            extend " you've saved me and protected me, again and again..."
            g "You're really stubborn you know that..."
            mc "... I don't care..."
            "I could say the same to you."
            g "Let's go back to the campsite. There should be some herbs nearby you can use."
            
            hide mSad
            with dissolve
            show mIdle at left2
            with dissolve
            
            stop Sound1 fadeout 2.0
            
            mc "Okay."
            "I'm so glad things didn't turn out for the worse."

            scene bg_forest3 
            with dissolve 
            
            play sfx1 ("OB_sound/Crickets.ogg") fadein 3.0
            play sfx2 ("OB_sound/Fireplace.ogg") fadein 3.0
            
            "It wasn't long before I treated his arm with the herbs he suggested using."
            "We went to the hot spring earlier and I even helped him wash off the blood on his body and clothes." 
            
            show gShyU at right2
            with dissolve 
            
            g "... Mmm..."
            
            show mIdle at left2
            with dissolve
            
            mc "Does it hurt?"
            g "It's fine. Just a little uncomfortable."
            "We didn't manage to go out and get those supplies we needed but that's alright.\n" 
            "Right now he's more important to me than leaving this island."
            "As I sat beside him watching the campfire flicker gently in the night. I stood up and turned to look at him."
            
            hide gShyU
            with dissolve
            show gIdleU at right2 behind mIdle
            with dissolve
            
            g "Hm?"
            g "What's wrong [povname]?"
            
            hide mIdle
            with dissolve
            show mBlush at left2
            with dissolve
            
            mc "I..."
            "Just say it [povname]. Just be brave and come out with it."
            mc "Y-You know... I've been thinking..."
            mc "I've really come to like you a lot and you mean a lot to me too."
            
            hide gIdleU
            with dissolve
            show gShockU at right2 behind mBlush
            with dissolve
            
            g "W-What's this all of sudden!?"
            "What am I trying to say?"
            mc "Like today, you helped me, you saved me and you use to hate me and all."
            "I'm not making any sense here am I?"
            mc "S-So..."
            extend " what I'm trying to say is..."
            g "... ... ..."
            
            hide gShockU 
            with dissolve
            show gHappyU at right2 behind mBlush
            with dissolve 
            
            g "Hehe..."
            
            hide gHappyU 
            with dissolve
            show gLaughU at right2 behind mBlush
            with dissolve 
            
            g "Hahaha."
            
            hide mBlush
            with dissolve
            show mShock at left2
            with dissolve
            
            mc "W-What's so funny?"
            g "It's nothing..."
            extend " you really are special..."
            
            hide mShock
            with dissolve
            show mFidget at left2
            with dissolve
            
            mc "Well sorry for being different..."
            
            hide gLaughU 
            with dissolve
            show gBlushU at right2 behind mFidget
            with dissolve
            
            g "That's not what I meant..."
            extend " I've never been more happier."
            g "You showed me something that no other human being has ever shown me."
            g "And thanks for saving me back there..."
            mc "E-Eh..."
            g "You really are..."
            
            hide mFidget
            with dissolve
            show mShock at left2
            with dissolve
            
            mc "W-Wait!"
            mc "Don't say it..."
            g "... ... ..."
            "Just come out with it already..."
            
            hide mShock
            with dissolve
            show mSigh at left2
            with dissolve
            
            "I closed my eyes and uttered those three words that I thought I would never say in my entire life." 
            
            hide mSigh
            with dissolve
            show mBlush at left2
            with dissolve
            
            play Sound1 ("OB_music/Twinkle.ogg") fadein 3.0
            
            mc "I love you..."
            g "... ... ..."
            g "I..."
            g "I love you too..."
            
            hide gBlushU
            with dissolve
            
            "He turned to stare at the camp fire, face red and flustered."
            
            hide mBlush
            with dissolve
            
            "I sat back down next to him and also watched the warm fire burning in front of us."
            g "I love you [povname]."
            "He said it again."
            "I looked up to him and repeated the same words."
            mc "I love you too Goro..."
            
            stop Sound1 fadeout 3.0
            
            "He lowered his head, his face getting closer and closer. Until his lips met mine."
            
            scene bg_Goro17
            with fade
        
            mc "... ... ..."
            g "... ... ..."            
            "I've never really given it much thought when kissing..."
            "After all, he is my first..."
            "I've seen this in many T.V series and dramas. That when kissing, I should push my tongue out to make it come in contact with his." 
            "It's such a strange feeling but..."
            g "... Mmmnghh ..."
            "It's so arousing..."
            mc "...Haa..."
            
            scene bg_forest3
            with fade
            
            play Sound1 ("OB_music/Silence.ogg") fadein 3.0
            
            
            "Our lips parted and all that left is a very strong feeling between my legs." 
            g "I-I've never done this before..."
            "Me neither but...\n"
            extend "I've seen a few adult videos before to know what needs to be done in these situation."
            "I better make the first move then."
            mc "... Just relax for now..."
            g "O-Okay..."
            "The cloth covering his private area is all pent up. I can see a huge tent forming." 
            "Where did that come from?"
            "I lowered my hand to rub over his tented area."
            g "... ... ..."
            mc "Could you..."
            extend " stand up for me?"
            "He paused for a moment and stood up."
            
            play sfx3 ("OB_sound/Clothes.ogg")
            
            "I removed the last piece of cloth he had on his body. I wasn't quite sure what to expect but..."
            
            show bg_xGoodL at left
            with moveinleft
            
            "I couldn't imagine anything bigger than this. His cock was huge in length and girth."
            "Well, this is a surprise. I've never seen his cock before..."
            "So when he's aroused. His cock comes out of this slit..."
            "I tried to wrap my small hand around his huge member and began stroking him gently."
            g "Ngg..."
            mc "I-Is that okay?"
            mc "Does it hurt?"
            g "N-No..."
            g "I-It..."
            extend " feels good..."
            "Hearing him say that makes me happy and even more aroused..."
            
            show bg_xGoodR at right
            with moveinright
            
            "I planted my lips around the tip of his cock and began licking it slowly and gently. Almost like I was savouring a very cold ice-lolly."            
            "I can feel him trembling with pleasure..."
            "I began pushing his cock into my mouth, it's so big that I could only take in so much. Not even half way down the shaft."
            
            play sfx4 ("OB_sound/xSuck.ogg")
            
            mc "... Mmmfff..."
            extend "haaa..."
            g "U-Ugghh..."
            "He began to tense up as I rubbed and sucked on his cock."
            g "[povname]..."
            g "I-I can't hold it back... it's coming..."
            "I knew what he'd meant, it felt so good for me that I too didn't want to stop."
            g "U-U-Uaaaagghh!!!"
            
            stop sfx4 
            
            hide bg_xGoodR
            hide bg_xGoodL
            show bg_xGoodRc at Shake((0.50, 1.0, 0.5, 1.0), 1.0, dist=5)
            with flash
            
            "The amount of semen he shot out was incredible. So much that I had to pull myself away from him." 
            "Thick white liquid trickled from my mouth as I gasped for air. Even though I had stopped, I watched in amazement as he continued to cum."
            g "Angghh!"
            "More of his semen poured out like a fountain. Eventually, the ground in front of him was completely covered in cum."
            g "Huff... Huff..."
            "I was so aroused that pre cum began for leak out and onto my shorts."
            "I couldn't contain myself any longer. I stood up to take off my clothes in a hurry and began stroking my cock." 
            
            hide bg_xGoodRc
            with dissolve
            
            g "... Stop ..."
            mc "W-Why?"
            "Goro sat down and fondled with my cock. Compared to his, mine looks really small. I felt slightly embarrassed." 
            g "T-This time, I'll do it for you."
            "I watched as he put my cock in his mouth and began wrapping his tongue around me."
            
            play sfx4 ("OB_sound/xSuck.ogg")
            
            "He sucked on it slowly and gently. His tongue felt amazing, I never knew it could feel this good!"
            "This extremely tingly sensation and something tickling in my groin..."
            "It was then that I knew I was about to cum too."
            mc "A-Ahh... G-Goro... I'm coming..."
            mc "P-Please... you have to stop..."

            "Even though he heard me loud and clear. He never stopped. His momentum became faster until I couldn't hold it in any longer."
            mc "A-Ahhhhh!"
            "I arched back and tensed up as I felt my tingling sensation peaked. Dollops of cum shot out of my cock until I couldn't cum anymore."
            
            
            scene bg_forest3
            with flash
            
            "I looked down to see Goro's lips still wrapped around my member."
            mc "Y-You can let go now Goro..."
            "I noticed him gulping down the semen I shot out."
            
            stop sfx4
            
            mc "W-Wha... y-you... didn't have to..."
            g "I-It's okay... don't worry about it..."
            g "It was really nice..."
            mc "O-Oh...."
            "Hmm?"
            "His cock is still erect. Did sucking mine made him hard again?"
            g "S-So..."
            extend  " w-what should we do next?"
            "Does he still want more?"
            "Not that I mind, I'm still hard just looking at his."
            mc "W-Well... there's something we can try..."
            mc "I... need you to stay still for me..."
            g "Okay..."
            "I climbed over Goro as he sat there nervously. I placed my hands on his chest and lowered my hip down."
            "He's really big. I hope I can take it. Even if it is just a little."
            "I rubbed his cock up and down in between my butt cheeks as I tried to stimulate him." 
            "It's a good thing that he's still nice and wet. I adjusted myself until I felt my tight hole come in contact with his cock."
            mc "Try not to move Goro..."
            g "Y-Yeah..."
            
            scene bg_xGood3
            with dissolve
            
            "I felt the tip of his huge cock gradually pushing against me. It hurts a little bit... this feeling around my hole makes me want more." 
            
            play sfx4 ("OB_sound/xWet.ogg")
            
            "I pushed further ever so slowly and gently down on his pre cum covered cock."
            mc "Nggh.."
            g "Unf..."
            g "You okay?"
            mc "Y-Yeah, I'm okay..."
            mc "P-Please... can you hold me Goro?"
            "He wrapped his hands around me tightly as I went for the last push."
            mc "Gaaaa!"
            mc "... Huff... hufff..."
            "I can feel my body heating up, sweating and shaking. His big hard cock was buried deep inside of me." 
            g "[povname]..."
            g "I-It feels so good..."
            mc "M-Me too... I've never felt anything like this before."
            g "I love you [povname]."
            "I looked up to Goro and found myself kissing him passionately."
            mc "... Haaa.."
            "I can't hold on any longer..."
            mc "I want more..."
            g "M-More?"
            mc "Lift me from my bottom..."
            
            play sfx4 ("OB_sound/xSlapping.ogg")
            
            "He placed his palm on each side of my buttocks and lifted me up slightly, I pushed down again and felt his cock rubbing my insides."
            mc "Ngg..."
            g "Ahhh..."
            "He placed his hand on my hip and began moving me faster."
            "Each push made me moan with intense pleasure."
            mc "N-Not so fast Goro..."
            g "I... I can't..."
            "I can't hold back any longer!"
            g "I'm coming [povname]!"
            mc "Me too..."
            
            scene bg_xGood3c at Shake((0.50, 1.0, 0.5, 1.0), 1.0, dist=5)
            with flash
            
            stop sfx4
            
            "He shot his warm cum all inside, filling me to the brim. There was so much cum that most of it leaked out."
            "We embraced each other with love, panting heavily, trying to catch our breath."
            "Goro squeezed me in his arms gently, hugging as if telling me not to go..."
            g "I love you..."
            "If only time would stop because I wouldn't mind staying like this together and forever."
            mc "I love you too..."
            "But I know..."
            extend " I have to leave..." 
            extend " there are things that I have to do."
            
            stop sfx1 fadeout 2.0
            stop sfx2 fadeout 2.0
            stop Sound1 fadeout 2.0
            
            "That I must face when I get back..."
            
            
            jump Chapter7

        "Pick up the nearest and biggest looking stick.":
            
            show gAngry_flip
            show tiger_flip at right
            with dissolve
        
            hide mAngry 
            with dissolve
            show mPumped at left
            with dissolve
            
            "I looked around searching frantically for a stick that can be used as a weapon."
            "Wait for me Goro. I'll help you!"
            "I panicked and hesitated while looking for a sturdy stick. I turned around and beside the tree laid a promising weapon."
            mc "That should do!"
            g "WHAT THE HELL ARE YOU DOING!?"
            g "I TOLD YOU TO RUN!"
            mc "NO!"
            mc "I'M GOING TO SAVE YOU!"
            
            show gAngry_flip at left
            with moveoutleft
            
            hide mPumped
            with dissolve
            show mAngry 
            with moveinleft
            
            "I picked up the weapon and ran towards the tiger, swinging randomly in front of me hoping to hit the feline."
            mc "GET AWAY FROM GORO!"
            "I swung hard missing every hit as the tiger avoids all of my attacks." 
            t "GROOOWL!!!"
            mc "GET AWAY!!!"
            g "STOP [povname!]!!"
            "I continued with my frenzy of attacks. I assumed they work because the tiger started backing away."
            t "GROWL!!"
            
            show tiger_flip at Shake((0.85, 1.0, 0.5, 1.0), 1.0, dist=5)
            
            "The giant feline leapt towards me and clawed through the stick I had in my hands."
            
            play sfx3 ("OB_sound/Hit.ogg")
            
            hide mAngry
            show mShock at Shake((0.50, 1.0, 0.5, 1.0), 1.0, dist=5)
            with dissolve
            
            "I fumbled and fell to the ground."
            
            hide mShock
            with dissolve
            show mCry at left2
            with dissolve
            
            mc "N-No... don't come near me..."
            "Completely powerless without a weapon and unable to move. My body felt heavy as my eyes met the beast's bloodlust gazes."
            g "[povname]!!"
            "The tiger leapt at me, jaws wide open, claws ready to strike."
            "And then."
            
            #Scene show Goro with tiger on him
            
            show mCry at left2
            with moveoutleft
            
            hide gAngry_flip
            show gBlood_flip at Shake((0.60, 1.0, 0.5, 1.0), 1.0, dist=5) behind mCry, tiger_flip
            with redFlash
            
            play sfx3 ("OB_sound/Hit.ogg")
            
            g "ARGHHH!!!"
            
            hide mCry
            with dissolve
            show mShock at left2
            with dissolve 
            
            "I watched in absolute horror, eyes wide with tears flowing." 
            "The tiger struck its sharp claws into Goro with its fangs bared deep into his neck, blood pouring all over his body."
            g "G-GRRRRRAAAAA!!!"
            "Goro retaliated with his fists, punching the sides of the tiger. I furry of hits landed and eventually it loosened its grip."
            
            play sfx3 ("OB_sound/Hit.ogg")
            
            "As the feline stumbled Goro held up both his hands together above himself and stuck down at the tiger's head with extreme force."
            
            play sfx3 ("OB_sound/HeavyPunch.ogg")
            
            show tiger_flip
            with redFlash 
            hide tiger_flip
            with moveoutbottom
            
            "The skull of the feline cracked upon the impact."
            
            stop Sound1 fadeout 5.0
            
            "I shook in fear, watching the horrible scene come to an end. The tiger was dead on the floor with Goro slumped to the ground. He fell onto his front and laid there unable to move."
            
            hide gBlood_flip
            with moveoutbottom
            
            play sfx3 ("OB_sound/HeavyPunch.ogg")
            
            hide mShock
            show mAngry at Shake((0.50, 1.0, 0.5, 1.0), 1.0, dist=5) 
            
            mc "G-GORO!!!"
            "I ran up to him, knees on the ground hands on his heavily wounded neck."
            
            hide mAngry
            with dissolve
            show mCry
            with dissolve
            
            mc "N-No... no..."
            extend " Goro!"
            mc "W-Wake up, p-please wake up..."
            
            play Sound1 ("OB_music/Sadness.ogg") fadein 3.0
            
            scene bg_badEnd
            with fade
            
            "I cried my heart out as I watched him lay there covered in his blood."
            g "Don't cry..."
            "Blood continued to pour out of his wound, I pressed against it with my hands. Praying and hoping that it will stop." 
            mc "N-No... I-"
            g "... I'm sorry..."
            mc "W-Why arge..."
            extend " ou apologising f-for?"
            g "I'm... sorry... I..."
            g "lo..."
            extend " ve..."
            extend " yo..."
            "His breathing came to a stop. My heart sank deep into my stomach. My world turned to a shade of grey."
            "I yelled out, screaming, shouting at Goro and nudging him."
            mc "No..."
            extend " please don't go..."
            extend " don't..."
            
            stop Sound1 fadeout 3.0
            
            extend " leave me all alone..." 

            scene bg_forest2
            with fade
            
            show mHurt
            with dissolve
            
            "Goro never woke up again. No matter how much I cried. I stayed beside him all night with never ending tears." 
            "The next day, I dragged Goro's body to the area where we'd spend our nights together."
            "It didn't matter how much I struggled, I wanted what was best for him..."
            extend " for us."
            "The camp fire was cold, nothing remained but his body beside the ashes."
            "No words can describe how I feel. Regret was one of the worse feelings that played on my mind."
            "I gathered the provision that we had set out to do yesterday and made my way to the boat."
            
            scene bg_boat2
            with fade
            
            "It didn't matter if I leave here or go back home. Without Goro, everything seemed meaningless."            
            "I threw my provisions into the boat and moved it to the beach."
            
            scene bg_beach
            with dissolve
            
            play sfx1 ("OB_sound/Seashore.ogg") fadein 3.0
            
            show mSad
            with dissolve
            
            mc "... .... ..."
            mc "I..."
            "I took hold of the food I'd gathered and tossed it onto the sandy beach."
            mc "I'm going to leave Goro..."
            mc "Don't worry..."
            extend " I'll see you again."
            
            hide mSad
            with dissolve
            show mCry
            with dissolve
            
            mc "Very soon."
            
            hide mCry 
            with dissolve
            
            "I pushed the boat out to the ocean and climbed into it."
            "I laid there with my eyes closed, basking in the sun."
            "Hoping once I wake up..."
            
            stop sfx1 fadeout 3.0
            
            extend " that this... "
            extend " was all just a very bad dream."
            
            scene bg_endscene
            with fade
            with Pause (2.0)

        
        "Grab the nearest rock.":
            
            show gAngry_flip
            show tiger_flip at right
            with dissolve
        
            hide mAngry 
            with dissolve
            show mPumped at left
            with dissolve
            
            "I picked up a heavy looking stone beside my foot."
            g "WAIT [povname]!"
            g "DON'T DO IT!"
            
            hide mPumped 
            with dissolve
            show mAngry
            with dissolve
            
            play sfx3 ("OB_sound/Hit.ogg")
            
            "I threw the rock at the tiger with enough force that it managed to get its attention."
            g "NO!"
            
            hide mAngry 
            with dissolve
            show mShock
            with dissolve
            
            "The giant feline began to approach me."
            t "MRRRR!!"
            
            hide mShock 
            with moveoutright
            
            "I turned my back against it and darted off into the forest."
            
            hide tiger_flip 
            with moveoutright
            
            scene bg_forest6
            with fade
            
            "My heart pounded as I ran, droplets of sweat began to form on my forehead."
            "The forest was so dense that I brushed past tree sticks, twigs,  leaves, rocks and other greenery."
            "Bruises and cuts began to form on my body but even so I ran. The tiger was chasing behind me catching up to me by the second."
            "I tripped up from the roots of a tree and fell to the ground."
            
            show mCry_flip at Shake((0.50, 1.0, 0.5, 1.0), 1.0, dist=5) 
            
            mc "AH!"
            t "GROWWWL!"
            
            show tiger at Shake((0.1, 1.0, 0.5, 1.0), 1.0, dist=5) 
            with redFlash
            
            "I panicked and turned over to witness the approaching feline jumping towards me."
            "It's teeth sank into my neck with its huge claws pushing my body down."
            
            play sfx3 ("OB_sound/HeavyPunch.ogg")
            
            "I screamed in excruciating pain as the deadly tiger mauled me across the ground."
            
            stop Sound1 fadeout 3.0
            scene black
            with fade
            
            "From there I had lost all consciousness. Cold drops of tears fell onto my face waking me from my sleep."
            "When I came to, my vision was covered in red."
            
            scene bg_badEnd2
            with fade
            
            play Sound1 ("OB_music/Sadness.ogg") fadein 3.0
            
            "My body felt numb and cold."
            "I looked up. Only to find Goro staring back at me full of tears."
            g "[povname]..."
            g "You idiot."
            g "Why did you go and do something like that..."
            "I've never seen him so hurt like that before. I tried to reply but no words came out of my mouth."
            g "I-I'm so..."
            mc "I-t's.... o-okay..."
            "I managed to squeeze out a few words. My vision started to blur and Goro's face began to fade."
            mc "I-..." 
            mc " so...rry..."
            g "Idiot..."
            extend " you'll be okay..."
            g "Just hold on for me!"
            "I'm sorry Goro but it seems like I can't hold on for much longer."
            "I put every ounce of strength that was left in me and smiled back. My vision began to fade into darkness and eventually into nothingness."
            
            stop Sound1 fadeout 3.0
            g "AAAAAAARRRRRRRRRRRRGHHHHHHH!!!!!!!!!"
            
            scene bg_endscene
            with fade
            with Pause (2.0)
            
return