label NRI02A:
    $currentlabel = "NRI02A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '18'
    $date = '2'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG07AA2@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG07AA2@2x.jpg" as bg0 with dissolve
    play sound "SE06_02"
    pause (32/32.0)
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
    voice "NRI02A_X8000"
    老师 "「那么，今天所说的，关于『志愿』的问题，你们要好好考虑。不要再无所事事了，时间真的是转瞬即逝。」"
    play sound "SE00_22"
    "留下一堆吓唬人的话，老师转身走出了教室。"
    window hide
#BG_DSP_DEF 0,BG07AA3
    scene expression "img/BG07AA3@2x.jpg" as bg0 with dissolve
    play music  "BGM14"
    志雄 "「哈～」"
    "志愿吗……"
    "未来的路该怎么走，我脑子里还是一团糨糊……"
    "自己想走的路，自己的未来。"
    "大家是怎么决定的呢。"
    "为什么都能现在就下定决心呢。"
    "我没有什么特殊的技能，兴趣也是平凡得很。"
    "即使选择升学，我也只能通过笼统的所谓的『就业率』和『热门专业』来选择我的去向……"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG12AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG12AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 0
#CHR_POSC 1,(320-192)
#CHR_POSC 2,(320+192)
#CHR_SETTC 0,1,2,RI_MAA01,CH_MAA01,TO_MAB02
#FADE_IN 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA01"),"True","img/RI_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA01"),"True","img/CH_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh2 zorder (10+2):
        xcenter .8
    with dissolve
    play music  "BGM10"
    voice "NRI02A_TO000"
    亨 "「哈哈哈哈，啊哈哈哈哈～」"
    "楼顶上传来亨如同弱智般空洞的傻笑。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC04"),"True","img/RI_MAC04A@2x.png") as lh0 zorder (10+0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC06"),"True","img/CH_MAC06A@2x.png") as lh1 zorder (10+1)
    voice "NRI02A_CH000"
    智纱 "「没，没事吧？佐贺君……」"
    voice "NRI02A_RI000"
    莉莉丝 "「想到什么高兴的事，要是偷着乐不说出来，可是会被当做变态的哦。」"
    "箱崎向亨投去关心的目光，而莉莉丝则带着充满怜悯的眼神。"
    "午休时，我们和往常一样，四人一起聚在楼顶吃饭。"
    "自从和莉莉丝交往以来，这习惯一直没改过。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB01"),"True","img/TO_MAB01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI02A_TO001"
    亨 "「啊，对不起对不起。」"
    "总是自己一个人纠结也不是个办法，不如问问他们吧。"
    "我小心翼翼地提到『你们对将来有什么打算』这样的字句，结果却招来了亨一阵令人汗毛倒立的冷笑。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA06"),"True","img/TO_MAA06A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI02A_TO002"
    亨 "「前途，前途呢……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA05"),"True","img/TO_MAA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI02A_TO003"
    亨 "「被老师说『以你现在的成绩，哪所大学都考不上吧！真是不用烦恼选择学校的问题呢！』，这种事情……哈哈哈……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI02A_TO004"
    亨 "「哈……」"
    voice "NRI02A_CH001"
    智纱 "「那，那个……」"
    "箱崎露出生硬的微笑。她是我们四人中成绩最好的，亨的苦处她也难以理解吧。"
    志雄 "「亨。你真是这学校的学生吗……」"
    "我们学校怎么说也是以培养『升学生』为重点方向的……"
    "不过，亨也只是单纯的太贪玩了。撇开学习，他也懂些音乐，能组建乐队之类的，确实很厉害。"
    "最近他还买了摩托车。说起来，这家伙竟然真的能拿到驾照……"
    voice "NRI02A_RI001"
    莉莉丝 "「佐贺君也终于认清自己面前危机四伏的状况了吧。」"
    voice "NRI02A_TO005"
    亨 "「唔……」"
    志雄 "「说起来，莉莉丝你也是一样吧……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA06"),"True","img/RI_MAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI02A_RI002"
    莉莉丝 "「呃……不过，也没有像佐贺君说得那么惨啦……」"
    voice "NRI02A_RI003"
    莉莉丝 "「老师只是说，『随便选几所还能看的学校填上，把第三志愿也填满，然后再稍微努力下吧。』，这样的……」"
    志雄 "「你那只是『五十步笑百步』吧……可不要真随便填。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI02A_TO006"
    亨 "「是吗，所以我们是同伴吗！莉莉丝！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD03"),"True","img/RI_MAD03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI02A_RI004"
    莉莉丝 "「喂……我讨厌这种连带感……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA01"),"True","img/CH_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI02A_CH002"
    智纱 "「不过，想到谈论这个话题也就是说，塚本君难道也被老师说了些什么吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA05"),"True","img/TO_MAA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI02A_TO007"
    亨 "「原来是这样……于是你是想炫耀吗！？　我的话无论哪所学校都考得上，是吗！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAB01"),"True","img/RI_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI02A_RI005"
    莉莉丝 "「志雄的成绩真是出乎意料的『还可以』呢。」"
    志雄 "「『出乎意料』四个字是多余的。」"
    志雄 "「我只是，怎么说呢……想知道大家是如何决定自己前进的方向的……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI02A_TO008"
    亨 "「什么嘛，原来是这样啊。」"
    voice "NRI02A_TO009"
    亨 "「虽然我的状况就如刚才所说的那样一团糟，不过就目标上谈，我还是打算考偏文科的大学。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI02A_TO010A"
    亨 "「然后，在大学里也继续搞乐队，用我出色的吉他技术和细腻的乐感来迷倒万千女生！」"
    voice "NRI02A_TO010B"
    亨 "「再者就是，有一个在我车后坐着的可爱的女友，要像这样……紧紧地……身体和身体贴在一起……」"
    志雄 "「真是简单易懂的理由呢……」"
    if not persistent.dictlist[53] and persistent.show_dict:
        $persistent.dictlist[53]=True
        show screen dict_pop(i=53)
    "不过，要是音乐能拯救亨的话，作为去年的奏云祭音乐会优胜者的亨，应该早就大受欢迎了吧。"
    "可事实却是……这其中的矛盾，这家伙注意到了吗。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA06"),"True","img/TO_MAA06A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI02A_TO011"
    亨 "「哈，为了达成这个目的，稍微提升下自己的成绩也是必须的，所以我答应父母暑假时去补习了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI02A_TO012"
    亨 "「……为了买车而问父母借了钱，也不好反抗他们就是了……唉……」"
    "亨又叹了口气。虽说有些自作自受的味道，可他的确也挺辛苦的。"
    voice "NRI02A_CH003"
    智纱 "「我只是想顺着自己的选课，去考偏理科的学校……」"
    voice "NRI02A_CH004"
    智纱 "「无趣的回答真是对不起。」"
    志雄 "「没关系，在升学这种事上，完全追求兴趣也不切实际。所以，已经在为自己理想的大学而努力了吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAB01"),"True","img/CH_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI02A_CH005"
    智纱 "「恩。我第一志愿的『录取预期评估』是Ｂ，老师说，只要在暑假时冲刺一下应该没问题的。」"
    志雄 "「是吗……莉莉丝呢，是要考专科大学吗？」"
    if not persistent.dictlist[37] and persistent.show_dict:
        $persistent.dictlist[37]=True
        show screen dict_pop(i=37)
    voice "NRI02A_RI006"
    莉莉丝 "「是啊。反正是要继承婆婆的店，升不升学的也无所谓了……不过婆婆太啰嗦啦。」"
    voice "NRI02A_RI007"
    莉莉丝 "「所以，把婆婆的期望和我的期望折中一下，就是考专科大学了。志愿填的也是女子专科大学的营养学科。」"
    voice "NRI02A_RI008"
    莉莉丝 "「那样的话，对料理的技艺提升也会有帮助，学以致用，不是吗？」"
    "虽然嘴上说是随便选择的，实际上，莉莉丝也是有认真考虑呢。"
    voice "NRI02A_TO013"
    亨 "「可恶。我也想去和莉莉丝相同的学校……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC02"),"True","img/RI_MAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI02A_RI009"
    莉莉丝 "「呵呵。你想穿女装吗？」"
    stop music fadeout 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA05"),"True","img/TO_MAA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI02A_TO014"
    亨 "「啊……原、原来还有这一手！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC05"),"True","img/RI_MAC05A@2x.png") as lh0 zorder (10+0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC04"),"True","img/CH_MAC04A@2x.png") as lh1 zorder (10+1)
    with dissolve
    "一瞬间，除了亨外的所有人都向远离他的方向后退了一步……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA01"),"True","img/RI_MAA01A@2x.png") as lh0 zorder (10+0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA01"),"True","img/CH_MAA01A@2x.png") as lh1 zorder (10+1)
    with dissolve
    play music  "BGM10"
    voice "NRI02A_RI010"
    莉莉丝 "「那、那志雄呢？」"
    志雄 "「啊，我只是随随便便的考虑了一下而已……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA06"),"True","img/RI_MAA06A@2x.png") as lh0 zorder (10+0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA04"),"True","img/CH_MAA04A@2x.png") as lh1 zorder (10+1)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh2 zorder (10+2)
    with dissolve
#CHR_DSPTC 0,1,2,RI_MAA06,CH_MAA04,TO_MAB05
    voice "NRI02A_RI011"
    莉莉丝 "「是吗？你的回答真是含糊不清呢。」"
    voice "NRI02A_TO015"
    亨 "「是啊～不是你想和我们商量的吗？」"
    志雄 "「那个，我再考虑考虑吧……」"
    "我暧昧地笑了笑，试图蒙混过关。"
    "总不能说我连文科，理科都没决定吧，这样会令莉莉丝担心的。"
    voice "NRI02A_RI012"
    莉莉丝 "「志雄，你真的考虑了吗？」"
    志雄 "「当然。这不是显而易见的吗。」"
    莉莉丝 "「……」"
    "莉莉丝虽然表面上看上去大大咧咧，可内心还是很纤细的，有时会为了些小事而操心过度。"
    "没有决定好考哪所大学是我自己的问题。"
    "我不愿意因为我的犹豫不决而让她担心。"
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