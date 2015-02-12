label NRI18A:
    $currentlabel = "NRI18A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '08'
    $day = '10'
    $date = '4'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 0,CAL_0810
    show expression "img/NIMG15A-568h@2x.jpg" as cal zorder 5
    show expression "img/08_10_THURSDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG16AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG16AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    play music  "OBGM04"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    voice "NRI18A_RI000"
    莉莉丝 "「多谢光顾！」"
    voice "NRI18A_XD000"
    客 "「不客气」"
    window hide
    show expression "img/BG17AA1@2x.jpg" as bg_over zorder 2 with dissolve
    play sound "SE00_11"
    voice "NRI18A_RI001"
    莉莉丝 "「哈……」"
    "送走了店里最后一个客人后，我不禁叹了口气。"
    "现在刚过中午，客人比较少。"
    "我把手伸进自己口袋中，没有一直不离身的戒指护身符的感触。"
    "结果在旅行途中，我还是没能找到志雄送我的戒指。"
    "住宿的日数是确定的，我也不能一个人一直留在龙境，就算找不到戒指也不得不回来。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA01"),"True","img/FU_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_FU000"
    富美子 "「莉莉丝～可以休息了～」"
    voice "NRI18A_RI002"
    莉莉丝 "「啊，嗯。」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#FADE_IN 0
    "……"
    window hide
#FADE_OUT 0
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG18AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG18AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    voice "NRI18A_RI003"
    莉莉丝 "「哈……」"
    play sound "SE03_07"
    "伴随着叹息声，我躺在了床上。"
    "倒在床上的同时，日历映入了我的眼帘。自从去龙境旅行已经过了一星期了。"
    "对了，今天明明是我的生日……"
    "难道志雄忘了吗……？"
    "可是，从自己口中说出来也很不好意思……"
    voice "NRI18A_RI004"
    莉莉丝 "「比起这个，我必须得去找戒指……」"
    "在龙境丢失的戒指是我无可替代的东西。绝对、绝对不能丢掉。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 0
#BG_INIC 2
#BG_PRI 2
    show expression "img/EV_RI18B@2x.png" as bg2 zorder 2 with dissolve
    hide bg1 with dissolve
    "因为那是志雄和我的回忆，是志雄喜欢我的证明。"
    "可是，在那之后已经过了一星期了，即使去找，找到的可能性也微乎其微……"
    window hide
#BG_INIC 1
#BG_PRI 1
#BG_PRI 2
    show expression "img/EV_RI18B@2x.png" as bg2 zorder 2 with dissolve
    hide bg2 with dissolve
#BG_ALPC 0
    hide bg1 with dissolve
    voice "NRI18A_RI005"
    莉莉丝 "「可是……即使这样，我也必须得去……」"
    "我从口袋中取出手机，然后看了下邮件的列表。"
    window hide
    play sound "SE02_05"
    pause (16/32.0)
    play sound "SE02_05"
    "从龙境回来后一星期，都没有和志雄见过面。只有一次简短的邮件交流。"
    window hide
#SCRMODE_SPC SCR_FULL
    play sound "SE02_05"
    "Ｔｏ：志雄{p}件名：明天{p}明天有空吗？"
#FILT_PRI 1
#FILT_IN 48,0,COL_DARK
#MES "%S032%FS%t002Ｔｏ：志雄%N%t002件名：明天%N%t005明天有空吗？%FE%K"
    play sound "SE02_05"
#MESX "%O032"
    window hide
#FILT_OUT 48
#SCRMODE_SPC SCR_WINDOW
#MES "%O032"
    "可他的反应却十分冷淡。"
    window hide
#SCRMODE_SPC SCR_FULL
    play sound "SE02_05"
#FILT_PRI 1
#FILT_IN 48,0,COL_DARK
#MES "%S032%FS%t002Ｆｒｏｍ：志雄%N%t002件名%t002：Ｒｅ明天%N%t007抱歉。我现在学习很忙，没什么时间。%N%t007下次我再联系你吧。%FE%K"
    "Ｆｒｏｍ：志雄{p}件名{w}：Ｒｅ明天{p}抱歉。我现在学习很忙，没什么时间。{w}下次我再联系你吧。"
    play sound "SE02_05"
#MESX "%O032"
    window hide
#FILT_OUT 48
#SCRMODE_SPC SCR_WINDOW
    "我重新看了一遍这封邮件，再次叹了口气。"
    voice "NRI18A_RI006"
    莉莉丝 "「诶？　智纱发来邮件了。」"
    "我没注意到这封邮件。大概在３０分钟以前，内容是『我就在你家附近，现在就去你家玩』。"
    "怎么办，我现在可没心情玩……"
    "可是，也许是因为她记得我生日想帮我庆祝。"
    "这样的话，我也不好意思拒绝……"
    window hide
    play sound "SE00_10"
    voice "NRI18A_CH000"
    智纱？ "「不好意思～莉莉丝在吗～？」"
    voice "NRI18A_RI007"
    莉莉丝 "「啊……已经来了」"
    voice "NRI18A_FU000A"
    富美子 "「啊，箱崎。欢迎欢迎，我现在就去把莉莉丝叫来。」"
    voice "NRI18A_FU000B"
    富美子 "「莉莉丝～！　箱崎来玩了～！」"
    voice "NRI18A_RI008"
    莉莉丝 "「好的～我现在就来～！」"
    "我从床上起来，把手机塞到口袋里，走出了房间。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG17AA1@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG17AA1@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LBA01"),"True","img/CH_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#FADE_IN 1
    voice "NRI18A_CH001"
    智纱 "「中午好，莉莉丝。」"
    voice "NRI18A_RI009"
    莉莉丝 "「总觉得很久没见到智纱了呢。」"
    voice "NRI18A_CH002"
    智纱 "「旅行之前是最后一次，已经有１０天以上没见到了呢」"
    voice "NRI18A_RI010"
    莉莉丝 "「１０天吗……不上学的话，觉得时间一下子就过去了呢。」"
    voice "NRI18A_RI011"
    莉莉丝 "「智纱果然在忙着学习吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LBB06"),"True","img/CH_LBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_CH003"
    智纱 "「嗯～是呢。不过不管怎么说，现在还是暑假中呢。　无论如何还是会有些放松。明明知道现在是必须要努力的时候。」"
    voice "NRI18A_RI012"
    莉莉丝 "「是吗……志雄也是这种感觉吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LBA04"),"True","img/CH_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_CH004B"
    智纱 "「啊，啊哈哈。是吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LBA01"),"True","img/CH_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_CH005"
    智纱 "「原来是这样啊……莉莉丝见不到塚本君，感到寂寞了吧？」"
    voice "NRI18A_RI013"
    莉莉丝 "「怎，怎么可能嘛！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+192)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA01"),"True","img/FU_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .8
    with dissolve
    voice "NRI18A_FU001"
    富美子 "「是啊。这孩子一旦有别人发邮件给她就会一下子很兴奋，可打开手机，看到不是志雄的时候就会唉声叹气的」"
    voice "NRI18A_RI014"
    莉莉丝 "「没，没这回事啦！　说什么呢，婆婆！」"
    window hide
    hide lh1 with dissolve
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LBB02"),"True","img/CH_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_CH006"
    智纱 "「哈哈哈，那样的话……」"
    voice "NRI18A_RI015"
    莉莉丝 "「诶？」"
    "智纱的声音太轻，以至于我没听清楚，于是我凝视着智纱。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LBA01"),"True","img/CH_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_CH007"
    智纱 "「不，没什么。」"
    voice "NRI18A_CH008"
    智纱 "「对了，我们去外面玩吧？　去买些东西之类的。」"
    voice "NRI18A_RI016"
    莉莉丝 "「啊……对不起。我还得帮店里的忙，而且今天我也不太想出去……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+192)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA01"),"True","img/FU_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .8
    with dissolve
    voice "NRI18A_FU002"
    富美子 "「店里的事没关系的，莉莉丝。你出去玩吧」"
    voice "NRI18A_FU003"
    富美子 "「你最近几乎没有出去过吧？　一直闷在家里只会更加失落而已。」"
    voice "NRI18A_RI017"
    莉莉丝 "「可是……」"
    voice "NRI18A_FU004"
    富美子 "「好啦好啦。智纱，莉莉丝就拜托你了。」"
    voice "NRI18A_CH009"
    智纱 "「啊，好的。」"
    window hide
    hide lh1 with dissolve
    voice "NRI18A_CH010"
    智纱 "「那我们走吧，莉莉丝。」"
    voice "NRI18A_RI018"
    莉莉丝 "「嗯……」"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG05AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG05AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_15L"
    pause (32/32.0)
#FADE_IN 1
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBC04"),"True","img/CH_MBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_CH011"
    智纱 "「天气热得整个人都要融化了呢。」"
    "夏天的阳光就像在恶作剧一般，无情地照射在我们身上。"
    "最近一直呆在家里吹空调的我擦拭着额头上的汗。"
    voice "NRI18A_CH012"
    智纱 "「７月２３日是大暑，最热的一天，８月应该会逐渐开始凉快，不过……」"
#MESEX_A M_NOA,A_CH_RI,NRI18A_RI019,"【りりす】「……」%K%P"
    莉莉丝 "「……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA01"),"True","img/CH_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_CH013"
    智纱 "「对了，莉莉丝。你有什么想去的地方吗？」"
    莉莉丝 "「……」"
#MESEX_A M_NOA,A_CH_RI,NRI18A_RI020,"【りりす】「……」%K%P"
    voice "NRI18A_CH014"
    智纱 "「……没有的话，去书店看看怎么样？」"
    莉莉丝 "「……」"
#MESEX_A M_NOA,A_CH_RI,NRI18A_RI021,"【りりす】「……」%K%P"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA04"),"True","img/CH_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_CH015"
    智纱 "「莉莉丝？」"
    莉莉丝 "「……」"
#MESEX_A M_NOA,A_CH_RI,NRI18A_RI022,"【りりす】「……」%K%P"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_XBA01"),"True","img/CH_XBA01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#ROUTINE_STA
#CHR_ALP_AUTOC 1,128,1,F24,8
#CHR_ALP_AUTOC 0,0,1,F24,8
#ROUTINE_STP
#BG_BLUR 0
    hide lh0 with dissolve
    voice "NRI18A_CH016"
    智纱 "「莉～莉～丝～！」"
    voice "NRI18A_RI023"
    莉莉丝 "「哇！」"
#THREAD_STA 1,THREAD_QUA_WIN
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESA A_CH_RI,NRI18A_RI023,"【りりす】「哇！」"
#THREAD_WAT 1
#WIN_POS 0,0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_XBA04"),"True","img/CH_XBA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#MESX "%K%P"
    "突然被碰到肩膀的我吓了一跳。"
    voice "NRI18A_CH017"
    智纱 "「怎么了？　总觉得你心不在焉的？」"
    voice "NRI18A_RI024"
    莉莉丝 "「啊，啊啊……那个，对不起」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_XBA01"),"True","img/CH_XBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI18A_CH018"
    智纱 "「那个，没关系……然后，莉莉丝有什么想去的地方吗？」"
    voice "NRI18A_RI025"
    莉莉丝 "「想去的地方……没什么特别想去的。」"
    "总不至于说想再去龙境吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_XBB01"),"True","img/CH_XBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI18A_CH019"
    智纱 "「是吗。那么，我们去书店吧？　说不定会发现什么有趣或者对考试有帮助的书。」"
    voice "NRI18A_RI026"
    莉莉丝 "「嗯，就这么决定吧。」"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG45AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG45AA@2x.jpg" as bg0 with dissolve
    pause (64/32.0)
    play sound "SE00_38"
#FADE_IN 1
    voice "NRI18A_CH020"
    智纱 "「哈～好凉快～」"
    voice "NRI18A_RI027"
    莉莉丝 "「嗯，是啊……」"
    show expression "img/EXBG02A@2x.jpg" as bg_over zorder 5
    show expression "img/CH_ZBA01A@2x.png" as lh0 zorder (10+0):
        xcenter ((320)/640.0)
    with dissolve
    play music  "OBGM20"
    "我们坐在了附近空着的位子上。然后，离我们比较近的店员把水拿了过来。"
    voice "EV99_ET007"
    店員 "「决定要点些什么了吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_ZBB02"),"True","img/CH_ZBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_CH021"
    智纱 "「啊，是的。我要奶油苏打。莉莉丝呢？」"
    莉莉丝 "「……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_ZBA04"),"True","img/CH_ZBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_CH022"
    智纱 "「莉莉丝？」"
    voice "NRI18A_RI029"
    莉莉丝 "「——啊，对不起」"
    voice "NRI18A_RI030"
    莉莉丝 "「那个，点东西是吗？　那我要混合咖啡。」"
    voice "EV99_ET008"
    店員 "「我知道了」"
    "店员手脚麻利地把我们点的东西写到点菜单上，离开了我们这一桌。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_ZBC02"),"True","img/CH_ZBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_CH023"
    智纱 "「莉莉丝没什么精神呢」"
    "说着，智纱把纸袋放在桌子上。刚才在书店里买的两册考试用问题集也在其中。"
    voice "NRI18A_RI031"
    莉莉丝 "「没、这回事……」"
    "虽然嘴上是这么说，可我自己很清楚自己是在说谎。"
    "戒指也找不到，志雄也见不到……现在的我完全无法掩饰自己的失落。"
    "而且想起来，至今为止也没有长达一周见不到志雄的情况。"
    "也许是丢失了戒指这种有形的东西，见不到志雄便使我感到更加不安。"
    "……我不认为自己是这么软弱的人。"
    voice "NRI18A_RI032"
    莉莉丝 "「智纱的学习正在步步为营地进行着吧？」"
    "我一边把视线转移到智纱的纸袋上，一边为了掩饰自己的不安而转移了话题。"
    voice "NRI18A_RI033"
    莉莉丝 "「学习的状况怎么样？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_ZBA01"),"True","img/CH_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "提到学习两个词使我的心感到阵阵刺痛。"
    "志雄也是因为学习忙才没空和我见面的……"
    voice "NRI18A_CH024"
    智纱 "「嗯，进度还是一般程度吧～莉莉丝怎么样？」"
    voice "NRI18A_RI034"
    莉莉丝 "「我完全不行啦……」"
    "我蜷缩着肩膀苦笑道。"
    voice "NRI18A_RI035"
    莉莉丝 "「我本来就是一个没有计划性的人。」"
    "智纱看着我笑了起来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_ZBB02"),"True","img/CH_ZBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_CH025"
    智纱 "「像这样也不错啊～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_ZBB05"),"True","img/CH_ZBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_CH026"
    智纱 "「朝着某个目标不顾一切的前进，抑或是珍惜现在积累起来的成果，一次来到达某个目标。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_ZBB01"),"True","img/CH_ZBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_CH027"
    智纱 "「数学中也有这种说法，归纳法和演算法。两种方法都没错，都是正确的。」"
    "虽然我不太明白『归纳法』和『演算法』这两个词，不过智纱想表达的东西我大概明白了。"
    voice "NRI18A_RI036"
    莉莉丝 "「嗯……谢谢你，智纱」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_ZBA01"),"True","img/CH_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE02_01"
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    voice "NRI18A_CH028"
    智纱 "「不客气。」"
    "智纱说话的同时，我手机收到邮件的声音响起。"
    voice "NRI18A_RI037"
    莉莉丝 "「嗯？」"
    "我拿出手机看了一下画面。邮件的送信者是——"
    stop music fadeout 132
    voice "NRI18A_RI038"
    莉莉丝 "「志雄？」"
    "时隔已久的邮件。吃惊，焦虑，不安，欣喜，种种感情交织在我心头，操纵手机的手指无法很顺畅地行动。不过最终我还是打开了信封。"
    "邮件的内容简洁明了。"
    window hide
#SCRMODE_SPC SCR_FULL
    play sound "SE02_05"
    "Ｆｒｏｍ：志雄{p}件名：{p}我在「富美」等你"
#FILT_PRI 1
#FILT_IN 48,0,COL_DARK
#MES "%S032%FS%t002Ｆｒｏｍ：志雄%N%t002件名%t002：%N%t007我在「富美」等你%FE%K"
    play sound "SE02_05"
#MESX "%O032"
    window hide
#FILT_OUT 48
#SCRMODE_SPC SCR_WINDOW
    play sound "SE03_12"
    show expression "img/BG45AA@2x.jpg" as bg_over zorder 2 with dissolve
    pause (32/32.0)
#BG_LAY 3,CH_MXA03,2,((320)-(320))
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA03"),"True","img/CH_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NRI18A_CH029"
    智纱 "「莉、莉莉丝？」"
#REMOVE_REEK_CHR 0
#BG_ALP 3
    "我就像被弹簧弹起来一般站了起来。"
    voice "NRI18A_RI039"
    莉莉丝 "「对不起，我必须先回去一下！」"
#REEK_CHR 0
    voice "NRI18A_CH030"
    智纱 "「诶？　莉莉丝，等一下！」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
    "我和智纱取消了在咖啡店点的东西，心急火燎地赶回了『富美』。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/BG16AA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
#FADE_IN 1
    voice "NRI18A_RI040"
    莉莉丝 "「我……我回来了！」"
    "由于一路是跑回家的，我有些喘不上气，说话也断断续续。"
    "我为什么要这么急呢。连我自己也不清楚……"
    window hide
    play sound "SE00_10"
#FADE_OUT 1
#SE_WATC 0
#BG_SET_BACK 
#BG_INIC 0
#FADE_IN 0
    "然后——"
    "径直迎向我的正是我青梅竹马兼恋人的他。"
#label QJUMP
    window hide
#FADE_OUT 0
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG17AA2@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG17AA2@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA04"),"True","img/RI_MCA04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (16/32.0)
    play sound "SE00_10"
#FADE_IN 1
    "归来的莉莉丝上气不接下气。"
    "那家伙这么急着跑回来的吗……"
    voice "NRI18A_RI040"
    莉莉丝 "「我……我回来了」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBC06"),"True","img/CH_MBC06A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA04"),"True","img/RI_MCA04A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    with dissolve
    voice "NRI18A_CH031"
    智纱 "「等，等一下啦～莉莉丝……」"
    "紧接着莉莉丝之后的是箱崎。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
    hide lh0
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LCA04"),"True","img/RI_LCA04A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
    with dissolve
#ROUTINE_STA
#CHR_ALP_AUTOC 1,0,1,F24
#CHR_ALP_AUTOC 2,0,1,F24
#CHR_ALP_AUTOC 0,128,1,F24
#ROUTINE_STP
#BG_BLUR 0
#CHR_ERSWC 1,2
    志雄 "「莉莉丝……」"
    "面对还气喘吁吁的莉莉丝，我比谁都先说出了这句话。"
    志雄 "「生日快乐！」"
    window hide
#CHR_SET_BACK
#CHR_ALP_AUTOC 0,0,0,1
#BG_BLUR 0
#ROUTINE_STA
#CHR_INIC 1
#CHR_INIC 2
#CHR_ALPC 1
#CHR_ALPC 2
#CHR_POSC 1,(320-224)
#CHR_POSC 2,(320+224)
#ROUTINE_STP
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MAB01"),"True","img/SN_MAB01A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
        xcenter .15
    with dissolve
    play sound "SE03_67"
#FADE_OUT 0,0,COL_WHITE
#ROUTINE_STA
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_SBB02"),"True","img/TO_SBB02A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .85
    with dissolve
#CHR_ALPC 0
#CHR_ALPC 1
#CHR_ALPC 2
#ROUTINE_STP
#FADE_IN 1
    voice "NRI18A_MIX02"
    亨 "「生日快乐！」"
    信 "「生日快乐！」"
    window hide
    play music  "BGM01NL"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SORT 0,1,2
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAB02"),"True","img/SU_MAB02A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA02"),"True","img/FU_MAA02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    play sound "SE03_90"
    if not persistent.dictlist[6] and persistent.show_dict:
        $persistent.dictlist[6]=True
        show screen dict_pop(i=6)
    voice "NRI18A_FU005"
    富美子 "「生日快乐！」"
    voice "NRI18A_SU000"
    铃 "「生日快乐！」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SORT 1,0,2
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA01"),"True","img/CH_MBA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA03"),"True","img/RI_MCA03A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    voice "NRI18A_CH032"
    智纱 "「生日快乐，莉莉丝～」"
    voice "NRI18A_RI041"
    莉莉丝 "「诶！？　啊……！」"
    "也许是因为吃惊和欣喜的关系——莉莉丝的表情显得有些不自然。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCD03"),"True","img/RI_MCD03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI18A_RI042"
    莉莉丝 "「谢谢……」"
    voice "NRI18A_RI043"
    莉莉丝 "「还装饰得这么漂亮……该不会智纱把我带出去也是……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBB02"),"True","img/CH_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_CH033"
    智纱 "「呼呼呼。对不起，是塚本君拜托我的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCD01"),"True","img/RI_MCD01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI18A_RI044"
    莉莉丝 "「志雄……原来你记得我的生日啊。」"
    志雄 "「那是当然的咯。你以为我们相处了几年啊。」"
    "而且，她是我最重视的人，怎么可能会忘记呢。"
    "不过，我一直没有直接提及有关她生日的话题。虽然有一部分原因是因为没准备好生日礼物，不过最主要的是想让莉莉丝大吃一惊。"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2,((320-160)-64)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MAA02"),"True","img/SN_MAA02A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR0 0
#MOV_CHR2 128,(320-160)
#MOV_CHR_GO 1
    hide lh0 with dissolve
    voice "NRI18A_SN001"
    信 "「那么，莉莉丝。这是我的礼物。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,((320-160)-64)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCA01"),"True","img/RI_MCA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR0 128,(320-160)
#MOV_CHR2 0
#MOV_CHR_GO 1
    hide lh2 with dissolve
    voice "NRI18A_TO001"
    亨 "「这是我的。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2,((320-160)-64)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAB02"),"True","img/SU_MAB02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR0 0
#MOV_CHR2 128,(320-160)
#MOV_CHR_GO 1
    hide lh0 with dissolve
    voice "NRI18A_SU001"
    铃 "「虽然不是什么大不了的东西……给。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,((320-160)-64)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA01"),"True","img/CH_MBA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR0 128,(320-160)
#MOV_CHR2 0
#MOV_CHR_GO 1
    hide lh2 with dissolve
    voice "NRI18A_CH034"
    智纱 "「我的是这个。生日快乐，莉莉丝～」"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2,((320-160)-64)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA02"),"True","img/FU_MAA02A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR0 0
#MOV_CHR2 128,(320-160)
#MOV_CHR_GO 1
    hide lh0 with dissolve
    voice "NRI18A_FU006"
    富美子 "「生日快乐。一直以来都要谢谢你。对了，香里说晚上她会来的。」"
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
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCB01"),"True","img/RI_MCB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    "大家都把各自装生日礼物的小包递给了莉莉丝。"
    voice "NRI18A_RI045"
    莉莉丝 "「谢谢……真的谢谢你们」"
    voice "NRI18A_SN002"
    信 "「那么，最后是……」"
    "所有人的视线都指向了我。"
    window hide
    stop music fadeout 1128
#CHR_SORT 0,1,2
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
    hide lh0
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XCB02"),"True","img/RI_XCB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 64
#MOV_CHR0 128
#MOV_CHR1 0
#MOV_FOCUS_BG 512
#MOV_CHR_GO 0
#BG_BLUR 0
    "一直无法决定送什么礼物好。结果还是没打听到莉莉丝想要什么。不过——"
    "现在的我已经决定了。"
    志雄 "「莉莉丝，这个。」"
    "我握起莉莉丝的手，把那个已经坏掉了的玩具戒指放在了她手心上。虽然泥是洗掉了，不过缺损的部分却没办法修复。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XCB02"),"True","img/RI_XCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_RI046"
    莉莉丝 "「这个是……！」"
    志雄 "「这是旅行时莉莉丝掉了的戒指。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XCC04"),"True","img/RI_XCC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_RI047"
    莉莉丝 "「你果然，知道吗……」"
    志雄 "「嗯。对不起，虽然好不容易找到了，可发现时已经坏掉了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XCD01"),"True","img/RI_XCD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_RI048"
    莉莉丝 "「是吗……不过志雄没什么好道歉的吧。谢谢你能找到它……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XCD03"),"True","img/RI_XCD03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "说着，莉莉丝的眼角开始闪烁着泪花。"
    "我一定是觉得她会流露出这种悲伤的表情，所以在旅行途中才没有还给她。"
    志雄 "「然后——和刚才的戒指不同，这边是生日礼物。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XCA03"),"True","img/RI_XCA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI18A_RI049"
    莉莉丝 "「诶？」"
    "我在莉莉丝面前拿出了护身符。"
    voice "NRI18A_RI050"
    莉莉丝 "「这是……？」"
    "我无视她的疑问打开了护身符，把里面的东西给莉莉丝看。里面是——"
    window hide
#BG_SET_BACK 
#BG_INIC 3
#BG_PRI 3
#BG_ALP 3
#BG_POSC 328
    show expression "img/NIMG06A@2x.png" as bg3 zorder 13 with dissolve
#BG_ALP_AUTOC 3,128,0,F24
#BG_POS_AUTOC 3,0,0,,F24
#BG_ALP_SAVEC 3
#BG_POS_SAVEC 3
    play music  "OBGM01"
#BG_UV_AUTOC 3,142,-40,930,552,1,F24
#BG_POS_SAVEC 3
    voice "NRI18A_RI051"
    莉莉丝 "「新的……戒指！？」"
    志雄 "「嗯。这不是玩具，是真的戒指，虽然只是个便宜货……」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_PRI 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI11A")]=True
    scene expression "img/EVN_RI11A@2x.jpg" as bg1 with dissolve
    hide bg3 with dissolve
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_SWPC 0
#BG_PRI 0
    "我拿起莉莉丝的左手，把戒指戴在她无名指上。"
    voice "NRI18A_RI052"
    莉莉丝 "「谢……谢谢……」"
    voice "NRI18A_SN003"
    信 "「塚本君为了买这个戒指，这一星期一直在酪萨克打工哟～」"
    "听了稻穗的话，我不禁露出了苦笑的表情。"
    "突然来到酪萨克，说只干一星期，这还真是无理取闹的要求。能接受我的请求还要多亏了稻穗帮我说好话。"
    志雄 "「最近几天一直没能来见你，真是对不起呢。」"
    "至今为止我们一直理所当然地在一起。也许在这一星期里，莉莉丝会感到寂寞吧。"
    voice "NRI18A_RI053"
    莉莉丝 "「不，我没事的。比起这个……」"
    voice "NRI18A_RI054"
    莉莉丝 "「你真是个笨蛋呢，志雄……在高三的夏天这么炎热的时候……为了这种事竟然打了一个星期的工……」"
    志雄 "「不是『为了这种事』吧，这可是为了我最重要的人而做的。」"
    志雄 "「对我来说，莉莉丝的笑容比什么都重要」"
    voice "NRI18A_RI055"
    莉莉丝 "「呜……」"
    "莉莉丝的眼眶里渗出了大颗大颗的泪滴。"
    voice "NRI18A_RI056"
    莉莉丝 "「谢谢……」"
    "然后，我拿起了还放在莉莉丝手心上的玩具戒指。"
    志雄 "「这个戒指怎么办？　不要了吗？」"
    "莉莉丝摇了摇头。"
    voice "NRI18A_RI057"
    莉莉丝 "「这也是我永远的宝物。即使坏掉了、即使损伤了也一样，因为这是我和志雄的回忆。」"
    志雄 "「是呢，谁也没规定宝物只允许有一个的。」"
    "莉莉丝朝我伸出了左手。即使不说话也明白她的意思，我不禁露出了笑容。"
    "我把坏掉的玩具戒指戴在了莉莉丝左手的无名指上。"
    "两个并列的戒指，感觉意外的搭调。"
    志雄 "「以后我会一直和莉莉丝在一起的。这是我的承诺。」"
    voice "NRI18A_RI058"
    莉莉丝 "「嗯……志雄……」"
    voice "NRI18A_RI059"
    莉莉丝 "「最喜欢你了。」"
    window hide
#FADE_OUT 1,64,COL_WHITE
    stop music fadeout 1
    stop se fadeout 1
    stop sound fadeout 1
    pause (64/32.0)
    scene expression Solid("000") with fade
#GRAPH_INI 
#FADE_IN 1
    stop music fadeout 11
    stop se
    stop sound
#MOV_PLY 1
#RSET S101
#FADE_OUT 0
    scene expression Solid("000") with fade
#GRAPH_INI 
#SET_BACKCOL 0,0
#BG_SET_BACK 
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI12A")]=True
    show expression "img/EVN_RI12A@2x.jpg" as bg1 zorder 1 with dissolve
#FADE_IN 1
#    play music  "OBGM01"
    "伴随着轻声细语，嘴唇相互接触。"
    "眼前是莉莉丝的脸。还有呼吸的温度。"
#MES_SYNC2
    voice "NRI18A_MIX00"
    亨 "「哦哦～！」"
    信 "「噢噢～！」"
#MES_SYNC2
    voice "NRI18A_MIX01"
    富美子 "「恭喜，莉莉丝」"
    智纱 "「恭喜你，莉莉丝」"
    voice "NRI18A_SU002"
    铃 "「哈，年轻人真是……」"
    window hide
#BG_SET_DEFC 0,BG17AA2
    scene expression "img/BG17AA2@2x.jpg" as bg0 with dissolve
#CHR_DSPC_P 0,RI_XCB07
    hide bg1 with dissolve
    "我和莉莉丝的未来，现在还是一张白纸。这之后将会有什么样的将来，我自己也不知道。"
    "可是有着和莉莉丝一起构筑起来的现在，即使之后有怎样的未来，也一定能笑着面对吧。"
    "所以，对于我们最重要的是——"
    志雄 "「以后莉莉丝会一直在我身边。」"
    voice "NRI18A_RI060"
    莉莉丝 "「志雄会一直在我身边——」"
    window hide
#BG_DSP_DEF 1,EVN_RI12A
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    "两人感受着对方的温暖，我们再一次许下了永久的誓言。"
    window hide
#MUS_VOL 255
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI12B")]=True
    scene expression "img/EVN_RI12B@2x.jpg" as bg1
    with dissolve
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
    pause (64/32.0)
#FADE_OUT 1,128,COL_WHITE
#EFF_STPC 0,EFF_SKIP
#GRAPH_INI 
    stop se
    stop sound
    stop music fadeout 1
#FADE_IN 0
    pause (90/32.0)
    scene expression "img/EVN_RI12C-568h@2x.jpg" as bg1 with dissolve
#FIN_DSP EVN_RI12C
    pause
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_QUA_WIN
#TH_QUAKE_WIN 4
#EOT
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT