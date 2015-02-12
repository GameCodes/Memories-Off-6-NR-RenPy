label NRI10A:
    $currentlabel = "NRI10A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '28'
    $date = '5'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/BG60EA@2x.jpg" as bg1 zorder 1 with dissolve
    scene expression "img/BG60EA@2x.jpg" as bg0 with dissolve
    play sound "SE05_13L"
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
    "结果在回到旅馆之前，两人一直紧靠着。"
    "……总觉得已经筋疲力尽了。似乎不是行走，而是在别的地方耗费了很多精力。"
    window hide
    stop sound fadeout 1
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG61EA@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBA02"),"True","img/RI_XBA02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#BG_BLUR 0
    hide bg1 with dissolve
    志雄 "「进到旅馆之后，已经不冷了吧？」"
    voice "NRI10A_RI000"
    莉莉丝 "「啊、嗯，嗯。是呢……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA02"),"True","img/RI_MBA02A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#ROUTINE_STA
#CHR_ALP_AUTOC 0,0,1,F24
#CHR_ALP_AUTOC 1,128,1,F24
#ROUTINE_STP
    hide lh0 with dissolve
#BG_BLUR 0
    "莉莉丝突然和我分开，刚才为止手臂上还残留着的温暖瞬间消失了。"
    "虽然有些不舍，不过总不能在旅馆里还挽着手吧。"
    "而且不管怎么说，那个人也在……"
    window hide
#CHR_SET_BACK
#CHR_POS_AUTOC 1,(320+160),F24,48
#CHR_INIC 0
#CHR_POSC 0,(320-160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA02"),"True","img/SN_MBA02A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC04"),"True","img/RI_MBC04A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    play music  "OBGM25"
    voice "NRI10A_SN000"
    信 "「噢噢，两位回来啦！」"
    志雄 "「嗯，我们回来了」"
    "……好险好险。"
    "要是被他看到我和莉莉丝手挽着手的样子，不知道会被他说些什么。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA01"),"True","img/SN_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI10A_SN001"
    信 "「晚饭怎么办？在房间里吃还是在食堂吃？」"
    志雄 "「莉莉丝你说呢？我哪边都无所谓。」"
    voice "NRI10A_RI001"
    莉莉丝 "「那个……是呢……我也无所谓。」"
    voice "NRI10A_SN002"
    信 "「对于人手不足的我们来说，你们要是能在食堂吃，省去我们拿来拿去的时间就好了。」"
    志雄 "「那就在食堂吃吧，莉莉丝可以吧？」"
    "本来也没什么理由一定要在房间里吃。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA04"),"True","img/RI_MBA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI10A_RI002"
    莉莉丝 "「……嗯，是呢。食堂几点开饭？」"
    voice "NRI10A_SN003"
    信 "「现在去也行哦。晚餐时间直到８点，所以只要在那之前吃完就行了。」"
    志雄 "「那么，我们先在房间里休息一会儿再去吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA06"),"True","img/SN_MBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI10A_SN004"
    信 "「哦，我知道了。两位慢慢享受。」"
    window hide
    stop music fadeout 1
    hide lh0 with dissolve
    "……？"
    "什么啊？离开前，稻穗露出了诡异的微笑……"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBC05"),"True","img/RI_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI10A_RI003"
    莉莉丝 "「怎么了，志雄？」"
    志雄 "「啊……不，没什么。」"
    "不过也不是什么值得在意的事。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG63NA2@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG63NA2@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    play sound "SE00_47"
#FADE_IN 1
    stop music fadeout 1
    voice "NRI10A_RI004"
    莉莉丝・志雄 "「……诶？」"
    play music  "BGM16"
    "我和莉莉丝走进房间时异口同声地叫道。"
    "房间里放着我们走时还没有的东西。"
    "被子……而且是双人用的。"
    "难道说，这就是那坏笑的意义所在吗？准备这些的是，稻穗！？"
    voice "NRI10A_RI005"
    莉莉丝 "「那，那个……」"
    "不管怎么说，这意图也太明显了吧……话说，稻穗到底在期待着些什么啊！？"
    play sound "SE00_47"
    voice "NRI10A_SN005"
    信 "「哦，两位。你们果然关系很好呢。这东西叫做双人铺。」"
    window hide
#CHR_SORT 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA02"),"True","img/SN_MBA02A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA03"),"True","img/RI_MBA03A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    志雄 "「不要卖弄你的知识了！准备这些的是稻穗你吧！？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA05"),"True","img/SN_MBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI10A_SN006"
    信 "「不，很遗憾我不记得自己有准备这些。那一定是妖精做的吧。」"
    志雄 "「真是邪恶的妖精呢……与其说它是妖精，不如说那是妖怪吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBB02"),"True","img/SN_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI10A_SN007"
    信 "「真是失礼。那妖精一定是拥有着一颗善良的心，希望使两人那停滞不前的关系稍稍有那么点进展吧。」"
    "虽然方法完全不正确……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA02"),"True","img/SN_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI10A_SN008"
    信 "「没关系。我不会偷看也不会偷听的，放心吧。」"
    志雄 "「这话的可信度连千分之一也没有。而且，只是和莉莉丝同一间房，就已经很是问题了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA05"),"True","img/SN_MBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI10A_SN009"
    信 "「什么，塚本君要做出会引发问题的事吗？」"
#CHR_GET_POSC 1,F24,F25
#RSUB F24
#BG_LAY 3,RI_MXC03,2,F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC03"),"True","img/RI_MBC03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#REEK_CHR 1
    voice "NRI10A_RI006"
    莉莉丝 "「诶！？」"
#THREAD_STP 1
    hide bg3 with dissolve
    志雄 "「啊不，没这回事……」"
    voice "NRI10A_SN010"
    信 "「哈哈。那么，即使身旁的她安心地睡着，你也什么都不做吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBB01"),"True","img/SN_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI10A_SN011"
    信 "「要是我的话才不会忍耐呢。啊啊，是那个吧，现在很流行的食草系？」"
    志雄 "「总，总之，没有普通一点的被子吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA04"),"True","img/SN_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI10A_SN012"
    信 "「真遗憾，我不是说过来了一个团队吗？被子的供应已经很紧张了。」"
    志雄 "「真的吗……？我已经开始怀疑你说的每句话了。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2
#CHR_PRIC 2
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA05"),"True","img/SN_LBA05A@2x.png") as lh0 zorder (10-2):
        ypos 0.0
    with dissolve
#ROUTINE_STA
#CHR_ALP_AUTOC 0,0,1,F24
#CHR_ALP_AUTOC 1,0,1,F24
#CHR_ALP_AUTOC 2,128,1,F24
#BG_BLUR 0
#ROUTINE_STP
#CHR_ERSWC 0,1
    voice "NRI10A_SN013"
    信 "「真的啦！不信你看着我的眼睛！」"
    志雄 "「那是在打着什么鬼主意的眼神。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA06"),"True","img/SN_LBA06A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI10A_SN014"
    信 "「作为大人，我经历过太多太多，苦辣酸甜各种滋味我早已尽尝了。」"
    志雄 "「这和被子有什么关系吗……」"
    志雄 "「对了。稻穗，我睡到你的房间吧？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+224)
#CHR_PRIC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBB03"),"True","img/RI_MBB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .9
    with dissolve
#BG_BLUR 0
    voice "NRI10A_RI007"
    莉莉丝 "「哎，那，那样的话……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBB04"),"True","img/SN_LBB04A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI10A_SN015"
    信 "「喂喂喂，等一下，塚本君。我可没有那方面的兴趣哟。」"
    志雄 "「我也没有啦！我只是认为和莉莉丝睡在一间房间里有些问题而已！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBB02"),"True","img/SN_LBB02A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI10A_SN016"
    信 "「嗯……怎么办呢……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA05"),"True","img/SN_LBA05A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI10A_SN017"
    信 "「果然不行。对于花钱来的顾客，不能让他们住在店员的房间里。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA06"),"True","img/SN_LBA06A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI10A_SN018"
    信 "「……因此，你就早早放弃，做好觉悟吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBB02"),"True","img/RI_MBB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    志雄 "「觉悟是指什么啊，觉悟！？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA02"),"True","img/SN_LBA02A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI10A_SN019"
    信 "「那么，我还有事要做，待会见。要好好吃饭哟。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA01"),"True","img/SN_LBA01A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI10A_SN019A"
    信 "「加油，塚本君！我会在暗处支持你的！」"
    志雄 "「加、什、么、油啊，什么嘛！？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA06"),"True","img/SN_LBA06A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI10A_SN020"
    信 "「哼哼哼～」"
    window hide
    stop music fadeout 1
    hide lh0 with dissolve
    play sound "SE00_48"
    play sound "SE05_17L"
    "稻穗把该说的都说完后离开了房间。"
    "那家伙到底想做什么啊。"
    "我来回看着铺在床上的被子和红着脸的莉莉丝。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBB02"),"True","img/RI_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「那个，怎么办？我只要拿着毯子睡在那边角落里就好的。」"
    voice "NRI10A_RI008"
    莉莉丝 "「……没、没关系的，睡在一起也可以。」"
    voice "NRI10A_RI009"
    莉莉丝 "「再说，我睡觉时的表情你不也是经常看到的吗，现在还拘束什么呀。」"
    志雄 "「那是两回事吧……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD04"),"True","img/RI_LBD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI10A_RI010"
    莉莉丝 "「总之，志雄在这种奇怪的地方太敏感了。太麻烦了，就这么定了！可以的吧？」"
    志雄 "「诶，你要是觉得没问题的话……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD05"),"True","img/RI_LBD05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI10A_RI011"
    莉莉丝 "「这，这也没办法吧？稻穗也说了不能住在他房间里，就算是我也不可能让你睡在走廊吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD02"),"True","img/RI_LBD02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI10A_RI012"
    莉莉丝 "「这也是不得已而为之的！」"
    "可是，这样真的好吗……？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA01"),"True","img/RI_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI10A_RI013"
    莉莉丝 "「先别提这事儿啦，我肚子都瘪了。咱们去吃饭吧。」"
    志雄 "「啊，说的也是。被子的事就待会儿再想吧。」"
    voice "NRI10A_RI014"
    莉莉丝 "「嗯。那走吧！」"
    志雄 "「喂，喂！不要拉我啊！」"
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
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT