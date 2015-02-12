label NSU21A:
    $currentlabel = "NSU21A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '08'
    $day = '20'
    $date = '0'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 4,CAL_0820
    show expression "img/NIMG15G-568h@2x.jpg" as cal zorder 5
    show expression "img/08_20_SUNDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG15MA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression Solid("000") with None
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
    "那之后我回到旅馆，和铃再次相见……"
    "在采纳了稻穗君的建议，与铃言归于好后，第二天我们一起返回了澄空。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
#FADE_IN 1,128
    play music "BGM14"
    voice "NSU21A_SU000"
    铃 "「志雄，早饭做好了哟」"
    "从客厅传来了铃的声音。"
    志雄 "「啊，马上过来」"
    "之后，依然什么也没有改变了。"
    show expression "img/EXBG09A@2x.jpg" as bg_over zorder 5
    show expression "img/SU_ZDB01A@2x.png" as lh0 zorder (10+0):
        xcenter ((320)/640.0)
    with dissolve
    "吃过铃准备的早饭，继续准备学生会的工作和考试。"
    "就像夏天下过的雨一样，没留下任何痕迹，关于旅行的回忆也被日常的生活所淹没……"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1,128
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop se
    stop sound
    stop music fadeout 1
#FADE_IN 0
#MOV_PLY 6
#FADE_OUT 0
#FADE_IN 0
    $ renpy.end_replay()
    return