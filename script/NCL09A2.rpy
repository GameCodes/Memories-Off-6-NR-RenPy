label NCL09A2:
    $month = '08'
    $day = '10'
    $date = '4'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG14EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG14EA@2x.jpg" as bg0 with dissolve
    play sound "SE05_13L"
    pause (32/32.0)
#FADE_IN 1
    志雄 "「咦？」"
    if not persistent.dictlist[46] and persistent.show_dict:
        $persistent.dictlist[46]=True
        show screen dict_pop(i=46)
    "在公寓门口，我看见了一个许久不见的熟悉面孔。"
    志雄 "「亨？」"
    window hide
#SE_VOLC 1,(64/2)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB05"),"True","img/TO_MBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "BGM09"
    voice "NCL09A_TO019A"
    亨 "「嗯，志雄，你怎么没在家——{w=5}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_TO019B"
    extend "哦，是出去买东西了吧。」"
    "亨好像想问些什么，不过看到我双手拎着的满满的东西就明白了似的点了点头。"
    志雄 "「是哪位同学突然说要吃火锅的来着？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_TO020"
    亨 "「啊，怎么能这么说！我也是在这么热的天里在外面等了很久啊……」"
    "亨瞬间转变出一幅笑脸，拍了拍我的肩膀。"
    志雄 "「虽然这么久没见，你还是老样子啊。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_TO021"
    亨 "「那是当然的啦！我才不是那么容易变的」"
    志雄 "「的确……」"
    "听了亨的话，我一怔，脑中浮现出了学姐的样子，不禁叹了口气。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB05"),"True","img/TO_MBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_TO022"
    亨 "「喂喂，这么没精神啊……接下来是火锅派对不是吗？这么紧张的话，本来开心的事情也开心不起来了哦！」"
    "被亨的叫声拉回现实，我慌忙露出笑容。"
    志雄 "「抱歉抱歉。说起来……那个，难道是你的摩托？」"
    "为了转移话题，我左右移动着视线寻找着能引起话题的东西，最终目光落在了停在亨身边的摩托。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_TO023"
    亨 "「哦？哦哦，好眼光啊！是啊，就是我的坐骑！」"
    "相当自豪啊。刚才还一脸担心的亨瞬间变为笑容，手也放在了摩托车上。"
    志雄 "「真厉害呢。不过我先问一句你拿到驾照了吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_TO024"
    亨 "「是啊～很麻烦才拿到呢。摩托的钱是用压岁钱还有微不足道的的打工收入，还向父母借了一部分才筹足了呢。嘛，不过那也是有代价的」"
    志雄 "「代价？」"
    voice "NCL09A_TO025"
    亨 "「对。父母借钱的时候提出了条件。就是这个夏天我必须认真参加暑期补习。明明是高中最后的暑假，却没有什么自由的时间咯」"
    志雄 "「倒不如说这才是备考生真正应该做的吧！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA06"),"True","img/TO_MBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_TO026"
    亨 "「不过，反正现在也对摸底成绩没什么信心，正好借这个机会提高一下吧。」"
    "听这语气，想必亨已经决定好要报考哪一所院校了吧。连最不靠谱的亨也找到目标并在努力做准备了。"
    "而相反的，我……"
    "不过貌似这种事情也不是他自己的意思啊。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_TO027"
    亨 "「啊，对了。我有个问题想和你说一下……」"
    志雄 "「问题？」"
    "面对我的疑问，亨大大地耸了耸肩膀，把手里拿着的塑料袋拿到我跟前打开。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_TO028"
    亨 "「说过了吧？为了买摩托我把压岁钱全都用了，彻底没钱了。所以，我只能拿出这些了呢」"
    志雄 "「喂……」"
    "亨手里拿着的袋子里，除了两袋魔芋之外，什么都没有。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_TO029"
    亨 "「哈～最近没钱所以也就没什么可吃的。而且，也能通过这次聚会见到莉莉丝！这实在是个一石二鸟的办法」"
    "面对笑着的亨，我也只能『呵呵』以对。"
    志雄 "「啊，俗话说『追二兔者终不得一兔』呢」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_TO030"
    亨 "「不不，我认真起来的话肯定是能两全其美的！」"
    志雄 "「唉，什么跟什么啊。总之，赶紧帮忙把东西拿进去吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_TO031"
    亨 "「哦！『不劳动者不得食』，我懂，你放心吧～」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我把手上大部分东西递给了亨，就径直走进了公寓里。"
    voice "NCL09A_TO032"
    亨 "「哇！等等！这些实在是太沉了——」"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/OIBG012A@2x.png" as bg0 zorder 0 with dissolve
    scene expression "img/BG33AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    "一进家门，我和亨把东西往脚边一扔，就开始大口地喘起气来。"
    window hide
    play sound "SE03_42"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_TO033"
    亨 "「啊～沉死了。东西放哪里？」"
    志雄 "「总之先放到厨房去吧。」"
    voice "NCL09A_TO034"
    亨 "「了解！」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    pause (32/32.0)
    show expression "img/BG15EA@2x.jpg" as bg_over zorder 2 with dissolve
    "我立刻就开始在桌子上准备起来。时间已经所剩无几，得赶紧准备才行。"
    window hide
#FADE_OUT 1
    pause (32/32.0)
    stop se
    pause (32/32.0)
    play sound "SE00_04"
    pause (32/32.0)
#FADE_IN 1
    志雄 "「嗯？」"
    "刚从厨房里把小型燃气炉和大锅拿到桌子上，就听到有人按门铃的声音。"
    志雄 "「大概是学姐她们回来了吧？」"
    "去商店街来回的话，是不是有些太快了……"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-192)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .15
    with move
    voice "NCL09A_TO035"
    亨 "「谁来了啊？」"
    志雄 "「我出去看看，你接着准备吧。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_TO036"
    亨 "「ＯＫ。我去把菜切成大块～」"
    window hide
    stop music fadeout 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "说完，亨就跑进了厨房里。"
    play sound "SE00_04"
    志雄 "「呃，在在，这就去开门啦～」"
    show expression "img/OIBG012A@2x.png" as bg_over zorder 2 with dissolve
    "我马上站起身来去门口开门。"
    stop se
    play sound "SE00_00"
    志雄 "「让您久等——啊」"
    "在门外站着的，并不是我预想里的学姐。"
    window hide
#SE_WATC 1
    play sound "SE03_90"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-96)
#CHR_POSC 1,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD01"),"True","img/RI_MBD01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAC01"),"True","img/SU_MAC01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    play music "BGM10"
    莉莉丝 "「好久不见……{w=4}{nw}"
#MESA A_CH_RI,NCL09A_RI000A,"【りりす】「好久不见……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD02"),"True","img/RI_MBD02A@2x.png") as lh0 zorder (10+0):
        xcenter .35
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAC02"),"True","img/SU_MAC02A@2x.png") as lh1 zorder (10+1):
        xcenter .65
    voice "NCL09A_RI000B"
    extend "啊，干吗露出一幅很遗憾的表情啊！」"
    voice "NCL09A_SU000"
    铃 "「对难得来一次的青梅竹马露出这样的表情，很失礼哦～」"
    志雄 "「啊，抱歉啦。话说，就你们俩人吗？」"
    "我记得亨也有约箱崎过来，还以为会一起过来呢……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC05"),"True","img/RI_MBC05A@2x.png") as lh0 zorder (10+0):
        xcenter .35
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAC01"),"True","img/SU_MAC01A@2x.png") as lh1 zorder (10+1):
        xcenter .65
    voice "NCL09A_RI001A"
    莉莉丝 "「智纱她吗？{w=3}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC04"),"True","img/RI_MBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCL09A_RI001B"
    extend "今天广播台那边临时有事情来不了了，今天就ＰＡＳＳ了」"
    志雄 "「这样啊」"
    "春日她作为学生会成员要准备奏云祭的事情，箱崎她也有在努力着吧。稍微有点儿罪恶感……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD01"),"True","img/RI_MBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCL09A_RI002"
    莉莉丝 "「给，还有这个。」"
    "莉莉丝打开手里拿着的购物袋。里面有单放猪肉的塑料袋，以及白菜和金针菇。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAB01"),"True","img/SU_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_SU001"
    铃 "「然后，这些是我的。总之，先把锅之类要用的东西从房间里拿过来吧。」"
    "铃的购物袋里露出了半截萝卜。稍微往里面看看的话，还能看到装着豆腐，鸡肉之类的小袋子。"
    "还好没有像亨那样……不过能在这种处境下还提议火锅派对的也只有他吧。。"
    scene expression "img/BG15EA@2x.jpg" as bg_over zorder 2 with dissolve
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2,(320-192)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .15
    with dissolve
    voice "NCL09A_TO037"
    亨 "「喂～志雄。菜已经切好了哦～」"
    "搞定手中事情的亨，出现在了客厅。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA04"),"True","img/RI_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_RI003"
    莉莉丝 "「啊，已经来了吗？」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
        xcenter .15
    with dissolve
    voice "NCL09A_TO038"
    亨 "「哦！好久不见啊，莉莉丝！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD01"),"True","img/RI_MBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,640
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAB01"),"True","img/SU_MAB01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .85
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR0 
#MOV_CHR1 128,(320+192)
#MOV_CHR2 ,(320-192)
#MOV_CHR_GO 1
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .15
    with dissolve
    voice "NCL09A_TO039"
    亨 "「啊，铃小姐也是！」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAB02"),"True","img/SU_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .85
    with dissolve
    voice "NCL09A_SU002"
    铃 "「嗯。难得楼上组织有趣的活动，哪有不参加的道理。」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA05"),"True","img/TO_MBA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .15
    with dissolve
    voice "NCL09A_TO040"
    亨 "「那真是诚惶诚恐，荣幸之至啊！」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAC04"),"True","img/SU_MAC04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .85
    with dissolve
    "自从亨知道了铃是稻穗信的姐姐以后，亨对她的态度就有些尊……哦不，应该说是相当滑稽。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD02"),"True","img/RI_MBD02A@2x.png") as lh0 zorder (10+0):
        xcenter .5
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAB04"),"True","img/SU_MAB04A@2x.png") as lh1 zorder (10+1):
        xcenter .85
    voice "NCL09A_RI004"
    莉莉丝 "「Ｓｔｏｐ。不要拿着菜刀到处乱晃！」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA06"),"True","img/TO_MBA06A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .15
    with dissolve
    voice "NCL09A_TO041"
    亨 "「哎呀，抱歉抱歉～」"
    window hide
    hide lh2 with dissolve
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD01"),"True","img/RI_MBD01A@2x.png") as lh0 zorder (10+0):
        xcenter .5
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAC03"),"True","img/SU_MAC03A@2x.png") as lh1 zorder (10+1):
        xcenter .85
    voice "NCL09A_SU003"
    铃 "「真是好危险呢……」"
    "做了简单的道歉之后，亨径直回到了厨房，然后抱着装着切好的菜的大碗走了出来。"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2,(320-192)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAC01"),"True","img/SU_MAC01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh2 zorder (10+2):
        xcenter .25
    志雄 "「那么，洗一下锅吧，用海带汁过一遍可以吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC05"),"True","img/RI_MBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_RI005"
    莉莉丝 "「我倒是没关系……别人呢？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAC06"),"True","img/SU_MAC06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_SU004"
    铃 "「我想四个人吃的话确实是有点儿多了」"
    "看到桌子上放着的蔬菜的量，莉莉丝和铃皱了皱眉头。"
    志雄 "「那没关系。马上克罗艾学姐她们就要回来了。」"
    voice "NCL09A_RI006"
    莉莉丝 "「她们？还有谁呢？」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB05"),"True","img/TO_MBB05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL09A_TO042"
    亨 "「已经有家室了吗，你这家伙……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA01"),"True","img/RI_MBA01A@2x.png") as lh0 zorder (10+0):
        xcenter .5
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAB02"),"True","img/SU_MAB02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NCL09A_SU005"
    铃 "「嘿～都成家了呢……真行啊，志雄～」"
    "三人津津有味的戏弄着我。不过也并没有什么值得隐瞒的，我决定直接说出事实。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAB01"),"True","img/SU_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    志雄 "「学姐的妹妹也一起过来哦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA03"),"True","img/RI_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_RI007"
    莉莉丝 "「诶？克罗艾学姐，有妹妹？」"
    "听了我的话，莉莉丝惊讶地叫了出来。"
    志雄 "「算是吧……」"
    play sound "SE00_04"
    "这时，门铃响了起来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA01"),"True","img/RI_MBA01A@2x.png") as lh0 zorder (10+0):
        xcenter .5
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh2 zorder (10+2):
        xcenter .25
    志雄 "「失陪一下。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我把准备工作拜托给她们二人，就去门口开门了。"
    show expression "img/OIBG012A@2x.png" as bg_over zorder 2 with dissolve
    志雄 "「来了——」"
    window hide
    play sound "SE00_00"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-96)
#CHR_POSC 1,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA02"),"True","img/NO_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .35
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC01"),"True","img/CL_MAC01A@2x.png") as lh1 zorder (10+1):
        xcenter .65
    voice "NCL09A_KU058"
    克罗艾 "「我回来了，志雄。」"
    voice "NCL09A_NO023"
    诺艾儿 "「我回来了——」"
    "打开门，克罗艾学姐和诺艾儿两人开开心心地回来了。"
    志雄 "「欢迎回家。马上就能准备好了哦。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC04"),"True","img/CL_MAC04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_KU059"
    克罗艾 "「是吗？对不起。应该再快一些回来的……」"
    志雄 "「请别在意了啦。好，赶紧进去吧」"
    voice "NCL09A_NO024"
    诺艾儿 "「进去吧！」"
    window hide
    play sound "SE01_13"
    hide lh0 with dissolve
    "诺艾儿把鞋甩在一边就跑了进去。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB05"),"True","img/CL_MAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_KU060"
    克罗艾 "「喂，诺艾儿！」"
    stop se
    "学姐想叫住诺艾儿，可是诺艾儿却装作完全没有听见的样子，啪嗒啪嗒地径直跑进了客厅。"
    "学姐有些疲倦地叹了口气，把散落着的鞋子摆放好。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB04"),"True","img/CL_MAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_KU061A"
    克罗艾 "「真是的哦……{w=4}{nw}"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB03"),"True","img/CL_MAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_KU061B"
    extend "诶？他们已经来了吗？」"
    志雄 "「嗯。莉莉丝和亨，还有铃三个人。箱崎她今天临时有事来不了了。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB05"),"True","img/CL_MAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_KU062"
    克罗艾 "「这样吗？那，看起来食材有点儿买多了呢……」"
    志雄 "「没关系的，大家坐在一起的话会比平常吃得多一些，多了也能解决掉的。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_KU063"
    克罗艾 "「也对。那么，虽然有点儿迟，不过我还是去帮忙准备吧。」"
    志雄 "「嗯，拜托了！」"
    voice "NCL09A_NO025"
    诺艾儿 "「大姐姐们，你们是谁？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB03"),"True","img/CL_MAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    "正当克罗艾学姐挽起袖子准备走进厨房的时候，客厅传来了诺艾儿的声音。"
    voice "NCL09A_TO043"
    亨 "「诶、诶诶！？难道是志雄和学姐的，孩、孩、孩子？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB04"),"True","img/CL_MAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_RI008"
    莉莉丝 "「笨蛋！刚才不是说了是妹妹吗！！」"
    play sound "SE04_08"
#THREAD_STA 1,THREAD_QUA_WIN
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NCL09A_TO044B"
    亨 "「好疼！？十分感谢！」"
    voice "NCL09A_RI009"
    莉莉丝 "「很好！」"
    "……亨，被调教了。"
    "我和学姐两人则站在原地面面相觑。"
    志雄 "「还是先向大家介绍一下诺艾儿比较好呢。」"
    voice "NCL09A_KU064"
    克罗艾 "「看起来是呢。」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/BG15EA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
#FADE_IN 1
    "我们向莉莉丝和亨还有铃简单介绍了一下诺艾儿。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 0
#CHR_POSC 1,(320+192)
#CHR_POSC 2,(320-192)
#CHR_DSPTC 0,1,2,NO_MAA01,SU_MAC01,TO_MBA01
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAA01"),"True","img/NO_MAA01A@2x.png") as lh0 zorder (20+0):
        ypos 0.2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAC01"),"True","img/SU_MAC01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .35
    voice "NCL09A_TO045"
    亨 "「原来如此～从法国来的呢。而且，日语说的真不错呢！」"
    voice "NCL09A_SU006"
    铃 "「确实呢。就像从小就在日本长大一样。」"
    window hide
    hide lh2 with dissolve
#CHR_POSC 2,(320-192)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA01"),"True","img/RI_MBA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCL09A_RI010"
    莉莉丝 "「诺艾儿，匆忙从国外回到这里，有没有觉得不安啊？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB02"),"True","img/NO_MAB02A@2x.png") as lh0 zorder (20+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO026"
    诺艾儿 "「没有，因为有妈妈陪着的。还有呢，现在和姐姐还有大哥哥在一起所以没关系的～」"
    window hide
    hide lh1 with dissolve
#CHR_POSC 1,(320+192)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB04"),"True","img/CL_MAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_KU065"
    克罗艾 "「诺艾儿……」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC02"),"True","img/RI_MBC02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCL09A_RI011A"
    莉莉丝 "「诺艾儿真是听话的好孩子呢。{nw=6}{nw}"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAA07"),"True","img/NO_MAA07A@2x.png") as lh0 zorder (20+0):
        xcenter .5
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC01"),"True","img/RI_MBC01A@2x.png") as lh2 zorder (10+2):
        xcenter .35
    voice "NCL09A_RI011B"
    extend "真希望那个某人能向人家学习一下」"
    志雄 "「为什么要看着我说这些啊……」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD06"),"True","img/RI_MBD06A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCL09A_RI012"
    莉莉丝 "「啊～啊～倒是更想要个直率可爱的弟弟呢～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAA09"),"True","img/NO_MAA09A@2x.png") as lh0 zorder (20+0):
        ypos .2
    with dissolve
    "边说着，莉莉丝那家伙边叹了口气。"
    志雄 "「你啊……」"
    "我不禁也叹了口气。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAA04"),"True","img/NO_MAA04A@2x.png") as lh0 zorder (20+0):
        ypos .2
    with dissolve
    "看着我和莉莉丝这样你一言我一语，诺艾儿很担心地揪住了学姐的衣襟。"
    voice "NCL09A_NO027"
    诺艾儿 "「呐，姐姐。他们两个人关系不好吗？」"
    志雄 "「不是不是，没有这回事哦。」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC03"),"True","img/RI_MBC03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .35
    with dissolve
#REEK_CHR 2
    voice "NCL09A_RI013"
    莉莉丝 "「对、对啊。这些只是开玩笑而已的！」"
#REMOVE_REEK_CHR 2
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAA09"),"True","img/NO_MAA09A@2x.png") as lh0 zorder (20+0):
        ypos .2
    with dissolve
    "看着慌乱的我还有莉莉丝，诺艾儿很不解的歪着脑袋。"
    voice "NCL09A_NO028"
    诺艾儿 "「是这样的吗？」"
    window hide
#CHR_ERSWC 1
#CHR_POSC 1,(320+192)
#CHR_POSC 2,(320-192)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAC01"),"True","img/SU_MAC01A@2x.png") as lh1 zorder (10+1):
        xcenter .35
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh2 zorder (10+2):
        xcenter .65
    voice "NCL09A_SU007"
    铃 "「有句俗话叫『打是亲，骂是爱』哦。」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_TO046"
    亨 "「从他们两个身上很容易就看出来了呢～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB09"),"True","img/NO_MAB09A@2x.png") as lh0 zorder (20+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO029"
    诺艾儿 "「诶～？」"
    window hide
    hide lh2 with dissolve
#CHR_POSC 2,(320-192)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC02"),"True","img/RI_MBC02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_RI014"
    莉莉丝 "「我们哪有又打又骂的。我只是把想到的事情说出来了而已啊。」"
    志雄 "「再说，我和莉莉丝根本就不能吵架嘛。」"
    voice "NCL09A_RI015"
    莉莉丝 "「是、是啊。」"
    志雄 "「要是违背她的意思的话，她直接就会踢——」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD04"),"True","img/RI_MBD04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .65
    with dissolve
    "说的有些得意忘形了，我慌忙捂住嘴。"
    "不过，这看起来太迟了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB02"),"True","img/NO_MAB02A@2x.png") as lh0 zorder (20+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO030"
    诺艾儿 "「是吗？人家想看看啦～」"
    "喂喂，诺艾儿别火上浇油啊……"
#BG_SET_BACK 
#BG_INIC 1
#BG_INIC 3
#BG_POSC 1,0,-(448),640,448
#BG_POSC 3,0,448,640,448
#BG_SETWC 1,3,BG_BLACK,BG_BLACK
#MUS_VOL 64
#THREAD_STA 1,THREAD_RIRISU_CUTIN
    play sound "SE07_18"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD02"),"True","img/RI_MBD02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .65
    with dissolve
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NCL09A_RI016"
    莉莉丝 "「……等等，志雄。」"
#MESA A_CH_RI,NCL09A_RI016,"【りりす】「……等等，志雄。」"
#THREAD_WAT 1
#MESX "%K%P"
    window hide
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB08"),"True","img/NO_MAB08A@2x.png") as lh0 zorder (20-0):
        ypos .2
    with dissolve
#MUS_VOL 128
#BG_COL_AUTOC 0,128,128,128,F24,48
#BG_POS_AUTOC 1,,-(448),,F24,48
#BG_POS_AUTOC 3,,448,,F24,48
#CHR_COL_AUTOC 0,128,128,128,F24,48
#CHR_COL_AUTOC 1,128,128,128,F24,48
#BG_COL_SAVEC 0
#BG_POS_SAVEC 1
#BG_POS_SAVEC 3
#CHR_COL_SAVEC 0
#CHR_COL_SAVEC 1
#BG_ERSWC 1,3,BG_NOFADE
#BG_POSC 1,0,0,640,448
#BG_POSC 3,0,0,640,448
    "我的背上直冒冷汗。"
    "莉莉丝的表情，怎么看怎么恐怖。"
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
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD02"),"True","img/RI_MBD02A@2x.png") as lh0 zorder (20+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_RI017"
    莉莉丝 "「既然诺艾儿希望的话，志雄。你就给我老实呆着别动！」"
    志雄 "「诶，开玩笑的吧？」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD06"),"True","img/RI_LBD06A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    "莉莉丝开始走向我这边，我下意识变得恭恭敬敬的。"
    voice "NCL09A_RI018"
    莉莉丝 "「放心吧。就如你所愿，一击就了断了你！」"
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
#CHR_INIC 2
#CHR_POSC 0
#CHR_POSC 1,(320+192)
#CHR_POSC 2,(320-192)
#CHR_DSPTC 0,1,2,NO_MAB02,SU_MAB05,TO_MBB02
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB02"),"True","img/NO_MAB02A@2x.png") as lh0 zorder (20+0):
        ypos 0.2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAB05"),"True","img/SU_MAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .35
    "在她身后，三个人用很开心的表情，为莉莉丝助威。"
    voice "NCL09A_SU008"
    铃 "「你放心地去吧～」"
    voice "NCL09A_TO047"
    亨 "「我会帮你收尸的哦～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAA02"),"True","img/NO_MAA02A@2x.png") as lh0 zorder (20+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO031"
    诺艾儿 "「要上了呢～」"
    "那个……比起这些，你们谁快来阻止她啊！"
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
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD02"),"True","img/RI_LBD02A@2x.png") as lh1 zorder 100:
        ypos 0.0
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB02"),"True","img/CL_LAB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter .25
#MOV_CHR_INIT 48
#MOV_CHR0 128,(320-160)
#MOV_CHR1 ,(320+160)
#MOV_CHR_GO 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA03"),"True","img/RI_LBA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with move
    voice "NCL09A_KU066"
    克罗艾 "「好好，到此为止。这样闹下去的话什么时候才能结束哦？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    "实在看不下去的学姐，插到了我和莉莉丝中间。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA05"),"True","img/RI_LBA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_RI019"
    莉莉丝 "「没办法呢。看在学姐的面子上饶了你……不过，没有下次哦！」"
    "莉莉丝好像消了气。"
    志雄 "「是……」"
    "好不容易捡回一条命的我，终于放下心来。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA01"),"True","img/CL_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL09A_KU067"
    克罗艾 "「好，那就赶紧开始准备吧。远峰来这边帮忙～」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA01"),"True","img/RI_LBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_RI020"
    莉莉丝 "「好——」"
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
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAA01"),"True","img/SU_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_SU009"
    铃 "「那我也来帮着做点什么吧。」"
    window hide
    stop music fadeout 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "三个人一起进了厨房。"
    "诶？材料不是已经全部准备好了吗？"
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAA09"),"True","img/NO_LAA09A@2x.png") as lh0 zorder 100:
        ypos .2
    with dissolve
    play music "BGM08"
    voice "NCL09A_NO032"
    诺艾儿 "「呐，大哥哥……」"
    "诺艾儿在身边拽了拽我的衣服下摆。"
    志雄 "「怎么了呢，诺艾儿？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAB09"),"True","img/NO_LAB09A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO033"
    诺艾儿 "「我也做点什么可以吗？」"
    志雄 "「没事的。马上就准备完了，诺艾儿坐着等就好了。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAB03"),"True","img/NO_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO034"
    诺艾儿 "「诶～人家想帮忙嘛！」"
    "这样的话可真是为难啊。"
    "要说有什么事情要做的话，就只剩下帮忙拿餐具了，我一个人就能搞定的。"
    "其他，诺艾儿可以帮忙的事情……"
    "突然，在桌子上咕嘟咕嘟煮着的火锅映入我的眼帘。"
    志雄 "「……对啊！诺艾儿就帮忙看着火锅好吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAB09"),"True","img/NO_LAB09A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO035"
    诺艾儿 "「火锅？」"
    志雄 "「嗯。如果水开了，顶得锅盖咣当咣当响的话就赶紧告诉大家。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAB02"),"True","img/NO_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO036"
    诺艾儿 "「嗯，我知道了！」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    window hide
    hide bg1 with dissolve
#BG_SWPC 0
#BG_PRI 1
#BG_PRI 0
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 2
##BG_POSC 0,(60),0,640,448
    #scene expression "img/EXBG10EA@2x.png" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB06"),"True","img/NO_ZAB06A@2x.png") as lh0 zorder (10-0):
        ypos .2
    with dissolve
    hide bg1 with dissolve
#EFF_STAC 0,YUGE5,EFF_SKIP
    "诺艾儿兴奋地回答之后，马上就跑回火锅前坐好，一动不动地盯着火锅。"
    "其实在那里什么都不做也没关系的。我不禁露出了笑容。"
    "不过，诺艾儿那天真无邪的样子，真不忍心就那么丢下她不管。"
#EFF_STPC 0,EFF_SKIP
    show expression "img/BG15EA@2x.jpg" as bg_over zorder 2 with dissolve
    志雄 "「接下来我也去帮着做点什么吧。」"
    window hide
    play sound "SE03_10L"
    show expression "img/BG33AA@2x.jpg" as bg0 with dissolve
    scene expression "img/BG33AA@2x.jpg" as bg0 with dissolve
    "看了看，亨不知道什么时候跑去厨房开始帮那三个人的忙了。"
    "我自己也不能偷懒啊。于是我从橱柜里拿出了与人数一样多的碗筷，在桌子上面摆放好。"
    window hide
    stop se fadeout 1
#FADE_OUT 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    show expression "img/BG15EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG15EA@2x.jpg" as bg0 with dissolve
    stop se
    pause (32/32.0)
    play sound "SE03_24L"
    pause (32/32.0)
#FADE_IN 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB04"),"True","img/NO_MAB04A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO037"
    诺艾儿 "「大哥哥，火锅已经咕嘟咕嘟啦！」"
    志雄 "「真的？等我一下。」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_INIC 3
##BG_POSC 1,(144),0,640,448
    #show expression "img/EXBG10EA@2x.png" as bg1 with dissolve
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_SWPC 0
#BG_SWPC 2
#BG_ERSWC 1,3,BG_NOFADE
#BG_PRI 1
#BG_PRI 3
#BG_PRI 0
#BG_PRI 2
#EFF_STAC 0,YUGE6,EFF_SKIP
    "在诺艾儿的呼喊声中，我看了一眼锅里。煮开了的汤汁马上就要溢出来了。"
#SE_VOLC 1,128
    "我急忙把火调小，把锅盖拿开。"
#EFF_STAC 0,YUGE7,EFF_SKIP
    志雄 "「真烫啊……」"
    "湿热的水蒸气迎面扑来，我不禁喊了出来。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB08"),"True","img/NO_ZAB08A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO038"
    诺艾儿 "「没、没事吧？」"
    志雄 "「啊，没事的。只是热蒸汽碰到脸上了而已……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我对着一脸担心的诺艾儿笑了笑，然后开始向锅中放入适当大小的蔬菜。"
    "首先要放入蔬菜一类的需要多煮一会儿的东西。豆腐什么的要放进去还稍微早了些。"
    "接着，我再一次把锅盖扣上，适当地调节了一下火的大小。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB09"),"True","img/NO_ZAB09A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO039"
    诺艾儿 "「还要多久才能好啊？」"
    志雄 "「嗯，大概１５分钟左右吧。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA03"),"True","img/NO_ZAA03A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO040"
    诺艾儿 "「嗯～」"
    "诺艾儿一副等不及了的样子，兴奋地再次目不转睛地盯着火锅。"
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
#FADE_IN 1
    "十几分钟后，咕咚咕咚煮好了的声音从锅里传了出来，我打开锅盖确认了一下。"
    "诺艾儿也和我一起，向锅里窥视着。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,640
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_XAB04"),"True","img/NO_XAB04A@2x.png") as lh0 zorder (10-0):
        ypos .2
    with dissolve
    window hide
#BG_ERSWC 1,3,BG_NOFADE
#BG_SWPC 0
#BG_SWPC 2
#BG_PRI 1
#BG_PRI 3
#BG_PRI 0
#BG_PRI 2
#BG_GET_NOC 1,F34
#BG_GET_NOC 3,F35
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 2
#BG_UVC 0,0,512,640,448
#BG_UVC 2,0,512,640,448
##BG_POSC 0,(144),0,640,448
##BG_POSC 2,(144),0,640,448
#BG_SETWC 0,2,F34,F35
#BG_ALP_AUTOC 1,0,0,F24,48
#BG_ALP_AUTOC 3,0,0,F24,48
#CHR_ALP_AUTOC 0,128,0,F24,48
#CHR_POS_AUTOC 0,(320+200),0,1,F24,48
#BG_ALP_SAVEC 1
#BG_ALP_SAVEC 3
#CHR_ALP_SAVEC 0
#CHR_POS_SAVEC 0
#BG_ERSWC 1,3,BG_NOFADE
#BG_ALPC 1,128
#BG_ALPC 3,128
    voice "NCL09A_NO041"
    诺艾儿 "「已经做好了吗？」"
    志雄 "「还差点儿火候呢。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_XAB03"),"True","img/NO_XAB03A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    "说完，我往还没煮好的锅里放入了生肉还有豆腐之类的东西。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_XAA09"),"True","img/NO_XAA09A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    "还可以往里面放点东西吧……"
    "好久没用过这个锅了，对量的把握有些不太准确了。"
    志雄 "「稍等一下，我去再拿点东西加进来。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_XAB01"),"True","img/NO_XAB01A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    "貌似对我的话产生了兴趣，诺艾儿一脸好奇，眼中闪着光芒问道。"
    voice "NCL09A_NO042"
    诺艾儿 "「呐，大哥哥。决定好往锅里放什么了吗？」"
    志雄 "「嗯～？还没有呢。嘛，虽然还会放一些锅里有的东西进去，不过今天还是多放些大家喜欢的东西吧～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_XAB09"),"True","img/NO_XAB09A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO043"
    诺艾儿 "「喜欢的东西？」"
    志雄 "「嗯。比如，豆腐啊，蔬菜啊什么的」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_XAA04"),"True","img/NO_XAA04A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO044"
    诺艾儿 "「嗯～」"
    "我说了几个菜码之后，诺艾儿露出一幅困惑的表情。"
    志雄 "「诺艾儿，比起菜来更喜欢吃肉吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_XAA02"),"True","img/NO_XAA02A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO045"
    诺艾儿 "「嗯～」"
#EFF_STPC 0,EFF_SKIP
    stop music fadeout 1
    scene expression "img/BG15EA@2x.jpg" as bg_over zorder 2 with dissolve
    "就在这时，亨拿着大盘子从厨房里走了出来。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320-192)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL09A_TO048"
    亨 "「喂～你那边怎样？」"
    志雄 "「大概东西放得有点儿少了。你拿的是什么啊？」"
    "听了我的话，亨把盘子拿到我的面前，上面盛的是意大利面，菜肉蛋卷，以及土豆沙拉。"
    window hide
    play music "BGM10"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL09A_TO049"
    亨 "「这个吗？学姐还有莉莉丝和铃说光吃火锅有点儿太单调了，所以就赶紧做了点儿这些」"
    志雄 "「诶？这么快？」"
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
#CHR_INIC 2
#CHR_POSC 0,(320-160)
#CHR_POSC 2,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC02"),"True","img/RI_MBC02A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC01"),"True","img/CL_MAC01A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    voice "NCL09A_RI021"
    莉莉丝 "「那当然，我出手的话，自然手到擒来哦」"
    voice "NCL09A_KU068"
    克罗艾 "「真的呢，多亏了远峰的帮忙哦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC01"),"True","img/RI_MBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL09A_RI022"
    莉莉丝 "「哪里哪里，好好品尝吧～」"
    志雄 "「莉莉丝……你也会做西式餐点啊……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD04"),"True","img/RI_MBD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL09A_RI023"
    莉莉丝 "「你这是什么意思啊？」"
    志雄 "「没有，很单纯的夸奖而已！」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB06"),"True","img/CL_MAB06A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    "到去年为止，莉莉丝还只会做和式的饭菜，不知不觉间都成长到这种地步了吗……"
    window hide
    hide lh0 with dissolve
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAA09"),"True","img/NO_MAA09A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL09A_NO046"
    诺艾儿 "「这些，也是要放到锅里的？」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB02"),"True","img/CL_MAB02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_KU069"
    克罗艾 "「不是哦。这些料理是做给那些光吃火锅不满足的人的。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB09"),"True","img/NO_MAB09A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL09A_NO047"
    诺艾儿 "「有这么多啊？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,640
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAC01"),"True","img/SU_MAC01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 64
#MOV_CHR0 ,(320-160)
#MOV_CHR1 128,(320+160)
#MOV_CHR2 ,(320-96)
#MOV_CHR_GO 1
    voice "NCL09A_SU010"
    铃 "「你太天真了，诺艾儿。这些量，五个人吃的话立刻就能消灭光的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB08"),"True","img/NO_MAB08A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    voice "NCL09A_NO048"
    诺艾儿 "「是吗！？」"
    志雄 "「啊，说起来，学姐。食材还有剩吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAA01"),"True","img/NO_MAA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB03"),"True","img/CL_MAB03A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    voice "NCL09A_KU070"
    克罗艾 "「嗯，倒是还有一些……怎么啦？」"
    志雄 "「没有，我想锅里还没放满，煮的话不妨再放些东西进去」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB04"),"True","img/CL_MAB04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_KU071"
    克罗艾 "「对不起，做其他料理的时候用了很多，基本没剩下什么了」"
    志雄 "「这样啊……」"
    window hide
    hide lh1 with dissolve
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA01"),"True","img/RI_MBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL09A_RI024"
    莉莉丝 "「学姐不用道歉的啦。再说，除了火锅也有别的料理嘛～」"
    window hide
#CHR_ERSWC 0
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2,(320-160)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA05"),"True","img/TO_MBA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_TO050"
    亨 "「意思是现在火锅里的食物还不是很足吗？」"
    志雄 "「嗯，可能吧。」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_TO051"
    亨 "「难得吃一次火锅，这样的话乐趣就会减半的……」"
    "说到这里，亨突然沉默了，仿佛在思考什么似的。不过，很快他就从容地抬起了头，脸上浮现出了恶作剧一般的笑容。"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_TO052"
    亨 "「我有一个提议。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA05"),"True","img/RI_MBA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL09A_RI025"
    莉莉丝 "「喂，你不会是在想一些很无聊的事情吧」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB05"),"True","img/TO_MBB05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_TO053"
    亨 "「你好过分，莉莉丝。我只是单纯的想给大家的火锅派对增添一份乐趣而已」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA06"),"True","img/RI_MBA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL09A_RI026"
    莉莉丝 "「好好，那你说说看？」"
    "对蓄势待发般的亨，莉莉丝不耐烦地催促起来。"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_TO054"
    亨 "「没什么，很简单的啦。总之不是因为食材不足在烦恼吗？」"
    志雄 "「难道你想说现在跑去买？」"
    window hide
#CHR_SORT 1,2
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAA04"),"True","img/SU_MAA04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter 0.25
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR0 128
#MOV_CHR1 ,(320+192)
#MOV_CHR2 ,(320-192)
#MOV_CHR_GO 1
    voice "NCL09A_SU011"
    铃 "「在火锅煮好之前跑去买回来，实在是太辛苦了吧。无论是肉体上还是精神上。」"
    voice "NCL09A_RI027"
    莉莉丝 "「我ＰＡＳＳ。要去的话你一个人去好了～」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_TO055"
    亨 "「不不。在这么热的天里跑出去，就算是超人般的我也不可能的」"
    志雄 "「那，该怎么办？」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA05"),"True","img/TO_MBA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_TO056"
    亨 "「我想，现在还是发扬一下火锅这种料理的最大特点好了。也就是说，大家把自己喜欢食材全部放进去煮——但是不可以看！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAA02"),"True","img/SU_MAA02A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA05"),"True","img/RI_MBA05A@2x.png") as lh1 zorder (10+1):
        xcenter .5
    志雄 "「喂，那不就是黑暗火锅了么？」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_TO057"
    亨 "「就是这样！不过，只能放进去自己会吃的东西。也就是不能往里面放不能吃的东西」"
    voice "NCL09A_RI028"
    莉莉丝 "「听上去确实有点意思，来试试看吧？」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_TO058"
    亨 "「来吧来吧！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAB01"),"True","img/SU_MAB01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA06"),"True","img/RI_MBA06A@2x.png") as lh1 zorder (10+1):
        xcenter .5
    voice "NCL09A_SU012"
    铃 "「这样也没什么不行的吧？」"
    "莉莉丝和铃有些无所谓的感觉，同意了亨的提案。"
    window hide
    hide lh0 with dissolve
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA02"),"True","img/CL_MAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL09A_KU072"
    克罗艾 "「真的要来吗？我倒是觉得不那么做也会十分开心的……」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_TO059"
    亨 "「啊哈，学姐。这肯定会是一段难忘的回忆的，没关系的啦～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB03"),"True","img/CL_MAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL09A_KU073"
    克罗艾 "「嗯？」"
    voice "NCL09A_TO060"
    亨 "「刚才看了一下，冰箱里好像没有什么不能放到锅里的吃的～」"
    "虽然学姐对此十分不安。不过最后还是勉强同意了亨的提议。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA02"),"True","img/CL_MAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL09A_KU074"
    克罗艾 "「真没办法呢……」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_TO061"
    亨 "「不愧是学姐，一说就明白了！」"
    "我看大家都同意了就没再说什么。不过，看这情形，应该不会演变成什么很糟糕的状况吧。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SORT 0,1,2
    志雄 "「真没办法呢……」"
    "掺杂着叹息声，我打开了锅盖。"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG33AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG33AA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
#SE_VOLC 1,128
#FADE_IN 1
    "然后，我们一个个去厨房，把自己想放进去的食材用小碗装好，捂着碗口放进了锅里。"
    show expression "img/BG15EA@2x.jpg" as bg_over zorder 2 with dissolve
#RSET F55,72
    window hide
    voice "NCL09A_RI029"
    莉莉丝 "「真的没关系吗……？」"
    志雄 "「不要乌鸦嘴……」"
    voice "NCL09A_TO062"
    亨 "「那么，差不多开始煮了哦～？」"
    志雄 "「放了相当多的东西啊」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_ZBA01"),"True","img/TO_ZBA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCL09A_TO063"
    亨 "「嗯～？可是你看，按做暗锅的规矩来说，这可没错啊。」"
    voice "NCL09A_SU013"
    铃 "「我弟弟来的话，就不知道会变成什么结果了哦～」"
    志雄 "「嘛，确实……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    show expression "img/EXBG10EA@2x.png" as bg0 zorder 0 with dissolve
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB02"),"True","img/NO_ZAB02A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAA01"),"True","img/CL_ZAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0

#BG_ERSWC 1,3
    voice "NCL09A_NO049"
    诺艾儿 "「呐，姐姐。还没好吗？」"
    克罗艾 "「再稍微等一会儿呢。嗯，已经差不多好——{w=7}{nw}"
#MESA A_CH_KU,NCL09A_KU075A,"【クロエ】「再稍微等一会儿呢。嗯，已经差不多好——"
    stop music fadeout 1
#SE_VOLC 1,255
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC05"),"True","img/CL_ZAC05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#REEK_CHR 1
    voice "NCL09A_KU075B"
    extend "了？」"
#REMOVE_REEK_CHR 1
    "听了诺艾儿的催促，打开锅盖确认火候的学姐，拿着锅盖僵在了原地。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA09"),"True","img/NO_ZAA09A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    志雄 "「学姐？发生了什么了？」"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NCL09A_KU076"
    克罗艾 "「那个……」"
    "克罗艾学姐，用微妙的笑容转过来看着我。学姐的嘴角颤抖着什么也没有说。我急忙把目光投向锅里。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play music "OBGM13"
    志雄 "「什么啊，这是……」"
    "锅里，稍微有点儿浑浊。而先放的白菜、苘蒿、豆腐等等东西已经好了……"
    "此外，裙带菜以及牛蒡也有，貌似放进了很多奇怪的东西。"
    "这个，只有那种奇怪口味的家里才做得出来吧。"
    "不过，问题是……"
    voice "NCL09A_RI030"
    莉莉丝 "「什么啊，这个？为什么锅里……有这黑黑的东西！？」"
    "莉莉丝最先尖叫了起来。"
    voice "NCL09A_SU014"
    铃 "「这是……什么锅啊？」"
    voice "NCL09A_TO064"
    亨 "「好甜！这甜甜的气味是什么啊！？」"
    "连坐的离锅最远的亨，在打开锅盖之后都惊讶地不禁站了起来。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD02"),"True","img/RI_ZBD02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL09A_RI031"
    莉莉丝 "「佐贺君。你，不会……」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_ZBB05"),"True","img/TO_ZBB05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_TO065"
    亨 "「等等等等，不是我了啦！我放进去的是年糕啊！」"
    voice "NCL09A_RI032"
    莉莉丝 "「那，这究竟是谁放进去啊！」"
    window hide
    stop music fadeout 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NCL09A_NO050"
    诺艾儿 "「那个，不可以的吗？」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA04"),"True","img/NO_ZAA04A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB03"),"True","img/CL_ZAB03A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
    play music "OBGM08"
    "听到莉莉丝的叫喊声，诺艾儿小声地嘟囔道。"
    voice "NCL09A_RI033"
    莉莉丝 "「诶？」"
    "莉莉丝突然停止了动作。"
    志雄 "「那个，难道说是诺艾儿放进去的吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB03"),"True","img/NO_ZAB03A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL09A_NO051"
    诺艾儿 "「可是，不是把自己喜欢的东西放进去吗。所以我就把巧克力……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NCL09A_SU015"
    铃 "「……这个黑黑的东西原来是巧克力」"
    "听了诺艾儿的话，我不禁摸了摸脑袋。"
    志雄 "「抱歉，我应该更认真地说明一下的……」"
    voice "NCL09A_TO066"
    亨 "「你看，不是我的问题吧……」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA05"),"True","img/RI_ZBA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL09A_RI034"
    莉莉丝 "「要不是你说要吃暗锅，怎么会变成现在这个样子呢！」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_ZBA03"),"True","img/TO_ZBA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_TO067"
    亨 "「对不起……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    show expression "img/EXBG10EA@2x.png" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA03"),"True","img/NO_ZAA03A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAA02"),"True","img/CL_ZAA02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0

#BG_ERSWC 1,3
    voice "NCL09A_NO052"
    诺艾儿 "「不能往火锅里放吗？」"
    voice "NCL09A_KU077"
    克罗艾 "「嗯，这个有点儿太……」"
    "看着露出担心神情的诺艾儿，学姐的面容也变得为难起来。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAA05"),"True","img/NO_ZAA05A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL09A_NO053"
    诺艾儿 "「是我的错吗？」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NCL09A_TO068"
    亨 "「没有没有，想不到还能有这样的组合呢……」"
    "看着快要哭出来的诺艾儿，多少有些罪恶感的亨赶紧慌忙拿起了碟子。在一旁的莉莉丝和铃也跟着拿起了碟子。"
    voice "NCL09A_SU016"
    铃 "「是啊是啊！得好好感受着新料理诞生的瞬间」"
    voice "NCL09A_RI035"
    莉莉丝 "「吃起来的话一定会意外的美味的，肯定！」"
    "说着，莉莉丝从锅里盛了一些放到我的碗里。我俩视线相交，莉莉丝的眼神里透露着一种要死一起死的感觉。"
    志雄 "「是，是啊！好不容易做出来的，我也吃点儿吧！」"
    "我全力地挤出笑容，把盛在碗里的茶色白菜放入了口中。"
    志雄 "「呃……！？」"
    "不出所料！虽然有心理准备，可是这也实在太……！"
    "斜眼看了看其他三个人，他们也和我一样在把东西放入口中的一刹那僵住了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB03"),"True","img/NO_ZAB03A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAA02"),"True","img/CL_ZAA02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
    voice "NCL09A_NO054"
    诺艾儿 "「大哥哥……？」"
    "眼里噙满泪水的诺艾儿，仰着头直直地看着我。"
    "我急忙把嘴里的东西咽了下去。"
    志雄 "「没，没事啊。吃下去了呢……」"
    "看着我的面容，诺艾儿一瞬间表情变得明快起来，不过马上就又恢复了要哭出来的样子。"
    voice "NCL09A_NO055"
    诺艾儿 "「不用勉强自己也行的……」"
    "她的眼睛里，泪珠悄然落下。"
    voice "NCL09A_KU078"
    克罗艾 "「喂，诺艾儿。别哭了？好吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB05"),"True","img/NO_ZAB05A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL09A_NO056"
    诺艾儿 "「可是，可是！」"
    "面对哭了起来的诺艾儿，我尽可能自然地对她报以微笑。"
    志雄 "「诺艾儿，我有个请求哦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB04"),"True","img/NO_ZAB04A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL09A_NO057"
    诺艾儿 "「诶？」"
    志雄 "「这个火锅很美味，所以我把诺艾儿那份也吃掉，可以吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB03"),"True","img/NO_ZAB03A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    voice "NCL09A_NO058"
    诺艾儿 "「大哥哥？」"
    voice "NCL09A_KU079"
    克罗艾 "「志雄？可别胡来……」"
    志雄 "「不是胡来，我是很认真的在说哦。」"
    "说完，我转过头看了看其他三个人。"
    "「……」"
    "在诺艾儿面前，三个人都没有做出任何表情，就仿佛在说『这个根本就是在勉强』。"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB05"),"True","img/NO_ZAB05A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAA02"),"True","img/CL_ZAA02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
    voice "NCL09A_NO059"
    诺艾儿 "「那个，不用勉强……」"
    "在诺艾儿说完之前，我拿起碗直接从锅里盛了好多出来。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_ZAB04"),"True","img/NO_ZAB04A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .25
    with dissolve
    诺艾儿 "「！？」"
    志雄 "「我开动了！！」"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
    scene expression "img/NIMG03C@2x.jpg" as bg0 with dissolve
    play sound "SE03_07"
    pause (32/32.0)
    play music "OBGM17"
    "之后，我一个人把整个锅里的东西都吃了，撑得自己动弹不得。"
    "诺艾儿边吃着饭边担心地看着我……"
    "在其他人努力使全场气氛热烈起来的情况下，诺艾儿终于停止了哭泣，露出了笑容。"
    志雄 "「太好了……」"
    "学姐和家庭之间的种种，我现在依然无法完全了解，不过……"
    "不单单是诺艾儿，能和学姐以及大家这么融洽地在一起，我真的很开心。"
    "大家欢乐的盛宴即将结束……"
    "学姐送诺艾儿回家，其他三个人帮忙收拾完之后，也都一一离开了。"
    "不过话说回来，嗓子里好甜啊……"
    志雄 "「这样的大骚动也很久没有遇上过了……」"
    "望着高悬于天空的明月，我开始自言自语起来。"
    志雄 "「那三个人，很忙啊。」"
    "莉莉丝也好，亨也好，都已经决定了自己将来的道路，在别人不知道的时候，默默为各种各样的事情努力着。"
    "铃最近好像也开始在杂志上连载作品了，因此也忙的热火朝天。"
    "……而我呢？"
    "胸中有无限的焦躁在翻涌着。自己想做的事情，能做的事情。我依然还没有头绪。"
    "我越想越急躁。"
    志雄 "「所以说，心急吃不了热豆腐吗？」"
    "就在我无奈的叹息之际，突然从上面出现一个人影。"
    window hide
#BG_SET_BACK 
#CHR_INIC 0
#CHR_POSC 0,320,(-60)
#CHR_SETC 0,NIMG22A
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"NIMG22A"),"True","img/NIMG22AA@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU080"
    克罗艾 "「怎么了啊？」"
    志雄 "「学姐！什么时候回来的！？」"
    "我急忙想起身。学姐则默默制止了我。"
    voice "NCL09A_KU081"
    克罗艾 "「好啦，不要勉强了。还不舒服吧？」"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "勉强爬起来":
            $F7=0
        "告诉学姐自己已经没事了":
            $F7=1
        "老实地听学姐的话":
            $F7=2
    if F7==0:
        jump L_NCL09A_SEL00_A
    if F7==1:
        jump L_NCL09A_SEL00_B
    if F7==2:
        jump L_NCL09A_SEL00_C
label L_NCL09A_SEL00_A:
    window hide
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/BG15NA1@2x.jpg" as bg1 with dissolve
    hide lh0 with dissolve
#BG_SWPC 0
    hide bg1 with dissolve
#BG_PRI 1
#BG_PRI 0
    "我还是撑着爬了起来，伸了一个大大的懒腰……还是稍微有些不舒服，不过要想办法动一动。"
    window hide
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC04"),"True","img/CL_LAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09X_KU000"
    克罗艾 "「再稍微睡一会儿吧？」"
    "学姐用担心的声音问道，我则摇着头，对学姐笑了笑。"
    志雄 "「已经没事了。那还要再收拾一下吗？」"
    "厨房里还有一些没洗完的餐具，小型燃气炉也还放在那里。今天真是发生了好多事，真想早点收拾完睡觉。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC01"),"True","img/CL_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09X_KU001"
    克罗艾 "「那倒也是呢……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我们两人认真地划分了各自分担的任务，然后开始了派对的最后整理工作。和学姐在一起，会心地相互微笑着，焦躁的情绪终于褪去了。"
    jump L_NCL09A_SEL00_X
label L_NCL09A_SEL00_B:
    志雄 "「那个，我没关系啦。」"
    "动起来还是有点儿难受，不过还是不要让学姐担心的好。听到我说了这些，学姐露出有些遗憾的表情。"
    voice "NCL09X_KU002"
    克罗艾 "「这种时候，撒娇一下也可以哦？」"
    志雄 "「怎么这样。总是撒娇的话，这种时候会遭报应的」"
    "稍微开玩笑般地说了这样的话，学姐微微沉思了起来。"
    voice "NCL09X_KU003"
    克罗艾 "「……今天志雄为了诺艾儿都那么努力了，接下来收拾的事情交给我来吧。」"
    志雄 "「诶？」"
    "说起来，燃气灶之类还放在厨房里呢。学姐笑着制止了慌忙想站起来的我。"
    voice "NCL09X_KU004B"
    克罗艾 "「志雄就睡觉吧。」"
    志雄 "「可是……」"
    voice "NCL09X_KU005"
    克罗艾 "「这种时候，就默默地依赖一下我吧，好吗？」"
    志雄 "「好……」"
    voice "NCL09X_KU006"
    克罗艾 "「很好～」"
    window hide
    hide lh0 with dissolve
    play sound "SE03_21L"
    "学姐说完了就走进了厨房。不一会儿就传来洗涮的声音。"
    play sound "SE03_53"
    "边听着那些声音，我觉得头越来越沉。伴随着那富有韵律的收拾声，睡意向我袭来。"
    stop se
    stop sound
    "不自觉地，我也忘掉了刚才的焦躁感，进入了梦乡。"
    jump L_NCL09A_SEL00_X
label L_NCL09A_SEL00_C:
    志雄 "「对不起，让你担心了……」"
    voice "NCL09A_KU082"
    克罗艾 "「要道歉的是我啦，对不起呢，诺艾儿她……」"
    志雄 "「不，火锅的事情是我的责任。」"
    voice "NCL09A_KU083"
    克罗艾 "「不要这么说哦。」"
    window hide
    hide lh0 with dissolve
    "说着，学姐坐在床边招手叫我过去。"
    voice "NCL09A_KU084"
    克罗艾 "「来吧，给你膝枕。」"
    志雄 "「诶？」"
    voice "NCL09A_KU085"
    克罗艾 "「好啦，快过来啊。」"
    "学姐红着脸，催促着我。"
    "虽然说得我也感觉很害羞。不过，还是决定享受一下这甜美的时刻。"
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL06A")]=True
    show expression "img/EVN_CL06A@2x.jpg" as bg_over zorder 2 with dissolve
    voice "NCL09A_KU086"
    克罗艾 "「好久都没这样了呢……」"
    志雄 "「学姐指什么？」"
    voice "NCL09A_KU087"
    克罗艾 "「给志雄膝枕啊。要说起来的话，最近我也没有向志雄撒娇……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL06B")]=True
    show expression "img/EVN_CL06B@2x.jpg" as bg0 with dissolve
    "说完，学姐有些寂寞地闭上了眼睛。"
    志雄 "「学姐？」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL06A")]=True
    show expression "img/EVN_CL06A@2x.jpg" as bg0 with dissolve
    voice "NCL09A_KU088"
    克罗艾 "「没什么啦。一时之间，感觉向志雄撒娇也有了种新鲜感。」"
    志雄 "「那个。我倒是好像每天都在向学姐撒娇呢。」"
    voice "NCL09A_KU089"
    克罗艾 "「没有这回事哦。今天，你连那样勉强自己的事情都做了……」"
    "学姐温柔地微笑着，轻轻抚摸着我的头。"
    志雄 "「那种事情没什么的啦，放心吧。」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL06C")]=True
    show expression "img/EVN_CL06C@2x.jpg" as bg0 with dissolve
    voice "NCL09A_KU090"
    克罗艾 "「哈哈，偶尔依赖一下也好呢。」"
    "就这样，我借着克罗艾学姐的膝枕，稍微休息了一会儿。"
    "体会着学姐的温度，我感到心中的那份焦躁感终于如初春的积雪一样消融不见了。"
    jump L_NCL09A_SEL00_X
label L_NCL09A_SEL00_X:
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop se
    stop sound
    stop music fadeout 1
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_RIRISU_CUTIN
#BG_COL_AUTOC 0,64,64,64,F123,48
#BG_POS_AUTOC 1,,-392,,F123,48
#BG_POS_AUTOC 392,,F123,48
#CHR_COL_AUTOC 0,64,64,64,F123,48
#CHR_COL_AUTOC 1,64,64,64,F123,48
#BG_COL_SAVEC 0
#BG_POS_SAVEC 1
#BG_POS_SAVEC 3
#CHR_COL_SAVEC 0
#CHR_COL_SAVEC 1
#EOT
#label THREAD_TORU_NEAR
#CHR_POS_AUTOC 2,(320-96),F123,48
#CHR_POS_SAVEC 2
#EOT
#label THREAD_QUA_WIN
#TH_QUAKE_WIN 4
#EOT
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT