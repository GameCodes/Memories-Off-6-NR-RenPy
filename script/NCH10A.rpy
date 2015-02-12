label NCH10A:
    $month = '09'
    $day = '01'
    $date = '5'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 5,CAL_0901
    show expression "img/NIMG15A-568h@2x.jpg" as cal zorder 5
    show expression "img/09_05_FRIDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 2
#BG_UVC 2,0,512,640,448
#BG_SETWC 0,2,BG07AA2,BG07AA3
    scene expression "img/BG07AA2@2x.jpg" as bg0 with dissolve
    play sound "SE06_02"
    pause (32/32.0)
#FADE_IN 1
    play music "BGM10"
    voice "NCH10A_X8000"
    老师 "「那么，明天开始就要上课了。这是考试前的冲刺，做好心理准备吧」"
    play sound "SE00_22"
    "教室中传来了责难和喝倒彩的声音，但班主任还是一副若无其事的样子从教室里走了出去。"
    stop sound
    "因为今天是第二学期的第一天，所以就只有开学典礼。"
    window hide
    stop se fadeout 1
    play sound "SE08_10L"
    show expression "img/BG07AA3@2x.jpg" as bg_over zorder 2 with dissolve
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA03"),"True","img/TO_MAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH10A_TO000"
    亨 "「哈……。暑假已经结束了啊」"
    voice "NCH10A_TO001"
    亨 "「又过去了一个季节啊……」"
    志雄 "「你啊，装成个诗人的样子，在说什么废话呢」"
    window hide
#CHR_SORT 0,2
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 2
#CHR_ALPC 0
#CHR_ALPC 2
#CHR_POSC 0,640
#CHR_POSC 2,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA06"),"True","img/RI_MAA06A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA03"),"True","img/TO_MAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with move

#ROUTINE_STA
#CHR_POS_AUTOC 1,(320-160),F24
#CHR_POS_AUTOC 0,(320+160),F24
#CHR_ALP_AUTOC 0,128,1,F24
#ROUTINE_STP
#MESA A_CH_RI,NCH10A_RI000A,"【りりす】「佐贺君，新学期第一天就这么散漫啊。"
#VO_WAT VO_WAIT_START
    voice "NCH10A_RI000A"
    莉莉丝 "「佐贺君，新学期第一天就这么散漫啊。{w=6}{nw}"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA05"),"True","img/RI_MAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH10A_RI000B"
    extend "拿出点精神好不好」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB03"),"True","img/TO_MAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH10A_TO002"
    亨 "「虽然话是这么说，但是一想到开学，就一点也开心不起来了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA01"),"True","img/RI_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH10A_RI001"
    莉莉丝 "「唉，这点上倒是有同感」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB02"),"True","img/TO_LAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH10A_TO003"
    亨 "「这么说来，志雄君。今年的夏天，怎么样啊？」"
#BG_ALP_AUTOC 0,0,0,F24,24
#CHR_ALP_AUTOC 2,128,0,F24,24
#BG_ALP_SAVEC 0
#CHR_ALP_SAVEC 2
#ROUTINE_STA
#BG_SWPC 0
#BG_PRI 0
#BG_PRI 2
#BG_ALPC 2
#BG_UVC 2,0,0,640,448
#CHR_SWPC 0
#CHR_ALPC 2
#CHR_SORT 0,1
#ROUTINE_STP
    voice "NCH10A_RI002"
    莉莉丝 "「对对。怎么样啊？」"
    "莉莉丝和亨对着我冷冷地笑着，让人害怕。"
    志雄 "「你，你们干什么啊。什么怎么样啊？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB01"),"True","img/TO_LAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH10A_TO004"
    亨 "「自然是说你和智纱的关系啊！」"
    志雄 "「为什么是“自然”啊……？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAD01"),"True","img/RI_LAD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH10A_RI003"
    莉莉丝 "「本来就是“自然”啊」"
    "……看来确实是很“自然”的了。"
    voice "NCH10A_TO005"
    亨 "「直到暑假结束为止，一直等着没有去问你们。8月这段时间，你们俩的关系，发生了什么变化……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB02"),"True","img/TO_LAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH10A_TO006"
    亨 "「就是为了听到那个变化，然后感到惊天快乐的那一刻啊！」"
    "已经特地做到这个地步了吗？　看来亨的这个暑假，大概是没什么高兴的事情吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAA01"),"True","img/RI_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH10A_RI004"
    莉莉丝 "「就是这么回事。我也很在意呢，和智纱的旅行怎么样，到最后也没问」"
    voice "NCH10A_RI005"
    莉莉丝 "「结果怎么样？　旅行」"
    志雄 "「怎么样……一般的高兴吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAA04"),"True","img/RI_LAA04A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB03"),"True","img/TO_LAB03A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NCH10A_TO007A"
    亨 "「一般，一般是啥啊。{w=5}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAA04"),"True","img/TO_LAA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH10A_TO007B"
    extend "一般到底是什么意思，二百字以内给我说明白！」"
    "突然就跟我说这么哲学的话！？　而且还有字数限制，太严格了！"
    志雄 "「一般就是一般啊。在街上买买东西，去徒步旅行，那里正好在开夏日祭典，我们也去了」"
    "我掰着手指数着，列举这次旅行中做过的事情。但是，莉莉丝和亨，都不知为什么看上去很不满。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAA03"),"True","img/RI_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH10A_RI006"
    莉莉丝 "「就这些？」"
    志雄 "「就这些啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAA06"),"True","img/RI_LAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH10A_RI007"
    莉莉丝 "「啊～？　你啊，好不容易和智纱两人住一个房间吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LAB04"),"True","img/TO_LAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    志雄 "「哎？」"
    "为什么莉莉丝会知道这个？　在旅行的地方确实给莉莉丝打过一次电话，但应该没有说过和智纱两人住在一个房间的事……。"
    志雄 "「啊！？」"
    志雄 "「难道，提案让我和智纱两人住一个房间的，是你吗！？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAC06"),"True","img/RI_LAC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH10A_RI008"
    莉莉丝 "「……啊哈哈」"
    志雄 "「别给我打哈哈！」"
    "我觉得自己终于弄明白和智纱两人住一个房间的来龙去脉了。莉莉丝向香里阿姨提案，香里阿姨跟老爸这么说的。"
    "所以莉莉丝会对智纱做出，潜入我的被窝里吧，这样的建议……！"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAA06"),"True","img/RI_LAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH10A_RI009"
    莉莉丝 "「啊～啊。不过，从刚才你的反应来看，这个夏天里和智纱之间好像没什么进展啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA06"),"True","img/RI_MAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    莉莉丝 "「啊……{w=3}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD05"),"True","img/RI_MAD05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH10A_RI010B"
    extend "真是废物」"
    window hide
#SE_VOLC 1,192
#MUS_VOL 64
#ROUTINE_STA
#CHR_POS_AUTOC 0,(640),F24
#CHR_ALP_AUTOC 0,0,1,F24
#ROUTINE_STP
#ROUTINE_STA
    hide lh0 with dissolve
#CHR_ALPC 0
#CHR_SET_BACK
#CHR_ALPC 2
#CHR_POSC 2,(320-160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB03"),"True","img/TO_MAB03A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
    with dissolve
#ROUTINE_STP
    hide lh1 with dissolve
#BG_ALP_AUTOC 0,0,0,F24,24
#CHR_ALP_AUTOC 2,128,0,F24,24
#BG_ALP_SAVEC 0
#CHR_ALP_SAVEC 2
#ROUTINE_STA
#BG_SWPC 0
    hide bg2 with dissolve
#BG_PRI 0
#BG_PRI 2
#BG_ALPC 2
#BG_UVC 2,0,0,640,448
#CHR_SWPC 1
    hide lh2 with dissolve
#CHR_ALPC 2
#CHR_SORT 0,1
#ROUTINE_STP
    voice "NCH10A_TO008"
    亨 "「真是废物啊」"
    window hide
#SE_VOLC 1,255
    stop music fadeout 1
#MOV_CHR_INIT 64
#MOV_CHR1 0
#MOV_CHR_GO 1
    hide lh1 with dissolve
#CHR_ALPC 1
    "两个人一起走掉了。"
    "这帮家伙……。乱说一气。"
    voice "NCH10A_CH000"
    智纱？ "「志雄君」"
    "嗯？"
#BG_OVER_MGNC_F BG08AA,0,CH_LKA01,CH_LAA01
    scene expression "img/BG08AA@2x.jpg" as bg0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAA01"),"not F103==0","img/CH_LKA01A@2x.png","True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "BGM03"
    "向着声音的方向转过去，智纱正站在教室的门口。看来是今天也来迎接我了。"
    scene expression "img/BG07AA3@2x.jpg" as bg_over zorder 2 with dissolve
    play sound "SE03_12"
    "我叹着气，把东西收拾到书包里，站了起来。"
    window hide
#SE_VOLC 1
#BG_OVER_MGNC_F BG08AA,0,CH_LKA01,CH_LAA01
    scene expression "img/BG08AA@2x.jpg" as bg0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAA01"),"not F103==0","img/CH_LKA01A@2x.png","True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH10A_CH001"
    智纱 "「今天也有学生会的工作吗？」"
    志雄 "「嗯，算是吧。不过我觉得也就是打声招呼，说句第二学期也加油吧就完事了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAC02"),"not F103==0","img/CH_LKC02A@2x.png","True","img/CH_LAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH10A_CH002A"
    智纱 "「这样啊……{w=3}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAC01"),"not F103==0","img/CH_LKC01A@2x.png","True","img/CH_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH10A_CH002B"
    extend "那，我等你吧」"
    志雄 "「你先回去也可以的啊？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAA01"),"not F103==0","img/CH_LKA01A@2x.png","True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH10A_CH003"
    智纱 "「没事，我去图书室学习。再见」"
    window hide
#SE_VOLC 1,255
    stop music fadeout 1
    play sound "SE01_04L"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    pause (8/32.0)
    stop se
    "啊，走掉了……。"
    志雄 "「没办法啊……」"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 1
#BG_COLC 1,0,0,0
#BG_SETWC 0,1,BG03AA,NIMG01B
#EFF_STAC 0,CLOUD_B,EFF_SKIP
    show expression "img/NIMG01B@2x.png"
    show expression "img/CloudB1_0@2x.png" as cloud0 zorder 5:
        ycenter .55
        xcenter .75
        linear 500 xcenter .0
    show expression "img/CloudB1_1@2x.png" as cloud1 zorder 5:
        ycenter .55
        xcenter .65
        linear 500 xcenter .0
    show expression "img/CloudB2_0@2x.png" as cloud2 zorder 8:
        ycenter .3
        block:
            xcenter 1.0
            linear 140 xcenter .0
            repeat
    show expression "img/CloudB2_1@2x.png" as cloud3 zorder 8:
        ycenter .2
        block:
            xcenter 1.0
            linear 100 xcenter .0
            repeat
    show expression "img/CloudB2_2@2x.png" as cloud4 zorder 8:
        ycenter .0
        block:
            xcenter 1.0
            linear 120 xcenter .0
            repeat
    show expression "img/CloudB3@2x.png" as cloud5 zorder 10:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.5
            linear 50 xpos .0
            xpos 1.0
            linear 50 xpos .5
            repeat
    show expression "img/CloudB4@2x.png" as cloud6 zorder 12:
        xanchor 1.0
        yalign 1.0
        block:
            xpos .6
            linear 78 xpos .0
            xpos 1.0
            linear 52 xpos .6
            repeat
    show expression "img/CloudB5@2x.png" as cloud7 zorder 15:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.2
            linear 20 xpos .0
            xpos 1.0
            linear 100 xpos .2
            repeat
    with dissolve
    pause 2
    scene expression "img/BG03AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MKB05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MAB05"),"not F103==0","img/CH_MKB05A@2x.png","True","img/CH_MAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "学生会那边不到一个小时就完事了，我决定先去图书室找智纱然后再一起回去。"
    window hide
#BG_COLC 1,128,128,128
    play sound "SE05_15L"
    pause (32/32.0)
#EFF_STAC 1,LENZ,EFF_SKIP
#FADE_IN 1
    play music "OBGM17"
    "我受着强烈的日光和地面的炙烤，一边流着汗，一边向前走着。"
    "但是这种炙烤一般的炎热，用不了多久也该说再见了。不经意间，一阵风吹过，风中已经带着少许秋天的凉意。"
    "季节确实已经在改变了。"
    window hide
#EFF_STPC 0,EFF_NOSKIP
#EFF_STPC 1,EFF_NOSKIP
#SE_VOLC 1,
    hide bg1 with dissolve
    voice "NCH10A_CH004"
    智纱 "「今年的夏天，也已经过完了呢」"
    "夏天结束了，到考试已经没什么时间了。升学志愿组已经开始一起进行最后的冲刺了吧。"
    "但是我们，还没有决定自己的志愿。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MKB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MAB01"),"not F103==0","img/CH_MKB01A@2x.png","True","img/CH_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH10A_CH005"
    智纱 "「今天也一起学习吗？」"
    志雄 "「嗯，就这样吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MKB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MAB02"),"not F103==0","img/CH_MKB02A@2x.png","True","img/CH_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "但是，最近开始觉得，那不也挺好嘛。"
    "和智纱的关系也是，学习也是——我们，按照自己的步调来走就好了。"
    "不着急，慢慢地来。"
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
#MOV_PLY 6
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
    $ renpy.end_replay()
    return