label NRI17A:
    $currentlabel = "NRI17A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '31'
    $date = '1'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 6,CAL_0731
    show expression "img/NIMG15K-568h@2x.jpg" as cal zorder 5
    show expression "img/07_30_SUNDAY@2x.png" as cal_date zorder 6:
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
    play sound "SE03_65"
    voice "NRI17A_RI000"
    莉莉丝 "「没有……怎么办……」"
    "嗯？"
    voice "NRI17A_RI001"
    莉莉丝 "「在包里吗……？」"
    window hide
    play sound "SE03_88"
    play sound "SE03_66"
    voice "NRI17A_RI002"
    莉莉丝 "「果然没有……」"
    "怎么了？　真吵……"
    "我慢慢睁开沉重的眼皮。"
    window hide
#FADE_OUT 0
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG63MA2@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG63MA2@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XEA04"),"True","img/RI_XEA04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#BG_BLUR 0
#FADE_IN 1
    play music  "BGM11"
    "就在躺着的我的身旁，莉莉丝有些不知所措。"
    志雄 "「……怎么了，莉莉丝？」"
    "莉莉丝在摸索着旅行用的包。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XEA01"),"True","img/RI_XEA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI17A_RI003"
    莉莉丝 "「啊，志雄。对不起，把你吵醒了？」"
    志雄 "「啊，没关系……反正马上就要到起来的时间了。」"
    志雄 "「对了，你在找什么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XEB04"),"True","img/RI_XEB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI17A_RI004"
    莉莉丝 "「啊，没有，没什么。」"
    window hide
    play sound "SE03_88"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "说着，把之前一直在找的包的拉链拉了起来。"
    志雄 "「在找东西吗？　我来帮你吧？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MEA04"),"True","img/RI_MEA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI17A_RI005"
    莉莉丝 "「不用了，真的没什么，没事的。」"
    voice "NRI17A_RI006"
    莉莉丝 "「比起这个，还是先快点起来吧？　早饭都快要被收掉了。」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "被莉莉丝这么一说我看了眼时间，与其说是早晨，不如说已经快中午了。"
    志雄 "「哇，还真是的。」"
    window hide
    "我急忙从被子里钻出来，朝洗手间去洗脸。"
    志雄 "「你也快点换好衣服准备准备吧？」"
    "对我抱怨的同时，莉莉丝也只是穿了一件睡衣而已。"
    voice "NRI17A_RI007"
    莉莉丝 "「啊，那个，没关系。我今天不吃早饭了。」"
    志雄 "「嗯？　为什么啊？」"
    voice "NRI17A_RI008"
    莉莉丝 "「啊、哎，那个，我脚还有点疼，去食堂有点……」"
    志雄 "「没事吧！？　让我看看你的脚。」"
    window hide
#FADE_OUT 0
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG63MA2@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG63MA2@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MEA03"),"True","img/RI_MEA03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_IN 1
    "我嘴里还塞着牙刷，准备看看莉莉丝的脚——"
    stop music fadeout 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MEA05"),"True","img/RI_MEA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI17A_RI009"
    莉莉丝 "「变、变态！」"
    play sound "SE04_06"
    with vpunch
    志雄 "「呜哇！？」"
#THREAD_STA 1,THREAD_QUA_WIN
#VIB_DOKA 
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESA A_CH_SI,"【志雄】「呜哇！？」"
#THREAD_WAT 1
#WIN_POS 0,0
#VIB_STP 5
#MESX "%K%P"
    play music  "BGM12"
    "这踢腿的力量……怎么说呢，和往常一样……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MED03"),"True","img/RI_MED03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI17A_RI010"
    莉莉丝 "「啊……对、对不起，一不小心就……」"
    志雄 "「真是的……我又不是别有用心才碰你的。要是扭伤了就不好了，我只是想看看有没有肿起来而已。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MED04"),"True","img/RI_MED04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI17A_RI011"
    莉莉丝 "「突然把手伸向别人的脚，谁都会吃惊的！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MED05"),"True","img/RI_MED05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI17A_RI012"
    莉莉丝 "「而且，也不是有什么大不了的伤啦。」"
    志雄 "「是吗……不过这样的话，我把早饭拿到房间里来就行了吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MEB01"),"True","img/RI_MEB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI17A_RI013"
    莉莉丝 "「不、不用了。为了我让你这么操心，我会过意不去的。还会被稻穗说三道四的……」"
    志雄 "「嗯……」"
    voice "NRI17A_RI014"
    莉莉丝 "「所以，不用在意我，一个人去吃饭吧。」"
    志雄 "「既然莉莉丝这么说的话……」"
    window hide
    play sound "SE00_47"
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG62AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression Solid("000") with None
#FADE_IN 0
    "然后我换好衣服之后，就像被莉莉丝赶出来一样离开了房间。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128
    scene expression "img/BG62AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    play sound "SE00_48"
    志雄 "「……到底怎么了？　莉莉丝这家伙……」"
    "我知道她只是不想让我待在房间里。"
    "只不过我不知道理由而已。"
    "刚才似乎在找什么东西，果然是因为这个原因吗……？"
    志雄 "「总之……拿点莉莉丝能吃的东西回去吧。」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG63MA1@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG63MA1@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    play sound "SE00_47"
#FADE_IN 1
    "迅速搞定早饭的我，拿着拜托食堂做的饭团和一些简单的菜朝房间走去。"
    "咦？　莉莉丝……？"
    志雄 "「喂～莉莉丝，不在吗？」"
    voice "NRI17A_RI015"
    りりす？ "「唔！？」"
    play sound "SE04_10"
#THREAD_STA 1,THREAD_QUA_WIN
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    voice "NRI17A_RI016"
    りりす？ "「好疼！？」"
#MESA A_CH_RI,NRI17A_RI016,"【りりす？】「好疼！？」"
#THREAD_WAT 1
#WIN_POS 0,0
#MESX "%K%P"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC06"),"True","img/RI_MBC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI17A_RI017"
    莉莉丝 "「好疼啊……」"
    "从纱门后，莉莉丝揉着脚走了出来。"
    voice "NRI17A_RI018"
    莉莉丝 "「呜呜……我撞到椅子了……」"
    志雄 "「没关系吧！？　……不过，你在这里干吗呀？」"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,RI_MXC03,2,F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC03"),"True","img/RI_MBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NRI17A_RI019"
    莉莉丝 "「没，没什么……只不过看到电视里播放的日常保健节目就……」"
    志雄 "「？」"
#REMOVE_REEK_CHR 0
#BG_ALP 3
#MESEX_A M_NOA,A_CH_SI,"【志雄】「？」%K%P"
    "可电视机并没有打开。"
    "果然莉莉丝有点奇怪……"
    志雄 "「啊，对了。我拜托食堂做了你的早饭，吃吗？」"
#REEK_CHR 0
    voice "NRI17A_RI020"
    莉莉丝 "「诶？谢谢……」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA01"),"True","img/RI_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "莉莉丝快速用手拿起一个饭团，大口吃了起来。"
    "什么嘛，还说不要早饭，果然已经饿扁了。"
    voice "NRI17A_RI021"
    莉莉丝 "「真好吃……捏的方式很恰当，饭团很松软。」"
    志雄 "「对了，今天怎么打算？」"
    "今天也是能在这里逗留的最后一天了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBC05"),"True","img/RI_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "『嗯？』莉莉丝含着饭团看着我。然后稍微有些慌张地朝口中送水。"
    voice "NRI17A_RI022"
    莉莉丝 "「那个，对呢……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE00_27"
    voice "NRI17A_YG000"
    雄吾？ "「喂～志雄、莉莉丝，我能进来吗？」"
    志雄 "「嗯，老爸？　没关系。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE00_47"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 1,(320-160)
#CHR_POSC 2,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    with dissolve
    voice "NRI17A_YG001"
    雄吾 "「哟，早上好。」"
    voice "NRI17A_KR000"
    香里 "「早上好，两位。」"
    "老爸和香里阿姨走进了房间。两人一起登场不禁使我联想到前天晚上的惨状。不过，现在还是中午应该不会喝吧。"
    志雄 "「有什么事吗？」"
    voice "NRI17A_YG002"
    雄吾 "「那个，我想问问看你们今天的预定。要是还没决定的话，我们趁着最后的机会一起去这附近的小镇逛一逛吧？」"
    voice "NRI17A_KR001"
    香里 "「对对。虽然去湖边或是山上的观光地也不错，不过有这难得的机会，还是想看一看当地的风景。」"
    志雄 "「说的也是呢……」"
    "说起来，以这种方式度过一天也不错呢。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBB01"),"True","img/RI_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「莉莉丝，怎么样？　我没问题。」"
    voice "NRI17A_RI023"
    莉莉丝 "「嗯……不了，今天我就在房间里休息好了。」"
    志雄 "「诶？」"
    志雄 "「怎么了？　果然脚还……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBB04"),"True","img/RI_LBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI17A_RI024"
    莉莉丝 "「啊，脚是有点问题，主要我有些不舒服。」"
    志雄 "「是吗？　那么我也……」"
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
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 1,(320-160)
#CHR_POSC 2,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    with dissolve
    志雄 "「对不起，老爸，香里阿姨。我今天不能一起去了。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_ALPC 0
#CHR_POSC 0,((320)+80)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA03"),"True","img/RI_LBA03A@2x.png") as lh0 zorder (100-0):
        ypos 0.0
    with dissolve
#BG_GET_NOC 0,F24
#BG_SET_BACK 
#BG_INIC 2
#BG_PRI 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
#BG_ALP_AUTOC 2,128,0,F24
#CHR_ALP_AUTOC 0,128,0,F24
#CHR_POS_AUTOC 0,F24
#BG_ALP_SAVEC 2
#CHR_ALP_SAVEC 0
#CHR_POS_SAVEC 0
#CHR_ERSWC 1
#BG_SWPC 0
    hide bg2 with dissolve
#BG_PRI 0
#BG_BLUR 0
#CHR_PRIC 0
    voice "NRI17A_RI025"
    莉莉丝 "「哇！　没关系的，志雄！　和妈妈她们一起去吧！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD04"),"True","img/RI_LBD04A@2x.png") as lh0 zorder (100+0):
        ypos 0.0
    with dissolve
    voice "NRI17A_RI026"
    莉莉丝 "「我没事的！」"
    voice "NRI17A_RI027"
    莉莉丝 "「比起这些，难得志雄还有你父亲一起来旅行。应该多花些时间一起度过吧？」"
    志雄 "「都现在了你要客气什么……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD02"),"True","img/RI_LBD02A@2x.png") as lh0 zorder (100+0):
        ypos 0.0
    with dissolve
    voice "NRI17A_RI028"
    莉莉丝 "「好了啦！　你去吧！」"
    "莉莉丝大声说道。被这么大声地催促，我连一点反驳的余地也没有。"
    志雄 "「……我，我知道了。我这就走。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SORT 1,0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 0,(320-192)
#CHR_POSC 1
#CHR_POSC 2,(320+192)
#CHR_DSPTC 0,1,2,KR_MAA06,SF_MAA06,RI_MBD02
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA06"),"True","img/KR_MAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA06"),"True","img/SF_MAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .5
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD02"),"True","img/RI_MBD02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .8
    with dissolve
    voice "NRI17A_YG003"
    雄吾 "「没关系吗？」"
    voice "NRI17A_KR002"
    香里 "「怎么了，莉莉丝？　肚子疼吗？」"
    "面对我和莉莉丝的争执，老爸和香里阿姨反而表现出一副担心的样子。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA04"),"True","img/RI_MBA04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI17A_RI029"
    莉莉丝 "「真的没事，不用担心。等我好些了再和你们会合。」"
    志雄 "「真的……没事吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD01"),"True","img/RI_MBD01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI17A_RI030"
    莉莉丝 "「好了好了，志雄也不要露出这种『对活着绝望了——！』的表情了。我只是在房间里休息一下而已。」"
    志雄 "「……啊啊」"
    "是……这样吧。"
    "不是什么值得担心的事吧……莉莉丝的身体状况也看不出多么差……我极力说服我自己。"
    voice "NRI17A_RI031"
    莉莉丝 "「好了，那么，大家走好。」"
    "像把我从房间里赶出来一样，莉莉丝在我们背后把我们往门那边推。"
    志雄 "「那我走了，有什么事马上打电话联系我。要是我来不及的话，还有稻穗在。」"
    voice "NRI17A_RI032"
    莉莉丝 "「嗯。我知道了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA06"),"True","img/KR_MAA06A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NRI17A_YG004"
    雄吾 "「那么莉莉丝，我们走了。」"
    window hide
    play sound "SE00_47"
    stop music fadeout 1
#FADE_OUT 1
#SE_WATC 0
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE00_48"
#FADE_IN 0
    voice "NRI17A_RI033"
    莉莉丝 "「终于走了……」"
    voice "NRI17A_RI034"
    莉莉丝 "「要趁现在做些什么才行……」"
    window hide
    stop sound fadeout 1
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG65AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG65AA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    stop sound
    pause (32/32.0)
    play sound "SE05_15L"
    pause (32/32.0)
#FADE_IN 1
    play music  "OBGM04"
    "我和老爸他们一起到山脚的街道转了转，然后在车站的椅子上休息片刻。"
    志雄 "「……」"
    "莉莉丝到底怎么了呢？　真的是身体不舒服吗？　还是说，有什么隐情呢……？　可是，瞒住我有什么意义呢……"
    voice "NRI17A_YG005"
    雄吾 "「你还是不放心吧，志雄？」"
    志雄 "「……」"
    "……是不能对我说的事吗？"
    voice "NRI17A_KR003"
    香里 "「志雄君？」"
    "莉莉丝真的没事吗……"
    window hide
#CHR_INIC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_XAA06"),"True","img/SF_XAA06A@2x.png") as lh1 zorder 100:
        ypos 0.0
    with dissolve
    voice "NRI17A_YG006"
    雄吾 "「喂，志雄」"
#THREAD_STA 1,THREAD_QUA_WIN
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESEX_A M_NOA,A_CH_SI,"【志雄】「……诶！」"
#MESX "%K%P"
    "有谁触碰到了我的肩膀，我这才回过神来。眼前是起身单手搭着我肩膀的老爸。"
    voice "NRI17A_YG007"
    雄吾 "「是担心莉莉丝吗？」"
    志雄 "「……啊啊，是有点。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_XAA03"),"True","img/SF_XAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    "听到我回答，老爸露出苦笑。"
    voice "NRI17A_YG008"
    雄吾 "「那你就快点回去吧。对你来说，现在最重要的是莉莉丝吧？」"
    voice "NRI17A_YG009"
    雄吾 "「虽然是我们提出的邀请，不过你没有必要硬是陪着我们。」"
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
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 1,(320-120)
#CHR_POSC 2,(320+120)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA06"),"True","img/SF_MAA06A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    with dissolve
    voice "NRI17A_KR004"
    香里 "「是啊。还是回去陪莉莉丝吧。」"
    "香里阿姨也以温柔的笑脸鼓励我。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA02"),"True","img/KR_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_KR005"
    香里 "「我要感谢你能这么重视那孩子。」"
    志雄 "「这是我应该做的……」"
    voice "NRI17A_KR006"
    香里 "「莉莉丝个性好强，一定不会当着志雄君的面感谢你的。所以我就代替那孩子谢谢你。」"
    "香里阿姨真的深爱着莉莉丝呢。"
    志雄 "「我知道了……我还是先回去吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA06"),"True","img/SF_MAA06A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI17A_YG010"
    雄吾 "「啊，就这么办吧。再说，我都这么大年纪了，也不至于想和你一起散步。去和莉莉丝加深关系吧……」"
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
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 1,(320-96)
#CHR_POSC 2,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .35
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA06"),"True","img/SF_MAA06A@2x.png") as lh2 zorder (10+2):
        xcenter .65
    with dissolve
    voice "NRI17A_KR007"
    香里 "「好了好了，这个话题下次再聊。那么志雄君，那孩子就拜托你了。」"
    志雄 "「嗯，我走了！」"
    window hide
    play sound "SE01_02L"
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/BG68AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    "越是思考，我就越是不安。"
    "好了，赶紧回去吧。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/BG66AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    pause (32/32.0)
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/BG60AA@2x.jpg" as bg0 zorder 0 with dissolve
    hide bg1 with dissolve
    stop se
    pause (16/32.0)
    stop sound fadeout 1
    show expression "img/BG61AA@2x.jpg" as bg0 with dissolve
    pause (16/32.0)
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA04"),"True","img/SN_MBA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_SN000"
    信 "「咦？　塚本君为什么会在这里？」"
    "在前厅的稻穗看到我，眉头皱成了个八字。"
    志雄 "「嗯？　你问我为什么我也……」"
    "我住在这旅馆里，所以在这里也没什么奇怪的吧……。"
    voice "NRI17A_SN001"
    信 "「我听莉莉丝说你和父母一起出去了。」"
    志雄 "「啊啊，是这样啊。我有些担心莉莉丝就回来了——」"
    voice "NRI17A_RI035"
    りりす？ "「稻穗～找到了吗？」"
    "咦？　这个声音是……"
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
#CHR_ALPC 0
#CHR_POSC 0,((320)+80)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA03"),"True","img/RI_MBA03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play music  "OBGM14"
#MOV_CHR_INIT 32
#MOV_CHR0 128
#MOV_CHR_GO 1
    voice "NRI17A_RI036"
    莉莉丝 "「哎？　为什么志雄也在！？」"
    "莉莉丝和稻穗表现出相同的反应。"
    志雄 "「那个，途中从老爸那边逃了回来。」"
    志雄 "「嗯……？　对了，你在这里走来走去干吗？　脚还疼吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC04"),"True","img/RI_MBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI17A_RI037"
    莉莉丝 "「啊，这，这是……」"
    voice "NRI17A_RI038"
    莉莉丝 "「那、那个。我刚从厕所回来，没有走来走去啦。」"
    voice "NRI17A_RI039"
    莉莉丝 "「那、那么我回房间去了……对不起。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    志雄 "「……真可疑」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA04"),"True","img/SN_MBA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    志雄 "「稻穗，莉莉丝究竟在干吗？」"
    voice "NRI17A_SN002"
    信 "「啊～……刚才的样子果然太明显了吗？」"
    志雄 "「莉莉丝这家伙，走路的样子完全感觉不到在疼嘛。而且她所说的『找到了吗？』是什么意思啊？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA02"),"True","img/SN_MBA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_SN003"
    信 "「莉莉丝因为脚伤和感冒一直睡到刚才，『找到了吗』是指感冒药。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBB05"),"True","img/SN_MBB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_SN004"
    信 "「……这么说……你相信吗？」"
    志雄 "「不可能相信吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBB02"),"True","img/SN_MBB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_SN005"
    信 "「是吗。没办法，我就老实告诉你吧。对不起了，莉莉丝。」"
    "稻穗朝着已经不在这里的莉莉丝的方向微微低下头，开始说道。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA03"),"True","img/SN_MBA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_SN006"
    信 "「实际上……莉莉丝把护身符弄丢了。」"
    志雄 "「护身符？」"
    "说起来，来这里的时候看到过好几次。她确实是很重视的样子……"
    voice "NRI17A_SN007"
    信 "「看来她不想让塚本君知道这件事，于是你不在的这段时间她让我帮忙一起找。」"
    志雄 "「丢了护身符有什么好隐瞒的……」"
    voice "NRI17A_SN008"
    信 "「她说在护身符里有个戒指。」"
    stop music fadeout 132
    志雄 "「戒指——难道说……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA05"),"True","img/SN_MBA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_SN009"
    信 "「怎么了？」"
    志雄 "「这护身符一定是……」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 0
#BG_INIC 2
#BG_PRI 2
    show expression "img/OIBG024A@2x.png" as bg2 zorder 200 with dissolve
    pause
#BG_ALPC 2
#CHR_ALPC 1
    show expression "img/EV_RI18B@2x.png" as bg2 zorder 200 with dissolve
    "那时候，我给她的戒指。"
    "对了，一定是……不会错的……"
    "所以才不想让我知道吧……"
    window hide
#BG_INIC 1
#BG_PRI 1
#BG_PRI 2
    show expression "img/EV_RI18B@2x.png" as bg2 zorder 200 with dissolve
    hide bg2 with dissolve
#BG_ALPC 0
#CHR_ALPC 1
    hide bg1 with dissolve
    play music  "OBGM29"
    志雄 "「真是的……」"
    "莉莉丝这么重视那个戒指我很高兴，不过我其实并不介意她把戒指弄丢的。她要是告诉我的话，我可以帮着一起找的。"
    "不，现在帮忙找也不晚。她大概还没找到那个戒指。"
    志雄 "「稻穗，我也一起帮忙找护身符吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA01"),"True","img/SN_MBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_SN010"
    信 "「啊啊，好啊。我也再找一下吧」"
    志雄 "「谢谢……那么，应该从哪儿开始找呢……？」"
    "想想在这个旅馆里莉莉丝可能去过的地方。"
#RSET F71
#RSET F72
#RSET F73
#RSET F74
    "房间里大概没有吧，莉莉丝应该已经找过了。这以外的话……"
label L_NRI17A_SEL00_Y:
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    menu:
        "走廊" if F71==0:
            $F7=0
        "更衣室" if F72==0:
            $F7=1
        "食堂" if F73==0:
            $F7=2
        "庭院" if F74==0:
            $F7=3
    if F7==0:
        jump L_NRI17A_SEL00_A
    if F7==1:
        jump L_NRI17A_SEL00_B
    if F7==2:
        jump L_NRI17A_SEL00_C
    if F7==3:
        jump L_NRI17A_SEL00_D
label L_NRI17A_SEL00_A:
    $F71=1
#RSET F71
    window hide
    stop sound
#BG_GET_NOC 0,F24
#IF F24=BG62AA, GOTO L_NRI17A_BRA00_X
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
#BG_SET_SKIP 0,BG62AA
#FADE_IN 1
label L_NRI17A_BRA00_X:
    "总之先在走廊找找看吧。为了找装有戒指的护身符这种小东西，我趴在地上寻找。"
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
    pause (64/32.0)
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA03"),"True","img/SN_MBA03A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#FADE_IN 1
    voice "NRI17A_SN011"
    信 "「没有呢……」"
    志雄 "「没找到……」"
    "把旅馆的走廊转了个遍，可还是没找到类似的东西。"
    志雄 "「到别的地方找找看吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA05"),"True","img/SN_MBA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    if not F72 or not F73 or not F74:
        jump L_NRI17A_SEL00_A2
    else:
        jump L_NRI17A_SEL00_A1
#CHECK_SEL_COMP L_NRI17A_SEL00_A1,L_NRI17A_SEL00_A2
label L_NRI17A_SEL00_A1:
#MSGNO_SAV 1
    voice "NRI17A_SN012"
    信 "「哦哦」"
    jump L_NRI17A_SEL00_X
label L_NRI17A_SEL00_A2:
#MSGNO_RET 1
    voice "NRI17A_SN012"
    信 "「哦哦」"
    jump L_NRI17A_SEL00_Y
label L_NRI17A_SEL00_B:
    $F72=1
#RSET F72
    志雄 "「浴室的更衣室……在脱衣服的时候掉了，这种可能性也不小。」"
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBB01"),"True","img/SN_MBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_SN013"
    信 "「是啊，那我们去找找看吧。」"
    window hide
    stop sound
#FADE_OUT 1
    pause (32/32.0)
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    scene expression "img/BG62AA@2x.jpg" as bg0 with dissolve
#BG_SET_SKIP 0,BG62AA
#FADE_IN 1
    "……可是，当我们来到更衣室门口才发觉。"
    志雄 "「男的要进女子更衣室，实在有点……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA06"),"True","img/SN_MBA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_SN014"
    信 "「我就是为了这种时候才存在的」"
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
    "稻穗留下了大胆的微笑，走到别处去了。"
    "……他怎么了？"
    window hide
#FADE_OUT 1
    pause (21/32.0)
#FADE_IN 1
    pause (16/32.0)
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA01"),"True","img/SN_MBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_SN015"
    信 "「久等了。」"
    "稻穗拿来了写着『清扫中』的牌子。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NRI17A_SN016"
    信 "「对不起～现在是清扫的时间！　有正在洗澡的人吗～？」"
    "稻穗对着女浴室叫道。可是，里面却是一片安静，没有人回应。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA02"),"True","img/SN_MBA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_SN017"
    信 "「好的，看来现在没人在洗澡。你运气真不错。」"
    "说着，稻穗把『清扫中』的牌子挂在门口。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA01"),"True","img/SN_MBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_SN018"
    信 "「这样就不会有人进来了。那么，到里面去找吧。」"
    志雄 "「嗯！」"
    "稻穗还真是意外的可靠呢。"
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
    "到更衣室里面找了下，可只发现了一些零钱或是钥匙圈而已，没有类似戒指的东西。"
    if not F71 or not F73 or not F74:
        jump L_NRI17A_SEL00_B2
    else:
        jump L_NRI17A_SEL00_B1
#CHECK_SEL_COMP L_NRI17A_SEL00_B1,L_NRI17A_SEL00_B2
label L_NRI17A_SEL00_B1:
#MSGNO_SAV 1
    志雄 "「这里也没有的话，还有……」"
    jump L_NRI17A_SEL00_X
label L_NRI17A_SEL00_B2:
#MSGNO_RET 1
    志雄 "「这里也没有的话，还有……」"
    jump L_NRI17A_SEL00_Y
label L_NRI17A_SEL00_C:
    $F73=1
#RSET F73
    window hide
    stop sound
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/BG89AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    "朝着地上瞪大了眼睛找遍了整个食堂。"
    "……可是，护身符和戒指都没能找到。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/BG62AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA04"),"True","img/SN_MBA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    pause (32/32.0)
#FADE_IN 1
    voice "NRI17A_SN019"
    信 "「我问了下厨房的人，他们说也没发现类似的东西。」"
    志雄 "「……是吗……」"
    voice "NRI17A_SN020"
    信 "「塚本君怎么样？　找到了吗？」"
    "我沉默地摇了摇头。"
    voice "NRI17A_SN021"
    信 "「是吗……」"
    if not F71 or not F72 or not F74:
        jump L_NRI17A_SEL00_C2
    else:
        jump L_NRI17A_SEL00_C1
