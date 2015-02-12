label NSU02A:
    $currentlabel = "NSU02A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '18'
    $date = '2'
    window hide
#FADE_OUT 0,0
    scene expression Solid("000") with fade
#FADE_IN 0,0
#CAL_DSP_GRP 5,CAL_0718,1
    show expression "img/NIMG15B-568h@2x.jpg" as cal zorder 5
    show expression "img/07_18_TUESDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
#FADE_OUT 1,32,COL_WHITE
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG14AA@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_PAL_BGC ID_ALL,BG14AA
    play sound "SE05_14L"
    pause (32/32.0)
#FADE_IN 1,32
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    志雄 "「呜～，今天看来也很热啊」"
    "像往常一样，我吃了铃做的早餐之后前往学校。"
    window hide
#BG_SET_BACK 
#FADE_OUT 1,32
#BG_INIC 1
#TODO
    show expression "img/NIMG01A@2x.png" as bg1 zorder 1 with dissolve
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
#EFF_STAC 0,CLOUD_A,EFF_NOSKIP,0
#FADE_IN 1,32
#EFF_STAC 0,LENSFLARE_SKY,EFF_SKIP,0
    pause (80/32.0)
    "阳光十分刺眼，不由得让人感觉今天一整天都会是令人厌烦的炎热天气。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1,32
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG07AA3@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_PAL_BGC ID_ALL,BG07AA3
    play sound "SE08_09L"
    pause (32/32.0)
#FADE_IN 1,32
    play music "BGM10"
    pause (16/32.0)
#SE_VOLC 1,64,64
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320),0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU02A_TO000"
    亨 "「哟，志雄，一起回去吧」"
    "今天课上的内容只有期末考试成绩的公布。"
    "班上的同学还在为考试的结果议论纷纷。"
    志雄 "「不行，接下来还有学生会」"
    "课程在上午就结束了，但我还有学生会的工作。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA04"),"True","img/TO_MAA04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU02A_TO001"
    亨 "「怎么，今天也要工作？」"
    志雄 "「有什么事吗？」"
    voice "NSU02A_TO002"
    亨 "「其实不是想约志雄，而是想约莉莉丝。可不知怎的她今天的心情看起来非常糟糕啊～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA03"),"True","img/TO_MAA03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    志雄 "「呃……」"
    if not persistent.dictlist[7] and persistent.show_dict:
        $persistent.dictlist[7]=True
        show screen dict_pop(i=7)
    "亨的脸色黯然无光。"
    "昨天铃没把新作品给莉莉丝那家伙看，这件事还拖着么。"
    "不过，和心情糟糕的莉莉丝两个人回去，即使是亨也会不舒服的。"
    voice "NSU02A_TO003"
    亨 "「所以我觉得志雄你也要想办法协助一下」"
    志雄 "「抱歉，我差不多要为奏云祭做准备了」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB04"),"True","img/TO_MAB04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU02A_TO004"
    亨 "「怎么这样早？还没到暑假啊」"
    "果然大家都说着同样的话。"
    "我苦笑着将昨天对铃所说的话重复了一遍。"
    志雄 "「去年活动办得非常仓促，所以今年想早一点准备」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA03"),"True","img/TO_MAA03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU02A_TO005"
    亨 "「也是，今年克罗艾学姐已经不在了」"
    志雄 "「别这么说嘛～，克罗艾学姐不在学生会就感到不安了？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA05"),"True","img/TO_MAA05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU02A_TO006"
    亨 "「有一点」"
    "亨严肃地说道。"
    "就算这样，这一届的学生会在老师那边得到的评价也还算不错。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU02A_TO007"
    亨 "「嘛，我会为你们加油的」"
    voice "NSU02A_TO008"
    亨 "「所以拜托了，就搞个像去年那样的，恋人们能打得火热的后夜祭！」"
    "原来这才是他的目的啊……"
    "在我们学校有这样一个传说：后夜祭上一起跳舞的恋人会得到幸福。"
    "亨也想在今年的后夜祭上沾一点光。"
    志雄 "「后夜祭是后辈负责的。不过我认为他们一定能做出一场花费甚低，却又精彩的演出的」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA05"),"True","img/TO_MAA05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU02A_TO009"
    亨 "「那你负责做什么？」"
    志雄 "「地点和时间的分配和调整，预算的分配等等，从整体上审视整个奏云祭」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#SET_SAVPNT
    voice "NSU02A_TO010A"
    亨 "「是～么。没办法，那你就忙吧。{w=3}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU02A_TO010B"
    extend "我是打心底想分担莉莉丝的心情啊！」"
#CLR_SAVPNT
    志雄 "「是么，那你就加油吧」"
    voice "NSU02A_TO011"
    亨 "「嗯！」"
    window hide
#SE_VOLC 1,255,64
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    with dissolve
    "亨摆着一个胜利的手势，走出了教室。"
    "……有时也有些羡慕这家伙毫无来由的积极态度。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1,32
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG08AA@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_PAL_BGC ID_ALL,BG08AA
#FADE_IN 1,32
    voice "NSU02A_CH000"
    智纱 "「塚本君？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320),0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA01"),"True","img/CH_MAA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    "刚刚看到学生会室，背后就传来了一道声音。"
    if not persistent.dictlist[2] and persistent.show_dict:
        $persistent.dictlist[2]=True
        show screen dict_pop(i=2)
    志雄 "「啊，箱崎……」"
    voice "NSU02A_CH001"
    智纱 "「是不是过会有学生会的工作？」"
    志雄 "「嗯」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAB01"),"True","img/CH_MAB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU02A_CH002"
    智纱 "「还没到暑假呢，真辛苦……啊，已经开始为奏云祭做准备了？」"
    "果真每见一个人就要重复同样的话啊。"
    "算了，事实上我自己一个人做，第一次了解了其中的艰辛。"
    志雄 "「正是如此，我在学生会也是有三年的学习经验了」"
#SET_SAVPNT
    voice "NSU02A_CH003A"
    智纱 "「去年可真辛苦啊。{w=3}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAB05"),"True","img/CH_MAB05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU02A_CH003B"
    extend "又到了这个时候了」"
#CLR_SAVPNT
    "箱崎眯起双眼，怀念地回忆着什么。"
    "明明是一年前的事情了，却仿佛近在眼前……"
    志雄 "「箱崎准备在奏云祭做些什么吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAB01"),"True","img/CH_MAB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU02A_CH004"
    智纱 "「嗯。我还要复习备考，所以没办法尽太大的力。但好不容易进了广播部，心想总能做些什么吧」"
    voice "NSU02A_CH005"
    智纱 "「要是有什么问题了我再来找你商量吧，能和志雄君一起讨论各种各样的事情我真的很开心呢」"
    志雄 "「嗯，如果有我能做的事情，我会尽力帮忙的」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAB02"),"True","img/CH_MAB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU02A_CH007"
    智纱 "「谢谢你，那回头见了」"
    志雄 "「再见……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    with dissolve
    play sound "SE01_04L"
#SE_VOLC 0,96,4
    pause (16/32.0)
    "我就这样望着箱崎的背影消失在我的视线中。"
    stop se fadeout 1
    "箱崎的笑容回荡在眼前。"
    志雄 "「……呼」"
    "说实话，这位少女真的很坚强呢。而我现在面对箱崎还会紧张，实在是没出息。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1,0
    show expression "img/BG09AA@2x.jpg" as bg1 zorder 1 with dissolve
    
#BG_ALP_AUTOC 1,128,0,F24,48,1
#BG_ALP_SAVEC 1
#BG_SWPC 0,1
    #hide bg1 with dissolve
    play sound "SE00_25"
#BG_ALPC 1,128
#BG_PRI 0,6
#BG_PRI 1,1
#CHR_PAL_BGC ID_ALL,BG09AA
    stop sound
    志雄 "「辛苦了～」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320),0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB01"),"True","img/YU_MAB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU02A_YU000"
    结乃 "「你也辛苦了」"
    "一走进学生会室，就看到以春日为首的学生会成员们聚集在一起。"
    "如今学生会的职能多半是由高二的学生承担，高三学生的工作很少。"
    "奏云祭结束后，就要全部进行交接了，也到了我引退的时候。从现在开始的奏云祭可以说是最后一次的演出舞台了。"
    志雄 "「大概都到齐了吧？」"
    voice "NSU02A_YU001"
    结乃 "「差不多了，还有两个人没来」"
    志雄 "「没到的都是高三生吧？那就先开始吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAA05"),"True","img/YU_MAA05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU02A_YU002"
    结乃 "「好的，那么——」"
    window hide
#FADE_OUT 1,32
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,(640/8),((448/16)*3),(640/2),(448/2)
    show expression "img/BG09EA@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_PAL_BGC ID_ALL,BG09EA
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+192),0
#CHR_SETC 0,YU_LAC01
    pause (32/32.0)
#FADE_IN 1,32
    voice "NSU02A_YU003"
    结乃 "「以上就是今天讨论的话题，会长有什么要说的吗？」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    with dissolve
    志雄 "「嗯。高三的学生要以考前复习为主，这无可厚非，但还是尽量出场吧，奏云祭有许多地方要教新来的高一学生」"
    志雄 "「高二的学生如果有不明白的地方，也不要憋在心里，请随时来询问」"
    voice "NSU02A_X3000"
    生徒会一同 "「是」"
    志雄 "「那好吧，今天就到这里，大家辛苦了」"
    window hide
    play sound "SE08_10L"
#BG_GET_NOC 0,F34
    "除了个别学生会成员留在这里，其他人都准备回去了。"
    window hide
#SE_VOLC 1,64,64
    play sound "SE03_29"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320),0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA01"),"True","img/YU_LAA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU02A_YU004"
    结乃 "「学长，请检查一下这个」"
    "我正为回家作准备，春日拿着装订好的文件走了过来。"
    志雄 "「辛苦你了，多亏有春日在，才能让气氛如此活跃的」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB05"),"True","img/YU_LAB05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#REEK_CHR 0,0
    voice "NSU02A_YU005"
    结乃 "「是么？」"
#REMOVE_REEK_CHR 0
    "春日并没有意识到自己优秀之处。"
    "比起我，春日才更适合成为克罗艾学姐的继承人，我发自内心这样认为。"
    志雄 "「多亏了春日的计划，担子真的很轻松。把太多的事情交给你来做，我都觉得有些不好意思了」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU02A_YU006"
    结乃 "「哪有，我只是向去年的学长们学习罢了」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB02"),"True","img/YU_LAB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU02A_YU007"
    结乃 "「总之暑假一结束，学长们就要开始努力了，所以请利用暑假时间好好学习哟」"
    "春日虽然露出了笑容，但眼神中却没有笑意……"
    志雄 "「好、好的」"
    "这样一来，已经分不清楚哪个才是会长了。"
    志雄 "「你辛苦了」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU02A_YU008"
    结乃 "「你也辛苦了」"
    window hide
#SE_VOLC 1,128,64
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    with dissolve
    "春日小跑着离开了，那精神饱满的姿态令我有些羡慕。"
    stop sound fadeout 1
    show expression "img/BG08EA@2x.jpg" as bg_over zorder 20 with dissolve
    play sound "SE00_26"
    志雄 "「不是那么可靠，这可真对不住啊……我也必须加把劲了……」"
    "作为学生会会长，我肩负着很大的重任，但也需要大家的帮助和支持。"
    "也想从铃那里得到些许的认可……不过还差得远啊。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music
#FADE_OUT 1,128
    scene expression Solid("000") with fade
#GRAPH_INI 
#SE_STPC 0
    stop sound
    stop music
#FADE_IN 0,0
    $ renpy.end_replay()
    return