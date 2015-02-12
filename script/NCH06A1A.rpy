label NCH06A1A:
    $currentlabel = "NCH06A1A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '28'
    $date = '5'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_BG NIMG15C,CAL_0728
    show expression "img/NIMG15C-568h@2x.jpg" as cal zorder 5
    show expression "img/07_28_FRIDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
#FADE_OUT 1,32,COL_WHITE
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG01AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG01AA@2x.jpg" as bg0 with dissolve
    play sound "SE08_17L"
    pause (32/32.0)
#FADE_IN 1
    play music "BGM10"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "终于，旅行的日子到了。"
    window hide
#SE_VOLC 1,128
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBA01"),"not F103==0","img/CH_MLA01A@2x.png","True","img/CH_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH000"
    智纱 "「早上好，志雄君」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA01"),"not F103==0","img/CH_LLA01A@2x.png","True","img/CH_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「早上好。已经来了啊」"
    "想着偶尔也要比智纱来得更早些，我明明比预定的见面时间还早到了10分钟。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB01"),"not F103==0","img/CH_LLB01A@2x.png","True","img/CH_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH001"
    智纱 "「嗯。让志雄君等我的话不太好」"
    "智纱到底是从多久之前就在这里等着了啊。"
    志雄 "「不需要那么操心的啊。学生会的工作也是，智纱总是比我先到学校」"
    "结果，进了暑假之后，智纱还是在帮忙处理学生会的工作。"
    "而且是比我还要更早地到学校，先把琐碎的工作处理好。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB02"),"not F103==0","img/CH_LLB02A@2x.png","True","img/CH_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH002"
    智纱 "「哪怕是能帮上志雄君一点的忙，我也是很高兴的」"
    志雄 "「……」"
    "不知道该怎么说好了。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK
#BG_INIC 0
#BG_PRI 0
    scene expression "img/BG37AA@2x.png" as bg0 zorder 0
    show expression "img/trainoutside_A@2x.png" as train_bg zorder -5
    show expression "img/trainoutside_tree1_A@2x.png" as train_tree1 zorder -2:
        ycenter .5
        block:
            xcenter .4
            linear 0.5 xcenter -.1
            repeat
    show expression "img/trainoutside_tree1_A@2x.png" as train_tree1 zorder -2:
        ycenter .5
        block:
            xcenter .6
            linear 0.5 xcenter 1.1
            repeat
    show expression "img/trainoutside_tree0_A@2x.png" as train_tree2 zorder -2:
        ycenter .5
        block:
            xcenter .4
            linear 0.7 xcenter -.1
            repeat
    show expression "img/trainoutside_house1_A@2x.png" as train_house1 zorder -3:
        ycenter .47
        block:
            xcenter .4
            linear 0.7 xcenter -.1
            repeat
    show expression "img/trainoutside_house1_A@2x.png" as train_house1 zorder -3:
        ycenter .47
        block:
            xcenter .7
            linear 0.7 xcenter 1.1
            repeat
    show expression "img/trainoutside_house2_A@2x.png" as train_house2 zorder -3:
        ycenter .5
        alpha 0
        pause .5
        alpha 1
        block:
            xcenter .4
            linear 0.7 xcenter -.1
            repeat
    with dissolve
    show expression "img/trainoutside_house1_A@2x.png" as train_house3 zorder -3:
        ycenter .47
        alpha 0
        pause .9
        alpha 1
        block:
            xcenter .4
            linear 0.7 xcenter -.1
            repeat
    with dissolve
#EFF_STAC 0,TRAINWINDOW2,EFF_NOSKIP
#BG_ZOOM_RATE 0,8
#BG_PRI 0
    stop se
    stop sound
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC03"),"not F103==0","img/CH_LLC03A@2x.png","True","img/CH_LBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE06_10L"
#FADE_IN 1
#EFF_STAC 1,QUAKE_TRAIN,EFF_NOSKIP
#EFF_STAC 2,QUAKE_CHR_TRAIN,EFF_NOSKIP
    if not persistent.dictlist[56] and persistent.show_dict:
        $persistent.dictlist[56]=True
        show screen dict_pop(i=56)
    voice "NCH06A_CH003"
    智纱 "「嗯～……」"
    志雄 "「怎么了？」"
    "旅行目的地的龙境，乘特快列车大约不到2个小时的路程。"
    "现在正在向特快列车出发的车站的途中，可是从刚才开始智纱就在愁眉不展地考虑着些什么。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC04"),"not F103==0","img/CH_LLC04A@2x.png","True","img/CH_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH004"
    智纱 "「果然还是应该给志雄君的父母，买盒点心什么的吧……」"
    志雄 "「点、点心？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC02"),"not F103==0","img/CH_LLC02A@2x.png","True","img/CH_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH005"
    智纱 "「嗯，总是受志雄君的照顾」"
    志雄 "「不用了吧，太夸张了」"
    voice "NCH06A_CH006"
    智纱 "「嗯～，是吗」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC05"),"not F103==0","img/CH_LLC05A@2x.png","True","img/CH_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH007"
    智纱 "「啊～。要是这样的话，就在昨天事先准备些什么了……」"
#MUS_VOL 64
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC02"),"not F103==0","img/CH_LLC02A@2x.png","True","img/CH_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH008"
    智纱 "「如果什么都不带上的话，会被认为是没有礼貌的孩子，还会让他们说什么，没法把志雄托付给这样的女人……」"
#MUS_VOL (64/2)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC03"),"not F103==0","img/CH_LLC03A@2x.png","True","img/CH_LBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH009"
    智纱 "「受到家长反对的我们的将来，会是前途多难的」"
#MUS_VOL 128
    志雄 "「没有没有没有。智纱，你想得太多了……」"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    play sound "SE08_17L"
    pause (32/32.0)
#FADE_IN 0
    "换乘电车到达了车站，准备乘的特快列车已经在月台等待发车了。特快列车的指定座位车票，好像老爸他们已经准备好了。"
    "车站的月台上没有老爸他们的身影，说不定已经先上车了。"
    "再早来一点儿的话也许会比较好？"
    window hide
    stop sound fadeout 1
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 2
    

#CHR_POSC 0
#CHR_POSC 1,(320-270)
#CHR_ALP_AUTOC 1,128,1,F24,1
#CHR_POS_SAVEC 1
#CHR_ALP_SAVEC 1
#BG_SET_BACK
#BG_INIC 1 
    
    show expression "img/NIMG01A@2x.png" as bg1 zorder 1
    show expression "img/CloudA1@2x.png" as cloud0 zorder 5:
        yalign 1.0
        xcenter .75
        linear 100 xcenter .0
    show expression "img/CloudA2_0@2x.png" as cloud2 zorder 8:
        yalign .0
        block:
            xcenter 1.0
            linear 140 xcenter .0
            repeat
    show expression "img/CloudA2_1@2x.png" as cloud3 zorder 8:
        ycenter .2
        block:
            xcenter 1.0
            linear 100 xcenter .0
            repeat
    show expression "img/CloudA2_2@2x.png" as cloud4 zorder 8:
        yalign .0
        block:
            xcenter 1.0
            linear 120 xcenter .0
            repeat
    show expression "img/CloudA3_3@2x.png" as cloud8 zorder 10:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.5
            linear 50 xpos .0
            xpos 1.0
            linear 50 xpos .5
            repeat
    show expression "img/CloudA3_0@2x.png" as cloud5 zorder 10:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.8
            linear 80 xpos .0
            xpos 1.0
            linear 20 xpos .8
            repeat
    show expression "img/CloudA3_1@2x.png" as cloud6 zorder 12:
        xanchor 1.0
        yalign 1.0
        block:
            xpos .6
            linear 78 xpos .0
            xpos 1.0
            linear 52 xpos .6
            repeat
    show expression "img/CloudA3_2@2x.png" as cloud7 zorder 15:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.2
            linear 20 xpos .0
            xpos 1.0
            linear 100 xpos .2
            repeat
    with dissolve
#EFF_STAC 0,CLOUD_A,EFF_NOSKIP
#FADE_IN 1
    志雄 "「老爸说过的座位，大概是在……」"
    "座位的号码是今天早晨老爸用邮件告诉我的。我在车厢里一边走着，一边寻找那个座位。"
    voice "NCH06A_CH010"
    智纱 "「首先，礼仪不端正可不行……第一印象很重要……」"
    "智纱好像是在苦想见到老爸他们以后，应该怎么做。"
    "这么说来，智纱和老爸他们实际见面，今天是第一次。紧张也是没有办法的。"
    志雄 "「……啊，是那边的座位」"
    window hide
    stop music fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    hide bg1
    scene expression "img/EXBG03A2@2x.png" as bg0 zorder 0
    stop sound
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA02"),"True","img/SF_ZAA02A@2x.png") as lh0 zorder (10+0):
        xcenter .75
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA02"),"True","img/KR_ZAA02A@2x.png") as lh1 zorder (10+1):
        xcenter .25
        ypos 0.0
    with dissolve
#EFF_STAC 0,TRAINTEXT,EFF_NOSKIP
#FADE_IN 1
    voice "NCH06A_YG000"
    雄吾 "「终于来了啊，你们两个」"
#ROUTINE_STA
#BG_POS_AUTOC 0,(160),0,640,448,1,F24
#CHR_POS_AUTOC 0,(320+160),0,1,F24
#CHR_POS_AUTOC 1,(320-120),0,1,F24
#ROUTINE_STP
    "终于找到了指定的座位。不出所料，老爸和香里阿姨已经坐在那里了。我们坐到了两人的对面。"
    window hide
    play music "BGM03"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA01"),"True","img/SF_ZAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_YG001"
    雄吾 "「肯定是没找对站台来晚了吧……」"
    window hide
#    hide bg4 with dissolve
#BG_SET_BACK 
#BG_INIC 1
    if F103!=0:
        jump NCH06A1_IF_ELSE1
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH04B2")]=True
    show expression "img/EVN_CH04B2@2x.jpg" as bg1 with dissolve
#BG_FLG EVN_CH04B2
    jump NCH06A1_IF_END1
label NCH06A1_IF_ELSE1:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH04G2")]=True
    show expression "img/EVN_CH04G2@2x.jpg" as bg1 with dissolve
#BG_FLG EVN_CH04G2
label NCH06A1_IF_END1:
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NCH06A_CH011"
    智纱 "「初、初次见面！」"
    "老爸的话还没说完，智纱就深深地低下了头。"
    voice "NCH06A_CH012"
    智纱 "「我、我是、和志雄君正在交往的，箱、箱崎智纱！」"
    voice "NCH06A_CH013"
    智纱 "「今天能邀请我这样的人来旅行，我真的是感到非常的高兴！」"
    voice "NCH06A_CH014"
    智纱 "「从今往后，不管到什么时候，都请您们多多关照了！」"
#MESEX_A M_NOA,A_CH_SF+A_CH_KR+A_CH_SI,NCH06A_MIX00,"【志雄・雄吾・香里】「……」%K%P"
    "智纱的头一直低着。老爸和香里阿姨，都愣住了。"
    志雄 "「那，那个，智纱。有点太夸张了……」"
    window hide
    if F103!=0:
        jump NCH06A1_IF_ELSE2
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH04C2")]=True
    show expression "img/EVN_CH04C2@2x.jpg" as bg1 with dissolve
#BG_FLG EVN_CH04C2
    jump NCH06A1_IF_END2
label NCH06A1_IF_ELSE2:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH04H2")]=True
    show expression "img/EVN_CH04H2@2x.jpg" as bg1 with dissolve
#BG_FLG EVN_CH04H2
label NCH06A1_IF_END2:
    voice "NCH06A_CH015"
    智纱 "「哎？」"
    if F103!=0:
        jump L_NCH06A_BRA00_A
#IF F103!0, GOTO L_NCH06A_BRA00_A
    jump L_NCH06A_BRA00_B
label L_NCH06A_BRA00_A:
    "智纱抬起脸，扶了一下歪掉的眼镜。"
    jump L_NCH06A_BRA00_X
label L_NCH06A_BRA00_B:
    "智纱抬起头，发着呆。"
    jump L_NCH06A_BRA00_X
label L_NCH06A_BRA00_X:
    window hide
#CHR_POSC 0
#CHR_POSC 1,(320-270)
#BG_POSC 0,0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA06"),"True","img/SF_ZAA06A@2x.png") as lh0 zorder (10+0):
        xcenter .5
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA02"),"True","img/KR_ZAA02A@2x.png") as lh1 zorder (10+1):
        xcenter 90/640.0
        ypos 0.0

    hide bg1 with dissolve
#EFF_STAC 0,TRAINTEXT,EFF_NOSKIP
    voice "NCH06A_YG003"
    雄吾 "「……啊，啊。我是我家这犬子的父亲，塚本雄吾。请多关照，箱崎小姐」"
    "老爸一脸的疑惑，对着智纱点头问好。"
    "从周围的座位传来了呵呵的笑声。向那边看了一圈，有几个乘客以一种微笑的视线在看着这边。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    if F103!=0:
        jump NCH06A1_IF_ELSE3
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH04A2")]=True
    show expression "img/EVN_CH04A2@2x.jpg" as bg1 zorder 100 with dissolve
#BG_FLG EVN_CH04A2
    jump NCH06A1_IF_END3
label NCH06A1_IF_ELSE3:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH04F2")]=True
    show expression "img/EVN_CH04F2@2x.jpg" as bg1 zorder 100 with dissolve
#BG_FLG EVN_CH04F2
label NCH06A1_IF_END3:
    voice "NCH06A_CH016"
    智纱 "「啊，那、那个……」"
    "智纱的脸一下子红了。"
    志雄 "「差、差不多车该开了」"
    window hide
    play sound "SE06_30"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    pause (32/32.0)
    hide bg1 with dissolve
    voice "NCH06A_XB000_K"
    車内放送の声 "「车门，要关上～了，请大家注意～」"
#EFF_STAC 0,QUAKE_H_00,EFF_NOSKIP
    "然后，随着振动，列车缓缓地驶出了站台。"
    window hide
    stop se fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    pause (32/32.0)
    stop se
#CHR_POSC 1,(320-250)

#BG_INIC 0
##BG_PRI 0
    scene expression "img/EXBG03AB@2x.png" as bg0 zorder 0
    show expression "img/trainoutside0@2x.png" as train_bg zorder -5:
        align (0,0)
    show expression "img/trainoutside_tree0@2x.png" as train_tree1 zorder -2:
        ycenter .2
        block:
            xcenter .4
            linear 0.3 xcenter -.1
            repeat
    play sound "SE06_17L"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA06"),"True","img/SF_ZAA06A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA01"),"True","img/KR_ZAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
    with dissolve
    pause (32/32.0)
#FADE_IN 1
    voice "NCH06A_YG004"
    雄吾 "「就是这个孩子啊……这样啊」"
    "老爸一边看着智纱，一边自言自语般地，小声嘟哝着。"
    "两个人直接见面今天是第一次。老爸果然是在想着什么的吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA01"),"True","img/SF_ZAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_YG005"
    雄吾 "「箱崎」"
    window hide
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#GRAPH_ERS
#BG_SET_BACK
#BG_INIC 0
    if F103!=0:
        jump NCH06A1_IF_ELSE4
    scene expression "img/EVN_BLANK_CH04B@2x.png" as bg0
#BG_FLG EVN_CH04B
    jump NCH06A1_IF_END4
label NCH06A1_IF_ELSE4:
    scene expression "img/EVN_BLANK_CH04G@2x.png" as bg0
#BG_FLG EVN_CH04G
label NCH06A1_IF_END4:
#BG_PRI 0
    show expression "img/trainoutside1@2x.png" as train_bg zorder -5
    show expression "img/trainoutside_mountain@2x.png" as train_mountain zorder -4:
        ycenter .7
        block:
            xanchor 1.0
            xpos 1.3
            linear 1000 xpos 1.0
            repeat
    show expression "img/trainoutside_cloud0@2x.png" as train_cloud1 zorder -3:
        ycenter .13
        block:
            xanchor 1.0
            xpos 1.0
            linear 1000 xpos 0.2
            repeat
    show expression "img/trainoutside_cloud1@2x.png" as train_cloud2 zorder -3:
        ycenter .17
        block:
            xanchor 1.0
            xpos .8
            linear 1000 xpos 0.3
            repeat
    show expression "img/trainoutside_cloud2@2x.png" as train_cloud3 zorder -3:
        ycenter .19
        block:
            xanchor 1.0
            xpos .75
            linear 1000 xpos 0.25
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree1 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 0.3
            linear 0.5 xpos -0.3
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree2 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 0.9
            linear 0.5 xpos 0.3
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree2 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 1.0
            linear 0.5 xpos 0.4
            repeat
    with dissolve
#FADE_IN 1
    voice "NCH06A_CH017"
    智纱 "「是，是！？」"
    "好像是后背碰上了冰柱一样、智纱一哆嗦，挺直了脊梁。"
    voice "NCH06A_YG006"
    雄吾 "「不用那么紧张的，没关系的」"
    window hide
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#GRAPH_ERS
#BG_SET_BACK
#BG_INIC 0
#BG_PRI 0
    scene expression "img/EXBG03AB@2x.png" as bg0 zorder 0
    show expression "img/trainoutside0@2x.png" as train_bg zorder -5:
        align (0,0)
    show expression "img/trainoutside_tree0@2x.png" as train_tree1 zorder -2:
        ycenter .2
        block:
            xcenter .4
            linear 0.3 xcenter -.1
            repeat
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA01"),"True","img/SF_ZAA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA02"),"True","img/KR_ZAA02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
    with dissolve
#BG_POSC 0,160
#CHR_POSC 0,(320+160)
#CHR_POSC 1,(320-120)
#CHR_PRIC 0
#CHR_PRIC 1
#FADE_IN 1
    voice "NCH06A_KR001"
    香里 "「对对，他又不是什么值得紧张的大人物」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA03"),"True","img/SF_ZAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_YG007"
    雄吾 "「喂喂，不是什么大人物，这么说太过分了吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA01"),"True","img/KR_ZAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH06A_KR002"
    香里 "「哎呀，这么说是有什么了不得的事情咯？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA02"),"True","img/SF_ZAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_YG008"
    雄吾 "「你这么说我可受不了啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA02"),"True","img/KR_ZAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    "老爸和香里阿姨互相开玩笑地说着话。他们俩真的是感情很好啊。"
    "如果是以前的我的话，见到他俩这样子说不定还会感到焦躁。"
    "但是现在，我也觉得自己能坦率对待老爸和香里阿姨的事情。这样真好。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA01"),"True","img/KR_ZAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH06A_KR003"
    香里 "「嗯，箱崎也是这么想的吧？」"
    window hide
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#GRAPH_ERS
#BG_SET_BACK
#BG_INIC 0
    if F103!=0:
        jump NCH06A1_IF_ELSE5
    scene expression "img/EVN_BLANK_CH04B@2x.png" as bg0
#BG_FLG EVN_CH04B
    jump NCH06A1_IF_END5
label NCH06A1_IF_ELSE5:
    scene expression "img/EVN_BLANK_CH04G@2x.png" as bg0
#BG_FLG EVN_CH04G
label NCH06A1_IF_END5:
#BG_PRI 0
    show expression "img/trainoutside1@2x.png" as train_bg zorder -5
    show expression "img/trainoutside_mountain@2x.png" as train_mountain zorder -4:
        ycenter .7
        block:
            xanchor 1.0
            xpos 1.3
            linear 1000 xpos 1.0
            repeat
    show expression "img/trainoutside_cloud0@2x.png" as train_cloud1 zorder -3:
        ycenter .13
        block:
            xanchor 1.0
            xpos 1.0
            linear 1000 xpos 0.2
            repeat
    show expression "img/trainoutside_cloud1@2x.png" as train_cloud2 zorder -3:
        ycenter .17
        block:
            xanchor 1.0
            xpos .8
            linear 1000 xpos 0.3
            repeat
    show expression "img/trainoutside_cloud2@2x.png" as train_cloud3 zorder -3:
        ycenter .19
        block:
            xanchor 1.0
            xpos .75
            linear 1000 xpos 0.25
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree1 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 0.3
            linear 0.5 xpos -0.3
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree2 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 0.9
            linear 0.5 xpos 0.3
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree2 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 1.0
            linear 0.5 xpos 0.4
            repeat
    with dissolve
#FADE_IN 1
    voice "NCH06A_CH018"
    智纱 "「哎！？　是，是这样呢」"
    voice "NCH06A_YG009"
    雄吾 "「……哈哈」"
    "老爸的脸上泛起了苦笑。嗯，刚才被肯定了，就只能笑了吧。"
    window hide
    if F103!=0:
        jump NCH06A1_IF_ELSE6
#    show expression "img/EVN_BLANK_CH04B@2x.png" as bg0 with dissolve
#BG_FLG EVN_CH04C
    jump NCH06A1_IF_END6
label NCH06A1_IF_ELSE6:
#    show expression "img/EVN_BLANK_CH04G@2x.png" as bg0 with dissolve
#BG_FLG EVN_CH04H
label NCH06A1_IF_END6:
    $persistent.albumlist[38]=True
#EFF_STAC 1,CH04_FLASH,EFF_NOSKIP
    voice "NCH06A_CH019"
    智纱 "「哎？　哎？」"
    "好像是不明白老爸为什么在笑，智纱的头上飘出了问号。"
    window hide
#EFF_STPC 1,EFF_SKIP
    if F103!=0:
        jump NCH06A1_IF_ELSE7
    #TODO
    show expression "img/EVN_BLANK_CH04A@2x.png" as bg0 with dissolve
#BG_FLG EVN_CH04A
    jump NCH06A1_IF_END7
label NCH06A1_IF_ELSE7:
    show expression "img/EVN_BLANK_CH04F@2x.png" as bg0 with dissolve
#BG_FLG EVN_CH04F
label NCH06A1_IF_END7:
    voice "NCH06A_CH020"
    智纱 "「呜呜……」"
    "智纱的脸啪地一下全红了。"
    window hide
#MUS_VOL 0
#FADE_OUT 1
#ROUTINE_STA
#EFF_STPC 0,EFF_SKIP
#GRAPH_ERS
#BG_INIC 0
#BG_PRI 0
    show expression "img/EXBG03AB@2x.png" as bg0 zorder 0
    show expression "img/trainoutside0@2x.png" as train_bg zorder -5:
        align (0,0)
    show expression "img/trainoutside_tree0@2x.png" as train_tree1 zorder -2:
        ycenter .2
        block:
            xcenter .4
            linear 0.3 xcenter -.1
            repeat
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA01"),"True","img/SF_ZAA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA01"),"True","img/KR_ZAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
    with dissolve
#BG_POSC 0,160
#CHR_POSC 0,(320+160)
#CHR_POSC 1,(320-120)
#CHR_PRIC 0
#CHR_PRIC 1
#ROUTINE_STP
#FADE_IN 1
    voice "NCH06A_CH021"
    智纱 "「……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA06"),"True","img/SF_ZAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#MESEX_A M_NOA,A_CH_YG,NCH06A_YG010,"【雄吾】「……」%K%P"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA06"),"True","img/KR_ZAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#MESEX_A M_NOA,A_CH_KR,NCH06A_KR004,"【香里】「……」%K%P"
    "之后，对话就一度中断了，老爸和香里阿姨也是，总觉得好像是找不到说话的机会吧，一句话也没说。"
    window hide
    "车窗外面的风景，以飞快的速度向后移动着。"
    "这样下去可不妙啊。有没有什么说话的机会……。"
    window hide
#MUS_VOL 128
    hide bg1 with dissolve
    志雄 "「对了，智纱。我们现在要去的龙境，在最新一期的杂志上登载了迷你特辑的」"
    window hide
#MUS_VOL 0
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#GRAPH_ERS
#BG_SET_BACK
#BG_INIC 0
    if F103!=0:
        jump NCH06A1A_IF_ELSE8
    scene expression "img/EVN_BLANK_CH04D@2x.png" as bg0
#BG_FLG EVN_CH04D
    jump NCH06A1A_IF_END8
label NCH06A1A_IF_ELSE8:
    scene expression "img/EVN_BLANK_CH04I@2x.png" as bg0
#BG_FLG EVN_CH04I
label NCH06A1A_IF_END8:
    $persistent.albumlist[39]=True
#BG_PRI 0
    show expression "img/trainoutside1@2x.png" as train_bg zorder -5
    show expression "img/trainoutside_mountain@2x.png" as train_mountain zorder -4:
        ycenter .7
        block:
            xanchor 1.0
            xpos 1.3
            linear 1000 xpos 1.0
            repeat
    show expression "img/trainoutside_cloud0@2x.png" as train_cloud1 zorder -3:
        ycenter .13
        block:
            xanchor 1.0
            xpos 1.0
            linear 1000 xpos 0.2
            repeat
    show expression "img/trainoutside_cloud1@2x.png" as train_cloud2 zorder -3:
        ycenter .17
        block:
            xanchor 1.0
            xpos .8
            linear 1000 xpos 0.3
            repeat
    show expression "img/trainoutside_cloud2@2x.png" as train_cloud3 zorder -3:
        ycenter .19
        block:
            xanchor 1.0
            xpos .75
            linear 1000 xpos 0.25
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree1 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 0.3
            linear 0.5 xpos -0.3
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree2 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 0.9
            linear 0.5 xpos 0.3
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree2 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 1.0
            linear 0.5 xpos 0.4
            repeat
    with dissolve
#FADE_IN 1
    "智纱没有反应。"
    志雄 "「智纱」"
    "……。"
    志雄 "「智～纱」"
    window hide
#MUS_VOL 128
    if F103!=0:
        jump NCH06A1A_IF_ELSE9
    show expression "img/EVN_BLANK_CH04E@2x.png" as bg0 with dissolve
#BG_FLG EVN_CH04E
    jump NCH06A1A_IF_END9
label NCH06A1A_IF_ELSE9:
    show expression "img/EVN_BLANK_CH04J@2x.png" as bg0 with dissolve
#BG_FLG EVN_CH04J
label NCH06A1A_IF_END9:
    $persistent.albumlist[40]=True
#QUA_BG2 0,0 
    voice "NCH06A_CH022"
    智纱 "「啊，哎，什么！？」"
    "好像是一点都没注意到我喊她的声音，智纱吓得哆嗦了一下。"
    voice "NCH06A_CH023"
    智纱 "「怎，怎么了，志雄君？」"
    志雄 "「……啊，没什么，也不是什么大不了的事情，我们等下要去的地方，登在观光杂志上面了」"
    voice "NCH06A_CH024"
    智纱 "「啊，这、这样啊。太、太好了呢！」"
    "不用对我也这样地生硬吧……。"
    window hide
    if F103!=0:
        jump NCH06A1A_IF_ELSE10
    show expression "img/EVN_BLANK_CH04B@2x.png" as bg0 with dissolve
#BG_FLG EVN_CH04B
    jump NCH06A1A_IF_END10
label NCH06A1A_IF_ELSE10:
    show expression "img/EVN_BLANK_CH04G@2x.png" as bg0 with dissolve
#BG_FLG EVN_CH04G
label NCH06A1A_IF_END10:
    voice "NCH06A_CH025"
    智纱 "「那、那个，能带我去那么好的地方，真的是非常感谢！」"
    "智纱又对着老爸深深地低下了头。"
    window hide
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#GRAPH_ERS
#BG_INIC 0
#BG_PRI 0
    scene expression "img/EXBG03AB@2x.png" as bg0 zorder 0
    show expression "img/trainoutside0@2x.png" as train_bg zorder -5:
        align (0,0)
    show expression "img/trainoutside_tree0@2x.png" as train_tree1 zorder -2:
        ycenter .2
        block:
            xcenter .4
            linear 0.3 xcenter -.1
            repeat
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA03"),"True","img/SF_ZAA03A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA05"),"True","img/KR_ZAA05A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
    with dissolve
#CHR_POSC 0
#CHR_POSC 1,(320-270)
#CHR_PRIC 0
#CHR_PRIC 1
#FADE_IN 1
    voice "NCH06A_YG011"
    雄吾 "「那～个」"
    "老爸好像在犹豫着到底应该怎样回答才好。"
    "嘛，对老爸来说，突然对着他低下了头他也会不知道该怎么应对吧。"
#ROUTINE_STA
#BG_POS_AUTOC 0,(160),0,640,448,1,F24
#CHR_POS_AUTOC 0,(320+160),0,1,F24
#CHR_POS_AUTOC 1,(320-120),0,1,F24
#ROUTINE_STP
    voice "NCH06A_KR005"
    香里 "「……真是没办法呢」"
    "看着那样的老爸和智纱，香里阿姨一副像是发愣，又像是苦笑的表情。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA01"),"True","img/KR_ZAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH06A_KR006"
    香里 "「雄吾」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA01"),"True","img/SF_ZAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_YG012"
    雄吾 "「嗯？　怎么了？」"
#CHR_POS_AUTOC 1,(320-70),0,1,F24
    voice "NCH06A_KR007"
    香里 "「去买点果汁怎样？　一起去」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA03"),"True","img/SF_ZAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_YG013"
    雄吾 "「唉，不了，我并不口渴……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA05"),"True","img/KR_ZAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH06A_KR008"
    香里 "「好啦好啦。走吧」"
#CHR_POS_AUTOC 1,-60,1,F123
#MESA A_CH_KR,NCH06A_KR008,"【香里】「好啦好啦。走吧」"
#THREAD_WAT 1
#MESX "%K%P"
    "香里阿姨抓着老爸的手，硬是把他拖了起来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA01"),"True","img/KR_ZAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH06A_KR009B"
    香里 "「一会儿见，志雄君。后面拜托了哦」"
#CHR_POS_AUTOC 0,(320+160),-60,1,F24
    voice "NCH06A_YG014"
    雄吾 "「喂、喂」"
    window hide
#CHR_POS_AUTOC 1,(320+240),-60,1,F123,48
    pause (8/32.0)
#ROUTINE_STA
#CHR_ALP_AUTOC 0,0,1,F123,48
#CHR_ALP_AUTOC 1,0,1,F123,48
#CHR_POS_AUTOC 0,((320+160)+(640/4)),-60,1,F123,48
#CHR_POS_AUTOC 1,((320+240)+(640/4)),-60,1,F123,48
#ROUTINE_STP
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_ALPC 0
#CHR_ALPC 1
    "老爸一脸茫然地，被香里阿姨拉走了。"
    "站起来的时候，香里阿姨给了我一个轻松的眼神。还有那句『拜托了哦』的话……。"
    "对智纱想点什么办法的意思是吗。"
    voice "NCH06A_CH026"
    智纱 "「哈～……」"
    "老爸他们已经去了别的车厢，智纱像是把积存的气吐出来一样长叹了一口气。"
    window hide
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#GRAPH_ERS
#BG_SET_BACK
#BG_INIC 0
    if F103!=0:
        jump NCH06A1A_IF_ELSE11
    show expression "img/EVN_BLANK_CH04E@2x.png" as bg0
#BG_FLG EVN_CH04E
    jump NCH06A1A_IF_END11
label NCH06A1A_IF_ELSE11:
    show expression "img/EVN_BLANK_CH04J@2x.png" as bg1
#BG_FLG EVN_CH04J
label NCH06A1A_IF_END11:
#BG_PRI 0
    show expression "img/trainoutside1@2x.png" as train_bg zorder -5
    show expression "img/trainoutside_mountain@2x.png" as train_mountain zorder -4:
        ycenter .7
        block:
            xanchor 1.0
            xpos 1.3
            linear 1000 xpos 1.0
            repeat
    show expression "img/trainoutside_cloud0@2x.png" as train_cloud1 zorder -3:
        ycenter .13
        block:
            xanchor 1.0
            xpos 1.0
            linear 1000 xpos 0.2
            repeat
    show expression "img/trainoutside_cloud1@2x.png" as train_cloud2 zorder -3:
        ycenter .17
        block:
            xanchor 1.0
            xpos .8
            linear 1000 xpos 0.3
            repeat
    show expression "img/trainoutside_cloud2@2x.png" as train_cloud3 zorder -3:
        ycenter .19
        block:
            xanchor 1.0
            xpos .75
            linear 1000 xpos 0.25
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree1 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 0.3
            linear 0.5 xpos -0.3
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree2 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 0.9
            linear 0.5 xpos 0.3
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree2 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 1.0
            linear 0.5 xpos 0.4
            repeat
    with dissolve
#FADE_IN 1
    "然后，用一种依靠的眼神看向我。"
    voice "NCH06A_CH027"
    智纱 "「志雄君，我，没关系的吧？」"
    志雄 "「没关系指的是，什么？」"
    voice "NCH06A_CH028"
    智纱 "「那个，就是对，志雄君的父亲大人和母亲大人失礼了之类的」"
    "智纱像是认真地在担心一样，向我询问着。"
    志雄 "「不用这么毕恭毕敬也没关系的嘛？　在你眼前的也不是鬼怪啊、恶魔啊什么的」"
    voice "NCH06A_CH029"
    智纱 "「可，可是，考虑到今后的事情，就不能不事先和志雄君的家人搞好关系的！」"
    voice "NCH06A_CH030"
    智纱 "「都说结婚后最大的问题是是能否与对方家庭好好相处。婆媳之间展开的对立也经常成为话题」"
    "结、结婚！？　在午间剧场倒是看过……。"
    voice "NCH06A_CH031"
    智纱 "「志雄君，我，到底该怎么办才好呢！？」"
    志雄 "「不，不用做出那样一副要哭出来的表情……」"
    志雄 "「我觉得和平常一样就行了啊」"
    "我想也就是聊聊旅行目的地，再做做自我介绍，说说学校的事情不就好了嘛。"
    voice "NCH06A_CH032"
    智纱 "「普通地……普通地……」"
    window hide
    if F103!=0:
        jump NCH06A1A_IF_ELSE12
    show expression "img/EVN_BLANK_CH04A@2x.png" as bg0 with dissolve
#BG_FLG EVN_CH04A
    jump NCH06A1A_IF_END12
label NCH06A1A_IF_ELSE12:
    show expression "img/EVN_BLANK_CH04F@2x.png" as bg0 with dissolve
#BG_FLG EVN_CH04F2
label NCH06A1A_IF_END12:
    voice "NCH06A_CH033"
    智纱 "「唉……该怎么办呢……」"
    "智纱抱着头，眼里噙着泪水。"
    "还没到达目的地就已经是这个样子了，再往后会变成什么样呢？　现在开始的几天里，要四个人在一起的。"
    志雄 "「没关系的，不管发生什么，我……」"
    window hide
    stop music fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#GRAPH_ERS
#BG_INIC 0
#BG_PRI 0
    show expression "img/EXBG03AB@2x.png" as bg0 zorder 0 with dissolve
    show expression "img/trainoutside0@2x.png" as train_bg zorder -5:
        align (0,0)
    show expression "img/trainoutside_tree0@2x.png" as train_tree1 zorder -2:
        ycenter .2
        block:
            xcenter .4
            linear 0.3 xcenter -.1
            repeat
#FADE_IN 1
    "后面的话，我猛地咽了下去。"
    "因为周围有着相当多的乘客，总觉得这样很不好意思。"
    menu:
        "说":
            $F7=0
        "不说":
            $F7=1
    if F7==0:
        jump L_NCH06A_SEL00_A
    if F7==1:
        jump L_NCH06A_SEL00_B
label L_NCH06A_SEL00_A:
    $F1+=1
    "但是，如果能稍稍鼓励下失落的智纱的话……这可不是我应该不好意思的时候。"
    "我下定了决心，说道。"
    window hide
    play music "OBGM28"
    志雄 "「婆媳关系什么的，那种事不用在乎也没关系的。不管发生什么，我都会保护智纱的……」"
    window hide
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#GRAPH_ERS
    if F103!=0:
        jump NCH06A1A_IF_ELSE13
    show expression "img/EVN_BLANK_CH04D@2x.png" as bg0
#BG_FLG EVN_CH04D
    jump NCH06A1A_IF_END13
label NCH06A1A_IF_ELSE13:
    show expression "img/EVN_BLANK_CH04I@2x.png" as bg0
#BG_FLG EVN_CH04I
label NCH06A1A_IF_END13:
#BG_PRI 0
    show expression "img/trainoutside1@2x.png" as train_bg zorder -5
    show expression "img/trainoutside_mountain@2x.png" as train_mountain zorder -4:
        ycenter .7
        block:
            xanchor 1.0
            xpos 1.3
            linear 1000 xpos 1.0
            repeat
    show expression "img/trainoutside_cloud0@2x.png" as train_cloud1 zorder -3:
        ycenter .13
        block:
            xanchor 1.0
            xpos 1.0
            linear 1000 xpos 0.2
            repeat
    show expression "img/trainoutside_cloud1@2x.png" as train_cloud2 zorder -3:
        ycenter .17
        block:
            xanchor 1.0
            xpos .8
            linear 1000 xpos 0.3
            repeat
    show expression "img/trainoutside_cloud2@2x.png" as train_cloud3 zorder -3:
        ycenter .19
        block:
            xanchor 1.0
            xpos .75
            linear 1000 xpos 0.25
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree1 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 0.3
            linear 0.5 xpos -0.3
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree2 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 0.9
            linear 0.5 xpos 0.3
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree2 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 1.0
            linear 0.5 xpos 0.4
            repeat
    with dissolve
#FADE_IN 1
    voice "NCH06A_CH034"
    智纱 "「……」"
    志雄 "「……？　智纱？」"
    voice "NCH06A_CH035"
    智纱 "「……」"
    window hide
    stop music fadeout 1
    "喂，没有在听吗！？"
    window hide
    "智纱发呆的视线好像在看着什么地方。在一群人的中间说出刚才那些台词，可是我这一生一次的豪赌啊！"
    "智纱到底在看什么啊？　沿着她的视线往前面看去。"
    jump L_NCH06A_SEL00_X
label L_NCH06A_SEL00_B:
    "婆媳关系什么的，那种事不用在乎也没关系。不管发生什么我都会保护智纱——本来想这么说的，结果因为在意周围人的视线，没有说。"
    window hide
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#GRAPH_ERS
#BG_INIC 0
#BG_PRI 0
    if F103!=0:
        jump NCH06A1A_IF_ELSE14
    show expression "img/EVN_BLANK_CH04D@2x.png" as bg0 zorder 0
#BG_FLG EVN_CH04D
    jump NCH06A1A_IF_END14
label NCH06A1A_IF_ELSE14:
    show expression "img/EVN_BLANK_CH04I@2x.png" as bg0 zorder 0
#BG_FLG EVN_CH04I
label NCH06A1A_IF_END14:
    show expression "img/trainoutside1@2x.png" as train_bg zorder -5
    show expression "img/trainoutside_mountain@2x.png" as train_mountain zorder -4:
        ycenter .7
        block:
            xanchor 1.0
            xpos 1.3
            linear 1000 xpos 1.0
            repeat
    show expression "img/trainoutside_cloud0@2x.png" as train_cloud1 zorder -3:
        ycenter .13
        block:
            xanchor 1.0
            xpos 1.0
            linear 1000 xpos 0.2
            repeat
    show expression "img/trainoutside_cloud1@2x.png" as train_cloud2 zorder -3:
        ycenter .17
        block:
            xanchor 1.0
            xpos .8
            linear 1000 xpos 0.3
            repeat
    show expression "img/trainoutside_cloud2@2x.png" as train_cloud3 zorder -3:
        ycenter .19
        block:
            xanchor 1.0
            xpos .75
            linear 1000 xpos 0.25
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree1 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 0.3
            linear 0.5 xpos -0.3
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree2 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 0.9
            linear 0.5 xpos 0.3
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree2 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 1.0
            linear 0.5 xpos 0.4
            repeat
    with dissolve
#FADE_IN 1
    voice "NCH06A_CH036"
    智纱 "「……」"
    志雄 "「智纱？」"
    "忽然注意到，智纱正在看着什么地方。"
    "是什么呢？　沿着智纱的视线往前面看去……。"
    jump L_NCH06A_SEL00_X
label L_NCH06A_SEL00_X:
    window hide
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#GRAPH_ERS
#BG_INIC 0
#BG_PRI 0
    scene expression "img/EXBG03AB@2x.png" as bg0 zorder 0
    show expression "img/trainoutside0@2x.png" as train_bg zorder -5:
        align (0,0)
    show expression "img/trainoutside_tree0@2x.png" as train_tree1 zorder -2:
        ycenter .2
        block:
            xcenter .4
            linear 0.3 xcenter -.1
            repeat
    with dissolve
#FADE_IN 1
    "智纱视线的前方，是从我这里看斜对面的座位。"
    "那边有个女人，抱着一个里面装着动物的手提袋。"
    voice "NCH06A_CH037"
    智纱 "「可……」"
    "可？"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_POSC 0,(320-224)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLC06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBC06"),"not F103==0","img/CH_XLC06A@2x.png","True","img/CH_XBC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "BGM13"
    voice "NCH06A_CH038"
    智纱 "「可爱啊……」"
    "就像要被融化一样的视线，还有语调。我第一次见到这样的智纱。"
    window hide
#CHR_DIAPPEAR 0,320,-60,10
    志雄 "「啊，智纱」"
    "智纱就像被催眠术操纵了一样，轻轻地从座位上站了起来，摇摇晃晃地走了过去。"
    "我也跟在智纱的后面，站了起来。"
    window hide
#BG_SET_BACK 
##GRAPH_ERS
#BG_INIC 1
    show expression "img/NIMG09A@2x.jpg" as bg1
#EFF_STPC 0,EFF_NOSKIP
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NCH06A_CH039"
    智纱 "「这个，是迷你达克斯芬特犬呢」"
    voice "NCH06A_XN000"
    乗客 "「啊，是的。没错呢」"
    voice "NCH06A_CH040"
    智纱 "「好可爱的小家伙啊」"
    voice "NCH06A_XN001"
    乗客 "「啊，谢谢你呢」"
    "……可爱？"
    "再看一看在宠物篮里面的达克斯芬特犬。长得过分的身体，短小的腿，很没精神耷拉着的耳朵……。"
    "可爱……吗？"
    window hide
#BG_SET_BACK
#BG_PRIC 0
    scene expression "img/EXBG03AA4@2x.png" as bg0 zorder 0 with dissolve
#EFF_STAC 0,TRAINTEXT,EFF_NOSKIP
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_POSC 0,(320+140),110
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBC01"),"not F103==0","img/CH_MLC01A@2x.png","True","img/CH_MBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_ALP_AUTOC 1,0,0,1,48
    
    voice "NCH06A_CH041"
    智纱 "「而且，看起来是很温顺、很听话的好孩子呢」"
    "哎？　智纱，能很普通地说话啊。要是平常的话，明明是那么地认生的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBB01"),"not F103==0","img/CH_MLB01A@2x.png","True","img/CH_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH042"
    智纱 "「那个，我摸摸它可以吗？」"
    voice "NCH06A_XN002"
    乗客 "「嗯，没关系的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBB02"),"not F103==0","img/CH_MLB02A@2x.png","True","img/CH_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH043"
    智纱 "「非常感谢。那……」"
    window hide
#BG_ALP_AUTOC 1,128,0,1,48
    "智纱慢慢地把手指接近它。对那个动作起了反应，身长腿短的狗抬起了前脚。"
    voice "NCH06A_CH044"
    智纱 "「啊……」"
    "叹了一口气。简直就是在梦境中的样子，非常地喜悦。"
    志雄 "「那个……，智纱？」"
    voice "NCH06A_CH045"
    智纱 "「好可爱……」"
    "好像没有听到我说的话……。"
    志雄 "「真的是那么可爱吗，这只狗？」"
    window hide
#BG_ALP_AUTOC 1,0,0,1,48
    voice "NCH06A_CH046"
    智纱 "「嗯，很可爱的」"
    "满面笑容、毫不犹豫地，立即回答。"
    志雄 "「可是，这只狗从外观上看……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBB01"),"not F103==0","img/CH_MLB01A@2x.png","True","img/CH_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH047"
    智纱 "「达克斯芬特犬就是因为是这种体型才可爱的」"
    "是、是那样的吗……？　现在有些搞不明白那个『可爱』的标准了……。"
    window hide
#BG_ALP_AUTOC 1,128,0,1,48
    voice "NCH06A_CH048"
    智纱 "「而且呢，这长长的身体和短短的腿，是为了达成它自己的任务，进化出来的」"
    voice "NCH06A_CH049"
    智纱 "「为了捕捉躲在洞穴中猪獾，就长成了如此细长的体型。达克斯芬特可是猎犬喔」"
    志雄 "「猎犬？　这是？」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBB02"),"not F103==0","img/CH_MLB02A@2x.png","True","img/CH_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    hide bg1 with dissolve
#CHR_PRIC 0
    voice "NCH06A_CH050"
    智纱 "「对！」"
    "发出了相当大的声音。这么说来智纱是喜欢动物吧。动物中好像对狗特别熟悉。"
    "达克斯芬特犬的主人看到了我们对话时的样子，好像感觉很可笑、呵呵地笑着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBA03"),"not F103==0","img/CH_MLA03A@2x.png","True","img/CH_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCH06A_CH051"
    智纱 "「啊……」"
#REMOVE_REEK_CHR 0
    "注意到了这一点，智纱的脸又红了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBC02"),"not F103==0","img/CH_MLC02A@2x.png","True","img/CH_MBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH052"
    智纱 "「嗯，对不起，志雄君。不由自主地一个人擅自热衷起来了……」"
    "智纱蜷成一团，低下了头。我轻轻地，把手放到了她的头上。"
    志雄 "「没事的啊」"
    "能见到这样的智纱的机会，非常稀少。"
    志雄 "「而且，比起紧张得有些生硬的智纱，我更喜欢有朝气的智纱啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBA03"),"not F103==0","img/CH_MLA03A@2x.png","True","img/CH_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCH06A_CH053"
    智纱 "「啊……」"
#REMOVE_REEK_CHR 0
    "我知道，听了这话，智纱的脸更红了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLA06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBA06"),"not F103==0","img/CH_MLA06A@2x.png","True","img/CH_MBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH054"
    智纱 "「谢谢……」"
    "虽说有些难为情，智纱对我微微一笑。"
    "这么说来，稻穗以前说过他养了一只狗。下次，和智纱一起去看看吧。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
#BG_ALPC 0
    show expression "img/EXBG03AB@2x.png" as bg0 zorder 0 with dissolve
    show expression "img/trainoutside0@2x.png" as train_bg zorder -5:
        align (0,0)
    show expression "img/trainoutside_tree0@2x.png" as train_tree1 zorder -2:
        ycenter .2
        block:
            xcenter .4
            linear 0.3 xcenter -.1
            repeat
    pause (32/32.0)
    stop music fadeout 1
#CHR_INIC 0
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 0,(320+160)
#CHR_POSC 1,(320-160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA01"),"True","img/SF_ZAA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA01"),"True","img/KR_ZAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0

#CHR_PRIC 0
#CHR_PRIC 1
#FADE_IN 1
    play music "BGM03"
    "回到了座位上，老爸和香里阿姨也已经回来了。"
    voice "NCH06A_KR010"
    香里 "「来，这个。给你们俩」"
    "香里阿姨把罐装的咖啡递给了我和智纱。"
    voice "NCH06A_KR011"
    香里 "「没问一下你们想要什么就买来了，不知道这个怎么样呢？」"
    志雄 "「嗯，没问题的」"
    voice "NCH06A_CH055"
    智纱 "「非常感谢」"
    "我和智纱从香里阿姨手里接过易拉罐。"
    window hide
#BG_SET_BACK 
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#GRAPH_ERS
    if F103!=0:
        jump NCH06A1A_IF_ELSE15
    scene expression "img/EVN_BLANK_CH04B@2x.png" as bg0
#BG_FLG EVN_CH04B
    jump NCH06A1A_IF_END15
label NCH06A1A_IF_ELSE15:
    scene expression "img/EVN_BLANK_CH04G@2x.png" as bg0
#BG_FLG EVN_CH04G
label NCH06A1A_IF_END15:
    $persistent.albumlist[37]=True
#BG_PRI 0
    show expression "img/trainoutside1@2x.png" as train_bg zorder -5
    show expression "img/trainoutside_mountain@2x.png" as train_mountain zorder -4:
        ycenter .7
        block:
            xanchor 1.0
            xpos 1.3
            linear 1000 xpos 1.0
            repeat
    show expression "img/trainoutside_cloud0@2x.png" as train_cloud1 zorder -3:
        ycenter .13
        block:
            xanchor 1.0
            xpos 1.0
            linear 1000 xpos 0.2
            repeat
    show expression "img/trainoutside_cloud1@2x.png" as train_cloud2 zorder -3:
        ycenter .17
        block:
            xanchor 1.0
            xpos .8
            linear 1000 xpos 0.3
            repeat
    show expression "img/trainoutside_cloud2@2x.png" as train_cloud3 zorder -3:
        ycenter .19
        block:
            xanchor 1.0
            xpos .75
            linear 1000 xpos 0.25
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree1 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 0.3
            linear 0.5 xpos -0.3
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree2 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 0.9
            linear 0.5 xpos 0.3
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree2 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 1.0
            linear 0.5 xpos 0.4
            repeat
    with dissolve
#FADE_IN 1
    voice "NCH06A_YG015"
    雄吾 "「智纱是喜欢狗吗？」"
    voice "NCH06A_CH056"
    智纱 "「哎，是、是的。……那个，您看到了吗？」"
    "智纱仿佛偷窥一样地看着雄吾。因为沉醉于玩小狗的样子被人看到了，好像有些不好意思。"
    voice "NCH06A_YG016"
    雄吾 "「啊。智纱也不是那种不爱说话的孩子啊。第一印象一下子就变过来了哦」"
    window hide
    if F103!=0:
        jump NCH06A1A_IF_ELSE16
    
    show expression "img/EVN_BLANK_CH04A@2x.png" as bg0 with dissolve
#BG_FLG EVN_CH04A
    jump NCH06A1A_IF_END16
label NCH06A1A_IF_ELSE16:
    show expression "img/EVN_BLANK_CH04F@2x.png" as bg0 with dissolve
#BG_FLG EVN_CH04F
label NCH06A1A_IF_END16:
    $persistent.albumlist[36]=True
    voice "NCH06A_CH057"
    智纱 "「唔……」"
    window hide
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#GRAPH_ERS
#BG_INIC 0
#BG_PRI 0
    scene expression "img/EXBG03AB@2x.png" as bg0 zorder 0 with dissolve
    show expression "img/trainoutside0@2x.png" as train_bg zorder -5:
        align (0,0)
    show expression "img/trainoutside_tree0@2x.png" as train_tree1 zorder -2:
        ycenter .2
        block:
            xcenter .4
            linear 0.3 xcenter -.1
            repeat
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA06"),"True","img/SF_ZAA06A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA01"),"True","img/KR_ZAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0

#CHR_POSC 0
#CHR_POSC 1,(320-270)
#CHR_PRIC 0
#CHR_PRIC 1
#FADE_IN 1
    voice "NCH06A_YG017"
    雄吾 "「志雄」"
    志雄 "「嗯？　什么啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA02"),"True","img/SF_ZAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_YG018"
    雄吾 "「现在暂且先把你将来的目标定下来吧。将来，要有一栋能养狗的独立房子才行」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA01"),"True","img/SF_ZAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_YG019"
    雄吾 "「虽说在公寓里也不是不能养宠物的，有一栋房子才安心啊。作为结婚以后的目标吧」"
    志雄 "「结、结婚是」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA03"),"True","img/KR_ZAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#ROUTINE_STA
#BG_POS_AUTOC 0,(160),0,640,448,1,F24
#CHR_POS_AUTOC 0,(320+160),0,1,F24
#CHR_POS_AUTOC 1,(320-120),0,1,F24
#ROUTINE_STP
    voice "NCH06A_KR012"
    香里 "「哎呀？　不结婚么？　和智纱」"
    志雄 "「哎？　不是，也不是说不结婚……」"
    window hide
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#GRAPH_ERS
#BG_SET_BACK
#BG_INIC 0
    if F103!=0:
        jump NCH06A1A_IF_ELSE17
    scene expression "img/EVN_BLANK_CH04E@2x.png" as bg0
#BG_FLG EVN_CH04E
    jump NCH06A1A_IF_END17
label NCH06A1A_IF_ELSE17:
    scene expression "img/EVN_BLANK_CH04J@2x.png" as bg0
#BG_FLG EVN_CH04J
label NCH06A1A_IF_END17:
#BG_PRI 0
    show expression "img/trainoutside1@2x.png" as train_bg zorder -5
    show expression "img/trainoutside_mountain@2x.png" as train_mountain zorder -4:
        ycenter .7
        block:
            xanchor 1.0
            xpos 1.3
            linear 1000 xpos 1.0
            repeat
    show expression "img/trainoutside_cloud0@2x.png" as train_cloud1 zorder -3:
        ycenter .13
        block:
            xanchor 1.0
            xpos 1.0
            linear 1000 xpos 0.2
            repeat
    show expression "img/trainoutside_cloud1@2x.png" as train_cloud2 zorder -3:
        ycenter .17
        block:
            xanchor 1.0
            xpos .8
            linear 1000 xpos 0.3
            repeat
    show expression "img/trainoutside_cloud2@2x.png" as train_cloud3 zorder -3:
        ycenter .19
        block:
            xanchor 1.0
            xpos .75
            linear 1000 xpos 0.25
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree1 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 0.3
            linear 0.5 xpos -0.3
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree2 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 0.9
            linear 0.5 xpos 0.3
            repeat
    show expression "img/trainoutside_tree1@2x.png" as train_tree2 zorder -2:
        yalign 1.0
        block:
            xanchor 0.0
            xpos 1.0
            linear 0.5 xpos 0.4
            repeat
    with dissolve
#FADE_IN 1
    "我向智纱那边瞥了一眼。不管怎么说都是太早了。"
    voice "NCH06A_KR013"
    香里 "「真是的。志雄君你一点都不干脆，所以，智纱不是会很伤心的吗」"
    window hide
    if F103!=0:
        jump NCH06A1A_IF_ELSE18
    show expression "img/EVN_BLANK_CH04B@2x.png" as bg0 with dissolve
#BG_FLG EVN_CH04B
    jump NCH06A1A_IF_END18
label NCH06A1A_IF_ELSE18:
    show expression "img/EVN_BLANK_CH04G@2x.png" as bg0 with dissolve
#BG_FLG EVN_CH04G
label NCH06A1A_IF_END18:
    voice "NCH06A_CH058"
    智纱 "「唉，我，我……」"
    voice "NCH06A_KR014"
    香里 "「呐，智纱。这个时候，应该跟志雄君这样说哦：『和我只是玩玩的吗？』」"
    志雄 "「你这是在教些什么啊！？」"
    window hide
    if F103!=0:
        jump NCH06A1A_IF_ELSE19
    show expression "img/EVN_BLANK_CH04E@2x.png" as bg0 with dissolve
#BG_FLG EVN_CH04E
    jump NCH06A1A_IF_END19
label NCH06A1A_IF_ELSE19:
    show expression "img/EVN_BLANK_CH04J@2x.png" as bg0 with dissolve
#BG_FLG EVN_CH04J
label NCH06A1A_IF_END19:
    voice "NCH06A_CH059"
    智纱 "「嗯。和我，只是玩玩的吗？」"
    志雄 "「不、不是那样的啊！」"
#MUS_VOL 0
    志雄 "「这么说来，智纱你也不应该这么听他们的话啊……」"
    window hide
    play sound "SE07_13"
    if F103!=0:
        jump NCH06A1A_IF_ELSE20
    show expression "img/EVN_BLANK_CH04A@2x.png" as bg0 with dissolve
#BG_FLG EVN_CH04A
    jump NCH06A1A_IF_END20
label NCH06A1A_IF_ELSE20:
    show expression "img/EVN_BLANK_CH04F@2x.png" as bg0 with dissolve
#BG_FLG EVN_CH04F
label NCH06A1A_IF_END20:
    voice "NCH06A_CH060"
    智纱 "「啊，嗯。对不起」"
    window hide
#MUS_VOL 128
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#GRAPH_ERS
#BG_INIC 0
#BG_PRI 0
    show expression "img/EXBG03AB@2x.png" as bg0 zorder 0 with dissolve
    show expression "img/trainoutside0@2x.png" as train_bg zorder -5:
        align (0,0)
    show expression "img/trainoutside_tree0@2x.png" as train_tree1 zorder -2:
        ycenter .2
        block:
            xcenter .4
            linear 0.3 xcenter -.1
            repeat
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA02"),"True","img/SF_ZAA02A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA02"),"True","img/KR_ZAA02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0

#BG_POSC 0,(160)
#CHR_POSC 0,(320+160)
#CHR_POSC 1,(320-120)
#CHR_PRIC 0
#CHR_PRIC 1
#FADE_IN 1
    "一边看着我们，老爸和香里阿姨一边很高兴地笑着。"
    voice "NCH06A_YG020"
    雄吾 "「嘛，你不加把劲也不行啊，为了和箱崎的小家庭」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA05"),"True","img/SF_ZAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_YG021"
    雄吾 "「因为你在人那么多的地方，突然就做了『我更喜欢有着朝气的智纱啊』这种爱的告白了嘛」"
    志雄 "「呃，老爸你也听到了吗」"
    "是我刚才对智纱说的话……。我知道自己的脸上已经热起来了。"
    志雄 "「忘了吧！　拜托您了，给我忘了吧！」"
    voice "NCH06A_KR015"
    香里 "「不行不行，那可不是想忘就能忘掉的事啊」"
    志雄 "「连香里阿姨都……」"
    voice "NCH06A_CH061"
    智纱 "「……呵呵」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA01"),"True","img/SF_ZAA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA01"),"True","img/KR_ZAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NCH06A_CH062"
    智纱 "「呵呵，好奇怪……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA02"),"True","img/SF_ZAA02A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_ZAA02"),"True","img/KR_ZAA02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    "仿佛是忍不住我们之间的交谈，智纱发出了很可爱的笑声。"
    "……她已经能笑出来了，看上去紧张已经烟消云散了。"
    voice "NCH06A_CH063"
    智纱 "「啊，对不起，不知怎的就笑了出来」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA01"),"True","img/SF_ZAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_YG022"
    雄吾 "「没事没事，没关系的」"
    voice "NCH06A_YG023"
    雄吾 "「嘛，总之，箱崎。这次旅行，玩得高兴点」"
    voice "NCH06A_CH064"
    智纱 "「是」"
    "智纱以和刚才一样的笑容，很平静地回答道。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_ZAA02"),"True","img/SF_ZAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_YG024"
    雄吾 "「旅行中，志雄就拜托你了啊。是个跟我一样，行为不端的家伙」"
    志雄 "「行为不端……」"
    "我倒觉得不至于像老爸那样。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#FADE_IN 0
    $ renpy.end_replay()
    return