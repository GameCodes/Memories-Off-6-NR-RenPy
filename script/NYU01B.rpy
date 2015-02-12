label NYU01B:
    $currentlabel = "NYU01B"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '20'
    $date = '4'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 3,CAL_0720
    show expression "img/NIMG15K-568h@2x.jpg" as cal zorder 5
    show expression "img/07_20_THURSDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG07AA3@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG07AA3@2x.jpg" as bg0 with dissolve
    play music "BGM10"
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
    "高三生活的第一个学期终于结束了。"
    "刚开始上学的时候，收到成绩通知单是一件非常吓人的事情。"
    "可是，现在已经是从小学算起的第十二年。"
    "由于根据考试的结果可以预估大概的分数，于是能做的就是等待既定的通知单到来。"
    "然后……高中最后一个暑假终于到来了。"
    window hide
    show expression "img/BG08AA@2x.jpg" as bg_over zorder 2 with dissolve
    pause (16/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC02"),"True","img/RI_MAC02A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NYU01B_TO000"
    亨 "「来了！　我亲爱的暑假！」"
    voice "NYU01B_RI000"
    莉莉丝 "「大海，高山还有夏日的庆典，全部都在召唤着我！」"
    "大概是在因为即将到来的升学考试而导致班级里的气氛过于压抑。"
    if not persistent.dictlist[7] and persistent.show_dict:
        $persistent.dictlist[7]=True
        show screen dict_pop(i=7)
    "刚出教室，亨和莉莉丝就在那里莫名地亢奋着。"
    志雄 "「哈～还真是羡慕你们这种无忧无虑的状态……」"
    "高中最后一个暑假。"
    "对于备考生来说，意味着校园决战的开始。"
    "这对于我面前的两人来说，也不例外。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA05"),"True","img/RI_MAA05A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NYU01B_TO001"
    亨 "「喂喂，离考试还有半年时间呢，这基本没用吧。」"
    voice "NYU01B_RI001"
    莉莉丝 "「就是说啊，只顾着学习而让暑假白白过去不是很可惜吗？」"
    志雄 "「想到半年后的考试决定着你之后的命运，你们就不能紧张点么？」"
    "不难想象，半年后考试成绩出来的时候，两人扭曲的表情。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD02"),"True","img/RI_MAD02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01B_RI002"
    莉莉丝 "「不愧是有女朋友共度暑假的人，完全不用担心该怎么打发时间呢！」"
    voice "NYU01B_TO002"
    亨 "「真是的，像我这种没有女朋友的……」"
    志雄 "「喂喂，不要乱换话题……」"
    "本想向他们重申高考的重要性，反而被他们机智地岔开了话题。"
    "当然，上帝的调皮起来的时候总是发生意想不到的剧本，这次也不例外。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_SAA05"),"True","img/YU_SAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01B_RI003"
    莉莉丝 "「啊。刚说到……」"
    voice "NYU01B_TO003"
    亨 "「结乃同学！这边这边！」"
    "结乃偏偏在这时候经过这里，看起来是正要去学生会。"
    "表面上看，对我不利的局势将扭转为势均力敌的２对２，不过……"
    "但是对于这两个恶魔级别的捣蛋专家来说，人越多似乎更能体现他们的邪恶本色。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 1,(320-160)
#CHR_POSC 2,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC01"),"True","img/RI_MAC01A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAA01"),"True","img/YU_MAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    voice "NYU01B_RI004"
    莉莉丝 "「现在正在拷问志雄在暑假里跟结乃有什么计划呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC02"),"True","img/RI_MAC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU01B_RI005"
    莉莉丝 "「真的……要这么做吗？」"
    志雄 "「等等……！！{w}别，别这样！」"
#MESA A_CH_SI,"【志雄】「等等……！！　"
#VO_WAT VO_WAIT_START
#VIB_DOUKI
#QUA3_ALL 
#VIB_STP 
#MESX "别，别这样！」%K%P"
    window hide
#CHR_SET_BACK
#CHR_BLUR 1
#CHR_BLUR 2
#CHR_INIC 0
#CHR_ALPC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAB02"),"True","img/TO_XAB02A@2x.png") as lh0 zorder (20-0):
        ypos 0.0
    with dissolve
#CHR_POSC 0,(-160)
#BG_BLUR 0
#ROUTINE_STA
#CHR_POS_AUTOC 0,(320-160),0,1,0
#CHR_POS_AUTOC 1,0,1,0
#CHR_ALP_AUTOC 0,128,0,1
#ROUTINE_STP
    voice "NYU01B_TO004"
    亨 "「啊哈～我们两个男人就去深入研究一下正确的恋爱观吧！」"
    "我想要阻止莉莉丝诱导式的拷问，却被亨捂住嘴吧拖走了。"
    window hide
    pause (16/32.0)
#BG_BLUR 0
    show expression "img/BG08AA@2x.jpg" as bg0 zorder 0 with dissolve
#ROUTINE_STA
#CHR_BLUR 1
#CHR_BLUR 2
#CHR_PRIC ID_ALL
#CHR_SORT 0,2
#ROUTINE_STP
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAC01"),"True","img/YU_MAC01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU01B_YU000"
    结乃 "「计划……？志雄学长都说了什么啊？」"
    voice "NYU01B_YU001"
    结乃 "「目前，除了一起去芦鹿岛烟花大会就没有别的什么计划了呢……」"
    "正如结乃所说，计划目前也只到这个地方为止。"
    "而且由于暑假期间也会因为学生会的事情常常见面，应该没有必要特意去做些安排，顺其自然就好。"
    voice "NYU01B_RI006"
    莉莉丝 "「哦？那个烟花大会啊，那之后……难道，不是吧……我已经不好意思再接着说下去了。」"
    window hide
#CHR_SET_BACK
##CHR_INIC 0
##CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAB02"),"True","img/TO_XAB02A@2x.png") as lh0 zorder (20+0):
        ypos 0.0
    with dissolve
    voice "NYU01B_TO005"
    亨 "「到了夏季，就连晚熟的志雄也变得大胆起来了吗……」"
    志雄 "「呃——！！」"
    "从诱导盘问到捏造真相……"
    "邪恶二人组打出了一套超强组合技，真是没办法啊。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB06"),"True","img/YU_MAB06A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    "先不说因为亨太过用力而导致极度缺氧的我，就连结乃也……"
    志雄 "（呃，这？）"
    "不知道为什么，结乃似乎一反常态的淡定。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAA05"),"True","img/YU_MAA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU01B_YU002"
    结乃 "「没什么……志雄学长才不是那种人。」"
    stop music fadeout 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAB04"),"True","img/TO_XAB04A@2x.png") as lh0 zorder (20-0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA03"),"True","img/RI_MAA03A@2x.png") as lh1 zorder (10+1)
    voice "NYU01B_TO006"
    亨 "「唉？」"
    "正准备乘胜追击的亨听到结乃的话楞了一下，我抓紧机会甩开他的手，大口的喘着气。"
    "莉莉丝也是一样，被结乃的话弄的不知所措。"
    "结乃是已经对这种玩笑免疫了吗，还是说……"
    voice "NYU01B_YU003"
    结乃 "「还有学生会的事情要做，不和你们闹了，志雄学长也要快些赶过来哦。」"
    志雄 "「好，好的……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "总算从亨的手上逃了出来，两人似乎还没缓过来，连对我的调侃也戛然而止了。"
    "结乃对我们行了礼，转身走向学生会室。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAD02"),"True","img/RI_LAD02A@2x.png") as lh0 zorder (20-0):
        ypos 0.0
    with dissolve
    voice "NYU01B_RI007"
    莉莉丝 "「啊……！混蛋志雄，怎么会这么受人信赖！」"
    voice "NYU01B_RI008"
    莉莉丝 "「简直不可饶恕！」"
    play sound "SE04_07"
    志雄 "「痛，很痛唉！」"
#THREAD_STA 1,THREAD_QUA_WIN
#VIB_DOKA 
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESA A_CH_SI,"【志雄】「痛，很痛唉！」"
#THREAD_WAT 1
#WIN_POS 0,0
#VIB_STP 5
#MESX "%K%P"
    "调戏失败的莉莉丝似乎内心极度不爽，倒霉的自然是我。"
    "一阵子没被踢了，突然这么一下真是格外的痛啊。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAA03"),"True","img/TO_LAA03A@2x.png") as lh0 zorder (20-0):
        ypos 0.0
    with dissolve
    voice "NYU01B_TO007"
    亨 "「你们，发生了什么吗？」"
    志雄 "「不，没什么吧……」"
    "亨似乎察觉到了结乃声音里隐藏的异样。"
    "我只有尴尬的笑了笑，模棱两可的回应了他一下。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    志雄 "（不知怎么了，有些奇怪……）"
    "总觉得，从『同居未遂』（铃后来便一直这么称呼这件事）后，结乃就变得有些过分冷淡。"
    "在学生会还是像以前那样工作，放学也是一起回家。"
    "可是，一起度过的时间和身边的气氛……从那天开始就有些不一样了。"
    志雄 "（算了，还是在烟花大会上找时间和她谈谈心吧。）"
    "要消除这微妙的不协调感，也只有这样了。"
    "于是，因为一个完全不同于亨和莉莉丝的理由，我也开始期待起暑假的到来。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
#CHR_PRIC ID_ALL
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop se
    stop sound
    stop music fadeout 1
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_QUA_WIN
#TH_QUAKE_WIN 4
#EOT
