label NYU16A:
    $currentlabel = "NYU16A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
    $month = '08'
    $day = '28'
    $date = '1'
#CAL_DSP_GRP 3,CAL_0828
    scene expression Solid("000") with fade
    show expression "img/NIMG15E-568h@2x.jpg" as cal zorder 5
    show expression "img/08_28_MONDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG08AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG08AA@2x.jpg" as bg0 with dissolve
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
    志雄 "「哎……果然还是传开了。」"
    "暑假渐进尾声……"
    "在返校日来到学园的我，俨然成了周围窃窃私语的矛头。"
    "别看我虽然这样，好歹也是澄空学园的学生会长，多少算得上是个名人。"
    "结乃也是放送部的ＤＪ，并且作为去年奏云祭上演出戏剧的核心人物，在同学中也有着极高的人气。"
    "而这样的我们的关系，在这个夏天走到终点这件事……自然而然成为了全校范围的话题。"
    voice "NYU16A_X5000"
    男子生徒Ａ "「据说塚本学长跟着其它女生跑了哦？」"
    voice "NYU16A_X6000"
    女子生徒Ａ "「还有呢、那个人竟然还是春日同学的好朋友哟。」"
    voice "NYU16A_X5001"
    男子生徒Ａ "「真的？太搞了吧！」"
    voice "NYU16A_X6001"
    女子生徒Ａ "「春日同学，好可怜啊……」"
    "大部份言论都对结乃表示同情，对我表示愤慨。"
    "传言基本上都是事实……中伤的对象不是结乃而是我已经算是万幸了。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 0
#CHR_POSC 1,(320-192)
#CHR_POSC 2,(320+192)
#CHR_DSPTC 0,1,2,RI_MAA06,TO_MAA03,CH_MAC04
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA06"),"True","img/RI_MAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA03"),"True","img/TO_MAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC04"),"True","img/CH_MAC04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .8
    with dissolve
    voice "NYU16A_TO000"
    亨 "「嘛、不要太放在心上。」"
    voice "NYU16A_RI000"
    莉莉丝 "「传言这种东西来也匆匆去也匆匆嘛。」"
    "莉莉丝和亨都在鼓励我。"
    "这种时候，才亲身体会到有着死党的好处。"
    voice "NYU16A_CH000"
    智纱 "「……」"
    "和两边都关系很好的智纱很困扰的看着我。"
    "但是，眼瞳中没有诉说对我或结乃的一点责备……只有这点我确实的理解了。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG09EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG09EA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    play sound "SE05_13L"
#FADE_IN 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAA01"),"True","img/YU_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU16A_YU000"
    结乃 "「那么，我先走了。大家辛苦了。」"
    "学生会的新学期准备会议结束了。"
    "那天之后，第一次见面的结乃似乎要比想象中精神……"
    "表面上还是和以前一样辅佐着我的工作，让会议顺利的进行了下来。"
    志雄 "「多谢了。结……春日同学。」"
    "一直习惯了直呼其名的我，把叫到了一半的名字咽了下去，改用最初相遇时候的叫法来称呼结乃。"
    "以此，再次确认两人之间拉开的距离，用我的方式划清界限。"
    voice "NYU16A_YU001"
    结乃 "「叫结乃就可以了。事到如今再用姓来称呼人家跟让人觉得难为情了。」"
    "在兴致勃勃地关注我们的学生会会员中，我们进行着久违的对话。"
    voice "NYU16A_YU002"
    结乃 "「不要紧的。虽然可能要花上一点时间……一定会过去的。」"
    voice "NYU16A_YU003"
    结乃 "「比起水族馆的回家路上……现在就算看到志雄学长心也不会痛了。时间一定会冲淡一切的。」"
    志雄 "「是吗……」"
    "在没有见面的这段时间里，结乃也一定以自己的方式整理过心情了吧。"
    "一定，下次见面的时候，一定能更接近至今的结乃吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB01"),"True","img/YU_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU16A_YU004"
    结乃 "「不管是学长、还是神奈……我都好喜欢。总有一天一定能说出祝福的话语的。」"
    "擦身而过的时候，结乃在我耳边窃窃私语道。"
    志雄 "「嗯。我等着。」"
    "我和神奈也是，不管哪个都好喜欢结乃。"
    "无论被多少人指责自私和任性……我们最想收到祝福依旧是来自结乃的。"
    志雄 "「辛苦你了。新学期也请多关照啊，结乃。」"
    voice "NYU16A_YU005"
    结乃 "「好的。会长也不要太操劳，早点回去哦。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE00_25"
    "结乃对我报以淡淡地笑容，和其它学生会成员结伴回家了。"
    "虽然那个笑容是发自内心的，但我能感到，这个笑容已经和之前她只为我绽放的笑容有了天壤之别。胸口的苦楚渐渐在身体里扩散开来。"
    志雄 "「真是自作自受啊。」"
    "在结乃的面前，选择了神奈的人是我。"
    "并不后悔做出了这个决断……然而把心中残破的地方重新补起，还需要相当长的时间。"
    志雄 "「但是，这些都要我一个人来收拾么……」"
    "惯例的学生会室残局处理让我非常头痛。"
    "以前都是结乃一起帮忙完成的工作，从今以后要一人来完成。"
    志雄 "「得想想在时间内把工作处理掉的方法了……」"
    "本来这些就是学生会长一个人应该处理掉的工作。"
    "是啊。至少去年的学生会长就是一个人解决掉的。"
    voice "NYU16A_KU000"
    克罗艾 "「不够格啊。这种处理的方法、天晓得啥时候能完成？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA05"),"True","img/CL_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM04"
    志雄 "「啊，克罗艾学姐。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA01"),"True","img/CL_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU16A_KU001"
    克罗艾 "「塚本，好久不见了呢。」"
    志雄 "「到底是吹了什么风！明明毕业以来一次都没有来过。」"
    "毫无前兆的跨进只剩一人的学生会室的人是……上届学生会长克罗艾学姐。"
    "那英姿飒爽的身姿一直是我的憧憬，她也一直很照顾我。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC04"),"True","img/CL_LAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU16A_KU002"
    克罗艾 "「在忙啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB02"),"True","img/CL_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU16A_KU003"
    克罗艾 "「不过呢，塚本的活跃表现我有耳闻哦。貌似成了个称职的学生会长了呢。」"
    "虽然没有身着校服，这个人只要站在学生会室里，就好像回到了一年前。"
    "克罗艾学姐的带领下……为奏云祭奔走的每天好充实。"
    志雄 "「哪，哪里的话。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA02"),"True","img/CL_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU16A_KU004"
    克罗艾 "「况且……不好的传闻，当然也有所耳闻。」"
    志雄 "「果然是这样么。」"
    "竟然已经传到身为毕业生的克罗艾学姐那里了。"
    "流言的传播速度真是可怕。"
    "因为担心这点，所以特地过来看望的么。"
    志雄 "「如果不是因为这样的理由就好了，其实我在别的时候更希望学姐你能过来啊。」"
    "最好是，暑假开始的时候。"
    "多希望看到的是和结乃两人一起努力的学生会，那样才能让克罗艾学姐安心。"
    "看到现在的我，只能让学姐感到失望和不安。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB03"),"True","img/CL_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU16A_KU005"
    克罗艾 "「比想象中……要有精神呢。」"
    志雄 "「是呢。毕竟光是垂头丧气也解决不了什么问题。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU16A_KU006"
    克罗艾 "「春日同学也说了一样的话呢。」"
    志雄 "「是……嘛……」"
    "来这里的途中擦身而过了么。"
    "结乃也……不希望让学姐看着现在这个状态吧。"
    window hide
    stop music fadeout 116
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE03_30"
    志雄 "「学，学姐？」"
    "因学姐的话语而低下的我的头，下一瞬间发现自己已经被克罗艾学姐抱入怀中。"
    voice "NYU16A_KU007"
    克罗艾 "「不要说话。刚才对春日同学也做过一样的事情的。」"
    "几近陷入混乱的我，现在被克罗艾学姐温柔的抱住。"
    "这份柔软和温暖的感触……让我渐渐恢复镇静。"
    voice "NYU16A_KU008"
    克罗艾 "「你们两个……都变得坚强了呢。」"
    志雄 "「才没有这回事。我一点点都没有变坚强……」"
    "真的变坚强的话，就应该不会感到心痛了。"
    "自己选择的人，和未来……应该能够勇往直前。"
    voice "NYU16A_KU009"
    克罗艾 "「但是，塚本你们不正在努力跨越这道坎么。」"
    "学姐继续温柔轻抚着我的头。"
    "好像有点……重拾儿时关于母亲的记忆的感觉了。"
    voice "NYU16A_KU010"
    克罗艾 "「和春日同学度过的岁月不觉得后悔吧？」"
    志雄 "「当然。怎么可能……会后悔……」"
    "泪水不禁在眼圈中打转。"
    "就算不勉强去制造什么回忆……和结乃一起度过的日日夜夜也全都刻在心中。"
    voice "NYU16A_KU011"
    克罗艾 "「两个人的岁月使得塚本和春日同学都成长了呢。」"
    voice "NYU16A_KU012"
    克罗艾 "「没关系。一定……你们一定能向着未来前进的。」"
    "已经……是……极限了。"
    "在学姐的怀里，我的泪水夺眶而出。"
    志雄 "「呜……咕……呜。」"
    "眼泪怎么都停不下来。"
    "对这样的我，学姐不顾衣服被泪水弄脏依旧拥抱着我。"
    voice "NYU16A_KU013"
    克罗艾 "「很努力了呢。至今为止一直没能哭出来吧。」"
    voice "NYU16A_KU014"
    克罗艾 "「现在没有其它人在看、尽情地哭出声来也可以。」"
    "在学姐的臂弯中，我大声地哭了起来。"
    "分手之日……不知为何没有流出的泪水，止也止不住的流了出来。"
    志雄 "「呜哇啊啊啊啊啊啊啊啊啊！！」"
    "随着泪水那天起一直积在心中的某种情感也宣泄而出……"
    "终于在我心中，一段小小的恋情真正迎来了结束。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 1
#BG_SETWC 0,1,BG33AA,BG39NA
    scene expression "img/BG33NA@2x.jpg" as bg0
    with dissolve
    pause 1
    scene expression "img/BG39NA@2x.jpg" as bg0
    with dissolve
#FADE_IN 1
    志雄 "「那么、接下来……」"
    "『Ｔ－ｗａｖｅ』开始前１０分钟。"
    "我拿出手机，播出电话簿最上面的手机号码。"
    志雄 "「今天也投了稿。要是能被读到就好了。」"
    "远隔两地的我们，无法一起听广播。"
    "所以，不知何时起一到广播的时间我们就互相呼叫对方的手机。"
    "今天正好轮到我，刚进房间我就急忙拨出了神奈的手机。"
    window hide
    play sound "SE02_19L"
    志雄 "「咦？」"
    "『Ｔ－ｗａｖｅ』的ＦＡＮＳ以外不能会有的这铃声……"
    "这铃声，随着我拨打的电话同时在门外响了起来。"
    voice "NYU16A_KA000"
    神奈？ "「真，真是的！为什么这个时候响起来啊啊啊啊！」"
    "接着听到的是，貌似在哪里听到过的模糊的声音。"
    "为什么，她会在这里？"
    志雄 "「真的假的……」"
    window hide
    play sound "SE00_00"
#SE_VOLC 1,64
    hide bg1 with dissolve
    scene expression "img/BG33AA@2x.jpg" as bg0 with dissolve
    "我房间的房门，不出所料的，自己打开了。"
    "房门锁好了这件事在今天早上，明明确认过了好几遍……。"
    window hide
#SE_VOLC 1,255
    show expression "img/BG15NA1@2x.jpg" as bg0 with dissolve
    scene expression "img/BG15NA1@2x.jpg" as bg0 with dissolve
    pause (16/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA02"),"True","img/KA_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU16A_KA001"
    神奈 "「哟！」"
    play sound "SE02_03"
    志雄 "「……怎么进来的？」"
    "比起对突然的来访者表示震惊，我下意识地先询问起了眼前的疑惑。"
    "要是这种程度就大惊小怪的话，是根本没法和神奈在一起的，这件事我最近已经深刻的体会到了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU16A_KA002"
    神奈 "「钥匙这种东西在上次来玩的时候就取得了。」"
    志雄 "「哈……什么时候？」"
    "真是不能掉以轻心。"
    "即便如此……在不法侵入者面前，我紧绷的表情还是逐渐缓和了下来。"
    志雄 "「要来玩的话至少事先联络一下呀。」"
    "神奈的行动总是让人摸不着头脑。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA08"),"True","img/KA_LAA08A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "然而，面对我的抱怨神奈不满的撅起嘴。"
    voice "NYU16A_KA003"
    神奈 "「今天才不是来玩的呢！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA03"),"True","img/KA_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU16A_KA004"
    神奈 "「今天呢……是找这间公寓主人的志雄同学有事呀。」"
    "那笑容的背后，貌似有什么阴谋……"
    "我暗暗做出无论会发生多么惨烈的事件都能勇于承受的觉悟，在自己的心灵前架好了抵御冲击的防壁。"
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
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU11A")]=True
    show expression "img/EVN_YU11A@2x.jpg" as bg0 with dissolve
#BG_SET_DEFC 0,EVN_YU11A
#FADE_IN 1
    voice "NYU16A_KA005"
    神奈 "「锵！」"
    window hide
    play music  "OBGM18"
    "面前出现的是……穿着熟悉的澄空高中校服的神奈。"
    志雄 "「为什么……穿着这个？」"
    voice "NYU16A_KA006"
    神奈 "「哈哈哈哈。插班考试合格了。」"
    "满脸得意的神奈，张开双手向我展示起校服来。"
    "不管发生什么事都决定处惊不乱的我，终于还是震惊的说不出话来。"
    voice "NYU16A_KA007"
    神奈 "「所、以呢，想要借一间房间。记得准备一间超级房间哦。」"
    "相隔的遥远距离，一瞬间缩短了……"
    "神奈的行动力真是惊人。"
    "至今为止在生活中最接近的女生是——莉莉丝……但这次，距离的记录被大大地刷新了，再这样下去，下次我就要被ＫＯ了吧。"
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU11B")]=True
    show expression "img/EVN_YU11B@2x.jpg" as bg0 with dissolve
    voice "NYU16A_KA008"
    神奈 "「啊，当然……一起住在这间房间里也完全没有问题，怎么样？」"
    志雄 "「神，神奈啊！」"
    "对不知道到底有几分是认真的神奈的话语，我终于发出了抗议的声音。"
    志雄 "「真够呛……」"
    "脑中浮现出今后也会被神奈搞得团团转的预感，我不禁苦笑起来；但这恰恰是最适合我们的交往方式，于是我只好加倍地苦笑。"
    "在现在的状况下转校到澄空这件事，实际上并没有想象中的那么多好处。"
    "即使这样……神奈她也来到了这里。"
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU11A")]=True
    show expression "img/EVN_YU11A@2x.jpg" as bg0 with dissolve
    voice "NYU16A_KA009"
    神奈 "「啊哈哈哈哈。今后也请多关照了，达令。」"
    "即使这样，对于走过的路我也不会后悔，今后也不想后悔。"
    "虽然大概和神奈一起迈向的道路将会是迄今为止从未想过的艰难。"
    "但是将来我们回过头去，看向自己曾经走过的路时，也一定……会露出发自内心的微笑的吧。"
    "从今以后，迎来的是和之前完全不同的每一天。新的道路，从此时，从身在这里的我们脚下，开始缓慢而坚定地延展。"
    window hide
#MUS_VOL 255
    pause (128/32.0)
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