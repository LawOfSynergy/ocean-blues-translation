label mMaze:
    
    "Which way should I go?"
    
    menu: 
        "Go left, it looks brighter.":
            
            scene bg_forest1
            with fade
            
            "... ... ..."
            "Doesn't look like I'm getting anywhere. These bugs are beginning to annoy me..."
            extend " they look creepy too..."
            "Now what should I do?"
            
        "Go right, maybe you'll get lucky.":
            
            scene bg_beach
            with fade
            
            stop Sound1
            play sfx1 ("OB_sound/Seashore.ogg")
            
            msub "Okay..."
            "Somehow I managed to get back to where I started..."
            "Great now what?"
            "I stood there under the sun, sweating and hungry."
            msub "Oh look a coconut!"
            "I picked up the tropical fruit and shook it."
            msub "... ... ..."
            msub "Sounds empty..."
            "I tossed the coconut onto the sand full of dissapointment."
            msub "Great..."
            extend " better go back into the forest and look for something edible."
            
            stop sfx1
            play Sound1 ("OB_music/StrangeForest.ogg") fadein 2.0
            
            scene bg_forest1
            with fade
            
            jump mMaze2
            
        "Keep walking.":
            
            jump gCont
            
            
label mMaze2:
    
    "Hmm... this isn't good..."
    "I think I took the wrong turn."
    
    menu: 
        "Just carry on walking. Don't doubt yourself.":
            "I continued to walk, unwilling to stop"
            msub "If only I had the energy to do that."
            "I think I'll go back for now."
          
            jump mMaze2
          
        "Go back and start over again.":
            
            jump mMaze
            
        "Give up.":
            "It's no good..."
            "I've walked and still nothing..."
            "I really am lost. Thrown into a completely hopeless situation."
            "This time..."
            "I don't think I'll ever wake up again..."
            msub "... ... ..."
            "No..."
            "I can't lose hope. Not yet."
            "I'll try go back and start again."
            "Hmm?"
            "What's this?"
            
            show bonus1
            with dissolve
            
            $ bonus = 1
            
            msub "I-It's a..."
            "Porn magazine!"
            "What's this doing here!?"
            "Featuring hot furry daddies, twinks, hunks and many more..."
            msub "Ermm..."
            "M-Maybe... I should take a quick peek inside..."
            msub "Hmm?"
            "The pages are all stuck together..."
            "Well so much for the fun."
            "I think I'll just put it back where I found it..."
            "That's strange. How did this end up all the way here?"
            "Oh well... nevermind I better go back and start again."
            
            hide bonus1
            with dissolve
            
            
            jump mMaze



label mForest:
    menu:
        "I have no other choice":
            "Hmm..."
            
            $ bonus += 1
            
            jump mContinue
            
            
        "I'll just wait here like he told me to...":
            "When night came, we sat around the fire together in silence."
            "I watched as he skewered each fish with a stick."
            "Grilled fish just like last night..."
            extend " is that the only thing he eats?"
            "Well he seems kind of content about it."
            "Another night gone by just like that.\n"
            extend "At least I got some food out of it."
    
            jump Chapter2

label mWaterfall:
    
    menu: 
        "Take it easy and get some rest.":
            jump  mContinue2
            
        "Follow him to see where he's going.":
            hide mSigh
            with dissolve
            
            mc "Well I am curious..."
            "He looked like he was ina hurry to go somewhere..."
            stop Sound1 fadeout 2.0  
            
            "I better go and check it out!"
            
            scene bg_forest6
            with fade
    
            play Sound1 ("OB_music/StrangeForest.ogg") fadein 3.0
            
            mc "I'm sure he went this way..."
            "I looked around for a bit before realising that he'd completely disappeared."
            "I'll just walk a little bit further. If I can't find him I'll go back."
            mc "Hmm?"
            "Is it me or does this place feel slightly..."
            extend " eerie..."
            
            stop Sound1 fadeout 2.0
            
            "I can feel the hairs on the back of my neck standing up."
            "Something... doesn't feel right here..."
            "It's like I'm being watched."
            "M-Maybe it wasn't a good idea for me to come here."
            "I stepped backwards, tripping over something small which made me fall to the ground."
            
            play Sound1 ("OB_music/Creepy.ogg") fadein 2.0
            
            mc "T-This is..."
            "B-BONES!"
            "Are these... human bones?"
            "N-No... they're not."
            "Looks like some sort of animal."
            
            stop Sound1 fadeout 2.0
            
            "I think I better get out of here now!"
            
            scene bg_waterfall
            with fade
            
            $ bonus += 1
            
            mc "Phew... made it back..."
            mc "That was a..."
            extend " odd expereince."
    
            play Sound1 ("OB_music/Everyday.ogg") fadein 3.0
            
            jump mContinue2
            
label mClimb:
    
    "I'm getting extremely irritated with him!"
    "I don't want to listen anymore."
    
    menu: 
        "Climb the way you want.":
            "That's it, I'll just climb however I want."
            "I don't need to follow his instructions to get to the top."
            "I've come so far now and so high up that I can hardly see the ground."
            mc "Ah!"
            "It was then that I realised how wrong I was for not following his lead."
            g "!"
            "I fell off the cliff, falling and unable to do anything."
            "Goro disappeared out of my sight as I fell further away from him..."
            extend " until..."
            
            stop sfx2
            
            scene black
            
            play sfx3 ("OB_sound/HeavyPunch.ogg")
            
            "My body hit the ground."
            
            scene bg_endscene
            with fade
            $renpy.pause(3.0, hard=True)
            
            jump Chapter4
                    
        "Just put up with him for now.":
            
            "I let out the biggest sigh and continued."
            $ bonus += 1
            
            jump mContinue3
    



label ChapterBadEnd:
    
    scene bg_badscene
    with fade
    
    play sfx1 ("OB_sound/Seashore.ogg")
    
    "We didn't speak much after that night and things just got from bad to worse." 
    "Every moment felt like the day we first met, except things got a bit distant between us."
    "He avoided me, almost like he was pretending I wasn't there."
    "Even when I left the island he made no eye contact or said anything."
    "We just... ended up going our separate ways..."
    "As I looked up to the blue sky while I drifted away on the boat. A tear streamed down my face."
    mc "...So I guess this is goodbye..."
        
    return
    
