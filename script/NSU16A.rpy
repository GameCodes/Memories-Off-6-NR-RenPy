label NSU16A:
    $currentlabel = "NSU16A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '30'
    $date = '0'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG60AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG60AA@2x.jpg" as bg0 with dissolve
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
#SE_VOLC 1,64
    "总算走回旅馆后，看到稻穗正在旅馆前打扫。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA02"),"True","img/SN_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "OBGM25"
    voice "NSU16A_SN000"
    信 "「哟，这不是塚本君吗」"
    志雄 "「……你好」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA01"),"True","img/SN_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN001"
    信 "「嗯？一副无精打采的样子，这是怎么了……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA05"),"True","img/SN_LBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "稻穗话还没说完，就左顾右盼张望着四周。"
    "在找铃吗？"
    voice "NSU16A_SN002"
    信 "「没在一起吗……老姐呢？」"
    志雄 "「我们今天各自行动」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBB02"),"True","img/SN_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN003"
    信 "「单独行动么……不过，志雄君看起来没什么精神啊。发生什么事啦？还是说，老姐给你添什么麻烦了？」"
    志雄 "「没……没什么，没事」"
    "吵架了……要把这种话说出口，我还是有点顾忌。"
    voice "NSU16A_SN004"
    信 "「要说这种话，语气不更镇定可不行呢」"
    志雄 "「抱歉……」"
    "可是，从刚才开始就感到后悔不已，止不住叹气。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBB01"),"True","img/SN_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN005"
    信 "「唔……塚本君，请在这稍等一下」"
    志雄 "「咦？啊，好的」"
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
    "稻穗收起扫帚后走进了旅馆。"
    志雄 "「……？」"
    "片刻后，稻穗拿着罐装咖啡走了出来。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA01"),"True","img/SN_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN006"
    信 "「给你。我也要休息一下，顺便聊聊吧」"
    志雄 "「……嗯」"
    "总觉得就算是对稻穗说了，也解决不了什么问题啊……"
    "不过，稻穗毕竟是铃的弟弟呢，或许的确该说点什么。这么下去只会是越来越消沉。"
    play sound "SE03_37"
    "我一边喝着咖啡，一边跟着稻穗在旅馆里溜达。"
    voice "NSU16A_SN007"
    信 "「说吧，到底发生什么了呢？」"
    志雄 "「那是……」"
    "我把旅行以来发生的事，大致上告诉了稻穗。"
    window hide
    play music "BGM14"
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG63AA@2x.jpg" as bg2 zorder 20 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,(320)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB01"),"True","img/SU_LBB01A@2x.png") as lh1 zorder (100-1):
        ypos 0.0
    with dissolve
#SE_VOLC 1,0,16
#BG_INIC 1
#BG_PRI 1
    #show expression "img/BG_WHITE@2x.jpg" as bg1 with dissolve
#BG_ALPC 2,128
#CHR_ALPC 1,128
#BG_BLUR 2
    hide bg1 with dissolve
    "被铃拉来旅行，期待着通过这次旅行两人的关系能有所进展。"
    window hide
#CHR_PRIC 1
#BG_PRI 2
#BG_SET_BACK 
#BG_BLUR 2
#BG_INIC 0
#BG_PRI 0
    show expression "img/BG64NA@2x.jpg" as bg0 zorder 20 with dissolve
#BG_ALP_AUTOC 2,0,0,F24,48
#CHR_ALP_AUTOC 1,0,0,F24,48
#EFF_STAC 0,YUGE2,EFF_SKIP
#BG_ALP_SAVEC 2
#CHR_ALP_SAVEC 1
#CHR_SWPC 0
    hide lh0 with dissolve
#BG_SWPC 0
    hide bg0 with dissolve
    "虽然也有开心的游玩，进入了很好的气氛之类的，不过也有怎么说也无法置之不理的事情。"
    window hide
#BG_PRI 2
#CHR_PRIC 1
#BG_SET_BACK 
#BG_INIC 0
#BG_PRI 0
#BG_UVC 0,0,512,640,448
#BG_ALPC 0
    show expression "img/BG70AA@2x.jpg" as bg0 zorder 0 with dissolve
    #scene expression "img/BGNO@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_ALPC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC03"),"True","img/SU_LCC03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#EFF_STPC 0,EFF_SKIP
#BG_ALP_AUTOC 0,128,0,F24,48
#CHR_ALP_AUTOC 0,128,0,F24,48
#BG_ALP_SAVEC 0
#CHR_ALP_SAVEC 0
#BG_ALPC 2
#CHR_ALPC 1
#BG_SWPC 0
#BG_PRI 2
#BG_PRI 0
#BG_BLUR 2
#CHR_SWPC 0
#CHR_PRIC 1
#CHR_PRIC 0
    "因为摩托车的事情和铃发生了口角。"
    window hide
    "而且……铃是如何看待我的，我并不清楚。"
    window hide
#BG_SET_BACK 
#BG_INIC 0
#BG_ALPC 0
    scene expression "img/BG60AA@2x.jpg" as bg0 zorder 0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA01"),"True","img/SN_LBA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
#BG_INIC 1
#BG_PRI 1
    show expression Solid("fff") as bg1
    with ImageDissolve("img/BG_MASK15@2x.png",1)
    hide bg2 with dissolve
    hide lh1 with dissolve
#BG_PRI 0
#BG_PRI 1
#BG_PRI 2
#CHR_PRIC 0
#CHR_PRIC 1
#BG_UVC 0,0,0,640,448
#BG_UVC 2,0,0,640,448
#BG_PRI 0
#BG_PRI 1
#BG_PRI 2
#CHR_PRIC 0
#CHR_PRIC 1
#BG_UVC 0,0,0,640,448
#BG_UVC 2,0,0,640,448
#BG_ALPC 0,128
#CHR_ALPC 0,128
#SE_VOLC 1,64
    hide bg1 with dissolve
    "我就这样倾诉着，不知不觉间把咖啡喝完了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA05"),"True","img/SN_LBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN008"
    信 "「正因为是和我老姐交往，确实是很困难呢……有各种各样要操心的」"
    志雄 "「真的是很困难……吗？」"
    "说实话，因为自己没什么恋爱经验，究竟有多困难，自己心里并不清楚。"
    "只是……感觉很辛苦。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA06"),"True","img/SN_LBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN009"
    信 "「作为弟弟的我来看，和老姐交往的话，用一般的手段可是行不通的」"
    "稻穗用手抵着下巴，一副自夸的样子点着头。"
    志雄 "「年龄有差距，是说铃有自己的一套呢，还是说我太我行我素了呢」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBB01"),"True","img/SN_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN010"
    信 "「啊～，不不不，没这回事」"
    "稻穗摇摇头笑着否认了我的话。"
    志雄 "「诶？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA01"),"True","img/SN_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN011"
    信 "「因为最近没怎么见到的缘故吧，或许多少会有些变化。但基本上，老姐对恋爱的事情是相当晚熟，很胆小的啊」"
    志雄 "「……胆小？」"
    voice "NSU16A_SN012"
    信 "「毕竟关系已经很深的人也在这里！她就是这种关键时刻会掉链子的类型啦。这么说能明白吗」"
    志雄 "「这个倒是看不出来……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA04"),"True","img/SN_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN013"
    信 "「正因为她是这样的人，所以她并不懂得分寸，对于喜欢的人就想要走的更近，赶紧扑进对方的怀抱呢」"
    "稻穗无奈地摇了摇头。不愧是弟弟，看的相当清楚。"
    志雄 "「……如此说来，是我会错意了吗？」"
    "铃到底是怎么看待我的呢？"
    "只是关系不错的朋友吗……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA01"),"True","img/SN_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN014"
    信 "「我觉得不是这样的」"
    志雄 "「为什么？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA03"),"True","img/SN_LBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN015"
    信 "「嗯……」"
    "稍稍沉默了一会儿，稻穗开口道。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA05"),"True","img/SN_LBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN016"
    信 "「接下来说的话，可要对老姐保密啊？」"
    window hide
#BG_SET_BACK 
#BG_INIC 3
#BG_ALPC 3
#BG_UVC 3,0,512,640,448
    show expression "img/BG16AA@2x.jpg" as bg3 zorder 11 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_INIC 2
#CHR_ALPC 1
#CHR_ALPC 2
#CHR_POSC 1,(320-192)
#CHR_POSC 2,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAC03"),"True","img/SU_MAC03A@2x.png") as lh1 zorder (10+1):
        xcenter (320-192)/640.0
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA06"),"True","img/RI_MBA06A@2x.png") as lh2 zorder (10+2):
        xcenter (320+96)/640.0
        ypos 0.0

#SE_VOLC 1,0,16
#BG_INIC 1
#BG_PRI 1
    #show expression "img/BG_WHITE@2x.jpg" as bg1 with dissolve
#BG_ALPC 3,128
#CHR_ALPC 1,128
#BG_BLUR 3
    hide bg1 with dissolve
    voice "NSU16A_SN017"
    信 "「……之前，我在『小文』和她碰过面的吧？」"
    "这么说来，几天前确实有过这么一回事……"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_UVC 2,0,512,640,448
    scene expression "img/BG17AA1@2x.jpg" as bg0
    with dissolve
#CHR_ALPC 1,128
#CHR_ALPC 2,128
    hide bg3 with dissolve
#BG_BLUR 2
    voice "NSU16A_SN018"
    信 "「事实上，那个时候，我和莉莉丝正在跟老姐商量她的恋爱问题」"
    志雄 "「诶？商量铃的恋爱问题？」"
    "他们在那里大声地争执，我只听到一部分，没想到竟然是在说这方面的事。"
    "铃竟然会和别人商量这种事情，这种不像铃的行为让我不敢相信。"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD01"),"True","img/RI_MBD01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NSU16A_SN019"
    信 "「正确的说，是莉莉丝盘问了老姐，为她打气来着」"
    志雄 "「莉莉丝吗？」"
    voice "NSU16A_SN020"
    信 "「问你和老姐到底进展如何了」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBB01"),"True","img/RI_MBB01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NSU16A_SN021"
    信 "「这种青梅竹马不是挺不错么」"
    "莉莉丝这家伙，真是瞎操心……"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAA07"),"True","img/SU_MAA07A@2x.png") as lh1 zorder (10+1):
        xcenter 0.25
        ypos 0.0
    with dissolve
    voice "NSU16A_SN022"
    信 "「然后呢，老姐虽然想方设法隐瞒，最后还是坦白了她很在意你」"
    志雄 "「是吗？……什么，这是真的吗？」"
    voice "NSU16A_SN023"
    信 "「一旦说出口，话就变得多了起来」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAC04"),"True","img/SU_MAC04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter 0.25
    with dissolve
    voice "NSU16A_SN024"
    信 "「和志雄君交往该怎么做才好呢……她说会有这样的烦恼」"
    志雄 "「铃会说这样的话……」"
    "……原来不是我一个人在烦恼。"
    "安心下来之后，突然有种如释重负的感觉。"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAA03"),"True","img/SU_MAA03A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA03"),"True","img/RI_MBA03A@2x.png") as lh2 zorder (10+2):
        xcenter .75
#CHR_SET_BACK
#CHR_SORT 3,1,2
#CHR_INIC 3
#CHR_ALPC 3
#CHR_POSC 3,(320-192)
    hide lh3
    hide lh1
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XAA05"),"True","img/SU_XAA05A@2x.png") as lh3 zorder (10-3):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 24
#MOV_CHR1 0,(320)
#MOV_CHR2 0,640
#MOV_CHR3 128,(320)
#MOV_CHR_GO 1
#CHR_ERSWC 1,2
#CHR_ALPC 1,128
#CHR_ALPC 2,128
#QUA2_ALL 
    voice "NSU16A_SN025"
    信 "「唉，虽说那个时候我挑衅过度，有些惹她生气了吧」"
#BG_BLUR 2
    window hide
#BG_SET_BACK 
#BG_INIC 0
#BG_ALPC 0
    show expression "img/BG60AA@2x.jpg" as bg0 zorder 0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBB01"),"True","img/SN_LBB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#BG_INIC 1
#BG_PRI 1
    #show expression "img/BG_WHITE@2x.jpg" as bg1 with dissolveBG_MASK15
    hide lh3 with dissolve
#CHR_SORT 0,1
    hide bg2 with dissolve
#BG_UVC 2,0,0,640,448
#BG_ALPC 0,128
#CHR_ALPC 0,128
#CHR_ALPC 2,128
#SE_VOLC 1,64
    hide bg1 with dissolve
    voice "NSU16A_SN026"
    信 "「我也只是给你一些建议而已」"
    志雄 "「难道说，这次的旅行是？」"
    "这么说来，才想起之前确实被铃问了各种各样奇怪的问题。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA01"),"True","img/SN_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN027"
    信 "「嗯，或许是这样吧」"
    voice "NSU16A_SN028"
    信 "「也就是说，你们在为相同的事情而烦恼」"
    "稻穗大口喝着罐装咖啡，无可奈何地耸耸肩。"
    志雄 "「不过，看不出铃有这种烦恼……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA03"),"True","img/SN_LBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN029"
    信 "「本来是信心满满地来到这里，也许是过于沉迷于游玩，又或者是因为胆怯吧」"
    voice "NSU16A_SN030"
    信 "「真是的，攻击我的时候明明那么凶猛」"
    志雄 "「和我一样……吗……这样的话，我该怎么做……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA01"),"True","img/SN_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN031"
    信 "「这样情况你即使不去管她，倒也没什么关系的」"
    voice "NSU16A_SN032"
    信 "「胆怯终归是老姐自身的问题。即使不去刻意做什么，也没什么问题吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA05"),"True","img/SN_LBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN033"
    信 "「至于你呢，只要将自己的心意传达给她就行了」"
    志雄 "「诶？」"
    voice "NSU16A_SN034"
    信 "「要传达对彼此的心意。那样的话，即使是老姐也会迈出关键的一步吧」"
    志雄 "「说得是啊……」"
    voice "NSU16A_SN035"
    信 "「嗯。不过，因此就懈怠下去是不行的哟。不要介意年龄的差距，要勇于向对方传达自己的心意。如果感觉不到你的心意的话……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA03"),"True","img/SN_LBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN036"
    信 "「老姐多半会从你的面前逃走的」"
    志雄 "「逃走……」"
    voice "NSU16A_SN037"
    信 "「果然是年龄上的差距啊……之类的。她是因为这种理由，会让自己在受伤之前逃跑的人」"
    志雄 "「啊……这下总算明白了」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA01"),"True","img/SN_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN038"
    信 "「老姐啊，虽然总是一副强硬的样子，偶尔也要让她意识到你的存在」"
    志雄 "「只是，因为过于强硬，会不会吵架呢……」"
    "会这样问，正是因为我们现在正在吵架。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA02"),"True","img/SN_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN039"
    信 "「吵架也无所谓啊。与两个人相互奇怪地试探距离相比，这个不是更合乎常理吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBB05"),"True","img/SN_LBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN040"
    信 "「……呵呵，原来如此。刚吵完架吧」"
    志雄 "「不，只是争执了几句罢了……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBB01"),"True","img/SN_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN041"
    信 "「那恕我直言了。莫非，是关于摩托车的吗？这个的话是老姐不好」"
    "稲穂一副了然于胸的样子，很干脆地下了结论。"
    志雄 "「不过我也过于激动，说了些否定铃的兴趣的话」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA01"),"True","img/SN_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN042"
    信 "「不过，老姐骑起摩托车实在过于乱来了。如果不说她的话，或许真的会出事。既然这样骑车的话，就需要相应的觉悟和关注的」"
    voice "NSU16A_SN043"
    信 "「不过，这回提醒已经不够了吧」"
    "是……这样啊。即使从旁观者的稻穗来看，果然也是这样。"
    "因为担心铃，到现在也不认为自己说错了话。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA05"),"True","img/SN_LBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN044"
    信 "「只是，塚本君。你也有不对的地方」"
    志雄 "「诶？」"
    voice "NSU16A_SN045"
    信 "「只是一味地责备她，老姐肯定不会接受吧」"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG70AA@2x.jpg" as bg2 zorder 20 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,(320)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC03"),"True","img/SU_LCC03A@2x.png") as lh1 zorder (30-1):
        ypos 0.0
    with dissolve
#SE_VOLC 1,0,16
#BG_INIC 1
#BG_PRI 1
    #show expression "img/BG_WHITE@2x.jpg" as bg1 with dissolve
    show expression "img/BG70AA@2x.jpg" as bg0 with dissolve
#BG_ALPC 0
#BG_ALPC 2,128
#CHR_ALPC 0
#CHR_ALPC 1,128
#BG_BLUR 2
    hide bg1 with dissolve
    hide lh0
    with dissolve
    "是这样没错……"
    "确实，那个时候只是在抱怨他。"
    "或许是坐在摩托车上的我从自己的角度出发，才会不停地责备铃……"
    志雄 "「没错、呢。自己究竟想说什么，我已经明白了」"
    "虽然自己的安全是很重要，但我想说的其实并不是这个。"
    "而是因为担心铃……如果能好好地告诉她就好了。"
    window hide
#BG_INIC 1
#BG_PRI 1
    #show expression "img/BG_WHITE@2x.jpg" as bg1 with dissolveBG_MASK15
#BG_BLUR 2
    hide lh1 with dissolve
    hide bg2 with dissolve
#BG_UVC 2,0,0,640,448
    scene expression "img/BG60AA@2x.jpg" as bg0 with dissolve
#BG_ALPC 0,128
#CHR_ALPC 0,128
#SE_VOLC 1,64
    hide bg1 with dissolve
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA05"),"True","img/SN_LBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN046"
    信 "「问题就在这里。对于照料老姐的塚本君来说，现在制造气氛的有用情报只有一个」"
    志雄 "「咦……是什么？」"
    voice "NSU16A_SN047"
    信 "「这座山上有条小路，路上有个露天浴池」"
    志雄 "「是宝树庵的那个？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA01"),"True","img/SN_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN048"
    信 "「对。因为在那里工作过一次，所以可以自由进出」"
    志雄 "「不是那种观光旅游的地方？」"
    voice "NSU16A_SN049"
    信 "「因为不是很大，游客也不会一拥而入，似乎是那种识货的人才会去的地方」"
    志雄 "「明白了！我这就去约铃！」"
    voice "NSU16A_SN050"
    信 "「平常傍晚以后更衣室就关闭了，这次算是特别服务，我会去打开的」"
    志雄 "「太感谢了」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA02"),"True","img/SN_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN051"
    信 "「那就请好好努力，降低老姐的危险性」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA01"),"True","img/SN_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN052"
    信 "「……可以的话，今后也拜托你了」"
    "稻穗把咖啡一饮而尽，向旅馆走去。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA01"),"True","img/SN_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU16A_SN053"
    信 "「接下来，我就享受成年人的特权，在一旁悠然看着少年与烦恼斗争了」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "稻穗回过头朝我笑了笑，挥挥手后走进了旅馆。"
    "稻穗君……比我想像中更成熟。"
    "我也想早点成为这样一个沉着冷静的人。"
    志雄 "「那么……就开始努力吧……」"
    "我一边想着该如何向铃开口，一边取出了手机。"
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