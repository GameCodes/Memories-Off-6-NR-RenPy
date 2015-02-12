label NCL07A:
    $currentlabel = "NCL07A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '08'
    $day = '05'
    $date = '6'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_BG NIMG15A,CAL_0805
    show expression "img/NIMG15F-568h@2x.jpg" as cal zorder 5
    show expression "img/08_05_SATURDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/EXBG09A@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/EXBG09A@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC03"),"True","img/CL_ZAC03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_IN 1,128
    play music "OBGM08"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "早上。克罗艾学姐的样子有些奇怪。"
    voice "NCL07A_KU000"
    克罗艾 "「唉……」"
    "明明做了这么丰盛的早餐，却时不时地停下手中的碗筷，叹着气。视线迷茫的看向远方，一副无限忧愁的样子。"
    志雄 "「我说，学姐……？」"
    "听到我的声音，学姐把身子转向我。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC05"),"True","img/CL_ZAC05A@2x.png") as lh0 zorder (10+0):
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
    voice "NCL07A_KU001"
    克罗艾 "「啊。那个……抱歉。我没听到你说什么……」"
#THREAD_STP 1
#REMOVE_REEK_CHR 0
    志雄 "「真的不要紧吗？　难道说是身体不舒服……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC01"),"True","img/CL_ZAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07A_KU002"
    克罗艾 "「志雄还真是爱操心呢。不过，没有听你说话是我不好……」"
    "说完，学姐继续吃起了早饭。但没过多久，就又叹起气来。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC03"),"True","img/CL_ZAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07A_KU003"
    克罗艾 "「唉……」"
    志雄 "「……」"
    "怎么看都不是没事的样子。不过，就状况看，与其说是身体不舒服，倒更像是为什么事情而烦恼。"
    "现在学姐会烦恼的事情就只有那个了吧。"
    "从那之后就没有再接到学姐父母的电话。"
    voice "NCL07A_KU004"
    克罗艾 "「唉……」"
    "又一次叹气，真是烦恼得不轻啊。"
    "这样下去一整天都会不愉快吧。还有可能会变得更糟糕。"
    "我希望学姐能够保持笑容。就算我无法解决学姐的烦心事，但至少要让烦恼中的学姐高兴起来。"
    志雄 "「学姐，去海边吧。肯定能让心情变好的。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB03"),"True","img/CL_ZAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07A_KU005"
    克罗艾 "「海边……？」"
    "听到我的提议，克罗艾学姐有些呆滞地眨了眨眼。"
    志雄 "「嗯，难得的暑假。而且学姐也说过想去的吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB05"),"True","img/CL_ZAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07A_KU006"
    克罗艾 "「虽然是说过……但是，志雄你是备考生，还有更重要的事情……」"
    "克罗艾学姐一脸困惑。"
    志雄 "「虽然是那样。但是，难得的暑假却一点回忆也没留下不是很寂寞吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB04"),"True","img/CL_ZAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07A_KU007"
    克罗艾 "「我只要和志雄在一起就不会感到寂寞……」"
    志雄 "「呃……」"
    "突然间听到学姐那么说，不禁感到脸颊热热的。"
    "不过，不能在这里停下来。"
    志雄 "「而且难得买了泳装。……啊，难道没拿来吗？」"
    "真是那样的话，就不得不放弃去海边的提案了。让我想想其他的转换心情的方法……"
    stop music fadeout 1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAA07"),"True","img/CL_ZAA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07A_KU008"
    克罗艾 "「实际上……我是有带来的……」"
    志雄 "「真的吗！？」"
    voice "NCL07A_KU009"
    克罗艾 "「那个，我也觉得去海边挺不错的呢～」"
    志雄 "「那就出发吧！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB04"),"True","img/CL_ZAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07A_KU010"
    克罗艾 "「但是考前复习也完全不能丢吧？」"
    志雄 "「多亏了学姐，复习进行得很顺利。话说回来，一直埋头学习，不偶尔到外面活动下的话，效率也会越来越低吧？」"
    voice "NCL07A_KU011"
    克罗艾 "「也是……」"
    window hide
    play music "BGM10"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07A_KU012"
    克罗艾 "「那咱们出发吧～」"
    志雄 "「嗯！」"
    scene expression "img/BG15MA@2x.jpg" as bg_over zorder 2 with dissolve
    "匆忙地处理好各种手头上的事后，我们来到了附近的海滩。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG21AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG21AA@2x.jpg" as bg0 with dissolve
    play sound "SE08_14L"
    pause (32/32.0)
#FADE_IN 1
    pause (32/32.0)
#SE_VOLC 1,128
#EFF_STAC 0,WATERTWINKLE,EFF_SKIP
#EFF_PRI 0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA01"),"True","img/CL_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07A_KU013"
    克罗艾 "「人真多啊……」"
    志雄 "「嗯，在真正的大海之前还有一片人海……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB06"),"True","img/CL_MAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07A_KU014"
    克罗艾 "「嘿嘿。」"
    "满怀着期待赶到海边的我们，面对着眼前蜿蜒着的人群，只能抱以无奈的叹息。"
    志雄 "「已经是旧历盂兰盆会的时候了，还以为人应该少些了……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07A_KU015"
    克罗艾 "「和期待的不一样呢。总之，先找个能下脚的地方吧。不然连泳装都没办法换了呢……」"
    window hide
#SE_VOLC 1,0
    stop music fadeout 1
#EFF_STPC 0,EFF_NOSKIP
#EFF_PRI 0
#FADE_OUT 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    scene expression Solid("000") with None
#FADE_IN 0
    "我们竭力穿梭在身边拥挤的人群中，好不容易到达了更衣室。"
    window hide
#FADE_OUT 0
    stop music fadeout 1
#BG_COLC 0,128,128,128,128
    scene expression "img/BG21AA@2x.jpg" as bg0 with dissolve
#SE_VOLC 1,255
#EFF_STAC 0,WATERTWINKLE,EFF_SKIP
#FADE_IN 1
    "我迅速的换好衣服，拿着带来的东西在会合地等克罗艾学姐。"
    志雄 "「说起来，我连学姐会穿着什么样的泳装都不知道呢……」"
    "在购物中心买东西的时候也不让我看。"
    voice "NCL07A_KU016"
    克罗艾 "「久等了～」"
    "在满怀期待与紧张的等待后，背后终于传来了学姐的声音。"
    "抑制住心脏的狂跳，我转过身，在那里的是——"
    window hide
#EFF_STPC 0,EFF_NOSKIP
#SE_VOLC 1,0
#BG_GET_NOC 0,F34
#BG_SET_BACK 
#BG_PRIC 0
#EFF_PRI 1
#BG_INIC 3
    show expression "img/NIMG01B@2x.png" as bg3:
        ypos 0.0
#EFF_STAC 1,CLOUD_B,EFF_NOSKIP
    with dissolve
#BG_PRIC 0
    play sound "SE07_25"
#FILT_IN 16,0,COL_SOFTSUN
#FILT_OUT 16
    pause (80/32.0)
#BG_SET_BACK 
#BG_INIC 1
#BG_INIC 0
#BG_PRI 1
#BG_PRI 0
#BG_ALPC 1
#BG_ALPC 0
#BG_POSC 1,0,-448,640,448
    show expression "img/NIMG18C@2x.jpg" as bg1 zorder 1:
        yalign 1.0
        linear 1 yalign 0.0
    pause 1
    play sound "SE07_23"
#ROUTINE_STA
#BG_ALP_AUTOC 1,128,0,F24
#BG_POS_AUTOC 1,,F24,192
#ROUTINE_STP
#EFF_PRI 0
#ROUTINE_STA
#EFF_STAC 0,LENZ,EFF_SKIP
#BG_ALP_AUTOC 0,64,0,F24,128
#ROUTINE_STP
#BG_ALP_AUTOC 0,0,0,F24,128
#BG_ALP_SAVEC 3
#BG_POS_SAVEC 1
#BG_POS_SAVEC 0
#BG_ERSWC 0,3,BG_NOFADE
    pause (192/32.0)
#EFF_STPC 0,EFF_NOSKIP
#EFF_STPC 1,EFF_NOSKIP
    志雄 "「……」"
    克罗艾 "「？」"
#MESEX_A M_NOA,A_CH_KU,NCL07A_KU017,"【クロエ】「？」%K%P"
    志雄 "「……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MCB03"),"True","img/CL_MCB03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
#BG_INIC 0
#BG_PRIC 0
    hide bg1
    scene expression "img/BG21AA@2x.jpg" as bg0 zorder 0
    with dissolve
    play music "BGM04"
#EFF_PRI 0
#EFF_STAC 0,WATERTWINKLE,EFF_SKIP
    voice "NCL07A_KU018"
    克罗艾 "「志雄……？」"
    "内心瞬间有种被什么东西完全充满了的感觉。"
    "无法用语言来表达。"
    "好美。学姐穿泳装的样子，比至今看过的所有东西都要更加美丽。"
    "周围的视线正在不寻常地聚集过来。"
    voice "NCL07A_XO000"
    カップル男性 "「哇哦。什么嘛？　模特吗……？」"
    voice "NCL07A_XP000"
    カップル女性 "「是啊，好美的人——……喂，别老盯着人家看！」"
    play sound "SE04_05"
    voice "NCL07A_XO001"
    カップル男性 "「好疼啊。不要打我啦……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MCB04"),"True","img/CL_MCB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "在我的视线下，克罗艾学姐害羞地缩了缩双臂。"
    voice "NCL07A_KU019"
    克罗艾 "「那个，难道说是……」"
    志雄 "「嗯？」"
    voice "NCL07A_KU020"
    克罗艾 "「不、不适合……吗？」"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "直率地夸奖":
            $F7=0
        "认真地夸奖":
            $F7=1
        "不加掩饰地夸奖":
            $F7=2
    if F7==0:
        jump L_NCL07A_SEL00_A
    if F7==1:
        jump L_NCL07A_SEL00_B
    if F7==2:
        jump L_NCL07A_SEL00_C
label L_NCL07A_SEL00_A:
    志雄 "「诶？」"
    志雄 "「啊，没有！　十分的合适……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MCB03"),"True","img/CL_MCB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07A_KU021A"
    克罗艾 "是、{w=1}{nw}"
#MESA A_CH_KU,NCL07A_KU021A,"【クロエ】「是、"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MCB06"),"True","img/CL_MCB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07A_KU021B"
    extend "是那样吗？」"
    "克罗艾学姐先是有些吃惊，之后立刻变得高兴了起来。"
    voice "NCL07A_KU022"
    克罗艾 "「太好了。那就走吧～」"
    jump L_NCL07A_SEL00_X
label L_NCL07A_SEL00_B:
    志雄 "「很合适——」"
    志雄 "「因为太合适了，所以不知不觉的就目不转睛了……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MCB03"),"True","img/CL_MCB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07X_KU000A"
    克罗艾 "诶……{w=2}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MCB06"),"True","img/CL_MCB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07X_KU000B"
    extend "啊，嗯。谢谢……」"
    "克罗艾学姐的脸彻底地红了起来，但是还是露出了高兴的笑容。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MCB04"),"True","img/CL_MCB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07X_KU001"
    克罗艾 "「真是的，一直这么盯着看我会害羞的啊。快点走吧～」"
    jump L_NCL07A_SEL00_X
label L_NCL07A_SEL00_C:
    志雄 "「不！　十分的适合。那个……十分的，美妙」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MCA07"),"True","img/CL_MCA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07X_KU002"
    克罗艾 "「谢，谢谢。那个……感觉今天志雄穿的也很帅……」"
    志雄 "「诶？」"
    voice "NCL07X_KU003"
    克罗艾 "「诶？　我、我是说谢谢……！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MCB04"),"True","img/CL_MCB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07X_KU004"
    克罗艾 "「那，那就走吧？」"
    window hide
    jump L_NCL07A_SEL00_X
label L_NCL07A_SEL00_X:
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XCB06"),"True","img/CL_XCB06A@2x.png") as lh0 zorder 100:
        ypos 0.0
        xcenter (320+224)/640.0
    with move
    "说着，学姐挽住我的胳膊。"
    "明明是和平时一样的动作，今天却比平时更加的激动。"
    voice "NCL07A_KU023"
    克罗艾 "「好了，快点！」"
    志雄 "「嗯，嗯！」"
    window hide
    play sound "SE01_23L"
    show expression "img/BG91AA@2x.jpg" as bg_over zorder 0 with dissolve
#EFF_PRI 0
#EFF_STAC 0,TWINKLE,EFF_SKIP
    pause (32/32.0)
    stop se
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_SCB06"),"True","img/CL_SCB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL07A_KU024"
    克罗艾 "「志雄——！」"
    志雄 "「喂，到处跑的话，小心要摔倒了哦！？　等一下啊！」"
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
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LCB06"),"True","img/CL_LCB06A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCL07A_KU025"
    克罗艾 "「邀请别人的人，自己却不做出表率，到底是怎么回事啊——嘿！！」"
    window hide
#EFF_STPC 0,EFF_NOSKIP
#EFF_PRI 0
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL04A")]=True
    show expression "img/EVN_CL04A@2x.jpg" as bg1 zorder 10
    play sound "SE03_56"
#BG_ALP_AUTOC 1,128,0,F24,24
#BG_ALP_SAVEC 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
#BG_SWPC 0
    with dissolve
#BG_PRI 0
#BG_PRI 1
#BG_ALPC 1,128
    "学姐慢慢地用手把海水往上撩，水劈头盖脸地泼了过来。"
    志雄 "「呜哇！　这么突然的，偷袭我！」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL04C")]=True
    show expression "img/EVN_CL04C@2x.jpg" as bg0 zorder 10 with dissolve
    voice "NCL07A_KU026"
    克罗艾 "「好不容易来一次。偶尔也想找回童心呢。不好吗？」"
    志雄 "「亏你说出来了呢～」"
    "说起找回童心的话——"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL04D")]=True
    show expression "img/EVN_CL04D@2x.jpg" as bg0 zorder 10 with dissolve
    voice "NCL07A_KU027"
    克罗艾 "「志雄……？」"
    "我也用手撩起海水，开始了反击。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL04B")]=True
    show expression "img/EVN_CL04B@2x.jpg" as bg1 zorder 10 with dissolve
    play sound "SE03_57"
#BG_ALP_AUTOC 1,128,0,F24,24
#BG_ALP_SAVEC 1
#BG_SWPC 0
    hide bg1 with dissolve
#BG_PRI 0
#BG_PRI 1
#BG_ALPC 1,128
    voice "NCL07A_KU028"
    克罗艾 "「啊！　喂，志雄。我可没做到那个地步！」"
    志雄 "「哈哈，『滴水之恩，当涌泉相报』这可是书上说的哦～」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL04D")]=True
    show expression "img/EVN_CL04D@2x.jpg" as bg0 zorder 10 with dissolve
    voice "NCL07A_KU029"
    克罗艾 "「这样……那我也十倍奉还给你！」"
    "说着，学姐用两只手把更多的水向我泼来。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL04A")]=True
    show expression "img/EVN_CL04A@2x.jpg" as bg0 zorder 10 with dissolve
    play sound "SE03_39L"
    voice "NCL07A_KU030"
    克罗艾 "「嘿！！」"
    志雄 "「呜哇！　那个，学姐？　有些过分了吧？」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL04C")]=True
    show expression "img/EVN_CL04C@2x.jpg" as bg0 zorder 10 with dissolve
    voice "NCL07A_KU031"
    克罗艾 "「什么？　要是觉得不甘心的话，加倍奉还就行了哦？　嘿——嘿——！」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL04A")]=True
    show expression "img/EVN_CL04A@2x.jpg" as bg0 zorder 10 with dissolve
    "就算说话的时候，学姐也丝毫没有停手，完全不给我还击的机会。"
    志雄 "「等一下啊！」"
    voice "NCL07A_KU032"
    克罗艾 "「要是投降的话，就给你喘息的机会。来吧！！」"
    志雄 "「我投降我投降！　我投降了！」"
    "虽然我口头上竖起了『白旗』，不过学姐一点都没有停手的意思……"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#BG_PRIC 0
#BG_INIC 3
    show expression "img/NIMG01B@2x.png" as bg3 zorder 3 with dissolve
#EFF_PRI 0
#EFF_STAC 0,CLOUD_B,EFF_SKIP
#BG_ALP_AUTOC 0,0,0,1
    stop se
    stop sound
    "在那之后，我们两个人在浅滩上寻找贝壳和小鱼，在海水里尽情的畅泳，完全享受沉浸在大海带来的快乐里。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    hide bg3 with dissolve
#EFF_PRI 0
#BG_PRIC 0
#BG_ALPC 0,128
    show expression "img/NIMG01C@2x.png" as bg1 zorder 1
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
#EFF_STAC 0,CLOUD_C,EFF_SKIP
    stop music fadeout 1
    play sound "SE05_19L"
#FADE_IN 1
    stop music fadeout 1
#SE_VOLC 1,64
    pause (64/32.0)
#BG_SET_BACK 
#BG_INIC 0
#BG_ALPC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG22EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG22EA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LCA01"),"True","img/CL_LCA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#ROUTINE_STA
#EFF_PRI 0
#BG_PRIC 1
#CHR_ALP_AUTOC 0,128,0,F24
#BG_ALP_AUTOC 0,128,0,F24
#ROUTINE_STP
    hide bg1 with dissolve
#EFF_STPC 0,EFF_NOSKIP
#BG_BLUR 0
#BG_PRIC 1
#EFF_PRI 0
    play music "BGM14"
    voice "NCL07A_KU033"
    克罗艾 "「人，变少了呢。」"
    志雄 "「是啊……」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_BLUR 0
    "注意到的时候，海岸上的人已经变得稀稀拉拉的。像是在梦中玩耍的我们，完全没有注意到时间在飞逝。"
    "人们大多都做着回家的准备，慢慢从海岸上散去了。"
    "像是被留下来一样……"
    "不禁产生了这样的想法。联想到为了前途而迷惑的我，焦躁的感觉瞬间又走遍了全身，缓缓地从每一个寒毛孔中渗了出来。"
    "明明是自己说要到海边来的，可现在又在纠结这样做到底好不好。"
    "至今还无法决定自己前进的方向，不安也随着时间的推移，被一点点放大……"
    志雄 "「真没用啊……」"
#CHR_INIC 0
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LCA02"),"True","img/CL_LCA02A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    "听到我漏出的小声嘟囔，克罗艾学姐有些在意地侧过头来。"
    voice "NCL07A_KU034"
    克罗艾 "「怎么了？」"
    志雄 "「啊，没、没什么……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LCA06"),"True","img/CL_LCA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07A_KU035"
    克罗艾 "「……是吗？」"
    "学姐的声音也没有什么精神。明明刚才还那么高兴的。"
    window hide
#SE_VOLC 1,128
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL05A")]=True
    show expression "img/EVN_CL05A@2x.jpg" as bg1 with dissolve
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "学姐坐在沙滩上向大海望去。"
    "我暂时按下心中的焦躁，也坐在了学姐的边上。"
    克罗艾 "「……」"
#MESEX_A M_NOA,A_CH_KU,NCL07A_KU036,"【クロエ】「……」%K%P"
    志雄 "「……」"
    "就这样，两个人朝向大海的方向眺望着慢慢落下去的夕阳。如画的风景中，克罗艾学姐的嘴唇微微开合。"
    voice "NCL07A_KU037"
    克罗艾 "「真的很开心呢。」"
    志雄 "「那就好。看来是来对了。」"
    "我暂且收起心中的纠葛，用明快的声音说着。"
    voice "NCL07A_KU038"
    克罗艾 "「嗯……」"
    "学姐的声音，果然没有精神。"
    "在我下定决心开口询问之前，学姐先开始说了起来。"
    voice "NCL07A_KU039"
    克罗艾 "「以前和家里人一起来过海边……」"
    志雄 "「……」"
    "仅仅听到这里，我就明白了学姐消沉的理由。"
    voice "NCL07A_KU040"
    克罗艾 "「和爸爸妈妈，我们三个人。久违地赶上爸爸休息的日子，从早上就开始做便当……」"
    "学姐一直注视着大海的方向，眼睛好像也有些湿润了。"
    voice "NCL07A_KU041"
    克罗艾 "「收集贝壳，用沙子搭城堡之类的。记忆中的我呢，可是一直在欢笑着的哦。既快乐，又高兴……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL05B")]=True
    show expression "img/EVN_CL05B@2x.jpg" as bg1 with dissolve
    voice "NCL07A_KU042"
    克罗艾 "「和现在的我完全不一样。」"
    志雄 "「学姐……」"
    voice "NCL07A_KU043"
    克罗艾 "「抱歉。难得的约会出来，我还说些这样的话……」"
    志雄 "「没事的。学姐不也听了我的烦恼吗？不要在意这些。」"
    voice "NCL07A_KU044"
    克罗艾 "「嗯……」"
    "学姐把脸埋在膝盖上，稍稍点了点头。"
    voice "NCL07A_KU045"
    克罗艾 "「那一天，还有现在，对我来说都是很重要的回忆哦。」"
    志雄 "「那样的话，下次就大家一起来吧！」"
    "我不知不觉的高兴起来，向学姐说出那样的提案。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL05C")]=True
    show expression "img/EVN_CL05C@2x.jpg" as bg1 with dissolve
    voice "NCL07A_KU046"
    克罗艾 "「诶？」"
    志雄 "「我和学姐，还有学姐的父亲和母亲。还有诺艾儿她们也一起。」"
    voice "NCL07A_KU047"
    克罗艾 "「是呢，那样也不错呢……」"
    "学姐像是说着无法实现的憧憬，表情落寞。"
    志雄 "「会实现的，一定的。」"
    voice "NCL07A_KU048"
    克罗艾 "「但是我，还没有和父母好好谈过……」"
    志雄 "「那样的话，就试着去谈吧。一定会顺利的哦。」"
    voice "NCL07A_KU049"
    克罗艾 "「或许，我会成为他们两个的负担的。我不希望变成那样。」"
    志雄 "「克罗艾学姐……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL05B")]=True
    show expression "img/EVN_CL05B@2x.jpg" as bg1 with dissolve
    voice "NCL07A_KU050"
    克罗艾 "「抱歉。不过，现在我还没有什么自信……」"
    志雄 "「我觉得也没必要那么着急。慢慢的，一点点的朝着那个方向努力就行了！」"
    "和我现在的烦恼不同，学姐还有足够的时间。"
    "既然之间有距离，那慢慢努力拉近就行了。"
    "避开勉强而受到的伤害，只要坚定的去做，总有隔阂消除，重回团聚的一天。"
    "这时候的我是这样想的。"
    voice "NCL07A_KU051"
    克罗艾 "「不需要……着急……」"
    "学姐嘴里重复着我说的话。"
    window hide
#SE_VOLC 1,0
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG22EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG22EA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
#SE_VOLC 1,128
#FADE_IN 1
    志雄 "「好了，差不多该回去了。」"
    voice "NCL07A_KU052"
    克罗艾 "「等一下。」"
#CHR_INIC 0
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XCB04"),"True","img/CL_XCB04A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    "我停止了动作，下一刻，学姐突然紧紧地把身子靠了过来。"
    志雄 "「学，学姐！？」"
    voice "NCL07A_KU053"
    克罗艾 "「气温，有些凉了呢。」"
    志雄 "「是，是呢……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XCB02"),"True","img/CL_XCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07A_KU054"
    克罗艾 "「和你在一起真好。」"
    志雄 "「诶，学姐你说了什么吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LCB04"),"True","img/CL_LCB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL07A_KU055"
    克罗艾 "「没有哦。那就回去吧。」"
    window hide
    play sound "SE01_23L"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    stop se fadeout 1
    "就这样，学姐向着存放物品的更衣室走去。"
    "我转身，又看了一眼夕阳，暖暖的黄从一点扩散开来，仿佛整个海滩都被点燃了……"
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