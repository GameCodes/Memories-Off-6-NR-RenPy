label NYU08A:
    $currentlabel = "NYU08A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '31'
    $date = '1'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 3,CAL_0731
    scene expression Solid("000") with fade
    show expression "img/NIMG15F-568h@2x.jpg" as cal zorder 5
    show expression "img/07_31_MONDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG36AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG36AA@2x.jpg" as bg0 with dissolve
    play music  "OBGM02"
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
    "报名截止的前一天早上。"
    "我们集合在酪萨克进行最终的商讨。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 0,(320-192)
#CHR_POSC 1,(320+192)
#CHR_POSC 2
#CHR_DSPTC 0,1,2,YU_MBA05,TO_MBA01,MH_MBA01
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA05"),"True","img/YU_MBA05A@2x.png") as lh0 zorder (10+0):
        xcenter .2
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh1 zorder (10+2):
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA01"),"True","img/MH_MBA01A@2x.png") as lh2 zorder (10+1):
        xcenter .8
        ypos 0.0
    with dissolve
    "参加这次会议的有我，结乃，拉来凑数的亨，还有不惜请假来凑热闹的麻寻小姐四个人。"
    voice "NYU08A_YU000"
    结乃 "「节目是需要主题的。」"
    voice "NYU08A_YU001"
    结乃 "「简而言之，就是让听众一听就能明白广播的主旨。」"
    "用结乃的话说，并不是讨论节目的进行方式，例如ＤＪ式或是话题式到什么的，而是讨论节目在根本上的方向。"
    "一言以蔽之就是『想让听众感受到什么』这个意思。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO000"
    亨 "「嗯，如果不明白那个的话，制作主题曲也就麻烦了……对吧？别看我这样，我也并不是随便作什么曲子都ＯＫ的人哦。」"
    志雄 "「唉？亨，你还打算作曲的吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA04"),"True","img/TO_MBA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO001"
    亨 "「喂，打算把我排除在外了吗！？」"
    voice "NYU08A_TO002"
    亨 "「即使被你们讨厌我也一定要来帮忙！」"
    "亨似乎是为自己被排除在外而感到不满，意志特别坚决，真让人不知道该感谢好还是头疼好。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA01"),"True","img/YU_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU002"
    结乃 "「佐贺学长，曲子作好的话请让我先听听哦。不过前提是要能赶上明天的录音。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO003"
    亨 "「明天啊，绝对赶得上进度哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO004"
    亨 "「比起我的事情，节目本身那边没有多少问题吧？在报名截止当天录音……」"
    志雄 "「正如你所说，我们没多少时间了，所以赶快继续话题吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO005"
    亨 "「哦，那么主题的话，已经考虑好了吧？」"
    voice "NYU08A_YU003"
    结乃 "「啊，是。」"
    play sound "SE03_29"
    "结乃拿出一些打印好的文件放在桌子上。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBB03"),"True","img/YU_MBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "我抬头看了看结乃，她也正满怀期待地望着我这边。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBB01"),"True","img/YU_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "我翘了翘嘴角作为回应，结乃的脸上也浮起淡淡的笑容。"
    "没问题的。"
    "我们都接受到了对方的讯息。"
    "彼此点头示意。"
    "然后，结乃开始说明文件的内容。"
    voice "NYU08A_YU004"
    结乃 "「嗯，我觉得……主题用『讯息』的话不错呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA05"),"True","img/TO_MBA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO006"
    亨 "「节目的主题是『讯息』吗？」"
    voice "NYU08A_TO007"
    亨 "「原来如此，这样就比较容易想到节目内容了，对吧？」"
    "亨表示内容很容易想到，脸上的表情却十分困惑。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA06"),"True","img/MH_MBA06A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA000"
    麻寻 "「那么，具体来说，你们打算怎么做？」"
    "麻寻小姐看着左思右想的亨，也提出了自己的疑问。"
    志雄 "「例如收集一些平时想对身边亲近的人说的，但是又不知道怎么开口的话作为投稿……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA01"),"True","img/YU_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU005"
    结乃 "「主要是短信投稿。与其说是节目，我到觉得更像是短信留言板了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO008"
    亨 "「啊，这个好。把我对心爱的莉莉丝的千言万语，全都凝聚在一句话里！」"
    "亨猛地一拍大腿跳了起来。"
    window hide
#CHR_PRIC 1
#BG_SET_BACK 
#BG_INIC 3
#BG_PRIC 3
    show expression "img/NIMG13A@2x.jpg" as bg3 zorder 100 with dissolve
#CHR_SET_BACK
#CHR_INIC 3
#CHR_PRIC 3
#CHR_POSC 3,(320-160)+32
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XAB07"),"True","img/RI_XAB07A@2x.png") as lh3 zorder (100+3):
        ypos 0.0
    with dissolve
    play sound "SE07_19"
#BG_ALP_SAVEC 1
#BG_ALP_SAVEC 3
#CHR_ALP_SAVEC 3
    voice "NYU08A_TO009"
    亨 "「莉莉丝听完肯定就对我朝思暮想，魂牵梦萦，不能自拔的爱上我了。」"
    voice "NYU08A_TO010"
    亨 "「哦哈哈哈……棒极了！」"
    hide bg3
    hide lh3
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBC05"),"True","img/YU_MBC05A@2x.png") as lh0 zorder (10+0):
        xcenter .2
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBB04"),"True","img/MH_MBB04A@2x.png") as lh2 zorder (10+2):
        xcenter .8
        ypos 0.0
    with dissolve
#ROUTINE_STA


#ROUTINE_STP
#BG_ALP_SAVEC 1
#BG_ALP_SAVEC 3
#CHR_ALP_SAVEC 3
#BG_PRIC 3
#CHR_PRIC 3
#CHR_PRIC 1
    "亨干劲十足地发着白日梦。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO011"
    亨 "「喂，志雄，我这天衣无缝的完美作战计划怎么样？」"
    志雄 "「哦，一定能成的，加油哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB03"),"True","img/TO_MBB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO012"
    亨 "「你这家伙……能不能不要敷衍我。」"
    "我无奈地摇了摇头。"
    "计划的内容大体上已经准确地传达了。"
    "我们是因为ＫＡＮＡＴＡ的节目聚集到一起的。此刻又再次感受到，她的节目正是我们向往的目标。"
    "但是，ＫＡＮＡＴＡ高超的主持水平，她节目的那种独特气氛，则是我和结乃难以企及的高度。"
    "毕竟我们只是业余爱好者而已。"
    "所以我们不能期望在主持上出彩，而是要让那些难以被说出口的讯息成为节目的主要内容。"
    志雄 "（……不过其实也都无所谓吧。）"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MCC03"),"True","img/MH_MCC03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA001"
    麻寻 "「呃，爱的告白暂且不说，不过这总让人想到某个别的节目……那样没问题吗？」"
    "还有些观望的麻寻小姐向结乃询问道。"
    "就像是拿ＫＡＮＡＴＡ作为例子一样，这个策划案最后还是受到了『Ｔ－ｗａｖｅ』很大的影响。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBC03"),"True","img/YU_MBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU006"
    结乃 "「……呃～嗯。虽然听起来也许会觉得我在逞强。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA01"),"True","img/MH_MBA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA002"
    麻寻 "「嗯。让我听听吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA01"),"True","img/YU_MBA01A@2x.png") as lh0 zorder (10+0):
        xcenter .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh1 zorder (10+1)
    voice "NYU08A_YU007"
    结乃 "「『Ｔ－ｗａｖｅ』的核心，可以说就是ＫＡＮＡＴＡ小姐。而她谈话的内容就比较随便，这个，怎么说呢……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA03"),"True","img/MH_MBA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA003"
    麻寻 "「啊哈哈……我明白你想说的话了。」"
    voice "NYU08A_MA004"
    麻寻 "「然后？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBB01"),"True","img/YU_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU008"
    结乃 "「我们呢，比起ＤＪ的发挥，更应该重视投稿来的讯息，用它们来作为核心。」"
    "结乃在小心仔细地用言语归纳着我们已经找到了的结论。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB03"),"True","img/TO_MBB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO013"
    亨 "「果然很逞……唔……」"
    "麻寻小姐伸出手堵住了亨的嘴，没让他继续说下去。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA05"),"True","img/MH_MBA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA005"
    麻寻 "「原来如此呢，不是挺好的么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA01"),"True","img/MH_MBA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA006"
    麻寻 "「创作者本身刻意地去制造区别，总是比无意间地模仿抄袭要好的。」"
    "捂着亨的嘴，麻寻小姐如此说道。"
    "麻寻小姐的话貌似也没有什么根据，但她说的这些令我们感到很欣慰。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MCC02"),"True","img/MH_MCC02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA007"
    麻寻 "「啊，特意去剽窃抄袭是更不行的哦？」"
    志雄 "「哈哈哈。结果，还是不能否认两者非常相似这个事实呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBB02"),"True","img/YU_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU009"
    结乃 "「实际上，确实就是很像的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA01"),"True","img/MH_MBA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA008"
    麻寻 "「这样的话追究起来就没完了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA05"),"True","img/MH_MBA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA009"
    麻寻 "「总不能说广播主持谈话的风格，除了哪位最先使用的人之外其他所有人都是剽窃吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO014"
    亨 "「哦，这倒也是有道理。」"
    "对于麻寻小姐的理论，亨也嗯嗯地点头称是。"
    "虽然觉得论点有些不同，但多少也有了一个能让我们硬着头皮做到底的依据了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBB01"),"True","img/YU_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU010"
    结乃 "「我也已经决定不在意了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA01"),"True","img/YU_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU011"
    结乃 "「那个节目对我非常的特别，所以如果做出来的不像反倒不正常了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA02"),"True","img/MH_MBA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA010"
    麻寻 "「这份气魄不错，是哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA05"),"True","img/TO_MBA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO015"
    亨 "「不过真这样做的话，要怎样去收集短信呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA05"),"True","img/YU_MBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU012"
    结乃 "「因为没多少时间了，我觉得大量收集这种事情是不可能的了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBB03"),"True","img/MH_MBB03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA011"
    麻寻 "「是那样呢。不过，又不好自己瞎编……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA01"),"True","img/YU_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU013"
    结乃 "「现在只能尽可能地找熟人，让他们投稿了。」"
    voice "NYU08A_MA012"
    麻寻 "「呃——也许只能那样了……」"
    志雄 "「稻穗先生那边如何？让其他店员朋友也来帮忙行吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA06"),"True","img/MH_MBA06A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA013"
    麻寻 "「哈，挺好的建议。看他们应该都会喜欢广播的吧。」"
    志雄 "「好，之后是……也试着拜托莉莉丝和铃小姐帮忙吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBB01"),"True","img/YU_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU014"
    结乃 "「智纱学姐和克罗艾学姐还有神奈。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO016"
    亨 "「我说，那个……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA06"),"True","img/TO_MBA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO017"
    亨 "「我……不行吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA04"),"True","img/MH_MBA04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    "指着自己的脸，亨插话道。"
    "亨他像发送短信的人自然是莉莉丝，不过这种情况下选用他的稿件，算是作弊吧？"
    志雄 "「你怎么觉得，结乃？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBB02"),"True","img/YU_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU015"
    结乃 "「我觉得不错啊。请对远峰学姐她，华丽地进行告白吧！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO018"
    亨 "「华，华丽地……？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA04"),"True","img/TO_MBA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    "亨听见这话不知为什么，盯着我看。"
    志雄 "「干嘛用那种眼神看着我。」"
    voice "NYU08A_TO019"
    亨 "「非也，我觉得这个意见真是很值得考虑。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBB06"),"True","img/YU_MBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "亨把环视了一下我和结乃，开始认真地思考着什么了。"
    "……这家伙到底准备搞什么？"
    志雄 "「先别慌。采用不采用暂时还不知道呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO020"
    亨 "「唉唉？我那可是为了你们两位ＤＪ着想啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MCC05"),"True","img/MH_MCC05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA014"
    麻寻 "「就算这样，也是不可以作弊的～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB05"),"True","img/TO_MBB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO021"
    亨 "「可恶……那我就更要深思熟虑一番了……」"
    "亨把头按在桌子上不住地挠头。看起来事情没有他想象的那么简单。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA06"),"True","img/MH_MBA06A@2x.png") as lh2 zorder (10+2)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA04"),"True","img/YU_MBA04A@2x.png") as lh0 zorder (10+0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh1 zorder (10+1)
    with dissolve
    "亨之外的我们则是面面相觑，叹了口气，耸耸肩……尤其是结乃和麻寻，更是露出了受不了的表情。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA01"),"True","img/MH_MBA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA015"
    麻寻 "「对了，不如在等人投稿的时候也上街去采访一些素材？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBB06"),"True","img/YU_MBB06A@2x.png") as lh0 zorder (10+0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh1 zorder (10+1)
    with dissolve
    志雄 "「采访？」"
    voice "NYU08A_YU016"
    结乃 "「去采访别人吗？」"
    voice "NYU08A_MA016"
    麻寻 "「嗯。」"
    voice "NYU08A_MA017"
    麻寻 "「用不用是另外一回事，不过用采访这种形式来收集讯息也不错吧？」"
    "麻寻说着，从口袋里拿出了某个手心大小的机器来。"
    voice "NYU08A_YU017"
    结乃 "「啊，那个是……！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA02"),"True","img/MH_MBA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA018"
    麻寻 "「嘿嘿嘿……」"
    voice "NYU08A_MA019"
    麻寻 "「ＩＣ录音机。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA01"),"True","img/MH_MBA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA020"
    麻寻 "「我买了以后就没怎么用过。拿这个去采访路过的人吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA01"),"True","img/YU_MBA01A@2x.png") as lh0 zorder (10+0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh1 zorder (10+1)
    with dissolve
    voice "NYU08A_YU018"
    结乃 "「唉唉，这个听起来不错啊。」"
    志雄 "「嗯，应该很不错。」"
    "如果运气好能采访到让人感动的故事，做到广播里的效果就会非常棒了。"
    "有了素材的话，那么１０分钟左右的节目，足够时间可以介绍两到三封邮件或是别的稿件。"
    voice "NYU08A_MA021"
    麻寻 "「嗯，主要要看采访的结果了。如果运气好的话就能找到非常好的素材。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBB02"),"True","img/YU_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU019"
    结乃 "「能够拜托你去吗，麻寻。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA02"),"True","img/MH_MBA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA022"
    麻寻 "「交给我吧！」"
    "麻寻小姐很快就答应来负责这件事了。"
    志雄 "「诶？你现在不是还在工作时间里么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA04"),"True","img/MH_MBA04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA023"
    麻寻 "「啊，哦，是的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBB04"),"True","img/MH_MBB04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA024"
    麻寻 "「不过剩下的时间也不多了嘛。我去解释一下，把排班改一下就好了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA01"),"True","img/YU_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU020"
    结乃 "「稻穗先生还没回来吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA06"),"True","img/MH_MBA06A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA025"
    麻寻 "「嗯？我也不知道，我先去后面看一下好了。」"
    "麻寻小姐把ＩＣ录音机递给了亨。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA01"),"True","img/MH_MBA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA026"
    麻寻 "「那么，亨君。这个借你，你先去采访一下吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO022"
    亨 "「诶？我吗？这么说来，我也要去？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA05"),"True","img/MH_MBA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA027"
    麻寻 "「助手啊助手，你好好表现，没准回来的时候就能给你表白的机会了哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO023"
    亨 "「哦哦！原来如此，那就是说我只要装作路过的人就好了吧。」"
    "麻寻……你自己都说了反对作弊的吧。"
    "难道这是为了让亨帮忙吗？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA02"),"True","img/TO_MBA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO024"
    亨 "「哈～哈～哈～我也来缔造传说吧。」"
    "不知为什么，亨是指着我说那句话的。"
    "看起来我当时在奏云祭上做的事，已经在澄空学生当中成为了传说……"
    "现在一回想，脸就红得像要喷火出来一样。"
    "要是亨他想要把那件事情再现的话，那估计真的是要乱来一通了。"
    "看起来得让麻寻盯好亨，别让他乱来。"
    "亨失控的时候的应对方法是……"
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    menu:
        "让麻寻来对他实施下段回旋踢":
            $F7=0
        "把摩托车留下来作人质":
            $F7=1
    if F7==0:
        jump L_NYU08A_SEL00_A
    if F7==1:
        jump L_NYU08A_SEL00_B
label L_NYU08A_SEL00_A:
    志雄 "「麻寻，要是这家伙表现不太正常的话，就请给他一记下段踢吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA06"),"True","img/MH_MBA06A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA028"
    麻寻 "「下段踢？」"
    志雄 "「那家伙最喜欢被踢了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA04"),"True","img/MH_MBA04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA029"
    麻寻 "「诶……那什么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA06"),"True","img/MH_MBA06A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA030"
    麻寻 "「难道他是个受虐狂？」"
    "麻寻困惑地问道。"
    "正想继续说些什么，没想到亨本人抢先开口回应了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO025"
    亨 "「啊哈，我只会对亲爱的莉莉丝献出我的爱。回旋踢不过是她对我回报的小赠品罢了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB03"),"True","img/TO_MBB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO026"
    亨 "「还有，我真的不是受虐狂……应该吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA02"),"True","img/MH_MBA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA031"
    麻寻 "「挺有趣的，真想把你说的话录下来。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    if not persistent.dictlist[62] and persistent.show_dict:
        $persistent.dictlist[62]=True
        show screen dict_pop(i=62)
    voice "NYU08A_TO027"
    亨 "「那么，麻寻，我们出发吧！前往传说之地，用我的『猫大人』送你吧！」"
    "哼不知道什么时候给自己的摩托车起了爱称。『猫大人』？"
    "麻寻一手抓住正准备冲出去的亨"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MCC02"),"True","img/MH_MCC02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA032"
    麻寻 "「走路去哦，走～路～去～没准路上就能撞到好的素材呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB05"),"True","img/TO_MBB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO028"
    亨 "「诶～」"
    "亨嘟起了嘴，一副很不满的样子。"
    志雄 "「拜托，就算你摆出一张忧郁难过的表情，也还是一点也不可爱啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA04"),"True","img/TO_MBA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO029"
    亨 "「你别管我！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA02"),"True","img/YU_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU021"
    结乃 "「哈哈哈。」"
    jump L_NYU08A_SEL00_X
label L_NYU08A_SEL00_B:
    志雄 "「这家伙要是太乱来就头疼了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA04"),"True","img/YU_MBA04A@2x.png") as lh0 zorder (10+0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA01"),"True","img/MH_MBA01A@2x.png") as lh2 zorder (10+2)
    with dissolve
    voice "NYU08A_YU022"
    结乃 "「是呢。不过有麻寻在一起，应该没问题吧。」"
    "一想象到亨失控时候的恐慌，恐怕以麻寻的能力也无法阻止他吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO030"
    亨 "「别担心。我可是到关键时刻最靠得住男人哦！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA01"),"True","img/YU_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU023"
    结乃 "「他都这么说了，那就让他去吧。」"
    "结乃都说道这份上了，不得不让去了。"
    "不过要尽量采取措施做好准备。"
    志雄 "「好，知道了。既然这样，今天就走路去采访吧。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#QUA2_CHR 1
    if not persistent.dictlist[62] and persistent.show_dict:
        $persistent.dictlist[62]=True
        show screen dict_pop(i=62)
    voice "NYU08A_TO031"
    亨 "「什么！你是说要拆散一心同体的我和『猫大人』？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA04"),"True","img/YU_MBA04A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA06"),"True","img/MH_MBA06A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    志雄 "「还『猫大人』……连名字都起了么。」"
    voice "NYU08A_YU024"
    结乃 "「感觉挺微妙的呢。」"
    "想象一下亨对着摩托车轻声呼唤『猫大人』的情景，我不禁背脊发凉。"
    "『猫大人』这名字也太中二了吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MCC02"),"True","img/MH_MCC02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA033"
    麻寻 "「当然了，要是骑摩托车的话，路上岂不是会错过很多好素材。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO032"
    亨 "「嗯。的确是呢……」"
    "麻寻说的是对的。"
    "不过，我的目的可不是那样。"
    志雄 "「如果做了什么奇怪的事情的话，『猫大人』就要代替你……承担过错责任啦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA04"),"True","img/TO_MBA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO033"
    亨 "「什么！真卑鄙！用人质要挟啊！」"
    "虽然不是人。不过，只要手上抓着他的把柄，想必他就不敢乱来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA05"),"True","img/MH_MBA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA034"
    麻寻 "「ＯＫ。有什么问题我就给志雄你打电话吧。」"
    志雄 "「拜托你了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB05"),"True","img/TO_MBB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO034"
    亨 "「可，可恶……我对不起你——『猫大人』。都是因为我没用……」"
    "这样的话，果然还是不会乱来了吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MCC02"),"True","img/MH_MCC02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    jump L_NYU08A_SEL00_X
label L_NYU08A_SEL00_X:
    voice "NYU08A_MA035"
    麻寻 "「好，各位开始行动吧！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA01"),"True","img/YU_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_MA036"
    麻寻 "「动吧，拉车的马儿。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB03"),"True","img/TO_MBB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU08A_TO035"
    亨 "「诶～」"
    hide lh1 with dissolve
    "麻寻号令一下，感觉亨就不太情愿地嘟囔着走出了店。"
    "看起来他还是想骑着爱车『猫大人』奔驰吧。"
    hide lh2 with dissolve
    "另一边，麻寻则慌忙地向后台走去。"
    "看起来是要用店里的电话找人代班。"
    "虽然客人只有我们几个，店里挺空闲的。不过这样想换班就换班真的没有问题吗？"
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
#BG_PRI 0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBA01"),"True","img/YU_ZBA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#BG_INIC 2
    show expression "img/EXBG01A@2x.jpg" as bg2 zorder 2 with dissolve
    hide bg0 with dissolve
    play music  "BGM06"
    志雄 "「总算是有些进展了，麻寻还真是有果敢的家长作风呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBB01"),"True","img/YU_ZBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU025"
    结乃 "「不是挺好的吗，挺有趣的呢。」"
    志雄 "「诶？是吗？」"
    "真没系那个到当初拘泥着要两个人独立完成此事的结乃会说出这样的话来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBB02"),"True","img/YU_ZBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU026"
    结乃 "「现在，非常需要大家齐心协力呢。」"
    "说着那样的话，她笑了。"
    "我觉得她变得比以前更坚强了。"
    "也许不只是她，连我都在潜移默化吧。"
    志雄 "「是啊，那我们现做什么呢？」"
    "ＩＣ录音机被亨带走了，麻寻的助手一个人也就够了。。"
    "这么一来，我和结乃的工作就是找人投稿了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBA01"),"True","img/YU_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU027"
    结乃 "「要问问神奈她的意见吗？」"
    "结乃拿着手机提议道。"
    志雄 "「嗯，也许不错。不知道她会怎么说呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBA04"),"True","img/YU_ZBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU028"
    结乃 "「会怎样呢……」"
    "结乃的脸上露出了些许犹豫。"
    "即使稍微坚强了一些，但也不能说完全就免疫了。"
    "就算是我，内心也有着不安的地方。"
    "神奈应该马上就会指出我们的节目和『Ｔ－ｗａｖｅ』太过相似了吧。"
    "而且可能还会从我们没有想到的地方，找出新的问题。"
    "但是我们也知道，这样的意见相当珍贵。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBA05"),"True","img/YU_ZBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU029"
    结乃 "「不管怎么样，投稿总是要拜托她呢。」"
    "结乃深深地吸了一口气，在手机上输入了神奈的号码。"
    window hide
    play sound "SE02_02L"
    "拨号音从手机中传出。"
    "我们安静地等待着这个声音的结束。"
    stop sound
    voice "NYU08A_KA000_K"
    神奈 "「哟呵～那边情况怎么样啦？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBA01"),"True","img/YU_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU030"
    结乃 "「嗯，还不错呢。现在，节目的框架已经大致确定了。」"
    voice "NYU08A_KA001_K"
    神奈 "「终于做好了！那真是太好啦。那么，是怎样的方案？」"
    "神奈的声音一如既往的活力十足，即使没有免提，也能勉强听清。"
    "所以我也能大概了解对话的内容了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBA05"),"True","img/YU_ZBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU031"
    结乃 "「首先，我们确定了节目的主题……」"
    "结乃仔细把方案计划说明清楚，神奈那头似乎在安静地听着。"
    voice "NYU08A_YU032"
    结乃 "「这样做１０分钟的节目，怎么样？」"
    voice "NYU08A_KA002_K"
    神奈 "「…………」"
    "沉重的寂静，果然还是不行吧。"
    voice "NYU08A_KA003_K"
    神奈 "「原来如此～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBC01"),"True","img/YU_ZBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU033"
    结乃 "「你有什么感想么……」"
    voice "NYU08A_KA004_K"
    神奈 "「哈？不是挺好的么，挺像的。」"
    "沉默忽然被打破，手机那里响起了神奈明亮的声音。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBA02"),"True","img/YU_ZBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU034"
    结乃 "「嘿嘿，很像我的风格吗？」"
    "两人的对话似乎都有意的避开了『Ｔ－ｗａｖｅ』的问题。"
    "结乃也不想点破吧。"
    voice "NYU08A_KA005_K"
    神奈 "「啊，不对不对，我说的是像『你们两个人』的风格。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBB06"),"True","img/YU_ZBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU035"
    结乃 "「诶？」"
    "结乃显然没有料到神奈会这么说，一脸迷茫地转过身来望向我。"
    志雄 "「神奈……」"
    voice "NYU08A_YU036"
    结乃 "「唉，唉？」"
    志雄 "「她的意思是，我们『两个人的节目』算是通过了，对吧？」"
    "结乃可能并没有意识到，她平时说道节目的时候总是用着『我的计划』，『我的节目』这样的字眼。"
    "虽然，是结乃找到了『讯息』这个关键词，也处理了很多有关节目的细节问题。"
    "但反过来，我始终有些无奈的寂寞。"
    "结乃应该也在刚才神奈的神来一句之后忽然意识到了吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBB01"),"True","img/YU_ZBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU037"
    结乃 "「啊——啊——啊——原来是这样……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBA06"),"True","img/YU_ZBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "还想说些什么，结果就这么沉默着。她能接收到这样的讯息就足够了吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBA02"),"True","img/YU_ZBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU038"
    结乃 "「哈哈？」"
    志雄 "「没办法呢。」"
    "我当然不会因为这种事情就对结乃不满，反之，她能意识到这点，我真的很开心。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBA01"),"True","img/YU_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU039"
    结乃 "「能让神奈你说ＯＫ，我就放心了。你还有什么建议吗？」"
    voice "NYU08A_KA006_K"
    神奈 "「按着你们的喜欢的去做好了，我只是局外人，就作为可爱的听众了哦！」"
    voice "NYU08A_YU040"
    结乃 "「嗯……不过，还有投稿的事情拜托了。」"
    voice "NYU08A_KA007_K"
    神奈 "「硬要我说说感想的话，虽然你们的节目不是那么特别，但是还是可以做出属于结乃你们的风格……」"
    "神奈一条条耐心的说着，完全不像没有准备的样子，真是用心良苦。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBA02"),"True","img/YU_ZBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU041"
    结乃 "「……谢谢！」"
    voice "NYU08A_KA008_K"
    神奈 "「总之，我也要投稿的吧？不过，说些什么好呢。」"
    voice "NYU08A_KA009_K"
    神奈 "「某个坏蛋抢走了我最好的朋友去做女朋友，我要不要借这个机会好好诅咒一下！」"
    "想必神奈不知道我在偷听吧，就开始拿我开玩笑了。"
    志雄 "「喂，我可是听到了哦。」"
    "我大声的说着，好让手机那头的神奈听见。"
    voice "NYU08A_KA010_K"
    神奈 "「呃，志雄也在那边么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBA01"),"True","img/YU_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU042"
    结乃 "「嗯，在的在的。」"
    voice "NYU08A_KA011_K"
    神奈 "「啊哈～是吗，不过用脚指头也能想到是这样的才对。请替我向他问好。」"
    "神奈态度立刻来了个１８０度大转弯，开始装傻。"
    志雄 "「我都说我听到了哦！」"
    voice "NYU08A_YU043"
    结乃 "「志雄学长说，他—听—到—了—。」"
    voice "NYU08A_KA012_K"
    神奈 "「是，是吗。知道了……那我就祝福你们恩恩爱爱一辈子。」"
    voice "NYU08A_KA013_K"
    神奈 "「嘿嘿，你们就好好期待吧。」"
    play sound "SE02_08"
    "神奈慌慌张张地挂断了电话。"
    "结乃盯着手机看了一会儿，目光转向了我这边。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBB02"),"True","img/YU_ZBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU044"
    结乃 "「啊，就是这样。"
    志雄 "「嗯……我听到了。」"
    "这样看来，神奈肯定会很开心地给我们送来戏弄……用的讯息吧。"
    "一个个朋友拜托过去，不知道能收到多少讯息呢？"
    志雄 "「讯息的筛选也是不是件小事呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBA01"),"True","img/YU_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU045"
    结乃 "「的确，不过……」"
    "总之，时间很紧张。没有太多时间准备，广播里也没有太多的时间去无限制发挥。"
    "前路似乎还是异常坎坷，但是……"
    "总觉得，整个人都被点燃了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBB01"),"True","img/YU_ZBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU046"
    结乃 "「不过，不觉得整个人都沸腾了吗？」"
    志雄 "「…………！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBB03"),"True","img/YU_ZBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU047"
    结乃 "「怎么了？学长。」"
    志雄 "「啊，不是，我现在也想着同样的事情呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBB02"),"True","img/YU_ZBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU048"
    结乃 "「啊哈！真是太好了呢。」"
    志雄 "「要加油啊，结乃。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZBA01"),"True","img/YU_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU08A_YU049"
    结乃 "「是，学长。」"
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
