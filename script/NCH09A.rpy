label NCH09A:
    $currentlabel = "NCH09A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    show expression "img/BG78AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG78AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_18L"
    pause (32/32.0)
##FADE_IN 1
    play music "OBGM14"
#label START
    $month = '07'
    $day = '29'
    $date = '6'
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
#THREAD_STA 1,THREAD_KYORO0
#MES "我环视四周。"
    "我环视四周。"
#THREAD_WAT 1
#THREAD_STA 1,THREAD_KYORO1
#MES "在哪里？"
    "在哪里？"
#THREAD_WAT 1
#THREAD_STA 1,THREAD_KYORO2
#MES "小狗的主人在哪里！？"
    "小狗的主人在哪里！？"
#THREAD_WAT 1
#MESX "%K%P"
    "在小溪边上有几个人在钓鱼，也注意到了顺流漂走的小狗。可是，谁也没有跳下去。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDC02"),"not F103==0","img/CH_MNC02A@2x.png","True","img/CH_MDC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "我斜眼看了下智纱。她已经快要哭出来了。"
    "……只能让我上了！"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_GET_NOC 0,F26
#BG_SET_BACK 
#BG_INIC 2
#BG_UVC 2,(640/4),(448/4),(640/2),(448/2)
#BG_UV_AUTOC 0,((640/8)*3),((448/8)*3),(640/4),(448/4),1,F123,48
    pause (24/32.0)
#BG_ALP_AUTOC 0,0,0,F25,24
#BG_SWPC 0
    hide bg2 with dissolve
#BG_PRI 0
#BG_PRI 2
#BG_UVC 2,0,0,640,448
#BG_POSC 2,0,0,640,448
#BG_ALPC 2
    "下定了决心，向着小溪的方向迈出一步——。"
    stop music fadeout 1
#SE_VOLC 1
    play sound "SE03_52"
    "哎？"


    "突然，在下游的方向上听到了跳进水里的声音。我反射性地转向声音传来的方向。"
    "听到了「有人跳进水里了！？」、「危险啊！」的喧闹声。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDA03"),"not F103==0","img/CH_MNA03A@2x.png","True","img/CH_MDA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
#REEK_CHR 0
    voice "NCH09A_CH000"
    智纱 "「那是，那只狗的主人？」"
#REMOVE_REEK_CHR 0
    志雄 "「也许是吧……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "在水面上，看见一个向着被冲走的小狗游过去的青年。"
    "他用一种很保险的方式游了过去，抱住了小狗，游回了岸边。"
    window hide
    play music "OBGM29"
    play sound "SE09_29"
    犬 "「汪！　汪！」"
    stop se
    "对着救了自己的主人，小狗开始嬉闹起来。"
    "看它那精神劲，根本不像是刚才溺水时候的样子了。这家伙，知道自己刚才差一点死了吗？"
    "真是的，天真的家伙……。"
    window hide

    play sound "SE03_47"
#BG_SWPC 0
#BG_PRI 1
#BG_PRI 0
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,(640/4),(448/4),((640/4)*3),((448/4)*3)

#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNC03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDC03"),"not F103==0","img/CH_LNC03A@2x.png","True","img/CH_LDC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    hide bg1 with dissolve
    "看到了那只小狗，智纱顿时放松了下来，一屁股坐到了地上。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDC01"),"not F103==0","img/CH_LNC01A@2x.png","True","img/CH_LDC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH09A_CH001"
    智纱 "「太好了……。没事了」"
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
#label THREAD_KYORO0
#BG_UV_AUTOC 0,0,(448/4),(640/2),(448/2),1,F123
#BG_UV_SAVEC 0
#EOT
#label THREAD_KYORO1
#BG_UV_AUTOC 0,(640/2),(448/4),(640/2),(448/2),1,F123
#BG_UV_SAVEC 0
#EOT
#label THREAD_KYORO2
#BG_UV_AUTOC 0,(640/4),(448/4),(640/2),(448/2),1,F123
#BG_UV_SAVEC 0
#EOT