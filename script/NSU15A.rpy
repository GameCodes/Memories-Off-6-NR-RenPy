label NSU15A:
    $currentlabel = "NSU15A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '30'
    $date = '0'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 6,CAL_0730
    show expression "img/NIMG15B-568h@2x.jpg" as cal zorder 5
    show expression "img/07_30_SUNDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG63MA1@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG63MA1@2x.jpg" as bg0 with dissolve
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
#SE_VOLC 1,128
    "第三天早上——吃过早饭后，我翻阅起放在屋内的观光介绍。"
    "因为还没决定今天做什么，自己想趁着铃洗澡的时间确认一下比较值得玩的地方。"
    志雄 "「湖已经去过了……」"
    "今天天气晴朗，其他地方的景色应该也会很好，还是去那些地方转转好了。"
    "头二天都玩的很尽兴。只是，还是那种和好朋友旅游的感觉。"
    "要说这种关系下再往前一步的话，很微妙地进展不下去。到明天为止旅行就要结束了，还是希望能改变一下两人之间的气氛。"
    "这样的话，那今天……"
    window hide
    hide bg1 with dissolve
#BG_SWPC 0
#BG_PRI 1
#BG_PRI 0
#BG_GET_NOC 1,F34
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,(640/2),(448/4+0),(640/2),(448/2)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MGB02"),"True","img/SU_MGB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#SE_VOLC 1,0
    play sound "SE00_47"
    play sound "SE03_90"
    hide bg1 with dissolve
    play music "BGM05"
    voice "NSU15A_SU000"
    铃 "「呼～，真是舒服啊」"
    "泡完了澡的铃，用毛巾擦拭着头发回到了房间。"
    "手上还拎着两瓶咖啡牛奶。"
    window hide
#BG_PRI 0
#BG_SET_BACK 
#BG_INIC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG63MA1@2x.jpg" as bg2 zorder 2 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_PRIC 1
#CHR_POSC 1,(320)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGB01"),"True","img/SU_LGB01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#BG_ALP_AUTOC 0,0,1,F24,96
#CHR_ALP_AUTOC 0,0,1,F24,96
#BG_ALP_SAVEC 0
#CHR_ALP_SAVEC 0
#CHR_SWPC 0
    hide lh1 with dissolve
#CHR_PRIC 0
#CHR_PRIC 1
#CHR_SORT 0
#CHR_ALPC 1,128
#BG_SWPC 0
    hide bg2 with dissolve
#BG_PRI 0
#BG_PRI 2
#BG_BLUR 0
#BG_ALPC 2,128
    play sound "SE03_33"
    voice "NSU15A_SU001"
    铃 "「志雄给你，昨天谢谢啦」"
    "铃将一瓶牛奶放在桌子上。"
    志雄 "「被你发现啦」"
    "想必这是昨晚为她买咖啡的谢礼吧。"
    "我拿起瓶子，铃已经小口小口把自己那瓶喝完了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGA01"),"True","img/SU_LGA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU002"
    铃 "「志雄不去洗澡吗？」"
    志雄 "「今天算了」"
    voice "NSU15A_SU003"
    铃 "「嗯～？为什么呢？」"
    "铃低头看起桌上的宣传册，水珠从头发上一滴一滴落下来。"
    "……这香味真不错啊。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGA03"),"True","img/SU_LGA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU004"
    铃 "「啊，不好意思。在看观光手册吗？」"
    志雄 "「嗯。在想今天该去哪好呢」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGB01"),"True","img/SU_LGB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU005"
    铃 "「唔～，今天不如就去Ｗｉｎｄｉｎｇ吧？」"
    志雄 "「Ｗｉｎｄｉｎｇ？」"
    "我歪着脑袋思考起这个陌生的单词。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGA01"),"True","img/SU_LGA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU006"
    铃 "「就是骑着摩托车，享受在蜿蜒曲折的道路上行驶的感觉」"
    "铃握住拳头，模仿着骑摩托的动作。"
    志雄 "「这样啊……这个有那么好玩吗？」"
    "倒也不是特别讨厌，只是这样的话似乎又被铃占了主动权，成了铃一个人的娱乐活动……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGA02"),"True","img/SU_LGA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU007"
    铃 "「怎么了？似乎不怎么感兴趣？」"
    志雄 "「倒也不是不行……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGA01"),"True","img/SU_LGA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU008"
    铃 "「那么，今天就自由活动吧？」"
    志雄 "「如此一来，不就又分开了吗？两个人好不容易出来一趟，这样有点……」"
    "若只是和普通朋友旅行的话，这样或许也没什么不可以……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGA02"),"True","img/SU_LGA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU009"
    铃 "「但是，勉强做没兴趣的事也没意思吧。或者，志雄知道其他好玩的地方？」"
    志雄 "「唔……」"
    "被问及值得玩的地方，一时也回答不上来，毕竟只是简单翻阅了一下而已。"
    voice "NSU15A_SU010"
    铃 "「没有吗？」"
    "似乎就是如此……"
    "我轻轻叹了口气，点点头。"
    志雄 "「那还是去Ｗｉｎｄｉｎｇ吧」"
#MUS_VOL 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGA05"),"True","img/SU_LGA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU011"
    铃 "「……真的不喜欢的话，还是算了吧」"
    志雄 "「诶？不不，没有不喜欢，没这回事」"
#MUS_VOL 128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGA01"),"True","img/SU_LGA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU012"
    铃 "「真的？」"
    "……好危险，用词得更谨慎点才行。"
    "明明想和铃一起营造美好的气氛，吵架的话就失去意义了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGB01"),"True","img/SU_LGB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU013"
    铃 "「放心吧，不会让你觉得无聊的」"
    志雄 "「还请你手下留情」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGB02"),"True","img/SU_LGB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU014"
    铃 "「呵呵，包在我身上」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG60AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG60AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#SE_VOLC 1,64
#FADE_IN 1
    voice "NSU15A_SU015"
    铃 "「嗯！说来今天的天气很好，是个游玩的好天气呢」"
    "铃把手搁在额头上遮住太阳，望着蔚蓝的天空，打心底一副开心的模样。"
    "看到铃这样，不禁觉得自己的选择果然是对的。"
    志雄 "「走哪条线路呢，决定了吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA01"),"True","img/SU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU016"
    铃 "「基本上还是第一天走的那条路。不过，从地图上看的话，除此之外也有其他有趣的路线呢，每一条都想去试试呢」"
    志雄 "「那样不会迷路吗？」"
    voice "NSU15A_SU017"
    铃 "「不要紧吧，大概」"
    志雄 "「唔……有点不安呢……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA02"),"True","img/SU_LCA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU018"
    铃 "「说什么呢？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU019"
    铃 "「迷路不也是一种快乐吗」"
    志雄 "「咦？还有这种说法吗？」"
    voice "NSU15A_SU020"
    铃 "「只要好好带着地图和手机，就算迷路也不怕了」"
    志雄 "「不过山上没有信号吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU021"
    铃 "「呵呵呵呵！志雄还真是爱操心啊」"
    voice "NSU15A_SU022"
    铃 "「这一带不是深山老林，不管发生什么，只要沿着道路走下去，就能到达有人的地方」"
    志雄 "「话是这样说没错……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU023"
    铃 "「喂喂，出发之前尽说些令人不安的话，越说越应验该怎么办啊？」"
    志雄 "「对、对不起」"
    "不过确实呢，一开始就消极起来的话可不行。"
    "难得的机会，要尽情享受才是。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU024"
    铃 "「那我们出发吧！」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    stop sound fadeout 1
    play sound "SE06_47L"
#FADE_OUT 1
#BG_SET_BACK 
#BG_INIC 3
#ROUTINE_STA
#BG_POSC 3,30,-60,749,450
    scene expression "img/EVC_SU02A2@2x.png" as bg3 with dissolve:
        block:
            align (.5,.5)
            parallel:
                linear 0.03 xalign 0.53
            parallel:
                linear 0.03 yalign 0.53
            repeat
    show expression im.Scale("img/Motor_EF_Wood1@2x.png",1136,263) as motor_eff_up zorder -6 at motor_eff_movein:
        yalign 1.0
    show expression im.Scale("img/Motor_EF_Wood1@2x.png",1136,263) as motor_eff_up2 zorder -6 at motor_eff_moveout:
        yalign 1.0
    show expression "img/Motor_AB_Trees@2x.png" at motor_eff_moveout as motor_eff_down zorder -5:
        yalign 1.0
    show expression "img/Motor_AB_Trees@2x.png" at motor_eff_movein as motor_eff_down2 zorder -5:
        yalign 1.0
    with dissolve
#EFF_PRI 0
#EFF_STAC 0,MOTOR_RIDE_AB,EFF_NOSKIP
#ROUTINE_STP
    pause (256/32.0)
#FADE_IN 1
    voice "NSU15A_SU025"
    铃 "「你看！非常舒服吧！」"
    志雄 "「是啊！」"
    "在铃欢欣雀跃的喧哗下，我的心情也变得兴奋起来。"
    "摩托在蜿蜒曲折的道路上飞驰，两旁的景色不断被甩下，这种轨道飞车般的感觉确实相当的开心。"
    show expression "img/EVC_SU02A1@2x.png" as bg3 with dissolve
    voice "NSU15A_SU026"
    铃 "「唔～那个！」"
    window hide
#FADE_OUT 1
    hide bg3 with dissolve
    scene expression "img/motor_day@2x.png" as motor_light_n_eff:
    show expression "img/NIMG12A@2x.jpg" as motor_light_n_eff_road zorder -1:
        block:
            yanchor 1.0
            ypos 0.0
            linear 0.3 ypos 1.0
            repeat
    show expression "img/NIMG12A@2x.jpg" as motor_light_n_eff_road2 zorder -1:
        block:
            yanchor 0.0
            ypos 0.0
            linear 0.3 ypos 1.0
            repeat
    with dissolve
#EFF_STPC 0,EFF_NOSKIP
#EFF_STAC 0,MOTOR_LIGHT_D,EFF_NOSKIP
#FADE_IN 1
    "在一个有些坡度的拐弯处，车子变得有些倾斜。"
    "后座的我为了不失去平衡，只有紧紧地抱住铃。"
    志雄 "「啊！？」"
    "开心当然是毫无疑问的，但不如铃那么兴奋也是事实……"
    "果然，是因为不是自己在驾驶吧？"
    window hide
    stop se fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG106AA@2x.jpg" as bg0 zorder 0 with dissolve
    #scene expression "img/BG66AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MBB01"),"True","img/SU_MBB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
##EFF_STAC 0,SUNLIGHT_BG66_FRONT,EFF_SKIP
##EFF_STAC 1,SUNLIGHT_BG66_BACK,EFF_SKIP
    play sound "SE05_15L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,64
    play music "BGM12"
    voice "NSU15A_SU027"
    铃 "「休息休息～」"
    "上山才到一半，铃突然停下了摩托车。"
    "与一般的驾驶相比，果然比较辛苦吧。"
    志雄 "「已经到了很高的地方呢」"
    "注意到这点的时候，映入眼帘的景色已变得截然不同。"
    "那些树木和植物，和在山下所看到的感觉上很是不一样。"
    voice "NSU15A_SU028"
    铃 "「往下看的话可真是一幅不错的景象呢啊」"
    "我眯着眼睛，可以看到下龙境车站前的街道。"
    "我们住宿的旅馆在哪里呢……？"
    志雄 "「要是带个数码相机来就好了。这么说来，铃不拍几张照吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MBC04"),"True","img/SU_MBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU029"
    铃 "「取材的时候偶尔也会照相，但以我的水平，即使用很好的相机，也无法将那一刻的感动和心情记录下来吧」"
    "铃也有着相同的感觉啊。虽然只是小事，不过还是很值得高兴。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MBB01"),"True","img/SU_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU030"
    铃 "「因此拍摄的时候」"
    "铃这时已把手机取了出来，把自己的摩托车当成背景拍进去。"
    window hide
    play sound "SE02_17"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MBA01"),"True","img/SU_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU031"
    铃 "「要把人和摩托车一起拍进去」"
    志雄 "「原来如此。那我也为铃拍几张吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MBB03"),"True","img/SU_MBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NSU15A_SU032"
    铃 "「诶？我就不用了吧」"
#REMOVE_REEK_CHR 0
    志雄 "「别这样，和摩托车一起照一张吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MBA03"),"True","img/SU_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU033"
    铃 "「喂，等等」"
    window hide
    play sound "SE02_17"
    "我在铃还未准备好之前就按下了快门。"
    "……啊，眼睛闭上了！"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MBA02"),"True","img/SU_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU034"
    铃 "「真是的，不要拍些奇怪的地方啊」"
    志雄 "「这是因为铃在乱动吧」"
    voice "NSU15A_SU035"
    铃 "「把这张删掉啦」"
    志雄 "「知道了。不过，再照一张吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MBB01"),"True","img/SU_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU036"
    铃 "「机会难得，干脆一起照一张吧。只有自己一个人的话，有点不舒服」"
    "说着，铃故意鼓起了脸颊。"
    "能和铃一起拍照，没有什么能比这更让人高兴了……"
    志雄 "「好吧。那两个人并排……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB01"),"True","img/SU_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "我和铃背靠着摩托车站在一起。"
    "尽可能地把拿着手机的手伸远，试着照了一张。"
    window hide
    play sound "SE02_17"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBC05"),"True","img/SU_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU037"
    铃 "「要拍了哦」"
    "确认之后，取景窗上清楚地映出了铃的脸。"
    志雄 "「嗯，果然很难啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBC01"),"True","img/SU_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU038"
    铃 "「还是再稍微靠近一点比较好吧」"
    window hide
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBC01"),"True","img/SU_XBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_BLUR 0
    "说着，铃用手搭住我的肩，紧紧地贴在我身上。"
    "哇，好近！"
    "铃的脸颊碰到我的脸颊了！"
    voice "NSU15A_SU039"
    铃 "「看，这样如何？」"
    志雄 "「嗯、嗯……ＯＫ，茄子」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU12A")]=True
#BG_SET_BACK 
#FADE_OUT 1
    play sound "SE02_17"
#SE_WATC 0
    pause (16/32.0)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBA02"),"True","img/SU_XBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#FADE_IN 1
    voice "NSU15A_SU040"
    铃 "「果然手机只有这种程度啊」"
    "看着手机的屏幕，铃歪着头似乎有点失望。"
    "屏幕上，稍稍有些僵硬的我和微笑着的铃亲密地并肩站着。"
    "几乎看不到背景，摩托车只在画面的一端占据一丝镜头。"
    "我和铃几乎把屏幕占满了。"
    "不过，感觉很开心……绝无仅有的只属于两人的照片。"
    "光是这样，我就非常满足了。"
    志雄 "「我觉得还不错……嗯，给铃发过去吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XBA01"),"True","img/SU_XBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU041"
    铃 "「嗯，麻烦你啦」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBA01"),"True","img/SU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU042"
    铃 "「那么，现在往下开去湖那边吧？」"
    "铃跨上摩托车，手里还拿着手套。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE06_40L"
    志雄 "「啊，稍等」"
    "我慌忙坐到铃的身后，于是摩托车以高昂的气势再度出发了。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
    play sound "SE06_14L"
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#EFF_STPC 1,EFF_SKIP
#SE_VOLC 0,0
    stop sound
    stop music fadeout 1
#BG_INIC 3
#ROUTINE_STA
#BG_POSC 3,30,-60,749,450
    scene expression "img/EVC_SU02A1@2x.png" as bg3 with dissolve:
        block:
            align (.5,.5)
            parallel:
                linear 0.03 xalign 0.53
            parallel:
                linear 0.03 yalign 0.53
            repeat
    show expression im.Scale("img/Motor_EF_Wood1@2x.png",1136,263) as motor_eff_up zorder -6 at motor_eff_movein:
        yalign 1.0
    show expression im.Scale("img/Motor_EF_Wood1@2x.png",1136,263) as motor_eff_up2 zorder -6 at motor_eff_moveout:
        yalign 1.0
    show expression "img/Motor_AB_Trees@2x.png" at motor_eff_moveout as motor_eff_down zorder -5:
        yalign 1.0
    show expression "img/Motor_AB_Trees@2x.png" at motor_eff_movein as motor_eff_down2 zorder -5:
        yalign 1.0
    with dissolve
#EFF_PRI 0
#EFF_STAC 0,MOTOR_RIDE_AB,EFF_NOSKIP
#ROUTINE_STP
    pause (64/32.0)
#SE_VOLC 0,255
#FADE_IN 1
    voice "NSU15A_SU043"
    铃 "「现在是下坡路，稍微加速试试哟！」"
    志雄 "「诶？现在吗？」"
    window hide
    stop se fadeout 1
    play sound "SE06_15L"
    play music "OBGM13"
    志雄 "「哇，要掉下去了！要滑倒了！」"
    voice "NSU15A_SU044"
    铃 "「好好抓紧了啊～！」"
    "摩托车以爆发性的加速度向拐角处冲去，发出一阵好強烈的引擎制动声。"
    window hide
    play sound "SE06_31"
#MB_BRK 3,5,10
#EFF_STAC 0,MOTOR_RIDE_AB,EFF_NOSKIP
    "与此同时，就在我感觉到摩托车似乎要倒下去的一瞬间，铃再次转动加速器，摩托车一下子冲过了拐角。"
    voice "NSU15A_SU045"
    铃 "「哇，感觉好棒！」"
    志雄 "「啊啊啊啊啊！」"
    "恐惧感还没消退，铃又向另一个拐角冲去。"
    志雄 "「喂，铃，稍微减下速吧！」"
    window hide
    show expression "img/EVC_SU02A2@2x.png" as bg3 with dissolve
    voice "NSU15A_SU046"
    铃 "「什么！？要加强引擎制动是吧！」"
    "不、不是这个！"
    "身体激烈地左右摇晃，目之所及之处，道路和悬崖都渐渐变得天旋地转。"
    "这速度几乎是人无法呼喊，只能拼命抓紧了铃。"
    window hide
    show expression "img/EVC_SU02A1@2x.png" as bg3 with dissolve
    voice "NSU15A_SU047"
    铃 "「啊～接下来是发卡弯！」"
    志雄 "「饶、饶了我吧……」"
    window hide
    play sound "SE04_33"
#MB_BRK 3,10,30
#EFF_STAC 0,MOTOR_RIDE_AB,EFF_NOSKIP
    voice "NSU15A_SU048"
    铃 "「呀～！」"
    "刚才是什么声音！"
    "就在耳边传来刺耳噪音的那一瞬间，感觉到摩托车的平衡有些奇怪。"
    voice "NSU15A_SU049"
    铃 "「喝！」"
    "但是，多亏了铃的精湛技术，摩托车在加速后很快便回复了原来的平衡。"
    "哇，刚才的生死时速是真的吗！？"
    voice "NSU15A_SU050"
    铃 "「好好！玩的真痛快！」"
    "与我的惊恐相反，充满自信的铃似乎更加激动了。"
    志雄 "「饶、饶了我吧～！」"
    "我诚恳的祈求落空了，摩托车把我的哀叫甩在一旁，继续疾驰着……"
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
    show expression "img/BG70AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG70AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_20L"
    pause (32/32.0)
    play sound "SE05_12"
#EFF_STAC 0,WATERTWINKLE,EFF_SKIP
#FADE_IN 1
#SE_VOLC 0,64
    志雄 "「呼呼呼……」"
    "在湖边下了车的我，大口大口吸着气。"
    "要夭寿了啦……"
    window hide
    stop se fadeout 1
#SE_VOLC 1,128
#EFF_STPC 0,EFF_SKIP
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    play music "OBGM14"
    voice "NSU15A_SU051"
    铃 "「哈哈，真开心呐！在这一带骑车真是太棒了！」"
    志雄 "「等等，铃！不管怎么说刚才那样也太危险了！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA01"),"True","img/SU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU052"
    铃 "「不要紧啦。虽然看起来很危险，只要掌握好安全底线就行了。速度也不是那么快呢」"
    志雄 "「已经够快了！用这种速度骑摩托车，如果跌倒了肯定会受伤的啊！」"
    voice "NSU15A_SU053"
    铃 "「话是没错。所以才需要有所控制地驾驶嘛」"
    志雄 "「但刚才也实在太危险了吧！」"
    "就在刚才，跟地面打滑的那一瞬间，真的是很吓人。"
    "虽然对于骑惯了摩托车的铃来说或许是很寻常……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA04"),"True","img/SU_LCA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU054"
    铃 "「那种程度并不危险啦，再说刚才不也没倒嘛」"
    志雄 "「这仅仅只是结果论吧？」"
    "铃的脑子真是需要治一治了。"
    "并不是故意对她的兴趣吹毛求疵，但危险毕竟是危险。"
    "这是骑车的本人所不清楚的，只有旁观者才会感觉到的心情。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA05"),"True","img/SU_LCA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU055"
    铃 "「我并没有用多危险的骑法拉。而且，这个去驾校也会学到的哦？」"
    "铃一副不服气的样子。"
    "不过我也不能退缩。"
    "必须再一次告诫铃要小心谨慎才行。"
    "如果铃有个万一的话，那我……"
    志雄 "「并不只是那样，摩托车毕竟是很危险的交通工具，还是应该更加注意啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC01"),"True","img/SU_LCC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU056"
    铃 "「所以说我很注意了啊」"
    志雄 "「可我只看见你在刻意做危险的行为啊」"
    voice "NSU15A_SU057"
    铃 "「所以说，我真的没有在做危险的行为。总是说骑摩托车的危险性，那不是根本就不用骑了么」"
    志雄 "「没错。正因为有危险性，所以还是不要再骑比较好」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC03"),"True","img/SU_LCC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU058"
    铃 "「骑不骑摩托车是我自己的事，轮不到志雄来插嘴」"
    志雄 "「什……」"
    voice "NSU15A_SU059"
    铃 "「骑摩托车是我自己的决定，花了钱去学习驾驶方法……我已经承担了自己该尽的责任，还不想被只是学生的志雄来说教」"
    志雄 "「跟那没关系吧。我不是也坐在后面吗？我还没对铃说些什么吧？不是仅仅听铃在一直说个不停吗？」"
    "我被铃口中的『学生的』的字眼激怒了。"
    "果然对铃来说，我只是个小鬼吧？"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC05"),"True","img/SU_LCC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU060"
    铃 "「那就别只是感情论，而请好好地反驳我。对于摩托车的事情志雄明明不是很了解……希望你能好歹能说出些有说服力和分量的话来」"
    志雄 "「明明和我的命也息息相关，难道我说的话就没有听的价值吗！？」"
    "对于铃来说，我的存在价值也只有这种程度吗……？"
    志雄 "「随随便便就做危险的事，铃虽然有这个权利，但这样不是太任性了吗。就凭这一点难道没有说服力吗」"
    voice "NSU15A_SU061"
    铃 "「……」"
    志雄 "「我不是铃的玩具，也不是铃的包袱」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC02"),"True","img/SU_LCC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU062"
    铃 "「……让志雄坐在后面看来是我的错」"
    志雄 "「诶？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC03"),"True","img/SU_LCC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU15A_SU063"
    铃 "「是我不好。这一切都是我太任性了」"
    志雄 "「等等！？」"
    "我真正想说的，其实不是这个……！"
    window hide
    stop music fadeout 1
#SE_VOLC 1,255
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE06_12"
    play sound "SE06_14L"
    pause (8/32.0)
    stop se fadeout 1
#EFF_STAC 0,WATERTWINKLE,EFF_SKIP
    "还没来得及想是不是自己说得太过份了，铃已经骑着摩托车离开了。"
    志雄 "「……我这是，在做什么呢」"
    "好不容易头脑清醒了，后悔的心情一下涌了上来。"
    "明明只是是想让她再多注意点的啊……"
    "好担心铃……"
    "为什么，就是不能把自己的真实心情传递过去呢……"
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