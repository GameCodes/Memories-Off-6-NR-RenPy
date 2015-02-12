label NCH05A:
    $currentlabel = "NCH05A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '23'
    $date = '0'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 7,CAL_0723
    show expression "img/NIMG15G-568h@2x.jpg" as cal zorder 5
    show expression "img/07_23_SUNDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG79AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG79AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA04"),"True","img/TO_MBA04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE08_17L"
    pause (32/32.0)
#FADE_IN 1,128
#SE_VOLC 1,64
    play music "BGM09"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    voice "NCH05A_TO000"
    亨 "「所以说呢，你对我和莉莉丝说话的时候，和对智纱说话的时候，口气都不一样啊。明显是对智纱说话的时候口气更温柔」"
    志雄 "「哎哎？　是吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO001"
    亨 "「就是那样啊，从这一点来看，你缺少对我和莉莉丝的温柔！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO002"
    亨 "「我们可是挚友啊。再对我好点啊！」"
    志雄 "「别用那种让人听起来不舒服的说话方式！」"
    window hide
#SE_VOLC 1,128
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    if not persistent.dictlist[29] and persistent.show_dict:
        $persistent.dictlist[29]=True
        show screen dict_pop(i=29)
    "今天来到浜咲的购物中心的目的是为了准备和智纱的旅行。"
    "本来还想是不是要和智纱一起来，不过好像今天是莉莉丝有事。"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG17AA1@2x.jpg" as bg2 zorder 2
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCD01"),"True","img/RI_LCD01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#SE_VOLC 1,0,16
#MUS_VOL 0,16
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 0
#BG_ALPC 2,128
#CHR_ALPC 1,128
    voice "NCH05A_RI000_K"
    莉莉丝 "「今天智纱就借给我了。偶尔也必须加深一下女人之间的友情」"
    window hide
#BG_INIC 1
#BG_PRI 1
    scene expression "img/BG79AA@2x.jpg" as bg0
#BG_ALPC 0,128
    hide bg2
#BG_UVC 2,0,0,640,448
    hide lh1
#SE_VOLC 1,128
#MUS_VOL 128
    hide bg1
    with dissolve
    "莉莉丝说了那样的话。不过，也想让智纱能珍惜和我以外的人在一起的时间，我觉得那样也不错。"
    "因此，我就一个人来做旅行的准备了，结果在店里偶然碰见了亨。他好像是来买新发行的ＣＤ的。"
    window hide
#SE_VOLC 1,64
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA05"),"True","img/TO_MBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO003"
    亨 "「这么说来，昨天的夜里，我好好反省过了」"
    志雄 "「反省，发生了什么吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO004"
    亨 "「不是，昨天四个人一起去焰火大会了吧」"
    志雄 "「啊……」"
    "昨天是每年惯例的芦鹿岛焰火大会的日子，智纱，莉莉丝，我，亨这个一贯的组合就一起去了。"
    志雄 "「但是，那又怎么样呢？　我并没觉得有什么需要反省的事情啊。玩得挺开心的」"
    "虽说人太多了，很难看到焰火，但是那是规模如此大的焰火大会所以也没办法。就算反省也没有用。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB03"),"True","img/TO_MBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO005"
    亨 "「是啊，我也是那么想的啊。如果可能的话我还是希望莉莉丝能穿着浴衣来，但是那也没办法」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO006"
    亨 "「不管怎样，和莉莉丝一起逛这么多的店，我玩得也很高兴啊」"
    志雄 "「所以说不挺好的嘛」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB05"),"True","img/TO_MBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO007"
    亨 "「不是，光那样是不行的啊。光高兴还是不行的。到最后掉以轻心了」"
    志雄 "「最后掉以轻心了？　哪里？」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA05"),"True","img/TO_LBA05A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCH05A_TO008"
    亨 "「『一直是四人一起行动』的啊！」"
    "昨天，焰火大会上，我们基本是一直凑在一起行动的。因为人很多，为了不被冲散才这样做的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA03"),"True","img/TO_LBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO009"
    亨 "「失败了啊，应该从中间就开始两人一组行动的啊。那样的话我和莉莉丝，还有你和智纱都能两个人单独享受焰火了吧？」"
    志雄 "「我倒是觉得所有人一起也不错的」"
    if not persistent.dictlist[41] and persistent.show_dict:
        $persistent.dictlist[41]=True
        show screen dict_pop(i=41)
    "我们四人凑在一起出去玩的情况，最近很少有了。是从什么时候开始的呢……去年，去水族馆的时候吗？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA04"),"True","img/TO_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "我正考虑着那些事，感到了亨冷冷的眼神，正在对着我。"
    志雄 "「什，什么啊，你那眼神」"
    voice "NCH05A_TO010A"
    亨 "「……所以说，你是有女朋友的人啊。{w=6}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA03"),"True","img/TO_LBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO010B"
    extend "什么时候都能两个人单独在一起所以才这么从容不迫」"
    志雄 "「没有，我并没有打算要那样的！」"
    志雄 "「先，先不说这个，你还有别的ＣＤ要买吗？」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA04"),"True","img/TO_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO011A"
    亨 "「岔开话题是吗……{w=5}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO011B"
    extend "嘛，算了」"
    voice "NCH05A_TO012"
    亨 "「想要的ＣＤ是还有几张的，不过心有余而钱不足啊。今天就到此为止了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO013"
    亨 "「先不说我，你才是，买东西的事情都完了吗？」"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "已经都买完了":
            $F7=0
        "感觉好像还有什么忘掉的":
            $F7=1
    if F7==0:
        jump L_NCH05A_SEL00_A
    if F7==1:
        jump L_NCH05A_SEL00_B
label L_NCH05A_SEL00_A:
    $F104=1
#RSET F104
    志雄 "「嗯，没关系的。本来也没有什么特别要买的东西」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA05"),"True","img/TO_MBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO014"
    亨 "「这么说来，你是来买什么的啊？」"
    志雄 "「……没，就是有点」"
    "含混地支支吾吾着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB05"),"True","img/TO_MBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO015"
    亨 "「很奇怪啊。来买啥的你倒是说啊」"
    志雄 "「真的是没有什么特别要买的。只是来买点日用品的啊」"
    "如果告诉他来买和智纱一起去旅行用的东西的话，又会被他说成是「笨蛋情侣！」之类的，白白地招来他的怨恨。"
    voice "NCH05A_TO016"
    亨 "「哼～嗯……」"
    "亨又用一种怀疑的眼光看向我。"
    志雄 "「先不说那个，你是要跟莉莉丝一起去演唱会吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO017"
    亨 "「噢，你知道了啊？」"
    "亨得意地笑着。那高兴的表情就像已经追到手了一样。"
    志雄 "「啊。从莉莉丝那听说的」"
    voice "NCH05A_TO018"
    亨 "「这样啊。啊，邀请她去演唱会时回了我两个『去』。现在莉莉丝的心，已经对我熊熊燃烧起来了啊」"
    志雄 "「什么熊熊燃烧……你是哪个时代的人啊」"
    "可是，莉莉丝确实是说过，亨是以一种要跪下来的势头去求她的……。大概她说的才是正确的吧。"
    "但是，既然莉莉丝已经说了要去，那么他们的关系就在发展了……这么想也没错吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO019"
    亨 "「这个夏天——我们的关系要改变了」"
    "亨呵呵地笑着。"
    志雄 "「你啊，在之前的春假，好像也说过一样的话吧？」"
    "结果那次，假期结束之后也没什么变化。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO020"
    亨 "「这，这回可不一样了！」"
    "……怎么样呢。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG02EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression Solid("000") with None
#FADE_IN 0
    "…………。"
    "……。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
    scene expression "img/BG02EA@2x.jpg" as bg0 with dissolve
    play sound "SE08_17L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,128
    "在和亨告别后，回家的路上，我忽然想起了智纱的事。莉莉丝说过找她有事，是什么样的事情呢？"
    "……没有被莉莉丝戏弄就好了啊。"
    "我从口袋里取出手机，拨了智纱的号码。"
    window hide
#BG_SET_BACK 
#BG_PRIC 0
#EFF_PRI 0
#BG_INIC 3
    scene expression "img/NIMG01C@2x.png" as bg3 zorder 3 with dissolve
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
#SE_VOLC 1,64
#EFF_STAC 0,CLOUD_C,EFF_SKIP

    play sound "SE02_03"
    pause (16/32.0)
    play sound "SE02_02L"
    "智纱是不是已经回家了？"
    window hide
    play sound "SE08_04L"
    voice "NCH05A_CH000_K"
    智纱 "「喂喂。志雄君？」"
    "怎么了？　智纱那头，人声嘈杂，好像在街上一样。"
