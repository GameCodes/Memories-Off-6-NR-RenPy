label NCH11A:
    $currentlabel = "NCH11A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '09'
    $day = '01'
    $date = '5'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG07AA2@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG07AA2@2x.jpg" as bg0 with dissolve
    play sound "SE06_02"
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
    voice "NCH11A_X8000"
    老师 "「那么，明天开始就要上课了。这是考试前的冲刺，做好心理准备吧」"
    play sound "SE00_22"
    "教室中传来了责难和喝倒彩的声音，班主任还是一副若无其事的样子，从教室里走了出去。"
    stop sound
    "因为今天是第二学期的第一天，所以就只有开学典礼。"
    window hide
    stop se fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    show expression "img/NIMG15A-568h@2x.jpg" as cal zorder 5
    show expression "img/09_05_FRIDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#FADE_IN 0
#CAL_DSP_GRP 1,CAL_0901
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 2
#BG_UVC 2,0,512,640,448
#BG_SETWC 0,2,BG07AA3,BG07AA3
    scene expression "img/BG07AA3@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA03"),"True","img/TO_MAA03A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
    play sound "SE08_10L"
#FADE_IN 1
    voice "NCH11A_TO000"
    亨 "「哈……。暑假已经结束了啊」"
    voice "NCH11A_TO001"
    亨 "「又过去了一个季节啊……」"
    志雄 "「你啊，装成个诗人的样子，在说什么废话呢」"
    window hide
#CHR_SORT 0,2
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 2
#CHR_ALPC 2
#CHR_ALPC 0
#CHR_POSC 0,640
#CHR_POSC 2,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA06"),"True","img/RI_MAA06A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA03"),"True","img/TO_MAA03A@2x.png") as lh1 zorder (10-1):
        xcenter .75
        ypos 0.0

#ROUTINE_STA
#CHR_POS_AUTOC 0,(320+160),0,0,F24,81
#CHR_ALP_AUTOC 0,128,1,F24,81
#CHR_POS_AUTOC 1,(320-160),0,0,F24,80
#ROUTINE_STP
#CHR_POS_SAVEC 0
#CHR_POS_SAVEC 1
    voice "NCH11A_RI000A"
    莉莉丝 "「佐贺君，新学期第一天就这么散漫啊。{w=6}{nw}"
#MESA A_CH_RI,NCH11A_RI000A,"【りりす】「佐贺君，新学期第一天就这么散漫啊。"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA05"),"True","img/RI_MAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH11A_RI000B"
    extend "拿出点精神好不好」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB03"),"True","img/TO_MAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH11A_TO002"
    亨 "「虽然话是这么说，但是一想到开学，就一点也开心不起来了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA01"),"True","img/RI_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH11A_RI001"
    莉莉丝 "「唉，这点上倒是有同感」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO_LAB02'",DynamicDisplayable(mouthanime,"TO_LAB02"),"True","img/TO_LAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH11A_TO003"
    亨 "「这么说来，志雄君。今年的夏天，怎么样啊？」"
#ROUTINE_STA
#BG_ALP_AUTOC 0,0,0,F24,24
#CHR_ALP_AUTOC 2,128,0,F24,24
#ROUTINE_STP
#BG_ALP_SAVEC 0
#CHR_ALP_SAVEC 2
#ROUTINE_STA
#BG_SWPC 0
    hide bg2 with dissolve
#BG_PRI 0
#BG_PRI 2
#BG_ALPC 2
#BG_UVC 2,0,0,640,448
#CHR_SWPC 0
#CHR_ALPC 2
#CHR_SORT 0,1
#ROUTINE_STP
    voice "NCH11A_RI002"
    莉莉丝 "「对对。怎么样啊？」"
    "莉莉丝和亨对着我冷冷地笑着，让人害怕。"
    志雄 "「你，你们干什么啊。什么怎么样啊？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB01"),"True","img/TO_LAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH11A_TO004"
    亨 "「自然是说你和智纱的关系啊！」"
    志雄 "「为什么是“自然”啊……？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAD01"),"True","img/RI_LAD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH11A_RI003"
    莉莉丝 "「本来就是“自然”啊」"
    "……看来确实是很“自然”的了。"
    voice "NCH11A_TO005"
    亨 "「直到暑假结束为止，一直等着没有去问你们。8月这段时间，你们俩的关系，发生了什么变化……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB02"),"True","img/TO_LAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH11A_TO006"
    亨 "「就是为了听到那个变化，然后感到惊天快乐的那一刻啊！」"
    "已经特地做到这个地步了吗？　看来亨的这个暑假，大概是没什么高兴的事情吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAA01"),"True","img/RI_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH11A_RI004"
    莉莉丝 "「就是这么回事。我也很在意呢，和智纱的旅行怎么样，到最后也没问」"
    voice "NCH11A_RI005"
    莉莉丝 "「结果怎么样？　旅行」"
    志雄 "「怎么样……是秘密哦」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAA03"),"True","img/RI_LAA03A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB04"),"True","img/TO_LAB04A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NCH11A_MIX00"
    りりす・亨 "「秘密～！？」"
    "最近这两个人的步调，出奇地一致。"
    志雄 "「要我说的话，全说给你们听也没问题。大概，我们已经过于幸福，以至于快要受不了了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAA05"),"True","img/RI_LAA05A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB05"),"True","img/TO_LAB05A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NCH11A_MIX01"
    りりす・亨 "「呃！」"
    play sound "SE03_12"
    志雄 "「哦，差不多该走了。那，我先走了！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAC03"),"True","img/RI_LAC03A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAA03"),"True","img/TO_LAA03A@2x.png") as lh1 zorder (10+1):
        xcenter .75
#REEK_CHR 0
    voice "NCH11A_RI008"
    莉莉丝 "「喂，你」"
#REMOVE_REEK_CHR 0
    window hide
    stop music fadeout 1
#SE_VOLC 1,255
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NCH11A_RI009"
    莉莉丝 "「你等一下啊～！」"
#BG_INIC 1
    show expression "img/BG08AA@2x.jpg" as bg1 with dissolve
    pause (32/32.0)
#SE_VOLC 1
#BG_INIC 0
    scene expression "img/NIMG01B@2x.png" as bg2 zorder 2
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
    
#EFF_PRI 0
#EFF_STAC 0,CLOUD_B,EFF_NOSKIP
    hide bg1 with dissolve
    voice "NCH11A_RI010"
    莉莉丝 "「别一个人去Happy End啊—！」"
    voice "NCH11A_TO009"
    亨 "「莉莉丝～！　我们也～！」"
    voice "NCH11A_RI011"
    莉莉丝 "「烦死了！」"
    play sound "SE04_07"
#THREAD_STA 1,THREAD_QUA_WIN
    voice "NCH11A_TO010"
    亨 "「痛啊」{w=5}{nw}"
#THREAD_WAT 1
#WIN_POS 0,0
#MESX "%K%P"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG83AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG83AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MKA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MAA01"),"not F103==0","img/CH_MKA01A@2x.png","True","img/CH_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
    play sound "SE05_15L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,(64/4)
    play music "BGM03"
    志雄 "「抱歉，久等了」"
    voice "NCH11A_CH000"
    智纱 "「没事」"
    voice "NCH11A_CH001"
    智纱 "「学生会的事情，已经结束了？」"
    志雄 "「嗯，就说了第二学期也要加油，简简单单就解决了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MKB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MAB01"),"not F103==0","img/CH_MKB01A@2x.png","True","img/CH_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH11A_CH002"
    智纱 "「那，回去吧」"
    志雄 "「好不容易这么早就结束，偶尔也绕道去什么地方吧」"
    志雄 "「想尝尝Wack的新款薯条的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MKB06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MAB06"),"not F103==0","img/CH_MKB06A@2x.png","True","img/CH_MAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH11A_CH003A"
    智纱 "「哎～。非要去的话我还是觉得甜的东西比较好啊。……{w=3}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MKB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MAB02"),"not F103==0","img/CH_MKB02A@2x.png","True","img/CH_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH11A_CH003B"
    extend "比如蛋糕？」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAB02"),"not F103==0","img/CH_LKB02A@2x.png","True","img/CH_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "手牵着手，走了出去。"
    window hide
#SE_VOLC 1,
    show expression "img/BG06AA@2x.jpg" as bg_over zorder 2 with dissolve
    voice "NCH11A_CH004"
    智纱 "「那个，志雄君……」"
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XKB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XAB01"),"not F103==0","img/CH_XKB01A@2x.png","True","img/CH_XAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「嗯？」"
    window hide
#SE_VOLC 1,255
#BG_SET_BACK 
#ROUTINE_STA
#BG_PRIC 0
#CHR_PRIC 0
#BG_INIC 1
#BG_PRIC 1
    show expression "img/NIMG01B@2x.png" as bg1 zorder 1 with dissolve
#EFF_PRI 0
#EFF_PRI 1
#EFF_STAC 0,CLOUD_B,EFF_NOSKIP
#EFF_STAC 1,LENSFLARE_SKY,EFF_NOSKIP
#ROUTINE_STP
#ROUTINE_STA
#BG_BLUR 2
#BG_BLUR 0
#BG_ALP_AUTOC 0,0,0,1
#BG_ALP_AUTOC 2,0,0,1
#CHR_ALP_AUTOC 0,0,0,1
#ROUTINE_STP
    "强烈的阳光和从海上吹来的风所注视的这个夏天，马上也要过去了。"
    "不经意间，一阵风吹过，风中已经带着少许秋天的凉意。"
    "和变迁的季节一样，我们也还会继续改变吧。"
    "偶尔也会回头，也会有所反复。"
    window hide
#SE_VOLC 1,
#ROUTINE_STA
#BG_ALP_AUTOC 0,128,0,1
#BG_ALP_AUTOC 2,128,0,1
#CHR_ALP_AUTOC 0,128,0,1
#ROUTINE_STP
    hide bg1 with dissolve
#ROUTINE_STA
#EFF_STPC 0,EFF_NOSKIP
#EFF_STPC 1,EFF_NOSKIP
#BG_BLUR 0
#EFF_PRI 0
#EFF_PRI 1
#BG_PRIC 0
#BG_PRIC 1
#CHR_PRIC 0
#ROUTINE_STP
    "但是，唯独与智纱的关系，只会不断地向前吧。"
    "不着急，慢慢地来。"
    window hide
    stop sound fadeout 1
#BG_SET_BACK 
#BG_INIC 1
#IF F103!0, GOTO IF_ELSE4
    if F103:
        jump NCH11A_IF_ELSE4
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH12A")]=True
    show expression "img/EVN_CH12A@2x.jpg" as bg1 zorder 100 with dissolve
    jump NCH11A_IF_END4
label NCH11A_IF_ELSE4:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH12B")]=True
    show expression "img/EVN_CH12B@2x.jpg" as bg1 zorder 100 with dissolve
label NCH11A_IF_END4:
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NCH11A_CH005"
    智纱 "「最喜欢你了」"
    window hide
#MUS_VOL 255
#IF F103!0, GOTO IF_ELSE5
    if F103:
        jump NCH11A_IF_ELSE5
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH12C")]=True
    show expression "img/EVN_CH12C@2x.jpg" as bg1 zorder 100  with dissolve
    pause
    jump NCH11A_IF_END5
label NCH11A_IF_ELSE5:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH12D")]=True
    show expression "img/EVN_CH12D@2x.jpg" as bg1 zorder 100 with dissolve
    pause
label NCH11A_IF_END5:
    pause (128/32.0)
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1,128,COL_WHITE
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop se
    stop sound
    stop music fadeout 1
#BG_SET_DEFC 0,BG_WHITE
#FADE_IN 0
    pause (96/32.0)
    if F103:
        jump L_FIN_01
#IF F103!0, GOTO L_FIN_01
label L_FIN_00:
#FIN_DSP EVN_CH12E
    scene expression "img/EVN_CH12E-568h@2x.jpg"
    with dissolve
    pause
    jump L_FIN_09
label L_FIN_01:
#FIN_DSP EVN_CH12F
    scene expression "img/EVN_CH12F-568h@2x.jpg"
    with dissolve
    pause
label L_FIN_09:
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#SETACHIEVE 27
    $ renpy.end_replay()
    return
#label THREAD_QUA_WIN
#TH_QUAKE_WIN 4
#EOT