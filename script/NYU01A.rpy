label NYU01A:
    $currentlabel = "NYU01A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '19'
    $date = '3'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/NIMG19E-568h@2x.jpg" as bg1 with dissolve
    pause
    hide bg1
    with dissolve
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG09EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG09EA@2x.jpg" as bg0 with dissolve
    play sound "SE05_13L"
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
    voice "NYU01A_X4000"
    女子生徒１ "「文件终于弄好了，这样就可以了吧？」"
    if not persistent.dictlist[4] and persistent.show_dict:
        $persistent.dictlist[4]=True
        show screen dict_pop(i=4)
    voice "NYU01A_YU000"
    结乃 "「嗯，稍微等一下……」"
    if not persistent.dictlist[42] and persistent.show_dict:
        $persistent.dictlist[42]=True
        show screen dict_pop(i=42)
    "澄空学园的暑假即将到来。"
    if not persistent.dictlist[53] and persistent.show_dict:
        $persistent.dictlist[53]=True
        show screen dict_pop(i=53)
    "去年的奏云祭后，不知不觉间我已经坐上了学生会会长的专用座位。"
    voice "NYU01A_YU001"
    结乃 "「啊……这里好像弄错了吧？」"
    voice "NYU01A_X4001"
    女子生徒１ "「诶？ 真的诶，对不起，我马上改过来。」"
    voice "NYU01A_YU002"
    结乃 "「没关系啦，这点小错我自己来就行了。」"
    "学生会成员经历了大换血，结乃也成了学姐，照顾着1年级的学弟学妹们。"
    if not persistent.dictlist[3] and persistent.show_dict:
        $persistent.dictlist[3]=True
        show screen dict_pop(i=3)
    "而我……虽然达不到前任会长克罗艾学姐的水平，但是基本的职责也还是有好好履行的。"
    "就像现在这样，我密切关注着学生会里每个人的工作表现……"
    voice "NYU01A_YU003"
    结乃 "「然后，这个地方要写的清楚一点，重点不能突出的话是不行的哦。」"
    "好吧，实话实说，其实我只是看着别人工作，自己做个样子而已。"
    "今年秋天的奏云祭后，我的会长任期就结束了。"
    "多亏了学生会核心人物结乃的帮助，我才能轻轻松松地度过这一年。"
    "大家都说，明年的学生会会长位置非结乃莫属，在这件事上，我也有相同的看法。"
    voice "NYU01A_YU004"
    结乃 "「其他的部分应该没问题了，今天就到这里吧。」"
    voice "NYU01A_YU005"
    结乃 "「辛苦了，剩下的交给我和会长做就可以了。」"
    "回过神来，除去现在正在与结乃对话的女生，其他人都已经离开了。"
    "拜夏季的漫长白昼所赐，我们注意到时间的时候，时钟的指针已经挪到了一个非常夸张的位置。"
    voice "NYU01A_X4002"
    女子生徒１ "「嗯，学姐也辛苦了。」"
    "那女生连忙点头行礼，抱着书包离开了学生会室……"
    voice "NYU01A_X4003"
    女子生徒１ "「那么，请二位慢慢享受吧～」"
    play sound "SE00_26"
    "本已经走出房门的女生又特意从门边探出头来，飞快地补充了一句。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    stop sound
    play music "BGM06"
    voice "NYU01A_YU006"
    结乃 "「啊哈哈哈～连１年级的新生都取笑我们了呢。」"
    志雄 "「习惯了这种玩笑的我们貌似也有问题吧？」"
    "现在，只要是熟识的人，几乎都会用这种语气和我们寒暄。而这种时候，我和结乃也只有相视一笑。"
    "我们在交往的事，整个澄空都无人不知。"
    "所以，对于发生在本校的学生会室里的戏弄我们都已经习以为常了，就像刚才那样，连１年级的新人也不会在这点上对我们客气。"
    voice "NYU01A_YU007"
    结乃 "「明明是个１年级生，却一点也不客气呢。」"
    志雄 "「结乃……你有资格这么说别人么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB04"),"True","img/YU_LAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU008"
    结乃 "「啊哈？我觉得我是个很温顺的学妹来着……」"
    志雄 "「呵呵呵……那刚才的那个１年级生明显是个更加温顺的学妹。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAC02"),"True","img/YU_LAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU009"
    结乃 "「诶？没那样的事啦！」"
    "虽然结乃一脸不满，但是，在戏弄学长这方面，她绝对不输给任何人。"
    "很多时候，她还要更胜一筹，会凶残到利用校园广播公开调戏我。"
    志雄 "「不过，１年级学生要是都能像结乃那样认真做事就好了。」"
    "相比那些懒散的学生，结乃这样精力充沛的类型或许更适合学生会。"
    志雄 "「不说了，把剩下的事情抓紧完成好了，还剩下哪些事情呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA01"),"True","img/YU_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU010"
    结乃 "「我想想，我修改刚刚的文件，志雄学长就看一下那边的文件吧。」"
    志雄 "「了解。」"
    "空荡荡的学生会室里，只剩下两个人在收拾余下的工作。"
    "这几乎成为了我和结乃每日必做的功课。"
    "……从某种意义上说，这种情况也可能是别人故意为之。但我们并不介意。"
    志雄 "「哇啊，还有这么多，看来要花一些时间了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB02"),"True","img/YU_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU011"
    结乃 "「打起精神来，会长。」"
    志雄 "「真没办法啊，你那边先完成的话来帮帮忙哦。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我和她单独相处的时间比和其他人待在一起的时间的总和还要长，要说我们像恋人一样，的确和真正的恋人没有什么区别。"
    "不过……"
    "一起度过了这么多的时光，却感觉两人的关系并没有什么实质性的发展。"
    voice "NYU01A_YU012"
    结乃 "「志雄学长，可以帮我拿一下那边的订书机吗？」"
    "虽然我对结乃直呼其名了，可是结乃一如既往地叫我『志雄学长』。"
    "并非是因为在外人面前会害羞，我们单独相处的时候，她依旧是这样的。"
    "虽然常有约会，但是牵手却非常困难……接吻更是屈指可数。"
    "尽管他人看向我的目光中经常饱含了嫉妒和鄙视，可真的什么也没有发生过……"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA01"),"True","img/YU_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU013"
    结乃 "「话说马上就要暑假了吧。」"
    志雄 "「嗯，期末考试也要到了。」"
    "临近暑假，面对贴出来的期末考试安排表，真想立刻转身装作没看见。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB06"),"True","img/YU_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU014"
    结乃 "「没问题吧？学长明明已经是备考生了……」"
    志雄 "「胜负角逐现在才刚刚开始呢，虽然并不知道该做些什么实质性的东西，还是预约去试听几个补习班的暑期课程吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAC01"),"True","img/YU_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU015"
    结乃 "「你要去上……补习班？」"
    志雄 "「嗯，我打算从秋天开始正式上课，现在先去试听一下。」"
    "试听……试用期么。这个词语不禁让我想起些许往事，感觉浑身不自在。"
    志雄 "「当然，高中最后的暑假，也要尽情的享受一下了！」"
    志雄 "「放烟花，去海边，爬山……想做的事有很多。」"
    "为了掩盖内心阴郁的氛围，我故作开朗的说道。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB02"),"True","img/YU_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU016"
    结乃 "「说的也是，我会和你一起去的。」"
    "或许是察觉到了我情绪的变化，结乃回答我时露出了欢快的表情。"
    "她向来善于察言观色，能敏感的注意到别人的难言之隐。"
    "当然，结乃的应和让我心中宽慰了不少，不过，或许也正是因为这个原因，我们的关系才裹足不前。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA06"),"True","img/YU_LAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU017"
    结乃 "「外宿旅行之类的怎么样？」"
    志雄 "「哈？」"
    "面对突如其然的大胆提议，我一时语塞。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA01"),"True","img/YU_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    if not persistent.dictlist[8] and persistent.show_dict:
        $persistent.dictlist[8]=True
        show screen dict_pop(i=8)
    voice "NYU01A_YU018"
    结乃 "「稻穗先生不是说在温泉旅馆打工么？」"
    志雄 "「啊，啊啊。说起来好像……」"
    voice "NYU01A_YU019"
    结乃 "「他说如果去的话，能给我们友情价格哦？」"
    志雄 "「呃，不过一个打工仔没有这种权力的吧。」"
    志雄 "「况且，即使能优惠一些，交通费用等等其他杂项也是一笔不容小视的数目……」"
    "不，等等！"
    "我的槽点好像偏了一些，错过了什么更本质的东西。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB02"),"True","img/YU_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU020"
    结乃 "「啊哈哈哈～明白啦，我只是说说而已。」"
    "恶作剧般笑着的结乃。"
    "自从我俩关系变亲密后，原来只会偶尔看到的小恶魔状态，现在几乎是能天天体会了。"
    "这也是我喜欢结乃的一个原因，虽然很多次我只是一笑置之。"
    志雄 "（原来只是个玩笑啊！）"
    "不过这次扑通扑通雀跃起来的心情被华丽的浪费掉了。"
    "但是，如果有钱的话……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU021"
    结乃 "「像学生这样的，不需要钱的约会就足够了吧。」"
    "……心里所想的事情又一次被微妙地读取了，心中的阴郁竟在一点点扩张，是我的错觉吗？"
    "究竟是怎么回事，这种失落感。"
    voice "NYU01A_YU022"
    结乃 "「这是能和身为高中生学长度过的最后一个夏天，所以让我们一起去创造更多的美妙回忆吧。愿望很多，但是哪怕最后只有一个能实现也好。」"
    志雄 "「嗯，为了这些美妙的愿望，我们得先把这些文件……」"
    "我看着眼前堆积如山的文件叹了口气。"
    "按照现在的情形，搞不好到暑假也还会被学生会的各种琐事所困扰。"
    志雄 "「能面不改色解决掉这些问题的克罗艾学姐有多伟大啊，终于体会到了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA02"),"True","img/YU_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU023"
    结乃 "「喂～有空说这种话不如好好工作哦，学姐可从来没有半点怨言。」"
    志雄 "「真是没办法，加油吧。」"
    "我重新打起精神，拿起手边的一份文件。"
    志雄 "「啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA01"),"True","img/YU_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU024"
    结乃 "「怎么了？」"
    "视线刚接触到文件的瞬间，整个身体就不自觉地挺了起来，难怪引起了结乃的不解。"
    志雄 "「没事，也对，已经到了必须做准备的时候了。」"
    voice "NYU01A_YU025"
    结乃 "「啊，奏云祭的……」"
    志雄 "「嗯。」"
    "那是仍然处于白纸阶段的奏云祭运营计划书模版。"
    voice "NYU01A_YU026"
    结乃 "「已经，过去一年了呢。」"
    志雄 "「嗯，就像眨眼之间的事。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB06"),"True","img/YU_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU027"
    结乃 "「真的吗？感觉已经是很久很久之前的事了……」"
    志雄 "「呃，可能高一和高二的时间观念不太一样吧。」"
    "更何况结乃是转校生。"
    "我们所感到的时间密度完全不在一个层次上了吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU028"
    结乃 "「不过，我很清楚地记得每一件事。」"
    voice "NYU01A_YU029"
    结乃 "「我敢保证，不管３年也好，５年也好……不，即使再过１０年，也忘不了。」"
    志雄 "「那是当然的啦。」"
    "通过奏云祭的准备，对结乃产生好感的那个秋天所发生的事，像走马观花一样，在脑海中重现。"
    "在大家永远无法忘怀的那场奏云祭的１年后。"
    "我们要再一次，酝酿那个属于秋天的故事。"
    志雄 "「今年结乃的班级打算出什么节目呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA01"),"True","img/YU_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU030"
    结乃 "「我这边有广播室的工作，班级那边似乎也被安排当作奏云祭的休息室了。」"
    "去年奏云祭后，热爱广播的结乃顺利地成为了校园广播的播音员。"
    "和戏剧部一起进行广播剧本创作，或者进行ＤＪ风格的午间广播……"
    "同时，她还兼任学生会成员，精力旺盛到让人佩服。"
    志雄 "「原来如此，舞台剧的话，的确也没办法一个人进行。」"
    "如果没有全班的配合，是不可能做到的。"
    "从这个意义上说，结乃去年所创作的剧本能获得奏云祭最佳节目的荣誉，真的是多亏了她的伙伴们。"
    志雄 "「我还想看到续集的……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA01"),"True","img/YU_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU031"
    结乃 "「不要那么失望啦，明年还有机会的。」"
    "结乃一副毫不在意的样子。"
    "但也许是不擅长说谎，过于刻意的脸部动作反倒暴露出她内心真实的想法。"
    voice "NYU01A_YU032"
    结乃 "「不过，今年就算了，学生会可比去年忙多了……」"
    voice "NYU01A_YU033"
    结乃 "「能和学长一起逛奏云祭，也只有这最后一次机会了呢。」"
    "虽然在微笑，却隐约可见表情深处的沉重。"
    "不过也确实，半年之后，高中毕业的我就要与结乃分道扬镳了。"
    "虽然看似很遥远，可是白驹过隙，半年的时光就在那里，留也留不住。"
    志雄 "「是啊，今年也一起巡视吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU034"
    结乃 "「当然，只有这个工作我不想让给其他干事！」"
    志雄 "「哈哈哈……这么麻烦的工作，除了我们以外也没有人想主动接手吧，不用担心。」"
    "因为这件麻烦的工作，才和结乃变得如此亲密，所以这也是我不想让给任何人的工作。"
    voice "NYU01A_YU035"
    结乃 "「为了不重蹈去年的覆辙，现在不好好做计划书可不行哦。」"
    志雄 "「嗯，那是必须的。」"
    "以防万一，我们也制定了应对突发事件的应急预案。"
    "如果现在偷懒，则意味着我和结乃在奏云祭时，将浪费更多的私人时间来处理因为疏忽而造成的麻烦。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA05"),"True","img/YU_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    if not persistent.dictlist[65] and persistent.show_dict:
        $persistent.dictlist[65]=True
        show screen dict_pop(i=65)
#DICT_FLG 61
    voice "NYU01A_YU036"
    结乃 "「那么，抓紧时间工作吧。不然不能赶在『Ｔ－ｗａｖｅ』开始前到家的话……」"
    "结乃不知道什么时候已经完成了自己预定的工作，说话间，又从我面前的文件中抽走了一些。"
    结乃 "「……」"
#MESEX_A M_NOA,A_CH_YU,NYU01A_YU037,"【結乃】「……」%K%P"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "聚精会神地看着文件，默不作声的结乃。"
    "我看着她认真的侧脸，心里有着一种说不出的安详，不知不觉地也加快了工作的速度。"
    "放学后的时间就这么过去了……"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
    pause (32/32.0)
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG09NA@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA04"),"True","img/YU_LAA04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play music "BGM10"
#FADE_IN 1
    志雄 "「还没结束吗？」"
    "我看着桌子上厚度依然感人的文件，叹了口气。"
    "感觉工作量远远超出了预期。"
    voice "NYU01A_YU038"
    结乃 "「好像快要完成的样子……」"
    志雄 "「是，是吗？」"
    "不知道她是为了安慰我而故作镇定，还是真的有用不完的精力。"
    "既然结乃这么说了，大概今天就真的能完成吧。"
    志雄 "「明明已经到了『Ｔ－ｗａｖｅ』开始的时间了。一直拖到现在还不能回去，真是抱歉。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA01"),"True","img/YU_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU039"
    结乃 "「没关系的，回不去的话，就在这里和学长一起听好了。」"
    志雄 "「说的也是。」"
    "我把抽屉里放着的，毫无时代感的古老收音机插上电源。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    show expression "img/OIBG009A@2x.png" as bg1 zorder 10 with dissolve
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
    if not persistent.dictlist[64] and persistent.show_dict:
        $persistent.dictlist[64]=True
        show screen dict_pop(i=64)
    "这是矿石收音机，在日常生活中几乎已经绝迹的古董。"
    "虽然曾经因为可以亲自动手制作而倍受欢迎，可因为只能接收到大发射功率的频道而逐渐被人们遗忘……"
    "而这个收音机经过改造，现在也能收听一般的地方电台节目了。"
    if not persistent.dictlist[18] and persistent.show_dict:
        $persistent.dictlist[18]=True
        show screen dict_pop(i=18)
    "帮忙改造的是结乃的挚友，一个名叫秋津神奈的女生。"
    "而修复结乃与神奈之间的裂痕，让两人重新拾起友谊的也正是这个矿石收音机。"
    window hide
    hide bg1 with dissolve
    志雄 "「最近神奈的状态超好啊，投稿几乎每天都有被ＫＡＮＡＴＡ读到。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA04"),"True","img/YU_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU040"
    结乃 "「第一代『凯尔玛妹妹』可不是泛泛之辈，我感觉自己一点都不是她的对手呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAC03"),"True","img/YU_LAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU041"
    结乃 "「但是，还是希望她能别总用我和志雄学长的事情作为话题……」"
    "把我和结乃的事情当作晚熟情侣的特例用于投稿，已经变成了『凯尔玛妹妹』的惯例了。"
    "作为稿件中被提及的两个当事人之一，虽然面对的不过是只收音机，但也经常被她的言辞调戏的面红耳赤。"
    志雄 "「既然知道会被拿去当作投稿素材，结乃就不要什么都和神奈说了啊……」"
    "我随口说出了内心的想法。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAC01"),"True","img/YU_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU042"
    结乃 "「可是，会有很多各种各样的事情只有女生之间才能商量的啊。」"
    "虽然在最初一段时间，我非常在意她们之间到底说了些什么……"
    "但因为神奈如此周到的泄密，所谓的女生之间的秘密我也一清二楚了。"
    "就结果而言，结乃对我是什么事也瞒不了。"
    志雄 "「不过，结乃的投稿被选中的次数不也很多么？」"
    "刚认识结乃的时候，她也是以『凯尔玛妹妹』的名字投稿的，而现在则用『淳淳的牛奶』作为昵称。"
    "『凯尔玛妹妹』原本是神奈的笔名。"
    "为了传递自己的想法，结乃就在神奈没有投稿的日子里，延用了『凯尔玛妹妹』这个名字继续投稿。"
    "虽然在神奈复出之后的一小段时间里，『凯尔玛妹妹』是两个人共用的笔名，但大概从今年的春天开始……"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG05AA@2x.jpg" as bg2 zorder 2 with dissolve
#BG_BLUR 2
#BG_INIC 1
#BG_PRI 1
    scene expression "img/BG05AA@2x.jpg" as bg0 with dissolve
#BG_ALPC 0
#BG_ALPC 2
#CHR_ALPC 0
    hide bg1 with dissolve
    voice "NYU01A_YU043_K" 
    结乃 "「想一个人试一试！」"
    window hide
#BG_INIC 1
#BG_PRI 1
    scene expression "img/BG09NA@2x.jpg" as bg0 with dissolve
    hide bg2 with dissolve
#BG_UVC 2,0,0,640,448
#BG_ALPC 0
#CHR_ALPC 0
    hide bg1 with dissolve
    "结乃那么说以后，就突然换成了『淳淳的牛奶』作为投稿笔名了。"
    "从那以后，两人一直在『Ｔ－ｗａｖｅ』上以各自的身份活跃着。"
    志雄 "「已经完全成了最受主播青睐的两位投稿者了吧。」"
    "这个节目的投稿被选中难度之高是有目共睹的。"
    "而将该电台节目长期占领的还是一对好朋友，更是令人叹服。"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,YU_LXB05,3,F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB05"),"True","img/YU_LAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NYU01A_YU044"
    结乃 "「我觉得没有那么厉害啊。只是因为最近其他知名听众都没有出手，嗯，一定是这样的。」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
#BG_PRI 3
    "不知为什么，结乃突然羞涩了起来，连手中的文件也发出不自然的哗哗声。"
    志雄 "（看来，之后那部分文件要重新审查一遍了。）"
    "这种状态的结乃多半是无法集中注意力在工作上了，这点我还是知道的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA01"),"True","img/YU_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU045"
    结乃 "「说起来，学长最近都没怎么投稿呢，对吧？」"
    voice "NYU01A_YU046"
    结乃 "「虽然学生会的琐事和备考生沉重的课业所带来的负担很重，但忙里偷闲写几条稿件也没关系吧？」"
    志雄 "「哈哈哈。对我来说，有你们这样的投稿人作为对手，还是学习比较轻松一点吧。」"
    "实际上我每天连发邮件的时间都没有多少。"
    "要是真的一直投稿的话，对于备考生来说真是一种恐怖的折磨。"
    "所以，就像现在这样，心血来潮的时候写几条就足够了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAC01"),"True","img/YU_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU047"
    结乃 "「我理解的，不过太可惜了。」"
    voice "NYU01A_YU048"
    结乃 "「要是有学长的话，『Ｔ－ｗａｖｅ』就不会像现在这样，只是我和神奈的舞台了。」"
    志雄 "「呃，要是毕业去向确定下来的话，我就会认真的复出了哦。」"
    "记得去年每天都投稿的时候，我被选中的稿件也没有『凯尔玛妹妹』的多，所以，即使全力以赴，也根本不可能是对手吧。"
    "不过偶尔在节目里露一下脸，找回身为ＫＡＮＡＴＡ超级听众的荣誉感也是很不错的。"
    志雄 "「再抓紧点吧，不然就和节目里说的一样，到末班车时间了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA04"),"True","img/YU_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU049"
    结乃 "「对哦，那样的话可就麻烦了。」"
    "由于是学生会成员，我们回家比较晚在一定程度上也是可以理解的。"
    "但是所谓理解，也是有限度的。"
    "一个人独自生活的我暂且不说，身为女孩子的结乃，家里肯定还有父母在担心着。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG90NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression Solid("000") with None
#FADE_IN 0
    if not persistent.dictlist[16] and persistent.show_dict:
        $persistent.dictlist[16]=True
        show screen dict_pop(i=16)
    "不知道是不是听着『Ｔ－ｗａｖｅ』背景音乐的缘故，处理积存文件的速度明显快了许多。"
    voice "NYU01A_YU050"
    结乃 "「啊？诶？没有了！」"
    "总算是把所有的工作完成了，看了时间，离末班车还有一段时间，总算可以松口气了。可是……"
    "一起走出校门时，结乃忽然的一声惨叫告诉我，又得重新返回校舍了。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128
    scene expression "img/BG90NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAC01"),"True","img/YU_LAC01A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
#FADE_IN 1
    voice "NYU01A_YU051"
    结乃 "「对不起，连学长都要陪我回来了。」"
    志雄 "「别说了，总之一起赶快找吧。」"
    "我们折返回来的目的地并不是学生会室，而是广播台。"
    voice "NYU01A_YU052"
    结乃 "「呃……明明最后是放在这里的说……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "制作中的广播剧剧本好像落在了广播台。"
    "虽说陪结乃一起来了不知道多少次了，可我仍然无法习惯这里的布局，能帮到多少忙也就可想而知了。"
    "我与结乃一边小心翼翼地避开各种器材，一边在各处摸索着。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB02"),"True","img/YU_LAB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU053"
    结乃 "「啊！找到了！太好了……」"
    "虽然还没有达到学生会室的程度，但广播台也是各种文件散落一地，相当混乱。"
    "结乃给外人的印象是工作细致准确的同时效率不减，但她却对收拾整理之类的事情并不在意。"
    志雄 "「虽然在你刚安心下来的时候就这么说有点过意不去，但是不得不提醒你，我们的时间不多了……」"
    "我向瘫坐在椅子上的结乃伸出手，用力把她拉起来。"
    志雄 "「目标末班车……抓紧！！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB06"),"True","img/YU_LAB06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU054"
    结乃 "「是、是啊！赶快吧！」"
    "我紧紧的握住结乃的手，从广播室飞跑出去。"
    window hide
#ROUTINE_STA
#CHR_PRIC 0
#BG_LAY 1,BG08NA,1,0,0,640,448
#BG_ALPC 1
#ROUTINE_STP
    play sound "SE00_07"
    pause (8/32.0)
#ROUTINE_STA
    hide lh0 with dissolve
#BG_ALP_AUTOC 1,128,0,1
#ROUTINE_STP
    pause (32/32.0)
#ROUTINE_STA
#BG_SWPC 0
#BG_PRI 0
#BG_PRI 1
    scene expression "img/BG08NA@2x.jpg" as bg0 with dissolve
    hide bg1 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB06"),"True","img/YU_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#ROUTINE_STP
    voice "NYU01A_YU055"
    结乃 "「学长！门……」"
    志雄 "「明天早上第一个来学校就可以了吧！」"
    voice "NYU01A_YU056"
    结乃 "「虽，虽然话是这么说……」"
    window hide
    play sound "SE01_11L"
    "还没来得及锁上广播室的门，在包里翻找钥匙的结乃就被我一把拉走了。"
    "就算锁上门，时间上的损失也不到１分钟。"
    "可现在连那么点时间也必须争取。"
    window hide
    show expression "img/BG83NA@2x.jpg" as bg_over zorder 2 with dissolve
    pause (16/32.0)
    play sound "SE01_10L"
    stop se
    pause (16/32.0)
    show expression "img/BG06NA@2x.jpg" as bg_over zorder 2 with dissolve
    "一口气冲出了学校，直奔车站。"
    志雄 "「时间紧迫啊。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA04"),"True","img/YU_LAA04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU057"
    结乃 "「对不起，要是我没有粗心大意忘了东西的话……」"
    "徒步上学的我怎么晚也没关系，坐电车的结乃就不一样了。"
    "刚才就不应该让她返回学校的，直接让她回家就好了。陪她一起回去广播室造成现在的后果，我也有责任。"
    志雄 "「有空道歉不如再跑快些！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA05"),"True","img/YU_LAA05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU058"
    结乃 "「是！」"
    "连休息一下的空暇也没有，我们在通向车站的夜路上狂奔。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG01NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG01NA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    志雄 "「诶……」"
    "当我看到一个小小的身影跌跌撞撞地从检票口那里走出来的时候，绝望的叹了口气。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAC01"),"True","img/YU_MAC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    play music "OBGM12"
    voice "NYU01A_YU059"
    结乃 "「不行了，明明已经看到电车在那里了，还是没能赶上……」"
    "在最后一刻目送末班车离开的结乃，垂头丧气的走了回来。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    志雄 "「看到有女孩子要上车，稍微通融一下也未尝不可啊……」"
    "我小声向着车站工作人员的方向抱怨着。"
    "工作人员在埋头处理剩下的工作，并没有注意到我那充满怨念的目光。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAC01"),"True","img/YU_LAC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU060"
    结乃 "「对不起，要是我能再跑快些……」"
    志雄 "「没有那回事，结乃作为女孩子已经跑的非常快了。」"
    "以前就曾经感受到结乃那令人惊讶的体能，刚才的一路上，她都是紧跟着全力奔跑的我。"
    "而且一看到车站，就马上超过了体力耗尽的我，出色地完成了到检票口的最后冲刺。"
    志雄 "「比起速度，现在的问题是……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA04"),"True","img/YU_LAA04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU061"
    结乃 "「那现在……应该怎么办？」"
    志雄 "「家里那边……没有问题吗？」"
    voice "NYU01A_YU062"
    结乃 "「那倒没有事，只要说清楚应该能够通融。」"
    志雄 "「真的吗？那真是太好了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA01"),"True","img/YU_LAA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU063"
    结乃 "「结乃平时都是好孩子，所以关键时刻才能得到大家的信任。」"
    "的确，在这一点上，结乃做的无可挑剔。"
    "可是，如果从父母的角度去考虑的话，夜不归宿……就算是信任她，也难免会担心吧。"
    志雄 "「那么，问题就是该在哪里呆到明天了……」"
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    menu:
        "莉莉丝的家":
            $F7=0
        "商业街":
            $F7=1
        "学生会室":
            $F7=2
    if F7==0:
        jump L_NYU01A_SEL00_A
    if F7==1:
        jump L_NYU01A_SEL00_B
    if F7==2:
        jump L_NYU01A_SEL00_C
label L_NYU01A_SEL00_A:
    志雄 "「没办法了，那就拜托那个家伙吧。」"
    voice "NYU01A_YU064"
    结乃 "「远峰学姐吗？」"
    志雄 "「嗯，不管怎么说，那家伙应该不会见死不救吧。」"
    "……虽然之后等着我的肯定是惨无人道的回报，不过现在还是把这种问题搁置一边吧。"
    志雄 "「只是，那个家伙的话……」"
    "从通讯录里找到莉莉丝的号码拨打过去。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE02_02L"
    "１次、２次、３次、４次……"
    志雄 "「果然是这样子……」"
    "看来即使再拨上２０次也不会打通了。"
    play sound "SE02_03"
    "对着不安的看着我的结乃摇了摇头，只好放弃了。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAC01"),"True","img/YU_LAC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    志雄 "「偏偏今天睡这么早……」"
    voice "NYU01A_YU065"
    结乃 "「那怎么办呢……」"
    "莉莉丝一旦睡着的话，被手机铃声吵醒的几率向来为零。"
    "所以，等她看到未接来电的时候已经是第二天早上了，毫无意义。"
    jump L_NYU01A_SEL00_X
label L_NYU01A_SEL00_B:
    志雄 "「应该会有的吧……」"
    "就是这种小镇，能借宿一晚的地方应该也会有很多。"
    "网吧、卡拉ＯＫ、餐厅……一路上看到的也有不少。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA04"),"True","img/YU_LAA04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU066"
    结乃 "「可是校服……还真是麻烦呢。」"
    "正如结乃所说，她身上的衣服是最大的难题。"
    "虽然地方很多，但却不会有接纳未成年人的地方。"
    志雄 "「有没有住在附近的朋友呢？」"
    voice "NYU01A_YU067"
    结乃 "「有是有，不过现在也太晚了……」"
    志雄 "「真是个难题啊……」"
    "这个时间突然去打扰也会给对方带来不便。"
    "那么，只好……"
    jump L_NYU01A_SEL00_X
label L_NYU01A_SEL00_C:
    志雄 "「要么……回学校怎么样？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAC01"),"True","img/YU_LAC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU068"
    结乃 "「那也是个方法，还好，还拿着会议室的钥匙……」"
    "只要躲过守门的老大爷并潜入学校，就能找到过夜的地方。"
    "而且是个可以一直睡到明天第一节课前的特别住所。"
    志雄 "「早知道有这种事情发生，就用学生会的预算买个睡袋了。」"
    voice "NYU01A_YU069"
    结乃 "「虽说如果准许通宵的话，批准这种预算也未尝不可……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA04"),"True","img/YU_LAA04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU070"
    结乃 "「可是，学生会成员做这种事情毕竟不太好吧……」"
    志雄 "「没有办法对其他学生起到模范作用了吗？」"
    "要是被新闻部曝光当了头条的话，可能也会引起不小的负面影响。"
    jump L_NYU01A_SEL00_X
label L_NYU01A_SEL00_X:
    志雄 "「真麻烦啊，其他能去的地方，只有我住的公寓……」"
    stop music fadeout 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB05"),"True","img/YU_LAB05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    结乃 "「……！！」"
#MESEX_A M_NOA,A_CH_YU,NYU01A_YU071,"【結乃】「……！！」%K%P"
    "不经意的一句话，让结乃的脸刷地一下红了。"
    window hide
    play music "BGM13"
    志雄 "「啊，不，那个……我没别的意思……」"
    "察觉到这句话有的问题后，我也手忙脚乱了起来。"
    "明明只是无心之言，可当认识到其中包含的那深层的意思后，便无法冷静了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB03"),"True","img/YU_LAB03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU072"
    结乃 "「可，可是……其它能过夜的地方已经……」"
    志雄 "「诶……？」"
    "真是意料之外的反应。"
    "难道说……结乃其实并不反对？"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG09EA@2x.jpg" as bg2 zorder 20 with dissolve
#BG_BLUR 2
#CHR_ERSTC 1,2,3
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA06"),"True","img/YU_LAA06A@2x.png") as lh1 zorder (30-1):
        ypos 0.0
    with dissolve
#SE_VOLC 1,0
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 0
#BG_ALPC 2
#CHR_ALPC 1
#CHR_ALPC 0
    hide bg1 with dissolve
    voice "NYU01A_YU073_K"
    结乃 "「外宿旅行之类的怎么样？」"
    "我回忆起了在学生会室中，以为是结乃在开玩笑的话。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh1 zorder (30+1):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU074_K"
    结乃 "「这是能和身为高中生学长度过的最后一个夏天，所以让我们一起去创造更多的美妙回忆吧。愿望很多，但是哪怕最后只有一个能实现也好。」"
    "最后的夏天。"
    "回忆……"
    "换作他人，也难免会想到一些失礼的东西吧。"
    window hide
#BG_INIC 1
#BG_PRI 1
    hide bg2 with dissolve
#BG_UVC 2,0,0,640,448
#BG_ALPC 0
    scene expression "img/BG01NA@2x.jpg" as bg0 with dissolve
    hide lh1 with dissolve
#CHR_ALPC 0
#SE_VOLC 1
    hide bg1 with dissolve
    志雄 "「那……没办法了吧。」"
    voice "NYU01A_YU075"
    结乃 "「是的，没办法了」"
    "结乃刻意模仿我的语气答道，想必她现在也很紧张吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU076"
    结乃 "「我要给家里打个电话，伪装一个假象出来，保持安静哦。」"
    志雄 "「呃，呃呃……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NYU01A_YU077"
    结乃 "「啊，喂喂，妈妈。那个，我说……」"
    "已经到了这个时候，就算理由正当，和父母解释起来也会比较费力吧。"
    "铃昨天窜进我家，留下一张写着去泡温泉的便条，就骑着摩托车出去了。"
    "用莉莉丝的话说，她是「逃跑了」吧。"
    "不过这次写着明天就会回来，也有可能是去取材了。"
    voice "NYU01A_YU078"
    结乃 "「嗯。明天一定会早早地回来啦。嗯……明白了，不用担心啦。」"
    "莉莉丝也正在睡觉，所以应该不会有人深夜到访……"
    voice "NYU01A_YU079"
    结乃 "「那么，就这样，我挂了，晚安。」"
    "在我慌慌张张不知所措的时候，结乃镇定的编织着假象。"
    voice "NYU01A_YU080"
    结乃 "「啊，喂喂？对不起啊，这么晚还打扰你……」"
    "和家里通话后，结乃又接着拨了另外一个号码。"
    "实在寻找还没睡的朋友。"
    voice "NYU01A_YU081"
    结乃 "「其实是这样的……」"
    "看来有很多不想我听到的内容，结乃背向着我，小声地对着电话那头窃窃私语。"
    "我木讷地看着这无法理解的浩大工程。"
    voice "NYU01A_YU082"
    结乃 "「变成大人什么的……不是那个意思啦。」"
    voice "NYU01A_YU083"
    结乃 "「没，没有带那种东西啦！都没想到那一层，真是的！」"
    "……脑补了对话内容，连我也不自觉的紧张了起来。"
    "结乃背对着我真是太好了。"
    "当然也要感谢夏夜不常见的微风，感谢它带走我脸庞上不自然的温度。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA02"),"True","img/YU_LAA02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU084"
    结乃 "「好了，看来没有问题了。」"
    志雄 "「是，是吗？」"
    "打完电话的结乃像只小猫一般，附着身子回头看我。"
    "虽然我已经尽力可能的保持冷静，但是紧张的心境依旧被自己的声音出卖了。"
    志雄 "「那么，走吧。对了，换洗衣服之类的要怎么办呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA01"),"True","img/YU_LAA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU085"
    结乃 "「睡衣的话就用学长的衬衣好了。」"
    "我的衬衣……"
    "脑中不禁浮现出结乃只穿着衬衣的样子。"
    voice "NYU01A_YU086"
    结乃 "「但是，牙刷之类的……其他东西不买不行呢，能去一下便利店吗？」"
    志雄 "「明白了，我家旁边的便利店可以吗？」"
    voice "NYU01A_YU087"
    结乃 "「好啊，请带路吧。」"
    "我们离开了车站。"
    "事已至此，已经不能回头了。"
    志雄 "「那么，这边，光线很暗，小心点。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU088"
    结乃 "「明白了。」"
    志雄 "「……！！」"
    "明明……我像平常一样肩并着肩。"
    "可是总感觉结乃和我靠的更近了，两人之间只保持了随时肩膀都有可能相碰的微小距离。"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,YU_LXB05,3,F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB05"),"True","img/YU_LAB05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NYU01A_YU089"
    结乃 "「走，走吧。」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
#BG_PRI 3
    志雄 "「哦，哦！」"
    "在某种意义上说，这是比牵手更让人脸红的状态。"
    "街灯的映照下，我们的影子长长地向后延伸，浓重的黑影好像紧贴着，重合在了一起……"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/BG14NA@2x.jpg" as bg0 with dissolve
    play sound "SE05_16L"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LXB05"),"True","img/YU_LAB05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
#BG_LAY 3,YU_LXB05,3
#FADE_IN 1
    志雄 "「久等了。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB05"),"True","img/YU_LAB05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NYU01A_YU090"
    结乃 "「是，是！」"
#REMOVE_REEK_CHR 0
    "我从便利店里回到结乃等我的地方。"
    志雄 "「似乎没有什么认识的人呢……还是快些买完吧。」"
#REEK_CHR 0
    voice "NYU01A_YU091"
    结乃 "「明白了。我不会买很多东西的，耽误不了太多时间。」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
#BG_PRI 3
    "或许我真的是修行不够吧，竟然会觉得在这个时间和女孩子一起同行是一件影响很不好的事情。"
    "所以我在结乃进去了一会儿后，才溜进了便利店的门。"
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
#FADE_IN 0
    "我站在杂志架前，装作翻看漫画周刊的样子。"
    "实际上是用余光留意着结乃在店里挑选的东西。"
    voice "NYU01A_YU092"
    结乃 "「牙刷还有……洗发露怎么办？反正只有今天，就用学长的吧。」"
    "是因为太注意倾听周围的动静了吗，好像听到了她自言自语。"
    "不过女孩子的洗发露是要和护发素一起用的吧，家里只有洗发露没问题吗？"
    voice "NYU01A_YU093"
    结乃 "「啊……但是一样的洗发露味道会被人误解吧……这也谈不上，但还是会引来不必要的麻烦吧？」"
    "听着结乃的自言自语，我自己倒因为脑中的臆想而脸红了。"
    "虽然感到有些害羞，可是我还是没有放过结乃的只言片语。"
    voice "NYU01A_YU094"
    结乃 "「然，然后是……内衣裤吧。」"
    voice "NYU01A_YU095"
    结乃 "「怎么办……要更可爱的便利店没有啊。」"
    "因为害羞而变得更小的说话声已经听不太清了。"
    "内衣裤的更换当然是必要的，不用说也明白。"
    voice "NYU01A_YU096"
    结乃 "「诶～～明明是这么重要的晚上……」"
    "为什么她要为可不可爱这样的事情思前想后呢。"
    "思考着这个问题，自己的脸不由得又红了。"
    "要是被别人看到我现在的样子，可能会以为我正在看某些少儿不宜的杂志吧。"
    voice "NYU01A_YU097"
    结乃 "「这，这个吧，这个算是最可爱的了……应该会喜欢吧。」"
    "正在偷听的我终于达到了忍耐力的极限。"
    "我像逃跑一样狼狈的冲出便利店，在路边的拐角处等着结乃。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA02"),"True","img/YU_LAA02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    play sound "SE05_16L"
#FADE_IN 1
    志雄 "「没有漏买什么东西吧？」"
    voice "NYU01A_YU098"
    结乃 "「嗯，不过真不好意思，还要你请吃便当……」"
    志雄 "「没关系的，这么晚做饭也实在太累了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA01"),"True","img/YU_LAA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU099"
    结乃 "「学长平时都是自己做饭的吗？」"
    "好像听到了什么令人难以置信的东西是的。"
    "我自己做饭有那么难以想象吗？"
    志雄 "「只有心血来潮的时候哦，基本上都是从便利店买，或者是在莉莉丝婆婆的料理店里解决的。」"
    voice "NYU01A_YU100"
    结乃 "「是那样吗？总觉得松了一口气呢。因为我对做饭不是很擅长……」"
    "看来女孩子对于不擅长做饭这种事真的是很敏感呢。"
    "虽然我并不太在意，可是自己的女朋友能意识到这点还是很欣慰的。"
    "当然，我也期待着有一天，能吃到她亲手做的佳肴。"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,YU_LXB05,3,F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB05"),"True","img/YU_LAB05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NYU01A_YU101"
    结乃 "「这，这地方也挺不错的。」"
#REMOVE_REEK_CHR 0
    if not persistent.dictlist[46] and persistent.show_dict:
        $persistent.dictlist[46]=True
        show screen dict_pop(i=46)
    "走到公寓入口的瞬间，结乃的笑容变得有些紧张。"
    志雄 "（也难怪呢。）"
    "毕竟第一次住男生家里。"
    "要是结乃一副习以为常的样子，不知所措的反而会是我吧。"
    志雄 "「那么，进去吧。像傻子一样站在门口是不行的哦。」"
    "至少我也要推她一把，给她勇气。"
    "我淡定地拍拍结乃的肩膀，向入口踏出了一步，示意她跟上来。"
#REEK_CHR 0
    voice "NYU01A_YU102"
    结乃 "「是，是的，请多多指教。」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
#BG_PRI 3
    "虽然肩膀颤抖了一下，可结乃并没有抗拒，跟着我走进了公寓大门。"
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
#MUS_WAT 
    pause (32/32.0)
    "原来如此……"
    "我和结乃，早就应该更积极一些了。"
    window hide
    play sound "SE06_31"
    志雄 "「啊……」"
    "要是刚才没有犹豫的话，就不会有现在的麻烦了。"
    voice "NYU01A_SU000"
    铃？ "「啊哈？怎么了，才一天没见……」"
    "那人从摩托车上下来，脱下头盔，原来是铃。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MCA01"),"True","img/SU_MCA01A@2x.png") as lh10 zorder (10-10):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAC01"),"True","img/YU_MAC01A@2x.png") as lh11 zorder (10-1):
        xcenter .75
    play sound "SE03_90"
    play music "BGM05"
    "她边整理着被风吹乱的头发，边走到我面前。"
    "我想起了昨天那张便条，她应该是明晚才回来才对……"
    志雄 "「不是去旅行了吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MCB01"),"True","img/SU_MCB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_SU001"
    铃 "「因为旅馆的饭菜太难吃，就提前一天回来了。」"
    "虽然这很符合铃的风格，但是我还是从心底诅咒着那个旅馆的厨师。"
    "总之，事后一定要弄清旅馆的名字，然后把它列入今后旅行的黑名单。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MCC01"),"True","img/SU_MCC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_SU002"
    铃 "「不过，看来提前回来真是太明智了，这里可不是那种地方哦？」"
    voice "NYU01A_YU103"
    结乃 "「哪，哪种地方……」"
    voice "NYU01A_SU003"
    铃 "「那么，可别告诉我说，结乃你没有那种期待哦。」"
#CHR_GET_POSC 1,F24,F25
#RSUB F24
#BG_LAY 3,YU_MXB05,3,F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB05"),"True","img/YU_MAB05A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
#REEK_CHR 1
    voice "NYU01A_YU104"
    结乃 "「期，期待什么的……那种事情……」"
#REMOVE_REEK_CHR 1
    hide bg3 with dissolve
#BG_PRI 3
    志雄 "「结乃别说话。」"
    "我制止了脸红红的正要否定的结乃。"
    "眼前的人不管怎么说也是『不靠谱的』稻穗信的亲姐姐。"
    "因为害羞而无法冷静思考的结乃被抓到话柄的话就麻烦了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAC01"),"True","img/YU_MAC01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    志雄 "「因为学生会的活动，错过了末班车。所以就近来我家而已。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MCB01"),"True","img/SU_MCB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_SU004"
    铃 "「哦～原来那女孩也是学生会成员啊，居然带头进行不纯异性交往，澄空也变了啊。」"
    "虽然脸上还是一本正经，但眼中已经流露出了笑意。"
    "她在戏弄我们，这点再清楚不过了。"
    志雄 "「不会那样做哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MCB03"),"True","img/SU_MCB03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NYU01A_SU005"
    铃 "「是吗，看来又捉弄失败了，真是个称职的骑士呢。」"
#REMOVE_REEK_CHR 0
    "铃眯着眼睛撇向我。"
    "那简直就是，看到长大的弟弟已经可以自立了的欣喜目光。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MCC03"),"True","img/SU_MCC03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_SU006"
    铃 "「只是，既然发现了，那么作为志雄的监护人，没理由睁一只眼闭一只眼。」"
    志雄 "「监护人……是那样吗？」"
    "大半个月不在家，总是骑着摩托车在日本到处飚车的人没有资格当监护人吧。"
    志雄 "「可是，她已经回不去了啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MCA01"),"True","img/SU_MCA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_SU007"
    铃 "「……跨区入学，不是那样的吧？」"
    "铃看着结乃，放佛在用眼神拷问她。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAC05"),"True","img/YU_MAC05A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU105"
    结乃 "「是的，我家在浜咲，坐电车的话有五站那么远……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MCB01"),"True","img/SU_MCB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_SU008"
    铃 "「原来如此，那么，我的这个是什么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAC01"),"True","img/YU_MAC01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU106"
    结乃 "「诶？」"
    "摩托车的话，的确是在这个时间也能把结乃送到家。"
    "所以我们看似合理的理由已经荡然无存。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MCC02"),"True","img/SU_MCC02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_SU009"
    铃 "「虽然我也没想像ＰＴＡ（家长教师会）里的那些大妈一样和你纠缠……」"
    voice "NYU01A_SU010"
    铃 "「但这种时候不好好计划的话，之后肯定会因为事情败露而引来一大堆麻烦。」"
    志雄 "「这、呃……」"
    "到底是在阻止我们，还是在怂恿我们啊。"
    "实在是看不透她的想法。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MCA01"),"True","img/SU_MCA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_SU011"
    铃 "「所以，今天我送你回去，坐到后面来吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB06"),"True","img/YU_MAB06A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NYU01A_YU107"
    结乃 "「啊？」"
    window hide
    hide lh1 with dissolve
    "铃不由分说的取出备用头盔戴在了结乃的头上。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MCB01"),"True","img/SU_MCB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU01A_SU012"
    铃 "「没意见吧？」"
    志雄 "「嗯……」"
    "事情的好坏先不说，铃的确一直占着理。"
    "在这里争吵的话只会给结乃留下不好的印象，我唯有选择沉默。"
    voice "NYU01A_YU108"
    结乃 "「学长……」"
    "结乃略带悲伤地看着我，然后似乎接受了现实，向我用力地点了点头，坐上了摩托。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NYU01A_YU109"
    结乃 "「拜托你了。」"
    voice "NYU01A_SU013"
    铃 "「嗯？难道说，你……」"
    "看着搂着自己腰的结乃，铃浮现出倍感意外的表情。"
    voice "NYU01A_YU110"
    结乃 "「怎么了吗？」"
    voice "NYU01A_SU014"
    铃 "「不，没什么，那么，出发了哦。」"
    voice "NYU01A_SU015"
    铃 "「速度很快，请牢牢抓紧！」"
    window hide
    play sound "SE06_12"
    play sound "SE06_13L"
    voice "NYU01A_YU111"
    结乃 "「哇啊啊啊！」"
    "连前轮都要腾空般的凶猛加速，结乃死死的抓住了铃的腰。"
    志雄 "「铃！安全驾驶！结乃很胆小的……」"
    voice "NYU01A_SU016"
    铃 "「没关系的！对吧？结乃妹妹！」"
    voice "NYU01A_YU112"
    结乃 "「嗯，是的！」"
    window hide
    play sound "SE06_15L"
    pause (32/32.0)
    stop se fadeout 1
    stop music fadeout 1
    "无视我的忠告，铃的摩托眨眼间就飚出去老远。"
    voice "NYU01A_YU113"
    结乃 "「哇啊啊啊啊！」"
    "空气中只留下了结乃的惨叫。"
    志雄 "「结乃……」"
    "不知怎么竟然有些开心。"
    "说起来，结乃好像说过她喜欢刺激的游戏设施，那样的话，或许能承受住铃那乱来的驾驶方式吧。"
    志雄 "「自称监护人的人却毫无顾忌的超速驾驶呢……」"
    "我苦笑着，拿着两人份的便当走进公寓。"
    "就算饿到这么晚了……一个人吃这分量，也太多了吧。"
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
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT
