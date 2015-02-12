label EX04:
    $in_game=True
    $currentlabel = "EX04"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
#MENU_DIS 2+3+4+5+6+14
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_PRI 0
#BG_ALPC 0
#BG_UVC 0,(0+(640/4)),(0+(448/4)),(640/2),(448/2)
    show expression "img/BG90AA@2x.jpg" as bg0 zorder 0
#BG_SET_BACK 
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 1
#BG_UVC 1,(0+(640/4)),(0+(448/4)),(640/2),(448/2)
    show expression "img/BG08AA@2x.jpg" as bg1 zorder 1
#BG_SET_BACK 
#BG_INIC 2
#BG_PRI 2
#BG_ALPC 2
#BG_UVC 2,(0+(640/4)),(0+(448/4)),(640/2),(448/2)
    show expression "img/BG83AA@2x.jpg" as bg2 zorder 2
#BG_SET_BACK 
#BG_INIC 3
#BG_PRI 3
#BG_ALPC 3
#BG_UVC 3,(0+(640/4)),(0+(448/4)),(640/2),(448/2)
    show expression "img/BG06AA@2x.jpg" as bg3 zorder 3
#FADE_IN 0
    play sound "SE07_06"
#BG_ALPC 3
#BG_UV_AUTOC 3,0,0,640,448,0,F24
#BG_UV_SAVEC 3
    pause (36/32.0)
#BG_ALPC 2
#BG_UV_AUTOC 2,0,0,640,448,0,F24
#BG_UV_SAVEC 2
    hide bg3 with dissolve
    pause (36/32.0)
#BG_ALPC 1
#BG_UV_AUTOC 1,0,0,640,448,0,F24
#BG_UV_SAVEC 1
    hide bg2 with dissolve
    pause (36/32.0)
#BG_ALPC 0
#BG_UV_AUTOC 0,0,0,640,448,0,F24
#BG_UV_SAVEC 0
    hide bg1 with dissolve
    pause (64/32.0)
#BG_PRI 0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAA02"),"True","img/TO_XAA02A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
#TITLE_DSP
#MESLOG_TITLE
    voice "EX04_TO000"
    亨 "「终于到了！　由我，佐贺亨来担任警告剧场的这一刻！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAB05"),"True","img/TO_XAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM01NL"
    voice "EX04_TO001"
    亨 "「虽然对我来说，把信师父扔到一边还是稍微有些罪恶感的……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAA02"),"True","img/TO_XAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "EX04_TO002"
    亨 "「不过！　这下就可以和莉莉丝一起来负责这个事情了。这么机不可失失不再来的条件，我哪有不接受的道理！？」"
    voice "EX04_TO003"
    亨 "「真是的……」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 1
#BG_UVC 1,0,0,640,448
    show expression "img/BG90AA@2x.jpg" as bg1 zorder 1 with dissolve
#CHR_SORT 0
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+192)
#CHR_ALPC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SAA04"),"True","img/RI_SAA04A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .8
    with dissolve
#BG_ALP_AUTOC 1,128,0,F24
#CHR_ALP_AUTOC 1,128,0,F24
#ROUTINE_STA
#BG_ALP_SAVEC 1
#CHR_ALP_SAVEC 1
#BG_SWPC 0
#BG_PRI 0
    hide bg1 with dissolve
#ROUTINE_STP
    voice "EX04_RI000"
    莉莉丝 "「老老实实做不就好了吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAB04"),"True","img/TO_XAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "EX04_TO004"
    亨 "「哇！？　莉莉丝？　你什么时候来的？」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB04"),"True","img/TO_MAB04A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA01"),"True","img/RI_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    voice "EX04_RI001"
    莉莉丝 "「从什么时候来无所谓，负责警告剧场从一开始不就决定好了吗～」"
    voice "EX04_RI002"
    莉莉丝 "「真想赶紧去泡温泉，赶紧利落地解决掉吧！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "EX04_TO005"
    亨 "「也、也是呢……那、那么！」"
    window hide
    stop music fadeout 1128
#CHR_PRIC 0
#BG_SET_BACK 
#BG_INIC 1
#BG_PRI 1
    pause (32/32.0)
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_PRI 1
#CHR_PRIC 0
#CHR_SET_BACK
#CHR_INIC 2
#CHR_PRIC 2
#CHR_POSC 2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAA05"),"True","img/TO_XAA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "EX04_TO006"
    亨 "（冷、冷静……冷静啊，佐贺亨。难得的和莉莉丝一起在公众场合登场的机会……）"
    voice "EX04_TO007"
    亨 "（在这里像志雄一样，说喜欢你或者其他什么之类的话进行告白的话，就会是既成事实了……）"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAA06"),"True","img/TO_XAA06A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "EX04_TO008"
    亨 "（呃，不……等等～）"
    voice "EX04_TO009"
    亨 "（这里，光我来说的话恐怕是不行的吧？）"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAA05"),"True","img/TO_XAA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "EX04_TO010"
    亨 "（莉莉丝来说的话……）"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
