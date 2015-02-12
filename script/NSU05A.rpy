label NSU05A:
    $currentlabel = "NSU05A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '22'
    $date = '6'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 4,CAL_0722
    show expression "img/NIMG15G-568h@2x.jpg" as cal zorder 5
    show expression "img/07_22_SATURDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG33AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG33AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDA01"),"True","img/SU_MDA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE03_21L"
    pause (32/32.0)
#FADE_IN 1,128
    play music "BGM05"
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
    志雄 "「铃，说起来」"
    "像往常一样，两人吃过饭后，一起收拾着餐具。"
    voice "NSU05A_SU000"
    铃 "「嗯？」"
    志雄 "「昨天邮件里说的事情」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDB01"),"True","img/SU_MDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU001"
    铃 "「啊，是今晚呢。嗯，时间没问题吧。不过，你打算去哪儿呢？」"
    "铃一边洗着餐具一边问道。"
    "如此说来，邮件里什么也没有写，只是问了问今晩是不是有时间。"
    "难道是铃……忘记了今天有焰火大会？"
    if not persistent.dictlist[30] and persistent.show_dict:
        $persistent.dictlist[30]=True
        show screen dict_pop(i=30)
    志雄 "「去芦鹿岛吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDA04"),"True","img/SU_MDA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU002"
    铃 "「唔，去做什么？」"
    "铃歪着头，一脸迷茫的表情。"
    "怎么办，我应该一五一十告诉她吗？"
    志雄 "「今天……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    with dissolve
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XDC05"),"True","img/SU_XDC05A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NSU05A_SU003"
    铃 "「等一下！」"
    "铃用湿漉漉的手捂住了我的嘴巴。"
    志雄 "「……嗯？？」"
    "本来被堵住的嘴巴似乎还可以发声，谁料铃想都没想，伸出剩下的食指，堵住了我的嘴巴。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XDC01"),"True","img/SU_XDC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU004"
    铃 "「好不容易有件让人期待的事情。如果可以的话，到地点后再给我惊喜好么。现在就不用说了」"
    "看到我点点头，铃这才把手松开。也不是什么特别的秘密啊。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDB02"),"True","img/SU_LDB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU005"
    铃 "「总觉得这样期待着，工作也有干劲呢！」"
    志雄 "「拜托你了，老师」"
    "在过于普通的日子里，能找到自己期待的事情，让人羡慕呢。"
    "这就是作为大人的铃所拥有的技艺吧……好，我来学习学习吧。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    play sound "SE03_41"
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/OIBG012A@2x.png" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDA01"),"True","img/SU_MDA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (32/32.0)
#FADE_IN 1
    voice "NSU05A_SU006"
    铃 "「那么，晚上见了」"
    if not persistent.dictlist[41] and persistent.show_dict:
        $persistent.dictlist[41]=True
        show screen dict_pop(i=41)
    志雄 "「嗯。啊，会合地点，芦鹿岛车站……不是，在水族馆前六点半吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDA02"),"True","img/SU_MDA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU007"
    铃 "「咦？不一起去吗？」"
    志雄 "「嗯，我得出去一下，然后从那边直接过去」"
    "……事实上，没有什么特别的事情。"
    "只是，与其从家里一起过去，在约会地点等的话更有约会的感觉吧。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDB01"),"True","img/SU_MDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU008"
    铃 "「这样啊。行，我知道了」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    with dissolve
    play sound "SE00_01"
    "好极了。首先约会的邀请成功了。"
    "总觉得自己太过于期待了，希望晚上的焰火大会一定要顺利啊。"
    window hide
    stop music
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG38EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG38EA@2x.jpg" as bg0 with dissolve
    play sound "SE08_17L"
    pause (32/32.0)
#FADE_IN 1
    "天已经黑了，芦鹿岛沉浸在一片暮色中。"
    "尽管如此，因为焰火大会的缘故，人却逐渐多了起来，让芦鹿岛的夜晚现出了生气。"
    志雄 "「是不是有点早呢？」"
    "手机上的时钟显示着现在时间是下午六点。"
    "因为有着在学生会一起行动时的习惯，就来得早了一些。如果是学生会的集合的话，这会人也应该到的差不多了……"
    志雄 "「铃她似乎很忙，晚点过来也是有可能的」"
    "我一面望着从车站涌向芦鹿岛的人群，一面摆弄着手机。"
    "总觉得，这样等着很让人紧张呢。"
    "诶？"
    "这样一来，确实会有约会的感觉呢……变得怦然心动了。"
    voice "NSU05A_TO000"
    亨 "「喂～，志雄～！」"
    "从人群中传来某个熟悉的声音。不用想也知道不是我等的人。"
    voice "NSU05A_TO001"
    亨 "「志雄！不要无视我啊～」"
    "可能的话倒是想无视掉呢。只是人就站在眼前，很难做到啊。"
    "这样下去会影响到和铃的碰面呢。"
    window hide
#SE_VOLC 1,64
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "BGM09"
    志雄 "「你在这里做什么啊？」"
    voice "NSU05A_TO002"
    亨 "「当然是来看焰火大会的啊」"
    "亨理所当然般地作答。"
    志雄 "「一个人吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_TO003"
    亨 "「呵呵～，不会是那样的吧？　Ｍｒ．塚本」"
    "亨晃着手指在那边装腔作势。别用这种奇怪的称呼方式啊。"
    志雄 "「和乐队的朋友吗？」"
    voice "NSU05A_TO004"
    亨 "「Ｎｏ。顺便再说一句也不是班上的男生」"
    "说到亨还有可能会叫的人……"
    "不会吧？"
    志雄 "「我说，难道是，真的？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_TO005"
    亨 "「呵呵。对了！不通过你，一样可以约到莉莉丝！」"
    志雄 "「真的呀！？」"
    "虽然这样说很对不起亨，不过莉莉丝和他一起来看焰火，真是无法想像。"
    "莫非是天气太热让我产生了幻觉？"
    志雄 "「这、这真是太好了……」"
    voice "NSU05A_TO006"
    亨 "「噢！今天对我来说，可是特别的一天！」"
    "亨突然欢欣雀跃起来。在他身后，熟悉的一群人走了过来。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,640
#CHR_COLC 1,128,120,112,128
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA03"),"True","img/RI_MBA03A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter 0.75
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter 0.25
    with move
#MOV_CHR_INIT 64
#MOV_CHR0 ,(320-160)
#MOV_CHR1 128,(320+160)
#MOV_CHR_GO 1
    voice "NSU05A_RI000"
    莉莉丝 "「哇。莫非你也和人约在这里？」"
    志雄 "「是啊。这里最好找嘛……」"
    "回过头一看，不仅是莉莉丝，箱崎和春日都来了。"
    "不是亨和莉莉丝两个人啊。这我就能理解了。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
#CHR_COLC 0,128,120,112,128
#CHR_COLC 1,128,120,112,128
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA01"),"True","img/CH_MBA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBB01"),"True","img/YU_MBB01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NSU05A_CH000"
    智纱 "「晚上好，塚本君」"
    voice "NSU05A_YU000"
    结乃 "「辛苦了，学长」"
    志雄 "「是这样啊。大家一起来的啊」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA01"),"True","img/YU_MBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NSU05A_YU002"
    结乃 "「不不，我是途中和大家碰上的。和朋友约好了她还在等我，先失陪了」"
    志雄 "「是这样啊。人很多相当拥挤呢，自己小心啊」"
    window hide
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA02"),"True","img/YU_MBA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    hide lh1 with dissolve
    play sound "SE01_04L"
#SE_VOLC 0,96
    pause (16/32.0)
    stop se fadeout 1
    "我像个老师一样提醒她。春日苦笑着点点头离开了。"
    window hide