#CHECK_SEL_COMP L_NRI17A_SEL00_C1,L_NRI17A_SEL00_C2
label L_NRI17A_SEL00_C1:
#MSGNO_SAV 1
    志雄 "「其他还有什么容易掉东西的地方吗……」"
    jump L_NRI17A_SEL00_X
label L_NRI17A_SEL00_C2:
#MSGNO_RET 1
    志雄 "「其他还有什么容易掉东西的地方吗……」"
    jump L_NRI17A_SEL00_Y
label L_NRI17A_SEL00_D:
    $F74=1
#RSET F74
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG60AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG60AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_14L"
    pause (32/32.0)
#FADE_IN 1
    pause (16/32.0)
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA03"),"True","img/SN_MBA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_SN022"
    信 "「要是在庭院里走动时掉了的话，找起来就有些麻烦了。」"
    志雄 "「是啊。可是……还是得找。」"
    "因为莉莉丝那么努力地想要找到。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBB01"),"True","img/SN_MBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_SN023"
    信 "「哦哦。我也去和店长说明一下事情的原委，好让我能休息一下。」"
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
    "在那之后，我们花了很长时间在庭院里寻找，可还是没找到。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA04"),"True","img/SN_MBA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_SN024"
    信 "「没有呢……」"
    志雄 "「是啊……」"
    if not F71 or not F72 or not F73:
        jump L_NRI17A_SEL00_D2
    else:
        jump L_NRI17A_SEL00_D1
#CHECK_SEL_COMP L_NRI17A_SEL00_D1,L_NRI17A_SEL00_D2
label L_NRI17A_SEL00_D1:
#MSGNO_SAV 1
    志雄 "「没办法。去别的地方找找看吧」"
    jump L_NRI17A_SEL00_X
label L_NRI17A_SEL00_D2:
#MSGNO_RET 1
    志雄 "「没办法。去别的地方找找看吧」"
    jump L_NRI17A_SEL00_Y
label L_NRI17A_SEL00_X:
#RSET F83
#RSET F71
#RSET F72
#RSET F73
#RSET F74
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG61EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG61EA@2x.jpg" as bg0 with dissolve
    pause (64/32.0)
#FADE_IN 1
    "结果在旅馆里找了个遍还是没找到护身符和戒指。我们还把事情告诉了服务台，可还没有消息。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA03"),"True","img/SN_LBA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    play music  "OBGM27"
    voice "NRI17A_SN025"
    信 "「也许不是掉在旅馆里面。」"
    志雄 "「外面吗……再说那家伙是什么时候掉的啊？」"
    "如果从第一天开始考虑的话，山上，神社，包括湖边，我们去过各种地方。"
    "要全部找过来是不可能的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA04"),"True","img/SN_LBA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_SN026"
    信 "「……啊，不好。差不多要准备晚饭了。看来我也只能帮到这里了。」"
    志雄 "「啊，不好意思。让你忙到现在……」"
    "确实，不经意间从窗口看去，天空已经被染成了绯红。"
    voice "NRI17A_SN027"
    信 "「不要介意。不好意思，到最后都没能帮你找到。」"
    志雄 "「不，稻穗不用在意。」"
    "而且稻穗作为旅馆的工作人员，旅馆的工作才是最重要的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA05"),"True","img/SN_LBA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_SN028"
    信 "「那么。莉莉丝那边我就告诉她『塚本君还没有回来』好了。」"
    志雄 "「多谢了。」"
    voice "NRI17A_SN029"
    信 "「这种小事就包在我身上了」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "稻穗轻轻挥了挥手，快速走进了旅馆里面。"
    "接下来……时间已经不多了。"
    "如果真是掉在旅馆外面的话，天色完全暗下来之后要找到几乎是不可能的。"
    "而且明天就必须离开旅馆了，没有找东西的时间。"
    "从时间上考虑的话，再找一处就是极限了。"
#RSET F83
#RSET F84
    "我和莉莉丝去过的地方，容易掉东西的地方是……"
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    menu:
        "湖":
            $F7=0
        "土产店街":
            $F7=1
        "神社":
            $F7=2
    if F7==0:
        jump L_NRI17A_SEL01_A
    if F7==1:
        jump L_NRI17A_SEL01_B
    if F7==2:
        jump L_NRI17A_SEL01_C
label L_NRI17A_SEL01_A:
    $F83=1
    $F84=1
#RSET F83
#RSET F84
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG67EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG67EA@2x.jpg" as bg0 with dissolve
    play sound "SE05_13L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,64
    "说不定掉在湖边的沙滩上了——这么想着，我朝湖边走去。"
    "当然，途中的山道，地面我也没忘记仔细地搜索。"
    "可是由于头要一直低着的关系，途中有好几次差点和别人撞到了。"
    voice "NRI17A_XG000"
    通行人 "「不要看着旁边走路！　很危险的！」"
    志雄 "「对、对不起！」"
    "每次我都向他们道歉，可是依然是看着地面走路。"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG70EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG70EA@2x.jpg" as bg0 with dissolve
#SE_VOLC 1,64
#FADE_IN 1
    "可是结果在山道上还是没找到类似的东西，就这样来到了湖边的沙滩上。这个时间果然已经没什么人了。"
    "不过，人少对找东西到是有些好处。"
    "要沿着沙滩边缘，一边走一边找护身符。"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    pause (32/32.0)
#SE_VOLC 1,64
#FADE_IN 1
    "呃……果然找不到吗……"
    志雄 "「难道在更衣室里吗？」"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    pause (64/32.0)
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG70NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG70NA@2x.jpg" as bg0 with dissolve
    stop sound
    play sound "SE05_16L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,64
    "不行。更衣室里面也没有。"
    "找着找着天色渐晚，地面也开始有些看不清了。"
    "最后抱着试一试的心态，我来到摊子向老板打听了一下，可回答仍旧是不知道。"
    "……已经不能再找下去了。"
    志雄 "「可恶……最终还是没找到吗……」"
    "我没能守护住和莉莉丝之间的回忆……"
    志雄 "「可是，最后的一个地方还是想去找一下……」"
    jump L_NRI17A_SEL01_X
label L_NRI17A_SEL01_B:
    $F83=1
    $F84=1
#RSET F83
#RSET F84
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG68EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG68EA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    "说不定在去土产店的时候掉了。"
    "我在土产店所在的街道上，把地面从头到尾仔仔细细地搜索了一遍。"
    window hide
    play sound "SE04_19"
#VIB_BIBIBI 
#QUA3_BG 
#VIB_STP 5
    "光看着地面，所以没注意到朝我走来的行人，于是撞到了。"
    志雄 "「对不起！」"
    voice "NRI17A_YG012"
    雄吾？ "「啊，我才是……嗯？」"
    志雄 "「哎？」"
    "这熟悉的声音是……"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-96)
#CHR_POSC 1,(320+96)
#CHR_COLC 0,128,120,112
#CHR_COLC 1,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    play music  "BGM16"
    志雄 "「老爸和香里阿姨？　在这里干吗呢？」"
    voice "NRI17A_KR008"
    香里 "「我们把整条街转了一遍，现在正在回来的途中。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA06"),"True","img/SF_MAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI17A_YG013"
    雄吾 "「对了，你在这里干吗？　你不是回莉莉丝那边去了吗？」"
    志雄 "「啊，那是因为……」"
    "我把事情的原委和老爸说明了一下。莉莉丝弄丢了护身符，她从早上起就有些奇怪就是因为这个原因……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA05"),"True","img/KR_MAA05A@2x.png") as lh0 zorder (10+0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA03"),"True","img/SF_MAA03A@2x.png") as lh1 zorder (10+1)
    voice "NRI17A_YG014"
    雄吾 "「原来如此……」"
    voice "NRI17A_KR009"
    香里 "「原来是这样啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA06"),"True","img/KR_MAA06A@2x.png") as lh0 zorder (10+0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA06"),"True","img/SF_MAA06A@2x.png") as lh1 zorder (10+1)
    voice "NRI17A_YG015"
    雄吾 "「那么，总之一定要找到这个装有戒指的护身符才行吧。我也来帮忙。」"
    voice "NRI17A_KR010"
    香里 "「诶，我也是。先在商店街这里找就行了吧？」"
    志雄 "「嗯……谢谢你们。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA02"),"True","img/KR_MAA02A@2x.png") as lh0 zorder (10+0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh1 zorder (10+1)
    voice "NRI17A_KR011"
    香里 "「找到之后再谢我们吧。而且，一家人互相帮助不是理所当然的嘛。」"
    voice "NRI17A_YG016"
    雄吾 "「就是这回事。」"
    "老爸和香里阿姨都笑着对我说道。"
    "家人吗……"
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
    志雄 "「找不到……」"
    "这边的太阳已经下山了，视界也变得很差。"
    window hide
#CHR_INIC 0
#CHR_INIC 1
#CHR_COLC 0,128,120,112
#CHR_COLC 1,128,120,112
#CHR_DSPWC_F 0,1,KR_LAA05,SF_LAA03
    voice "NRI17A_YG017"
    雄吾 "「现在这种情况看来是不行了……」"
    "确实，正如老爸所说……"
    voice "NRI17A_KR012"
    香里 "「对不起呢，志雄君……」"
    志雄 "「不，香里阿姨没什么好道歉的……」"
    "虽然我这么说，但是失落的心情还是通过言语表现了出来。"
    "再去别的地方找的话能找到戒指吗……？"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我摇了摇头，甩去了这种想法。再怎么多想也不是个办法。时间不可能倒流……"
    志雄 "「可是，这里绝对是最后一个地方了……」"
    jump L_NRI17A_SEL01_X
label L_NRI17A_SEL01_C:
    jump L_NRI17A_SEL01_X
label L_NRI17A_SEL01_X:
    志雄 "「对了……」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 0
#BG_INIC 2
#BG_PRI 2
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI09A")]=True
    show expression "img/EVN_RI09A@2x.jpg" as bg2 zorder 2:
        yalign 0.0
    with dissolve
    hide bg1 with dissolve
#SE_VOLC 1,0
    "我想起了夏日祭之后，回去时莉莉丝摔倒的情形。这也使她的脚受伤了……"
    "难道是摔倒的时候掉了吗。"
    window hide
#SE_VOLC 1,64
#BG_INIC 1
#BG_PRI 1
    hide bg2 with dissolve
#BG_ALPC 0
    hide bg1 with dissolve
    "好的，去神社看下吧。"
#label QJUMP
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    if F83==0:
        jump IF_ELSE1
    $F24 = "BG71NA"
    $F25 = "SE05_16L"
#RSET F24,BG71NA
#RSET F25,SE05_16L
    jump IF_END1
label IF_ELSE1:
    $F24 = "BG71EA"
    $F25 = "SE05_13L"
label IF_END1:
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/"+F24+"@2x.jpg" as bg0 zorder 0 with dissolve
    play sound F25
    pause (32/32.0)
#FADE_IN 1
    play music  "OBGM26"
    "莉莉丝摔倒确实是在下坡的时候——"
    "我从最底下开始一阶一阶，仔仔细细地往上找。"
    "也因此周围的人都默默地把奇异的眼光抛向了我。"
    "可是，现在不是在意这种事情的时候。"
    志雄 "「没有呢……」"
    "拜托了……一定要掉在这里……不在这里的话，或许就真的找不到了。"
    "今天要是找不到的话，我就必须回去澄空了。"
    "那是我和莉莉丝珍贵的回忆，我不想在她心中留下悲伤……"
    window hide
#FADE_OUT 1
#BG_ALPC 0
    if F83==0:
        jump IF_ELSE2
    scene expression "img/NIMG01D@2x.png" as bg_over zorder 2
    show expression "img/CloudD1_0@2x.png" as cloud0 zorder 5:
        ycenter .55
        xcenter .75
        linear 500 xcenter .0
    show expression "img/CloudD1_1@2x.png" as cloud1 zorder 5:
        ycenter .55
        xcenter .65
        linear 500 xcenter .0
    show expression "img/CloudD1_2@2x.png" as cloud2 zorder 8:
        ycenter .3
        block:
            xcenter 1.0
            linear 140 xcenter .0
            repeat
    show expression "img/CloudD2_1@2x.png" as cloud3 zorder 8:
        ycenter .2
        block:
            xcenter 1.0
            linear 100 xcenter .0
            repeat
    show expression "img/CloudD2_0@2x.png" as cloud4 zorder 8:
        ycenter .0
        block:
            xcenter 1.0
            linear 120 xcenter .0
            repeat
    show expression "img/CloudD3@2x.png" as cloud5 zorder 10:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.5
            linear 50 xpos .0
            xpos 1.0
            linear 50 xpos .5
            repeat
    with dissolve
#EFF_STAC 0,CLOUD_D,EFF_NOSKIP
    jump IF_END2
label IF_ELSE2:
    scene expression "img/NIMG01C@2x.png" as bg_over zorder 2
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
label IF_END2:
#FADE_IN 1
    志雄 "「拜托你了，神啊……」"
    "我仰天长叹。"
    "可是，这种时候拜托神明也没用。"
    "有这点时间还不如自己去找。"
    window hide
#EFF_STPC 0,EFF_SKIP
    if F83==0:
        jump IF_ELSE3
    $F24 = "BG71NA"
#RSET F24,BG71NA
    jump IF_END3
label IF_ELSE3:
    $F24 = "BG71EA"
#RSET F24,BG71EA
#BG_SET_BACK 
label IF_END3:
    scene expression "img/"+F24+"@2x.jpg" as bg_over zorder 2 with dissolve
    if F0>=-2:
        jump L_NRI17A_BRA_01_A
#IF F17>=-2, GOTO L_NRI17A_BRA_01_A
    jump L_NRI17A_BRA_01_B
label L_NRI17A_BRA_01_A:
#RSET F108
    stop music fadeout 1
#BG_ALPC 0
    "当我再次把视线投向地面时……"
    志雄 "「……？」"
#MESEX_A M_NOA,A_CH_SI,"【志雄】「……？」%K%P"
    "视界的角落里有一个不自然的红色物体。"
    志雄 "「啊……！」"
    window hide
#BG_INIC 3
#BG_PRI 3
#BG_ALP 3
#BG_POSC 328
    show expression "img/NIMG21A@2x.png" as bg3 zorder 3 with dissolve
#BG_ALP_AUTOC 3,128,0,F24
#BG_POS_AUTOC 3,0,0,,F24
    "在石阶上——发现掉落的护身符时，我几乎差点跌倒。"
    "一定是这个……！"
    "我压抑着心中的激动之情，用颤抖的手去确认其内部。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_PRI 1
#BG_ALP 1
    show expression "img/NIMG20A@2x.png" as bg1 zorder 1 with dissolve
#BG_POS_AUTOC 328,,F24
    pause (32/32.0)
#BG_ALP_AUTOC 3,0,0,F26
#BG_ALP_AUTOC 1,128,0,F26
#BG_POS_SAVEC 3
#BG_ALP_SAVEC 3
#BG_ALP_SAVEC 1
    hide bg3 with dissolve
    志雄 "「是这个……可、这是……」"
    "我看着手中的戒指，不禁皱起眉头。"
    "也许是戒指被谁踩到了吧，已经完全断裂了。"
    志雄 "「要是把这个交给莉莉丝的话……」"
    "她一定会伤心的……"
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
label L_NRI17A_BRA_01_B:
    $F108=1
#RSET F108
    window hide
#BG_ALPC 0
    hide bg1 with dissolve
    "可是，依然找不到莉莉丝的戒指，时间无情地流逝着。"
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
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT