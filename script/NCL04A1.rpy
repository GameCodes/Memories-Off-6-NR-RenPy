label NCL04A1:
    $currentlabel = "NCL04A1"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '24'
    $date = '1'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 2,CAL_0724
    show expression "img/NIMG15B-568h@2x.jpg" as cal zorder 5
    show expression "img/07_24_MONDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG06AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG06AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_15L"
    pause (32/32.0)
#FADE_IN 1,128
#SE_VOLC 1,64
    play music "OBGM17"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    志雄 "「唉……」"
    if not persistent.dictlist[42] and persistent.show_dict:
        $persistent.dictlist[42]=True
        show screen dict_pop(i=42)
    "站在澄空学园的校门前，我深深地叹了口气。"
    "今天是暑假开始后，学生会的奏云祭准备工作正式开始的日子，虽说我只是来帮忙的……"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG09AA@2x.jpg" as bg2 zorder 2 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#SE_VOLC 1,0,16
#MUS_VOL 64,16
#BG_INIC 1
#BG_PRI 1
    #show expression "img/BG_WHITE@2x.jpg" as bg1 with dissolve
#BG_ALPC 0
#BG_BLUR 2
#BG_ALPC 2,128
#CHR_ALPC 0,128
    hide bg1 with dissolve
    voice "NCL04A_YU000_K"
    结乃 "「这里交给我们几个人就可以的啦～」"
    志雄 "「别这样，人手是必要的吧？况且学生会里所有的人都放弃了暑假在努力准备奏云祭……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA05"),"True","img/YU_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_YU001_K"
    结乃 "「所以说啦，从暑假开始准备正是为了不给学长添麻烦啊～」"
    志雄 "「这个……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_YU002_K"
    结乃 "「学长应该了解了吧？那么这边的事情就请放心地交给我们吧～」"
    志雄 "「是……」"
    window hide
#BG_INIC 1
#BG_PRI 1
    show expression Solid("fff") as bg1 with dissolve
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    scene expression "img/BG06AA@2x.jpg" as bg0 with dissolve
    hide bg2
#BG_UVC 2,0,0,640,448
#BG_ALPC 0,128
#SE_VOLC 1,64
#MUS_VOL 128
    hide bg1 with ImageDissolve("img/BG_MASK15@2x.png",1)
    "结果，还是被赶了出来。"
    志雄 "「这个样子的话真的没关系吗？」"
    "新一届学生会的成员确实很可靠，大家在去年失败教训的基础上认真地开展着工作。"
    "对那些忙碌的身影感到安心的同时，我也感到些许的寂寞。"
    "说不定会给人留下『奏云祭的活动能办得这么完美是因为学长把事情都托付给了后辈们』这样的印象。"
    志雄 "「去年克罗艾学姐活跃的身影，总在脑中挥之不去呢。」"
    "虽说做到那种程度有点不太现实，不过说到底大家多少还是想依赖学生会长吧。"
    window hide
    play sound "SE01_04L"
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG03AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG03AA@2x.jpg" as bg0 with dissolve
#SE_VOLC 1,64
#FADE_IN 1
    志雄 "「哈啊……」"
    "走出校门，漫步在回家的路上，我不禁打了个哈欠。"
    "……最近总是熬夜。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    #show expression "img/BG_BLACK@2x.jpg" as bg1 with dissolveBG_LINEAR_SLIDE
    show expression "img/BG04AA@2x.jpg" as bg0 zorder 0 with dissolve
    hide bg1 with dissolve
    "虽说现在是盛夏时节，可稍不留神，时间就会从指缝间溜走。"
    "因为暑假里总有很多要帮忙做事情，所以不知不觉间，考试复习变成了常态的夜间活动。我也变成了一个货真价实的『夜猫子』。"
    stop music fadeout 1
    voice "NCL04A_KU000"
    クロエ？ "「志雄……？」"
    stop se
#MESX "%K%P"
    "听到背后有人喊我的名字，我便急忙把头转了过去。"
    window hide
#SE_VOLC 1,(64/2)
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB06"),"True","img/CL_MBB06A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    play music "BGM04"
    voice "NCL04A_KU001"
    克罗艾 "「果然是志雄。」"
    "是克罗艾学姐。"
    window hide
#MUS_VOL 64
#CHR_SET_BACK
#CHR_INIC 1
#CHR_PRIC 0
#CHR_PRIC 1
#CHR_ALPC 1
#CHR_POSC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA01"),"True","img/YZ_MAA01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .65
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB06"),"True","img/CL_MBB06A@2x.png") as lh0 zorder 100:
        ypos 0.0
        xcenter .35
    with move
#MOV_CHR_INIT 48
#MOV_CHR0 ,(320-96)
#MOV_CHR1 128,(320+96)
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
    "和她在一起的是一个有些眼熟的中年男性。"
    "模糊的印象渐渐清晰了起来，在奏云祭结束那天见过的，他是克罗艾学姐的父亲。"
    "不过，会在这个地方遇到学姐和她的父亲我也有些意外。"
    window hide
#MUS_VOL 128
#CHR_PRIC 1
#CHR_PRIC 0
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XBB05"),"True","img/CL_XBB05A@2x.png") as lh0 zorder 100:
        ypos 0.0
        xcenter .35
    with dissolve
    "见我傻傻地站在那里，学姐担心地看着我的脸。"
    voice "NCL04A_KU002"
    克罗艾 "「没事吧？」"
    志雄 "「呃？啊、嗯，没事！」"
    "听到我略显慌乱的回答，克罗艾学姐像安心了一般，长出了一口气。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XBA02"),"True","img/CL_XBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCL04A_KU003"
    克罗艾 "「听说今年中暑的人特别多呢，乱来可不行哦。」"
    "听到学姐的关心真的是很开心呢，我的脸上不禁绽开了笑容。注意到这一点的学姐，也不好意思了起来。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XBA04"),"True","img/CL_XBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCL04A_KU004"
    克罗艾 "「不许笑人家啦！」"
    "多好的气氛就这么被我傻傻地破坏了，我还真是不谨慎啊。想到这里，我立刻修正了表情。"
    志雄 "「真的没事的。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC03"),"True","img/CL_LBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCL04A_KU005"
    克罗艾 "「真拿你没办法……」"
    "克罗艾学姐对我表现算是勉勉强强接受了，然后从我身边走开。"
    志雄 "「说起来……」"
    "我们的对话告一段落后，我也把视线投向了学姐的父亲。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_PRIC 1
#CHR_PRIC 0
#CHR_ALPC 1
#CHR_POSC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA01"),"True","img/YZ_MAA01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter (320+96)/640.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC03"),"True","img/CL_LBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-96)/640.0
    with move
#MOV_CHR_INIT 48
#MOV_CHR0 ,(320-96)
#MOV_CHR1 128,(320+96)
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
    志雄 "「这位是……」"
    "虽然在探病的时候见过，不过这样面对面相见我们还是第一次。"
    "好在学姐马上就意识到了我的想法。"
#CHR_PRIC 1
#CHR_PRIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL_MBA02'",DynamicDisplayable(mouthanime,"CL_MBA02"),"True","img/CL_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    voice "NCL04A_KU006"
    克罗艾 "「说起来，还没给你介绍呢。」"
    voice "NCL04A_KU007"
    克罗艾 "「这位是我的父亲。爸爸，这是塚本志雄。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA02"),"True","img/YZ_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter (320+96)/640.0
    with dissolve
    voice "NCL04A_KZ000"
    幸蔵２ "「啊，你好你好。」"
    hide lh1 with dissolve
#CHR_SORT 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB01"),"True","img/YZ_LAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter (320+96)/640.0
    with dissolve
    if not persistent.dictlist[13] and persistent.show_dict:
        $persistent.dictlist[13]=True
        show screen dict_pop(i=13)
    voice "NCL04A_KZ001"
    幸蔵２ "「我是克罗艾的父亲嘉神川幸藏。女儿平时承蒙关照了。」"
    "学姐的父亲，握住我伸出的手说道。"
    志雄 "「初次见面，我是塚本志雄。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA02"),"True","img/YZ_LAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter (320+96)/640.0
    with dissolve
    voice "NCL04A_KZ002"
    幸蔵 "「你就是志雄君啊。我从克罗艾那里听到不少关于你的事情呢」"
    "学姐的父亲向我微笑着说道。"
    window hide
#BG_GET_NOC 0,F34
#BG_SET_BACK 
#BG_INIC 2
#BG_UVC 2,0,512,640,448
#BG_BLUR 2
#SE_VOLC 1,255
#MUS_VOL 0
#ROUTINE_STA
#BG_UV_AUTOC 0,(640/4),,((640/4)*3),((448/4)*3),1,F24,48
#BG_UV_AUTOC 2,(640/4),,((640/4)*3),((448/4)*3),1,F24,48
#BG_ALPC 0,0,1,F24,48
#CHR_ALP_AUTOC 0,0,1,F24,48
#CHR_POS_AUTOC 0,((320)-((((320+96)-(320-96))*3)/2)),(110),1,F24,48
#CHR_SCL_AUTOC 1,384,384,1,F24,48
#CHR_POS_AUTOC 1,(110),1,F24,48
#CHR_SCL_AUTOC 0,384,384,1,F24,48
#ROUTINE_STP
#BG_UV_SAVEC 0
#BG_UV_SAVEC 2
#BG_ALP_SAVEC 0
#CHR_SCL_SAVEC 1
#CHR_POS_SAVEC 1
#CHR_SCL_SAVEC 0
#CHR_POS_SAVEC 0
#CHR_ALP_SAVEC 0
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB02"),"True","img/YZ_LAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter (320+96)/640.0
    with dissolve
    voice "NCL04A_KZ003"
    幸蔵 "「你愿意的话，也可以直接称呼我『爸爸』，就可以了。」"
    志雄 "「这，这实在是……」"
    "我不知道该作何回答，只好傻傻地笑了笑回应。"
    "虽然曾经从学姐的话里猜想他是一位十分严厉的人，不过现在看来要率直得多。"
    window hide
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB04"),"True","img/CL_MBB04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
#SE_VOLC 1,(64/2)
#MUS_VOL 128
#ROUTINE_STA
#BG_UV_AUTOC 0,0,0,640,448,1,F24,48
#BG_UV_AUTOC 2,0,0,640,448,1,F24,48
#BG_ALP_AUTOC 0,128,1,F24,48
#CHR_SCL_AUTOC 1,170,170,1,F24,48
#CHR_POS_AUTOC 1,(320+80),0,1,F24,48
#CHR_SCL_AUTOC 0,170,170,1,F24,48
#CHR_POS_AUTOC 0,(320-80),0,1,F24,48
#CHR_ALP_AUTOC 0,128,1,F24,48
#ROUTINE_STP
#BG_UV_SAVEC 0
#BG_UV_SAVEC 2
#BG_ALP_SAVEC 0
#CHR_SCL_SAVEC 1
#CHR_POS_SAVEC 1
#CHR_SCL_SAVEC 0
#CHR_POS_SAVEC 0
#CHR_ALP_SAVEC 0
    hide bg2 with dissolve
#BG_UVC 2,0,0,640,448
#BG_ALPC 2,128
    voice "NCL04A_KU008"
    克罗艾 "「爸爸……」"
    "学姐也一副很吃惊的样子，用十分困扰的表情看着我们。"
#CHR_SCLC 1,256,256
#CHR_SORT 0
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA02"),"True","img/YZ_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter (320+96)/640.0
    with dissolve
    voice "NCL04A_KZ004"
    幸蔵 "「啊，不好意思。看起来还言之尚早咯？」"
    "学姐的父亲看到学姐的样子，露出一副十分抱歉的神情。"
    克罗艾 "「……」"
    "克罗艾学姐也露出些许含羞的表情，不过之后什么都没有说。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA01"),"True","img/YZ_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter (320+96)/640.0
    with dissolve
    志雄 "「嗯……？」"
    "看到她们两人的样子，我不禁感觉到有种莫名的违和感。"
    "说点什么呢，那个……"
#CHR_SCLC 0,256,256
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB03"),"True","img/CL_MBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    voice "NCL04A_KU010"
    克罗艾 "「怎么了啊？」"
    志雄 "「啊，没有。没什么的。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBA01"),"True","img/CL_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    voice "NCL04A_KU011"
    克罗艾 "「这之后我要陪爸爸去一趟医院。有时间的话，志雄也一起来吧？」"
    "呃，我看上去是那么有闲工夫的样子吗？"
    "……说不定还真是那样呢。"
    志雄 "「不了，还是算了吧。」"
    "学姐还要照顾她的父亲，我要是一起凑过去的话，会添麻烦的吧。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBA02"),"True","img/CL_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    voice "NCL04A_KU012"
    克罗艾 "「是吗……那我们走了，多保重哦。」"
    志雄 "「好的。学姐也多保重。」"
    "虽然有点恋恋不舍，不过难得家人在一起，打扰他们会很不合适的。"
    志雄 "「那么，我就此告辞了——」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NCL04A_KZ005"
    幸蔵 "「稍等一下。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-96)
#CHR_POSC 1,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB03"),"True","img/CL_MBB03A@2x.png") as lh0 zorder (10+0):
        xcenter (320-96)/640.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA01"),"True","img/YZ_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter (320+96)/640.0
    voice "NCL04A_KZ006"
    幸蔵 "「你们俩个人不用在意我的。难得的暑假不是吗？两个人去哪里玩玩才好嘛。」"
    "学姐的父亲那样说着，推了推学姐的后背。"
    hide lh0 with dissolve
#CHR_SORT 0
#CHR_POSC 0,(320-160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC05"),"True","img/CL_LBC05A@2x.png") as lh0 zorder (10+2):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAB01"),"True","img/YZ_MAB01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    "学姐向我这边走了两三步后急忙回头。"
    hide lh0 with move
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBA02"),"True","img/CL_LBA02A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL04A_KU013"
    克罗艾 "「您在说什么啊？那去医院的事情……」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA01"),"True","img/YZ_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL04A_KZ007"
    幸蔵 "「什么嘛，这种程度的小活动我一个人也能去的。」"
    "面对克罗艾学姐的担心，他挺起胸膛回答道。"
    voice "NCL04A_KU014"
    克罗艾 "「可是……」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA02"),"True","img/YZ_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL04A_KZ008"
    幸蔵 "「没关系的，最近身体的情况相当好。也算是稍微做一点儿恢复性训练了。」"
    "克罗艾学姐似乎还想说些什么，不过最终还是放弃了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBA03"),"True","img/CL_LBA03A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL04A_KU015"
    克罗艾 "「我知道了。不过，病才刚刚好，千万要保重身体哦。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAA01"),"True","img/YZ_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL04A_KZ009"
    幸蔵 "「我知道啦。」"
    window hide
    play sound "SE01_04L"
#MOV_CHR_INIT 48
#MOV_CHR1 0
#MOV_FOCUS_BG 512
#MOV_CHR_GO 1
    hide lh1 with dissolve
#CHR_ALPC 1,128
    stop se fadeout 1
    "学姐的父亲脸上浮现起了笑容，然后一个人向着医院的方向徐徐而去。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBA06"),"True","img/CL_LBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU016"
    克罗艾 "「唉。」"
    "微微地叹息了一声，学姐马上恢复了笑容，向我转过身来。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB01"),"True","img/CL_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU017"
    克罗艾 "「那，现在该怎么办呢？」"
    志雄 "「……」"
    "看着学姐询问着我的神情，一种诡异的感觉从心底油然而生。"
    "总感觉，像是喉咙被鱼刺卡住了似的……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB03"),"True","img/CL_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU018"
    克罗艾 "「志雄？」"
    志雄 "「啊，是呢。总之，天气这么热，去一个凉快一些的地方吧。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB01"),"True","img/CL_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU019"
    克罗艾 "「嗯。咖啡店怎么样？」"
    window hide
    play sound "SE01_12L"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "这样说着，我握住学姐的手，向咖啡厅的方向走去。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG45AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG45AA@2x.jpg" as bg0 with dissolve
    play sound "SE00_38"
    pause (32/32.0)
    play sound "SE07_22L"
#FADE_IN 1
    "进到店内，身体马上就被清凉的空气包围了。"
    "对于在阳光下毒晒了很长时间的人来说，这里简直就是天堂啊。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC01"),"True","img/CL_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL04A_KU020"
    克罗艾 "「难得的机会，就在这里吃午饭吧……志雄看起来也很累了。」"
    志雄 "「抱歉啊。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    pause (32/32.0)
    stop se fadeout 1
    show expression "img/EXBG02A@2x.jpg" as bg_over zorder 5
    show expression "img/CL_ZBB03A@2x.png" as lh0 zorder (10+0):
        xcenter ((320)/640.0)
    with dissolve
    voice "NCL04A_KU021"
    克罗艾 "「说起来，为什么在暑假期间还穿着校服呢？」"
    "正沉浸在冷气中，贪婪地享受着伟大的科技带来的福利的我，听到学姐的问话不禁端正了一下坐姿。"
    志雄 "「呃，稍微有点儿事去了学校一趟，回来的路上才遇见了学姐。」"
    voice "NCL04A_KU022"
    克罗艾 "「去学校……啊。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB01"),"True","img/CL_ZBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "克罗艾学姐若有所思地碎碎念着，不过马上就明白了。"
    voice "NCL04A_KU023"
    克罗艾 "「奏云祭的准备工作，对吧。难道今年还是有问题吗？」"
    志雄 "「没有，今年没有什么问题。」"
    "我吸取了去年的教训，今年早早地就开始了准备工作。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB04"),"True","img/CL_ZBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU024"
    克罗艾 "「原来如此。」"
    志雄 "「准备工作本身一切顺利。可是我明明是学生会会长却没有做什么，真是很为难呢。」"
    "听了这句玩笑话，学姐浮现出了笑容。"
    voice "NCL04A_KU025"
    克罗艾 "「学生会要做的工作里有奏云祭的相关事项，这难道不是件值得高兴的事情么？」"
    志雄 "「倒是这样没错，毕竟是高中最后一次了呢。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB02"),"True","img/CL_ZBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU026"
    克罗艾 "「是啊。虽然去年确实很糟糕，但其中也包含了不少挑战。」"
    "学姐仿佛想起了那个时候的事情。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB01"),"True","img/CL_ZBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU027"
    克罗艾 "「可是，如果没有那些忙碌的话，说不定那时也就不需要志雄了呢。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB04"),"True","img/CL_ZBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "我们互相凝视着彼此，两个人都不好意思地笑了。"
    "学姐慌忙把视线转向菜单。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBC05"),"True","img/CL_ZBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#REEK_CHR 0
    voice "NCL04A_KU028"
    克罗艾 "「那个，说起来点些什么呢？」"
#REMOVE_REEK_CHR 0
    志雄 "「是，是啊……」"
    "我结束漫无边际地回忆，专心开始选择今天的午饭。"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBC01"),"True","img/CL_ZBC01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (64/32.0)
#SE_VOLC 1,(64/2)
#FADE_IN 1
    "在等待上菜的时间里，我向克罗艾学姐问了一件一直很在意的事情。"
    志雄 "「那个，学姐。」"
    voice "NCL04A_KU029"
    克罗艾 "「嗯？」"
    志雄 "「你父亲，看起来好多了呢。」"
    "脑中浮现起了刚才见到的学姐父亲的身影。"
    "看起来脸色也好多了，看不出是大病初愈的样子。"
    "可是，听了我的话之后，克罗艾学姐露出来有些痛苦的表情。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBC04"),"True","img/CL_ZBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU030"
    克罗艾 "「可是，虽然看着是好多了。」"
    志雄 "「难道还有哪里不太好吗？」"
    "话刚出口我就后悔了。也许这并不是我应该问的。"
    "学姐脸上露出了忧郁的表情，但还是刻意用明亮的声音回答了我。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBC02"),"True","img/CL_ZBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU031"
    克罗艾 "「也不是特别严重，只是……」"
    "学姐在这里停顿了一下，用感到很为难的声音继续说。"
    voice "NCL04A_KU032"
    克罗艾 "「父亲的身体还没有完全康复，不能做那些勉强自己的事情。」"
    志雄 "「这样啊……」"
    "我放心了下来。"
    voice "NCL04A_KU033"
    克罗艾 "「可是，毕竟病才刚刚好，还是很担心呢。」"
    "这么说来，学姐应该是特意和父亲一起去医院的了。"
    志雄 "「对不起……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB03"),"True","img/CL_ZBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU034"
    克罗艾 "「怎么了，为什么志雄要道歉？」"
    志雄 "「如果没有遇到我的话，克罗艾学姐应该好好地送父亲去医院的。」"
    "面对道歉的我，学姐慌忙摇了摇手。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBC05"),"True","img/CL_ZBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU035"
    克罗艾 "「怎么会，不是志雄的错啊。而且……"
#BG_SET_BACK 
#REEK_CHR 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBC03"),"True","img/CL_ZBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REMOVE_REEK_CHR 0
    "学姐说到这里顿了顿，有些害羞地向天花板看去。"
    voice "NCL04A_KU036"
    克罗艾 "「而且，去完医院之后本来就想去见志雄来着……」"
    志雄 "「这，这样吗？」"
    voice "NCL04A_KU037"
    克罗艾 "「……」"
    志雄 "「……」"
    "两个人都沉默了起来。"
    "最后，还是我终于忍耐不住先开口了。"
    志雄 "「看时间，学姐的父亲应该正在回家的路上了吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB04"),"True","img/CL_ZBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU038"
    克罗艾 "「嗯。」"
    志雄 "「那个，虽然问这样的事情可能会很奇怪，不过……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB03"),"True","img/CL_ZBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU039"
    克罗艾 "「不过？」"
    志雄 "「平常的时候，学姐和父亲都谈些什么呢？稍微有些在意……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB05"),"True","img/CL_ZBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU040"
    克罗艾 "「……」"
    "听了我的话，克罗艾学姐露出了些许沉重的表情。"
    志雄 "「啊，那个，对不起。只是有些好奇，不方便的话……」"
    voice "NCL04A_KU041"
    克罗艾 "「哎，志雄。」"
    "学姐慌忙打断我的提问，接着继续说道。"
    stop music fadeout 1
    voice "NCL04A_KU042"
    克罗艾 "「志雄看见我和父亲两个人，有什么想法呢？」"
    志雄 "「什么想法，那个……」"
    "被学姐这样问到，那种如鲠在喉的感觉又来了。"
    "克罗艾学姐，用极其认真的目光一直注视着我。"
    志雄 "「……这么说也许会很失礼，不过看上去有些距离感。」"
    "听了我的话，学姐无力地叹了口气。"
    window hide
    play music "OBGM08"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB04"),"True","img/CL_ZBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU043"
    克罗艾 "「果然。」"
    志雄 "「那个，果然是指？」"
    "我不知道这其中发生了什么事情，只好接着问道。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBA06"),"True","img/CL_ZBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU044"
    克罗艾 "「我也是这么想的——总觉得有些无法填补的东西。」"
    "说完这句话，学姐的表情变得愈加沉重。"
    志雄 "「学姐……？」"
    "对于我的困惑，学姐无力地笑了笑。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBA01"),"True","img/CL_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU045"
    克罗艾 "「最近呢，父亲一直在家工作。」"
    voice "NCL04A_KU046"
    克罗艾 "「医生说，父亲病倒是经年累月的疲惫积累起来一并发作的结果。」"
    voice "NCL04A_KU047"
    克罗艾 "「所以，父亲接受了医生的建议，有好好保养身体，就像很多年前一样。」"
    "学姐脸上喜忧参半。"
    voice "NCL04A_KU048"
    克罗艾 "「晚饭的时候也能坐在一起吃，就像回到了最初最和睦的那种家庭状态，我真的很开心。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBA02"),"True","img/CL_ZBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU049"
    克罗艾 "「可是，我不知道……」"
    "伴随着这句话，学姐的脸上露出了困惑。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBA06"),"True","img/CL_ZBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU050"
    克罗艾 "「以前的我，是用怎样的表情，对爸爸说着怎样的话。全部，都想不起来……」"
    志雄 "「学姐……」"
    voice "NCL04A_KU051"
    克罗艾 "「我很紧张，所以十分认真地附和着父亲说话。生怕说错了什么。」"
    voice "NCL04A_KU052"
    克罗艾 "「不过，我不知道这个样子真的好吗？」"
    "学姐低着头，一点一滴地吐露着心声。"
    voice "NCL04A_KU053"
    克罗艾 "「明明一直生活在一起，该对爸爸说怎样的话才好，我真的不明白。」"
    voice "NCL04A_KU054"
    克罗艾 "「明明是一家人……」"
    "学姐那寂寞的表情我无法再看下去，于是，我下定决心要开口说些什么。"
    志雄 "「没关系的哦，肯定。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB03"),"True","img/CL_ZBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU055"
    克罗艾 "「诶？」"
    志雄 "「我想克罗艾学姐的父亲，有很用心地想着学姐的事情哦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB04"),"True","img/CL_ZBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU056"
    克罗艾 "「是那样吗？」"
    志雄 "「是啊。是那样的不是吗？关于我的事情学姐的父亲也很认真的记住了。」"
    "脑中浮现起了那个时候学姐父亲的表情。"
    志雄 "「我想学姐的父亲，一定是很认真地听了学姐说的每一句话。所以，不用担心哦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB05"),"True","img/CL_ZBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU057"
    克罗艾 "「啊……」"
    志雄 "「不过，我和学姐父亲说话今天也才是第一次，也许没什么说服力就是了。」"
    stop music fadeout 1
    voice "NCL04A_XJ000"
    店員Ｃ "「让您久等了。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB04"),"True","img/CL_ZBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "说到这里的时候，我们点的食物好了。"
    play sound "SE03_33"
    "店员把我们的餐具轻轻放在桌子上，便向别的位子走去。"
    "很不合时宜的被打断了，呆呆地坐在那里。"
    "停顿了一下之后，我才觉得自己刚刚说了很难为情的话。"
    志雄 "「那个，所以说……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB02"),"True","img/CL_ZBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU058"
    克罗艾 "「说的是呢。」"
    "学姐对着我微笑了一下，微微地点了点头。"
    window hide
    play music "BGM13"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB01"),"True","img/CL_ZBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU059"
    克罗艾 "「对不起，说了这么沉重的话。」"
    "看学姐的样子，现在已经没有消沉的感觉了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB06"),"True","img/CL_ZBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU060"
    克罗艾 "「那，趁饭还没凉，咱们赶紧开动吧～」"
    "学姐拿起了刀叉，话的底气明显足了许多。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB02"),"True","img/CL_ZBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU061"
    克罗艾 "「我开动了！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB06"),"True","img/CL_ZBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「我开动了！」"
    window hide
#SE_VOLC 1,0
#MUS_VOL 64
#FADE_OUT 1
    show expression Solid("000") as bg_over zorder 100 with None
#BG_PRI 0
##FADE_IN 0
    "…………"
    "……"
    window hide
##FADE_OUT 0
#BG_COLC 0,128,128,128,128
#BG_PRI 0
    hide lh0
    hide bg_over
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBC03"),"True","img/CL_ZBC03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (32/32.0)
#SE_VOLC 1,(64/2)
#MUS_VOL 128
#FADE_IN 1
#MESEX_A M_NOA,A_CH_KU,NCL04A_KU062,"【クロエ】「……」%K%P"
    voice "NCL04A_KU062"
    克罗艾 "「……」"
    "吃完午饭，我们一起喝着饭后茶。"
    "虽然刚才学姐一直精力十足的样子，不过话语之间还是有些在勉强自己。"
    "我停下了脑中的胡思乱想，向学姐搭话。"
    志雄 "「接下来，咱们去哪里转转吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBC05"),"True","img/CL_ZBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#REEK_CHR 0
    voice "NCL04A_KU063"
    克罗艾 "「诶？」"
#REMOVE_REEK_CHR 0
    志雄 "「难得见一次面，就这样回去了总觉得很扫兴呢。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBC01"),"True","img/CL_ZBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU064"
    克罗艾 "「也是呢……」"
    "对我的提案，学姐微笑着回应了。"
    "如果学姐能恢复心情的话，无论什么地方也要陪学姐去。我在心里默默地起誓。"
    志雄 "「学姐有什么想要去的地方吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB02"),"True","img/CL_ZBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU065"
    克罗艾 "「是呢……」"
    "学姐一边把手抵在嘴角思考一边说道。"
    "不一会儿，学姐好像想到了好主意，开口说道。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB01"),"True","img/CL_ZBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU066"
    克罗艾 "「好久没有去骑马了，一起去吧？」"
    志雄 "「呃，这个……」"
    "上次骑马之后全身肌肉疼的感觉一瞬间在我的脑海中重现，我不禁一颤。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB05"),"True","img/CL_ZBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU067"
    克罗艾 "「还是说，去其他什么更好的地方呢？」"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "当然是和学姐一起骑马":
            $F7=0
        "没有什么自信":
            $F7=1
    if F7==0:
        jump L_NCL04A_SEL00_A
    if F7==1:
        jump L_NCL04A_SEL00_B
label L_NCL04A_SEL00_A:
    志雄 "（刚刚不是决定了无论什么地方都会陪学姐去的吗。）"
    志雄 "「当然和学姐一起去骑马了。」"
    "对着露出些许寂寞表情的学姐，我微笑着。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB01"),"True","img/CL_ZBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「这次让学姐看看我骑马时的英姿吧！」"
    jump L_NCL04A_SEL00_X
label L_NCL04A_SEL00_B:
    志雄 "「呃，那个……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB04"),"True","img/CL_ZBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04X_KU000"
    克罗艾 "「果然还是去别的什么地方吧？」"
    "可能是看到了我在踌躇，学姐露出了些许寂寞的神情。"
    志雄 "「啊，不！我不介意的。只是……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB03"),"True","img/CL_ZBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04X_KU001"
    克罗艾 "「只是？」"
    志雄 "「经过那个非常的经历之后，身体还记得那种感觉呢……」"
    "对着不安地碎碎念着的我，学姐露出了细小的笑容。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB01"),"True","img/CL_ZBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04X_KU002"
    克罗艾 "「志雄真是的，在意那种事情吗？没关系的。这样的话，这么办吧，我从最初的要领开始教你。」"
    志雄 "「请手下留情……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB02"),"True","img/CL_ZBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04X_KU003"
    克罗艾 "「啊，那就要看志雄掌握的快慢了哦～」"
    jump L_NCL04A_SEL00_X
label L_NCL04A_SEL00_X:
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB06"),"True","img/CL_ZBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU068"
    克罗艾 "「哈哈。那么咱们出发吧！」"
    志雄 "「嗯。」"
    show expression "img/BG45AA@2x.jpg" as bg_over zorder 2 with dissolve
    "我和学姐快速地喝完茶、买单，然后便向骑乘俱乐部进发。"
    window hide
    play sound "SE00_38"
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
    stop music fadeout 1
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT