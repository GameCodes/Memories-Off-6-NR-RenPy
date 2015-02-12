label NSU10A:
    $currentlabel = "NSU10A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '28'
    $date = '5'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG63EA@2x.jpg" as bg0 zorder 0 with dissolve
    play sound "SE05_13L"
    pause (32/32.0)
#FADE_IN 1
    play music "OBGM17"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
#SE_VOLC 1,(64/2)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAB02"),"True","img/SU_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU10A_SU000"
    鈴・志雄 "「哎，真累呢——」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC01"),"True","img/SU_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU10A_SU001"
    铃 "「明明没跑那么长时间，一直都是坐在车上」"
    志雄 "「铃已经习惯这样了，也会感到累吗？」"
    voice "NSU10A_SU002"
    铃 "「今天一直是两个人在骑车，是会比平时累啊」"
    志雄 "「啊，对不起」"
#CHR_GET_POSC 0,F24,F25
#RSUB F24,(320)
#BG_LAY 3,SU_LXB04,2,F24
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAB04"),"True","img/SU_LAB04A@2x.png") as lh0 zorder (10+0):
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
    voice "NSU10A_SU003"
    铃 "「没必要道歉的，我才要说对不起呢。我喜欢让你坐在后面，你不用道歉」"
#THREAD_STP 1
    hide bg3 with dissolve
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAB01"),"True","img/SU_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU10A_SU004"
    铃 "「而且志雄应该比我还要累吧？」"
    志雄 "「嗯，说真的，是有点腰疼」"
    "由于必须一直保持身体前倾抓着她的腰，早上起来身体出乎意料的僵硬。"
    "大概是用上了平时不太锻炼的肌肉吧。"
    voice "NSU10A_SU005A"
    铃 "「所以说啊。{w=3}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAB02"),"True","img/SU_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU10A_SU005B"
    extend "对了，这会正是泡温泉的好时机。」"
    志雄 "「是呢，可以慢慢地享受」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAB01"),"True","img/SU_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU10A_SU006"
    铃 "「对了，志雄，顺便告诉你浴池可不是混浴的哦？」"
    志雄 "「哎！？等等，我可没期待这个！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC03"),"True","img/SU_LAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU10A_SU007"
    铃 "「这说法我怎么听着那么别扭啊，这算什么啊？」"
    志雄 "「不啊，是铃这也不行那也不行的……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC02"),"True","img/SU_LAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU10A_SU008"
    铃 "「真是的，被我锻炼了这么久身体还是没有变得好起来吗」"
    志雄 "「哎……？」"
    "是这个方向上的别扭吗？"
    "这就是所谓的女性的性感，或者说成年人的魅力吗……？"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAB02"),"True","img/SU_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU10A_SU009"
    铃 "「呵呵，那就赶快进去吧？」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "不知不觉，铃已经把换下的衣服和浴衣夹在腋下，准备从房间里走出去。"
    志雄 "「哎，换衣服换衣服……」"
    "我慌忙抓起换下的衣服追在后面。"
    "铃真的很开心啊，所谓的取材旅行都变成什么样了……"
    window hide
    stop sound fadeout 1
    stop music
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG64NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG64NA@2x.jpg" as bg0 with dissolve
    play sound "SE00_49"
    play sound "SE05_16L"
    pause (32/32.0)
#EFF_STAC 0,YUGE2,EFF_NOSKIP
#FADE_IN 1
#SE_VOLC 1,64
    play music "BGM11"
    "浴池并不算大，基本是丝柏式的袖珍型构造。大概是没有其他客人的缘故，现在给人感觉是个非常惬意的地方。"
    play sound "SE03_78"
    志雄 "「啊～」"
    "仔细地洗净了身上的汗水和污渍，从脚尖起慢慢浸入浴池。"
    "当肩部也浸入水中的时候，忍不住像个大叔一样叹了一口气。"
    志雄 "「看来很容易上瘾啊」"
    "平时泡温泉虽然也会令人心情愉快，不过由于乘坐摩托的速度而导致的疲劳，相比之下现在的感觉更是舒畅。"
    志雄 "「哼哼……温泉旅行也不错嘛」"
    "说起旅行，浮现在脑海中的都是娱乐场所和观光地这种地方。"
    "不过以温泉为目的的休闲式旅行也挺舒适的。"
    "只是又会被亨称为老头子了。"
    voice "NSU10A_SU010_K"
    铃 "「感觉不错吧～！」"
    志雄 "「是啊……铃！？」"
    "不知为何，我听到了铃的声音在回答我。"
    "这里的墙壁薄到这种程度么……"
    voice "NSU10A_SU011_K"
    铃 "「是我」"
    "我寻找起音源，发现声音是从为了通气而打开的窗户里传来的。"
    志雄 "「原来窗户开着啊」"
    voice "NSU10A_SU012_K"
    铃 "「嗯，这里的窗户是开着的，所以能听见吧。因此我才听到志雄大叔般的感慨」"
    志雄 "「好了，不要说这些了……话说回来，这里没有其他的客人吗？」"
    "靠近打开的窗户，铃的声音听得更清楚了。"
    voice "NSU10A_SU013_K"
    铃 "「只有我一个～」"
    志雄 "「我这里也是，客人这么少啊？」"
    voice "NSU10A_SU014_K"
    铃 "「啊，现在好像是预备开放中，只有住宿的客人可以进来」"
    志雄 "「原来如此，总觉得有点浪费呢」"
    voice "NSU10A_SU016_K"
    铃 "「绝对不浪费，感觉这次会成为非常愉快的旅行」"
    志雄 "「嗯，饭也很好吃，这就不用说了」"
    "享受着悠然的心情，我闭上双眼，从早上开始积累下的慌乱情绪就像浮云般消散了。"
    voice "NSU10A_SU017_K"
    铃 "「哼～哼，是这样啊」"
    "铃的声音断断续续离我更近了。"
    志雄 "「你在干什么？」"
    voice "NSU10A_SU018_K"
    铃 "「没什么，我在想这里的浴室是怎样造的」"
    志雄 "「真是奇怪的爱好」"
    "莫非这也是取材的一道流程？"
    "正当我这样想的时候，铃的声音愈发接近了。"
    voice "NSU10A_SU019_K"
    铃 "「唔～嗯，这院子果然是连通的呢」"
    志雄 "「这怎么了？」"
    voice "NSU10A_SU020_K"
    铃 "「你努力从窗户出来的话，是可以偷窥到这里的哟？」"
    play sound "SE03_77"
#THREAD_STA 1,THREAD_QUA_WIN
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    志雄 "「噗！你、你在说什么！？」"
#MESA A_CH_SI,"【志雄】「噗！你、你在说什么！？」"
#THREAD_WAT 1
#WIN_POS 0,0
#MESX "%K%P"
    "我不禁从浴池中一下子站了起来。"
    voice "NSU10A_SU021_K"
    铃 "「你在胡闹什么？还真的想偷窥啊？」"
    志雄 "「我怎么可能做出这种事！会被逮捕的啊！」"
    "这人真是的……那么喜欢捉弄人。"
    voice "NSU10A_SU023_K"
    铃 "「不过，混浴也不是办不到哦」"
    志雄 "「怎么回事？」"
    voice "NSU10A_SU024_K"
    铃 "「这里的浴池虽然是男女分开的，不过可以以家族浴池的名义包场的」"
#MUS_VOL 0
    志雄 "「哎？」"
    voice "NSU10A_SU025_K"
    铃 "「也就是说，可以一起进同一个浴池，怎么样，要租下来吗？」"
    window hide
#BG_SET_BACK 
#FADE_OUT 1,32,COL_WHITE
#EFF_STPC 0,EFF_NOSKIP 
    show expression "img/NIMG13A@2x.jpg" as bg3 zorder 3 with dissolve
#CHR_INIC 0
#CHR_PRIC 0
#CHR_ALPC 0
#CHR_POSC 0,320,512
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XFB02"),"True","img/SU_XFB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#EFF_STAC 0,BG_WAVE_IN,EFF_NOSKIP
#FADE_IN 1
    pause (32/32.0)
#CHR_POS_AUTOC 0,320,100,0,1
#CHR_ALP_AUTOC 0,128,0,1
    play sound "SE07_02"
#EFF_STPC 0,EFF_NOSKIP
    pause (64/32.0)
#EFF_STAC 0,BG_WAVE_OUT,EFF_NOSKIP
#CHR_POS_AUTOC 0,320,512,0,1
#CHR_ALP_AUTOC 0,0,0,1
    pause (8/32.0)
#FADE_OUT 1,32,COL_WHITE
#EFF_STPC 0,EFF_NOSKIP
    hide bg3 with dissolve
#CHR_PRIC 0
    hide lh0 with dissolve
#CHR_ALPC 0,128
#EFF_STAC 0,YUGE2,EFF_NOSKIP
#FADE_IN 1
    "等、等等……这是认真的吗！？"
    "我……和、和铃一起……！？混浴！？"
    志雄 "「那个……给、给我十秒钟考虑一下！」"
    voice "NSU10A_SU026_K"
    铃 "「要不要租啊～？」"
    window hide
#FADE_OUT 1,16,COL_WHITE
#EFF_STPC 0,EFF_NOSKIP 
    show expression "img/NIMG13A@2x.jpg" as bg3 zorder 3 with dissolve
#CHR_INIC 0
#CHR_PRIC 0
#CHR_ALPC 0
#CHR_POSC 0,320,512
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XFB02"),"True","img/SU_XFB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#EFF_STAC 0,BG_WAVE_IN,EFF_NOSKIP
#FADE_IN 1
    pause (32/32.0)
#CHR_POS_AUTOC 0,320,100,0,1
#CHR_ALP_AUTOC 0,128,0,1
#EFF_STPC 0,EFF_NOSKIP
    play sound "SE07_02"
    pause (64/32.0)
#EFF_STAC 0,BG_WAVE_OUT,EFF_NOSKIP
#CHR_POS_AUTOC 0,320,512,0,1
#CHR_ALP_AUTOC 0,0,0,1
    pause (8/32.0)
#FADE_OUT 1,32,COL_WHITE
#EFF_STPC 0,EFF_NOSKIP
    hide bg3 with dissolve
#CHR_PRIC 0
    hide lh0 with dissolve
#CHR_ALPC 0,128
#EFF_STAC 0,YUGE2,EFF_NOSKIP
#FADE_IN 1
    "在这里拒绝的话，是不是太没有男子汉的胆量了？"
    "但是，突然间就变成这样，是要有心理准备的……"
    "我该怎么办？同意还是拒绝……"
    window hide
    play sound "SE07_16L"
    voice "NSU10A_SU027_K"
    铃 "「怎么样了～？不快点做决定我就当没说过这句话了～」"
    "呜……我、我该怎么办……"
    voice "NSU10A_SU028_K"
    铃 "「５……４……３、２」"
    "铃开始做倒计时。"
    "而且从３之后加快了速度！"
    志雄 "「等、等等！」"
    voice "NSU10A_SU029_K"
    铃 "「嗯～？怎么了～？」"
    志雄 "「那个……」"
    voice "NSU10A_SU030_K"
    铃 "「我听不见～？」"
    志雄 "「……对不起，我求你再稍等一下！」"
    voice "NSU10A_SU031_K"
    铃 "「……呵呵呵」"
    志雄 "「……哎？」"
    window hide
    stop sound fadeout 1
#MUS_VOL 128
    voice "NSU10A_SU032_K"
    铃 "「呵呵呵……啊哈哈哈哈！」"
    "难、难道，这是……"
    play sound "SE03_82"
    voice "NSU10A_SU033_K"
    铃 "「哦呵呵呵……向我……求饶了啊……」"
    play sound "SE03_58"
#THREAD_STA 1,THREAD_QUA_WIN
    "呜！绝对被捉弄了！被欺骗了！"
#THREAD_WAT 1
#WIN_POS 0,0
#MESX "%K%P"
    "冷静地想一想，这种事情根本就不可能啊……"
    "以铃的性格来看，捉弄我也不出乎意料……"
    "啊！！"
    voice "NSU10A_SU034_K"
    铃 "「啊哈哈哈」"
    "可恶，竟然还在笑……"
    志雄 "「我、我先出去了啊！」"
    "为了掩饰自己羞愧的心情，我迅速从浴池里爬了出来。"
    "虽然我希望能再多待一下吧……"
    stop se fadeout 1
    voice "NSU10A_SU035_K"
    铃 "「啊，志雄，对不起！在入口等我～！」"
    "在叹着气的我的身后，传来了终于收起笑声的铃的声音。"
    window hide
#FADE_OUT 1
#EFF_STPC 0,EFF_NOSKIP
    scene expression Solid("000") with fade
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 0
#BG_SET_DEFC 0,BG62NA
    scene expression "img/BG62NA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    "在走廊稍等片刻，待羞红的脸冷却下来的时候，终于看到穿着浴衣的铃从女浴池中走了出来。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGC01"),"True","img/SU_LGC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU10A_SU036A"
    铃 "「久等了。{w=3}{nw}"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGC04"),"True","img/SU_LGC04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU10A_SU036B"
    extend "啊……生气了吗？」"
    "说实话，我不清楚现在该摆出一副怎样的表情。"
    "不过把我的沉默当成是生气，这误会就太大了。"
    志雄 "「是该说生气好呢……还是该说难为情呢……」"
    "虽说上了当的自己也不对，但她还是把我当成孩子一般看待，这点很让我在意。"
    志雄 "「算了，没什么。如果铃能笑一笑开心的话，那就这样吧」"
    "这么没完没了的话也会后悔，所以听到我说了几句带有自虐性质的话，铃露出过意不去的神情挠着头。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGB01"),"True","img/SU_LGB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU10A_SU037"
    铃 "「玩笑开的过分了，我向你道歉。不过，不知为什么我很安心」"
    志雄 "「安心？」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGA01"),"True","img/SU_LGA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU10A_SU038"
    铃 "「泡完浴池的身体已经冷下来了，回房间去吗？」"
    window hide
    hide lh0 with dissolve
#CHR_INIC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XGA01"),"True","img/SU_XGA01A@2x.png") as lh10 zorder 100:
        ypos 0.0
        xcenter .25
    with dissolve
    "我们走在回廊中，铃继续说道。"
    voice "NSU10A_SU039"
    铃 "「志雄你啊，在学校是学生会会长，对女孩也很温柔，不过竟然在公寓里一个人生活」"
    voice "NSU10A_SU040"
    铃 "「想到这点，真是太了不起了呢」"
    "这也太高估我了吧。"
    "但是，铃能从这样的角度看待我……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XGA04"),"True","img/SU_XGA04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU10A_SU041"
    铃 "「但是呢，透过刚才那一幕，我亲身感受到志雄也是一名普通的高中生」"
    志雄 "「啊哈哈……」"
    "我不由得露出了苦笑。如果真是这样，也只是因为想让喜欢的人看到自己的长处吧。"
    "如果看到不好的地方还能安心的话，那就太奇怪了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XGA07"),"True","img/SU_XGA07A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU10A_SU042"
    铃 "「我啊，想从更多的方面来了解志雄」"
    志雄 "「嗯……」"
    "铃说的如此直白，自己真感到不好意思。"
    "忽然意识到自从来旅行后，一直在被铃用各种各样的手段戏弄。"
    "可即使如此……"
    hide lh0 with dissolve
#CHR_POSC 0,(320)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XGC04"),"True","img/SU_XGC04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU10A_SU043"
    铃 "「嗯，怎么了？不会是头晕吧？」"
    "在浴池里泡微红的脸颊也好，能透过浴衣看到的脖颈也好，这个也好，那个也好。"
    "还散发着香皂的香气……这是该说有相当大的破坏力呢，还是其它什么呢？"
    "啊，不能继续下去了。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XGB01"),"True","img/SU_XGB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU10A_SU044"
    铃 "「哼哼，稍微有点舒服就泡过头了吧？不过感觉确实很舒服呢」"
    志雄 "「啊？嗯，很香的味道」"
    "糟糕，不知不觉就喊出来了。"
    voice "NSU10A_SU045"
    铃 "「是啊，扁柏的香味也不错呢」"
    "危险危险……如果说的是铃本人身上的味道，又该被捉弄了。"
    "就在这时，从过道窜出一个人，与看向我的铃撞了个满怀。"
    window hide
    stop music
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XGA03"),"True","img/SU_XGA03A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
    play sound "SE04_19"
#QUA2_CHR 0
    voice "NSU10A_SU046"
    铃 "「啊，对不起」"
    voice "NSU10A_SN000"
    信？ "「哎呀，不好意思，诶……」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "一瞬间，我和铃都呆住了。"
    "对方看到我的脸，似乎也同样感到惊讶，再看看自己撞到的人，一下子变得面无血色。"
    window hide
    play music "OBGM13"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MGA03"),"True","img/SU_MGA03A@2x.png") as lh0 zorder (10-0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBB04"),"True","img/SN_MBB04A@2x.png") as lh1 zorder (10-1):
        xcenter .75
    with dissolve
    voice "NSU10A_SN001"
    信 "「咦……咦咦咦咦！？」"
    voice "NSU10A_SU047"
    铃 "「……啊！？」"
    "站在面前的是稻穗，而且怎么看都是一副这里的员工的打扮。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBB05"),"True","img/SN_MBB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NSU10A_SN002"
    信 "「那……个」"
    window hide
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBB03"),"True","img/SN_MBB03A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .75
        parallel:
            linear 0.2 alpha 0
        parallel:
            linear 0.2 xcenter 1.0
    with dissolve
    play sound "SE01_00B"
#MOV_CHR_INIT 16
#MOV_CHR1 0,640
#MOV_CHR_GO 1
    hide lh1 with dissolve
#CHR_ALPC 1,128
    "稻穗立刻转过身，想以冲刺的速度逃离现场。"
    "可是……"
    window hide
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MGB04"),"True","img/SU_MGB04A@2x.png") as lh0 zorder (10+10):
        ypos 0.0
    with dissolve
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2,(320-160)
    hide lh0
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MGA05"),"True","img/SU_MGA05A@2x.png") as lh2 zorder (10):
        ypos 0.0
        parallel:
            linear 1 alpha 0
        parallel:
            linear 1 xcenter 1.0
    with dissolve
#MOV_CHR_INIT 24
#MOV_CHR0 0,(320)
#MOV_CHR2 128,(320)
#MOV_CHR_GO 1
#CHR_ALPC 0,128
    voice "NSU10A_SU048"
    铃 "「休想逃！」"
    play sound "SE03_63"
    "铃用尽全力，将拿在手中的浴巾向稻穗投去。"
    stop se
    "浴巾缠住了稻穗的脚！"
    play sound "SE04_17"
#THREAD_STA 1,THREAD_QUA_WIN
    voice "NSU10A_SN003"
    信 "「哎呀！」"
#THREAD_WAT 1
#WIN_POS 0,0
#MESX "%K%P"
    "稻穗翻了个跟头倒在地上。"
    window hide
#MOV_CHR_INIT 16
#MOV_CHR2 0,640
#MOV_CHR_GO 1
    hide lh2 with dissolve
#CHR_ALPC 2,128
    play sound "SE04_36"
    "铃随即用力踩住稻穗的背……捕获完成。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SORT 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320+96)
#CHR_POSC 1,(320+224)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SGC03"),"True","img/SU_SGC03A@2x.png") as lh0 zorder (10-0):
        xcenter (320+96)/640.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_SBA03"),"True","img/SN_SBA03A@2x.png") as lh11 zorder (10-1):
        xcenter (320+224)/640.0
    voice "NSU10A_SU049"
    铃 "「信，你在这种地方做什么？说啊？」"
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_SBB05"),"True","img/SN_SBB05A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
        xcenter (320+224)/640.0
    with dissolve
    voice "NSU10A_SN004"
    信 "「今、今天似乎有更多多余的力气呢……比起平时」"
    "稻穗的气息也渐渐减弱了，至少别再让他痛苦了放松一下吧……"
    voice "NSU10A_SU050"
    铃 "「你真的和女朋友出去旅行了？嗯～？」"
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_SBA04"),"True","img/SN_SBA04A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
        xcenter (320+224)/640.0
    with dissolve
    voice "NSU10A_SN005"
    信 "「她、已经回去了，所以，我才刚来打工……」"
    play sound "SE04_23"
#QUA2_CHR 1
    voice "NSU10A_SU051"
    铃 "「真的吗～？」"
    "铃没有留情，继续来回踩踏着稻穗。"
    "一直深有体会的我很是明白，铃对稻穗根本不会手下留情……好可怕。"
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_SBA03"),"True","img/SN_SBA03A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
        xcenter (320+224)/640.0
    with dissolve
    voice "NSU10A_SN006"
    信 "「痛痛痛痛痛！那是谎话，都是假的，骗人的！」"
    voice "NSU10A_SU052"
    铃 "「果然呢，和女朋友一起旅行根本就是胡说」"
    voice "NSU10A_SN007"
    信 "「没、没错」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SGC06"),"True","img/SU_SGC06A@2x.png") as lh0 zorder (10+10):
        ypos 0.0
        xcenter (320+96)/640.0
    with dissolve
    voice "NSU10A_SU053"
    铃 "「你究竟在想些什么啊，撒这么无聊的谎话……」"
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_SBB01"),"True","img/SN_SBB01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
        xcenter (320+224)/640.0
    with dissolve
    voice "NSU10A_SN008A"
    信 "「挂念心爱的姐姐，为了姐弟间美好的爱……{w=5}{nw}"
    stop music
    play sound "SE04_37"
#QUA2_CHR 1
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_SBB04"),"True","img/SN_SBB04A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
        xcenter (320+224)/640.0
    with dissolve
    voice "NSU10A_SN008B"
    extend "啊呀」"
    hide lh11 with dissolve
    "铃一脚用力踩在稻穗身上，稻穗就这样断了气……不不，是倒下了。"
    "把铃真的惹火的话就会是这种下场吧，我也一定要记住……"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play music "BGM14"
#CHR_INIC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGA05"),"True","img/SU_LGA05A@2x.png") as lh10 zorder 100:
        ypos 0.0
    with dissolve
    voice "NSU10A_SU054"
    铃 "「哼，真是的！那家伙的话果然不能太当真……」"
    "铃不知为什么一副懊悔的表情，狠狠咬住嘴唇。"
    志雄 "「稻穗的话怎么了吗？」"
#CHR_GET_POSC 0,F24,F25
#RSUB F24,(320)
#BG_LAY 3,SU_LXB04,2,F24
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGB04"),"True","img/SU_LGB04A@2x.png") as lh10 zorder (10+10):
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
    voice "NSU10A_SU055"
    铃 "「没、没什么，志雄不要在意」"
#THREAD_STP 1
    hide bg3 with dissolve
    志雄 "「……？」"
    "啊，对了。之前稻穗和铃争得面红耳赤的时候，我在店外不小心听到了。"
    "不过铃不知道我听到了他俩之间的对话。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGC02"),"True","img/SU_LGC02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU10A_SU056"
    铃 "「真的没什么好在意的……总之先回房间去吧」"
    志雄 "「好、好的」"
    "看着稻穗的“遗骸”，我觉得这完全是自作自受。"
    "总之，旅馆里的人会发现他吧。"
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
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_QUA_WIN
#TH_QUAKE_WIN 4
#EOT
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT