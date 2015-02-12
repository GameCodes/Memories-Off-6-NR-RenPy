label NCH06A1D:
    $currentlabel = "NCH06A1D"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    window hide
##FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG63AA@2x.jpg" as bg0 zorder 0 with dissolve
#BG_BLUR 0
    scene expression "img/BG63AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB03"),"not F103==0","img/CH_LLB03A@2x.png","True","img/CH_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
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
    志雄 "「那就先上街，去土特产店吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB01"),"not F103==0","img/CH_LLB01A@2x.png","True","img/CH_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "在车站到旅馆来的路上发现了一个商店街。以土特产作为主要商品的店看上去有很多。"
    "去那边转转的话，说不定会很有意思。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 1
#BG_SETWC 0,1,BG71AA,NIMG01B
#EFF_STAC 0,CLOUD_A,EFF_SKIP
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
    play sound "SE01_12L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 0
    "我和智纱一起出了旅馆，向着卖土特产的街道出发。那里离车站比离旅馆更近。走路的话大约是20分钟的距离。"
    "但是，好不容易来到了观光地，也想看看小镇的样子。我和智纱决定走着去那儿。"
    window hide
    stop se fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    hide bg1 with dissolve
    stop se
    scene expression "img/BG71AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_15L"
    pause (32/32.0)
#EFF_STAC 0,SUNLIGHT_BG71,EFF_SKIP
#FADE_IN 1
#SE_VOLC 1
    play music "BGM11"
    "在去商店街的途中，有一个神社。"
    "来旅馆的路上是乘出租车的，所以没有注意到。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLB06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBB06"),"not F103==0","img/CH_MLB06A@2x.png","True","img/CH_MBB06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
        xcenter .35
    with dissolve
    志雄 "「是神社啊……{w=3}{nw}"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBB01"),"not F103==0","img/CH_MLB01A@2x.png","True","img/CH_MBB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    extend "过去看看怎么样？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBB02"),"not F103==0","img/CH_MLB02A@2x.png","True","img/CH_MBB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH102"
    智纱 "「嗯」"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG73AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG73AA@2x.jpg" as bg0 with dissolve
#SE_VOLC 1
#EFF_STAC 0,SUNLIGHT_BG50_FRONT,EFF_SKIP
#EFF_STAC 1,SUNLIGHT_BG50_BACK,EFF_SKIP
#FADE_IN 1
    pause (32/32.0)
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC03"),"not F103==0","img/CH_LLC03A@2x.png","True","img/CH_LBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH103"
    智纱 "「……哈」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC01"),"not F103==0","img/CH_LLC01A@2x.png","True","img/CH_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "登上了石阶，喘了口气。跟在我身后爬上来的智纱的额头上渗出了豆大的汗珠。"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE03_88"
    "我从包里取出运动饮料。"
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBC01"),"not F103==0","img/CH_XLC01A@2x.png","True","img/CH_XBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「智纱，给你这个」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBA04"),"not F103==0","img/CH_XLA04A@2x.png","True","img/CH_XBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH104"
    智纱 "「哎？」"
    "智纱一副很诧异的表情，接过了我递出的塑料瓶。"
    志雄 "「补充水分。万一中暑了可就不好办了，不喝点什么可不行」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBA01"),"not F103==0","img/CH_XLA01A@2x.png","True","img/CH_XBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH105"
    智纱 "「谢谢」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLB05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBB05"),"not F103==0","img/CH_XLB05A@2x.png","True","img/CH_XBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "智纱打开了盖子，把塑料瓶凑到了嘴边。咕嘟咕嘟地，小小的喉咙上下蠕动着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBB01"),"not F103==0","img/CH_XLB01A@2x.png","True","img/CH_XBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "把塑料瓶从嘴边拿开，稍稍喘了一口气之后，智纱看向我这边。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBA01"),"not F103==0","img/CH_XLA01A@2x.png","True","img/CH_XBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#BG_INIC 3
#BG_PRI 3
#BG_ALPC 3
#BG_POSC 3,0,(448/4)+(448/4),640,448
    show expression "img/NIMG17B@2x.png" as bg3 zorder 10:
        xcenter ((448/4)+(448/4))/640.0
    with dissolve
#THREAD_STA 1,THREAD_PET
    voice "NCH06A_CH106"
    智纱 "「……那个，志雄君也喝吗？」{w=3}{nw}"
#THREAD_WAT 1
#MESX "%K%P"
    志雄 "「哎？」"
    "智纱把瓶口朝向我这边。"
    志雄 "「不用了，没关系！　也带着自己的了」"
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
    hide bg3
#BG_SWPC 0
    hide bg1
    with dissolve
#BG_PRI 0
#BG_PRI 1
    "我慌张地取出了自己用的塑料瓶。明明已经实际地吻过智纱了，为什么反倒会对间接接吻感到不好意思啊。"

#BG_INIC 1
#BG_ALPC 1
#ROUTINE_STA
#BG_ALP_AUTOC 1,128,0,1,48
#BG_UV_AUTOC 0,0,0,(640/2),(448),0,1,48
#ROUTINE_STP
    pause (32/32.0)
#BG_UVC 0,(640/2),0,(640/2),(448)
    show expression "img/BG72AA@2x.jpg" as bg0 zorder 0 with dissolve
#ROUTINE_STA
#BG_ALP_AUTOC 1,0,0,1,48
#BG_UV_AUTOC 0,0,0,(640),(448),0,1,48
#ROUTINE_STP
    pause (32/32.0)
#ROUTINE_STA
#BG_ALP_AUTOC 1,128,0,1,48
#BG_UV_AUTOC 0,0,0,(640/2),(448),0,1,48
#ROUTINE_STP
#BG_UVC 0,(640/2),0,(640/2),(448)

#ROUTINE_STA
#BG_ALP_AUTOC 1,0,0,1,48
#BG_UV_AUTOC 0,0,0,(640),(448),0,1,48
#ROUTINE_STP
    "我一边喝着塑料瓶里的饮料，一边环视着神社境内。并不是个多大的神社。"
#ROUTINE_STA
#BG_ALP_AUTOC 1,128,0,1,48
#BG_UV_AUTOC 0,0,0,(640/2),(448),0,1,48
#ROUTINE_STP
    pause (32/32.0)
#BG_UVC 0,(640/2),0,(640/2),(448)
    show expression "img/BG72AA@2x.jpg" as bg0 zorder 0 with dissolve
#ROUTINE_STA
#BG_ALP_AUTOC 1,0,0,1,48
#BG_UV_AUTOC 0,0,0,(640),(448),0,1,48
#ROUTINE_STP
    志雄 "「……嗯？　那个，是什么啊？」"
    "视野内的一端——离开参拜道路的地方，放着一些像是床单一样的东西。在那旁边，有着好像帐篷的骨架一样的东西……。"
    "那个是什么啊？"
    voice "NCH06A_CH107"
    智纱 "「啊，志雄君，有抽签的地方。去抽一个好吗？」"
#ROUTINE_STA
#BG_ALP_AUTOC 1,128,0,1,48
#BG_UV_AUTOC 0,0,0,(640/2),(448),0,1,48
#ROUTINE_STP
    pause (32/32.0)
#BG_UVC 0,(640/2),0,(640/2),(448)
    show expression "img/BG73AA@2x.jpg" as bg0 zorder 0 with dissolve
#ROUTINE_STA
#BG_ALP_AUTOC 1,0,0,1,48
#BG_UV_AUTOC 0,0,0,(640),(448),0,1,48
#ROUTINE_STP
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBA01"),"not F103==0","img/CH_XLA01A@2x.png","True","img/CH_XBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "听到了智纱的喊声，我转了过去。"
    志雄 "「抽签？　那样的话，我也来抽一个看看吧」"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#EFF_STPC 1,EFF_SKIP
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG72AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG72AA@2x.jpg" as bg0 with dissolve
    play sound "SE03_104"
#SE_VOLC 1
#EFF_STAC 0,SUNLIGHT_BG50_FRONT,EFF_SKIP
#EFF_STAC 1,SUNLIGHT_BG50_BACK,EFF_SKIP
#FADE_IN 1
    "我和智纱在社务所抽了签。"
    window hide
#SE_VOLC 1,255
#MUS_VOL 0
#ROUTINE_STA
#BG_INIC 1
#ROUTINE_STP
#EFF_STAC 2,EXT_BG_ROTATE,EFF_NOSKIP,1,390
#BG_BLUR 1
    志雄 "「真……真的吗……？」"
    "以一种难以置信的心情，我注视着自己手里的签。"
    志雄 "「平常的话，不是只放好签的吗……？」"
    "手上的签——上面写着的是，『大凶』两个字。"
    "写着的内容是……『愿望』是「不会实现。就算实现也会后悔」。『学习』是「前景暗淡」。『恋爱』是「恐怕会要破裂」。"
    "好的事情，一个都没有。特别是学习运：「前景黯淡」。从现在的我的状况来看，笑不出来……。"
    window hide
#SE_VOLC 1
#MUS_VOL 128
#BG_BLUR 1
#EFF_STAC 2,EXT_BG_ROTATE,EFF_NOSKIP,1
#ROUTINE_STA
    hide bg1 with dissolve
#BG_ALPC 0
#EFF_STAC 0,SUNLIGHT_BG50_FRONT,EFF_SKIP
#EFF_STAC 1,SUNLIGHT_BG50_BACK,EFF_SKIP
#ROUTINE_STP
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,640
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBB01"),"not F103==0","img/CH_XLB01A@2x.png","True","img/CH_XBB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 64
#MOV_CHR0 128,(320+192)
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
    voice "NCH06A_CH108"
    智纱 "「志雄君的签是什么呢？」"
    play sound "SE03_43"
    志雄 "「——！？」"
#THREAD_STA 1,THREAD_QUA_WIN
#VIB_DOKA 
#MESA A_CH_SI,"【志雄】「——！？」"
#THREAD_WAT 1
#WIN_POS 0,0
#VIB_STP 5
#MESX "%K%P"
    "智纱从我的肩膀后面偷看着。我立刻把我的签藏了起来，因为恋爱运是「恐怕会要破裂」，智纱说不定会在意……。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBA04"),"not F103==0","img/CH_XLA04A@2x.png","True","img/CH_XBA04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH109"
    智纱 "「为什么要藏着呢？」"
    志雄 "「没、没，并不是要藏着的。啊哈哈哈……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBC04"),"not F103==0","img/CH_XLC04A@2x.png","True","img/CH_XBC04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    "智纱歪着头，很奇怪地看着我这里。"
    志雄 "「先、先不说这个，智纱你的签是什么呢？　是大吉吗？」"
    "总之先要摆脱掉这种微妙的氛围，敷衍着问问。"
    "从刚才智纱快活的样子来看，我想一定是得到了好结果。"
    hide lh0 with dissolve
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB01"),"not F103==0","img/CH_LLB01A@2x.png","True","img/CH_LBB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH110"
    智纱 "「啊，那～个。我的是这个」"
    "向智纱拿出来的签看过去。"
    志雄 "「……小吉？」"
    "意外地，并不是什么特别好的结果啊。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB05"),"not F103==0","img/CH_LLB05A@2x.png","True","img/CH_LBB05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH111"
    智纱 "「嗯。虽说是小吉……来，看看这里」"
    "智纱指着写着恋爱运的地方。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB01"),"not F103==0","img/CH_LLB01A@2x.png","True","img/CH_LBB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH112"
    智纱 "「写着『接近转机。向着更好的一层发展』呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB02"),"not F103==0","img/CH_LLB02A@2x.png","True","img/CH_LBB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH113"
    智纱 "「其它的倒是没有写什么特别好的东西，不过哪怕是有一件好事我也很高兴了哦」"
    voice "NCH06A_CH114"
    智纱 "「而且，那件事，还正好是和志雄君的事」"
    "对啊……还有这种考虑方法的啊。就算全都不好也没关系，哪怕只有一件是好事。"
    志雄 "「好！」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我又重新看了看自己的签。在这个『大凶』里面，如果有哪怕一个好的地方的话……！"
    志雄 "「……」"
    window hide
#SE_VOLC 1,255
#MUS_VOL 0
#BG_INIC 1
#BG_PRIC 1
#BG_ALPC 1
    show expression "img/BG72AA_BLUE@2x.jpg" as bg1 zorder 1 with dissolve
#BG_ALP_AUTOC 1,100,0,1,48
    志雄 "「……不行，什么都没有……」"
    "看遍了签的每一个角落，哪怕是一件好事都没有。真不愧是大凶。"
    window hide
#SE_VOLC 1
#MUS_VOL 128
#BG_ALP_AUTOC 1,0,0,1,48
    hide bg1 with dissolve
#BG_PRIC 1
#BG_ALPC 1
#CHR_MGNC_F 10,CH_XLC04,CH_XBC04
    voice "NCH06A_CH115"
    智纱 "「志、志雄君？　怎么了，一副如此失落的脸色？」"
    "智纱注视着我的脸。然后，视线滑到了我拿着的签上面。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBA04"),"not F103==0","img/CH_XLA04A@2x.png","True","img/CH_XBA04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH116"
    智纱 "「啊，大凶……」"
    志雄 "「呜」"
    "被她看见了……。"
    voice "NCH06A_CH117"
    智纱 "「而且，恋爱是『破裂』……」"
    "……。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBC04"),"not F103==0","img/CH_XLC04A@2x.png","True","img/CH_XBC04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH118"
    智纱 "「没关系的啊！　抽签什么的，只是占卜而已！　是迷信的，迷信！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBC01"),"not F103==0","img/CH_XLC01A@2x.png","True","img/CH_XBC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH119"
    智纱 "「对了！　这么的话，你知道把凶签除去的方法吗？」"
    志雄 "「把凶除去？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBA01"),"not F103==0","img/CH_XLA01A@2x.png","True","img/CH_XBA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH120"
    智纱 "「凶的签，要用自己不好用的那只手系在树上，就能够除去坏运气了」"
    志雄 "「不好用的那只手……难道是单手来做吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBB02"),"not F103==0","img/CH_XLB02A@2x.png","True","img/CH_XBB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH121"
    智纱 "「嗯」"
    "完全没有犹豫的点头……可是，这件事不是相当难吗？"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#EFF_STPC 1,EFF_SKIP
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,(640/2),(448/4),(640/2),(448/2)
    show expression "img/BG73AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG72AA@2x.jpg" as bg0 with dissolve
    pause (48/32.0)
#SE_VOLC 1
#EFF_STAC 0,SUNLIGHT_BG73_FRONT2,EFF_SKIP
#EFF_STAC 1,SUNLIGHT_BG73_BACK2,EFF_SKIP
#FADE_IN 1
    志雄 "「呜呜呜」"
    "在树下，我用单手拿着抽来的签，陷入了苦战。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_POSC 0,(320-96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC01"),"not F103==0","img/CH_LLC01A@2x.png","True","img/CH_LBC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCH06A_CH122"
    智纱 "「加油！　然后就是把那一头插进去拉一下就好了」"
    "听着智纱的助威声，总算是把打结的环做了出来……。"
    志雄 "「啊，手要抽筋了」"
    "树枝比自己的身高还要高，手必须一直往上伸着，很累。"
    "智纱看着我的样子，沉思了片刻。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA01"),"not F103==0","img/CH_LLA01A@2x.png","True","img/CH_LBA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH123"
    智纱 "「那，我也来帮忙吧」"
    志雄 "「哎？」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    if F103!=0:
        jump NCH06A1D_IF_ELSE
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH05A")]=True
    scene expression "img/EVN_CH05A@2x.jpg" as bg1 with dissolve
    jump NCH06A1D_IF_END
label NCH06A1D_IF_ELSE:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH05B")]=True
    scene expression "img/EVN_CH05B@2x.jpg" as bg1 with dissolve
label NCH06A1D_IF_END:
    "智纱的手，轻轻放到了我握着签的那只手上。她手上的那份温暖传了过来。"
    voice "NCH06A_CH124"
    智纱 "「好，就这样……这样……」"
    window hide
    scene expression "img/BG72AA@2x.jpg" as bg0 with dissolve
    志雄 "「……做好了」"
    "到底是有两只手，结起签来比起一只手要简单得多。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB05"),"not F103==0","img/CH_LLB05A@2x.png","True","img/CH_LBB05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH125"
    智纱 "「这样志雄君的凶就能除去了呢」"
    志雄 "「谢谢」"
    志雄 "「可是，这不就违反规则……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB01"),"not F103==0","img/CH_LLB01A@2x.png","True","img/CH_LBB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH126"
    智纱 "「没关系的，志雄君只用了一只手的事实是没有改变的」"
    志雄 "「是……呢」"
    "能够和智纱这样在一起，就不可能是大凶了。"
    voice "NCH06A_CH127"
    智纱 "「这样恋爱运也是，志雄君不好的部分也能够除掉了。剩下的只有我的好运了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB02"),"not F103==0","img/CH_LLB02A@2x.png","True","img/CH_LBB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH128"
    智纱 "「所以，我们今后也能『向着更好的方向』。一定能很好地走下去的」"
    "嗯，一定是这样的。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#EFF_STPC 1,EFF_SKIP
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_QUA_WIN
#TH_QUAKE_WIN 4
#EOT
#label THREAD_PET
#WAIT2 48
#BG_ALP_AUTOC 3,128,1,F123
#BG_POS_AUTOC 3,,(448/4),,F123
#BG_ALP_SAVEC 3
#BG_POS_SAVEC 3
#EOT