label NCL10A:
    $currentlabel = "NCL10A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '08'
    $day = '12'
    $date = '6'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/NIMG03D@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/NIMG03D@2x.jpg" as bg0 with dissolve
    play sound "SE05_14L"
    pause (32/32.0)
#FADE_IN 1,128
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
    "感受到从窗帘间隙中照进来的阳光，我醒了过来。"
    志雄 "「真不想起床……」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    play sound "SE03_28"
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
#BG_SWPC 0
#BG_ALPC 1,128
#BG_PRI 0
#BG_PRI 1
    scene expression "img/BG15MA2@2x.jpg" as bg0 with dissolve
    "我耷拉着意识仍有些模糊的脑袋，下床站了起来。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
#FADE_IN 0
    show expression "img/NIMG15A-568h@2x.jpg" as cal zorder 5
    show expression "img/08_12_SATURDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
#CAL_DSP_GRP 5,CAL_0812
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG33AA@2x.jpg" as bg0 zorder 0 with dissolve
#FADE_IN 1
    "换好衣服，走出自己的房间。打算去洗脸的我走进客厅，学姐竟然已经起床了。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(448/8)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_SAC03"),"True","img/CL_SAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "OBGM08"
    voice "NCL10A_KU000"
    克罗艾 "「呼……」"
    "正当我想说早上好的时候，听到了那样的叹气声。"
    "和亨他们一起聚会吃料理之后的第二天，学姐恢复了些精神，这完全要拜和许久未见的朋友们一起开心说笑所赐。"
    "不过，总体来说，学姐依旧没有完全恢复正常的状态。"
    志雄 "「早上好，学姐。」"
    "我不想让学姐察觉到我的想法，所以尽量用有朝气的声音说道。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_SAC01"),"True","img/CL_SAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU001"
    克罗艾 "「啊，早上好，志雄。」"
    "听到我的声音抬起头来的克罗艾学姐，也立刻就换成明朗的表情。"
    "看到学姐这样的转变，我的胸中一紧。"
    "虽然我希望学姐把我当做可以倾诉烦恼的对象。不过，学姐不想让我担心的心情，也不得不理解。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_SAB03"),"True","img/CL_SAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU002"
    克罗艾 "「怎么了？」"
    志雄 "「哎？没有，只是还有些迷糊……」"
    "大概是因为我看起来好像在思考着什么。学姐看向我的视线里多了一份担心，为了不让学姐察觉我的心情，我有些慌张地随口找了个理由。"
    hide lh0 with dissolve
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB03"),"True","img/CL_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU003"
    克罗艾 "「真的吗？最近好像都学习到很晚的样子，要不要再睡一下？」"
    志雄 "「真的不要紧的……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB04"),"True","img/CL_LAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU004"
    克罗艾 "「哦。但是，不要勉强哦？」"
    志雄 "「我知道的。」"
    "重复地肯定了几次，学姐总算是接受了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB06"),"True","img/CL_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU005"
    克罗艾 "「那就吃早饭吧。」"
    "被面带笑容的学姐催促着，我来到饭桌前。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/EXBG09A@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/EXBG09A@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAA01"),"True","img/CL_ZAA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (32/32.0)
#FADE_IN 1
    play music "BGM04"
    "吃完早饭的我和克罗艾学姐，在客厅里喝着饭后的茶水。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAA02"),"True","img/CL_ZAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU006"
    克罗艾 "「喂，志雄……」"
    志雄 "「嗯，怎么了？」"
    voice "NCL10A_KU007"
    克罗艾 "「虽然不好意思，不过过一会儿还要打工，所以今天没办法辅导你学习了。」"
    志雄 "「没关系，不要在意。」"
    "面对一脸抱歉的学姐，我慌忙摇了摇头。学姐一直在辅导我学习，我这边才是应该感谢，学姐没有道歉的理由。"
    志雄 "「我没关系的。学姐好好打工就行了。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAA01"),"True","img/CL_ZAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU008"
    克罗艾 "「谢谢。傍晚就会回来的。」"
    志雄 "「那样的话，晚饭怎么办？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB02"),"True","img/CL_ZAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU009A"
    克罗艾 "「是呢……{w=4}{nw}"
#MESA A_CH_KU,NCL10A_KU009A,"【クロエ】「是呢……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU009B"
    extend "偶尔去外面去吃一次吧？」"
    "这两天一直在家里学习，这估计是个呼吸新鲜空气的好机会。"
    "但是等一下，那样的话……我想起了在暑假开始的时候与学姐之间的约定。"
    志雄 "「好不容易的机会，要放焰火吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB03"),"True","img/CL_ZAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU010"
    克罗艾 "「焰火？」"
    志雄 "「嗯。在焰火大会那天约好的吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB04"),"True","img/CL_ZAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU011"
    克罗艾 "「是呢……」"
    "不知学姐是不是想起了那天的事情，脸上浮现了笑容。"
    志雄 "「准备就交给我吧。打工结束的时候，我会去接你的。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU012"
    克罗艾 "「嗯，那就拜托你了。打工结束大概是５点左右……放完焰火之后再吃晚饭吧。」"
    show expression "img/BG33AA@2x.jpg" as bg_over zorder 2 with dissolve
    "说着，克罗艾学姐一幅很开心的样子准备要去打工。"
    "学姐刚要出门，突然停了下来。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC01"),"True","img/CL_MAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL10A_KU013"
    克罗艾 "「对了。你差不多该整理大学历届招生的试题集了哦。」"
    志雄 "「历届试题集吗？」"
    voice "NCL10A_KU014"
    克罗艾 "「嗯。出题倾向之类的，提前了解的话对考试很有帮助。」"
    志雄 "「我知道了。既然这样，那我就去下书店吧。」"
    "听了我的回答，学姐使劲地点了点头。虽然有在全力备考，可是前途依旧看不到光。"
    show expression "img/OIBG012A@2x.png" as bg_over zorder 2 with dissolve
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU015"
    克罗艾 "「那我就出发了。」"
    志雄 "「嗯，路上小心。」"
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
    play sound "SE00_01"
    window hide
    show expression "img/BG33AA@2x.jpg" as bg0 with dissolve
    scene expression "img/BG33AA@2x.jpg" as bg0 with dissolve
    "目送学姐到玄关，我又回到了客厅。"
    window hide
    show expression "img/EXBG09A@2x.jpg" as bg0 with dissolve
    scene expression "img/EXBG09A@2x.jpg" as bg0 with dissolve
    志雄 "「哈……」"
    "坐到椅子上，我叹了口气。"
    window hide
    play music "BGM14"
    志雄 "「考大学吗……」"
    "８月过半。应该是开始准备考试的时候了……"
    "要考的大学，还没有决定。"
    "不。其实我想要和学姐去同一所大学的。"
    "不过，考虑到自己的将来，那样真的好吗，自己无法判断。"
    志雄 "「就算烦恼也解决不了的事情。」"
    window hide
    show expression "img/BG33AA@2x.jpg" as bg0 with dissolve
    scene expression "img/BG33AA@2x.jpg" as bg0 with dissolve
    "一直在家里这样待着，只会让思考的范围变得越来越窄。"
    "总之，先去趟书店吧，这么想着，我把钱包放进口袋。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG03AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG03AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_14L"
    pause (32/32.0)
    play sound "SE01_04L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,64
    pause (32/32.0)
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/BG04AA@2x.jpg" as bg0 zorder 0 with dissolve
    hide bg1 with dissolve
    pause (32/32.0)
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 1
#BG_SETWC 0,1,BG02AA,NIMG01B
    scene expression "img/BG02AA@2x.jpg" as bg0 with dissolve
    play sound "SE08_17L"
    pause (32/32.0)
    play sound "SE05_15L"
    pause (32/32.0)
#EFF_STAC 0,CLOUD_B,EFF_SKIP
#FADE_IN 1
    "炽热阳光火辣辣的，从头上直射下来。"
    "在商店街的书店里转了好几圈，我不禁再一次叹着气。"
    志雄 "「果然还是决定不了目标啊……」"
    "在放着试题集的书架前看过来看过去，结果还是什么都没有买就走出了书店。"
    window hide
    stop se fadeout 1
#SE_VOLC 1,255
#FADE_OUT 1,16
##BG_ALP_AUTOC 1,0,1,F24
    hide bg1 with dissolve
#EFF_STPC 0,EFF_SKIP
#FADE_IN 1,16
    stop se
    "就那样的没有目标的环视着商店街。"
    志雄 "「没有时间了呢……」"
    "胸中的焦急感膨胀的厉害。倒不如去找谁谈谈的话就好了……"
    stop music fadeout 1
    voice "NCL10A_NO000"
    诺艾儿 "「啊！是大哥哥！」"
    志雄 "「诶？」"
    "突然的听到背后有人叫我。同时在腰的附近，感觉到什么抱了过来。"
    window hide
#SE_VOLC 1,128
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA01"),"True","img/NO_LBA01A@2x.png") as lh0 zorder 100:
        ypos .2
    with dissolve
    play music "BGM08"
    voice "NCL10A_NO001"
    诺艾儿 "「大哥哥好～」"
    "……是诺艾儿。"
    志雄 "「你好。刚好出门吗？」"
    "因为事出突然，下意识地盘问起来。不过诺艾儿还是一副高兴的表情，一字一句的回答道。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA02"),"True","img/NO_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL10A_NO002"
    诺艾儿 "「嗯！和爸爸妈妈一起！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_PRIC 1
#CHR_ALPC 1
#CHR_POSC 1,(320+160)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_SAA03"),"True","img/YS_SAA03A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .75
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR0 0
#MOV_CHR1 128
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
    hide lh0 with dissolve
    voice "NCL10A_EL000A"
    爱丽丝 "「真是的，诺艾儿你。那个，抱歉，突然的……{w=7}{nw}"
