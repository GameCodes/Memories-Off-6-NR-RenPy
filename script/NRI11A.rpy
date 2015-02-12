label NRI11A:
    $currentlabel = "NRI11A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '28'
    $date = '5'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#GRAPH_INI 
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/BG89NA@2x.jpg" as bg1 zorder 1 with dissolve
    scene expression "img/BG89NA@2x.jpg" as bg0 with dissolve
    play sound "SE08_04L"
    pause (32/32.0)
#FADE_IN 1
    play music  "BGM02"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "我们把饭菜装到盘子里后，坐到了位子上。"
    window hide
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/EXBG05N@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA01"),"True","img/RI_ZBA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    stop sound
    hide bg1 with dissolve
    志雄 "「果然没有看似和我们同龄的人呢。」"
    voice "NRI11A_RI000"
    莉莉丝 "「现在不是毕业旅行的时候，而且感觉这里也不适合年轻人来。」"
    志雄 "「不过，我还真是服了稻穗了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBC04"),"True","img/RI_ZBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI11A_RI001"
    莉莉丝 "「虽然是受婆婆之托……酪萨克没关系吗？」"
    "说的也是呢……在酪萨克里稻穗也算是个很重要的角色……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD01"),"True","img/RI_ZBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI11A_RI002"
    莉莉丝 "「啊，这个很好吃呢！」"
    "莉莉丝吃着天妇罗说道。"
    志雄 "「对旅馆来说，好吃的料理是很重要的吧？」"
    voice "NRI11A_RI003"
    莉莉丝 "「这可是婆婆的朋友开的旅馆。这方面当然不可能会差。」"
    voice "NRI11A_RI004"
    莉莉丝 "「志雄也吃吃看吧？」"
    "莉莉丝若无其事地夹着天妇罗递给我。"
    志雄 "「诶，那个，能放在其他盘子里的话……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD04"),"True","img/RI_ZBD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI11A_RI005"
    莉莉丝 "「快点吃啦，我一直夹着很累的」"
    志雄 "「啊，啊啊……」"
    "这样下去莉莉丝会一直夹着不放，估计心情也会变差……哎，没办法了。"
    "我下定决心，准备吃下莉莉丝递给我的天妇罗——"
    stop music fadeout 18
    voice "NRI11A_YG000"
    雄吾？ "「哦，两人关系很好嘛！」"
    voice "NRI11A_KR000"
    香里？ "「雄吾，不能妨碍他们啦。」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBB03"),"True","img/RI_ZBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE03_12"
#QUA2_CHR 0
    "突然听到背后发出的声音，我和莉莉丝都为之一震。"
    "这，这熟悉的声音是——"
#BG_INIC 1
    scene expression "img/BG89NA@2x.jpg" as bg1
#CHR_SET_BACK
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 1,(320-160)
#CHR_POSC 2,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    with dissolve
    if not persistent.dictlist[10] and persistent.show_dict:
        $persistent.dictlist[10]=True
        show screen dict_pop(i=10)
    if not persistent.dictlist[12] and persistent.show_dict:
        $persistent.dictlist[12]=True
        show screen dict_pop(i=12)
#MES_SYNC2
    voice "NRI11A_RI006"
    莉莉丝 "「妈妈！？」"
    志雄 "「爸爸！？」"
    play music  "OBGM02"
    voice "NRI11A_YG001"
    雄吾 "「真是巧呢，没想到会在这里见到你们。」"
    voice "NRI11A_KR001"
    香里 "「雄吾……再怎么说，也不可能这么巧吧？」"
    voice "NRI11A_RI007"
    莉莉丝 "「为、为什么妈妈会在这里啊！？」"
    voice "NRI11A_KR002"
    香里 "「当然会在啊，我也是被母亲邀请来这里的啊？」"
    voice "NRI11A_RI008"
    莉莉丝 "「诶？」"
    志雄 "「啊，说起来……」"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG17EA@2x.jpg" as bg2 zorder 200 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_LAA02"),"True","img/FU_LAA02A@2x.png") as lh0 zorder (1000-0):
        ypos 0.0
    with dissolve
#SE_VOLC 1,0
#MUS_VOL 64
#BG_INIC 1
#BG_PRI 1
#CHR_ERSWC 1,2
#CHR_ALPC 0
#BG_ALPC 1
#BG_ALPC 2
#BG_BLUR 2
    voice "NRI04A_FU005B_K"
    富美子 "「当然。志雄已经像是我们家族一员的存在了。」"
    window hide
#BG_SET_BACK 
#BG_INIC 0
#BG_ALPC 0
    scene expression "img/EXBG05N@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#SE_VOLC 1,16
#MUS_VOL 128
#BG_INIC 1
#BG_PRI 1
    hide lh1 with dissolve
    scene expression "img/EXBG05N@2x.jpg" as bg0 with dissolve
    hide bg2 with dissolve
    hide lh0 with dissolve
#BG_ALPC 0
#CHR_INIC 1
#CHR_POSC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBC04"),"True","img/RI_ZBC04A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#BG_BLUR 0
    hide bg1 with dissolve
    志雄 "「那时富美子婆婆说的家族旅行……是这个意思吗？」"
    "不止我和莉莉丝，连我老爸和莉莉丝的母亲也来了。在这里的，毫无疑问的是一个家庭。"
    voice "NRI11A_RI009"
    莉莉丝 "「婆婆这次送给我们的意外真是太多了……」"
    "伴随着叹气声，莉莉丝小声说道。"
    "突然变成和莉莉丝两个人的旅行，稻穗的登场，最后还有老爸和香里阿姨。"
    "这也太恶搞了吧，富美子婆婆。"
    "该不会她本来就不准备来吧……"
    志雄 "「啊，对了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBB04"),"True","img/RI_ZBB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI11A_RI010"
    莉莉丝 "「怎么了？」"
    "我惊奇地看着莉莉丝。"
    志雄 "「老爸他们也住在旅馆的话，我们就不必担心房间的问题了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBB02"),"True","img/RI_ZBB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI11A_RI011"
    莉莉丝 "「啊……是、是呢……」"
    "本来应该是包括文子婆婆，我们三个一起来的，那么房间应该是三、四人用的，如果是这样，再加上老爸他们的话……"
    show expression "img/BG89NA@2x.jpg" as bg_over zorder 2 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 1,(320-160)
#CHR_POSC 2,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    with dissolve
#BG_BLUR 0
    voice "NRI11A_KR003"
    香里 "「对不起，我们已经订好别的房间了。」"
    志雄 "「诶？是这样吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA02"),"True","img/KR_MAA02A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA05"),"True","img/SF_MAA05A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    with dissolve
#THREAD_STA 1,THREAD_MOV_CHRW01
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    voice "NRI11A_YG002"
    雄吾 "「啊啊，那是当然的吧。我和香里怎么说也是新婚嘛。我们两对就分头行动吧。」"
#THREAD_WAT 1
    志雄 "「哈？等，等一下！这样好吗，老爸！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA02"),"True","img/SF_MAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI11A_YG003"
    雄吾 "「没事的。我相信你，志雄。总之……加油！」"
    "加什么油啊！？"
    "还有，不要眨眼啦，真令人不舒服。"
    voice "NRI11A_KR004"
    香里 "「那我们先走了，你们两个有什么事的话，随时可以叫我们。」"
    voice "NRI11A_RI012"
    莉莉丝 "「诶？不一起吃吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    voice "NRI11A_YG004"
    雄吾 "「年轻人就和年轻人一起吃吧。」"
    voice "NRI11A_KR005"
    香里 "「就是这样。加油哦，莉莉丝～♪」"
    voice "NRI11A_RI013"
    莉莉丝 "「真是的，连妈妈也这样……」"
    window hide
    stop music fadeout 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "老爸和香里阿姨微微一笑就离开了。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    play music  "BGM13"
    voice "NRI11A_KR006"
    香里 "「啊，对了对了。有件事忘说了。」"
    voice "NRI11A_RI014"
    莉莉丝 "「嗯？什么？」"
    "面对一脸惊异的莉莉丝，香里阿姨竖起大拇指，笑着说道。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_XAA02"),"True","img/KR_XAA02A@2x.png") as lh1 zorder (10-0):
        ypos 0.0
    with dissolve
    stop music fadeout 1
#ROUTINE_STA
#CHR_ALP_AUTOC 0,128,1,F24
#CHR_ALP_AUTOC 1,0,1,F24
#ROUTINE_STP
    voice "NRI11A_KR007"
    香里 "「关键时刻，女孩子要带头出击哟。」"
    play music  "OBGM02"
    voice "NRI11A_RI015"
    莉莉丝 "「妈、妈妈！？」"
    "带头做什么？"
    window hide
#ROUTINE_STA
#CHR_ALP_AUTOC 0,0,1,F24
#CHR_ALP_AUTOC 1,128,1,F24
#BG_BLUR 0
#ROUTINE_STP
    hide lh0 with dissolve
    voice "NRI11A_KR008"
    香里 "「那么，志雄君。要和莉莉丝和睦相处哟。这孩子就交给你咯。」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "这次香里阿姨和老爸终于一起走开了。"
    window hide
#CHR_ALPC 0
    show expression "img/EXBG05N@2x.jpg" as bg_over zorder 5
    show expression "img/RI_ZBA05A@2x.png" as lh0 zorder (10+0):
        xcenter ((320)/640.0)
    with dissolve
    voice "NRI11A_RI016"
    莉莉丝 "「真，真是的……妈妈也太……」"
    "莉莉丝目送着香里阿姨的背影抱怨着，像是在闹别扭又像是在生气。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD04"),"True","img/RI_ZBD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI11A_RI017"
    莉莉丝 "「你不要在意妈妈说的话啊！」"
    "香里阿姨是这么健谈的人吗？"
    "该不会是和老爸在一起之后近墨者黑了吧……"
    "唉，最近和莉莉丝处得也不错，算了吧。 "
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop se
    stop sound
    stop music fadeout 1
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_MOV_CHRW01
#CHR_POS_AUTOC 1,((320)-72),F123,48
#CHR_POS_AUTOC 2,((320)+72),F123,48
#CHR_POS_SAVEC 1
#CHR_POS_SAVEC 2
#EOT