label NCL11A:
    $currentlabel = "NCL11A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '08'
    $day = '16'
    $date = '3'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 2,CAL_0816
    show expression "img/NIMG15A-568h@2x.jpg" as cal zorder 5
    show expression "img/08_16_WEDNESDAY@2x.png" as cal_date zorder 6:
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
#BG_INIC 2
##BG_POSC 0,(60),0,640,448
    scene expression "img/EXBG10AA@2x.png" as bg0 with dissolve
#FADE_IN 1,128
    play music "BGM13"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "暑假只剩下两周了。"
    志雄 "「那个，学姐。这个地方我还有些问题……」"
    "我指着没弄懂的题目，抬起头看着学姐。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBA06"),"True","img/CL_ZBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    克罗艾 "「……」"
#MESEX_A M_NOA,A_CH_KU,NCL11A_KU000,"【クロエ】「……」%K%P"
    "克罗艾学姐心不在焉地看着窗外。"
    志雄 "「学姐？」"
    "又叫了一次学姐，这才终于有了反应。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB03"),"True","img/CL_ZBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU001A"
    克罗艾 "「啊，{w=2}{nw}"
#MESA A_CH_KU,NCL11A_KU001A,"【クロエ】「啊，"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB01"),"True","img/CL_ZBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU001B"
    extend "是。怎么了？」"
    志雄 "「那个呢，这里的积分我有些不明白……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB02"),"True","img/CL_ZBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU002"
    克罗艾 "「嗯，啊，这里啊……」"
    "自从和家人一起放过焰火之后，学姐就一直都是这样，总是一副失神的样子。"
    "放焰火时学姐的笑脸，再次在我的脑中浮现。为了能再一次看到那笑容，我必须要做些什么。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB03"),"True","img/CL_ZBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU003"
    克罗艾 "「那个，这里也出错了哦……」"
    志雄 "「诶？啊，真的……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB05"),"True","img/CL_ZBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU004"
    克罗艾 "「真是的，你都没有集中精神。」"
    志雄 "「对不起……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB01"),"True","img/CL_ZBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "要集中……要集中……能集中吗？学姐的事情，为了前途努力学习的事情，各种事情错乱的混在一起，占据着我的大脑。"
    志雄 "「唉……」"
    window hide
    play sound "SE02_06L"
    "深呼吸，定了定神，我又把视线落回到手里的参考书上，这时，家里的电话响了起来。"
    志雄 "「嗯？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBA01"),"True","img/CL_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU005"
    克罗艾 "「没关系，我去接吧。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "学姐站起来，拦住了想要起身的我，向电话的方向走去。"
    window hide
    play sound "SE02_16"
    voice "NCL11A_KU006"
    克罗艾 "「是，这里是塚本家。……妈妈？嗯……诶？可是这么急……嗯，我知道了。」"
    window hide
    play sound "SE02_07"
#BG_SWPC 0
#BG_SWPC 2
#BG_ERSWC 0,2,BG_NOFADE
#BG_PRI 1
#BG_PRI 3
#BG_PRI 0
#BG_PRI 2
#BG_POSC 0,0,0,640,448
#BG_POSC 2,0,0,640,448
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG15AA@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBC02"),"True","img/CL_MBC02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#BG_ERSWC 1,3
#BG_POSC 1,0,0,640,448
#BG_POSC 3,0,0,640,448
    "学姐回到房间来，仿佛有些高兴又好像有几分忧虑。"
    志雄 "「妈妈打来的？」"
    voice "NCL11A_KU007"
    克罗艾 "「嗯。」"
    "试着问了问学姐，学姐则呆呆地点了点头。"
    voice "NCL11A_KU008"
    克罗艾 "「为了庆祝爸爸出院。今晚想让我过去呢……」"
    志雄 "「是吗？那今天晚饭就只好各自吃各自的了。」"
    "克罗艾学姐住到我家来之后，几乎没有一个人吃饭的时候。如果家里突然只剩自己，晚餐也会变得很乏味吧。"
    "但是，学姐很久都没有和家人在一起了。学姐去的话也许正是消除和双亲之间隔阂的契机……"
    voice "NCL11A_KU009"
    克罗艾 "「另外，志雄也被邀请了哦。」"
    志雄 "「诶？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB04"),"True","img/CL_MBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU010"
    克罗艾 "「总觉得，他们两个人都很在意志雄的事情，诺艾儿也很想你……」"
    志雄 "「可是，我去的话不会打扰到吗？」"
    "学姐略显羞涩地低下了头。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBA07"),"True","img/CL_MBA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU011"
    克罗艾 "「我也觉得如果志雄在的话，会安心许多……」"
    志雄 "「嗯，我知道了。」"
    "都说到这种程度了，说什么也不能推辞了。"
    "而且这也是一个天赐的大好机会。如果能通过这次晚餐促成什么的话，我也一定会鼎力相助——"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG81NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG81NA@2x.jpg" as bg0 with dissolve
    play sound "SE05_16L"
    pause (32/32.0)