#SE_VOLC 0,(64/2)
    志雄 "「智纱，还在外面吗？」"
    voice "NCH05A_CH001_K"
    智纱 "「嗯，和莉莉丝在一起」"
    voice "NCH05A_CH002_K"
    智纱 "「有什么事吗？」"
    志雄 "「啊，没有」"
    "一时语塞。『忽然想起了智纱的事』这种话，总觉得很不好意思。"
    志雄 "「那个啊……对了，我在想、旅行的准备，智纱这边有没有问题」"
    voice "NCH05A_CH003_K"
    智纱 "「准备？　嗯，没问题的」"
    voice "NCH05A_CH004_K"
    智纱 "「莉莉丝要帮我买东西，现在一起到购物中心来了」"
    "什么啊。那么说来，和莉莉丝有事，是旅行的准备的事情啊。"
    voice "NCH05A_RI001_K"
    りりす？ "「什么，电话？　莫非是志雄打来的？」"
    "从智纱的声音的后面，传来了莉莉丝的声音。"
    voice "NCH05A_CH005_K"
    智纱 "「嗯，好像在担心旅行的准备是不是做好了」"
    voice "NCH05A_RI002_K"
    莉莉丝 "「真是的，真能操心呢～。电话，给我用下」"
    voice "NCH05A_CH006_K"
    智纱 "「嗯，好的」"
    voice "NCH05A_RI003_K"
    莉莉丝 "「喂，志雄。还好吗？」"
    志雄 "「一直到刚才还挺好的，听到了莉莉丝的声音就一下子就不好了」"
    voice "NCH05A_RI004_K"
    莉莉丝 "「这算什么啊！」"
    voice "NCH05A_RI005_K"
    莉莉丝 "「呃，如果你在我跟前的话，我就把你一脚踢飞了……」"
    "打电话真好。"
    voice "NCH05A_RI006_K"
    莉莉丝 "「看来你是挂念着智纱的事情才给她打电话的呢，比起担心别人不如先担心担心自己？　你才是啊，做好准备了没有？」"
    志雄 "「就算你不说，我也都准备好了啦」"
    voice "NCH05A_RI007_K"
    莉莉丝 "「这样啊。这样的话就好」"
    voice "NCH05A_RI008_K1"
    莉莉丝 "「又不是你，智纱的话才不用担心呢。还有我那美妙的建议在……你就期待着吧，呵呵」"
    "啥？　期待着？"
    voice "NCH05A_RI009_K"
    莉莉丝 "「拜拜～」"
    window hide
    play sound "SE02_08"
#SE_VOLC 1,128
#BG_ALP_AUTOC 0,128,0,F24,48
#ROUTINE_STA
    hide bg3
    scene expression "img/BG02EA@2x.jpg" as bg0
    with dissolve
#EFF_STPC 0,EFF_SKIP
#BG_PRIC 0
#EFF_PRI 0
#ROUTINE_STP
    "莉莉丝这家伙，随便就把电话挂了。"
    play sound "SE02_03"
    "而且还说什么……『期待着』？　是怎么回事？"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1,128
    stop se
    stop sound
    stop music fadeout 1
#FADE_IN 0
    scene expression "img/BG79AA@2x.jpg" as bg0 zorder 0 with dissolve
    $ renpy.end_replay()
    return
label L_NCH05A_SEL00_B:
    $F1+=1
    $F104=1
#RSET F104
    "是不是还有其它什么忘了准备或者必需的东西吗？　有没有忘掉什么呢……。"
    stop music fadeout 1
#SE_VOLC 1,128
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO021"
    亨 "「嗯？　在那边的，不是莉莉丝和智纱吗？」"
    "突然，亨指着我的身后说着。"
    志雄 "「哎？」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "顺着亨指着的方向看去，在那边的确实是智纱和莉莉丝的身影。"
    window hide
#SE_VOLC 1,64
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320+96)
#CHR_POSC 1,(320+224)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_SNB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_SDB04"),"not F103==0","img/CH_SNB04A@2x.png","True","img/CH_SDB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SCA03"),"True","img/RI_SCA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .9
    with dissolve
    play music "BGM10"
    voice "NCH05A_CH007"
    智纱 "「啊，志雄君」"
    voice "NCH05A_RI010"
    莉莉丝 "「还有佐贺君也在」"
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
#CHR_INIC 1
#CHR_POSC 0,(320+160)
#CHR_POSC 1,(320-160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA03"),"True","img/RI_MCA03A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NCH05A_TO022"
    亨 "「namasute～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA05"),"True","img/RI_MCA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_RI011"
    莉莉丝 "「那打招呼方式是什么啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO023"
    亨 "「最近我的个人流行」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA06"),"True","img/RI_MCA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_RI012"
    莉莉丝 "「佐贺君，到底怎么才会有这种让人难以捉摸的流行啊……」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDA01"),"not F103==0","img/CH_LNA01A@2x.png","True","img/CH_LDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "亨在和莉莉丝说话。我站在他们的旁边，转向智纱。"
    志雄 "「莉莉丝说要和你出来，是来这里啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNB06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDB06"),"not F103==0","img/CH_LNB06A@2x.png","True","img/CH_LDB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_CH008A"
    智纱 "「那个，{w=2}{nw}"
#MESA A_CH_CH,NCH05A_CH008A,"【智紗】「那个，"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDB01"),"not F103==0","img/CH_LNB01A@2x.png","True","img/CH_LDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_CH008B"
    extend "嗯，就是这样，莉莉丝说要帮我做旅行的准备。"
#MESA A_CH_CH,NCH05A_CH008B,"嗯，就是这样，莉莉丝说要帮我做旅行的准备。"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDB02"),"not F103==0","img/CH_LNB02A@2x.png","True","img/CH_LDB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_CH008C"
    extend "啊，啊哈哈」"
    "怎么了？　智纱笑得很不自然……。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDA01"),"not F103==0","img/CH_LNA01A@2x.png","True","img/CH_LDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_CH009"
    智纱 "「志雄君也是做旅行的准备？」"
    志雄 "「嗯」"
    "忽然看见，智纱的手里握着一个纸袋。"
    志雄 "「买什么了？在那个纸袋里」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDB04"),"not F103==0","img/CH_LNB04A@2x.png","True","img/CH_LDB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_CH010"
    智纱 "「哎？」"
    voice "NCH05A_CH011"
    智纱 "「啊，这个，这个是……！」"
    "智纱注意到了我的视线，慌慌张张地把纸袋藏到了背后。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDB03"),"not F103==0","img/CH_LNB03A@2x.png","True","img/CH_LDB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_CH012"
    智纱 "「啊，啊哈哈……」"
    "很明显是装出来的笑。"
    "很在意。那个纸袋里面，是什么呢？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDB01"),"not F103==0","img/CH_LNB01A@2x.png","True","img/CH_LDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_CH013"
    智纱 "「真，真的没有什么特别的」"
    "嗯嗯……既然不是什么特别的东西，那给我看看也可以吧。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,640
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDB01"),"not F103==0","img/CH_LNB01A@2x.png","True","img/CH_LDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCA06"),"True","img/RI_LCA06A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .75
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR0 ,(320-160)
#MOV_CHR1 128,(320+160)
#MOV_CHR_GO 1
    voice "NCH05A_RI013"
    莉莉丝 "「志～雄。少女啊，是有很多很多的秘密的哦。不过你可能没法理解就是了」"
    "莉莉丝责备我似地说道。"
    "虽说总觉得有点不爽，但是关于女孩子的心思，我也许确实不怎么清楚……。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCD03"),"True","img/RI_LCD03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH05A_RI014"
    莉莉丝 "「对不起啊，智纱。我这个弟弟不懂女孩子的心」"
    志雄 "「偏偏在这种时候摆姐姐的架子啊你」"
    "确实，既然莉莉丝成了老爸的女儿，她也就是我的姐姐了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDA01"),"not F103==0","img/CH_LNA01A@2x.png","True","img/CH_LDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_CH014"
    智纱 "「没事的，没关系的，你们不用在意，不管是志雄君还是莉莉丝」"
    "智纱一个劲地摇着头。"
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
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 0,(320-192)
#CHR_POSC 1,(320+192)
#CHR_POSC 2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDA01"),"not F103==0","img/CH_MNA01A@2x.png","True","img/CH_MDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCD03"),"True","img/RI_MCD03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .8
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO024"
    亨 "「话说回来，你们俩，还有什么要买的东西吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA01"),"True","img/RI_MCA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH05A_RI015"
    莉莉丝 "「没了，我已经没有要买的了。智纱你还有什么要买的吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDC01"),"not F103==0","img/CH_MNC01A@2x.png","True","img/CH_MDC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH05A_CH015"
    智纱 "「嗯，我的也已经都买完了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC01"),"True","img/RI_MCC01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH05A_RI016"
    莉莉丝 "「那就回去吧。佐贺君也一起回去？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCH05A_TO025"
    亨 "「请务必让小人陪同！」"
#CHR_DIAP_WC 1,2,620,428,10
#CHR_POS_SAVEC 1
#CHR_POS_SAVEC 2
#CHR_ALP_SAVEC 1
#CHR_ALP_SAVEC 2
    "忠犬·亨兴高采烈地摇着尾巴，跟着莉莉丝走了。"
#MES "忠犬゛亨兴高采烈地摇着尾巴，跟着莉莉丝走了。"
#THREAD_WAT 1
#MESX "%K%P"
#CHR_ERSWC 1,2
#CHR_ALPC 1,128
#CHR_ALPC 2,128
    window hide
#BG_PRI 0

#BG_SET_BACK 
#BG_INIC 2
#BG_UVC 2,(640/2),(448/4),(640/2),(448/2)
#BG_ALPC 2

#CHR_SET_BACK
#ROUTINE_STA
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 1,(320+130)
#CHR_POSC 2
#CHR_ALPC 1
#CHR_ALPC 2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
    with dissolve
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCD06"),"True","img/RI_MCD06A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#BG_ALP_AUTOC 0,0,0,F24,48
#BG_ALP_AUTOC 2,128,0,F24,48
#CHR_ALP_AUTOC 1,128,0,F24,48
#CHR_ALP_AUTOC 2,128,0,F24,48
#CHR_ALP_AUTOC 0,0,0,F24,48
#ROUTINE_STP
    hide lh0 with dissolve
#CHR_ALPC 0,128
#ROUTINE_STA
#BG_SWPC 0
    hide bg2 with dissolve
#BG_PRI 0
#BG_PRI 2
#CHR_PRIC 2
#CHR_PRIC 1
#CHR_SORT 1,2
#BG_ALPC 2,128
#BG_UVC 2,0,0,640,448
#ROUTINE_STP
    voice "NCH05A_RI017"
    莉莉丝 "「还有站在那边的笨蛋弟弟」"
    志雄 "「谁是笨蛋弟弟啊。再说了，别把我当弟弟对待」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCD01"),"True","img/RI_MCD01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH05A_RI018A"
    莉莉丝 "「从别人看来就像是弟弟一样，不是吗？{w=6}{nw}"
#MESA A_CH_RI,NCH05A_RI018A,"【りりす】「从别人看来就像是弟弟一样，不是吗？　"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC02"),"True","img/RI_MCC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH05A_RI018B"
    extend "管我叫姐姐大人也好啊」"
    志雄 "「绝对不会叫！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,((320-160)-(640/2))
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDB02"),"not F103==0","img/CH_LNB02A@2x.png","True","img/CH_LDB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .2
    with dissolve
#ROUTINE_STA
#CHR_ALP_AUTOC 0,128,1,F24,96
#CHR_ALP_AUTOC 1,0,1,F24,96
#CHR_ALP_AUTOC 2,0,1,F24,96
#CHR_POS_AUTOC 0,(320-160),F24,96
#CHR_POS_AUTOC 1,((320+160)+(640/2)),F24,96
#CHR_POS_AUTOC 2,((320)+(640/2)),F24,96
#BG_UV_AUTOC 0,(640/4),(448/4),(640/2),(448/2),1,F24,96,0
#ROUTINE_STP
#BG_UV_SAVEC 0
#CHR_PRIC ID_ALL
#CHR_SORT 0,1
    "看着我们这样的交谈，智纱温柔地笑了。"
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
    stop music fadeout 1
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_GOHOME
#CHR_DIAP_WC 1,2,620,620,40
#CHR_POS_SAVEC 1
#CHR_POS_SAVEC 2
#CHR_ALP_SAVEC 1
#CHR_ALP_SAVEC 2
#EOT