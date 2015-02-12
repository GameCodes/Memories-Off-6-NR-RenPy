label NCL14A:
    $currentlabel = "NCL14A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '08'
    $day = '22'
    $date = '2'
    window hide
    scene expression Solid("000") with fade
    show expression "img/NIMG01D@2x.png" as bg0 zorder 0
    show expression "img/CloudD1_0@2x.png" as cloud0 zorder 5:
        ycenter .55
        xcenter .75
        linear 500 xcenter .0
    show expression "img/CloudD1_1@2x.png" as cloud1 zorder 5:
        ycenter .55
        xcenter .65
        linear 500 xcenter .0
    show expression "img/CloudD1_2@2x.png" as cloud2 zorder 8:
        ycenter .3
        block:
            xcenter 1.0
            linear 140 xcenter .0
            repeat
    show expression "img/CloudD2_1@2x.png" as cloud3 zorder 8:
        ycenter .2
        block:
            xcenter 1.0
            linear 100 xcenter .0
            repeat
    show expression "img/CloudD2_0@2x.png" as cloud4 zorder 8:
        ycenter .0
        block:
            xcenter 1.0
            linear 120 xcenter .0
            repeat
    show expression "img/CloudD3@2x.png" as cloud5 zorder 10:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.5
            linear 50 xpos .0
            xpos 1.0
            linear 50 xpos .5
            repeat
    with dissolve
    play sound "SE05_16L"
    pause (32/32.0)
#EFF_STAC 0,CLOUD_D,EFF_SKIP
#FADE_IN 1,128
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "经历了多少年的阴差阳错轮回，一家人终于能够真心交流了。"
    "几天之后……"
    window hide
#SE_VOLC 1,64
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 2,CAL_0822
    show expression "img/NIMG15G-568h@2x.jpg" as cal zorder 5
    show expression "img/08_22_TUESDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG81NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG81NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB05"),"True","img/CL_LAB05A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
#SE_VOLC 1,(64/2)
#BG_BLUR 0
#FADE_IN 1
    play music "BGM04"
    voice "NCL14A_KU000"
    克罗艾 "「唔……」"
    "再次造访自家的学姐，停在了公寓的大门前。"
    "我把手轻轻地放到学姐的背后，稍稍地推了一下学姐。"
    志雄 "「好啦，要在这里站到什么时候呢？」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC02"),"True","img/CL_LAC02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL14A_KU001"
    克罗艾 "「嗯，可是……」"
    志雄 "「不快点的话，就要错过约定的时间咯？」"
    "我装出些许愕然的声音说着。要是一本正经地问学姐『没关系吧』的话一定会让她更加紧张的。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC03"),"True","img/CL_LAC03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL14A_KU002"
    克罗艾 "「我知道啦……」"
    "听了我的话，学姐闹情绪似的把身子转向了一边。"
    "今天一早，接到了学姐父母打来的邀请电话。"
    志雄 "「爸爸也好，妈妈也好，都非常想念学姐呢，不是吗？」"
    voice "NCL14A_KU003"
    克罗艾 "「那个，倒是那样没错……」"
    志雄 "「所以，没关系的。一会儿直接打招呼就好了，距离会自然而然地缩短的。」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC02"),"True","img/CL_LAC02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL14A_KU004"
    克罗艾 "「那要是……没缩短呢？」"
    志雄 "「绝对不会的，一定能缩短之间的距离的。」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB03"),"True","img/CL_LAB03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL14A_KU005"
    克罗艾 "「为什么你能这么肯定呢？」"
    志雄 "「因为，是学姐的家人啊。」"
    "我挺起胸膛，做出断言。面对如此坚定的我，学姐终于展露了笑脸。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB04"),"True","img/CL_LAB04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL14A_KU006"
    克罗艾 "「的确，没有任何理由呢……」"
    志雄 "「是啊！」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB06"),"True","img/CL_LAB06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL14A_KU007A"
    克罗艾 "「哈哈……{w=4}{nw}"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB04"),"True","img/CL_LAB04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL14A_KU007B"
    extend "不过，志雄说的没错。因为是我的家人嘛。要直接地好好打招呼才行。」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "说着，学姐与我的手紧紧地牵在了一起。并肩踏进了公寓。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG82NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG82NA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAB01"),"True","img/YZ_MAB01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    "第一个迎接我们的是学姐的父亲。看到了父亲的身影，学姐不禁往我后面稍稍退了一步。"
    window hide
    play music "BGM10"
    voice "NCL14A_KZ000A"
    幸蔵 "「欢迎光临，志雄……{w=5}{nw}"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAB02"),"True","img/YZ_MAB02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCL14A_KZ000B"
    extend "还有，欢迎回家，克罗艾。」"
    志雄 "「是，打扰了。」"
    voice "NCL14A_KU008"
    克罗艾 "「我、我回来了，爸爸……」"
    "穿过走廊，首先映入眼帘的是桌上丰盛的饭菜。油炸出来的食物、煮好的菜肴还有沙拉等等，全部在桌子上星罗棋布地摆放着。"
    志雄 "「那个，这些是？」"
    "怎么看都是为了庆贺什么而准备的一样……"
    window hide
#CHR_SET_BACK
#CHR_INIC 3
#CHR_ALPC 3
#CHR_POSC 3,(320-192)
    hide lh3
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA02"),"True","img/YS_MAA02A@2x.png") as lh3 zorder (10-3):
        ypos 0.0
        xcenter .65
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAB02"),"True","img/YZ_MAB02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .35
    with move
#CHR_PRIC ID_ALL
#ROUTINE_STA
#CHR_POS_AUTOC 3,(320-96),F24
#CHR_ALP_AUTOC 3,128,1,F24
#CHR_POS_AUTOC 2,(320+96),F24
#ROUTINE_STP
    voice "NCL14A_EL000"
    爱丽丝 "「诶？比预想的来得早呢。」"
    "学姐的母亲带着烹饪用的手套从厨房里走了出来。手里端着的是刚刚做好的奶汁烤菜。"
    voice "NCL14A_KU009"
    克罗艾 "「那个，妈妈？这到底是……」"
    "学姐不禁小声地问道。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh3 zorder (10+3):
        ypos 0.0
    with dissolve
    voice "NCL14A_EL001"
    爱丽丝 "「看了应该就知道了吧？接下来是要庆祝啦。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh3 zorder (10+3):
        ypos 0.0
        xcenter .75
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAB02"),"True","img/YZ_MAB02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB02"),"True","img/NO_MAB02A@2x.png") as lh1 zorder (10-1):
        ypos .2
    with move
#CHR_SORT 0,1,2
#ROUTINE_STA
#CHR_ALP_AUTOC 1,128,1,F24
#CHR_POS_AUTOC 2,(320+160),F24
#CHR_POS_AUTOC 3,(320-160),F24
#ROUTINE_STP
    voice "NCL14A_NO000"
    诺艾儿 "「庆祝啦～」"
    "听到这个回答，我和学姐都有些不解。我，姑且试着说出了自己的疑问。"
    志雄 "「那个，是祝贺学姐父亲痊愈吗？」"
    "最近发生了许许多多的事情，想来应该是为这个吧？这样的话还是能够理解的。"
    window hide
#CHR_PRIC ID_ALL
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_INIC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA01"),"True","img/YZ_LAA01A@2x.png") as lh1 zorder 100:
        ypos 0.0
    with dissolve
    "不过，学姐的父亲却对我的这个结论摇了摇头。"
    voice "NCL14A_KZ001"
    幸蔵 "「不，这是为了祝贺别的事情的。」"
    voice "NCL14A_KU010"
    克罗艾 "「别的事情？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB02"),"True","img/YZ_LAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL14A_KZ002"
    幸蔵 "「咱们一家人好久都没有在一起了，现在团聚了，还没有为此而庆祝一下吧？」"
    voice "NCL14A_KU011"
    克罗艾 "「诶！？」"
    "听了父亲的话，学姐发出了惊讶的声音。于此同时，学姐的母亲开口说道。"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2,(320-192)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA02"),"True","img/YS_LAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .2
    with dissolve
    voice "NCL14A_EL002"
    爱丽丝 "「一会儿，要庆祝诺艾儿和爸爸还有姐姐见面哦～」"
    voice "NCL14A_KU012"
    克罗艾 "「啊……」"
    "学姐什么都没有说，只是更加紧握住我的手。"
    window hide
    hide lh1 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(448/8)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAA09"),"True","img/NO_LAA09A@2x.png") as lh1 zorder (10+1):
        ypos .2
    with dissolve
    "这时，正在帮忙的诺艾儿跑了过来。"
    voice "NCL14A_NO001"
    诺艾儿 "「呐，妈妈。」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA01"),"True","img/YS_LAA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCL14A_EL003"
    爱丽丝 "「怎么啦？」"
    voice "NCL14A_NO002"
    诺艾儿 "「为什么今天没做柿子椒呢？」"
    克罗艾 "「……」"
#MESEX_A M_NOA,A_CH_KU,NCL14A_KU013,"【クロエ】「……」%K%P"
    "学姐躲到了我的身后，把头埋在了我的背上。"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA03"),"True","img/YS_LAA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCL14A_EL004"
    爱丽丝 "「那个呢……其实你姐姐她不喜欢吃柿子椒啦……」"
#THREAD_STA 1,THREAD_ELISE_WHISPER
#MESA A_CH_EL,NCL14A_EL004,"【エリーズ】「那个呢……其实你姐姐她不喜欢吃柿子椒啦……」"
#THREAD_WAT 1
#MESX "%K%P"
    "学姐的母亲，看到学姐的样子什么都没有说，而是对诺艾儿低头耳语。像说悄悄话一般，不过这边也能够听得到声音。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_XAB03"),"True","img/NO_XAB03A@2x.png") as lh1 zorder (10+1):
        ypos .2
    with dissolve
    voice "NCL14A_NO003"
    诺艾儿 "「挑食是不行的！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,640
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XAC05"),"True","img/CL_XAC05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_XAB03"),"True","img/NO_XAB03A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .85
    with move
#MOV_CHR_INIT 48
#MOV_CHR0 128,(320+224)
#MOV_CHR1 ,(320-160)
#MOV_CHR_GO 1
#BG_SET_BACK 
#REEK_CHR 0
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NCL14A_KU014"
    克罗艾 "「对、对不起……」"
#THREAD_STP 1
#REMOVE_REEK_CHR 0
    "被诺艾儿教训了，学姐从我的肩膀处露出头来道了歉。"
    hide lh0 with dissolve
#CHR_POSC 1,(320-160),(448/8)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAB01"),"True","img/NO_LAB01A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL14A_NO004"
    诺艾儿 "「不过，没办法呢。为了让大家都开心，我就忍耐一下啦！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA02"),"True","img/YS_LAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    "诺艾儿挺起胸脯装作大人的样子说出原谅的话，学姐的母亲则温柔地抚摸着她的头。"
    voice "NCL14A_EL005"
    爱丽丝 "「嗯，真了不起。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAA07"),"True","img/NO_LAA07A@2x.png") as lh1 zorder (10+1):
        ypos .2
    with dissolve
    voice "NCL14A_NO005"
    诺艾儿 "「嘿嘿～」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_SCLC 0,384,384
#CHR_POSC 0,(320+96),(448/2)
#CHR_POSC 1,(320-96),(448/8)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC01"),"True","img/CL_MAC01A@2x.png") as lh0 zorder (10+0):
        xcenter .35
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAA01"),"True","img/NO_LAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .65
    "学姐的视线凝聚在了跑过来的诺艾儿身上。"
    voice "NCL14A_KU015"
    克罗艾 "「谢谢你，诺艾儿……」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAA02"),"True","img/NO_LAA02A@2x.png") as lh1 zorder (10+1):
        ypos .2
    with dissolve
    voice "NCL14A_NO006"
    诺艾儿 "「不用谢哦～」"
    window hide
    hide lh1 with dissolve
    "诺艾儿又吧嗒吧嗒地跑回厨房拿其他的碗碟去了。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 0,(320+224)
#CHR_POSC 1,(320-224)
#CHR_POSC 2
#CHR_DSPTC 0,1,2,CL_LAB05,YZ_LAA01,YS_LAA01
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB05"),"True","img/CL_LAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .85
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA01"),"True","img/YZ_LAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .15
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA01"),"True","img/YS_LAA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCL14A_KU016"
    克罗艾 "「呐，爸爸，妈妈……」"
    "看到父母的背影，学姐带着些许的不安，用一本正经的声音向他们开口说道。"
    voice "NCL14A_EL006"
    爱丽丝 "「嗯？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA06"),"True","img/YZ_LAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL14A_KZ003"
    幸蔵 "「怎么了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB04"),"True","img/CL_LAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL14A_KU017"
    克罗艾 "「如果，可以的话……我，可以回家来住吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA01"),"True","img/YZ_LAA01A@2x.png") as lh1 zorder (10+1)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA02"),"True","img/YS_LAA02A@2x.png") as lh2 zorder (10+2)
    voice "NCL14A_EL007"
    爱丽丝 "「嗯……当然啦。这里本来就是你的家啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB02"),"True","img/YZ_LAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL14A_KZ004"
    幸蔵 "「住回来是理所应当的嘛。」"
    "听到了父母应允的话语，学姐无法抑制从心底涌出的喜悦，脸上洋溢着幸福的笑容。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB06"),"True","img/CL_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL14A_KU018"
    克罗艾 "「嗯！」"
    window hide
#FADE_OUT 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_UVC 0,0,(448/8),(640/2),(448/2)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 0,(448/8)
#CHR_POSC 1,(320-224)
#CHR_POSC 2,(320+224)
#CHR_SETTC 0,1,2,NO_LAA02,YZ_LAA02,YS_LAA02
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAA02"),"True","img/NO_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .85
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA02"),"True","img/YZ_LAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .15
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA02"),"True","img/YS_LAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    pause (32/32.0)
#FADE_IN 1
    "全家人围坐餐桌前，晚饭开始了。在这里有快乐，也有幸福，更有这一家人团聚的美妙时光。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA04"),"True","img/YS_LAA04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCL14A_EL008"
    爱丽丝 "「喂，诺艾儿。这边的豆腐也要吃点啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAA03"),"True","img/NO_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL14A_NO007"
    诺艾儿 "「诶～那个好难吃啦，不要～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB04"),"True","img/YZ_LAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL14A_KZ005"
    幸蔵 "「诺艾儿，吃豆腐对身体可好哦？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAA04"),"True","img/NO_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL14A_NO008"
    诺艾儿 "「不想吃就是不想吃～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB05"),"True","img/YZ_LAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL14A_KZ006"
    幸蔵 "「这可怎么办好呢，克罗艾也说说她嘛。」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL09A")]=True
    show expression "img/EVN_CL09A@2x.jpg" as bg1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NCL14A_KU019"
    克罗艾 "「诶？那个……诺艾儿？挑食可是不行的哦。会长不高的哦？」"
    voice "NCL14A_NO009"
    诺艾儿 "「姐姐不也是不吃柿子椒的吗？」"
    voice "NCL14A_KU020"
    克罗艾 "「好、好了啦，姐姐已经长得很高了！」"
    voice "NCL14A_NO010"
    诺艾儿 "「那诺艾儿长不高也无所谓了啦～」"
    voice "NCL14A_KU021"
    克罗艾 "「志雄，换你了……」"
    志雄 "「诶，我！？」"
    "平和的气氛，融洽的谈话。经管依然难为情，尽管依然有暂时无法消融的残存心结，不过，此时此刻，温暖幸福的感觉正拥抱着我们每一个人。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/BG81NA@2x.jpg" as bg0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+96)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC01"),"True","img/CL_LAC01A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
    play sound "SE05_16L"
    pause (32/32.0)
    play sound "SE01_12L"
    pause (32/32.0)
#FADE_IN 1
    play music "BGM13"
    pause (32/32.0)
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/BG03NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG03NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
    hide bg1 with dissolve
    "回家的路上——我与学姐两个人，正缓步走回这个夏天我们生活一起的家里。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB06"),"True","img/CL_LAB06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    "路上，我们聊了很多很多。学姐刚来我家那天的事，打工的事，放焰火的事。心中有种莫名的紧迫感，催促着我不断提起各种话题。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/BG04NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG04NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA01"),"True","img/CL_LAA01A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
    hide bg1 with dissolve
    "要问我原因的话，学姐住回自己家，也就意味着我们在一起的生活即将终结……"
    "说不会寂寞那是谎话。可是，这对于学姐来说是件值得高兴的事情。"
    window hide
    stop se fadeout 1
#BG_SET_BACK 
#BG_INIC 1
#FADE_OUT 0
    scene expression Solid("000") with fade
    stop se
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG14NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG14NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+96)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC02"),"True","img/CL_MAC02A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
#SE_VOLC 1,(64/2)
#FADE_IN 1
    voice "NCL14A_KU022"
    克罗艾 "「对不起，来的时候也是，回去的时候也是，都那么突然……」"
    志雄 "「我并没有介意哦。」"
    志雄 "「不过，就是有点……」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB03"),"True","img/CL_MAB03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL14A_KU023"
    克罗艾 "「就是有点？」"
    "今后，我们在一起的时间就会变短了。要说出这样的话实在太难为情了，于是我改变了话题。"
    志雄 "「不，没什么啦。」"
    window hide
#SE_VOLC 1,128
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "话到嘴边我又咽了下去。因为害怕被学姐察觉，我急忙向前快走了两步。"
    stop se
    voice "NCL14A_KU024B"
    克罗艾 "「呐，志雄——」"
    "学姐的声音，突然从意想不到的近处传来。学姐从身后很快的跟上来了吗？在耳边听到学姐声音而感到吃惊的我不禁回头看去——"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,640
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XAB02"),"True","img/CL_XAB02A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
#SE_VOLC 1,(64/2)
#MOV_CHR_INIT 64
#MOV_CHR0 128,(320+192)
#BG_BLUR 0
#MOV_CHR_GO 1
    志雄 "「怎——」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XAB04"),"True","img/CL_XAB04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    志雄 "「诶？那个……」"
    "脸上一阵温暖的触感。"
    "又是突然袭击，我的脑袋里一片空白，一句话也说不出来。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XAA07"),"True","img/CL_XAA07A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL14A_KU025"
    克罗艾 "「嗯，稍微，有些这样的心情啦……」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+96)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA07"),"True","img/CL_MAA07A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
#BG_BLUR 0
    "学姐轻轻附在我的耳边说道，然后再次与我拉开距离。"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
#BG_UVC 0,0,512,640,448
#BG_BLUR 0
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB04"),"True","img/CL_LAB04A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
    pause (32/32.0)
#SE_VOLC 1,(64/2)
#FADE_IN 1
    voice "NCL14A_KU026"
    克罗艾 "「能够和爸爸还有妈妈那样开心地说话，都是志雄的功劳呢……」"
    "学姐稍微解释了两句。"
    志雄 "「我只是稍微在学姐身后推了一把而已哦。」"
    "归根结底，我并没有做什么了不起的事情。能够和父母解开心结完全是靠学姐自己的努力。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB02"),"True","img/CL_LAB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL14A_KU027"
    克罗艾 "「最重要的，是有那样一个在背后推我一把的人在，一定是这样呢。」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB04"),"True","img/CL_LAB04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL14A_KU028"
    克罗艾 "「所以，谢谢你。」"
    志雄 "「嗯……」"
    window hide
#BG_SET_BACK 
#FADE_OUT 1
#BG_INIC 1
    scene expression "img/NIMG01D@2x.png" as bg1 zorder 1
    show expression "img/CloudD1_0@2x.png" as cloud0 zorder 5:
        ycenter .55
        xcenter .75
        linear 500 xcenter .0
    show expression "img/CloudD1_1@2x.png" as cloud1 zorder 5:
        ycenter .55
        xcenter .65
        linear 500 xcenter .0
    show expression "img/CloudD1_2@2x.png" as cloud2 zorder 8:
        ycenter .3
        block:
            xcenter 1.0
            linear 140 xcenter .0
            repeat
    show expression "img/CloudD2_1@2x.png" as cloud3 zorder 8:
        ycenter .2
        block:
            xcenter 1.0
            linear 100 xcenter .0
            repeat
    show expression "img/CloudD2_0@2x.png" as cloud4 zorder 8:
        ycenter .0
        block:
            xcenter 1.0
            linear 120 xcenter .0
            repeat
    show expression "img/CloudD3@2x.png" as cloud5 zorder 10:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.5
            linear 50 xpos .0
            xpos 1.0
            linear 50 xpos .5
            repeat
    with dissolve
#EFF_STAC 0,CLOUD_D,EFF_SKIP
#SE_VOLC 1,255
#FADE_IN 1
    "就这样，我与学姐的第二次同居生活迎来了完结的时刻。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1,128
#EFF_STPC 0,EFF_SKIP
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop se
    stop sound
    stop music fadeout 1
#FADE_IN 0
#MOV_PLY 3
#RSET S101
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_ELISE_WHISPER
#CHR_POS_AUTOC 2,(320-96),F123
#CHR_POS_SAVEC 2
#EOT
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT