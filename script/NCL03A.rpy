label NCL03A:
    $currentlabel = "NCL03A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '22'
    $date = '6'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG15NA3@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG15NA3@2x.jpg" as bg0 with dissolve
    play sound "SE05_16L"
    pause (32/32.0)
#FADE_IN 1,128
#SE_VOLC 1,(64/2)
    play music "OBGM20"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "一整天，我都抱着头烦恼着。"
    志雄 "「呃，该做些什么才好呢？」"
    "我一边看着日历，一边不停地挠着头。"
    window hide
#MUS_VOL 64
#FADE_OUT 1
#BG_ALPC 0
#FADE_IN 0
#CAL_DSP_GRP 2,CAL_0722
    show expression "img/NIMG15H-568h@2x.jpg" as cal zorder 5
    show expression "img/07_22_SATURDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
#FADE_OUT 0
#BG_ALPC 0,128
#MUS_VOL 128
#FADE_IN 1
    "７月２２日——今天是芦鹿岛的焰火大会举办的日子。"
    "今晚并不是很热。即使不开空调，从窗口吹进的风也令人感觉十分凉爽。"
    "本来的话，这个时候应该和克罗艾学姐两个人穿着浴衣，走在这凉爽之夜的道路上，到海边去的……"
    志雄 "「学姐，今天得打工呢。」"
    "回想起两天前看到的克罗艾学姐那十分抱歉的表情，脑中不禁一阵翻腾起伏。那时还露出不满情绪的自己，真是太小家子气了。"
    志雄 "「明明说了不用在意也没关系了。」"
    "虽然嘴上是这么说……实际上还是很期待和克罗艾学姐一起开心地去看焰火大会……"
    志雄 "「真是够矛盾的啊……」"
    "就这个样子恍惚间看了一眼客厅，桌子上放着的纸映入我的眼帘。"
    志雄 "「……」"
    "『志愿调查表』，仍然保持着白纸的状态，躺在那里。"
    "自己究竟是怎么想的？"
    "想继续读大学？　还是想以别的东西为目标？"
    play sound "SE03_51"
    "敞开的窗户外，传来了远方放焰火的声音。"
    "循声望去，在远处山脊棱线上的夜空中，能依稀看到正在散开的大型焰火华丽优雅的顶端部分。"
    志雄 "「已经开始了吗？」"
    "难得的焰火大会，只能一个人在房间里学习真是郁闷。积累的懈怠，也终于在不知道第几声叹气中爆发了。"
    stop music fadeout 1
    志雄 "「不行！在这个地方闷闷不乐可不行！」"
    "难得的焰火大会，代学姐的那一份期待，去开心地一饱眼福，之后再说给学姐听吧。"
    "决定了之后，我迅速地收拾准备好，离开了家。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG01NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG01NA@2x.jpg" as bg0 with dissolve
    play sound "SE08_17L"
    pause (32/32.0)
#FADE_IN 1
    "大街上，所有对烟火目所能及的道路都被多到难以置信的人群淹没了。"
    志雄 "「哇，果然好多的人啊。」"
    "不仅仅是本地人，也有很多专程从外地赶来的人。不用说大路的步行道，连小胡同里都有非常多的人紧挨着，缓慢行进。"
    "『如果在去的途中能遇上熟人就好了。』即便我是如此想的，但我也清醒地意识到，这种想法只是美好的幻想罢了。"
    志雄 "「这样的话就算笔直地向海前进，到焰火结束的时候也未必能看上了。」"
    "说起来，自己连看焰火的绝佳地点之类的都不知道呢。"
    "而且，一个人寂寞地去看焰火，也一点都开心不起来吧。"
    志雄 "「不过，要是抓亨一起来的话……」"
    "虽然拿出了手机，但是最终我也没有呼出那个号码。"
    志雄 "「唉，这个时候果然……」"
    "我认真思考了一下之后，开始向着与人流不同的方向走去。"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG97NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG97NA@2x.jpg" as bg0 with dissolve
    play sound "SE00_32"
    pause (32/32.0)
#SE_VOLC 1,(64/2)
#FADE_IN 1
    voice "NCL03A_KU000"
    クロエ？ "「欢迎光临～」"
    "走进店里的同时，一个非常熟悉的声音，用平常听不到的明亮的音调迎接了我。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEB06"),"True","img/CL_MEB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU001"
    克罗艾 "「请问您一共几……位……诶！？」"
    if not persistent.dictlist[35] and persistent.show_dict:
        $persistent.dictlist[35]=True
        show screen dict_pop(i=35)
    "刚刚还满脸笑容，身穿酪萨克制服的克罗艾学姐，再看到我后愣在了原地。"
    志雄 "「一位哦。」"
    window hide
    play music "BGM04"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEB03"),"True","img/CL_MEB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU002"
    克罗艾 "「志雄！？　怎么回事？」"
    志雄 "「当然是来喝茶的啦。」"
    "学姐非常的吃惊，仿佛忘记了自己的工作。当然，说完场面话之后，我也追加了自己的真心话。"
    志雄 "「还有……我想见学姐啦～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEB04"),"True","img/CL_MEB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU003"
    克罗艾 "「这、这样啊……」"
    "下了决心试着把话说出来了，但克罗艾学姐的反应并不大，只是忽然变得很羞涩。"
    "是怕刚才的对话被谁听到吗？我环视了一下店内，好在谁也没有注意这里。"
    "说起来，这个时候客人还真是少的可怜。一定是这个时间段，大多数的人还聚集在海岸边看焰火的缘故。"
    志雄 "「嗯，那么座位在？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEB03"),"True","img/CL_MEB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU004"
    克罗艾 "「啊，对呢。那个，吧台可以吧？」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    #show expression Solid("000") as bg1 with ImageDissolve("img/BG_LINEAR_SLIDE@2x.png",1)
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    scene expression "img/BG36AA@2x.jpg" as bg0 with dissolve
    hide bg1 with dissolve
    "在回到正常腔调的学姐引领下，我在店里的吧台坐了下来。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEA03"),"True","img/CL_MEA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    "到了席位上，克罗艾学姐就发出了不满的声音。"
    voice "NCL03A_KU005"
    克罗艾 "「突然就来了，吓了我一跳呢……」"
    志雄 "「对不起……」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEA02"),"True","img/CL_MEA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU006"
    克罗艾 "「不用道歉的啦，说真的，没出什么事吧？」"
    "大概还是以为我有什么事情所以才来这里的吧。"
    志雄 "「没有，想见学姐是真心的哦。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEB03"),"True","img/CL_MEB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU007"
    克罗艾 "「诶？」"
    "我再一次说出了来这里的本意，克罗艾学姐的表情呆住了。"
    志雄 "「当然，也是想来看看学姐工作的地方。」"
    "学姐在这家酪萨克打工的事情，我以前就知道的。"
    "不过，在学姐打工的时间段来店里，还是头一次。"
    志雄 "「之前总是有这样那样的事情，时间上合不到一起，今天机会很难得，所以想来看看学姐工作的环境呢。」"
    voice "NCL03A_KU008"
    克罗艾 "「可是，焰火呢？　就算志雄一个人，也想要开开心心的吧？」"
    志雄 "「那个嘛，虽然是那样。」"
    "稍微有些为难，但最终我还是决定把自己的真实想法说出来。"
    志雄 "「和克罗艾学姐一起去才会开心，一个人去完全开心不起来的。」"
    "对我直抒胸臆的话语，学姐哑然了一小会儿后，捂着嘴笑了起来。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEB06"),"True","img/CL_MEB06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU009"
    克罗艾 "「哈哈……」"
    志雄 "「有那么可笑吗？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEB01"),"True","img/CL_MEB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU010"
    克罗艾 "「没有，不可笑。」"
    志雄 "「不，你笑了吧？」"
    voice "NCL03A_KU011"
    克罗艾 "「才没有笑呢～」"
    "明明是很认真的表白，克罗艾学姐却兴奋地像个孩子是的。"
    "这样被学姐戏弄的情况是常有的事情，所以不知不觉声音也大了起来。"
    志雄 "「绝对笑了！」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEB02"),"True","img/CL_MEB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU012"
    克罗艾 "「怎么会呢，嘲笑顾客那种事情。」"
    stop music fadeout 1
    voice "NCL03A_MA000"
    麻尋？ "「啊，不好意思～」"
    "一个陌生的声音从一旁插了进来。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,640
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA02"),"True","img/MH_LCA02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter .75
#MOV_CHR_INIT 48
#MOV_CHR0 128
#MOV_CHR1 ,(320-160)
#MOV_CHR_GO 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEB03"),"True","img/CL_MEB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with move
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA05"),"True","img/MH_LCA05A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    pause (16/32.0)
#    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA02"),"True","img/MH_LCA02A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    play music "OBGM14"
    "我看向声音的主人，她正挂着营业式的笑容走到我和学姐之间。"
    voice "NCL03A_MA001"
    麻尋２ "「这位客人，实在是不好意思。请问有什么问题吗？」"
    志雄 "「呃？　不，那个……」"
    "我无从面对这突发的状况，翻了一下白眼。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA03"),"True","img/MH_LCA03A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL03A_MA002"
    麻尋２ "「如果我们哪里有失误的话，实在是不好意思。不过，您这样会给其他的顾客带来困扰的哦。」"
    "我们的谈话被迫中止了，比我早回复平常状态的克罗艾学姐和穿同样制服的女生打起招呼。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEA02"),"True","img/CL_MEA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL03A_KU013"
    克罗艾 "「那个、仙堂小姐。不是那样的——」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LBC02"),"True","img/MH_LBC02A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL03A_MA003"
    麻尋３ "「没关系的哦，嘉神川。这种问题就交给我吧。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEB05"),"True","img/CL_MEB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    "打断了想解释什么的克罗艾学姐，被称为仙堂的女生再次向我转过身来。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA03"),"True","img/MH_LCA03A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL03A_MA004"
    麻尋３ "「实在不好意思，这位客人。那么您想点些什么呢？」"
    "看起来，她把我当成是向克罗艾学姐恶意搭讪的客人了。"
    "不过，从旁观者的角度来看，说不定确实是那个样子。"
    voice "NCL03A_MA005"
    麻尋３ "「还没有决定要点些什么吗？　如果是这样的话，您决定好点什么了再叫我吧」"
    "仙堂小姐脸上的笑容没有间断，看起来是沉着冷静地面对我的样子。"
    "不过，很快，事实证明，她也就是看起来是那样吧……"
    志雄 "「那个……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA01"),"True","img/MH_LCA01A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL03A_MA006"
    麻尋３ "「决定好了吗？」"
    志雄 "「在那之前，请先让我看一下菜单吧。」"
    stop music fadeout 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA04"),"True","img/MH_LCA04A@2x.png") as lh0 zorder (10+2):
        xcenter .75
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEB03"),"True","img/CL_MEB03A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    voice "NCL03A_MA007"
    麻尋３ "「啊！」"
    window hide
    hide lh0 with dissolve
    pause (64/32.0)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA01"),"True","img/MH_LCA01A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    "我指出这点之后，仙堂小姐慌忙地去拿来了菜单。"
    志雄 "「……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA02"),"True","img/MH_LCA02A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL03A_MA008"
    麻尋３ "「啊哈哈哈……」"
    "这个人，意想不到的马虎吗？"
    window hide
    show expression Solid("000") as bg_over zorder 100 with fade
#FADE_OUT 1
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEA02"),"True","img/CL_MEA02A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBB01"),"True","img/MH_MBB01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0

    stop music fadeout 1
    pause (32/32.0)
    hide bg_over with fade
#FADE_IN 1
    play music "BGM07"
    voice "NCL03A_MA009"
    麻寻 "「呃，对不起！！」"
    志雄 "「那个，不用这样道歉的。」"
    if not persistent.dictlist[17] and persistent.show_dict:
        $persistent.dictlist[17]=True
        show screen dict_pop(i=17)
    "那之后，克罗艾学姐和拿来菜单的仙堂小姐终于搭上了话，也成功地解除了误会。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBB04"),"True","img/MH_MBB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL03A_MA010"
    麻寻 "「这位难道就是嘉神川的男朋友吗……」"
    "听了学姐的解释，仙堂小姐稍有失礼地垂着头嘟囔了一下。"
    voice "NCL03A_KU014"
    克罗艾 "「倒是我们，真的像出现了纠纷一样呢。」"
    "克罗艾学姐也对她感到十分抱歉。"
    "为了打破这一尴尬的气氛，我稍微试着改变话题。"
    if not persistent.dictlist[8] and persistent.show_dict:
        $persistent.dictlist[8]=True
        show screen dict_pop(i=8)
    志雄 "「说起来，稻穗前辈他不在吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEA01"),"True","img/CL_MEA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL03A_KU015"
    克罗艾 "「嗯，他这个夏天有什么地方要去，不来这里了呢。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MCC05"),"True","img/MH_MCC05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL03A_MA011"
    麻寻 "「拜他所赐这边的工作真是多的要命……真是的，那个家伙真————的给我适可而止吧！！」"
    "仙堂小姐突然变得暴走了起来。"
    志雄 "「难道对稻穗他有什么怨恨的事情吗？」"
    window hide
#BG_GET_NOC 0,F34
#BG_SET_BACK 
#BG_INIC 3
#BG_ALPC 3
#BG_UVC 3,(640/2),(448/4),(640/2),(448/2)
    #show expression "img/F34@2x.jpg" as bg3 zorder 3 with dissolve
#BG_PRI 3
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2
    hide lh1
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_XBC02"),"True","img/MH_XBC02A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
        xcenter .75
    with dissolve
#CHR_PRIC 2
#MUS_VOL 0
#BG_ALP_AUTOC 3,128,1,F24,8
#CHR_ALP_AUTOC 2,128,1,F24,8
#BG_ALP_SAVEC 3
#CHR_ALP_SAVEC 2
    voice "NCL03A_MA012"
    麻寻 "「数不清了！」"
    "哇，斩钉截铁地，而且没有犹豫立刻就回答了！"
    window hide
    hide lh2
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MCC03"),"True","img/MH_MCC03A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .75
    with dissolve
#MUS_VOL 128
#BG_ALP_AUTOC 3,0,1,F24,48
#CHR_ALP_AUTOC 2,0,1,F24,48
#BG_ALP_SAVEC 3
#CHR_ALP_SAVEC 2
    hide bg3 with dissolve
#BG_ALPC 3,128
    hide lh2 with dissolve
#CHR_PRIC 2
#CHR_ALPC 2,128
    voice "NCL03A_MA013"
    麻寻 "「不过啊，从他那里也得到了和这些差不多程度的帮助。也想还借的钱，看在这些的份上，擅离职守之类的事情就原谅他吧。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEB06"),"True","img/CL_MEB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL03A_KU016"
    克罗艾 "「哈哈。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA02"),"True","img/MH_MBA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL03A_MA014"
    麻寻 "「啊，那么我差不多该继续去工作了。　这位客人，请和嘉神川小姐慢慢享受吧～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEB03"),"True","img/CL_MEB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL03A_KU017"
    克罗艾 "「啊……」"
    window hide
    stop music fadeout 1
    hide lh1 with dissolve
    "给我们留下了一个媚眼，仙堂小姐就去招呼别的客人了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEB04"),"True","img/CL_MEB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL03A_KU018"
    克罗艾 "「呃，该怎么办呢？」"
    "克罗艾学姐向我投来很为难的视线。如果真按麻寻说的那样的话就和偷懒或怠工之类的一样了，不过从经验上来说，学姐是不会那样做的。"
    志雄 "「话说回来，还是先点些东西，可以吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MEB01"),"True","img/CL_MEB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL03A_KU019"
    克罗艾 "「啊，嗯。」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL03A")]=True
    show expression "img/EVN_CL03A@2x.jpg" as bg1
##BG_ANM_ONC 1,0,CHRID_CL
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play music "BGM04"
    voice "NCL03A_KU020"
    克罗艾 "「啊，不对……您决定好要点什么了吗？」"
    "面对这种态度的克罗艾学姐的，我也不禁纠正了一下坐姿。"
    voice "NCL03A_KU021"
    克罗艾 "「这位客人？」"
    "平时见惯了的酪萨克制服，穿在学姐身上，却显得格外有魅力。"
    "看来，学姐和制服已经不是一般程度上的合适了。"
    "怎么说也太可爱了啊……"
    voice "NCL03A_KU022"
    克罗艾 "「这位客人？　这、这个样子看着我的话会很困扰的……」"
    志雄 "「啊、那个……一杯咖啡。」"
    voice "NCL03A_KU023"
    克罗艾 "「知道了，请您稍等片刻。」"
    window hide
#BG_ANM_OFFC 1
    hide bg1 with dissolve
    志雄 "「好的。」"
    "依旧带着些紧张，遥望着学姐的背影。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG35NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG35NA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    play music "OBGM17"
    "两个小时以后……喝完咖啡的我在酪萨克的外面，等着克罗艾学姐出来。"
    play sound "SE03_50"
    "远方依稀还能听到焰火绽开的声音，不过，即使这样，拥挤的人群也没有散开的意思。"
    志雄 "「结果，今年完整的错过了这场焰火大会呢。」"
    "不过作为补偿，能看到克罗艾学姐工作时的身影，也就不那么遗憾了。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_SAA06"),"True","img/MH_SAA06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_MA015"
    麻寻 "「诶？　嘉神川的男朋友，难道是在这里等她吗？」"
    志雄 "「嗯，算是吧。」"
    "意料之外的问候，原来是刚才误会了我和克罗艾学姐的仙堂小姐。"
    hide lh0 with dissolve
#CHR_POSC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA03"),"True","img/MH_MAA03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_MA016"
    麻寻 "「真好呢啊，男朋友来接～」"
    志雄 "「呃，那个……」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA02"),"True","img/MH_MAA02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_MA017"
    麻寻 "「不要害羞，不要害羞～」"
    志雄 "「仙堂小姐也刚好打工结束吗？」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA01"),"True","img/MH_MAA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_MA018"
    麻寻 "「嗯，和嘉神川她一起。我想她马上就出来了吧？」"
    志雄 "「非常感谢。」"
    voice "NCL03A_MA019"
    麻寻 "「不不、不用谢的。那么，在妨碍到你们之前先告辞咯。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "边说着，仙堂小姐取来了停在店里停车场的橘黄色自行车。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA01"),"True","img/MH_MAA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    志雄 "「夜路很危险呢，请多加小心啊。」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA02"),"True","img/MH_MAA02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_MA020"
    麻寻 "「不要紧的。如果骑着它的话马上就能到的。那么，辛苦了哦～」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "感觉是骑惯了自行车的样子，仙堂小姐英姿飒爽的蹬车离去。"
    志雄 "「用那种速度骑，真的没关系么……」"
    "远远看着的话，总觉得很危险，真是个不让人放心的人啊。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_SAB03"),"True","img/CL_SAB03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU024"
    克罗艾 "「志雄？」"
    "就像仙堂小姐说的一样，没过一会儿学姐就出来了。不过显然，在这里看见我，学姐还是非常意外的。"
    志雄 "「辛苦了哦。」"
    hide lh0 with dissolve
#CHR_POSC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB04"),"True","img/CL_MAB04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU025"
    克罗艾 "「一直等着我吗？　抱歉了。」"
    志雄 "「没有啦，是我想要等学姐的」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU026"
    克罗艾 "「谢谢……」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG03NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG03NA@2x.jpg" as bg0 with dissolve
    play sound "SE05_16L"
    pause (32/32.0)
#FADE_IN 1
    play sound "SE03_50"
    "伴随着夏夜的习习微风，我们向着车站走去。远处仍有焰火声此起彼伏地响起。"
    window hide
#SE_VOLC 1,(64/2)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC03"),"True","img/CL_MAC03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU027"
    克罗艾 "「焰火……没有去看成呢。」"
    "克罗艾学姐小声嘟囔的声音，在我耳中澄澈地回响着。"
    志雄 "「明年还可以的哦。」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC01"),"True","img/CL_MAC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU028B"
    克罗艾 "「可是，浴衣还是可惜了……」"
    志雄 "「确实，好不容易买了，暂且就拿来喂养衣橱好了。」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU029"
    克罗艾 "「都是志雄啦，说今年一定要去才特意买的。」"
    志雄 "「啊哈，你看，俗话不是说『心动不如行动』么？」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB02"),"True","img/CL_MAB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU030"
    克罗艾 "「原来如此——」"
    志雄 "「啊，开玩笑啦，不必放在心上。」"
    "说真的，即使一会儿也好。能和学姐一起穿着浴衣看烟火，我的期待在我脑中膨胀着，仿佛都要溢出来了……"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB05"),"True","img/CL_MAB05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU031"
    克罗艾 "「如果这个夏天里有另外的机会就好了。比如呢……祭典之类的。」"
    志雄 "「能穿浴衣去看的活动……到秋天以前都没有了呢。」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB04"),"True","img/CL_MAB04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU032"
    克罗艾 "「是啊。而且那个时候，天气也凉了呢。」"
    志雄 "「啊，如果能那样的话就没问题了！」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB03"),"True","img/CL_MAB03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU033"
    克罗艾 "「？」"
    "面对我突然大声的一句，克罗艾学姐明显有些不知所措。"
    志雄 "「可以的啊，我们自己来办吧？　『专属焰火大会』。」"
    voice "NCL03A_KU034"
    克罗艾 "「诶？」"
    志雄 "「虽然那种放射的大型焰火不太可能，不过店里能买到的焰火还是可以的。」"
    voice "NCL03A_KU035"
    克罗艾 "「就我们两个人吗？」"
    志雄 "「那样也可以啊，觉得寂寞的话，也可以叫些人一起呢。我想亨那家伙不用打招呼也会跑来的，莉莉丝也是……」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB06"),"True","img/CL_MAB06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU036"
    克罗艾 "「看来会很热闹呢。」"
    志雄 "「啊，不过。」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB03"),"True","img/CL_MAB03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    "说到这里，虽然有些害羞，不过我还是决定试着说出自己的心意。"
    志雄 "「我呢，如果可以的话还是想和学姐两个人一起……」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU037"
    克罗艾 "「嗯，我也是呢～」"
    志雄 "「那么，约定好了哦！」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB03"),"True","img/CL_MAB03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU038"
    克罗艾 "「嗯？」"
    志雄 "「这个夏天，来一次两个人的『专属焰火大会』吧。」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh10 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCL03A_KU039"
    克罗艾 "「嗯，真的很期待呢。」"
    "看着克罗艾学姐迅速伸出小指，我也毫不犹豫的用自己的小指将它勾住……"
    voice "NCL03A_KU040"
    克罗艾 "「拉钩算数。」"
    志雄 "「一百年不许变！」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB06"),"True","img/CL_LAB06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL03A_KU041"
    克罗艾 "「拉钩了哦～」"
    window hide
#BG_SET_BACK 
#FADE_OUT 1
#BG_INIC 1
#BG_ALPC 1
    scene expression "img/NIMG01D@2x.png" as bg1 zorder 1
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
#SE_VOLC 1,128
    play sound "SE01_12L"
#BG_ALPC 1,128
#FADE_IN 1
    "我和学姐带着真诚的约定，在满满的幸福的期待中，告别了彼此，各自回家了。"
    window hide
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#BG_COLC 1,0,0,0,128
    "…………"
    "……"
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