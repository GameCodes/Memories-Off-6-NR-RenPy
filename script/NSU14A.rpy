label NSU14A:
    $currentlabel = "NSU14A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '30'
    $date = '0'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/NIMG02D@2x.jpg" as bg0 zorder 0 with dissolve
    play sound "SE05_16L"
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
#SE_VOLC 1,64
    志雄 "「唔……」"
    "突然觉得口干舌燥。"
    "深夜时分，周围一片漆黑。"
    "逛完夏祭回到旅馆后，由于白天玩过头了，我们两人都很快进入了梦乡。"
    "看了一下手机，已经两点多了。"
    "意识一下子清醒过来，感觉到浑身的酸痛。"
    "或许是许久没有游泳的缘故吧，肌肉也开始罢工了。明天，会很难受吧……"
    志雄 "「……嗯？」"
    "旁边的被褥里，没有见到铃的身影。"
    志雄 "「咦……？」"
    show expression "img/BG63NA8@2x.jpg" as bg_over zorder 2 with dissolve
    "仔细看去，我发现隔壁厢房的拉门紧闭着。"
    "透过中间的一点缝隙，可以看到铃的身影。"
    window hide
    play sound "SE06_24"
    "好像是在工作吧。"
    "从拉门的缝隙中，可以看见铃正坐在椅子上，膝上放着笔记本电脑。"
    志雄 "「铃」"
    "小声呼唤她，不过没有反应。"
    "仔细看去，她戴着耳机，身体还不时随着节奏晃动。"
    "原来如此，平时也是这样来集中精力的么。"
    "如此看来，确实是在工作吧。说是取材旅行我还以为是开玩笑。"
    stop se
    voice "NSU14A_SU000"
    铃 "「啊～～」"
    "过了一会儿，铃像头疼一般地挠起头，开始烦恼起来。"
    voice "NSU14A_SU001"
    铃 "「呼……」"
    "盘起腿，用手托着腮。"
    "好像在烦恼什么，没关系吗？"
    "有什么我能帮上忙的就好了……想到这，我正要起身过去时，铃啪地一下拍了自己的脸。"
    voice "NSU14A_SU002"
    铃 "「嗯，好吧」"
    window hide
    play sound "SE06_25"
    "或许是在想着什么，铃以极强的气势敲打起键盘。"
    "仔细想想，铃工作时的样子我还是头一次看到呢……"
    stop se
    voice "NSU14A_SU003"
    铃 "「呵呵」"
    "这次又突然笑了起来……。"
    "到底在写着什么呢？"
    voice "NSU14A_SU004"
    铃 "「这里……」"
    "在自己印象中铃应该是一副冷静工作的样子，没想到意外的情感外露呢。"
    "一会儿这样一会儿那样，很是有趣呢。"
    "不过，还是别打扰她比较好吧。"
    window hide
    stop se fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with None
#BG_UVC 0,0,0,640,448
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    stop se
#FADE_IN 0
    "我去旅馆的前厅买了茶和罐装的咖啡，将咖啡放到厢房门前就回来了。"
    志雄 "「辛苦了……」"
    "总是能看到她的优秀之处……"
    "浮现在脑海中的，是在月光中与键盘苦战着的铃的样子……"
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
    $ renpy.end_replay()
    return