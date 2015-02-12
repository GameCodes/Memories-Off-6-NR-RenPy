label NCH02A:
    $currentlabel = "NCH02A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '18'
    $date = '2'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_BG NIMG15J,CAL_0718
    show expression "img/NIMG15J-568h@2x.jpg" as cal zorder 5
    show expression "img/07_18_TUESDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
#FADE_OUT 1,32,COL_WHITE
    scene expression Solid("000") with fade
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG12AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG12AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_15L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,(64/2)
    play music "BGM13"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    志雄 "「我吃饱了」"
    "感觉饱得恰到好处，我放下了筷子。"
    window hide
#SE_VOLC 1,0
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB01"),"True","img/CH_LAB01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCH02A_CH000"
    智纱 "「粗茶淡饭不成敬意」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA01"),"True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    
    voice "NCH02A_CH001"
    智纱 "「……」"
    "虽然嘴里没有说，但是智纱已经用充满期待的目光望向了我这边。"
    "就连智纱这种视线中的含义，我最近也能够全部领会了。"
    志雄 "「今天的午饭也很好吃呢。一直以来谢谢你了，智纱」"
    "听了这句话，就像绷紧的弦终于松下来了一样，智纱放心地舒了一口气。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB02"),"True","img/CH_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH002"
    智纱 "「……太好了」"
    "智纱微微一笑。"
    志雄 "「可是，这不是很麻烦么？　每天连我的那份便当都要做」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB01"),"True","img/CH_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH003"
    智纱 "「一个人的量和两个人的量，没有太大差别的，不用太在意的，没关系」"
    志雄 "「……那样的话倒是没问题」"
    "对智纱这种直截了当的好意，以及两个人独处的时间，还是稍微感到有些害羞和紧张。"
    "从开始交往过了这么长的时间，在这一点上也和那个时候没有什么不同。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_INIC 2
#BG_PRI 1
#BG_PRI 2
    show expression "img/EV_CH01B@2x.png" as bg2 zorder 20 with dissolve
#MUS_VOL 64
    hide bg1 with dissolve
    "在去年的秋天，被智纱告白了……。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_PRI 1
#BG_PRI 2
    hide bg2
#BG_INIC 3
    show expression "img/EV_CH09A@2x.png" as bg3 zorder 30 with dissolve
    hide bg1 with dissolve
    "智纱开始为我做便当，就是从那个时候开始的。这种『一起吃便当』的习惯，到现在也一直未曾改变。"
    window hide
#BG_INIC 1
#BG_PRI 1=
    hide bg3 with dissolve
#BG_ALPC 0
#CHR_ALPC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB04"),"True","img/CH_LAB04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#MUS_VOL 128
    hide bg1 with dissolve
    voice "NCH02A_CH004"
    智纱 "「怎么了？　总觉得你有点发呆」"
    志雄 "「没什么，就是想起了和智纱刚开始交往那时候的事情了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB03"),"True","img/CH_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH005B"
    智纱 "「啊……」"
    "智纱的脸红了，脸上浮现了呆板的笑容。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA06"),"True","img/CH_LAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH006"
    智纱 "「啊哈哈。发生了很多事呢」"
    "想起刚开始交往的时候的事情，果然是有点不好意思。我也是。"
    志雄 "「而、而且，智纱真的很擅长做菜呢。就算是将来自己开餐馆，不是也足够了吗？」"
    "为了掩盖自己的难为情，我把话题转向别的方向。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB02"),"True","img/CH_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH007"
    智纱 "「啊哈哈，那个就太夸张了」"
    志雄 "「不不，没有夸张啦」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB01"),"True","img/CH_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH008"
    智纱 "「不是，就是夸张啦。我只是觉得，能让志雄君说好吃，仅仅这样，就足够了」"
    "智纱那样说着，对我腼腆地一笑。"
    "对眼前这个女孩的那份爱，从心底涌了上来。"
    "就像是被那种感情所驱动，我向智纱伸出了手——。"
    if persistent.autosave_choice:
        python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                 persistent.auto_slot = 1
    menu:
        "抚摸她的头":
            $F7=0
        "克制住":
            $F7=1
    if F7==0:
        jump L_NCH02A_SEL00_A
    if F7==1:
        jump L_NCH02A_SEL00_B
label L_NCH02A_SEL00_A:
    $F1+=1
    "我把手放在了智纱的头上。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB04"),"True","img/CH_LAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH009"
    智纱 "「哎，那个，志雄君？」"
    "突然间头被摸了，智纱很困惑地仰视着我。但是，绝对不是因为感到讨厌。"
    志雄 "「就让我这样摸一小会儿吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB03"),"True","img/CH_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH010"
    智纱 "「……嗯」"
    "两颊微红，智纱脸朝下轻轻点了点头。那种像小动物一样的动作，让人不由得感到可爱……。"
#SE_VOLC 1,(64/2)
    stop music fadeout 1
    voice "NCH02A_TO000"
    亨？ "「这对，笨蛋情侣啊－－－－！！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB04"),"True","img/CH_LAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE09_36"
#THREAD_STA 1,THREAD_QUA_WIN
#VIB_DOKA 
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    志雄 "「好疼！？」"
    with vpunch
#MESA A_CH_SI,"【志雄】「好疼！？」"
#THREAD_WAT 1
#WIN_POS 0,0
#VIB_STP 5
#MESX "%K%P"
    "一阵让视野摇动的冲击，冲向我的头部。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA03"),"True","img/CH_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#REEK_CHR 0
    voice "NCH02A_CH011"
    智纱 "「没，没事吧！？」"
#REMOVE_REEK_CHR 0
    志雄 "「到底，怎么回事啊……」"
    "揉着发痛的头部，我回头看着身后。"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#SE_VOLC 1,0
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA02"),"True","img/TO_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    play music "BGM09"
    if not persistent.dictlist[7] and persistent.show_dict:
        $persistent.dictlist[7]=True
        show screen dict_pop(i=7)
    "站在背后的是我的狐朋狗友，亨。他的手里拿着客人用的拖鞋。"
    志雄 "「你在搞什么飞机啊！」"
    voice "NCH02A_TO001"
    亨 "「搞什么飞机，还搞飞碟呢！」"
    "飞碟？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA03"),"True","img/TO_MAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO002"
    亨 "「……哈」"
    "直到刚才，亨的脸上还充满着不动明王还是仁王一样的怒气，但现在他只是呆然地叹着气，然后朝着我这边瞪了过来。"
    jump L_NCH02A_SEL00_X
label L_NCH02A_SEL00_B:
#SE_VOLC 1,(64/2)
    stop music fadeout 1
    play sound "SE07_18"
    志雄 "「——！？」"
    "在这一瞬间，我感觉从背后传来了『杀气』一般的气息。"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#SE_VOLC 1,0
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA02"),"True","img/TO_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    play music "BGM09"
    "回过头来看，站在那里的是我的狐朋狗友，亨。他的手里拿着不知从哪里找来的，客人用的拖鞋。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA04"),"True","img/TO_MAA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO003"
    亨 "「……嗯」"
    "亨的拖鞋，已经以完全要打下来的架势，抡过了头顶。"
    志雄 "「你这是，搞什么啊？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA05"),"True","img/TO_MAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO004"
    亨 "「没什么，就是在想拿这个打你」"
    志雄 "「凭什么打我啊！？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB04"),"True","img/TO_MAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO005"
    亨 "「竟然问……凭什么？」"
    "亨把已经抡过头顶的拖鞋慢慢地放下，叹了口气。"
    "然后用呆然的视线看着我，戏虐地说道。"
    jump L_NCH02A_SEL00_X
label L_NCH02A_SEL00_X:
    window hide
    stop music fadeout 1
#MOV_CHR_INIT 64
#MOV_CHR1 ,(320-160)
#MOV_CHR_GO 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    play music "OBGM28"
    voice "NCH02A_TO006"
    亨 "「智纱……一直以来都为我做便当，太感谢你了！　你真的是太可爱了！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA05"),"True","img/TO_MAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO007"
    亨 "「我，已经忍不住了啊！」"
    window hide
#MOV_CHR_INIT 32
#MOV_CHR1 0
#MOV_CHR_GO 1
#CHR_POSC 1,640
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 64
#MOV_CHR1 128,(320+160)
#MOV_CHR_GO 1
    voice "NCH02A_TO008"
    亨 "「啊，志雄君！　把我抱得再紧一些吧！」"
    window hide
    stop music fadeout 1
#MOV_CHR_INIT 64
#MOV_CHR1 
#MOV_CHR_GO 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO009"
    亨 "「……嗯，就是像这样吧」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAA02"),"True","img/TO_LAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#BG_BLUR 0
    play music "OBGM23NL"
    voice "NCH02A_TO010"
    亨 "「大中午的，你们就在这展现那种连我看了都害臊的场面，你们啊，当我是笨蛋吗！？」"
    志雄 "「你等等！　我才没做那种事！　我才没抱着她呢！」"
    window hide
    stop music fadeout 1
#SE_VOLC 1,(64/2)
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
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA03"),"True","img/TO_MAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO011A"
    亨 "「哼。但是，{w=4}{nw}"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB01"),"True","img/TO_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO011B"
    extend "你是打算要那样做的吧？」"
    志雄 "「怎么可能！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA05"),"True","img/CH_MAA05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB01"),"True","img/TO_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with move
#MOV_CHR_INIT 48
#MOV_CHR0 128,(320-160)
#MOV_CHR1 ,(320+160)
#MOV_CHR_GO 1
    voice "NCH02A_CH012"
    智纱 "「就，就是啊！」"
    "智纱也红着脸否定着。"
    "真是的……。在这种不知道什么时候就会来人的地方，可不能去抱智纱啊。"
    window hide
#SE_VOLC 1,0
    play music "BGM09"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA06"),"True","img/TO_MAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO012"
    亨 "「……什么啊，是我一时冲动，搞错了吗」"
    志雄 "「要是因为你的一时冲动而被打，任谁也都受不了啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA04"),"True","img/TO_MAA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO013A"
    亨 "「啊～，即使是那样你挨揍也是理所当然的。因为你每天都和可爱的女朋友一起吃着便当，还做着{w=10}{nw}"
#VO_WAT VO_WAIT_START
#MESA A_CH_TO,NCH02A_TO013A,"【亨】「啊～，即使是那样你挨揍也是理所当然的。因为你每天都和可爱的女朋友一起吃着便当，还做着"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO013B"
    extend "『来，啊～。亲爱的』{w=4}{nw}"
#MESA A_CH_TO,NCH02A_TO013B,"『来，啊～。亲爱的』"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA03"),"True","img/CH_MAA03A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA02"),"True","img/TO_MAA02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NCH02A_TO013C"
    extend "这种事情」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA03"),"True","img/TO_MAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO014"
    亨 "「到底要晒到什么程度你才满意啊！？　你已经彻底地和全世界的光棍为敌了！」"
    志雄 "「亨，你的眼神好可怕……」"
    志雄 "「本来，我们也没有每天『来，啊～』什么的啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA05"),"True","img/CH_MAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH013"
    智纱 "「嗯，嗯。是的呢。没那样做的」"
    "智纱搪塞一般地，游动着视线。看到她的动作，亨的眼睛闪过一丝光芒。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA05"),"True","img/TO_MAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO015"
    亨 "「……做了吧，每天」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA03"),"True","img/CH_MAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「才，才没做！」"
    "这么说来，偶尔也是互相喂饭吃的……但是那也仅限于，智纱来到我家，给我做饭的时候了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB03"),"True","img/TO_MAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO016A"
    亨 "「……用不了多久，你一定会被暗中袭击的。{w=5}{nw}"
#MESA A_CH_TO,NCH02A_TO016A,"【亨】「……用不了多久，你一定会被暗中袭击的。"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA02"),"True","img/TO_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO016B"
    extend "不，不如就让我来！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC06"),"True","img/CH_MAC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「总，总之先冷静下来」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA06"),"True","img/TO_MAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO017"
    亨 "「这能让我冷静得下来吗！？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA02"),"True","img/TO_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO018"
    亨 "「大体上说，作为校园模范的学生会长这样好吗！？　学生会长允许这样的不纯异性交往吗！？　对其他的干事起到模范作用了吗！？」"
    志雄 "「不，可是，这事大家已经都知道了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAB03"),"True","img/CH_MAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "让人难为情的是，包括春日同学在内的学生会全体成员，与其说是在期待我们两人关系的进展，不如说是在煽风点火。"
    stop music fadeout 1
    voice "NCH02A_CH014"
    智纱 "「那个，还有呢……佐贺君」"
    "智纱很客气地，跟在我的后面开始反驳起了亨。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA06"),"True","img/CH_MAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH015A"
    智纱 "「我们，可不是不纯异性交往哦。不是不纯的而是纯洁的……{w=7}{nw}"
    
#VO_WAT VO_WAIT_START
#MESA A_CH_CH,NCH02A_CH015A,"【智纱】「我们，可不是不纯异性交往哦。不是不纯的而是纯洁的……"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC05"),"True","img/CH_MAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH015B"
    extend "也许是有点强词夺理」"
    window hide
    play music "BGM13"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB03"),"True","img/TO_MAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    志雄 "「智纱……」"
    "听到了这句话，亨的肩膀突然无力地垂了下来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO019"
    亨 "「喔、喔喔……喔、喔……」"
    "亨的嘴里发出了来自地底的幽鬼一般的呻吟声。"
    志雄 "「没，没关系吧，亨？」"
    "有点担心他了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB04"),"True","img/TO_MAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO020"
    亨 "「……喔、我……！」"
    window hide
    stop music fadeout 1
#SE_VOLC 1,(64/2)
#ROUTINE_STA
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_UVC 0,(640/4),(448/4),(640/2),(448/2)
#CHR_INIC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAA14"),"True","img/TO_XAA14A@2x.png") as lh1 zorder 100:
        ypos 0.0
    with dissolve
#EFF_STAC 0,EYETWINKLE,EFF_NOSKIP,1,230,65,415,65
#ROUTINE_STP
    voice "NCH02A_TO021"
    亨 "「我也想和，莉莉丝一起过着卿卿我我的校园生活啊啊啊啊啊！」"
    window hide
#BG_CAMERA_OUT 0,BG12AA
#ROUTINE_STA
#BG_UV_AUTOC 0,(640/2),(448/4),(640/2),(448/2),1,F24
#CHR_POS_AUTOC 1,(640+320),0,1,F134
#ROUTINE_STP
    hide lh1 with dissolve
#EFF_STAC 0,TRAILTWINKLE,EFF_NOSKIP
    play sound "SE01_00B"
    pause (32/32.0)
    stop se
#SE_WATC 0
    play sound "SE00_31"
    pause (32/32.0)
#EFF_STPC 0,EFF_NOSKIP
    "亨这家伙，全力猛冲着跑开了。"
#ROUTINE_STA
#BG_INIC 0
    show expression "img/BG12AA@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA04"),"True","img/CH_LAA04A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
#ROUTINE_STP
    voice "NCH02A_CH016"
    智纱 "「佐贺君，难道是哭了？」"
    志雄 "「啊……看起来是那样的」"
    "刚才，确实感觉从亨的眼角看见了一点发光的东西。"
    志雄 "「这么说来，刚才亨的声音一定是已经响彻全校了吧。莉莉丝是不是也会听见呢」"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 0
#FADE_IN 0
    play sound "SE04_05"
    play sound "SE04_05"
    play sound "SE04_06"
    play sound "SE04_08"
    play sound "SE04_07"
#FADE_OUT 0
#BG_COLC 0,128,128
    scene expression "img/BG07AA3@2x.jpg" as bg0 with dissolve
#CHR_SORT 1,0,2
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320+160)
#CHR_POSC 1,(320-160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD04"),"True","img/RI_MAD04A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0

#CHR_SET_BACK
#FADE_IN 1
    play music "BGM10"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB04"),"True","img/TO_MAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO022"
    亨 "「疼疼疼」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_RI000"
    莉莉丝 "「别高声地喊那些让人难为情的话啊，真是的！」"
    "果然亨的叫声连莉莉丝也听到了。午休结束回到教室后，看到莉莉丝正在踢着亨。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB04"),"True","img/TO_MAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO023"
    亨 "「等，等等啊，莉莉丝！　我只是老实地面对自己的心情的！」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD02"),"True","img/RI_MAD02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE07_00"
#FILT_PRI 6
#FILT_IN 48,0,COL_DARK2
#BG_COL_SAVEC 0
#CHR_SET_BACK
#CHR_INIC 4
#CHR_INIC 5
#CHR_COLC 4,96,96,192,60
#CHR_COLC 5,80,80,192,76
#CHR_POSC 4,(320+160)
#CHR_POSC 5,(320+160)
#CHR_PRIC 1
#CHR_PRIC 0
#CHR_PRIC 4
#CHR_PRIC 5
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD02"),"True","img/RI_MAD02A@2x.png") as lh0 zorder (10+4):
        xcenter .25
        ypos 0.0
        linear 0.3 xcenter .75
    voice "NCH02A_RI001"
    莉莉丝 "「我说了那个让人很难为情的！」"
#FILT_OUT 48
#THREAD_STA 1,THREAD_RIRISU_KICK
#MESA A_CH_RI,NCH02A_RI001,"【莉莉丝】「我说了那个让人很难为情的！」"
#THREAD_WAT 1
#MESX "%K%P"
#CHR_ERSWC 2,3
#CHR_ERSWC 4,5
#CHR_PAL_BGC 2,BG07AA3
#CHR_PAL_BGC 3,BG07AA3
#CHR_PAL_BGC 4,BG07AA3
#CHR_PAL_BGC 5,BG07AA3
    play sound "SE04_07"
#ROUTINE_STA
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MHE01"),"True","img/RI_MHE01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA06"),"True","img/TO_MAA06A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .9
    with move
    pause 1
#CHR_POSC 0
#CHR_POS_AUTOC 1,(320+224),(0),0,F24,8
#CHR_SCL_AUTOC 1,512,512,0,F24,8
#ROUTINE_STP
#CHR_POS_SAVEC 1
#CHR_SCL_SAVEC 1
    play sound "SE04_15"
#QUA_CHR 1
    window hide
#FILT_PRI 5
#FILT_IN 48,0,COL_DARK2
#CHR_SORT 1,2
#CHR_SET_BACK
#CHR_INIC 2
#CHR_CNTC 2,480,308
#CHR_POSC 2,((320+160)-80),((-400)-224)
    "最近，感觉比起对我，莉莉丝踢亨的次数多了起来。"
    "但是莉莉丝的脚，其实只是踢向相当亲近的人。从那个角度来看，莉莉丝和亨的关系，也比之前有所进展了吧。"
    window hide
#FILT_OUT 48
#FILT_PRI 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA06"),"True","img/RI_MAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_RI002"
    莉莉丝 "「这家伙，真是的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA03"),"True","img/TO_MAA03A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
    亨 "「呜，莉莉丝……」"
#THREAD_STA 1,THREAD_TORU_ZURU
#MESA A_CH_TO,NCH02A_TO024,"【亨】「呜，莉莉丝……」"
#THREAD_WAT 1
#MESX "%K%P"
    window hide
#CHR_POS_AUTOC 2,(320+110)
#CHR_POS_AUTOC 2,(320+120),-160,0,F24,12
#CHR_ANG_AUTOC 2,2048,0,F24,12
#CHR_POS_SAVEC 2
#CHR_ANG_SAVEC 2
#CHR_ANGC 2
    play sound "SE04_35"
#QUA2_CHR 1
#THREAD_STA 1,THREAD_SHOES
    hide lh1 with dissolve
#CHR_SCLC 1,256,256
    play sound "SE04_17"
#QUA2_ALL 
#THREAD_WAT 1
    play sound "SE03_04"
    "加油吧，亨。直到你的心愿传达到的那天为止。"
    window hide
    stop se fadeout 1
#FADE_OUT 1
#CHR_SORT 0,1,2
    scene expression Solid("000") with fade
    stop se
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG07AA2@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG07AA2@2x.jpg" as bg0 with dissolve
    play sound "SE06_02"
    pause (32/32.0)
#FADE_IN 1
    voice "NCH02A_X8000"
    老师 "「那今天就到这里。给我直接回家，不要到处乱逛」"
    play sound "SE00_22"
    "终礼结束了，班主任从教室里走了出去。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    stop sound
    stop se fadeout 1
    play sound "SE08_09L"
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
#BG_SWPC 0
#BG_ALPC 1
#BG_PRI 0
#BG_PRI 1
    scene expression "img/BG07AA3@2x.jpg" as bg0 with dissolve
    志雄 "「哈～……今天的课程终于结束了啊～」"
    "我四肢无力地趴在了桌子上。由于已经３年级了，这段时间上课的内容也变难了。"
    window hide
#SE_VOLC 1
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO025"
    亨 "「哟，现在就回去吗？」"
    志雄 "「不，今天还有学生会的工作」"
    "我把脸贴在桌子上回答道。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO026"
    亨 "「怎么啦，有气无力的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO027"
    亨 "「拿出点精神来，看吧，外面天气多棒啊！」"
    window hide
#BG_SET_BACK 
#CHR_PRIC 1
#BG_PRIC 0
#EFF_PRI 0
#EFF_PRI 1
    scene expression "img/NIMG01B@2x.png" as bg2 zorder 2:
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
#ROUTINE_STA
#EFF_STAC 0,CLOUD_B,EFF_NOSKIP
#EFF_STAC 1,LENZ,EFF_NOSKIP
    hide lh1 with dissolve
#BG_ALP_AUTOC 0,0,0,1
#ROUTINE_STP
    hide bg0 with dissolve
    play sound "SE07_25"
    voice "NCH02A_TO028"
    亨 "「看，这强烈的阳光！　夏天从现在才开始啊！」"
    "只是阳光太过于强烈了，今天的气温已经超过３０度了。"
    window hide
#BG_ALPC 0
    scene expression "img/BG07AA3@2x.jpg" as bg0 with dissolve
#EFF_STPC 0,EFF_NOSKIP
#EFF_STPC 1,EFF_NOSKIP
#EFF_PRI 0
#EFF_PRI 1
    hide bg2 with dissolve
#BG_PRIC 0
    stop se
    志雄 "「就算是这样，你又怎么了，激动成这样」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB01"),"True","img/TO_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO029"
    亨 "「喔。不管怎么说，马上就要到暑假了嘛」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO030"
    亨 "「就是要在这个夏天，缩短和莉莉丝之间的距离啊」"
    "今天是7月17日。再过用一只手的指头都能数过来的天数，就是暑假了——高中的最后一个夏天。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO031"
    亨 "「你的暑假，定了什么计划没有？」"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "定好了":
            $F7=0
        "还没定好":
            $F7=1
    if F7==0:
        jump L_NCH02A_SEL01_A
    if F7==1:
        jump L_NCH02A_SEL01_B
label L_NCH02A_SEL01_A:
    $F1+=1
    志雄 "「姑且算是定好了」"
    voice "NCH02A_TO032"
    亨 "「哦，是呢。果然夏天对于我们学生来说是最重要的时间呢」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB01"),"True","img/TO_LAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO033"
    亨 "「那，是什么计划呢？」"
    "亨探出身子，注视着我的脸。"
    志雄 "「总之，准备要和智纱一起出去玩」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAA05"),"True","img/TO_LAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO034"
    亨 "「嘛，那是当然的了。然后呢，决定去哪里玩了没？」"
    志雄 "「去哪里玩啊……也没有特别决定下来。比如看电影啦，去购物啦之类的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB03"),"True","img/TO_LAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO035"
    亨 "「喂喂，这算什么啊。这些和平时做的事情不是没什么区别吗」"
    志雄 "「说起来好像还就是那样」"
    jump L_NCH02A_SEL01_X
label L_NCH02A_SEL01_B:
    志雄 "「没，并没有特别定什么计划」"
    志雄 "「就和去年一样磨磨蹭蹭地度过吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB03"),"True","img/TO_MAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO036"
    亨 "「喂喂，这算什么啊，那种一点干劲都没有的态度」"
    voice "NCH02A_TO037"
    亨 "「好不容易的暑假，什么计划都没有吗？」"
    志雄 "「啊，而且学生会的工作也是不做不行的」"
    "在暑假里也有学生会的事务。"
    if not persistent.dictlist[53] and persistent.show_dict:
        $persistent.dictlist[53]=True
        show screen dict_pop(i=53)
    "再加上，一开学奏云祭也就快到了。去年的奏云祭就麻烦不断，搞得一团糟。"
    "为了今年不变成那样，所以必须从暑假就开始进行准备。"
    志雄 "「在这以外，还有公寓的管理工作吧」"
    "那些已经年久失修的地方，得在这个暑假里安排修理人员修理一下才行呢。"
    jump L_NCH02A_SEL01_X
label L_NCH02A_SEL01_X:
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_INIC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XAA02"),"True","img/TO_XAA02A@2x.png") as lh1 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCH02A_TO038"
    亨 "「你傻啊—！」"
    play sound "SE03_12"
#THREAD_STA 1,THREAD_QUA_WIN
#VIB_DOKA 
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    志雄 "「哇！？」"
#MESA A_CH_SI,"【志雄】「哇！？」"
#THREAD_WAT 1
#WIN_POS 0,0
#VIB_STP 5
#MESX "%K%P"
    "听到了亨突然的叫喊，我不由得从椅子上摔了下来。"
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
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAA04"),"True","img/TO_LAA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO039"
    亨 "「志～雄～，你这个家伙……。这可是高中最后的暑假了吧？　过去的时间可不会再回来的啊？　就那样度过好吗」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB02"),"True","img/TO_LAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO040"
    亨 "「说到夏天，就是那火热的阳光！　衣着暴露的女孩子们！　敞开的心扉！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAA05"),"True","img/TO_LAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO041"
    亨 "「为了发展和女生之间的关系，夏天这个季节可不能不好好利用啊！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB01"),"True","img/TO_LAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO042"
    亨 "「我在这个夏天，为了和莉莉丝的关系变得更好，已经制定了周密的计划」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB02"),"True","img/TO_LAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO043"
    亨 "「已经拿到了摩托车的执照，能带着莉莉丝一起去兜风了啊！」"
    志雄 "「不，可是呢」"
    "我已经有智纱了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB05"),"True","img/TO_LAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO044"
    亨 "「呃，你这个恋爱的赢家」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAA05"),"True","img/TO_LAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO045"
    亨 "「……但是，我认为，你有点大意了」"
    志雄 "「大意？」"
    voice "NCH02A_TO046"
    亨 "「是啊」"
    "亨郑重地点了点头。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAA03"),"True","img/TO_LAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO047"
    亨 "「确实，智纱在你身上投入的精力真不是一星半点」"
    voice "NCH02A_TO048"
    亨 "「每天为了你做便当，为了能一起回家来我们教室！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB03"),"True","img/TO_LAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO049"
    亨 "「考试前把考试范围的要点教给你，明明不是干事还去学生会帮忙……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB05"),"True","img/TO_LAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO050"
    亨 "「而且不只是在学校，休息日还到你家里，给你做饭，给你打扫，等等！」"
    "亨一边掰着手指，一边喋喋不休着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAA03"),"True","img/TO_LAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO051"
    亨 "「要列举智纱的献身行动的话，要多少有多少」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAA05"),"True","img/TO_LAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO052"
    亨 "「但是，与此相对的，你怎么样呢？」"
    志雄 "「怎么样……」"
    "不知道亨想要说些什么，我一时语塞。"
    voice "NCH02A_TO053"
    亨 "「你把现在的状况认为理所当然的，只是单纯地在那里接受，不是吗？　那就是你大意了」"
    志雄 "「那，那种事情……」"
    stop music fadeout 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB03"),"True","img/TO_LAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO054"
    亨 "「这种状态如果就这样一直持续下去的话，总有一天，智纱的心会从你的身边离开的」"
    志雄 "「哎……？」"
    window hide
    hide lh1
#BG_SET_BACK 
#CHR_SET_BACK
#BG_INIC 1
#BG_INIC 2
#BG_PRI 1
#BG_UVC 2,0,512,640,448
#CHR_ALPC 1
#BG_ALPC 0
    show expression "img/BG24EA@2x.jpg" as bg2 zorder 8
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2
#CHR_COLC 2,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC04"),"True","img/CH_LAC04A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
    with dissolve
#CHR_ALPC 2
    stop sound
#BG_BLUR 2
    hide bg1 with dissolve
    play music "OBGM16"
    voice "NCH02A_CH017_K"
    智纱 "「我，已经不能再和你在一起了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA02"),"True","img/CH_LAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH018_K"
    智纱 "「分手吧」"
    window hide
    hide lh2 with dissolve
    "怎，怎么会！？　等等啊，智纱！"
    window hide
    play sound "SE04_20"
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2,(320+96)
#CHR_COLC 2,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA05"),"True","img/CH_MAA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .65
    with move
    voice "NCH02A_CH019_K"
    智纱 "「不要这么随随便便地碰我。还有，不要再那么亲密地喊我智纱了」"
    "为什么会这样！？　我们一起度过的那些日子，都是幻想吗！？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC05"),"True","img/CH_MAC05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH020A_K"
    智纱 "「幻想，{w=3}{nw}"
#MESA A_CH_CH,NCH02A_CH020A_K,"【智纱】「幻想，"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC02"),"True","img/CH_MAC02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH020B_K"
    extend "是这样的呢」"
    window hide
    stop music fadeout 1
    play sound "SE01_00B"
    hide lh2 with dissolve
    "智，智纱－－－－－！！"
    window hide
    play sound "SE08_09L"
    voice "NCH02A_TO055"
    亨 "「喂、志雄！」"
    window hide
    stop se
#BG_PRI 1
#BG_BLUR 2
    scene expression "img/BG07AA3@2x.jpg" as bg0 with dissolve
    hide bg2 with dissolve
#BG_UVC 2,0,0,640,448
#BG_UVC 0,0,512,640,448
    stop se
    stop music fadeout 1
#BG_ALPC 0
#CHR_ALPC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB04"),"True","img/TO_LAB04A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#SE_VOLC 1,255
    hide bg1 with dissolve
    志雄 "「啊！？」"
    "亨的声音，让我回过神来。"
    if not persistent.dictlist[38] and persistent.show_dict:
        $persistent.dictlist[38]=True
        show screen dict_pop(i=38)
    "好险好险，一不小心就想到最坏的方向上去了。而且，在接受智纱告白的公园分手，这种事情太悲惨了。"
#SE_VOLC 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play music "BGM10"
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA05"),"True","img/TO_MAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO056"
    亨 "「总之。为了不会变成那样——」"
    志雄 "「为了不会变成那样？」"
    voice "NCH02A_TO057"
    亨 "「这个暑假里，去海边啊，去露营啊，这类的大型活动果然还是必须有啊！　我、莉莉丝、你、智纱四个人」"
    志雄 "「……为什么会说到那里去了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO058"
    亨 "「由你来邀请的话，智纱一定会很高兴的吧。而且，不觉得那是一种对智纱的报答么？」"
    "嗯～，是那样的吗？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA03"),"True","img/TO_MAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO059"
    亨 "「呐，这挺好的吧。志雄也一起来的话，也比较容易约到莉莉丝的啊」"
    志雄 "「结果，那个就是你的目的吗」"
    "但是对于智纱的情况来说，总觉得亨的说法，也不是没有道理……。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO060"
    亨 "「总之，２２日的芦鹿岛焰火大会，决定就四个人一起去了」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC01"),"True","img/RI_MAC01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter .25
    with move
#ROUTINE_STA
#CHR_POS_AUTOC 0,(320-160),F24,48
#CHR_ALP_AUTOC 0,128,1,F24,48
#CHR_POS_AUTOC 1,(320+160),F24,48
#ROUTINE_STP
    voice "NCH02A_RI003"
    莉莉丝 "「什么？　暑假出去玩的计划？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO061"
    亨 "「对啊。正在说暑假里我和莉莉丝、志雄、智纱四人要不要一起去玩」"
    voice "NCH02A_TO062"
    亨 "「而且，首先是芦鹿岛的焰火大会，一起去怎么样，之类的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC05"),"True","img/RI_MAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_RI004A"
    莉莉丝 "「芦鹿岛焰火大会，吗。{w=4}{nw}"
#MESA A_CH_RI,NCH02A_RI004A,"【莉莉丝】「芦鹿岛焰火大会，吗。"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC02"),"True","img/RI_MAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_RI004B"
    extend "那个很好啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD06"),"True","img/RI_MAD06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_RI005"
    莉莉丝 "「啊，可是，我觉得智纱可能会想和某人两个人单独去看的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD03"),"True","img/RI_MAD03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_RI006"
    莉莉丝 "「智纱也是，最近根本是一点也不陪着我了～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB01"),"True","img/TO_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    "那个难道是因为下课后和休息日智纱都是和我在一起的缘故吗？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD06"),"True","img/RI_MAD06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_RI007"
    莉莉丝 "「啊～啊，有了男人以后女人的友情什么的就没有了看来是真的呢」"
    "莉莉丝的嘴角浮现了一丝微笑。完全被这家伙戏弄了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA06"),"True","img/RI_MAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_RI008"
    莉莉丝 "「还有就是佐贺君，暑假就这么去玩没问题么？　今天的志愿辅导，不是被老师训得相当惨吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB04"),"True","img/TO_MAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO063"
    亨 "「呃」"
    "今天的课程在上午就结束了，下午全班的所有学生一个一个地在志愿辅导室接受了个别面谈。"
    "在这些人里，亨好像是被特别关照的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO064"
    亨 "「‘按现在的成绩无论如何也考不上志愿校’，被这样说了。不觉得很过分吗？」"
    志雄 "「但是，事实是怎样的呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA03"),"True","img/TO_MAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO065"
    亨 "「不过，确实就是那样的啊～。家长也给我定下来了，要去暑期补习的」"
    志雄 "「你的事情可真是麻烦啊……不过我也没法当成没自己的事一样」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA05"),"True","img/RI_MAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "在志愿辅导上被注意，我也是一样的。理由就是因为还没有决定好志愿。"
    志雄 "「到了现在这个时候如果还没决定志愿的话，被老师们盯得紧，那也是当然的了吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA04"),"True","img/RI_MAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_RI009"
    莉莉丝 "「但是，你的成绩也不错了，想去考就能考上的大学，也有不少吧？」"
    志雄 "「可是，也没有什么明确地想要做的事情吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA01"),"True","img/RI_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_RI010"
    莉莉丝 "「不管是谁都是那个样子的吧。就算是那样，大家也都把自己可能合得来的志愿『无意地』决定了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA04"),"True","img/TO_MAA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO066"
    亨 "「就是呢，你这个挑剔的家伙」"
    志雄 "「嗯～……但是那种选择方法，总让人觉得有些随便啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA06"),"True","img/RI_MAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_RI011"
    莉莉丝 "「净在奇怪的地方认真了呢，你这家伙」"
    志雄 "「也不是那样的啦」"
    "说是随便什么的，不过是对优柔寡断的自己的一个借口了。"
    stop music fadeout 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB03"),"True","img/TO_MAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO067"
    亨 "「哈～……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD04"),"True","img/RI_MAD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "我和亨一同叹着气。"
    window hide
    play music "OBGM25"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA06"),"True","img/TO_MAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO068"
    亨 "「志雄。索性，一起退学了，然后去印度吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC05"),"True","img/RI_MAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「什么啊，你非要扯上我干啥啊。再说了为啥是印度？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    if not persistent.dictlist[8] and persistent.show_dict:
        $persistent.dictlist[8]=True
        show screen dict_pop(i=8)
    voice "NCH02A_TO069"
    亨 "「因为稻穗好像就是那样做的」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC06"),"True","img/RI_MAC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 0
    scene expression "img/NIMG01B@2x.png" as bg0 zorder 100 with dissolve
    show expression "img/CloudB1_0@2x.png" as cloud0 zorder 105:
        ycenter .55
        xcenter .75
        linear 500 xcenter .0
    show expression "img/CloudB1_1@2x.png" as cloud1 zorder 105:
        ycenter .55
        xcenter .65
        linear 500 xcenter .0
    show expression "img/CloudB2_0@2x.png" as cloud2 zorder 108:
        ycenter .3
        block:
            xcenter 1.0
            linear 140 xcenter .0
            repeat
    show expression "img/CloudB2_1@2x.png" as cloud3 zorder 108:
        ycenter .2
        block:
            xcenter 1.0
            linear 100 xcenter .0
            repeat
    show expression "img/CloudB2_2@2x.png" as cloud4 zorder 108:
        ycenter .0
        block:
            xcenter 1.0
            linear 120 xcenter .0
            repeat
    show expression "img/CloudB3@2x.png" as cloud5 zorder 110:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.5
            linear 50 xpos .0
            xpos 1.0
            linear 50 xpos .5
            repeat
    show expression "img/CloudB4@2x.png" as cloud6 zorder 112:
        xanchor 1.0
        yalign 1.0
        block:
            xpos .6
            linear 78 xpos .0
            xpos 1.0
            linear 52 xpos .6
            repeat
    show expression "img/CloudB5@2x.png" as cloud7 zorder 115:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.2
            linear 20 xpos .0
            xpos 1.0
            linear 100 xpos .2
            repeat
    with dissolve
#CHR_SET_BACK
#CHR_INIC 4
#CHR_ALPC 4
#CHR_POSC 4
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_XAA06"),"True","img/SN_XAA06A@2x.png") as lh4 zorder (150+4):
        ypos 0.0
    with dissolve
#CHR_ALPC 0
#CHR_ALPC 1
#CHR_ALPC 4
#EFF_PRI 0
#EFF_STAC 0,CLOUD_B,EFF_NOSKIP
#CHR_PRIC 4
#SE_VOLC 1,0
    "稻穗，你这个人呐……。一向是不按常理出牌，不走寻常路的人啊。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_XAB01"),"True","img/SN_XAB01A@2x.png") as lh4 zorder (100+4):
        ypos 0.0
    with dissolve
    if not persistent.dictlist[42] and persistent.show_dict:
        $persistent.dictlist[42]=True
        show screen dict_pop(i=42)
    "姑且来说，澄空应该也是以升学为主的学校。"
    window hide
#BG_INIC 1
#EFF_STPC 0,EFF_SKIP
#EFF_PRI 0
    hide bg0
    hide lh4
    scene expression "img/BG07AA3@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_ALPC 0
#CHR_ALPC 1
#SE_VOLC 1
    stop music fadeout 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA04"),"True","img/RI_MAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_RI012"
    莉莉丝 "「哎？　那不是智纱么」"
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
    window hide
#SE_VOLC 1,255
#BG_OVER_CHRC_F BG08AA,0,CH_LAA01
#BG_BLUR 0
    "随着莉莉丝的声音，向教室门口看去，智纱正站在那里，好像要躲在门后一样。"
    window hide
#SE_VOLC 1
    show expression "img/BG07AA3@2x.jpg" as bg_over zorder 2 with dissolve
    play music "BGM10"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA04"),"True","img/RI_MAA04A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NCH02A_TO070"
    亨 "「这么说来，智纱为什么总是在教室外面等着呢？　进来就好了嘛」"
    志雄 "「她说这不是她自己班的教室，进去还是有点害怕。明明不用那么在意也没关系的啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA06"),"True","img/RI_MAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "反正我和智纱在交往这件事，同学们已经都知道了。"
    志雄 "「可是呢，那个样子才比较像智纱吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB04"),"True","img/TO_MAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO071A"
    亨 "「呜哇，听见了吗莉莉丝！　刚才那种确确实实地『我理解智纱的事情』的发言！{w=7}{nw}"
#MESA A_CH_TO,NCH02A_TO071A,"【亨】「呜哇，听见了吗莉莉丝！　刚才那种确确实实地『我理解智纱的事情』的发言！　"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO071B"
    extend "本来就是夏天了，现在更热了啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD01"),"True","img/RI_MAD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_RI013"
    莉莉丝 "「别嫉妒，别嫉妒。这不是挺好的嘛」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD04"),"True","img/RI_MAD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_RI014"
    莉莉丝 "「喂，志雄你要让智纱等到什么时候啊。赶紧去！」"
    志雄 "「嗯。你不说我也知道」"
    "可是，今天还有学生会的工作，没法和智纱一起回去了。"
    "这样想着，我麻利地把桌子里的学习用品收拾到了书包里，从椅子上站了起来。"
    志雄 "「那，明天见了啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD01"),"True","img/RI_MAD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_RI014A"
    莉莉丝 "「嗯，明天见」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO072"
    亨 "「再见啦」"
    window hide
    stop music fadeout 1
#SE_VOLC 1,255
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NCH02A_TO073"
    亨 "「那，莉莉丝。我们也像往常一样，一起回去吧」"
    voice "NCH02A_RI015"
    莉莉丝 "「我倒是不记得和你一起回去已经到了『和往常一样』的地步呢」"
    voice "NCH02A_RI016"
    莉莉丝 "「不过算了，也没什么理由拒绝掉」"
    voice "NCH02A_TO074"
    亨 "「好嘞！」"
    "那段对话，从后方传来。"
    window hide
#SE_VOLC 1
#BG_OVER_CHRC_F BG08AA,0,CH_LAA01
    scene expression "img/BG08AA@2x.jpg" as bg0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA01"),"True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "BGM03"
    志雄 "「久等了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB05"),"True","img/CH_LAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH021"
    智纱 "「没事，完全没有等」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB01"),"True","img/CH_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "智纱一个劲地摇着头。"
    "……就像是约会碰头时的对话一样。本来就不是什么大不了的事情。"
    志雄 "「那～个。不好意思，今天有学生会的工作，没法一块儿回去了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB02"),"True","img/CH_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH022"
    智纱 "「嗯。我知道的哦」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA01"),"True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH023"
    智纱 "「所以才来帮你处理学生会的工作。」"
    志雄 "「啊，那样啊」"
    志雄 "「我总是受智纱照顾呢。真不好意思」"
    "亨也这么说过，智纱并不是干事，但总是来学生会帮忙。"
    "因此，学生会的全体成员都知道了我和智纱的关系。托了这个的福，总是被春日同学他们戏弄。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA03"),"True","img/CH_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#REEK_CHR 0
    voice "NCH02A_CH024"
    智纱 "「没事，不用在意的！」"
#REMOVE_REEK_CHR 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB01"),"True","img/CH_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH025"
    智纱 "「那么，有没有什么我能做的呢？」"
    志雄 "「没有了，今天没关系的。只有在暑假之前的会议了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB03"),"True","img/CH_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH026"
    智纱 "「这样啊……」"
    志雄 "「对不起。明明你是特地过来的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB04"),"True","img/CH_LAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH027"
    智纱 "「没事，志雄君没有什么需要道歉的！　因为是我自己要来的」"
    "智纱慌忙地摇了摇头。稍稍红着脸，继续说着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB03"),"True","img/CH_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH028"
    智纱 "「还有，就算不一块回去，光是能见到志雄君就已经很高兴了……」"
    "从教室里的同学们那里，感受到了一种微温的视线，听到了「哦～哦～，又开始了哦」那样的玩笑声。"
    "因为就在教室门口的走廊里，所以引人注目也是没有办法的事。"
    志雄 "「啊～、咳。总之」"
    "为了蒙混过去，我故意咳嗽了一声。"
    志雄 "「因为就是这样，今天你先回去吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA01"),"True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH029"
    智纱 "「嗯，就这样」"
    志雄 "「那好，明天见」"
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
    "我和智纱轻轻地挥手告别，在教室前面分开了。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
#FADE_IN 0
    "话虽然这么说……。"
    "智纱今天也像是理所应当似的，要来学生会帮忙。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_PRI 1
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG07AA3@2x.jpg" as bg2 zorder 2 with dissolve
#BG_BLUR 2
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAA03"),"True","img/TO_LAA03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#BG_ALPC 0
#BG_ALPC 2
#CHR_ALPC 0
    hide bg1 with dissolve
    play music "BGM14"
    voice "NCH02A_TO047_K"
    亨 "「确实，智纱在你身上投入的精力真的不是一点半点了」"
    voice "NCH02A_TO048_K"
    亨 "「每天为了你做便当，为了能一起回家来我们教室！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB03"),"True","img/TO_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO049_K"
    亨 "「考试前把考试范围的要点教给你，明明不是干事还去学生会帮忙……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB05"),"True","img/TO_LAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_TO050_K"
    亨 "「而且不只是在学校，休息日还到你家里，给你做饭，给你打扫，等等！」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "智纱真的是为我做了太多的事情。对我现在的生活，有多大的帮助已经不知道了。"
    "但是，时间也是有限的。为我付出的时间越多，智纱自己的时间就越少——。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAD03"),"True","img/RI_LAD03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_RI006_K"
    莉莉丝 "「智纱也是，最近根本是一点也不陪着我了～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAD06"),"True","img/RI_LAD06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_RI007_K"
    莉莉丝 "「啊～啊，有了男人以后女人的友情什么的就没有了看来是真的呢」"
    "虽说，莉莉丝是开着玩笑说的那些话……。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NCH02A_YU000"
    结乃？ "「……学长……学长」"
    "到现在为止都没有特别意识到，莫非智纱她为我做了很多牺牲吗。"
    voice "NCH02A_YU001"
    结乃？ "「……长……学长」"
    "如果是那样的话，对智纱来说真的好吗？"
    voice "NCH02A_YU002"
    结乃？ "「塚本学长」"
    志雄 "「哎？」"
    window hide
    stop music fadeout 1
#BG_INIC 1
#BG_PRI 1
    scene expression "img/BG09AA@2x.jpg" as bg0 with dissolve
    hide bg2 with dissolve
#BG_UVC 0,(640/8),((448/16)*3),(640/2),(448/2)
#BG_UVC 2,0,0,640,448
    stop music fadeout 1
#BG_ALPC 0
#BG_COLC 0,128,128
    hide bg1 with dissolve
    "感到自己的侧腹部被轻轻地捅了一下，我突然回过神来。"
    "在眼前的既不是教室，也不是走廊，而是学生会室。在那里的既不是智纱也不是亨，而是学生会的干事们。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+192)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAC03"),"True","img/YU_LAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "BGM10"
    "在我旁边的春日同学，用略带惊讶的眼神看着我。"
    "刚才捅我侧腹部的好像就是春日同学。"
    voice "NCH02A_YU003"
    结乃 "「什么，是在发呆吗，塚本先輩」"
    "对啊，现在是会议中。不知不觉就想起事情来了。"
    "在学生会室里，正在商量后天要举行的期末典礼和暑假中教室开放日等事项。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAC02"),"True","img/YU_LAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_YU004"
    结乃 "「真是的，打起精神来呀」"
    voice "NCH02A_YU005"
    结乃 "「『学生会长』不听会议这种事，根本没法给其他的干事们做出表率嘛」"
    志雄 "「真的。谢谢你，我会注意的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAC01"),"True","img/YU_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_YU006"
    结乃 "「没事没事，不用谢」"
    "春日同学浮现了带着点恶作剧的微笑。好像是故意为了不让别人注意到，她把音量放得很小。"
    "真是的，让她以这种形式提醒了，都不知道哪边是前辈了。不愧是下期学生会长最有力的候补人。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我重新打起了精神，集中在眼前的会议上。"
    voice "NCH02A_X2000"
    学生会干事 "「……首先，暑假里除了暑假补习之外，还有要进行社团活动的学生等会来到学校。因此我认为，教室的上锁管理可能无法得到贯彻」"
    voice "NCH02A_X2001"
    学生会干事 "「关于这个问题……」"
    志雄 "「关于各部的活动，学生会过于干涉就不好了，因此我认为，教室和备用品这些，就以每个社团为单位，让各部自己去管理」"
    志雄 "「另一方面，从暑假开始之前就要联络各部的部长，通知他们备用品管理的注意事项，例如向学校借用什么之类的情况，一定要贯彻经过部长许可这一点……」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#FADE_OUT 0
    show expression "img/NIMG01C@2x.png" as bg_over zorder 2
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
#FADE_IN 1
    "在那之后，议题一直说到了开学之后的奏云祭，结束的时候天空已经开始有些泛红了。"
    window hide
##EFF_STPC 0,EFF_SKIP
#    show expression "img/NIMG01C@2x.jpg" as bg_over zorder 2 with dissolve
##EFF_STAC 0,CLOUD_C,EFF_NOSKIP
    pause (32/32.0)
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#BG_COLC 0,128,128
    scene expression "img/BG83EA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAA04"),"True","img/YU_MAA04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE05_13L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,(64/4)
    voice "NCH02A_YU007"
    结乃 "「哈……。明明已经傍晚了，一点也没有凉快下来嘛～」"
    "春日同学叹着气。"
    志雄 "「是啊」"
    "空气中还充满着夏天的暑热，只是稍微走几步，皮肤上就已经开始渗出汗水来了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB05"),"True","img/YU_MAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCH02A_YU008"
    结乃 "「哎？　站在校门那里的，不是智纱学姐吗？」"
#REMOVE_REEK_CHR 0
    志雄 "「哎？」"
    "听到了春日同学的话，我向校门的方向望去。"
    window hide
#SE_VOLC 1
#MUS_VOL 64
#BG_SET_BACK 
#BG_INIC 1
#BG_INIC 3
#BG_POSC 1,0,(0-((448/2)+(448/40))),640,448
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH02A")]=True
    show expression "img/EVN_CH02A@2x.jpg" as bg1 zorder 10 with dissolve:
        yalign 1.0
        linear 1 yalign 0.0
    pause (32/32.0)

#BG_POS_SAVEC 1
#BG_POS_SAVEC 3
    hide bg3 with dissolve
#BG_FLG EVN_CH02A
    "在那里，看到了智纱的身影。"
    "为什么智纱会还在学校？　我明明说过今天有学生会的会议让她先回去的……"
    "智纱背靠着柱子，呆呆地望着暮色渐浓的天空。"
    window hide
    hide bg1
#SE_VOLC 1,(64/4)
#MUS_VOL 128
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB02"),"True","img/YU_MAB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    hide bg1 with dissolve
    "春日同学来回地看着智纱和我，噗哧一声一笑。"
    voice "NCH02A_YU009"
    结乃 "「两个人的感情真好啊，我真是羡慕死你们了」"
    hide lh0 with dissolve
#CHR_POSC 0,(320-192)
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_SAB01"),"True","img/YU_SAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .2
    with move
    voice "NCH02A_YU010"
    结乃 "「我好像打扰到你们了，那就先失陪了～」"
    志雄 "「啊，春日同学？」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "春日同学先走掉了。"
    "远远地望见，她好像在校门那里和智纱说了些什么。"
    "目送春日同学回去以后，智纱好像很闲的样子，在看一张像是传单一样的东西。"
    "智纱一副愁眉不展的表情。是在看什么传单呢？"
    "我换下了拖鞋，走出了校舍。"
    window hide
    stop music fadeout 1
#SE_VOLC 1
#BG_SET_BACK 
#BG_INIC 1
##BG_UVC 1,(640/2),((448/8)*3),(640/2),(448/2)
#BG_SWPC 0
#BG_PRI 0
#BG_PRI 1
#BG_UVC 1,0,0,640,448
    scene expression "img/BG06EA@2x.jpg" as bg0 with dissolve
    志雄 "「智纱」"
    window hide
#SE_VOLC 1,(64/2)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAB01"),"True","img/CH_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "BGM03"
    voice "NCH02A_CH030"
    智纱 "「哎？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAB04"),"True","img/CH_MAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH031"
    智纱 "「啊，志雄君」"
    "智纱大概没有注意到我这边，听到我叫她好像有些吃惊。"
    "把手中拿着的传单放进了包里，再转向我这边。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA01"),"True","img/CH_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH032"
    智纱 "「学生会的工作，已经完了吗？」"
    志雄 "「嗯。智纱怎么还在这里呢。我以为你已经回去了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC05"),"True","img/CH_MAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH033"
    智纱 "「啊，那个」"
    "智纱不知为什么，支支吾吾的。就像因为淘气，被家长盯着的小孩子一样。"
    志雄 "「啊……。难道是，在等我出来？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC01"),"True","img/CH_MAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH034"
    智纱 "「嗯」"
    "智纱抬起了低着的头，对我笑了笑。"
    "但是，从放学到学生会的会议开完应该有两个小时以上的时间啊。"
    "还有……。"
    window hide
#SE_VOLC 1
#BG_SET_BACK 
#ROUTINE_STA
#BG_PRIC 0
#BG_INIC 3
    scene expression "img/NIMG01C@2x.png" as bg3 zorder 30 with dissolve
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
#EFF_PRI 0
#CHR_PRIC 0
#EFF_STAC 0,CLOUD_C,EFF_NOSKIP
#ROUTINE_STP
#ROUTINE_STA
#BG_ALP_AUTOC 0,0,1,0
#CHR_ALP_AUTOC 0,0,1,0
#ROUTINE_STP
    "我抬头看了看天空。今天几乎没有云，阳光一直很强烈。如果在这里等着的话，那一定是相当热了。"
    window hide
#SE_VOLC 1,(64/2)
#ROUTINE_STA
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC01"),"True","img/CH_LAC01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
#BG_ALP_AUTOC 0,128,1,0
#CHR_ALP_AUTOC 0,128,1,0
#ROUTINE_STP
#EFF_STPC 0,EFF_NOSKIP
#ROUTINE_STA
    hide bg3 with dissolve
#BG_UVC 0,0,512,640,448
#EFF_PRI 0
#CHR_PRIC 0
#ROUTINE_STP
    志雄 "「对不起，智纱。我要是能早点来的话……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC06"),"True","img/CH_LAC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH035"
    智纱 "「没事的，你有工作，没办法的啊！　而且，我也不是一直在这里等着的」"
    "智纱一个劲地摆着手。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA01"),"True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH036"
    智纱 "「在图书室呆了一会儿，那里有冷气的。我在那里学习来着」"
    志雄 "「哎？　但是今天，图书室是在做暑假前的书架整理，放学后应该就不开放了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA03"),"True","img/CH_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#REEK_CHR 0
    voice "NCH02A_CH037"
    智纱 "「啊，那个！　其、其实我是，图书委员！」"
#REMOVE_REEK_CHR 0
    志雄 "「嘿呀」"
    "我轻轻地把手放在了智纱的头上。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC04"),"True","img/CH_LAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH038"
    智纱 "「啊呜」"
    "当然，不是在拍打她。这种抚摸一般的接触方式，让智纱害羞得脸都红了。"
    志雄 "「不要撒谎嘛。智纱是图书委员什么的，我可从来没有听说过哦」"
    志雄 "「实际上在什么地方？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC05"),"True","img/CH_LAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH039"
    智纱 "「呜呜。志雄君你欺负人」"
    "智纱有些不太愉快地别开了视线。"
    voice "NCH02A_CH040"
    智纱 "「在教室里等了一会儿，估计着会议快结束的时候，就从教室里出来……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC02"),"True","img/CH_LAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH041"
    智纱 "「那以后，就一直在这里等着……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC05"),"True","img/CH_LAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH042"
    智纱 "「因为，我想和志雄君一起回去」"
    "在开始变得发红的空气中，智纱那小声的嘟哝慢慢地溶化了。"
    志雄 "「这样啊……」"
    志雄 "「谢谢你，智纱」"
    "对一直在这里等着我的智纱，『明明你先自己回去就好了』这样的话怎么也说不出口。所以，我把感谢的心情说了出来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA01"),"True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH043"
    智纱 "「不用谢，我是自己想在这等才等下去的啊」"
    "就算那样，我想仍然还是要谢谢你。"
    志雄 "「那，我们回去吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB03"),"True","img/CH_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    智纱 "「啊……"
#MESA A_CH_CH,NCH02A_CH044A,"【智纱】「啊……"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB01"),"True","img/CH_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH044B"
    extend "嗯」"
    "两个长长的影子离开了校门的柱子。手的那部分的影子，连成一片。"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG03EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG03EA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB01"),"True","img/CH_LAB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#SE_VOLC 1,(64/2)
#BG_BLUR 0
#FADE_IN 1
    志雄 "「这么说来，刚才在校门口看的传单是什么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB06"),"True","img/CH_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH045"
    智纱 "「啊—……那个是……」"
    "智纱的脸上，不知怎的浮现了很窘迫的表情。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB01"),"True","img/CH_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    if not persistent.dictlist[39] and persistent.show_dict:
        $persistent.dictlist[39]=True
        show screen dict_pop(i=39)
    voice "NCH02A_CH046"
    智纱 "「志愿调查表啊。下午有志愿辅导」"
    志雄 "「啊，别的班也都在做这个啊」"
    "下午的志愿辅导，大概是对３年级学生所有人都进行了。"
    "可是，智纱一边看着志愿调查表一边在叹气……发生什么事了吗。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA01"),"True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH047"
    智纱 "「那个，志雄君的志愿，怎么样了？　已经决定了吗？」"
    "志愿吗……。"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "打岔":
            $F7=0
        "老实地回答":
            $F7=1
    if F7==0:
        jump L_NCH02A_SEL02_A
    if F7==1:
        jump L_NCH02A_SEL02_B
label L_NCH02A_SEL02_A:
    $F1+=1
    志雄 "「首先，就先说目标是大联盟吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA03"),"True","img/CH_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#REEK_CHR 0
    voice "NCH02A_CH048"
    智纱 "「哎，志雄君，要当棒球选手吗！？」"
#REMOVE_REEK_CHR 0
    志雄 "「别，别，别当真」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA04"),"True","img/CH_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH049A"
    智纱 "「啊，{w=2}{nw}"
#MESA A_CH_CH,NCH02A_CH049A,"【智纱】「啊，"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA01"),"True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH049B"
    extend "那也是呢……」"
    "智纱看上去很安心地叹了口气。再怎么说，也不会做那种无谋的事情。"
    志雄 "「先不说那些，智纱暑假里有什么预定吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA04"),"True","img/CH_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH050"
    智纱 "「预定？」"
    志雄 "「嗯。如果有空的话不一起去哪里玩吗？　比如露营啊」"
    "说到夏天首先想到的要去的地方可能是海或者是游泳池，但是，智纱非常地怕水。去不了和水有关的游玩场所。"
    voice "NCH02A_CH051"
    智纱 "「露营的话，和我一起可以吗？」"
    志雄 "「那是当然的吧。这么说来，除了智纱以外我还能跟谁去呢？」"
    voice "NCH02A_CH052"
    智纱 "「难道是，只有我们两个人？」"
    "啊……虽然还没有考虑到那个份上，不过和智纱两个人去旅行这事可能也不错呢。"
    志雄 "「嗯，是呢」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA06"),"True","img/CH_LAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH053"
    智纱 "「那，那样啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC06"),"True","img/CH_LAC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH054A"
    智纱 "「当，当然是要去的了！{w=5}{nw}"
#MESA A_CH_CH,NCH02A_CH054A,"【智纱】「当，当然是要去的了！　"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC02"),"True","img/CH_LAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH054B"
    extend "啊，但是，能不能去这件事，还是得问问父母亲……」"
    "如果是当日往返那种程度的出行到也就罢了，是去露营的话就自然是要住在外面了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA05"),"True","img/CH_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH055"
    智纱 "「但是我一定要去！　就算不顾父亲和母亲的反对也硬是要去！」"
    志雄 "「嘿」"
    window hide
    play sound "SE07_13"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC04"),"True","img/CH_LAC04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#QUA2_CHR 0
    "我敲了一下智纱的头。"
    志雄 "「硬来可是不行的。如果想去的话，要好好得到父母的许可」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC02"),"True","img/CH_LAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "虽然自己这么说，但还是觉得那个可能会有点困难。"
    "让年轻的女儿和男人在外面一起夜不归宿这种事，对于家长来说，必须做出在寒冬的天气里从悬崖峭壁上跳入海中的那种觉悟。"
    "智纱的表情稍有不满，最后还是点头了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC03"),"True","img/CH_LAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH056"
    智纱 "「……嗯，我知道了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC05"),"True","img/CH_LAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH057"
    智纱 "「如果是和莉莉丝一起去的话，我觉得他们一定不会反对的」"
    "然后这样小声嘟囔了一句。"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "……好了。这样智纱的注意力，就转到暑假的计划上面了。看来是很好地逃离了谈论志愿的话题。"
    "在几乎没有考虑过志愿的现在，还是不怎麽想去触碰这个话题。自己也觉得自己没出息。"
    "但是，暑假出去玩的这个提案，倒不只是为了岔开志愿的话题。"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG07AA3@2x.jpg" as bg2 zorder 2 with dissolve
#BG_BLUR 2
#BG_INIC 1
#BG_PRI 1
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAA01"),"True","img/TO_LAA01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#SE_VOLC 1,0
#MUS_VOL 64
    scene expression "img/BG07AA2@2x.jpg" as bg0 with dissolve
#BG_ALPC 0
#BG_ALPC 2
#CHR_ALPC 0
#CHR_ALPC 1
    hide bg1 with dissolve
    voice "NCH02A_TO058_K"
    亨 "「由你来邀请去玩的话，智纱一定会很高兴的吧。而且，不觉得那就是对智纱的一种报答么？」"
    window hide
#BG_INIC 1
#BG_PRI 1
    scene expression "img/BG03EA@2x.jpg" as bg0 with dissolve
    hide lh1 with dissolve
    hide bg2 with dissolve
#BG_UVC 2,0,0,640,448
#BG_ALPC 0
#CHR_ALPC 0
#SE_VOLC 1,(64/2)
#MUS_VOL 128
    hide bg1 with dissolve
    "亨还真是说中了啊。确实，亨说的可能没错。"
    "如果就是那样的话，觉得在暑假去点平时去不了的地方看看，也许会很不错——。"
#CHR_INIC 0
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC02"),"True","img/CH_LAC02A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCH02A_CH058"
    智纱 "「啊，可是」"
    志雄 "「嗯，什么？　有什么其它的愿望？」"
    "好不容易的暑假，我打算只要有时间就陪着智纱。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA01"),"True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH059"
    智纱 "「那个，也不是那样……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA01"),"True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH060"
    智纱 "「志雄君，备考的学习进展如何？」"
    志雄 "「……」"
    "把话题岔开的作战，看来是以失败告终了。"
    志雄 "「是该说有进展呢，还是该说没有进展呢……」"
    "只能做出一些，模棱两可的回答了。"
    "虽说觉得现在的成绩还算不错，但没有决定好志愿所以应考复习基本没有什么进展。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA02"),"True","img/CH_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH061"
    智纱 "「啊，是这样啊……」"
    "好像是从含混不清的语气中，察觉了我的复习没有进展，智纱有点不高兴的样子。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA03"),"True","img/CH_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#REEK_CHR 0
    voice "NCH02A_CH062"
    智纱 "「不，不过这也是没有办法的呢！　因为志雄君还有学生会的工作，在那之外还做着公寓的管理员呢！」"
#REMOVE_REEK_CHR 0
    "嗯～，可是呢……。"
    jump L_NCH02A_SEL02_X
label L_NCH02A_SEL02_B:
    志雄 "「遗憾的是，我还没有决定自己的志愿。就因为这个，在志愿辅导被要求注意了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC02"),"True","img/CH_LAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "澄空怎么说也是以升学为主的学校，所以班上其他同学都已经定下了目标，针对各自的志愿校开始了备考复习。"
    志雄 "「哇，这话从自己的嘴里一说，更有危机感了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC04"),"True","img/CH_LAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "其实这不是已经相当危险了嘛，我现在的状况。"
    "想抱着脑袋一屁股坐到地上了。"
    志雄 "「其实啊，在这之前，在学生会室里，春日同学也摊着自己的志愿调查表在那里犹豫」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC01"),"True","img/CH_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH063"
    智纱 "「啊，是呢。２年级学生也该在某种程度上决定志愿呢，就是在分文科和理科的时候」"
    志雄 "「就是那样。当她用那种天真无邪的表情来问我能不能跟她商量商量她的志愿的时候，我真觉得自己很失败」"
    "学弟学妹们也已经开始决定志愿了，可是我……。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC06"),"True","img/CH_LAC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH064"
    智纱 "「没，没办法的嘛！　因为志雄君，学生会的工作很忙的，还有公寓的管理工作呢！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA01"),"True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH065"
    智纱 "「因为你做着公寓管理这份工作，所以比起其他人，我觉得志雄君已经超前一步了」"
    "虽说智纱是在夸奖我，因为我知道她是在为我操心，反倒心情更郁闷了。"
    jump L_NCH02A_SEL02_X
label L_NCH02A_SEL02_X:
    "本来，说是公寓的管理工作，其实也没做什么大不了的事。"
    "只是有的时候，会出现有问题的人倒在那里的情况。比如铃。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC01"),"True","img/CH_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH066"
    智纱 "「而且，连我的志愿，也还没有决定下来呢」"
    志雄 "「哎？　是吗？」"
    "意外啊，智纱是个很可靠的人，明明觉得她已经瞄准了自己的志愿，针对考试展开复习了。"
    "因为没有决定自己的志愿，所以不太好说这方面的话题，直到现在也没问智纱的志愿是什么。"
    voice "NCH02A_CH067"
    智纱 "「嗯，是啊」"
    "智纱用力地点了点头。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA05"),"True","img/CH_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH068"
    智纱 "「所以说志雄君，没关系的！」"
    "呼地握紧了双手看着我，智纱好像在陈述事实一样，如是说道。"
    "没关系，吗。智纱是这样对我说的……。"
    "可是，真的没关系吗……。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG01EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG01EA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA01"),"True","img/CH_LAA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE08_17L"
    pause (32/32.0)
#BG_BLUR 0
#FADE_IN 1
#SE_VOLC 1
    voice "NCH02A_CH069"
    智纱 "「所以呢」"
    "走到了澄空车站之后，智纱盯着我的脸，说道。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB03"),"True","img/CH_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH070"
    智纱 "「那个……一起复习怎么样？　我备考的复习，也没有什么进展」"
    "和智纱一起学习吗……。"
    志雄 "「嗯，就这样办吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB02"),"True","img/CH_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH071"
    智纱 "「那，现在就去志雄君的家里！」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "在站前，智纱快速转过了身走了起来，但是被我拉住了。"
#CHR_INIC 0
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB04"),"True","img/CH_LAB04A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    志雄 "「不对，等一下。今天已经晚了，明天开始的话不是更好吗」"
    "虽说夏天白天比较长，但也是早就过了６点。回到家里还来不及学习，就到了该准备晚饭的时间了。"
    voice "NCH02A_CH072"
    智纱 "「那样啊……也是呢」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB06"),"True","img/CH_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH073"
    智纱 "「啊，可是，因为需要做很多的准备，是不是从明天开始比较好……」"
    "智纱自言自语般地说道。"
    "准备？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB01"),"True","img/CH_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH074"
    智纱 "「那么，我得早点回去了」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "智纱又一次更改方向，这次是向着车站检票口的方向走去。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_SAA01"),"True","img/CH_SAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH075"
    智纱 "「明天见」"
    window hide
    stop music fadeout 1
#SE_VOLC 1,255
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "最后说完了这些，智纱快步地通过了检票口。"
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
#label THREAD_QUA_WIN
#TH_QUAKE_WIN 4
#EOT
#label THREAD_RIRISU_KICK
#CHR_POS_AUTOC 0,(320-64),0,1,F133
#CHR_POS_AUTOC 1,0,1,F133
    pause (4/32.0)
#CHR_POS_AUTOC 4,(320-64),0,1,F133
    pause (4/32.0)
#CHR_POS_AUTOC 5,(320-64),0,1,F133
#CHR_POS_SAVEC 0
#CHR_POS_SAVEC 1
#CHR_POS_SAVEC 2
#CHR_ALPC 2
#CHR_POS_SAVEC 3
#CHR_ALPC 3
#CHR_POS_SAVEC 4
#CHR_ALPC 4
#CHR_POS_SAVEC 5
#CHR_ALPC 5
#EOT
#label THREAD_TORU_ZURU
#CHR_POS_AUTOC 1,,(160),1,F123,24
#WAIT2 32
#CHR_POS_AUTOC 1,,(240),1,F123
#CHR_POS_SAVEC 1
#EOT
#label THREAD_SHOES
#CHR_POS_AUTOC 2,(320+110),360,0,F123
#CHR_POS_SAVEC 2
#CHR_ANG_SAVEC 2
#CHR_ANGC 2
#EOT
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT