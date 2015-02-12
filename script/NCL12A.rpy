label NCL12A:
    $currentlabel = "NCL12A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '08'
    $day = '18'
    $date = '5'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 2,CAL_0818
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG33AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG33AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1,128
    play music "OBGM28"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "『最好能和父母敞开心扉地谈一谈。』"
    "尽管已经过去两天，但听了我的话下定决心的学姐依然在苦恼如何与父母交谈。"
    "那么多年的思绪情感纠缠在一起，这些时间也是说服自己下定决心所必要的。"
    "我并没有着急，只是期盼着学姐能够自行化解心结，能做的，也只是静静陪在她身边。"
    "终于，学姐有了动静了，她下定决心给家里打了电话。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC01"),"True","img/CL_MAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL12A_KU000"
    克罗艾 "「喂？——嗯，是的。那个……」"
    "听起来学姐的父亲刚好不在家。通话很快结束，放下电话听筒学姐向我转过身来。"
    window hide
    play sound "SE02_07"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL12A_KU001"
    克罗艾 "「爸爸，接下来要去医院呢。」"
    志雄 "「诶？不会吧……」"
    "不禁担心了起来，不过学姐却用笑容回应了我。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB06"),"True","img/CL_MAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL12A_KU002"
    克罗艾 "「不是的哦，只是去做身体检查，顺便拿回放在那里的行李。」"
    志雄 "「这样啊，太好了……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL12A_KU003"
    克罗艾 "「还有，咱们要和他们在医院集合哦。果然还是有些担心……」"
    志雄 "「我会帮忙搬行李的。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB04"),"True","img/CL_MAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL12A_KU004"
    克罗艾 "「谢谢帮忙……」"
    "既然决心要陪在学姐身边，那我也要一起过去吧。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG40AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG40AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320+160)
#CHR_POSC 1,(320-160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA01"),"True","img/CL_LAA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB01"),"True","img/YZ_LAB01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0

    pause (32/32.0)
#FADE_IN 1
    voice "NCL12A_KZ000"
    幸蔵 "「抱歉呐，你们特意跑一趟来陪我。谢谢……」"
    志雄 "「哪里，这点程度而已请不用介意。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA02"),"True","img/YZ_LAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL12A_KZ001"
    幸蔵 "「话说回来，这样就代表已经没有需要再要麻烦医院的事情了吧。」"
    "听了父亲轻松的发言，学姐脸上又泛起了担心的神情。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA02"),"True","img/CL_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL12A_KU005"
    克罗艾 "「……爸爸，暂时还是要定期到医院来检查，刚才医生不是这样说了吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA06"),"True","img/YZ_LAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL12A_KZ002"
    幸蔵 "「是那样的吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA06"),"True","img/CL_LAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL12A_KU006"
    克罗艾 "「真是的……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA01"),"True","img/YZ_LAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    "叹了口气之后，学姐再次用认真的表情开口说道。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA03"),"True","img/CL_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL12A_KU007"
    克罗艾 "「那个，爸爸，今天，有些话想和您说……」"
    "我默默地在一边看着这一切。这种时候，如果不是学姐亲口说出来就没有意义了。"
    "我静静地注视着学姐，听着她一字一句地吐露出心声。"
    voice "NCL12A_KU008"
    克罗艾 "「我，真的非常感谢爸爸……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA02"),"True","img/YZ_LAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL12A_KZ003"
    幸蔵 "「突然之间……怎么了？」"
    "学姐的父亲不好意思地笑了笑。而学姐依然是一幅极其认真的表情。"
    voice "NCL12A_KU009"
    克罗艾 "「请听我说……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA06"),"True","img/YZ_LAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    "仿佛从学姐的神情里察觉到了什么，学姐的父亲也变成了一幅认真的神情。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA02"),"True","img/CL_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL12A_KU010"
    克罗艾 "「我，是看着爸爸的背膀长大的。多亏了爸爸，我现在才能够在这里。一直，都想将这份心情传递给爸爸，真的非常感谢！」"
    voice "NCL12A_KZ004"
    幸蔵 "「克罗艾……」"
    voice "NCL12A_KU011"
    克罗艾 "「但是只有一件事，无论如何也想问问……」"
    voice "NCL12A_KZ005"
    幸蔵 "「是什么难题吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA06"),"True","img/CL_LAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL12A_KU012"
    克罗艾 "「自从妈妈离开之后，爸爸就一直埋头于工作。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA02"),"True","img/CL_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL12A_KU013"
    克罗艾 "「那时我还是孩子，并不是很懂事。即使如此我也明白，爸爸和妈妈之间，发生了什么。」"
    幸蔵 "「……」"
    "学姐的话，学姐的父亲静静地侧耳倾听着，表情始终是一幅认真的样子，没有一丝一毫地变化。"
    "说不定……在约定今天见面的时候就已经有了会被问及这些事情的觉悟了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA06"),"True","img/CL_LAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL12A_KU014"
    克罗艾 "「独自一个人的时间变多了，在家待着的时候心里很害怕。一个人的时候，即使不想去思考，这些事情也会自己出现在脑子里。」"
    "说到这里，学姐像是要忍耐什么似的深深地吸了一口气。"
    voice "NCL12A_KU015"
    克罗艾 "「为什么妈妈没有带我一起走？为什么爸爸一直工作都不会回来？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA02"),"True","img/CL_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL12A_KU016"
    克罗艾 "「是因为……我是多余的吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA03"),"True","img/YZ_LAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    幸蔵 "「……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC02"),"True","img/CL_LAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL12A_KU017"
    克罗艾 "「这就是……所有想说的……」"
    "说完这些的学姐，深深地喘息着。"
    "学姐的父亲听完学姐吐露的心声，咬紧了嘴唇。然后，他从口中慢慢叫出了学姐的名字。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA06"),"True","img/YZ_LAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL12A_KZ008"
    幸蔵 "「克罗艾。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA02"),"True","img/CL_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL12A_KU018"
    克罗艾 "「嗯……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB06"),"True","img/YZ_LAB06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL12A_KZ009"
    幸蔵 "「我也有必须要讲给你听的事情。」"
    voice "NCL12A_KU019"
    克罗艾 "「嗯……」"
    "学姐稍微有些不安，仿佛不想漏过父亲说的每一个字一般竖起耳朵认真听着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB03"),"True","img/YZ_LAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL12A_KZ010"
    幸蔵 "「是你妈妈离家出走之前的事情。」"
    "听到父亲说出这样的话，学姐的肩膀微微地颤抖了一下。"
    window hide
    show expression "img/EV_CL10D@2x.png" as bg2 zorder 200 with dissolve
#MUS_VOL 64,16
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 0
#CHR_ALPC 0
#CHR_ALPC 1
#BG_ALPC 2,128
#BG_COLC 1,128,128,128,128
#BG_COLC 2,128,128,128,128
#CHR_ALPC 0
    voice "NCL12A_KZ011"
    幸蔵 "「……那时候经营困难。从几年前开始，若干的规划因为其他公司的原因而推迟。公司面临着倒闭的危机，为了重整一切，我只能强迫自己不停的工作。」"
    window hide
    show expression "img/BG82NA@2x.jpg" as bg2 zorder 100 with dissolve
    voice "NCL12A_KZ012"
    幸蔵 "「某一天，我也一如既往的晚归。因为彻夜的应酬醉的一塌糊涂，只能让部下送回来。」"
    voice "NCL12A_KZ013"
    幸蔵 "「那个部下很有才能，非常理解当时公司的状况。所以，在整理重要的文件议案的时候总是带着她。」"
    voice "NCL12A_KZ014"
    幸蔵 "「我以为你妈妈她理解我。公司的事情也好，没日没夜、时常晚归地工作也好。可是……」"
    voice "NCL12A_KZ015"
    幸蔵 "「总是带着部下的事情，也和你妈妈说过。但是，得知那个部下是位女性的时候，你妈妈她……怀疑起了我们的关系。」"
    window hide
    hide bg2 with dissolve
#BG_COLC 1,128,128,128,128
#BG_COLC 2,128,128,128,128
#BG_ALPC 0,128
#CHR_ALPC 0,128
#CHR_ALPC 1,128
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB05"),"True","img/CL_LAB05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#MUS_VOL 128
    voice "NCL12A_KU020"
    克罗艾 "「诶？」"
    "震惊。不仅是我，连学姐也是第一次听说吧。"
    voice "NCL12A_KZ016"
    幸蔵 "「当然，那些自然是无中生有。那只是，为了公司团结一致，单纯的信赖。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA02"),"True","img/CL_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL12A_KU021"
    克罗艾 "「可是，只要好好把话说清楚就好了啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA05"),"True","img/YZ_LAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL12A_KZ017"
    幸蔵 "「啊，说得很对。不过，那个时候的我并没有照顾家庭的时间。说明一些事情的时候，也是很不耐烦的态度……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB03"),"True","img/YZ_LAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL12A_KZ018"
    幸蔵 "「全部都是我的责任。你妈妈她离开的事情也好，那之后你所经历的痛苦也好，全部都是。」"
    voice "NCL12A_KZ019"
    幸蔵 "「那之后，我也责备着自己。还有，我实在无法面对自己最重要的女儿，只能借工作来逃避。绝对没有过半点『你是多余的』这样的想法」"
    "学姐的父亲反复地说着充满懊悔之情的言语。不知不觉，我又想起咨询志愿出路的时候，他和我所说的那些话。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB04"),"True","img/CL_LAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL12A_KU022"
    克罗艾 "「爸爸……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB06"),"True","img/YZ_LAB06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL12A_KZ020"
    幸蔵 "「事到如今可能已经晚了，不过真的对不起。」"
    "学姐阻止了道歉的父亲。"
    voice "NCL12A_KU023"
    克罗艾 "「怎么这样，不用道歉的。一开始就说过了吧，我真的真的很感谢爸爸。」"
    "学姐的父亲，悄悄地用力抱住了泪流满面的学姐。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB03"),"True","img/YZ_LAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL12A_KZ021"
    幸蔵 "「真的对不起……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB06"),"True","img/CL_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL12A_KU024"
    克罗艾 "「嗯，我也是，真的谢谢你，爸爸。」"
    "克罗艾学姐满是泪水的脸上，露出了开心而纯粹的笑容。"
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
#label THREAD_KOZO_HUG
#CHR_POS_AUTOC 1,F123,80
#CHR_POS_SAVEC 1
#EOT