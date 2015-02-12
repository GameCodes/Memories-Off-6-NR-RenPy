label NSU04A:
    $currentlabel = "NSU04A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    play music "OBGM17"
#label START
    $month = '07'
    $day = '21'
    $date = '5'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/EXBG09A@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/EXBG09A@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBC02"),"True","img/RI_ZBC02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
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
    voice "NSU04A_RI000"
    莉莉丝 "「嗯。果然是上好的肉，就不应该用那种不高明的小花招来料理才对」"
    志雄 "「这可真是谢谢您捧场了啊」"
    "莉莉丝把剩下的高级黑猪肉干净利索地消灭掉，小口抿着饭后的麦茶。 "
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD03"),"True","img/RI_ZBD03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI001"
    莉莉丝 "「怎么了，看起来心情不好啊」"
    志雄 "「这种情况下，请告诉我心情会好的理由」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD06"),"True","img/RI_ZBD06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI002"
    莉莉丝 "「哈哈哈哈——是我打扰了你们两人？」"
    志雄 "「你不是很明白么」"
    voice "NSU04A_RI003"
    莉莉丝 "「我可没说哦。这么说，你们刚才度过了属于恋人的甜蜜时光咯？」"
    志雄 "「还、还没到那一步……嘛，的确是向着那个方向努力呢」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA01"),"True","img/RI_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI004"
    莉莉丝 "「然后呢？到底在谈些什么啊」"
    "莉莉丝像是不相信我的话似的，托着腮听着。"
    志雄 "「嗯……在商量今后的出路」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA06"),"True","img/RI_ZBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI005"
    莉莉丝 "「呼～」"
    "我刚一回答，莉莉丝便失望地叹了口气。"
    志雄 "「怎么啦」"
    voice "NSU04A_RI006"
    莉莉丝 "「光靠关于前途的那种谈话，想成为恋人关系是不够的吧？」"
    志雄 "「但是，的确是想和铃谈谈关于两人的未来」"
    "虽然试图抵抗，但说出来的话却很无力。"
    voice "NSU04A_RI007"
    莉莉丝 "「也只是想而已啊。这个，也就是你所认为的情侣间的对话吗？」"
    志雄 "「……不，当然不是」"
    "本来，在关于未来的打算这件事上，我们在年龄上和经历上的差距就完全体现出来了。"
    "若不是听了我那种过于严肃的话，气氛也不会变成这样。"
    "或者，不如说这对话让我强烈地感觉到大人和孩子之间的那种差距。"
    stop music
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA04"),"True","img/RI_ZBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI008"
    莉莉丝 "「……我想问你些根本上的问题。志雄和铃，有正式地在交往吗？」"
    "对于意志消沉的我，莉莉丝一语击中了痛处。"
    志雄 "「嗯，这个是当然……或许是……怎么说呢……」"
    voice "NSU04A_RI009"
    莉莉丝 "「嗯」"
    window hide
    play music "OBGM14"
    志雄 "「这个……我自己也不是很清楚」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA06"),"True","img/RI_ZBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "莉莉丝托着腮，不住地挠头。"
    voice "NSU04A_RI010"
    莉莉丝 "「明明怀着那样的感情，为什么情况却变成这个样子了呢？」 "
    志雄 "「就算你问为什么，我也不是很清楚」"
    "到底是为什么呢。"
    if not persistent.dictlist[46] and persistent.show_dict:
        $persistent.dictlist[46]=True
        show screen dict_pop(i=46)
    "铃既然回到了我的公寓，我们的关系，一定会发生什么改变。"
    "我是这样认为的没错……"
    "结果呢，只是回到了以前的关系而已。什么也没有改变。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA05"),"True","img/RI_ZBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI011"
    莉莉丝 "「这样么，真可怜呢」"
    志雄 "「是因为我的关系吗？果然是这样吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA06"),"True","img/RI_ZBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI012"
    莉莉丝 "「似乎是呢。明明是要进行一场精心的告白，却变成了现在悠闲自得的交谈」"
    志雄 "「看上去是这样吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD04"),"True","img/RI_ZBD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI013"
    莉莉丝 "「就是这样呢。或许，志雄是满足于目前这种铃陪伴在身旁的状态？」"
    志雄 "「……唔」"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG33AA@2x.jpg" as bg2 zorder 20 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,(320)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LDC01"),"True","img/SU_LDC01A@2x.png") as lh1 zorder (100-1):
        ypos 0.0
    with dissolve
#MUS_VOL 64,16
#BG_INIC 1
#BG_PRI 1
    show expression "img/BG33AA@2x.jpg" as bg0 with dissolve
#BG_ALPC 0
#BG_ALPC 2,128
#CHR_ALPC 0
#CHR_ALPC 1,128
#BG_BLUR 2
    "或许是这样吧……"
    "当然是想认真地和铃交往，但维持目前的这种关系也不错。"
    "早上起床，已经为我准备好了早饭，看到铃的笑脸。"
    "只需喊一下马上就可以到身旁 ……"
    window hide
#BG_INIC 1
#BG_PRI 1
    show expression Solid("fff") as bg1 with ImageDissolve("img/BG_MASK15@2x.png",1)
    hide lh1
    hide bg2
#BG_UVC 2,0,0,640,448
    show expression "img/EXBG09A@2x.jpg" as bg0
#BG_ALPC 0,128
#CHR_ALPC 0,128
#MUS_VOL 128,64
    hide bg1
    with dissolve
    voice "NSU04A_RI014"
    莉莉丝 "「难道说，现在开始退缩了吗？」"
    志雄 "「没有的事……大概吧」"
    "不，也许真的是这样？"
    "奇怪地陷了进来，但不知道铃又会消失到哪里去，我在害怕这一点吗？"
    志雄 "「我看起来是这样的吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD03"),"True","img/RI_ZBD03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI015"
    莉莉丝 "「唔，有点呢」"
    志雄 "「这样啊……外人看起来是这样子的话……唔……」"
    stop music
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA01"),"True","img/RI_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI016"
    莉莉丝 "「可是，或许还有救」"
    志雄 "「怎么个救法？」"
    voice "NSU04A_RI017"
    莉莉丝 "「一起准备料理的志雄和铃，和之前比起来感觉好很多呢」"
    window hide
    play music "OBGM29"
    志雄 "「诶，真的！？」"
    play sound "SE03_92"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBB03"),"True","img/RI_ZBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI018"
    莉莉丝 "「总之，不由得有这种感觉」"
    "我激动地一再追问。莉莉丝不禁把身子向后仰回答我。"
    志雄 "「那我接下来该怎么做呢？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD04"),"True","img/RI_ZBD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI019"
    莉莉丝 "「这种问题为什么要问我」"
    "你也不用发出这种很不情愿的声音吧……"
    志雄 "「因为没有其他值得信赖的人啊。拜托了，莉莉丝」"
    "亨的话虽然听过，但却从没想过那家伙的建议能对我有帮助。"
    if not persistent.dictlist[8] and persistent.show_dict:
        $persistent.dictlist[8]=True
        show screen dict_pop(i=8)
    "其他可以商量的只有稻穗先生了，但关于铃的事的话……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD03"),"True","img/RI_ZBD03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI020"
    莉莉丝 "「但你就算是期待着我也没辙啊」"
    志雄 "「总要想点办法吧！你是铃代老师的粉丝吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD05"),"True","img/RI_ZBD05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI021"
    莉莉丝 "「所以，为什么是我……」"
    "我就这样双手合十，低头恳求着。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA06"),"True","img/RI_ZBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI022"
    莉莉丝 "「咳……算了，我反正也正无聊，与其看志雄做些奇怪的事使铃走掉，还不如给你些建议」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA01"),"True","img/RI_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI023"
    莉莉丝 "「不过，或许给不了什么好建议哟？」"
    志雄 "「没问题。比起我一个人独自烦恼，这已经是相当有帮助了」"
    "虽然莉莉丝一副勉勉强强接受的样子，但不知为什么，感觉到她已经和我站到了同一战线。"
    "难能可贵的青梅竹马。"
    志雄 "「莉莉丝你觉得到底是哪里还不行呢？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBC01"),"True","img/RI_ZBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI024"
    莉莉丝 "「唔～，志雄和铃约会过吧？」"
    志雄 "「约会？只是偶尔让她骑车带我回来，一起去吃个饭而已」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBC04"),"True","img/RI_ZBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI025"
    莉莉丝 "「唔，不是指这些。就是普通的约会」"
    志雄 "「普通的约会么。有什么不一样吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD01"),"True","img/RI_ZBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI026"
    莉莉丝 "「光是玩可不行哦。以恋人之间的约会这种形式来说，气氛不正是最重要的嘛」"
    志雄 "「和我们这种有什么不同吗？」"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG15MA@2x.jpg" as bg2 zorder 20 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,(320)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LEB02"),"True","img/SU_LEB02A@2x.png") as lh1 zorder (100-1):
        ypos 0.0
    with dissolve
#MUS_VOL 64,16
#BG_INIC 1
#BG_PRI 1
    #show expression "img/BG_WHITE@2x.jpg" as bg1 with dissolve
    #scene expression "img/BG15MA@2x.jpg" as bg0 with dissolve
#BG_ALPC 0
#BG_ALPC 2,128
#CHR_ALPC 0
#CHR_ALPC 1,128
#BG_BLUR 2
    hide bg1 with dissolve
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA04"),"True","img/RI_ZBA04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    "我不由得想起了和铃两人相处的时候。"
    "基本上，铃也是满脸灿烂的啊。"
    "但是，老实说的话……"
    window hide
#BG_INIC 1
#BG_PRI 1
    show expression Solid("fff") as bg1 with ImageDissolve("img/BG_MASK15@2x.png",1)
    hide lh1 with dissolve
    hide bg2 with dissolve
#BG_UVC 2,0,0,640,448
    show expression "img/EXBG09A@2x.jpg" as bg0 with dissolve
#BG_ALPC 0,128
#CHR_ALPC 0,128
#MUS_VOL 128,64
    hide bg1 with dissolve
    voice "NSU04A_RI027"
    莉莉丝 "「怎么说呢，是好朋友相处的那种感觉吗？」"
    "莉莉丝不急不缓地选择着措辞。"
    "的确是这样。和铃在一起的时候，像是朋友相处的那种感觉。"
    "而且，是和男性朋友差不多的感觉吧。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA01"),"True","img/RI_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI028"
    莉莉丝 "「所以，不妨再认真地约会看看，我想铃的意识或许是会改变的呢」"
    志雄 "「形式有那么重要吗」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD01"),"True","img/RI_ZBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI029"
    莉莉丝 "「这样的话，我想铃总会以男友的眼光来看待志雄的」"
    "莉莉丝抱着胳膊连连点头。"
    "老实说，我没有想到从莉莉丝这里能得到这么好的建议。"
    志雄 "「就是说，我这边必须得做点什么吧」"
    voice "NSU04A_RI030"
    莉莉丝 "「没错。好好回想一下追求铃的时候的那份感情吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD02"),"True","img/RI_ZBD02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI031"
    莉莉丝 "「和智纱在一起也有那么多那么多的回忆，都铭记于心吧，在心里！」"
    志雄 "「哦，哦」"
    "是呢啊。"
    "一定要让铃看到我的决心，一次也好。如果我变得更加主动的话，应该可以的。"
    "就这么定了！"
    志雄 "「那么，现在就去约铃吧！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD01"),"True","img/RI_ZBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI032"
    莉莉丝 "「正好，邀请她去明天的焰火大会吧？」"
    志雄 "「啊，明天吗」"
    "完全忘记了，明天是芦鹿岛的焰火大会呢。两个人一起欣赏焰火的话，确实有恋人般的感觉呢。"
    志雄 "「嗯。真是绝妙的主意啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA05"),"True","img/RI_ZBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI033"
    莉莉丝 "「也不能完全这么说！不如说是志雄你们的情况，正好适合这种比较简单易懂的方式」"
    志雄 "「这样么。不管怎样都要谢谢你」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBB01"),"True","img/RI_ZBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI034"
    莉莉丝 "「嗯，千万不要搞得一团糟啊」"
    志雄 "「哦。那么，现在……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    with dissolve
#SE_PLYC 0,SE02_03
    pause (16/32.0)
    play sound "SE02_03"
    "说着我拿出了手机，开始写起邮件来。"
    window hide
#SE_PLYC 0,SE02_03
    pause (8/32.0)
#SE_PLYC 0,SE02_03
    pause (8/32.0)
    play sound "SE02_03"
    "铃工作忙的时候，不方便打电话，于是用邮件来联络。"
    play sound "SE02_03"
    "只是在真正忙的时候，邮件也会很晚回，大多数时候都是等着铃来联系我。"
    play sound "SE02_01"
    "啊，邮件竟然很快就得到回复了。"
    play sound "SE02_03"
    window hide
#SCRMODE_SPC SCR_FULL
    play sound "SE02_03"
#FILT_IN 48,0,COL_DARK2
#SET_SAVPNT
#MES "%S032%FS%t002Ｆｒｏｍ：铃%N%t002件名%t002：Ｒｅ：明天有空吗？%N%t007ＯＫ，等工作结束之后吧。%FE%K"
    "Ｆｒｏｍ：铃"
    "件名{w}：Ｒｅ：明天有空吗？"
    "ＯＫ，等工作结束之后吧。"
    play sound "SE02_03"
#MESX "%O032"
#CLR_SAVPNT
    window hide
#SCRMODE_SPC SCR_WINDOW
#FILT_OUT 48
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD04"),"True","img/RI_ZBD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「太好了！定在明天了！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA05"),"True","img/RI_ZBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI035"
    莉莉丝 "「真是的，到现在为止你都在干嘛呢」"
    志雄 "「没办法啊……我在这方面……真的是经验不足」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA01"),"True","img/RI_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU04A_RI036"
    莉莉丝 "「那在不占用老师的执笔时间的前提下，加油吧」"
    "接着，莉莉丝一副随便说说的样子耸耸肩，将剩下的麦茶一饮而尽。"
    志雄 "「好，明天一定要加油啊……」"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music
#FADE_OUT 1,128
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop se
    stop sound
    stop music
#FADE_IN 0
    $ renpy.end_replay()
    return