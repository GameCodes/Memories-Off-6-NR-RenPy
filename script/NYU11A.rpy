label NYU11A:
    $currentlabel = "NYU11A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '08'
    $day = '27'
    $date = '0'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 3,CAL_0827
    scene expression Solid("000") with fade
    show expression "img/NIMG15D-568h@2x.jpg" as cal zorder 5
    show expression "img/07_29_SATURDAY@2x.png" as cal_date zorder 6:
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
    play music  "BGM06"
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
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA04"),"True","img/KA_LAA04A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NYU11A_KA000"
    神奈 "「我，喜欢春日结乃！」"
    window hide
#CHR_PRIC ID_ALL
#CHR_SET_BACK
#CHR_INIC 2
#CHR_INIC 3
#CHR_SCLC 2,280,280
#CHR_SCLC 3,280,280
#CHR_ANGC 2
#CHR_ANGC 3,-64
#CHR_POSC 2,-256
#CHR_POSC 3,896
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_SBB02"),"True","img/TO_SBB02A@2x.png") as lh2 zorder (10+2):
        xcenter .3
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_SCA02"),"True","img/MH_SCA02A@2x.png") as lh3 zorder (10+3):
        xcenter .1
        ypos 0.0
    with dissolve


#CHR_POS_SAVEC 2
#CHR_POS_SAVEC 3
    voice "NYU11A_MIX00"
    亨 "「呀～！」"
    麻寻 "「呀～！」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA02"),"True","img/KA_LAA02A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve


#CHR_POS_SAVEC 2
#CHR_POS_SAVEC 3
#CHR_ANGC 2
#CHR_ANGC 3
#CHR_POSC 2,(320-192),576
#CHR_POSC 3,(320+192),512


#CHR_POS_SAVEC 2
#CHR_POS_SAVEC 3
#CHR_ANGC 2
#CHR_ANGC 3


#CHR_POS_SAVEC 2
#CHR_POS_SAVEC 3
#CHR_ANGC 2
#CHR_ANGC 3
    voice "NYU11A_MIX01"
    神奈 "「我也想听到这种台词呐～～」"
    亨 "「我也想听到这种台词呐～～」"
    麻寻 "「我也想听到这种台词呐～～」"
    "今天酪萨克甚是喧嚣。"
    "打工中的亨找到空子就会来到我的座位处闲谈，名叫神奈的新顾客也总让人感到格外的显眼……"
    "对那个样子的神奈兴趣满满地麻寻也趁着没有顾客的时候和亨一起来凑热闹。"
    "然后……一向冷静沉着、稳重、言谈举止十分讲礼貌的结乃也……"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160),448
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC02"),"True","img/YU_LBC02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter .75
    with dissolve
#ROUTINE_STA




#ROUTINE_STP
#CHR_POS_SAVEC 0
#CHR_POS_SAVEC 1
#CHR_ERSWC 2,3
#CHR_PRIC ID_ALL
    voice "NYU11A_YU000"
    结乃 "「不～～行！那个是我专用的！」"
    "在神奈的面前都变成了这样。"
    voice "NYU11A_YU001"
    结乃 "「神奈，我说过的吧？将他人真诚的话语拿来当笑话般戏弄是不好的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NYU11A_KA002"
    神奈 "「不啊……我才没有当笑话来讲，反而是很羡慕呐。」"
    "迄今为止我从未见过的表情，一个接一个地出现着。"
    "这才是真正相互敞开心扉的挚友啊，这就是神奈的能力吗……身为恋人的我可真是功力不够呢……"
    voice "NYU11A_KA003"
    神奈 "「哼……好久不见成熟了不少嘛？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA03"),"True","img/YU_LBA03A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    voice "NYU11A_YU002"
    结乃 "「被三番五次地戏耍之后，谁都会习惯起来的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA03"),"True","img/KA_LAA03A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NYU11A_KA004"
    神奈 "「明明在电话里模仿学园祭的表彰式那一幕的时候，还满脸通红的呢～♪」"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_INIC 3
#CHR_PRIC ID_ALL
#CHR_POSC 2,(320-160)-320
#CHR_POSC 3,(320+160)+320
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh2 zorder (10+2)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA06"),"True","img/MH_MBA06A@2x.png") as lh3 zorder (10+3)
    with dissolve
#ROUTINE_STA




#CHR_ALP_AUTOC 0,0,,

#CHR_ALP_AUTOC 1,0,,


#ROUTINE_STP
#BG_UV_SAVEC 0
#CHR_POS_SAVEC 0
#CHR_POS_SAVEC 1
#CHR_POS_SAVEC 2
#CHR_POS_SAVEC 3
    voice "NYU11A_MA002"
    麻寻 "「诶？什么啊，学园祭那一幕是什么？」"
    voice "NYU11A_TO002"
    亨 "「澄空学园那个最新的传说哦。」"
    window hide
#ROUTINE_STA


#CHR_ALP_AUTOC 0,128,,

#CHR_ALP_AUTOC 1,128,,




#ROUTINE_STP
#BG_UV_SAVEC 0
#CHR_POS_SAVEC 0
#CHR_POS_SAVEC 1
#CHR_ERSWC 2,3
#CHR_PRIC ID_ALL
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,YU_LXB05,3,F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB05"),"True","img/YU_LBB05A@2x.png") as lh0 zorder (20):
        ypos 0.0
        xcenter .8
    with dissolve
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#REEK_CHR 0
    voice "NYU11A_YU003"
    结乃 "「什、什么啊神奈，你怎么知道我脸红了的！？」"
#REMOVE_REEK_CHR 0
#THREAD_STP 1
    hide bg3 with dissolve
#BG_PRI 3
    voice "NYU11A_KA005"
    神奈 "「我当然知道啦，因为是挚友啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NYU11A_KA006"
    神奈 "「不过呢，还真的有满脸通红呢，我可是刚刚才知道的哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC02"),"True","img/YU_LBC02A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    voice "NYU11A_YU004"
    结乃 "「诱……诱导的询问禁止啦～！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA03"),"True","img/KA_LAA03A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NYU11A_KA007"
    神奈 "「哦呵呵、又变红了呢，真是个可爱的人啊。」"
    "看来还是神奈要高上二三等。不愧是初代的『凯尔玛妹妹』。"
    "此时此刻我的大脑中正把眼前的一切组织起来，变成有趣又好玩的稿件然后投稿给『Ｔ－ｗａｖｅ』。"
    "就算被戏弄也要当做事不关己……如今就暂且在一旁学石头一样沉默忍耐吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA04"),"True","img/KA_LAA04A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
#MESEX_A M_NOA,A_CH_KA,NYU11A_KA008,"【神奈】「…………」%K%P"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC01"),"True","img/YU_LBC01A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    "偶然一瞥，发现神奈正直勾勾地看着我，"
    志雄 "「怎……怎么了？」"
#CHR_PRIC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA04"),"True","img/KA_XAA04A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    "神奈她边凝视着边把脸靠近了过来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA08"),"True","img/KA_XAA08A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NYU11A_KA009"
    神奈 "「志雄。要是让这么可爱的结乃不幸福的话，我一定会加倍奉还给你的！」"
    "……相当认真的眼神啊。"
    志雄 "「我一定铭记于心。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC02"),"True","img/YU_LBC02A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    voice "NYU11A_YU005"
    结乃 "「等等神奈！？还有，志雄学长别说多余的话了啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA02"),"True","img/KA_LAA02A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
#CHR_PRIC 1
    voice "NYU11A_KA010"
    神奈 "「这可不是多余的话哦～广播大赛的奖金不是计划要用在你和志雄两个人的温泉旅行上吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB06"),"True","img/YU_LBB06A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    voice "NYU11A_YU006"
    结乃 "「呀！真是的，说什么呢！」"
    志雄 "「诶？那是什么，完全没有听过哦，那种事情。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA08"),"True","img/KA_LAA08A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NYU11A_KA011"
    神奈 "「真是的，就是因为如此，我才忠告如果让她不幸福的话我一定加倍奉还！志雄可真是太迟钝了啊！！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC02"),"True","img/YU_LBC02A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    voice "NYU11A_YU007"
    结乃 "「真是的～不要喋喋不休地说那些不说也罢的事情啦！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA04"),"True","img/KA_LAA04A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NYU11A_KA012"
    神奈 "「说不说什么的是我来决定的。因为最后温泉计划也是因为你才没有实现的。」"
    志雄 "「啊……是这样啊？」"
    "无论如何也要获胜。结乃一直那样说的理由现在我终于明白了。"
    "是想要用获胜的奖金，来和我去旅行啊……"
    voice "NYU11A_KA013"
    神奈 "「不过，可惜的是１０万日元没有拿到呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC03"),"True","img/YU_LBC03A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    志雄 "「也是呢啊……」"
    结乃 "「…………」"
#MESEX_A M_NOA,A_CH_YU,NYU11A_YU008,"【結乃】「…………」%K%P"
    "是的，我们在那个直播的决胜战里，彻底地输了。"
    "最佳优胜奖也好，准优胜奖也好，都被其他的队伍拿走了，第三名以下的分数没有公布。"
    "毋庸置疑，我在最后的时候乱来的直接导致我们的节目出局。"
    "本来只要计算好时间，将信息传送给结乃就能１０分钟内结束掉的……但是由于节目内容太过有趣了而使得计算出了差错……"
    "我做了无法原谅的事情呢……"
    "不过，就观众的反响来说我们是当之无愧的第一呢……至少我们已经非常满足了。"
    "没有后悔。"
    voice "NYU11A_YU009"
    结乃 "「诶……真想去旅行啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA07"),"True","img/KA_LAA07A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NYU11A_KA014"
    神奈 "「真是的，刚说完不可以不幸福，就立刻露出那种表情了。」"
    志雄 "「对不起啊，我真是做了件不靠谱的事呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NYU11A_KA015"
    神奈 "「真没办法。为消沉的结乃奉上最好的礼物好了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB02"),"True","img/YU_LBB02A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    voice "NYU11A_YU010"
    结乃 "「诶？什么什么！？」"
    "刚才一直叹息着的结乃，此时抬起头来。刚才脸上忧郁的表情也一扫而空。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA07"),"True","img/KA_LAA07A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NYU11A_KA016"
    神奈 "「一点都没变呢，真是个肤浅的家伙。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB04"),"True","img/YU_LBB04A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    voice "NYU11A_YU011"
    结乃 "「才没有呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA02"),"True","img/KA_LAA02A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NYU11A_KA017"
    神奈 "「算了，不和你计较！好，请大家注意咯——！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    stop music fadeout 132
    "神奈拍着双手宣布道。"
    "连刚刚回去工作的亨与麻寻，也好奇地看着这边。"
    voice "NYU11A_KA018"
    神奈 "「当当当，当～」"
    "神奈拿出一个豪华的袋子，交给了结乃。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA03"),"True","img/KA_LAA03A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NYU11A_KA019"
    神奈 "「这次我来，正是为了将这个『广播比赛评委特别奖』颁发给『浜咲讯息』的！」"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,YU_LXB05,3,F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB05"),"True","img/YU_LBB05A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    志雄 "「什么！？」"
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#REEK_CHR 0
    voice "NYU11A_YU012"
    结乃 "「评委……特别奖！？」"
#REMOVE_REEK_CHR 0
#THREAD_STP 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA02"),"True","img/KA_LAA02A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    play music  "BGM13"
    voice "NYU11A_KA020"
    神奈 "「恭喜你们了哦！顺便一提，附加奖品是这个温泉旅行的招待券～！」"
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#REEK_CHR 0
    voice "NYU11A_YU013"
    结乃 "「温泉旅行～！真的吗！？」"
#REMOVE_REEK_CHR 0
#THREAD_STP 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA07"),"True","img/KA_LAA07A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NYU11A_KA021"
    神奈 "「我才不会去编这么复杂的谎言呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA04"),"True","img/KA_LAA04A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NYU11A_KA022"
    神奈 "「你以为我是谁。我可是大赛的前任冠军兼浜咲ＦＭ兼职中的神奈大人哦！」"
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#REEK_CHR 0
    voice "NYU11A_YU014"
    结乃 "「是、是吗！所以神奈你……」"
#REMOVE_REEK_CHR 0
#THREAD_STP 1
    hide bg3 with dissolve
