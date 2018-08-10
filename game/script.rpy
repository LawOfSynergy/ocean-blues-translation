# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
# Declare characters used by this game.
#define mc = Character('Ray', color="#000000")
#define goro = Character('Goro', color = "#ffffff")
init python:

    #looping sound and music
    renpy.music.register_channel("Sound1", "music", True)
    renpy.music.register_channel("sfx1", "sfx", True)
    renpy.music.register_channel("sfx2", "sfx", True)
    renpy.music.register_channel("sfx3", "sfx", False)
    renpy.music.register_channel("sfx4", "sfx", True)

init:
    # Set Language to Spanish
    renpy.change_language("spanish")

    $ bonus = 0

    # Setting new calling positions
    $ left2 = Position(xpos=0.25, xanchor='left')
    $ right2 = Position(xpos=0.90, xanchor='right')

    # The variable we store the entered name of the character in.
    $ povname = ""
    $ povlast = ""

    # And this is a DynamicCharacter that has the same stored in
    # povname.
    $ pov = DynamicCharacter("povname", color=(64, 64, 64, 255))
    $ povl = DynamicCharacter("povlast", color=(64, 64, 64, 255))

    ##Transition Effect
    $ flash = Fade(.25, 0, .75, color="#fff")
    $ redFlash = Fade(.25, 0, .75, color="#FF0000")
    $ whiteFade = Fade(1.0, 0, .75, color="#fff")



    #Character Text name
    $ mc = DynamicCharacter(_('povname'),
                       window_background="UI/talkBox1.png",
                       what_outlines=[(1, "#000000", 0, 0)],#, (3, "#282", 0, 0)],
                       show_two_window=True)
                       #ctc=anim.Filmstrip("circle.png", (20, 20), (2, 1), .30, xpos=850, ypos=560, xanchor=0, yanchor=0),
                       #ctc_position="fixed")

    #$ mcl = DynamicCharacter(_('povlast'),
                      # window_background="UI/talkBox1.png",
                       #what_outlines=[(2, "#000000", 0, 0)],#, (3, "#282", 0, 0)],
                       #show_two_window=True)
                       #ctc=anim.Filmstrip("circle.png", (20, 20), (2, 1), .30, xpos=850, ypos=560, xanchor=0, yanchor=0),
                       #ctc_position="fixed")

    #$ mc = Character(_('Ray'),
                       # window_background="UI/talkBox1.png",
                        #what_outlines=[(1, "#000000", 0, 0)],#, (3, "#282", 0, 0)],
                        #show_two_window=True)
                        #ctc=anim.Filmstrip("circle.png", (20, 20), (2, 1), .30, xpos=850, ypos=560, xanchor=0, yanchor=0),
                        #ctc_position="fixed"

    $ g = Character(_('Goro'),
                           window_background="UI/talkBox.png",
                           what_outlines=[(1, "#003131", 0, 0)],#, (3, "#282", 0, 0)],
                           show_two_window=True)
                           #ctc=anim.Filmstrip("circle.png", (20, 20), (2, 1), .30, xpos=850, ypos=560, xanchor=0, yanchor=0),
                           #ctc_position="fixed")

    $ msub = Character(_('????'),
                           window_background="UI/talkBox1.png",
                           what_outlines=[(1, "#003131", 0, 0)],#, (3, "#282", 0, 0)],
                           show_two_window=True)
                           #ctc=anim.Filmstrip("circle.png", (20, 20), (2, 1), .30, xpos=850, ypos=560, xanchor=0, yanchor=0),
                           #ctc_position="fixed")

    $ sub = Character(_('????'),
                           window_background="UI/talkBox.png",
                           what_outlines=[(1, "#003131", 0, 0)],#, (3, "#282", 0, 0)],
                           show_two_window=True)
                           #ctc=anim.Filmstrip("circle.png", (20, 20), (2, 1), .30, xpos=850, ypos=560, xanchor=0, yanchor=0),
                           #ctc_position="fixed")

    $ snake = Character(_('Snake'),
                           window_background="UI/talkBox2.png",
                           what_outlines=[(1, "#003131", 0, 0)],#, (3, "#282", 0, 0)],
                           show_two_window=True)

    $ t = Character(_('Tiger'),
                           window_background="UI/talkBox2.png",
                           what_outlines=[(1, "#003131", 0, 0)],#, (3, "#282", 0, 0)],
                           show_two_window=True)


#Delcare custom transitions

init:

    python:

        import math

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #

#

define fBlack = Fade(1.0, 0.0, 1.0)


#Declare Main Character sprite
image mIdle = "MainC/MainP1C.png"
image mShock = "MainC/MainP2C.png"
image mPumped = "MainC/MainP3C.png"
image mHurt = "MainC/MainP4C.png"
image mFidget = "MainC/MainP5C.png"
image mSad = "MainC/MainP6C.png"
image mSigh = "MainC/MainP7C.png"
image mRelax = "MainC/MainP8C.png"
image mHappy = "MainC/MainP9C.png"
image mAngry = "MainC/MainP10C.png"
image mDuh = "MainC/MainP10DuhC.png"
image mCry = "MainC/MainP15C.png"
image mBlush = "MainC/MainP5Cb.png"

image mIdle_flip = im.Flip("MainC/MainP1C.png", horizontal=True)
image mShock_flip = im.Flip("MainC/MainP2C.png", horizontal=True)
image mPumped_flip = im.Flip("MainC/MainP3C.png", horizontal=True)
image mHurt_flip = im.Flip("MainC/MainP4C.png", horizontal=True)
image mFidget_flip = im.Flip("MainC/MainP5C.png", horizontal=True)
image mSad_flip = im.Flip("MainC/MainP6C.png", horizontal=True)
image mSigh_flip = im.Flip("MainC/MainP7C.png", horizontal =True)
image mRelax_flip = im.Flip("MainC/MainP8C.png", horizontal=True)
image mHappy_flip = im.Flip("MainC/MainP9C.png", horizontal=True)
image mCry_flip = im.Flip("MainC/MainP15C.png", horizontal=True)
image mFidgetn_flip = im.Flip("MainC/MainP5.png", horizontal=True)

#Main naked here -----------
image mIdlen = "MainC/MainP1.png"
image mShockn = "MainC/MainP2.png"
image mPumpedn = "MainC/MainP3.png"
image mHurtn = "MainC/MainP4.png"
image mFidgetn = "MainC/MainP5.png"
image mSadn = "MainC/MainP6.png"
image mSighn = "MainC/MainP7.png"
image mRelaxn = "MainC/MainP8.png"
image mHappyn = "MainC/MainP9.png"
image mDuhn = "MainC/MainP10Duh.png"
image mBlushn = "MainC/MainP5b.png"

#Main Ill here ---------------
image mIdleS = "MainC/MainP14C.png"
image mSadS = "MainC/MainP11C.png"
image mSighS = "MainC/MainP12C.png"
image mHappyS = "MainC/MainP13C.png"

#Main 5Y
image aIdle = "MainC/nMain1.png"
image aHappy = "MainC/nMain2.png"
image aCry = "MainC/nMain3.png"
image aSigh = "MainC/nMain4.png"

#Declare Goro Character Sprite-------------
image gIdle = "Goro/GoroP1C.png"
image gSigh = "Goro/GoroP2C.png"
image gPoint = "Goro/GoroP3C.png"
image gAnnoyed = "Goro/GoroP4C.png"
image gShy = "Goro/GoroP5C.png"
image gShock = "Goro/GoroP6C.png"
image gAngry = "Goro/GoroP7C.png"
image gHappy = "Goro/GoroP8C.png"
image gBlush = "Goro/GoroP9C.png"
image gBlood = "Goro/GoroP14C.png"

#Goro Naked here---------------
image gIdlen = "Goro/GoroP1.png"
image gSighn = "Goro/GoroP2.png"
image gPointn = "Goro/GoroP3.png"
image gAnnoyedn = "Goro/GoroP4.png"
image gShyn = "Goro/GoroP5.png"
image gShockn = "Goro/GoroP6.png"
image gAngryn = "Goro/GoroP7.png"
image gHappyn = "Goro/GoroP8.png"
image gBlushn = "Goro/GoroP9.png"
image gSighbn = "Goro/GoroP2b.png"
image gShockbn = "Goro/GoroP6b.png"

#Goro Underwear here --------------
image gIdleU = "Goro/GoroP10C.png"
image gSighU = "Goro/GoroP11C.png"
image gShyU = "Goro/GoroP12C.png"
image gShockU = "Goro/GoroP13C.png"
image gHappyU = "Goro/GoroP15C.png"
image gLaughU = "Goro/GoroP16C.png"
image gBlushU = "Goro/GoroP17C.png"


image gIdle_flip = im.Flip("Goro/GoroP1C.png", horizontal=True)
image gSigh_flip = im.Flip("Goro/GoroP2C.png", horizontal=True)
image gPoint_flip = im.Flip("Goro/GoroP3C.png", horizontal=True)
image gAnnoyed_flip = im.Flip("Goro/GoroP4C.png", horizontal=True)
image gShy_flip = im.Flip("Goro/GoroP5C.png", horizontal=True)
image gShock_flip = im.Flip("Goro/GoroP6C.png", horizontal=True)
image gAngry_flip = im.Flip("Goro/GoroP7C.png", horizontal=True)
image gHappy_flip = im.Flip("Goro/GoroP8C.png", horizontal=True)
image gBlush_flip = im.Flip("Goro/GoroP9C.png", horizontal=True)
image gBlood_flip = im.Flip("Goro/GoroP14C.png", horizontal=True)

#Declare Subs
image sIdle = "Sub/Snake1.png"
image sAttack = "Sub/Snake2.png"
image tiger = "Sub/Tiger.png"
image tiger_flip = im.Flip("Sub/Tiger.png", horizontal=True)

#Declare background images
image bg_ship1 = "Scenes/ShipScene.png"
image bg_ship2 = "Scenes/ShipScene2.png"
image bg_beach = "Scenes/BeachScene.png"
image bg_forest1 = "Scenes/ForestScene.png"
image bg_forest2 = "Scenes/ForestScene2.png"
image bg_forest3 = "Scenes/ForestScene3.png"
image bg_forest4 = "Scenes/ForestScene4.png"
image bg_forest5 = "Scenes/ForestScene5.png"
image bg_forest6 = "Scenes/ForestScene6.png"
image bg_waterfall = "Scenes/WaterfallScene.png"
image bg_hotspring = "Scenes/HotspringScene.png"
image bg_wall = "Scenes/Wall.png"
image bg_outcave = "Scenes/CaveOuter.png"
image bg_incaveD = "Scenes/CaveInsideD.png"
image bg_incave = "Scenes/CaveInside.png"
image bg_boat1 = "Scenes/BoatScene1.png"
image bg_boat2 = "Scenes/BoatScene2.png"
image bg_stars = "Scenes/StarsScene.png"

image bg_black = "Scenes/BlackScene.png"
image bg_badscene = "Scenes/BadScene.png"
image bg_endscene = "Scenes/EndScene.png"

image ui_firstn = "UI/FirstName.png"
image ui_lastn = "UI/LastName.png"
#Declare Special Event

image bg_Goro1 = "ScenesEvent/wCrack.png"
image bg_Goro1a = "ScenesEvent/wCrack2.png"
image bg_Goro2 = "ScenesEvent/tFall.png"
image bg_Goro3 = "ScenesEvent/HotSpring.png"
image bg_Goro4 = "ScenesEvent/mClimb.png"
image bg_Goro5 = "ScenesEvent/mAwake.png"
image bg_Goro6 = "ScenesEvent/mAwake2.png"
image bg_Goro7 = "ScenesEvent/wHug.png"
image bg_Goro8 = "ScenesEvent/wHug2.png"
image bg_Goro9 = "ScenesEvent/HotSpring2.png"
image bg_Goro10 = "ScenesEvent/HotSpring3.png"
image bg_Goro11 = "ScenesEvent/gKiss.png"
image bg_Goro12 = "ScenesEvent/gSleep.png"
image bg_Goro13 = "ScenesEvent/gSleep2.png"
image bg_Goro14 = "ScenesEvent/mFrustration.png"
image bg_Goro15 = "ScenesEvent/mSharp.png"
image bg_Goro16 = "SCenesEvent/gConfess.png"
image bg_Goro17 = "ScenesEvent/gKiss2.png"
image bg_Goro18 = "ScenesEvent/gKiss3.png"

image bg_xBadL = "ScenesEvent/xSceneBadL.png"
image bg_xBadM = "ScenesEvent/xSceneBadM.png"
image bg_xBadR = "ScenesEvent/xSceneBadR.png"
image bg_xBad2 = "ScenesEvent/xSceneBad2.png"
image bg_xBad3 = "ScenesEvent/xSceneBad3.png"
image bg_xBad3c = "ScenesEvent/xSceneBad3c.png"

image bg_xGoodL = "ScenesEvent/xSceneGoodL.png"
image bg_xGoodR = "ScenesEvent/xSceneGoodR.png"
image bg_xGoodRc = "ScenesEvent/xSceneGoodRc.png"
image bg_xGood3 = "ScenesEvent/xSceneGood3.png"
image bg_xGood3c = "ScenesEvent/xSceneGood3c.png"


image bg_badEnd = "ScenesEvent/gDies.png"
image bg_badEnd2 = "ScenesEvent/mDies.png"

image bg_goodEnd = "ScenesEvent/gEnd.png"

image bg_Rain = "ScenesEvent/RainEvent.png"
image bonus1 = "ScenesEvent/xMag.png"

image bg_tEnd1 = "ScenesEvent/tEnd1.png"
image bg_tEnd2 = "ScenesEvent/tEnd2.png"
image bg_tEnd3 = "ScenesEvent/tEnd3.png"
image bg_tEnd4 = "ScenesEvent/tEnd4.png"
image bg_tEnd5 = "ScenesEvent/tEnd5.png"
image bg_tEnd6 = "ScenesEvent/tEnd6.png"
image bg_tEnd7 = "ScenesEvent/tEnd7.png"
image bg_tEnd8 = "ScenesEvent/tEnd8.png"
image credits = "ScenesEvent/Credits.png"

image alert1 = "UI/Alert1.png"
image alert2 = "UI/Alert2.png"

# The game starts here.
label splashscreen:
    scene black
    with Pause(1)

    scene alert1
    with dissolve
    with Pause (5)

    scene alert2
    with dissolve
    with Pause (5)

    return

label start:

    stop music

    scene bg_ship1
    with dissolve
    $renpy.pause(3.0, hard=True)

    play sfx1 ("OB_sound/Rain.ogg") fadein 1.0
    scene bg_ship2
    with dissolve
    $renpy.pause(4.0, hard=True)

    scene bg_ship2
    with flash
    play sfx3 ("OB_sound/Thunder.ogg")
    $renpy.pause(2.0, hard=True)

    stop sfx1 fadeout 1.0

    jump Chapter1

    return
