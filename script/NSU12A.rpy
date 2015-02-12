label NSU12A:
    $currentlabel = "NSU12A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '29'
    $date = '6'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
    show expression "img/NIMG15L-568h@2x.jpg" as cal zorder 5
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
    show expression "img/NIMG02A@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/NIMG02A@2x.jpg" as bg0 with dissolve
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
    志雄 "「嗯…………呜啊啊啊啊啊啊啊啊」"
    "听到服务员告知食堂里可以吃早餐的消息，我睁开了眼睛。"
    "伸懒腰的同时，打了一个大大的呵欠。"
    "不知不觉已经到早上了啊……"
    "结果发现自己几乎是一夜未眠。"
    "闭上眼睛，脑海中便浮现铃的美丽身姿。"
    window hide
    show expression "img/BG63MA3@2x.jpg" as bg0 with dissolve
    scene expression "img/BG63MA1@2x.jpg" as bg0 with dissolve
    "我又打了一个大大的呵欠，摇了摇还在睡梦中的铃。"
    play sound "SE03_85"
    志雄 "「铃，该起床了——」"
    voice "NSU12A_SU000"
    铃 "「唔～，已经早上了？」"
    window hide
    stop se
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGA05"),"True","img/SU_LGA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "BGM11"
    "铃缓缓地坐起身来。"
    "眼睛还没完全睁开，看上去一副睡眼朦胧的样子。"
    voice "NSU12A_SU001"
    铃 "「……看来是喝过头了」"
    "多多少少还算有些自知之明。"
    "说起来，喝下去的那些啤酒，都跑到什么地方去了……"
    志雄 "「不要紧吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGC04"),"True","img/SU_LGC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU002"
    铃 "「勉勉强强，吃了早饭大概就可以缓过来了……」"
    "铃摇晃着抓了抓稍微有点乱的头发。"
    "脖子看上去相当妩媚……姑且不说这个，现在很明显是一副宿醉的样子，真的没事么。"
    志雄 "「那、那么，叠好被子吧」"
    voice "NSU12A_SU003"
    铃 "「嗯」"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/EXBG05N@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/EXBG05N@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZEC04"),"True","img/SU_ZEC04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_IN 1
    "食堂的餐桌上摆放着米饭、味噌汤、鱼干和酱菜，典型的日式早餐。"
    voice "NSU12A_SU004"
    铃 "「大概是晚饭太丰盛了，总觉得早饭很寻常」"
    志雄 "「嘘！让旅馆的人听见了可怎么办！」"
    voice "NSU12A_SU005"
    铃 "「好的好的」"
    志雄 "「那我开动了」"
    "这个人真是的……"
    "叹了一口气，我用筷子夹起鱼干尝了一口后，吃惊地望向铃。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZEC05"),"True","img/SU_ZEC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "铃也同样看着我的脸。"
    voice "NSU12A_SU006A"
    铃 "「唔……唔……嗯？{w=3}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZEC01"),"True","img/SU_ZEC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU006B"
    extend "……原来如此」"
    志雄 "「喂，铃……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZEB01"),"True","img/SU_ZEB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU007"
    铃 "「我收回“寻常”的发言，这个鱼干还是很美味的」"
    志雄 "「是啊！这样的鱼干还是第一次吃到！」"
    "看来我们在想的是同一件事。"
    voice "NSU12A_SU008"
    铃 "「是吧？」"
    志雄 "「只要有这个鱼干，其它的菜都没必要上了」"
    "面对味道极其鲜美的鱼干，铃一下子清醒了。"
    "两人于是闷声吃着早饭。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG63MA1@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG63MA1@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LEB01"),"True","img/SU_LEB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE05_14L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,64
    voice "NSU12A_SU009"
    铃 "「呼……吃完了吃完了」"
    志雄 "「怎么样？精神些了？」"
    voice "NSU12A_SU010"
    铃 "「精神多了，果然早饭是基础啊」"
    "太好了，铃看上去好像恢复生气了。"
    志雄 "「那今天去什么地方？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LEB02"),"True","img/SU_LEB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU011"
    铃 "「嗯，今天天气很好，风也很合适，到湖边去玩吧！」"
    "铃举起拳头宣布。"
    志雄 "「哇，鼓掌鼓掌……等等，难道还要下水么？我可没准备泳衣啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LEA01"),"True","img/SU_LEA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU012"
    铃 "「是么，那就在路上买一件吧」"
    志雄 "「这倒也可以……」"
    "如果早一点说的话，就可以省下不必要的费用——我慌忙咽下这句话。"
    "没必要特意去打击铃的情绪。"
    "比起这个，更该考虑的是应该如何享受今天。"
    "别在像昨天那样被捉弄，希望铃对我多少有一点异性意识吧……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LEB01"),"True","img/SU_LEB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU013"
    铃 "「好的，那出发吧」"
    志雄 "「咦，就这样走吗？不骑摩托车吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LEC05"),"True","img/SU_LEC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU014"
    铃 "「嗯，既然去游泳的话就不骑摩托车了。等游完都累得不行了，那样的话就算想骑摩托车也骑不动了吧？」"
    志雄 "「原来如此。游泳之后浑身会酸痛，我也有同感」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LEB02"),"True","img/SU_LEB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU015"
    铃 "「那就出发吧！」"
    "由于以上原因，我们首先去车站附近的商店街买泳衣。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG68AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG68AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LEA01"),"True","img/SU_LEA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE08_18L"
    pause (32/32.0)
#BG_BLUR 0
#FADE_IN 1
#SE_VOLC 1,64
    play music "BGM12"
    voice "NSU12A_SU016"
    铃 "「不愧是车站附近，还真是嘈杂。我去那边的店里买吧？」"
    志雄 "「嗯，买个差不多的就可以了」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LEA05"),"True","img/SU_LEA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU017"
    铃 "「不要买吓人的那种哦～」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "男式泳衣里哪有什么吓人的款式啊……"
    "三角泳裤或兜裆布之类的？"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
#BG_UVC 0,0,512,640,448
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LEC05"),"True","img/SU_LEC05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (32/32.0)
#SE_VOLC 1,64
#FADE_IN 1
    voice "NSU12A_SU018"
    铃 "「唔」"
    "铃上下打量着我买的泳衣。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LEB01"),"True","img/SU_LEB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU019"
    铃 "「不错，选了件比较正常的」"
    "我买的是到膝盖以上的那种普通的款式。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LEA05"),"True","img/SU_LEA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU020"
    铃 "「虽说在这种地方捉弄人是很招人厌的，不过那家伙就经常开这种玩笑」"
    "那家伙？啊，是稻穗吧。"
    "……说起来，那个人会穿成什么样啊。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LEA01"),"True","img/SU_LEA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU021"
    铃 "「说起来志雄这个样子也非常有趣，真的很不错，放心吧」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    志雄 "「等等，就算你说很有趣……哎？」"
    "我正准备辩驳的时候，铃已经飞快地走在了前面。"
    "这么做好狡猾……"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG69AA1@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG69AA1@2x.jpg" as bg0 with dissolve
    play sound "SE05_21L"
    pause (32/32.0)
#FADE_IN 1
    play sound "SE05_12"
#EFF_STAC 0,TWINKLE4,EFF_SKIP
    "乘公交车来到湖畔的我们，在更衣室换好衣服并存好行李后，走到了湖边。"
    "阳光照得眼睛发痛，沙子也散发着热气。"
    志雄 "「今天还是很热啊……」"
    voice "NSU12A_SU022"
    铃 "「志雄，让你久等了～！」"
    window hide
#SE_VOLC 1,0
#BG_GET_NOC 0,F34
#BG_SET_BACK 
#EFF_PRI 0
#BG_PRIC 0
#BG_INIC 3
    show expression "img/NIMG01B@2x.png" as bg3 with dissolve
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
#EFF_STAC 0,CLOUD_B,EFF_NOSKIP
#BG_PRIC 0
    play sound "SE07_25"
#BG_SET_BACK 
#BG_INIC 1
#BG_INIC 0
#BG_PRI 1
#BG_POSC 1,0,-448,640,448
    scene expression "img/NIMG18D@2x.jpg" as bg1 zorder 100:
        linear 2 ypos 0.0
    with dissolve
    play sound "SE07_23"
#EFF_STPC 0,EFF_NOSKIP
#EFF_PRI 0
#BG_ALP_AUTOC 3,0,0,F24
#BG_POS_AUTOC 1,,F24,192
#BG_POS_AUTOC 0,,448,,F24,192
#EFF_STAC 0,LATHER,EFF_SKIP
#BG_ALP_SAVEC 3
#BG_POS_SAVEC 1
#BG_POS_SAVEC 0
#BG_ERSWC 0,3,BG_NOFADE
#BG_COLC 0,128,128,128,128
#BG_UVC 0,0,0,640,448
#BG_ALPC 3,128
#SE_VOLC 1,128
    play music "BGM05"
#EFF_STPC 0,EFF_NOSKIP
#BG_PRI 1
#BG_COL_AUTOC 1,128,128,128,128,1,F24
#BG_COL_SAVEC 1
#BG_SET_BACK 
#BG_INIC 0
    #show expression "img/F34@2x.jpg" as bg0 zorder 0 with dissolve
    "回过头去，映入眼帘的是一副不输给太阳的绚丽景色。"
    "穿着泳衣的铃正微笑着走过来。"
    "泳衣很适合她那苗条的身材……"
    志雄 "「啊……」"
    voice "NSU12A_SU023"
    铃 "「怎么样？是之前新出的泳衣哟」"
    "铃的身材高挑，肌肉紧绷，就算说是模特也不过分。"
    "顺便一提，我发现不仅是我，其他客人也有视线集中在铃的身上。"
    "唔……我真的可以在这个人身边吗？"
    "那威风凛凛的举止，更为她增添了一份美感，就好像能看到Ａｕｒａ一般……"
    window hide
    hide bg1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    scene expression "img/BG69AA1@2x.jpg" as bg0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MFA06"),"True","img/SU_MFA06A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#EFF_PRI 0
#EFF_STAC 0,TWINKLE4,EFF_SKIP
    voice "NSU12A_SU024"
    铃 "「在发什么呆呢……喂～，志雄？」"
    voice "NSU12A_SU025"
    铃 "「我说……你要看到什么时候，至少也说说感想啊」"
    志雄 "「哎？对不起」"
    "我慌忙避开铃的视线。"
    "脸颊变得滚烫，似乎并不只因为天气炎热的原因。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MFB01"),"True","img/SU_MFB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU026"
    铃 "「……怎么样？」"
    志雄 "「非、非常合适，相当的不错」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MFB02"),"True","img/SU_MFB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU027"
    铃 "「呵呵，多谢夸奖」"
    "太好了……铃看起来很高兴的样子。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MFA01"),"True","img/SU_MFA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU028"
    铃 "「首先，我们玩什么好呢？」"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "马上去游泳吧":
            $F7=0
        "稍微晒一下日光浴吧":
            $F7=1
    if F7==0:
        jump L_NSU12A_SEL00_A
    if F7==1:
        jump L_NSU12A_SEL00_B
label L_NSU12A_SEL00_A:
    $F4+=1
    $F106=0
#RSET F106
    志雄 "「那还用说，先去游泳吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MFB02"),"True","img/SU_MFB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU029"
    铃 "「好啊，那就去吧！」"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG92AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG92AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_20L"
    pause (32/32.0)
#EFF_PRI 0
#EFF_STAC 0,WATERTWINKLE,EFF_NOSKIP
#FADE_IN 1
    "稍稍做过柔软体操后，我用脚试了试水温。"
    "虽然对海没有什么好的回忆，不过游泳或是在水边玩这样的事倒也不排斥。"
    "只是，最近确实是感觉有点运动不足啊。"
    window hide
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFB05"),"True","img/SU_LFB05A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NSU12A_SU030"
    铃 "「湖水果然很冷。既然还没有适应水温，不如先在这边玩一下吧」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE03_59"
    "铃仰面朝上，轻飘飘地浮在湖面上。"
    "偶尔会翻过身慢慢地游一会儿。"
    "不管做什么都像是画一样美啊……"
    志雄 "「那么我也来游一下吧」"
    "湖水相当的清澈美丽，湖面也很平静，很适合游泳。"
    "再说也不能一直这么看着铃，于是我开始了蛙泳。"
#EFF_STPC 0,EFF_NOSKIP
#BG_BLUR 0
    window hide
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFA01"),"True","img/SU_LFA01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NSU12A_SU031"
    铃 "「志雄也做完热身运动了么」"
    "铃一下子游到我身边。"
    志雄 "「和学校的泳池比起来，这里真是太棒了」"
    voice "NSU12A_SU032"
    铃 "「嗯。这边差不多总是晴空万里、风平浪静，感觉非常的舒适」"
    voice "NSU12A_SU033"
    铃 "「接下来我们差不多该认真游了吧。不如就游到那个地方吧」"
    "顺着铃指的方向，可以看到远处漂浮着浮标。"
    "虽然有些距离，游过去还是没有什么问题的。"
    志雄 "「好，现在就让你见识一下高中生的体力」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFC05"),"True","img/SU_LFC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU034"
    铃 "「哼哼，说得好。既然是比赛，输了的话就要接受惩罚哟」"
    志雄 "「求之不得！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFC01"),"True","img/SU_LFC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU035"
    铃 "「那么、准备、开始！」"
    window hide
#BG_BLUR 0
#EFF_PRI 0
#EFF_STAC 0,WATERTWINKLE,EFF_NOSKIP
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE03_76"
    "话音刚落，铃就以优美的自由泳姿势出发了。"
    志雄 "「要输了啊！」"
    window hide
    stop se fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_NOSKIP
#BG_UVC 0,0,512,640,448
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFA01"),"True","img/SU_LFA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (64/32.0)
    stop se
#BG_BLUR 0
#FADE_IN 1
    志雄 "「啊～，累死了」"
    voice "NSU12A_SU036"
    铃 "「志雄也应该稍微运动一下啊。年轻的时候不运动的话，以后就不好办了啊」"
    志雄 "「也许吧……」"
    "结果，被铃甩开一大截……毫无疑问输掉了。"
    "不管怎么说，能灵活运用身长的自由泳，实在太犯规了。"
    "不管我如何努力，也无法缩短这种差距。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFB01"),"True","img/SU_LFB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU037"
    铃 "「那么，接下来的话……」"
    window hide
    play sound "SE06_22L"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_BLUR 0
#EFF_PRI 0
#EFF_STAC 0,WATERTWINKLE,EFF_NOSKIP
    "就在这时，在我们的视线前方，驶过来一辆摩托艇。"
    "摩托艇后面牵引着一辆香蕉船，上面的女孩子正发出欢快的笑声。"
#EFF_STPC 0,EFF_NOSKIP
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFC06"),"True","img/SU_LFC06A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    "在我身边的铃似乎也有点跃跃欲试。那……就试试这个吧。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFC01"),"True","img/SU_LFC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU038"
    铃 "「喂、志雄，我们坐这个吧。借不到的话就坐香蕉船好了」"
    志雄 "「果然……」"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1
#BG_UVC 0,0,0,640,448
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    pause (32/32.0)
    stop se
    stop sound
#FADE_IN 1
    jump L_NSU12A_SEL00_X
label L_NSU12A_SEL00_B:
#RSET F106
    $F106=1
    志雄 "「阳光稍微有点强烈」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MFA05"),"True","img/SU_MFA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU039"
    铃 "「嗯～，这么玩的话，是很容易晒黑。不过」"
    "就凭这种说话的口气，铃果然是个户外活动派……"
    "无论是游泳还是玩水，铃都是一副投入的样子。"
    "而我多多少少希望能和铃像情侣一样，在这边悠闲地待着。"
    志雄 "「对了，铃你最近这么忙，一直待在屋里没出来吧？不如趁这个时侯好好享受一下阳光」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MFA02"),"True","img/SU_MFA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU040"
    铃 "「我是陈年的被褥吗……」"
    voice "NSU12A_SU041"
    铃 "「不过，在夏天这样的皮肤确实是显得苍白了些呢」"
    "铃一边看着自己的上臂一边呢喃道。"
    志雄 "「我也是因为在屋内待的时间有些长，才想晒晒太阳」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MFB01"),"True","img/SU_MFB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU042"
    铃 "「偶尔这样也无妨。那么，就好好享受一下疗养院的待遇吧」"
    志雄 "「就是说嘛。玩的时间再怎么都是有的」"
    window hide
#FADE_OUT 1
    stop sound fadeout 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    stop sound
#BG_SET_BACK 
#BG_INIC 1
#BG_POSC 1,0,0,640,448
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU06A")]=True
    show expression "img/EVN_SU06A@2x.jpg" as bg1 zorder 1 with dissolve
    play sound "SE05_19L"
    pause (32/32.0)
#MUS_VOL 64
#FADE_IN 1
    pause (32/32.0)
#BG_POS_AUTOC 1,256,,,F34,96
#BG_POS_SAVEC 1
#BG_POS_SAVEC 3
#BG_FLG EVN_SU06A
    voice "NSU12A_SU043"
    铃 "「嗯～」"
    志雄 "「啊，真暖和啊……」"
    "铺好随身带来的垫子，以毛巾代替枕头躺下来，很快就感觉到背部开始发热。"
    "看到身边铃也在做着同样的动作，我闭上了眼睛。"
    voice "NSU12A_SU044"
    铃 "「多亏了这么好天气。估计不一会儿就会晒黑吧」"
    志雄 "「是啊。估计回去的时候皮肤会被晒得脱层皮了」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU06B")]=True
    show expression "img/EVN_SU06B@2x.jpg" as bg1 with dissolve
    voice "NSU12A_SU045"
    铃 "「不凃防晒油是不行的。就算是晒太阳，不凃防晒油的话，皮肤会变得粗糙，不注意的话还会长水泡」"
    志雄 "「这样就不好了……」"
    voice "NSU12A_SU046"
    铃 "「事实如此嘛。把我的防晒油借你吧？」"
    "……诶？如此说来，难道铃已经涂过防晒油了？"
    "这种情节，怎么感觉像是电视剧或是漫画里那样的展开呢？"
    志雄 "「……铃涂过防晒油了吗？」"
    voice "NSU12A_SU047"
    铃 "「嗯？当然涂了啊，这不是理所应当的吗……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU06C")]=True
    show expression "img/EVN_SU06C@2x.jpg" as bg1 with dissolve
    voice "NSU12A_SU048"
    铃 "「啊，莫非……莫非是在期待着『我说，能帮我涂一下防晒油吗？』这样的场景吗？」"
    志雄 "「没、没这回事」"
    "……话音刚落，又开始痛恨起自己的言不由衷。"
    voice "NSU12A_SU049"
    铃 "「一边对着女生的皮肤心动不已，一边又诚惶诚恐地涂着，想着“泳衣下面怎么办呢？要不要涂呢？”这种问题……」"
    志雄 "「这种事……」"
    "真的没去想啊！"
    "……只是稍微有点罢了。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU06B")]=True
    show expression "img/EVN_SU06B@2x.jpg" as bg1 with dissolve
    voice "NSU12A_SU050"
    铃 "「真是遗憾，刚刚换衣服的时候我已经涂过啦……哈哈，我在自己的书里早就写过的，怎么会忘记这种情景呢」"
    "……竟然还写过。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU06C")]=True
    show expression "img/EVN_SU06C@2x.jpg" as bg1 with dissolve
#BG_FLG EVN_SU06C
    voice "NSU12A_SU051"
    铃 "「呵呵，那现在还要帮我涂吗？」"
    "可恶，在铃看来，绝对把我当成那种不敢做这种事的笨蛋了吧。"
    "想到这……"
    志雄 "「好！那现在就让我塚本志雄，来为您涂防晒油吧！」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU06D")]=True
    show expression "img/EVN_SU06D@2x.jpg" as bg1 with dissolve
#BG_FLG EVN_SU06D
    voice "NSU12A_SU052"
    铃 "「诶？你是认、认真的？」"
    voice "NSU12A_SU053"
    铃 "「刚刚是在开玩笑呢，玩笑！当然不行啦！」"
    志雄 "「什么嘛……」"
    "当然，如果真让我站在铃面前，我肯定也是什么都不敢做的。"
    "算了，早知道这样开始时就不说那些话了……"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU06A")]=True
    show expression "img/EVN_SU06A@2x.jpg" as bg1 zorder 1 with dissolve
#BG_FLG EVN_SU06A
    stop sound
    pause (32/32.0)
    play sound "SE06_22L"
    pause (32/32.0)
#FADE_IN 1
    voice "NSU12A_SU054"
    铃 "「嗯？」"
    window hide
    scene expression "img/BG69AA1@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MFB01"),"True","img/SU_MFB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#MUS_VOL 128
    hide bg1 with dissolve
    "在享受了片刻的日光浴后，我听见远处传来了引擎声。"
    "铃似乎也注意到了，眺望着在湖面上行驶的摩托艇。"
    voice "NSU12A_SU055"
    铃 "「啊，是摩托艇，似乎很好玩呢」"
    "铃将视线转回到湖边，眺望着附近的码头。"
    志雄 "「怎么了？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MFB02"),"True","img/SU_MFB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU056"
    铃 "「那边好像有租船的，去看看吧！」"
    "果然呢，铃不想就这么悠哉地消磨时间……"
    "我追着兴高采烈跑向码头的铃，不禁感慨起来。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
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
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG92AA@2x.jpg" as bg0 zorder 0 with dissolve
#EFF_STPC 0,EFF_NOSKIP
    scene expression "img/BG92AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    jump L_NSU12A_SEL00_X
label L_NSU12A_SEL00_X:
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFB01"),"True","img/SU_LFB01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NSU12A_SU057"
    铃 "「准备好啦～？」"
    志雄 "「稍等一下」"
    "意外的是，原来摩托艇只要简单接受讲解就可以借来操纵了。"
    "只是，无法进行长距离长时间的航行，仅限于在监视船所能看到的范围内航行。"
    志雄 "「嗯，ＯＫ」"
    "事先已经对各种可能遇到的危险做了讲解，救生衣也已经反复检查过了。"
    志雄 "「如此说来，铃有摩托艇的经验吧？」"
    voice "NSU12A_SU058"
    铃 "「什么？我也是第一次啊！」"
    "咦，第一次！？"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFB02"),"True","img/SU_LFB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU059"
    铃 "「好极了！那么，出发吧！」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU07A")]=True
    show expression "img/EVN_SU07A@2x.jpg" as bg1 zorder 1 with dissolve
    play sound "SE06_45L"
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
#BG_UVC 0,0,0,640,448
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NSU12A_SU060"
    铃 "「呀————！」"
    志雄 "「啊啊啊啊啊啊！！！！」"
    "铃一副兴致勃勃的样子，从一开始就把节气杆拉到了最大。"
    "因为两个人乘坐的缘故，指导员说力度可能会有些不够，我还以为会更慢一些……"
    voice "NSU12A_SU061"
    铃 "「啊，心情超舒畅～，看！论体感速度的话这边比摩托车更快啊！」"
    "速度实在是太快了啊！"
    "根本不知道实际开出了几公里，只感觉到冲击在身体上的水流相当激烈，沿途的风景也是一瞬间从眼前擦过，真实效果超群的极速感。"
    voice "NSU12A_SU062"
    铃 "「好极了，总算掌握到要领了！」"
    "感觉有什么要发生，有种不祥的预感……"
    志雄 "「以防万一我提醒一下，请注意安全驾驶……」"
    "但是话音未落，铃已经开始一点一点地掉头。"
    voice "NSU12A_SU063"
    铃 "「好，ＯＫ！」"
    志雄 "「哇哇哇！」"
    "因为摩托艇左右剧烈地摇晃着，我拼命抓住铃不放。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU07B")]=True
    show expression "img/EVN_SU07B@2x.jpg" as bg1 with dissolve
    voice "NSU12A_SU064"
    铃 "「好开心啊！！志雄，我是不是很厉害啊！？」"
    志雄 "「唔，有点胡来啊……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU07A")]=True
    show expression "img/EVN_SU07A@2x.jpg" as bg1 with dissolve
    voice "NSU12A_SU065"
    铃 "「那么接下来，要准备快速转弯了啊！」"
    志雄 "「这太乱来了吧……」"
    "就在我被铃吸引去注意力的一瞬间……"
    play sound "SE06_41"
    "摩托艇闪电般转头！"
    window hide
#SE_VOLC 1,64
    stop music fadeout 1
    show expression "img/IBG01B@2x.jpg" as bg1 with ImageDissolve("img/BG_MASK23@2x.png",1)
    "迄今为止从未感受过的离心力正把我的身体从摩托艇上甩出去。"
    "……在那一瞬间看到的天空，竟是蓝得如此的透彻而一望无垠。"
    window hide
#SE_VOLC 1,0,16
    play sound "SE04_14"
    show expression Solid("000") as bg1 with ImageDissolve("img/BG_MASK15@2x.png",1)
#SE_WATC 0
    play sound "SE07_05L"
    show expression "img/OIBG010A@2x.png" as bg1 with dissolve
#EFF_PRI 0
#EFF_STAC 0,SHAKE_WATER,EFF_NOSKIP
    "……"
    "…………"
    window hide
    stop se
#SE_WATC 0
    play sound "SE03_87"
#SE_VOLC 1,255,16
#EFF_STPC 0,EFF_NOSKIP
    hide bg1 with dissolve
#EFF_PRI 0
#EFF_STAC 0,WATERTWINKLE,EFF_NOSKIP
    志雄 "「啊！」"
    window hide
#EFF_STPC 0,EFF_NOSKIP
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFA03"),"True","img/SU_LFA03A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    play music "OBGM27"
    voice "NSU12A_SU066"
    铃 "「志雄！不要紧吧！？」"
    window hide
    stop sound fadeout 1
    play sound "SE06_13L"
    "铃慌张地降低速度转回来，利用惯性朝我过来。"
    "身上的救生衣让我浮了起来，只是呛了点水就能了事……"
    志雄 "「啊……不碍事」"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,SU_LXB04,2,F24
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFB04"),"True","img/SU_LFB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NSU12A_SU067"
    铃 "「真的吗？没受伤吧？疼吗？」"
#THREAD_STP 1
    hide bg3 with dissolve
    志雄 "「真的没事」"
    "我游到完全停下来的水上摩托车前，重新爬上后面的座位。"
    志雄 "「只是吓了一跳而已，没事的，也没有什么受伤的地方」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFC04"),"True","img/SU_LFC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU068"
    铃 "「真的对不起！有点兴奋过头了」"
    "铃抱歉地低下了头。"
    志雄 "「不是挺好玩的嘛，别在意了。只是，希望你能稍稍注意点安全驾驶吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFC02"),"True","img/SU_LFC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU069"
    铃 "「唔，知道了。我会注意的……」"
    window hide
    stop se fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    pause (32/32.0)
    stop se
    stop sound
    stop music fadeout 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFA01"),"True","img/SU_LFA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE06_46L"
    pause (32/32.0)
#FADE_IN 1
    play music "BGM05"
    voice "NSU12A_SU070"
    铃 "「真的很开心，风吹过的感觉也很舒服」"
    志雄 "「是啊」"
    "这就像平时骑摩托车一样，感受着相同的速度和空气。"
    "看着像孩子一样天真无邪玩闹着的铃，我目不转睛地注视着她的身姿。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG69AA1@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG69AA1@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFB02"),"True","img/SU_LFB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE05_21L"
#BG_BLUR 0
#FADE_IN 1
    voice "NSU12A_SU071"
    铃 "「哈哈～，玩够了玩够了」"
    志雄 "「确实是有点累了」"
    "到了湖边，才注意到时间已经过去了大半。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFB01"),"True","img/SU_LFB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU072"
    铃 "「去吃点什么吧？」"
    志雄 "「顺便休息一下，稍微走走吧」"
    stop music fadeout 1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFC05"),"True","img/SU_LFC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU073"
    铃 "「嗯」"
    "就在我们准备出发的时候，突然铃的视线中有个人影晃了一下。"
    "定睛一看，有个女孩蹲在前面。"
    window hide
#SE_VOLC 1,64
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_BLUR 0
#EFF_PRI 0
#EFF_STAC 0,TWINKLE4,EFF_NOSKIP
    play music "OBGM14"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SFC05"),"True","img/SU_SFC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU074"
    铃 "「喂，不要紧吧？」"
    "铃跑过去问道。"
    voice "NSU12A_XT000"
    女孩 "「……似乎有点站不稳」"
    voice "NSU12A_SU075"
    铃 "「是贫血？还是中暑？到这边去吧」"
    "铃扶着对方向附近的小卖部伞下走去。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SFC03"),"True","img/SU_SFC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU076"
    铃 "「志雄，去买两瓶运动饮料吧！」"
    志雄 "「嗯，好的」"
    window hide
#FADE_OUT 1
#BG_UVC 0,0,512,640,448
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFC05"),"True","img/SU_LFC05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE03_96"
#EFF_STPC 0,EFF_NOSKIP
#BG_BLUR 0
#FADE_IN 1
    "我去自动贩卖机买饮料，铃又回到了生病的女孩身边。"
    志雄 "「来、给你！」"
    voice "NSU12A_SU077"
    铃 "「谢谢。身体如何？稍微喝一点吧？」"
    "铃向小卖部的人说明情况，让女孩在帐篷的阴凉处休息。"
    "自己就这样在旁边照看。"
    "利索地处理着中暑症状，铃的应急处置能力很出色。"
    "果然是个厉害的人啊。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
#BG_BLUR 0
#BG_UVC 0,0,0,640,448
    stop music fadeout 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFC05"),"True","img/SU_LFC05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE06_26"
    pause (32/32.0)
#SE_VOLC 1,255
#FADE_IN 1
    play music "BGM13"
    志雄 "「没关系了吧？」"
    "女孩似乎是当地人，一个人过来玩。"
    "平时都没事……所以自己并没有多加注意不管不顾地玩结果就成了这样了。"
    voice "NSU12A_SU078"
    铃 "「症状倒不是特别严重，应该不碍事……慎重起见还是先住院观察，中暑是很可怕的」"
    "铃非常担心，一直把她送上救护车。"
    志雄 "「话说回来，铃对中暑的应急处理很了解啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFC01"),"True","img/SU_LFC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU079"
    铃 "「唔～，在夏天摩托车骑的时间太长的话是会中暑的、所以得多留心啊」"
    志雄 "「是啊……那铃也要注意了」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFB01"),"True","img/SU_LFB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU080"
    铃 "「当然了」"
    "当然？铃，你可是有过骑摩托车骑到晕倒的前科呢……"
    "我想起第一次捡到晕倒的人的事，不由得苦笑出来。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LFA01"),"True","img/SU_LFA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU12A_SU081"
    铃 "「话说回来，还好没出什么大事」"
    "铃松了口气，脸上重新浮现出微笑。真是个喜欢帮助别人的人呢。"
    "认识到这样的铃，我也不由自主地笑了起来。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop se
    stop sound
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT