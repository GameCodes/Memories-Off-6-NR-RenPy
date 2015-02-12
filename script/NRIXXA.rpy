label NRIXXA:
    $currentlabel = "NRIXXA"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '08'
    $day = '01'
    $date = '2'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 6,CAL_0801
    show expression "img/NIMG15C-568h@2x.jpg" as cal zorder 5
    show expression "img/08_01_TUESDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG63AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG63AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_14L"
    pause (32/32.0)
#FADE_IN 1
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "第二天也是忙于离开旅馆的准备工作，没时间寻找护身符……"
    window hide
    show expression "img/BG65AA@2x.jpg" as bg_over zorder 2 with dissolve
    "结果我们就这样离开了龙境。"
    window hide
    stop sound
#FADE_OUT 1
    scene expression Solid("000") with fade
#FADE_IN 0
    $month = '08'
    $day = '02'
    $date = '3'
    show expression "img/NIMG15E-568h@2x.jpg" as cal zorder 5
    show expression "img/08_02_WEDNESDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
#CAL_DSP_GRP 5,CAL_0802
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG17AA1@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG17AA1@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA01"),"True","img/TO_XBA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#CAL_ERS 
    play music  "BGM10"
    "第二天，我和亨一起在『富美』吃饭。"
    志雄 "「对了，你暑期补习怎么样了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA04"),"True","img/TO_XBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRIXXA_TO000"
    亨 "「哼，我觉得暑期补习对我的人生来说是不需要的。对于大力提倡节约资源的现在，我们不应该浪费无谓的能量。」"
    志雄 "「就是说，觉得太麻烦，所以逃走了，是吧……」"
    "要是被父母知道了该怎么办呢……之前还为摩托车借过钱呢。"
    window hide
#CHR_SORT 0
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,(320+192)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA01"),"True","img/RI_MCA01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .8
    with dissolve
#MOV_CHR_INIT 32
#MOV_CHR1 128
#MOV_FOCUS_BG 0
#MOV_CHR_GO 0
    voice "NRIXXA_RI000"
    莉莉丝 "「给。」"
    "莉莉丝把我和亨点的东西放到了桌子上。"
    window hide
    play sound "SE03_12"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA01"),"True","img/RI_MCA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    voice "NRIXXA_TO001"
    亨 "「谢谢，莉莉丝！」"
    "面对从椅子上站起来高声道谢的亨，莉莉丝露出了苦笑的表情。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA06"),"True","img/RI_MCA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRIXXA_RI001"
    莉莉丝 "「太小题大作了啦，佐贺君。」"
    voice "NRIXXA_TO002"
    亨 "「不是小题大作，我只是表达自己的真实感情而已」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC02"),"True","img/RI_MCC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRIXXA_RI002"
    莉莉丝 "「啊哈哈……」"
    "莉莉丝的笑脸看起来和往常没什么区别。"
    志雄 "「莉莉丝……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC04"),"True","img/RI_MCC04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRIXXA_RI003"
    莉莉丝 "「嗯……」"
    hide lh1 with dissolve
    "即使我叫她，她也只是瞥了我一眼，很尴尬地挪开视线走开了。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA05"),"True","img/TO_XBA05A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NRIXXA_TO003"
    亨 "「……你和莉莉丝怎么了吗？」"
    志雄 "「没有……」"
    "自从旅行回来之后，莉莉丝和我似乎有所疏远。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBB03"),"True","img/TO_XBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRIXXA_TO004"
    亨 "「旅行期间发生了什么事吗？」"
    "亨单手托着下巴，用『一切都被我看穿了』的口吻说道。"
    "旅行期间发生了什么事吗……"
    "也许莉莉丝现在还在意那件事吧……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA05"),"True","img/TO_XBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRIXXA_TO005"
    亨 "「我说你们啊，这次旅行怎么样了？　稍微有些进展了吗？」"
    志雄 "「进展？　你指什么啊？」"
    voice "NRIXXA_TO006"
    亨 "「当然是指你和莉莉丝的关系咯。该不会什么都没发生吧？」"
    志雄 "「嘘。什么都没有啦！」"
    window hide
#CHR_SORT 0
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,(320+192)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA04"),"True","img/RI_MCA04A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .8
    with dissolve
#MOV_CHR_INIT 32
#MOV_CHR1 128
#MOV_FOCUS_BG 0
#MOV_CHR_GO 0
    "和莉莉丝双目相交。"
#BG_GET_NOC 0,F24
#BG_SET_BACK 
#BG_INIC 2
#BG_PRI 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
#BG_ALP_AUTOC 2,128,0,F24
#CHR_ALP_AUTOC 1,0,0,F24
#BG_ALP_SAVEC 2
#CHR_ALP_SAVEC 1
    hide lh1 with dissolve
#BG_SWPC 0
    hide bg2 with dissolve
#BG_PRI 2
#BG_PRI 1
    "莉莉丝再一次尴尬地移开了视线。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBB02"),"True","img/TO_XBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRIXXA_TO007B"
    亨 "「真的吗？　没有被心中燃起的年轻的热情所驱使，做出一些出格的事吗？　类似你实在太饥渴了导致莉莉丝退避三舍之类的。」"
    志雄 "「不会不会。」"
    "什么嘛，出格的事。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBB05"),"True","img/TO_XBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRIXXA_TO008"
    亨 "「怎么会……你们旅行究竟去干吗了」"
    志雄 "「去干吗了……是呢。去湖里游泳，去神社许愿，买土产……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBB04"),"True","img/TO_XBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRIXXA_TO009"
    亨 "「只是这样吗？」"
    志雄 "「基本上就是这些了。」"
    "如果加上突发事件，那还有和喝醉了的老爸以及新母亲有关的一系列事情。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA04"),"True","img/TO_XBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRIXXA_TO010"
    亨 "「什么嘛，真无趣。其他的呢？」"
    志雄 "「没了，就这些了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBB03"),"True","img/TO_XBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRIXXA_TO011"
    亨 "「只有这些啊……」"
    "叹着气的亨眼神中表露出了明显的失望之情。为什么非得为这种事而失望啊……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA01"),"True","img/TO_XBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRIXXA_TO012"
    亨 "「啊，对了，再过不久就是莉莉丝生日了吧？」"
    "已经对旅行的事完全失去兴趣了吗，亨改变了话题。"
    志雄 "「啊啊，是啊。」"
    "仔细想想，旅行途中也没有打听出莉莉丝喜欢什么。"
    voice "NRIXXA_TO013"
    亨 "「要送什么礼物莉莉丝才会高兴呢……」"
    "这个问题我也想问。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBB01"),"True","img/TO_XBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRIXXA_TO014"
    亨 "「喂～莉莉丝～」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA01"),"True","img/RI_MCA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    voice "NRIXXA_RI004"
    莉莉丝 "「什么？」"
    voice "NRIXXA_TO015"
    亨 "「这次生日你想要什么生日礼物？」"
    "亨这家伙，堂堂正正地问出了口……丝毫不犹豫也不拐弯抹角。"
    "总觉得至今为止犹豫不决的自己像个笨蛋一样。"
    stop music fadeout 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC04"),"True","img/RI_MCC04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRIXXA_RI005"
    莉莉丝 "「礼物……」"
    "可是，听到礼物二字的莉莉丝的脸上蒙上了一层阴影。"
    voice "NRIXXA_RI006"
    莉莉丝 "「礼物就不用了啦……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「诶？」"
    voice "NRIXXA_RI007"
    莉莉丝 "「反正我也会丢的……」"
    hide lh1 with dissolve
    "莉莉丝背对着我们，朝店里面走去。"
    window hide
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 3
#BG_PRI 3
#BG_ALPC 3
    scene expression "img/NIMG01B@2x.png" as bg3 zorder 3
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
#EFF_STAC 0,CLOUD_B,EFF_SKIP
#BG_ALP_AUTOC 3,128,0,1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    hide bg0 with dissolve
    play sound "SE05_01"
    "可是，看着她的背影，我暗暗下定了决心。"
    "莉莉丝的生日送她一个新的戒指吧。"
    "之前既没有时间也没有钱，所以只能送她一个玩具戒指……可是这次是真货。"
    "是的。这样的话，莉莉丝一定会高兴的。"
    "失去了什么东西之后，再拿到新的就行了。"
    "因为对我来说真正重要的她，一直就在我身边……"
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
#MOV_PLY 6
    $ renpy.end_replay()
    return