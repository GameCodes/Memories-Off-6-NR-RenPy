label NSU08A:
    $currentlabel = "NSU08A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '28'
    $date = '5'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG60AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG60AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_15L"
    pause (32/32.0)
#FADE_IN 1
    play music "BGM11"
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
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    voice "NSU08A_SU000"
    铃 "「到了～」"
    "离开服务区后，途中包含加油的一个小时后，最后到达了目的地龙境温泉。"
    志雄 "「呼，总算平安到达了」"
    "我们预定的住宿处，是从马路一直延伸至小巷中的纯和式旅馆。"
    if not persistent.dictlist[49] and persistent.show_dict:
        $persistent.dictlist[49]=True
        show screen dict_pop(i=49)
    志雄 "「是叫宝树庵啊，总觉很有氛围呢～，那种古代的文豪闭门写作的感觉」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    voice "NSU08A_SU002"
    铃 "「似乎会让什么灵验呢。接下来……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC01"),"True","img/SU_LCC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    "铃边说边把摩托车放入停车场。"
    "我用力伸了个懒腰，果然身体已经僵硬了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC02"),"True","img/SU_LCC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    voice "NSU08A_SU003"
    铃 "「抱歉，骑这么长时间的摩托车太累了吧？」"
    志雄 "「嗯，是有一点」"
    "虽然真的很累，但不太想在铃面前露出自己的软弱。"
    "而且和铃亲密接触的时光，就足以让我感到高兴和振奋。"
    voice "NSU08A_SU004"
    铃 "「说起来我也有点累了」"
    志雄 "「哈哈哈」"
    志雄 "「不过摩托太热了，吹吹风会凉快些吧」"
    "摩托自身发出的热量，再加上道路的反射光线相当强烈。"
    "这两方面加起来比起阳光的照射还要恐怖。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA01"),"True","img/SU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    voice "NSU08A_SU005"
    铃 "「是吧？炎热的夏天像北海道这样的高地是不能去的，摩托是最基本的冬寒夏暖的交通工具」"
    志雄 "「还真是挺不方便的交通工具啊……」"
    voice "NSU08A_SU006"
    铃 "「如果要方便的话坐汽车最好不过，而摩托则更有趣味性，不“喜欢”的话就不要坐」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB04"),"True","img/SU_LCB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    "说到这里，铃慌忙组织起语言。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB05"),"True","img/SU_LCB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    voice "NSU08A_SU007"
    铃 "「可是你看，在美丽的景色中飞驰，可以直接感受空气的存在」"
    志雄 "「啊哈哈，没关系，我并不讨厌摩托车。要说喜欢不喜欢的话，我还是属于喜欢的那派」"
    window hide
#BG_SET_BACK 
#FADE_OUT 1
#BG_INIC 1
#TODO
    show expression "img/NIMG01B@2x.png" as bg1 zorder 100 with dissolve
#EFF_STAC 0,CLOUD_B,EFF_SKIP
#SE_VOLC 1,0
    play sound "SE06_39L"
#BG_ALP_SAVEC 1
#FADE_IN 1
    "的确，沿海飞驰的畅快和驶向山顶的清爽感，在电车和汽车的移动过程中是感受不到的。"
    "感受着轻风的吹拂……这句话我可以真切地体会到。"
    window hide
    stop se fadeout 1
#SE_VOLC 1,0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_OUT 1
#BG_ALPC 1
#EFF_STPC 0,EFF_SKIP
    hide bg1 with dissolve
#FADE_IN 1
    voice "NSU08A_SU008"
    铃 "「是么，那就太好了」"
    志雄 "「是啊，和骑摩托的人擦肩而过的时候，会做些什么呢？」"
    "与同样驾车远游的摩托车擦过的时刻，铃举起了左手，对方也举起了左手作为回复。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU08A_SU009"
    铃 "「这个啊，摩托车手的打招呼方式？虽说是友好的寓意……可即使未必友好，竖旗拇指也好敬礼也好怎样都行啦」"
    "铃用左手作着各种各样的手势回答道。她的双眼熠熠生辉，仿佛按下了什么开关。"
    志雄 "「你好像很开心的样子啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA01"),"True","img/SU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU08A_SU010"
    铃 "「我很喜欢一瞬间那种心情共通的感觉。然而最近这样的人少了，毕竟一去不复返的事情也多了」"
    志雄 "「听起来有点寂寞呢」"
    voice "NSU08A_SU011"
    铃 "「乘坐叔叔的摩托时，他说起这些总感觉很惋惜，所以想尽可能做出这样的手势」"
    志雄 "「原来如此，回来的时候我也试着模仿下吧」"
    "坐在摩托上原来也有各种各样的情趣。"
    "听了铃的话，我忽然想坐在摩托上亲自体验一下。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU08A_SU012"
    铃 "「好了，也别站着说话了，先办理下存放行李的手续吧」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    #show expression "img/BG61AA@2x.jpg" as bg1 zorder 1 with dissolve
    stop sound fadeout 1
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    #with dissolve
#BG_SWPC 0
    #hide bg1 with dissolve
#BG_ALPC 1,128
#BG_PRI 0
#BG_PRI 1
    scene expression "img/BG61AA@2x.jpg" as bg0 with dissolve
    stop sound
    voice "NSU08A_XR000"
    仲居のおじさん "「欢迎光临」"
    "伴随着微寒的冷气，迎接我们的是旅馆里的人的招呼声。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+96)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC01"),"True","img/SU_LCC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU08A_SU013"
    铃 "「你好，我是预定过的稻穗」"
    play sound "SE03_44"
    "男服务员走进柜台，好像在确认着底帐。"
    voice "NSU08A_XR001"
    仲居のおじさん "「稻穗女士……是姐弟两个人吧，请稍等一下」"
    "姐弟？铃是以姐弟的名义预约的么。"
    "虽然这样似乎更方便些吧……"
    "话说回来，在铃眼中，我这样的人果然还是个弟弟吧。"
    voice "NSU08A_XR002"
    仲居のおじさん "「请在这里签一下名」"
    voice "NSU08A_SU014"
    铃 "「好的」"
    voice "NSU08A_XR003"
    仲居のおじさん "「这就带您去房间」"
    show expression "img/BG62AA@2x.jpg" as bg_over zorder 2 with dissolve
    voice "NSU08A_XR004"
    仲居のおじさん "「行李的话，立刻帮您搬到房间内」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBA01"),"True","img/SU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU08A_SU015"
    铃 "「谢谢」"
    志雄 "「这么说来行李是事先送过来的，不过有那么多吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBA04"),"True","img/SU_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU08A_SU016"
    铃 "「唔～，摩托车上不能放那么多行李，再加上志雄你还坐在后面。而且，还带来了各种各样的东西」"
    志雄 "「各种各样？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB01"),"True","img/SU_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU08A_SU017"
    铃 "「这个敬请期待」"
    "这笑容……难道有什么企图？"
    志雄 "「……虽然不太明白，但我还是期待一下吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB02"),"True","img/SU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU08A_SU018"
    铃 "「这么说就好，呵呵呵呵」"
    "铃故意装腔作势笑了起来。"
    "这一点倒是和稻穗很像，不愧为姐弟……"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NSU08A_XR005"
    仲居のおじさん "「就是这里」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    show expression "img/BG63AA@2x.jpg" as bg1 zorder 1 with dissolve
    play sound "SE00_46"
    pause (32/32.0)
    play sound "SE00_47"
#BG_ALP_AUTOC 1,128,0,F24,48
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
#BG_ALPC 1,128
#BG_PRI 0
#BG_PRI 1
    scene expression "img/BG63AA@2x.jpg" as bg0 with dissolve
#SE_WATC 0
    "房间是传统的单间旅馆，从某个角落散发出令人怀念的气息。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+224)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MBB01"),"True","img/SU_MBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NSU08A_XR006"
    仲居のおじさん "「晚饭在六点为您送上可以吗？」"
    voice "NSU08A_SU019"
    铃 "「可以」"
    "男服务员说明了几点注意事项，便从房间内走了出去。"
    "怎么？"
    志雄 "「铃？」"
    play sound "SE03_55"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MBA01"),"True","img/SU_MBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NSU08A_SU020"
    铃 "「什么事？」"
    "铃把包放在房间的角落里，可以确定这是之前送过来的旅行提包。"
    志雄 "「只预定了这一间么？」"
    voice "NSU08A_SU021"
    铃 "「是的」"
    志雄 "「为什么？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MBA02"),"True","img/SU_MBA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NSU08A_SU022"
    铃 "「什么为什么？」"
    "这么不可思议的事情，她却……"
    志雄 "「那～个」"
    window hide
    stop music
    play sound "SE07_16L"
    "就是说……我要和铃睡在同一个房间！？"
    "我知道自己的心脏在剧烈地搏动着。"
    "这是怎么回事？就是这么回事么？"
    voice "NSU08A_SU023"
    铃 "「你怎么了？」"
    志雄 "「那、那个……」"
    window hide
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MBA06"),"True","img/SU_MBA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#SE_VOLC 0,255
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,(320+224)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBC01"),"True","img/SU_LBC01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter (320+224)/640.0
    with dissolve
#MOV_CHR_INIT 64
#MOV_CHR0 128,(320)
#MOV_CHR1 0,(320)
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
    hide lh1 with dissolve
#CHR_ALPC 1,128
    voice "NSU08A_SU024"
    铃 "「哈哈～嗯，志雄君？你在想什么呢～？」"
    "铃微微一笑，就像看到猎物的猫一样舔了舔嘴唇。"
    志雄 "「什、什么呀」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBC02"),"True","img/SU_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320)/640.0
    with move
    voice "NSU08A_SU025"
    铃 "「是不是在想歪脑筋，觉得我们要住在一起～？」"
    志雄 "「我、我没想那些啦！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB02"),"True","img/SU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU08A_SU026"
    铃 "「真的么？」"
    "……冒出一身冷汗。"
    voice "NSU08A_SU027"
    铃 "「嗯？」"
    志雄 "「那个，是有一点……」"
    window hide
    stop se
    play music "BGM05"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB02"),"True","img/SU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU08A_SU028"
    铃 "「啊哈哈哈哈哈」"
    "铃大笑起来。"
    voice "NSU08A_SU029"
    铃 "「哈哈，志雄想太多了。和朋友一起旅行的话，大家挤在一起睡很正常哦」"
    "对大人而言这样很正常……是么？"
    "我还以为自己会遇到什么重要的剧情事件……"
    志雄 "「能、能别笑的那么厉害么？我可是单纯的高中生啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB01"),"True","img/SU_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU08A_SU030"
    铃 "「对不起对不起，我有点过火了」"
    志雄 "「我原谅你……但要怎么做呢？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBA01"),"True","img/SU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU08A_SU031"
    铃 "「别担心，而且饭既然是送到这里，住在同一个房间显然更合适吧」"
    志雄 "「这么说倒是没问题……」"
    voice "NSU08A_SU032"
    铃 "「你要是特别在意的话，可以用被子把外屋和里屋隔开」"
    "房间里有放着很大的餐桌的外屋，和放着小套桌的里屋。因为用纸拉门分隔开了，也确实没有什么难办的事。"
    志雄 "「啊，不，铃要有其它问题的话……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB01"),"True","img/SU_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU08A_SU033"
    铃 "「所以，我不要紧，如果志雄没有想那些奇怪的东西～」"
    志雄 "「啊，行了！别再没完没了捉弄我了……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB02"),"True","img/SU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU08A_SU034"
    铃 "「啊哈哈」"
    "被铃这么戏弄着，是在说我没有作为男人应有的意识么？"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB01"),"True","img/SU_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU08A_SU035"
    铃 "「嘛，如果真的那样，我会彻底把你放倒的，所以安心吧」"
    "这句话是让人相信好呢，还是不信好呢……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBA01"),"True","img/SU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU08A_SU036"
    铃 "「接下来，就这样待在这间房里也不行呢，稍微找找地方吃午饭吧！」"
    "脑中本来装了太多的事，不过听到这句话我便都搁置在一边了。"
    "到现在只吃了高速公路休息区内的饭团，是有点不够。"
    志雄 "「也是呢，吃些好吃的东西吧」"
    window hide
    play sound "SE00_47"
#FADE_OUT 1
    scene expression Solid("000") with dissolve
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#FADE_IN 0
    "我和铃一起离开了房间。"
    "即使如此……如果可以的话，我希望在旅行的过程中摆脱那种微妙的关系，而铃又是怎么想的呢？"
    "困难重重的前途是否能有希望……判断起来实在是很困难呢……"
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