label NRI01A:
    $currentlabel = "NRI01A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '18'
    $date = '2'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#BG_SET_BACK 
#BG_INIC 3
#BG_PRI 3
    show expression "img/NIMG19A-568h@2x.jpg" as bg3 with dissolve
    pause
#FADE_OUT 1,32,COL_WHITE
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_ALPC 0
#BG_PRI 0
    show expression "img/BG03AA@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_PAL_BGC ALL,BG03AA
#BG_SET_BACK 
#BG_INIC 1
#BG_PRI 1
    show expression "img/NIMG01B@2x.png" as bg1 zorder 1
    show expression "img/CloudB1_0@2x.png" as cloud0 zorder 5:
        ycenter .55
        xcenter .75
        linear 500 xcenter .0
    show expression "img/CloudB1_1@2x.png" as cloud1 zorder 5:
        ycenter .55
        xcenter .65
        linear 500 xcenter .0
    show expression "img/CloudB2_0@2x.png" as cloud2 zorder 8:
        ycenter .3
        block:
            xcenter 1.0
            linear 140 xcenter .0
            repeat
    show expression "img/CloudB2_1@2x.png" as cloud3 zorder 8:
        ycenter .2
        block:
            xcenter 1.0
            linear 100 xcenter .0
            repeat
    show expression "img/CloudB2_2@2x.png" as cloud4 zorder 8:
        ycenter .0
        block:
            xcenter 1.0
            linear 120 xcenter .0
            repeat
    show expression "img/CloudB3@2x.png" as cloud5 zorder 10:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.5
            linear 50 xpos .0
            xpos 1.0
            linear 50 xpos .5
            repeat
    show expression "img/CloudB4@2x.png" as cloud6 zorder 12:
        xanchor 1.0
        yalign 1.0
        block:
            xpos .6
            linear 78 xpos .0
            xpos 1.0
            linear 52 xpos .6
            repeat
    show expression "img/CloudB5@2x.png" as cloud7 zorder 15:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.2
            linear 20 xpos .0
            xpos 1.0
            linear 100 xpos .2
            repeat
    with dissolve
#EFF_STAC 0,CLOUD_B,EFF_NOSKIP
    play sound "SE05_14L"
#EFF_PRI 0
#EFF_PRI 1
#EFF_STAC 1,LENSFLARE1_SKY,EFF_NOSKIP
#FADE_IN 1
    pause (100/32.0)
#BG_SHOWC 5
#EFF_STPC 0,EFF_SKIP
#EFF_STPC 1,EFF_SKIP
    hide bg1
    scene expression "img/BG03AA@2x.jpg" as bg0 zorder 0
    with dissolve
#BG_PRI 0
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAB05"),"True","img/RI_LAB05A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
#SE_VOLC 1,128
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
    if not persistent.dictlist[1] and persistent.show_dict:
        $persistent.dictlist[1]=True
        show screen dict_pop(i=1)
    voice "NRI01A_RI000"
    莉莉丝 "「好～热～啊～」"
    志雄 "「按照天气预报里的说法，今天还算比较凉快的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAC04"),"True","img/RI_LAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI001"
    莉莉丝 "「喂，志雄，你想想办法啊～」"
    志雄 "「我有什么办法。再说了，你出生时正值夏季，应该比较耐热才对啊。」"
    voice "NRI01A_RI002"
    莉莉丝 "「怎么可能～那是迷信，迷信啊。」"
    "我们终于成功地度过了第一学期的期末考试，当然，时间也已经在不知不觉中推移到了夏天。"
    "早晨的阳光像是为了表现自己一般，无情地炙烤着我们。"
    voice "NRI01A_RI003"
    莉莉丝 "「呼～」"
    "走在在我身旁的莉莉丝，微微拉开了制服的领子，挥动着手给自己纳凉。"
    志雄 "「真是的，太不检点了……富美子婆婆看见了可是会生气的哟。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAC05"),"True","img/RI_LAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI004"
    莉莉丝 "「诶？」"
    "听了我的话，莉莉丝突然有些失措。"
    "可马上，脸上又露出了坏坏的笑容。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAD06"),"True","img/RI_LAD06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI005"
    莉莉丝 "「哈哈，志雄是在担心我被别人偷看到吧～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAA01"),"True","img/RI_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI006"
    莉莉丝 "「呐、呐，这就是所谓的独占欲吧？」"
    志雄 "「不，不是的……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAA06"),"True","img/RI_LAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI007"
    莉莉丝 "「不是？真是的，你也稍微担心一下啊。这可是美少女的危机啊！？」"
    志雄 "「是你自己硬要给别人看，哪有什么危机可言……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAA05"),"True","img/RI_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI008"
    莉莉丝 "「不要把别人说得跟变态似的～！」"
    play sound "SE04_09"
    with vpunch
    play sound "SE04_30"
    志雄 "「噢！」"
#THREAD_STA 1,THREAD_SI_HIRARI
#MESA A_CH_SI,"【志雄】「噢！」"
#THREAD_WAT 1
#WIN_POS 0,0
#MESX "%K%P"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAA03"),"True","img/RI_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI009"
    莉莉丝 "「啊！　又避开了！？」"
    志雄 "「我也是在不断成长的。和某人的胸部可是完全不一样呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAD02"),"True","img/RI_LAD02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI010"
    莉莉丝 "「！？　等、等一下！　某人是指谁啊！？」"
    志雄 "「啊，好热好热～」"
    voice "NRI01A_RI011"
    莉莉丝 "「这天气本来就热得让人烦躁，看来你是真想惹我生气啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAB02"),"True","img/RI_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI012"
    莉莉丝 "「……再说了，明明你也没有好好看过啊。」"
    志雄 "「是吗？每天都看的话自然就清楚了啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAD06"),"True","img/RI_LAD06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI013"
    莉莉丝 "「诶～哦～是吗～」"
    voice "NRI01A_RI014"
    莉莉丝 "「志雄每天只顾着看我的胸部啊～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAB02"),"True","img/RI_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI015"
    莉莉丝 "「变态……」"
    志雄 "「不是啊！」"
    stop music fadeout 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XAC01"),"True","img/RI_XAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI016"
    莉莉丝 "「那么，你不想看吗？」"
#SE_VOLC 1,255
    "说着，莉莉丝故意用手指把衣襟稍稍挑开，小心翼翼地抬头看着我。"
    "雪白的肌肤和隐约可见的汗珠。锁骨勾勒出的曲线……还有——"
    "等、等一下，再这样下去……！"
    "……额，怎么能看得入迷。"
    stop sound
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XAB07"),"True","img/RI_XAB07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI017"
    莉莉丝 "「变态……」"
    志雄 "「不是的！」"
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
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM09"
    if not persistent.dictlist[7] and persistent.show_dict:
        $persistent.dictlist[7]=True
        show screen dict_pop(i=7)
    voice "NRI01A_TO000"
    亨 "「哟。早上好～！」"
    志雄 "「噢噢！？」"
#THREAD_STA 1,THREAD_QUA_WIN
#MESA A_CH_SI,"【志雄】「噢噢！？」"
#THREAD_WAT 1
#WIN_POS 0,0
#MESX "%K%P"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB04"),"True","img/TO_MAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_TO001"
    亨 "「怎、怎么了？　干吗这么吃惊！？」"
    志雄 "「亨、亨吗。啊，没、没什么……」"
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
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD06"),"True","img/RI_MAD06A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    play music  "BGM09"
    voice "NRI01A_RI018"
    莉莉丝 "「呐～呐～听我说，佐贺君。志雄一直对我的胸部……」"
    志雄 "「哇！　哇！　没什么！　什么都没有！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_TO002"
    亨 "「胸部！？　胸部是……是指莉莉丝那勾勒着诱惑的曲线，丰满而美丽的胸部吗！？」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_PRIC ID_ALL
#CHR_INIC 2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAA02"),"True","img/TO_XAA02A@2x.png") as lh2 zorder 100:
        ypos 0.0
    with dissolve
    stop music fadeout 1
    voice "NRI01A_TO003"
    亨 "「难道志雄……难道说……你对莉莉丝的……！？」"
    志雄 "「脸太近！　太近了啦！」"
    voice "NRI01A_TO004"
    亨 "「如果万一你有那么一丝非分之想的话……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAA03"),"True","img/TO_XAA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI01A_TO005"
    亨 "「我会哭的！」"
    voice "NRI01A_TO006"
    亨 "「我！」"
    voice "NRI01A_TO007"
    亨 "「一定会！」"
    志雄 "「是吗……那你就哭吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAB05"),"True","img/TO_XAB05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI01A_TO008"
    亨 "「噢噢噢噢噢噢噢噢！！　志雄你！　你和莉莉丝！　终于跨入了成人的阶段了吗！」"
    window hide
#CHR_SORT 2,0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_PRIC 0
#CHR_PRIC 1
#CHR_POSC 0,(320+192)
#CHR_POSC 1,(320-160)
#CHR_ALPC 0
#CHR_ALPC 1
    
    hide lh2 with dissolve
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAA06"),"True","img/TO_LAA06A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAE01"),"True","img/RI_LAE01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 1
    play sound "SE04_31"
#FADE_OUT 1,8,COL_WHITE
#CHR_ALPC 0
#CHR_ALPC 1
#BG_ALPC 1
#FADE_IN 0
#BG_ALP_AUTOC 1,0,0,F24
#QUA_CHR 0
    pause (50/32.0)
#BG_ALP_SAVEC 1
    hide bg1 with dissolve
    hide lh0 with dissolve
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAA05"),"True","img/RI_LAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI018A"
    莉莉丝・志雄 "「谁跨入了啊！」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_PRI 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SORT 0,1
#BG_UVC 0,0,0,640,448
    scene expression "img/BG04AA@2x.jpg" as bg0 with dissolve
    hide bg1 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_ALPC 0
#CHR_ALPC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,((320+160)+(640/4))
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA01"),"True","img/CH_MAA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAB01"),"True","img/RI_MAB01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
    with dissolve
    play music  "BGM10"
#CHR_ALP_AUTOC 0,128,0,F24
#CHR_ALP_AUTOC 1,128,0,F24
#CHR_POS_AUTOC 1,(320+160),F24,48
#CHR_ALP_SAVEC 0
#CHR_ALP_SAVEC 1
#CHR_POS_SAVEC 1
    if not persistent.dictlist[2] and persistent.show_dict:
        $persistent.dictlist[2]=True
        show screen dict_pop(i=2)
    voice "NRI01A_RI019"
    莉莉丝 "「啊，智纱！　早！」"
    voice "NRI01A_CH000"
    智纱 "「早上好，莉莉丝，塚本君。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC06"),"True","img/CH_MAC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_CH001"
    智纱 "「啊……佐贺君你怎么了？　这幅德行？」"
    voice "NRI01A_RI020"
    莉莉丝 "「这是为了让他成为一个坚强男人而进行的特训。」"
    voice "NRI01A_TO009"
    亨 "「……对不起对不起对不起对不起。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC04"),"True","img/RI_MAC04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI021"
    莉莉丝 "「真是的，你这样岂不是让我出更多汗吗。志雄，现在就把季节变成冬天～」"
    志雄 "「怎么可能！」"
    "再说，如果变成了冬天，那样你该喊冷了吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA01"),"True","img/CH_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_CH002"
    智纱 "「话说回来，天气真正开始热起来了呢。有种盛夏到来的感觉了。」"
    voice "NRI01A_RI022"
    莉莉丝 "「真希望现在暑假就到来。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAB01"),"True","img/CH_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_CH003"
    智纱 "「恩～不过这样的话我们就会见不到了哦……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA01"),"True","img/RI_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI023"
    莉莉丝 "「为什么？　即使不去学校，我们也可以一起出去玩啊。」"
    window hide
#CHR_SORT 1,0
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2,(320+640)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
    with dissolve
#CHR_ALP_AUTOC 2,128,0,F24,20
#CHR_POS_AUTOC 2,F24,40
    pause (64/32.0)
#CHR_POS_AUTOC 0,(320-192),F25,20
#CHR_POS_AUTOC 1,(320+192),F25,20
#CHR_POS_SAVEC 2
#CHR_POS_SAVEC 0
#CHR_POS_SAVEC 1
    voice "NRI01A_TO010"
    亨 "「对啊对啊！　……对了，大海，去海边吧！　泳衣，泳衣，泳衣在呼唤着我！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA03"),"True","img/CH_MAA03A@2x.png") as lh0 zorder (10+0):
        xcenter .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC06"),"True","img/RI_MAC06A@2x.png") as lh1 zorder (10+1):
        xcenter .8
    with dissolve
    志雄 "「亨的声音就这样被无视了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI01A_TO011"
    亨 "「太过分了！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC04"),"True","img/CH_MAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_CH004"
    智纱 "「嗯……说实话我也想一起去玩呢……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA04"),"True","img/RI_MAA04A@2x.png") as lh1 zorder (10+1)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh2 zorder (10+2)
    "说着，箱崎露出了有些困扰的微笑。"
    志雄 "「嘛，说的也是呢。莉莉丝和亨不要给箱崎添麻烦哟。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA04"),"True","img/CH_MAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_CH005"
    智纱 "「不，不会给我添麻烦的……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD01"),"True","img/RI_MAD01A@2x.png") as lh1 zorder (10+1)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh2 zorder (10+2)
    voice "NRI01A_RI024"
    莉莉丝 "「这不是挺好嘛。海边！　去海边吧！」"
    voice "NRI01A_TO012"
    亨 "「哦耶！」"
    志雄 "「那个……你们几个，有点高三学生的自觉好吗……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC05"),"True","img/RI_MAC05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI025"
    莉莉丝 "「哎？　啊……」"
    "这家伙该不会真的忘了吧……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA03"),"True","img/TO_MAA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI01A_TO013"
    亨 "「不过，现在临时抱佛脚也起不了多大作用了啊。老师和父母对我抱有过高的期望也是没用的，真希望他们早点察觉到这一点。」"
    "这家伙的问题也不少……"
    志雄 "「至少不要妨碍到箱崎学习吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA01"),"True","img/CH_MAA01A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
        xcenter .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA04"),"True","img/RI_MAA04A@2x.png") as lh1 zorder (10+2):
        ypos 0.0
        xcenter .8
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA05"),"True","img/TO_MAA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
#CHR_DSPTC 0,1,2,CH_MAA01,RI_MAA04,TO_MAB05
    voice "NRI01A_RI026"
    莉莉丝 "「你真啰嗦。我知道的啦。」"
    "事实上，班里大多数的人都在努力地准备着复习迎考。"
    "当然我也是其中之一。"
    "现在可以说是最后的冲刺阶段。"
    "虽说如此，但我到现在也还没有确定要考的学校和志愿……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA05"),"True","img/TO_MAA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI01A_TO014"
    亨 "「不，果然莉莉丝说的话是绝对正确的。现在正是玩的季节！夏天不玩也太不完整了吧！」"
    voice "NRI01A_TO015"
    亨 "「炽热的太阳使人们的内心得以解放，邂逅和分别会使人变得更加坚强！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI01A_TO016"
    亨 "「现在的我是寻找崭新恋爱的狩猎人……没错，让我来狩猎你的心吧！」"
#    window hide
#MOV_CHR_INIT 40
#MOV_CHR0 ,(320-96)
#MOV_CHR1 ,(320+96)
#MOV_CHR_GO 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC01"),"True","img/CH_MAC01A@2x.png") as lh0 zorder (10+0):
        xcenter .35
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAB01"),"True","img/RI_MAB01A@2x.png") as lh1 zorder (10+1):
        xcenter .65
#    hide lh2 with dissolve
#CHR_ALPC 2
#CHR_BLUR 2
    if not persistent.dictlist[63] and persistent.show_dict:
        $persistent.dictlist[63]=True
        show screen dict_pop(i=63)
    voice "NRI01A_RI027"
    莉莉丝 "「对了对了，昨天看『蘑菇宝宝』了吗？」"
    voice "NRI01A_CH006"
    智纱 "「当然看了！蘑菇宝宝的舞姿真是可爱极了～」"
    voice "NRI01A_RI028"
    莉莉丝 "「嗯！我已经学会了。」"
    voice "NRI01A_CH007"
    智纱 "「啊，我也是我也是～」"
    window hide
#CHR_ERSWC 0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI01A_TO017"
    亨 "「…………啊。」"
    志雄 "「那个，怎么说呢，你要坚强啊……夏日的阳光会使你变得更加坚强的，对吧？」"
    "这样下去亨也太可怜了，于是我只好接着他的话茬说了一句。"
    "不过，却似乎起到了反效果，亨朝我白了一眼。"
    window hide
#CHR_SORT 2,0
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2
#CHR_ALPC 2
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAA04"),"True","img/TO_XAA04A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 16
#MOV_CHR0 0
#MOV_CHR2 128
#MOV_FOCUS_BG 512
#MOV_CHR_GO 0
    hide lh1
    hide lh0 with dissolve
    voice "NRI01A_TO018"
    亨 "「哼，有女朋友的家伙真是毫无压力呢～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAB05"),"True","img/TO_XAB05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI01A_TO019"
    亨 "「反正你们也准备像对笨蛋情侣一样，情意绵绵地黏在一起吧。」"
    voice "NRI01A_TO020"
    亨 "「果然是胸部什么的，胸部什么的，胸部什么的……可恶！为什么莉莉丝会选择你啊！」"
    "亨在以前就公开表示了对莉莉丝的好感。"
    "即使在我和莉莉丝正式交往以后这点也没改变。"
    "只是，莉莉丝会和我交往他似乎早就预料到了，所以，他也常常捉弄我。"
    "所以，我们依然还保持着良好的关系。"
    window hide
#CHR_PRIC 2
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_ALPC 0
#CHR_POSC 0,(320+192)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SAA06"),"True","img/RI_SAA06A@2x.png") as lh0 zorder (10-0):
        ypos 0.2
        xcenter .8
    with dissolve
#MOV_CHR_INIT 2
#MOV_CHR0 128
#MOV_CHR1 128
#MOV_FOCUS_BG 0
#MOV_CHR_GO 0
    voice "NRI01A_RI029"
    莉莉丝 "「你们在说什么？」"
    志雄 "「亨不肯从梦幻的世界中醒过来……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAA02"),"True","img/TO_XAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI01A_TO021"
    亨 "「想着莉莉丝每天都和志雄过着不检点的生活……不可原谅，不可原谅，塚本志雄！」"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,RI_SXC03,3,F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SAC03"),"True","img/RI_SAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.2
    with dissolve
#REEK_CHR 0
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    voice "NRI01A_RI030"
    莉莉丝 "「不、不检点的生活是指什么呀！？」"
#THREAD_STP 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SAC03"),"True","img/RI_SAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.2
    with dissolve
    hide bg3 with dissolve
#BG_PRI 3
#CHR_SORT 2,0
#CHR_PRIC ID_ALL
    志雄 "「从梦幻的世界又跳转到妄想的世界了吗……」"
    "再说，亨只是自说自话地兴奋起来而已，我和莉莉丝之间根本没做过什么特别的事。"
    "能够没有顾虑，说说笑笑的和睦相处。维持着一如既往，波澜不惊的关系。"
    "感觉这种不求进取的关系，从那天起一直维持到现在……"
    "今天早上也是……"
    window hide
#BG_SET_BACK
#BG_INIC 2
#BG_ALPC 2
    
#BG_INIC 3
    stop music fadeout 1
#SE_VOLC 1,0
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI01A")]=True
    show expression "img/EVN_RI01A@2x.jpg" as bg2 zorder 2
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_ALPC 0
#BG_ALPC 2
    hide bg3 with dissolve
#BG_ALPC 3
##BG_UVC 0,0,512,640,448
    志雄 "「喂，起来啦」"
    voice "NRI01A_RI031"
    莉莉丝 "「嗯……志雄……？」"
    志雄 "「快点起来吃饭。富美子婆婆也在等着呢。」"
    voice "NRI01A_RI032"
    莉莉丝 "「嗯……知道了……ＺＺＺ……」"
    志雄 "「每天早上都是这样，真是不管过了多少年都不会进步的家伙……」"
    "总之，这确实是个麻烦。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_PRI 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI01B")]=True
    show expression "img/EVN_RI01B@2x.jpg" as bg1 zorder 1 with dissolve
    play sound "SE03_54"
#BG_UVC 2,(640/4),(448/2),(640/2),(448/2)
    pause (4/32.0)
#BG_ALP_AUTOC 2,0,0,F24
#BG_ALP_SAVEC 2
    hide bg2 with dissolve
    voice "NRI01A_RI033"
    莉莉丝 "「嗯……不行……」"
    "要是寒冬的季节，强行把被子扒掉，多半会起来吧……"
    "不过现在这个季节，有没有被子都没差吧。"
    志雄 "「你给我老老实实起来啦」"
    莉莉丝 "「ＺＺＺ……」"
#MESEX_A M_NOA,A_CH_RI,NRI01A_RI034,"【りりす】「ＺＺＺ……」%K%P"
    "这家伙，既然这样的话……"
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    menu:
        "挠痒痒":
            pass
        "摇动她":
            pass
        "在耳旁吹气":
            pass
    "正当我准备选择惯用的招式时。"
    voice "NRI01A_RI035"
    莉莉丝 "「……志雄……」"
    voice "NRI01A_RI036"
    莉莉丝 "「……最……喜欢……了……」"
    play music  "BGM13"
    志雄 "「！？」"
    "一瞬间，我的脑子里一片空白。"
    "眼前的莉莉丝也太没有防备了。"
    "从这娇小的嘴唇里吐出的细语……。"
    stop music fadeout 18
    voice "NRI01A_RI037"
    莉莉丝 "「……博斯特尔的布丁……下次再吃吧…………」"
    play music  "BGM02"
    "原来是布丁啊……"
    "稍微有些期待的，我还真是个笨蛋。"
    "我拿起枕头边蘑菇宝宝的玩偶，砸了一下莉莉丝的脸。"
    play sound "SE04_34"
    志雄 "「你给我起来～！」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI01C")]=True
    show expression "img/EVN_RI01C@2x.jpg" as bg1 with dissolve
    voice "NRI01A_RI038"
    莉莉丝 "「嗯……什么啊……志雄……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI01B")]=True
    show expression "img/EVN_RI01B@2x.jpg" as bg1 with dissolve
    voice "NRI01A_RI039"
    莉莉丝 "「晚安……ＺＺＺ……」"
    志雄 "「莉莉丝，你睡衣没穿好哟！」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI01D")]=True
    show expression "img/EVN_RI01D@2x.jpg" as bg1 with dissolve
    voice "NRI01A_RI040"
    莉莉丝 "「不会吧……！？」"
    志雄 "「啊啊，是骗你的。」"
    voice "NRI01A_RI041"
    莉莉丝 "「呃……！」"
    志雄 "「醒了的话就起来换衣服。还有，肚脐露出来是真的。」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI01E")]=True
    show expression "img/EVN_RI01E@2x.jpg" as bg1 with dissolve
    voice "NRI01A_RI042"
    莉莉丝 "「啊……！」"
    voice "NRI01A_RI043"
    莉莉丝 "「真是，志雄这个笨蛋……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAA02"),"True","img/RI_LAA02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    stop music fadeout 18
#ROUTINE_STA
#BG_UVC 0,0,512,640,448
#BG_INIC 2
#BG_PRI 0
#CHR_PRIC 0
#BG_PRI 1
#BG_PRI 2
#ROUTINE_STP
#CHR_ALPC 0
    hide bg1
#BG_ALPC 0
    hide bg2
    with dissolve
    play sound "SE05_14L"
    voice "NRI01A_RI044"
    莉莉丝 "「什，什么嘛……一直看着我的脸。」"
    志雄 "「不，没什么。」"
    "关于妄想，我也许没有资格嘲笑亨……"
    志雄 "「哈……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAA05"),"True","img/RI_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI045"
    莉莉丝 "「唔……」"
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    hide lh1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XAE01"),"True","img/RI_XAE01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
##BG_PRI 0
#CHR_PRIC 1
#CHR_PRIC 2
#MOV_CHR_INIT 8
#MOV_CHR0 0
#MOV_CHR1 128
#MOV_CHR_GO 0
    play sound "SE04_07"
    with vpunch
    with hpunch
    志雄 "「噢噢……」"
#THREAD_STA 1,THREAD_QUA_WIN
#VIB_DOKA 
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESA A_CH_SI,"【志雄】「噢噢……」"
#THREAD_WAT 1
#WIN_POS 0,0
#VIB_STP 5
#MESX "%K%P"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XAA05"),"True","img/RI_XAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI01A_RI046"
    莉莉丝 "「哼！」"
    window hide
    hide lh1 with dissolve
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    志雄 "「啊！等，等一下！莉莉丝！」"
    window hide
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG06AA@2x.jpg" as bg0 with dissolve
    scene expression "img/BG06AA@2x.jpg" as bg0 with dissolve
    "即使过了半年多，我们的关系还是一点没变。"
    "习惯的氛围，以及习惯的距离感。"
    "莉莉丝就在我身边。"
    "和亨，箱崎也还是老样子。"
    "要是能一直这样下去的话——"
    "当然，我也毫不怀疑这一点，我很知足了。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
#GRAPH_INI 
    pause (120/32.0)
    stop se
    stop sound
    stop music fadeout 1
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_SI_HIRARI
#WIN_POS 640,0
#WIN_POS (640*-1),0
#WIN_POS 0,0
#WIN_POS 0,0
#EOT
#label THREAD_QUA_WIN
#TH_QUAKE_WIN 4
#EOT
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT