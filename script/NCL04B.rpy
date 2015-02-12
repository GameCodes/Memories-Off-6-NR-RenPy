label NCL04B:
    $currentlabel = "NCL04B"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '31'
    $date = '1'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_BG NIMG15I,CAL_0731
    show expression "img/NIMG15I-568h@2x.jpg" as cal zorder 5
    show expression "img/07_31_MONDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG81EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG81EA@2x.jpg" as bg0 with dissolve
    play sound "SE05_13L"
    pause (32/32.0)
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
    pause (32/32.0)
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 2
#BG_PRI 0
#BG_UVC 2,(640/4),(448/4),(640/2),(448/2)
#BG_SETWC 0,2,BG82EA,BG82EA
    scene expression "img/BG82EA@2x.jpg" as bg0 with dissolve
    play sound "SE06_29L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,64
    voice "NCL04B_KU000"
    克罗艾 "「……唉」"
    "到底，该怎么办才好。"
    "这里，是我的家。"
    "这里，是我和我家人的家。"
    "这里，是我被安置于此的，家。"
    "这里，是我被弃之不顾的，家。"
    "……"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA03"),"True","img/YS_MAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04B_EL000A"
    爱丽丝 "「克罗艾……」"
    voice "NCL04B_KU001B"
    克罗艾 "「啊，妈妈……」"
    voice "NCL04B_KU001C"
    克罗艾 "「妈妈，我稍微……出去一下。顺路去下爸爸那里……」"
    "我的脸上，现在究竟是一副怎样的表情呢。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA02"),"True","img/YS_MAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04B_EL002"
    爱丽丝 "「这样啊。你什么时候回来呢？今天想做克罗艾你最喜欢吃的东西呢。」"
    play sound "SE07_02"
#CHR_INIC 1
#CHR_ALPC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA02"),"True","img/YS_LAA02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#ROUTINE_STA
#BG_ALP_AUTOC 0,0,1,F24
#BG_UV_AUTOC 2,(640/5),(448/5),((640/3)*2),((448/3)*2),0,1,16
#CHR_ALP_AUTOC 0,0,1,F24
#CHR_ALP_AUTOC 1,128,1,F24
#ROUTINE_STP
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NCL04B_KU003"
    克罗艾 "「！？」"
#MESEX_A M_NOA,A_CH_KU,NCL04B_KU003,"【クロエ】「！？」"
#THREAD_WAT 1
#MESX "%K%P"
    window hide
#ROUTINE_STA
#CHR_ALP_AUTOC 0,128,1,F24
#CHR_ALP_AUTOC 1,0,1,F24
#BG_ALP_AUTOC 0,128,1,F24
#ROUTINE_STP
    hide bg2 with dissolve
    hide lh1 with dissolve
#CHR_ALPC 1,128
#BG_PRI 0
    voice "NCL04B_KU004"
    克罗艾 "「那个，今天，已经太晚了……我想。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA03"),"True","img/YS_MAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04B_EL003"
    爱丽丝 "「也是……那明天做给你吃吧，好吗？」"
    "事到如今，我该怎么办才好。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04B_EL004"
    爱丽丝 "「哎，克罗艾？晚饭——」"
    voice "NCL04B_KU005"
    克罗艾 "「事、事、事到……如今——」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA06"),"True","img/YS_MAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    爱丽丝 "「！？」"
#MESEX_A M_NOA,A_CH_EL,NCL04B_EL005,"【エリーズ】「！？」%K%P"
    window hide
#SE_VOLC 1,128,16
#FADE_OUT 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    scene expression Solid("000") with None
    "事到如今……？"
    "我，现在到底在说些什么啊！？"
    voice "NCL04B_KU006"
    克罗艾 "「我、我……我走了！」"
    window hide
    stop sound
    play sound "SE00_16"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
##FADE_OUT 1,128
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop se
    stop sound
    stop music fadeout 1
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_SHOCK
#BG_ALP_AUTOC 0,0,1,F123,16
#CHR_ALP_AUTOC 0,0,1,F123,16
#BG_UV_AUTOC 2,(640/8),((448/8)+512),(640-640/4),(448-448/4),1,F123,16
#CHR_SCL_AUTOC 1,256,256,1,F123,16
#CHR_POS_AUTOC 1,1,F123,16
#BG_ALP_SAVEC 0
#CHR_ALP_SAVEC 0
#BG_UV_SAVEC 2
#CHR_SCL_SAVEC 1
#CHR_POS_SAVEC 1
#EOT