#CHR_ALPC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XAB07"),"True","img/RI_XAB07A@2x.png") as lh1 zorder (1000-1):
        ypos 0.0
#BG_SET_BACK 
#BG_INIC 2
#BG_PRI 2
#BG_ALPC 2
    show expression "img/NIMG13A@2x.jpg" as bg2 zorder 200 with dissolve
#FADE_OUT 1,8,COL_WHITE
#CHR_ALPC 2
#BG_ALPC 1
#CHR_ALPC 1
#BG_ALPC 2
#FADE_IN 1
    play music  "OBGM29"
    voice "EX04_TO011"
    亨 "（阿亨……笨蛋……但是，喜欢你……）"
    window hide
    
    stop music fadeout 18
#FADE_OUT 1,8,COL_WHITE
#CHR_ALPC 2
#BG_ALPC 1
#CHR_ALPC 1
#BG_ALPC 2
#FADE_IN 1
    voice "EX04_TO012"
    亨 "（之类的～）"
    window hide
#FADE_OUT 1,8,COL_WHITE
#CHR_ALPC 2
#BG_ALPC 1
#CHR_ALPC 1
#BG_ALPC 2
#FADE_IN 1
    play music  "OBGM29"
    voice "EX04_TO013"
    亨 "（小亨……最喜欢你了～❤）"
    window hide
    stop music fadeout 18
#FADE_OUT 1,8,COL_WHITE
#CHR_ALPC 2
#BG_ALPC 1
#CHR_ALPC 1
#BG_ALPC 2
#FADE_IN 1
    voice "EX04_TO014"
    亨 "（之类的～）"
    window hide
#FADE_OUT 1,8,COL_WHITE
#CHR_ALPC 2
#BG_ALPC 1
#CHR_ALPC 1
#BG_ALPC 2
#FADE_IN 1
    play music  "OBGM29"
    voice "EX04_TO015"
    亨 "（我想穿着这套衣服陪你一起度过明天～♥）"
    window hide
    stop music fadeout 18
#FADE_OUT 1,8,COL_WHITE
#CHR_ALPC 2
#BG_ALPC 1
#CHR_ALPC 1
#BG_ALPC 2
#FADE_IN 1
    voice "EX04_TO016"
    亨 "（之类的～）"
    window hide
#FADE_OUT 1,8,COL_WHITE
#CHR_ALPC 2
#BG_ALPC 1
#CHR_ALPC 1
#BG_ALPC 2
#FADE_IN 1
    play music  "OBGM29"
    voice "EX04_TO017"
    亨"（我也，一直一直喜欢你～♥）"
    window hide
    stop music fadeout 18
#FADE_OUT 1,8,COL_WHITE
#CHR_ALPC 2
#BG_ALPC 1
#CHR_ALPC 1
#BG_ALPC 2
#FADE_IN 1
    voice "EX04_TO018"
    亨 "（之类的～）"
    window hide
#FADE_OUT 1,8,COL_WHITE
#CHR_ALPC 2
#BG_ALPC 1
#CHR_ALPC 1
#BG_ALPC 2
#FADE_IN 1
    play music  "OBGM29"
    voice "EX04_TO019"
    亨 "（心与心连在一起呢～♥）"
    window hide
    stop music fadeout 18
#FADE_OUT 1,8,COL_WHITE
#CHR_ALPC 2
#BG_ALPC 1
#CHR_ALPC 1
#BG_ALPC 2
#FADE_IN 1
    voice "EX04_TO020"
    亨 "（之类的～）"
    hide lh2
    hide lh1
    hide bg2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAA04"),"True","img/TO_XAA04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "EX04_TO021"
    亨 "（不这样说的话……就没有意义了！　绝对超赞！）"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAB03"),"True","img/TO_XAB03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "EX04_TO022"
    亨 "（这样的话，首先要创造一个好的气氛吧！）"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAB01"),"True","img/TO_XAB01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "EX04_TO023"
    亨 "（呃～师父给我的攻略本确实是在这里……哼哼……嘿嘿…………诶、啊、啊，是这样。　啊、啊，原来如此……）"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAB02"),"True","img/TO_XAB02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "EX04_TO024"
    亨 "（太好了！　这样的话就能完美攻略了！　等着我哦，我的莉莉丝～）"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_ALPC 0
#CHR_ALPC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA06"),"True","img/RI_MAA06A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
    with dissolve
#FADE_OUT 1,8,COL_WHITE
    hide bg1
#CHR_ALPC 0
#CHR_ALPC 1
    hide lh2
    with dissolve
#CHR_PRIC 2
#FADE_IN 1
    play music  "BGM09"
    voice "EX04_RI003"
    莉莉丝 "「喂——佐贺君！」"
    window hide
#CHR_SORT 1,2
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2,((320+192)+96)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB03"),"True","img/CL_MAB03A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
        xcenter .8
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA06"),"True","img/RI_MAA06A@2x.png") as lh1 zorder (10+1):
        xcenter .5
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh0 zorder (10+0):
        xcenter .2
        ypos 0.0
    with move
#MOV_CHR_INIT 40
#MOV_CHR0 ,(320-192)
#MOV_CHR1 
#MOV_CHR2 128,(320+192)
#MOV_CHR_GO 1
    voice "EX04_KU000"
    克罗艾 "「咦，怎么了，远峰同学？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC04"),"True","img/RI_MAC04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "EX04_RI004"
    莉莉丝 "「啊，克罗艾学姐。我们要在这里发布一下『警告』，不过佐贺君突然陷进了自己的世界里了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC04"),"True","img/CL_MAC04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "EX04_KU001"
    克罗艾 "「看起来……回不来了呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC01"),"True","img/CL_MAC01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "EX04_KU002"
    克罗艾 "「那，我来做可以吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC02"),"True","img/RI_MAC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "EX04_RI005"
    莉莉丝 "「诶！　真的吗！？　帮大忙了！」"
    voice "EX04_KU003"
    克罗艾 "「原稿在……这里呢。」"
    voice "EX04_RI006"
    莉莉丝 "「是，拜托了！」"
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
#CHR_SORT 0,1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAD01"),"True","img/RI_LAD01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
#BG_BLUR 0
    play music  "BGM01NL"
#MESA A_CH_KU,EX04_KU006"【クロエ】「您现在所玩的这个游戏软件是，ＩＯＳ专用的游戏软件。」%K%P"
    voice "EX04_KU006"
    克罗艾 "「您现在所玩的这个游戏软件是，ＩＯＳ专用的游戏软件。」"
    voice "EX04_KU007"
    克罗艾 "「请不要放入其他的游戏机以及其他的播放器里进行游戏或者播放。」"
    "谜之声：对不起我作死了。"
    voice "EX04_RI007"
    莉莉丝 "「以上，是警告信息！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2,(320-640)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_SAB04"),"True","img/TO_SAB04A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 20
#MOV_CHR2 
#MOV_CHR_GO 1
#BG_BLUR 0
    voice "EX04_TO025B"
    亨 "「嗯！？　什么！？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAC02"),"True","img/RI_LAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#ROUTINE_STA
#BG_BLUR 0
#CHR_BLUR 2
#ROUTINE_STP
    play music  "BGM01NL"
    voice "EX04_RI008"
    莉莉丝 "「克罗艾学姐谢谢你。把要说的全部都说了呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC01"),"True","img/CL_LAC01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "EX04_KU008"
    克罗艾 "「没什么。能够完成任务的话，再好不过了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAC01"),"True","img/RI_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "EX04_RI009"
    莉莉丝 "「啊，难得的机会学姐不一起去温泉吗？　我外婆的熟人开的店铺，实在是个不错的地方呢……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_SAA03"),"True","img/TO_SAA03A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
    with dissolve
#CHR_BLUR 2
    voice "EX04_TO026"
    亨 "「喂，莉莉丝，警告呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAC05"),"True","img/RI_LAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#ROUTINE_STA
#BG_BLUR 0
#CHR_BLUR 2
#ROUTINE_STP
    voice "EX04_RI010"
    莉莉丝 "「啊，已经结束了，所以佐贺君也赶紧回去吧～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAC02"),"True","img/RI_LAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#ROUTINE_STA
#BG_BLUR 0
#CHR_BLUR 2
#ROUTINE_STP
    voice "EX04_RI011"
    莉莉丝 "「啊还有还有，连露天温泉也有呢……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB04"),"True","img/CL_LAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "EX04_KU009"
    克罗艾 "「塚……塚本他，也去吗？」"
    window hide
    stop music
    hide lh1
    hide lh0
    with dissolve
#MOV_CHR_INIT 240
#MOV_CHR0 ,((320-160)+(640+(640/2)))
#MOV_CHR1 ,((320+160)+(640+(640/2)))
#MOV_CHR_GO 0
#CHR_ERSWC 0
#ROUTINE_STA
#BG_BLUR 0
#CHR_BLUR 2
#ROUTINE_STP
    play sound "SE00_28"
    play sound "SE00_29"
    play music  "OBGM16"
    voice "EX04_TO027"
    亨 "「在应该告白的地方连警告都没有做成，去温泉也不带我……我的这份悲伤只有信师父才能理解啊！」"
    stop music fadeout 18
    play sound "SE02_01"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_SAB04"),"True","img/TO_SAB04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "EX04_TO028"
    亨 "「诶，短信？」"
    play sound "SE02_03"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_SAA05"),"True","img/TO_SAA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "EX04_TO029"
    亨 "「『接下来要暂时在温泉旅馆打工！　佐贺君就在补习学校好好努力吧！　Ｂｙ信』」"
    window hide
    play sound "SE05_12"
    pause (48/32.0)
#ROUTINE_STA
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAB05"),"True","img/TO_XAB05A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
    with dissolve
#QUA_BG 0
#ROUTINE_STP
    voice "EX04_TO030"
    亨 "「我也要去温泉啊啊啊啊啊啊啊——」"
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
#MENU_ENA 2+3+4+5+6+14
#SETACHIEVE 23
    $ renpy.end_replay()
    return