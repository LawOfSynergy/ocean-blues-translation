label Chapter2:
    
    scene bg_forest2
    with fade
    
    play sfx1 ("OB_sound/Cicada.ogg") fadein 3.0   
    play sfx2 ("OB_sound/Birds.ogg") fadein 3.0   
    
    mc ".... Ugggh..." 
    "I couldn't sleep a wink..."
    "My mind was too preoccupied with everything that's happened so far." 
    "I keep thinking to myself... \n"
    extend "What happens if I can't go home..."
    "What if I was the only one who survived and news had gone out telling all passenger are dead?"
    " All these thoughts keep jumping at me."
    " I just don't know what to think anymore..."
    
    show gSigh at right
    with dissolve
    
    g "Hey!"
    
    show mShock at left
    with dissolve
    
    mc "!"
    mc "Y-Yes?"
    "Geez that scared the hell out of me!" 
    g "Today you'll stay here alone until dawn and wait until I get back human."
    "What!?" 
    mc "B-But what happens if a wild animal appears?"
    
    hide gSigh
    with dissolve
    show gIdle at right
    with dissolve
    
    g "... ... ..."
    g "That's unlikely to happen." 
    
    hide gIdle
    with dissolve
    show gSigh at right
    with dissolve
    
    g "I've lived here for a long time and no wild animal has ever come here." 
    
    hide mShock
    hide gSigh
    with dissolve
    show mSigh at left
    show gIdle at right
    with dissolve
    
    "But this is me you're talking about, anything could happen."
    "To you it's okay because no animal would be stupid enough to come near you."
    "Still... the thought of sitting here alone and a chance I might be attacked is...\n"
    extend "scary..."
    
    hide mSigh
    with dissolve
    show mSad at left
    with dissolve
    
    mc "Please take me with you!"
    
    hide gIdle 
    with dissolve
    show gAnnoyed at right
    with dissolve
    
    g "Sigh..."
    g "Not this again..." 
    mc "... ... ..."
    g "No! You'll just get in the way human!"
    
    hide mSad
    with dissolve
    show mPumped at left
    with dissolve
    
    mc "I won't get in your way. I promise..."
    mc "Please... let me go with you..."
    mc "I'll do anything to help!" 
    
    hide mPumped
    with dissolve
    show mHurt at left
    with dissolve
    
    mc "Just... please..." 
    "I don't want to be alone..."
    
    hide gAnnoyed
    with dissolve
    show gSigh at right
    with dissolve
    
    g "... ... ..."
    g "Sigh..."
    g "Alright, I get it!!!"
    g "If you slow me down I'll leave you behind!"
    
    hide mHurt
    with dissolve
    show mPumped at left 
    with dissolve
    
    mc "I-I won't I promise!" 
    g "... ... ..."
    
    hide gSigh
    with dissolve
    show gPoint at right
    with dissolve
    
    g "Let's go."
    
    hide mPumped 
    with dissolve
    show mIdle at left
    with dissolve
    
    stop sfx1 fadeout 2.0
    stop sfx2 fadeout 2.0
    stop Sound1 fadeout 2.0
    
    mc "Okay."
###-----------------------------------------------------
    scene bg_forest6
    with fade
    
    play Sound1 ("OB_music/StrangeForest.ogg") fadein 2.0
    play sfx1 ("OB_sound/Birds.ogg") fadein 2.0
    
    "I know I only have myself to blame for being so pathetic but..."
    "I'm grateful to him. Even though he refused at first when I asked if I could come along."
    "I wonder where we're going?"
    "Everything here looks kind of..."
    extend " different.\n" 
    extend "Are we going somewhere far?"
    "I hope we'll be getting rest stops. Especially if it's going to be a long walk..."
    
    show gSigh at right
    with dissolve
    
    g "Snakes..." 
    
    show mIdle at left
    with dissolve 
    
    mc "... ... ..."
    g "There are snakes on this path."
    
    hide mIdle
    with dissolve
    show mShock at left
    with dissolve
    
    " D-Did he just say snakes..."
    g "Try not to get yourself eaten human." 
    g "Not that I care if you did."
    mc "R-Right!"
    "This isn't funny... I didn't think there would be snakes here!"
    "Why would he choose to walk in this direction knowing this!?"
    
    hide mShock
    hide gSigh
    with dissolve
    show mPumped at left
    show gIdle at right
    with dissolve
    
    
    mc "... ... ..."
    " It's okay, I'll be sure to stick to him like glue. That way I won't get attacked by one."
    " I mean just his presence alone is enough to send a lion running."
    g "... ... ..."
    
    stop Sound1 fadeout 3.0 
    stop sfx1 fadeout 3.0
    
    hide gIdle
    with dissolve
    show gSigh at right
    with dissolve
    
    g "Sigh..."

###-------------------------------------------------------------------


    scene bg_waterfall
    with fade
    
    play Sound1 ("OB_music/Everyday.ogg") fadein 3.0

    show mHappy at left
    with moveinleft

    mc "Wow..."
    mc "It's a waterfall!"
    
    show gSigh at right
    with moveinright
    
    g "Stay here and don't move!"
    
    hide mHappy
    with dissolve 
    show mIdle at left
    with dissolve
    
    hide gSigh 
    with moveoutright
    
    mc "Huh?"
    
    hide mIdle
    with dissolve
    show mShock at left
    with dissolve
    
    mc "H-Hey wait a minute-"
    
    hide mShock
    with dissolve
    show mSigh
    with dissolve
    
    "And gone... just like that..."
    mc "...Oh well..." 
    
    jump mWaterfall
    
    label mContinue2:
    
    hide mSigh
    with dissolve
    show mIdle 
    with dissolve
    
    "I guess this is a good time to sit here and rest up."
    "... ... ..."
    "What an amazing place...\n" 
    extend "If only my parent's were here to see this too..."
    
    hide mIdle
    with dissolve
    show mSad
    with dissolve
    
    "Mum...\n"
    extend "Dad..."
    "... ... ..."
    
    hide mSad
    with dissolve
    show mPumped
    with dissolve
    
    "No."
    "Got to focus on something else!"
    
    hide mPumped
    with dissolve
    show mIdle
    with dissolve
    
    "Hmm?"
    "I see something sparkling over there by the river."
    
    hide mIdle
    with moveoutright
    
    "Without a second thought, I walked towards the area where the lights are reflecting from the surface of the water."
    
    show mShock
    with moveinleft
    
    play sfx1 ("OB_sound/Stream.ogg") fadein 3.0
    
    mc "Wow!" 
    "The water's so clear, I can even see the rocks at the bottom."
    "Look at all those fishes!"
    
    hide mShock
    with dissolve
    show mHappy
    with dissolve
    
    "Maybe I should try and catch some."
    "That big one over there looks tasty!"
    
    hide mHappy
    with dissolve
    show mIdle
    with dissolve
    
    "But..." 
    
    hide mIdle
    with dissolve
    show mSigh
    with dissolve
    
    "I won't be able to cook them..."
    mc "... ... ..."
    
    hide mSigh
    with dissolve
    show mIdle
    with dissolve
    
    "Oh well, what's the harm in trying." 
    "Besides it's so hot today, I could do with a little splash in the water." 
    
    hide mIdle
    with dissolve
    
    "I took off my sneakers and stepped into the flowing river."
    
    play sfx3 ("OB_sound/Splash.ogg")

    mc "Oh this is great, it's nice and cool."
    mc "Hehe!"
    "Like a child I splashed around aimlessly playing with the water."
    mc "I've never really tried catching fishes before..." 
    mc "Hmm...."
    "There's one!"
    "I jumped towards the direction of where the fishes were swimming and dug my hands into the water."
    mc "Hyaa!"
    
    play sfx3 ("OB_sound/Splash.ogg")
    
    mc "Damn, it got away..."
    mc "I won't give up!" 
    mc "Not until I catch one!"
    
    "With multiple failed attempts and no results. I began panting away while I stood there, soaked and parched." 
    mc "Phew... Maybe I should stop..."
    mc "Alright! One last go!"
    "My previous attempts may have failed but this time I'll wait until they swim towards me."
    "Patience is the key... although I'm running out of it."
    "There!\n"
    extend "Haa!!"
    
    play sfx3 ("OB_sound/Splash.ogg")
    
    "This time with one scoop, I managed to catch one."
    mc "Gotcha!"
    mc "Yes I did it!"
    "I watched as the fish wriggled around in my hands fantically. It was so slippery that I lost my grip and it managed to escape."  

    play sfx3 ("OB_sound/Splash.ogg")

    "*huff* ... *pant*"
    mc "This is.. *pant*.\n" 
    extend "Tougher than... *huff*\n" 
    extend "It looks..."
    
    show gSigh at right
    with dissolve 
    
    g "Hey!"    
    mc "Huh?" 
    "As I turned around to find out where that familiar voice was coming from, I quickly lost my balance and slipped." 
    mc "Waaa!"
    
    play sfx3 ("OB_sound/WaterSmack.ogg")
    
    mc "... ... ..."
    mc "Ow...\n" 
    extend "That hurt..."
    g "What are you doing human?"
    mc "I um..." 
    mc "I thought I'd catch us some fish..." 
    g "... ... ..." 
    g "Get out..." 
    mc "O-Okay... "
    
    show mFidget at left
    with dissolve
    
    "Is he angry with me?"
    "Did I do something wrong again?"
    "I was only trying to help..."
    
    hide gSigh
    with dissolve
    show gIdle at right
    with dissolve
    
    g "... ... .."
    
    hide mFidget
    with dissolve
    show mIdle at left
    with dissolve
    
    mc "What's he looking for?"
    g "This would do..."
    "He picked up a large rock, that looks extremely heavy."
    "Don't tell me he plans on throwing that in there." 
    
    hide gIdle
    with dissolve
    show gPoint at right
    with dissolve
    
    g "This is how you catch fish, human!" 
    
    hide gPoint
    with dissolve
    show gIdle at right
    with dissolve
    
    "I watched carefully as he threw it in the river, even a child knows that throwing a rock as big as that won't be able to hit any of the fishes." 

    play sfx3 ("OB_sound/WaterSmack.ogg")

    "Huh?" 
    "That was strange. It sounded like it collided with something before hitting the water."
    "Could it be that rock sticking out from the river?"
    "Wasn't he planning to throw that at the fishes?"
    "We stood there waiting for a while..."
    
    hide mIdle
    with dissolve
    show mShock at left
    with dissolve
    
    mc "W-What happened?"
    mc "They're all floating like they're dead!"
    mc "H-How did you do that!?"
    
    hide gIdle
    with dissolve
    show gShy at right
    with dissolve
    
    g "... ... ..."
    g "The shock..."
    
    hide gShy 
    with dissolve
    show gSigh at right
    with dissolve
    
    g "Knocked them unconscious..."
    
    hide mShock
    with dissolve
    show mIdle at left
    with dissolve
    
    mc "You mean..."
    
    hide mIdle
    with dissolve
    show mPumped at left
    with dissolve
    
    mc "You aimed at that rock over there on purpose and it caused a shockwave or something."
    g "Yeah."
    mc "Wow, I never knew there was an easier way of catching fishes!"
    "Is that even possible?" 
    
    hide mPumped
    with dissolve
    show mSigh at left
    with dissolve
    
    "So all this time, I was in there throwing myself around trying to catch them...\n"
    extend "and he was probably watching me..."
    
    hide gSigh
    with dissolve
    show gIdle at right
    with dissolve
    
    "Ugh... this is so embarrassing!" 
    
    hide gIdle
    with dissolve
    show gSigh at right
    with dissolve 

    g "Hurry up with the fishes!" 
    
    hide mSigh
    with dissolve
    show mShock at left
    with dissolve

    mc "R-Right!"
    
    hide mShock
    hide gSigh
    with dissolve
    
    "We both got into the water and began picking up the fishes floating on the surface."
    "He placed several of them onto a large leaf and and began wrapping them up."
    
    show mSigh at left
    with dissolve
    
    mc "Phew..." 
    mc "And that's the last one..."
    "There's quite a lot here..."
    "As I sat down to rest, Goro handed me an apple."
    
    show gSigh at right
    with dissolve
    
    g "Here..." 
    "Fruits again?"
    "I'm getting tired of eating these..."
    
    hide mSigh
    with dissolve
    show mIdle at left
    with dissolve
    
    mc "... ... ..." 
    "Who am I to complain..." 
    "Food is food and besides I am hungry after all that moving around."
    
    hide mIdle
    with dissolve
    show mHappy at left
    with dissolve
    
    mc "Thank you..."
    
    hide mHappy 
    hide gSigh
    with dissolve
    
    stop Sound1 fadeout 3.0
    
    "It wasn't long before I finished eating my apple."
    "I began by looking around aimlessly at the scenary and then tried to relax by watching the waterfall."
    mc "... ... ..."
    
    show gSigh at right
    with dissolve 
    
    g "Do you..." 
    g "Despise me human?"
    
    show mIdle at left
    with dissolve
    
    "Where did that come from all of a sudden?"
    mc "... ... ..."
    
    hide mIdle 
    with dissolve
    show mPumped at left
    with dissolve
    
    mc "No.\n" 
    
    hide mPumped 
    with dissolve
    show mIdle at left
    with dissolve
    
    extend "No I don't..."
    
    hide gSigh
    with dissolve
    show gIdle at right
    with dissolve
    
    g "... ... ..."
    
    hide mIdle
    with dissolve
    show mSigh at left
    with dissolve
    
    mc "I mean, yes, I was scared at first...\n" 
    extend "But isn't that just a normal reaction?" 
    mc "Given the situation to another, I'm sure they would probably react the same way."
        
    hide mSigh
    with dissolve
    show mSad at left
    with dissolve
    
    mc "It's just that..."
    mc "It's true that I've cause you a lot of problems...\n"
    extend "But that wasn't by choice... "
    mc "... ... ..."
    mc "I know you're not happy with me being here... "
    extend "but...\n"
    extend "I've never despised you...\n" 
    extend "Even for-"   
    
    hide gIdle
    with dissolve
    show gSigh at right
    with dissolve
    
    g "Lies..."
    
    play Sound1 ("OB_music/A Void.ogg")
    
    hide mSad 
    with dissolve
    show mIdle at left
    with dissolve
    
    mc "Wha-?"
    
    hide gSigh 
    with dissolve
    show gAngry at right
    with dissolve
    
    g "You think, I could believe those words from a human!?"
    g "All you humans ever do is lie!"
    
    hide mIdle 
    with dissolve
    show mSad at left
    with dissolve
    
    mc "... ... ..."
    "It's not one hundred percent lies. But that's because he keeps treating me like I'm some sort of disease..."
    "I'm not saying I harbour any ill feelings towards him..."
    "But he could at least try and show a little more compassion..."
    "His stare was as cold as ice. Completely voided from any feelings."
    
    g "You humans will be nothing more but scum to me!"
    g "Every last one of you!"
    
    hide gAngry
    with dissolve
    show gIdle at right
    with dissolve
    
    g "Even you!"
    
    hide mSad
    with dissolve
    show mHurt at left
    with dissolve
    
    hide gIdle
    with dissolve 
    show gSigh at right
    with dissolve
    
    g "Hmph!"
    g "We're leaving human!"
    
    hide gSigh
    with moveoutright
    
    "Why...\n"
    extend "Why does he say those things?"
    "His words hurt me so much..."
    "That I..."
    mc "... ... .."
    "But I can't... \n"
    extend "Not here...\n" 
    extend "Not now..." 
    "I'll hold onto these feelings inside of me even if it kills me..."
    
    stop sfx1 fadeout 3.0
    stop Sound1 fadeout 3.0
    
    "Because if I cry now...\n"
    extend "I'll end up being nothing more than a useless pathetic human being..."
    
    hide mSigh
    with dissolve

##--------------------------------------------------------------------------------------------
    scene bg_forest6
    with fade
    
    play Sound1 ("OB_music/StrangeForest.ogg") fadein 3.0
    play sfx1 ("OB_sound/Birds.ogg") fadein 2.0
    
    "We've walked pretty far from the waterfall." 
    "I guess it won't be long before we get back."
    
    show mIdle at left
    with dissolve
    show gIdle_flip at right
    with dissolve
    
    mc "... ... ..."
    msub "Hsss..."
    mc "Huh?"
    "What's that sound?" 
    "Did that come from him?" 
    
    hide mIdle
    with dissolve
    show mHappy at left
    with dissolve
    
    "How strange of him to make weird noises like that all of a sudden."
    msub "Hsss!"
    
    stop Sound1 fadeout 2.0
    stop sfx1 fadeout 2.0
    
    hide mHappy
    with dissolve
    show mIdle at left
    with dissolve
    
    "Actually..."
    "Doesn't sound like the kind of noise he'd make..."
    msub "HSSSSS!"     
    "It's getting louder..."
    "I slowly turn to look beside my feet and saw a large snake slithering towards me."
    
    hide mIdle
    show mShock_flip at Shake((0.55, 1.0, 0.5, 1.0), 1.0, dist=5)
    
    show sIdle at left
    with moveinleft
    
    play Sound1 ("OB_music/Thrill.ogg") 
    
    mc "AHH!" 
    
    "I jumped towards Goro out of shock and pulled on his clothes."
    
    hide gIdle_flip
    show gShock at Shake((0.80, 1.0, 0.5, 1.0), 1.0, dist=5)
    
    mc "I-I-It's a snake!"
    snake "Hssss...."
    "Goro turned around quickly to asses the situation."
    
    hide gShock
    with dissolve
    show gAngry at right
    with dissolve
    
    g "Don't move!"
    
    "I stood there completely frozen in fear, he told me not to move but even if I wanted to, my body wouldn't listen."
    "He dropped all the fishes on the floor that we was carrying back and cautiously walked up to the snake."
    
    hide gAngry
    with dissolve
    show gIdle at right
    with dissolve
    
    g "Just stay still!"
    
    hide mShock_flip
    with dissolve
    show mSigh_flip at right
    with dissolve
    show gIdle 
    with dissolve
    
    "I gave a small nod in response."
    mc "... ... ..."
    
    "As Goro approached the snake he broke off a long stick from a tree."
    "The snake noticed his presence and began initiating it's intimidating pose." 
    "It swayed left and right as it hissed." 
    "He tried fending off the snake by pushing it's slithering body away from us."

    snake "Hsss!"
    
    hide sIdle
    show sAttack at Shake((0.13, 1.0, 0.5, 1.0), 1.0, dist=5)
    snake "Shaaa!"
    
    hide gIdle
    show gAngry at Shake((0.50, 1.0, 0.5, 1.0), 1.0, dist=5)
    with dissolve

    "The snake struck towards Goro with great speed."
    "It was so fast that I wasn't able to see what happened but..."
    
    hide sAttack
    with dissolve
    show sIdle at left
    with dissolve
    
    "The snake returned to it's slithering pose again and began propping it's head up from the floor."    
    g "Grrr!"
    "I was so fixated at the snake that I didn't notice Goro dropping the stick."
    "But just as fast as the snake had struck him."
    "Goro held up his fist and struck down at the snakes head."
    "He swung so hard that a loud thump can be heard from his fist as it came in contact with the ground."
    
    hide sIdle
    show sAttack at Shake((0.13, 1.0, 0.5, 1.0), 1.0, dist=5)
    play sfx3 ("OB_sound/HeavyPunch.ogg")
    with redFlash
    hide sAttack with moveoutbottom
    
    stop Sound1 fadeout 3.0
    
    g "Grrr!!!"
    
    hide mSigh_flip
    with dissolve
    show mShock_flip at right 
    with dissolve
    
    "!" 
    "The snake was no longer moving and it was slightly horrifying to see."
    "I tried to pay no attention to the dead snake but rather at Goro."
    "Because at this precise moment...\n"
    
    play Sound1 ("OB_music/The Past.ogg") fadein 1.0
    
    hide gAngry
    with dissolve
    show gAngry_flip
    with dissolve
    
    "He's beginning to scare me a little..."
    "Those eyes of his... they arn't normal.\n"
    "It's like he's ready to lash out at me."
    
    g "Grrrr...."
    
    mc "I-I.."
    
    hide gAngry_flip
    with dissolve
    
    stop Sound1 fadeout 3.0
    
    show gSigh_flip
    with dissolve
    
    g "Tsk..."
    g "You should try and be more cautious."
    
    hide mShock_flip
    with dissolve 
    show mSad_flip at right
    with dissolve
    
    mc "I-I'm sorry... I will be next time."
    
    play Sound1 ("OB_music/TreadingCarefully.ogg") fadein 3.0
    
    hide mSad_flip 
    with dissolve
    show mIdle_flip at right
    with dissolve
    
    "Seems like he's back to normal..."
    "But something about him didn't seem right..."
    "His eyes are less itimidating than they we're earlier."
    "Which is a good thing but..."
    "Hmm?"
    "What's with the hand?"
    "He's holding it kind of funny..."
    
    mc "... ... ..."
    "I tried examining him closely."
    "Did he get bitten?"
    
    hide mIdle_flip
    with dissolve
    show mFidget_flip at right
    with dissolve
    
    mc "A-Are you okay?"
    
    hide gSigh_flip
    with dissolve
    show gAngry_flip
    with dissolve
    
    g "I'm fine!"
    g "Grr..." 
    
    hide mFidget_flip
    with dissolve
    show mShock_flip at right
    with dissolve
    
    "I noticed him covering his hand frantically, trying his best not to show me his wounds." 
    "He's clearly not okay..."
    "I knew I was bound to get him angry if I asked him to show me his hand... "
    extend "but right now he's hurt and needs help."
    
    hide mShock_flip
    with dissolve
    show mPumped_flip at right
    with dissolve
    
    "I swallowed hard and built up the courage to tell him."
    mc "Let me see your hand!"
    "I stepped in front of him and forcefully took hold of his wounded hand."
    
    hide gAngry_flip
    with dissolve
    show gShock_flip
    with dissolve
    
    g "!"
    
    hide gShock_flip
    with dissolve
    show gAngry_flip
    with dissolve
    
    g "Let go human!"

    "I wasn't quite sure what came over me but I was scared and yet I didn't want to back down."
    mc "No!" 
    
    hide mPumped_flip
    with dissolve
    show mIdle_flip at right
    with dissolve

    mc "... ... ..."
    mc "No..."
    extend " just..."
    extend " stay still..."
    
    hide gAngry_flip
    with dissolve
    show gShy_flip
    with dissolve
    
    g "... ... ..."
    "That's quite unexpected. For him to back down and doesn't fight back."
    mc "You really did get bitten..."
    
    hide mIdle_flip
    with dissolve
    show mPumped_flip at right
    with dissolve
    
    mc "This is bad that snake could have been poisonous!"

    g "What does it matter to you human!?"
    g "... ... ..."

    "He tried pulling his hand away from me but I persistently held onto him."
    "I have to do something..." 
    "That's right!" 
    "I just have to suck out all the poison...\n" 
    extend "I remember watching it on T.V once!"
    "It's better than nothing."
    mc "Just hold still..."
    " I just have to suck it out and make sure not to swallow any."
    "I pressed my lips on the area where he was bitten and began extracting the poison."
    
    hide gShy_flip
    with dissolve
    show gShock_flip
    with dissolve
    
    "!"
    
    hide mPumped_flip
    hide gShock_flip
    with dissolve
    
    
    g "... ... ..."
    "Hmm?" 
    "That's strange..." 
    "His scales.\n" 
    extend "They feel so smooth..." 
    "I always thought they'd be kind of rough and sharp around the edges." 
    "I tried sucking out the poison as much as I can and spat it out."
    mc "There that should do it...\n"
    extend "I hope."
    
    show gShy at right
    with dissolve

    g "... That was...\n" 
    extend "Unnecessary... "
    extend "human..."
    
    show mFidget
    with dissolve

    mc "It's the only thing I know if you get bitten by a snake." 
    mc "And... well... I've never been poisoned before...\n"
    extend "So... are you... "
    
    hide gShy
    with dissolve
    show gAnnoyed behind mFidget at right
    with dissolve

    g "I won't die if that's what you're getting at human."
    mc "O-Oh that's good..."
    mc "It's... not much but..."
    mc "This is all I can do to repay you.\n"
    extend "For protecting me..."
    
    hide gAnnoyed
    with dissolve
    show gShy at right
    with dissolve
    
    g "... ... ..."
    
    hide mFidget
    with dissolve
    show mIdle
    with dissolve
    
    "As he pulled his hand away from me, he began picking up the fishes he had dropped on the floor earlier."
    "There wasn't much to say, except I hope I did the right thing..."
    
    stop Sound1 fadeout 3.0

    g "Let's move, we're not far now..."
    mc "Okay."
    
    
##-----------------------------------------------------------------------------------#######

    scene bg_forest3
    with fade
    
    play sfx1 ("OB_sound/Fireplace.ogg") fadein 3.0   
    play sfx2 ("OB_sound/Crickets.ogg") fadein 3.0  
    
    show mIdle at left
    with dissolve
    
    mc "Wow, it's gotten a lot darker all of a sudden... "
    "Good thing we made it back before sunset. After hauling all those fishes back here, I think my arms and legs are about to break."
    "We haven't spoken much since getting back and eating our food."
    "The fishes he made this time wasn't any different from the last.\n" 
    extend "I'm starting the get a bit tired of eating plain grilled fish..."  
    "Well at least the silence between us doesn't feel too bad.\n"
    extend "Not sure why...\n"
    "I mean we've sat here before eating like this. Up until now, he practically told me I was a nuisance. Like a bad thorn to his backside." 
    "But right now it feels different..."
    "Different in a good a way I guess."
    
    show gIdle at right
    with moveinright
    
    g"Hey..." 
    
    hide mIdle
    with dissolve
    show mShock at left
    with dissolve
    
    mc "W-What is it?" 
    
    hide gIdle 
    with dissolve
    show gPoint at right
    with dissolve
    
    g "Come." 
    "Wonder what's up with him all of a sudden..."
    
    hide mShock
    with dissolve
    show mIdle at left
    with dissolve
    
    mc "Okay..."
    
    hide gPoint  
    with moveoutright
    
    "Is there something over there in the forest?"
    "I got up from where I was sitting comfortably and followed him into the woods."
    
    hide mIdle
    with moveoutright
    
    "It's a bit dark and creepy during the night..."
    
    stop sfx1 fadeout 3.0
    "We walked further into woods until no traces of light from the campfire can be seen."    
    "The only source of light remaining is the moon that's shining brightly above us."
    "If it wasn't for the moon I think we'll be walking blindly in the dark."
    

##----------------------------------------------

    scene bg_hotspring
    with fade
        
    "It wasn't long before we arrived at something I would never expect to see out here."
    
    show mHappy at left
    with moveinleft

    mc "Wow! It's a hot spring!"
    mc "I remember watching a documentry that a certain country was really popular with these!\n" 
    extend "There's so much steam coming from the water too."
    
    show gSigh at right
    with moveinright
    
    g "Hurry up and get in." 
    
    hide mHappy
    with dissolve
    show mShock at left
    with dissolve
    
    mc "H-Huh?"  
    mc "Y-you mean now?" 
    g "Don't make me repeat myself..."
    
    hide mShock
    with dissolve
    show mFidget at left
    with dissolve
    
    mc "B-But I... I'll have to take all my clothes off and that means I'll be...\n" 
    extend "N-n-naked..." 
    
    hide gSigh
    with dissolve
    show gAnnoyed at right
    with dissolve
    
    g "... ... ..." 
    g "And you think that matters to me?" 
    g "That puny human body of yours doesn't interest me." 
    
    "It's a little embarrassing but..."
    mc "O-Okay, well if it's alright with you then..."
    
    hide mFidget
    hide gAnnoyed
    with dissolve 
    
    "I turned to look away from Goro and took off my clothes quickly." 
    play sfx3 ("OB_sound/Clothes.ogg")
    
    show mFidgetn at left
    with dissolve
    
    mc "... ... ..."
    "Leaving my clothes behind on the floor I walked up to the spring and dipped my foot in to test the temperature."
    mc "Just right..."
    play sfx3 ("OB_sound/Splash.ogg")
    
    "I placed my foot in futher and soon realised the water wasn't as deep as I thought it'd be."
    "I went in slowly walking futher into the spring until the water was just above my waist."
    mc "This should be okay."
    "I sat myself down.\n"
    extend "The water was just enough to cover up my chest up."
    
    hide mFidgetn
    with dissolve
    show mRelaxn at left
    with dissolve
    
    mc "Ahh..." 
    mc "I've always wanted to try soaking in an outside hot spring."
    
    hide mRelaxn
    with dissolve
    show mIdlen at left
    with dissolve
    
    "I turned to look at Goro out of curiosity."
    play sfx3 ("OB_sound/Clothes.ogg")

    "He removed all his clothes and slowly made his way into the water."
    
    show gIdlen at right
    with moveinright 
    
    "I couldn't help noticing that huge scar on his chest.\n"
    extend "Did he get into a fight with a wild animal or something?"
    "I was quite curious as to what he actually looks like down there..." 
    "It's not every day you get to meet a dragon after all. I took a quick glance at his neither regions without trying to be obvious."
    mc "... ... ..."
    
    hide mIdlen
    with dissolve
    show mShockn at left
    with dissolve
    
    "Where is it?\n"
    extend "Why doesn't he have one?"
    
    hide mShockn
    with dissolve
    show mFidgetn at left
    with dissolve
    
    "How in the world do they...\n" 
    extend "Do it?"    
    "I tried not to stare too much as it might make him feel uncomfortable." 
    
    hide mFidgetn 
    with dissolve
    show mIdlen at left
    with dissolve
    
    "Instead I looked towards the sky where the stars are visible during the night."
    play sfx3 ("OB_sound/Splash.ogg")
    
    hide gIdlen
    with dissolve
    show gHappyn at right
    with dissolve
    
    g "Haaa....."
    
    hide mIdlen 
    with dissolve
    show mFidgetn at left
    with dissolve
    
    mc "I-It feels great...\n"
    extend "Do you always come here?"
    
    hide gHappyn
    with dissolve
    show gIdlen at right
    with dissolve
    
    g "... ... ..."
    "He didn't say much but only gave a faint nod."
    
    hide mFidgetn
    hide gIdlen
    with dissolve
    
    "We both sat there watching the stars twinkle in the night sky."
    "It's an amazing experience. Something I could never imagine in a million years."
    "Sitting here in a hot spring, enjoying the night view and..."
    "As I looked towards Goro, I notice his expression was somewhat...\n"
    extend "sad..."
    "What's with him all of a sudden?" 
    "Why the painful expression on his face?" 
    "I mean he even said it before. That being sad is not part of his emotions..."
    "And yet, why does he look like that?"
    
    show mFidgetn at left
    with dissolve
    
    mc "Um..." 
    
    show gSighn at right
    with dissolve
    
    g "What human?"
    mc "If you don't mind me asking..." 
    mc "Have you been living here since you were born?"
    
    hide gSighn 
    with dissolve
    show gAnnoyedn at right
    with dissolve
    
    g "... ... ..." 
    
    hide mFidgetn
    with dissolve
    show mShockn at left
    with dissolve
    
    mc "I-It's okay, you don't have to answer. I-I got ahead of myself for asking..."
    
    hide mShockn
    with dissolve
    show mSadn at left
    with dissolve
    
    mc "Sorry..."
    mc "... ... ..."
    "Way to go and make an awkward moment out of this..." 
    
    hide gAnnoyedn
    with dissolve
    show gIdlen at right
    with dissolve
    
    g "Why do you ask human?"
    mc "It's just that..."
    mc "I've always wanted to get to know you better."
    mc "You might not believe me but..."
    mc "From the first moment we met I did think to myself that it would be great if we could...\n"
    extend "... ... ..."
    
    g "What?"
    mc "Become friends..."
    
    hide gIdlen
    with dissolve
    show gShyn at right
    with dissolve
    
    mc "... ... ..."
    
    hide gShyn
    with dissolve
    show gSighn at right
    with dissolve
    
    g "I don't know when." 
    g "The earliest memories I have.\n"
    extend "Was somewhere cold and dark." 
    
    hide mSadn
    with dissolve
    show mIdlen at left
    with dissolve
    
    mc "That doesn't sound very comfortable..."
    "And definitely doesn't sound like he was living on this island."
    g "I was always locked up in a small room." 
    "A room?"
    "Was he being treated as a pet or something?"
    
    hide gSighn
    with dissolve
    show gIdlen at right
    with dissolve
    
    g "Everyday would be the same as the last."
    mc "What about your parents?"
    mc "Or siblings?" 
    g "... ... ..." 
    
    hide gIdlen
    with dissolve
    show gSighn at right
    with dissolve
    
    g "I don't have this thing where you humans call 'family' to begin with.\n" 
    extend "Ever since I was born..."
    g "I have been alone." 
    
    hide mIdlen
    with dissolve
    show mSadn at left
    with dissolve
    
    mc "... It must've been hard for you..."
    
    hide gSighn
    with dissolve
    show gHappyn at right
    with dissolve
    
    g "Heh...\n" 
    
    hide gHappyn
    with dissolve
    show gSighn at right
    with dissolve
    
    extend "it's nothing special." 
    "So all this time. He's been locked up and living all alone by himself." 
    "I think I can relate in a way. Although my case isn't as severe as his..."
    "To live in a place where you're suppose call home... yet only to find nothing." 
    "But an empty and meaningless shell as your only comfort..." 
    
    hide mSadn 
    with dissolve
    show mFidgetn at left
    with dissolve
    
    mc "So... umm...\n" 
    extend "How did you end up here on this island?" 
    
    hide gSighn
    with dissolve
    show gAnnoyedn at right
    with dissolve
    
    g "You really do have no decency as a human..."
    
    hide mFidgetn
    with dissolve
    show mShockn at left
    with dissolve
    
    mc "Ah I mean-"
    
    hide mShockn
    with dissolve
    show mSighn at left
    with dissolve
    
    mc "Sorry..."
    "I just blurted it out without thinking." 
    
    hide gAnnoyedn
    with dissolve
    show gSighn at right 
    with dissolve
    
    g "I escaped. Found myself a boat and ended up here by chance."
    
    hide mSighn
    with dissolve
    show mSadn at left
    with dissolve
    
    mc "I... see..." 
    mc "The place you was living must of been really bad..."
    
    hide gSighn
    with dissolve
    
    g "... ... ..."
    "I then realised how insensitive my words were. So I turned to look towards him and tried to apologise."
    
    hide mSadn
    with dissolve
    show mShockn at left
    with dissolve
    
    mc "I'm sorry, that wasn't what I meant!"
    
    hide mShockn
    with dissolve
    
    scene bg_Goro3
    with dissolve
    
    play Sound1 ("OB_Music/The Past.ogg") fadein 1.0
    
    "He sat there frozen in fear as if remembering a really long and horrible nightmare. At this point I couldn't help but call out to him."    
    mc "H-Hey are you..."
    extend " okay?"
    g "I'm fine!"
    
    mc "I-If you say so..."
    "I must of touched a very sensitive subject here."
    "... ... ..."
    "Me and my big mouth..."
    
    g "That light... those... that sound..."
    g "No... stop..." 
    "What? I can't hear him?"
    "What is he saying?"
    mc "H-Hey are you sure you're okay?"
    "I watched as he began to trembled."
    "My words didn't seem to reach him and now he's sat there completely silent."
    g "... ... ..." 
    "Something's not right... he's starting to shake uncontrollably." 
    "This is bad. I get the feeling that if he stays in that state any longer..."
    "Things are going to get very dangerous..."
    extend " for me."
    "Wh-what should I do?" 
    mc "Goro..." 
    mc "Goro!"
    "It's no good..."
    "If that's the case then I'll just have to do this!"
    "I pushed the surface of the water with the palm of my hands and managed to cover his face with water."
    
    play sfx3 "OB_Sound/Splash.ogg"
    stop Sound1 fadeout 1.0
    
    scene bg_hotspring
    show mPumpedn at left
    show gShockn at Shake((0.76, 1.0, 0.5, 1.0), 1.0, dist=5)
    
    
    g "!"
    "That seemed to work. Although I think I'm gonna be in trouble now..." 
    
    hide gShockn
    with dissolve
    show gAngryn at right
    with dissolve
    
    g "W-What the hell was that for human!?"
    
    hide mPumpedn
    with dissolve
    show mFidgetn at left
    with dissolve
    
    mc "You didn't seem like you was responding when I called you so..." 
    
    hide gAngryn
    with dissolve
    show gSighn at right
    with dissolve
    
    g "Hmph!" 
    
    hide mFidgetn
    with dissolve
    show mSighn at left
    with dissolve
    
    mc "... ... ..."
    mc "You were..."
    extend " really out of it just then." 
    "And began mumbling to yourself."
    
    hide mSighn
    with dissolve
    show mFidgetn at left
    with dissolve
    
    mc "Is everything okay?"
    
    hide gSighn
    with dissolve
    show gIdlen at right
    with dissolve
    
    g "... ... ..."
    
    hide gIdlen
    with dissolve
    show gAnnoyedn at right
    with dissolve
    
    g "No..."
    g "I relapse from time to time thinking about the past."
    
    hide mFidgetn
    with dissolve
    show mSadn at left
    with dissolve
    
    
    "Must of been one hell of a past for you to go into a trance..."
    g "You want to know why human?"
    "Well I am curious..." 
    "I mean what's the harm in knowing..."
    extend " right?"
    
    hide mSadn
    with dissolve
    show mIdlen at left
    with dissolve
    
    mc "Yeah..."
    
    hide gAnnoyedn
    with dissolve
    show gSighn at right
    with dissolve
    
    g "I was kept in the dark..."
    g "Isolated from the rest of the human civilization." 
    g "No one was to know of my existence."
    mc "But you ran away right?" 
    mc "If you did wouldn't you attract a lot of attention to yourself?"
    
    hide gSighn
    with dissolve
    show gAnnoyedn at right
    with dissolve
    
    g "... ... ..."
    g "I was able to escape onto a boat because of the uproar I created." 
    
    hide mIdlen
    with dissolve
    show mSadn at left
    with dissolve
    
    mc "... What kind of-"
    
    hide gAnnoyedn
    with dissolve
    show gAngryn at right
    with dissolve
    
    play Sound1 ("OB_Music/A Void.ogg") fadein 1.0
    
    g "I destroyed it..."
    extend " the facility,"
    extend " humans,"
    extend " everything!"
    
    hide mSadn
    with dissolve
    show mShockn at left
    with dissolve
    
    mc "!"
    
    hide gAngryn
    with dissolve
    show gAnnoyedn at right
    with dissolve
    
    g "The whole place fell under and fire spread throughout the area." 
    g "Humans panicked and ran as I escaped. Some even tried to hunt me down." 
    
    hide mShockn
    with dissolve
    show mSadn at left
    with dissolve
    
    
    mc "I don't understand..."
    mc "You're not as bad as you look and you've done nothing wrong."
    mc "So..."
    mc "Why would they want to lock you up?"
    
    hide mSadn
    with dissolve
    show mPumpedn at left
    with dissolve
    
    mc "What was it that they did for you to-"
    g "... ... ..."
    
    hide gAnnoyedn
    with dissolve
    show gSighn at right
    with dissolve
    
    g "Bio gene mutilation..."
    extend " and multipe experiments..."
    
    hide mPumpedn
    with dissolve
    show mIdlen at left
    with dissolve
    
    mc "Bio gene... mutilation...?"
    g "One day after another..." 
    g "Doing anything and everything for results..."
    g "At first, they fed me and raised me normally..."
    g "But things gradually changed..."
    g "They started to do various experiments to my body. They injected small amounts of animal genes into me every day."
    g "Including human genes."
    g "Fed me nothing but water for a whole month, torture me with strange equipments and inserted experimental objects into my body."
    g "At first, I thought this was just something temporary..." 
    g "Until one day..."
    g "I fell asleep in my room..."
    extend " my body was completely dead and exhausted..."
    g "But when I woke up. I found myself chained to a table..." 
    extend " I still remember the pain..." 
    extend " something sharp cutting into my body." 
    g "Blood pouring out of my chest." 
    g "That's when my anger took over, I lost control of myself and I began destroying everything around me..." 
    g "When I came to my senses I stood over a bunch of humans. Their bloodied corpses laid on the floor..."
    g "My hands covered in blood..."
    extend " It was then, that I realised what I had done..."
    g "I killed those humans that tortured me..."
    
    hide mIdlen
    with dissolve
    show mSadn at left
    with dissolve
    
    mc "... ... ..." 
    mc "I-I..."
    "Huh?"
    "Wait... what did I wanted to say again?"
    "Just hearing all this, is making me really upset... so much that it aches inside."
    g "Hmph..."
    g "There must be something wrong with me." 
    g "Talking to a human as if you'll understand..."
    mc "... ... ..."
    "I do... I do understand... but at the same time... I don't think I can understand that same level of pain and torture you've been through..."
    g "Don't let it bother you human. It's just a stupid story about the past." 
    g "Time to get out." 
    
    play sfx3 "OB_Sound/Splash.ogg"
    
    hide gSighn
    with moveoutright
    
    "How can he say that so casually?"
    "If that was me, I don't think I would have the will to live." 
    "To be born into this world alone, chained up in some room just to be some kind of tool for those people...and maybe even... hating your life because there's no escape..."
    "It's not normal... not for humans, animals or dragons... in fact it's too..."
    "It's extremely..."
    
    stop Sound1 fadeout 1.0
    stop sfx3 fadeout 1.0
    
    "... cruel..."    
    
    jump Chapter3
    
    return