#FADE_IN 1
    pause (32/32.0)
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG82NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG82NA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAA02"),"True","img/NO_MAA02A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    play music "BGM08"
    voice "NCL11A_NO000"
    诺艾儿 "「姐姐，欢迎回家～」"
    "最先出现迎接我们的，是活蹦乱跳的诺艾儿。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+192)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBC01"),"True","img/CL_MBC01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .8
    with dissolve
    voice "NCL11A_KU012"
    克罗艾 "「我回来了，诺艾儿。」"
    志雄 "「今晚打扰了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB01"),"True","img/NO_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL11A_NO001"
    诺艾儿 "「那个呢，料理，我有帮忙呢！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB06"),"True","img/CL_MBB06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU013"
    克罗艾 "「诶，那可真是令人期待。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2,(320-192)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_SAA04"),"True","img/YS_SAA04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .2
    with dissolve
    voice "NCL11A_EL000"
    爱丽丝 "「诶？诺艾儿不是在帮爸爸端料理的吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB08"),"True","img/NO_MAB08A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL11A_NO002"
    诺艾儿 "「啊，对了！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_SAA02"),"True","img/YS_SAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCL11A_EL001"
    爱丽丝 "「知道了的话就快去吧。那么多的盘子爸爸一个人可端不过来哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAA02"),"True","img/NO_MAA02A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL11A_NO003"
    诺艾儿 "「好～的～」"
    window hide
    hide lh0 with dissolve
    "听了母亲的话，诺艾儿急匆匆地跑进了厨房。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCL11A_EL002"
    爱丽丝 "「欢迎，两位。抱歉，突然就把你们叫来……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBC01"),"True","img/CL_MBC01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU014"
    克罗艾 "「嗯，没关系的。」"
    志雄 "「感谢您的招待。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA02"),"True","img/YS_MAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCL11A_EL003"
    爱丽丝 "「请稍等片刻。马上就准备好了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBC05"),"True","img/CL_MBC05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
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
    voice "NCL11A_KU015"
    克罗艾 "「那个，我也来帮忙吧。」"
#THREAD_STP 1
#REMOVE_REEK_CHR 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA03"),"True","img/YS_MAA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCL11A_EL004"
    爱丽丝 "「不用啦，你们是客人嘛，请等一会儿就好了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBC02"),"True","img/CL_MBC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU016"
    克罗艾 "「嗯……」"
    window hide
    hide lh2 with dissolve
    "学姐点了点头，学姐的妈妈则又走进了厨房。"
    window hide
#BG_GET_NOC 0,F24
#BG_SET_BACK 
#BG_INIC 1
#BG_UVC 1,72,(448/4),(640/4),(448/4)
#BG_ALPC 1
#BG_BLUR 1
#BG_ALP_AUTOC 1,128,0,F24
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_SWPC 0
    hide bg1 with dissolve
#BG_PRI 0
#BG_PRI 1
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 2
#CHR_POSC 0,(320-96),(448/8)
#CHR_POSC 2,(320-192)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAB01"),"True","img/NO_LAB01A@2x.png") as lh0 zorder (10+0):
        xcenter .35
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB03"),"True","img/YZ_LAB03A@2x.png") as lh2 zorder (10+2):
        xcenter .2
    "诺艾儿和学姐的爸爸都双手端着盘子从厨房走了出来。"
    "稍微有些勉强吧，学姐的父亲脚下稍有不稳。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+192)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB05"),"True","img/CL_LBB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .8
    with dissolve
    voice "NCL11A_KU017"
    克罗艾 "「爸爸，大病初愈的，不用勉强自己啦……」"
    志雄 "「那个，我来端吧？」"
    "听到我和学姐有些惊慌的声音，学姐的爸爸露出一副欣慰的笑容。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB01"),"True","img/YZ_LAB01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCL11A_KZ000"
    幸蔵 "「啊，坐下吧。没关系的。也算是康复性训练，这点程度没问题的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAB02"),"True","img/NO_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL11A_NO004"
    诺艾儿 "「没问题的～」"
    "模仿着爸爸说话的诺艾儿，紧紧跟在爸爸后面。话说，这样是不是有些危险啊。"
    window hide
#CHR_ERSWC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC05"),"True","img/CL_LBC05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    "因为父母两人都坚决不同意我们帮忙，所以我们只能静静地坐着，看着他们忙碌的身影。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "所幸的是没有发生任何事故，我和学姐面前的桌子上星罗棋布地放满了料理。"
    "炸虾、炸鸡块、油炸肉饼……就算是为了庆祝康复，做这么多油炸食品真的好吗？"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2,(320-192),(448/8)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAB02"),"True","img/NO_LAB02A@2x.png") as lh2 zorder (10+2):
        ypos .2
        xcenter .2
    with dissolve
    voice "NCL11A_NO005"
    诺艾儿 "「主食来了～」"
    "最后的时候，诺艾儿兴高采烈地端着盘子走了过来。大概是超喜欢的料理登场了吧。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+192)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB01"),"True","img/CL_LBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .8
    with dissolve
    voice "NCL11A_KU018"
    克罗艾 "「诶，是什么啊？」"
    voice "NCL11A_NO006"
    诺艾儿 "「我最喜欢吃的东西！」"
    play sound "SE03_33"
    "诺艾儿把盘子从手里放到桌子上的时候，学姐的表情瞬间僵住了。"
    stop music fadeout 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB05"),"True","img/CL_LBB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU019"
    克罗艾 "「这个……」"
    voice "NCL11A_NO007"
    诺艾儿 "「Sｔｕｆｆｅｄ　ｐｉｍｅｎｔ！」"
    window hide
    play music "OBGM19"
#BG_SET_BACK
#FILT_PRI 6
#FILT_IN 32,0,COL_DARK
#BG_UVC 0,72,((448/4)+512),(640/4),(448/4)
#RSET F121
##THREAD_STA 1,THREAD_PIMENT
#BG_UV_AUTOC 0,120,((448/4)+512),(640/4),(448/4),1,F24
#CHR_POS_AUTOC 1,F24
#CHR_POS_AUTOC 2,0,F24
#CHR_ALP_AUTOC 2,0,1,F24
#BG_UV_SAVEC 0
#CHR_POS_SAVEC 1
#CHR_POS_SAVEC 2
#CHR_ALP_SAVEC 2
    hide lh2 with dissolve
#CHR_ALPC 2,128
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC02"),"True","img/CL_LBC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    克罗艾 "「……」"
#MESEX_A M_NOA,A_CH_KU,NCL11A_KU020,"【クロエ】「……」%K%P"
    "学姐的笑容顿时消失得无影无踪。不经意地流露出一副难看的脸色。"
    志雄 "「没事吧？」"
#RSET F121
#THREAD_WAT 1
    hide bg3 with dissolve
#BG_ALPC 3,12
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC05"),"True","img/CL_LBC05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#FILT_OUT 32
#REEK_CHR 1
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NCL11A_KU021A"
    克罗艾 "「诶？{w=2}{nw}"
#MESA A_CH_KU,NCL11A_KU021A,"【クロエ】「诶？"
#THREAD_STP 1
#REMOVE_REEK_CHR 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC01"),"True","img/CL_LBC01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU021B"
    extend "嗯，没事……」"
    "小声地对学姐说道，而学姐则依然笑容全无地回应。"
    "根本就不是没事嘛。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC02"),"True","img/CL_LBC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    "像是在忍耐着什么似的，学姐把手放在膝盖上垂下了头。"
    window hide
    "Sｔｕｆｆｅｄ　ｐｉｍｅｎｔ，也就是柿子椒塞肉。对学姐来说是母亲的味道。"
    "可是……"
    "可是，如今已是不喜欢的事物了。回忆中的灰色料理。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_UV_SAVEC 0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_INIC 2
#CHR_ALPC 0
#CHR_ALPC 1
#CHR_ALPC 2
#CHR_POSC 0,(448/8)
#CHR_POSC 1,(320+192)
#CHR_POSC 2,(320-192)
#CHR_DSPTC 0,1,2,NO_LAA01,YS_LAA01,YZ_LAA01
#ROUTINE_STA
#BG_UV_AUTOC 0,72,((448/4)+512),(640/4),(448/4),1,F24
#CHR_ALP_AUTOC 0,128,0,F24
#CHR_ALP_AUTOC 1,128,0,F24
#CHR_ALP_AUTOC 2,128,0,F24
#ROUTINE_STP
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAA01"),"True","img/NO_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA01"),"True","img/YS_LAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .8
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ_LAA01'",DynamicDisplayable(mouthanime,"YZ_LAA01"),"True","img/YZ_LAA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .2
    
    "把学姐的纠结放在一边，全家人在饭桌前坐好了。"
    voice "NCL11A_KZ001"
    幸蔵 "「那么，大家开动吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAA02"),"True","img/NO_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL11A_NO008"
    诺艾儿 "「哦～！」"
    "面对眼前的丰盛大餐，诺艾儿欢呼着。看到这样学姐的母亲责备道。"
    window hide
#ROUTINE_STA
#BG_UV_AUTOC 0,96,((448/4)+512),(640/4),(448/4),1,F24,24
#CHR_POS_AUTOC 0,(320-96),F24,24
#CHR_POS_AUTOC 1,(320+96),F24,24
#CHR_POS_AUTOC 2,(320-256),F24,24
#CHR_ALP_AUTOC 2,0,1,F24,24
#ROUTINE_STP
#BG_UV_SAVEC 0
#CHR_POS_SAVEC 0
#CHR_POS_SAVEC 1
#CHR_POS_SAVEC 2
#CHR_ALP_SAVEC 2
    hide lh2 with dissolve
#CHR_ALPC 2,128
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA04"),"True","img/YS_LAA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL11A_EL005"
    爱丽丝 "「诺艾儿，要有礼貌才行。要先说开动了哦？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAB01"),"True","img/NO_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL11A_NO009"
    诺艾儿 "「是，妈妈。」"
    "看着诺艾儿点了点头，学姐的母亲把视线转向了学姐。"
    window hide
#ROUTINE_STA
#BG_UV_AUTOC 0,120,((448/4)+512),(640/4),(448/4),1,F24,24
#CHR_POS_AUTOC 0,(320-192),F24,24
#CHR_POS_AUTOC 1,F24,24
#CHR_ALP_AUTOC 0,0,1,F24,24
#ROUTINE_STP
#BG_UV_SAVEC 0
#CHR_POS_SAVEC 0
#CHR_POS_SAVEC 1
#CHR_ALP_SAVEC 0
    hide lh0 with dissolve
#CHR_ALPC 0,128
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA02"),"True","img/YS_LAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL11A_EL006"
    爱丽丝 "「你最喜欢吃柿子椒塞肉了吧？之前没来得及吃你就出门了，所以就想再做一次看看。」"
    "学姐的母亲，笑着说道。"
    "那笑容告诉我们，她还什么都不知道。学姐没能说出自己已经讨厌那个料理了……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA01"),"True","img/YS_LAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL11A_EL007"
    爱丽丝 "「如果，如果可以的话，差不多可以回来了吧？」"
    "学姐的母亲相信，用回忆的料理作为契机，能够缩短二人之间的距离……"
    克罗艾 "「……」"
    "学姐的眼里噙满了泪水。注意到这些的母亲停止了话语。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA06"),"True","img/YS_LAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL11A_EL008"
    爱丽丝 "「克罗艾……？」"
    "学姐无法吃下母亲好不容易为自己做出的料理，也许是对自己的不争气感到悲愤吧。"
    "不过，学姐的妈妈眼中却映出了别的东西。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA03"),"True","img/YS_LAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL11A_EL009"
    爱丽丝 "「啊，对不起。突然说了这样的话……这样的话会很困扰的吧……」"
    "悲伤的话语。"
    window hide

#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    play sound "SE03_12"
#BG_ALP_AUTOC 1,128,0,F24
#BG_ALP_SAVEC 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_SWPC 0
    hide bg1 with dissolve
#BG_UVC 1,0,0,640,448
#BG_ALPC 1,128
#BG_PRI 0
#BG_PRI 1
    "听了这些，学姐从椅子上站了起来，就这样跑了出去。"
    "无法说出自己的感受。"
    "然后，也无法听到对方的心意。"
    "虽然很想马上追上去。不过还是先向学姐的父母说明一下更要紧……"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA03"),"True","img/YS_MAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_EL010"
    爱丽丝 "「是啊，我随便就离开，回来也这么突然……」"
    voice "NCL11A_EL011"
    爱丽丝 "「明明想慢慢地缩短距离的，我真是……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320-160)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_MAB03"),"True","img/YZ_MAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL11A_KZ002"
    幸蔵 "「不，是我的错。和克罗艾那么长时间一直生活在一起，却没有去理解她的感受……」"
    "学姐的父母一起叹息着。我不禁想起了与学姐谈家人的事情时，她那忧伤的身影……"
    "我感觉他们像是对彼此之间的距离担心过多，而对彼此的心意理解出现了偏差。"
    志雄 "「那个，其实……克罗艾学姐她并没有……」"
    "对情不自禁说着话的我，学姐的妈妈低下了头。"
    voice "NCL11A_EL012"
    爱丽丝 "「对不起呢，志雄……」"
    志雄 "「没有啦……」"
    "于是，也没能说出什么。果然，如果不是当事人的话，一点意义也没有。"
    voice "NCL11A_KZ003"
    幸蔵 "「志雄，虽然对不住你，不过可以请你去追那孩子吗？我们去了也会给那个孩子带来负担的。」"
    志雄 "「好的。」"
    "我从屋里飞奔了出去。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/BG81NA@2x.jpg" as bg0 with dissolve
    play sound "SE05_16L"
    pause (32/32.0)
#FADE_IN 1
    "公寓的入口处，学姐的背影映入我的眼帘。"
    window hide
#SE_VOLC 1,(64/2)
#CHR_INIC 1
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBA02"),"True","img/CL_LBA02A@2x.png") as lh11 zorder 100:
        ypos 0.0
    with dissolve
    志雄 "「学姐！」"
    voice "NCL11A_KU023"
    克罗艾 "「志雄……？」"
    志雄 "「回去吧？你父母都在担心呢。」"
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBA06"),"True","img/CL_LBA06A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU024"
    克罗艾 "「志雄。我……跑出来了……」"
    志雄 "「没关系的。好好地说出心声的话，大家会理解的。」"
    "我想学姐和父母之间的隔阂不好好沟通是无法消除的。"
    "不过，学姐摇了摇头。"
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC02"),"True","img/CL_LBC02A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU025"
    克罗艾 "「我做不到……」"
    志雄 "「学姐……」"
    "我屏住了呼吸。克罗艾学姐的眼中噙满了泪水。"
    voice "NCL11A_KU026"
    克罗艾 "「回家吧。今天，已经够了……」"
    "学姐用十分悲伤的表情说道。"
    "我想说点什么，却组织不起任何有用的句子，只能静静地沉默着。"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_PRIC ID_ALL
#CHR_SORT 0,1
#CHR_ALPC 2
#CHR_POSC 2
    hide lh12
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC02"),"True","img/CL_LBC02A@2x.png") as lh11 zorder (10+1):
        ypos 0.0
        xcenter .65
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB04"),"True","img/NO_MAB04A@2x.png") as lh10 zorder (10+2):
        ypos .2
        xcenter .35
    with move
#MOV_CHR_INIT 48
#MOV_CHR1 ,(320+96)
#MOV_CHR2 128,(320-96)
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
#ROUTINE_STA
#CHR_PRIC ID_ALL
#CHR_SORT 0,1
#ROUTINE_STP
    voice "NCL11A_NO010"
    诺艾儿 "「姐姐，大哥哥！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC05"),"True","img/CL_LBC05A@2x.png") as lh11 zorder (10+1):
        ypos 0.0
    with dissolve
#REEK_CHR 1
    voice "NCL11A_KU027"
    克罗艾 "「诺艾儿？」"
#REMOVE_REEK_CHR 1
    "我很惊讶，难道是为了追我们跑出来了吗？"
    window hide
    hide lh2 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96),(448/8)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAB04"),"True","img/NO_LAB04A@2x.png") as lh10 zorder (10+2):
        ypos .2
    with dissolve
#BG_BLUR 0
    voice "NCL11A_NO011"
    诺艾儿 "「姐姐，我做了什么错事了吗？」"
#REEK_CHR 1
    voice "NCL11A_KU028"
    克罗艾 "「诶……？」"
#REMOVE_REEK_CHR 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAB05"),"True","img/NO_LAB05A@2x.png") as lh10 zorder (10+10):
        ypos .2
    with dissolve
    voice "NCL11A_NO012"
    诺艾儿 "「姐姐生气了吧？对不起，对不起」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC02"),"True","img/CL_LBC02A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU029"
    克罗艾 "「诺艾儿……」"
#THREAD_STA 1,THREAD_CHLOE_HUG
    "学姐什么都没有说，只是默默地抱紧了诺艾儿。"
    志雄 "「诺艾儿没有任何错哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAA03"),"True","img/NO_LAA03A@2x.png") as lh10 zorder (10+10):
        ypos .2
    with dissolve
    voice "NCL11A_NO013"
    诺艾儿 "「可是……」"
    志雄 "「对吧，学姐？」"
    voice "NCL11A_KU030"
    克罗艾 "「嗯……」"
    "是啊，诺艾儿什么错都没有。学姐现在责备的，只是自己而已。"
    window hide
#CHR_SET_BACK
#ROUTINE_STA
#CHR_INIC 2
#CHR_ALPC 2
#CHR_PRIC ID_ALL
#CHR_SORT 0,1
#CHR_POSC 2,(320+256)
#ROUTINE_STP
    hide lh12
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA06"),"True","img/YS_MAA06A@2x.png") as lh12 zorder (10-12):
        ypos 0.0
        xcenter .9
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR2 128
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
#ROUTINE_STA
#CHR_PRIC ID_ALL
#CHR_SORT 0,1
#ROUTINE_STP
    voice "NCL11A_EL013"
    爱丽丝 "「诺艾儿！？克罗艾！啊，太好了……」"
    voice "NCL11A_KU031"
    克罗艾 "「妈妈……」"
    "应该是为了追诺艾儿吧，学姐的母亲气喘吁吁地出现在我们面前。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA04"),"True","img/YS_MAA04A@2x.png") as lh12 zorder (12):
        ypos 0.0
    with dissolve
    voice "NCL11A_EL014"
    爱丽丝 "「这可不行啊诺艾儿，这么晚了还一个人跑出来。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAA04"),"True","img/NO_LAA04A@2x.png") as lh10 zorder (10+10):
        ypos .2
    with dissolve
    voice "NCL11A_NO014"
    诺艾儿 "「对不起……」"
    "学姐的母亲并没有生克罗艾学姐的气。也无法生气。四目相对，又都马上移了视线。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC03"),"True","img/CL_LBC03A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU032"
    克罗艾 "「……对不起，我们今天就先回去了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA03"),"True","img/YS_MAA03A@2x.png") as lh12 zorder (12):
        ypos 0.0
    with dissolve
    voice "NCL11A_EL015"
    爱丽丝 "「这样啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAA04"),"True","img/NO_LAA04A@2x.png") as lh10 zorder (10+10):
        ypos .2
    with dissolve
    voice "NCL11A_NO015"
    诺艾儿 "「那，那个，妈妈……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LAB04"),"True","img/NO_LAB04A@2x.png") as lh10 zorder (10+10):
        ypos .2
    with dissolve
    voice "NCL11A_NO016"
    诺艾儿 "「我，今天能住到姐姐那里去吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB05"),"True","img/CL_LBB05A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU033"
    克罗艾 "「诶？」"
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
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 1,(320-96)
#CHR_POSC 2,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB04"),"True","img/NO_MAB04A@2x.png") as lh11 zorder (10-1):
        xcenter .35
        ypos .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA03"),"True","img/YS_MAA03A@2x.png") as lh12 zorder (10-2):
        xcenter .65
    
    voice "NCL11A_EL016"
    爱丽丝 "「怎么了呢？突然之间……」"
    "对于诺艾儿突然提出的要求，学姐和母亲都十分惊讶。"
    "诺艾儿双手合十，向妈妈请求着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB03"),"True","img/NO_MAB03A@2x.png") as lh11 zorder (10+11):
        ypos .2
    with dissolve
    voice "NCL11A_NO017"
    诺艾儿 "「无论如何！呐，不行吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA04"),"True","img/YS_MAA04A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
    with dissolve
    voice "NCL11A_EL017"
    爱丽丝 "「不可以无理取闹啦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB05"),"True","img/NO_MAB05A@2x.png") as lh11 zorder (10+11):
        ypos .2
    with dissolve
    voice "NCL11A_NO018"
    诺艾儿 "「求求你了，妈妈……」"
    "学姐的母亲一幅很为难的表情，就是不肯答应。不过，诺艾儿又为什么如此执着呢？"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC02"),"True","img/CL_LBC02A@2x.png") as lh10 zorder (100-10):
        ypos 0.0
        xcenter .15
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA04"),"True","img/YS_MAA04A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
        xcenter .6
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB05"),"True","img/NO_MAB05A@2x.png") as lh11 zorder (10+11):
        ypos .2
    with move
#ROUTINE_STA
#CHR_POS_AUTOC 1,F24
#CHR_ALP_AUTOC 1,0,1,F24
#CHR_POS_AUTOC 2,(320+192),F24
#CHR_ALP_AUTOC 2,0,1,F24
#CHR_POS_AUTOC 0,(320-224),F24
#CHR_ALP_AUTOC 0,128,1,F24
#ROUTINE_STP
#BG_BLUR 0
    志雄 "「学姐……」"
    voice "NCL11A_KU034"
    克罗艾 "「嗯。」"
#MESEX_A M_NOA,A_CH_KU,NCL11A_KU034,"【クロエ】「嗯。」%K%P"
    "我小声地向学姐确认着，尽管如此学姐也还是回应了我。"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC02"),"True","img/CL_LBC02A@2x.png") as lh10 zorder (100-10):
        ypos 0.0
        xcenter .5
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA04"),"True","img/YS_MAA04A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
        xcenter .65
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB05"),"True","img/NO_MAB05A@2x.png") as lh11 zorder (10+11):
        ypos .35
    with move
#CHR_SETWC 11,2,NO_MAB05,YS_MAA04
#ROUTINE_STA
#CHR_POS_AUTOC 1,(320-96),F24
#CHR_ALP_AUTOC 1,128,1,F24
#CHR_POS_AUTOC 2,(320+96),F24
#CHR_ALP_AUTOC 2,128,1,F24
#CHR_POS_AUTOC 0,(0),F24
#CHR_ALP_AUTOC 0,0,1,F24
#ROUTINE_STP
#BG_BLUR 0
    志雄 "「那个，我们这边的话没关系的。」"
#CHR_DSPWC 11,2,NO_MAB03,YS_MAA03
    voice "NCL11A_EL018"
    爱丽丝 "「诶，可是……」"
    诺艾儿 "「……」"
#MESEX_A M_NOA,A_CH_NO,NCL11A_NO019,"【ノエル】「……」%K%P"
    voice "NCL11A_EL019"
    爱丽丝 "「可是，会给你们添麻烦的。」"
    志雄 "「完全没有啦。倒不如说多一个人会更热闹一些。」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC03"),"True","img/CL_LBC03A@2x.png") as lh10 zorder (10+100):
        ypos 0.0
    with dissolve
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA04"),"True","img/YS_MAA04A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
        xcenter .65
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB05"),"True","img/NO_MAB05A@2x.png") as lh11 zorder (10+11):
        ypos .35
    with move
#ROUTINE_STA
#CHR_POS_AUTOC 1,F24
#CHR_ALP_AUTOC 1,0,1,F24
#CHR_POS_AUTOC 2,(320+192),F24
#CHR_ALP_AUTOC 2,0,1,F24
#CHR_POS_AUTOC 0,(320-224),F24
#CHR_ALP_AUTOC 0,128,1,F24
#ROUTINE_STP
#BG_BLUR 0
    "我转过头看着垂着脑袋的学姐。现在，必须要考虑一下诺艾儿的心意。"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC02"),"True","img/CL_LBC02A@2x.png") as lh10 zorder (100-10):
        ypos 0.0
        xcenter .5
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA04"),"True","img/YS_MAA04A@2x.png") as lh12 zorder (10+12):
        ypos 0.0
        xcenter .65
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB05"),"True","img/NO_MAB05A@2x.png") as lh11 zorder (10+11):
        ypos .35
    with move
#ROUTINE_STA
#CHR_POS_AUTOC 1,(320-96),F24
#CHR_ALP_AUTOC 1,128,1,F24
#CHR_POS_AUTOC 2,(320+96),F24
#CHR_ALP_AUTOC 2,128,1,F24
#CHR_POS_AUTOC 0,(0),F24
#CHR_ALP_AUTOC 0,0,1,F24
#ROUTINE_STP
#BG_BLUR 0
#CHR_ALPC 0,128
    "学姐的母亲依然一副困惑的表情，不过交替看了看我和克罗艾学姐后，她开口说道。"
    voice "NCL11A_EL020"
    爱丽丝 "「那就实在是麻烦你们了……」"
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MAB09"),"True","img/NO_MAB09A@2x.png") as lh11 zorder (10+11):
        ypos .2
    with dissolve
    志雄 "「明天中午我们就把诺艾儿送回来。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我们和诺艾儿一起，从学姐家往回走……"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG39NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG39NA@2x.jpg" as bg0 with dissolve
#SE_VOLC 1,(64/2)
#FADE_IN 1
    pause (32/32.0)
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    stop sound fadeout 1
    play sound "SE00_00"
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
#BG_SWPC 0
#BG_ALPC 1,128
#BG_PRI 0
#BG_PRI 1
    scene expression "img/BG33AA@2x.jpg" as bg0 with dissolve
#SE_WATC 0
    stop sound
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-96)
#CHR_POSC 1,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB06"),"True","img/NO_MBB06A@2x.png") as lh0 zorder (10+0):
        xcenter .35
        ypos .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBC03"),"True","img/CL_MBC03A@2x.png") as lh1 zorder (10+1):
        xcenter .65
    voice "NCL11A_NO020"
    诺艾儿 "「我有话想对姐姐说……」"
    "刚到家，诺艾儿便对学姐说道。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB03"),"True","img/NO_MBB03A@2x.png") as lh0 zorder (10+0)
    with dissolve
    voice "NCL11A_NO021"
    诺艾儿 "「在我出生以前，发生过什么吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBC02"),"True","img/CL_MBC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    克罗艾 "「！？」"
#MESEX_A M_NOA,A_CH_KU,NCL11A_KU035,"【クロエ】「！？」%K%P"
    voice "NCL11A_NO022"
    诺艾儿 "「为什么姐姐和我没有生活在一起？」"
    克罗艾 "「……」"
#MESEX_A M_NOA,A_CH_KU,NCL11A_KU036,"【クロエ】「……」%K%P"
    voice "NCL11A_NO023"
    诺艾儿 "「为什么在我出生的时候，爸爸和姐姐都不在一起呢？」"
    "没有任何间隙，一次又一次地质问着。"
    "诺艾儿要来我家的原因，就是这个吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBC01"),"True","img/CL_MBC01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU037"
    克罗艾 "「姐姐，被妈妈扔下了呢……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB05"),"True","img/NO_MBB05A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    "一直冷静的学姐终于无法继续维持平和的表情。露出为难的笑容回答着诺艾儿的质问。"
    voice "NCL11A_NO024"
    诺艾儿 "「为什么？」"
    voice "NCL11A_KU038"
    克罗艾 "「大概，是太累了吧。所以把我扔下了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA04"),"True","img/NO_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL11A_NO025"
    诺艾儿 "「可是，回来了啊？」"
    "对学姐的回答，诺艾儿很不理解地把头歪向一边。"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB04"),"True","img/CL_MBB04A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#CHR_POS_AUTOC 1,F24,48
#CHR_POS_SAVEC 1
    voice "NCL11A_KU039"
    克罗艾 "「嗯，妈妈回来，和诺艾儿相见，我真的很开心。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB03"),"True","img/NO_MBB03A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL11A_NO026"
    诺艾儿 "「开心？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB06"),"True","img/CL_MBB06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU040"
    克罗艾 "「嗯，非常开心」"
    "说完学姐笑了笑，像是掩饰心情一般的笑容。而对此，诺艾儿却并不放过，连续地质问着。"
    voice "NCL11A_NO027"
    诺艾儿 "「那，被扔下的时候呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBA06"),"True","img/CL_MBA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU041"
    克罗艾 "「那个……」"
    "学姐不禁语塞。或者应该说，是一幅迷茫的样子。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB05"),"True","img/NO_MBB05A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL11A_NO028"
    诺艾儿 "「我，讨厌被扔下。那样好痛苦，心中会疼到无法忍受，一定会哭出来的。姐姐呢？心里不会痛的吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBA02"),"True","img/CL_MBA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU042"
    克罗艾 "「我……」"
    "学姐什么都说不出来，只是抚摸着诺艾儿的头。"
    "大概是一口气宣泄出了太多的情绪，诺艾儿用手擦拭着不断落下的眼泪。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB03"),"True","img/NO_MBB03A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL11A_NO029"
    诺艾儿 "「痛苦的时候就要好好地讲出来，妈妈是这么说的……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBA06"),"True","img/CL_MBA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU043"
    克罗艾 "「是呢……」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL08A")]=True
    show expression "img/EVN_CL08A@2x.jpg" as bg0 zorder 0 with dissolve
    pause (32/32.0)
#FADE_IN 1
    "哭累了的诺艾儿恍恍惚惚地枕着学姐的腿睡着了。"
    voice "NCL11A_NO030"
    诺艾儿 "「呜……嗯……」"
    voice "NCL11A_KU044"
    克罗艾 "「对不起，诺艾儿。」"
    志雄 "「好好讲出来吗……」"
    "我不禁把诺艾儿的话小声地念了出来，学姐也停下了抚摸诺艾儿的手，若有所思。"
    "那是很难的事情吧，克罗艾学姐和我都深切地体会到了这一点……"
    window hide
    stop music fadeout 1
#FADE_OUT 1,128
    scene expression Solid("000") with fade
#FADE_IN 0
    $month = '08'
    $day = '17'
    $date = '4'
#CAL_DSP_GRP 2,CAL_0817
    show expression "img/NIMG15A-568h@2x.jpg" as cal zorder 5
    show expression "img/08_17_THURSDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
#FADE_OUT 1,32,COL_WHITE
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 1
#BG_UVC 0,0,512,640,448
#BG_SETWC 0,1,BG81AA,NIMG01A
    scene expression "img/BG81AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB03"),"True","img/NO_LBB03A@2x.png") as lh0 zorder (10-0):
        ypos .2
    with dissolve
    play sound "SE05_15L"
    pause (32/32.0)
#EFF_STAC 0,CLOUD_A,EFF_SKIP
#FADE_IN 1,128
#BG_BLUR 0
    play music "OBGM08"
    "第二天，我一个人送诺艾儿回家。"
    "学姐昨天晚上开始，就一直把自己关在屋里。"
    "来到学姐门前，诺艾儿突然紧紧地握住了我的手。"
    window hide
#SE_VOLC 1,(64/2)
#FADE_OUT 1
#BG_ALPC 1
#EFF_STPC 0,EFF_SKIP
    hide bg1 with dissolve
#FADE_IN 1
    voice "NCL11A_NO031"
    诺艾儿 "「大哥哥……」"
    志雄 "「怎么了呢？」"
    voice "NCL11A_NO032"
    诺艾儿 "「姐姐她在痛苦着呢。可是却什么都没有说……」"
    志雄 "「嗯，是啊……」"
    "诺艾儿那悲伤的表情让我的胸口一紧。这件事上真是一点忙都没帮上。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB04"),"True","img/NO_LBB04A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL11A_NO033"
    诺艾儿 "「所以，大哥哥，帮帮姐姐吧？」"
    志雄 "「！？」"
    "诺艾儿突然说了这样的话。"
    "如果还没做些什么的话，现在开始去做就好了！"
    志雄 "「真没办法啊……」"
    "我不禁对不中用的自己碎碎念道。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB09"),"True","img/NO_LBB09A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL11A_NO034"
    诺艾儿 "「真没办法？」"
    "诺艾儿瞪圆了好奇的眼睛。这句话她还是第一次听到吧。"
    "对于这句饱受大家诟病的口头禅，字面上的意思的确不太好理解呢。"
    志雄 "「就是『交给我吧』的意思哦。没关系的，大哥哥我会好好帮助你姐姐的」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB02"),"True","img/NO_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL11A_NO035"
    诺艾儿 "「嗯！」"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG33AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG33AA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
#FADE_IN 1
    "回到家，香喷喷的气味迎面扑来。大概学姐正在做饭。"
    志雄 "「那首先——」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBC03"),"True","img/CL_MBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "尚未打招呼，学姐便沉默着端着盘子走了出来。"
    志雄 "「诶！？」"
    window hide
    play sound "SE03_33"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "当看到盘子里盛的东西的时候，我瞠目结舌地愣在了原地。那里面盛的是她最讨厌吃的柿子椒塞肉。"
    志雄 "「这个是，为什么……」"
    show expression "img/EXBG09A@2x.jpg" as bg_over zorder 5
    show expression "img/CL_ZBA06A@2x.png" as lh0 zorder (10+0):
        xcenter ((320)/640.0)
    with dissolve
    "看着吃惊的我，学姐坐到桌子前，用叉子叉起一块柿子椒塞肉。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB05"),"True","img/CL_ZBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU045"
    克罗艾 "「就是这样的感觉哦。」"
    "明显是一幅很勉强的神情。学姐边含着眼泪边努力地吃着讨厌的食物。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBC02"),"True","img/CL_ZBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU046"
    克罗艾 "「咳、咳、咳……」"
    志雄 "「没，没事吧！？」"
    "我把倒满水的杯子递给了学姐。"
    "将喉咙中的食物冲下，学姐开口说道。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBC03"),"True","img/CL_ZBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU047"
    克罗艾 "「我一直恐惧着。怕被问及从家里跑出来的理由。可是，如果不被问的话，我也很害怕。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBC02"),"True","img/CL_ZBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU048"
    克罗艾 "「因为，不问的话不就是意味着他们并不关心我吗？」"
    志雄 "「那种事情……」"
    "就算我说什么也没有意义，这样想着的我也陷入了沉默。"
    voice "NCL11A_KU049"
    克罗艾 "「我想相信一切，脑子里也明白这些。可是，那种不安自己却无法控制。那一天的冰冷的饭菜总是会在我的脑中浮现。」"
    voice "NCL11A_KU050"
    克罗艾 "「爸爸出院了，回到日常的生活的话，妈妈是不是又会不在了呢？」"
    志雄 "「……」"
    voice "NCL11A_KU051"
    克罗艾 "「我无法确信？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBC03"),"True","img/CL_ZBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU052"
    克罗艾 "「已经不行了，我。从那个时候开始就什么也没有改变……」"
    志雄 "「没有那种事情的哦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBC02"),"True","img/CL_ZBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "我向垂着头的学姐说道。至少，我要传递出我的心情。"
    志雄 "「学姐不是一直都在努力着吗？这些我全部都看在眼里。学姐，比我所认识的任何一个人都更加地努力着。」"
    志雄 "「就算是现在也是，你看」"
    "我指着桌子上。"
    志雄 "「……明明是你最不喜欢吃的菜，却依然努力地去吃。」"
    voice "NCL11A_KU053"
    克罗艾 "「可是，即使这样，还是不能改变我不喜欢吃的事实呢……」"
    志雄 "「嗯，确实完全看不到好吃的神情。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB04"),"True","img/CL_ZBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU054"
    克罗艾 "「对吧？」"
    "学姐自嘲般地笑了。不过，这是学姐认真地在听我说的话的证据。"
    志雄 "「学姐，很喜欢父亲的吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB03"),"True","img/CL_ZBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU055"
    克罗艾 "「诶？」"
    window hide
    play music "OBGM29"
    志雄 "「母亲呢？诺艾儿呢？讨厌家人吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB05"),"True","img/CL_ZBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU056"
    克罗艾 "「当然不讨厌了……」"
    "学姐使劲摇着头，全力地否定着。"
    志雄 "「所以，没关系的。对不喜欢的事情依然那样努力的学姐，不可能会在喜欢的事情上失败的吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBA02"),"True","img/CL_ZBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU057"
    克罗艾 "「……可是我该怎么办才好呢？完全没有方向……」"
    "面对用柔弱地声音说着的学姐，我用开朗了起来。"
    志雄 "「那样的话好好地说出来就好。一个人独自承受是不行的，要试着和别人谈心哦。」"
    voice "NCL11A_KU058"
    克罗艾 "「谈……心？」"
    志雄 "「学姐对父母吐露心声的话，父母也一定会用真心交流的。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBA06"),"True","img/CL_ZBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU059"
    克罗艾 "「我的……心声……」"
    "小声地念叨着，学姐开始了深思。完全是心有余而力不足的感觉。"
    志雄 "「虽然很辛苦也说不定，不过我想，如果要消除彼此的隔阂的话，就需要一次完全敞开心扉的谈心。」"
    "害怕是因为彼此有着距离感。学姐和父母之间如果不走得比现在更近的话就什么也改变不了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBA02"),"True","img/CL_ZBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU060"
    克罗艾 "「我明白了……」"
    "学姐对我的建议表示理解。不过在传递心意的事情上，还是有些许犹豫的样子。"
    "不过，除此之外没有别的任何方法了吧。"
    志雄 "「要是学姐无论如何都感到不安的话——」"
    "我的呼吸急促起来，不断地紧张着。"
    志雄 "「我就陪在你身边。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB03"),"True","img/CL_ZBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    克罗艾 "「……」"
    志雄 "「必要的话，我会一直紧握住你的双手哦。绝对，不会离开的。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB04"),"True","img/CL_ZBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU062"
    克罗艾 "「志雄……」"
    "除此以外，一切就要看学姐自己了。"
    "虽然有做不到的事情，我还是会毫不犹豫地全力去做我能做到的事情。"
    "一直迟疑不决的话，就意味着失败。我想力所能及地帮助学姐。我下定了决心。"
    志雄 "「不去做的话可是会被诺艾儿笑话的呢。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB05"),"True","img/CL_ZBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU063"
    克罗艾 "「诶？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB01"),"True","img/CL_ZBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL11A_KU064"
    克罗艾 "「呐，志雄……总算是不对我用敬语了呢」"
    志雄 "「诶？咦？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB06"),"True","img/CL_ZBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "自己完全没有意识到。"
    "不过。"
    "学姐微笑着，平静而美丽，仿佛刚刚新生的一般。"
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
#label THREAD_CHLOE_HUG
#CHR_POS_AUTOC 1,F123
#CHR_POS_SAVEC 1
#EOT
#label THREAD_PIMENT
#label TH_PIMENT_00
#RRND F133,33
#RADD F133
#WAIT2 F133
#RRND F133,33
#RADD F133
#RRND F134,65
#RADD F134
#RSET F123
#RSET F124,F133
    if F121==0:
        jump TH_PIMENT_90
#BG_ALP_AUTOC 3,F134,1,F123,F124
#BG_ALP_SAVEC 3
#RRND F133,33
#RADD F133
#RSET F123
#RSET F124,F133
    if F121==0:
        jump TH_PIMENT_90
#BG_ALP_AUTOC 3,0,1,F123,F124
#BG_ALP_SAVEC 3
#JUMP TH_PIMENT_00
#label TH_PIMENT_90
#BG_ALP_SAVEC 3
#BG_ALP_AUTOC 3,0,1,F123,24
#BG_ALP_SAVEC 3
#EOT
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT