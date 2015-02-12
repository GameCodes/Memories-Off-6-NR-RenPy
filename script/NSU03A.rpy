label NSU03A:
    $currentlabel = "NSU03A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '21'
    $date = '5'
    window hide
#FADE_OUT 0,0
    scene expression Solid("000") with fade
#FADE_IN 0,0
#CAL_DSP_GRP 4,CAL_0721,0
    show expression "img/NIMG15C-568h@2x.jpg" as cal zorder 5
    show expression "img/07_21_FRIDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
#FADE_OUT 0,0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/EXBG09A@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/EXBG09A@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320),0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC05"),"True","img/SU_ZDC05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
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
    志雄 "「嗯……今天的饭也很好吃」"
    "最近，铃到我家做早饭的次数渐渐多了起来。"
    "当然，随着截止日期的临近也会有她脱不开身的时候，这时反而是我来做饭。"
    voice "NSU03A_SU000"
    铃 "「……」"
    志雄 "「……？」"
    "不知为什么，铃一直盯着我这边。"
    "我做了什么吗……？"
    voice "NSU03A_SU001"
    铃 "「有颗饭粒」"
    志雄 "「啊」"
    "我慌忙摸起脸颊，却什么也没摸到。"
    志雄 "「……？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB01"),"True","img/SU_ZDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU002"
    铃 "「对不起，骗你的」"
    志雄 "「诶？」"
    "她真像个孩子……"
    "我不由得放下筷子，叹了一口气。"
    voice "NSU03A_SU003"
    铃 "「我是在想，是不是发生了什么好事了呢？」"
    志雄 "「好事？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC01"),"True","img/SU_ZDC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU004"
    铃 "「嗯，是该说你脸上没有紧张感呢，还是说你没有男子汉气概呢……」"
    志雄 "「是、是这样么？」"
    "虽然我并没有这样感觉……"
    voice "NSU03A_SU005"
    铃 "「发生了什么事吗？」"
    志雄 "「唔……从今天开始放假了吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA03"),"True","img/SU_ZDA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU006"
    铃 "「什么！？已经……放假了！？明明在这之前还是黄金周呢……」"
    "铃吃惊地把身体向后仰。说起黄金周……现在已经是七月了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA02"),"True","img/SU_ZDA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU007"
    铃 "「这么说来，我去买东西的时候，就感觉天气好热……原来已经暑假了啊」"
    "正是一个充实的夏天！可以这样说吧。而且在这之前，还有一些有关奏云祭的事情。"
    "虽说社会人对季节的变迁不大敏感，但对于眼前的这个人来说，好像不是这样的……"
    志雄 "「是不是工作太忙了？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA04"),"True","img/SU_ZDA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU008"
    铃 "「嗯，是很忙，但基本在家里工作，可以说对日期和星期的感觉都很稀薄吧」"
    "目睹了铃的生活后，我的确有这种感觉。"
    "我对铃这种平时和周末没有区别的日子，感到有点可怜。"
    志雄 "「不过，你不看日历吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB05"),"True","img/SU_ZDB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU009"
    铃 "「说起来好像不会刻意去看……」"
    "铃像个淘气的孩子那样微微耸了下肩。"
    志雄 "「身为作家却不去检查截稿日期，这可不太好啊」"
    志雄 "「编辑一定会急哭的」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA06"),"True","img/SU_ZDA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU010"
    铃 "「呃……志雄有时候也会对我很严苛啊」"
    "铃不悦地抬高了嗓门。"
    "平时总是一副成年人的模样，可一提到截止日期却又变得像个任性的孩子，她就是这样的人。"
#SET_SAVPNT
    voice "NSU03A_SU011A"
    铃 "「嗯……{w=2}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA01"),"True","img/SU_ZDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU011B"
    extend "但是……是啊，已经到暑假了。那我最好不要给你做早饭了吧？」"
#CLR_SAVPNT
    志雄 "「啊，关于这一点我反而要拜托你。现在这边要和平时一样学习，还要安排学生会的工作」"
    "没错，就算是暑假，我依然是个考生。"
    "何况还有学生会的工作，是没办法这样悠闲的。"
    voice "NSU03A_SU012"
    铃 "「嗯，那今天呢？」"
    志雄 "「先去学校露个面，然后复习功课」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA02"),"True","img/SU_ZDA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU013"
    铃 "「难得的暑假，就这样多可惜啊」"
    志雄 "「没办法啊，铃在面临考试的时候也是要努力学习的吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA01"),"True","img/SU_ZDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU014"
    铃 "「也是呢。志雄想往哪方面发展呢？」"
    志雄 "「大概是上大学……吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA02"),"True","img/SU_ZDA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU015"
    铃 "「吧？这回答很暧昧啊，有没有想从事的职业呢？」"
    志雄 "「嗯……没有特别想做的。所以直说的话，也没确定要上大学。话说回来，是否真有上大学的必要呢……」"
    voice "NSU03A_SU016"
    铃 "「如果没有及早训练成为在某方面有一技之长的社会人的想法，那么去大学更好一些」"
    志雄 "「老师和家长也是这样说的……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA04"),"True","img/SU_ZDA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#SET_SAVPNT
    voice "NSU03A_SU017A"
    铃 "「嗯～，{w=3}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA01"),"True","img/SU_ZDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU017B"
    extend "怎么了，好像很烦恼呢」"
#CLR_SAVPNT
    window hide
#BG_BLUR 0,1
#CHR_BLUR 0,1
#FILT_IN 48,0,COL_DARK2
    "大人和孩子，社会人和学生。要想跨越两者间的隔阂，就职应该是最可行的手段吧。"
    "可能的话，想尽早与铃站在同等的位置……然而客观地看，还是不清楚这样做是不是正确的。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC04"),"True","img/SU_ZDC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#ROUTINE_STA
#CHR_BLUR 0,1
#CHR_POS_AUTOC 0,320,100,1,F123,64,0
#CHR_SCL_AUTOC 0,512,512,1,F123,64,1
#ROUTINE_STP
#SET_SAVPNT
    voice "NSU03A_SU018"
    铃 "「喂……志雄～」{w=3}{nw}"
#MESX "%K%P"
#CLR_SAVPNT
    window hide
#BG_BLUR 0,0
#CHR_BLUR 0,0
#FILT_OUT 24
    志雄 "「什、什么事？」"
    "眼前所看见的，是铃探过来的脸。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC05"),"True","img/SU_ZDC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU019"
    铃 "「怎么还是一副迷迷糊糊的样子，打起精神来！」"
    志雄 "「对、对不起……刚才想问什么吗？」"
    window hide
#ROUTINE_STA
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA01"),"True","img/SU_ZDA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#CHR_POS_AUTOC 0,320,0,1,F123,64,0
#CHR_ALP_AUTOC 0,0,1,F123,64,0
#CHR_SCL_AUTOC 0,128,128,1,F123,64,1
#ROUTINE_STP
#ROUTINE_STA
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA01"),"True","img/SU_ZDA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    hide lh1 with dissolve
#ROUTINE_STP
#CHR_SCL_SAVEC 0
    voice "NSU03A_SU020"
    铃 "「你什么时候从学校回来？」"
    志雄 "「中午回来，然后在家或在图书馆复习」"
    "在家学习固然很好，但在图书馆之类的地方感觉学习效率高些……也许只是心理作用。"
    voice "NSU03A_SU021"
    铃 "「嗯～，晚饭就在外边吃了？还是提前做些什么？」"
    志雄 "「每天都让你做饭，真的不好意思呢」"
    "我知道铃每天一如既往地忙于工作，不想再给她添加负担。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB02"),"True","img/SU_ZDB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "然而铃看到我这样的表情，却微笑起来。"
    voice "NSU03A_SU022"
    铃 "「是么？我自己一个人也同样要做的，所以就不必在意啦」"
    志雄 "「老师也请好好地工作。啊，对了」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB01"),"True","img/SU_ZDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU023"
    铃 "「有事吗？」"
    志雄 "「铃晚上有时间么？」"
    voice "NSU03A_SU024"
    铃 "「有些忙，不过能腾出时间」"
    志雄 "「那么，今天的晚饭就由我来做」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB02"),"True","img/SU_ZDB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU025"
    铃 "「哦～，真罕见啊，究竟有什么阴谋呢？」"
    "铃一瞬间有些目瞪口呆，不过立刻恢复了甜美的笑容。"
    志雄 "「不是的，只是关于未来的发展方向，想稍微听一下你的意见。现在得去学生会，快要迟到了」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA06"),"True","img/SU_ZDA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU026"
    铃 "「是这样啊，我本以为你在酝酿着某些非法进入大学的方法呢」"
    志雄 "「也不是这样……等等，你知道方法吗！？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA01"),"True","img/SU_ZDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU027"
    铃 "「不，完全不知道」"
    "……我有些焦躁。对于铃来说，知道一两种走后门入学的方法也没什么不可思议的。"
    志雄 "「所以说，能挤出时间吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB01"),"True","img/SU_ZDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU028"
    铃 "「要是这件事的话，我提前空出时间吧。你会做点什么呢？就让我好好期待一下吧。」"
    志雄 "「你有想吃的菜吗？」"
    voice "NSU03A_SU029"
    铃 "「不不，要是我决定的话不就没有意思了么。我很想看看志雄会准备什么样的菜谱。可以的话，能让我大吃一惊是最好不过」"
    志雄 "「喂，不要用这么奇怪的方式提高难度啊……」"
    "被给予太高的期待也是很令人很为难的事啊。和莉莉丝不一样，我做饭的水平至多算是说得过去。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB02"),"True","img/SU_ZDB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU030"
    铃 "「呵呵呵，我期待着哦」"
    志雄 "「我说，别抱那么大的希望……」"
    "比起前途和学业，今晚的菜谱似乎更难办啊。"
    "可即使如此，说出的话也收不回了，铃似乎也在期待着。"
    "于是……"
    window hide
    stop music
#FADE_OUT 1,32
    scene expression Solid("000") with fade
    stop music
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG17AA1@2x.jpg" as bg0 zorder 0 with dissolve
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    with dissolve
#FADE_IN 0,0
    if not persistent.dictlist[37] and persistent.show_dict:
        $persistent.dictlist[37]=True
        show screen dict_pop(i=37)
    "一上午都在学校商量事宜的我，回家时准备顺便路过一下『小文』。"
    if not persistent.dictlist[9] and persistent.show_dict:
        $persistent.dictlist[9]=True
        show screen dict_pop(i=9)
    "如果是莉莉丝或富美子婆婆的话，一定能给我传授一些不错的主意。"
    window hide
#FADE_OUT 0,0
#BG_COLC 0,128,128,128,128
#BG_UVC 0,0,512,640,448
    scene expression "img/BG17AA1@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_ALPC 0,0
#CHR_POSC 0,(320),0
#CHR_POSC 1,(320+160),0
#BG_BLUR 0,1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA01"),"True","img/RI_MBA01A@2x.png") as lh0 zorder (10+0):
        xcenter .5
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_LAA01"),"True","img/FU_LAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0

#FADE_IN 1,32
    play music "BGM10"
    play sound "SE03_33"
    voice "NSU03A_FU000"
    富美子 "「请别客气，志雄」"
    志雄 "「我开动了」"
    window hide
#ROUTINE_STA
#BG_BLUR 0,0
#CHR_POS_AUTOC 1,(640)
#CHR_ALP_AUTOC 1,0,1,F24,32,0
#CHR_ALP_AUTOC 0,128,1,F24,32,1
#ROUTINE_STP
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_LAA01"),"True","img/FU_LAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
        parallel:
            linear 1 alpha 0
        parallel:
            linear 1 xcenter 1.25
    hide lh1 with dissolve
#CHR_ALPC 1,128
    voice "NSU03A_RI000"
    莉莉丝 "「虽说去年就想过，不过连暑假里也在忙你还真是相当努力呢啊」"
    "虽说莉莉丝也在放暑假，不过看起来还是一如既往地在小文帮忙呢。"
    "尽管是每年如此，但这家伙怎么说也是考生啊……"
    志雄 "「学生会的活动，也是像社团那样啊。运动部的话，暑假也还要返校练习的」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA06"),"True","img/RI_MBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI001"
    莉莉丝 "「但又没有什么运动会，有什么意思啊」"
    志雄 "「随便你怎么说吧」"
    "我大口吃着中华冷面，脑子里塞满了疑问。"
    志雄 "「好好地把学校的活动办成功才有的充实感，以及找到处理任务的技巧是最开心的……」"
    voice "NSU03A_RI002"
    莉莉丝 "「年级委员和学生会委员这些人，我只觉得他们是办杂事的」"
    志雄 "「嗯，或许是这样，即使是自己来说，也觉得这只是份很朴素的工作吧」"
    "起初的确对学生会的工作抱着美好的印象。"
    "然而，这样的幻想不久就被打碎了。工作的内容正如莉莉丝所说，多半是文案和其它零碎的工作。"
    "像克罗艾学姐这样的人，让我们深切地体会到了她的特别之处。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD01"),"True","img/RI_MBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI003"
    莉莉丝 "「知道了还要去做，真是奇怪的人啊」"
    志雄 "「你这么说真失礼啊。还有，谁都有不得不做的工作吧？」"
    "再说，原本推荐我加入学生会的就是莉莉丝……"
    "不过，现在是因为做着自己喜欢的事情，所以觉得还不错。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA04"),"True","img/RI_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI004"
    莉莉丝 "「一直在学生会干下去，你沉得住气吗？」"
    志雄 "「什么意思？」"
    voice "NSU03A_RI005"
    莉莉丝 "「你是准备要升学的吧？」"
    志雄 "「姑且，是决定这么做的……嗯」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA06"),"True","img/RI_MBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI006"
    莉莉丝 "「搞什么呀，这么优柔寡断的」"
    志雄 "「基本确定是去参加大学考试。只是，我还在思考有没有其它的可能性，虽然我知道已经没有那么多时间了」"
    voice "NSU03A_RI007"
    莉莉丝 "「还是犹豫啊，真是优柔寡断……」"
    "唔……一针见血，无法反驳……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA04"),"True","img/RI_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI008"
    莉莉丝 "「总是这样的话会招铃讨厌的哦」"
    志雄 "「什、什么呀」"
    "突然冒出这么一句，我忍不住将口中的冷面喷了出来。"
    voice "NSU03A_RI009"
    莉莉丝 "「像铃那样能干的人，对于磨磨蹭蹭、迟迟不肯下结论的人是很反感的」"
    志雄 "「这、这个嘛……可能是吧……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD01"),"True","img/RI_MBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI012"
    莉莉丝 "「没错，而且你亲自邀请铃，这也很少见的吧？」"
    志雄 "「嗯……」"
    "切中要害。不愧是我的青梅竹马，能确实地说到我的痛处。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA04"),"True","img/RI_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI013"
    莉莉丝 "「认为反正铃也忙，所以就有顾虑，这是不行的」"
    志雄 "「不过，今天要约她吃饭」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD06"),"True","img/RI_LBD06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI014"
    莉莉丝 "「呵呵？」"
    "这话似乎引起了莉莉丝的兴趣，她向我探出身子。"
    志雄 "「今天晚上我要亲手做饭，还准备说许多事」"
    voice "NSU03A_RI015"
    莉莉丝 "「呵～呵」"
    志雄 "「怎么了，这种反应」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD01"),"True","img/RI_LBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI016"
    莉莉丝 "「难得的夏天啊，不想稍微冒险一下吗～，如果是铃代老师的小说的话，将会是气氛热烈的一幕哦？」"
    志雄 "「不要把我的现实和小说混为一谈……」"
    voice "NSU03A_RI017"
    莉莉丝 "「所以呢？计划好要做什么了？」"
    志雄 "「还没决定。所以说，我就是来找你商量这个的。有没有什么好的推荐菜谱啊？对了，中华冷面怎么样？」"
    志雄 "「啊，不过确实还有剩下的猪肉……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA06"),"True","img/RI_LBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI018"
    莉莉丝 "「呼……我说你呀」"
    voice "NSU03A_RI019"
    莉莉丝 "「你就不能做点更有品位的，让女孩子能接受的料理么？」"
    志雄 "「如果我会的话，就不必特意来问你了」"
    "一般来说双亲不在身边独立生活的人，知道的东西会更多，理应比同龄的伙伴更会做菜才对。"
    "然而我会做的仅仅是既便宜又简单，能填饱肚子的适合独居男人的料理。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBC06"),"True","img/RI_LBC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI020"
    莉莉丝 "「啊，不过，以志雄的手艺，即使做最喜欢的食物也会很失败就是了」"
    志雄 "「一个人的话，做的东西能吃就行了啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD01"),"True","img/RI_LBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI021"
    莉莉丝 "「要是这样就行了的话，那就做些更简单的？」"
    志雄 "「简单？比如说？」"
    voice "NSU03A_RI022"
    莉莉丝 "「反正材料是猪肉……夏天吃白切肉片怎么样」"
    志雄 "「啊，这个主意不错，我也喜欢」"
    "实际上，制作白切肉片不用花费大量时间，却很好吃。"
    "可这也太简单了吧？"
    志雄 "「不会被认为是偷工减料吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA01"),"True","img/RI_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI023"
    莉莉丝 "「说偷工减料的话也的确如此，但可以准备一些调料和调味汁，再做一道别的不就好了么」"
    志雄 "「原来如此……那就着手准备吧」"
    voice "NSU03A_RI024"
    莉莉丝 "「用质量好的肉，很轻易就能做出好味道」"
    "技术不擅长的话，要从别的地方补偿吗。"
    志雄 "「是啊，难得努力一次呢……冰箱里的肉用来做别的东西吧，谢谢你，上了一课」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD01"),"True","img/RI_LBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI025"
    莉莉丝 "「难得一回啊，加油吧」"
    志雄 "「嗯。啊，我吃完了」"
    window hide
    stop music
#FADE_OUT 1,32
    scene expression Solid("000") with fade
    stop music
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,(640/4),(448/4),(640/2),(448/2)
    show expression "img/BG33AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG33AA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
#FADE_IN 1,32
    play sound "SE03_42"
    志雄 "「接下来，要鼓足干劲了」"
    "回家之后集中精力，做了两个小时的暑假作业。"
    "然后去买晚饭需要的东西。"
    "平时总觉得做饭很麻烦，更想做学习一类的事情，为什么呢……"
    "这是逃避的行为么？"
    "铃明明那么忙，还热心地为我做饭。"
    window hide
    play sound "SE03_24L"
    "首先煮好南瓜，接着要做味噌汤，然后是白切肉片？"
    play sound "SE03_69"
    voice "NSU03A_SU031"
    铃 "「饭煮好了吗？我刚看了，省时省力的菜很多，所以必须快点做」"
#SET_SAVPNT
    志雄 "「啊，我忘了{w}"
#BG_SWPC 0,1
#BG_PRI 1,1
#BG_PRI 0,6
#BG_GET_NOC 1,F34
#BG_SET_BACK 
#BG_INIC 0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320),0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDA01"),"True","img/SU_LDA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE03_90"
    hide bg1 with dissolve
    extend "……啊，什么！？」"
#CLR_SAVPNT
    "不知什么时候铃已在我的身后，兴趣颇深地在我身边窥视着。"
    play sound "SE07_02"
    志雄 "「呜哇！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU_MDA03'",DynamicDisplayable(mouthanime,"SU_MDA03"),"True","img/SU_MDA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE03_71"
    voice "NSU03A_SU032"
    铃 "「危险！」"
    "吓、吓我一跳……"
    "脱手的菜刀扎在脚下的地板上。"
    志雄 "「啊，铃！？」"
    window hide
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CHR'",DynamicDisplayable(mouthanime,"SU_LDC04"),"True","img/SU_LDC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "BGM13"
    voice "NSU03A_SU033"
    铃 "「没事吧？有没有受伤？」"
    志雄 "「哎？啊，没事，我一点事没有」"
    "我边说边拾起扎在地板上的菜刀。"
    "啊，心跳的真是厉害呢。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDC02"),"True","img/SU_LDC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU034"
    铃 "「幸好没事～。突然之间出声吓到你，对不起」"
    志雄 "「吓死我了，不知不觉就站在这里……说起来，你来的真早啊？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDB03"),"True","img/SU_LDB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0,0
    voice "NSU03A_SU035"
    铃 "「没有啦，原稿写不动了，然后不经意就到这来了」"
#REMOVE_REEK_CHR 0
    志雄 "「等我全部做好再看吧，不是要让你大吃一惊吗」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDC04"),"True","img/SU_LDC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU036"
    铃 "「啊～，我全忘了」"
    "果然以铃作为对象，任何事情都会和计划发生偏差。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDC01"),"True","img/SU_LDC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU037"
    铃 "「来都来了，干脆我也帮忙吧？」"
    志雄 "「……不能让客人帮忙吧」"
    "铃一直为我做饭，感谢还来不及呢……"
#SET_SAVPNT
    "但是，一起做会更有意思。"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "一起做吧":
            $F7=0
        "你看着就行了":
            $F7=1
#CLR_SAVPNT
    if F7==0:
        jump L_NSU03A_SEL00_A
    if F7==1:
        jump L_NSU03A_SEL00_B
label L_NSU03A_SEL00_A:
    $F4+=1
    志雄 "「我知道了，那就一起做吧。你一直在后面看着，我也平静不下来」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDB02"),"True","img/SU_LDB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU038"
    铃 "「那就这么办。光在后面看着，我还是不放心」"
    志雄 "「别看这样，我好歹也一个人生活了很长时间的」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDC02"),"True","img/SU_LDC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU039"
    铃 "「志雄和我不一样，总是愿意事必躬亲呢」"
    志雄 "「啊，确实什么都是我自己亲自动手呢」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDC01"),"True","img/SU_LDC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU040"
    铃 "「就是这样。所以看你做饭的时候，就非常想出手帮忙」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU01A")]=True
    scene expression "img/EVN_SU01A@2x.jpg" as bg1 with dissolve
    "铃边说边洗好了手，站在我身边。"
    "……总觉得这样也不错。"
    "两人一起干活，就像是新婚夫妇的感觉……"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU01C")]=True
    show expression "img/EVN_SU01C@2x.jpg" as bg1 with dissolve
    voice "NSU03A_SU041"
    铃 "「话说回来，我该做什么呢？」"
    志雄 "「唔，我接着煮南瓜，味噌汤就拜托你了」"
    voice "NSU03A_SU042"
    铃 "「知道了，配料呢？」"
    "太危险了太危险了，不能让她看透我的心在动摇。"
    志雄 "「有豆腐、裙带菜和葱」"
    window hide
    stop se
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU01A")]=True
    show expression "img/EVN_SU01A@2x.jpg" as bg1 with dissolve
    voice "NSU03A_SU043"
    铃 "「呵呵」"
    "听了我的说明，铃立刻拿起菜刀切葱。和我相比，铃的手法要灵巧许多。"
    "如果和莉莉丝在料理上一决胜负的话，或许会很有意思吧。"
    window hide
    play sound "SE03_09L"
    "铃似乎在哼小曲，这一光景意外地令人怀念。一阵刺眼的感觉袭来，我忍不住眯起眼睛。"
    voice "NSU03A_SU044"
    铃 "「志雄，你的手停下来了哦。煮东西是最花时间的，必须要早点做」"
    志雄 "「……啊，嗯」"
    "糟糕，看得着了迷，不知不觉被吸引住了。"
    window hide
    stop se
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU01C")]=True
    show expression "img/EVN_SU01C@2x.jpg" as bg1 with dissolve
    voice "NSU03A_SU045"
    铃 "「志雄？」"
    志雄 "「啊，没事，什么都没有」"
    voice "NSU03A_SU046"
    铃 "「什么没事啊……看我的家庭主妇的打扮看入迷了？」"
    志雄 "「啊，嗯。我觉得很好看……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU01B")]=True
    show expression "img/EVN_SU01B@2x.jpg" as bg1 with dissolve
    voice "NSU03A_SU047"
    铃 "「咳咳……你在说什么呀」"
    "铃在尝味噌汤的时候被呛到了。"
    志雄 "「咦？等等？那个……」"
    "哇！我都说了些什么呀！这样不加思索就都说出来了……"
    志雄 "「对、对不起，说了这么奇怪的话……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU01D")]=True
    show expression "img/EVN_SU01D@2x.jpg" as bg1 with dissolve
    voice "NSU03A_SU048"
    铃 "「没、没关系……真是的，志雄有时候很狡猾啊……」"
    志雄 "「哎？狡猾是什么意思？」"
    voice "NSU03A_SU049"
    铃 "「没什么。肚子也开始饿得咕咕叫了，赶紧做吧」"
    jump L_NSU03A_SEL00_X
label L_NSU03A_SEL00_B:
    志雄 "「你看着就行了，又不是绞尽脑汁才设计出来的菜谱。冰箱里有啤酒，可以拿出来喝」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDB01"),"True","img/SU_LDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU050"
    铃 "「准备的很周到呢」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDC01"),"True","img/SU_LDC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU051"
    铃 "「不过，这对话就像是同居的恋人之间才会有的。而且搭配性别的台词反了吧」"
    play sound "SE03_72"
    "切坏了南瓜，菜刀摔在了案板上，被切成奇形怪状的南瓜滚到了水槽里。"
    志雄 "「哇，都是因为铃说了奇怪的话……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDB01"),"True","img/SU_LDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU052"
    铃 "「自己笨手笨脚，就不要把责任推给别人」"
    window hide
    play sound "SE03_70"
    pause (8/32.0)
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1,32
#BG_UVC 0,(640/4),((448/4)+512),(640/2),(448/2)
    pause (32/32.0)
#SE_WATC 0
#SE_WATC 1
    play sound "SE03_73"
    play sound "SE03_24L"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDA02"),"True","img/SU_LDA02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_IN 1,32
    voice "NSU03A_SU053"
    铃 "「看，锅还在煮着吧？可别让火灭了，还有葱一定要切得更细点」"
    志雄 "「嗯，我知道了」"
    "话虽这么说……"
    "因为是同时在处理多个料理的环节，要是某一个阶段出了状况，整个局面都会被影响的。"
    stop se fadeout 1
#SE_VOLC 1,255,64
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDC04"),"True","img/SU_LDC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU054"
    铃 "「啊～，锅里煮开了」"
    志雄 "「好奇怪啊……」"
    hide lh0 with dissolve
#CHR_POSC 0,(320-96),0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XDA01"),"True","img/SU_XDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU055"
    铃 "「你看吧。志雄就继续切大葱和洋葱，煮南瓜和味噌汤就由我来看着吧」"
    play sound "SE03_09L"
    voice "NSU03A_SU056"
    铃 "「对，葱切好了放到这里」"
    "铃似乎看不下去了，终于离开了座位。"
    "调了一下火，灵活地给煮南瓜和味噌汤放入调料。"
    "……我可真没用啊。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XDA02"),"True","img/SU_XDA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU057"
    铃 "「可别死要面子哦」"
    志雄 "「不，我平常不是这样的……是、是真的」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XDB01"),"True","img/SU_XDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU058"
    铃 "「那就等下次再给我看吧。而且你看，一起动手不也很开心么？」"
    志雄 "「啊，嗯」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    with dissolve
    "结果到最后，我还是很没用。"
    "但和铃一起做饭非常开心，也算是收获吧？"
    jump L_NSU03A_SEL00_X
label L_NSU03A_SEL00_X:
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1,32
    scene expression Solid("000") with fade
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/EXBG09A@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/EXBG09A@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320),0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA01"),"True","img/SU_ZDA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_IN 1,32
    voice "NSU03A_SU059"
    铃 "「我开动～了」"
    play sound "SE03_37"
    "在面对面坐着的我们中间，摆放着白切肉、煮南瓜、味噌汤和米饭。 "
    "白切肉下面放了些切好的莴苣和洋葱片还有干鲣鱼。"
    "调料是橙汁、芝麻、酱油，此外还有加上橄榄油的生牛肉片。"
    "另外为了防止油腻，还准备了辣椒萝卜泥和生姜等佐料。"
    "虽然有些单调，但我觉得已经可以算是让人食欲大开的菜肴了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB02"),"True","img/SU_ZDB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU060"
    铃 "「嗯～嗯。肉很好吃，这个很适合做下酒菜啊」"
    play sound "SE03_38"
    "铃吞下一大口肉，然后将啤酒一饮而尽。"
    "吃得津津有味。"
    志雄 "「太好了，我本来还担心要是不好吃的话该怎么办呢」"
    window hide
#SE_WATC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC01"),"True","img/SU_ZDC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU061"
    铃 "「猪肉是鹿儿岛产的高级黑猪，啤酒是弁天啤酒，真是下了血本啊」"
    voice "NSU03A_SU062"
    铃 "「这就不是靠做料理的手艺，而是靠食材来决胜负了啊」"
    志雄 "「啊哈哈，露馅了呢」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC02"),"True","img/SU_ZDC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU063"
    铃 "「嗯，你能这么努力我真高兴……花费不要紧吧？」"
    志雄 "「结果就只是这种程度，也没花多少」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB02"),"True","img/SU_ZDB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU064"
    铃 "「……既然这样那就多谢你了，请我吃这么美味的一顿大餐」"
    志雄 "「呵呵，难得吃一顿美食」"
    window hide
#FADE_OUT 1,32
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    with dissolve
#FADE_IN 0,0
    "吃着这不同于平日的饭菜，我心里很开心。一转眼桌上的饭菜就被一扫而空了。"
    window hide
#FADE_OUT 0,0
#BG_COLC 0,128,128,128,128
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320),0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB02"),"True","img/SU_ZDB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_IN 1,32
    voice "NSU03A_SU065"
    铃 "「啊～，真好吃啊」"
    志雄 "「唔唔……好像吃的有点多了」"
    "果真是太得意忘形了，做得太多了……就算是两人份也太多了。"
    "好吧，剩下的饭菜明天早上再吃吧。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA01"),"True","img/SU_ZDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU066"
    铃 "「好了，来谈谈你未来的目标吧？」"
    "铃一点点地喝着剩下的啤酒，笑着对我说。"
    "明明已经喝了几瓶，却没有明显的醉意。"
    "铃最起码酒量还挺强的。"
    志雄 "「嗯，是呢，这才是今天的目的」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC05"),"True","img/SU_ZDC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU067"
    铃 "「早上也听你说了，是准备上大学吧？」"
    "铃在椅子上笔直地坐正，露出严肃的神情问道。"
    志雄 "「话虽如此，但怎么说才好呢，自己好像也没找到非上大学不可的理由……」"
    志雄 "「以这样的想法来看，上大学或许比较好吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC01"),"True","img/SU_ZDC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU068"
    铃 "「志雄果然是个认真的人呢」"
    "铃的脸上浮现出微笑。"
    "虽然也许只是苦笑。"
    志雄 "「是这样吗」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC05"),"True","img/SU_ZDC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU069"
    铃 "「我觉得，现在的学生基本上都是没有确定的理由和想要学的东西，就去上大学了吧」"
    志雄 "「话虽如此，但如果这样就太浪费时间和金钱了吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA04"),"True","img/SU_ZDA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#SET_SAVPNT
    voice "NSU03A_SU070A"
    铃 "「嗯。{w=3}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA02"),"True","img/SU_ZDA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU070B"
    extend "不过说句不好听的话，我觉得大学毕业后只要有个学历，就会对毕业后的就职有利，可以把这个当成自己的目的」"
#CLR_SAVPNT
    志雄 "「但是也有人想先到社会上积累经验吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA01"),"True","img/SU_ZDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU071"
    铃 "「这点早上也说了，那些地方需要有一技之长，不是么？」"
    voice "NSU03A_SU072"
    铃 "「要是一般的就职，志雄还是应该上大学，而且可以在大学里找到自己希望的方向」"
    志雄 "「这意见比我想像中还普通」"
    "虽然这么说，却也在我预料之中。"
    "铃对自己的事情很粗枝大叶，可除此之外，与其说是个大人，不如说是有常识的人。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA05"),"True","img/SU_ZDA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU073"
    铃 "「喂，你以为我是谁呀？普通的意见和理所当然的意见，不就是最起码的正确结论么？」"
    志雄 "「……嗯」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA01"),"True","img/SU_ZDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU074"
    铃 "「而且即使没有理由就上大学，也必将对志雄的未来起正面作用，当然如果只是抱着玩玩的心态的话肯定不行」"
    志雄 "「为了学到什么而上学……这么说就是取决于我是不是用心了？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB01"),"True","img/SU_ZDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU075"
    铃 "「就是这样」"
    "铃表示认同地点点头，随即将啤酒一饮而尽。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC05"),"True","img/SU_ZDC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU076"
    铃 "「反问你一句，志雄不想上学么？」"
    志雄 "「该怎么说呢，与其说不想上大学，不如说是想早点自立吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC02"),"True","img/SU_ZDC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU077"
    铃 "「啊，你父母的事也很复杂呢」"
    志雄 "「确实有这种感觉……吧」"
    if not persistent.dictlist[10] and persistent.show_dict:
        $persistent.dictlist[10]=True
        show screen dict_pop(i=10)
    "我和老爸的关系虽然不坏，但老爸和莉莉丝的母亲香里再婚，各种事情就变复杂了。"
    if not persistent.dictlist[12] and persistent.show_dict:
        $persistent.dictlist[12]=True
        show screen dict_pop(i=12)
    "我自己如果能独立起来，彼此的气氛就会融洽些。"
    "但这不是唯一的理由"
    "想早一点自立，长大成人，真正的理由就在眼前。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC06"),"True","img/SU_ZDC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU078"
    铃 "「但是，有可以依靠的人在身边，去依靠也不是坏事」"
    "铃望着远处说道。"
    志雄 "「但如果只是一味地依靠别人，不就无法独当一面了么？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC01"),"True","img/SU_ZDC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU079"
    铃 "「并不能这么说，要想长大成人，就需要时刻向人求助，不如说擅长学会求助的人才是成熟的人啊？」"
    志雄 "「好像明白了，又好像没明白」"
    voice "NSU03A_SU080"
    铃 "「建立起依靠与被依靠的关系是很难的」"
    志雄 "「充满了切身体会啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC02"),"True","img/SU_ZDC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU081"
    铃 "「我也曾经非常想独当一面，也做过各种各样的傻事」"
    志雄 "「铃也有过这种经历啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB02"),"True","img/SU_ZDB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU082"
    铃 "「啊哈哈哈。到了社会上之后，才发现自己就是一个小女孩」"
    志雄 "「真的么？」"
    "在我看来，铃非常优秀，优秀得让人有点不敢接近。"
    "无论从年龄上，还是从精神上。"
    "我意识到了过了那么久，自己还是个孩子……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB01"),"True","img/SU_ZDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU083"
    铃 "「是的，所以志雄没必要那么急躁，慢慢地成长就好」"
    "我能理解她说的话，但是……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC01"),"True","img/SU_ZDC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU084"
    铃 "「呵呵，看你的表情好像不太认同啊」"
    志雄 "「……」"
    voice "NSU03A_SU085"
    铃 "「毫无道理地装成熟是不对的哦」"
    志雄 "「……是么」"
    "对我而言，即使逞强也想站在铃的身旁，这是我真实的想法。"
    "不过，这样一来和铃说的一样吧。"
    "感到有一点寂寞呢……因为她看到的并不是个男人，而是个比她年幼的小男孩。"
    window hide
    stop music
    play sound "SE00_04"
    pause (16/32.0)
    志雄 "「是谁啊？这个时候？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC05"),"True","img/SU_ZDC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU086"
    铃 "「有客人么？」"
    play sound "SE00_50"
    "回过头去，门铃正不停地响着。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC04"),"True","img/SU_ZDC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU087"
    铃 "「……有种非常不好的预感」"
    志雄 "「……这种响门铃的方式好像在哪听过」"
    "这种响门铃的方式，让我想到了来访的人是谁。铃的表情也同样扭曲了。"
    stop se
    voice "NSU03A_RI026_K"
    莉莉丝 "「志～雄～！」"
    window hide
    play music "BGM10"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB04"),"True","img/SU_ZDC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「果真如此」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC06"),"True","img/SU_ZDC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "能干的编辑（自称）来了。"
    "话说回来，我说过今晚铃会过来……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC02"),"True","img/SU_ZDC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU088"
    铃 "「呜、呜、呜呜……」"
    "铃将头抱成一团。"
    志雄 "「那个，开门没关系吧？」"
    voice "NSU03A_SU089"
    铃 "「姑且，要给莉莉丝看一下的那部分写好了」"
    "铃虽然这么说，却像是躲避着什么。"
    志雄 "「真的没关系吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB05"),"True","img/SU_ZDB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU090"
    铃 "「不是，总觉得，害怕她已经成为条件反射了」"
    "铃无力地笑了，莉莉丝这家伙，已经把铃逼到这个地步了啊。"
    voice "NSU03A_RI027_K"
    莉莉丝 "「志雄，快开门啊，我来吃晚饭啦」"
    志雄 "「真拿你没办法啊」"
    show expression "img/OIBG012A@2x.png" as bg_over zorder 2 with dissolve
    play sound "SE00_00"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320),0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD04"),"True","img/RI_MBD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI028"
    莉莉丝 "「真是的，因为帮店里的忙帮到很晚，干得又热又累，所以快点让我进来吧」"
    志雄 "「我说啊，这是硬闯进来的家伙应该说的话吗？话说你来干吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD01"),"True","img/RI_MBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI029"
    莉莉丝 "「当然是来吃饭的啊，主要想吃高档肉，而且也想和铃见上一面」"
    "她劝我买高档肉，难道就是为了这么……"
    志雄 "「我说你呀，好不容易才」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD04"),"True","img/RI_MBD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI030"
    莉莉丝 "「好不容易才？怎么？我给你们添乱了？」"
    志雄 "「呜……啊，啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD06"),"True","img/RI_MBD06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI031"
    莉莉丝 "「反正是志雄，吃平常的饭菜就行了吧」"
    志雄 "「啊……不、不是这么回事，是在商量我未来的出路……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC01"),"True","img/RI_MBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU03A_RI032"
    莉莉丝 "「那有什么关系，今天这种日子我在也没事吧，别在意别在意」"
    志雄 "「不是，所以说呢……」"
    window hide
    play sound "SE01_13"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    with dissolve
    "莉莉丝趁我无言以对的时候迅速窜进了房间。"
    志雄 "「啊、喂！」"
    window hide
    stop se fadeout 0.5
    show expression "img/BG33AA@2x.jpg" as bg_over zorder 2 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160),0
#CHR_POSC 1,(320+160),0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDB05"),"True","img/SU_MDB05A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBB01"),"True","img/RI_MBB01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NSU03A_RI033"
    莉莉丝 "「铃，晚上好」"
    "莉莉丝面对着我，一反常态笑着低下了头。"
    voice "NSU03A_SU091"
    铃 "「晚、晚上好，莉莉丝」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA04"),"True","img/RI_MBA04A@2x.png") as lh1 zorder (10+1)
    with dissolve
    voice "NSU03A_RI034"
    莉莉丝 "「还有，铃代老师，之前给我看的原稿……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDC04"),"True","img/SU_MDC04A@2x.png") as lh0 zorder (10+0)
    with dissolve
    "铃的脸上呈现出紧张的神情，稍稍挺直了身子。"
    "是认识到了，莉莉丝称呼铃的笔名时，肯定会有什么事吧。"
    voice "NSU03A_SU092"
    铃 "「嗯，嗯」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC02"),"True","img/RI_MBC02A@2x.png") as lh1 zorder (10+1)
    with dissolve
    voice "NSU03A_RI035"
    莉莉丝 "「非常有意思！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDB02"),"True","img/SU_MDB02A@2x.png") as lh0 zorder (10+0)
    with dissolve
    voice "NSU03A_SU093"
    铃 "「太、太好了，真的……太好了」"
    "铃刚才还有点紧张，现在一下露出了笑容。"
    voice "NSU03A_RI036B"
    莉莉丝 "「真是的，我已经无法用言语来形容了，感想之类的我用邮件发给你吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDB03"),"True","img/SU_MDB03A@2x.png") as lh0 zorder (10+0)
    with dissolve
#REEK_CHR 0,0
    voice "NSU03A_SU094"
    铃 "「嗯嗯，我会作为借鉴的」"
#REMOVE_REEK_CHR 0
    "莉莉丝这家伙真的是典型的粉丝，然而对面倾听着的铃却因此陷入为难的境地。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDA01"),"True","img/SU_MDA01A@2x.png") as lh0 zorder (10+0)
    with dissolve
    志雄 "「那么，先吃饭吧？」"
    "肉还剩下不少，既然特意地过来了，就这么赶回去也很过分。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD01"),"True","img/RI_MBD01A@2x.png") as lh1 zorder (10+1)
    with dissolve
    voice "NSU03A_RI037"
    莉莉丝 "「当然了。志雄，你们吃完了？」"
    志雄 "「我们已经吃完了。菜都放在那了，你就吃吧。我去稍微热一下味噌汤，你等一下」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC02"),"True","img/RI_MBC02A@2x.png") as lh1 zorder (10+1)
    with dissolve
    voice "NSU03A_RI038"
    莉莉丝 "「太好了」"
    voice "NSU03A_SU095"
    铃 "「我也来帮忙吧」"
    志雄 "「那就把煮南瓜和味噌汤热一下，肉由我来做」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDC01"),"True","img/SU_MDC01A@2x.png") as lh0 zorder (10+0)
    with dissolve
    voice "NSU03A_SU096"
    铃 "「ＯＫ，洋葱片也必须再切些」"
    志雄 "「铃来做的话更快一些吧，拜托你了」"
    voice "NSU03A_SU097"
    铃 "「如果让莉莉丝等着的话，不是太可怜了么」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    with dissolve
    hide bg1 with dissolve
#BG_SWPC 0,1
#BG_PRI 1,1
#BG_PRI 0,6
#BG_GET_NOC 1,F34
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,(640/4),((448/4)+512),(640/2),(448/2)
    #show expression "img/F34@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96),0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XDA01"),"True","img/SU_XDA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#BG_BLUR 0,1
    hide bg1 with dissolve
    play sound "SE03_10L"
    志雄 "「虽然等一下也不要紧，但我怕自己一着急会切到手」"
    voice "NSU03A_SU098"
    铃 "「是谁说自己会做饭的啊」"
    "因为一起做了一次饭，这次手法变得灵活多了。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1,32
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/EXBG09A@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/EXBG09A@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
#FADE_IN 1,32
    "除了汤汁要热一下，猪肉要静置一下之外，其它的饭菜全都没问题。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320),0
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBB03"),"True","img/RI_ZBB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#MESEX_A M_NOA,A_CH_RI,NSU03A_RI039,"【りりす】「……」%K%P"
    play sound "SE03_33"
    志雄 "「好了，可以吃了」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBC03"),"True","img/RI_ZBC03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#REEK_CHR 1,0
    voice "NSU03A_RI040"
    莉莉丝 "「哎！？啊、嗯，那么，我开动了」"
#REMOVE_REEK_CHR 1
    "有什么好惊讶的？"
    "莉莉丝不知为何露出吃惊的神情。我在她面前摆放好餐具。"
    show expression "img/BG33AA@2x.jpg" as bg_over zorder 2 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320),0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDA01"),"True","img/SU_MDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NSU03A_SU099"
    铃 "「我差不多该回去了」"
    志雄 "「怎么，要回去了？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1,0
##CHR_POSC 1,640,0
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBB03"),"True","img/RI_MBB03A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .75
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR0 ,(320-160)
#MOV_CHR1 128,(320+160)
#MOV_CHR_GO 1
    voice "NSU03A_RI041"
    莉莉丝 "「哎？再待一会儿不行么？」"
    "莉莉丝赶在我开口之前挽留铃。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDB01"),"True","img/SU_MDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NSU03A_SU100"
    铃 "「我还有工作啊～」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD03"),"True","img/RI_MBD03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NSU03A_RI042"
    莉莉丝 "「明明有好多话想说的啊～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDB02"),"True","img/SU_MDB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NSU03A_SU101"
    铃 "「对不起，下次再一起吃饭吧」"
    voice "NSU03A_RI043"
    莉莉丝 "「好～吧」"
    window hide
    hide lh1 with dissolve
    "也没什么特别的理由要留下来，所以莉莉丝便又埋头吃起饭来。"
    "唉，工作的话就没办法了，原本铃就是个大忙人。"
    window hide
    stop music
#FADE_OUT 1,32
    scene expression Solid("000") with fade
    stop music
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG39NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG39NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320),0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDA01"),"True","img/SU_LDA01A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
    play sound "SE00_00"
    play sound "SE05_16L"
    pause (32/32.0)
#BG_BLUR 0,1
#FADE_IN 1,32
    play music "OBGM17"
    "送行的时候，我把铃喝剩下的啤酒递给她。"
    志雄 "「今天谢谢你了」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDB01"),"True","img/SU_LDB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU102"
    铃 "「没什么，我才要谢谢你，给我这么好的礼物」"
    志雄 "「不用客气，倒是莉莉丝添了麻烦，真对不起」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDB02"),"True","img/SU_LDB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU103"
    铃 "「没事啦，我回去工作了」"
    "铃笑着挠了挠头。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDC01"),"True","img/SU_LDC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU03A_SU104"
    铃 "「那么，明天见」"
    志雄 "「晚安」"
    window hide
#SE_VOLC 1,128,64
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    with dissolve
#BG_BLUR 0,0
    "铃心情愉快地离开了……或许也留下了一点遗憾吧。"
    "话说回来，也必须好好考虑一下自己前进的道路了。"
    "虽然铃对我说应该继续上学……"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1,32
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop se
    stop sound
#FADE_IN 0,0
    $ renpy.end_replay()
    return
#label THREAD_SUZU_NEAR
#CHR_SCL_AUTOC 0,288,288,1,F123,64,1
#CHR_SCL_SAVEC 0
#EOT