#CHR_ALPC 0,128
#CHR_PRIC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA06"),"True","img/YS_MAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL10A_EL000B"
    extend "咦，是志雄？」"
    志雄 "「您好。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2,(320-160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA01"),"True","img/YZ_MAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    with move
    voice "NCL10A_KZ000"
    幸蔵 "「啊，志雄君。好久不见。」"
    志雄 "「您好。您身体怎么样了？」"
    "不经意间问出了心中惦记的事情。学姐的父亲脸上浮现出了笑容，用抱有几分歉意的语气说道。"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAB02"),"True","img/YZ_MAB02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL10A_KZ001"
    幸蔵 "「啊，也让你担心了呢。虽然还定期去医院，不过已经不要紧的了。」"
    志雄 "「那真是太好了。」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA01"),"True","img/YZ_MAA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL10A_EL001"
    爱丽丝 "「咦，今天没有和克罗艾一起吗？」"
    志雄 "「嗯。克罗艾今天去打工了。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA06"),"True","img/YS_MAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL10A_EL002"
    爱丽丝 "「打工吗……」"
    志雄 "「对……您不知道吗？」"
    "克罗艾学姐明明说和家里人说过了……"
    "看到两人都是一副惊讶的表情，学姐的父亲，有些困扰的问道。"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAB03"),"True","img/YZ_MAB03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL10A_KZ002"
    幸蔵 "「……没有说过吗？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA04"),"True","img/YS_MAA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL10A_EL003B"
    爱丽丝 "「我没听说过……」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA06"),"True","img/YZ_MAA06A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL10A_KZ003"
    幸蔵 "「不过，克罗艾也是大学生了。打工也没什么问题的吧。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA03"),"True","img/YS_MAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL10A_EL004"
    爱丽丝 "「倒不是那个意思呢。既然要去打工，怎么也应该和家里说一下吧……」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA03"),"True","img/YZ_MAA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    "母亲哑然的伫立在那里，叹着气。"
    志雄 "「那，那个……」"
    voice "NCL10A_EL005"
    爱丽丝 "「啊，对不起。我不知不觉的就……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA01"),"True","img/YZ_MAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    "总之是岔开话题了。我感觉到学姐并不打算拉近和家里人之间的距离，气氛也显得稍稍有些凄凉……"
    志雄 "「那个，大家是去买东西吗？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA01"),"True","img/NO_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL10A_NO003"
    诺艾儿 "「去买焰火！」"
    志雄 "「焰火？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA02"),"True","img/NO_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL10A_NO004"
    诺艾儿 "「嗯！夏日特有的风物诗～」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA02"),"True","img/YZ_MAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL10A_KZ004"
    幸蔵 "「说到夏天，想到的就是焰火呢。前段时间的焰火大会也没有去。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA02"),"True","img/YS_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    志雄 "「是这样啊。」"
    "我不禁有些愕然，竟然有如此的巧合。"
    "在约好和克罗艾学姐一起放焰火的这一天，学姐的家里人也要放焰火。"
    "把这个作为契机，大家一起放焰火的话。感觉会有好的发展。"
    "就在我考虑那个的时候，诺艾儿抑制不住欢喜的声音喊道。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB01"),"True","img/NO_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL10A_NO005"
    诺艾儿 "「喂喂，大哥哥你们也来一起放焰火吧！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA03"),"True","img/YS_MAA03A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA01"),"True","img/YZ_MAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    voice "NCL10A_EL006"
    爱丽丝 "「诺艾儿……姐姐有工作，哥哥要复习考试的哦？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB04"),"True","img/NO_MBB04A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL10A_NO006"
    诺艾儿 "「不行吗？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA04"),"True","img/YS_MAA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL10A_EL007"
    爱丽丝 "「不能让别人困扰的。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB03"),"True","img/NO_MBB03A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    志雄 "「那、那个！好不容易的机会，我们也一起可以吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB01"),"True","img/NO_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA03"),"True","img/YS_MAA03A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    voice "NCL10A_EL008"
    爱丽丝 "「咦？但是……」"
    志雄 "「事实上，在克罗艾打工结束了之后，我们也打算去放焰火的……」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL10A_EL009"
    爱丽丝 "「这样啊……」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAB02"),"True","img/YZ_MAB02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL10A_KZ005"
    幸蔵 "「还真是巧呢。好吧，那样就要去多买点儿焰火了。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA09"),"True","img/NO_MBA09A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL10A_NO007"
    诺艾儿 "「多买点儿是多少？」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA02"),"True","img/YZ_MAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL10A_KZ006"
    幸蔵 "「是啊，就买到诺艾儿自己一个人抱不了的程度那么多吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA02"),"True","img/NO_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA03"),"True","img/YS_MAA03A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    voice "NCL10A_NO008"
    诺艾儿 "「万岁～！」"
    voice "NCL10A_EL010"
    爱丽丝 "「也不需要那么多吧……」"
    "学姐的母亲，看着诺艾儿和父亲两个人你一言我一语地说着不禁深深地叹了口气。"
    志雄 "「地点我来决定可以吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA01"),"True","img/YZ_MAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    voice "NCL10A_EL011"
    爱丽丝 "「嗯，那可是帮大忙了。我好久没到这边来了，她爸对这边也不是太了解」"
    "就这样，我告诉了他们今天打算去放焰火的海岸的位置。由于傍晚我还要去接学姐，所以最后决定到现场集合。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA01"),"True","img/NO_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL10A_KZ007"
    幸蔵 "「那接下来。我们就继续去买东西了……志雄的打算呢？」"
    "本来想要回答回家去学习，可实际上并没有说出来。"
    "和学姐的家人商量下志愿的问题怎么样呢？脑中产生了这样的想法。"
    "学姐的爸爸，完全看不出大病初愈的样子，稳稳地站在那里。"
    "作为学姐的目标，学姐所憧憬的，自立的社会人。"
    志雄 "「没，没有特别想要做的事。虽然是这样……」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAB02"),"True","img/YZ_MAB02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL10A_KZ008"
    幸蔵 "「这样啊。那样的话要一起吗？」"
    志雄 "「要是不打扰的话」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA02"),"True","img/YS_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL10A_EL012"
    爱丽丝 "「啊，那机会难得，咱们好好地聊一聊吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA02"),"True","img/NO_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL10A_NO009"
    诺艾儿 "「聊一聊吧～」"
    window hide
    stop music fadeout 1
    play sound "SE01_03L"
    hide lh0 with dissolve
    "一边用着和妈妈极为相似的口气说着，诺艾儿沿着道路向前快速地跑着。"
    stop se fadeout 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA04"),"True","img/YS_MAA04A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA01"),"True","img/YZ_MAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    voice "NCL10A_EL013"
    爱丽丝 "「啊，喂！那样很危险的吧？」"
    window hide
    hide lh1 with dissolve
    "学姐的妈妈慌忙追了上去。"
    "学姐的父亲紧随其后，不慌不忙地在后面跟着她们，而我则配合学姐父亲的步调跟了上去。"
    window hide
    play music "OBGM28"
    志雄 "「抱歉。突然打扰给您添麻烦了。」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAB01"),"True","img/YZ_MAB01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL10A_KZ009"
    幸蔵 "「不用太在意的哦。我也想要和你聊聊天……而且，也有想问我的事情的吧？」"
    志雄 "「被发现了吗？」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA02"),"True","img/YZ_MAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL10A_KZ010"
    幸蔵 "「不必闪烁其辞的嘛。」"
    "学姐的父亲说着脸上浮出了笑容。"
    志雄 "「说是问事情，倒不如说是想商量一下……关于志愿的事情。」"
    "我有些难以启齿，视线一边从学姐的父亲身上挪开，一边说出心中想商量的事情。"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG05AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG05AA@2x.jpg" as bg0 with dissolve
#SE_VOLC 1,128
#FADE_IN 1
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0
#CHR_POSC 1,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_SBA02"),"True","img/NO_SBA02A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_SAA02"),"True","img/YS_SAA02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    "在前方走着的母女俩，正高兴地手拉着手。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA01"),"True","img/YZ_LAA01A@2x.png") as lh0 zorder 100:
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL10A_KZ011"
    幸蔵 "「志愿啊。确实是让人烦恼的事情呢。」"
    志雄 "「笼统的也有个目标。不过，为了达到那个目标走哪条路最好，我有些迷茫。」"
    "我的目标。将来，想要帮助学姐实现梦想。"
    "不过，为了那个目标，我到底能做些什么呢？为了那个目标，如今我又该怎么做呢？"
    "听到我的话，学姐的父亲像是在思考什么，摸了摸下颌。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB06"),"True","img/YZ_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KZ012"
    幸蔵 "「原来是这样……我认为，你烦恼的事情和志愿问题有些许的不同。」"
    志雄 "「诶？」"
    voice "NCL10A_KZ013"
    幸蔵 "「你已经看到了答案。只是不清楚那个答案是否正确。」"
    "听到这里，我心中有什么地方被击中了，慌乱之中，我下意识地反驳道。"
    志雄 "「但，但是！我连要去哪所大学都还没有决定……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA01"),"True","img/YZ_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KZ014"
    幸蔵 "「真的吗？人在烦恼的时候就等于已经得出了答案哦。」"
    志雄 "「是那样吗……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB06"),"True","img/YZ_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KZ015"
    幸蔵 "「你恐怕是在为了是否要为了将来牺牲现在而烦恼。所谓鱼和熊掌不可兼得。」"
    志雄 "「这倒是没错……」"
    "有了将来的目标，为了那个，现在就必须要努力，应该是那样想的。"
    "而且那也是为了自己的将来。"
    "像是看透了我的想法，学姐的父亲继续说道。"
    voice "NCL10A_KZ016"
    幸蔵 "「但是，能兼得鱼和熊掌的，也只有对两者都不放手的人。比起选择其中一个之后后悔，还是选择权宜双方的方法要更好些。」"
    志雄 "「那样的话，能够顺利进行下去吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA01"),"True","img/YZ_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KZ017"
    幸蔵 "「当然是不可能的。」"
    "毫不犹豫的就回答了。学姐的父亲用有些不好意思的语气继续说道"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB03"),"True","img/YZ_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KZ018"
    幸蔵 "「我以前也是那样考虑的。要为了将来而牺牲掉现在。所以我什么都不顾的工作。家里的事情完全不顾。坚信那是为了家庭的选择。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA05"),"True","img/YZ_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "说到这里，学姐的父亲轻轻的叹了口气。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA03"),"True","img/YZ_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KZ019"
    幸蔵 "「我本应更加珍惜和家人一起度过的现在。因为没有注意到那点，让家里人……特别是克罗艾渡过了那段寂寞的时光。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB01"),"True","img/YZ_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KZ020"
    幸蔵 "「你还年轻。还来得及重新来过。你要知道，即使我已经这个岁数了，也依然想要回到过去和家人重新过一次幸福开心的日子。」"
    志雄 "「……这些对学姐说过吗？」"
    "听到我的话，父亲困扰地挠了挠头。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA03"),"True","img/YZ_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KZ021"
    幸蔵 "「到了这个年纪，想要传达自己直率的心情就很难了。」"
    志雄 "「但是，不说的话是传达不到的吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA06"),"True","img/YZ_LAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KZ022"
    幸蔵 "「嗯……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA01"),"True","img/YZ_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KZ023"
    幸蔵 "「是那样呢。」"
    "这样说着，学姐的父亲寂寞的笑了笑。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_PRIC 1
#CHR_ALPC 1
#CHR_POSC 1,(320+160)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA02"),"True","img/NO_MBA02A@2x.png") as lh1 zorder (10-1):
        ypos .2
        xcenter .75
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA01"),"True","img/YZ_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with move
#MOV_CHR_INIT 32
#MOV_CHR1 128
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
#CHR_PRIC 1
    voice "NCL10A_NO010"
    诺艾儿 "「爸爸！」"
    window hide
    hide lh1 with dissolve
#CHR_PRIC 0
#CHR_PRIC 1
#CHR_SORT 1
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,(448/8)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA02"),"True","img/NO_LBA02A@2x.png") as lh1 zorder (10-1):
        ypos .2
        xcenter .75
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR1 128
#MOV_FOCUS_BG 512
#MOV_CHR_GO 1
#CHR_PRIC 0
#CHR_PRIC 1
#CHR_SORT 1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB02"),"True","img/YZ_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL10A_KZ024"
    幸蔵 "「怎么了，诺艾儿？」"
    "一边叫着一边跑回来的诺艾儿，父亲温柔的接住她。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB01"),"True","img/NO_LBB01A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL10A_NO011"
    诺艾儿 "「那个呢，妈妈说可以买点心！一起选吧～」"
    voice "NCL10A_KZ025"
    幸蔵 "「那样的话，爸爸就选饼干吧？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA04"),"True","img/NO_LBA04A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .75
    with dissolve
    voice "NCL10A_NO012"
    诺艾儿 "「咦～，太硬了不要～」"
    window hide
#SE_VOLC 1,255
    play sound "SE01_12L"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SORT 0
    stop se
    "看着向前走去的两个人，我停下脚步，留在了原地。"
    志雄 "「……要两边都选吗？」"
    "要重视现在。才能实现将来的目标。"
    "为了完成这个选择，普通的努力程度一定是不够的吧。"
    "不过，选择本身倒是让人感觉很舒畅。"
    window hide
    stop se
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+192)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_SBA02"),"True","img/NO_SBA02A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .65
    with dissolve
    voice "NCL10A_NO013"
    诺艾儿 "「大哥哥也快点～！」"
    志雄 "「这就来。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "重视和克罗艾学姐一起度过的现在，为了能帮助学姐而学习——如果学姐和家里人关系变得更好，就省去很多事了。"
    "我向着学姐的家里人那边迈出了脚步，脑子里还是各种不着边际的胡思乱想。"
    "现在学姐在这里的话就好了……"
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
    #show expression "img/BG35EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG35EA@2x.jpg" as bg0 with dissolve
    play sound "SE05_13L"
    pause (32/32.0)
#FADE_IN 1
    志雄 "「差不多快结束了吧。」"
    "在酪萨克前，我拿出手机确认了下时间。时间刚好是５点。克罗艾学姐应该已经下班了吧。"
    voice "NCL10A_KU016"
    克罗艾 "「等了很久吗？」"
    "就在我刚想走进店里确认下的时候，从背后传来学姐的声音。"
    window hide
#SE_VOLC 1,(64/2)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB04"),"True","img/CL_MAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "OBGM17"
    志雄 "「没，刚到而已。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU017"
    克罗艾 "「这样，太好了。那就先回一次家吧。」"
    志雄 "「嗯？为什么？」"
    "听到学姐的提案，我带着疑惑，歪过脑袋。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB06"),"True","img/CL_MAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU018"
    克罗艾 "「要去放焰火的吧？所以要回去换浴衣的。」"
    志雄 "「就算说是放焰火，也不用那么重视的哦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU019"
    克罗艾 "「但是，难得买了焰火，在这种时候还是想要换上呢……」"
    志雄 "「是啊，是那样呢……」"
    "不过这样和学姐的父亲他们见面就要稍微晚点了……"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG03EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG03EA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-160)
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA01"),"True","img/CL_LAA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter .25
    with dissolve
#SE_VOLC 1,(64/2)
#BG_BLUR 0
#FADE_IN 1
    voice "NCL10A_KU020"
    克罗艾 "「而且说起来有些冷清呢。只有两个人放焰火……」"
    志雄 "「不会啦，其实我还邀请了别人哦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB03"),"True","img/CL_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU021"
    克罗艾 "「是吗？是谁啊？」"
    志雄 "「那个，你就期待一下吧。」"
    "听到我恶作剧一般的回答，学姐眉毛拧到了一起，露出了不满的表情。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB05"),"True","img/CL_LAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU022"
    克罗艾 "「马上就会见到的，没有必要保密的吧？」"
    志雄 "「那可是个惊喜！」"
    "估计是察觉到我没有说出来的打算，学姐无奈地笑了笑，点了点头。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB02"),"True","img/CL_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU023"
    克罗艾 "「真没办法呢。」"
    "我们一边继续说着相关的话题，一边向家的方向走去……"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG03NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG03NA@2x.jpg" as bg0 with dissolve
    play sound "SE05_16L"
    pause (32/32.0)
    play sound "SE01_19L"
    pause (32/32.0)
#FADE_IN 1
    "我尴尬地叫着走在前面的学姐。"
    志雄 "「等一下，学姐！稍微等一下！」"
    window hide
#BG_GET_NOC 0,F34
#BG_SWPC 0
#BG_PRI 1
#BG_PRI 0
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,((640/4)-50),100,(640/2),(448/2)
    #show expression "img/F34@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_SCLC 0,512,512
#CHR_POSC 0,0,-224
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LDB04"),"True","img/CL_LDB04A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
    stop se fadeout 1
#SE_VOLC 1,255
#BG_ALP_AUTOC 1,0,1,F24
#CHR_POS_AUTOC 0,F24,96
#BG_UV_AUTOC 0,(640/4),100,(640/2),(448/2),1,F24,96
#BG_ALP_SAVEC 1
#BG_UV_SAVEC 0
#CHR_POS_SAVEC 0
#BG_ALPC 1,128
    pause (32/32.0)
#BG_UV_AUTOC 0,(640/4),0,(640/2),(448/2),1,F24,96
#CHR_POS_AUTOC 0,,224,1,F24,96
#BG_UV_SAVEC 0
#CHR_POS_SAVEC 0
#BG_PRI 0
#BG_SET_BACK 
#BG_INIC 2
#BG_UVC 2,0,512,640,448
    #show expression "img/F34@2x.jpg" as bg2 zorder 2 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_PRIC 1
#CHR_POSC 1
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LDB04"),"True","img/CL_LDB04A@2x.png") as lh11 zorder (10-11):
        ypos 0.0
    with dissolve
#SE_VOLC 1,64
#BG_ALP_AUTOC 0,0,1,F24,96
#CHR_ALP_AUTOC 0,0,1,F24,96
#BG_BLUR 2
#BG_ALP_SAVEC 0
#CHR_ALP_SAVEC 0
#CHR_SWPC 0
#CHR_PRIC 0
#CHR_PRIC 1
#CHR_ALPC 1,128
#BG_SWPC 0
#BG_PRI 0
#BG_PRI 2
#BG_ALPC 2,128
    stop se
    voice "NCL10A_KU024"
    克罗艾 "「真是的，还没有习惯吗？」"
    志雄 "「不可能这么快就习惯的吧！」"
    "我对强忍着笑容的学姐说道。"
    "我一边被不习惯的衣服的裤脚束缚着，一边小心翼翼地走着。"
    window hide
    play sound "SE01_18L"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "相比之下，克罗艾学姐则闲庭信步地向前走着。"
    window hide
#BG_GET_NOC 0,F34
#BG_SWPC 0
#BG_PRI 1
#BG_PRI 0
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,((640/8)*3),(448/4),(640/2),(448/2)
    #show expression "img/F34@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,112,112,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_SDB06"),"True","img/CL_SDB06A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    stop se
    voice "NCL10A_KU025"
    克罗艾 "「喂，志雄。要把你落下了啊？」"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG04NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG04NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MDB03"),"True","img/CL_MDB03A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
    pause (32/32.0)
#SE_VOLC 1,(64/2)
#FADE_IN 1
    志雄 "「学姐，平时就经常穿这样的衣服吗？」"
    voice "NCL10A_KU026"
    克罗艾 "「为什么这么问？」"
    志雄 "「没，感觉完全不像我这样……」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MDB01"),"True","img/CL_MDB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU027"
    克罗艾 "「我也很久没有穿过浴衣了哦。」"
    志雄 "「我倒没那么觉得……」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MDB02"),"True","img/CL_MDB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU028"
    克罗艾 "「真的哦。什么事只要掌握了窍门就容易多了。」"
    志雄 "「窍门吗？是什么窍门？」"
    "看到我无助的样子，学姐露出了得意的表情。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MDB01"),"True","img/CL_MDB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU029"
    克罗艾 "「也没有什么了不起的。志雄走起来很困难是因为步幅太大的缘故」"
    志雄 "「步幅吗？」"
    voice "NCL10A_KU030"
    克罗艾 "「因为勉强迈大步的话，肯定会被裤脚缠住的哦。越是着急想向前走，相反就越是无法顺利的前进。」"
    志雄 "「我本来是想按照平时走路的步伐走的……」"
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
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LDB06"),"True","img/CL_LDB06A@2x.png") as lh10 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCL10A_KU031"
    克罗艾 "「偶尔的也试着慢慢的走吧。」"
    window hide
    play sound "SE01_19L"
    "学姐在我的面前竖起手指，像老师一样的说着，我不好意思的笑了笑，开始试着改变步伐大小。"
    志雄 "「原来如此。确实走起来轻松多了。」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LDB01"),"True","img/CL_LDB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU032"
    克罗艾 "「好了，继续走吧。让别人等可不好。」"
    志雄 "「是啊……喂，还没完全适应，再走的慢点啊！」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LDB06"),"True","img/CL_LDB06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU033"
    克罗艾 "「喂喂，快点快点～」"
    "我一边痛苦地迈着不习惯的步子，一边带着克罗艾学姐向约好的地方前进。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG22NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG22NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LDB03"),"True","img/CL_LDB03A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
        xcenter .75
    with dissolve
    play sound "SE05_10L"
    pause (32/32.0)
#BG_BLUR 0
#FADE_IN 1
    "学姐看到约定地点等着的三个人后，一脸惊讶的表情。"
    voice "NCL10A_KU034"
    克罗艾 "「诶？怎么会？」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA02"),"True","img/YS_MAA02A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    play music "OBGM08"
    voice "NCL10A_EL014"
    爱丽丝 "「啊，浴衣？不错呢，我要是也穿着就好了……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA09"),"True","img/NO_MBA09A@2x.png") as lh10 zorder (10+10):
        ypos .2
        xcenter .35
    with dissolve
    voice "NCL10A_NO014"
    诺艾儿 "「浴衣，是什么～？」"
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCL10A_EL015"
    爱丽丝 "「就是他们两人现在穿着的衣服哦。」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB02"),"True","img/NO_MBB02A@2x.png") as lh10 zorder (10+10):
        ypos .2
        xcenter .35
    with dissolve
    voice "NCL10A_NO015"
    诺艾儿 "「我也想试着穿下呢～」"
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA02"),"True","img/YS_MAA02A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCL10A_EL016"
    爱丽丝 "「是呢。记得克罗艾小的时候好像也穿过……」"
    "学姐的妈妈在努力回忆着。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "转回视线，看到单手拿着塑料桶的学姐的父亲正向这边走来。"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2
    hide lh12
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAB01"),"True","img/YZ_MAB01A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
    with dissolve
    voice "NCL10A_KZ026"
    幸蔵 "「呀。」"
    志雄 "「不好意思。来晚了……」"
    hide lh12
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA02"),"True","img/YZ_MAA02A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
    with dissolve
    voice "NCL10A_KZ027"
    幸蔵 "「没，我们也刚好准备完成。」"
    "说着，学姐的父亲举起手里拿着的塑料桶让我看。"
    "一直愣在那里的学姐此时终于无法抑制住自己的困惑，开口问道。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,640
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MDC05"),"True","img/CL_MDC05A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
        xcenter .75
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA02"),"True","img/YZ_MAA02A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
        xcenter .25
    with move
#MOV_CHR_INIT 48
#MOV_CHR1 128,(320+160)
#MOV_CHR2 ,(320-160)
#MOV_CHR_GO 1
#BG_SET_BACK 
#REEK_CHR 1
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NCL10A_KU035"
    克罗艾 "「那个，志雄？难道说邀请的其他人就是指……」"
#THREAD_STP 1
#REMOVE_REEK_CHR 1
    志雄 "「在商店街偶然碰到，然后就说到一起放焰火的事情。」"
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MDC02"),"True","img/CL_MDC02A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL10A_KU036"
    克罗艾 "「这样……」"
    hide lh12
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA06"),"True","img/YZ_MAA06A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL10A_KZ028"
    幸蔵 "「克罗艾。打工还顺利吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MDC01"),"True","img/CL_MDC01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU037"
    克罗艾 "「嗯。爸爸，身体怎么样了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA01"),"True","img/YZ_MAA01A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
    with dissolve
    voice "NCL10A_KZ029"
    幸蔵 "「已经不要紧了。让你担了不少的心。」"
    voice "NCL10A_KU038"
    克罗艾 "「没有。那是应该的……」"
    voice "NCL10A_KZ030"
    幸蔵 "「嗯……」"
    "学姐和学姐父亲的对话有些呆板。大概是互相都存有顾虑，听起来有些别扭。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA02"),"True","img/NO_MBA02A@2x.png") as lh10 zorder (10-10):
        ypos .2
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR0 128
#MOV_CHR1 ,(320+192)
#MOV_CHR2 ,(320-192)
#MOV_CHR_GO 1
    "这时，手里拿着装着焰火的袋子的诺艾儿，高兴得飞跑过来。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB02"),"True","img/NO_MBB02A@2x.png") as lh10 zorder (10+10):
        ypos .2
    with dissolve
    voice "NCL10A_NO016"
    诺艾儿 "「姐姐！焰火，焰火！放焰火吧！」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA02"),"True","img/YS_MAA02A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
    with dissolve
    voice "NCL10A_EL017"
    爱丽丝 "「喂，诺艾儿。那样使劲的握着，会把焰火弄坏的哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA02"),"True","img/NO_MBA02A@2x.png") as lh10 zorder (10+10):
        ypos .2
    with dissolve
    voice "NCL10A_NO017"
    诺艾儿 "「知道了～」"
    window hide
    hide lh10 with dissolve
    voice "NCL10A_KU039"
    克罗艾 "「妈妈……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
    with dissolve
    voice "NCL10A_EL018"
    爱丽丝 "「好久不见呢，克罗艾……」"
    voice "NCL10A_KU040"
    克罗艾 "「两天前送诺艾儿的时候不是还见到了吗……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA02"),"True","img/YS_MAA02A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
    with dissolve
    voice "NCL10A_EL019"
    爱丽丝 "「是、是呢。最近还好吧？」"
    voice "NCL10A_KU041"
    克罗艾 "「嗯……」"
    "和母亲的对话也是，总觉得学姐和母亲之间拉开了一段距离。"
    "像是双方都在避开真正想要说的话……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
    with dissolve
    voice "NCL10A_EL020"
    爱丽丝 "「开始打工了呢？」"
    voice "NCL10A_KU042"
    克罗艾 "「嗯……」"
    voice "NCL10A_EL021"
    爱丽丝 "「……现在过得快乐吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MDC03"),"True","img/CL_MDC03A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU043"
    克罗艾 "「嗯，很快乐。而且十分的充实。不过……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA06"),"True","img/YS_MAA06A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
    with dissolve
    voice "NCL10A_EL022"
    爱丽丝 "「不过？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MDC01"),"True","img/CL_MDC01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU044A"
    克罗艾 "「……没什么。{w=4}{nw}"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MDB05"),"True","img/CL_MDB05A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
#REEK_CHR 1
    voice "NCL10A_KU044B"
    extend "比起这个，诺艾儿在做什么呢？」"
#REMOVE_REEK_CHR 1
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    hide lh12
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_SBA09"),"True","img/NO_SBA09A@2x.png") as lh10 zorder (10+10):
        ypos .2
    with dissolve
    "在学姐手指的方向，手里拿着小小的发射焰火的诺艾儿，正向筒里面窥视着。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320-192)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA04"),"True","img/YS_MAA04A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
        xcenter .2
    with dissolve
    voice "NCL10A_EL023B"
    爱丽丝 "「啊！等一下，诺艾儿！那个不是拿着放的焰火！」"
    hide lh1 with dissolve
#CHR_POSC 1,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_SAA04"),"True","img/YS_SAA04A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
        xcenter .65
    with move
    "克罗艾学姐和母亲慌张的制止住诺艾儿。一拿过诺艾儿手上拿着的发射的焰火，两个人就教训起诺艾儿来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_SBB02"),"True","img/NO_SBB02A@2x.png") as lh10 zorder (10+10):
        ypos .2
    with dissolve
    voice "NCL10A_NO018"
    诺艾儿 "「对不起！」"
    "虽然被责备，但是诺艾儿似乎并没有意识到自己所犯的错误。"
    window hide
#SE_VOLC 1,0
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
#SE_VOLC 1,64
    play sound "SE03_98L"
    scene expression "img/BG22NA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    "开始放焰火之后，海滩就一下子变得热闹起来。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+96)
#CHR_COLC 0,128,120,112,128
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_SBA02"),"True","img/NO_SBA02A@2x.png") as lh10 zorder (10+10):
        ypos .2
    with dissolve
    "诺艾儿吵闹地挥动着点燃的冷焰火，在空中划着圆圈。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+192)
#CHR_COLC 1,128,120,112,128
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_SAA02"),"True","img/YS_SAA02A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
        xcenter .8
    with dissolve
    "妈妈则在一旁教着诺艾儿正确的放焰火的方法。"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2,(320-96)
#CHR_COLC 2,128,120,112,128
    hide lh12
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_SAA06"),"True","img/YZ_SAA06A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
        xcenter .35
    with dissolve
    "学姐的父亲，在那两人旁边做着焰火发射的准备。"
    window hide
    stop music fadeout 1
    stop se
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    scene expression "img/BG22NA@2x.jpg" as bg0 with dissolve
    voice "NCL10A_YG000"
    雄吾？ "「志雄？」"
    志雄 "「诶？」"
    "我看着海滩上学姐一家人在一起其乐融融的景象，心中的疏离感却渐渐扩大，正在这时，突然听到有人在后面叫我。"
    window hide
#SE_VOLC 1,64
#CHR_SET_BACK
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 1,(320+96)
#CHR_POSC 2,(320-96)
#CHR_DSPWC 11,2,SF_MAA01,KR_MAA01
    play music "OBGM29"
    志雄 "「老爸，香里阿姨……」"
    志雄 "「为什么会在这里？」"
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA03"),"True","img/SF_MAA03A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCL10A_YG001"
    雄吾 "「见面就问『为什么』，也太冷淡了吧。父母和孩子见面需要理由吗？」"
    志雄 "「但是……」"
    "老爸他们住的是位于蓝之丘的公寓。不可能是因为散步而凑巧走到海边。"
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA06"),"True","img/SF_MAA06A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCL10A_YG002"
    雄吾 "「到了暑假，有点在意你过的怎么样呢。」"
    志雄 "「老爸……」"
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCL10A_YG003"
    雄吾 "「碰巧外出正在回公寓的路上，难得的机会就和香里来看看晚上的大海。」"
    hide lh12
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA02"),"True","img/KR_MAA02A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
        xcenter .75
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
        xcenter .25
    with move
    志雄 "「是是……」"
    "还是一如既往的卿卿我我呢，我亲切地微笑着。"
#CHR_DSPWC 11,2,SF_MAA06,KR_MAA01
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
        xcenter .75
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA06"),"True","img/SF_MAA06A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
        xcenter .25
    voice "NCL10A_YG004"
    雄吾 "「另外，学习怎么样？志愿，已经决定了吗？」"
    志雄 "「哈哈……有在按着自己的步调进行着呢。」"
    "而真正的情况是，自己想要走的路，还尚未看到方向。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA02"),"True","img/KR_MAA02A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
    with dissolve
    voice "NCH07A_KR001A"
    香里 "「哈哈。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
    with dissolve
    "好像已经完全被香里阿姨看破了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_LAA01"),"True","img/SF_LAA01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCL10A_YG005"
    雄吾 "「不要紧的。我就不多说了，你可要振作起来哦。」"
    "老爸把手搭在我的肩膀上。感觉从那里传来了亦或是温柔亦或是信赖的很多东西。"
    "看着学姐的家庭团聚的感伤也消失得无影无踪了。"
    "我到底在想些什么。我不是也有属于自己的家庭吗？"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,(320+192)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
        xcenter .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_LAA01"),"True","img/SF_LAA01A@2x.png") as lh11 zorder (20+11):
        ypos 0.0
        xcenter .5
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MDB03"),"True","img/CL_MDB03A@2x.png") as lh10 zorder (10):
        ypos 0.0
        xcenter .8
    with move
#ROUTINE_STA
#CHR_ALP_AUTOC 0,128,1,F24
#CHR_ALP_AUTOC 1,0,1,F24
#CHR_ALP_AUTOC 2,0,1,F24
#ROUTINE_STP
#CHR_ERSWC 1,2
    voice "NCL10A_KU045"
    克罗艾 "「咦，这位是？」"
    "和诺艾儿她们一起放焰火的学姐，不知什么时候来到了我的身边。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 1
#CHR_POSC 2,(320-192)
#CHR_DSPWC 11,2,SF_MAA01,KR_MAA01
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
        xcenter .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh11 zorder (20+11):
        ypos 0.0
        xcenter .5
    志雄 "「啊，是我的父母。说起来学姐还是第一次见吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MDB04"),"True","img/CL_MDB04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU046"
    克罗艾 "「嗯，一直想要去拜访的……」"
    志雄 "「老爸，香里阿姨。这个是一直照顾我的克罗艾学姐。」"
    克罗艾 "「不好意思这么迟才来打招呼，我是嘉神川克罗艾。{w=6}{nw}"
#MESA A_CH_KU,NCL10A_KU047A,"【クロエ】「不好意思这么迟才来打招呼，我是嘉神川克罗艾。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MDB02"),"True","img/CL_MDB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU047B"
    extend "请多关照——」"
#MESA A_CH_KU,NCL10A_KU047B,"请多关照——」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MDB01"),"True","img/CL_MDB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    "克罗艾学姐低下头的同时，老爸和香里阿姨也说着『请多关照』。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA03"),"True","img/SF_MAA03A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCL10A_YG006"
    雄吾 "「啊啊，克罗艾是名字吗？」"
    志雄 "「母亲是法国人哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCL10A_YG007"
    雄吾 "「另外那边的是……」"
    志雄 "「啊，是克罗艾学姐的家人。」"
    "我用眼神示意着在那边对焰火入迷的诺艾儿以及注视着诺艾儿的学姐的父母。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA06"),"True","img/SF_MAA06A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCL10A_YG008"
    雄吾 "「难道说是志雄的女朋友吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MDB04"),"True","img/CL_MDB04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    志雄 "「啊，那个嘛……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA02"),"True","img/KR_MAA02A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
    with dissolve
    window hide
#CHR_POS_AUTOC 2,(320-160),F24,48
#CHR_POS_SAVEC 2
    voice "NCH06A_KR006"
    香里 "「雄吾先生。」"
    "香里阿姨一边窃窃的笑着，一边拉住老爸的胳膊阻止他继续说下去。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCL10A_YG009"
    雄吾 "「嗯……也是呢。比起这个，要先去和嘉神川小姐的父母打招呼吧，看起来一直都很照顾志雄呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
    with dissolve
    voice "NRI11A_KR004A"
    香里 "「那，你们二位一会儿见～」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    hide lh12
    with dissolve
#CHR_ERSWC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MDA07"),"True","img/CL_MDA07A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL10A_YG010B"
    雄吾 "「晚上好，真是漂亮的焰火。初次见面，我是塚本志雄的父亲。」"
    voice "NCL10A_NO019"
    诺艾儿 "「大哥哥的爸爸和妈妈？」"
    voice "NCL10A_EL024"
    爱丽丝 "「喂，诺艾儿！不要拿着焰火走过去，很危险的吧！」"
    "看着远处互相寒暄着的我们的父亲们，学姐不知不觉地微笑了起来。"
    window hide
    
#CHR_INIC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LDC01"),"True","img/CL_LDC01A@2x.png") as lh10 zorder 100:
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL10A_KU048"
    克罗艾 "「真是对好父母呢。」"
    志雄 "「虽然不完全是，不过也差不多吧……」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LDB06"),"True","img/CL_LDB06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    "自己也不是很明白，于是说出了前后矛盾的话。至今为止，我和老爸之间也发生了许多许多的事情。"
    "不过现在和老爸之间的关系，倒也算不上坏。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LDB04"),"True","img/CL_LDB04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCL10A_KU049"
    克罗艾 "「志雄……」"
    "就在我想着这些事情的时候，学姐向我这边看了过来。之后，把背后藏着的一束焰火递向我。"
    voice "NCL10A_KU050"
    克罗艾 "「我们也一起放焰火吧～」"
    window hide
#SE_VOLC 1,0
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL07A")]=True
    show expression "img/EVN_CL07A@2x.jpg" as bg0 zorder 0 with dissolve
    image firework:
        "img/firework1@2x.png"
        pause 0.1
        "img/firework2@2x.png"
        pause 0.1
        "img/firework3@2x.png"
        pause 0.1
        "img/firework4@2x.png"
        pause 0.1
        "img/firework5@2x.png"
        pause 0.1
        "img/firework6@2x.png"
        pause 0.1
        "img/firework7@2x.png"
        pause 0.1
        "img/firework8@2x.png"
        pause 0.1
        "img/firework9@2x.png"
        pause 0.1
        "img/firework10@2x.png"
        pause 0.1
        "img/firework11@2x.png"
        pause 0.1
        "img/firework12@2x.png"
        pause 0.1
        "img/firework13@2x.png"
        pause 0.1
        repeat
    show firework:
        pos (0.191,0.611)
#EFF_STAC 0,SPOTFIREWORKS,EFF_NOSKIP
#SE_VOLC 1,(64/2)
    play sound "SE09_28L"
#FADE_IN 1
    play music "BGM13"
    "我和学姐，注视着对方手里的点燃的焰火。"
    志雄 "「那个……对不起，擅自的叫来学姐的父母……」"
    "老爸和学姐的家人的说话声从远处传来，乘着夜风传到耳边。"
    voice "NCL10A_KU051"
    克罗艾 "「志雄……」"
    志雄 "「在。」"
    voice "NCL10A_KU052"
    克罗艾 "「真是爱管闲事……」"
    志雄 "「抱歉……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL07B")]=True
    show expression "img/EVN_CL07B@2x.jpg" as bg0 with dissolve
    voice "NCL10A_KU053"
    克罗艾 "「但是……谢谢你。」"
    志雄 "「学姐……」"
    voice "NCL10A_KU054"
    克罗艾 "「互相之间的距离，不能相见的时间，虽然有各种各样的问题，不过今天能这样，简简单单的聊天……我很高兴。」"
    志雄 "「是这样啊……」"
    "虽然在我觉得还远远不够……不过即使是一点点，学姐和父母的关系也在重新走回正轨，这就已经很不错了。"
    "按这样发展，或许可以比想象中更早地让学姐和父母之间的隔阂烟消云散。"
    "能交谈，就能传达彼此的心情。心里最重要的想法也应该能藉此让对方了解。"
    "看着身边学姐那开心的笑容，我真切地希望一切都能重归于好。"
    voice "NCL10A_KU055"
    克罗艾 "「嗯……真漂亮呢，焰火……」"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1,128
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