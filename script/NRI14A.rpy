label NRI14A:
    $currentlabel = "NRI14A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '29'
    $date = '6'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG66EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG66EA@2x.jpg" as bg0 with dissolve
    play sound "SE05_13L"
    pause (32/32.0)
#FADE_IN 1
    play music  "BGM11"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "天色渐晚，我们两个决定返回旅馆……"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCB06"),"True","img/RI_MCB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI14A_RI000"
    莉莉丝 "「哈……」"
    "莉莉丝在我身旁走着，从刚才起就没什么精神。"
    "来的时候明明那么欢快，现在却基本不说话。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCB05"),"True","img/RI_MCB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI14A_RI001"
    莉莉丝 "「呼……」"
    "莉莉丝轻轻打了个哈欠。"
    志雄 "「没事吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MCC04"),"True","img/RI_MCC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI14A_RI002"
    莉莉丝 "「嗯～……今天真的累了」"
    voice "NRI14A_RI003"
    莉莉丝 "「哈～……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "背后感到了一个娇小女生的分量和温暖。"
    志雄 "「……怎么了，突然就……」"
    voice "NRI14A_RI004"
    莉莉丝 "「总觉得能靠在志雄背上就会轻松一点」"
    "那是因为你不用承受自己的体重才会轻松的吧，于是在我身上的体重就大大增加了。"
    志雄 "「哎，真拿你没办法。」"
    "我握住莉莉丝的手。"
    志雄 "「来，这样很危险，好好走路。」"
    voice "NRI14A_RI005"
    莉莉丝 "「啊……」"
    voice "NRI14A_RI006"
    莉莉丝 "「嗯，我知道了……」"
    "莉莉丝没有说多余的话来反驳我，而是在我斜后方跟着。"
    "绯红的天空下——手牵着手的我们的身影，长长地倒映在了山道上。"
#label QJUMP
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG63NA3@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG63NA3@2x.jpg" as bg0 with dissolve
    play sound "SE05_16L"
    pause (32/32.0)
    play sound "SE03_77"
    pause (64/32.0)
#SE_VOLC 1,64
    play sound "SE00_47"
#FADE_IN 1
    志雄 "「哈……真舒服。果然洗个澡能赶走身上的疲劳。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LEA06"),"True","img/RI_LEA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI14A_RI007"
    莉莉丝 "「你怎么像个老爸一样。」"
    志雄 "「要你管。」"
    "总之既然已经洗过澡了，之后也没什么特别的事要做，就睡吧……"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "在榻榻米上已经铺好了被子。当然，不是昨日那条大的双人被。我和莉莉丝分开睡，所以有两条被子。"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_PRI 2
#BG_INIC 1
#BG_PRI 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI06B")]=True
    show expression "img/EVN_RI06B@2x.jpg" as bg2 zorder 2 with dissolve
#SE_VOLC 1,0
#MUS_VOL 0
    hide bg1 with dissolve
#BG_ALPC 0
#BG_ALPC 2
    pause (128/32.0)
#BG_INIC 1
#BG_PRI 1
#BG_PRI 2
#BG_ALPC 2
#BG_ALPC 0
#SE_VOLC 1,64
#MUS_VOL 128
    hide bg2 with dissolve
#MESEX_A M_NOA,A_CH_SI,"【志雄】「……嗯！」%K%P"
    "哇，我在回想什么呀！？"
    "可是……昨夜那幕是现实吗？　还是梦呢……？"
    "梦就是愿望的写照。如果说昨夜那光景是梦的话，就是说、那是我的愿望吗……？"
    "可是，如果那不是梦而是现实的话……那么说，莉莉丝真的……"
    志雄 "「不明白……」"
    window hide
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XEA01"),"True","img/RI_XEA01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NRI14A_RI008"
    莉莉丝 "「什么不明白？」"
    志雄 "「哇！？」"
#THREAD_STA 1,THREAD_QUA_WIN
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESA A_CH_SI,"【志雄】「哇！？」"
#THREAD_WAT 1
#WIN_POS 0,0
#MESX "%K%P"
    "意识到时，莉莉丝的脸已经出现在我眼前。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XED04"),"True","img/RI_XED04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI14A_RI009"
    莉莉丝 "「什，什么嘛，真失礼。干吗这么吃惊啊？」"
    "看到我的反应，莉莉丝反而吃了一惊。"
    志雄 "「啊，不，没什么」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XED06"),"True","img/RI_XED06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI14A_RI010"
    莉莉丝 "「……哈哈～多半是在想什么奇怪的事吧？」"
    "奇怪的事？"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 0
#CHR_ALPC 0
#BG_INIC 2
#BG_PRI 2
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI06B")]=True
    show expression "img/EVN_RI06B@2x.jpg" as bg2 zorder 2 with dissolve
#SE_VOLC 1,0
#MUS_VOL 0
    hide bg1 with dissolve
#BG_ALPC 2
    pause (128/32.0)
#BG_INIC 1
#BG_PRI 1
#BG_PRI 2
#BG_ALPC 2
#BG_ALPC 0
#CHR_ALPC 0
#SE_VOLC 1,64
#MUS_VOL 128
    hide bg2 with dissolve
    志雄 "「啊啊啊啊！　不要回想起来啊！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XEB06"),"True","img/RI_XEB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI14A_RI011"
    莉莉丝 "「回，回想起来？」"
    "莉莉丝眉间的皱纹越来越深了。"
    志雄 "「……不，没什么」"
    voice "NRI14A_RI012"
    莉莉丝 "「我看你不像没什么的样子……」"
    志雄 "「不，真的没什么」"
    志雄 "「比、比起这个，虽然有点早，我们还是先睡吧？」"
    "我敷衍般地说道。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XEB01"),"True","img/RI_XEB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI14A_RI013"
    莉莉丝 "「嗯，说的也是。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我低头看着铺好的被子。"
    "由于昨晚的那点事儿，我怎么都没办法不在意。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MEA01"),"True","img/RI_MEA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI14A_RI014"
    莉莉丝 "「今天玩了一整天，游了那么久的泳也实在累了。那就快点刷完牙睡吧。」"
    "不过，莉莉丝的态度和往常没有任何变化。"
    "果然昨晚的事是梦吗……"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    stop music fadeout 1
    play sound "SE00_27"
    voice "NRI14A_YG000"
    雄吾？ "「喂～志雄。在吗～」"
    "这声音……是老爸吗？"
    "正当我这么想时，门被打开了，意料之中的人物出现在我面前。"
    window hide
    play sound "SE00_47"
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA05"),"True","img/SF_MAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    play music  "BGM12"
    voice "NRI14A_YG001"
    雄吾 "「哟，我可爱的儿子～过得好吗？」"
    "是老爸……而且还喝醉了。"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2,(320-160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA03"),"True","img/KR_MAA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .25
    with dissolve
    "紧跟在老爸之后，香里阿姨也出现了。"
    voice "NRI14A_KR000"
    香里 "「志雄君，对不起呢。这个人喝醉了……」"
    voice "NRI14A_YG002"
    雄吾 "「什么？　我可没醉。想要灌醉我的话就把酒桶拿来。唔哈哈哈哈！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA07"),"True","img/SF_MAA07A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI14A_YG003"
    雄吾 "「哈哈哈哈哈，啊哈哈哈！」"
    "老爸是这种喝醉酒就会笑的人……？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA02"),"True","img/KR_MAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI14A_KR001"
    香里 "「说什么呢，真是的。来，喝点水冷静一下」"
    "说着，香里拿出来的是一个酒杯。"
    "……咦？"
    "等，等一下！　难道香里阿姨也醉了吗？"
#MES_SYNC2
    voice "NRI14A_RI015"
    莉莉丝・志雄 "「妈妈，你在干什么呀！？」\n「老爸，你在干什么呀！？」"
    play sound "SE03_25"
    voice "NRI14A_YG004"
    雄吾 "「噢噢，异口同声地说出来了。哈哈哈」"
    voice "NRI14A_KR002"
    香里 "「真厉害，你们真是太合拍了」"
    "老爸和香里对我们鼓起掌来。"
    "不不不不，即使被两个醉酒的人夸奖，我也只会困扰而已。"
    stop se
    志雄 "「就算是在旅行，这也喝太多了吧……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA05"),"True","img/SF_MAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI14A_YG005A"
    雄吾 "「笨蛋。我不管怎么喝，不管怎么……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA03"),"True","img/SF_MAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#THREAD_STA 1,THREAD_QUA_CHR1
    voice "NRI14A_YG005B"
    extend "呜……」"
#THREAD_WAT 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA03"),"True","img/KR_MAA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI14A_KR003"
    香里 "「没，没事吧！？　雄吾！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA04"),"True","img/KR_MAA04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI14A_KR004"
    香里 "「对不起，都是我不断劝酒……对不起，真是对不起，呜呜呜，咕，呜呜……」"
    "香里哭了起来！？"
    voice "NRI14A_RI016"
    莉莉丝 "「妈妈是醉了酒就会哭的……」"
    "一边是一醉酒就会笑，一边是一喝酒就会哭……这对夫妇究竟是怎么回事？"
    voice "NRI14A_YG006"
    雄吾 "「唔……志雄，借我洗手间一用行吗……」"
    志雄 "「啊，啊啊……当然」"
    voice "NRI14A_YG007"
    雄吾 "「不好意思……莉莉丝，香里拜托你了」"
    window hide
    play sound "SE00_17"
    hide lh1 with dissolve
    "老爸这家伙，究竟是干吗来了……？"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_XAA04"),"True","img/KR_XAA04A@2x.png") as lh1 zorder 100:
        ypos 0.0
    with dissolve
    voice "NRI14A_KR005"
    香里 "「呜呜，对不起，真是对不起……都怪我没看管好雄吾才给莉莉丝和志雄君造成……呜呜……」"
    志雄 "「啊，那个，香里阿姨不要哭了……」"
    voice "NRI14A_RI017"
    莉莉丝 "「哈……真是的……」"
    window hide
    stop music fadeout 1
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
    stop music fadeout 1
#FADE_IN 1
    voice "NRI14A_YG008"
    雄吾 "「呼～……志雄真是长大了呢……」"
    voice "NRI14A_KR006"
    香里 "「咕……呜呜……要和志雄君和睦相处哟……」"
    "结果老爸和香里大闹一场之后就睡着了。最要命的是还睡在我们的房间。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LEA05"),"True","img/RI_LEA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI14A_RI018"
    莉莉丝 "「真是一对乱来的新婚夫妇呢……」"
    志雄 "「真是的……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我叹了一口气，然后低头看向两个已经睡着的人。"
    "顺便一提，即使是睡着了，这两人的手还是牵在一起。"
    window hide
    play music  "BGM14"
    志雄 "「哈。不过，我和莉莉丝也……」"
    "——总有一天也会像他们这样吧？"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LEA01"),"True","img/RI_LEA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI14A_RI019"
    莉莉丝 "「诶？」"
    志雄 "「诶？　啊，不，没什么。」"
    "说到一半的话，我慌忙吞了回去。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LEA04"),"True","img/RI_LEA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    莉莉丝 "「……？」"
#MESEX_A M_NOA,A_CH_RI,NRI14A_RI020,"【りりす】「……？」%K%P"
    志雄 "「总之，把他们搬到房间去吧。」"
    voice "NRI14A_RI021"
    莉莉丝 "「嗯，可是搬的话会很辛苦哟？　要不我们睡在他们房间吧。」"
    志雄 "「啊啊，也是。"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    extend "喂，老爸，钥匙借我一用」"
#MESX "喂，老爸，钥匙借我一用」%K%P"
    play sound "SE03_03"
    voice "NRI14A_YG009"
    雄吾 "「……哦……ＺＺＺ……」"
    window hide
#FADE_OUT 1
    pause (32/32.0)
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG63NA4@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG63NA4@2x.jpg" as bg0 with dissolve
    play sound "SE00_47"
#FADE_IN 1
    志雄 "「呃，好重的酒味！」"
    voice "NRI14A_RI022"
    莉莉丝 "「稍微开点窗子吧」"
    play sound "SE00_42"
    "老爸他们的房间和我们一样，被子也已经铺好了。"
    "唯一的区别就是，他们房间明显有着喝完酒的痕迹。"
    "我和莉莉丝叹着气收拾起来。"
    志雄 "「姑且不说我老爸，我还以为香里阿姨是个可靠点的人呢……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MEA06"),"True","img/RI_MEA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI14A_RI023"
    莉莉丝 "「真不好意思，平时的话确实不是这样的。」"
    "莉莉丝的脸上浮现出了苦涩的笑容。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MEA05"),"True","img/RI_MEA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI14A_RI024"
    莉莉丝 "「呼……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MEB01"),"True","img/RI_MEB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI14A_RI025"
    莉莉丝 "「刚才又忙了一阵，更乏了，差不多就睡吧。」"
    志雄 "「嗯，说的也是……」"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
    show expression "img/NIMG02D@2x.jpg" as bg2 zorder 2 with dissolve
    play sound "SE06_16"
#FADE_OUT 1
#SE_WATC 0
#BG_SWPC 0
#BG_PRI 0
#BG_ALPC 0
    hide bg2 with dissolve
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE03_46"
#FADE_IN 1
    "我躺下后，一旁的莉莉丝钻进被子的声音也传入了我耳中。"
    "面对着莉莉丝睡，总觉得有些害羞，因此我现在背对着她。莉莉丝也和我一样，背对着我。"
    "刚才老爸他们的姿态浮现在我脑海中。"
    "手牵着手的两人……那幸福的表情一定不是因为酒的缘故。"
    志雄 "「……」"
#MESEX_A M_NOA,A_CH_SI,"【志雄】「……」%K%P"
    "那是两人相互信赖，幸福的睡脸。这种关系真美好。"
    voice "NRI14A_RI026"
    莉莉丝 "「志雄……」"
    "背后传来小声呼唤我名字的声音。"
    window hide
    stop se fadeout 1
#SE_VOLC 1,255
#BG_SET_BACK 
#BG_INIC 0
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI08A")]=True
    show expression "img/EVN_RI08A@2x.jpg" as bg0 with dissolve
    "我假装转身面向莉莉丝的方向。"
    志雄 "「……」"
    莉莉丝 "「……」"
#MESEX_A M_NOA,A_CH_SI,"【志雄】「……」%K%P"
#MESEX_A M_NOA,A_CH_RI,NRI14A_RI027,"【りりす】「……」%K%P"
    "莉莉丝一言不发。我也什么都不说。取而代之的是，盖着被子的莉莉丝似乎稍稍动了一下。"
    "莉莉丝也一定在想着同样的事吧。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI08B")]=True
    show expression "img/EVN_RI08B@2x.jpg" as bg0 with dissolve
    "我悄悄地握住了从被子里伸出的手。"
    voice "NRI14A_RI028"
    莉莉丝 "「晚安，志雄。」"
    志雄 "「晚安，莉莉丝。」"
    "有些痒，有些害羞，似乎又有些欣喜……感受着这种温暖，我们相互笑了起来。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with None
#FADE_IN 0
    "即使在梦里，莉莉丝也一直紧握着我的手。"
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
#label THREAD_QUA_CHR1
#QUA_CHR 0
#EOT