#BG_PRI 3
    "这样说的话，神奈来这里的旅费是浜咲ＦＭ提供的呢，貌似有说过这样的事情……原来这也是工作吗？"
    "所以，也就是说她是跑腿的？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NYU11A_KA023"
    神奈 "「哈，结乃。这个是你们的东西了哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC04"),"True","img/YU_LBC04A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    voice "NYU11A_YU015"
    结乃 "「神奈……谢谢你～」"
    "神奈是否也注意到了这件事呢……但是，在这值得庆贺的场面说这种扫兴的话实在是有些不妙，还是不要提的为好。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBB01"),"True","img/YU_XBB01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    志雄 "「太好了，结乃。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBA06"),"True","img/YU_XBA06A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    voice "NYU11A_YU016"
    结乃 "「嗯……这样的话，与学长两个人……一起去温泉……」"
    志雄 "「真的要……两个人去吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBA01"),"True","img/YU_XBA01A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    voice "NYU11A_YU017"
    结乃 "「我不是已经说过很多次了吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBB01"),"True","img/YU_XBB01A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    voice "NYU11A_YU018"
    结乃 "「想创造出只属于咱们两个人的回忆。」"
    "两个人的……只属于两个人的回忆……吗？"
    "的确，制作广播的时候，也是一直坚持要二人来做来着……"
    "那天在晚霞时分的屋顶上，因为回到了原点而变得不怎么提起这句话了……其实这就是结乃的愿望啊。"
    "这个愿望我无论如何也要实现。"
    志雄 "「那咱们两个就一起去吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBB02"),"True","img/YU_XBB02A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    voice "NYU11A_YU019"
    结乃 "「好……好的！」"
    window hide
    stop music fadeout 1
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
#CHR_POSC 0,(320+192)
#CHR_POSC 1,(320-192)
#CHR_POSC 2
#CHR_SETTC 0,1,2,YU_MBA01,TO_MBB01,KA_MAA01
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,YU_LXB05,3,F24
    play music  "BGM10"
#FADE_IN 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA01"),"True","img/YU_MBA01A@2x.png") as lh0 zorder (20):
        xcenter .2
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh1 zorder (20+1):
        xcenter .8
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_MAA01"),"True","img/KA_MAA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    voice "NYU11A_TO003"
    亨 "「诶～不过真是太神奇了啊。特别奖的附加奖品居然恰好就是双人温泉住宿招待券。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_MAA10"),"True","img/KA_MAA10A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU11A_KA024"
    神奈 "「诶？不是哦，我可没说是双人温泉住宿招待券。」"
    stop music fadeout 132
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBB05"),"True","img/YU_MBB05A@2x.png") as lh0 zorder (20):
        xcenter .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh1 zorder (20+1):
        xcenter .8
    with dissolve
    voice "NYU11A_TO004"
    亨 "「咦？」"
    志雄 "「嗯？」"
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#REEK_CHR 0
    voice "NYU11A_YU020"
    结乃 "「诶？」"
#REMOVE_REEK_CHR 0
#THREAD_STP 1
    hide bg3 with dissolve
#BG_PRI 3
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_MAA02"),"True","img/KA_MAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU11A_KA025"
    神奈 "「附加奖品是温泉旅行的团体住宿劵哦～♪」"
    志雄 "「啊，也、也就是说！？」"
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
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA04"),"True","img/TO_XBA04A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    play music  "OBGM18"
    voice "NYU11A_TO005"
    亨 "「志～雄～，你还没还给我『猫大人』的人情呢吧～？对吧～？也带上我吧～」"
    "亨露出如同亡灵般的表情缠到了我的身边。"
    志雄 "「那不行的吧，说要靠自己想办法解决的人是你吧！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA02"),"True","img/TO_XBA02A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    voice "NYU11A_TO006"
    亨 "「还不止如此！结果我采访素材也没有用上吧！感觉超寂寞的！」"
    志雄 "「是被广播局否决的！你自作自受！」"
    "至于亨究竟些了些什么……这个问题就不要再追究了，让它永远地封印在过去的时空里吧。"
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
#CHR_POSC 0,(320+160)
#CHR_POSC 1,(320-160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC04"),"True","img/YU_LBC04A@2x.png") as lh0 zorder (20):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh1 zorder (20+1):
        xcenter .75
    with dissolve
    voice "NYU11A_YU021"
    结乃 "「啊啊……专属于两个人的……旅行啊……」"
    voice "NYU11A_KA026"
    神奈 "「当然，我也会去的。我必须在志雄的毒牙之下保护我最好的挚友哦～」"
    "在我被亨缠住的同时，神奈说了很不靠谱的话语。"
    志雄 "「喂，那边！不要胡说些莫名其妙的话！」"
    voice "NYU11A_TO007"
    亨 "「我很寂寞的啊～，志～雄～！」"
    window hide
#VIB_DOUKI 
#QUA3_ALL 
#VIB_STP 
    with vpunch
    志雄 "「哇。」"
    "亨从我背后扑了上来。"
    "你是背后灵吗！"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBB03"),"True","img/TO_XBB03A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    志雄 "「你啊，约上莉莉丝坐着『猫大人』去飞翔吧！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBB01"),"True","img/TO_XBB01A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    voice "NYU11A_TO008A"
    亨 "「对啊！也约上莉莉丝一起去温泉吧！那样的话自然的智纱也会来的。{w=5}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBB02"),"True","img/TO_XBB02A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    voice "NYU11A_TO008B"
    extend "嗯，一定会非常热闹的！」"
    "亨自顾自地增加着邀请的人数，而麻寻则正给谁打着电话。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA01"),"True","img/MH_LCA01A@2x.png") as lh0 zorder (20):
        ypos 0.0
    with dissolve
    voice "NYU11A_MA003"
    麻寻 "「啊，喂喂，信吗？有好事情告诉你，是温泉哦，温泉……诶？已经够了？你说什么呢啊，那可是温泉哦？」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "明明想着是一次只属于两个人的温泉旅行呢……"
    "不过，团体招待劵，总共可以带几个人去呢？把大家都带去行吗？"
    志雄 "「算了，爱怎样怎样吧……」"
    "我无奈地摇了摇头。"
    "这样说的话，帮助收录工作的亨与麻寻是肯定的，还有包括帮助投稿的大家在内，邀请大家一起去温泉好了。"
    "谁要大家都这么兴奋呢。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU12A")]=True
    show expression "img/EVN_YU12A@2x.jpg" as bg1 with dissolve
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NYU11A_YU022"
    结乃 "「志雄学长……」"
    "结乃嘟着嘴说道，不满情绪明显已经膨胀到极限了。"
    voice "NYU11A_YU023"
    结乃 "「绝对，绝～对！有时间一定要做一次只属于两个人的旅行哦！」"
    志雄 "「啊，说好了哦。」"
    voice "NYU11A_YU024"
    结乃 "「和我拉钩吧。」"
    window hide
#BG_SET_BACK 
#BG_INIC 3
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU12B")]=True
    show expression "img/EVN_YU12B@2x.jpg" as bg3 zorder 3 with dissolve
#BG_FLG EVN_YU12B
    hide bg1 with dissolve
    pause (32/32.0)

#BG_POS_SAVEC 3
#BG_SET_BACK 
#BG_INIC 0
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU13A")]=True
    show expression "img/EVN_YU13A@2x.jpg" as bg0 zorder 0 with dissolve
    pause (64/32.0)
    hide bg3 with dissolve
    "结乃强行地拉起我的手，用小指与我的小指勾在了一起。"
    voice "NYU11A_YU025"
    结乃 "「啊对了，还要给『Ｔ－ｗａｖｅ』发一封起誓的投稿，当然我也会写的！」"
    "感觉约定的内容在不断增加，这样拉钩的话会不会很吃亏啊？"
    voice "NYU11A_YU026"
    结乃 "「拉钩上吊，一百年不许变～拉钩了哦！」"
    "结乃松开了勾好的小指，露出了十分满足的笑容。"
    voice "NYU11A_YU027"
    结乃 "「那这一次就勉为其难的改变计划，大家一起热热闹闹地去温泉旅行吧！」"
    "结乃这么说完，就奔向了在对面起草旅行计划的神奈那里。"
    志雄 "「真是的，真没办法啊。」"
    "两个人的旅行吗……"
    "今年我要备考，明年则是结乃……这个约定看来又要等很久才能兑现了。"
    志雄 "（虽然如此……）"
    "我看了看刚才和结乃拉钩的小指。"
    "手指相勾，我们的心也紧紧地连接在了一起。"
    "所以，这个约定，无论隔多久还没有实现，我都不会忘记。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU13B")]=True
    show expression "img/EVN_YU13B@2x.jpg" as bg0 with dissolve
    voice "NYU11A_YU028"
    结乃 "「喂，学长，干什么呢，快点过来一起啊！」"
    志雄 "「好好，这就过去～」"
    "我们间的羁绊不知不觉变得更加的坚固，绝对不会有断点。"
    "我能够如此坚信，这个夏天，我创造了不朽的记忆。"
    "虽然夏天即将结束……我们在一起的日子却会永远的延续下去。"
    window hide
#MUS_VOL 255
    pause (128/32.0)
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1,128,COL_WHITE
    stop se
    stop sound
    stop music fadeout 1
#BG_SET_BACK
#BG_INIC 0
    scene expression "img/EVN_YU13C-568h@2x.jpg" as bg0 zorder 0 with dissolve
#FADE_IN 1
    pause (96/32.0)
#FADE_OUT 1
#GRAPH_ERS
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT
