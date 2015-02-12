label NRI06A:
    $currentlabel = "NRI06A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '21'
    $date = '5'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 5,CAL_0721
    show expression "img/NIMG15E-568h@2x.jpg" as cal zorder 5
    show expression "img/07_21_FRIDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG15NA1@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG15NA1@2x.jpg" as bg0 with dissolve
    play sound "SE05_16L"
    pause (32/32.0)
#FADE_IN 1
    play music  "BGM10"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
#SE_VOLC 1,64
    play sound "SE03_66"
    志雄 "「毛巾、换洗衣物、学习用具……还有泳衣。」"
    "我把一直都在用的泳衣塞进旅行包里。"
    "不过，莉莉丝这家伙真是买了好多东西啊……"
    "看来她对这次的旅行真的很期待。"
    "我也是，这么早就开始准备了，看来我也有些蠢蠢欲动了呢。"
    志雄 "「——呃，现在还把学习用具放在包里干吗！？」"
    "也许我只是想把不想看到的东西封印起来而已。"
    "明明在去旅行之前一定要好好学习才行……"
    "形式上我还是准备带一本过去，不过在那边必然不能正经地学习。"
    play sound "SE02_01"
    志雄 "「……？莉莉丝吗。」"
    window hide
#SCRMODE_SPC SCR_FULL
    play sound "SE02_03"
#FILT_PRI 1
#FILT_IN 48,0,COL_DARK
    if not persistent.dictlist[30] and persistent.show_dict:
        $persistent.dictlist[30]=True
        show screen dict_pop(i=30)
    "Ｆｒｏｍ：　　莉莉丝{p}内容　　：忘记了！{p}明天是芦鹿岛焰火大会，一起去吗？"
#MES "%S032%FS%t002Ｆｒｏｍ：　　莉莉丝%N%t002内容　　：忘记了！%N%t007明天是芦鹿岛焰火大会，一起去吗？%FE%K""
    play sound "SE02_03"
#MESX "%O032"
    window hide
#FILT_OUT 48
#SCRMODE_SPC SCR_WINDOW
    "焰火大会——对了，光顾着旅行的事，差点忘了还有这档子事。"
    "芦鹿岛焰火大会是这里最大的焰火庆典，我每年都和朋友一起去。"
    "大多是和莉莉丝，还有同班同学们一起……不过只有今年是和她两个人去吧。"
    "我回信，『当然去』。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG01NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG01NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SBD04"),"True","img/RI_SBD04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
#FADE_IN 1
    play music  "BGM02"
    voice "NRI06A_RI000"
    莉莉丝 "「好慢啊～！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD04"),"True","img/RI_LBD04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
#BG_BLUR 0
    志雄 "「不好意思，出门的时候被铃逮到了。」"
    "这不是谎言也不是借口，真的是在家门口突然被搭话说『现在去喝一杯吗』。"
    "看来她是稿子写不出来了，准备暂时逃离现实吧。"
    "要是写完了，我应该会把她叫上一起来看焰火大会吧……"
    "总之为了说服铃再次回到办公桌前花了我大概１５分钟。"
    voice "NRI06A_RI001"
    莉莉丝 "「时间不是问题。让女孩子等，这种行为本身就应该受到惩罚！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBC04"),"True","img/RI_LBC04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI06A_RI002"
    莉莉丝 "「在等你的时候被很多怪人搭讪了……」"
    志雄 "「诶？　没，没事吧？。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD04"),"True","img/RI_LBD04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI06A_RI003"
    莉莉丝 "「要是有事的话，就不能在这里和你说话了吧。」"
    志雄 "「是、是呢……太好了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA04"),"True","img/RI_LBA04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI06A_RI004"
    莉莉丝 "「真是的，好了啦。找我搭讪的人都被我的扫堂腿赶跑了。」"
    志雄 "「总、总之，迟到是我不好。作为道歉，会给你买苹果糖的啦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBB01"),"True","img/RI_LBB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI06A_RI005"
    莉莉丝 "「……还有棉花糖。」"
    志雄 "「知道了知道了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBC02"),"True","img/RI_LBC02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI06A_RI006"
    莉莉丝 "「嗯。那就原谅你了～♪」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG93NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG93NA@2x.jpg" as bg0 with dissolve
    play sound "SE08_04L"
#FADE_IN 1
    志雄 "「这次来的人也很多呢。」"
    "环顾四周，人潮涌动。不愧是这一代最盛大的焰火大会，真没办法呢。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,112,96
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA01"),"True","img/RI_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI06A_RI007"
    莉莉丝 "「那么～去哪个摊子呢～？先去吃炒面填饱肚子吧。啊，还有苹果糖和棉花糖不要忘记咯。」"
    志雄 "「刚到就想着吃吗……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA05"),"True","img/RI_LBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI06A_RI008"
    莉莉丝 "「唔，有什么不好，距离放烟花还有一段时间呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA04"),"True","img/RI_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI06A_RI009"
    莉莉丝 "「难道志雄不饿吗？」"
    志雄 "「当然饿……」"
    "今天连晚饭都没吃。在摊头摆出来时吃饭，然后再去看烟花——这种打算真是愚蠢之极。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBC02"),"True","img/RI_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI06A_RI010"
    莉莉丝 "「那首先就去吃炒面吧～♪」"
    hide lh0 with dissolve
    "说着，莉莉丝快步走到了我的前面。"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBC05"),"True","img/RI_XBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_BLUR 0
    志雄 "「等一下，人流这么混杂，要是一个人在前面走的话很容易走散的。我们牵着手走吧。」"
    "这么多人，要是走散了，再想会合会很麻烦。"
    voice "NRI06A_RI011"
    莉莉丝 "「手……？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBB02"),"True","img/RI_XBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI06A_RI012"
    莉莉丝 "「没、没事的。又不是小孩子了。」"
    志雄 "「话是这么说……」"
    "为了防止走散而牵手，这样的理由，对于我们现在的年龄而言很奇怪吗……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBA01"),"True","img/RI_XBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI06A_RI013"
    莉莉丝 "「那么，我们快走吧。」"
    志雄 "「好好。」"
    "真没办法。"
    "总之，还是留意着不要让莉莉丝走开吧。"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    pause (32/32.0)
#SE_VOLC 1,64
#BG_UVC 0,0,512,640,448
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,112,96
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBB01"),"True","img/RI_XBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#FADE_IN 1
    voice "NRI06A_RI014"
    莉莉丝 "「婆婆做的饭固然很好吃，不过，偶尔常常小摊上的料理也很不错呢——」"
    "莉莉丝舔着右手的苹果糖，开心地说道。顺便一提，她的左手拿着的是两袋棉花糖……"
    "虽然她说有一袋是带给富美子婆婆的礼物，不过，一会儿她一定会忍不住自己吃掉的。"
    志雄 "「买这么多能吃完吗？」"
    voice "NRI06A_RI015"
    莉莉丝 "「没关系。对于甜食，我向来是来者不拒的。」"
    志雄 "「……会变胖的哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBA06"),"True","img/RI_XBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI06A_RI016"
    莉莉丝 "「唔……没，没关系的。我有长不胖的体质。」"
    "确实，莉莉丝发福的样子，实在是无法想象……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBA05"),"True","img/RI_XBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    莉莉丝 "「……」"
    "果然是『变胖』这个词对每个女生都有着强大的影响力吗，莉莉丝的视线竟在我和苹果糖之间不断徘徊。"
    window hide
#BG_SET_BACK 
#BG_INIC 3
#BG_PRI 3
#BG_ALPC 3
#BG_POSC 3,,(230+80)
    show expression "img/NIMG17A@2x.png" as bg3 zorder 30:
        xcenter 120/640.0
    with dissolve
#CHR_SORT 1
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
#CHR_COLC 1,128,112,96
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBD05"),"True","img/RI_XBD05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    stop music fadeout 1
#CHR_ALP_AUTOC 0,0,0,F24
#CHR_ALP_AUTOC 1,128,0,F24
#BG_ALP_AUTOC 3,128,0,F24
#BG_POS_AUTOC 358,,F24,40
#CHR_ALP_SAVEC 0
#CHR_ALP_SAVEC 1
#BG_ALP_SAVEC 3
#BG_POS_SAVEC 3
#CHR_SWPC 0
    hide lh1 with dissolve
    莉莉丝 "「嗯！」"
    "突然，她把苹果糖递到我眼前。"
    voice "NRI06A_RI019"
    莉莉丝 "「给你！我现在不想吃苹果味的！」"
    志雄 "「诶，啊，那个……」"
    "这个苹果糖是莉莉丝刚才舔过的，那就是说……"
    "不过，都交往了这么长时间了，现在也不必在意这种事吧？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBD04"),"True","img/RI_XBD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI06A_RI020"
    莉莉丝 "「难得我说要给你，你赶快拿去啊……」"
    "难道说……这家伙也很在意？"
    志雄 "「那个～……」"
    stop sound
    stop music fadeout 132
    voice "NRI05A_CH012A"
    智纱？ "「啊！莉莉丝，塚本君。」"
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
#CHR_COLC 1,128,112,96
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBB03"),"True","img/RI_XBB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#BG_POS_AUTOC 3,,448,,F24,8
#CHR_ALP_AUTOC 0,0,0,F24,8
#CHR_ALP_AUTOC 1,128,0,F24,8
#QUA_CHR 0
#QUA_CHR 1
#BG_POS_SAVEC 3
#CHR_ALP_SAVEC 0
#CHR_ALP_SAVEC 1
#CHR_POSC 0
#CHR_POSC 1
#CHR_SWPC 0
    hide lh1
    hide bg3
    "我和莉莉丝都吃了一惊。莉莉丝光速般的收回了递给我苹果糖的那只手。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_BLUR 0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
#CHR_COLC 0,128,112,96
#CHR_COLC 1,128,112,96
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MJA01"),"True","img/CH_MJA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBB01"),"True","img/RI_MBB01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    play music  "BGM03"
    voice "NRI06A_RI021"
    莉莉丝 "「智纱也来了吗？」"
    voice "NRI06A_CH000"
    智纱 "「嗯，和爸爸妈妈一起。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MJA04"),"True","img/CH_MJA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI06A_CH001"
    智纱 "「说起来，刚才你们两个好像被我吓到了吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBB03"),"True","img/RI_MBB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI06A_RI022"
    莉莉丝 "「没、没这回事。」"
    志雄 "「啊啊，没有啦。」"
    voice "NRI06A_CH002"
    智纱 "「嗯……？」"
    "箱崎侧着头。总不可能告诉她，我们正在为间接接吻的事而感到害羞吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA01"),"True","img/RI_MBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI06A_RI023"
    莉莉丝 "「智、智纱今天穿了浴衣嘛。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MJA01"),"True","img/CH_MJA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI06A_CH003"
    智纱 "「嗯。我说不要穿了，可妈妈说机会难得，叫我穿上。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MJB06"),"True","img/CH_MJB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI06A_CH004"
    智纱 "「很奇怪吗？我平时不穿的，感觉完全不搭调。」"
    "箱崎举起双手，像是为了让我们确认自己的衣服似的，原地转了一圈。"
    志雄 "「不，看起来很合适。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MJB02"),"True","img/CH_MJB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI06A_CH005"
    智纱 "「真的？太好了～」"
    "智纱的表情一下子开朗了起来。"
    志雄 "「嗯。浴衣有一种『日本』的感觉，你穿起来别有一番情调呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MJB01"),"True","img/CH_MJB01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA04"),"True","img/RI_MBA04A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NRI06A_CH006"
    智纱 "「我也这么想。虽然走起路来有些不方便，不过也有种很端庄的感觉。」"
    志雄 "「箱崎平时就给人一种很端庄的感觉呢……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MJB03"),"True","img/CH_MJB03A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA05"),"True","img/RI_MBA05A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NRI06A_CH007"
    智纱 "「是，是吗……？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD05"),"True","img/RI_MBD05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    莉莉丝 "「……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MJA01"),"True","img/CH_MJA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI06A_CH008"
    智纱 "「啊。那么，爸爸和妈妈还在等我，我先走了！」"
    window hide
    stop music fadeout 1
    play sound "SE01_18L"
    hide lh0 with dissolve
    stop se fadeout 1
    "箱崎朝着反方向走入了人群中。"
    志雄 "「浴衣吗……」"
    "穿着那种和平时完全不同风格的服装也挺新鲜的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD02"),"True","img/RI_MBD02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    莉莉丝 "「……」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBD05"),"True","img/RI_XBD05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    hide lh1
    with dissolve
    play sound "SE04_06"
    志雄 "「嗯？」"
    "莉莉丝轻轻踢了我一脚。"
    voice "NRI06A_RI026"
    莉莉丝 "「这是你用不纯洁的眼神看智纱的惩罚。」"
    志雄 "「不、不要乱说——」"
    window hide
    play music  "BGM13"
    pause (8/32.0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBB03"),"True","img/RI_XBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "正当我想反驳时，夜空中绽开了巨大的火花。巨大的爆炸声，盖过了我们的对话。"
    voice "NRI06A_RI027"
    莉莉丝 "「啊……」"
    "两个、三个，五彩缤纷的花瓣尽情的在夜空中飞舞。"
    "我和莉莉丝都完全沉浸在其中，刚才在说的、想说的，都已经忘得一干二净了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBB01"),"True","img/RI_XBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI06A_RI028"
    莉莉丝 "「好大的震撼力啊。明明毎年都来，感觉和以往没什么区别，不过……」"
    志雄 "「是啊……这烟花真漂亮。」"
    "环顾周围，有不少情侣手牵着手，专注地欣赏着烟花。"
    "莉莉丝的手就在我身旁……"
    "她的瞳仁里，映射着天空中闪耀的光芒，兴奋不已。想去握住那只手，却怕惊扰到她那满分的笑容。我笑了笑，也仰起头，和她一同仰望着夜空中花朵，争先恐后地绽放。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
    stop se
    stop sound
    stop music fadeout 1
    $ renpy.end_replay()
    return