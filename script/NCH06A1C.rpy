label NCH06A1C:
    $currentlabel = "NCH06A1C"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    window hide
    scene expression Solid("000") with fade
    scene expression "img/BG63AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB03"),"not F103==0","img/CH_LLB03A@2x.png","True","img/CH_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
##FADE_IN 1
    play music "BGM16"
#label START
    $month = '07'
    $day = '28'
    $date = '5'
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
#RSET F105
    $F105=1
    志雄 "「是呢……总之，先在旅馆里随便转转吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA04"),"not F103==0","img/CH_LLA04A@2x.png","True","img/CH_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH088"
    智纱 "「在旅馆里？」"
    志雄 "「嗯。后面还要在这里住好几天呢，就是想确认下这是个什么样的旅馆」"
    "但是最大的理由是，不做点什么事情，只是两个人单独在房间里呆着，让人觉得很窘迫。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA01"),"not F103==0","img/CH_LLA01A@2x.png","True","img/CH_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH089"
    智纱 "「嗯，说的也是呢」"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG61AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG61AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBB01"),"not F103==0","img/CH_MLB01A@2x.png","True","img/CH_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
#FADE_IN 1
    play music "BGM12"
    志雄 "「仔细看看的话，这也是间挺漂亮的旅馆呢」"
    voice "NCH06A_CH090"
    智纱 "「刚才的房间也很整洁呢」"
    "这是个刚刚建好的旅馆，也有这方面的缘故吧。"
    "这个大厅很宽阔，布局很和谐。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBA01"),"not F103==0","img/CH_MLA01A@2x.png","True","img/CH_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH091"
    智纱 "「在旅馆里好像只有很小的土特产店呢」"
    志雄 "「这么说来……想多转转的话，就只能去外面了吗」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBB02"),"not F103==0","img/CH_MLB02A@2x.png","True","img/CH_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH092"
    智纱 "「是呢」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG62AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression Solid("000") with None
#FADE_IN 0
    "也从工作人员那里听说了，这个旅馆的浴场是有温泉的。"
    "不只是在旅馆的里面，后山好像也有露天温泉的。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128
    scene expression "img/BG62AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
#MUS_VOL 0
    志雄 "「嗯？」"
    "在旅馆中走着的时候，我不由自主地停了下来。"
    window hide
#MUS_VOL 128
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBB04"),"not F103==0","img/CH_MLB04A@2x.png","True","img/CH_MBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCH06A_CH093"
    智纱 "「怎么了？」"
    志雄 "「没事……」"
    "我揉了揉自己的眼睛。并不是因为眼睛痒或者是脏东西进到了眼睛里。"
    志雄 "「刚才我好像看到了有个不应该出现在这里的人……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBA04"),"not F103==0","img/CH_MLA04A@2x.png","True","img/CH_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH094"
    智纱 "「不应该出现在这里的人？」"
    志雄 "「嗯」"
    志雄 "「不会的，可能只是看错了吧」"
    "我自然地接受了。肯定只是偶然看起来相似的。"
    voice "NCH06A_CH095"
    智纱 "「……？」"
    "智纱一副很奇怪的表情。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG61AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression Solid("000") with None
#FADE_IN 0
    "…………。"
    "……。"
    window hide
#FADE_OUT 0
#BG_UVC 0,0,512,640,448
#BG_COLC 0,128,128,128
    scene expression "img/BG61AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA01"),"not F103==0","img/CH_LLA01A@2x.png","True","img/CH_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#FADE_IN 1
    voice "NCH06A_CH096"
    智纱 "「已经转了一圈了呢」"
    志雄 "「是啊……」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "这旅馆中并没有什么娱乐设施。就算是全逛一遍，也不需要花多少时间。"
    "时间还绰绰有余呢，那么……。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_INIC 2
#CHR_ALPC 1
#CHR_ALPC 2
#CHR_POSC 1,((320+96)+((320)/2))
#CHR_POSC 2,((320+256)+((320)/2))
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .65
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .9
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR1 128,(320+96)
#MOV_CHR2 128,(320+256)
#MOV_CHR_GO 1
    voice "NCH06A_KR022"
    香里 "「啊，你们俩，在这种地方干什么呢？」"
    "老爸和香里阿姨从旅馆的门走了进来。"
    志雄 "「是去外面了吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA02"),"True","img/KR_MAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCH06A_KR023"
    香里 "「嗯」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC01"),"not F103==0","img/CH_LLC01A@2x.png","True","img/CH_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCH06A_CH097"
    智纱 "「去湖的那边游泳了没有？」"
    voice "NCH06A_YG034"
    雄吾 "「没有没有，到了我这把年纪就不会一到旅馆就早早跑去游泳了啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA02"),"True","img/KR_MAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCH06A_KR024"
    香里 "「哎呀，我倒是觉得那样也不错的」"
    "看香里阿姨的表情，好像是在和老爸开玩笑。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA02"),"True","img/SF_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH06A_YG035"
    雄吾 "「喂喂，饶了我吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC05"),"not F103==0","img/CH_LLC05A@2x.png","True","img/CH_LBC05A@2x.png") as lh1 zorder (10+0):
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0

    with dissolve
    voice "NCH06A_CH098"
    智纱 "「我也，在湖边……泳衣……」"
    志雄 "「哎？」"
    "智纱好像要说些什么……没有听清楚。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC06"),"not F103==0","img/CH_LLC06A@2x.png","True","img/CH_LBC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH099"
    智纱 "「啊，没事，什么事也没有！」"
    "智纱摇着双手，搪塞着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC01"),"not F103==0","img/CH_LLC01A@2x.png","True","img/CH_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0

    with dissolve
    voice "NCH06A_KR025"
    香里 "「我们刚才上街购物去了。逛了逛土特产店」"
    voice "NCH06A_KR026"
    香里 "「志雄君和智纱也是，有空的话也上街去挑选下土特产吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA01"),"not F103==0","img/CH_LLA01A@2x.png","True","img/CH_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH100"
    智纱 "「啊，好的」"
    voice "NCH06A_YG036"
    雄吾 "「那我们先回房间了」"
    window hide
    hide lh1
    hide lh2
    with dissolve
#MOV_CHR_INIT 64
#ROUTINE_STA
#CHR_POS_AUTOC 1,(576),F24
#CHR_ALP_AUTOC 1,0,1,F24
#CHR_POS_AUTOC 2,(763),F24
#CHR_ALP_AUTOC 2,0,1,F24
#CHR_POS_AUTOC 0,F24
#ROUTINE_STP
#CHR_ERSWC 1,2
#CHR_ALPC 1
#CHR_ALPC 2
    "老爸和香里阿姨转过身去，离开了大厅。"
    志雄 "「是呢……智纱，去外面看看吧」"
    "虽然还在想，刚一开始旅行就马上买土特产怎么样呢，不过既然有充裕的时间没地方打发，这样也好。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB02"),"not F103==0","img/CH_LLB02A@2x.png","True","img/CH_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH101"
    智纱 "「嗯，走吧」"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#FADE_IN 0
    $ renpy.end_replay()
    return