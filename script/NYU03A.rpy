label NYU03A:
    $currentlabel = "NYU03A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '24'
    $date = '1'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_SUB NIMG15E,CAL_0724
    show expression "img/NIMG15E-568h@2x.jpg" as cal zorder 5
    show expression "img/07_24_MONDAY@2x.png" as cal_date zorder 6:
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
#BG_INIC 1
    scene expression "img/BG52AA@2x.jpg" as bg0 with dissolve
    play sound "SE09_26"
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
    pause (32/32.0)
#SE_VOLC 1,255
    hide bg1 with dissolve
    scene expression "img/BG50AA@2x.jpg" as bg0 with dissolve
    "拿着从自动贩卖机上买来的饮料，回到包间。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU02A")]=True
    show expression "img/EVN_YU02A@2x.jpg" as bg1 with dissolve
    "结乃正在兴致勃勃的大声唱着。"
    "她不用翻开目录就按出想唱的歌曲编码。"
    "熟练地调节着麦克风的角度。"
    "看来她相当熟悉这里了。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,136,136
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB02"),"True","img/YU_LCB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    hide bg1
    with dissolve
    voice "NYU03A_YU000"
    结乃 "「啊，饮料，谢谢啦～」"
    stop sound
    "唱完一曲的结乃对我点头致谢。"
    "暂时中断的歌声所带来的安静给房间渲染上一层奇怪的氛围。"
    play music "OBGM18"
    志雄 "「我说，今天不是为了制作广播才出来的么？」"
    "将饮料递给结乃时，我小心的问道。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB04"),"True","img/YU_LCB04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU03A_YU001"
    结乃 "「唉？是取材哦，取材！精妙的取材。」"
    志雄 "「就算如此，也不用刻意重复这么多次吧……」"
    "面对如此“取材”的结乃，我只好尴尬的笑了笑。"
    "单独相处的房间，自助饮料，的确是个讨论问题的好地方。"
    "但是……"
    志雄 "「隔壁唱的还真是ＨＩＧＨ啊。」"
    "从墙壁另一面传来的动漫歌曲，让我们完全没办法静下心来思考。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA01"),"True","img/YU_LCA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU03A_YU002"
    结乃 "「有喝的东西的话，就可以尽兴的唱到够呢。」"
    志雄 "「等等，所以说，我们不用讨论广播了吗……」"
    "直到在车站接到结乃时还一切顺利。"
    "原本以为会去酪萨克之类的地方，但是经过卡拉ＯＫ门口时，计划就突然被改变了。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA02"),"True","img/YU_LCA02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU03A_YU003"
    结乃 "「没错，说到广播的话，就不得不提音乐，所以不掌握最新音乐潮流可不行呢。」"
    "只要想做总能找到很多理由的道理我还是知道的。"
    "所以面对结乃的主张，这样匪夷所思的取材似乎也变得合情合理起来。"
    志雄 "「就算是这样，你刚才唱的好像也不是什么流行歌曲吧？」"
    "这几年的新歌还算说得过去，不过连那种在我们还没出生时就有的歌也在歌单之列……"
    "不过换个角度去想，结乃对歌曲的认知面还真的是非常广阔。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA05"),"True","img/YU_LCA05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU03A_YU004"
    结乃 "「温故而知新，你应该懂吧……」"
    志雄 "「好吧，在怎么说我也是备考生啊，这怎么会不知道……」"
    "节奏又回到了结乃那里，我也放弃了抵抗下去的打算。"
    "我翻开一旁的目录，开始寻找一些自己音域能够胜任的歌曲。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB01"),"True","img/YU_LCB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU03A_YU005"
    结乃 "「唉？终于要出手了吗？」"
    志雄 "「既然说不过你，那么不好好享受一下岂不是很浪费。」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB02"),"True","img/YU_LCB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU03A_YU006"
    结乃 "「这就对了嘛。」"
    "小恶魔般的笑容，胜利的喜悦溢于言表。"
    "她当然知道，我今晚有补习班的安排。"
    "劳逸结合……结乃也许就是为了让我走出备考的焦虑状态才把我拉来的吧。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA02"),"True","img/YU_LCA02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU03A_YU007"
    结乃 "「最近和学长去过很多地方，但是卡拉ＯＫ已经好久没来了吧？」"
    志雄 "「是吗，没怎么在意呢。」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC01"),"True","img/YU_LCC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU03A_YU008"
    结乃 "「当然是真的……一直有很想来的说。」"
    "不特意提起的话的确没有想到，似乎真的很久没来过这里了。"
    "可能是因为这里并没有什么特别的地方，反而就这样被忽略了。"
    志雄 "「是这样，对不起，明明有说好……」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA06"),"True","img/YU_LCA06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU03A_YU009"
    结乃 "「还记得就好啦。」"
    "结乃很开心地笑了起来。"
    "在去年准备奏云祭的时候，明明答应过她有机会再去卡拉ＯＫ的，但因为种种原因一直没有兑现。"
    "而后，就是不知不觉的过去了一年……"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA01"),"True","img/YU_LCA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU03A_YU010"
    结乃 "「想到要和学长一起去卡拉ＯＫ唱歌……因此悄悄练习了好多歌曲的。」"
    志雄 "「这样啊，真是期待你的表现呢。」"
    "我想起了，在感情刚刚萌芽的时候，偶然在屋顶上遇到了唱ＫＡＮＡＴＡ新歌的她。"
    "那个时候，感觉她只是单纯的喜爱广播，因此更多的都是关注她歌声以外的东西。"
    "一年的时间，酝酿了这么久的结乃，究竟会给我带来怎样惊艳的表演呢？"
    "满满的期待。让你等待了这么久，真是抱歉了。"
    stop music fadeout 1
    play sound "SE09_27"
    志雄 "「哈……」"
    "不知道什么时候，结乃已经点好了新的曲目。"
    "房间里响起了那天傍晚屋顶上的那个旋律。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU02B")]=True
    show expression "img/EVN_YU02B@2x.jpg" as bg_over zorder 2
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NYU03A_YU011"
    结乃 "「如果是这首歌，学长也能一起唱的吧？」"
    志雄 "「当然，因为这首歌，很重要。」"
    "怎么可能会忘记，在Ｔ－ｗａｖｅ里听过很多次。"
    "更何况，这首歌见证了太多太多，我和结乃感情中最纯粹的部分，都溶在了里面。"
    voice "NYU03A_YU012"
    结乃 "「嗯，那就一起来吧！」"
    志雄 "「交给我了！」"
    "我将放在一边的另一个麦克风打开，从座位上站了起来。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU02C")]=True
    show expression "img/EVN_YU02C@2x.jpg" as bg0 with dissolve
    voice "NYU03A_YU013"
    结乃 "「哈哈，这是第一次和学长一起唱呢。」"
    "即使不看歌词也能完整的唱出来。"
    志雄 "（唱的还真是欢乐呢。）"
    "如果只比声音的话，也许莉莉丝会更厉害些。看着面前这个欢快的女孩，我知道，那里有比歌声更吸引我的东西，在熠熠闪光。"
    "我顺着心中的歌词，出神的看着结乃唱歌时的侧脸。"
    window hide
    stop se fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG02EA@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB02"),"True","img/YU_LCB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (32/32.0)
    play sound "SE08_17L"
    play music "BGM06"
#FADE_IN 1
    voice "NYU03A_YU014"
    结乃 "「真是愉快的经历啊。」"
    志雄 "「嗯，下次还来这里吧。」"
    "直到加了两次单才结束。"
    "不快点的话，补习班就要迟到了。"
    志雄 "「谢谢了，是个很不错的心情转换～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB03"),"True","img/YU_LCB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU03A_YU015"
    结乃 "「唉？不过……因为延长太久了，都忘记商量广播的事情了……」"
    志雄 "「和结乃唱的歌说不定可以用在广播里哦。」"
    "在这层意义上，今天所做的事并不算浪费时间。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA01"),"True","img/YU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU03A_YU016"
    结乃 "「是这样的，有很多喜欢的歌曲，无论如何都想用上去，但是感觉还是不够抢眼。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA04"),"True","img/YU_LCA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU03A_YU017"
    结乃 "「如果可以的话，比起用别人的歌，感觉还是原创的音乐会好些的……」"
    "如果是作为录音原声用曲的话，的确是原创的比较好。"
    志雄 "「结乃有作曲的经验么？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC03"),"True","img/YU_LCC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU03A_YU018"
    结乃 "「非常可惜，完全没有……就算有的话，时间上也不允许了吧。」"
    志雄 "「也是呢，在暑假里出现这样的突发状况，实在是不太好应对……」"
    "正当我完全陷入绝望的时候，脑子里忽然闪过一张男人的面庞。"
    志雄 "「等等，说不定我有方法了，今天回去联络一下试试看吧。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB06"),"True","img/YU_LCB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU03A_YU019"
    结乃 "「真的么？那真是太好了！」"
    志雄 "「应该没问题的，不过作曲水平……我认为并不差吧。」"
    "反正要求也不会太高，应该能处理好吧。"
    志雄 "「那么，我去补习班了，晚上给你电话。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA01"),"True","img/YU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU03A_YU020"
    结乃 "「好的，学习时要专心哦。」"
    "在结乃的目光中，我飞奔向补习班。"
    "心情变得格外的晴朗，今天可要打起精神来好好听课。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG15NA1@2x.jpg" as bg0 zorder 0 with dissolve
    pause (64/32.0)
    scene expression "img/BG15NA1@2x.jpg" as bg0 with dissolve
    play music "OBGM17"
