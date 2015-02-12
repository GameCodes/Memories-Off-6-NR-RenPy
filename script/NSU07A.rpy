label NSU07A:
    $currentlabel = "NSU07A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '28'
    $date = '5'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
    show expression "img/NIMG15G-568h@2x.jpg" as cal zorder 5
    show expression "img/07_28_FRIDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/NIMG03D@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/NIMG03D@2x.jpg" as bg0 with dissolve
    show expression Solid("000") as bg_over with None
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
    play sound "SE03_90"
    voice "NSU07A_SU000"
    铃？ "「志雄……志雄……志雄……」"
    志雄 "「嗯」"
    "有谁在叫我。"
    voice "NSU07A_SU001"
    铃？ "「喂，快起来」"
    志雄 "「什么啊？预算会议的时间还没到啊……」"
    voice "NSU07A_SU002"
    铃？ "「喂。你适可而止快给我起来！」"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide bg_over
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBC03"),"True","img/SU_XBC03A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
#FADE_IN 1
    志雄 "「！？」"
    "睁开眼睛，就在能感到呼吸的距离内，我看到了一张人脸。"
    志雄 "「呜哇！什、什么！？」"
    window hide
    play sound "SE03_28"
#CHR_SCL_AUTOC 0,384,384,0,F24,16
#CHR_POS_AUTOC 0,,(100),0,F24,16
#CHR_SCL_SAVEC 0
#CHR_POS_SAVEC 0
    play sound "SE04_18"
#THREAD_STA 1,THREAD_QUA_CHR0_WIN
#VIB_DOKA 
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    志雄 "「呃！」"
    with vpunch
#THREAD_WAT 1
#WIN_POS 0,0
#VIB_STP 5
#MESX "%K%P"
    window hide
    hide lh0 with dissolve
#CHR_SCLC 0,256,256
#CHR_COLC 0,128,128,128,128
#CHR_POSC 0,(320)
    show expression "img/BG15MA2@2x.jpg" as bg_over zorder 5
    show expression "img/SU_LBC04A@2x.png" as lh0 zorder (10-0):
        xcenter ((320)/640.0)
    with dissolve
    play music "BGM05"
    voice "NSU07A_SU003"
    铃 "「好疼～」"
    "我莫名其妙地跳起身来，额头上感到一阵剧痛。与此同时，铃的惨叫声传入我的双耳。"
    志雄 "「是、是铃？什么事情啊？」"
    "坐起身来发现，铃就在我的床边。"
    志雄 "「才刚这个时间啊？」"
    "一边揉着撞上的额头一边看着表，还没到６点。"
    hide lh0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBC02"),"True","img/SU_LBC02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU004"
    铃 "「啊～。吓着你了，抱歉」"
    "铃一边揉着发红的额头，一边对我苦笑着。"
    "真是的，都是因为这个人突然做了这种像小孩子一样的事……。"
    志雄 "「嘛，这倒没事……怎么了？这么早就过来？」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBA01"),"True","img/SU_LBA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU005"
    铃 "「志雄等下也没有去学生会和补习学校的打算吧？」"
    志雄 "「……？　是呢。我倒是想先在家学习一下的吧」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB02"),"True","img/SU_LBB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU006"
    铃 "「好～了。那，我们去旅行吧！」"
    window hide
    pause (32/32.0)
    "啊？"
    "我还没睡醒吗？"
    "要说这是梦的继续的话，我的额头倒是还有点痛……。"
    志雄 "「那～个，谁去？」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB01"),"True","img/SU_LBB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU007"
    铃 "「当然是，我和志雄了」"
    志雄 "「去干什么？」"
    voice "NSU07A_SU008"
    铃 "「旅、旅行。驾车远游！　喜欢的话就请来吧」"
    "本来就不太灵光的脑子，想了半天才想好该说啥。"
    志雄 "「难道是，现在就去？」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB02"),"True","img/SU_LBB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU009"
    铃 "「是啊！」"
    "在昏暗的房间里，铃挺着胸。"
    志雄 "「什么？」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB05"),"True","img/SU_LBB05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU010A"
    铃 "「啊～，那个。{w=3}{nw}"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBA01"),"True","img/SU_LBA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU010B"
    extend "嗯，是小说的取材」"
    "啊，原来如此。作家的话可能也会有这些事。但是……。"
    志雄 "「为什么我也去？」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBA05"),"True","img/SU_LBA05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU011"
    铃 "「问题太多了啊」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBA01"),"True","img/SU_LBA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU012"
    铃 "「志雄你夏天好像也没有去哪里玩的计划吧。这是之前去看焰火的回礼」"
    "难道，她之前说的活动什么的指的就是这个吗！？"
    "就算是这么说，突然说两个人要去旅行什么的……。"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "也只能去了吧":
            $F7=0
        "可这么突然……":
            $F7=1
    if F7==0:
        jump L_NSU07A_SEL00_A
    if F7==1:
        jump L_NSU07A_SEL00_B
label L_NSU07A_SEL00_A:
    $F4+=1
    "为什么这么早就出去，事先也没和我联络过，说起来我还是应考生，本来想对她提出各种各样的意见的……。"
    "背后透射出的晨曦衬托着铃的笑容，看到这样的一幕的我感觉无论怎样都无所谓了。"
    "既然是难得的机会，那就好好享受吧！"
    志雄 "「那么，要去哪里呢？」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBC04"),"True","img/SU_LBC04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU013"
    铃 "「……哎？」"
    志雄 "「怎么了？」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBC01"),"True","img/SU_LBC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU014"
    铃 "「没，本以为，你会再发些牢骚的」"
    志雄 "「如果我发牢骚的话，你打算怎么办呢？」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBC02"),"True","img/SU_LBC02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU015"
    铃 "「给你按摩直到你改变想法了呢？还是做出一副可爱的样子软磨硬泡呢？二选一吧」"
    志雄 "「可别说缩头技什么的就是按摩啦。啊，不过软磨硬泡的样子倒是说不定想见识一下」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBC03"),"True","img/SU_LBC03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU016"
    铃 "「开、开玩笑的啊」"
    志雄 "「那，我是不是不去了呢～」"
    "就是在这种情况下，我更是想稍微欺负一下铃了。"
    "这种机会，可实在是机不可失失不再来啊。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBA05"),"True","img/SU_LBA05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU017"
    铃 "「呜……」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBA01"),"True","img/SU_LBA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    "一瞬间，铃仿佛露出了不愉快的神情，不过马上就转为笑容了。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE03_92"
#CHR_INIC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBB03"),"True","img/SU_XBB03A@2x.png") as lh10 zorder 100:
        ypos 0.0
    with dissolve
    "然后，她坐到了床上，一下子靠向我身边。"
#REEK_CHR 0
    voice "NSU07A_SU018"
    铃 "「志雄……和我一起，去旅行吧？」"
#REMOVE_REEK_CHR 0
    志雄 "「哎……等、等等……？」"
    "铃就这样把她的脸，倚靠在我的胸前。"
    "她的头发，隐约带着不知道是哪种花的芬芳。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBC02"),"True","img/SU_XBC02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU019"
    铃 "「我一个人好寂寞啊……和我一起玩吧……」"
    "铃用脸颊抵着我的胸口，仰视着我。"
    "不由得，看见她的眼睛有些湿润。"
    "然后，她的手仿佛要拥抱着我，绕到了我的身后……。"
    voice "NSU07A_SU020"
    铃 "「如果……不跟我一起去的话……」"
    志雄 "「铃，我已经知……」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBC03"),"True","img/SU_XBC03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU021"
    铃 "「哦呀！」"
    window hide
#VIB_DOKA 
    play sound "SE04_23"
    with vpunch
    with hpunch
#QUA3_ALL 
#VIB_STP 
    志雄 "「疼疼疼疼疼疼！」"
    "不知不觉间，铃已用关节技将我的右胳膊紧紧地制住。"
    "果然变成这样了吗！"
    志雄 "「投降、投降！我跟你一起去！让我跟你一起去吧所以饶了我吧！」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    stop se
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB01"),"True","img/SU_LBB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU022"
    铃 "「很好，一开始就这样诚实的话那该有多好」"
    "铃终于把手放开。"
    "就因为有一点恶作剧之心，就差点失去右胳膊……今后要多加注意了。"
    志雄 "「疼疼疼疼疼……真是的手下留情点啊。一下子就清醒过来了」"
    "完全地忽视了我的牢骚，铃笑嘻嘻地微笑着。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB02"),"True","img/SU_LBB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU023"
    铃 "「还有，日程是４天３夜。费用你就不用管了」"
    志雄 "「别啊，我会付的。再怎么说，让你把这些都承担下来也不太好」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBC02"),"True","img/SU_LBC02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU024"
    铃 "「可是，这也是因为我任性的要求呢。而且价钱也不低哦？」"
    志雄 "「既然这样，就更不能让你替我来付了啊」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB01"),"True","img/SU_LBB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU025"
    铃 "「那就先这样吧。我先临时替你垫上」"
    志雄 "「嗯」"
    voice "NSU07A_SU026"
    铃 "「然后等到回来以后，如果你觉得这是次值得的旅行你再付给我。直接还清、分期付款都ＯＫ啦」"
    志雄 "「嗯～，我知道了。那就拜托你了」"
    jump L_NSU07A_SEL00_X
label L_NSU07A_SEL00_B:
    志雄 "「呃，虽说这样就定下来了……」"
    "旅行本身是很快乐，但还是不能一下子就决定下来啊。"
    "学生会的工作也不是没有，应考复习也不能不做。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBC02"),"True","img/SU_LBC02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU028"
    铃 "「因为我工作的原因，所以才这么紧迫地定好的计划」"
    "嘛，铃的计划是很难定的这一点，我倒是挺清楚……"
    志雄 "「对了，说是要去旅行，莫非是要住在外面吗？」"
    志雄 "「如果要住上几天的话，那旅费……」"
    "平常倒并不是为钱发愁，不过我也并没有富裕到说临时出去旅游就能随时拿出全部经费的程度。"
    志雄 "「还有……」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBC03"),"True","img/SU_LBC03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU029"
    铃 "「啊～，够了，磨磨蹭蹭地烦死人了！」"
    志雄 "「铃、铃？」"
    voice "NSU07A_SU030"
    铃 "「别考虑什么多余的事，想不想和我一起去旅游，就回答我这个！」"
    志雄 "「所以我说……」"
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
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBC03"),"True","img/SU_XBC03A@2x.png") as lh10 zorder 100:
        ypos 0.0
    with dissolve
    voice "NSU07A_SU031"
    铃 "「回゛答゛我」"
    "铃走到我的跟前，用国王俯视臣民般的姿势盯着我。"
    "然后她伸出了修长的手指……。"
    window hide
#VIB_DOKA 
    play sound "SE07_15"
    with vpunch
    with hpunch
#QUA3_ALL 
#VIB_STP 
    志雄 "「疼疼疼疼！」"
    "按住了我的太阳穴，使劲地钻了起来。"
    stop se
    "然后持续数秒的头晕目眩与激烈的疼痛之后，她放松了手上的力道。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBC05"),"True","img/SU_XBC05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    铃 "「嗯？」"
    "从铃的手指间看到的她的表情，好像在期待着什么。"
    "没、没法拒绝的啊。……本来，两个人一起去旅行这个计划，本身就是非常具有魅力的。"
    志雄 "「我想和你一起去……」"
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
#CHR_POSC 0,(320)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBC01"),"True","img/SU_LBC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU033"
    铃 "「好。既然这样就走吧」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBC02"),"True","img/SU_LBC02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU034"
    铃 "「因为我的任性让你陪着我，倒是觉得有点不好意思」"
    voice "NSU07A_SU035"
    铃 "「如果错过了这次志雄你也该忙起来了吧，我也安排不开时间了」"
    志雄 "「啊，没事，只是你突然这么一说我有些吃惊了……并不是我不想去啊」"
    "我一边摸着依然残留着疼痛感的太阳穴，一边说道。铃则是莞尔一笑。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB01"),"True","img/SU_LBB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU036"
    铃 "「日程是４天３夜。费用什么的你就不用管了」"
    志雄 "「哎？这也太不好了吧」"
    "既然都决定要去了，旅行的费用不自己来出可不行啊……。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB03"),"True","img/SU_LBB03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NSU07A_SU037"
    铃 "「刚才我也说过了，这都是因为我的任性。我先垫了吧，如果你还在意的话之后再付就行了」"
#REMOVE_REEK_CHR 0
    志雄 "「嗯～，我知道了」"
    "多多少少有些从情理上说不过去，不过我还是点头接受了这个提议。"
    jump L_NSU07A_SEL00_X
label L_NSU07A_SEL00_X:
    "嘛，这点程度就姑且顺从一下好了。"
    "而且在这种地方吵架也没有意义，说起来铃还是为我着想，不想给我增加负担的吧。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBA01"),"True","img/SU_LBA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU027"
    铃 "「那，就赶快去准备吧」"
    志雄 "「明白了。嗯，要带些什么好呢……？」"
    window hide
    play sound "SE03_66"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "总之就先按铃说的那样，把替换衣服和牙刷之类的简单的旅行套装塞到了包里。"
    window hide
    stop se fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG14AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG14AA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
#FADE_IN 1
    "做好准备，走出了公寓。已经提前出去的铃，和爱车一同在那里等着我。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA01"),"True","img/SU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「久等了」"
    voice "NSU07A_SU039"
    铃 "「没关系，时间还有富余」"
    "仰望着天空，还是有些昏暗。气温也还没有高起来。"
    志雄 "「铃，你的行李就只有这些？」"
    "虽然摩托车的储物箱已经放置了东西，不过作为女生出门旅行的行李来说这还是显得太少了点。"
    voice "NSU07A_SU040"
    铃 "「嗯，已经事先送到要住的地方了」"
    志雄 "「嘿～」"
    "准备得意外的周全嘛。看起来是无论如何也想去旅行呢。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU041"
    铃 "「给」"
    window hide
    play sound "SE03_75"
    "铃把拿在手里的头盔扔给了我。"
    "头盔的式样相同但颜色不一样。因为铃经常载我出去，所以也给我准备了一个。"
    志雄 "「好」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE06_12"
    play sound "SE06_13L"
    voice "NSU07A_SU042"
    铃 "「那我们就走吧」"
    "骑在车上的铃，立刻发动了引擎，我也迅速坐到了后面的座位上。"
    志雄 "「我暂且先说一句，要安全驾驶啊！」"
    "我用不输引擎轰鸣声的嗓门提醒着她。铃也明白这是难得的旅行吧，应该不需要我说的。"
    "总之，迄今为止我已经看见过无数次的深渊地狱就别再……。"
    voice "NSU07A_SU043"
    铃 "「嗯～？知道啦知道啦」"
    window hide
    play sound "SE06_15L"
    #TODO
#BG_INIC 3
    #show expression Solid("fff") as bg1 with dissolve
#ROUTINE_STA
#BG_POSC 3,30,-60,749,450
    scene expression "img/EVC_SU02A1@2x.png" as bg3:
        block:
            align (.5,.5)
            parallel:
                linear 0.03 xalign 0.53
            parallel:
                linear 0.03 yalign 0.53
            repeat
    show expression "img/Motor_EF_BG@2x.png" as motor_eff_bg zorder -10
    show expression "img/Motor_EF_Building1@2x.png" as motor_eff_down_s zorder -8:
        xcenter .25
        ycenter .7
    show expression "img/Motor_EF_Building2@2x.png" as motor_eff_up_s zorder -7:
        xcenter .75
        ycenter .7
    show expression im.Scale("img/Motor_EF_Wood1@2x.png",1136,263) as motor_eff_up zorder -6 at motor_eff_movein:
        yalign 1.0
    show expression im.Scale("img/Motor_EF_Wood1@2x.png",1136,263) as motor_eff_up2 zorder -6 at motor_eff_moveout:
        yalign 1.0
    show expression "img/Motor_EF_Wood2@2x.png" at motor_eff_moveout as motor_eff_down zorder -5:
        yalign 1.0
    show expression "img/Motor_EF_Wood3@2x.png" at motor_eff_movein as motor_eff_down2 zorder -5:
        yalign 1.0
    with dissolve
#EFF_PRI 0
#EFF_STAC 0,MOTOR_RIDE_EF,EFF_NOSKIP
#ROUTINE_STP
    hide bg1 with dissolve
    志雄 "「呜，哇啊，你完全没往心里去吧～！」"
    "我在后座上坐稳的一瞬间，铃就驾驶摩托冲了出去。"
    show expression "img/EVC_SU02A2@2x.png" as bg3 with dissolve
    "经过角度很小的弯道之后来到了宽阔的直路上，铃一下子将油门转把拧到了最大。"
    "还是一成不变的驾驶模式呢，我拼命地抱紧了铃的腰。"
    "这种状态下，连害羞害臊什么的都顾不上了。"
    window hide
    show expression "img/EVC_SU02A1@2x.png" as bg3 with dissolve
    志雄 "「……！！」"
    "摩托车不断地左右倾斜着，不一会儿就进入了沿海国道的直线路上"
    "这样是不是稍微可以喘息一下了呢。"
    window hide
    scene expression Solid("000") as bg1 with ImageDissolve("img/BG_MASK18@2x.png",1)
    #TODO
#ROUTINE_STA
#EFF_PRI 0
#EFF_STPC 0,EFF_NOSKIP
#EFF_STAC 0,MOTOR_RIDE_IJ,EFF_NOSKIP
#ROUTINE_STP
    scene expression "img/EVC_SU02A1@2x.png" as bg3:
        block:
            align (.5,.5)
            parallel:
                linear 0.03 xalign 0.53
            parallel:
                linear 0.03 yalign 0.53
            repeat
    show expression "img/Motor_IJ_BG@2x.png" as motor_eff_bg zorder -10
    show expression "img/Motor_IJ_Wall@2x.png" as motor_eff_wall zorder -8 at motor_eff_movein:
        yanchor 0.0
        ypos 0.27
    show expression "img/Motor_IJ_Wall@2x.png" as motor_eff_wall2 zorder -8 at motor_eff_moveout:
        xanchor 0.0
        ypos 0.27
    "完全出乎意料的是这之后立刻进入了高速公路，两旁景色向后飞驰而去的速度越来越快。"
    志雄 "「铃啊啊啊啊啊啊啊！真的请你小心一点呀啊啊啊啊啊啊啊！」"
    "我最大限度地大声疾呼着，不过最后也只是徒劳的抵抗。"
    "这个时候，我稍微转过头看了看侧方的景象，那边是被晨曦照耀着的大海。"
    志雄 "「哦……」"
    "引擎的轰鸣声与撕开空气一般的风声交织在一起，在如此的背景音衬托下这样的景色也不错啦。"
    "不过，我刚想稍微安心地看一看这幅景象……"
    window hide
    stop se fadeout 1
    stop music
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop music
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/BG84AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_19L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,64
    play music "OBGM18"
    志雄 "「呃～～」"
    "用力地舒展了一下身体，活动了一下脖子。"
    "从公寓出来之后走了大概一个小时左右，我们在高速公路的休息区稍作休息。"
    志雄 "「天气有些热呢」"
    "因为休息区是临海而建，所以太平洋海面的景色可以尽收眼底。太阳缓缓升起，开始在海面上泼洒下绚丽的光波。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+96)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU044"
    铃 "「是啊」"
    "铃从商店里买来了罐装咖啡和饭团。"
    志雄 "「谢谢。不过为什么是咖啡？」"
    "这样与饭团的组合，还真是让人无法理解呢。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA06"),"True","img/SU_LCA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU045"
    铃 "「嗯？要说驾车远游的话搭配不就是咖啡吗」"
    "铃则是用一副仿佛在说“你在说什么呢啊”的表情回答着。"
    "是、是这样的吗？"
    "真是不太理解骑摩托车的人的思路啊……"
    志雄 "「虽然事到如今才问有些晚，不过咱们是去哪里啊？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC04"),"True","img/SU_LCC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU046"
    铃 "「我没说吗？」"
    志雄 "「完全没说……嘛，我也真是的，问都没问就跟着来了」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA01"),"True","img/SU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    if not persistent.dictlist[48] and persistent.show_dict:
        $persistent.dictlist[48]=True
        show screen dict_pop(i=48)
    voice "NSU07A_SU047"
    铃 "「去温泉哦。一个叫龙境温泉的地方。文子婆婆介绍给我的温泉旅店」"
    志雄 "「温泉吗……也好。我反正也没有什么特别想去的地方」"
    voice "NSU07A_SU048"
    铃 "「啊，那里不止是温泉哦。虽然旅店在山里，不过附近好像有一个湖呢」"
    志雄 "「诶，那具体来说要取材什么呢？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA03"),"True","img/SU_LCA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU049"
    铃 "「啊？取材？」"
    志雄 "「呃？」"
#CHR_GET_POSC 0,F24,F25
#RSUB F24,(320)
#BG_LAY 3,SU_LXB04,2,F24
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB04"),"True","img/SU_LCB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NSU07A_SU050A"
    铃 "「啊！啊，嗯。那个，{w=3}{nw}"
#THREAD_STP 1
    hide bg3 with dissolve
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB05"),"True","img/SU_LCB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU050B"
    extend "想观察的是温泉旅店……呢。要是也能多了解那样的街道的气氛与感觉就好了呢」"
    志雄 "「……」"
    "真的是要去取材才旅行的吗？只要不是快截稿了所以逃跑了就行。"
    "要真是那样的话，之后一定会被莉莉丝埋怨的……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC02"),"True","img/SU_LCC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU051"
    铃 "「啊，要是也能看到女招待的话就更好了。这可是好好工作了哦？」"
    志雄 "「嘛，这虽说是为了取材的旅行，也不是说不能开开心心地度过啦」"
    "大概，我也毫无疑问想和铃进行一次愉快的旅行吧。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC01"),"True","img/SU_LCC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU052"
    铃 "「说得好呢。虽然是工作也尽量要享受其中才好呢」"
    志雄 "「这个我能理解呢。去年的时候克罗艾学姐也这么说过的呢」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "听了我的话，铃露出了很满足的微笑，然后将咖啡一饮而尽。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU053"
    铃 "「那么，已经休息好了的话就出发吧。接下来从这里将直接开到目的地，要好好补充好水分哦。"
    志雄 "「明白。啊，我先去趟洗手间好了」"
    window hide
#SE_VOLC 1,0
    stop music fadeout 1
#FADE_OUT 1
    pause (32/32.0)
#SE_VOLC 1,64
    stop music
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SCA01"),"True","img/SU_SCA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_IN 1
    "我很快回到停车场，看到铃的长发在空中随风飘舞，心情舒畅地享受着阳光与海风。"
    "真是如画的光景啊。"
    voice "NSU07A_XQ000"
    バイカー "「真是罕见的摩托啊，进口车吗？」"
    "看来被此情此景吸引的不只是我呢。貌似也是驾车远游的一个男人向铃搭话了。"
    voice "NSU07A_SU054"
    铃 "「啊，是的。意大利产的车哦」"
    voice "NSU07A_XQ001"
    バイカー "「诶～多少ｃｃ？」"
    window hide
    play music "OBGM14"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SCA05"),"True","img/SU_SCA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU055"
    铃 "「９００的」"
    "虽然我想都是骑摩托车的应该很有话题才对，不过铃的心情看起来好像很糟糕的样子。"
    voice "NSU07A_XQ002"
    バイカー "「诶～、接下来要去哪里啊？我们接下来要去伊豆那边呢」"
    voice "NSU07A_SU056"
    铃 "「是吗……」"
    "难道这是假借摩托的话题来搭讪的？"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "立刻插到他们当中":
            $F7=0
        "远远地看着":
            $F7=1
    if F7==0:
        jump L_NSU07A_SEL01_A
    if F7==1:
        jump L_NSU07A_SEL01_B
label L_NSU07A_SEL01_A:
    $F4+=1
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
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA05"),"True","img/SU_LCA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「慢着！」"
    "我情绪激动地喊着，三步并作两步地跑了回来。"
    voice "NSU07A_SU057"
    铃 "「欢迎回来……那么我们要走了哦」"
    voice "NSU07A_XQ003"
    バイカー "「啊，那再见了」"
    stop music
    "好像因为我的登场放弃了找铃的样子，搭讪的人就这么离开了。"
    voice "NSU07A_SU058"
    铃 "「呼……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "轻轻叹了口气的铃，面带笑容地转过来看向我。"
    voice "NSU07A_SU059"
    铃 "「这么快回来真是得救了啊」"
    志雄 "「果然是搭讪吗？」"
    window hide
    play music "OBGM18"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC04"),"True","img/SU_LCC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU060"
    铃 "「嗯。骑摩托的女生很少呢。所以无论如何都会要搭两句话的」"
    "嗯……虽然我觉得理由其实不止这些。"
    "这样如画般的美人，任谁都会在意的吧。"
    voice "NSU07A_SU061"
    铃 "「喜欢摩托的人虽然没什么，不过像刚才那样摩托怎样都好，只是想约出去玩的人我可是很讨厌呢」"
    志雄 "「这么说的话，你很清楚是怎么回事呢啊？」"
    "对我的询问、铃微微地点了点头叹息道。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC02"),"True","img/SU_LCC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU062"
    铃 "「对于我来说想结交喜欢摩托的同伴的话，还是希望对方骑摩托能骑得很好才行呢」"
    志雄 "「原来如此呢」"
    voice "NSU07A_SU063"
    铃 "「而且……」"
    志雄 "「嗯？」"
    play sound "SE05_01"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA07"),"True","img/SU_LCA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU064"
    铃 "「难得的二人旅行，不能让别的事情来打扰嘛」"
    志雄 "「诶？」"
    "因为和海风的声音掺杂在一起，我没能听清楚铃的话。"
    stop se fadeout 1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU065"
    铃 "「那么，还有一小会儿！抓紧时间咱们出发吧」"
    志雄 "「知道了。不过，拜托你再多注意一下安全驾驶哦」"
    jump L_NSU07A_SEL01_X
label L_NSU07A_SEL01_B:
    "那种搭讪男，铃靠自己也能搞定的吧。"
    "而且之后要是开始讲摩托的各种话题的话，也不该打扰呢……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SCC03"),"True","img/SU_SCC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「啊」"
    "在这一刻，我与铃的视线重合了。"
    "……生气了吗？"
    "看起来非常不高兴的样子，像是要责备一般地盯着我看。"
    voice "NSU07A_SU066"
    铃 "「啊，我朋友来了……抱歉了」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "铃把一直拼命找话题搭话的那个男的利落地晾在了原地。"
    "那个男的一副很遗憾的表情，黯然地离开了。"
    "铃可真过分啊。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA05"),"True","img/SU_LCA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU067"
    铃 "「志雄。看到了就来帮我解围啊」"
    志雄 "「可是好像没有我出场的机会啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA02"),"True","img/SU_LCA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU068"
    铃 "「并不在说这个」"
    志雄 "「……？」"
    voice "NSU07A_SU069"
    铃 "「一起的女生遭遇了那种情况，你是不是应该想些什么啊」"
    志雄 "「那个……」"
    "肯定不是什么好事就是了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA05"),"True","img/SU_LCA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU070"
    铃 "「虽然我自己也能应对，但是还是希望你可以来帮助我啊」"
    志雄 "「抱歉」"
    "是啊。现在不是随随便便转换心情的时候。"
    "作为男人，当然还是要守护对自己来说最重要的人。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA01"),"True","img/SU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU07A_SU071"
    铃 "「……没有，我也是对小事太过在意了呢。好不容易的机会还是开开心心地出发吧」"
    志雄 "「好的」"
    "铃为了改变气氛发出了洪亮的声音，我也应声答道。"
    "不更加积极地去努力的话……"
    "我一边跨上摩托车的座位，一边下定了新的决心。"
    jump L_NSU07A_SEL01_X
label L_NSU07A_SEL01_X:
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE06_47L"
    pause (256/32.0)
    #TODO
#BG_INIC 3
    #show expression "img/BG_WHITE@2x.jpg" as bg1 with dissolve
#ROUTINE_STA
#BG_POSC 3,30,-60,749,450
#EFF_PRI 0
#EFF_STAC 0,MOTOR_RIDE_IJ,EFF_NOSKIP
#ROUTINE_STP
    scene expression "img/EVC_SU02A1@2x.png" as bg3:
        block:
            align (.5,.5)
            parallel:
                linear 0.03 xalign 0.53
            parallel:
                linear 0.03 yalign 0.53
            repeat
    show expression "img/Motor_IJ_BG@2x.png" as motor_eff_bg zorder -10
    show expression "img/Motor_IJ_Wall@2x.png" as motor_eff_wall zorder -8 at motor_eff_movein:
        yanchor 0.0
        ypos 0.27
    show expression "img/Motor_IJ_Wall@2x.png" as motor_eff_wall2 zorder -8 at motor_eff_moveout:
        xanchor 0.0
        ypos 0.27
    hide bg1 with dissolve
    pause (128/32.0)
    show expression "img/EVC_SU02A2@2x.png" as bg3 zorder 3 with dissolve
    pause (128/32.0)
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music
#FADE_OUT 1
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop se
    stop sound
    stop music
    $ renpy.end_replay()
#FADE_IN 0
    return
#label THREAD_QUA_CHR0_WIN
#TH_QUA_CHR_WIN
#EOT
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT