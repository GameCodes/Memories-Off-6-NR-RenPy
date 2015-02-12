label NYU15A:
    $currentlabel = "NYU15A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '08'
    $day = '13'
    $date = '0'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_SUB NIMG15H,CAL_0813
    show expression "img/NIMG15H-568h@2x.jpg" as cal zorder 5
    show expression "img/08_13_SUNDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG100AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG100AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_15L"
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
    志雄 "「真慢啊。在这里迟到的话，实在是太没面子了。」"
    "我的视线在车站的时钟和出站口之间不停地游走着。"
    "早就过了我们约定的时间了。"
    "因为曾有过电车晚点的通知，所以我知道这次迟到并不是对方的错，但即便如此，心中的焦躁仍在不断升级。"
    志雄 "「果然这么做还是太勉强了。」"
    "使用未成年人车票，连续换乘普通电车。"
    "晚上搭乘深夜的班车启程，第二天早上到达这里……"
    "虽然我对于这种麻烦又疲惫的方案很是担心，但是当事者却完全不当一回事。"
    志雄 "「真没办法啊……和结乃也仍然联络不上。」"
    "这次总不能再像之前那样住在我的公寓里了。"
    "唯一能为她提供住宿的好友，至今也联络不上。"
    window hide
    play sound "SE06_30"
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_SAA01"),"True","img/KA_SAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「噢，终于出来了！」"
    "在发车铃声响后不久，等待已久的人终于通过了验票口。"
    "向带着完全不符合女孩子旅行所需容量的小包的她，我不断挥手示意。"
    志雄 "「这里这里——！！」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA02"),"True","img/KA_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM10"
    voice "NYU15A_KA000"
    神奈 "「志雄！久等了——！」"
    "看到了我以后，神奈兴高采烈地小跑过来。"
    voice "NYU15A_KA001"
    神奈 "「好想见你哟——」"
    "好似演出一场感人的再会场景般的，神奈冲过来抱向我。"
    志雄 "「不好意思。真的没有时间了。」"
    "但是，十分遗憾，我还是将神奈的拥抱给躲开了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA08"),"True","img/KA_LAA08A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA002"
    神奈 "「真是。一点也不懂气氛。」"
    "对着鼓起了嘴的神奈，我苦笑说道。"
    志雄 "「拥抱之类的等到之后再补吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA003"
    神奈 "「这倒是。现在算起，几个小时后，一定会有欢喜的拥抱的。」"
    志雄 "「就是这样了。但是，如果赶不上的话，也就没希望了。我们赶快吧。」"
    "从这里到会场，徒步也用不了１０分钟。"
    "如果用跑的话，怎么看都是来得及的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA04"),"True","img/KA_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA004"
    神奈 "「好——！再呆在那里的话，我可不等你咯～」"
    window hide
    play sound "SE01_00B"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "明明是迟到的那个人，却比我先跑了出去。"
    志雄 "「真是——没有办法啊。」"
    "在叹气之前，我却先因为这神奈式的行动方式而失笑。"
    "在海边道路上来来往往都是带着孩子的父母，追赶着神奈的我肯定是一道少见的风景吧。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG22AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG22AA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    play sound "SE05_19L"
#FADE_IN 1
    "最终，我们还是勉强赶在截止之前办完了手续。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「真是感谢你啊。特地大老远过来。」"
    voice "NYU15A_KA005"
    神奈 "「在说啥呢。这可是我们两人制作的广播哦？到了现在再把我一脚踢开的话，我可要哭了。」"
    志雄 "「如果没有神奈在的话，肯定是无法完成的，那时我只能退出了。」"
    "我和神奈在截止前赶工制作的广播，最终平稳地获得了优秀作品奖。"
    "今天是优秀作品奖获得者，在海岸进行现场放送的日子。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA08"),"True","img/KA_LAA08A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA006"
    神奈 "「但是哦。电车都晚点那么多了，稍微把开始时间向后延一点也应该没什么问题的嘛。」"
    "神奈好不容易才调整好因为跑步而打乱的呼吸节奏，嘟囔着抱怨道。"
    志雄 "「其他人都是本地的哦，时间不会那么紧的。」"
    "大家应该都已经早早到达，做好了充分的准备，在等待比赛的开始吧。"
    "和其他出场者相比，我们已经背上了很大的不利因素。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA07"),"True","img/KA_LAA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA007"
    神奈 "「临时抱佛脚的人是没法得到好成绩的哦……」"
    志雄 "「等一下，可不能说这种话。」"
    "作为去年优胜者的发言，或许这的确是事实也说不定……"
    "但对于为了竞赛而准备到现在的人来说，听到这种话，心里肯定会不舒服的吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA008"
    神奈 "「我知道我知道。今年不知道跟什么样的人一起参加放送呢？真令人期待啊。」"
    志雄 "「去年的时候，都有些什么样的人？」"
    "去年的夏天，神奈是如何度过现场放送的，突然，我对此感到了好奇。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA07"),"True","img/KA_LAA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA009"
    神奈 "「实际上因为我太专心了，都没怎么注意。」"
    志雄 "「哈。神奈也会有这种事啊。太紧张了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA05"),"True","img/KA_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA010"
    神奈 "「不是哦。其实去年我也差点迟到了……」"
    "原来在办理手续的地方，工作人员看到神奈的时候露出的很复杂的表情是因为这个……"
    "还以为是因为她是去年的优胜者呢。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA011"
    神奈 "「而且出场顺序是第一组。于是就在根本搞不清状况的情况下开始，才注意到了就结束了。」"
    志雄 "「原来如此……」"
    "就那种状态下，都可以获得优胜，这才是神奈最可怕的地方吧。"
    志雄 "「那么，今年可要好好记住啦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA02"),"True","img/KA_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA012"
    神奈 "「那当然。这是夏天重要的回忆嘛。」"
    "回忆……"
    "普通的一句话，却让我的心里感到一丝疼痛。"
    "当初是为了制造回忆，才打算参加这次比赛的。"
    "那时我也和神奈一样，觉得那将成为我重要的回忆。"
    "但是……本该一起制造回忆的另一方，却在不知不觉中换了人。"
    志雄 "「不过，那个……神奈也真和这个小镇有缘，总觉得有些不可思议。」"
    "为了挥去心头灰暗的思绪，我很开朗地跟神奈搭起了话。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA013"
    神奈 "「嗯。所以，听说结乃要搬到这里来的时候，我真的很震惊哦。」"
    "只是一时兴起随意报名参加的比赛的举办地，正好是她的好友结乃转学的目的地……"
    "如果结乃的转学是在暑假中的话，或许还能听到比赛中神奈的广播呢。"
    voice "NYU15A_KA014"
    神奈 "「命运这东西，偶尔会以令人无法相信的形式来作弄人们。」"
    志雄 "「所以，我并不怎么喜欢那个词。」"
    "在自己如何努力也无法触及的地方持续地影响着自己的力量……"
    "如果说这就是命运的话，这种东西我才不要呢。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA03"),"True","img/KA_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA015"
    神奈 "「但是……反过来说，单纯地顺着命运的轨迹走下去的话，或许也会很有趣也说不定呢？」"
    志雄 "「命运这种东西，一定是像浊流一般奔腾的吧，这种东西我才不想要。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA02"),"True","img/KA_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA016"
    神奈 "「啊哈哈哈。这就是被称为『人生』的刺激类游乐项目吧。」"
    "开着玩笑的我们，至少打消了一部分因公开放送而带来的紧张感。"
    志雄 "「那么，差不多该开始了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA017"
    神奈 "「嗯！加油哟～」"
    "明明应该鼓足干劲的神奈，发出的却是让人感到脱力的声音。"
    stop music fadeout 132
    "但这时我们都还没有意识到。"
    "我们已经快要被卷入，称之为浊流都显得太过轻巧的命运的旋涡中了……"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG96AA@2x.jpg" as bg0 zorder 0 with dissolve
    pause (32/32.0)
    scene expression "img/BG96AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    "原本还是一片和谐的气氛。"
    "或者说是需要为大家制造一些竞争的感觉……"
    "因此，比赛的出场者们的确应该有一个见面的机会。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA06"),"True","img/MH_MAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_MA000"
    麻寻 "「啊？志雄结果还是来参加了？」"
    "但是，至少出场者中有两组……"
    "在互相看到对方的脸之后都呆住了。"
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
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_MAA10"),"True","img/KA_MAA10A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBB06"),"True","img/YU_MBB06A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    play music  "OBGM12"
    voice "NYU15A_YU000"
    结乃 "「学长……神奈……」"
    voice "NYU15A_KA018"
    神奈 "「结乃……」"
    志雄 "「……」"
    "结乃也在这里，和麻寻组成一组。"
    "然后，我和神奈则是一组。"
    "这里面所包含的意义，使我们两方都受到了冲击。"
    志雄 "「一直联络不上……原来是因为这个啊。」"
    voice "NYU15A_YU001"
    结乃 "「学长……为什么和神奈一起？」"
    "我是为了和结乃创造两人的回忆，而决定制作广播的。"
    "但是现在却和别人组成了另一组制作了另一个节目……现在，这两者猛烈地冲撞在了一起。"
    "刚决定参加比赛的时候，究竟要怎样才能想到现在这样的一个结局呢？"
    志雄 "「这个……」"
    "是为了结乃……"
    "这句话最终还是被我咽了下去。"
    "到了现在……说什么都已经没有用了。"
    志雄 "「结乃才是，一直以为联络不上，结果是在做这个啊？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBC05"),"True","img/YU_MBC05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU15A_YU002"
    结乃 "「这，这是……为了获胜后，和学……」"
    "结乃好像想说些什么，但和我一样，她也把话咽了下去。"
    "我和结乃的心里都明白。"
    "双方，都各有自己的想法这件事。"
    "但是，也知道我们采用的手段……制造了一条很难被修补的鸿沟这件事。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA04"),"True","img/MH_MAA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU15A_MA001"
    麻寻 "「啊，什么？怎么感觉气氛好奇怪啊？」"
    "只有在一旁还未能理解状况的麻寻露出了微妙的不可思议表情。"
    "因为某些原因，这次广播变成我一个人做了，所以帮帮忙吧……"
    "结乃一定是仅仅对她说了这些吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_MAA01"),"True","img/KA_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA019"
    神奈 "「嗯～发生了很多事呢。麻寻。果然瞒着我们和结乃两人在做这个啊～」"
    "配合着麻寻，神奈也用自己原有的悠闲的语气说道。"
    "这样，就完全化解了麻寻的警戒心……之后就可以随心所欲的从她那里问出真相了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA01"),"True","img/MH_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU15A_MA001A"
    麻寻 "「就是这样啊。已经决定要帮忙了之后……你们来了……为了不说多余的话，我可是费尽了心机啊。」"
    "虽然我猜测到她或许是帮忙隐瞒了结乃的行踪，但是，结果居然还帮她一起做了另一个节目。"
    "果然，那时候应该果断地追问到底的啊。"
    "但是……因为没有那么做而引起的命运，已经变成了不可阻挡的洪流。"
    voice "NYU15A_KA021"
    神奈 "「对了，结乃？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBC03"),"True","img/YU_MBC03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU15A_YU003"
    结乃 "「什么？」"
    "对于事情的大概了解了的神奈，面向结乃跨出了一步。"
    "她的表情并不是严肃的，而是以一种温和的眼神望着结乃。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_MAA04"),"True","img/KA_MAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA022"
    神奈 "「这么做，一定是有理由……的吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBC04"),"True","img/YU_MBC04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU15A_YU004"
    结乃 "「嗯……但是，但是……」"
    voice "NYU15A_KA023"
    神奈 "「志雄也是有理由的。这一点我能保证。」"
    "神奈轻轻地拍了结乃的肩膀，之后径直向我走来。"
    voice "NYU15A_KA024"
    神奈 "「志雄。结乃这么做一定是她自己的想法的，这一点我能够保证。」"
    "这是只有十分了解我和结乃两人的神奈才能下的断言。"
    "然后……对于我和结乃来说，神奈是一个足以信任的人。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_MAA01"),"True","img/KA_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA025"
    神奈 "「首先还是互相听一下对方的节目吧。有话也放到那之后再说……没问题吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBC05"),"True","img/YU_MBC05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU15A_YU005"
    结乃 "「嗯……」"
    志雄 "「明白了。」"
    "现在的我们除了点头之外什么都做不到。"
    "我们并不是相互背叛了对方……"
    "但是为了要说明这点，光靠语言是没有意义的。"
    "现在只有通过作为联结起两人的纽带的广播节目，才能证明这一点。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBC01"),"True","img/YU_MBC01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU15A_YU006"
    结乃 "「那么，等下再见了。因为我们先出场……你们好好听着哦。」"
    voice "NYU15A_KA026"
    神奈 "「当然，即使你说不要听我们也非听不可的哦。」"
    志雄 "「嗯，我很期待的。」"
    "期待这点我是真心的。"
    "结乃制作的广播节目，我决不能说没有兴趣。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA01"),"True","img/YU_MBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU15A_YU007"
    结乃 "「学长你们是最后一组吧。刚才在客席上我很清楚地听到的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_MAA02"),"True","img/KA_MAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA027"
    神奈 "「Ｏ——Ｋ。播放时看到了对方的话就挥挥手哦。」"
    "面对着一点变化都没有的神奈，看得出结乃的紧张感也得到了很大程度的缓解。"
    "结果……从头至尾我们都处于神奈的关照之下啊。"
    voice "NYU15A_YU008"
    结乃 "「麻寻，我们去吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA01"),"True","img/MH_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_MA002"
    麻寻 "「嗯。回头见。让我们好好决一胜负吧。」"
    window hide
    stop music fadeout 132
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "小幅挥着手离开的两人还是保持着笑容的，虽然只有一点点。"
    "这样的话……应该可以用万全的状态来迎接最后的播放的吧。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA028"
    神奈 "「喂！别摆出那么严肃的神情！」"
    window hide
    play sound "SE04_24"
#VIB_DOUKI 
#QUA3_ALL 
#VIB_STP 
    志雄 "「好痛！」"
    "对着呆呆地望着结乃她们离去的我，神奈猛地打了一下我的屁股。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA08"),"True","img/KA_LAA08A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA029"
    神奈 "「为了向结乃传递思念，都努力到了现在不是嘛？要更加振作一点。」"
    志雄 "「的确是这样……」"
    "好好地完成这次放送……"
    "接下来我所要做的，才是真正传达给结乃的，我想说的话。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA04"),"True","img/KA_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA030"
    神奈 "「那么，我们来对一下内容吧。对方可是结乃……要好好加把劲了。」"
    志雄 "「你还真有干劲啊……」"
    "就在刚才还在说，临时抱佛脚的家伙是不行的呢。"
    voice "NYU15A_KA031"
    神奈 "「那是当然的喽。结乃虽然是好友……但也是竞争对手啊。」"
    志雄 "「是这样？但是，就『Ｔ－ｗａｖｅ』的投稿的被采用次数来说，神奈可以压倒性的胜利啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA07"),"True","img/KA_LAA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    神奈 "「……」"
    "神奈以无比失望的眼神望着我。"
    "我真的说了如此奇怪的话了吗？"
    voice "NYU15A_KA033"
    神奈 "「志雄……你的脑子里难道只有广播吗？」"
    志雄 "「不是……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA05"),"True","img/KA_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA034"
    神奈 "「哎……」"
    "这次神奈回给我的是一声叹息。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA035"
    神奈 "「我和结乃可是青梅竹马。从小时候开始，无论学习还是运动，都一直视对方为竞争对手的哦。」"
    志雄 "「这样啊……」"
    "到底我的脑子被广播毒化到什么程度了呢。"
    "我不禁也苦笑了起来。"
    voice "NYU15A_KA036"
    神奈 "「学习也好，运动也好，美术也好，音乐也好……一切的一切，都是结乃以微弱的优势领先于我。」"
    志雄 "「这可真是令人意外啊……」"
    "不仅仅是投稿，神奈还能把矿石收音机改装接收ＦＭ广播。"
    "总觉得她在别的方面也应该是一个能够胜过结乃，事事领先的人物。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA04"),"True","img/KA_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA037"
    神奈 "「初恋也是结乃比较早啊！」"
    志雄 "「那个……并不能说是越早越好的事吧……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA07"),"True","img/KA_LAA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    神奈 "「……」"
    "啊……"
    "又被瞪了一次……"
    voice "NYU15A_KA039"
    神奈 "「对于结乃来说，初恋就等于首位男友就等于志雄哦……」"
    志雄 "「这，这样啊……」"
    "再次被强调了这件事，不禁让人略感害羞。"
    "……如果说对手的初恋是在高中还输了的话，的确有些太晚了。"
    志雄 "「说是输了的话，也就是说至今还没有初恋了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA040"
    神奈 "「不是哦。也不是那样。现在正在火热初恋中呢。」"
    志雄 "「这样啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA08"),"True","img/KA_LAA08A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA041"
    神奈 "「慢着！这时候难道不应该问，对方是谁之类的吗？」"
    "她抓住对此没有反应的我的肩膀，猛烈地前后摇晃着。"
    "莫非这是她很想要被问的事情？"
    志雄 "「但是，就算问了我也不认识吧？」"
    "对于完全不了解神奈的生活的我来说，自认为这种程度的反应已经是极限了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA042"
    神奈 "「这也未必哦？」"
    "神奈小声地嘀咕道，具体说的是什么我也没听清楚。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA08"),"True","img/KA_LAA08A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA043"
    神奈 "「总之，关于广播方面的事情，是我好不容易才找到的能够胜过结乃的一点哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA04"),"True","img/KA_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA044"
    神奈 "「既然结乃都出场了，我就决不能失败～」"
    "……结果她好像朝着比较微妙的方向鼓足了干劲啊。"
    "就是因为结乃执着于比赛结果，我才和她闹翻，最终导致了今天的这种情况。"
    "我可不想再因为同样原因和神奈搞成那种状况了……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA045"
    神奈 "「我拜托朋友们收集了一些投稿用的素材。让我们一起来选择一些能用的吧。」"
    志雄 "「哦，好。」"
    "还好……"
    "神奈还是那个神奈啊。"
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
    play music  "OBGM02"
#FADE_IN 1
    "广播比赛平稳地进行着。"
    "果然不愧是只有前几名才有权出场的现场直播。"
    "从现在的情况看，已经成为了一场超出预想的高水平比赛。"
    window hide
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA01"),"True","img/KA_XAA01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    志雄 "「我们能留出到现在还真是不可思议呢。」"
    voice "NYU15A_KA046"
    神奈 "「有吗？我完全不觉得我会输给到现在为止出场的任何一个人哦。」"
    志雄 "「不愧是去年的优胜者……」"
    "对于已经快要被压力击溃的我来说，神奈的自信无疑是一剂强心针。"
    "被她这么一说，快要失去的自信又回来了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA04"),"True","img/KA_XAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA047"
    神奈 "「不过，是说到目前为止的……」"
    志雄 "「问题是之后的出场者了。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我们所注目着的特别演播室中，有着略显紧张神色的熟人在里面。"
    "毫无疑问……那是我们想取得比赛优胜所要面对的最大敌人。"
    志雄 "「但是……看起来好像很紧张啊？」"
    window hide
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA05"),"True","img/KA_XAA05A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NYU15A_KA048"
    神奈 "「是啊。那样的话，很可能发挥不出平时应有的实力啊。」"
    "神奈也很担心的关注着结乃的情况。"
    "因为是密友，又是竞争对手……才更希望她能保持完美的状态。"
    "关于这点，我也抱有同样的想法。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA10"),"True","img/KA_XAA10A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA049"
    神奈 "「啊。但是好像不要紧的。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "不过，我们的不安立即被跟在结乃后面上场的麻寻消除了。"
    "看到了麻寻那同手同脚的走路方式，结乃自己的那份紧张也一定会忘记吧。"
    志雄 "「如果是故意这么做的，那还真厉害呢。」"
    window hide
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA01"),"True","img/KA_XAA01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NYU15A_KA050"
    神奈 "「结乃的话，或许正适合作为关照他人的那一方呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA02"),"True","img/KA_XAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA051"
    神奈 "「从某种意义上来说，麻寻正是结乃的最佳拍档。」"
    "在让紧张到快僵硬的麻寻放松的同时，结乃自己也完全静下心来。"
    "她们两人坐下，结乃在麻寻的暗示下开始了广播，而我和神奈则目不转睛地注视着她们。"
    window hide
#FADE_OUT 1
    pause (32/32.0)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA05"),"True","img/KA_XAA05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_IN 1
    志雄 "「嗯——这下……」"
    voice "NYU15A_KA052"
    神奈 "「或许要败了。」"
    "就如同结乃向我提案的一样，海边响起了她重视地方色彩的个性发挥型杂谈节目。"
    voice "NYU15A_YU009_K"
    结乃 "「接下来，波浪可能会有些高。正在游泳的各位请注意了。」"
    "结乃所追求的是『现场感』。"
    "就如同在和当天身处那个地方的人们说话一般，她的节目就这样持续地进行着。"
    "关注着周围的状况……同时也使用了之前调查过的天气预报等内容。"
    "根据实际情况的变化，杂谈的内容也随之千变万化。"
    志雄 "「对于满脑子都是节目构成的其他出场者来说，做到这样是不可能的呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA04"),"True","img/KA_XAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA053"
    神奈 "「因为是现场直播啊。这样的才是正确的广播节目哦。」"
    "『情报提供节目』。"
    "经过这方面特化的作品，在整个『比赛』场上也是一种特别的存在。"
    "因此，给听众的冲击也就特别大……而且，对于一定范围内的受众也会获得很好的反响吧。"
    voice "NYU15A_YU010_K"
    结乃 "「啊，喂，喂。要打破的是西瓜啊！千万不要把埋在沙里的人的头给打破了啊！」"
    play sound "SE07_08"
    "对于海滩边上正在发生的一些事情，她们也有注意到。"
    "作为广播的长期投稿者，她时常展现出来的异于常人的观察力，果然还健在。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA01"),"True","img/KA_XAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA054"
    神奈 "「即兴演出能做到这种程度，还真是出人意料。」"
    志雄 "「是啊。这样的话，剧本的存在意义也就差不多没有了。」"
    "至少，要是我干ＤＪ这一行的话，绝对不可能做出这样的节目。"
    voice "NYU15A_KA055"
    神奈 "「结乃或许很适合做主持人。进入这行的话，或许很快就能成为人气主持人了。」"
    志雄 "「或许吧。」"
    "通过显像管，看着手握麦克风做着报道的结乃的日子……"
    "或许这也是一种不错的未来呢。"
    志雄 "「但是，果然还是和目标有所偏差啊。」"
    "这个作品都是依靠结乃的个人能力完成的，麻寻只不过在那里进行一些器材的管理之类。"
    "如果，这个节目是和我一起完成的话……我能够从中得到什么参加比赛的实感吗？"
    "那样就真的能够成为属于两人的回忆吗？"
    志雄 "「即使没有好的结果，一样可以制造回忆啊。」"
    "听了我的话神奈静静地点了点头。"
    voice "NYU15A_KA056"
    神奈 "「那么，志雄用自己的节目来证明这一点不就行了？」"
    志雄 "「我知道。」"
    "作为比赛，我们已经知道自己的胜机是十分渺茫的了。"
    "即便如此，还是想要将这个充满了我的思念……包含了我的自信的广播给传达出去。"
    "因为我相信那样做的话，一定会……在我们心中留下某些东西的。"
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
    play sound "SE07_08"
    志雄 "「以上，就是我们最后的投稿。」"
    "将最后时刻写出来的来自莉莉丝的投稿作为结尾，我和神奈的节目的播送结束了。"
    "和审查员席上大家紧绷着的表情相反……海岸的观众们多次爆发出欢快的大笑。"
    voice "NYU15A_KA057_K"
    神奈 "「只受内部者欢迎的话可是没有意义的哦。」"
    "在我收集身边的人的投稿时，神奈反复地对我这么说。"
    "要将这些我们这个小圈子里的笑料拿出来让大家都感到有趣。"
    "这就是，这次我和神奈所确定的目标。"
    志雄 "「只有小圈子才能接受的节目啊……我也觉得我们的目标，只要有一点差错就会演变这样的节目。」"
    "我突然转换成了和至今为止相反的严肃语气，周围的人们一下子静了下来。"
    志雄 "「但即使如此，在我身边的，对我来说重要的人们，是他们始终支持着我……因此我想在这里向他们传达我的谢意。」"
    志雄 "「我是在很多人的帮助下，才能最终站在这里的。对此，向你们表示诚挚的感谢。」"
    "会场里，我深深地低下了头。"
    "向着听到了最后的观众们。"
    "以及……并不在现场的我的同伴们。"
    window hide
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA02"),"True","img/KA_XAA02A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NYU15A_KA058"
    神奈 "「也想向这其中，对你来说最最重要的人，传达些什么吧？」"
    志雄 "「是的。我就是因此才来参加这次比赛的。」"
    "我在节目刚开始的时候就注意到了，一个女孩子混在观众席之中。"
    "时而欢笑。时而不安。"
    "她也将这个广播节目，听到了最后。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA03"),"True","img/KA_XAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA059"
    神奈 "「真是的，就算把广播作为私人用途也要有个限度啊。」"
    "因为还留有一些搞笑节目的余韵，神奈小小地吐了我一下槽。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA01"),"True","img/KA_XAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA060"
    神奈 "「在那些烦人的审查员和管理人员们冲进来之前，请赶快。」"
    window hide
    stop music fadeout 132
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "虽然很紧张，但这也是我期待已久的时间。"
    "在这里，如果传达了我的思念的话，至今为止的所有事情全部都会付之流水，一切都会变回原样。"
    "至少，在和她联络不通之前，我都是这么认为的。"
    志雄 "「有这么一位始终支撑着……一个人一事无成的我的女生。」"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_SBA05"),"True","img/YU_SBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM14"
    "在人群中，她的眼眶湿润了，但却仍然紧紧地盯着我。"
    "那是一种包含着对之后的话语的期待的视线。"
    "我接受着这视线，说出了之前反复咀嚼过多次的感谢之语。"
    "强迫着……将自己从暑假开始就一直在思考的想法，原原本本地说出。"
    志雄 "「我的高中生活的最后的暑假，能和她一起度过，我真心的表示感谢。」"
    "在人群中的她的表情，些微有些变得僵硬。"
    "她……这个暑假也在我的身边。"
    "但是，能够被感谢的记忆……可能很淡吧。"
    志雄 "「她，曾多次用她那小小的手引导着陷入迷路的我。」"
    "从刚见面开始，一直到这个夏天，她对我来说一直是这样的存在。"
    "但是，现在的她……却正是那个使我陷入迷宫的人。"
    "我正打算说出一些很过分的事情。"
    "但是，我对于她……结乃的视线，却一点也没有逃避，我们仍然对视着。"
    志雄 "「我当初就是为了创造回忆而决定参加这次比赛的。」"
    志雄 "「和她一起制作的这个广播……为我创造了无法从心中忘却的回忆。」"
    "就算是一个也好，想更多地去创造回忆。结乃是这么说的。"
    "最终逃走的，是我还是结乃呢……"
    "但是，应该有着面对面的双方的回忆里面，并没有结乃的身影。"
    window hide
    hide lh0 with dissolve
#CHR_INIC 1
#CHR_POSC 1
#CHR_INIC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA10"),"True","img/KA_XAA10A@2x.png") as lh1 zorder 100:
        ypos 0.0
    with dissolve
    voice "NYU15A_KA061"
    神奈 "「慢点，志雄！什么……」"
    "这不寻常的状况，使旁边的她发起了慌。"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBC04"),"True","img/YU_MBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "坐在观众席上的她，就像是不愿听一般，堵住了自己的耳朵。"
    志雄 "「从今以后也，想要像制作这个节目一样……和她一起去创造更多的回忆。」"
    "这些，和我当初想好的话语没有任何区别。"
    "但是……本来应该传达思念的对象，已经不再是结乃了。"
    "我的心，无法阻止自己在不经意间将对象转换成了她。"
    hide lh0 with dissolve
#CHR_INIC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA08"),"True","img/KA_XAA08A@2x.png") as lh1 zorder 100:
        ypos 0.0
    with dissolve
    voice "NYU15A_KA062"
    神奈 "「志雄！别在那里瞎说啊！这样的话，就好像……」"
    "我仅仅用眼神就制止了想要插进话来的她——神奈。之后我继续说道。"
    志雄 "「每当我再次听到这个广播的时候，我都希望能够想起这个夏天所发生的一切。」"
    志雄 "「因为在这里的思念，回忆……将会一直留存下去。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA10"),"True","img/KA_XAA10A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    神奈 "「……！！」"
    "正好……结束的时间到了，麦克风被强制地关掉了。"
    "这之后，神奈对我所发出的抗议之声，外面的人已经听不到了……"
    "同时，在观众席上，则有一个掩面而泣的人影。"
    window hide
    stop music fadeout 1
    hide bg2 with dissolve
    hide lh0 with dissolve
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "冲出演播区的神奈，直接跑向了那个人影。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG22EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG22EA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    play sound "SE05_19L"
#FADE_IN 1
    "１小时后，到了发表审查结果的时间……"
    "带着憔悴的表情，结乃一个人出现在了发奖式的会场上。"
    "麻寻走过去安慰了她，她则回以一个刚强的笑脸。"
    "接着……向着我微微地低了一下头。"
    voice "NYU15A_X7000_K"
    アナウンス "「浜咲ＦＭ主办，广播比赛……今年最优秀的作品是……」"
    voice "NYU15A_X7001_K"
    アナウンス "「澄空高校２年生——春日结乃的作品！」"
    play sound "SE08_05"
    "就和我们预想的一样，最终优胜被结乃的广播所夺得了。"
    "而我们的广播……则完全落在了圈外。"
    "最终将『告白』加入的时候，我已经将结果置之度外了，所以并没有太多吃惊。"
    "而且，就算受到表彰……我也无法一个人来接受这个奖状。"
    "如果没有神奈在场的话，我没有取得那个的资格。"
    voice "NYU15A_YU011"
    结乃 "「志雄……学长。能稍微给我点时间吗？」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC01"),"True","img/YU_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "在大家的拍手中归来的结乃，带着略显虚弱的笑容，向我搭话道。"
    "我默默地点了点头，被结乃带着到了会场的外面。"
    window hide
    stop se fadeout 1
    pause (32/32.0)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play music  "OBGM16"
    voice "NYU15A_YU012"
    结乃 "「我获得了优胜。」"
    志雄 "「真厉害啊。祝贺你了。」"
    "对于瞄准着优胜的结乃来说，这是最好的结果了。"
    "我首先说出了祝福的言语。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC01"),"True","img/YU_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_YU013"
    结乃 "「学长？你知道为什么我会那么在意，那么想要获得优胜，你知道吗？」"
    志雄 "「……」"
    "我无法回答。"
    "如果我能够知道的话……结乃如果能够告诉我的话。"
    "或许我走过的道路就会和现在大不相同。"
    "面对沉默着的我，结乃露出自虐式的笑容，这么回答道。"
    voice "NYU15A_YU014"
    结乃 "「想要用奖金……和学长一起去旅行。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC03"),"True","img/YU_LBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_YU015"
    结乃 "「从稻穗那里，我连旅馆的资料也拿到了，只要优胜了的话，就……」"
    "保持着笑容，结乃的眼角，浮现出了泪珠。"
    "即便如此，她仍然保持着刚强的笑容，用正常的声音对我说到了最后。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC05"),"True","img/YU_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_YU016"
    结乃 "「但是，这已经没有意义了呢。」"
    志雄 "「是，啊……」"
    "手段和目的，在我和结乃之间完全的反转了过来。"
    "我，追求着在广播的制作过程中创造回忆……"
    "结乃，则希望以比赛的奖金来创造回忆。"
    "从这里面所产生的裂痕……最终没能被填补。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC01"),"True","img/YU_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_YU017"
    结乃 "「神奈这么说了。」"
    voice "NYU15A_YU018"
    结乃 "「那个最后的告白……本来是为了我而做的。」"
    "追了上去的神奈貌似把所有的事情都告诉她了。"
    voice "NYU15A_YU019"
    结乃 "「有一本叫『麦琪的礼物』的小说，你知道吗？」"
    志雄 "「知道大概内容。」"
    "两个相爱着的恋人，各自有着对自己来说最珍贵的怀表和美丽的长发。"
    "两人分别想要将装饰怀表的表链，以及梳理美丽长发的梳子来作为给对方的礼物。"
    "为此，他们分别将怀表和长发变卖了。"
    "结果他们只剩下了已经没有用的锁和梳子，但是，两人却仍然很幸福……这样的一个故事。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC05"),"True","img/YU_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_YU020"
    结乃 "「各自为了对方的奖金和告白……结果都变成了没有意义的东西。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC03"),"True","img/YU_LBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_YU021"
    结乃 "「但是，却没能留下任何幸福。那一定可以被称为——愚者的礼物了吧。」"
    "想借着玩笑保持笑容的的结乃……结果却从眼眶中溢出了眼泪。"
    "我不禁想将她抱进怀里，但却在差一点就要伸手的时候忍住了。"
    志雄 "「对不起。」"
    "深深地。"
    "我低下了头。"
    "对现在的我来说，除了这个之外什么都不能做。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC01"),"True","img/YU_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_YU022"
    结乃 "「如果在这里能够拥抱我的话，就能够逆转成为好结局了呢。」"
    voice "NYU15A_YU023"
    结乃 "「果然凡事不能像戏剧一样完美呢。」"
    "她表现得很开朗。"
    "但是，结乃她的确已经接受了跟我分手这件事情。"
    voice "NYU15A_YU024"
    结乃 "「神奈她……在海岸等你。」"
    voice "NYU15A_YU025"
    结乃 "「她应该以为我也会去的吧……帮我向她道歉吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC05"),"True","img/YU_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_YU026"
    结乃 "「果然今天，还是不行。要是去的话，或许我会对神奈说很过分的话也说不定。」"
    "说完这些，结乃用手背将眼眶里积蓄的泪水抹去，抬起了头。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC03"),"True","img/YU_LBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_YU027"
    结乃 "「再……」"
    "刚说到一半，她就以一字形并拢了嘴，把之后的部分咽了下去。"
    "对于这句话的意义，结乃比谁都更加能够理解。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_YU028"
    结乃 "「至今为止的一切，谢谢你。」"
    "再见……回避着这个单词，结乃向我道了谢。"
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
    "说完之后，结乃便跑着从我面前消失了。"
    志雄 "「结乃……」"
    "眼中感到了一阵发热。"
    "但即便如此……"
    "我还是没有流下哪怕一滴眼泪。"
    window hide
#FADE_OUT 1
    pause (32/32.0)
#FADE_IN 1
    "半落的夕阳照耀着海岸，人群已渐散去。"
    "海滩上是一个谈情说爱的好地方，周围也尽是一对对的情侣。"
    "对于现在的我来说，这里或许仍是一个令人痛苦的地方吧。"
    志雄 "「在了……」"
    "在这之中，有一个团坐在地上望着夕阳的女孩子。"
    "看到了我的话，她可能会逃走吧……"
    "怀着这种不好的预感和胆怯的心情，我从她背后悄悄接近。"
    voice "NYU15A_KA064"
    神奈 "「……志雄果然来了啊。」"
    voice "NYU15A_KA065"
    神奈 "「结乃不会来的这件事，其实我心里也很清楚的。」"
    "我的预感应该没有错吧。"
    "伴随着一声叹息，神奈站了起来，转身面向我。"
    window hide
#CHR_INIC 0
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA05"),"True","img/KA_XAA05A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NYU15A_KA066"
    神奈 "「为什么要来呢。在那里抱紧结乃，帮她擦去眼泪的话……明明就能大逆转收获一个完美结局的说。」"
    志雄 "「结乃跟你也说了一样的话哦。」"
    "面对着这对在奇怪的方面很同步的密友，我苦笑了一下。"
    志雄 "「但是，不能不来啊。因为我还没有等到属于我的结果发布呢。」"
    "和比赛相比更重要的结果还没有被公布。"
    "审查员只有一人……"
    "只有面前面露怒色的神奈一个人。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA04"),"True","img/KA_XAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA067"
    神奈 "「我可是既站在结乃那一边，又站在志雄这一边的啊。」"
    voice "NYU15A_KA068"
    神奈 "「如果不能两全的话……只站在其中一方的那一边这种事，我不干！」"
    "神奈正在妄图制造一条名为逃避的路。"
    "而这也一定已经被结乃看穿了吧。"
    志雄 "「结乃她……并没有跟我说再见哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA05"),"True","img/KA_XAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA069"
    神奈 "「傻瓜，为什么在这种时候，那个孩子还要担心这些事情呢！」"
    "浮于形式的愤怒发言。"
    "但是，因为结乃的行动，神奈失去了最容易寻找的那条逃避之路。"
    志雄 "「这样的话，就只剩下神奈到底是喜欢还是讨厌我的问题了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA04"),"True","img/KA_XAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA070"
    神奈 "「甩掉了自己的女朋友，然后向她的好友告白……这种人难道有什么能让人喜欢上的理由吗？！」"
    "和以往轻佻的玩笑不同，这次则是从正面说出了撕开我伤口一般的尖锐话语。"
    "但是……从来不会去伤害别人的人所说的话……往往也会伤害到自己。"
    "在那愤怒的表情背后，很明显的隐藏着痛苦之色，这也是神奈的风格吧。"
    志雄 "「没有。但是对于神奈你不同，因为神奈你并不正常的吧。」"
    "即使会被１００个女孩子讨厌，但只要有一人能在身边就行。"
    "如果这一人是神奈的话……对我来说就没有任何问题。"
    voice "NYU15A_KA071"
    神奈 "「那么，反过来说，初恋比好友晚一步爱上了同一个人……」"
    voice "NYU15A_KA072"
    神奈 "「在好友被甩了的同时，对于对方的告白轻松ＯＫ了的女孩子，有什么被喜欢的理由吗？」"
    "充满了纠结自虐的发言。"
    "就好像用尖刀扎进心脏来回搅动一般……痛苦，我们两个人都是这样。"
    志雄 "「没有。」"
    "我重复了刚才的回答。"
    志雄 "「但是，因为我也不正常。」"
    "即使有１００个人在背后对神奈指指点点……我也有成为唯一不这么做的一个人的觉悟。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA05"),"True","img/KA_XAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU15A_KA073"
    神奈 "「我可以说喜欢你吗？」"
    志雄 "「现在不说的话，就没有机会了哦。」"
    "我们互相承受着自责……同时，在其中也包含着我们不得不接受的事实。"
    "在这里不能达成一致的话，我们两人一定不会有未来。"
    voice "NYU15A_KA074"
    神奈 "「或许会成为超远距离恋爱哦？」"
    志雄 "「就算如此，也已经喜欢上了啊。」"
    voice "NYU15A_KA075"
    神奈 "「我很粗暴哦？」"
    志雄 "「即使如此也已经喜欢上了哦？」"
    voice "NYU15A_KA076"
    神奈 "「或许是一个……背叛好友的女孩哦？」"
    志雄 "「就算这样也……喜欢。」"
    "缺点什么的，不说也知道。"
    "但是，这种东西不管积累多少……我喜欢神奈的感情都是无法抑制的。"
    window hide
    stop sound
#BG_SET_BACK 
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU10A")]=True
    scene expression "img/EVN_YU10A@2x.jpg" as bg1 with dissolve
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play music  "OBGM29"
    voice "NYU15A_KA077"
    神奈 "「我也是……不管怎样都喜欢志雄！」"
    "说出口的同时，神奈向我的怀里飞扑了过来。"
    voice "NYU15A_KA078"
    神奈 "「好痛苦啊。看到你和结乃两人闹起别扭，我却在心里暗暗高兴。」"
    voice "NYU15A_KA079"
    神奈 "「我都快要讨厌我自己了……」"
    "神奈在我怀里声泪俱下地诉说道。"
    "或许是不想让我看见哭泣的脸，她把脸深深埋进了我的怀里。"
    志雄 "「就算神奈讨厌自己，我也还是喜欢神奈。」"
    "这一点，已经再也不会改变了。"
    "这已经是不能改变的，背负在我身上的十字架了。"
    voice "NYU15A_KA080"
    神奈 "「嗯……谢谢、」"
    "虽说就这么把头埋着也不错，但这样的话，有些事情就做不了了。"
    志雄 "「神奈。抬一下头好吗？」"
    voice "NYU15A_KA081"
    神奈 "「不要。才不想让你看见人家哭呢。」"
    "神奈就这么在我怀里摇起了头。"
    "不过，利用这个机会，我顺势把神奈的头抬了起来。"
    voice "NYU15A_KA082"
    神奈 "「真是的。都说了不要了……」"
    志雄 "「没关系。哭泣也好，发怒也好，我喜欢神奈的心情，不会改变。」"
    voice "NYU15A_KA083"
    神奈 "「笨……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU10B")]=True
    scene expression "img/EVN_YU10B@2x.jpg" as bg1 with dissolve
    "在发出抗议之声之前，我封住了神奈的唇。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU10C")]=True
    scene expression "img/EVN_YU10C@2x.jpg" as bg1 with dissolve
    "神奈闭上了眼，接受这一切……"
    "这样的表情，同样也是我的最爱。"
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
#MOV_PLY 6
#RSET S91
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
    $ renpy.end_replay()
    return