#FADE_IN 1
    "刚从补习班回来，我就一下扑到在床上，把手机贴在耳边。"
    window hide
    play sound "SE02_02L"
    "制作音乐需要大量的时间和精力，当然音乐细胞也要不赖。"
    "完全不把备考当回事的，每天都闲的要死给我打骚扰电话，音乐方面还算有点天赋的人，我身边还真有一个……"
    stop sound
    voice "NYU03A_TO000_K"
    亨 "「喂喂，刚想打电话给你的！」"
    志雄 "「你还是一样的闲呢……」"
    "看来打电话的时间稍微早了一点。"
    "只要耐住性子几分钟，电话费就可以省掉了。"
    voice "NYU03A_TO001_K"
    亨 "「这是当然，我又不用在暑假里每天去补习班，实在是太无聊了……」"
    "虽然我认为，他去上补习班，反而会觉得更无聊。"
    "但是这样状态下的亨，似乎才更是我所需要的。"
    志雄 "「所以，我这里有个比学习更有趣的建议」"
    voice "NYU03A_TO002_K"
    亨 "「真的？要出去玩么？哈哈哈，也对，逃课一天也没什么吗。」"
    志雄 "「虽然不是出去玩……但是有点想要拜托你的事情。」"
    voice "NYU03A_TO003_K"
    亨 "「没关系，我没理由拒绝基友的请求吧！」"
    "虽然我也承认我俩的关系的确不坏，但是，搞基什么的挂在嘴边，真是受不了啊……"
    "至于他的回答……我像只要不是叫他陪我去上补习班，提议应该都会被同意吧。"
    志雄 "「谢谢啦，那我和你细说一下。」"
    voice "NYU03A_TO004_K"
    亨 "「很复杂？」"
    志雄 "「不容易吧……」"
    "要把比赛的事情和对他的委托讲清楚。"
    "不花上一点功夫说清楚可是不行的。"
    voice "NYU03A_TO005_K"
    亨 "「我知道了！现在我就去你家，我会和我的爱车一起飞过来的，稍微等一下哦！」"
    志雄 "「现在？都已经这么晚……」"
    window hide
    play sound "SE02_08"
    pause (32/32.0)
    "电话那边传来了忙音，亨已经挂断了。"
    "虽然我一个人住，什么时候来都不会太麻烦，但是这都这个时候了，动静太大邻居们也会受不了吧。"
    志雄 "「也罢，就当满足一下他和他的摩托双宿双飞的愿望好了。」"
    "刚取得摩托车驾照的亨，为了能攒够钱买摩托出去兜风拼命的打工和存零花钱。"
    "最后，还是在父母那里恳求到了足够的资助。"
    "不过作为代价，亨必须在下学期开学的时候去上补习班，同时，被允许骑摩托车的范围也被严格定死了。"
    "好不容易买了摩托车却无法畅快的兜风，只能在附近开着超慢速闲逛。"
    "不过就算如此，他也如同一个刚拿到新玩具的孩子一样兴奋，连去步行几分钟就到的便利店也要骑车。"
    "所以，得到机会，能骑车到我家这种稍微有点距离的地方，他也是求之不得吧。"
    window hide
    play sound "SE06_36"
    志雄 "「好快。」"
    "正在收拾房间的时候，屋外响起了摩托车排气孔的吼叫声。"
    "这级别显然不是铃的摩托。"
    "听觉极度兴奋，光听声音就能辨别骑车的人了。"
    window hide
    play sound "SE06_36"
    pause (64/32.0)
    play sound "SE00_04"
    pause (16/32.0)
#    show expression "img/OIBG012A@2x.jpg" as bg_over zorder 2 with dissolve
    志雄 "「来了！」"
    window hide
    stop music fadeout 1
    play sound "SE00_00"
    show expression "img/BG39NA@2x.jpg" as bg_over zorder 2 with dissolve
#BG_INIC 1
#BG_ALPC 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA01"),"True","img/TO_LBA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    play music "BGM09"
    voice "NYU03A_TO006"
    亨 "「好，就这样直接去酪萨克吧！」"
    "站在门口的亨直接甩给了我一个备用头盔，完全没有进门的意思。"
    "还要特意去酪萨克，看来这家伙还真是被父母委屈的太久了呢。"
    志雄 "「我知道了，不过，ＡＡ制你知道的吧？」"
    "我傻笑着，走出房间。"
    window hide
#BG_SET_BACK
#ROUTINE_STA
#BG_PRIC 0
#CHR_PRIC 0
#BG_INIC 1
#BG_PRIC 1
#EFF_PRI 0
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
#ROUTINE_STP
    play sound "SE06_48L"
#ROUTINE_STA


#ROUTINE_STP
    "结果……"
    "我完全低估了亨的热情，车并没有驶向酪萨克，而是以全速行驶在远离他家的各个方向。"
    voice "NYU03A_TO007"
    亨 "「哇哈～就这样直接去海边吧！」"
    志雄 "「随你喜欢吧……」"
    "在车后面，我将帮忙比赛的事情说明了，亨很爽快的就答应了，任务算是完成了。"
    "那么，作为回报，今天就当作陪亨兜风吧……"
#label QJUMP
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
#ROUTINE_STA
#EFF_STPC 0,EFF_SKIP
#BG_PRIC 0
#CHR_PRIC 0
#BG_PRIC 1
#EFF_PRI 0
    scene expression Solid("000") with fade
#ROUTINE_STP
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG15NA1@2x.jpg" as bg0 zorder 0 with dissolve
    pause (32/32.0)
    scene expression "img/BG15NA1@2x.jpg" as bg0 with dissolve
    play music "OBGM17"
#FADE_IN 1
    志雄 "「麻烦了，竟然忘记带手机。」"
    "等到从亨那里解放出来的时候，日历已经翻到了新的一页。"
    "而手机上的未读信息也已经堆积如山。"
    志雄 "「这样直接打过去没问题吧……」"
    "短信都是神奈发来的。"
    "在这个时间给女孩子打电话总觉得很失礼。"
    志雄 "「呃……不过打手机的话应该没问题吧。」"
    "已经也曾有事打过她家的电话，不过接电话的却是他的父亲，因此引来一阵尴尬。"
    "现在能用手机直接联络，所以还是不要让悲剧再重演的好。"
    "如果一次打不通的话，就明天再打吧……"
    window hide
    play sound "SE02_02L"
    pause (24/32.0)
    stop sound
    voice "NYU03A_KA000_K"
    神奈 "「好慢啊！明明已经到熟睡的时候了！」"
    "连嘟嘟的提示音都没有，手机听筒里就传来了神奈的声音。"
    "似乎一直等着我回拨过去似的……"
    志雄 "「对不起，临时有事出门，手机又忘记带了……」"
    voice "NYU03A_KA001_K"
    神奈 "「真是的，手机是为什么而存在的？对于你来说，这东西完全没有意义了嘛！」"
    志雄 "「你说的对……」"
    "眼前浮现出电话那头生气的面容。"
    voice "NYU03A_KA002_K"
    神奈 "「但因为是暑假，熬夜什么的也是常事，就不怪你了。」"
    "事实并不如我想象的那样，神奈似乎并没有真的生气。"
    voice "NYU03A_KA003_K"
    神奈 "「虽然很晚了，但是就和昨天说的一样，有一些关于广播的想法，听一下吗？」"
    志雄 "「嗯，那真是得救了。」"
    voice "NYU03A_KA004_K"
    神奈 "「做笔记什么的也很麻烦吧，我们网上说。」"
    "知道神奈是去年的优胜者后，就拜托她给出一些提议。"
    "虽然不可能照搬她的成功，但是我想，让有经验的人提供的建议还是很具有价值的。"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_PRI 2
    show expression "img/NIMG14A@2x.jpg" as bg2 zorder 2 with dissolve
#BG_HIDEC 3
    "今天也一样，在聊天软件刚启动的时候，神奈的消息就迅速的弹了出来。"
#CHAT_STA
#BG_SET_BACK 
#BG_INIC 1
#BG_COLC 0,128,128,128
#BG_ALPC 1
    show expression "img/CHAT_3A_00@2x.png" as bg_chat zorder (10-1)
    show expression "img/NIMG14C@2x.jpg" as bg1
    with dissolve
    play sound "SE09_35"


#BG_ALP_SAVEC 0
#BG_ALP_SAVEC 1
#BG_ALPC 0
#BG_ALPC 1
    hide bg2 with dissolve
#CHAT_STR "〈神奈：〉%N首先吧，开头必须带有冲击力，第一印象相当重要。"
#WAIT_KEY 96
    show expression "img/CHAT_3A_01@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N恩恩……"
#WAIT_KEY 96
#CHAT_END
    "神奈的广播制作讲座，一直持续到深夜。"
    window hide
#FADE_OUT 1
    $month = '07'
    $day = '25'
    $date = '2'
    pause (32/32.0)
    show expression "img/CHAT_3A_02@2x.png" as bg_chat
#FADE_IN 1
#CHAT_STA
    show expression "img/CHAT_3A_03@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N唉？竟然有那么多好想法！"
#WAIT_KEY 96
#CHAT_END
    "我终于知道为什么要用聊天软件了。"
    "如果用边打电话边用笔记录的话，这么多内容绝对是个不容小视的浩大的工程。"
#CHAT_STA
    show expression "img/CHAT_3A_04@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N是么？再给我一点时间我还能想到更多哦～"
#WAIT_KEY 96
#CHAT_END
    志雄 "「因为有这么强的精力和想象力，所以才成为了Ｔ－ｗａｖｅ的投稿Ｎｏ、1吗……」"
    "我再一次深刻的认识到神奈——第一代『凯尔玛妹妹』的强大之处。"
    "如果有心去当一名作家，我觉得她完全不会输给任何知名作家。"
#CHAT_STA
    show expression "img/CHAT_3A_05@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N那个，神奈不参加这次的比赛了吗？"
#WAIT_KEY 96
#CHAT_END
    "不想增加参与者……我也了解结乃的心意。"
    "但是都已经向亨提出邀请了，如果不拜托神奈似乎有些说不过去。"
    "要将我和结乃的思念表现出来，神奈的位置是必不可少的。"
#CHAT_STA
    show expression "img/CHAT_3A_06@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N不要啦，我来参加的话，谁来给你们的广播节目投稿呢？"
#WAIT_KEY 96
#CHAT_END
    "我的提议被干脆的拒绝了。"
#CHAT_STA
    show expression "img/CHAT_3A_07@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N打算连比赛作品都投稿么……"
#WAIT_KEY 96
    show expression "img/CHAT_3A_08@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N当然，所谓的广播，不就是要通过主持人将听众散落在各地的心连在一起么？"
#WAIT_KEY 96
    show expression "img/CHAT_3A_09@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N也对哦……"
#WAIT_KEY 96
#CHAT_END
    "对于这点，我深有感触。"
    "我对那种自以为很厉害，只根据自己的心情和趣味来选择读信的主持人非常反感。"
    "和听众之间没有什么距离，这就是我对ＫＡＮＡＴＡ，对Ｔ－ｗａｖｅ如此执着的深层原因。"
#CHAT_STA
    show expression "img/CHAT_3A_0A@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N节目的投稿千篇一律，并且刻意找人做写手的情况可是有很多的哦。"
#WAIT_KEY 96
    show expression "img/CHAT_3A_0B@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N这个也是，必须代表我们铁杆广播听众表示强烈谴责！"
#WAIT_KEY 96
#CHAT_END
    "许多新节目，就常常给人这种厌恶感觉。"
    "如果神奈一同参与制作，再进行投稿，那我们的广播就和这些节目没差了。"
#CHAT_STA
    show expression "img/CHAT_3A_0C@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N哈哈，就是这样。所以如果主题定下来了一定要及时告诉我哦，我会给你们投上最完美的一稿的。"
#WAIT_KEY 96
    show expression "img/CHAT_3A_0D@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N嗯，很期待呢。"
#WAIT_KEY 96
#CHAT_END
    scene expression "img/NIMG14B@2x.jpg" as bg0 with dissolve
    "如果运气好的话，就能借着去年优胜者的光环一路晋级……"
    "想法有点卑鄙，但早就被看穿了也说不定。"
    志雄 "（因为这是专属于我和结乃的广播啊。）"
    "再怎么说，也只能靠我们彼此的努力。"
    "看着屏幕，这样的意思透过屏幕上的字里行间，传递过来。"
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
