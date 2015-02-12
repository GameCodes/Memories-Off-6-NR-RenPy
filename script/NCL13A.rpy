label NCL13A:
    $currentlabel = "NCL13A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_BG NIMG15I,CAL_0819
    show expression "img/NIMG15A-568h@2x.jpg" as cal zorder 5
    show expression "img/08_19_SATURDAY@2x.png" as cal_date zorder 6:
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
    scene expression "img/BG33AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBC03"),"True","img/CL_MBC03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_IN 1,128
    play music "OBGM26"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "学姐向父亲吐露心声的第二天。学姐在客厅的电话前踌躇着。"
    志雄 "「冷静些，只是打电话说一下见面的事情.」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBC02"),"True","img/CL_MBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL13X_KU000"
    克罗艾 "「可是……」"
    "学姐不安的目光，一动不动地凝视着电话听筒。好不容易学姐才消除了与母亲说话的犹豫之感。"
    志雄 "「虽然能够理解学姐的心情……」"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "还是让克罗艾学姐自己联系":
            $F7=0
        "提出代替克罗艾学姐联系":
            $F7=1
    if F7==0:
        jump L_NCL13A_SEL00_A
    if F7==1:
        jump L_NCL13A_SEL00_B
label L_NCL13A_SEL00_A:
    志雄 "「我想，还是学姐自己来联系比较好吧。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB05"),"True","img/CL_MBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    克罗艾 "「……」"
    志雄 "「自己不亲自去说的话可是不行的。如果在这里跌倒的话，就无法传递自己真正的心意了哦，学姐。」"
    "可能说得有些过分了吧……"
    "不过……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB04"),"True","img/CL_MBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL13X_KU002"
    克罗艾 "「嗯……」"
    "学姐听了我的话，轻轻地，稍微点了点头。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBC03"),"True","img/CL_MBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "学姐的手伸向电话听筒。我静静地注视着学姐那颤抖的手指。"
    window hide
    play sound "SE02_05"
    pause (24/32.0)
    play sound "SE02_05"
    pause (32/32.0)
    play sound "SE02_05"
    pause (8/32.0)
    play sound "SE02_02L"
    pause (240/32.0)
    play sound "SE02_08"
    voice "NCL13X_KU003"
    克罗艾 "「喂，妈妈……？」"
    jump L_NCL13A_SEL00_X
label L_NCL13A_SEL00_B:
    志雄 "「要我来打吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBC05"),"True","img/CL_MBC05A@2x.png") as lh0 zorder (10+0):
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
    voice "NCL13X_KU004B"
    克罗艾 "「诶！？」"
#THREAD_STP 1
#REMOVE_REEK_CHR 0
    "听了我的话，学姐用惊奇地视线看着我的脸。"
    志雄 "「我来帮学姐打电话过去吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBC02"),"True","img/CL_MBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL13X_KU005"
    克罗艾 "「可是……」"
    "学姐交替地看着我和电话，脸上浮现出困惑的表情。"
    志雄 "「看不见对方的表情确实很令人不安。更何况是到现在为止一直没能好好沟通的人。」"
    "听了我的话，学姐的视线一时之间彷徨了起来。"
    "不过……不久便微微地点了点头。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB04"),"True","img/CL_MBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL13X_KU006"
    克罗艾 "「嗯……果然，还是要自己来打啊。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBC03"),"True","img/CL_MBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "说着，下定决心的学姐把手伸向了电话听筒。"
    "学姐总算是恢复到平时的模样了。"
    jump L_NCL13A_SEL00_X
label L_NCL13A_SEL00_X:
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG81AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG81AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_15L"
    pause (32/32.0)
#FADE_IN 1
    "我们来到了学姐的家门前。学姐从公寓的门口向自家窗户望去，脸上带着一副严肃的表情。"
    window hide
#SE_VOLC 1,(64/2)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBA02"),"True","img/CL_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    克罗艾 "「……」"
#MESEX_A M_NOA,A_CH_KU,NCL13A_KU000,"【クロエ】「……」%K%P"
    "到现在为止一直生活在一起的爸爸姑且不论，学姐和妈妈之间连正常的家庭对话尚不能进行。"
    "现在就吐露心声的话，总有着各种各样的顾虑。学姐表现出的紧张与不安也可以理解。"
    "为了让学姐振作起来，我紧紧握住学姐的手，用尽可能明快的声音向学姐说道。"
    志雄 "「那，咱们进去吧。」"
    voice "NCL13A_KU001"
    克罗艾 "「嗯……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "一直一副严肃表情的学姐微微点了点头，于是我拉着她的手，两个人并肩走进了公寓大门。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG82AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG82AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    "学姐的母亲用笑脸迎接了来访的我们。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB04"),"True","img/CL_MBB04A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NCL13A_EL000"
    爱丽丝 "「欢迎光临，两位。」"
    志雄 "「打扰了。」"
    voice "NCL13A_KU002"
    克罗艾 "「我回来了……」"
    "学姐生硬地说出了问候，学姐的母亲则看起来很高兴的样子。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA02"),"True","img/YS_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL13A_EL001"
    爱丽丝 "「嗯，欢迎回家。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB03"),"True","img/CL_MBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "然而，学姐则是一副不可思议的感觉，稍稍歪了歪头。如果是平时的话，诺艾儿这时肯定会飞奔出来。"
    voice "NCL13A_KU003"
    克罗艾 "「咦，诺艾儿和爸爸呢……？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL13A_EL002"
    爱丽丝 "「他们俩去买东西了呢。」"
    志雄 "「抱歉，让您多费心了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA02"),"True","img/YS_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL13A_EL003"
    爱丽丝 "「啊，不是的。冰箱里确实是快空空如也了……」"
    "对低头致歉的我，学姐的母亲慌忙说道。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL13A_EL004"
    爱丽丝 "「稍等片刻哦，我去给你们泡茶。」"
    "在学姐母亲的催促下，我们坐到了席位上。"
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
#BG_UVC 0,0,((448/4)+512),(640/2),(448/2)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320+224)
#CHR_POSC 1,(320-96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XBC03"),"True","img/CL_XBC03A@2x.png") as lh0 zorder (10+0):
        xcenter (320+224)/640.0
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA03"),"True","img/YS_LAA03A@2x.png") as lh1 zorder (10+1):
        xcenter (320-96)/640.0
        ypos 0.0

#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    
    pause (32/32.0)
#FADE_IN 1
    "一时之间，我们聊着无关紧要的话题。学姐和母亲之间的对话则是稍显生硬。那些言语点滴之间流露出来的，是她们互相在意对方的心情。"
    克罗艾 "「……」"
    爱丽丝 "「……」"
    "不过，今天是为了迈出新的一步而来的。我重新握住了学姐的手。"
    志雄 "「学姐……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XBB04"),"True","img/CL_XBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL13A_KU005"
    克罗艾 "「谢谢，我知道了。」"
    "学姐正襟危坐，转身面朝母亲。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XBC02"),"True","img/CL_XBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL13A_KU006"
    克罗艾 "「……妈妈。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA01"),"True","img/YS_LAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL13A_EL006"
    爱丽丝 "「怎么了？啊，茶还要再来一杯吗？」"
    voice "NCL13A_KU007"
    克罗艾 "「嗯，不是的。今天是，那个，想来道歉的……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA06"),"True","img/YS_LAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL13A_EL007"
    爱丽丝 "「诶？」"
    voice "NCL13A_KU008"
    克罗艾 "「爸爸他，快要康复的那个时候……」"
    "那个时候，学姐的母亲刚刚做好饭，学姐却从家里跑了出来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA03"),"True","img/YS_LAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL13A_EL008"
    爱丽丝 "「啊，那个时候。该道歉的是我呢。自顾自地说了那些话……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XBC03"),"True","img/CL_XBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL13A_KU009"
    克罗艾 "「不是的。那个时候，我所想的其实是其他的事情。」"
    voice "NCL13A_EL009"
    爱丽丝 "「其他事情？」"
    stop music fadeout 1
    voice "NCL13A_KU010"
    克罗艾 "「妈妈，离家出走那天的事情……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA06"),"True","img/YS_LAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    爱丽丝 "「……！」"
#MESEX_A M_NOA,A_CH_EL,NCL13A_EL010,"【エリーズ】「……！」%K%P"
#CHECK_NOWSKIP L_SKIP_FLASH_BACK_00
#RSET F122
#THREAD_STA 1,THREAD_FLASH_BACK2
label L_SKIP_FLASH_BACK_00:
    voice "NCL13A_KU011"
    克罗艾 "「我想起了，那一天的事情。」"
    "学姐低下了头——"
    voice "NCL13A_KU012"
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL10A")]=True
    show expression "img/EVN_CL10A@2x.jpg" as bg1 zorder 100 with dissolve
    克罗艾 "「孤零零一个人，坐在比现在显得更大的桌子前。」"
    "——心如刀割般的声音"
    hide bg1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XBB04"),"True","img/CL_XBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL13A_KU013"
    克罗艾 "「呐，妈妈？我，从那以后，柿子椒和胡萝卜，就再也无法吃下去了……」"
    "话音变得沉重。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA03"),"True","img/YS_LAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL13A_EL011"
    爱丽丝 "「诶……？」"
    "学姐含着泪光郑重地道歉着。说着母亲最擅长的料理自己却无法吃下的事情。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play music "OBGM01"
    voice "NCL13A_KU014"
    克罗艾 "「对不起。可是真的不行。明明是以前最喜欢的。明明只要吃了的话，就能展露出以前的笑容……可是，从那天开始，就再也品尝不出那种美味的感觉了。」"
    "眼泪，终于从学姐的眼眶中滑落。泪滴无力地掉落在桌子上，就像美玉摔碎了一般散成晶莹的微粒。"
    voice "NCL13A_KU015"
    克罗艾 "「无论如何……也不行了！」"
    voice "NCL13A_EL012"
    爱丽丝 "「克罗艾……那种事情……」"
    voice "NCL13A_KU016"
    克罗艾 "「真的好寂寞！一直都是那样寂寞！孤零零一个人……而且，把我一个人扔下，我，我是没人要的孩子吗！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA03"),"True","img/YS_LAA03A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
    hide bg1 with dissolve
    "看过去，坐在学姐正对面的母亲现在也是一副眼泪夺眶欲出的样子。"
    voice "NCL13A_KU017"
    克罗艾 "「所以，我……！」"
    voice "NCL13A_EL013"
    爱丽丝 "「克罗艾……」"
    window hide

#BG_SET_BACK 
#BG_INIC 1
#BG_UVC 1,0,((448/8)+0),(640/2),(448/2)

    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_SWPC 0
    hide bg1 with dissolve
#BG_PRI 1
#BG_PRI 0
    "学姐的母亲走到了学姐跟前，紧紧地抱住了她。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL11A")]=True
    show expression "img/EVN_CL11A@2x.jpg" as bg1 with dissolve
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NCL13A_EL014"
    爱丽丝 "「不是的。不是的哦，克罗艾。你绝对不是没人要的孩子。对不起，对不起！」"
    voice "NCL13A_EL015"
    爱丽丝 "「根本没有去好好考虑你的感受……我，真的是没资格作为一个母亲呢……」"
    voice "NCL13A_KU018"
    克罗艾 "「不是的，才没有这种事。」"
    "学姐更加用力地抱紧了母亲。"
    voice "NCL13A_KU019"
    克罗艾 "「妈妈，一直都记得。不好的人是我……自顾自地钻牛角尖，是我不好！」"
    voice "NCL13A_EL016"
    爱丽丝 "「克罗艾……」"
    "是啊。也许仅仅是缺少这么一个用心交流的契机。"
    "人，总是如此，最重要的东西就挂在嘴边却无法言明。"
    "只因为些许的阴差阳错，微小的契机被命运拨动，人们便有了失败与误解。"
    "可是，只需要稍微地整理一下情绪，利用同样微小的契机，人们也能再度共同欢笑。"
    "想到这些，我的视线就再也没有离开这对相拥而泣的母女。"
    window hide
#FADE_OUT 1
    hide bg1 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320+96)
#CHR_POSC 1,(320-96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC02"),"True","img/CL_LBC02A@2x.png") as lh0 zorder (10+0):
        xcenter .35
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA03"),"True","img/YS_LAA03A@2x.png") as lh1 zorder (10+1):
        xcenter .65
        ypos 0.0

    pause (32/32.0)
#FADE_IN 1
    "那之后两个人说了很多话，直到两人的心情都平静下来。学姐的母亲又再度开口说道。"
    voice "NCL13A_EL017"
    爱丽丝 "「那天，离家出走的我，直接躲回了娘家。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB03"),"True","img/CL_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    if not persistent.dictlist[52] and persistent.show_dict:
        $persistent.dictlist[52]=True
        show screen dict_pop(i=52)
    voice "NCL13A_KU020"
    克罗艾 "「在斯特拉斯堡的外婆那里？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA01"),"True","img/YS_LAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL13A_EL018"
    爱丽丝 "「嗯。还没有带克罗艾回去过呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB02"),"True","img/CL_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL13A_KU021"
    克罗艾 "「嗯，不过，从诺艾儿那里听说了很多。真是个不错的城市呢。」"
    voice "NCL13A_EL019"
    爱丽丝 "「是个十分安静的地方哦。观光客之类的也不怎么来。所以，正好能适当地调整心情。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB03"),"True","img/CL_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL13A_KU022"
    克罗艾 "「调整心情？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA03"),"True","img/YS_LAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL13A_EL020"
    爱丽丝 "「我其实并没有去想爸爸见异思迁之类的。只是，那个时候……发生很多很多事情……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC02"),"True","img/CL_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "说着，学姐母亲的视线落到了手中的茶杯上。"
    voice "NCL13A_EL021"
    爱丽丝 "「其实，本想马上就回来的。不过妈妈她——也就是你外婆，她身体突然恶化，无法动弹。」"
    voice "NCL13A_EL022"
    爱丽丝 "「再之后，发觉了自己怀孕的事情，所以到诺艾儿出生之前都无法离开娘家了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC03"),"True","img/CL_LBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL13A_KU023"
    克罗艾 "「那样的话，联络一下不就好了吗？」"
    voice "NCL13A_EL023"
    爱丽丝 "「确实呢。哪怕联系一次的话……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA06"),"True","img/YS_LAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL13A_EL024"
    爱丽丝 "「不过真的是想回去呢。也担心着留在这边的你，也想让爸爸他见一见新出生的孩子……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC02"),"True","img/CL_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "可是，随着时间的流逝。时机也错过了……"
    voice "NCL13A_EL025"
    爱丽丝 "「妈妈她去世了，之后把事情都整理好，终于可以和你爸爸他取得联系了。之后……」"
    voice "NCL13A_KU024"
    克罗艾 "「之后，就是那天在医院见面了吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA03"),"True","img/YS_LAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL13A_EL026"
    爱丽丝 "「嗯，吓到你了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB04"),"True","img/CL_LBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL13A_KU025"
    克罗艾 "「嗯……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA05"),"True","img/YS_LAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL13A_EL027"
    爱丽丝 "「所以，你才不是没人要的孩子。只是，我直到现在才坦诚面对自己的心……克罗艾？」"
    voice "NCL13A_KU026"
    克罗艾 "「嗯、嗯……」"
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL11B")]=True
    show expression "img/EVN_CL11B@2x.jpg" as bg_over zorder 2 with dissolve
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "学姐一边点着头一边流着眼泪。"
    voice "NCL13A_EL028"
    爱丽丝 "「真的对不起……」"
    voice "NCL13A_KU027"
    克罗艾 "「嗯，嗯……」"
    "学姐心中的阴霾终于消散，变回了淡蓝色的明朗晴空。"
    "而我心中一直下着的雨，也终于停息了。"
    "学姐的母亲再一次温柔地将学姐的头轻轻地搂入怀中。"
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