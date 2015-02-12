label NRI12A:
    $currentlabel = "NRI12A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '28'
    $date = '5'
    window hide
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG63NA2@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG63NA2@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA02"),"True","img/RI_LBA02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE05_16L"
    pause (32/32.0)
    莉莉丝 "「……」"
    志雄 "「……」"
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
#MESEX_A M_NOA,A_CH_RI,NRI12A_RI000,"【りりす】「……」%K%P"
#MESEX_A M_NOA,A_CH_SI,"【志雄】「……」%K%P"
    "为什么。"
    "究竟是为什么！？为什么只要是两个人独处时，就没有任何对话呢？"
    "我和莉莉丝在双人被前一言不发。"
    "……就是这个！"
    "一定是这个会令人浮想联翩的东西造成的！"
    志雄 "「总、总之先得把被子收拾好？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA03"),"True","img/RI_LBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI12A_RI001"
    莉莉丝 "「诶？」"
    志雄 "「把被子拿到老爸他们的房间里，他们一定会有备用的被子的。这被子也太……这个……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBC04"),"True","img/RI_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI12A_RI002"
    莉莉丝 "「说、说的也是呢……」"
    "……？莉莉丝这家伙，似乎有些遗憾啊……"
    stop sound
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD01"),"True","img/RI_LBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM02"
    voice "NRI12A_RI003"
    莉莉丝 "「好，那我们就把它收拾起来吧！」"
    志雄 "「哦，哦！」"
    "我和莉莉丝刻意高声说道。"
    "只是收拾被子而已，为什么非要这么费劲呢？——连我自己也不知道。"
    志雄 "「那我拿这头，莉莉丝拿那头。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA01"),"True","img/RI_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI12A_RI004"
    莉莉丝 "「了解！」"
    "莉莉丝和我分别拿着被子的两端，靠近把被子对折——"
    window hide
#CHR_SORT 1
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    hide lh1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBC05"),"True","img/RI_XBC05A@2x.png") as lh0 zorder (10-1):
        ypos 0.0
    with dissolve
    stop music fadeout 1
#ROUTINE_STA
#CHR_ALP_AUTOC 0,0,0,1
#CHR_ALP_AUTOC 1,128,0,1
#ROUTINE_STP
#BG_BLUR 0
    "于是，莉莉丝的脸出现在我眼前。那柔软的嘴唇也近在眼前，再靠近的话就要碰到了……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBC06"),"True","img/RI_XBC06A@2x.png") as lh0 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI12A_RI005"
    莉莉丝 "「唔哇哇！？」"
    志雄 "「哦哇哇！？」"
#QUA_ALL
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MES_SYNC2
#MESA A_CH_RI,NRI12A_RI005,"【りりす・志雄(りりす)】「唔哇哇！？」%NS「哦哇哇！？」"
#THREAD_WAT 1
#WIN_POS 0,0
#MESX "%K%P"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SBA02"),"True","img/RI_SBA02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE03_07"
#ROUTINE_STA
#CHR_ALP_AUTOC 0,128,0,1
#CHR_ALP_AUTOC 1,0,0,1
#ROUTINE_STP
#BG_BLUR 0
    play sound "SE05_16L"
    "我和莉莉丝都不由自主地把被子扔在地上，向后退去。"
    "我在做什么呀！用这种方法叠被子，莉莉丝会来到我面前那不是当然的嘛！？"
    志雄 "「果、果然两个人叠被子效率太低了！」"
    voice "NRI12A_RI006"
    莉莉丝 "「是、是呢！」"
    志雄 "「那我来收拾被子，莉莉丝叠毛毯吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD01"),"True","img/RI_MBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI12A_RI007"
    莉莉丝 "「好的。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我靠近刚才扔在地上的被子，独自开始叠起被子。这时，莉莉丝把手伸向毛毯。"
    "由于是双人用的大被，我把被子叠成三层，捧了起来。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD01"),"True","img/RI_MBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "瞥了一眼旁边，莉莉丝也叠完了毛毯，把它拿了起来。"
    志雄 "「好的，接下来一下子塞到壁橱里去！」"
    voice "NRI12A_RI008"
    莉莉丝 "「嗯。我们数一二三一起放！」"
    voice "NRI12A_RI009"
    莉莉丝・志雄 "「一，二～」"
    voice "NRI12A_RI010"
    莉莉丝・志雄 "「三！」"
    "我把叠起来的被子，莉莉丝把叠起来的毛毯一口气准备塞进壁橱里——"
    window hide
#CHR_SORT 1
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBD01"),"True","img/RI_XBD01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    stop sound
#ROUTINE_STA
#CHR_ALP_AUTOC 0,0,0,1
#CHR_ALP_AUTOC 1,128,0,1
#ROUTINE_STP
#BG_BLUR 0
    hide lh0 with dissolve
    "莉莉丝的脸再次出现在我的面前。那柔软的嘴唇也近在我眼前，再靠近的话就要碰到了……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBB02"),"True","img/RI_XBB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI12A_RI011"
    莉莉丝・志雄 "「哇—！　哇—！　哇—！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SBC04"),"True","img/RI_SBC04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE03_07"
#ROUTINE_STA
#CHR_ALP_AUTOC 0,128,0,1
#CHR_ALP_AUTOC 1,0,0,1
#ROUTINE_STP
#BG_BLUR 0
    play sound "SE05_16L"
    "我在做什么呀！　用这种方法收拾，莉莉丝会来到我面前那不是当然的嘛！"
    志雄 "「没，没关系，莉莉丝！　毛毯和被子都由我来收拾吧！」"
    voice "NRI12A_RI012"
    莉莉丝 "「知，知道了！」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我把已经折好的被子和毛毯一条一条塞进壁橱。"
    "就在这时，我们注意到。"
    志雄 "「话说……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA06"),"True","img/RI_MBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI12A_RI013"
    莉莉丝 "「普通的被子！　不是有吗！」"
    "壁橱里整整齐齐地放着两人份的被子。"
    "果然是稻穗的阴谋吗……"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_SET_BACK 
#BG_INIC 0
#FADE_IN 0
    "我们把两床单人被拿出来，铺在地上。"
    window hide
#FADE_OUT 0
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG63NA3@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG63NA3@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    play music  "BGM16"
    "……呼。终于告一段落了。"
    "被子的问题也解决了。这下我和莉莉丝能毫无顾忌地说话了吧。"
    志雄 "「那个……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBB02"),"True","img/RI_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "说什么呢？"
    "……"
    "…………"
    "说什么好呢！？"
    voice "NRI12A_RI014"
    莉莉丝 "「那个……」"
    "莉莉丝也和我一样，正在犹豫着说什么好。"
    "和之前双人被在的时候一样，令人尴尬的沉默……"
    志雄 "「……」"
#MESEX_A M_NOA,A_CH_SI,"【志雄】「……」%K%P"
    志雄 "「啊，我去洗个澡吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBC02"),"True","img/RI_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI12A_RI015"
    莉莉丝 "「嗯，嗯。我也去。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我站了起来，开始准备沐浴露和毛巾。莉莉丝也开始准备，而我不等莉莉丝，自己先走出了房间。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    show expression "img/BG62NA@2x.jpg" as bg1 zorder 1 with dissolve
    stop sound fadeout 1
    play sound "SE00_47"
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
#BG_SWPC 0
    hide bg1 with dissolve
#BG_ALPC 1
#BG_PRI 0
#BG_PRI 1
    scene expression "img/BG62NA@2x.jpg" as bg0 with dissolve
    "啊啊啊啊！　我在逃避什么呀！？"
    window hide
#FADE_OUT 1
    pause (32/32.0)
    play sound "SE05_17L"
    play sound "SE03_77"
    stop sound fadeout 1
    play sound "SE03_64"
#SE_WATC 1
    play sound "SE05_16L"
#FADE_IN 1
    志雄 "「哈……热水真舒服」"
    "和莉莉丝在一起时由于紧张而产生的疲劳，在进入澡堂后就完全消失了。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
#SE_VOLC 1,64
    play sound "SE00_47"
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
#BG_SWPC 0
#BG_ALPC 1
#BG_PRI 0
#BG_PRI 1
    scene expression "img/BG63NA3@2x.jpg" as bg0 with dissolve
    "回到房间后，莉莉丝已经睡在了铺好的被子里。"
    "已经换上睡衣了，大概是洗完澡就睡了吧。"
    window hide
    stop sound fadeout 1
#BG_SET_BACK 
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI05A")]=True
    show expression "img/EVN_RI05A@2x.jpg" as bg1 with dissolve
    志雄 "「不过话说回来，这家伙还是老样子，一副毫无防备的样子……」"
    莉莉丝 "「……嗯……ＺＺＺ……」"
#MESEX_A M_NOA,A_CH_RI,NRI12A_RI016,"【りりす】「……嗯……ＺＺＺ……」%K%P"
    "莉莉丝连毛毯也没盖就睡着了。该不会是晕过去了吧，稍微有些担心。"
    志雄 "「莉莉丝，睡觉的话要盖好啊。这样会感冒的。」"
    voice "NRI12A_RI017"
    莉莉丝 "「嗯，唔嗯……」"
    志雄 "「哦～」"
    莉莉丝 "「嗯，嗯嗯……」"
#MESEX_A M_NOA,A_CH_RI,NRI12A_RI018,"【りりす】「嗯，嗯嗯……」%K%P"
    "不管我怎么叫，都只能听见她睡着的呼吸声而已。我轻轻叹了口气。"
    "不过，这家伙不容易叫醒，我是比谁都清楚的。"
    "没办法。我决定帮莉莉丝盖上毛毯。"
    "正在这时——"
    莉莉丝 "「嗯……」"
#MESEX_A M_NOA,A_CH_RI,NRI12A_RI019,"【りりす】「嗯……」%K%P"
    window hide
    stop music fadeout 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI05B")]=True
    show expression "img/EVN_RI05B@2x.jpg" as bg1 with dissolve
    志雄 "「……！？」"
#MESEX_A M_NOA,A_CH_SI,"【志雄】「……！？」%K%P"
    "莉莉丝翻了个身，她的睡衣稍稍有些展开。"
    "因为刚洗完澡吧，莉莉丝的脸颊还有些泛红。"
    "不止是脸颊，睡衣附近的皮肤都有些发红。"
    "配合着呼吸，胸部有节奏地起伏着……"
    "…………"
    志雄 "「哈！？」"
    "我在盯着哪里看呀！？"
    "…………"
    "不过，等等……现在不正是应该接吻的好时机吗？"
    "不不，可是……"
    志雄 "「……」"
#MESEX_A M_NOA,A_CH_SI,"【志雄】「……」%K%P"
    window hide
    play sound "SE05_16L"
    hide bg1 with dissolve
    play sound "SE03_28"
    "……结果我还是从莉莉丝身上移开视线，在那毫无防备的身体上胡乱盖上了毯子。"
    莉莉丝 "「嗯嗯…………」"
#MESEX_A M_NOA,A_CH_RI,NRI12A_RI020,"【りりす】「嗯嗯…………」%K%P"
    志雄 "「哈……」"
    "刚洗完澡明明应该很轻松的，现在又疲惫起来。"
    志雄 "「今天就睡吧……」"
    "我暗自嘀咕着，正当我想在睡前刷个牙的时候……"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MEB05"),"True","img/RI_MEB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI12A_RI021"
    莉莉丝 "「唔……」"
    "揉着眼睛，莉莉丝突然坐了起来。"
    志雄 "「怎……」"
    "难道她一直醒着吗！？　那么我刚才想要接吻的姿态也……！？"
    voice "NRI12A_RI022"
    莉莉丝 "「呼……我再去……洗个澡……」"
    "莉莉丝一边打着哈欠一边说道。"
    志雄 "「洗澡？　刚才不是洗过了吗？」"
    voice "NRI12A_RI023"
    莉莉丝 "「（摇头）……嗯……」"
    hide lh0 with dissolve
    "到底是肯定还是否定啊。在这莫名其妙的回应之后，莉莉丝晃晃悠悠地朝门的方向走去。"
    play sound "SE00_48"
    "那家伙没关系吧……？"
    "没办法……在她回来之前我还是等着吧。"
    志雄 "「总之看看电视来打发时间吧……」"
    "明明是备考生，现在居然想不到复习，真不应该啊……"
    window hide
    play sound "SE02_03"
    pause (64/32.0)
    play sound "SE02_03"
    pause (32/32.0)
    play sound "SE02_03"
    志雄 "「频道很少……」"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    pause (64/32.0)
#SE_VOLC 1,128
#FADE_IN 1
    志雄 "「呼……」"
    "我不禁打了个哈欠。莉莉丝还没有回来。"
    "今天坐电车过来之后去了很多地方也走了很多路，已经相当疲倦了吧。"
    志雄 "「好困……」"
    "可是，莉莉丝还没回来……"
    "可是，好困啊……"
    志雄 "「……ｚｚｚ」"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    pause (64/32.0)
#FADE_IN 0
    play music  "BGM14"
    "嗯……怎么了？　莉莉丝？"
    "你在干什么……？"
    "……身体不能动弹……总觉得脑子也迷迷糊糊的。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI06A")]=True
    show expression "img/EVN_RI06A@2x.jpg" as bg0 with dissolve
    voice "NRI12A_RI024"
    莉莉丝 "「志雄……」"
    "这就是传说中的『缚身术』吗？　还是说，这是梦吗？"
    voice "NRI12A_RI025B"
    莉莉丝 "「为什么……不了解我的心情呢……」"
    "正当我在思考之时，嘴唇上有柔软的感觉。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI06B")]=True
    show expression "img/EVN_RI06B@2x.jpg" as bg0 with dissolve
    莉莉丝 "「……嗯……」"
    "嘴边的气息很温暖。"
    志雄 "「唔……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI06A")]=True
    show expression "img/EVN_RI06A@2x.jpg" as bg0 with dissolve
    voice "NRI12A_RI027"
    莉莉丝 "「啊……」"
    "在惊讶什么啊？"
    志雄 "「莉莉丝……」"
    voice "NRI12A_RI028"
    莉莉丝 "「……」"
#MESEX_A M_NOA,A_CH_RI,NRI12A_RI028,"【りりす】「……」%K%P"
    window hide
    show expression "img/NIMG02D@2x.jpg" as bg0 with dissolve
    "咦？　莉莉丝……在哪里……"
    "是梦吗……？"
    window hide
    stop music fadeout 1
#FADE_OUT 1
#FADE_IN 0
    "…………"
    "……"
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
#label THREAD_QUA_CHR1_WIN
#QUA_CHR 1
#TH_QUAKE_WIN
#EOT