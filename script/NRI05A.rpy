label NRI05A:
    $currentlabel = "NRI05A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '20'
    $date = '4'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 7,CAL_0720
    show expression "img/NIMG15J-568h@2x.jpg" as cal zorder 5
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
    show expression "img/BG02AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG02AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_15L"
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
    志雄 "「喂～还有啊……稍微休息一下吧。」"
    window hide
    stop sound fadeout 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA06"),"True","img/RI_MCA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM10"
    voice "NRI05A_RI000"
    莉莉丝 "「你还真是没用啊～」"
    "明明已经无条件的把我当做拎东西的机器在使唤了，却还抱怨我不够卖力。"
    "我们正在为旅行而购买各种必需品。"
    "于是，从刚才起，衣服，包，以及其它各种东西就在不断填满我的双手……"
    志雄 "「又不是去国外旅行，不必这么认真吧……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA01"),"True","img/RI_MCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI001"
    莉莉丝 "「有什么关系。为旅行做准备也是旅行的不可忽略的乐趣之一哦。」"
    志雄 "「话是这么说……」"
    "学校的散学式已经结束，有一阵子可以不用去了。"
    "记得在我们离开学校前，老师还一脸正经地说着『这点时间用来玩还不如多学点东西』之类的话。"
    "要是在这种地方被老师看到……又不知道会被说些什么了……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC02"),"True","img/RI_MCC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI002"
    莉莉丝 "「那么，接下来去那边！」"
    志雄 "「好好……」"
    voice "NRI05A_RI003"
    莉莉丝 "「快点快点～♪」"
    window hide
    play sound "SE01_02L"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "莉莉丝兴奋地跑向那里。"
    "看到她那笑容，我无奈地摇了摇头，赶忙跟着过去……"
    志雄 "「真没办法呢……」"
    window hide
    stop music fadeout 132
    stop se fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 1
#BG_ALPC 0
#BG_SETWC 0,1,BG79AA,EVN_RI02A
    scene expression "img/BG79AA@2x.jpg" as bg0 with dissolve
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI02A")]=True
    show expression "img/EVN_RI02A@2x.jpg" as bg1 with dissolve
    pause (32/32.0)
#FADE_IN 1
    play music  "BGM01NL"
    voice "NRI05A_RI004"
    莉莉丝 "「嗯～」"
    志雄 "「喂，还有吗？」"
    voice "NRI05A_RI005"
    莉莉丝 "「嗯……」"
    志雄 "「差不多了吧……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI02B")]=True
    show expression "img/EVN_RI02B@2x.jpg" as bg1 with dissolve
    voice "NRI05A_RI006"
    莉莉丝 "「真是的！人家在犹豫不决的时候，你能不能保持男士应有的风度啊。」"
    志雄 "「可是你已经犹豫了３０分钟了啊……」"
    voice "NRI05A_RI007"
    莉莉丝 "「因，因为……实在难以抉择嘛。」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI02A")]=True
    show expression "img/EVN_RI02A@2x.jpg" as bg1 with dissolve
    "莉莉丝在犹豫要买哪件泳衣。"
    "她以那种在学习时绝对见不到的认真的眼神，比对着手上的不同款式。"
    志雄 "「真拿你没办法……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI02C")]=True
    show expression "img/EVN_RI02C@2x.jpg" as bg1 with dissolve
    voice "NRI05A_RI008"
    莉莉丝 "「……嗯。好，决定了！」"
    "哈，终于好了吗……双脚早就开始发麻了，能从这种百无聊赖的痛苦中解脱出来，真是太好了。"
    "正当我这么想时……"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI02D")]=True
    show expression "img/EVN_RI02D@2x.jpg" as bg1 with dissolve
    voice "NRI05A_RI009"
    莉莉丝 "「呐，志雄，你说选哪件啊？」"
    志雄 "「诶？我吗？」"
    志雄 "「是……要说选哪件的话……」"
    window hide
#BG_UVC 0,0,512,640,448
#BG_ALPC 0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCA03"),"True","img/RI_LCA03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    hide bg1 with dissolve
    voice "NRI05A_RI010"
    莉莉丝 "「啊！」"
    志雄 "「……？」"
#MESEX_A M_NOA,A_CH_SI,"【志雄】「……？」%K%P"
    voice "NRI05A_RI011"
    莉莉丝 "「这件的尺寸似乎小了点！我去问下还有没有大号的！」"
    window hide
    play sound "SE01_03L"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    pause (32/32.0)
    stop se
    "明明都这么大了，做事还是这么大大咧咧的……"
    play sound "SE01_04L"
    "在我无限感慨的功夫，莉莉丝沮丧着脸，走了回来。"
    window hide
    pause (64/32.0)
    stop se
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCC04"),"True","img/RI_LCC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI012"
    莉莉丝 "「唉～这里只剩下挂在店头的那件了……」"
    志雄 "「那没办法了。选另外一件吧」"
    voice "NRI05A_RI013"
    莉莉丝 "「诶？可是，那样做决定总觉得有点消极呢，好像不是我自己选的一样。」"
    志雄 "「刚才让我决定的是谁啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCA04"),"True","img/RI_LCA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI014"
    莉莉丝 "「志雄怎么想？」"
    志雄 "「我……觉得……这件就行了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCA05"),"True","img/RI_LCA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI015"
    莉莉丝 "「真的？不要敷衍我哟？」"
    志雄 "「真的啦。那件尺寸小的我觉得有些太露骨了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCC04"),"True","img/RI_LCC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI016B"
    莉莉丝 "「是吗……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCB01"),"True","img/RI_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI017"
    莉莉丝 "「那就这件吧！服务员！」"
    window hide
    play sound "SE01_03L"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    pause (32/32.0)
    stop se
    志雄 "「唉……」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG05AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG05AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCA01"),"True","img/RI_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE05_15L"
#FADE_IN 1
    志雄 "「还需要什么吗？」"
    stop sound
    voice "NRI05A_RI018"
    莉莉丝 "「我想想……再多备几件夏装吧。」"
    志雄 "「这种东西，家里的不是应该足够了吗？和我不同，身为女孩子，你已经有很多了吧。」"
    "因为夏天容易出汗，多带几件换洗的衣服也是可以理解的。可是也没必要特地去买新的吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCA06"),"True","img/RI_LCA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI019"
    莉莉丝 "「真是的。女孩子和你们男生不同啦，很多事情都不是你们那种脑子能考虑到的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCC06"),"True","img/RI_LCC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI020"
    莉莉丝 "「还有……啊，那个一定要另外买……」"
    志雄 "「什么啊，反正要买就一起买了带回去吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCD02"),"True","img/RI_LCD02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI021"
    莉莉丝 "「志雄你个笨蛋……」"
    window hide
    play sound "SE04_05"
    with vpunch
#VIB_DOKA 
#QUA2_BG 
#VIB_STP 5
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA05"),"True","img/RI_MCA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「哈！？你干什么！」"
    voice "NRI05A_RI022"
    莉莉丝 "「哼！都是志雄不好！」"
    志雄 "「真是莫名其妙……」"
    voice "NRI05A_RI023"
    莉莉丝 "「女孩子是有很多秘密的。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE01_04L"
    志雄 "「好了好了，我知道了……」"
    "经过这么多年的历练，我早就放弃理会她的强词夺理了。"
    "我轻轻叹了口气，跟着莉莉丝走去。"
    stop se
    stop music fadeout 1
    "就在这时……"
    voice "NRI05A_TO000"
    亨？ "「啊，莉莉丝！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCB01"),"True","img/RI_MCB01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    voice "NRI05A_TO001"
    亨 "「……还有，志雄。」"
    play music  "BGM09"
    志雄 "「不要把我说得像是充话费送的好么。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB05"),"True","img/TO_MBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_TO002"
    亨 "「是呢。冷静地想一想，你也不适合作为附赠品。」"
    "……冷静地想一想，我是不是该把这家伙揍一顿。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_TO003"
    亨 "「说起来，之前我看到你们就觉得，你们现在的关系真是好呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCB03"),"True","img/RI_MCB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI024"
    莉莉丝 "「哎！？看到我们，在哪里！？」"
    voice "NRI05A_TO004"
    亨 "「那个……」"
    window hide
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 2
#BG_PRI 2
#BG_ALPC 2
    show expression "img/NIMG13A@2x.jpg" as bg2 zorder 200 with dissolve
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2,(320+160)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA01"),"True","img/TO_XBA01A@2x.png") as lh2 zorder (1000-2):
        ypos 0.0
        xcenter .75
    with dissolve
#FADE_OUT 1,8,COL_WHITE
#CHR_ERSWC 0,1
#BG_ALPC 0
#BG_ALPC 2
#CHR_ALPC 2
#FADE_IN 1
    play music  "BGM13"
    voice "NRI05A_TO005"
    亨 "「哪件泳衣好呢？志雄～？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,(320+160)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBB02"),"True","img/TO_XBB02A@2x.png") as lh2 zorder (1000-1):
        ypos 0.0
        xcenter .75
    with dissolve
#MOV_CHR_INIT 20
#MOV_CHR2 0,(320-160)
#MOV_CHR1 128,(320-160)
#MOV_CHR_GO 1
    hide lh2 with dissolve
    voice "NRI05A_TO006"
    亨 "「你真傻……哪件都适合你啦。可是，其实……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBB01"),"True","img/TO_XBB01A@2x.png") as lh2 zorder (1000+1):
        ypos 0.0
    with dissolve
    voice "NRI05A_TO007"
    亨 "「就如刚出生时的你那最纯洁的样子才是最棒的！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2,(320-160)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA05"),"True","img/TO_XBA05A@2x.png") as lh2 zorder (1000-2):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 20
#MOV_CHR1 0,(320+160)
#MOV_CHR2 128,(320+160)
#MOV_CHR_GO 1
    hide lh1 with dissolve
    voice "NRI05A_TO008"
    亨 "「志雄！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_ALPC 0
#CHR_ALPC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    hide bg2
    hide lh2
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC04"),"True","img/RI_MCC04A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
    with dissolve
    stop music fadeout 132
#FADE_OUT 1,8,COL_WHITE
#BG_ALPC 0
#CHR_ALPC 0
#CHR_ALPC 1
#FADE_IN 1
    voice "NRI05A_TO009"
    亨 "「于是两人就这样结成了一对。可喜可贺啊。」"
    play music  "BGM09"
    志雄 "「你真的不要紧吗，我能为你做些什么吗？」"
    voice "NRI05A_RI025"
    莉莉丝 "「赶紧去一次眼科，耳鼻科，还有脑外科也许比较好哦？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA04"),"True","img/TO_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_TO010"
    亨 "「诶诶！烦死了烦死了烦死——了！」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA02"),"True","img/TO_XBA02A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NRI05A_TO011"
    亨 "「什么嘛！想炫耀吗？　想对这个１８年没有女朋友的我炫耀吗！？」"
    voice "NRI05A_TO012B"
    亨 "「若无其事地展现出这种用眼神交流的甜蜜场景！　真可恶！　志雄你这家伙太可恶了！」"
    "稍稍回想了一下，我们有做过这种事吗……"
    "和往常一样无理取闹般的展开，然后和往常一样的收尾，仅此而已……"
    voice "NRI05A_TO013"
    亨 "「还有那自然得无懈可击的感情交流！」"
    "那扫堂腿要是也能称为感情交流的话……还是饶了我吧。"
    志雄 "「你在这里干吗呢？　不是为了跟踪我们吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBB05"),"True","img/TO_XBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_TO014"
    亨 "「暑期补习回来而已。真是的，好不容易到了暑假，竟然要补习。」"
    "亨无力地垂下肩膀。"
    "不过，说意外还真意外。这家伙竟然会认真去补习。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA01"),"True","img/TO_XBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_TO015B"
    亨 "「什么时候走？　去海边？　游泳馆？　也叫上箱崎吧！」"
    志雄 "「啊啊，这个啊。不好意思，其实……」"
    "因为是家族旅行，这趟是不可能带上亨他们一起了。"
    "正当我想说明情况的时候……"
    window hide
#CHR_PRIC 0
#CHR_PRIC 1
#BG_LAY 3,RI_MXC03,3,((320+192)-(320))
#CHR_SET_BACK
#ROUTINE_STA
#CHR_INIC 2
#CHR_PRIC 2
#CHR_ALPC 2
#CHR_POSC 2,(320+192)
#ROUTINE_STP
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC03"),"True","img/RI_MCC03A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
        xcenter .8
    with dissolve
#CHR_ALP_AUTOC 2,128,1,F24
#REEK_CHR 2
    voice "NRI05A_RI026"
    莉莉丝 "「啊——！」"
#REMOVE_REEK_CHR 2
    hide bg3 with dissolve
#BG_PRI 3
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBB04"),"True","img/TO_XBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_TO016"
    亨 "「哇！？」"
    志雄 "「噢噢！？」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_PRIC ID_ALL
#CHR_SORT 0,1,2
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC03"),"True","img/RI_MCC03A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    志雄 "「怎么了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC06"),"True","img/RI_MCC06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI027"
    莉莉丝 "「诶！？　啊，不。那个，就是，看……有，有一只小虫子在飞！」"
    志雄 "「虫子？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC03"),"True","img/RI_MCC03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#REEK_CHR 1
    voice "NRI05A_RI028"
    莉莉丝 "「那可是只不得了的虫子！　有密密麻麻的大概有十只脚，眼睛大概有二十个……」"
#REMOVE_REEK_CHR 1
    "哎，那已经不能称为虫子了吧。"
    voice "NRI05A_RI029"
    莉莉丝 "「真的很厉害啊！　令人毛骨悚然的哦！」"
    "嗯？　总觉得她有点想瞒混过关的样子，算了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA01"),"True","img/RI_MCA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI030"
    莉莉丝 "「总之没什么特别的啦。去玩的时候会叫上你们的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_TO017"
    亨 "「噢噢！　真不愧是我的女神莉莉丝！　别的女孩子也拜托你们了！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCD01"),"True","img/RI_MCD01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI031"
    莉莉丝 "「好啦好啦。那我们先走了。还要去买些东西。」"
    voice "NRI05A_TO018"
    亨 "「噢噢。再见～♪」"
    window hide
    stop music fadeout 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    hide bg1 with dissolve
    "莉莉丝丢下情绪高涨的亨，拉着我的衣襟快步往前走。"
    志雄 "「啊，喂，莉莉丝？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCD05"),"True","img/RI_LCD05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI032"
    莉莉丝 "「真是的……为什么这么轻易地就想说出去啊……」"
    志雄 "「诶？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCD02"),"True","img/RI_LCD02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI033"
    莉莉丝 "「没什么……」"
    "怎么了，莉莉丝这家伙，尽说些我听不懂的话……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCD05"),"True","img/RI_LCD05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI034"
    莉莉丝 "「……你完全不在意吗？」"
    window hide
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
#FADE_IN 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,((320-192)-80)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_SBA01"),"True","img/CH_SBA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter (48/640.0)
        linear 1 xcenter .2
    with dissolve
    play sound "SE00_34"
#MOV_CHR_INIT 40
#MOV_CHR0 128,(320-192)
#MOV_CHR_GO 1
    voice "NRI05A_RI035"
    莉莉丝 "「啊，智纱。」"
    "竟然在书店的门口发现了箱崎的身影。箱崎也注意到我们，向这边走来。"
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
#CHR_PRIC 0
#CHR_PRIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA01"),"True","img/CH_MBA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA01"),"True","img/RI_MCA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    play music  "BGM10"
    voice "NRI05A_CH000"
    智纱 "「莉莉丝。还有塚本君。」"
    voice "NRI05A_RI036"
    莉莉丝 "「智纱，你在这里干吗？」"
    voice "NRI05A_CH001"
    智纱 "「嗯，我来买参考书。」"
    志雄 "「对了……我待会也要挑几本。莉莉丝，你也挑一些把，不要总是一副事不关己的样子哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC06"),"True","img/RI_MCC06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI037"
    莉莉丝 "「呃……」"
    "莉莉丝听了我的话明显有些不知所措。"
    "也难怪，对考试复习没什么进展的莉莉丝来说，我说的确实不是什么令人高兴的话。"
    voice "NRI05A_CH002"
    智纱 "「两人在约会吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC04"),"True","img/RI_MCC04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI038"
    莉莉丝 "「啊，那个～」"
    志雄 "「是在为旅行做准备。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA03"),"True","img/RI_MCA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI039"
    莉莉丝 "「志，志雄！？」"
    志雄 "「……？　怎么了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCD02"),"True","img/RI_MCD02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI040"
    莉莉丝 "「为什么说出来了啦！？」"
    志雄 "「那个，你也不用这么生气啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA06"),"True","img/RI_MCA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI041"
    莉莉丝 "「哈……」"
    "莉莉丝像是有什么要说似地叹了口气。"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA03"),"True","img/CH_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    voice "NRI05A_CH003"
    智纱 "「诶？　……难道说……只有你们两个人去旅行吗！？」"
#THREAD_STP 1
#REMOVE_REEK_CHR 0
#CHR_SORT 1
#CHR_PRIC ID_ALL
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA03"),"True","img/RI_MCA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI042"
    莉莉丝 "「不、不是啦！　不只有两个人！　婆婆也一起去！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBC06"),"True","img/CH_MBC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI05A_CH004"
    智纱 "「什，什么嘛……吓了我一跳……」"
    window hide
    stop music fadeout 1
#CHR_SORT 2,0
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA02"),"True","img/TO_XBA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 16
#MOV_CHR0 0
#MOV_CHR1 0
#MOV_CHR2 128
#MOV_FOCUS_BG 512
#MOV_CHR_GO 0
    voice "NRI05A_TO019"
    亨 "「你果然是我的敌人！　恋人之间的旅行！？　什么啊，这梦幻般的情景！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBB05"),"True","img/TO_XBB05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI05A_TO020"
    亨 "「在目的地发生了一些突发事件，然后两人的关系就有了巨大的进展……唉！？　两人在夜晚借着远离本地的开放感就含情脉脉地……」"
    play music  "BGM09"
    志雄 "「谁会这样啊！　再说了，你是从什么地方冒出来的啊。不是才刚分开吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA02"),"True","img/TO_XBA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI05A_TO021"
    亨 "「我也是来看参考书的！　绝不是来探究你们两人是否会就这样远走高飞的！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA03"),"True","img/TO_XBA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI05A_TO022"
    亨 "「因为即使我这么做，最后感到寂寞的也只会是我自己！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA04"),"True","img/TO_XBA04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI05A_TO023"
    亨 "「呵……再说，男人无论是，谁最初都会这么说。『没关系，我什么都不会做的！』」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA03"),"True","img/TO_XBA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI05A_TO024"
    亨 "「可到头来……哼……」"
    "究竟是什么和什么啊。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_ALPC 0
#CHR_ALPC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBC06"),"True","img/CH_MBC06A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA07"),"True","img/RI_MCA07A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
    with dissolve
#ROUTINE_STA
#CHR_ALP_AUTOC 1,128,1,F24
#CHR_ALP_AUTOC 2,0,1,F24
#CHR_ALP_AUTOC 0,128,1,F24
#ROUTINE_STP
    hide lh2 with dissolve
    voice "NRI05A_CH005"
    智纱 "「哇哇……」"
    "箱崎满脸通红。"
    voice "NRI05A_RI043"
    莉莉丝 "「所以我不是说了吗，不是只有两个人，不会演变成这样的啦！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCD02"),"True","img/RI_MCD02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI044"
    莉莉丝 "「真是！　都怪志雄这么口无遮拦地说出去才会这样的！　你要负责！　负责！」"
    "啊啊……所以莉莉丝才这么生气吗……"
    window hide
#CHR_SORT 1,0
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2,0
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
    with dissolve
#CHR_ALP_AUTOC 2,128,0,F24
#CHR_POS_AUTOC 2,F24,40
    pause (20/32.0)
#CHR_POS_AUTOC 0,(320-192),F25,20
#CHR_POS_AUTOC 1,(320+192),F25,20
#CHR_ALP_SAVEC 2
#CHR_POS_SAVEC 2
#CHR_POS_SAVEC 0
#CHR_POS_SAVEC 1
    voice "NRI05A_TO025"
    亨 "「包包包包在我身上！　我会对莉莉丝负起责任的！」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBC01"),"True","img/CH_MBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR0 ,(320-96)
#MOV_CHR_GO 1
    voice "NRI05A_CH006"
    智纱 "「不行。这是塚本君的事。呐？」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA01"),"True","img/RI_MCA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR1 ,(320+96)
#MOV_CHR_GO 1
    voice "NRI05A_RI045"
    莉莉丝 "「呐？」"
#ROUTINE_STA
    hide lh0 with dissolve
    hide lh1 with dissolve
#CHR_ALPC 2
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB05"),"True","img/TO_MBB05A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
    with dissolve
#ROUTINE_STP
#CHR_BLUR 2
#CHR_POS_AUTOC 0,(320-160),F25,20
#CHR_POS_AUTOC 1,(320+160),F25,20
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LBC01"),"True","img/CH_LBC01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCA01"),"True","img/RI_LCA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    志雄 "「唔……」"
    "不行了，两个女生联合起来的话，我不觉得自己仍能游刃有余的应付了。"
    "总之，先想办法让她心情好转吧……"
#label QJUMP
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG50AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG50AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    play music  "OBGM18"
    "于是，我们四人来到了卡拉ＯＫ。"
    "自从去年学园祭那件事之后，我就经常和莉莉丝他们一起去卡拉ＯＫ唱歌。"
    "很多次我们之间有小摩擦的时候，也是来这里和好的。"
    "至于还要买的东西，之后还有的是时间。"
    "反正亨本来也没打算去学习，箱崎偶尔放松下心情也不错吧。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_COLC 0,96,96,96
#CHR_COLC 1,96,96,96
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
#CHR_COLC 0,128,136,136
#CHR_COLC 1,128,136,136
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh10 zorder (10+10):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC04"),"True","img/RI_MCC04A@2x.png") as lh11 zorder (10+1):
        xcenter .75
    voice "NRI05A_RI046"
    莉莉丝 "「大概就是因为一直来这里，我的成绩才会上不去的……」"
    voice "NRI05A_TO026"
    亨 "「没事，偶尔放松下是有必要的！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI05A_TO027"
    亨 "「在这里尽情地唱一番，把暑期补习的不满一下子发泄出来吧！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA01"),"True","img/RI_MCA01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    志雄 "「是啊，放松的时间也是很重要的。」"
    "话说回来，他们两个明明一直以来都处于放松的状态吧……"
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
#CHR_COLC 0,96,96,96
#CHR_COLC 0,128,136,136
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBB06"),"True","img/CH_MBB06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI05A_CH007"
    智纱 "「啊哈哈……」"
    "被一起带过来的箱崎，脸上则浮出了无奈的笑容。"
    window hide
    stop music fadeout 1
    hide lh0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,136,136
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCA01"),"True","img/RI_LCA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI047"
    莉莉丝 "「那么，就由我来打头阵吧！」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE09_24"
    "莉莉丝的歌还是唱得这么好……"
    "看着她唱得如此欢乐，我也不知不觉高兴了起来。"
    "除开让她尽兴的目的，老实说，我也挺想听她唱歌的。"
    "一边的箱崎也鼓掌配合着莉莉丝唱歌的节奏。"
    window hide
#CHR_INIC 0
#CHR_COLC 0,128,136,136
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA01"),"True","img/TO_XBA01A@2x.png") as lh10 zorder 100:
        ypos 0.0
    with dissolve
    voice "NRI05A_TO028"
    亨 "「……喂。」"
    志雄 "「嗯？」"
    voice "NRI05A_TO029"
    亨 "「关于你和莉莉丝的旅行。」"
    志雄 "「话说在前头，你所意淫的片段是不会发生的。」"
    voice "NRI05A_TO030"
    亨 "「我知道啦。我也不是真的认为你们能有什么大的进展……不过，一定会有一些小的变化哟。」"
    志雄 "「小的变化？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBB03"),"True","img/TO_XBB03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI05A_TO031"
    亨 "「啊啊。再说，你和莉莉丝已经交往了半年以上了吧。可是，在旁人看来，你们的关系却似乎没什么变化……停滞期？」"
    志雄 "「唔……没、没这回事……」"
    voice "NRI05A_TO032"
    亨 "「像这种情侣我也见得多了、这种类型大多会……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA05"),"True","img/TO_XBA05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI05A_TO033"
    亨 "「自然消亡！」"
    志雄 "「真的吗……？」"
    voice "NRI05A_TO034"
    亨 "「真的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA01"),"True","img/TO_XBA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI05A_TO035"
    亨 "「所以，这不是一个很好的机会吗？　处在不同的环境下的话，人也会变得稍微大胆些的～」"
    志雄 "「嗯……」"
    "虽然亨说的也有些道理……但有必要做到这种程度吗。"
    window hide
#BG_BLUR 0
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我把视线投向紧握麦克正在高歌的莉莉丝。"
    "现在我和莉莉丝的关系——这样不也很好嘛。又没有什么烦恼。"
    stop sound fadeout 1
    "就在我胡思乱想的时候，莉莉丝的歌已经唱完了。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
#CHR_COLC 0,96,96,96
#CHR_COLC 1,96,96,96
#CHR_COLC 0,128,136,136
#CHR_COLC 1,128,136,136
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh10 zorder (10+10):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA01"),"True","img/RI_MCA01A@2x.png") as lh11 zorder (10+1):
        xcenter .75
    play music  "OBGM18"
    voice "NRI05A_TO036"
    亨 "「那么，下面该轮到我了。莉莉丝，女声的部分就拜托你了。」"
    voice "NRI05A_RI049"
    莉莉丝 "「OK～♪」"
    "拿着桌上放的另一个麦克，亨站了起来。"
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
#CHR_COLC 0,128,136,136
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_XBA01"),"True","img/CH_XBA01A@2x.png") as lh10 zorder 100:
        ypos 0.0
    with dissolve
    voice "NRI05A_CH008"
    智纱 "「呐，塚本君。」"
    志雄 "「嗯？」"
    "伴随着亨点选的对唱的前奏曲响起，这次是箱崎小声的向我搭话道。"
    voice "NRI05A_CH009"
    智纱 "「马上就要到莉莉丝的生日了，你有什么打算吗？」"
    志雄 "「打算？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_XBB01"),"True","img/CH_XBB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI05A_CH010"
    智纱 "「那个，生日两个人一起过之类的，像这种计划有没有想过。难道说，旅行就是为了庆祝她的生日吗？」"
    志雄 "「不、不是的！　那只是单纯的家族旅行啦……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_XBB02"),"True","img/CH_XBB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI05A_CH011"
    智纱 "「是吗，太好了。」"
    "箱崎似乎有些放下心来，小声叹了口气。"
    志雄 "「……？　怎么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_XBA01"),"True","img/CH_XBA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI05A_CH012"
    智纱 "「莉莉丝的生日，我想大家一起庆祝的。」"
    voice "NRI05A_CH013"
    智纱 "「不过，如果塚本君打算和莉莉丝单独庆祝的话，我们去打扰就不好啦。」"
    志雄 "「没事啦，我想她一定会很乐意看到你们来的。」"
    "像生日派对之类的活动……难得的生日，大家一起庆祝一定会更热闹吧。"
    "对了。我得想想要送什么礼物才好。"
    window hide
#BG_BLUR 0
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
#CHR_COLC 0,128,136,136
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCA01"),"True","img/RI_LCA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI050"
    莉莉丝 "「志雄，给，麦克。」"
    志雄 "「哎？　我吗？」"
    志雄 "「我什么歌都没点啊……」"
    voice "NRI05A_RI051"
    莉莉丝 "「我知道。所以我帮你点了。这次和我一起唱吧。」"
    志雄 "「哎？　等一下。我没听过这首歌啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCC02"),"True","img/RI_LCC02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI05A_RI052"
    莉莉丝 "「好了好了。来，站起来，拿好麦克～」"
    "莉莉丝拉着我的手臂，硬是把我拽起来。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG15NA1@2x.jpg" as bg0 zorder 0 with dissolve
#FADE_IN 0
    "结果那之后和莉莉丝一起唱了一首我完全不了解的歌。"
    "我完全不知道怎么唱，唱得个四不像，不过莉莉丝却很高兴似的，这也就够了吧……"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128
#FADE_IN 1
    play music  "OBGM17"
    play sound "SE03_86"
    "看着自己房间里的日历，拿起笔，在旅行之后的某一天上标了记号。"
    "８月１０日，莉莉丝的生日。"
    志雄 "「礼物选什么好呢……」"
    "距离莉莉丝的生日还有两周。"
    "不过，我也买不起什么昂贵的东西……而且，莉莉丝想要什么呢？　能让她高兴地东西是什么呢？"
    "每年这个时候都会烦恼……"
    voice "NRI05A_X9000_K"
    ラジオ "「今天最佳的建议是昵称为『有了男朋友』的女孩给我们带来的……」"
    window hide
#FADE_OUT 1
    pause (32/32.0)
#FADE_IN 1
    voice "NRI05A_XA000_K"
    ラジオ "「……今天正是他的生日。所以我就果断地用『生日礼物就是，我·自·己～』来……」"
    志雄 "「把自己作为礼物……」"
    "把自己用带子卷起来……"
    "……白痴吗。"
    "有点惊悚的感觉……我马上对自己无节制想象感到后悔了起来。"
    志雄 "「总之……」"
    "还有一些时间。不需要着急，到时候会想到的吧。"
    "比起礼物，现在更应该先考虑旅行的事。"
    志雄 "「旅行的时候装作若无其事地问问她好了。」"
    "没错。在旅行的时候知道她喜欢和想要的东西就行了。"
    "虽说富美子婆婆也在，不过两人独处的机会还是有的吧。"
    "一定会知道的。"
    志雄 "「嗯。」"
    "我一个人深深地点了点头。"
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
#label THREAD_QUA_CHR0_WIN
#QUA_CHR 0
#TH_QUAKE_WIN
#EOT
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT