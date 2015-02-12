label NRI13A:
    $currentlabel = "NRI13A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '29'
    $date = '6'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 6,CAL_0729
    show expression "img/NIMG15F-568h@2x.jpg" as cal zorder 5
    show expression "img/07_21_FRIDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_DEFC 0,BG_BLACK
    play sound "SE05_14L"
    pause (32/32.0)
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
    志雄 "「嗯，嗯……」"
    window hide
#FADE_OUT 0
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG63MA3@2x.jpg" as bg0 zorder 0 with dissolve
#BG_SET_BACK 
#BG_INIC 1
#BG_UVC 1,0,512,640,448
#SE_VOLC 1,128,256
#FADE_IN 1
    hide bg1 with dissolve
    "朦胧的视线中出现了陌生的画面。"
    "这是哪里？……"
    志雄 "「原来如此……」"
    "我和莉莉丝一起旅行来到这里。"
    "从被窝里爬出来，伸了个懒腰。"
    志雄 "「嗯……」"
    "不经意间看到了枕边的时钟。"
    "时钟的指针表示现在已经过了十点。"
    play sound "SE03_28"
    志雄 "「诶……已经这么晚了吗！？」"
    志雄 "「喂，莉莉丝！起床了！」"
    "啊……咦？被子里没有莉莉丝的身影。"
    志雄 "「莉莉丝？你在哪里……？」"
    voice "NRI13A_RI000"
    莉莉丝 "「这边这边，不要叫这么大声啦。」"
    window hide
    stop sound
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MEB01"),"True","img/RI_MEB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM11"
    "莉莉丝从洗手间走了出来，看来她刚去洗脸了。"
    志雄 "「对不起，我睡过头了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MEB04"),"True","img/RI_MEB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI001"
    莉莉丝 "「……？为什么道歉呢？」"
    志雄 "「啊，那个……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MEB01"),"True","img/RI_MEB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI002"
    莉莉丝 "「先别说这个，志雄也去洗个脸吧？再不去食堂的话，就要到中午了。」"
    "咦……她好像不是很生气嘛？"
    window hide
#BG_SET_BACK 
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LED02"),"True","img/RI_LED02A@2x.png") as lh0 zorder (10-1):
        ypos 0.0
    with dissolve
#MUS_VOL 64
#BG_INIC 1
#BG_ALPC 1
    hide bg1 with dissolve
#CHR_ALPC 0
#BG_ALPC 1
#BG_UVC 0,0,512,640,448
#CHR_ALPC 1
    voice "NRI13A_RI003_K"
    莉莉丝 "「你以为现在几点了啊！都是因为你的关系，早上的时间都浪费了！」"
    play sound "SE04_06"
    志雄 "「唔，好疼！」"
#THREAD_STA 1,THREAD_QUA_WIN
#VIB_DOKA 
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESA A_CH_SI,"【志雄】「唔，好疼！」"
#THREAD_WAT 1
#WIN_POS 0,0
#VIB_STP 5
#MESX "%K%P"
    window hide
#BG_INIC 1
#BG_PRI 1
    hide lh1 with dissolve
#BG_UVC 0,0,0,640,448
#CHR_ALPC 0
#MUS_VOL 128
    hide bg1 with dissolve
    "——还以为会这样呢。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MEA01"),"True","img/RI_MEA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI004"
    莉莉丝 "「喂，你在发什么呆啊？快点准备～来，毛巾和牙刷。」"
    志雄 "「啊，啊啊……」"
    "莉莉丝她怎么了……"
    "仿佛就像个理想女友一样。"
    "我疑惑地接过莉莉丝递给我的洗刷用具，朝洗手间走去。"
    window hide
    志雄 "「……那真是莉莉丝吗？」"
    "就算是正午之前她自己起来，也没有生气，还帮我准备洗刷用具。"
    "她的心境到底有了什么变化？气候果然能改变人的性格吗？"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG62AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG62AA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
#FADE_IN 1
    play music  "BGM12"
    voice "EV99_ET002"
    仲居 "「啊，终于起来了吗？」"
    志雄 "「对不起……不知不觉就睡过头了。」"
    voice "EV99_ET003"
    仲居 "「呼呼，没什么好道歉的，好好享受就行。」"
    voice "EV99_ET004"
    仲居 "「对了，你们父母让我告诉你们，他们已经出去了。」"
    志雄 "「是吗，谢谢你。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCC05"),"True","img/RI_LCC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI005"
    莉莉丝 "「那两人真的关系很好呢」"
    window hide
    show expression "img/EXBG05N@2x.jpg" as bg_over zorder 2 with dissolve
    "早饭是米饭、味噌汤、小片的生鱼片以及青菜等典型的和式菜肴。"
    "而且每种菜都很可口，尽管我和莉莉丝都是刚起床，可还是把所有菜都一扫而空了。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG62AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG62AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA01"),"True","img/RI_MCA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (32/32.0)
#FADE_IN 1
    voice "NRI13A_RI006"
    莉莉丝 "「真好吃。果然旅行的乐趣还是在于享受美食。」"
    志雄 "「这里离海边很近，海产比较美味吧？」"
    voice "NRI13A_RI007"
    莉莉丝 "「我家的生鱼片虽然也不差，不过和这里一比嘛……」"
    志雄 "「对了，今天准备去哪儿？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCD01"),"True","img/RI_MCD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI008"
    莉莉丝 "「这里离海很近吧，而且昨天也没去成湖那边……」"
    voice "NRI13A_RI009"
    莉莉丝 "「从车站到这里还有土产店，还可以在那里买些东西。」"
    志雄 "「说的是呢……啊，对了。」"
    "正好说到买东西，再若无其事地问问看她关于生日礼物的事吧。"
    志雄 "「莉莉丝，那个……」"
    "正当我要说出口时，有人插了进来。"
    voice "NRI13A_SN000"
    信？ "「我想在这附近，恐怕是没法游泳的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC05"),"True","img/RI_MCC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「诶？」"
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
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC05"),"True","img/RI_MCC05A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA01"),"True","img/SN_MBA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    "听到熟悉的声音我回过头去，稻穗站在那里。"
    voice "NRI13A_SN001"
    信 "「看来你们在犹豫不知道去哪儿玩吧，年轻人。」"
    voice "NRI13A_RI010"
    莉莉丝 "「啊，是的」"
    voice "NRI13A_RI011"
    莉莉丝 "「那个，不能去海边游泳是为什么呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBB01"),"True","img/SN_MBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI13A_SN002"
    信 "「这边的海域是捕鱼区，可没有海水浴场啊。」"
    voice "NRI13A_SN003"
    信 "「只有市场附近开的海鲜屋超好吃，值得一去呀。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC04"),"True","img/RI_MCC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI012"
    莉莉丝 "「是这样啊……亏我还准备了泳衣呢。」"
    "我想起了在旅行前陪莉莉丝去买泳衣的事。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA06"),"True","img/SN_MBA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI13A_SN004"
    信 "「不过，也用不着垂头丧气啊！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC05"),"True","img/RI_MCC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「诶？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA01"),"True","img/SN_MBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI13A_SN005"
    信 "「虽然海上是不行，可还有其他可以游泳的地方。你们知道山上有湖吧？」"
    志雄 "「嗯，我知道。」"
    "昨天和莉莉丝爬到一半，坡道尽头确实有名为『门亚湖』的大湖。"
    voice "NRI13A_SN006"
    信 "「那个湖是可以游泳的。虽然离这里有一段距离，不过大家都是在那里游泳的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCD01"),"True","img/RI_MCD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI013"
    莉莉丝 "「诶，有这么大吗？」"
    voice "NRI13A_SN007"
    信 "「一眼望去和大海没什么区别，而且在游泳区域还有人工沙滩呢。」"
    志雄 "「那我们去那儿看看吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA01"),"True","img/RI_MCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI014"
    莉莉丝 "「嗯！」"
    "莉莉丝重重地点了点头。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    pause (32/32.0)
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG67AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG67AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_15L"
    pause (32/32.0)
#EFF_STAC 0,SUNLIGHT_BG67_FRONT,EFF_SKIP
#EFF_STAC 1,SUNLIGHT_BG67_BACK,EFF_SKIP
#FADE_IN 1
    play music  "BGM16"
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCB01"),"True","img/RI_MCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI015"
    莉莉丝 "「稻穗也说了，有一段距离呢。」"
    志雄 "「是呢。」"
    "莉莉丝并没有显得特别疲倦，依旧步履轻盈地走着。"
    "她的包比我要稍稍鼓一些，看来带了不少东西。"
    志雄 "「你在包里放了些什么东西？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCD01"),"True","img/RI_MCD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI016"
    莉莉丝 "「啊，这个？……嗯，各种杂物吧。」"
    志雄 "「各种杂物？」"
    "除了便携水壶和泳衣以外，应该没有别的东西了吧……"
    "说起来，莉莉丝在出门准备的时候，还小心翼翼地把那个护身符塞进包里了。"
    voice "NRI13A_RI017"
    莉莉丝 "「那个～防晒油之类的东西。保护皮肤很重要呀。」"
    志雄 "「重吗，我来拿吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA03"),"True","img/RI_MCA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI018"
    莉莉丝 "「嗯嗯，没关系！不必在意！」"
    "莉莉丝面向我，像是要护着包一样。"
    "……？她怎么了？"
    "往常的话，根本不用我说出口，她也会让我拿的。"
    voice "NRI13A_RI019"
    莉莉丝 "「好了，快走啦！」"
    志雄 "「啊啊」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#EFF_STPC 0,EFF_SKIP
#EFF_STPC 1,EFF_SKIP
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    show expression "img/BG77AA1@2x.jpg" as bg0 zorder 0 with dissolve
    hide bg1 with dissolve
    "这之后又走了一阵……"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG70AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG70AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_12"
    pause (32/32.0)
#FADE_IN 1
    if not persistent.dictlist[50] and persistent.show_dict:
        $persistent.dictlist[50]=True
        show screen dict_pop(i=50)
    志雄 "「哈……真累啊……」"
    "话说回来，莉莉丝还真是有精神啊。竟然毫无倦态，如风般走进了更衣室。难道是我太缺乏锻炼吗？"
    "我在更衣室换好衣服，现在正在等莉莉丝。"
    "这样等着真是无聊啊……"
    "环顾周围，就像稻穗所说的那样，还有很多来客在游泳。"
    voice "NRI13A_RI020"
    莉莉丝 "「志雄！久等了！」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_INIC 3
#BG_PRI 1
#BG_PRI 3
#BG_POSC 1,0,(448*-1),640,448
    show expression "img/NIMG18A@2x.jpg" as bg1 zorder 1:
        yalign 1.0
        linear 1.5 yalign 0.0
    with dissolve
#BG_ALPC 1
#BG_ALPC 3
#FADE_IN 1
    play music  "BGM02"
#BG_COL_AUTOC 1,128,128,128,128,0,F24
#BG_COL_SAVEC 1
    pause (64/32.0)
#EFF_STAC 0,LATHER,EFF_SKIP
#BG_POS_AUTOC 1,,F24,256
#BG_POS_SAVEC 1
    pause (64/32.0)
#EFF_STPC 0,EFF_SKIP
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    hide bg1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDB07"),"True","img/RI_MDB07A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    "啊……"
    voice "NRI13A_RI021"
    莉莉丝 "「怎、怎么样？」"
    志雄 "「哎，那个，怎么说呢……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDA05"),"True","img/RI_MDA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI022"
    莉莉丝 "「合适吗？当然合适吧！？」"
    "那个，即使你不用这样威胁我也已经很——"
    志雄 "「我觉得很合适。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDC02"),"True","img/RI_MDC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI023"
    莉莉丝 "「哈，太好了……」"
    "虽然买东西的时候我也一起去选了，可莉莉丝试穿的样子是绝对不可能看到的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDA03"),"True","img/RI_MDA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI024"
    莉莉丝 "「等，等一下……你看得入迷我是能理解，可你也不要老是盯着我看嘛！」"
    志雄 "「不是这样……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDA02"),"True","img/RI_MDA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI025"
    莉莉丝 "「……呼」"
    "莉莉丝的脸比刚才更红了。我也和她差不多……"
    志雄 "「去游泳吧？」"
    voice "NRI13A_RI026"
    莉莉丝 "「是、是呢……啊」"
    voice "NRI13A_RI027"
    莉莉丝 "「志雄的泳衣，也很合适哟～」"
    志雄 "「哦、哦」"
    "在旁人看来简直笨蛋一样害羞着的我，为了掩饰这一点，快步走向了湖那里。"
    window hide
#FADE_OUT 1
    play sound "SE03_77"
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/BG92AA@2x.jpg" as bg0 with dissolve
#EFF_STAC 0,TWINKLE,EFF_SKIP
#FADE_IN 1
    "远远望去湖面与天际交于一线，近看湖水清亮喜人。"
    志雄 "「看上去真的和大海没什么区别呢。」"
    voice "NRI13A_RI028"
    莉莉丝 "「不过，这水一点都不咸。看！」"
    window hide
#BG_SET_BACK 
#BG_INIC 3
#BG_ALPC 3
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI07A")]=True
    show expression "img/EVN_RI07A@2x.jpg" as bg3 zorder 3 with dissolve
    play sound "SE03_56"
#BG_ALP_AUTOC 3,128,0,F24,48
#BG_ALP_SAVEC 3
    志雄 "「哇！？」"
    voice "NRI13A_RI029"
    莉莉丝 "「啊哈哈。怎么样？不咸吧？」"
    志雄 "「真的……莉莉丝，你也尝尝吧！」"
    window hide
#BG_SET_BACK
#ROUTINE_STA
#BG_PRIC 1
#BG_PRIC 3
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI07B")]=True
    show expression "img/EVN_RI07B@2x.jpg" as bg1 zorder 1 with dissolve
#BG_UVC 3,(640/2),(448/2),(640/2),(448/2)
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI07B")]=True
    show expression "img/EVN_RI07B@2x.jpg" as bg3 zorder 3 with dissolve
#ROUTINE_STP
#BG_UV_AUTOC 3,(640/3),(448/8),(640/2),(448/2),0,F24
    pause (32/32.0)
#BG_ALP_AUTOC 3,0,0,F24,48
    play sound "SE03_57"
    hide bg3 with dissolve
    voice "NRI13A_RI030"
    莉莉丝 "「哇！好冷！」"
    voice "NRI13A_RI031"
    莉莉丝 "「你这家伙！这样的话！」"
    window hide
    play sound "SE03_59"
    hide bg1 with dissolve
    "什么啊，莉莉丝这家伙竟然潜到水里去了……"
    志雄 "「哦！？」"
    "脚好像碰到什么东西了。水中浮现出莉莉丝的身影。"
    志雄 "「哦，啊，啊啊……！」"
    "脚被抓住，我失去了平衡——"
    window hide
    play sound "SE03_60"
#FADE_OUT_STA 32
#QUA_ALL 
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/OIBG010A@2x.png" as bg1 zorder 1 with dissolve
#EFF_STAC 0,SHAKE_WATER,EFF_NOSKIP
#FADE_IN 1
#SE_WATC 1
    play sound "SE03_61"
    play sound "SE03_87"
#BG_SET_BACK
#EFF_STPC 0,EFF_SKIP
    hide bg1 with dissolve
    window hide
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI07A")]=True
    show expression "img/EVN_RI07A@2x.jpg" as bg1 with dissolve
    志雄 "「唔哈！」"
    voice "NRI13A_RI032"
    莉莉丝 "「啊哈哈哈∥」"
    "看到我被水呛的样子，莉莉丝大笑起来。"
    志雄 "「咳……莉莉丝，你太过分了」"
    voice "NRI13A_RI033"
    莉莉丝 "「哈哈哈，对不起对不起。你摔得太华丽了，就像漫画里一样。哈哈哈。」"
    志雄 "「唔，那我也……！」"
    "我把手伸向莉莉丝。"
    window hide
    play sound "SE03_59"
    hide bg1 with dissolve
    "可是，莉莉丝轻巧地躲开后，潜到了水里。"
    "下一刻，在和我有一段距离的地方，莉莉丝的头从水中冒了出来。"
    play sound "SE03_87"
    "莉莉丝这家伙，比我游得还好……"
    voice "NRI13A_RI034"
    莉莉丝 "「哼哼～！我不会这么容易被抓住的～『澄空之人鱼』的名号可不是浪得虚名的！」"
    志雄 "「我可是第一次听说。」"
    voice "NRI13A_RI035"
    莉莉丝 "「啊哈哈哈～」"
    "可恶……这样的话，就算是为了争这口气，我也要把她弄倒！"
    "正当我在考虑这件事的时候，突然感到尿急。"
    志雄 "「停！暂时休战！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDA01"),"True","img/RI_MDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI036"
    莉莉丝 "「什么？」"
    志雄 "「我去下厕所……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDA05"),"True","img/RI_MDA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI037A"
    莉莉丝 "「唔，你真煞风景……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDB04"),"True","img/RI_MDB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI037B"
    extend "那我就在这附近游游泳好了。」"
    志雄 "「哈哈，对不起。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDD04"),"True","img/RI_MDD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI038"
    莉莉丝 "「志雄，要快点回来哦？我可不想再被搭讪了。」"
    志雄 "「被搭讪的话，就像人鱼一样逃走吧。」"
    show expression "img/BG70AA@2x.jpg" as bg_over zorder 2 with dissolve
    "我苦笑着游上了沙滩。"
    window hide
    stop music fadeout 1
    show expression Solid("000") as bg0 zorder 100 with fade
#FADE_OUT 1
    pause (32/32.0)
    stop music fadeout 1
    hide bg0 with dissolve
#FADE_IN 1
    "回到沙滩的我回顾了下四周。"
    "嗯……莉莉丝在哪儿呢？"
    voice "NRI13A_RI039"
    りりす？ "「那、那个，我有男朋友的！」"
    志雄 "「！？」"
#MESEX_A M_NOA,A_CH_SI,"【志雄】「！？」%K%P"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SDB04"),"True","img/RI_SDB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "OBGM14"
    "此时莉莉丝正在被两个男人围着。那两个男的大概是大学生吧，皮肤有点被晒黑的样子，嘿嘿地傻笑着。"
    voice "NRI13A_RI040"
    莉莉丝 "「所、所以说，你们这样我很困扰……」"
    voice "NRI13A_XE000"
    男Ａ "「这不是很好嘛，我们只是邀请你一起玩而已嘛～」"
    voice "NRI13A_XF000"
    男Ｂ "「要不然，叫你男朋友也一起来吧。」"
    voice "NRI13A_RI041"
    莉莉丝 "「那个，请不要这样……」"
    "莉莉丝因为身材娇小，两个男人完全是呈俯视的状态。"
    "面对那种家伙，像往常一样把他们踢飞不就行了。"
#MESEX_A M_NOA,A_CH_RI,NRI13A_RI042,"【りりす】「……」%K%P"
    "可是，莉莉丝连头都不敢抬，惊恐地蜷缩着身体。"
    志雄 "「真拿她没办法……」"
    window hide
#CHR_SORT 1
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XDC04"),"True","img/RI_XDC04A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
#MOV_CHR_INIT 32
#MOV_CHR0 0
#MOV_CHR1 128
#MOV_FOCUS_BG 512
#MOV_CHR_GO 0
    hide lh0
    with dissolve
    志雄 "「喂～莉莉丝～」"
    voice "NRI13A_XE001"
    男Ａ "「啊？」"
    voice "NRI13A_XF001"
    男Ｂ "「什么？谁啊？」"
    志雄 "「不好意思，我就是她的男朋友。」"
    志雄 "「走了，莉莉丝～」"
    voice "NRI13A_RI043"
    莉莉丝 "「嗯、嗯……」"
    window hide
    stop music fadeout 132
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我拉着莉莉丝的手，把她从那两个人之间带了出来。"
    voice "NRI13A_XE002"
    男Ａ "「原来是男朋友啊，真没劲。找别的吧，别的。」"
    voice "NRI13A_XF002"
    男Ｂ "「嘛，我对那种像孩子般的女孩也没什么兴趣。难得她的泳衣还算比较可爱。」"
    "把莉莉丝带出来之后，听到身后猥琐的笑声。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LDC04"),"True","img/RI_LDC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI044"
    莉莉丝 "「……呜……」"
    志雄 "「那些家伙……！」"
    voice "NRI13A_RI045"
    莉莉丝 "「等一下！」"
    "正当我想折返的时候，莉莉丝抓住我的手臂阻止了我。"
    voice "NRI13A_RI046"
    莉莉丝 "「算了，我们走吧。」"
    志雄 "「……嗯，莉莉丝这么说的话，那就算了吧。」"
    "也许莉莉丝不想引起大骚动吧。"
    "虽然一瞬间头脑发热，不过继续和他们纠缠下去，也只是自找麻烦而已。"
    window hide
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    hide bg1 with dissolve
    stop music fadeout 1
    "离开那两个男人后，莉莉丝安心地叹了口气。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDA06"),"True","img/RI_MDA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM13"
    voice "NRI13A_RI047"
    莉莉丝 "「哈……真是太倒霉了……」"
    志雄 "「像平时对付我一样，用你擅长的踢腿教训他们不就行了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDA05"),"True","img/RI_MDA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI048"
    莉莉丝 "「怎、怎么可能！当时我真是害怕极了……！」"
    "莉莉丝身体微微颤抖了一下。"
    "也难怪……在莉莉丝看来，她是被两个身高马大的男人围住的状态。"
    "而且事实上，莉莉丝并非是十分刚强的人……虽说不上是怕见生人，可面对不认识的人，还是有些害怕的吧。"
    志雄 "「快忘了吧，别再在意了。」"
    志雄 "「仔细想想，那个……你也是因为可爱才被搭讪的吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDC01"),"True","img/RI_MDC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI049"
    莉莉丝 "「嗯，没事的……」"
    "说完，莉莉丝抬头看着我。无助的眼神中充满了不安。"
    voice "NRI13A_RI050"
    莉莉丝 "「志雄不是说了嘛，这件泳衣很适合我。所以……没事的。」"
    志雄 "「……」"
#MESEX_A M_NOA,A_CH_SI,"【志雄】「……」%K%P"
    "我轻轻握住莉莉丝的手。"
    志雄 "「很合适哟，莉莉丝。」"
    "我又说了一次。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDC02"),"True","img/RI_MDC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI051"
    莉莉丝 "「……嗯。」"
    "我可爱的女朋友再次对我露出了微笑。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDA01"),"True","img/RI_MDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI052"
    莉莉丝 "「好的！」"
    "莉莉丝的声音终于回归到往常一般的开朗。"
    window hide
    play sound "SE03_62"
    "啪啪轻拍着自己的脸回复精神的莉莉丝，微笑着站了起来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDD01"),"True","img/RI_MDD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI053"
    莉莉丝 "「那么，这次我们来比比看谁游得远！」"
    志雄 "「啊，喂！　……真是的，真拿她没办法……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XDB01"),"True","img/RI_XDB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 32
#MOV_CHR0 0
#MOV_CHR1 128
#MOV_CHR_GO 0
    hide lh0 with dissolve
    play sound "SE01_16L"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "莉莉丝抓住我的手，拉了起来。我跌跌撞撞地和莉莉丝一起跳入了湖中。"
    voice "NRI13A_RI054"
    莉莉丝 "「目标是横渡这座湖！」"
    志雄 "「怎么可能！」"
    window hide
    stop se fadeout 1
#BG_SET_BACK 
#FADE_OUT 1
    scene expression "img/NIMG01B@2x.png" as bg_over zorder 2
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
#FADE_IN 1
    "虽然横渡这座湖是不可能的，不过我们两个还是游了很远。"
    window hide
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    scene expression "img/BG70AA@2x.jpg" as bg_over zorder 2 with dissolve
#FADE_IN 1
    stop se
    stop music fadeout 1
    pause (32/32.0)
    play sound "SE05_12"
    stop music fadeout 1
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LDA06"),"True","img/RI_LDA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM12"
    voice "NRI13A_RI055"
    莉莉丝 "「哈，好累啊～」"
    "上岸后的莉莉丝大大叹了口气。"
    志雄 "「确实累了，肚子也有点饿了。去哪儿买点东西吃吧。」"
    "环顾周围，沙滩的一端正好有家小店，那里肯定有卖什么吃的东西吧。"
    志雄 "「莉莉丝要吗？　饮料之类的。」"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,RI_LXC03,2,F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LDC03"),"True","img/RI_LDC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NRI13A_RI056"
    莉莉丝 "「啊！　等一下。」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
#BG_PRI 3
    志雄 "「嗯？　怎么了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LDC01"),"True","img/RI_LDC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI057"
    莉莉丝 "「那样的话，我去吧。你在这里等着」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LDD01"),"True","img/RI_LDD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI058"
    莉莉丝 "「听好了？　你就呆在这里？　不要一个人跑去买！」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "莉莉丝叮嘱了我好几次，然后跑去了别的地方。"
    "……？　莉莉丝，你到哪儿去了呢？"
    "刚才肚子就饿扁了，稍微有些难受……"
    "可是，她既然这么叮嘱我……也没办法。就按她说的在这里等吧。"
    window hide
#MUS_VOL 255
#FADE_OUT 1
#FADE_IN 0
    "…………"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128
#MUS_VOL 128
#FADE_IN 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    with fade
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LDD01"),"True","img/RI_LDD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI059"
    莉莉丝 "「久等了！」"
    志雄 "「你去哪儿了？」"
    voice "NRI13A_RI060"
    莉莉丝 "「给。这个！」"
    "莉莉丝硬是把手里用布包着的东西塞给了我。"
    志雄 "「……？」"
#MESEX_A M_NOA,A_CH_SI,"【志雄】「……？」%K%P"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LDB02"),"True","img/RI_LDB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI061"
    莉莉丝 "「便当……」"
    "便当？"
    志雄 "「哎！？　难道这是莉莉丝做的吗？」"
    voice "NRI13A_RI062"
    莉莉丝 "「嗯。向旅馆的人借用了厨房做的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LDD04"),"True","img/RI_LDD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI063"
    莉莉丝 "「什、什么嘛，你不要…吗？」"
    voice "NRI13A_RI064"
    莉莉丝 "「不、不要的话，也没关系！　那你就去吃小店里卖的东西好了！」"
    志雄 "「不不，当然要咯！　不要随便决定我的想法。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LDD01"),"True","img/RI_LDD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "想要把便当收起来的莉莉丝急忙停止了动作。"
    志雄 "「我只是有点吃惊而已……」"
    "……啊，是吗，难道莉莉丝比我早起就是为了这个吗？"
    voice "NRI13A_RI065"
    莉莉丝 "「那就在这里吃午饭吧。」"
    "莉莉丝不仅做好了便当，还带来了野餐用的布，把它铺在沙滩上。"
    "莉莉丝的包比较鼓，就是便当和野餐布所造成的吧。"
    "这样的话，早点告诉我不就好了。"
    "……不过，她一定是为了给我一个惊喜，才这么做的。"
    "就算是我，也能想到这点。"
    志雄 "「……谢谢你，莉莉丝。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LDA02"),"True","img/RI_LDA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI066"
    莉莉丝 "「也、也不是什么大不了的事啦，便当而已。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LDB01"),"True","img/RI_LDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI067"
    莉莉丝 "「那么，我们快点吃吧。我的肚子也饿了。」"
    志雄 "「噢噢。」"
    window hide
#BG_SET_BACK 
#FADE_OUT 1
    scene expression "img/NIMG01B@2x.png" as bg_over zorder 2
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
#BG_SET_BACK
#EFF_STAC 0,CLOUD_B,EFF_NOSKIP
#FADE_IN 1
    "便当的话是考验烹饪手艺的。这种东西即使不是新鲜出炉的，也要非常好吃才算合格。"
    "我刚开始一个人生活的时候也尝试过好几次，可就是做不好。"
    "可是，莉莉丝做的便当却很好吃。"
    window hide
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    scene expression "img/BG70AA@2x.jpg" as bg_over zorder 2 with dissolve
#BG_UVC 0,0,(448/2),(640/2),(448/2)
#FADE_IN 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XDA01"),"True","img/RI_XDA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    志雄 "「呼……我吃饱了，很好吃。」"
    "面对着被扫荡一空的便当和为我做便当的莉莉丝，我双手合十。"
    voice "NRI13A_RI068"
    莉莉丝 "「粗茶淡饭而已。」"
    志雄 "「有这般手艺的话，马上就能继承『富美』了吧？」"
    voice "NRI13A_RI069"
    莉莉丝 "「呼呼。这些都是婆婆教我的，好吃是理所当然的咯。」"
    "莉莉丝有些自豪地挺起胸膛。"
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    menu:
        "莉莉丝会是个贤惠的妻子的":
            $F7=0
        "莉莉丝会是个优秀的女掌柜的":
            $F7=1
    if F7==0:
        jump L_NRI13A_SEL00_A
    if F7==1:
        jump L_NRI13A_SEL00_B
label L_NRI13A_SEL00_A:
    志雄 "「莉莉丝一定会成为一个贤惠的妻子的」"
#BG_SET_BACK 
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XDC03"),"True","img/RI_XDC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NRI13A_RI070"
    莉莉丝 "「什！？」"
#REMOVE_REEK_CHR 0
#REEK_CHR 0
    voice "NRI13A_RI071"
    莉莉丝 "「什什什、什么……」"
#REMOVE_REEK_CHR 0
    志雄 "「料理这么拿手，而且很重视家庭吧？」"
    "都是受到富美子婆婆的影响吧。"
    "只不过，早上起不来床以及那条件反射的踢腿，与贤妻的形象相去甚远啊。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XDC06"),"True","img/RI_XDC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI072"
    莉莉丝 "「那、那个……」"
    voice "NRI13A_RI073"
    莉莉丝 "「我，我想再去游一下。饭也吃饱了，也休息得差不多了。」"
#BG_GET_NOC 0,F24
    "莉莉丝慌忙把便当盒抱上站了起来。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDB02"),"True","img/RI_MDB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    莉莉丝 "「……」"
#MESEX_A M_NOA,A_CH_RI,NRI13A_RI074,"【りりす】「……」%K%P"
    "然后回头看了我一眼……"
    voice "NRI13A_RI075"
    莉莉丝 "「那，那我走了！　志雄在这里休息就行了！」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "莉莉丝涨着比刚才更红的脸，向湖边跑去。"
    志雄 "「喂。不要这么急，小心摔倒！」"
    voice "NRI13A_RI076"
    莉莉丝 "「没，没关系的——」"
    play sound "SE04_32"
    "话音未落，脚就被绊了一下摔了个大跟斗。"
    "又犯老毛病了……"
    window hide
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LDC04"),"True","img/RI_LDC04A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    志雄 "「喂，莉莉丝！　不要紧吧！？」"
    "我急忙跑向莉莉丝，莉莉丝皱着眉头，很疼的样子。"
    voice "NRI13A_RI077"
    莉莉丝 "「好疼……没、没关系」"
    志雄 "「脚没有扭伤吧？」"
    voice "NRI13A_RI078"
    莉莉丝 "「那个……应该没受伤。」"
    window hide
#CHR_INIC 1
#CHR_ALPC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDB01"),"True","img/RI_MDB01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#ROUTINE_STA
#CHR_ALP_AUTOC 0,0,1,F24,48
#CHR_ALP_AUTOC 1,128,1,F24,48
#BG_BLUR 0
#ROUTINE_STP
    hide lh0 with dissolve
    "像是为了证实自己没事，莉莉丝站了起来……嗯，似乎是没受伤。"
    志雄 "「真是的，不要这么慌张嘛。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDA05"),"True","img/RI_MDA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI079"
    莉莉丝 "「我、我知道啦」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDC04"),"True","img/RI_MDC04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI080"
    莉莉丝 "「真是的……本来就是因为志雄说什么贤妻之类的话……对象不就是你吗……」"
    志雄 "「嗯？　你说什么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDD04"),"True","img/RI_MDD04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI081"
    莉莉丝 "「不，没什么。」"
    "莉莉丝的语气有些不高兴。"
    "……？　为什么会生气呢？　我说了什么会惹她生气的话吗……？"
    志雄 "「刚吃完就运动会肚子疼的，多休息一下再去比较好吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDA04"),"True","img/RI_MDA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI082B"
    莉莉丝 "「……嗯，我知道了。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#ROUTINE_STA
#BG_INIC 1
#BG_ALPC 1
#BG_UVC 1,0,(448/2),(640/2),(448/2)
    show expression "img/BG70AA@2x.jpg" as bg1 zorder 1 with dissolve
#ROUTINE_STP
#BG_ALP_AUTOC 1,128,0,1
#BG_UVC 0,0,(448/2),(640/2),(448/2)
    hide bg1 with dissolve
#BG_BLUR 0
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XDA04"),"True","img/RI_XDA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#CHR_ALP_AUTOC 0,128,0,F24
#CHR_ALP_SAVEC 0
    "莉莉丝再次坐到了野餐布上。她的表情有少许不快。"
    "……现在还是说一些别的话题比较好。"
    jump L_NRI13A_SEL00_X
label L_NRI13A_SEL00_B:
    $F0-=1
#RSET F83
    志雄 "「莉莉丝一定会成为一个优秀的女掌柜的」"
    voice "NRI13A_RI083"
    莉莉丝 "「嗯，会吧。总有一天我会继承『富美』的。」"
    "是呢……虽然富美子婆婆希望莉莉丝去读短期大学，不过最后莉莉丝一定会回来继承『富美』成为女掌柜的。"
    "那时我会怎么样呢……"
    "帮莉莉丝一起经营『富美』？　还是做别的工作呢？"
    "虽然现在还不知道……"
    "看着在我眼前整理便当盒的，我青梅竹马的恋人，我开始思考起自己的将来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XDD01"),"True","img/RI_XDD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「啊，对了。」"
    voice "NRI13A_RI085"
    莉莉丝 "「嗯？　什么？」"
    jump L_NRI13A_SEL00_X
label L_NRI13A_SEL00_X:
    志雄 "「莉莉丝觉得最近的生活有情趣吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XDD04"),"True","img/RI_XDD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI086"
    莉莉丝 "「……？　什么情趣啊，那么突然？」"
    志雄 "「情趣就是情趣啊。只是平平淡淡地度过每天不是很乏味吗。那是为了让生活更快乐而存在的东西……」"
    "我的意思似乎没有传达到莉莉丝心里，她皱起双眉露出惊讶的表情。"
    "啊，真是的！　就算是想知道莉莉丝的生日礼物想要什么，也不至于让她直接说出来吧。"
    "离开旅馆之前，由于稻穗的突然出现使得我没问出口。"
    "然后就需要再找借口询问，我对自己这不争气的脑子感到十分懊悔。就没有什么能若无其事地问出她喜欢的东西的方法吗！？"
    "可恶，这样的话，就只能开门见山地问了！"
    志雄 "「那个，总之，现在你有什么想要的东西吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XDB04"),"True","img/RI_XDB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI087"
    莉莉丝 "「想要的东西呢……现在肚子也填饱了……」"
    voice "NRI13A_RI088"
    莉莉丝 "「你之前也问过相同的问题，有什么事吗？」"
    志雄 "「不，也没什么特别的意义，只是有些兴趣罢了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XDD04"),"True","img/RI_XDD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI089"
    莉莉丝 "「唔。不知道你在想些什么。」"
    志雄 "「好了啦。总之你有什么想要的东西吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XDD05"),"True","img/RI_XDD05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI090"
    莉莉丝 "「想要的东西呢……」"
    voice "NRI13A_RI091A"
    莉莉丝 "「嗯～……{w=3}{nw}"
#MESA A_CH_RI,NRI13A_RI091A,"【りりす】「嗯～……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XDD01"),"True","img/RI_XDD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI13A_RI091B"
    extend "也没什么。」"
    "莉莉丝不假思索就若无其事地给出了答案。"
    "没有……。没有想要的东西、吗……？真的吗？"
    "可真是这样的话，我究竟该送她什么呢？"
    "嗯～……"
    window hide
#BG_SET_BACK 
#FADE_OUT 1
    scene expression "img/NIMG01B@2x.png" as bg_over zorder 2
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
#FADE_IN 1
    voice "NRI13A_RI092"
    莉莉丝 "「哈……真舒服。运动了这么长时间，已经累得散架了。」"
    "莉莉丝躺在餐布上，四肢伸展开来。"
    "这之后我们没有再去游泳，两人就躺在餐布上度过了剩余的时间。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
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
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT