label NCL08A:
    $currentlabel = "NCL08A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '08'
    $day = '08'
    $date = '2'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 2,CAL_0808
#FADE_OUT 1,32,COL_WHITE
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 1
#BG_INIC 2
##BG_POSC 0,(72),0,640,448
##BG_POSC 2,(72),0,640,448
#BG_SETTC 0,1,2,EXBG10AA,NIMG01B,EXBG10AA
#EFF_STAC 0,CLOUD_B,EFF_NOSKIP
    scene expression "img/EXBG10AA@2x.png" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB05"),"True","img/CL_ZAB05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_IN 1,128
    play music "BGM04"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "外面万里无云，头顶上是澄澈的青空，是个适合出门的好天气。"
    "不过我却紧锁眉头，为了复习考试而全力奋斗。身在开着冷气的屋子本应该很舒服，但我却烦恼不断。"
    window hide
#MUS_VOL 128
#EFF_STPC 0,EFF_SKIP
    hide bg1 with dissolve
    voice "NCL08A_KU000"
    克罗艾 "「志雄。那里有错误哦！」"
    志雄 "「诶，真的吗？」"
    voice "NCL08A_KU001"
    克罗艾 "「嗯。怎么了？　今天老是出现这样简单的失误。」"
    "学姐注视着我，脸上写满了担心。"
    "我稍微定了定心，尽可能的用很有干劲的声音说道。"
    志雄 "「没有，只是有些走神……已经不要紧了。」"
    voice "NCL08A_KU002"
    克罗艾 "「那就好。」"
    "语气里显然并没有完全接受我的说辞，不过看渐渐舒缓下来的表情，也说明她不再深究了。"
    window hide
#BG_BLUR 0
#CHR_BLUR 0
#FILT_IN 48,0,COL_DARK2
    "也难怪学姐会担心。"
    "今天的学习才刚刚开始两个小时了。在这段时间里，这样的失误已经重复五次了。"
    "虽然说，只要把全部的注意力放在学习上就行了……"
    "不过此刻我心里却充满了不安与焦躁。"
    "两件事占据着我大脑内本身就不是和富足的资源。"
    "一件事是关于前途的。暑假已经过去了一半，可『志愿调查表』上依然空空如也。"
    "已经足够认真地去考虑了……或者说，烦恼的主要原因就是因为过分认真的考虑，权衡各方面的信息，结果却沦落到了完全不知道该怎么办好的地步了。"
    "总之，这件事在暑假结束前要得出结论……"
#ROUTINE_STA
#CHR_INIC 1
#CHR_PRIC 1
#CHR_PRIC 0
#FILT_PRI 5
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB05"),"True","img/CL_ZAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#ROUTINE_STP
#CHR_BLUR 0
#CHR_PRIC 0
    hide lh1 with dissolve
    "另外……"
    window hide
#BG_BLUR 0
#FILT_OUT 48
#FILT_PRI 1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB03"),"True","img/CL_ZAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL08A_KU003"
    克罗艾 "「……我的脸上有什么东西吗？」"
    志雄 "「啊，没。没什么……」"
    "完全没注意到，发呆的时候一直看着学姐。听到学姐的话后，我慌忙移开了视线。"
    voice "NCL08A_KU004"
    克罗艾 "「志雄真奇怪……」"
    window hide
#BG_BLUR 0
#FILT_IN 48,0,COL_DARK2
    "另外一件事就是关于克罗艾学姐的了。说的再确切一点，就是学姐和她的父母之间的事。"
    "学姐已经在我家住下快一周了。这段时间里，克罗艾学姐和父母的交流那屈指可数。"
    "而那有限的几次，也都很短，大多发生在她去医院探望父亲的时候。"
    "除此之外学姐就一次也没有去见过自己的父母了。"
    "当初母亲离开的事情应该在学姐心里留下了很深的伤痕。"
    "所以这也不是着急就能解决的事情……"
    "可是像这样，彼此之间没有什么接触，就算经过再长的时间，也无法缩短距离的吧。"
    window hide
#BG_BLUR 0
#FILT_OUT 48
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB05"),"True","img/CL_ZAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL08A_KU005"
    克罗艾 "「你又做错了……」"
    志雄 "「啊……」"
    "因为心不在焉，结果又是在只要注意一下就能解出的地方出错了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAA01"),"True","img/CL_ZAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL08A_KU006"
    克罗艾 "「好啦，休息一下吧！」"
    志雄 "「诶？　还没有完成预定的习题量……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAA03"),"True","img/CL_ZAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL08A_KU007"
    克罗艾 "「就算学再长的时间，精神不集中的话也没有意义的。这种时候，比起强迫自己继续学还是休息一下更好吧。」"
    "确实……像现在这样继续下去，脑子里也记不住什么东西。"
    志雄 "「知道了。要不要喝点茶？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAA01"),"True","img/CL_ZAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL08A_KU008"
    克罗艾 "「我来吧，志雄好好休息就行了。休息完之后，可要进行测验的哦～」"
    志雄 "「诶？　又要来吗？」"
    voice "NCL08A_KU009"
    克罗艾 "「只是盯着参考书看是不够的吧？　学习就是要伴随着这样的刺激进行的哦～」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "说着学姐向厨房走去。"
    志雄 "「啊，怎么办啊……今天学的完全没有记住啊……」"
    window hide
    play sound "SE02_06L"
    "就在我叹气的时候，电话铃响了。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/BG33AA@2x.jpg" as bg1 with dissolve
#BG_ERSWC 0,2,BG_NOFADE
#BG_POSC 0,0,0,640,448
#BG_POSC 2,0,0,640,448
#BG_SWPC 0
#BG_PRI 1
#BG_PRI 0
    pause (32/32.0)
    play sound "SE02_16"
#MUS_VOL 64
    志雄 "「喂，我是塚本。」"
    voice "NCL08A_EL000_K"
    爱丽丝 "「喂，塚本君吗？　我是嘉神川。」"
    "电话是学姐的母亲打来的。"
    志雄 "「请问有什么急事吗？」"
    "我有些紧张地问道。"
    "克罗艾学姐的母亲上次打来电话还是在学姐从家里逃出来的时候。也许是有什么紧急的事情吧？"
    "不知道是不是察觉到了我的紧张，学姐的母亲像是为了让我安心一样，用沉着的声音告诉我说。"
    voice "NCL08A_EL001_K"
    爱丽丝 "「这边没有什么变故呢。只是，有点事，想要拜托塚本君……」"
    志雄 "「嗯。」"
    voice "NCL08A_EL002_K"
    爱丽丝 "「那个，如果有时间的话，想要去你那里拜访一下……不知道方便吗？」"
    志雄 "「嗯，没问题的。您还在医院吗……？」"
    voice "NCL08A_EL003_K"
    爱丽丝 "「嗯。这就准备从医院出来了。」"
    志雄 "「可以稍微等一下吗？」"
    voice "NCL08A_EL004_K"
    爱丽丝 "「诶？」"
#MUS_VOL 128
    "我没有挂断，正准备把身体转向克罗艾学姐在的厨房方向。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC02"),"True","img/CL_MAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "不过，学姐已经紧贴在我身后，关心着这边的情况了。"
    voice "NCL08A_KU010"
    克罗艾 "「……妈妈打来的吗？」"
    志雄 "「嗯。要接吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC05"),"True","img/CL_MAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#REEK_CHR 0
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NCL08A_KU011"
    克罗艾 "「诶！　那个，现在有点……」"
#THREAD_STP 1
#REMOVE_REEK_CHR 0
    "学姐一度逃避地把视线挪开，但之后视线终于又回到了我的身上。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC02"),"True","img/CL_MAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL08A_KU012"
    克罗艾 "「那个，妈妈有什么事吗？」"
    志雄 "「好像找学姐有些事。现在还在医院……要过去吗？」"
    "听到我的话，学姐稍稍的思考了下，微微的点了点头。"
    voice "NCL08A_KU013"
    克罗艾 "「嗯。对爸爸的病情也有些在意。」"
    志雄 "「明白了。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我确认学姐的回答后，再次拿起话筒。"
#MUS_VOL 64
    志雄 "「喂，久等了。」"
    voice "NCL08A_EL005_K"
    爱丽丝 "「没关系。」"
    志雄 "「我们现在去您那边拜访。」"
    voice "NCL08A_EL006_K"
    爱丽丝 "「你们方便吗？」"
    志雄 "「嗯。学姐也正好想要去探望的。」"
    voice "NCL08A_EL007_K"
    爱丽丝 "「这样啊。我知道了。那我在这里等你们。」"
    志雄 "「那我就先挂了。」"
    window hide
    play sound "SE02_08"
#MUS_VOL 128
    play sound "SE02_07"
    "就在我挂断电话前，我好像听到了学姐的母亲发出了一声放心的叹息。"
    "学姐的母亲也一定在担心学姐的吧。"
    志雄 "「得做些什么了……」"
    "自己竟不自觉的把心里想的这句话漏了出来。我慌忙闭上嘴。幸运的是，克罗艾学姐好像并没有在意。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC02"),"True","img/CL_MAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL08A_KU014"
    克罗艾 "「抱歉，本来是在学习的，却因为我的原因……」"
    志雄 "「别这么说，我从来都没有觉得学姐给我添过麻烦哦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC01"),"True","img/CL_MAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL08A_KU015"
    克罗艾 "「谢谢……」"
    志雄 "「没有没有，这是应该的～」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "说起来，学姐的母亲究竟有什么话要说呢……"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG80AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG80AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA06"),"True","img/CL_LAA06A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (32/32.0)
    克罗艾 "……"
    "在病房前站着的克罗艾学姐，和以往一样，一副十分紧张的表情。"
    "握着在路上花店买的花束的手，稍稍地颤抖着。"
    志雄 "「那就进去吧。」"
    "我尽可能让自己的声音听起来很温柔，学姐静静地点了点头。"
    "我把手伸向房门。就在我刚要敲门的时候，学姐伸手阻止了我。"
    志雄 "「学姐？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA02"),"True","img/CL_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL08A_KU017"
    克罗艾 "「让我来吧。」"
    "说着，克罗艾学姐站到了门前，伸出手去敲门。"
    window hide
    play sound "SE00_27"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA06"),"True","img/CL_LAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL08A_KU018"
    克罗艾 "「那个。我进来了……」"
    "客气的通报之后，克罗艾学姐走进了父亲的病房。我也跟在后面走了进去。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
#BG_SWPC 0
#BG_ALPC 1,128
#BG_PRI 0
#BG_PRI 1
    scene expression "img/BG40AA@2x.jpg" as bg0 with dissolve
    window hide
#BG_PRI 0
#BG_GET_NOC 0,F24
#BG_SET_BACK 
#BG_INIC 2
#BG_UVC 2,(640/4),0,(640/2),(448/2)
#CHR_PRIC 2
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2,(320-224)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB02"),"True","img/YZ_LAB02A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
        xcenter .15
    with dissolve
#BG_ALP_AUTOC 0,0,0,1
#BG_SWPC 0
    hide bg2 with dissolve
#BG_PRI 0
#BG_PRI 2
#CHR_PRIC 2
    play music "OBGM08"
    voice "NCL08A_KZ000"
    幸蔵 "「欢迎你们两个。这么热的天，过来很不容易吧？」"
    "一走进病房，躺在病床上的学姐的父亲就起身迎接我们。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC01"),"True","img/CL_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL08A_KU019"
    克罗艾 "「没有，不要紧的……妈妈呢？」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA01"),"True","img/YZ_LAA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .15
    with dissolve
    voice "NCL08A_KZ001"
    幸蔵 "「啊，你妈妈去找诺艾儿了。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC04"),"True","img/CL_LAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL08A_KU020"
    克罗艾 "「她……迷路了？」"
    志雄 "「我们也去找找吧？」"
    "看到我们担心的样子，学姐的父亲苦笑着。"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA02"),"True","img/YZ_LAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .15
    with dissolve
    voice "NCL08A_KZ002"
    幸蔵 "「啊，不用担心的。这是常有的事情哦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC05"),"True","img/CL_LAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
#REEK_CHR 0
    voice "NCL08A_KU021"
    克罗艾 "「咦？」"
#REMOVE_REEK_CHR 0
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB01"),"True","img/YZ_LAB01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .15
    with dissolve
    voice "NCL08A_KZ003"
    幸蔵 "「与其说是迷路，倒更像是探险。对于诺艾儿来说，这个医院就像一个大型游乐场一样」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC04"),"True","img/CL_LAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    志雄 "「但是，很危险的吧？」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA03"),"True","img/YZ_LAA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .15
    with dissolve
    voice "NCL08A_KZ004"
    幸蔵 "「啊，事实上就是为了这件事叫你们来的」"
    voice "NCL08A_KU022"
    克罗艾 "「这是怎么回事……」"
    window hide
    play sound "SE00_27"
    pause (32/32.0)
#BG_GET_NOC 0,F24
    "这时，我们听到敲门的声音，都转向了门的方向。"
    window hide
    play sound "SE00_53"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-96)
#CHR_POSC 1,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh0 zorder (10+0):
        xcenter .35
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA02"),"True","img/NO_MBA02A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .65
    voice "NCL08A_NO000"
    诺艾儿 "「我回来了！」"
    "门被用力推开，诺艾儿和学姐的母亲一起走进病房。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA06"),"True","img/YS_MAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCL08A_EL008"
    爱丽丝 "「诺艾儿。我说过在医院里不能到处乱跑的吧？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA08"),"True","img/NO_MBA08A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter .65
    with dissolve
    voice "NCL08A_NO001"
    诺艾儿 "「啊，是姐姐和哥哥～」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    hide bg1 with dissolve
#BG_SWPC 0
#BG_PRI 1
#BG_PRI 0
#BG_GET_NOC 1,F34
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    #show expression "img/F34@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(448/8)
#CHR_POSC 1,(320+192)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA01"),"True","img/NO_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.2
        xcenter (448/8)/640.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC01"),"True","img/CL_LAC01A@2x.png") as lh1 zorder (10+1):
        xcenter .8
        ypos 0.0

    hide bg1 with dissolve
#BG_BLUR 0
    "诺艾儿丝毫没有听进母亲说的话，向我和克罗艾学姐这边靠来。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB02"),"True","img/NO_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.2
        xcenter (448/8)/640.0
    with dissolve
    voice "NCL08A_NO002"
    诺艾儿 "「欢迎回来，姐姐～」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB06"),"True","img/CL_LAB06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .8
    with dissolve
    voice "NCL08A_KU023"
    克罗艾 "「嗯，我回来了。」"
    "面对诺艾儿的寒暄，学姐很好地回应着。看着她们俩满脸欢笑地交谈着，我不禁笑了起来。"
    voice "NCL08A_NO003"
    诺艾儿 "「也欢迎哥哥～」"
    "看着诺艾儿的笑脸，我也不禁露出了笑容。"
    志雄 "「我又来玩了，诺艾儿。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA01"),"True","img/NO_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.2
        xcenter (448/8)/640.0
    with dissolve
    window hide
#ROUTINE_STA
#CHR_SET_BACK
#CHR_INIC 2
#CHR_PRIC ID_ALL
#CHR_SORT 0,1
#CHR_ALPC 2
#CHR_POSC 2,(320-224)
#ROUTINE_STP
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA03"),"True","img/YS_MAA03A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
        xcenter .2
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR2 128
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
#ROUTINE_STA
#CHR_PRIC ID_ALL
#CHR_SORT 0,1
#ROUTINE_STP
    voice "NCL08A_EL009"
    爱丽丝 "「啊啦，已经来了呢。抱歉，我把你们叫来自己却不在……」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC01"),"True","img/CL_LAC01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .8
    with dissolve
    志雄 "「没关系的。我们也是刚刚到的。」"
    "我满怀期待地向学姐投去确认说法的目光，而学姐只是有些僵硬的点了点头。"
    voice "NCL08A_KU024"
    克罗艾 "「嗯，是这样的。」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA02"),"True","img/YS_MAA02A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
        xcenter .2
    with dissolve
    voice "NCL08A_EL010"
    爱丽丝 "「嗯，那就好。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_INIC 0
#CHR_INIC 1
#CHR_DSPWC_F 0,1,CL_LAC01,YS_LAA01,(320+192),(320-192)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC01"),"True","img/CL_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA01"),"True","img/YS_LAA01A@2x.png") as lh1 zorder (10-2):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCL08A_KU025"
    克罗艾 "「那个，找我们是……？」"
    voice "NCL08A_EL011"
    爱丽丝 "「啊，是呢。其实是打算拜托你们关于诺艾儿的事情。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB03"),"True","img/CL_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
    克罗艾"「诺艾儿……的事情？」"
    voice "NCL08A_KU026"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA03"),"True","img/YS_LAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCL08A_EL012"
    爱丽丝 "「嗯。我因为要一直照顾你父亲，所以没有什么时间去照顾诺艾儿。而且，那孩子现在在这里还没有朋友……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC03"),"True","img/CL_LAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
    "学姐也陷入了沉思。"
    "对于母亲所说的，学姐也感到些困惑。"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2
#CHR_PRIC ID_ALL
#CHR_SORT 0,1
    hide lh0
    hide lh1
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB02"),"True","img/NO_MBB02A@2x.png") as lh2 zorder (10-2):
        ypos 0.2
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR2 128
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
#ROUTINE_STA
#CHR_PRIC ID_ALL
#CHR_SORT 0,1
#ROUTINE_STP
    voice "NCL08A_NO004"
    诺艾儿 "「哎嘿……」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB01"),"True","img/NO_MBB01A@2x.png") as lh2 zorder (10+2):
        ypos .2
    with dissolve
    "诺艾儿在盯着学姐看。"
    window hide
#ROUTINE_STA
#CHR_PRIC ID_ALL
#CHR_SORT 0,1
#ROUTINE_STP
#MOV_CHR_INIT 48
#MOV_CHR2 0
#MOV_FOCUS_BG 512
#MOV_CHR_GO 1
#ROUTINE_STA
#CHR_PRIC ID_ALL
#CHR_SORT 0,1
    hide lh2 with dissolve
#CHR_ALPC 2,128
#ROUTINE_STP
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC01"),"True","img/CL_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    "不知道是不是下定了决心，学姐对母亲点了点头。"
    voice "NCL08A_KU027"
    克罗艾 "「我知道了。只１天的话也可以吗？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA02"),"True","img/YS_LAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_EL013"
    爱丽丝 "「嗯，帮大忙了。谢谢你，克罗艾」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB04"),"True","img/CL_LAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL08A_KU028"
    克罗艾 "「嗯……」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA01"),"True","img/YS_LAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_EL014"
    爱丽丝 "「诺艾儿，来一下。」"
    window hide
#CHR_SORT 2,0
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2,(448/8)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA09"),"True","img/NO_LBA09A@2x.png") as lh2 zorder (10-2):
        ypos 0.2
        xcenter .5
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR2 128
#MOV_CHR_GO 1
    "被母亲叫道，诺艾儿带着一副不明所以的表情靠了过去。"
    voice "NCL08A_NO005"
    诺艾儿 "「怎么了，妈妈？」"
    voice "NCL08A_EL015"
    爱丽丝 "「妈妈呢，今天要照顾爸爸。所以呢，今天就去姐姐她们那里玩吧。」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA08"),"True","img/NO_LBA08A@2x.png") as lh2 zorder (10+2):
        ypos 0.2
        xcenter .5
    with dissolve
    voice "NCL08A_NO006"
    诺艾儿 "「诶？可以吗！？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL08A_KU029"
    克罗艾 "「当然。今天姐姐我们会陪着你玩的。」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB02"),"True","img/NO_LBB02A@2x.png") as lh2 zorder (10+2):
        ypos 0.2
        xcenter .5
    with dissolve
    voice "NCL08A_NO007"
    诺艾儿 "「谢谢你，姐姐～」"
    voice "NCL08A_EL016"
    爱丽丝 "「诺艾儿。要听话哦？」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA01"),"True","img/NO_LBA01A@2x.png") as lh2 zorder (10+2):
        ypos .2
        xcenter .5
    with dissolve
    voice "NCL08A_NO008"
    诺艾儿 "「知道，妈妈。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB06"),"True","img/CL_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL08A_KU030"
    克罗艾 "「哈哈……」"
    "看着诺艾儿的笑脸，我和学姐不禁笑了出来。"
    voice "NCL08A_EL017"
    爱丽丝 "「然后，虽然觉得不太合适，还是拜托你们了……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL08A_KU031"
    克罗艾 "「嗯，放心吧。」"
    "太好了。不知道是不是多亏了诺艾儿，学姐的紧张感少了很多。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA03"),"True","img/YS_LAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_EL018"
    爱丽丝 "「要是有什么事的话就打电话……看来也行不通呢。怎么办好呢？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC01"),"True","img/CL_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL08A_KU032"
    克罗艾 "「没关系的哦。妈妈就专心照顾爸爸吧。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA01"),"True","img/YS_LAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_EL019"
    爱丽丝 "「可以吗？那就拜托你们了。」"
    "和睦的家族对话。不过，在我看来其中还有些别扭的地方。"
    "……谁都不想提起学姐从家里逃出来的事情。"
    "就好像是在接触的时候刻意避开痛苦的地方，让人感觉十分别扭。"
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
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA01"),"True","img/NO_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.2
        xcenter .2
    with dissolve
    voice "NCL08A_NO009"
    诺艾儿 "「快点走吧？」"
    "诺艾儿像是催促着我们似的，打开房门等在门口。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_PRI 0
#BG_GET_NOC 0,F24
#BG_SET_BACK 
#BG_INIC 2
#BG_UVC 2,(640/4),0,(640/2),(448/2)
    #show expression "img/F24@2x.jpg" as bg2 zorder 2 with dissolve
#ROUTINE_STA
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_INIC 2
#CHR_PRIC ID_ALL
#CHR_SORT 0,1
#CHR_POSC 0,(320+224)
#CHR_POSC 1
#CHR_POSC 2,(320-224)
#ROUTINE_STP
#CHR_SETTC 0,1,2,CL_LAC01,YS_LAA01,YZ_LAA01
#BG_ALP_AUTOC 0,0,0,1
#BG_SWPC 0
    hide bg2 with dissolve
#ROUTINE_STA
#BG_PRI 0
#BG_PRI 2
#CHR_PRIC ID_ALL
#CHR_SORT 0,1
#ROUTINE_STP
    voice "NCL08A_EL020"
    爱丽丝 "「晚上的时候会去接她的。」"
    志雄 "「啊，没关系。我们送她回来就行了。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA03"),"True","img/YS_LAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL08A_EL021"
    爱丽丝 "「可以吗……？」"
    志雄 "「嗯，交给我吧。」"
    voice "NCL08A_KU033"
    克罗艾 "「那晚上见了。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA02"),"True","img/YZ_LAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL08A_KZ005"
    幸蔵 "「多加小心。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA02"),"True","img/YS_LAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL08A_EL022"
    爱丽丝 "「慢走，克罗艾……」"
    voice "NCL08A_KU034"
    克罗艾 "「嗯，我走了……」"
    "就这样我们带着诺艾儿离开了医院。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG14AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG14AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_15L"
    pause (32/32.0)
#FADE_IN 1
    pause (32/32.0)
#SE_VOLC 1,(64/2)
    show expression "img/BG39AA@2x.jpg" as bg_over zorder 2 with dissolve
    play music "BGM08"
    "停在我家门前的诺艾儿满脸好奇。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-96)
#CHR_POSC 1,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA09"),"True","img/NO_MBA09A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .35
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh1 zorder (10+1):
        xcenter .65
    voice "NCL08A_NO010"
    诺艾儿 "「这里是哥哥的家吗？」"
    voice "NCL08A_KU035"
    克罗艾 "「是哦。」"
    voice "NCL08A_NO011"
    诺艾儿 "「姐姐也住在这里吗？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB06"),"True","img/CL_MAB06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL08A_KU036"
    克罗艾 "「嗯。」"
#MUS_VOL 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB07"),"True","img/NO_MBB07A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .35
    with dissolve
    voice "NCL08A_NO012"
    诺艾儿 "「那就是同居的意思？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB04"),"True","img/CL_MAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    "听到从诺艾儿口中说出的『同居』，学姐的脸有些微微发红。"
    "说起来，连这样的事情都知道呢……"
    "是该说童言无忌吗。孩子的话还是不必当真好了。"
    voice "NCL08A_KU037"
    克罗艾 "「诺艾儿……那些话是在哪学到的？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA09"),"True","img/NO_MBA09A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .35
    with dissolve
    voice "NCL08A_NO013"
    诺艾儿 "「电视上～」"
#MUS_VOL 128
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB05"),"True","img/CL_MAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL08A_KU038"
    克罗艾 "「原来是这样」"
    "听着学姐深深的叹气声，我打开了房间的门。"
    window hide
    play sound "SE00_46"
    play sound "SE00_00"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA01"),"True","img/NO_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .35
    with dissolve
    hide lh0 with dissolve
    "与此同时，诺艾儿从我的旁边挤了过去，跑进了屋子里面。"
    voice "NCL08A_NO014"
    诺艾儿 "「打扰了！」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB04"),"True","img/CL_MAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL08A_KU039"
    克罗艾 "「真有精神呢。」"
    志雄 "「是啊。」"
    stop sound
    show expression "img/BG33AA@2x.jpg" as bg_over zorder 2 with dissolve
    play sound "SE00_01"
#SE_WATC 1
    play sound "SE03_65"
    "诺艾儿站在客厅里，聊有兴趣地环视着周围。"
    "她眼睛里充满了好奇，这里那里来回窜着。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+160)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA04"),"True","img/NO_MBA04A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .35
    with dissolve
    voice "NCL08A_NO015"
    诺艾儿 "「榻榻米，没有呢？」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "一会儿看看电视的背面，一会儿又试着用窗帘把自己包起来，什么都感到新鲜。"
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA01"),"True","img/CL_LAA01A@2x.png") as lh0 zorder 100:
        ypos 0.0
        xcenter .5
    with dissolve
    "稍后，克罗艾学姐也进到客厅里。"
    voice "NCL08A_KU040"
    克罗艾 "「诺艾儿。过来一下。」"
    window hide
    stop sound
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+160),(448/8)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA09"),"True","img/NO_LBA09A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO016"
    诺艾儿 "「什么事？姐姐」"
    voice "NCL08A_KU041"
    克罗艾 "「放在门厅的鞋子，不好好的摆好是不行的哦？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA08"),"True","img/NO_LBA08A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO017"
    诺艾儿 "「啊！」"
    window hide
    play sound "SE01_13"
    hide lh1 with dissolve
    stop sound fadeout 1
    "被学姐指出后，诺艾儿一副恍然大悟的表情，慌忙跑向门厅。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL08A_KU042"
    克罗艾 "「真是的，慌慌张张的呢……」"
    "虽然嘴上那么说，不过克罗艾学姐的表情舒缓了许多。"
    "注视着跑开的诺艾儿的背影，学姐的视线里饱含着温情。"
    "不自觉间，我盯着学姐的侧脸看入了神。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB03"),"True","img/CL_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL08A_KU043"
    克罗艾 "「我的脸上有什么东西吗？」"
    志雄 "「啊，没、没什么……」"
    克罗艾 "不会什么都没有的吧？……{w=4}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB04"),"True","img/CL_LAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL08A_KU044B"
    extend "啊，难道说是，刚刚的我有些说教的感觉吗？」"
    "克罗艾学姐困惑地询问我。"
    志雄 "「没有那回事的。怎么说呢，就像是教育孩子的母亲，和那一样的感觉吧……」"
    stop sound
    stop music fadeout 1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC02"),"True","img/CL_LAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL08A_KU045"
    克罗艾 "「好过分啊。我明明还是花季少女……」"
    志雄 "「啊，没，只是比喻啊！是说你很厉害的意思！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB04"),"True","img/CL_LAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL08A_KU046"
    克罗艾 "「真的是那样想的……？」"
    window hide
    play music "BGM13"
    志雄 "「嗯，学姐一定会成为一个好母亲的！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA07"),"True","img/CL_LAA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL08A_KU047"
    克罗艾 "「是，是吗？那样的话，志雄也加油，一定要成为一个好父亲……」"
    志雄 "「诶？　那个」"
    "说完两人的脸都红了起来，谁也不说话。"
    window hide
#CHR_SET_BACK
#ROUTINE_STA
#CHR_INIC 1
#CHR_INIC 2
#CHR_ALPC 1
#CHR_ALPC 2
#CHR_POSC 1,(320+160)
#CHR_POSC 2,(320-160)
#CHR_PRIC ID_ALL
#CHR_SORT 0,2
#ROUTINE_STP
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA09"),"True","img/NO_MBA09A@2x.png") as lh1 zorder (10+1):
        xcenter .25
        ypos 0.2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC05"),"True","img/CL_LAC05A@2x.png") as lh2 zorder (10+2):
        xcenter .75
        ypos 0.0

#MOV_CHR_INIT 32
#MOV_CHR1 128
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
#ROUTINE_STA
#CHR_PRIC ID_ALL
#CHR_SORT 0,2
#ROUTINE_STP
    "从门厅回来的诺艾儿歪着脑袋看着我们。"
    stop music fadeout 1
    voice "NCL08A_NO018"
    诺艾儿 "「夫妻相声吗？」"
    window hide
#CHR_ALPC 2,128
#CHR_ALPC 0
#QUA2_CHR 2
    hide lh0 with dissolve
#CHR_ALPC 0,128
#BG_SET_BACK 
#REEK_CHR 2
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NCL08A_KU048"
    克罗艾 "「啊！？」"
#THREAD_STP 1
#REMOVE_REEK_CHR 2
    志雄 "「呜哇！我去收拾下桌子！」"
    window hide
    hide lh1 with dissolve
    "看着突然慌张起来的我们，诺艾儿有些不明白的坐在了椅子上。"
    window hide
    play music "BGM10"
#REEK_CHR 2
    voice "NCL08A_KU049"
    克罗艾 "「那，那我去准备饮料！诺艾儿想喝什么？」"
#REMOVE_REEK_CHR 2
    voice "NCL08A_NO019"
    诺艾儿 "「橙汁就好了。」"
    show expression "img/BG15AA@2x.jpg" as bg_over zorder 2 with dissolve
    "我尽量让无法控制的心跳平静下来，埋头收拾着桌子上的教材。"
    window hide
#FADE_OUT 1
#CHR_SORT 0,1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 2
##BG_POSC 0,(60),0,640,448
    show expression "img/EXBG10AA@2x.png" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320+160)
#CHR_POSC 1,(320-160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA02"),"True","img/NO_ZAA02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.2

#CHR_SORT 1
#FADE_IN 1
    "接过克罗艾学姐倒的饮料，我们围坐在桌子边。"
    "诺艾儿也坐了下来，很美味地享受着水溶橙汁。"
    "看着难得安静下来的诺艾儿，我忽然想到了些什么。"
    志雄 "「说起来，诺艾儿是从外国到这来的呢。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB01"),"True","img/NO_ZAB01A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO020"
    诺艾儿 "「嗯。坐飞机从法国来的。」"
    志雄 "「可是诺艾儿的日语很好哦？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB02"),"True","img/NO_ZAB02A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO021"
    诺艾儿 "「嗯，是妈妈教我的。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB03"),"True","img/CL_ZAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_KU050"
    克罗艾 "「妈妈……？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA01"),"True","img/NO_ZAA01A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO022"
    诺艾儿 "「妈妈说将来会搬去日本和爸爸还有姐姐一起住的。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB05"),"True","img/CL_ZAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    克罗艾 "「……」"
    "听到诺艾儿的话，我和学姐都陷入了沉默。"
    "说起来，学姐的母亲和诺艾儿，为什么会到现在才回来呢。"
    "或许应该问为什么一直到现在都不曾回来。"
    "当然，这样的问题不可能直接去问诺艾儿的……"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB04"),"True","img/NO_ZAB04A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO023"
    诺艾儿 "「姐姐？怎么了？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_KU052"
    克罗艾 "「没，没什么。那个，诺艾儿，可以的话，跟姐姐说说诺艾儿和妈妈在那边一直都是怎样生活的吧？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB02"),"True","img/NO_ZAB02A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO024"
    诺艾儿 "「嗯！我想想？我们住的地方是——」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB06"),"True","img/CL_ZAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    window hide
#FADE_OUT 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA02"),"True","img/NO_ZAA02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.2

    pause (64/32.0)
#FADE_IN 1
    "那之后的一段时间，学姐和我听了许多关于学姐的妈妈和诺艾儿生活在家乡的事情。"
    "虽然言语有些笨拙，还有很难懂的地方，不过学姐一直饶有兴趣地听着。"
    "一定是很想知道吧。"
    "在异国生活。还有异国的文化。在那样的环境里生活着的家庭轶事。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB01"),"True","img/NO_ZAB01A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO025"
    诺艾儿 "「其他的？还有什么想要听的吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB06"),"True","img/CL_ZAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_KU053"
    克罗艾 "「没有了……谢谢你，诺艾儿。真是个十分开心的话题呢。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA02"),"True","img/NO_ZAA02A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO026"
    诺艾儿 "「啊哈～」"
    "被学姐温柔的抚摸着头发，诺艾儿很舒服地眯起了眼睛。"
    "如此美妙的身姿与情境，最近好久都没有见到了。她们完全像是至今为止一直生活在一起的姐妹一样。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB01"),"True","img/NO_ZAB01A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO027"
    诺艾儿 "「喂喂，姐姐。我也有想要知道的事情……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_KU054"
    克罗艾 "「嗯，是什么？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB09"),"True","img/NO_ZAB09A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO028"
    诺艾儿 "「姐姐和哥哥是如何开始交往的？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB04"),"True","img/CL_ZAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    志雄 "「唔——！」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB04"),"True","img/NO_ZAB04A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO029"
    诺艾儿 "「那个……开始的契机？」"
    "我差点把口中的茶水吐了出来，慌忙地用手捂住嘴。"
    志雄 "「咳咳！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC05"),"True","img/CL_ZAC05A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA08"),"True","img/NO_ZAA08A@2x.png") as lh1 zorder (10+1):
        xcenter .75
#BG_SET_BACK 
#REEK_CHR 0
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NCL08A_KU055"
    克罗艾 "「志，志雄，不要紧吧！？」"
#THREAD_STP 1
#REMOVE_REEK_CHR 0
    志雄 "「啊，抱歉。有些呛到了」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB01"),"True","img/NO_ZAB01A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO030"
    诺艾儿 "「喂——是怎么样的嘛？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC02"),"True","img/CL_ZAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_KU056"
    克罗艾 "「那个，嗯……是秘密……」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB03"),"True","img/NO_ZAB03A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO031"
    诺艾儿 "「诶～！人家想要知道嘛～！」"
    "见学姐不说，诺艾儿开始撒娇了。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB01"),"True","img/NO_ZAB01A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO032"
    诺艾儿 "「好不好嘛～告诉我吧，说了又不会有什么损失～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC04"),"True","img/CL_ZAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_KU057"
    克罗艾 "「诺艾儿，追问别人不想说的事情是不行的。明白吗？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA04"),"True","img/NO_ZAA04A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO033"
    诺艾儿 "「追问？人家不明白那是什么意思啦～」"
    "看到诺艾儿歪着头，学姐把食指竖起来讲解了起来。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC01"),"True","img/CL_ZAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_KU058"
    克罗艾 "「对于别人想要作为秘密的事情，不能强迫别人说出来的哦。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA09"),"True","img/NO_ZAA09A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO034"
    诺艾儿 "「但是，秘密就是让人探明的吧？侦探先生在电视上是这么说的哦～」"
    "虽然学姐不断地想要结束这个话题，可是诺艾儿却一再的追问，一点都不让步。"
    志雄 "「原来如此。情报源是中午的悬疑剧吗……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB05"),"True","img/CL_ZAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_KU059"
    克罗艾 "「真是的。志雄也说点什么啊……」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB07"),"True","img/NO_ZAB07A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO035"
    诺艾儿 "「相遇的时候是怎么样的？　紧张吗？　还是说十分期待？」"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "对诺艾儿说与学姐相遇的事情":
            $F7=0
        "想办法岔开话题":
            $F7=1
        "让两个人都冷静下来":
            $F7=2
    if F7==0:
        jump L_NCL08A_SEL00_A
    if F7==1:
        jump L_NCL08A_SEL00_B
    if F7==2:
        jump L_NCL08A_SEL00_C
label L_NCL08A_SEL00_A:
    志雄 "「那么有兴趣吗……？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB02"),"True","img/NO_ZAB02A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08X_NO000"
    诺艾儿 "「嗯！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC05"),"True","img/CL_ZAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
#BG_SET_BACK 
#REEK_CHR 0
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NCL08X_KU000"
    克罗艾 "「等一下，志雄！？」"
#THREAD_STP 1
#REMOVE_REEK_CHR 0
    志雄 "「学姐，这里还是说出来比较好吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC04"),"True","img/CL_ZAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08X_KU001"
    克罗艾 "「但是，对诺艾儿还太早了啊……」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA03"),"True","img/NO_ZAA03A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08X_NO001"
    诺艾儿 "「哎～才没有那回事呢」"
    志雄 "「学姐，那样有些保护过头了……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC02"),"True","img/CL_ZAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08X_KU002"
    克罗艾 "「什，什么嘛，连志雄都这样……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAA06"),"True","img/CL_ZAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    "说着，学姐转向了一边。看着学姐像是小孩子一样的表现，我不禁笑了起来。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB03"),"True","img/NO_ZAB03A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08X_NO002"
    诺艾儿 "「喂，契机是～？」"
    "……那个，好像有些不太好说。"
    jump L_NCL08A_SEL00_X
label L_NCL08A_SEL00_B:
    志雄 "「比，比起那个，诺艾儿到日本来之后，有什么困扰着你的事情吗？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB09"),"True","img/NO_ZAB09A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08X_NO003"
    诺艾儿 "「困扰的事情？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB04"),"True","img/CL_ZAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08X_KU003"
    克罗艾 "「是、是啊。有吗？诺艾儿，应该会有些不适应的地方吧？」"
    志雄 "「我们可以的话，会帮助你的哦～」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA04"),"True","img/NO_ZAA04A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08X_NO004A"
    诺艾儿 "「那个……嗯……{w=4}{nw}"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB01"),"True","img/NO_ZAB01A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08X_NO004B"
    extend "啊，有一件事」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB06"),"True","img/CL_ZAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08X_KU004"
    克罗艾 "「嗯，是什么呢？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB03"),"True","img/NO_ZAB03A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08X_NO005"
    诺艾儿 "「最近，对比我大很多的姐姐持有我不知道的秘密这件事，我感到很困扰」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB05"),"True","img/CL_ZAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    志雄 "「……」"
#MESEX_A M_NOA,A_CH_KU,NCL08X_KU005,"【クロエ】「……」%K%P"
    jump L_NCL08A_SEL00_X
label L_NCL08A_SEL00_C:
    志雄 "「那个，两个人都冷静一下吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC03"),"True","img/CL_ZAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08X_KU006"
    克罗艾 "「我很冷静的哦？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB04"),"True","img/NO_ZAB04A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08X_NO006"
    诺艾儿 "「喂——告诉我吧——」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC02"),"True","img/CL_ZAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08X_KU007"
    克罗艾 "「所以说呢，诺艾儿。不是告诉你不要对别人的事刨根问底吗？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB03"),"True","img/NO_ZAB03A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08X_NO007"
    诺艾儿 "「但是但是，女孩子都会很想要听关于这方面的事情的……」"
    志雄 "「那个……你们两个？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB05"),"True","img/CL_ZAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08X_KU008"
    克罗艾 "「就算那样也要把持住自己，这才是真正的淑女哦。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB04"),"True","img/NO_ZAB04A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08X_NO008"
    诺艾儿 "「就算是淑女对于想知道的事情也会追问的～」"
    志雄 "「不行，完全没有在听……」"
    "没办法啊……"
    "但是，看着她俩你来我往的，感觉心里面变得暖呼呼的。"
    jump L_NCL08A_SEL00_X
label L_NCL08A_SEL00_X:
    window hide
#FADE_OUT 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB04"),"True","img/CL_ZAB04A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA01"),"True","img/NO_ZAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.2

    pause (64/32.0)
#FADE_IN 1
    "最终，我们还是败给了诺艾儿的好奇心。"
    "结局是我们陷入了不得不告诉诺艾儿那段奏云祭上经历的窘境，那正是我和学姐开始交往的契机。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA09"),"True","img/NO_ZAA09A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO036"
    诺艾儿 "「奏云祭？」"
    志雄 "「奏云祭就是举行祭典的意思哦。只是学校的学生在准备，之后会请许多的人来」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB08"),"True","img/NO_ZAB08A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO037"
    诺艾儿 "「祭典啊！诺艾儿也想要去～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_KU060"
    克罗艾 "「是呢。今年的奏云祭也是那个时候，要不要和姐姐一起去？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB01"),"True","img/NO_ZAB01A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO038"
    诺艾儿 "「真的吗！？」"
    志雄 "「太好了呢，诺艾儿。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB02"),"True","img/NO_ZAB02A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO039"
    诺艾儿 "「嗯！好期待！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB03"),"True","img/CL_ZAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_KU061"
    克罗艾 "「啊，对了！」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA01"),"True","img/NO_ZAA01A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    "学姐突然地说道。"
    志雄 "「怎么了？」"
    voice "NCL08A_KU062"
    克罗艾 "「说起来，有去年奏云祭的录像带呢。」"
    志雄 "「啊，那个正好在我家里哦。」"
    "正好今年的奏云祭准备也开始了，也可以把去年的奏云祭拿出来当做参考。"
    "我靠近电视旁，从下面的柜子里取出一盘贴着奏云祭标签的带子。"
    window hide
#FADE_OUT 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC01"),"True","img/CL_ZAC01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB01"),"True","img/NO_ZAB01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.2

    pause (64/32.0)
    play sound "SE08_04L"
#FADE_IN 1
    voice "NCL08A_KU063"
    克罗艾 "「你看，这就是学校的正门哦。这个学校的全部学生都在自己专属的场地工作着。」"
    voice "NCL08A_NO040"
    诺艾儿 "「人真多呢。」"
    voice "NCL08A_KU064"
    克罗艾 "「这个是午后的影像，是一天中人最多的时候呢。」"
    志雄 "「今年也能有这么多人就好了……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_KU065"
    克罗艾 "「一定会办好的，学生会和执行委员的工作都有在进行了吧？」"
    志雄 "「嗯，是呢。」"
    "每年在准备的时候都会出现问题。今年虽然工作很早就开始了，但是也绝对不能掉以轻心。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB02"),"True","img/NO_ZAB02A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO041"
    诺艾儿 "「大家都好高兴。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB02"),"True","img/CL_ZAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_KU066"
    克罗艾 "「是呢。虽然准备的时候很累，不过看到成果的时候，还是快乐多些。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA09"),"True","img/NO_ZAA09A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO042"
    诺艾儿 "「哥哥和姐姐就是在这个祭典上相识的吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_KU067"
    克罗艾 "「不，志雄和我，在这之前一段时间是作为学生会的成员进行准备活动的。」"
    voice "NCL08A_NO043"
    诺艾儿 "「那为什么，会开始交往呢？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC05"),"True","img/CL_ZAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
#BG_SET_BACK 
#REEK_CHR 0
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NCL08A_KU068"
    克罗艾 "「那个是因为……」"
#THREAD_STP 1
#REMOVE_REEK_CHR 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC03"),"True","img/CL_ZAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    "面对诺艾儿的疑问，克罗艾学姐脸通红地低下头。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB01"),"True","img/NO_ZAB01A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO044"
    诺艾儿 "「喂，为什么嘛？」"
    志雄 "「哎？那个是……」"
    "矛头转向了我。我把视线移开想要蒙混过关。"
    "——我和学姐就是在奏云祭的准备过程中走到一起的。"
    "那样让人害羞的事情，要怎样才能说出口啊。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC05"),"True","img/CL_ZAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
#BG_SET_BACK 
#REEK_CHR 0
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NCL08A_KU069"
    克罗艾 "「啊，你看！诺艾儿。现在，拍到志雄了哦」"
#THREAD_STP 1
#REMOVE_REEK_CHR 0
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB04"),"True","img/NO_ZAB04A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO045A"
    诺艾儿 "「不要用那种事情打马虎眼嘛……{w=6}{nw}"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA02"),"True","img/NO_ZAA02A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO045B"
    extend "啊，真的呢！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC04"),"True","img/CL_ZAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    志雄 "「……啊——」"
    "确实现在电视画面上出现的是我。不过说起来，这盘带子本来就是为了奏云祭的准备要用到的资料，所以主要都是工作人员出现在带子中。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA03"),"True","img/NO_ZAA03A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO046"
    诺艾儿 "「哥哥很拼命呢。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC01"),"True","img/CL_ZAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_KU070"
    克罗艾 "「嗯，是呢。但是准备的时候，比这个还要拼命的哦。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA09"),"True","img/NO_ZAA09A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL08A_NO047"
    诺艾儿 "「为什么？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB02"),"True","img/CL_ZAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL08A_KU071"
    克罗艾 "「那个是……」"
    志雄 "「唔，感觉有些听不下去了……」"
    "去年混乱的状况相当的严重。要是没有学姐的话，完全无法渡过难关吧。"
    "相比之下，今年的学生会长——也就是我，就懈怠了许多。"
    志雄 "「我，我离开一下……」"
    window hide
    stop sound fadeout 1
#BG_SET_BACK 
#BG_INIC 1
    scene expression "img/BG15AA@2x.jpg" as bg1 with dissolve
#CHR_ERSWC 0,1
#BG_ERSWC 0,2,BG_NOFADE
#BG_POSC 0,0,0,640,448
#BG_POSC 2,0,0,640,448
#BG_SWPC 0
#BG_PRI 1
#BG_PRI 0
#CHR_SORT 0
    voice "NCL08A_KU072"
    克罗艾 "「啊，逃跑了……」"
    voice "NCL08A_NO048"
    诺艾儿 "「逃跑了？」"
    stop sound
    show expression "img/BG33AA@2x.jpg" as bg_over zorder 2 with dissolve
    "就在我飞似的逃离现场，来到厨房倒茶的时候。"
    window hide
    play sound "SE02_06L"
    "电话铃响了起来。"
    window hide
#MUS_VOL 64
    play sound "SE02_16"
    志雄 "「喂，我是塚本。」"
    voice "NCL08A_EL023_K"
    爱丽丝 "「喂，我是克罗艾的妈妈。想问问她俩怎么样了。」"
    志雄 "「现在的状况吗？她们两个现在正在看电视。要让她们接吗？」"
    voice "NCL08A_EL024_K"
    爱丽丝 "「不，没关系的……」"
    "感觉到回答中有些犹豫。"
    志雄 "「这样啊……」"
    voice "NCL08A_EL025_K"
    爱丽丝 "「差不多，要从医院离开了。那个……还是我去接吧？」"
    志雄 "「照顾病人一天肯定累了吧？那种程度的事情请交给我来做吧。」"
    "照顾病人比起这个要累的多，看看学姐就明白了这一点。"
    "要是，连妈妈也累倒下的话，学姐和诺艾儿都会伤心的。"
    voice "NCL08A_EL026_K"
    爱丽丝 "「谢谢你这样为我着想。」"
    志雄 "「这不算什么的。」"
    "我的视线落到了自己的脚尖上。我对学姐，还有那个家庭依旧是什么都做不了。"
    志雄 "「要是有什么我能做的事情，不必客气请说出来。」"
    voice "NCL08A_EL027_K"
    爱丽丝 "「谢谢你，有你这份心意我就很满足了。」"
    志雄 "「嗯。差不多该送诺艾儿回家了呢……」"
    "注意到自己的声音有些气馁，慌忙抬高了几度，用有精神的声音说道。"
    voice "NCL08A_EL028_K"
    爱丽丝 "「呵呵。」"
    "从听筒那边传来了，和克罗艾学姐的风格完全一样的轻笑。"
    志雄 "「诶。我说了什么奇怪的话吗？」"
    voice "NCL08A_EL029_K"
    爱丽丝 "「没。那孩子，克罗艾，遇到了一个很棒的男生呢。」"
    志雄 "「没，怎么会，不要开我玩笑啦……」"
    voice "NCL08A_EL030_K"
    爱丽丝 "「没有，是真心的。那么克罗艾也就拜托你了呢。」"
    志雄 "「诶？啊，嗯……」"
    window hide
#MUS_VOL 128
    play sound "SE02_08"
    "说了这些后，学姐的妈妈就挂掉了电话。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+160)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB03"),"True","img/CL_MAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL08A_KU073"
    克罗艾 "「志雄，有电话吗？」"
    play sound "SE02_07"
    志雄 "「嗯，学姐的妈妈打来的。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB05"),"True","img/CL_MAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL08A_KU074"
    克罗艾 "「……说了什么？」"
    "学姐的表情变得有些紧张。"
    "果然和妈妈之间的距离还是没有缩短。"
    "也许竖起心墙的就是学姐自己也说不定。"
    voice "NCL08A_KU075"
    克罗艾 "「志雄？」"
    志雄 "「诶？没什么。妈妈好像要从医院离开了的样子。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL08A_KU076"
    克罗艾 "「哦。那差不多该送诺艾儿回家了呢……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAA09"),"True","img/NO_MAA09A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL08A_NO049"
    诺艾儿 "「怎么了？」"
    "注意到提起她名字的我们，诺艾儿离开电视前走了过来。"
    hide lh1 with dissolve
#CHR_POSC 1,(320+160),(448/8)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter .75
    with dissolve
    "学姐在诺艾儿面前弯下腰微笑说道。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB06"),"True","img/CL_MAB06A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter .75
    with dissolve
    voice "NCL08A_KU077"
    克罗艾 "「妈妈呢，现在也要回家了。诺艾儿也差不多要准备回去了哦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAA02"),"True","img/NO_MAA02A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL08A_NO050"
    诺艾儿 "「嗯～」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB02"),"True","img/CL_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter .75
    with dissolve
    voice "NCL08A_KU078"
    克罗艾 "「好。姐姐要奖赏一下听话的好孩子诺艾儿！」"
    "说着，学姐从口袋里拿出来各色的糖果。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB06"),"True","img/CL_MAB06A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter .75
    with dissolve
    voice "NCL08A_KU079"
    克罗艾 "「嗯，挑一个你喜欢的吧～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB03"),"True","img/NO_MAB03A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL08A_NO051A"
    诺艾儿"「嗯～{w=2}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAA01"),"True","img/NO_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL08A_NO051B"
    extend "那就这个绿的吧！」"
    志雄 "「诺艾儿也喜欢绿色吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB02"),"True","img/NO_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL08A_NO052"
    诺艾儿 "「嗯。还有红色也喜欢。因为是妈妈料理的颜色～」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB05"),"True","img/CL_MAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter .75
    with dissolve
    克罗艾 "「……」"
    "听到诺艾儿的话，克罗艾学姐的肩稍稍颤抖了一下。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB04"),"True","img/CL_MAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter .75
    with dissolve
    voice "NCL08A_KU081"
    克罗艾 "「诺艾儿喜欢妈妈吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAA02"),"True","img/NO_MAA02A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL08A_NO053"
    诺艾儿 "「嗯，最喜欢了！姐姐呢？」"
    voice "NCL08A_KU082"
    克罗艾 "「我……我也最喜欢哦。」"
    voice "NCL08A_NO054"
    诺艾儿 "「爸爸呢？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter .75
    with dissolve
    voice "NCL08A_KU083"
    克罗艾 "「也喜欢呢。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB01"),"True","img/NO_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL08A_NO055"
    诺艾儿 "「……那我呢？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB06"),"True","img/CL_MAB06A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter .75
    with dissolve
    voice "NCL08A_KU084"
    克罗艾 "「当然也最喜欢诺艾儿了！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB03"),"True","img/NO_MAB03A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    "听到这里，突然地诺艾儿低下了头，沉默不语。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB03"),"True","img/CL_MAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter .75
    with dissolve
    voice "NCL08A_KU085"
    克罗艾 "「怎么了？」"
    "我和学姐都因为不明白缘由变得担心起来。"
    "暂时的沉寂之后，诺艾儿抑或天真，抑或认真地注视着学姐。"
    window hide
#BG_GET_NOC 0,F34
#BG_SET_BACK 
#BG_INIC 2
#ROUTINE_STA
#BG_PRI 0
#CHR_PRIC 1
#CHR_PRIC 0
#ROUTINE_STP
#BG_UVC 2,(640/4),((448/8)+512),((640/4)*3),((448/4)*3)
    #show expression "img/F34@2x.jpg" as bg2 zorder 2 with dissolve
#ROUTINE_STA
#CHR_SET_BACK
#CHR_INIC 2
#CHR_INIC 3
#CHR_PRIC 2
#CHR_PRIC 3
#CHR_POSC 2,(320-160)
#CHR_POSC 3,(320+160)
#ROUTINE_STP
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB03"),"True","img/NO_ZAB03A@2x.png") as lh0 zorder (10+2):
        xcenter .25
        ypos 0.2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB03"),"True","img/CL_ZAB03A@2x.png") as lh1 zorder (10+3):
        xcenter .75
        ypos 0.2

    stop music fadeout 1
#BG_ALP_AUTOC 0,0,0,F24,16
#CHR_ALP_AUTOC 0,0,0,F24,16
#CHR_ALP_AUTOC 1,0,0,F24,16
#CHR_PRIC 0
#CHR_PRIC 1
#BG_ALP_SAVEC 0
#CHR_ALP_SAVEC 0
#CHR_ALP_SAVEC 1
#ROUTINE_STA
#CHR_SWPC 0
#CHR_SWPC 1
#CHR_PRIC ID_ALL
#CHR_SORT 0,1,2
#CHR_ERSWC 2,3
#CHR_ALPC 2,128
#CHR_ALPC 3,128
#ROUTINE_STP
#BG_SWPC 0
    hide bg2 with dissolve
#BG_UVC 2,0,0,640,448
#BG_ALPC 2,128
    voice "NCL08A_NO056"
    诺艾儿 "「那为什么姐姐不回家呢？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC03"),"True","img/CL_ZAC03A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter .75
    with dissolve
    voice "NCL08A_KU086"
    克罗艾 "「那是……」"
    "学姐的表情僵住了。"
    "诺艾儿盯着那样的学姐继续说。"
    window hide
    play music "OBGM08"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB04"),"True","img/NO_ZAB04A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL08A_NO057"
    诺艾儿 "「对妈妈，生气了吗？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC02"),"True","img/CL_ZAC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter .75
    with dissolve
    voice "NCL08A_KU087"
    克罗艾 "「为什么会那么想？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA03"),"True","img/NO_ZAA03A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL08A_NO058"
    诺艾儿 "「不知道……」"
    "诺艾儿也像是在拼命地寻找着答案一样。"
    "诺艾儿，就算是小孩子，也能注意到家族关系的不自然的吧……"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC01"),"True","img/CL_ZAC01A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter .75
    with dissolve
    "克罗艾学姐温柔地抚摸着妹妹的头。"
    voice "NCL08A_KU088"
    克罗艾 "「不要紧的。没有生气的。只是因为一直没有见面，所以有些不知所措了……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA09"),"True","img/NO_ZAA09A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL08A_NO059"
    诺艾儿 "「不知了什么？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB06"),"True","img/CL_ZAB06A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter .75
    with dissolve
    voice "NCL08A_KU089"
    克罗艾 "「和妈妈交谈的方法。但是不要紧的。那个很快就会想起来的。」"
    "虽然学姐依旧是和刚刚相同的笑脸……"
    "但是在我看来，却像是快要哭出来一样。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB03"),"True","img/NO_ZAB03A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL08A_NO060"
    诺艾儿 "「真的？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB04"),"True","img/CL_ZAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter .75
    with dissolve
    voice "NCL08A_KU090"
    克罗艾 "「嗯，真的哦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB02"),"True","img/NO_ZAB02A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL08A_NO061"
    诺艾儿 "「太好了～」"
    window hide
    hide lh0 with dissolve
    "诺艾儿恢复了笑脸，走向了门厅。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC02"),"True","img/CL_ZAC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter .75
    with dissolve
    志雄 "「学姐……」"
    voice "NCL08A_KU091"
    克罗艾 "「嗯，不要紧的。我会试着想起来的……」"
#BG_GET_NOC 0,F34
    "那样说着，学姐站起身来转向我这边。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+160)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB06"),"True","img/CL_MAB06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL08A_KU092"
    克罗艾 "「好了，出发吧。要在天黑前把这孩子送回去。」"
    志雄 "「……是呢，出发吧。」"
    "学姐的那个笑容在我的脑中挥之不去。虽然怎么看都像是快乐的，不过，那来自内心深处的哭泣，也只有我能听见吧……"
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