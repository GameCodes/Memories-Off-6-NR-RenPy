label NYU02A:
    $currentlabel = "NYU02A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '22'
    $date = '6'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 3,CAL_0722
    show expression "img/NIMG15C-568h@2x.jpg" as cal zorder 5
    show expression "img/07_22_SATURDAY@2x.png" as cal_date zorder 6:
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
    scene expression "img/BG93NA@2x.jpg" as bg0 with dissolve
    play music "BGM06"
    play sound "SE08_17L"
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
    "作为澄空在校生的最后一个暑假……"
    "同时还是一个备考生。"
    "虽然只是去试听暑期补习班，可是加上学生会的工作，一天天基本都这么糊里糊涂的过去了。"
    "而且几乎每天都有各种理由需要要去学校，完全没有一点暑假的样子。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,112,96
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB03"),"True","img/YU_LCB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「说起来，人还真是多啊。」"
    voice "NYU02A_YU000"
    结乃 "「是呢。」"
    "结乃的态度还是一如既往的不冷不热。"
    "并不是说她在逃避我，每个晚上我们也有打电话，补习之余也忙里偷闲的找时间见面。"
    "可是，不止为什么，她的反应总让人觉得怪怪的。"
    志雄 "「结乃喜欢烟花吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA01"),"True","img/YU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU02A_YU001"
    结乃 "「喜欢啊，我想不会有人讨厌这种东西吧。」"
    "期盼已久的约会，芦鹿岛烟花大会终于到了。"
    "结乃也一反常态的精神，早早地到了会场。"
    "不过到这里的人大都是想看烟花的人，即使来的很早，能不能占到一个合适的位置也只能靠运气了。"
    志雄 "「大家都穿了浴衣呢。结乃没有吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA04"),"True","img/YU_LCA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU02A_YU002"
    结乃 "「有时有，不过今天妈妈不在家……一个人穿不了。」"
    志雄 "「哦，这样啊……」"
    "打算随便提点什么展开话题，不过似乎却适得其反。"
    "或许今天没能穿上浴衣也是她闷闷不乐的原因之一。"
    志雄 "（真是没办法呢。）"
    "在约会的时候，还是避开补习之类的话题好。"
    "但是，要是那样的话，在暑假无聊度日的我很快就会陷入无话可说的境地。"
    "往常这个时候一般都是结乃引起话题的，否则沉默的状态就会一直持续下去。"
    window hide
    play sound "SE06_00"
    pause (32/32.0)
    voice "NYU02A_X7000_K"
    揚聲器 "「晚上好～烟花大会即将开始，大家都准备好了吗」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA01"),"True","img/YU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「喔，要开始了。」"
    "真是及时的救场。"
    "只要有烟花的话，就不怕没有什么新的话题。"
    "就算没什么话说，两个人看着同一种美妙的东西，总能产生些共鸣吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB06"),"True","img/YU_LCB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU02A_YU003"
    结乃 "「啊哈？」"
    "结乃也非常期待烟花吗？很久没见过结乃主动说话了。"
    voice "NYU02A_YU004"
    结乃 "「学长，广播里的声音……是不是好像很年轻的样子呢？」"
    志雄 "「是吗？没怎么注意呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB01"),"True","img/YU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU02A_YU005"
    结乃 "「是新手吧……年纪一定和我们差不多。」"
    "不愧是广播的骨灰级听众。"
    "虽然说这次是祭典的广播，可只要和广播有关系，都逃不过她那敏锐的洞察力。"
    stop music fadeout 1
    voice "NYU02A_X7001_K"
    揚聲器 "「那么，烟花大会即将开始，大家一起来倒数吧！」"
    "嗯，听起来的确像是一个新手。"
    "不过，那年轻开朗的声音到也和会场中的气氛相得益彰，人们不知不觉间就被广播中的激情所感染了。"
    stop sound
    voice "NYU02A_X7002_K"
    揚聲器 "「８、７、６……」"
    "整个会场上的人们随着广播一起数着数。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA01"),"True","img/YU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU02A_YU006"
    结乃 "「３、２、１……」"
    "不知从几开始，结乃也跟着广播倒数了起来。"
    "就在整个会场响彻着巨大的「１——」之后……"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_INIC 3
#BG_ALPC 1
#BG_ALPC 3
#BG_UVC 3,0,0,640,448
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU01A")]=True
    show expression "img/EVN_YU01A1@2x.jpg" as bg3 zorder 3 with dissolve
#BG_FLG EVN_YU01A

#EFF_STAC 0,HANABI_FLASH,EFF_NOSKIP,3,EVN_YU01A
#BG_POS_SAVEC 1
#BG_POS_SAVEC 3
#BG_ALP_SAVEC 1
#BG_ALP_SAVEC 3
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    pause (192/32.0)
    "第一枚烟花闪亮着，快速的划过夜幕，在夜空中绽放开来。"
    window hide
    play music "BGM13"
    voice "NYU02A_YU007"
    结乃 "「哇～真漂亮……」"
    "在烟花的光芒中，身旁的结乃也和天空一起绽放出了微笑。"
    "久违的……结乃发自内心的笑容啊。"
    voice "NYU02A_X7003_K"
    揚聲器 "「那么，好戏还在后面，接下来是芦鹿岛著名的……」"
    "就像配合播音员一样，烟花接二连三的划过天际，绽放出美丽的光辉。"
    voice "NYU02A_YU008"
    结乃 "「好壮观！志雄学长！你看这天空！」"
    志雄 "「嗯，真是太绚丽了……」"
    "烟花盛开的时间是那么的短暂。"
    "就像是是呼应着人们的恋恋不舍，一发又一发的光点被不断的射上天空，五颜六色的光芒点燃了整片天空。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU01D")]=True
    show expression "img/EVN_YU01D1@2x.jpg" as bg3 zorder 3 with dissolve
#BG_FLG EVN_YU01D
#EFF_STAC 0,HANABI_FLASH,EFF_NOSKIP,3,EVN_YU01D
    voice "NYU02A_YU009"
    结乃 "「这里的每一枚烟花，都要很长时间才能做好吧……」"
    志雄 "「是啊，可是刚留下一点光辉，就又匆匆离去了……」"
    "为了这瞬间的美丽，工人们花了数十倍的时间来精心策划。"
    "他们现在又是以怎样的心情，去端详这美妙的夜空呢？"
    voice "NYU02A_YU010"
    结乃 "「去年奏云祭表演结束的时候，我也想到过同样的问题。」"
    voice "NYU02A_YU011"
    结乃 "「明明大家那么的努力，花了那么多时间辛苦排练，可是演出却只有那么短。」"
    志雄 "「但是，不是获得了成功么？」"
    "打动观众的内心，被评选为最佳节目。"
    "而且，把心意传达给神奈，这个最终的目的也达到了。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU01B")]=True
    show expression "img/EVN_YU01B1@2x.jpg" as bg3 zorder 3 with dissolve
#BG_FLG EVN_YU01B
#EFF_STAC 0,HANABI_FLASH,EFF_NOSKIP,3,EVN_YU01B
    voice "NYU02A_YU012"
    结乃 "「高中生活，也像烟花一样眨眼就会过去吧……」"
    voice "NYU02A_YU013"
    结乃 "「遇到学长之后，不知不觉已经过去一年了。真的是，不知不觉呢……」"
    志雄 "「嗯。」"
    "和结乃在一起的时间，的确已经有一年了。"
    "一起经历的那些事情，清晰地仿佛就是昨天刚发生的一样。可回头望去，那幽邃的来路，有似乎有着说不完的故事。"
    voice "NYU02A_YU014"
    结乃 "「和志雄学长交往的时间，一转眼就过去了……」"
    voice "NYU02A_YU015"
    结乃 "「一切结束之后，那段时间和四年，究竟能留下些什么呢？」"
    志雄 "「结乃？」"
    "她沐浴在烟花光芒中的侧脸，散发出一种忧郁的色彩。"
    "明明近在咫尺，却感觉心与心之间隔着天涯。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU01C")]=True
    show expression "img/EVN_YU01C1@2x.jpg" as bg3 zorder 3 with dissolve
#BG_FLG EVN_YU01C
#EFF_STAC 0,HANABI_FLASH,EFF_NOSKIP,3,EVN_YU01C
    voice "NYU02A_YU016"
    结乃 "「与学长经历过的高中生活，那些点滴的回忆，会保存在我内心的深处，永远也不会忘记。」"
    voice "NYU02A_YU017"
    结乃 "「但是……只有这些的话，我还是会感到不安。就算像烟花那样，哪怕只有一瞬也好，我想要和学长留下些闪着辉光的记忆。」"
    voice "NYU02A_YU018"
    结乃 "「这么想是不是很任性？」"
    "结乃把双手紧紧地握在一起，放在胸前，好像一不注意，思念就会倾泻而出，随着无形的风一同消逝在茫茫夜幕之中。"
    voice "NYU02A_YU019"
    结乃 "「对不起。那个晚上明明有期待那样的回忆。」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU01B")]=True
    show expression "img/EVN_YU01B1@2x.jpg" as bg3 zorder 3 with dissolve
#EFF_STAC 0,HANABI_FLASH,EFF_NOSKIP,3,EVN_YU01B
    voice "NYU02A_YU020"
    结乃 "「结果还是不行。我可以埋怨铃的多管闲事，但也不得不责备自己不够坚定。」"
    voice "NYU02A_YU021"
    结乃 "「你们两个明明都是在为我着想，而我……真的是不够成熟呢。」"
    "拨动心弦，结乃的背负那那么久的包袱明明白白的展开在了我的眼前。"
    "我得做点什么，为了眼前这个为我背负如此之多的女孩。"
    志雄 "「没那样的事，其实我和你一样呢。」"
    "那时候的事，虽然只是漫长时间中的一个小点，却在心中留下了比烟花更加鲜明的印象。"
    志雄 "「暑假里，那种像烟花一样的回忆，就算只有一个也好，能把心中填的满当当的就好了。」"
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU01B")]=True
    show expression "img/EVN_YU01B1@2x.jpg" as bg3 with dissolve
    voice "NYU02A_YU022"
    结乃 "「嗯。」"
    "放烟花的准备是完成了。"
    "我们究竟能够创造怎样绚丽的美景呢。"
    voice "NYU02A_YU023"
    结乃 "「现在，也是重要的回忆哦。」"
    "头顶的夜空中，烟花仍然不知疲倦的重复着绽放——消逝——。"
    window hide
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    hide bg3 with dissolve
    pause (32/32.0)
#FADE_IN 1
    voice "NYU02A_X7004_K"
    揚聲器 "「辛劳已毕，感谢大家能来。不过，最后我还有些东西想和在场的各位分享。」"
    "最后一朵硕大而明亮的烟花，仿佛要照亮整个岛般的耀眼，献上了大会的华丽谢幕。"
    voice "NYU02A_X7005_K"
    揚聲器 "「今天的广播是由去年浜咲广播大赛第二名的我为大家播报的……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,112,96
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA01"),"True","img/YU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「广播比赛？」"
    if not persistent.dictlist[60] and persistent.show_dict:
        $persistent.dictlist[60]=True
        show screen dict_pop(i=60)
    voice "NYU02A_YU024"
    结乃 "「有听说过，应该是浜咲ＦＭ主办的广播节目创作大赛吧。」"
    "我今天才知道世界上还有这么一种比赛。"
    "加入广播台的结乃应该会有所耳闻吧，但是只作为听众的我不知道也不足为奇了。"
    voice "NYU02A_X7006_K"
    揚聲器 "「今年的广播大赛也即将到来。」"
    voice "NYU02A_X7007_K"
    揚聲器 "「距离报名截止还有充足的时间，期待大家能积极参与！」"
    voice "NYU02A_X7008_K"
    揚聲器 "「那么，感谢今天到场的诸位，烟花大会到这里就结束了，大家回去的路上要小心哦！」"
    play sound "SE08_06"
    "在众人的掌声与欢呼中，烟花大会算是落下了帷幕。"
    "而我，站在逐渐散去的人群中，听着周遭嘈杂的声响，默默地思考着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA04"),"True","img/YU_LCA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU02A_YU025"
    结乃 "「志雄学长？」"
    志雄 "「对了，这个活动没有限定必须从属于哪个特定的社团才能参加吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB01"),"True","img/YU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU02A_YU026"
    结乃 "「应该没有限制必须是专业的人员才能参与吧……」"
    "虽然不明白专业的基准是什么，不过就我而言，这方面的经验几乎为零。"
    "结乃一直在做校内广播，虽然没有报酬，但在经验上应该没话说的。"
    志雄 "「那个……我们去参加吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB06"),"True","img/YU_LCB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "本来我们的羁绊就是从Ｔ－ｗａｖｅ延伸开来的。"
    "那么创造共同回忆，恐怕没有什么比这个比赛更合适的了。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG97NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG97NA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    play music "BGM10"
#FADE_IN 1
    if not persistent.dictlist[35] and persistent.show_dict:
        $persistent.dictlist[35]=True
        show screen dict_pop(i=35)
    "烟花大会过后不久，我们在酪萨克的店里碰头。"
    "因为稻穗信在这家店打工，所以在讨论问题的时候，一般不会考虑来这里。"
    "不过，由于稻穗先生在夏天要去温泉旅馆兼职，所以餐厅这边请了长假。"
    "于是酪萨克成了没有任何人打扰的，进行作战策划的绝佳场所。"
    window hide
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XCA01"),"True","img/YU_XCA01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NYU02A_YU027"
    结乃 "「那么，基本的规则就是这些吧。」"
    志雄 "「原来如此。」"
    "幸运的是，烟花大会的会场里有贴出比赛的海报。"
    "比赛的主办方浜咲ＦＭ是芦鹿岛烟花大会的重要赞助者。"
    志雄 "「虽然广播里说时间还很充足……不过现在看来，也没有多少时间了……能赶上吧？」"
    voice "NYU02A_YU028"
    结乃 "「录音倒是不用花多少时间的。」"
    "因为参赛录音要求限制在15分钟内，所以在录音上的确不需要太多的时间。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XCA05"),"True","img/YU_XCA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU02A_YU029"
    结乃 "「只是，没有足够的时间策划一项新的节目了。」"
    "即便如此，也不是不可能，结乃曾经这样说过。"
    "在我看来，她并不是那种信口开河的人。"
    志雄 "「放心啦，以我们这种Ｔ－ｗａｖｅ超级投稿者的能力，应该不难克服。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XCB01"),"True","img/YU_XCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU02A_YU030"
    结乃 "「不过制作节目和投稿完全不是一个事啊，不能掉以轻心的……」"
    "最近广播台正在制作ＤＪ风格的广播，恐怕结乃挤不出白天的时间。"
    voice "NYU02A_YU031"
    结乃 "「但还是想尝试一下，重在参与么，参赛本身也是一件很有意思的事情吧。」"
    志雄 "「嗯。只要节目完成，多少也能当作纪念。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XCB02"),"True","img/YU_XCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU02A_YU032"
    结乃 "「是呢，那么我们开始讨论节目的内容吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XCA01"),"True","img/YU_XCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU02A_YU033"
    结乃 "「不过……既然想要参加，果然还是不想空手回去呢。」"
    "结乃看着小册子上的优胜奖励，眼里闪着光。"
    "优胜者可以获得１０万日元，这对于高中生来说已经是相当大一笔数目了。"
    志雄 "「是啊，既然要做的话，全力以赴也是必须的。」"
    "从看到比赛介绍的时候，我的目的就已经确定了。"
    "倒不是为了那１０万日元，即使没有获得优胜也没有关系，我有着必须努力的理由。"
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
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA01"),"True","img/YU_LCA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA01"),"True","img/MH_LCA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    play music "BGM07"
    voice "NYU02A_MA000"
    麻寻 "「唉？是志雄和结乃啊。」"
    志雄 "「呃，你好……」"
    voice "NYU02A_YU034"
    结乃 "「你好。」"
    "下意识的把摊在桌子上的小册子用手臂盖住。"
    "虽说稻穗不在，可也不能掉以轻心。"
    if not persistent.dictlist[17] and persistent.show_dict:
        $persistent.dictlist[17]=True
        show screen dict_pop(i=17)
    "先堂麻寻，似乎和在这里兼职稻穗信关系相当不错。"
    voice "NYU02A_MA001"
    麻寻 "「这个时间看你们，真是少见呢。是刚约会完准备回去了吗？」"
    "因为都是稻穗的「朋友」，所以很容易地就搭上话了。"
    "也因为这层关系，点菜的时候往往我们也能获得不少特殊优惠。"
    "要是只是那样到还好，只是……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA02"),"True","img/MH_LCA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU02A_MA002"
    麻寻 "「嗯哼，刚才藏了什么，也给我看看么～」"
    志雄 "「啊……」"
    "好奇心异常旺盛……"
    "在客人对话的时候若无其事的插话进来，真是让人头疼。"
    "不但如此，她还敏锐的发现了问题的关键，真是麻烦。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA01"),"True","img/MH_LCA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU02A_MA003"
    麻寻 "「唉？你们要参加这个比赛吗？」"
    志雄 "「嗯，是的。」"
    "虽然很想敷衍过去，不过这个时候了，多问问别人的看法也许会有意外的收获。"
    "并且这时如果可以隐瞒，可能会让事情别的更复杂，所以只好老实说明了。"
    voice "NYU02A_MA004"
    麻寻 "「看上去很有趣的样子。如果需要的话，我可以帮忙，别看我现在是个服务生，以前也是有电影制作经验的……」"
    "果然变成这样子了……"
    "所以才想要隐瞒的……"
    voice "NYU02A_YU035"
    结乃 "「真的吗？那么要是有什么需要帮忙的地方就拜托了！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA02"),"True","img/MH_LCA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU02A_MA005"
    麻寻 "「嗯，包在我身上。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA03"),"True","img/MH_LCA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU02A_MA006"
    麻寻 "「啊，那边的客人叫我了，我先去应付一下。要是有什么需要帮忙的地方，真的不用客气哦～」"
    window hide
    stop music fadeout 1
    hide lh1 with dissolve
    pause (16/32.0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC03"),"True","img/YU_LCC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "看着麻寻飞快跑开的背影，我和结乃不约而同的叹了口气。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XCC03"),"True","img/YU_XCC03A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    志雄 "「很感激她的好意，不过似乎我们战队的战斗力还是很弱啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XCC01"),"True","img/YU_XCC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU02A_YU036"
    结乃 "「是的，不过她做过电影的场记，到时候可能要拜托她帮忙。」"
    "结乃曾经因为制作广播剧而请教过她一些关于电影制作的事情。"
    "但是从麻寻那里得到的建议全部太过理想化，可行性几乎为零。"
    "从那以后，麻寻在我们心中的股价就一路跌停。"
    志雄 "「收集素材的事情……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XCA01"),"True","img/YU_XCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    if not persistent.dictlist[2] and persistent.show_dict:
        $persistent.dictlist[2]=True
        show screen dict_pop(i=2)
    voice "NYU02A_YU037"
    结乃 "「我想，找智纱学姐会比较好吧、」"
    志雄 "「是吧……」"
    "虽然我和智纱之间发生过很多事，但是，现在她是我和结乃最大的拥护者。"
    "作为前辈，对加入广播台的结乃更是爱护有加，大家都说她们像一对关系很好的姐妹。"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XCB01"),"True","img/YU_XCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "BGM06"
    voice "NYU02A_YU038"
    结乃 "「但是，我们至少得把节目的主题确定下来。」"
    志雄 "「这是必须的吧。」"
    "那是为了创造我们美好回忆的广播节目。"
    "想要尽可能的只通过彼此的力量来经营它的心情并不难理解。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XCB02"),"True","img/YU_XCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "我们充满干劲的构思节目，完全沉醉其中。"
    "以至于最后，又要目送结乃冲向末班车的身影。"
    "好在最后还是赶上了，不过下次还是稍微注意点时间好了。"
#label QJUMP
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
    play music "OBGM17"
#FADE_IN 1
    "回家后，我打开电脑。"
    "自动启动的聊天软件里弹出了神奈的留言。"
#CHAT_STA
#BG_SET_BACK 
#BG_INIC 1
#BG_INIC 3
#BG_ALPC 1
#BG_ALPC 3
    show expression "img/NIMG14C@2x.jpg" as bg3
    show expression "img/CHAT_2A_00@2x.png" as bg_chat zorder (10-1)
    with dissolve
    play sound "SE09_35"


#BG_ALP_SAVEC 1
#BG_ALP_SAVEC 3
#BG_ALPC 1
#BG_ALPC 3
#CHAT_STR "〈神奈：〉%N原来如此，就是说想要我帮忙搜集一些素材对吧？"
#WAIT_KEY 96
    show expression "img/CHAT_2A_01@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N嗯，因为我和结乃的广播回忆里也不能缺少神奈呢。"
#WAIT_KEY 96
#CHAT_END
    "和结乃商量过，我想在节目里向所有给予我们支持的朋友致谢。"
    "第一个必须要感谢的人，无疑就是神奈。"
#CHAT_STA
    show expression "img/CHAT_2A_02@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N可以啊～不过不要再借机炫耀你们人尽皆知的幸福了哦～"
#WAIT_KEY 96
#CHAT_END
    "在多次联系神奈后，还担心她会不会厌烦，现在看来似乎是小瞧她了。"
    "神奈是一个很好的倾听者，总会给出切实可行的提议。"
    "这样也就理解了为什么结乃总是如此依赖神奈，找她商量问题了。"
    "要想得到有效的帮助，没有谁比神奈更靠谱了，虽然可能在事后听广播的时候并不这么认为……"
#CHAT_STA
    show expression "img/CHAT_2A_03@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N完全没有打算这么做啊……"
#WAIT_KEY 96
    show expression "img/CHAT_2A_04@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N是吗？我怎么总觉得你们是借制作广播之名来秀恩爱的……"
#WAIT_KEY 96
    show expression "img/CHAT_2A_05@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N不是啦，只是有想好好谢谢她。"
#WAIT_KEY 96
#CHAT_END
    "在节目中，给她一个策划之外的『谢谢』。"
    "那就是制作这个广播节目的终极目标。"
    "只要这样，这个广播一定能承载住我们之间的那份真情。"
#CHAT_STA
    show expression "img/CHAT_2A_06@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N不过，要是那样的话，节目必须要非常优秀才行的。"
#WAIT_KEY 96
    show expression "img/CHAT_2A_07@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N说的是啊，要是作品最后不能被公开播放，目的就达不到了。"
#WAIT_KEY 96
    show expression "img/CHAT_2A_08@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N超过５００个作品里只有８个名额哦，你有自信吗？"
#WAIT_KEY 96
#CHAT_END
    "通过录音磁带选出来的８组优胜者，可以在浜咲的海岸上的特别广播室里进行现场播报比赛。"
    "就算是结乃，也无法阻止我在现场直播的时候偷改脚本吧。"
    "不管多么害羞也好，我的心意一定要让她听到。"
#CHAT_STA
    show expression "img/CHAT_2A_09@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N我就直和你说吧，这个比赛的难度，非常的高呢～"
#WAIT_KEY 96
    show expression "img/CHAT_2A_0A@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N呃，我一直想问，你为什么对这个比赛这么了解呢？"
#WAIT_KEY 96
#CHAT_END
    "在她详细的列举各种比赛细则的时候我就很在意了。"
    "明明不记得这些信息有写在简介里，她却知道的特别详细。"
#CHAT_STA
    show expression "img/CHAT_2A_0B@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N好吧，因为我就是去年的优胜者！"
#WAIT_KEY 96
#CHAT_END
    志雄 "「我了个去！！」"
    "这样似乎就能明白为什么今天烟花大会的播音员是『准优胜者』了。"
    "因为优胜者家距离会场太远，不方便赶到现场。"
#CHAT_STA
    show expression "img/CHAT_2A_0C@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N很厉害啊，不仅是一流的投稿者，连制作广播节目也是如此厉害呢。"
#WAIT_KEY 96
    show expression "img/CHAT_2A_0D@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N本质都是一样的啦，只是将对广播的热爱表现在了多个方面罢了～"
#WAIT_KEY 96
#CHAT_END
    scene expression "img/NIMG14B@2x.jpg" as bg0
    with dissolve
    "第一任『凯尔玛妹妹』，就连这方面都要比我和结乃强。"
    志雄 "（不能输啊）"
    "在Ｔ－ｗａｖｅ以外的战场，我对『凯尔玛妹妹』的求胜心也燃了起来。"
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
