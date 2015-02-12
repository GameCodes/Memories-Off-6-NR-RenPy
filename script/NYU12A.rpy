label NYU12A:
    $currentlabel = "NYU12A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '30'
    $date = '0'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 3,CAL_0730
    scene expression Solid("000") with fade
    show expression "img/NIMG15F-568h@2x.jpg" as cal zorder 5
    show expression "img/07_30_SUNDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG15AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG15AA@2x.jpg" as bg0 with dissolve
    play music  "OBGM27"
#FADE_IN 1
    play sound "SE02_02L"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "距离广播比赛已经没有多少时间了。"
    "尽管如此，节目仍然处于连内容都没有规划的状态。"
    志雄 "「总之，把我和结乃的企划再对比一次看看吧。」"
    "目前，我和结乃在节目的定性上互不相让……还是还是双方先都冷静下来吧。"
    "因为节目未能完成，而无法参赛……一定要避免这种最坏的结果。"
    "这样下去的话，创造回忆的计划将完全成为泡影。"
    "但是……"
    play sound "SE02_03"
    "面对持续无人接听的手机，我只能无奈地叹了一口气。"
    志雄 "「没办法……联络不上。」"
    "从早上就不停的打电话给结乃，但她一次也没有接。"
    "发出去的短信和语音留言，也不知道她看了没有。"
    "连这一点都无法确认，我的心情也渐渐急躁起来。"
    志雄 "「没办法。只能直接去结乃的家里看看了。」"
    "幸好我还是知道她家的地址的，结乃的母亲也曾多次邀请我去玩。"
    "不过实际上一次也没去过……"
    "第一次上门拜访就是为了这种事情……虽然我也不愿意这样，但是这也是没有办法的办法了吧。"
    window hide
    play sound "SE02_00L"
    "就在这时，我紧握在手中的手机响了。"
    志雄 "「莫非是结乃？」"
    "但是，显示屏上显示出的是另一个令人意外的名字。"
    "不过对方也是让我无法无视的人，所以我一边做着出门准备，一边按下通话键。"
    play sound "SE02_03"
    志雄 "「喂？」"
    voice "NYU12A_KA000_K"
    神奈 "「太好了。这边打通了。」"
    "电话那边传来安心的声音，紧接着长舒了一口气。"
    "我很快明白了对方之所以不安的原因。"
    voice "NYU12A_KA001_K"
    神奈 "「结乃也在一起吧？不好意思，能让她听一下吗？」"
    志雄 "「果然如此啊……很可惜，我们不在一起。」"
    "面对神奈意料之中的要求，我只能深深地叹息。"
    志雄 "「从今天早上开始就联络不上了，我也一直在找她。」"
    voice "NYU12A_KA002_K"
    神奈 "「这样吗……看来，结乃一定是想一个人静一下吧。」"
    "电话那头，神奈的回答显得很平静。"
    "平静的声音，也让我心中的不安稍稍减退。"
    voice "NYU12A_KA003_K"
    神奈 "「但是，真可惜。本想给结乃一个惊喜，才默不作声地跑来玩的……」"
    志雄 "「什么？　已经到这里了？」"
    "没有任何前兆，就连说这句话的声音也是极度平静。"
    "虽然神奈的行动一直出人意料，但怎么说这也太突然了。"
    voice "NYU12A_KA004_K"
    神奈 "「嗯。现在就在结乃家门前。不过谁都不在。」"
    志雄 "「这样啊……如果没有事先说好的话，碰到这种事也束手无策了吧。」"
    "如果知道神奈会来的话，不管怎么样，结乃都会等她的吧。"
    "那样的话，我也能做些欢迎的准备了。"
    志雄 "（不过，果然也不在家啊……）"
    "虽然省去了去结乃家的时间，但现在的情况似乎更棘手了。"
    "如果是在学校里的话那还好说，如果出门了的话，在手机不通的情况下，能够找到的可能性微乎其微。"
    voice "NYU12A_KA005_K"
    神奈 "「对了。既然都这样了，不如我们一起去找她？」"
    "电话那头神奈提议道。"
    "我没有拒绝的理由。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG01AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG01AA@2x.jpg" as bg0 with dissolve
    play sound "SE08_01"
#EFF_STAC 1,SUN_LE,EFF_SKIP
#FADE_IN 1
    play sound "SE05_15L"
    "我们简单交流了一下结乃最有可能在的地方后……"
    "最终决定在离澄空学园最近的车站汇合。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「真不好意思。要是我能够联络到结乃就好了……」"
    voice "NYU12A_KA006"
    神奈 "「不要紧。本来也要顺便看看志雄的，对我来说完全没影响的。」"
    志雄 "「原来我是顺便啊……」"
    "相比没有联络就能直接去结乃家，在神奈的心里，结乃的优先度必然是远远高于我的。"
    voice "NYU12A_KA007"
    神奈 "「别在意别在意。能联络上你太好了，要是我一个人的话，一定也找不到结乃。」"
    志雄 "「不会吧。结乃的行动规律，神奈要比我把握的更好吧？」"
    "对我来说，神奈就好像是突然出现的救世主一般。"
    "但是，救世主却摇着头，郑重地说道。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA05"),"True","img/KA_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA008"
    神奈 "「搬家到这里之后的结乃，我并不能说完全了解。现在只能靠志雄。」"
    志雄 "「这……样啊。」"
    "的确，不管神奈和结乃之间的羁绊有多深……"
    "但这１年间，一直陪在结乃身边的人，毫无疑问是我。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA009"
    神奈 "「所以，你应该更加有自信些，不是吗？」"
    "面对神奈的鼓励，我努力地还以笑容。"
    "心里其实已经感动地快要哭出来了。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1
#EFF_STPC 1,EFF_SKIP
    scene expression Solid("000") with fade
    show expression "img/BG06AA@2x.jpg" as bg0 zorder 0 with dissolve
    pause (16/32.0)
    play sound "SE05_14L"
#FADE_IN 1
    pause (32/32.0)
    show expression "img/BG10AA@2x.jpg" as bg0 with dissolve
    play sound "SE01_11L"
    stop se
    pause (32/32.0)
    show expression "img/BG83AA@2x.jpg" as bg0 with dissolve
    play sound "SE01_11L"
    stop se
    pause (32/32.0)
    show expression "img/BG08AA@2x.jpg" as bg0 with dissolve
    play sound "SE01_11L"
    stop se
    pause (32/32.0)
    show expression "img/BG07AA1@2x.jpg" as bg0 with dissolve
    stop se
    pause (32/32.0)
    show expression "img/BG09AA@2x.jpg" as bg0 with dissolve
    play sound "SE01_11L"
    stop se
    pause (32/32.0)
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG36AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG36AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    "在澄空学园各处找了一圈，结果还是没能找到结乃……"
    "之后，又找了一些地方，累了很久却依然毫无收获的我们决定先到酪萨克吃点东西。"
    window hide
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA01"),"True","img/KA_XAA01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    志雄 "「对不起。带着你到处走。结果却没能找到……」"
    voice "NYU12A_KA009A"
    神奈 "「没事没事。能在志雄你们的学校里看看也是机会难得哦。」"
    "因为不是本校学生，我本想让神奈在外面等一下的，结果却被坚决地拒绝了。"
    "『总有办法的。』"
    "就凭这一句话，神奈强行穿着私服进了学校。"
    志雄 "「不过……居然谁都没有说你呢。」"
    voice "NYU12A_KA010"
    神奈 "「因为志雄是学生会会长。我能进来，别人都以为是有什么理由的吧。」"
    "和做贼心虚的我相比，神奈则大大方方的在学校里走动着。"
    "或许也是因为暑假里学校里没有什么老师值班，直到最后，我们也没有遭到任何讯问……"
    "结果，我们就这么在学校里搜索，直到放学。"
    志雄 "「这么找都没能找到的话……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA04"),"True","img/KA_XAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA011"
    神奈 "「应该不在学校里吧……或许是去闲逛了吧。」"
    "那样的话，就真的没有办法了。"
    "在寻找的同时，也不停的打着结乃的手机和家里电话，仍然一次也没有接通过。"
    voice "NYU12A_MA000"
    麻寻 "「啊……欢迎。」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA01"),"True","img/MH_LCA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    志雄 "「晚上好。」"
    "拿来菜单的是麻寻。"
    "不过，今天她显得没有平时那么活泼。"
    志雄 "「对了，今天结乃来过这里吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA04"),"True","img/MH_LCA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU12A_MA001"
    麻寻 "「结、结乃？　我不知道哦？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LBB03"),"True","img/MH_LBB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU12A_MA002"
    麻寻 "「今天怎么不在一起啊？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LBB01"),"True","img/MH_LBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU12A_MA003"
    麻寻 "「啊，说起来，你带着别的女孩子！」"
    "直到现在她才注意到神奈的存在。"
    "很明显有问题。"
    voice "NYU12A_KA012"
    神奈 "「你好。我是结乃的朋友，是我让志雄帮我一起找结乃的哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA04"),"True","img/MH_LCA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU12A_MA004"
    麻寻 "「诶？　这样……」"
    voice "NYU12A_KA013"
    神奈 "「嗯。如果碰到结乃的话，能否对她转达一声，就说神奈在找她，好吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LBB01"),"True","img/MH_LBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU12A_MA005"
    麻寻 "「知、知道了。神奈对吧。啊，对不起。今天我其实是主要负责厨房的。」"
    voice "NYU12A_MA006"
    麻寻 "「所以不能在这里说太久。请先慢用吧。」"
    window hide
    hide lh1 with dissolve
    "留下了这么一句话，麻寻快步向着厨房走去。"
    "完全不像那个一直说些有的没的，还经常乱插话的麻寻。"
    志雄 "「店里看起来并不是很忙的样子啊……」"
    "店里完全没有忙到需要负责厨房的店员出来招呼客人的程度。"
    "而且，对于神奈，她居然没有表示出任何兴趣，这点也十分反常。"
    voice "NYU12A_MA007_K"
    麻寻 "「发现了！　这就是传说中的禁断的三角关系！」"
    "我所知的麻寻，应该是像这样双眼闪着光芒对于八卦话题紧追着不放才对。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA04"),"True","img/KA_XAA04A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NYU12A_KA014"
    神奈 "「那个人……应该知道些什么。」"
    志雄 "「神奈也这么想？」"
    "连第一次碰面的人都无法瞒过的演技。"
    "以前麻寻好像参与过电影制作，不过，现在看来，一定不是作为演员。"
    志雄 "「如果死缠烂打的话，我觉得一定会露馅的，不过……」"
    voice "NYU12A_KA015"
    神奈 "「她本人应该也意识到了这点，所以才早早说完逃走吧。」"
    志雄 "「与其说自己意识到……不如说是结乃这么指挥她的吧。」"
    "麻寻的弱点，结乃可是早就牢牢掌握了。"
    "就算神奈的出现是一个意外，但对付我的应对措施还是准备过的……大概就是这么一回事了。"
    志雄 "「没办法。现在只能来点强硬的手段了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA01"),"True","img/KA_XAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA016"
    神奈 "「还是别这样比较好哦。那个人也只是被牵连进来的嘛。」"
    "我站起身来，准备追上麻寻，却被神奈一把抓住了手。"
    voice "NYU12A_KA017"
    神奈 "「而且……估计她也不知道结乃的所在地。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA04"),"True","img/KA_XAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA018"
    神奈 "「就算知道，估计等我们过去，结乃也会先接到联络更换地方了吧。」"
    志雄 "「的确是这样……」"
    "这样的话，麻寻现在对我们隐瞒的很可能是别的事情。"
    "她知道我们两人现在这种微妙的关系吗……"
    "我们正在参加广播比赛这件事情是知道的。"
    "所以，很可能是和这个相关的事情。"
    志雄 "「那样的话，岂不是更应该去问个究竟了嘛……」"
    voice "NYU12A_KA019"
    神奈 "「除了结乃所在地之外，估计啥都不会说哦。」"
    "事情越是重大，口风也就越紧吧。"
    "对于正在打工中的麻寻，也没办法过分地逼问。如此一来，线索搜寻就更加困难了。"
    voice "NYU12A_KA020"
    神奈 "「相比之下，现在有着更加严重的问题哦。」"
    "从刚才开始，神奈就时不时地把电话贴近耳边。"
    voice "NYU12A_KA021"
    神奈 "「那个……结乃的父母，也还没回家。」"
    "看来并不是打给结乃的电话，而是往她家里打的。"
    "春日家的人如果回来了的话，一定会因为海量的电话留言而大吃一惊吧。"
    志雄 "「会不会是全家一起出门了？」"
    voice "NYU12A_KA022"
    神奈 "「有可能。可能本来只是父母预定出去，结果因为和志雄之间闹得不愉快了，于是一起出去了之类的。」"
    "在学校里寻找结乃的时候，我告诉了神奈一些用电话难以说清的，我们两人这几天的情况。"
    "倾听过程中时而愕然，时而真心的为我们担心，有时又对我鼓励打气的神奈，已经不是这件事情的无关者了。"
    voice "NYU12A_KA023"
    神奈 "「现在已经很晚了哦。可能是全家出游之类的，今天都不回来了也说不定……」"
    志雄 "「的确有那个可能性……」"
    "明明已经没有时间了，今天还完全联络不上更是雪上加霜。"
    "看现在的情况，或许连参加比赛都要被迫放弃了。"
    voice "NYU12A_KA024"
    神奈 "「如果真的就这么不回来了，我可是非——常的困扰哦。」"
    stop music fadeout 132
    志雄 "「难道，你不会是想说……本打算今晚在结乃家过夜的吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA02"),"True","img/KA_XAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA025"
    神奈 "「完全正确！你果然了解我！」"
    志雄 "「居然真是这样……」"
    window hide
    play music  "BGM10"
    "神奈并没有向我或者结乃之中的任何一人通知过她要过来这件事情。"
    "也就是说，结乃的父母也自然没有通知过吧。"
    志雄 "「不管怎么说你这都太没有计划性了吧……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA03"),"True","img/KA_XAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA026"
    神奈 "「啊哈哈哈。因为是突然想出来的方案嘛。想到了就立即行动是我的一贯作风嘛。」"
    "看着若无其事地大笑着的神奈，我觉得自己好像忽略了什么重要的事情。"
    志雄 "（莫非……）"
    "很有可能是因为最近我和结乃都和神奈谈了很多关于比赛，以及两人之间僵硬气氛的事情。"
    "所以她……可能比我们两个都要了解我们之间的状态。"
    "作为结乃的密友，神奈一定是坐不住了。"
    志雄 "（或许真的是……飞奔出来的呢。）"
    "如果真是那样，我也有责任。"
    "我也没有什么资格去责怪神奈的鲁莽。"
    志雄 "「真是没办法呢。那就跟你一起去找一下，旅馆，或者网吧之类……能够住到明早的地方吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA01"),"True","img/KA_XAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA027"
    神奈 "「很可惜，那也不行。」"
    "神奈不知为何，很得意地将自己的钱包打开了给我看。"
    "存放纸币的位置……只有有两张１０００日元的纸币。"
    志雄 "「这些是……全部财产？」"
    voice "NYU12A_KA028"
    神奈 "「嗯。因为之前已经买了回去的车票了哦。」"
    "去一个无法当天返回的地方，只带这点钱实在是略显寒酸了。"
    "虽说回去的手段已经确保了，但还是遭遇了最坏的情况，今天还是需要在这里过夜的。"
    志雄 "「没办法呢。先借你一些钱吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA04"),"True","img/KA_XAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA029"
    神奈 "「我可是不借钱主义者哦。」"
    志雄 "「现在已经不是在意这种事的时候了吧……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA08"),"True","img/KA_XAA08A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA030"
    神奈 "「但是！　我在结乃转校前借给她的５０００日元被赖账到现在了啊！」"
    "……结乃还真是留下了难办的『历史遗留问题』啊。"
    "不过，应该是转学的冲击过大，导致无法顾及这些事情了……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA01"),"True","img/KA_XAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA031"
    神奈 "「嗯，就是这样。所以拜托你了。」"
    志雄 "「真没办法。说说看吧。」"
    "接下来会是什么提议呢。"
    "带着不安和好奇，我等待着神奈的回答。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA02"),"True","img/KA_XAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA032"
    神奈 "「让我住志雄的公寓吧！」"
    志雄 "「真没办法……法，才怪！」"
    "不自觉回答出的口癖，刚出口就被自己驳回了。"
    "这件事实在是不能简单就能承诺的啊。"
    志雄 "「那个，神奈？我也算是有结乃这个女朋友的……」"
    "这里就应该摆出年长男性的姿态，冷静地尝试说服才行。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA05"),"True","img/KA_XAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA033"
    神奈 "「果然是这个结果啊。没办法了。只能使出最终必杀技……」"
    "神奈取出了手机，不知往什么地方发送了一条短信。"
    志雄 "「什么嘛。还有什么办法的话早说嘛。」"
    voice "NYU12A_KA034"
    神奈 "「本来不想用这手的。附近有个网友……叫ｌｉｅｓｈｉｎ的。」"
    志雄 "「网、网上！？这样的话，岂不是连面都没见过嘛……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA01"),"True","img/KA_XAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA035"
    神奈 "「嗯。跟他说起过有朋友住在这里，于是他就告诉我他也住这里，就连住所也告诉我了哦。」"
    voice "NYU12A_KA036"
    神奈 "「还邀请我如果有机会过来的话，也去拜访一下他……」"
    志雄 "「那个……神奈？」"
    志雄 "「怎么看这都是别有用心的邀请啊……」"
    "不过在这之前，在见都没见过的人那里过夜这种事情……"
    "这次真的不得不怀疑一下神奈的钝感了。"
    voice "NYU12A_KA037"
    神奈 "「啊——不要紧的。那人现在因为去了某处的温泉旅馆打工，所以现在家中没人。」"
    志雄 "「嗯……？」"
    "怎么觉得好像这事情在什么地方听到过。"
    "而且，笔名是……ｌｉｅｓｈｉｎ？"
    志雄 "「那个。既然知道住所，那应该连真名也知道吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA07"),"True","img/KA_XAA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    stop music fadeout 132
    voice "NYU12A_KA038"
    神奈 "「嗯。好像是叫……稻穗……嗯？名字是啥来着。」"
    志雄 "「不行不行不行不行的！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA10"),"True","img/KA_XAA10A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA039"
    神奈 "「嗯？你们认识？那么，不就更加没有问题了嘛？」"
    志雄 "「就是因为认识所以才说不行的！」"
    window hide
    play music  "OBGM25"
    "本来，在网上认识的人的家里过夜这种事已经是很有问题了……"
    "再加上，对方还是那个稻穗？"
    "我是绝对不可能同意的。就算只大一岁，这也是我作为学长的责任。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA07"),"True","img/KA_XAA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA040"
    神奈 "「志雄，先冷静一下。现在，稻穗不是不在嘛？」"
    志雄 "「啊……」"
    "稻穗现在正在很远的温泉旅馆里长住打工中，是没办法回到公寓中来的。"
    志雄 "「这种事情你都知道了啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA01"),"True","img/KA_XAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA041"
    神奈 "「嗯。果然上了网就变成大嘴巴的人也是存在的呢。」"
    "那个人平时也是个大嘴巴吧，不过这个先不去说它。"
    "对一个连长相都不知道的人，没有必要进一步去破坏他的形象了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA03"),"True","img/KA_XAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA042"
    神奈 "「就连隐藏钥匙的位置都已经告诉我了哦。」"
    志雄 "「傻子啊，那家伙……」"
    voice "NYU12A_KA043"
    神奈 "「因为家里没有啥被偷了会造成麻烦的东西，所以经常连锁都不锁，他是这么说的……」"
    "关于这点，我可以理解。"
    "反而是处心积虑进去的小偷会比较可怜吧。"
    window hide
    play sound "SE02_19L"
    pause (64/32.0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA10"),"True","img/KA_XAA10A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    pause (16/32.0)
    play sound "SE02_03"
    voice "NYU12A_KA044"
    神奈 "「啊，回信来了。说可以去那里住哦。」"
    志雄 "「果然……是他本人……」"
    "神奈的手机上收到的短信的发信地址，毫无疑问是稻穗，内容则是大大咧咧的允许住宿的词句。"
    志雄 "「即使这样，在那种地方过夜还是太危险了。」"
    志雄 "「我手头的公寓，还有几间空房间，你就用那里吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA02"),"True","img/KA_XAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU12A_KA045"
    神奈 "「哇——！　太好了。果然住在不认识的人那里还是很让人不安的呀。」"
    志雄 "「真是，让人没办法……」"
    "对着天真地高兴着的神奈，我苦笑着答应了住宿的事。"
    "虽说如此……"
    "人这种东西，究竟是如何奇妙地联系在一起的，还真是难以琢磨呢。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG15NA1@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG15NA1@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    play music  "OBGM17"
#FADE_IN 1
    "今天铃也不在……"
    "神奈很容易地进入了公寓。"
    "离睡觉时间还早，结果就变成了到我的房间里聊天……"
    志雄 "「果然，还是没有办法呢。」"
    "说着说着，神奈不知何时睡着了。"
    "突然决定的长途旅行，以及一整天寻找结乃……"
    "如果不累的话才比较奇怪吧。"
    voice "NYU12A_KA046"
    神奈 "「咕……呼……」"
    "为了好朋友，以及她的男友，立即飞奔了过来。"
    "就凭着这份善良，已经很好地拯救了我一次了。"
    志雄 "「谢谢你哦。为了我们两个。」"
    "即使到了房间，还是继续听我说着这些事情。"
    "她并不是只站在我这边，同时也在意着结乃的想法……能够在这两边周旋协调的，也只有神奈一个人吧。"
    志雄 "「晚安……」"
    "我轻轻把毯子盖上神奈肩头。"
    "在这种情况下，让她去空房间之类的话也说不出口了。"
    "而且……没人住的房间又寒冷又容易让人感到孤单。"
    voice "NYU12A_KA047"
    神奈 "「啊呜……安。」"
    "神奈就这么迷迷糊糊地回答了我。"
    window hide
    show expression "img/BG15NA2@2x.jpg" as bg0 with dissolve
    scene expression "img/BG15NA2@2x.jpg" as bg0 with dissolve
    "为了不吵醒她……我悄悄地缩到了房间的一角。"
    "为了防止神奈半夜醒来因为找不到舒适的睡觉的地方而难堪，我把床空在那里了。"
    志雄 "「今晚不知道能不能睡着呢，我……」"
    "在这种房间里熟睡是一件很难的事。"
    "反正肯定只能浅浅地睡着，所以明天应该能够早起。"
    "如果早起了的话……再尝试联络一下结乃吧。"
    "然后，敞开心扉好好地谈一谈。"
    "就算是为了如此关心我们的神奈……我也必须全力以赴。"
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