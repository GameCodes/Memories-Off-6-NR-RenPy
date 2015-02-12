label NCL02A:
    $currentlabel = "NCL02A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '20'
    $date = '4'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
    show expression "img/NIMG15F-568h@2x.jpg" as cal zorder 5
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
    show expression "img/BG33AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression Solid("000") with None
    play sound "SE00_00"
#FADE_IN 0
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "持续了一上午的散学式结束了，回到家中，一股诱人食欲的香味在室内弥漫着。"
    play sound "SE03_94"
    志雄 "「是我太饿产生错觉了吗……」"
    "从客厅的方向传来了啪嗒啪嗒的拖鞋声。"
    志雄 "「难道？」"
    window hide
#FADE_OUT 0
    scene expression "img/BG33AA@2x.jpg" as bg0 with dissolve
#BG_COLC 0,128,128,128,128
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB06"),"True","img/CL_MAB06A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter .75
    with dissolve
    stop se
#FADE_IN 1
    play music "BGM04"
    voice "NCL02A_KU000"
    克罗艾 "「啊，志雄，欢迎回家。」"
    "如预想一般，克罗艾学姐正在那里做着吐司和沙拉，桌子上还放着煎蛋卷。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB05"),"True","img/CL_MAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU001"
    克罗艾 "「怎么了，傻傻地站着？」"
    志雄 "「啊，那个……我回来了！」"
    window hide
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB02"),"True","img/CL_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    pause (16/32.0)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "对着慌忙做出反应的我，学姐把手贴到腰上，深深地点了点头。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC01"),"True","img/CL_MAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU002"
    克罗艾 "「嗯。那么，马上午饭就能做好了，你先去换衣服洗手吧。」"
    志雄 "「好……」"
    voice "NCL02A_KU003"
    克罗艾 "「啊，还有，一会儿要出门，所以不要直接换了睡衣哦。」"
    志雄 "「出门？去哪里？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB06"),"True","img/CL_MAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU004"
    克罗艾 "「当然是约会啦~♪」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "说了那样的话之后，学姐返回了厨房。"
    志雄 "「约会……？」"
    "完全没有一点前奏讯号。"
    "虽然总觉得有些突然，但不管怎么说，雀跃起来的心情倒是格外的真实。"
    志雄 "「总之，先去换衣服吧。」"
    window hide
#FADE_OUT 1
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC01"),"True","img/CL_LAC01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_IN 1
    "看着换好衣服从房间里出来的我，学姐流露出很满意的表情。"
    voice "NCL02A_KU005"
    克罗艾 "「很好。看来有很听话地换好衣服了呢。」"
    志雄 "「说起来，为什么要突然约会呢？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC05"),"True","img/CL_LAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#REEK_CHR 0
    voice "NCL02A_KU006"
    克罗艾 "「那是……那个。」"
#REMOVE_REEK_CHR 0
    "带着疑惑，问题似乎有些刻意。不过学姐匆忙含糊了一下之后，马上改变了话题。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC04"),"True","img/CL_LAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU007"
    克罗艾 "「你看、好不容易做的午饭要变凉了哦。」"
    志雄 "「那个，克罗艾学姐？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC01"),"True","img/CL_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU008"
    克罗艾 "「我也还没有吃东西，肚子都快饿扁了呢。还是先吃饭吧。」"
    "真是相当强硬的掩饰方式呢。也罢，大概现在还不想说吧。"
    志雄 "「我知道了……」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/EXBG09A@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/EXBG09A@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_IN 1
    "说完，我就对手边的沙拉开动了。"
    志雄 "「诶？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB03"),"True","img/CL_ZAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU009"
    克罗艾 "「怎么了？」"
    志雄 "「没有，总觉得和之前调料的味道有些不一样。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB04"),"True","img/CL_ZAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU010"
    克罗艾 "「注意到了？　时间有些宽裕，所以就试着做了一下。」"
    志雄 "「那样的话，费了很大一番工夫吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU011"
    克罗艾 "「制作过程本身并不复杂呢。只是费了一点时间，不过不能长期保存，真是美中不足。」"
    志雄 "「……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAA02"),"True","img/CL_ZAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU012"
    克罗艾 "「难道不合你的口味吗？」"
    "说完感慨的我不知不觉地陷入了沉思，当回过神来的时候，克罗艾学姐正用很担心的神情注视着我。"
    志雄 "「啊，不，很美味呢。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAA01"),"True","img/CL_ZAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU013"
    克罗艾 "「太好了！」"
    "看着克罗艾学姐的笑容，总感到心中有一种无法释然的东西在慢慢扩散。"
    "果然学姐的含糊里，还是隐藏了什么吧……"
    "不过，算了——"
    志雄 "「这个煎蛋卷火候真的是非常到位呢，特别的好吃！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB06"),"True","img/CL_ZAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU014"
    克罗艾 "「是吗？」"
    "无论有什么样的理由，对我而言，与克罗艾学姐一起度过的时间用什么也无法替代。"
    "所以，在她本人想说之前，就姑且耐心等待吧。"
    window hide
#MUS_VOL 64
#FADE_OUT 1
#BG_PRI 0
##FADE_IN 0
    "…………"
    "……"
    window hide
##FADE_OUT 0
#BG_COLC 0,128,128,128,128
#BG_PRI 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#MUS_VOL 128
#FADE_IN 1
    志雄 "「啊，谢谢款待。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB02"),"True","img/CL_ZAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU015"
    克罗艾 "「嗯、粗茶淡饭而已。」"
    show expression "img/BG33AA@2x.jpg" as bg_over zorder 2 with dissolve
    play sound "SE03_53"
    "吃完饭后，两个人开始收拾饭桌。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC01"),"True","img/CL_MAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「说起来、约会是要去哪里呢？」"
    if not persistent.dictlist[29] and persistent.show_dict:
        $persistent.dictlist[29]=True
        show screen dict_pop(i=29)
    voice "NCL02A_KU016"
    克罗艾 "「想去一趟浜咲的购物中心。」"
    if not persistent.dictlist[56] and persistent.show_dict:
        $persistent.dictlist[56]=True
        show screen dict_pop(i=56)
    志雄 "「那么坐电车去？　不过我觉得会很拥挤的样子」"
    "考虑到今天是散学式，明天开始就是暑假了。"
    "不管在哪里，肯定都是大批大批的从学校的束缚中解放出来的学生。"
    voice "NCL02A_KU017"
    克罗艾 "「不过，机会难得呢，对吧？　我今天也正好有时间」"
    志雄 "「嘛，倒是可以。」"
    "不知是否太过敏感了，学姐所说的话里，似乎有刻意强调『今天』这个概念，让我稍微有点在意。"
    window hide
    stop se fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/NIMG01B@2x.png" as bg0 zorder 0 with dissolve
    show expression "img/CloudB1_0@2x.png" as cloud0 zorder 5:
        ycenter .55
        xcenter .75
        linear 500 xcenter .0
    show expression "img/CloudB1_1@2x.png" as cloud1 zorder 5:
        ycenter .55
        xcenter .65
        linear 500 xcenter .0
    show expression "img/CloudB2_0@2x.png" as cloud2 zorder 8:
        ycenter .3
        block:
            xcenter 1.0
            linear 140 xcenter .0
            repeat
    show expression "img/CloudB2_1@2x.png" as cloud3 zorder 8:
        ycenter .2
        block:
            xcenter 1.0
            linear 100 xcenter .0
            repeat
    show expression "img/CloudB2_2@2x.png" as cloud4 zorder 8:
        ycenter .0
        block:
            xcenter 1.0
            linear 120 xcenter .0
            repeat
    show expression "img/CloudB3@2x.png" as cloud5 zorder 10:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.5
            linear 50 xpos .0
            xpos 1.0
            linear 50 xpos .5
            repeat
    show expression "img/CloudB4@2x.png" as cloud6 zorder 12:
        xanchor 1.0
        yalign 1.0
        block:
            xpos .6
            linear 78 xpos .0
            xpos 1.0
            linear 52 xpos .6
            repeat
    show expression "img/CloudB5@2x.png" as cloud7 zorder 15:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.2
            linear 20 xpos .0
            xpos 1.0
            linear 100 xpos .2
            repeat
    with dissolve
#EFF_STAC 0,CLOUD_B,EFF_NOSKIP
##FADE_IN 0
    "…………"
    "……"
    window hide
##FADE_OUT 0
    scene expression "img/BG100AA@2x.jpg" as bg0 with dissolve
    play sound "RAILWAY_003"
    play sound "SE08_17L"
    pause (32/32.0)
#FADE_IN 1
    "乘着晃荡而拥挤的电车来到了浜咲，人比预想中的还要多的多。"
    "携眷出行的人、情侣等等，大家都想饱享这个夏天，所以都在愉快地说笑着。"
    window hide
#FADE_OUT 0
#EFF_STPC 0,EFF_SKIP
    hide bg0 with dissolve
    show expression "img/BG100AA@2x.jpg" as bg0 zorder 0 with dissolve
#BG_BLUR 0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+96)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC04"),"True","img/CL_LAC04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter .65
    with dissolve
#FADE_IN 0
    play music "BGM10"
    志雄 "「好、好、好多人。」"
    voice "NCL02A_KU018"
    克罗艾 "「这真是不得了呢。」"
    "两个人都不由自主地露出了苦笑。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC01"),"True","img/CL_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL02A_KU019"
    克罗艾 "「不过，好不容易来了。就到处逛逛看看吧。」"
    志雄 "「是啊。在这里站着也不是办法。」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_BLUR 0
    play sound "SE01_12L"
    "为了不会走散我们紧紧地牵着手，走进了人山人海当中。"
    window hide
    stop se fadeout 1
#SE_VOLC 1,0
#BG_SET_BACK 
#BG_INIC 1
    #show expression "img/BG_BLACK@2x.jpg" as bg1 with dissolveBG_LINEAR_SLIDE
#FADE_OUT 0
#GRAPH_ERS
    stop se
#BG_SET_BACK 
#BG_INIC 0
    #show expression "img/BG43AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG43AA@2x.jpg" as bg0 with dissolve
#SE_VOLC 1,128
#FADE_IN 1
    "先问问学姐想去哪里吧。"
    window hide
#SE_VOLC 1,(64/2)
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh0 zorder 100:
        ypos 0.0
        xcenter .65
    with dissolve
    志雄 "「那么，从哪里开始逛呢？」"
    "虽说作为男生这样说会让人觉得很不用心，不过这次主题未知、突如其来的约会是学姐邀请的，还真是没办法呢。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB02"),"True","img/CL_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL02A_KU020"
    克罗艾 "「呃……果然，说到夏天就要说泳装了吧？」"
    志雄 "「泳装吗？」"
    "克罗艾学姐穿泳装的样子……稍微想象了一下。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL02A_KU021"
    克罗艾 "「虽然离海非常近，不过这个夏天一次也没有去游过呢」"
    志雄 "「虽然是个很好的提议，不过我想这里和附近的海滩现在都很拥挤的吧？」"
    "这附近的海岸相当的知名，每年的这个季节都会有非常多的游客来这里的海水浴场。"
    "虽然从内陆来的人会乐在其中，不过对于看惯了海的本地人而言，这个季节的海滩实在是太过拥挤了。"
    志雄 "「如果是游泳的话，休闲泳池之类的地方不是也可以吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA02"),"True","img/CL_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL02A_KU022"
    克罗艾 "「游泳池不是更拥挤了么？　而且，海和游泳池是完全不一样的两个东西呀。」"
    志雄 "「哈，确实是对海更怀有感情呢。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA01"),"True","img/CL_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL02A_KU023"
    克罗艾 "「而且，试着找一找说不定会有意想不到的好地方呦？」"
    "克罗艾学姐直接无视了我的担忧。"
    志雄 "「已经有什么既定的目标了吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB06"),"True","img/CL_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL02A_KU024"
    克罗艾 "「嗯，谁知道呢？」"
    "虽然这么说、但是学姐看起来相当有自信。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL02A_KU025"
    克罗艾 "「嘛，不过有目标现在也没有泳装呢。」"
    志雄 "「是啊，呃，泳装卖场在……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC01"),"True","img/CL_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL02A_KU026"
    克罗艾 "「好像是那边呢。」"
    window hide
    play sound "SE01_12L"
    pause (16/32.0)
    stop se fadeout 1
#BG_SET_BACK 
#BG_INIC 1
    #show expression "img/BG_BLACK@2x.jpg" as bg1 with dissolveBG_LINEAR_SLIDE
#FADE_OUT 0
    scene expression Solid("000") with fade
    stop se
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,(448/4),(640/2),(448/2)
    scene expression "img/BG79AA@2x.jpg" as bg0 with dissolve
#FADE_IN 0
    "用手不断地分开拥挤的人流，终于到达了泳装卖场，等待着我的是……"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_IN 1
    voice "NCL02A_KU027"
    克罗艾 "「稍微试穿一下哦。」"
    志雄 "「请、请便。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB04"),"True","img/CL_LAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU028"
    克罗艾 "「偷看可不行哦……！」"
    志雄 "「才不会呢！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB06"),"True","img/CL_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU029"
    克罗艾 "「哈哈。」"
    window hide
    play sound "SE03_16"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "恶魔的诱惑？　女神的诱惑？"
    "无论是哪边都是残酷的战斗呢。"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    hide bg1 with dissolve
#BG_SET_BACK 
#BG_INIC 1
    #show expression "img/BG_BLACK@2x.jpg" as bg1 zorder 1 with dissolve
##FADE_IN 0
    "…………"
    "……"
    window hide
##FADE_OUT 0
    hide bg1 with dissolve
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG79AA@2x.jpg" as bg0 zorder 0 with dissolve
#BG_BLUR 0
    scene expression "img/BG79AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB06"),"True","img/CL_LAB06A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#SE_VOLC 1,(64/2)
#FADE_IN 1
    voice "NCL02A_KU030"
    克罗艾 "「真不愧是大商场，东西很全，质量也很不错呢。」"
    "克罗艾学姐心情十分愉快，手里紧紧抱着刚才买的泳装的袋子。"
    志雄 "「……」"
    "试了好几件泳装的学姐，最后并没有告诉我买的是哪一件。说是一起去海边之前的秘密。"
    "……老实地说，我很在意。"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "下决心试着问":
            $F7=0
        "乐趣应该保留到以后":
            $F7=1
        "比起那种事情还是帮学姐拎东西要紧":
            $F7=2
    if F7==0:
        jump L_NCL02A_SEL00_A
    if F7==1:
        jump L_NCL02A_SEL00_B
    if F7==2:
        jump L_NCL02A_SEL00_C
label L_NCL02A_SEL00_A:
    "我无法抑制住自己的好奇心，不禁向学姐问道。"
    志雄 "「那个，学姐。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02X_KU000"
    克罗艾 "「怎么了？」"
    志雄 "「还是请告诉我吧，学姐买了什么样的泳装——」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB02"),"True","img/CL_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02X_KU001"
    克罗艾 "「不行」"
    "立刻就被否决了。"
    "问到最后学姐也没有告诉我。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02X_KU002"
    克罗艾 "「不要那么心急嘛，到海边自然就能看见了哦？」"
    "看来还是不肯告诉我的样子。"
    志雄 "「也是呢……」"
    jump L_NCL02A_SEL00_X
label L_NCL02A_SEL00_B:
    "……算了，乐趣应该保留到以后。"
    "学姐也那么说了，现在还继续追问的话，会显得别有用心吧。"
    "……当然，也不能问心无愧的说完全没有那样的念头。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB03"),"True","img/CL_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU031"
    克罗艾 "「怎么了吗？」"
    "学姐看着在想那些事情的我，很好奇地问我。"
    志雄 "「啊，没，没什么」"
    "我慌忙的摇了摇头。"
    jump L_NCL02A_SEL00_X
label L_NCL02A_SEL00_C:
    志雄 "「学姐，东西我来拿吧？」"
    "之后去哪里逛还没有决定，不过今天的日程显然没有到此为止。作为男生，不帮着拿东西可不行。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA01"),"True","img/CL_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02X_KU003"
    克罗艾 "「有那么在意吗……？」"
    "学姐浮现出恶作剧的笑容看着我。"
    志雄 "「呃？　在意是指？」"
    voice "NCL02X_KU004"
    克罗艾 "「不过不行哦。在去海边之前这可是秘密。」"
    "仿佛在防着我偷看购物袋中东西的样子。"
    志雄 "「啊，不，不是那样的啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA02"),"True","img/CL_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02X_KU005"
    克罗艾 "「诶，那你完全不在意的吗？」"
    "学姐露出些许生气的表情。"
    志雄 "「那，那个……当、当然在意啦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA01"),"True","img/CL_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02X_KU006"
    克罗艾 "「那么，果然还是不能让志雄拿呢～」"
    "说了这样的话，学姐把购物袋紧紧地抱在怀里。"
    jump L_NCL02A_SEL00_X
label L_NCL02A_SEL00_X:
    window hide
#BG_GET_NOC 0,F34
#BG_SET_BACK 
#BG_INIC 2
    #show expression "img/F34@2x.jpg" as bg2 zorder 2 with dissolve
#SE_VOLC 1,64
#MUS_VOL 64
#ROUTINE_STA
#BG_UV_AUTOC 0,(640/2),((448/4)+512),(640/2),(448/2),1,F24
#BG_UV_AUTOC 2,(640/2),((448/4)+0),(640/2),(448/2),1,F24
#BG_ALP_AUTOC 0,0,1,F24
#CHR_ALP_AUTOC 0,0,1,F24
#CHR_SCL_AUTOC 0,512,512,1,F24
#CHR_POS_AUTOC 0,0,F24
#ROUTINE_STP
#BG_UV_SAVEC 0
#BG_UV_SAVEC 2
#BG_ALP_SAVEC 0
#CHR_ALP_SAVEC 0
#CHR_SCL_SAVEC 0
#CHR_POS_SAVEC 0
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_ALPC 0,128
#CHR_SCLC 0,256,256
#BG_SWPC 0
    hide bg2 with dissolve
#BG_PRI 0
#BG_PRI 2
#BG_ALPC 2,128
    "这个时候——一个小女孩和她父母一家三口从我们面前走过。"
    voice "NCL02A_KU032"
    克罗艾 "「果然，哪里人都很多呢。全家一起外出的好像也特别的多哦。」"
    "看到了那样的情景，克罗艾学姐不禁小声地嘟囔着。"
    window hide
    hide bg1 with dissolve
#BG_SWPC 0
#BG_PRI 1
#BG_PRI 0
#BG_GET_NOC 1,F34
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC01"),"True","img/CL_LAC01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#BG_BLUR 0
#SE_VOLC 1,(64/2)
#MUS_VOL 128
    hide bg1 with dissolve
    志雄 "「是啊，这就是所谓的家族休闲吧？」"
    "目光追随在那一家三口后面的克罗艾学姐，现在是什么样的感觉呢……无法想象。"
    "但是，看到学姐那样的神情，我决定强行改变一下话题。"
    志雄 "「对了，这次去看看浴衣吧！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC05"),"True","img/CL_LAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCL02A_KU033"
    克罗艾 "「诶？」"
#REMOVE_REEK_CHR 0
    志雄 "「啊？」"
    "老实说学姐的反应是我没有料到的。比预想的还要吃惊的样子……"
#REEK_CHR 0
    voice "NCL02A_KU034"
    克罗艾 "「为、为什么，要看浴衣？」"
#REMOVE_REEK_CHR 0
    "简直就像发现了恶作剧的孩子一样呢……"
    志雄 "「说什么呢啊？２２号的焰火大会，提议穿浴衣的不是学姐吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC04"),"True","img/CL_LAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU035"
    克罗艾 "「啊，对呢。」"
    志雄 "「……」"
    "看着微妙地小声嘟囔着的学姐，那心情不好的样子实在有些奇怪，还是先去找衣服卖场吧。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    pause (32/32.0)
    stop music fadeout 1
#BG_UVC 0,0,0,640,448
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB05"),"True","img/CL_MAB05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#BG_BLUR 0
#FADE_IN 1
    play music "OBGM14"
    voice "NCL02A_KU036"
    克罗艾 "「……」"
#MESEX_A M_NOA,A_CH_KU,NCL02A_KU036,"【クロエ】「……」%K%P"
    "在卖场的时候，克罗艾学姐的表情一直看起来很不好，还是问一问吧。"
    志雄 "「果然，发生了什么吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB03"),"True","img/CL_MAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU037"
    克罗艾 "「不，什么也没有。」"
    志雄 "「真的吗？　有什么说出来也没关系的。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC03"),"True","img/CL_MAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU038"
    克罗艾 "「那，我说了哦……」"
    "再次询问之后，克罗艾学姐终于看上去很难为情地开口了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC02"),"True","img/CL_MAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU039"
    克罗艾 "「其实，我有必须向志雄道歉的事情。」"
#REEK_CHR 0
    志雄 "「诶？」"
#REMOVE_REEK_CHR 0
    voice "NCL02A_KU040"
    克罗艾 "「总之，先找个地方坐下来吧。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "学姐一副抱歉的表情，拉着我的手走进了附近的某个餐厅。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/EXBG11A@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/EXBG11A@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC02"),"True","img/CL_ZAC02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE00_38"
    play sound "SE07_22L"
#FADE_IN 1
    stop music fadeout 1
    voice "NCL02A_KU041"
    克罗艾 "「对不起。」"
    "在店员带我们走到座位点完东西之后，学姐突然低下了头。"
    "突然听到学姐这么说，完全出乎我的意料，不自觉的有些惊慌失措。"
    志雄 "「等、等一下。我完全不知道学姐有什么地方需要道歉的啊。」"
    voice "NCL02A_KU042"
    克罗艾 "「其实，是焰火大会的事情。」"
    "在低了一分钟左右的头之后，学姐总算抬起了头。"
    志雄 "「呃，那么浴衣——」"
    window hide
    play music "OBGM08"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC03"),"True","img/CL_ZAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU043"
    克罗艾 "「虽然是那样说……可是实际上，我的打工安排有了了调整。」"
    志雄 "「啊……」"
    "克罗艾学姐，从进入大学之后开始打工。"
    "『学费之类的，多少也要靠自己挣一些。』她开玩笑般地说了这样的话。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC02"),"True","img/CL_ZAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU044"
    克罗艾 "「一起打工的人受伤了很为难，我必须要去代班了……对不起。」"
    志雄 "「那个……」"
    voice "NCL02A_KU045"
    克罗艾 "「更早一些说出来就好了，可是无论如何也说不出口……」"
    "克罗艾学姐是真的十分抱歉的样子。"
    "对我来说，怎么说呢，虽然那确实是很让人失望的话不过我却已经没有任何的不满情绪了。"
    志雄 "「什么嘛，是这么回事啊……」"
    "不知不觉，嘴角露出了笑容。"
    "从学姐深刻的表情来看，还以为是更加重大的问题呢，不过看起来好像是我杞人忧天了。"
    voice "NCL02A_KU046"
    克罗艾 "「那个，志雄？」"
    志雄 "「学姐，没关系。请不用在意的」"
    志雄 "「焰火大会之类的，也不是什么只有今年才有的。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC03"),"True","img/CL_ZAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU047"
    克罗艾 "「可是，明明约好了的……」"
    志雄 "「学姐没有放着有困难的同事不管呢。　做得很对啊。没必要那么忧虑的」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC02"),"True","img/CL_ZAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU048"
    克罗艾 "「可是……」"
    志雄 "「对了。」"
    "面对仍没有抬起头的学姐，我提出了交换条件。"
    志雄 "「那么，作为交换能听听我的愿望吗？」"
    stop music fadeout 1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC05"),"True","img/CL_ZAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCL02A_KU049"
    克罗艾 "「诶？」"
#REMOVE_REEK_CHR 0
    志雄 "「因为我也因此受了很大的挫折，所以今天的晚饭请务必做牛肉饼补偿一下吧！」"
    "我提出了玩笑一样的愿望。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB03"),"True","img/CL_ZAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "看着那样的我，克罗艾学姐愣了一下，不过马上就捂着嘴笑了起来。"
    window hide
    play music "BGM13"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB06"),"True","img/CL_ZAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU050"
    克罗艾 "「志雄你啊，真是的……」"
    志雄 "「哼哼，那么接受了是吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB02"),"True","img/CL_ZAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL02A_KU051"
    克罗艾 "「嗯。请让我全力来做吧，主人～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "应对我夸张的表达方式，学姐也玩笑一般的回答了。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/NIMG01C@2x.png" as bg0 zorder 0
    show expression "img/CloudC1_0@2x.png" as cloud0 zorder 5:
        ycenter .55
        xcenter .75
        linear 500 xcenter .0
    show expression "img/CloudC1_1@2x.png" as cloud1 zorder 5:
        ycenter .55
        xcenter .65
        linear 500 xcenter .0
    show expression "img/CloudC2_0@2x.png" as cloud2 zorder 8:
        yalign .0
        block:
            xcenter 1.0
            linear 140 xcenter .0
            repeat
    show expression "img/CloudC2_1@2x.png" as cloud3 zorder 8:
        ycenter .2
        block:
            xcenter 1.0
            linear 100 xcenter .0
            repeat
    show expression "img/CloudC2_2@2x.png" as cloud4 zorder 8:
        yalign .0
        block:
            xcenter 1.0
            linear 120 xcenter .0
            repeat
    show expression "img/CloudC2_3@2x.png" as cloud8 zorder 8:
        ycenter .0
        block:
            xcenter 1.0
            linear 135 xcenter .0
            repeat
    show expression "img/CloudC3_0@2x.png" as cloud5 zorder 10:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.5
            linear 50 xpos .0
            xpos 1.0
            linear 50 xpos .5
            repeat
    show expression "img/CloudC3_1@2x.png" as cloud6 zorder 12:
        xanchor 1.0
        yalign 1.0
        block:
            xpos .6
            linear 78 xpos .0
            xpos 1.0
            linear 52 xpos .6
            repeat
    show expression "img/CloudC4@2x.png" as cloud7 zorder 15:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.2
            linear 20 xpos .0
            xpos 1.0
            linear 100 xpos .2
            repeat
    with dissolve
#EFF_STAC 0,CLOUD_C,EFF_NOSKIP
    play sound "SE05_13L"
    pause (32/32.0)
    play sound "SE01_12L"
#FADE_IN 1
    "在一阵开心的笑声之后，我和克罗艾学姐又去卖食材的地方买了些东西，便踏上了回家的路。"
    "今晚的牛肉饼一定会是到有史以来最美味的食物——这样想着，踏上归路的脚步也比变得轻盈了起来。"
    "虽然，不能和学姐一起去焰火大会虽然很遗憾，不过明年再一起去就好了。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    hide bg0 with dissolve
#BG_SET_BACK
#BG_INIC 0
#BG_PRI 0
    scene expression "img/BG37EA@2x.png" as bg0 zorder 0 with dissolve
    show expression "img/trainoutside_E@2x.png" as train_bg zorder -5
    show expression "img/trainoutside_tree1_E@2x.png" as train_tree1 zorder -2:
        ycenter .5
        block:
            xcenter .4
            linear 0.5 xcenter -.1
            repeat
    show expression "img/trainoutside_tree1_E@2x.png" as train_tree1 zorder -2:
        ycenter .5
        block:
            xcenter .6
            linear 0.5 xcenter 1.1
            repeat
    show expression "img/trainoutside_tree0_E@2x.png" as train_tree2 zorder -2:
        ycenter .5
        block:
            xcenter .4
            linear 0.7 xcenter -.1
            repeat
    show expression "img/trainoutside_house1_E@2x.png" as train_house1 zorder -3:
        ycenter .47
        block:
            xcenter .4
            linear 0.7 xcenter -.1
            repeat
    show expression "img/trainoutside_house1_E@2x.png" as train_house1 zorder -3:
        ycenter .47
        block:
            xcenter .7
            linear 0.7 xcenter 1.1
            repeat
    show expression "img/trainoutside_house2_E@2x.png" as train_house2 zorder -3:
        ycenter .5
        alpha 0
        pause .5
        alpha 1
        block:
            xcenter .4
            linear 0.7 xcenter -.1
            repeat
    with dissolve
    show expression "img/trainoutside_house1_E@2x.png" as train_house3 zorder -3:
        ycenter .47
        alpha 0
        pause .9
        alpha 1
        block:
            xcenter .4
            linear 0.7 xcenter -.1
            repeat
    with dissolve
#EFF_STAC 0,TRAINWINDOW2,EFF_NOSKIP
#BG_ZOOM_RATE 0,8
#BG_PRI 0
    stop se
    stop sound
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_PRIC 0
#CHR_POSC 0,320
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA07"),"True","img/CL_LAA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#CHR_ALPC 0,128
    play sound "SE06_10L"
#FADE_IN 1
#EFF_STAC 1,QUAKE_TRAIN,EFF_NOSKIP
#EFF_STAC 2,QUAKE_CHR_TRAIN,EFF_NOSKIP
    pause (32/32.0)
    voice "NCL02A_KU052"
    克罗艾 "「志雄……」"
    志雄 "「啊？」"
    voice "NCL02A_KU053"
    克罗艾 "「谢谢……」"
    志雄 "「嗯。」"
    "永远在一起的话，一定……就算今年不行，明年也一定行的……"
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