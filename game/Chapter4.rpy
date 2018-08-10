label Chapter4:
    
    play sfx1 ("OB_sound/Cicada.ogg") fadein 3.0   
    play sfx2 ("OB_sound/Birds.ogg") fadein 3.0   
    
    scene bg_forest2
    with fade
    with Pause (1.0)

    mc "Yawn...\n" 
    extend "Ahh..." 
    
    show mIdle
    with dissolve

    "I glanced over at Goro to see if he was awake."
    mc "Seems like I woke up first."
    "Just looking at him stirred up some memories from yesterday..."
    
    hide mIdle
    with dissolve
    show mSigh
    with dissolve
    
    "Sure I might have broken our promise unintentionally."
    "But even so he didn't have to get that angry with me."
    "I watched as he slept like a log beside the camp fire and snoring away." 
    
    hide mSigh
    with dissolve
    show mHappy 
    with dissolve
    
    mc "Hehe..."
    "That's a funny snore."
    
    hide mHappy
    with dissolve
    show mIdle
    with dissolve
    
    "He's no different from any human being."
    "Sure he maybe a dragon, but at least he thinks and acts like a human..."
    "So far I've yet to see him breathe out fire or ice..." 
    "Then again, if he ever did something like that, it wouldn't make a difference..."

    "Oh. He's waking up."
    mc "Good morning..."
    g "Yawn...."
    "He didn't reply but only gave a faint nod while rubbing his eyes." 
    g "... ... ..."
    g "Sniff... Sniff...."
    "Hmm?"
    "What's he sniffing around for?" 
    
    show mIdle at left
    with moveoutleft
    show gIdle at right
    with moveinright
    
    "This is the first time I've seen him like this and he's also mumbling to himself."
    g "... We need to move..."
    
    g "Hey!"
    
    hide mIdle
    with dissolve
    show mShock at left
    with dissolve
    
    mc "Y-Yes?"
    
    hide mShock
    with dissolve
    show mIdle at left
    with dissolve
    
    "What's up with him all of sudden?"
    
    hide gIdle
    with dissolve
    show gPoint at right
    with dissolve
    
    g "We'll be moving to a different spot to camp from now on." 
    "Huh?"
    mc "W-Why's that?"
    
    hide gPoint
    with dissolve
    show gSigh at right
    with dissolve
    
    "A storm is coming." 
    
    hide mIdle
    with dissolve
    show mShock at left
    with dissolve
    
    "A Storm!?" 
    
    hide mShock
    with dissolve
    show mFidget at left
    with dissolve

    mc "But the weather looks great. Surely it's-"
       
    hide gSigh
    with dissolve
    show gAngry at right
    with dissolve
    
    g "Do you doubt me human!?" 
    
    hide mFidget
    with dissolve
    show mShock at left
    with dissolve
    
    mc "N-No I'm not."
    
    hide mShock
    with dissolve
    show mSad at left
    with dissolve

    "Still... it's hard to believe..."
    
    hide mSad
    with dissolve
    show mFidget at left
    with dissolve

    mc "So..."
    extend " what should I do to help?"
    
    hide gAngry
    with dissolve
    show gSigh at right
    with dissolve
    
    g "Nothing."
    "He got up from the floor and began stretching his body and then started walking towards the woods." 
    
    hide mFidget
    with dissolve
    show mPumped at left
    with dissolve 
    
    mc "W-Wait! "
    
    hide mPumped
    with dissolve
    show mIdle at left
    with dissolve 
    
    mc "I thought we were-"
    
    hide gSigh
    with dissolve
    show gIdle at right 
    with dissolve
    
    g "Just stay here human."
    g "This storm is not something you can handle."
    
    hide mIdle
    with dissolve
    show mSad at left
    with dissolve
    
    mc "It's just a stupid storm... it's not like it'll hurt me or anything..."
    
    hide gIdle
    with dissolve
    show gAngry at right
    with dissolve
    
    g "Grrr..."
    g "Enough with your senseless talk!"
    g "You humans are fragile creatures. Even the slightest change is enough to kill you!"
    
    hide mSad
    with dissolve
    show mShock at left
    with dissolve
    
    mc "!"
    
    hide mShock
    with dissolve
    show mSad at left
    with dissolve
    
    mc "... ... ..."
    mc "Fine..."
    
    hide mSad
    with dissolve
    show mPumped at left
    with dissolve 
    
    mc "But I won't just sit here and do nothing."
    
    hide gAngry
    with dissolve
    show gAnnoyed at right
    with dissolve
    
    g "Tch... \n"
    
    hide gAnnoyed
    with dissolve
    show gPoint at right
    with dissolve
    
    extend "Go gather some firewood."
    g "We need enough for a few days."
    
    hide mPumped
    with dissolve
    show mSad at left
    with dissolve
    
    "What's with him today and his attitude?" 
    "Especially first thing in the morning..."
    mc "... Fine..."
    
    hide mSad
    hide gPoint
    with dissolve
    
    scene bg_forest2
    with fade
    
    show mSigh
    with dissolve
    
    mc "Phew...\n" 
    extend "That should be enough."
    "Isn't he back yet?"
    "Talk about slacking..."
    mc "... ... ..."
    
    hide mSigh
    play sfx3 ("OB_sound/Thunder.ogg")
    show mShock at Shake((0.45, 1.0, 0.5, 1.0), 1.0, dist=5)
    
    "!"
    "W-Was that thunder?"
    
    show gIdle at right
    with moveinright
    
    g "Hey!"
    
    mc "Ah!\n"
    
    hide mShock
    with dissolve
    show mIdle at left
    with dissolve
        
    "He's back. What took him so long?"
    
    hide gIdle
    with dissolve
    show gPoint at right
    with dissolve
    
    g "Bring those here and tie them with this."
    
    mc "What's this?" 
    "He held out his hand holding some sort of rope that resembles the vines from the forest."

    g "Make sure it's tight."
    
    hide mIdle
    with dissolve
    show mSigh at left
    with dissolve
    
    mc "O-Okay..."
    
    hide mSigh
    with dissolve
    show mIdle at left
    with dissolve
        
    "How in the world do I tie this all up?" 
    
    hide gPoint
    with dissolve
    show gAngry at right
    with dissolve
    
    g "Make it quick human!"
    
    hide mIdle
    with dissolve
    show mPumped at left
    with dissolve
    
    mc "I'm trying!"
    "I'll just tie it however I can for now."
    "Just going to wrap it around a few times and tie a double knot."
    
    hide mPumped 
    with dissolve
    show mIdle at left
    with dissolve
    
    "There!" 
    "That should do it."
    
    hide gAngry
    with dissolve
    show gIdle at right
    with dissolve
    
    g "We don't have time human!"
    
    hide gIdle
    with dissolve
    show gPoint at right
    with dissolve
    
    g "Move!"
    
    scene bg_forest1
    with fade
    
    stop sfx1 fadeout 3.0
    
    "We've been walking down a path so steep that it's become extremely hard for me to maintain my balance."
    "If I'm not careful I might get hurt."
    "And how much longer do we have to walk anyway?"
    "He hasn't said a single word since we left..."
    "Wasn't this storm suppose to show up soon or something?" 
    "Hmm?" 
    "What's wrong?"
    "Why did we stop?"
    
    show gPoint at right
    with moveinright
    
    g "We'll be climbing up there human."
    
    hide gPoint 
    with dissolve

    scene bg_wall
    with dissolve
    
    "I looked towards where he was pointing to." 
    
    show mShock at left
    with moveinleft
    
    "It's a huge wall covered with stones, rocks and all sorts of greenary."
    
    hide mShock
    with dissolve
    show mIdle at left
    with dissolve
    
    "And not just that but it has all these big roots twisting and turning all over the place."
    "Looks like it goes all the way to the top."
    "Guess I'll be using those as foothold."   
    
    show gIdle at right
    with dissolve
    
    g "Here!" 
    "He threw towards me yet another long piece of vine."
    
    hide gIdle
    with dissolve
    show gAngry at right
    with dissolve
    
    g "Tie that around yourself!" 
    
    "Okay, I got it...\n" 
    "No need to shout..."
    
    hide mIdle
    with dissolve
    show mSigh at left
    with dissolve
    
    mc "Done..."
    "There... you happy?"
    g "Make sure you attach that to the firewood!"
    mc "Sure..."
    g "Hurry up!"
    
    hide gAngry
    hide mSigh
    with dissolve
    
    g "Just follow my lead!"
    "I watched as he grabs hold of the large vines and begins climbing the wall."
    "I'm surprise he's able to do that without breaking them..."
    g "Don't idle around!"
    mc "Okay. I'm going."
    "With that, I began following his lead like he insisted."
    mc "Mngh..."
    "This is really tough for a beginner!"
    g "Climb faster!"
    
    jump mClimb
    
    label mContinue3:
    
    "What in the world does he expect from me. Mountain climbing on a day like this!?"
    "And the rope tied around my waist with a bunch of firewood on my back is weighing me down too!"
    "Why are we even climbing this in the first place!?"
    mc "Unff..."
    mc "Almost there..."
    
    "I pushed myself hard climbing on the unstable vines."
    "My legs were about to break and I feel like my knees were about to give up on me."
    "Just as we were approaching towards the edge of the cliff. I felt I was gradually losing my balance."
    
    mc "Ah!!!"
    
    stop sfx2
    play Sound1 ("OB_music/Thrill.ogg")
    
    "Not good! I'm going to fall!"
    "Just as I was about to slip off and fall to my death. Goro thrusts out his hand and grabs onto mine."
    
    scene bg_Goro4
    with dissolve
    
    mc "!"
    g "Pull yourself up human!"
    mc "Huff...\n" 
    extend "Pant..."
    "As I tried to regain my footing I felt a slight movement shifting behing my back."
    "Some of the firewood came loose. I watched in dissapointment as they began to fall further away from me."
    mc "On no!"
    extend "The firewood!"
    mc "They came loose!"
    g "Leave them!" 
    mc "But!"
    g "I said leave them!\n"
    extend "Do you want to die that badly!?"
    
    "A bolt of lighting struck from afar and soon rain began to pour from the sky."
    
    play sfx3 ("OB_sound/Thunder.ogg") 
    play sfx1 ("OB_sound/Rain.ogg") fadein 5.0
    scene bg_Goro4
    show bg_Rain
    with flash
    
        
    g "What are you doing!?"
    g "Keep moving!"
    
    mc "I tried to pull myself up by grabbing onto the nearest vine."
    g "Hurry up!"
    mc "Look, I'm trying my best!"
    g "... ... ..."
    "With all the struggle I had to go through to scale the the wall."
    "We'd managed to reach the top." 
    
    stop Sound1 fadeout 3.0
    
    scene bg_outcave
    show bg_Rain
    with fade
    
    "Large droplets of rain fell from the sky.\n"
    extend "And each droplet that collided with the surface was enough to make a dent." 
    "I crawled onto the landing and layed flat on my back.\n"
    extend "Trying to catch my breath."
    
    scene bg_outcave
    show bg_Rain
    with flash
    play sfx3 ("OB_sound/Thunder.ogg")
    
    g "No time to rest!"
    g "We're not far now!"
    
    "No time to rest!?"
    "I nearly died back there climbing up here!"
    mc "... ... ..."
    "At this point I couldn't even muster the energy to say anything."
    "I got up ever so slowly and painfully before following him."
    "We came to a stop outside a cave."
    "What's with this crazy weather... it just started to rain heavily."
    "Not only that... I feel the wind getting stronger..."  
    
    show mSigh at left
    show gPoint at right
    with dissolve
    
    g "We'll be camping in there."
    mc "... ... ..."
    "A cave...?"
    
    stop Sound1 fadeout 2.0
    stop sfx1 fadeout 2.0
    
    scene bg_incaveD
    with fade
    
    "...It's so dark in here and...\n"
    extend "feels kind of damp..."
    
    show gPoint 
    with moveinright

    g "Wait here."
    
    hide gPoint 
    with moveoutleft 
    
    "This place doesn't look very comfortable and it's also really cold in here..."
    "There's a bunch of gigantic leaves left on the stone floor over there."
    "And some ashes over there..." 
    "Looks like he's been here before..."
    
    show gPoint at right
    with dissolve
    
    g "Hey!" 
    g "Take these and put those over there human."
    
    show mSad at left
    with dissolve
    
    "I'm getting really annoyed having him ordering me around with that attitude."
    "I walked over to the place he'd pointed and dropped the firewood onto the floor." 
    mc "... ... ..."
    "I can hear the echoes of the rainfall from outside..."
    "Sounds like it's raining even harder than before..."
    
    hide gPoint
    with dissolve
    show gSigh at right
    with dissolve
    
    g "You..."
    extend " afraid?"
    
    hide mSad
    with dissolve
    show mIdle at left
    with dissolve
    
    mc "What?"
    g "Are you afraid human?"
    mc "... ... ..."
    "Afraid?\n" 
    extend "Afraid of what?" 
    g "Hmph...\n"
    extend "No matter..." 
    "What kind of question is that? "
    
    hide mIdle
    with dissolve
    show mSigh at left
    with dissolve
    
    "Maybe it's because of what I went through today but I'm getting more and more agitated by the second."
    "Not that I could help it. Especially with the way he's been acting and talking to me."
    "More importantly, hurry up and set up camp fire. I'm all drenched from the rain and it's cold in here." 
    
    hide mSigh
    hide gSigh
    with dissolve
    
    scene bg_incave
    with fade
    
    play sfx1 ("OB_sound/Fireplace.ogg")
    
    "Not a single word..."
    "He's obviously very upset with something..."
    "Was it because of the firewood that I dropped earlier?" 
    mc ".. ... .."
    "It's not like I could help it. They just fell out..." 
    
    show mSad at left
    with dissolve
    
    mc "Um..."
    mc "You...\n" 
    extend "You don't have to be...\n"
    extend "That angry with me..."
    mc "... ... ..."
    
    show gSigh at right
    with dissolve 
    
    g "I'm not. "
    
    hide mSad
    with dissolve
    show mSigh at left
    with dissolve
    
    mc "Yes, you are..."
    
    hide gSigh
    with dissolve
    show gAngry at right
    with dissolve
    
    g "I said I'm not!"

    "I could be no further from the truth..."
    
    hide mSigh
    with dissolve
    show mHurt at left
    with dissolve
    
    mc "You've been really angry with me since this morning..."
    mc "Was it something I did?"
    mc "Was it the firewood I dropped?"
    
    hide gAngry
    with dissolve
    show gAnnoyed at right
    with dissolve
    
    g "... ... ..."
    
    hide mHurt
    with dissolve
    show mSigh at left
    with dissolve
    
    mc "It was, wasn't it?"
    
    hide gAnnoyed
    with dissolve
    show gSigh at right
    with dissolve
    
    g "... ... ..."
    
    hide mSigh
    with dissolve
    show mSad at left
    with dissolve
    
    "Why aren't you saying anything..."
    mc "Are you that angry that you can't tell me?"
    
    hide gSigh
    with dissolve
    show gAngry at right
    with dissolve
    
    g "I told you it's nothing!"
    g "Just shut up and stop talking human!"
    
    hide mSad
    with dissolve
    show mAngry at left
    with wiperight
    
    mc "That's it!" 
    
    stop sfx1 fadeout 2.0
    play Sound1 ("OB_music/A Void.ogg") fadein 1.0
    
    hide gAngry
    with dissolve
    show gShock at right
    
    mc "I've had just about enough!" 
    mc "Stop calling me human!"
    mc "I have a name you know!"
    mc "If you're really angry with something I've done. Just spit it out!"
    "I can't take this anymore... I want to go home..."
    mc "Just what am I suppose to do!?"
    mc "I've tried to be nice and do everything I can to be helpful!"
    mc "I know I'm causing you trouble for being here but that doesn't mean you should talk to me like I'm dirt!"
    mc "From the beginning!"
    mc "All the way up until now..."
    
    hide mAngry
    with dissolve
    show mSigh at left
    with dissolve
    
    mc "I.." 
    mc "I just..."
    mc "... ... ..."
    "Huh?\n" 
    extend "What's..."
    extend " this...?"
    "Somehow I feel ..."
    extend " very..."
    extend " dizzy..."
    
    hide mSigh
    with moveoutbottom
    play sfx3 ("OB_sound/HeavyPunch.ogg")
    
    scene bg_black
    with fade
    
    stop Sound1 fadeout 3.0
    
    g "H-HEY!" 
    g "Hey!"
    mc "... ... ..."
    g "Tsk..." 
    
    play sfx1 ("OB_sound/Fireplace.ogg") fadein 3.0
    
    mc "... ... ..."
    
    scene bg_Goro5
    with fade
    
    mc "...Ngh..."
    
    scene bg_Goro6
    with dissolve
    
    mc "Cough... Cough..." 
    "What..."
    extend " happened...?"
    "... ... ..." 
    "?"
    "What's this?\n" 
    "These big leaves..."
    extend " when did I fall asleep here?"
    mc "Cough... cough..."
    "I tried to regain my focus by looking around."
    "Something feels heavy on my body...\n"
    "Hmm?\n"
    "These arn't my clothes..."
    "Could this be... his?"
    
    scene bg_incave
    with fade
    
    "I pushed myself off from where I was lying and sat upright."
    
    show mIdleS
    with dissolve
    
    "I must of been completely out cold for him to change my clothes without noticing."
    "Saying that, where's my clothes?"
    
    hide mIdleS
    with dissolve
    show mSighS
    with dissolve
    
    mc "Cough, Cough... "
    "My head throbbed with pain with each cough."
    mc "Ugnhh..."
    extend " I feel horrible..."
    
    play sfx3 ("OB_sound/Thunder.ogg")
    
    hide mSighS
    with dissolve
    show mIdleS
    with dissolve
    
    "So he was right after all..."  
    "A storm appear..."
    extend " still that doesn't explain why he was in a bad mood."
    "I noticed Goro was nowhere to be seen."
    "Where did he go?" 
    "I looked towards the entrance of the cave as something was approacing."
    mc "What's that sound..."
    "Footsteps soon echoed within the cave."
    
    play sfx3 ("OB_sound/Thunder.ogg")
    
    show mIdleS at left
    with moveoutleft
    show gIdleU at right
    with moveinright
    
    g "Finally awake?"
    "He's completely drenched from the rain!"
    "What was he thinking going out like that?"
    
    hide mIdleS 
    with dissolve
    show mSighS at left
    with dissolve
    
    mc "Cough, Cough..."
    
    hide gIdleU
    with dissolve
    show gSighU at right
    with dissolve
    
    g "Here..." 
    "He held out a bunch of purple leaves.\n"
    extend "It looks ominous..."
    
    hide mSighS
    with dissolve
    show mIdleS at left
    with dissolve
    
    mc "... ... ..."
    mc "What's..."
    extend " that?"
    
    hide gSighU
    with dissolve
    show gShyU at right
    with dissolve
    
    g "This should..."
    extend " help lower your fever." 
    mc "... ... ..."
    "I took the leaves out of his hand and examined it for a while.\n"
    extend "I brought the strange looking leaf to my mouth and hesitated before taking a bite."
    
    hide mIdleS
    with dissolve
    show mSadS at left
    with dissolve
    
    mc "Ugh..."
    mc "This tastes really bad..."
    
    hide gShyU
    with dissolve
    show gSighU at right
    with dissolve
    
    g "Make sure you chew and swallow all of it."
    "I'm trying to...\n"
    extend "Would be a lot easier if I could get some water or something..."
    mc "... ... ..."
    
    hide mSadS
    with dissolve
    show mIdleS at left
    with dissolve
    
    "I watched as he walked over to the corner of the cave and picked up something else."    
    g "Here..."
    extend " drink this."
    "He presented me a wooden bowl filled with brightly coloured yellow liquid."
    
    hide mIdleS
    with dissolve
    show mSighS at left
    with dissolve
    
    mc "O-Oh..."
    extend " thank you..."
    
    hide gSighU
    with dissolve
    show gShyU at right
    with dissolve
    
    g "I..."
    extend " made that with some fruits..."
    
    "I gave no hesitation to drink the juice he made for me."
    "I gulped it down slowly."
    "A sweet mixture of fruits swirled around my mouth and tongue."
    
    hide mSighS 
    with dissolve
    show mHappyS at left
    with dissolve
    
    mc "That was..."
    extend " really good."
    "Except for the leaves..."
    
    hide mHappyS
    with dissolve
    show mIdleS at left
    with dissolve
    
    "So he's been out in the rain getting those herbs for me..." 
    mc "Aren't you cold?"
    
    hide gShyU
    with dissolve
    show gSighU at right
    with dissolve
    
    g "No... not really."
    "I placed my hand on his arm."
    
    hide gSighU
    with dissolve 
    show gShockU at right
    with dissolve
    
    g "!"
    
    mc "You're..." 
    extend " freezing..." 
    mc "If you don't dry yourself. You'll get sick."
    
    hide gShockU
    with dissolve
    show gSighU at right
    with dissolve
    
    g "I won't die from a little rain."
    mc "... ... ..."
    
    hide mIdleS
    with dissolve
    show mSighS at left
    with dissolve 
    
    mc "Umm... where are my clothes..."
    g "Over there..."
    
    hide mSighS
    with dissolve
    show mIdleS at left
    with dissolve 
    
    "I looked towards to where he was pointing.\n"
    "Why didn't I notice it earlier..."
    
    hide mIdleS
    with dissolve
    show mSighS at left
    with dissolve 
    
    mc "Cough, cough..."
    mc "... Could I please have them?"
    
    hide gSighU
    with moveoutright
    
    hide mSighS
    with dissolve
    show mIdleS at left
    with dissolve
    
    "I watched him walk towards the wooden rack with my clothes hung up to dry."
        
    show gIdleU at right
    with moveinright
    
    g "Here..." 
    
    play sfx3 ("OB_sound/Clothes.ogg")
    
    "They look dry enough..."
    "I took my clothes from his hand and stood up."
    "I'll just use this to dry him off as much as I can."
    "With that I began dabbing his wet body with my clothes."
    
    hide gIdleU
    with dissolve
    show gShockU at right
    with dissolve
    
    g "W-What are you doing!?" 
    
    hide mIdleS
    with dissolve
    show mSighS at left
    with dissolve
    
    mc "Please... stay still..."
    mc "It's the least I can do to repay you."
    mc "Cough, cough..."
    
    hide mSighS
    hide gShockU
    with dissolve
    show mIdleS at left
    show gIdleU at right
    with dissolve
    
    "I tried my best to wipe off the water from his body, starting from his back."
    "I've never really paid much attention but he's got some really broad shoulders..."
    "Big enough to carry a ship on them..."
    "I shook my head trying to remove the unnecessary thoughts."
    "... What am I thinking..."
    
    hide mIdleS
    with dissolve
    show mHappyS at left
    with dissolve
    
    mc "There..."
    extend " cough..."
    
    hide mHappyS
    with dissolve
    show mIdleS at left
    with dissolve
    
    
    mc "It's better than being cold and wet at the same time."
    
    hide gIdleU
    with dissolve
    show gShyU at right
    with dissolve
    
    g "You really are... "
    extend "strange for a human..."
    
    mc "Well..." 
    extend " thanks..." 
        
    hide mIdleS
    with dissolve
    show mHappyS at left
    with dissolve
    
    extend " you're pretty strange yourself..." 
    
    hide mHappyS
    hide gShyU
    with dissolve
    show mIdleS at left
    show gIdleU at right
    with dissolve
    
    g "... ... ..."
    g "After all the things I've said..."
    
    hide gIdleU
    with dissolve
    show gSighU at right
    with dissolve
    
    g "How can you..."
    extend " still worry about something that's not of your own kind?"
    g "Don't you detest me?" 
    
    hide mIdleS
    with dissolve
    show mSadS at left
    with dissolve
    
    mc "... ... ..."
    mc "I admit...\n"
    extend "I was upset, frustrated and angry..."
    extend " but...\n" 
    extend "I don't hate you..."
    
    hide gSighU
    with dissolve
    show gShyU at right
    with dissolve
    
    g "Why?"
    g "How can you not after all you've been through?\n"
    extend "And all the things I've put you through?"

    mc "... That's because...\n"
    extend "... because..." 
    
    hide mSadS
    with dissolve
    show mIdleS at left
    with dissolve
    
    mc "I don't really see you being any different from us..." 
    extend " from me..." 
    
    hide gShyU
    with dissolve
    show gSighU at right
    with dissolve
    
    g "Don't go comparing your kind to me..." 
    g "I'm not human to begin with..."
    
    hide mIdleS
    with dissolve
    show mSadS at left
    with dissolve
    
    mc "It's not about being human or about being something else..."
    mc "You have a heart, "
    extend "you've got feelings," 
    extend " you get hurt, "
    extend " you feel pain,"
    extend " loneliness..."
    extend " happiness..."  
    mc "There's nothing different between us at all..."
    mc "At least that's what I've come to understand..."
    mc "You have goodness in you. I know that, I'm sure of it."
    
    g"No I'm-"
    mc "Yes, you do. Otherwise, why would you even bother going out into the rain getting those herbs for me."
        
    hide gSighU
    with dissolve
    show gIdleU at right
    with dissolve
    
    g "... ... ..."
    
    hide mSadS
    with dissolve
    show mIdleS at left
    with dissolve
    
    mc "It's getting cold..." 
    
    hide mIdleS
    with dissolve
    show mHappyS at left
    with dissolve

    mc "Why don't we sit beside the fire to warm ourselves up?"
    mc "Oh and..." 
    
    hide mHappyS
    with dissolve
    
    play sfx3 ("OB_sound/Clothes.ogg")
    
    mc "Here... you might want this back."
    
    show mHappyn at left
    with dissolve
    
    hide gIdleU
    with dissolve
    show gShyU at right
    with dissolve
    
    g "Keep it on..." 
    mc "No, it's okay. You can have it back..." 
    mc "Besides, I'm sure just having that small campfire here isn't enough to warm you up."
    
    hide mHappyn
    with dissolve
    show mFidgetn at left
    with dissolve
    
    mc "I'll just sit there and use these big leaves to keep warm..."
    
    play sfx3 ("OB_sound/Clothes.ogg")
    
    g "... ... ..."
    
    hide gShyU
    with dissolve
    show gBlush at right
    with dissolve
    
    g "... T-Thank you..."
    "That sounded slightly strange coming from him. But to hear him say that makes me a little happy."
    "I planted myself near the fire with my knees close to my chest."
    "I pulled a few of the big leaves towards me that were on the floor and used them to cover myself."
    
    hide gBlush
    with dissolve
    show gIdle 
    with dissolve
    
    "It was unexpected but Goro moved over and sat next to me."
    
    hide mFidgetn
    with dissolve
    show mIdlen at left
    with dissolve
    
    "This feels slightly strange and a bit uncomfortable because we've only ever sat on opposite sides from each other."
    mc "Is something the matter?"
    
    hide gIdle
    with dissolve
    show gSigh
    with dissolve
    
    g "Those leaves won't be enough..."
    extend " t-to keep warm."
    g "So I'll sit here..."
    
    hide gSigh
    with dissolve
    show gBlush
    with dissolve
    
    g "Next..." 
    extend " to you..."
    g "... ... ..." 
    
    hide mIdlen
    with dissolve
    show mFidgetn at left
    with dissolve
    
    mc "O-okay..."

    "That's very kind of him..." 
    
    hide mFidgetn
    with dissolve
    show mSighn at left
    with dissolve
    
    mc "Cough, cough..."
    
    hide gBlush
    with dissolve
    show gIdle
    with dissolve
    
    g "Are you... okay?"
    mc "Yeah..."
    extend "I'm fine..." 
    mc "Cough, cough..."
    g "... ... ..."
    "I looked away from Goro as I coughed, while trying to supress it by holding it in at the same time."
    "I then took a deep breath and exhaled."
    "Seems like it's stopped for now."
    "Suddenly I felt a presence from behind.\n"
    extend "Goro had moved even closer."
    
    hide mSighn
    with dissolve
    show mShockn at left
    with dissolve
    
    mc "G-Goro?\n"
    extend "What are you-"
    
    hide gIdle
    with dissolve
    show gBlush
    with dissolve
    
    g "Shut up...\n" 
    extend "J-Just hold still."
    
    scene bg_Goro7
    with fade
    
    play sfx3 ("OB_sound/Clothes.ogg")
    play Sound1 ("OB_music/Silence.ogg") fadein 5.0
    
    "He's too close!\n"
    extend "I can feel his big body pressing against my back..."
    g "... ... ..."
    "I hope he's warm enough. Just by touching him I can feel he's extremely cold."
    mc "U-Um..." 
    g "W-What?"
    mc "Uh, no..." 
    extend " It's nothing..."
    g "I-If you don't like it. Just tell me."
    mc "N-No that's not it..." 
    mc "Just..."
    extend " a little surprised..." 
    extend "that's all..."
    "And very unexpected."
    "H-Huh?"
    "Why am I feeling nervous all of a sudden?\n"
    "I know he's just trying to keep me from getting cold...\n"
    extend "That all, nothing to it!"
    
    mc "Um...\n" 
    extend "Thank you for the herb and fruit juice earlier..." 
    extend " I feel a lot better..."
    mc "And..." 
    extend " I'm sorry for shouting at you earlier..."
    mc "... ... ..."
    g "It's okay..."
    extend " I don't mind..."
    
    "It wasn't my intention to raise my voice at him but keeping all my thoughts bottled up for so long..."
    extend " just ended up exploding."
    
    mc "... ... ..."
    mc "You know..."
    mc "Before coming to this Island, I was on a trip."
    mc "It was the very first time I got permission to do something I've always wanted to. Without being chained to a room."  
    g "Your..." 
    extend " first time?"
    mc "Yeah..." 
    extend " it made me really happy, that my parents finally agreed to let me go on a trip." 
    mc "Although my parents didn't come with me."
    g "You went alone?"
    mc "No. I was with a tour group, I wasn't particularly alone... just sad..."
    g "Why didn't you go with your family?"
    
    "I hesistated at those words for a moment."

    mc "My parents prefer to spend more time at work than with their own child." 
    extend " There'll be days and even months where I don't get to see them at all." 
    mc "The house we live is normally empty because of their busy schedule."
    mc "I guess you could say they just don't have the time for anything else." 
    g "Don't you have any siblings or friends?"
    mc "I'm the only child in the family..."
    extend " as for friends, I don't have any either."
    
    mc "But that's all because I was kept inside the house every day." 
    g "So you wasn't allowed to go outside?"
    mc "... ... ..."
    mc "When I was five there was a time when I was kidnapped by some really bad people." 
    mc "The kidnappers at the time demanded a ransom in exchange for my safety."
    mc "I can't remember how long I was held hostage. But it was scary..."
    mc "There were times where they'd left me in a small empty room with no light for hours."
    mc "Of course I cried... unable to do anything and missing my parents." 
    mc "Some days later I was found and rescued in a rundown cabin..." 
    mc "I was really too young to understand what was going on at the time."
    mc "Even so it wasn't until I was older that I'd finally realised what had happened to me back then."
    mc "But..."
    extend " it was after that incident that my parents decided to keep me inside the house..." 
    extend " I wasn't allowed to go out. Everything I did, I had to do it at home."  
    g "... ... ..."
    mc "Hehe..." 
    extend " sorry... I didn't mean to tell you something so depressing..."
    g "No."
    extend " It's fine..." 
    mc "A-Anyway...\n" 
    mc "I was happy that I'd finally gotten the permission to go on a tour."
    mc "You can probably guess what happens next..."
    mc "The cruise ship I was on for my tour was swallowed up by the sea because of a huge storm."
    mc "I remember evacuating onto these life boats..." 
    extend " but the waves was so strong that I got swept away into the currents..."
    extend " and that's how I ended up here..."  
    
    "I watched the flames in front of me as I paused. Thinking if I had said too much."
    "To be honest, I've never spoken to anyone about my past. Not even to the people for homeschooling."
    
    g "Are you angry at your parents?"
    mc "Why?"
    g "For locking you up?"
    mc "I'm...\n" 
    extend "No... I can't say that I am. They only did it to protect me..."
    "A short silence came between us as I watched the flames in front of me flicker ever so gently." 
    g "Were you..." 
    extend " lonely?"

    "Those words that he muttered under his breath was the first I've ever heard that not even my parents had asked."
    mc "N-no..."
    extend "I wasn't..."
    "I was never very good at hiding my emotions even though I always tried to make it sound like everything was fine."
    "Which is why ending up on this deserted island, only to wake up and find no one but myself here was quite scary."  
    "I shuddered at the thought of being desserted and alone..."
    extend " and of my past."
    
    
    g "I'm sorry..."
    scene bg_Goro8
    with Dissolve(1.0)

    
    "It was then that Goro started to wrap his arms around me."
    "I flinched unexpectedly from his actions but even so he held me tighter,"
    extend " holding me"
    extend " and hugging me ever so gently."
    "I was completely taken aback from his actions that I began to feel something well up inside of me."
    
    g "I'm..."
    extend " sorry..."
    
    "It was those words he muttered gently to my ear that I was no longer able to hold it in..."
    mc "H-Huh?" 
    "What's wrong with me all of a sudden?"
    mc "W-why are you apologising?"
    mc "Why..." 
    "Why won't...\n"
    extend "These tears stop falling..."
    
    g "... ... ..." 
    "Tears rolled from my face as I began crying like I've never cried before." 
    "I tried my best to stop as I wiped them from my eyes but Goro did nothing but held me tighter." 
    "It's been such a long time since I've cried like this..."
    "I feel so ashamed, so embarrassed..." 
    "As the storm raged outside with the fire crackling in front of us. I continued to drown in my own tears." 
    "Somewhere between all of that. I was sure I heard Goro whispering to me... "
    extend "telling me that everything will be okay..."
    
    stop Sound1 fadeout 2.0
    
    "That night I spent every waking hour in his arms.\n"
    "Eventually falling into a deep sleep..."
    
    scene bg_incave
    with fade
    
    g "... ... ..."
    
    play sfx3 ("OB_sound/Clothes.ogg")
    
    mc "Ungmmm..."
    mc "Hmmm...?" 
    
    "I woke up to find Goro sitting near the fire grilling a few fishes."
    
    show gShy at right
    with dissolve

    g "Sorry..." 
    extend " did I wake you?"

    mc "Oh..."
    mc "No you didn't..."
    
    g "Your clothes are dried..." 
    extend " I left them beside you."
    
    "That's very considerate of him..."
    "It became apparent to me that I was naked the whole night with Goro beside me."
    "Feeling slightly embarrassed I grabbed my clothes and got dressed with my back facing him." 
    
    play sfx3 ("OB_sound/Clothes.ogg")
    
    g "How are you feeling?"
    
    play Sound1 ("OB_music/PleasantFeeling.ogg") fadein 3.0
    
    show mHappy at left
    with dissolve
    
    mc "I feel great."
    
    hide mHappy
    with dissolve
    show mFidget at left
    with dissolve
    
    mc "T-Thank you..." 
    extend " for last night..."
    
    hide gShy
    with dissolve
    show gShock at right
    with dissolve
    
    g "!"
    
    hide gShock
    with dissolve
    show gBlush at right
    with dissolve
    
    g "I-It was nothing..."
    extend " you don't need to thank me for it..."
    
    g "I-I'm just making some fish..."
    g "... ... ..." 
    g "You..." 
    extend " want some?"
    
    hide mFidget
    with dissolve
    show mHappy at left
    with dissolve
    
    mc "... Yes please..."
    
    hide mHappy
    hide gBlush
    with dissolve
    show mIdle at left
    show gIdle at right
    with dissolve
    
    "He sat beside me all night..."
    extend " I wonder if he had gotten any sleep."
    "I watched as he takes one of the fishes from the fire and gives it to me."
    
    g "Eat while it's hot." 
    
    hide mIdle
    with dissolve
    show mHappy at left
    with dissolve
    
    mc "Thank you..."
    
    hide gIdle
    with dissolve
    show gShy at right
    with dissolve
    
    g "... ... .."
    g "Your name..."
    
    hide mHappy 
    with dissolve
    show mIdle at left
    with dissolve
    
    mc "?"
    "I looked at him slightly confused."
    
    g "Y-Your name..."
    extend " it's [povname] wasn't it?" 
    
    hide mIdle
    with dissolve
    show mFidget at left
    with dissolve
    
    mc "Y-yeah..."
    "That's the first time he's ever called my name."
    g "I'll try..."
    mc "... ... ..."
    
    hide gShy
    with dissolve
    show gBlush at right
    with dissolve
    
    g "I'll try..."
    extend " calling by your name from now on...."
    
    hide mFidget
    with dissolve
    show mShock at left
    with dissolve
    
    hide mShock
    with dissolve
    show mHappy at left
    with dissolve
    
    hide gBlush
    with dissolve
    show gShock at right
    with dissolve
    
    g "W-What!?"
    mc "I'm just really happy."
    mc "Thanks Goro..."
    
    hide gShock
    with dissolve
    show gBlush at right
    with dissolve
    
    stop Sound1 fadeout 2.0
    
    g "Umm... s-sure..."
    
    jump Chapter5
    
    return