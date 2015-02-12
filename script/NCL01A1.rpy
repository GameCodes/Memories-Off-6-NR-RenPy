label NCL01A1:
    $currentlabel = "NCL01A1"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '18'
    $date = '2'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    show expression "img/NIMG19C-568h@2x.jpg" as bg1 zorder 1 with dissolve
#FADE_IN 0
    play sound "SE06_02"
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
    pause
#FADE_OUT 1,32,COL_WHITE
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG07AA3@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG07AA3@2x.jpg" as bg0 with dissolve
    play sound "SE08_10L"
    pause (32/32.0)
#FADE_IN 1,128
    play music "BGM10"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "随着午休铃声的响起，教室里也瞬间被一种慌乱的气氛所包围。"
    "同学们手里拿着各式各样的参考书和复习资料，匆匆忙忙地赶去补习班，图书馆或者是回家进行毫无杂念的复习。"
    志雄 "「果然，到了这个时候，大家就都不一样了呢。」"
    "我不禁叹了口气。"
    stop se
    "明明还记得今年春天刚升到三年级的时候的样子，不知不觉却已经过去三个月了。"
    "这个已经被过于现实的气息所吞噬的教室，到处都散发着紧张、疲惫的味道。"
    "当然，现在也有着必须要考虑的事情。"
    "我凝视着放在桌子上的那张纸。"
    "『志愿调查表』五个字格外的显眼。"
    "志愿一栏却仍然空着。"
    "结果，还是不知道该写些什么呢。"
    "这就是今天要陪伴我一整个下午的东西。"
    "显然，我需要琢磨出一些靠谱的内容来填满它。"
    志雄 "「已经没有时间了。」"
    play sound "SE03_12"
    "我强忍着内心焦躁的情绪，拿起了书包。"
    if not persistent.dictlist[0] and persistent.show_dict:
        $persistent.dictlist[0]=True
        show screen dict_pop(i=0)
    voice "NCL01A_TO000"
    亨 "「志～雄！」"
    window hide
#SE_VOLC 1,64
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_TO001"
    亨 "「啊哈～终于到了这个季节了啊！」"
    志雄 "「什么啊，吓了我一跳。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_TO002"
    亨 "「喂喂，你这是多冷淡的反应啊！青春的光辉正在我们眼前闪耀着呢！」"
    志雄 "「高中最后的暑假……对吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB01"),"True","img/TO_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_TO003"
    亨 "「看吧，你这不是挺清楚的么？」"
    志雄 "「这些天你不是尽说这个来着吗，耳朵都听得快起茧子了。」"
    if not persistent.dictlist[7] and persistent.show_dict:
        $persistent.dictlist[7]=True
        show screen dict_pop(i=7)
    "明明大家都正为自己的未来命运而担忧，亨却恰恰相反。"
    "准确的说，亨真是相当期待这个暑假呢。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA05"),"True","img/TO_MAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_TO004"
    亨 "「行啦，志雄。」"
    voice "NCL01A_TO005"
    亨 "「接下来迎接我们的是最——后——的——暑假唉，可以说是高中生活最后的黄金时间！」"
    voice "NCL01A_TO006"
    亨 "「是弥补这三年来所留下的遗憾，实现没有完成的心愿的最后机会哦。」"
    志雄 "「哈，那倒也是呢。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_TO007"
    亨 "「总之呢！这个夏天，是在高中阶段与莉莉丝发展关系的最后机会了！」"
    志雄 "「所以，还是要去哪里吗……？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA05"),"True","img/TO_MAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_TO008"
    亨 "「那当然咯！」"
    "亨的语气里没有半点玩笑的意思。虽然周围的人都因为即将到来的考试而格外紧张，但这家伙却似乎完全没有被影响，有时候倒真是挺羡慕这样的性格。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_TO009"
    亨 "「我说，我们一起找个地方旅行吧？」"
    志雄 "「诶？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB01"),"True","img/TO_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_TO010"
    亨 "「虽然还稍微早了些，不过真有毕业旅行的感觉呢啊。」"
    志雄 "「嗯，这也是个不坏的主意。」"
    "所谓『毕业旅行』，正如字面，是高三毕业的同学一起去旅行的意思。"
    "但是对于还没有毕业的我们而言，应对考试才是这个夏天的主旋律吧。这个时候要进行旅行，想一想也确实是挺难的。"
    "不过话说回头，亨真正的目标也只有莉莉丝吧，其他同学的参与度在这个大背景下也就显得不重要了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_TO011"
    亨 "「好，既然决定了就趁热打铁！赶快去邀莉莉丝吧！」"
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
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB02"),"True","img/TO_LAB02A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    "话刚说完，亨就拽着我的手腕——"
    志雄 "「慢着，我可没答——」"
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
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA03"),"True","img/TO_MAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_TO012"
    亨 "「请志雄大神帮帮我吧！有你在比较好说话啦！！」"
    志雄 "「什么和什么啊！？」"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 2
#BG_ALPC 0
#BG_UVC 0,(640/4),((448/4)+512),(640/2),(448/2)
#BG_SETWC 0,2,BG08AA,BG08AA
    scene expression "img/BG08AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_SCLC 0,512,512
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XAA04"),"True","img/RI_XAA04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#SE_VOLC 1,128
#FADE_IN 1
    stop music fadeout 1
#THREAD_STA 1,THREAD_RIRISU_DON
    voice "NCL01A_RI000"
    莉莉丝 "「我拒绝！」"
#THREAD_WAT 1
#MESX "%K%P"
    hide bg2 with dissolve
    stop music fadeout 1
    "亨的提议还没说完，就立刻被否决了。"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    window hide
#SE_VOLC 1,64
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320+160)
#CHR_POSC 1,(320-160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA04"),"True","img/RI_MAA04A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    play music "BGM09"
    voice "NCL01A_TO013"
    亨 "「别这么说嘛。就当是为了留下高中最后的回忆！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD04"),"True","img/RI_MAD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL01A_RI001"
    莉莉丝 "「拒绝。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB03"),"True","img/TO_MAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL01A_TO014B"
    亨 "「呃……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD02"),"True","img/RI_MAD02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL01A_RI002"
    莉莉丝 "「这个暑假还是用来学习比较有价值吧，你缺乏作为考生的自觉啊！」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB04"),"True","img/TO_MAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL01A_TO015"
    亨 "「当、当然也会学习的！对吧！？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA05"),"True","img/RI_MAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    志雄 "「别扯到我身上啊……」"
    "就算莉莉丝不说，我也肯定是会以学习为主的，不过亨是不是有这样的觉悟，我就不敢保证了。"
    "莉莉丝斜着眼看了我们一阵，深深地叹了口气。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA06"),"True","img/RI_MAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL01A_RI003"
    莉莉丝 "「唉～你们这样乱来，到最后肯定会吃苦头的哦！」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL01A_TO016"
    亨 "「别这么说嘛。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA04"),"True","img/RI_MAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL01A_RI004"
    莉莉丝 "「很遗憾，今年的夏天我得为了高考而发奋。所以，我拒绝。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB03"),"True","img/TO_MAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL01A_TO017"
    亨 "「怎么这样……」"
    "原本还在挣扎着的亨，在受到莉莉丝的完美最后一击后，彻底跪下了。"
    志雄 "「真不留情面啊……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD04"),"True","img/RI_MAD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL01A_RI005"
    莉莉丝 "「什么嘛，换做是志雄你，还不是得学习，哪有那么多闲工夫。」"
    志雄 "「啊、嗯。那是。」"
    "因为被莉莉丝拒绝而消沉下去的亨显然并没有默默离开的意思，猛的就用另外一个话题强行介入了我和莉莉丝的对话。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL01A_TO018"
    亨 "「对了，你志愿怎么办？」"
    志雄 "「这个嘛……」"
    "眼里浮现出那张慌忙间塞进书包里的，还是空白的『志愿调查表』。"
    志雄 "「你、你有什么打算呢？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA06"),"True","img/TO_MAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL01A_TO019"
    亨 "「我？嗯～还没决定啊！」"
    志雄 "「你这还真干脆……」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB01"),"True","img/TO_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL01A_TO020"
    亨 "「你想，这种事也不能急着做决定，对吧？」"
    志雄 "「那你干嘛瞎操心别人的志愿啊。」"
    voice "NCL01A_TO021"
    亨 "「高考志愿总给人一种『一纸定终生』的感觉啊。作为朋友，我很关心志雄君的将来啊。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD06"),"True","img/RI_MAD06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL01A_RI006"
    莉莉丝 "「志雄的志愿还用得说嘛？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB04"),"True","img/TO_MAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    "看来亨的方法奏效了，不过，加入话题的莉莉丝，脸上挂着不明所以的坏笑。"
    if not persistent.dictlist[3] and persistent.show_dict:
        $persistent.dictlist[3]=True
        show screen dict_pop(i=3)
    voice "NCL01A_RI007"
    莉莉丝 "「他肯定是要和克罗艾学姐报同一个大学的啦～」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    志雄 "「诶？」"
    "连我都对自己下意识的反应有些出乎意料。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA03"),"True","img/RI_MAA03A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB04"),"True","img/TO_MAB04A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    "莉莉丝见了我的反应，更是满脸的意外。"
    voice "NCL01A_RI008"
    莉莉丝 "「咦？怎么，我说错了？」"
    志雄 "「那也是选择之一……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA04"),"True","img/RI_MAA04A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB01"),"True","img/TO_MAB01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    voice "NCL01A_RI009"
    莉莉丝 "「哦，我还以为你早就这么决定了。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA01"),"True","img/RI_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL01A_RI010"
    莉莉丝 "「不过，要考大学是没错的吧？」"
    "大学志愿。这的确是最佳的选择。"
    "可是……那之后呢？那之后我到底想做什么？"
    志雄 "「嗯，我有点自己的想法。」"
    "无言以对，就只好找了这么一句蒙混的话应付过去了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA06"),"True","img/RI_MAA06A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    voice "NCL01A_RI011"
    莉莉丝 "「哦～？」"
    "莉莉丝显然不满意我的回答，但是很快，她就对这些细节失去了兴趣，自己转换了话题。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA04"),"True","img/RI_MAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL01A_RI012"
    莉莉丝 "「说起来，志雄也算是学生会会长吧？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    志雄 "「你这『也算是』听着真刺耳啊。」"
    if not persistent.dictlist[53] and persistent.show_dict:
        $persistent.dictlist[53]=True
        show screen dict_pop(i=53)
    voice "NCL01A_RI013"
    莉莉丝 "「不要在意这些细节啦。去年奏云祭不就因为各种突发情况而忙得不可开交么，就想提醒你今年可要提前上心了。」"
    志雄 "「必须的。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB01"),"True","img/TO_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    "去年的奏云祭的确发生了很多事。当然，也包括，在那过程中我……呃、那个，和克罗艾学姐开始交往了。"
    志雄 "「我想应该没问题。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD04"),"True","img/RI_MAD04A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    voice "NCL01A_RI014"
    莉莉丝 "「这种时候，就算是说假话，也要坚定地说『没问题』啊！」"
    志雄 "「啊、嗯。没问题的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD05"),"True","img/RI_MAD05A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB03"),"True","img/TO_MAB03A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NCL01A_RI015"
    莉莉丝 "「那就好……就算不提留下什么『完美回忆』之类的要求了，这毕竟是最后的奏云祭了」"
    志雄 "「尝到了去年那种忙劲儿，今年就提早了一些开始准备。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC04"),"True","img/RI_MAC04A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA01"),"True","img/TO_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    voice "NCL01A_RI016"
    莉莉丝 "「一点不轻松吧？今年和去年不同，我们也算是备考生了。」"
    志雄 "「话是如此，可学生会会长总不能随便翘班吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD01"),"True","img/RI_MAD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL01A_RI017"
    莉莉丝 "「唉……你把握分寸吧～」"
    window hide
    hide lh0 with dissolve
    "莉莉丝说着耸了耸肩，一个人回家去了。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB01"),"True","img/TO_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL01A_TO022"
    亨 "「那我也回家了，明天见。」"
    志雄 "「嗯，明天见。」"
    window hide
    stop music fadeout 1
#SE_VOLC 1,128
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "『一纸定终生』么……这个词深深的烙在了脑海里。"
    "不过，身为学生会会长，职责在身，现在可不是能抛开一切的时候。"
    志雄 "「总之，事情得一件一件的来。」"
    "志愿是我个人的事，而奏云祭却背负了整个学园学生的美好期望。"
    "要是因为自己的私事分心，导致发生了什么无法挽回的乱子可不是闹着玩的。"
    "给自己鼓了鼓劲，便迈步向学生会室走去。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    #show expression "img/BG09AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression Solid("000") with None
#FADE_IN 0
    play sound "SE00_27"
    志雄 "「打扰了。」"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
    scene expression "img/BG09AA@2x.jpg" as bg0 with dissolve
    play sound "SE00_25"
    play sound "SE08_10L"
#FADE_IN 1
    "因为亨的突发奇想，当我来到学生会室里，干事们已经在为各种工作忙碌起来了。"
    window hide
#SE_VOLC 1,64
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+96)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB01"),"True","img/YU_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
    play music "BGM06"
    voice "NCL01A_YU000"
    结乃 "「啊、学长，辛苦了。」"
    志雄 "「抱歉，我来晚了。工作进度怎样了？」"
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
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA01"),"True","img/YU_LAA01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCL01A_YU001"
    结乃 "「现在正在按班级分配模拟店资格。不出所料，餐饮系的请求比较多呢。这样下去只能抽选通过一部分申请了。」"
    志雄 "「好的，费心了。我能帮点什么忙呢？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA05"),"True","img/YU_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "面对我的请求，春日想了片刻，还是拒绝了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_YU002"
    结乃 "「不用了。今天就我们也没问题的。」"
    志雄 "「诶？可是……」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我看向学生会室里匆匆忙忙的后辈们。"
    "一眼就看得出来，人手紧缺。"
    "应该说，作为学生会长我，更该率先行动起来才对。"
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCL01A_YU003"
    结乃 "「当然了。学长你是会长，肯定也会请你帮忙的。」"
    志雄 "「那……」"
    "春日像是看穿了我的想法似的说道。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA05"),"True","img/YU_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_YU004"
    结乃 "「不过，我们去年就太依赖克罗艾前会长了。」"
    "的确，去年的奏云祭我们将很多事都推给克罗艾学姐了。"
    "正因如此，今年为了挽回这一点，才会打起万分精神开始准备工作……"
    志雄 "「可是人手多一点比较好吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA04"),"True","img/YU_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_YU005"
    结乃 "「那是当然，可是……」"
    "听我一说，她露出了些许为难的表情。"
    voice "NCL01A_YU006"
    结乃 "「如果连身为备考生的学长也要参与进来帮忙的话，就失去提早开始工作的意义了。」"
    志雄 "「呃——」"
    "被她这么一说，我就没什么立场说话了。"
    "可是想到去年的辛苦，也就更不愿意『因为是考生』这样的理由而袖手旁观了。"
    "不管怎么说，这也是我们最后的奏云祭了……"
    志雄 "「随便什么都行，打杂也无所谓哦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_YU007"
    结乃 "「没事的。去年的教训都铭刻在我们心里了～」"
    "说着，春日自豪地挺了挺腰板。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB02"),"True","img/YU_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_YU008"
    结乃 "「学长就有个会长的样子，偶尔巡视一下就可以了～♪」"
    志雄 "「可以吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_YU009"
    结乃 "「是的。所以，你就先回家去学习吧。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB04"),"True","img/YU_LAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_YU010"
    结乃 "「要是最后因为忙于学生会的工作而考试落榜的话，岂不是得不偿失？」"
    志雄 "「的、的确……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB02"),"True","img/YU_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_YU011"
    结乃 "「好了，回去吧回去吧～！」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "春日推着我，把我赶出了学生会室。一路上，遇见的其他干事们也一边做着工作一边朝着这边点头。"
    "真没办法。放弃继续争辩的同时，也真的从心底感谢春日他们的努力。"
    志雄 "「谢谢……」"
    "最后这么说了一句，便离开了学生会室。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG83AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG83AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_15L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,(64/4)
    play music "BGM14"
    志雄 "「备考生么……」"
    "还没决定好志愿的我，也能称得上备考生么？"
    "现在到处都弥漫着考试的紧张感，我的这种心态让我感觉很对不起其他正在努力的人。"
    "刚升上三年级的时候，我的确像莉莉丝说的那样，想和克罗艾学姐上同一所大学。"
    "……然而，要问这究竟是不是自己真正想所的事，我就无言以对了。"
    志雄 "「要说现在想做的事的话，嗯……」"
    "奏云祭。"
    "去年，我奋斗在奏云祭准备工作的前线。"
    "虽说有些事还是没做好，但重要的是，那段时间过的很充实。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
#SE_VOLC 1,128
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
#BG_SWPC 0
#BG_ALPC 1,128
#BG_PRI 0
#BG_PRI 1
    scene expression "img/BG06AA@2x.jpg" as bg0 with dissolve
    志雄 "「可现在，什么忙都帮不上了啊。」"
    "来自后辈们的好意显然不能直接无视掉，强行去帮忙反而会让他们费心……"
    志雄 "「怎么办好呢……」"
    "不由得叹了口气。"
    window hide
    play sound "SE03_15"
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
#SE_WATC 0
    stop music fadeout 1
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_RIRISU_DON
#BG_ALP_AUTOC 0,128,1,F123
#CHR_ALP_AUTOC 0,128,1,F123
#BG_UV_AUTOC 0,0,512,640,448,1,F123
#CHR_SCL_AUTOC 0,128,128,1,F123,8
#BG_ALP_SAVEC 0
#BG_UV_SAVEC 0
#CHR_ALP_SAVEC 0
#CHR_POS_SAVEC 0
#CHR_SCL_SAVEC 0
#EOT