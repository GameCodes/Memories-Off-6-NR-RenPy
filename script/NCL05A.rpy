label NCL05A:
    $currentlabel = "NCL05A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '08'
    $day = '01'
    $date = '2'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 5,CAL_0801
    show expression "img/NIMG15N-568h@2x.jpg" as cal zorder 5
    show expression "img/08_01_TUESDAY@2x.png" as cal_date zorder 6:
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
    scene expression "img/BG15MA@2x.jpg" as bg0 with dissolve
    play sound "SE05_14L"
    pause (32/32.0)
#FADE_IN 1,128
#SE_VOLC 1,(64/2)
    play music "OBGM27"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    志雄 "「唉……」"
    "我凝望着日历，不由自主地发出一声叹息。"
    "和克罗艾学姐一起去病房探望父亲之后，已经过去了６天。"
    "可是，学姐一直也没有再联系我。"
    志雄 "「嘛，毕竟也那么长时间没有团聚了，积攒下来的话肯定很多呢。」"
    "莫名其妙的担心学姐的父亲会不会又晕倒，想来只是找了一个学姐的影子，而后又过份放大了罢了。"
    "不过，我觉得无论什么问题，只要一家人能够团聚，就是再好不过了。"
    "只是，有一件事情令我很在意……"
    志雄 "「那个时候的学姐，总觉得有些不太对劲呢。」"
    "又想起在病房看到的那一幕。明明是一家人的团聚，却感觉只有克罗艾学姐一直都没能融进那个环境里。"
    "果然，１２年多的隔阂不是这么简单就能解决的。"
    志雄 "「总觉得心情无法平静下来呢。」"
    "情不自禁地低语了两句。"
    "作为备考生，本应好好复习……"
    "打开摊在桌子上的参考书和笔记本，可心烦意乱的我无论如何也无法集中精力。"
    "说起来，像这样和克罗艾学姐多日不见的情况还是第一次吧？"
    "刚开始交往的时候每天在学校都形影不离，学姐毕业之后也基本保持两天见一面。"
    志雄 "「可是像这样一周都没见，甚至都没有什么联系的情况……」"
    "于是就这么一副狼狈相了。要是１２年见不到的话，那我岂不是会相思而亡？"
    志雄 "「１２年吗……？」"
    "如果１２年没见的话。我与那个人，还会像以前一样地交谈吗？会马上就记起所有事情吗？"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG33AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG33AA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    play sound "SE00_04"
#FADE_IN 1
    "门口的敲门声打断了我的混乱的思绪。"
    志雄 "「嗯……？」"
    "好像我不知道什么时候在客厅睡着了。"
    "看了一眼表，马上就要到中午了。"
    window hide
    play sound "SE00_04"
    pause (32/32.0)
    play sound "SE03_28"
    "听到敲门声再次响起，我慌忙爬了起来。"
    "也许外面的人已经不知道敲了多少回了。"
    play sound "SE01_13"
    志雄 "「啊！在呢，马上就来！」"
    window hide
    stop se
    show expression "img/OIBG012A@2x.png" as bg_over zorder 2 with dissolve
    "我马上飞奔到门口，跳过了确认门外是谁的过程直接打开了房门。"
    window hide
    play sound "SE00_00"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "BGM04"
    voice "NCL05A_KU000"
    克罗艾 "「早上好。」"
    "阔别６日的重逢，克罗艾学姐站在门外。"
    志雄 "「早上好这……已经快要中午了吧？」"
    "面对我的反问，学姐尴尬地地笑了笑。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB04"),"True","img/CL_MAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU001"
    克罗艾 "「对不起。其实，早上就想要过来了，可是怎么也溜不出来……」"
    志雄 "「溜出来？什么——」"
    "说到这里，我才发现学姐的脚下，还放着一个人大小的手提包。"
    志雄 "「呃，这是个？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU002"
    克罗艾 "「这个？生活用品……」"
    志雄 "「呃，为什么来我家拿着这些东西呢？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB02"),"True","img/CL_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU003"
    克罗艾 "「因为，从今天开始我要住在志雄家了啊，带随身衣物是必要的吧？」"
    志雄 "「……啊？」"
    "学姐轻描淡写地，像什么事都没发生般地说道。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC01"),"True","img/CL_MAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU004"
    克罗艾 "「啊，还没吃午饭呢吧？」"
    志雄 "「啊？嗯，接下来就要吃呢」"
    voice "NCL05A_KU005"
    克罗艾 "「我已经买了食材了哦，很快就能做好。志雄稍微等我一下吧～」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "说了这样的话，学姐便走进屋，径直向厨房走去。"
    show expression "img/BG33AA@2x.jpg" as bg_over zorder 2 with dissolve
    志雄 "「诶！？」"
    "还没能理解状况的我，不禁冒失地叫出声来。"
    "从今天开始住下……学姐她？"
    "这样嘛，每天都能和学姐在一起的话真的很高兴……不对！"
    play sound "SE03_66"
    志雄 "「那个，学姐。」"
    voice "NCL05A_KU006"
    克罗艾 "「什——么——？」"
    "厨房里开始传来叮铃咣当的声音。"
    "看起来，已经开始做饭了。"
    "尽管如此，还是要先问一下吧。"
    "我迅速地安顿好学姐的行李，然后奔向了厨房。"
    志雄 "「……学姐父亲的病，怎么样了？」"
    stop se
    stop music fadeout 1
    "学姐没有回应，只是一瞬间，厨具碰撞的响动声也停止了，只留下令人不安的沉默。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC06"),"True","img/CL_MAC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL05A_KU007"
    克罗艾 "「嗯……」"
    voice "NCL05A_KU008"
    克罗艾 "「妈妈她，在照顾着呢……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE03_09L"
    "接着，学姐便又集中精神开始做饭了……"
    window hide
#SE_VOLC 1,64
#BG_SET_BACK 
#BG_INIC 1
#BG_INIC 3
#BG_POSC 1,(60),0,640,448
    scene expression "img/EXBG10AA@2x.png" as bg1 with dissolve
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_SWPC 0
#BG_SWPC 2
#BG_ERSWC 1,3,BG_NOFADE
#BG_PRI 1
#BG_PRI 3
#BG_PRI 0
#BG_PRI 2
    "还是先不要再打扰学姐了吧。这么想着，便走向摊开着的参考书。"
    "自私地说，只要见到学姐的话，到现在为止的所有的不安，都在一瞬间，彻彻底底地消失了。"
    志雄 "「可是……」"
    "学姐，真的只是想住到我家来吗？"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    pause (32/32.0)
    play sound "SE03_24L"
#FADE_IN 1
    "我边听着学姐做饭声音边看着参考书，不一会儿，有谁趴到了我的背上。"
    window hide
    play sound "SE03_14"
#QUA3_ALL 
    voice "NCL05A_KU009"
    克罗艾 "「稍微，休息下吧～」"
    志雄 "「那个，学姐？」"
    "背后传来了学姐的体温和心脏的跳动声。"
    志雄 "「正做着饭，放下厨房那边不管可以吗……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,640
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XAC01"),"True","img/CL_XAC01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter .65
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR0 128,(320+96)
#MOV_CHR_GO 1
    voice "NCL05A_KU010"
    克罗艾 "「没关系的。只是在煮面条而已，稍微离开一下没关系的。」"
    "边说着，学姐又贴紧了身体。"
    "怎么说呢，真是好害羞的状态……"
    voice "NCL05A_KU011"
    克罗艾 "「我有好好看着时间，也有放盐进去，所以我想不用担心水会扑出来。」"
    志雄 "「这样的话倒是没关系……」"
    "学姐微微地发出了低沉的耳语。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XAC03"),"True","img/CL_XAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU012"
    克罗艾 "「妈妈她，照顾爸爸去了……」"
    "这是，刚才说过的话。"
    window hide
    play music "OBGM20"
    voice "NCL05A_KU013"
    克罗艾 "「她说迄今为止一直让家里空荡荡的，也让我平添了许多辛苦，所以今后她想好好补偿我一下……」"
    "学姐抱着我的手臂，稍稍地用力起来。学姐口中一字一句挤出的话语，隐约透出了困惑与无奈。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XAC02"),"True","img/CL_XAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU014"
    克罗艾 "「可是我，并没有感到痛苦之类的。虽然曾经稍微有些状况，不过隔了那么久能和爸爸好好说话了，我真的很开心……」"
    志雄 "「学姐……」"
    voice "NCL05A_KU015"
    克罗艾 "「现在本来应该会更好的，可是，比起母亲她们回来之前的时候，总觉得放宽的心中又多了些什么……」"
    "说到这里，学姐轻轻地笑了笑。是带有些许自嘲的笑吧。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XAB04"),"True","img/CL_XAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU016"
    克罗艾 "「哈哈，好奇怪呢。不过，妈妈回来了，我真的是很高兴。尤其是自己有了妹妹……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XAB06"),"True","img/CL_XAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU017"
    克罗艾 "「从前呢，我曾经撒娇着说想要个妹妹。妈妈，是认真的记住了那些事吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XAB01"),"True","img/CL_XAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU018"
    克罗艾 "「１１岁了。明明才刚刚见面，却已经是能说话的年纪了……」"
    志雄 "「……」"
    "我，什么也没有说。现在还是做一个专注的聆听者更好吧。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XAC02"),"True","img/CL_XAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU019"
    克罗艾 "「该怎么办才好呢。总觉得什么都说不出来……」"
    stop music fadeout 1
    play sound "SE03_100"
    "这个时候，厨房里传来了水滴在火上的声响。"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XAC05"),"True","img/CL_XAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
#BG_SET_BACK 
#REEK_CHR 0
    voice "NCL05A_KU020"
    克罗艾 "「啊！！不好！！」"
#REMOVE_REEK_CHR 0
    window hide
    play sound "SE01_13"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "学姐赶忙站起身，转身冲进了厨房。"
    stop sound fadeout 1
    play sound "SE03_101"
    voice "NCL05A_KU021"
    克罗艾 "「啊！煮过头了……」"
    "从厨房里传来了学姐悲痛地尖叫。"
    "听到那个声音，我的肩膀也一下子没了力气。"
    志雄 "「真没办法呢……」"
    show expression "img/BG15AA@2x.jpg" as bg_over zorder 2 with dissolve
    "我也立刻直起腰站了起来。让克罗艾学姐一个人收拾残局，怎么也是办不到的吧。"
    志雄 "「学姐，当心别烫着！」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/EXBG09A@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/EXBG09A@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC02"),"True","img/CL_ZAC02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (32/32.0)
#FADE_IN 1
    play music "OBGM17"
    "桌子上放着色拉和汤。还有稍微有些多的意大利面。"
    voice "NCL05A_KU022"
    克罗艾 "「呃，对不起……」"
    志雄 "「没关系啦。是不是做的有点多？」"
    voice "NCL05A_KU023"
    克罗艾 "「真是平生最大的败笔……」"
    志雄 "「真的没关系的啦～」"
    "说着，我用叉子卷起一些放到了嘴里。"
    "嗯，十足的美味。"
    志雄 "「比我做的好吃太多了！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB05"),"True","img/CL_ZAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU024"
    克罗艾 "「志雄……你偷吃哦～」"
    志雄 "「哎呀，对不起……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU025"
    克罗艾 "「好啦，志雄想说什么我明白啦。那么，咱们开动吧～」"
    志雄 "「对啊。我开动——」"
    window hide
    play sound "SE02_06L"
    "正当我要开始动筷的时候，家里的电话突然响了起来。"
    志雄 "「抱歉，我失陪一下。」"
    voice "NCL05A_KU026"
    克罗艾 "「嗯，我等着你。」"
    show expression "img/BG33AA@2x.jpg" as bg_over zorder 20 with dissolve
    "我从椅子上站起，向电话走去。"
    window hide
    play sound "SE02_16"
    志雄 "「您好，我是塚本。」"
    stop music fadeout 1
    voice "NCL05A_EL000_K"
    エリーズ？ "「那个，我是嘉神川……」"
    "听到话筒另一端传来的声音，我不禁回头看向饭桌的方向。"
    志雄 "「莫非是，学姐……克罗艾的母亲？」"
    voice "NCL05A_EL001_K"
    爱丽丝 "「是的。其实，我是稍微有点事想询问一下。」"
    志雄 "「是什么事呢？」"
    voice "NCL05A_EL002_K"
    爱丽丝 "「……克罗艾，是去你那里打扰了吧？」"
    志雄 "「嗯，要让她听电话吗？」"
    voice "NCL05A_EL003_K"
    爱丽丝 "「不，不用了。要是在塚本那里的话，我就可以放心了。」"
    window hide
    play music "OBGM08"
    志雄 "「那个，克罗艾她——」"
    voice "NCL05A_EL004_K"
    爱丽丝 "「帮着拿行李，实在是麻烦你了呢……」"
    志雄 "「是……」"
    voice "NCL05A_EL005_K"
    爱丽丝 "「这段时间，可以让那孩子留宿在你那里吗？」"
    志雄 "「诶？当然可以，那倒是没有关系。」"
    voice "NCL05A_EL006_K"
    爱丽丝 "「给你添麻烦了真是不好意思。不过，我想让那个孩子按照自己的想法去做。」"
    志雄 "「……」"
    voice "NCL05A_EL007_K"
    爱丽丝 "「……那么就说到这里吧，我会再联络的。」"
    window hide
    play sound "SE02_08"
    "结束通话后，我呆若木鸡地凝视了话筒好一阵子。"
    "电话里听到的学姐母亲的声音，给我一种与之前完全不同的印象。"
    "怎么形容呢，虽然我能听出来她很担心学姐，可是言语之间却仿佛间隔了很遥远的距离一般。"
    "对了，就和学姐与父亲冷淡的时候一样呢……"
    "还有，就是没有打学姐的手机，而是打到我家的座机上。"
    "不过我和学姐正在交往的事情，因为是很八卦的话题，所以出乎意料的相当有名呢。按理说问一下学校的相关人士马上就能知道了……"
    "一直到找到我家为止，一定都有在拼命打听吧……"
    play sound "SE02_07"
    "总之，她们并没有引起不必要的争吵，我也稍微放心了些。"
    hide bg_over
#BG_GET_NOC 0,F24
#BG_SET_BACK 
#BG_INIC 2
#ROUTINE_STA
#BG_UVC 2,((640/4)+30),(448/4),(640/2),(448/2)
    #show expression "img/F24@2x.jpg" as bg2 zorder 2 with dissolve
#BG_BLUR 2
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB05"),"True","img/CL_ZAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_ALP_AUTOC 0,0,0,1,48
#ROUTINE_STP
    voice "NCL05A_KU027"
    克罗艾 "「谁打来的啊？」"
    "回到饭桌上，学姐用担心的神情询问着我。"
    志雄 "「学姐的妈妈打来的……」"
    voice "NCL05A_KU028"
    克罗艾 "「是吗……」"
    "学姐似乎并不意外，但紧接着，又低下头，沉默不语。"
    志雄 "「可以问点问题吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB04"),"True","img/CL_ZAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU029"
    克罗艾 "「请说……」"
    志雄 "「我想学姐一定是因为吵架跑出来了，不过好像并不是那样呢……」"
    voice "NCL05A_KU030"
    克罗艾 "「是呢。与其说是吵架，不如说是自己闹别扭……」"
    voice "NCL05A_KU031"
    克罗艾 "「实在无法忍受，就跑了出来……」"
    "克罗艾学姐的眉宇间充满了痛苦。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC01"),"True","img/CL_ZAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU032"
    克罗艾 "「妈妈她说今天给我做最喜欢吃的东西……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC03"),"True","img/CL_ZAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU033"
    克罗艾 "「我，无论如何也说不出口。我已经……不喜欢那个了……」"
    志雄 "「学姐……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC02"),"True","img/CL_ZAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU034"
    克罗艾 "「很好笑吧。」"
    志雄 "「没有那种事哦。」"
    voice "NCL05A_KU035"
    克罗艾 "「是吗？」"
    志雄 "「因为，已经１２年不见了吧？只是还没能想办法消除相互之间的隔阂罢了。」"
    "这种空缺，一定会随着时间的前行，慢慢被填补上的。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB02"),"True","img/CL_ZAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU036"
    克罗艾 "「是呢……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB04"),"True","img/CL_ZAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU037"
    克罗艾 "「可是，现在还是想稍微保持距离。」"
    "克罗艾学姐用十分抱歉的神情窥视着我的脸。"
    voice "NCL05A_KU038"
    克罗艾 "「所以，只要一阵子就好，让我留在这里可以吗？」"
    志雄 "「当然了。请把这里当做自己的家吧。」"
    voice "NCL05A_KU039"
    克罗艾 "「谢谢……」"
    志雄 "「那就快吃饭吧，面都要凉了！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU040"
    克罗艾 "「嗯。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB06"),"True","img/CL_ZAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL05A_KU041"
    クロエ・志雄 "「我开动了！」"
    "嗯，太好吃了。"
    "对学姐来说也许是失败了，不过对于我来说，难得的全熟意大利面也别有一番风味呢。"
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
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT