label NSU20A:
    $currentlabel = "NSU20A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '04'
    $day = '27'
    $date = '5'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 4,CAL_0427
#FADE_OUT 1,32,COL_WHITE
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG01AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG01AA@2x.jpg" as bg0 with dissolve
    play sound "SE08_17L"
#FADE_IN 1,128
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
#SE_VOLC 1,128
    "——在那以后，过了差不多半年时间。"
    "在熟悉的澄空的街道上，伴随着春天的结束，预示着崭新的季节到来的风，吹起来了。"
    voice "NSU20A_X0000"
    友人Ａ "「喂，塚本，黄金周准备做什么呢？」"
    志雄 "「唔～」"
    voice "NSU20A_X1000"
    友人Ｂ "「要去社团什么的吗？」"
    志雄 "「还没决定社团呢」"
    voice "NSU20A_X0001"
    友人Ａ "「你也没有女朋友吧？」"
    voice "NSU20A_X1001"
    友人Ｂ "「同为寂寞的同志们，去哪里玩好呢～」"
    志雄 "「等等！在这点上别把我跟你们相提并论啊！」"
    voice "NSU20A_X1002"
    友人Ｂ "「喂喂塚本～，真薄情啊～」"
    window hide
    stop music fadeout 1
    play sound "SE06_14L"
    "熟悉的引擎声逐渐逼近。"
    "刚刚还发邮件问她在哪里，我还在想她会不会来……"
    window hide
    stop se
#SE_WATC 0
    play sound "SE06_13L"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SCB01"),"True","img/SU_SCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE03_90"
    play music "BGM05"
    voice "NSU20A_SU000"
    铃 "「到啦到啦！耶！」"
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
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    志雄 "「铃！稿子写完了吗？」"
    voice "NSU20A_SU001"
    铃 "「相当完美！昨天睡了一天，现在也恢复精神了……」"
    志雄 "「那就好。今天气色看起来不错啊」"
    "自那之后，最终，我选择了在本地大学进修。"
    "和铃的关系，依然没有大的改变……不过这一点上我倒是不太在意。"
    "只要有耐性的话，终究能够下定决心的。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA01"),"True","img/SU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU20A_SU002"
    铃 "「志雄大学放假了吧？」"
    志雄 "「嗯。总觉得大学的假期很多啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU20A_SU003"
    铃 "「那我们去旅行吧！」"
    "铃拿出了头盔。"
    "一如既往的突然啊。"
    志雄 "「好是好，也不能这样直接去啊？好歹也该拿些换洗衣服」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC01"),"True","img/SU_LCC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU20A_SU004"
    铃 "「我知道啊」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    志雄 "「那不好意思，我先走了啊。再见」"
    voice "NSU20A_X0002"
    友人Ａ "「诶？哦、哦」"
    voice "NSU20A_X1003"
    友人Ｂ "「加、加油啊」"
    window hide
    play sound "SE06_14L"
    "两人一副目瞪口呆的样子。铃的气场果然强大啊。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG14AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG14AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA01"),"True","img/SU_LCA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#BG_BLUR 0
#FADE_IN 1
    志雄 "「那我准备准备，稍等一下」"
    voice "NSU20A_SU005"
    铃 "「知道了」"
    window hide
#BG_BLUR 0
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "铃在公寓前等着。我则回到房间里，利索地收拾起行李。"
    "不过，没有直接回到她在的地方。"
    "而是去了……。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#FADE_IN 0
    play music "OBGM09"
    "终于派上用场了！"
    "在进大学的时候，我就去驾校进行了学习，考取了驾照。"
    "从那时候起为了摩托车开始攒钱，最近，终于买了自己的摩托车。"
    window hide
#FADE_OUT 0
#BG_SET_BACK 
#BG_INIC 0
#EFF_STAC 0,MOTOR_LIGHT_D,EFF_NOSKIP
    play sound "SE06_34"
    pause (32/32.0)
#FADE_IN 1
    scene expression "img/motor_day@2x.png" as motor_light_n_eff:
    show expression "img/NIMG12A@2x.jpg" as motor_light_n_eff_road zorder -1:
        block:
            yanchor 1.0
            ypos 0.0
            linear 0.3 ypos 1.0
            repeat
    show expression "img/NIMG12A@2x.jpg" as motor_light_n_eff_road2 zorder -1:
        block:
            yanchor 0.0
            ypos 0.0
            linear 0.3 ypos 1.0
            repeat
    with dissolve
    "从公寓后面的停车场出来，稍微绕了一点远路，沿着公寓前的路向铃的方向开去。"
    
#EFF_STPC 0,EFF_NOSKIP
    scene expression "img/BG14AA@2x.jpg" as bg_over zorder 2 with dissolve
    志雄 "「喂！铃！」"
    "铃回过头，瞪大了眼睛看着我。"
    志雄 "「嘿嘿，吃惊吧」"
    "就这样不慌不忙地走向她，用左手打出胜利的手势。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU11A")]=True
    scene expression "img/EVN_SU11A@2x.jpg" as bg1 zorder 1 with dissolve
    stop sound fadeout 1
    play sound "SE06_33"
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
    志雄 "「一起骑吧！约定好的啊？」"
    "铃噗哧地笑了出来，回以相同的胜利手势。"
    voice "NSU20A_SU006"
    铃 "「ＯＫ，走吧！」"
    "于是我们乘着相同的风，感受着相同的热量，以相同的速度开始行驶。"
    "没错……从今以后永远……"
    "我们，一起奔驰下去。"
    window hide
#MUS_VOL 255
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU11B")]=True
    show expression "img/EVN_SU11B@2x.jpg" as bg1 with dissolve
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
    scene expression "img/EVN_SU11C-568h@2x.jpg" with dissolve
    pause 
#FIN_DSP EVN_SU11C
    pause (256/32.0)
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
    $ renpy.end_replay()
    return