#MOV_CHR_INIT 64
#MOV_CHR0 ,(320)
#MOV_CHR_GO 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA01"),"True","img/CH_MBA01A@2x.png") as lh0 zorder (10+0):
        xcenter .5
    with move
    志雄 "「箱崎也常来的吗？」"
    "莉莉丝和亨常来参加，这个我是知道的。"
    "不过，到去年为止，基本上都是和我一起来的……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBB01"),"True","img/CH_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_CH002"
    智纱 "「我很久没有好好欣赏焰火大会了呢」"
    voice "NSU05A_CH003"
    智纱 "「要不是莉莉丝执意要我来的话，今年也不会来呢」"
    志雄 "「是这样啊。住这一带的话，不来还是有点遗憾呢」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA04"),"True","img/CH_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_CH004"
    智纱 "「从塚本君的公寓看不到吗？」"
    志雄 "「倒也不是看不见」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_COLC 1,128,120,112,128
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC04"),"True","img/RI_MBC04A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA04"),"True","img/CH_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with move
#MOV_CHR_INIT 64
#MOV_CHR0 ,(320+96)
#MOV_CHR1 128,(320-96)
#MOV_CHR_GO 1
    voice "NSU05A_RI001"
    莉莉丝 "「从楼顶是能看到，只是看起来小得可怜」"
    志雄 "「天空清澈与否，看到的景色也不尽相同呢。无论怎样，还是近处看到的好啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA01"),"True","img/CH_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NSU05A_CH005"
    智纱 "「原来如此」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC01"),"True","img/RI_MBC01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NSU05A_RI002"
    莉莉丝 "「不过要是从学校的楼顶上看，能看到的话还是会很开心呢」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBB02"),"True","img/CH_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NSU05A_CH006"
    智纱 "「大家聚在一起看的话确实很好呢」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC02"),"True","img/RI_MBC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NSU05A_RI003"
    莉莉丝 "「是啊～」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「亨……通向特别的一天的路看起来还很漫长啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA04"),"True","img/TO_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_TO009"
    亨 "「话说回来，你又怎么样呢。在这个地方一个人站着」"
    志雄 "「我在等人啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_TO010"
    亨 "「啊，是那个年长一点的女朋友吗」"
    志雄 "「嗯，是啊」"
    voice "NSU05A_TO011"
    亨 "「那辆大型摩托车不错啊」"
    志雄 "「嗯？你对摩托车也有兴趣了？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_TO012"
    亨 "「说什么呢。别看我这个样子，摩托车的驾照我已经拿到了哦」"
    志雄 "「诶！？什么时候的事啊？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_TO013"
    亨 "「不仅如此，我经过努力打工挣钱，没过多久连爱车都到手了！」"
    "你傻啊你！"
    "这家伙一点毕业生的自觉都没有啊……"
    志雄 "「亨，不要说这些不着调的话了，多多少少该学习了啊……」"
    "亨要是看到之前考试成绩的话，现在就会和莉莉丝一样闷不做声了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_TO014"
    亨 "「就是因为这个才减少打工时间的啊。还是不够的话就只好向家里借了」"
    志雄 "「家里居然没生气啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_TO015"
    亨 "「……不，确实生气了。因为这个，暑假才不得不去参加预备校的的夏季讲座呢。也就因为这个我暑假都没有时间玩了」"
    "话是这样没错。不过，能买辆摩托车的话，多多少少会让人羡慕吧。"
    "我也在想要是最近能拿到驾照，和铃一起兜风该多好啊。"
    志雄 "「那你准备买什么样的车呢？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_TO016B"
    亨 "「２２５的街头摩托车……」"
    志雄 "「啊～，是那种在老款基础上装了加载轮胎的么」"
    voice "NSU05A_TO017"
    亨 "「没错没错。不过，太普通了点，我想攒钱改装呢～」"
    "亨看上去兴致颇高，把诸如这款车的时尚度高、可定制突出等优点都向我们宣传了一遍。"
    "……不过说实话，听完还是一知半解。"
    志雄 "「话虽如此，也要好好学习啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_TO018"
    亨 "「知道啦。不过，你对摩托车也挺清楚的嘛」"
    志雄 "「嗯……我也只是偶尔看一下这方面的杂志而已」"
    voice "NSU05A_TO019"
    亨 "「呵呵，是为了能和女朋友有话题聊吧」"
    "嗯，正是如此。"
    "铃对她所钟爱的摩托车话题总是乐此不疲，偶尔我会把她房间里放着的摩托车杂志借来看。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_TO020"
    亨 "「手段看起来很高明啊」"
    志雄 "「唔……勉勉强强吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA04"),"True","img/TO_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_TO021"
    亨 "「可恶，为什么你总是能进行得这么顺利呢？」"
    志雄 "「你现在也算是左拥右抱吧，姑且算是……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_TO022"
    亨 "「完全不同呢。话说回来，莉莉丝光是和箱崎说话啊」"
    "这个没办法吧。"
    "本来就只是箱崎和莉莉丝约好一起来的，亨你只是中途插进来的而已。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA04"),"True","img/TO_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#SET_SAVPNT
    voice "NSU05A_TO023A"
    亨 "「哼。我有什么比你差的？我本来也要加入学生会的啊，{w=5}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_TO023B"
    extend "只是学生会已经满员罢了～」"
#CLR_SAVPNT
    志雄 "「原来原因是体制方面的因素啊」"
    "幸好是满员了。亨进来的话学生会会变成什么样子，光是想想就很可怕。"
    voice "NSU05A_TO024"
    亨 "「虽说能进的话我人生的第一个受欢迎期说不定就到来……不过学生会大概不会有合适的吧」"
    "我觉得，没几个家伙会把学生会当成是个可以邂逅的地方吧。"
    "不过，去年以克罗艾学姐为目标的人确实是很多。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD01"),"True","img/RI_MBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_RI004"
    莉莉丝 "「哎，差不多该到处逛逛了吧？我想去货摊那边去转转呢」"
    "莉莉丝拿出手机看了看后说道。"
    "听她一说，我也看了看时间，已经近六点半了。"
    志雄 "「啊，已经这个时候啦」"
    "已经过了和铃约定的时间，铃却还没和我联络。"
    voice "NSU05A_RI005"
    莉莉丝 "「志雄要一起来吗？还是和别人约好在这里汇合？」"
    志雄 "「嗯。地点不明显的话，汇合会比较困难吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC05"),"True","img/RI_MBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_RI006"
    莉莉丝 "「那你是在这里等了？」"
    志雄 "「不知道怎么样了……总之我先联系一下吧」"
    window hide
    hide lh0 with dissolve
    pause (32/32.0)
    play sound "SE02_03"
    pause (32/32.0)
    play sound "SE02_03"
    play sound "SE02_02L"
    pause (8/32.0)
    stop se fadeout 1
#MUS_VOL 64,16
#FADE_OUT 1
    pause (96/32.0)
#SE_WATC 0
    pause (32/32.0)
    play sound "SE02_03"
#FADE_IN 1
#MUS_VOL 128,16
    "试着打铃的电话，铃声在响了一会儿之后便传出了请留言的信息。"
    "或许是在路上？"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD03"),"True","img/RI_MBD03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_RI007"
    莉莉丝 "「没联系上吗？」"
    志雄 "「唔。就算联系不上，也不能走掉，我还是在这里等好了」"
    voice "NSU05A_RI008"
    莉莉丝 "「这样么，那就再稍微等一下吧」"
    志雄 "「诶？大家就不用等了，先去玩吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC06"),"True","img/RI_MBC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU05A_RI009"
    莉莉丝 "「这样的话，总觉得是自己唆使大家的呢」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_COLC 1,128,120,112,128
    hide lh0
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA01"),"True","img/CH_MBA01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter 0.3
#MOV_CHR_INIT 64
#MOV_CHR0 ,(320-96)
#MOV_CHR1 128,(320+96)
#MOV_CHR_GO 1
    voice "NSU05A_CH007"
    智纱 "「怎么了吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC04"),"True","img/RI_MBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .7
    with dissolve
    志雄 "「没事，只是还没联系上对方」"
    voice "NSU05A_CH008"
    智纱 "「铃吗？」"
    志雄 "「嗯。即使会晚来，至少也该联系一下啊」"
    "铃明明是那种即使迟到，也会先联系的人啊。"
    "或许是工作还没结束，也可能是被编辑催稿也说不定……"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBC02"),"True","img/CH_MBC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .3
    with dissolve
    voice "NSU05A_CH009"
    智纱 "「她会有什么事吗？」"
    志雄 "「应该没什么事吧……」"
    "铃是骑摩托车过来的吗？一下子想到这个令自己生厌的问题。"
    voice "NSU05A_CH010"
    智纱 "「真的吗？」"
    志雄 "「唔。我想……应该没事的」"
    "铃最近太忙了，睡眠不足的话骑车会很危险的。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG38NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression Solid("000") with None
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    with dissolve
#FADE_IN 0
    "不对，如果身体状况不好的话可能会乘电车过来或者就取消了吧。但，因为太晚也有可能会考虑骑摩托车飞奔过来……"
    志雄 "「唔……应该……没事的」"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
    scene expression "img/BG38NA@2x.jpg" as bg0 with dissolve
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-96)
#CHR_POSC 1,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA06"),"True","img/RI_MBA06A@2x.png") as lh10 zorder (10-10):
        xcenter .3
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBC02"),"True","img/CH_MBC02A@2x.png") as lh1 zorder (10-1):
        xcenter .7
        ypos 0.0

#FADE_IN 1
    voice "NSU05A_RI010"
    莉莉丝 "「喂志雄，你冷静点啊」"
    志雄 "「啊，不好意思。想到些不太好的事情」"
    "一旦开始往不好的方向思考后，就无论如何都摆脱不掉这样的念头。"
    "心中的这种不安似乎在扩大，连箱崎她们也是一副担心的样子。"
    voice "NSU05A_CH011"
    智纱 "「铃是骑摩托车来吗？」"
    志雄 "「唔，这个我不知道」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA05"),"True","img/RI_MBA05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
        xcenter .3
    with dissolve
    voice "NSU05A_RI011"
    莉莉丝 "「说起来，为什么不一起过来呢？」"
    志雄 "「唔，也没什么特别的原因。与其一起从家过来，在这边先等的话气氛会比较好吧」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA06"),"True","img/RI_MBA06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
        xcenter .3
    with dissolve
    voice "NSU05A_RI012"
    莉莉丝 "「我说……不必拘泥于这种奇怪的形式吧」"
    志雄 "「没必要在意的。铃一定是工作太忙了」"
    "我故意强打起精神说道。确认时间，还差５分就７点了。约定的时间早就过了。"
    "如果只是爽约的话我倒是可以接受，可万一不是那样的话……"
    voice "NSU05A_RI013"
    莉莉丝 "「再试着联系看看吧」"
    志雄 "「对啊……」"
    "就在我慌慌张张打开手机的时候，电话通了。"
    window hide
    stop music
    play sound "SE06_15L"
    志雄 "「啊，来了？」"
    "虽然混杂着周围的喧闹声，但仍然可以听到。最初并不知道和其它的摩托车有什么不同，但那种充满爆发力的加速的机械声是无法忘却的。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC05"),"True","img/RI_MBC05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
        xcenter .3
    with dissolve
    voice "NSU05A_RI014"
    莉莉丝 "「诶？怎么了？」"
    hide lh11
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBB04"),"True","img/CH_MBB04A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
        xcenter .7
    with dissolve
    "不止是莉莉丝，箱崎和亨也注意到了。"
    志雄 "「 嗯，是铃」"
    voice "NSU05A_RI015"
    莉莉丝 "「在哪里呢？」"
#SE_VOLC 0,64
    "大家都向周围望去， 当然是看不到铃的身影的。但是摩托车引擎的声音越来越近了。"
    志雄 "「嗯～应该已经到了……看」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#SE_VOLC 0,255
    pause (32/32.0)
    stop se fadeout 1
#SE_WATC 0
    play sound "SE06_31"
    "话音刚落，从道路远处现出了铃骑着摩托车的身影。"
    "铃将车开到我们面前才熄火，摘下头盔甩甩头，头发一下子膨松地飘散开来。"
    "就像是某个电影或广告的场景。"
#CHR_INIC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC05"),"True","img/SU_LCC05A@2x.png") as lh10 zorder 100:
        ypos 0.0
    with dissolve
    play sound "SE03_90"
    play music "BGM05"
    voice "NSU05A_SU009"
    铃 "「志雄！我迟到了，对不起！」"
    "和我的眼神一交汇，铃立刻低下了头。"
    志雄 "「没事，不要紧的……发生什么事了吗？」"
    voice "NSU05A_SU010"
    铃 "「碰头会的电话拖延了时间。想联系你也没办法」"
    志雄 "「是这样啊。因为电话联系不上你，有点担心你发生了什么事」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC04"),"True","img/SU_LCC04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU011"
    铃 "「啊～，真是对不起！这个我一定会补偿你的」"
    志雄 "「这就不必了，反正没事就好。你看，放焰火的时间到了」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU012"
    铃 "「是啊。来的时候还在想为什么今天道路这么拥堵呢，原来是芦鹿岛的焰火大会啊。总算是记起来了」"
    志雄 "「完全没注意到吗？」"
    "街上到处都张贴着传单，再怎么说都会注意到的吧。"
    voice "NSU05A_SU013"
    铃 "「彻底忘干净了，幸亏最后还是赶上了。一年仅此一度，明天想来都不行了呢」"
    "这个时候，铃才注意到了我周围这群人的存在。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA03"),"True","img/SU_LCA03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU014"
    铃 "「这是？莉莉丝，你们也在呢」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_INIC 2
#CHR_SORT 0,2
#CHR_ALPC 1
#CHR_ALPC 2
#CHR_POSC 1,((320+96)+((320)/2))
#CHR_POSC 2,((320+256)+((320)/2))
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC02"),"True","img/RI_MBC02A@2x.png") as lh11 zorder (20-11):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA01"),"True","img/CH_MBA01A@2x.png") as lh2 zorder (10-2):
        xcenter .75
        ypos 0.0
    with move
#ROUTINE_STA
#CHR_POS_AUTOC 1,(320+96),F24
#CHR_ALP_AUTOC 1,128,1,F24
#CHR_POS_AUTOC 2,(320+220),F24
#CHR_ALP_AUTOC 2,128,1,F24
#CHR_POS_AUTOC 0,(320-160),F24
#BG_BLUR 0
#ROUTINE_STP
    voice "NSU05A_RI016"
    莉莉丝 "「晚上好～」"
    voice "NSU05A_CH012"
    智纱 "「晚上好」"
    "铃就这样骑在摩托车上和两人打了招呼，一副带着些歉意的表情。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC02"),"True","img/SU_LCC02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU015"
    铃 "「难道，今天大家约好见面了吗？」"
    "听到刚刚我们的对话，莉莉丝灵机一动。"
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC01"),"True","img/RI_MBC01A@2x.png") as lh11 zorder (10+9):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NSU05A_RI017"
    莉莉丝 "「不是的，我们各自分头行动」"
    志雄 "「对，刚刚偶然碰到了」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU016"
    铃 "「是这样啊。那就没有问题了」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh11
    with dissolve
#CHR_SORT 0,1
#CHR_INIC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh10 zorder 100:
        ypos 0.0
    with dissolve
    play sound "SE03_75"
    志雄 "「哇！」"
    "铃把绑在后座上的头盔递给了我。"
    window hide
    stop se
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA01"),"True","img/SU_LCA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU017"
    铃 "「那么，就把志雄借给我了啊」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    with dissolve
    志雄 "「啊，等一……」"
    "铃一见我做到后座上，立即启动了引擎。"
    window hide
    play sound "SE06_40L"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 0,(320+160)
#CHR_POSC 1,(320-160)
#CHR_POSC 2,(320)
#CHR_DSPTC 10,1,2,CH_MBA04,TO_MBB04,RI_MBA03
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA04"),"True","img/CH_MBA04A@2x.png") as lh3 zorder (10):
        ypos 0.0
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh1 zorder (11):
        ypos 0.0
        xcenter .5
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA03"),"True","img/RI_MBA03A@2x.png") as lh2 zorder (10):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NSU05A_SU018"
    铃 "「再见啦！」"
    window hide
    scene expression Solid("000") as bg1 with ImageDissolve("img/BG_MASK18@2x.png",1)

    play sound "SE06_14L"
    "轻轻挥手和大家道别，铃迅速开动了摩托车。"
    "没多久，莉莉丝她们便成了反光镜中的一个小点。"
    "个个都是错愕不已的表情……"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 0
    scene expression Solid("000") with fade
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 3
#ROUTINE_STA
#BG_POSC 3,30,-60,749,450

    scene expression "img/EVC_SU02B1@2x.png" as bg3:
        block:
            align (.5,.5)
            parallel:
                linear 0.03 xalign 0.53
            parallel:
                linear 0.03 yalign 0.53
            repeat
    #TODO
    
    show expression "img/Motor_KL_BG@2x.png" as motor_eff_bg zorder -10
    show expression "img/Motor_KL_RailDown_Stake@2x.png" at motor_eff_movein as motor_eff_down_s zorder -8
    show expression "img/Motor_KL_RailUp_Stake@2x.png" at motor_eff_movein as motor_eff_up_s zorder -7
    show expression "img/Motor_KL_RailUp@2x.png" at motor_eff_moveout as motor_eff_up zorder -6
    show expression "img/Motor_KL_RailDown@2x.png" at motor_eff_moveout as motor_eff_down zorder -5
    with dissolve
    
#EFF_PRI 0
#EFF_STAC 0,MOTOR_RIDE_KL,EFF_NOSKIP
#ROUTINE_STP
    play sound "SE06_14L"
    pause (32/32.0)
#FADE_IN 1
    志雄 "「接下来呢！想好去哪儿了吗！？」"
    window hide
    show expression "img/EVC_SU02B2@2x.png" as bg3 with dissolve
    voice "NSU05A_SU019"
    铃 "「好不容易来到了焰火大会，夹杂在人群中看的话岂不是太可惜了吗！」"
    志雄 "「你知道什么好的观赏场所吗？」"
    voice "NSU05A_SU020"
    铃 "「交给我好了！」"
    window hide
    scene expression Solid("000") as bg1 with ImageDissolve("img/BG_MASK18@2x.png",1)
#EFF_PRI 0
#EFF_STPC 0,EFF_NOSKIP
#EFF_STAC 0,MOTOR_LIGHT_N,EFF_NOSKIP
    show expression "img/motor_night@2x.png" as motor_light_n_eff:
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
    "说着，铃以极佳的心情拧紧了加速器，引擎声和耳边的风声很快就掩盖了我们。"
    window hide
    stop sound fadeout 1
    stop music
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG91NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG91NA@2x.jpg" as bg0 with dissolve
    play sound "SE05_10L"
    pause (32/32.0)
#FADE_IN 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBA01"),"True","img/SU_LBA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
#SE_VOLC 1,64
    voice "NSU05A_SU021"
    铃 "「就是这里」"
    "沿着海岸开了一段后，铃停了下来。"
    志雄 "「什么也没有啊？」"
    voice "NSU05A_SU022"
    铃 "「所以才好啊。离车站有点远，所以也不会有什么人来」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    with dissolve
#CHR_INIC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBA01"),"True","img/SU_XBA01A@2x.png") as lh10 zorder 100:
        xcenter 0.35
        ypos 0.0
    with dissolve
    "我在铃的催促下，向防波堤上走去。"
    志雄 "「的确是没有其他人……」"
    "就在我漫不经心回答着的时候，突然，眼前的视线一下子变得开阔。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    with dissolve
    stop sound
    #TODO
#EFF_PRI 0
#EFF_STAC 0,HANABI,EFF_NOSKIP
    show expression "img/fireworks2_0@2x.png" as firework:
        ypos .2
        xcenter .6
        anchor (0.5,0.5)
        zoom 0.5
        parallel:
            linear 1 zoom 2
        parallel:
            linear 1 alpha 0
    pause 1
    hide firework
    show expression "img/fireworks2_1@2x.png" as firework:
        ypos .1
        xcenter .8
        anchor (0.5,0.5)
        zoom 0.5
        parallel:
            linear 1 zoom 2
        parallel:
            linear 1 alpha 0
    pause 1
    hide firework
    show expression "img/fireworks2_2@2x.png" as firework:
        ypos .25
        xcenter .5
        anchor (0.5,0.5)
        zoom 0.5
        parallel:
            linear 1 zoom 2
        parallel:
            linear 1 alpha 0
    pause 1
    hide firework
    show expression "img/fireworks2_3@2x.png" as firework:
        ypos .15
        xcenter .7
        anchor (0.5,0.5)
        zoom 0.5
        parallel:
            linear 1 zoom 2
        parallel:
            linear 1 alpha 0
    play music "BGM13"
    志雄 "「啊！」"
    "一个个绚丽的光点在绘出美丽的图案后淡去。"
    "由于四周没什么遮挡物，焰火看上去出乎意料的近，我们为这种扣人心弦的美所折服。"
    "前一个焰火的余韵犹在，后一个又紧接着划过夜幕，夜空中布满了绚丽的色彩。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBB02"),"True","img/SU_XBB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU023"
    铃 "「从这里看就不会看见那些多余的东西，能把焰火尽收眼底呢」"
    志雄 "「真的呢……」"
    "但是，这样回答的我，不仅仅是在看焰火。"
    "在我身边的那位年长的姐姐。"
    "那端庄的侧脸和瞳孔中映着的光彩，让我不由地看呆了。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBB01"),"True","img/SU_XBB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU024"
    铃 "「真的很想穿一次浴衣，一心一意地观赏一次焰火呢。不过发现今天有焰火大会的时候已经从家里出来了」"
    志雄 "「真是遗憾呢……果然应该提前说一下的。不过……」"
    志雄 "「……真美啊」"
    "不由地脱口而出。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBB02"),"True","img/SU_XBB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU025"
    铃 "「听你这么说我很开心呢。作为没给你看浴衣的补偿，所以告诉你这个独享的秘密地点好了」"
    "虽然我并不是在说焰火的事情……老实说现在并不是能够集中心思欣赏焰火的状态。"
    voice "NSU05A_SU026"
    铃 "「志雄开心的话，我也会开心」"
    "本来我是想让你高兴的，结果这样……也不错。"
    "就结果而言，铃确实也很高兴。"
    "就在这时……"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBB04"),"True","img/SU_XBB04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU027"
    铃 "「啊！」"
#SET_SAVPNT
    "突然刮来的一阵强风，让铃踉跄了一下。"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "抓住她的手":
            $F7=0
        "站在上风口":
            $F7=1
#CLR_SAVPNT
    if F7==0:
        jump L_NSU05A_SEL00_A
    if F7==1:
        jump L_NSU05A_SEL00_B
label L_NSU05A_SEL00_A:
    $F4+=1
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    hide lh10
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU03A")]=True
    show expression "img/EVN_SU03A@2x.jpg" as bg1 zorder 1 with dissolve
    play sound "SE07_14"
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
#EFF_STPC 0,EFF_NOSKIP
#EFF_PRI 0
    hide lh0 with dissolve
    志雄 "「不要紧吧？」"
    "为了支撑住铃，紧紧抓住了她的胳膊。"
    voice "NSU05A_SU028"
    铃 "「嗯。谢谢」"
    志雄 "「啊……」"
    window hide
#BG_UV_AUTOC 1,((640/64)*11),((448/8)*3),((640/8)*5),((448/8)*5),1,F24,48
#BG_UV_SAVEC 1
    "就在铃的手要撤回去的一瞬间，我很自然地握住了铃的手。"
    voice "NSU05A_SU029"
    铃 "「啊……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBA01"),"True","img/SU_XBA01A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
#EFF_PRI 0
#EFF_STAC 0,HANABI,EFF_NOSKIP
    hide bg1 with dissolve
#BG_UVC 1,0,0,640,448
    pause (32/32.0)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBA07"),"True","img/SU_XBA07A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    pause (96/32.0)
    
    voice "NSU05A_SU030"
    铃 "「……」"
    "铃看了我一下，又把视线回到焰火那边。只是，我的手被握紧了。"
    "我也用力握住铃的手。"
    "之后我们便像忘记了语言一般，只是注视着焰火……"
    jump L_NSU05A_SEL00_X
label L_NSU05A_SEL00_B:
#MOV_CHR_INIT 48
#MOV_CHR0 ,(320)
#MOV_CHR_GO 1
    志雄 "「没关系吧？」"
    "看到有些摇晃的铃，我若无其事地向上风的地方动了动。"
    "虽然也只能起到安心的作用，但多少会好些吧。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBC01"),"True","img/SU_XBC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU031"
    铃 "「呵呵」"
    志雄 "「怎么？」"
    "铃望着焰火，哧哧地笑了。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBB01"),"True","img/SU_XBB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU032"
    铃 "「不要掉进风旋里去啊」"
    志雄 "「嗯」"
    "觉得有点难为情。我试图作为抵挡海风的盾牌的意图，一下子就暴露了。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBA06"),"True","img/SU_XBA06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU033"
    铃 "「为什么要做到这种程度呢？倒是很温柔，不过是该说你没用还是说你什么好呢」"
    志雄 "「为什么这么说」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBA07"),"True","img/SU_XBA07A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU034"
    铃 "「男孩子的话，不是都会想抱一下什么的么～」"
    "铃侧目看了我一眼。"
    "这种事情真是想都没想过……"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBB02"),"True","img/SU_XBB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU05A_SU035"
    铃 "「不过，这样才像志雄不是吗？呵呵」"
    "这算是夸奖吗？"
    "是陷入了什么回忆中了吗，铃笑了好一会儿，而那笑声早已盖过了焰火的声音在我的耳中回响着。"
    jump L_NSU05A_SEL00_X
label L_NSU05A_SEL00_X:
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music
#FADE_OUT 1,128
#EFF_STPC 0,EFF_NOSKIP
#EFF_PRI 0
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop se
    stop sound
    stop music
    $ renpy.end_replay()
#FADE_IN 0
    return