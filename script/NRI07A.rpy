label NRI07A:
    $currentlabel = "NRI07A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '27'
    $date = '4'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 0,CAL_0727
    show expression "img/NIMG15E-568h@2x.jpg" as cal zorder 5
    show expression "img/07_27_THURSDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG17NA@2x.jpg" as bg0 zorder 0 with dissolve
#FADE_IN 0
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "就这样，到了旅行的前一天——"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128
    scene expression "img/BG17NA@2x.jpg" as bg0 with dissolve
#CHR_SORT 0,1,2
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC03"),"True","img/RI_MCC03A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA03"),"True","img/FU_MAA03A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
    with dissolve
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,RI_MXC03,3,F24
#FADE_IN 1
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#REEK_CHR 0
    voice "NRI07A_RI000"
    莉莉丝 "「诶诶——？」"
#THREAD_STP 1
#BG_ALP 3
    window hide
    play music  "OBGM15"
    "莉莉丝声音回响在已经关门了的小店里。"
    "然而，不只是她，我的心情也和莉莉丝一样。"
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#REEK_CHR 0
    voice "NRI07A_RI001"
    莉莉丝 "「婆婆不能去了吗！？」"
#THREAD_STP 1
    hide bg3 with dissolve
#BG_PRI 3
    voice "NRI07A_FU000"
    富美子 "「对不起。明天或后天，有一个老朋友要来。」"
    voice "NRI07A_FU001A"
    富美子 "「他现在住在离这里很远的地方，来一次非常难得。」"
    voice "NRI07A_FU001B"
    富美子 "「这家店开张时也颇受他照顾，所以一定要好好招呼他一番呢。」"
    志雄 "「可是，这次旅行原本就是邀请富美子婆婆的吧？您要是不去的话……」"
    "我向莉莉丝的方向瞥了一眼。"
    志雄 "「要不要把旅行延期吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC04"),"True","img/RI_MCC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI07A_RI002"
    莉莉丝 "「诶……」"
    志雄 "「因为不可能只有我们两个人去吧？何况只是延期而已，又不是中止」"
    志雄 "「把旅行定在别的日期，应该没关系吧？」"
    voice "NRI07A_FU002"
    富美子 "「嗯。旅馆的朋友说随时都可以去，所以没关系。不过……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA05"),"True","img/RI_MCA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI07A_RI003"
    莉莉丝 "「唔唔……」"
    "莉莉丝皱起了眉头，一副不能接受的样子。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA04"),"True","img/RI_MCA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI07A_RI004"
    莉莉丝 "「但是，像这样说是延期，最后却中止的情况很多呀。」"
    志雄 "「可是……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCD03"),"True","img/RI_MCD03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI07A_RI005"
    莉莉丝 "「志雄……不想去吗？」"
    志雄 "「不，不是这样……可是，这次本来就是打算和富美子婆婆一起的家族旅行，不是吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCD05"),"True","img/RI_MCD05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI07A_RI006"
    莉莉丝 "「嗯……没错……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA01"),"True","img/RI_MCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI07A_RI007"
    莉莉丝 "「……我知道了。那这次就这样吧，之后大家再一起去吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA01"),"True","img/FU_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI07A_FU003"
    富美子 "「莉莉丝。」"
    莉莉丝 "「……？」"
    voice "NRI07A_FU004"
    富美子 "「你最近一直很期待的吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC05"),"True","img/RI_MCC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI07A_RI009"
    莉莉丝 "「呃……算是吧……」"
    voice "NRI07A_FU005"
    富美子 "「你也帮了我不少忙，而且晚上也学习到很晚。」"
    voice "NRI07A_RI010"
    莉莉丝 "「那个，我平时也是这样的……」"
    "帮店里的忙也就算了，平时总是学习？那必然是假的。"
    "不过……莉莉丝这家伙，这么期待这次旅行吗。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA06"),"True","img/FU_MAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI07A_FU006"
    富美子 "「志雄怎么样？」"
    stop music fadeout 1128
    志雄 "「我……」"
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    menu:
        "我很期待":
            $F7=0
        "让莉莉丝决定":
            $F7=1
    if F7==0:
        jump L_NRI07A_SEL00_A
    if F7==1:
        jump L_NRI07A_SEL00_B
label L_NRI07A_SEL00_A:
    "是呢……老实说，我也很期待。"
    "在陌生的地方，不知道会发生什么事的这种神秘感……"
    "而且，了解莉莉丝现在想要什么，着也是迫在眉睫的事情。"
    志雄 "「是呢……有些遗憾了。」"
    jump L_NRI07A_SEL00_X
label L_NRI07A_SEL00_B:
    $F0-=1
    "不管怎么说……这次的旅行基本都是莉莉丝和富美子婆婆在张罗的。"
    "如果考虑到升学，现在根本不是应该去旅行的的时候。"
    "可是……"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCD03"),"True","img/RI_MCD03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#CHR_PRIC 0
#BG_BLUR 0
#CHR_BLUR 1
    莉莉丝 "「…………」"
    "莉莉丝的眼睛，我知道那是正在传达着忍耐之意的眼神。"
    "富美子婆婆一定也知道吧。"
    "所以才要询问我的意见吧。"
    "那么……我的回答必须是……"
    window hide
#BG_BLUR 0
#CHR_BLUR 1
#CHR_PRIC ID_ALL
    志雄 "「……我也很期待，有些遗憾呢。」"
    jump L_NRI07A_SEL00_X
label L_NRI07A_SEL00_X:
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA01"),"True","img/FU_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI07A_FU007"
    富美子 "「那么就这么决定了，这次还是你们两个去吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC03"),"True","img/RI_MCC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM13"
    志雄 "「诶？可是……」"
    "我们还都未成年，没有家长陪同在外留宿的话……就算是朋友，旅馆那边会借房子给我们吗？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA02"),"True","img/FU_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI07A_FU008"
    富美子 "「那个你不用担心。」"
    "富美子婆婆露出了有些恶作剧般的微笑。"
    "这下反倒是我一头雾水了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA01"),"True","img/FU_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI07A_FU009"
    富美子 "「总之旅馆那边由我负责联系，你们明天就去吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCB01"),"True","img/RI_MCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI07A_RI012"
    莉莉丝 "「真的可以吗！？」"
    "莉莉丝的表情一下子开朗了起来。"
    "这家伙果然十分期待呢。"
    志雄 "「可是……嗯……」"
    "富美子婆婆的笑脸把我的不安一扫而尽。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA02"),"True","img/FU_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI07A_FU010"
    富美子 "「不用担心，我已经想好办法了。」"
    志雄 "「……？」"
    voice "NRI07A_FU011"
    富美子 "「没事的，没事的。」"
    "面对着心里没底的我，富美子婆婆的口气十分明快有力。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA01"),"True","img/FU_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI07A_FU012"
    富美子 "「莉莉丝，还有志雄，你们就尽情享受吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCD01"),"True","img/RI_MCD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI07A_RI013"
    莉莉丝 "「嗯！我们会带特产回来的！」"
    "富美子婆婆似乎是有意想要打发我们走的感觉……还有，『已经想好办法了』，究竟是什么意思呢……"
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
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT