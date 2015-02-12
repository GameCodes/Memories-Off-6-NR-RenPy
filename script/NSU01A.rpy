label NSU01A:
    $currentlabel = "NSU01A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
#label DSTART
#SCRMODE SCR_WINDOW,5
    window hide
#FADE_OUT 0,0
    scene expression Solid("000") with fade
#FADE_IN 0,0
#label START
    $month = '07'
    $day = '17'
    $date = '1'
    window hide
#FADE_OUT 0,0
    scene expression Solid("000") with fade
#FADE_IN 0,0
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/NIMG19D-568h@2x.jpg" as bg1 with fade
    pause
    hide bg1
    with dissolve
#FADE_OUT 0,0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_ALPC 0,0
#BG_SETC 0,BG15MA
#CHR_PAL_BGC ID_ALL,BG15MA
    play sound "SE05_14L"
    pause (32/32.0)
#FADE_IN 1,32
    play music "OBGM13"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            savestr="auto-"+str(persistent.auto_slot)
            renpy.save(savestr)
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    show expression "img/NIMG03A@2x.jpg" as bg_over zorder 5
    show expression "img/SU_ZDC05A@2x.png" as lh0 zorder (10-0):
        xcenter ((320)/640.0)
    with dissolve
#BG_ALPC 0,128
    志雄 "「…………」"
    "唔——。"
    "不得不承认，我在技术和腕力上都不是她的对手。"
    "我默默地用视线与压制着我的作家老师对抗着。"
    志雄 "「……（都已经是成年人了，就要认真履行自己的责任啊）」"
    if not persistent.dictlist[6] and persistent.show_dict:
        $persistent.dictlist[6]=True
        show screen dict_pop(i=6)
    志雄 "「……（原本没能遵守截稿日期的不正是铃么）」"
    志雄 "「……（所以说，即使来到这里，也解决不了什么问题吧？）」"
    志雄 "「……（我相信铃是个言出必行的人）」"
    "差不多过了十秒钟。"
    window hide
#SE_VOLC 1,0,64
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB02"),"True","img/SU_ZDB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play music "BGM10"
    "铃目不转睛地注视着我的双眼，随即微微一笑。"
    "她终于理解了吗……"
#SE_VOLC 1,(64/2),64
#MUS_VOL 0,32
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB01"),"True","img/SU_ZDB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_SU000"
    铃 "「怎么了？想拍垫认输的话，就在垫子上叩两下吧」"
    "……压根没明白嘛。"
    "还以为这样就能解决问题了，如此认为的自己真是个笨蛋。"
    志雄 "「那个……这种事情是不应该的吧」"
    voice "NSU01A_SU001"
    铃 "「唔，这样吧，如果能把我藏起来别让那个魔鬼志愿者编辑找到，就松开你好了」"
    志雄 "「……」"
#SE_STPC 1,64
#MUS_VOL 128,64
    play sound "SE00_44"
    if not persistent.dictlist[0] and persistent.show_dict:
        $persistent.dictlist[0]=True
        show screen dict_pop(i=0)
    voice "NSU01A_RI000"
    莉莉丝 "「志雄～！你在３０秒之内给我站起来，让我踢两脚！否则我就要强制执行了！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB02"),"True","img/SU_ZDB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_SU002"
    铃 "「好了好了，放开你吧，不过我的事情要保密哦！」"
    "铃露出了亲切的微笑。"
    "一如既往，那灿烂的笑容沁人心脾。"
    "……如果没有对我施加关节技的话。"
    志雄 "「我知道了……再这样闹下去的话，我也很难办的」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC01"),"True","img/SU_ZDC01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_SU003"
    铃 "「我相信你哟」"
    "她只有在这种时候才会露出认真的表情，这不禁让我感到为难……"
    voice "NSU01A_RI001_K"
    莉莉丝 "「志雄～！！」"
    window hide
    play sound "SE03_46"
    hide lh1
    hide lh2
    hide lh3
    hide lh4 with dissolve
    pause (32/32.0)
#BG_NOEFFECT 0
    show expression "img/BG15MA@2x.jpg" as bg0
    voice "NSU01A_RI001_K"
    莉莉丝 "「志雄～！！」"
    window hide
    play sound "SE00_50"
    pause (64/32.0)
    志雄 "「啊——真是的，请适可而止一点」"
    window hide
    show expression "img/OIBG012A@2x.png" as bg0 zorder 10
#CHR_PAL_BGC ID_ALL,OIBG012A
    play sound "SE00_00"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320),0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD04"),"True","img/RI_MBD04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    志雄 "「我说你呀，多多少少也应该知道，这样会吵到邻居的……」"
    play sound "SE01_13"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD04"),"True","img/RI_LBD04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    "我正要开口抱怨，她纤细的身躯却从我身边轻轻滑过，自顾自地准备走进房间里去。"
    志雄 "「啊，等等！要去哪啊！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD02"),"True","img/RI_LBD02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#SET_SAVPNT
#THREAD_STA 1,THREAD_RIRISU_COMEUP
    voice "NSU01A_RI002"
    莉莉丝 "「啊～够了！闪开！」"
#MESA A_CH_RI,NSU01A_RI002,"【りりす】「啊～够了！闪开！」"
#THREAD_WAT 1
#MESX "%K%P"
#CLR_SAVPNT
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD02"),"True","img/RI_LBD02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        parallel:
            linear 1 zoom 1.5
        parallel:
            linear 1 alpha 0
        parallel:
            linear 1 xcenter 0.2
        parallel:
            linear 1 ycenter 0.8
    pause 1.0
#CHR_ALPC 0,128
#CHR_SCLC 0,256,256
    if not persistent.dictlist[1] and persistent.show_dict:
        $persistent.dictlist[1]=True
        show screen dict_pop(i=1)
    "莉莉丝光速般脱掉了鞋，不顾我的阻拦，径直走了进去。"
    "这样下去的话，铃和莉莉丝就会碰上了。"
    "到那时候，我就会因为藏匿罪而变成莉莉丝脚下的牺牲品……！"
    志雄 "「喂、喂！等等啊！」"
    scene expression "img/BG15MA@2x.jpg" as bg_over zorder 5
    show expression "img/RI_MBC05A@2x.png" as lh0 zorder (30-0):
        xcenter ((320+160)/640.0)
    with dissolve
    voice "NSU01A_RI011"
    莉莉丝 "「咦？我觉得她应该在这里啊……」"
    "莉莉丝追到了房间里，正慌乱地翻弄着我的被窝。"
    志雄 "「不、不可能在这里啊？我直到刚才还在睡觉」"
    "房间里没有铃的身影。"
    "大概是在我走向玄关的时候，她回到了自己的房间。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD04"),"True","img/RI_MBD04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_RI012"
    莉莉丝 "「好奇怪啊～」"
    window hide
    hide lh1
    hide lh2
    hide lh3
    hide lh4 with dissolve
    play sound "SE03_65"
    "莉莉丝似乎无法接受这一事实，时而窥视桌底，时而又去查看窗帘背面，在房间里不停地闹腾。"
    "真是的，铃也好，莉莉丝也罢，为什么我身边的女孩子全都那么随便……"
    window hide
#SE_STPC 0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96),0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD03"),"True","img/RI_MBD03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    voice "NSU01A_RI013"
    莉莉丝 "「真是的～铃，肯定是还没动笔。明明我那么期待着，结果不得不从早上就开始郁闷～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD05"),"True","img/RI_MBD05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_RI014"
    莉莉丝 "「我现在的心情，也想分给志雄点啊」"
    "恕我拒绝您的“好意”。"
    "话说回来，从卷入纠纷的这一刻开始，感到相当郁闷的应该是我才对。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA05"),"True","img/RI_MBA05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_RI015"
    莉莉丝 "「哈～啊」"
    "莉莉丝一边叹着气，一边用锐利的目光盯着我。"
    voice "NSU01A_RI016"
    莉莉丝 "「即使如此，这也是个相当悠闲的早晨吧，学生会长先生？」"
    志雄 "「今天是休息日，放轻松点没什么问题吧？我又没有什么截稿日之类的事」"
    if not persistent.dictlist[3] and persistent.show_dict:
        $persistent.dictlist[3]=True
        show screen dict_pop(i=3)
    voice "NSU01A_RI017"
    莉莉丝 "「是么？如果是克罗艾学姐的话，就算是节假日期间也会早早地到学校工作呢」"
    志雄 "「呃……」"
    志雄 "「克、克罗艾学姐是例外！那个人模仿不来的」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA06"),"True","img/RI_MBA06A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_RI018"
    莉莉丝 "「一开始就放弃的话，什么都做不成了」"
    志雄 "「我知道我知道，总而言之，我要换衣服了，你先出去吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD04"),"True","img/RI_MBD04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_RI022"
    莉莉丝 "「那么突然，想干嘛啊」"
    志雄 "「照莉莉丝说的，向克罗艾学姐那样努力学习」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD01"),"True","img/RI_MBD01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_RI023"
    莉莉丝 "「临阵磨枪可不好呢」"
    志雄 "「那你到底想要我怎么样啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD04"),"True","img/RI_MBD04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_RI024"
    莉莉丝 "「而且没必要这么着急地把我赶出去吧？」"
    "莉莉丝完全不打算出去。这家伙莫非是想监视我的房间，把铃揪出来？"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD03"),"True","img/RI_MBD03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    if not persistent.dictlist[5] and persistent.show_dict:
        $persistent.dictlist[5]=True
        show screen dict_pop(i=5)
    voice "NSU01A_RI025B"
    莉莉丝 "「原本以为好不容易有了值得一看的书，现在却看不到了，铃代老师也逃走了，你就没有丝毫安慰你那受到伤害的青梅竹马的心情吗……」"
    志雄 "「很可惜，一丝一毫也没有。再说了，你如果是粉丝的话就不要总是给老师添麻烦」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA06"),"True","img/RI_MBA06A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_RI026"
    莉莉丝 "「哪有这回事。我和她约好的，写完就给我看的啊」"
    志雄 "「所以说，你一大早就来打扰我……」"
    window hide
    stop music
#FADE_OUT 1,32
#BG_COLC 0,0,0,0,128
    scene expression Solid("000") with fade
#MUS_STP 
#FADE_IN 0,0
    "结果，在那之后我足足花了３０分钟才说服莉莉丝回去。"
    "饶了我吧，明明是难得的休息日啊……"
    window hide
#FADE_OUT 0,0
#BG_COLC 0,128,128,128,128
#FADE_IN 1,32
    志雄 "「累死了……」"
    "确认莉莉丝已经回去之后，睡意顿时袭来。"
    window hide
    play sound "SE03_07"
    show expression "img/NIMG03A@2x.jpg" as bg0
    志雄 "「呼……好困……」"
    "我躺在被窝里，渐渐闭上了眼睛……"
    window hide
    
#FADE_OUT 1,64
    scene expression Solid("000") with fade
#SE_STPC 0
#BG_SET_BACK 
#BG_INIC 0
#BG_SETC 0,NIMG03A
#BG_COLC 0,0,0,0,128
#FADE_IN 0,0
    志雄 "「……」"
    志雄 "「……嗯……」"
    window hide
#FADE_OUT 0,0
#BG_COLC 0,128,128,128,128
    play sound "SE06_29L"
#FADE_IN 1,64
    play sound "SE03_28"
    show expression "img/BG15MA@2x.jpg" as bg0
#CHR_PAL_BGC ID_ALL,BG15MA
    志雄 "「不好，我睡着了！？现在几点了？」"
    voice "NSU01A_SU004A"
    铃 "「你睡了差不多３０分钟吧？」"
    window hide
#SE_STPC 1,32
    play sound "SE03_90"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320),0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MEA01"),"True","img/SU_MEA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play music "BGM05"
    志雄 "「哎？真的呢，铃？」"
    "看了下手机上的时间，果真睡了整整３０分钟。"
    "这时，饭菜的香味迎面飘来。"
    voice "NSU01A_SU005"
    铃 "「再稍等一下，早饭马上做好」"
    "享受着轻拂脸颊的微风，我将窗户稍稍打开，向外望去。"
    "刚刚回去了的铃，大概又是从那里进来了吧。"
    "……这么说来，她巧妙地从莉莉丝的视线中逃脱了嘛。"
    志雄 "「啊，做饭什么的让我……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MEB02"),"True","img/SU_MEB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_SU006"
    铃 "「没事没事，这种时候就别那么客气了」"
    志雄 "「真的不用了，你都那么忙……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MEA05"),"True","img/SU_MEA05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_SU007"
    铃 "「别说了！现在不用考虑那些事情」"
    志雄 "「……知道了。就听老师您的指示」"
    "听到我故意称呼她「老师」，铃皱紧了眉头，叹了口气。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MEA01"),"True","img/SU_MEA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_SU008"
    铃 "「唉，总觉得是自作自受」"
    voice "NSU01A_SU009"
    铃 "「先不说这些，还是赶快把衣服换好，把脸也洗了，在我把早饭准备好的这段时间里」"
    志雄 "「嗯」"
    window hide
#FADE_OUT 1,32
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_SETC 0,BG33AA
#CHR_PAL_BGC ID_ALL,BG33AA
#FADE_IN 1,32
    "我洗了脸，换上制服，只见餐桌上摆放着米饭、味噌汤以及昨天剩下的菜肴。"
    "朴实却又美味的菜肴香味弥漫在空气中。"
    show expression "img/EXBG09A@2x.jpg" as bg_over zorder 5
    show expression "img/SU_ZEB01A@2x.png" as lh0 zorder (30-0):
        xcenter ((320)/640.0)
    with dissolve
    voice "NSU01A_SU010"
    铃 "「我开动了」"
#MESA A_CH_SU+A_CH_SI,NSU01A_SU010,"【鈴・志雄】「我开动了」%K%P"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZEC04"),"True","img/SU_ZEC04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_SU011"
    铃 "「嗯——味噌汤稍微有点咸吧？」"
    志雄 "「是么？这种咸味反而适合下饭」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZEC02"),"True","img/SU_ZEC02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_SU012"
    铃 "「那就好，自己大概是太累了，想吃点味道重一点的东西」"
    志雄 "「看起来真是相当的累呢」"
    voice "NSU01A_SU013"
    铃 "「要说的话也就是和平时一样吧，嘛，刚才你也看到了，姑且有所行动就好了」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZEC01"),"True","img/SU_ZEC01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_SU014"
    铃 "「比起这些，志雄这边怎么样了？」"
    志雄 "「我？」"
    voice "NSU01A_SU015"
    铃 "「备考的复习也差不多接近尾声了，学生会那边也有事吧？」"
    if not persistent.dictlist[53] and persistent.show_dict:
        $persistent.dictlist[53]=True
        show screen dict_pop(i=53)
    志雄 "「这个啊，学生会的后辈们都很努力。不过，差不多也该考虑奏云祭的事情了」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZEC05"),"True","img/SU_ZEC05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_SU016"
    铃 "「奏云祭的准备？太早了吧？」"
    "被称为所谓文化祭的奏云祭是在十月举行。"
    "的确，如果对于一般的学生，在这个时候就开始准备似乎早了些。但作为举办方，提早做准备是理所应当的。"
    志雄 "「在各班决定执行委员之前，还有许多必须决定的事情」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZEC01"),"True","img/SU_ZEC01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_SU017"
    铃 "「嗯～，去年好像准备得挺慌乱的啊」"
    志雄 "「所以要反省啊。今年为了即使发生意外也不会手忙脚乱，想把日程安排得充裕一些」"
    "去年直到开幕前才发现预算工作做得一团糟，真是有够麻烦的……"
    "我觉得如果不是因为大家的齐心协力，一定会无法收场的。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZEC06"),"True","img/SU_ZEC06A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_SU018"
    铃 "「充裕的日程安排……真是值得赞美的口号」"
    "截稿日期真的很悬么？铃的眼神看上去有些空虚。"
    志雄 "「总之，不管结果怎样，接下来都要拿出自信来。至少我这边想要预先规划一下。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZEC02"),"True","img/SU_ZEC02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_SU019"
    铃 "「但是这样的话，暑假里准备工作会非常忙的吧？」"
    志雄 "「不至于吧？这次是以整体管理这样的工作为主，我认为不会像去年那么慌乱的……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZEC01"),"True","img/SU_ZEC01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_SU020"
    铃 "「真的没关系么～？这可不是悠闲地和我一起吃饭的时候啊？」"
    志雄 "「后辈们为我努力地工作，所以在休息日还是可以悠闲一点的」"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2,0
#BG_UVC 2,0,512,640,448
#BG_SETC 2,BG09AA
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1,0
#CHR_POSC 1,(320),0
#CHR_SETC 1,YU_LAB01
#BG_INIC 1
#BG_PRI 1,0
    show expression Solid("fff") as bg1
    with ImageDissolve("img/BG_MASK15@2x.png",1)
    show expression "img/BG09AA@2x.jpg" as bg2 zorder 20
    show expression "img/YU_LAB01A@2x.png" as lh1 zorder (30-1)
#CHR_PAL_BGC ID_ALL,BG09AA
#BG_ALPC 0,0
#BG_ALPC 2,128
#CHR_ALPC 0,0
#CHR_ALPC 1,128
#BG_BLUR 2,1
    hide bg1 with dissolve
#CHR_SETC 0,SU_ZEA06
    if not persistent.dictlist[4] and persistent.show_dict:
        $persistent.dictlist[4]=True
        show screen dict_pop(i=4)
    "实际上，多亏了春日他们这些学生会会员的努力，我的负担比想像中要少得多。"
    "去年虽然几乎是克罗艾学姐一个人在做，但对我而言学习这一点是很困难的。"
    "虽然大家是齐心协力没错，不过也要认真地分担各自的任务，这就是我作为学生会会长最初执行的方案。"
    window hide
#BG_INIC 1
#BG_PRI 1,0
    show expression Solid("fff") as bg1
    hide bg2
    hide lh1
    with ImageDissolve("img/BG_MASK15@2x.png",1)
#BG_UVC 2,0,0,640,448
#CHR_PAL_BGC ID_ALL,EXBG09A
#BG_ALPC 0,128
#CHR_ALPC 0,128
    hide bg1 with dissolve
    voice "NSU01A_SU021"
    铃 "「话是这么说，可也是在依靠别人啊～」"
    志雄 "「嗯……至少算是相互信赖吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZEB02"),"True","img/SU_ZEB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_SU022"
    铃 "「是啊，毕竟是学生会会长，差使别人也是工作的一部分，不算过分嘛」"
    "说着，铃微微地笑了。"
    "时不时会在我面前露出的这种姐姐般的侧脸，真的让人感觉很狡猾……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZEB01"),"True","img/SU_ZEB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_SU028"
    铃 "「真是的，好不容易刚刚营造起气氛就被破坏掉了。快点吃吧，不要管我了」"
    志雄 "「哎？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZEA02"),"True","img/SU_ZEA02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_SU029"
    铃 "「等下要有个碰头会」"
    志雄 "「这么早啊？」"
    "听我这么一说，铃深深地叹了口气。"
    "不过，原稿还没有完成就开什么碰头会的话，也只能叹气了。"
    志雄 "「那饭后的收拾就由我来做吧，铃你必须快去准备了」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZEA01"),"True","img/SU_ZEA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "NSU01A_SU032"
    铃 "「是么？那就拜托了」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4 with dissolve
    play sound "SE03_53"
    "铃匆忙收拾好碗筷放入水池里，从窗户钻回自己的房间。"
    志雄 "「……为什么不正常点从大门走回去啊」"
    "我一边胡思乱想着这些事情，一边夹起咸菜放入口中嚼着。"
    "一如既往的日子……一度消失的铃回来之后，我们又像原来一样，恢复到了房东与房客之间的关系。"
    "这样的日常，在觉得很好的同时，也感觉有什么缺憾之处……"
    window hide
#SE_STPC 0,64
#SE_STPC 1,64
    stop music
#FADE_OUT 1,128
    scene expression Solid("000") with fade
#GRAPH_INI 
#SE_STPC 0
#SE_STPC 1
#MUS_STP 
#FADE_IN 0,0
    $ renpy.end_replay()
    return
#label THREAD_RIRISU_COMEUP
#CHR_SCL_AUTOC 0,384,384,1,F123,48,0
#CHR_POS_AUTOC 0,(320-192),(192),1,F123,48,0
#CHR_ALP_AUTOC 0,0,1,F123,48,1
#CHR_SCL_SAVEC 0
#CHR_POS_SAVEC 0
#CHR_ALP_SAVEC 0
#EOT