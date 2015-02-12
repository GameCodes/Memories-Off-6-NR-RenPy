label NCH06A2:
    $currentlabel = "NCH06A2"
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
    show expression "img/BG68AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG68AA@2x.jpg" as bg0 with dissolve
    play sound "SE08_17L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1
    play music "BGM12"
#RSET F122
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "然后，我们来到了车站附近的商店街。"
    window hide
#SE_VOLC 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBA01"),"not F103==0","img/CH_MLA01A@2x.png","True","img/CH_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
    志雄 "「总是觉得有点不可思议呢，为什么土特产店总是有卖木刀的呢？」"
    "那种作为时代剧舞台的景点暂且不论，就算不是那种地方，也是到处都在卖。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLB06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBB06"),"not F103==0","img/CH_MLB06A@2x.png","True","img/CH_MBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH129"
    智纱 "「确实呢，不管去哪都是土特产的固定项目呢」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBB01"),"not F103==0","img/CH_MLB01A@2x.png","True","img/CH_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH130"
    智纱 "「比如说可以给走累了的旅行者当手杖用啊，听说过去的乱斗中这个也是固定有的」"
    window hide
#SE_VOLC 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_GET_NOC 0,F24
#BG_SET_BACK 
#BG_INIC 1
#BG_UVC 1,(360),(116),(263),(196)
#BG_SWPC 0
    hide bg1 with dissolve
#BG_PRI 0
#BG_PRI 1
#BG_UVC 1,0,0,640,448
    "是这样啊，我一边点着头，一边用手拿起了木刀。嗯～……。"
    志雄 "「如果把这把木刀，当土特产送给莉莉丝的话……」"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG24AA@2x.jpg" as bg2 zorder 8
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SBD06"),"True","img/RI_SBD06A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#SE_VOLC 1,0
#MUS_VOL 0
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 0
#BG_ALPC 2
#BG_BLUR 2
#CHR_ALPC 0
#CHR_ALPC 1
    hide bg1 with dissolve
    play sound "SE04_13"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD06"),"True","img/RI_MBD06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    play sound "SE04_13"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD06"),"True","img/RI_LBD06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH06A_RI000_K"
    莉莉丝 "「呵呵呵，志雄～，佐贺君～，用这把木刀～」"
#CHECK_NOWSKIP L_SKIP_00
#RSET F121
#THREAD_STA 1,THREAD_QUA_WIN_L=
#MESA A_CH_TO+A_CH_SI,NCH06A_TO000_K,"【亨・志雄】「啊啊啊啊啊！」"=
#THREAD_WAT 1
#WIN_POS 0,0=
#RSET F121
#MESX "%K%P"
    亨 "「啊啊啊啊啊！」"
    window hide
#BG_INIC 1
#BG_PRI 1
    scene expression "img/BG68AA@2x.jpg" as bg0
    hide bg2
#BG_UVC 2,0,0,640,448
    hide lh1
    with dissolve
#BG_ALPC 0
#CHR_ALPC 0
#SE_VOLC 1
#MUS_VOL 128
    hide bg1 with dissolve
    "不不，肯定不会变成那样的吧……大概。"
    "脊背有点发凉。我用一种对待危险物的心情，把那把木刀放回了原处。"
    window hide
#SE_VOLC 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC05"),"not F103==0","img/CH_LLC05A@2x.png","True","img/CH_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .35
    with dissolve
    "偶然地往旁边一瞥，智纱正盯着店门口挂着的钥匙链。"
    "智纱盯着的是……狗的钥匙链。"
    voice "NCH06A_CH131"
    智纱 "「……」"
    志雄 "「想要吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC01"),"not F103==0","img/CH_LLC01A@2x.png","True","img/CH_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH132"
    智纱 "「嗯。就是在想，要买哪个呢」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_POSC 1,140,-50,640,448
    play sound "SE03_03"
    show expression "img/NIMG16D@2x.png" as bg1 zorder 20 with dissolve
    "智纱就像在品评一样，一个一个地把弄着那三个小狗的钥匙链。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA05"),"not F103==0","img/CH_LLA05A@2x.png","True","img/CH_LBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH133"
    智纱 "「要买哪个才好呢……呜呜」"
    "智纱以一种我至今没有见过的可怕表情，挑选着钥匙链。说是在挑选要买的东西，不如说是在死盯着宿敌一样。"
    voice "NCH06A_CH134"
    智纱 "「呜～……」"
    window hide
    hide bg1 with dissolve
#BG_POSC 1,0,0,640,448
    志雄 "「既然这么难以决定，那就３个都买了吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC02"),"not F103==0","img/CH_LLC02A@2x.png","True","img/CH_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH135"
    智纱 "「嗯～，话虽如此，没有那么多钱啊……」"
    window hide
#BG_INIC 1
#BG_POSC 1,140,-50,640,448
    play sound "SE03_03"
    show expression "img/NIMG16A@2x.png" as bg1 zorder 20 with dissolve
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA01"),"not F103==0","img/CH_LLA01A@2x.png","True","img/CH_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH136"
    智纱 "「嗯，就决定是这个了！」"
    "考虑了相当长时间之后，智纱选择了３个中的一个。"
    window hide
    hide bg1 with dissolve
#BG_POSC 1,0,0,640,448
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB01"),"not F103==0","img/CH_LLB01A@2x.png","True","img/CH_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH137"
    智纱 "「那，我去买了」"
    window hide
    play sound "SE01_04L"
#CHR_DIAPPEAR 0,0,0,10
    pause (32/32.0)
#SE_VOLC 0,0
    "……。"
    window hide
#SE_VOLC 0,255
    pause (32/32.0)
#CHR_ALPC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC04"),"not F103==0","img/CH_LLC04A@2x.png","True","img/CH_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 64
#MOV_CHR0 128,(320-96)
#MOV_CHR_GO 1
    stop se
    志雄 "「哎？　怎么了？」"
    "本来应该是去了收银台方向的智纱，又回来了。"
    voice "NCH06A_CH138"
    智纱 "「果然，再，再去买一个」"
    "智纱再次面向小狗的钥匙链。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA05"),"not F103==0","img/CH_LLA05A@2x.png","True","img/CH_LBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH139"
    智纱 "「那个……」"
    voice "NCH06A_CH140"
    智纱 "「应·该·买·哪·个·才·好·呢……」"
    "犹豫过后，结果好像还是让上天代替自己决定了。"
    window hide
#BG_INIC 1
#BG_POSC 1,140,-50,640,448
    play sound "SE03_03"
    show expression "img/NIMG16B@2x.png" zorder 50 as bg1 with dissolve
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB02"),"not F103==0","img/CH_LLB02A@2x.png","True","img/CH_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH141"
    智纱 "「嗯。这个」"
    window hide
    hide bg1 with dissolve
#BG_POSC 1,0,0,640,448
    "用一只手取下钥匙链，再一次向收银台的方向走去。"
    window hide
    play sound "SE01_04L"
#CHR_DIAPPEAR 0,0,0,10
    pause (32/32.0)
#SE_VOLC 0,0
    "……。"
    window hide
#SE_VOLC 0,255
    pause (32/32.0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC04"),"not F103==0","img/CH_LLC04A@2x.png","True","img/CH_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .35
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR0 128,(320-96)
#MOV_CHR_GO 1
    stop se
    voice "NCH06A_CH142"
    智纱 "「……」"
    志雄 "「果然，还是决定３个都买了吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC06"),"not F103==0","img/CH_LLC06A@2x.png","True","img/CH_LBC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH143"
    智纱 "「不，没关系的，就这两个！」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB03"),"not F103==0","img/CH_LLB03A@2x.png","True","img/CH_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE01_03L"
#MOV_CHR_INIT 32
#MOV_CHR0 0
#MOV_CHR_GO 0
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_ALPC 0
    pause (32/32.0)
    stop se fadeout 1
    "……。"
    "看着智纱挑剩下的最后一个钥匙链。"
    志雄 "「是那么值得犹豫的事情吗？」"
    "还是有点不太明白……。"
    window hide
#FADE_OUT 1
#BG_UVC 0,0,512,640,448
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB01"),"not F103==0","img/CH_LLB01A@2x.png","True","img/CH_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter.65
    with dissolve
    pause (32/32.0)
#FADE_IN 1
    志雄 "「智纱的土特产打算怎么办？　回去的那天再买？」"
    "食品之类的土特产不能放太久，要买的话也许还是旅行的最后一天再买比较好。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB06"),"not F103==0","img/CH_LLB06A@2x.png","True","img/CH_LBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH144"
    智纱 "「说的也是呢，怎么办好呢……？　送给结乃什么样的土特产她会高兴呢？」"
    志雄 "「然后还有，智纱你父母的份呢」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB04"),"not F103==0","img/CH_LLB04A@2x.png","True","img/CH_LBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH145A"
    智纱 "「哎……{w=3}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB03"),"not F103==0","img/CH_LLB03A@2x.png","True","img/CH_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH145B"
    extend "啊，是啊」"
    志雄 "「『是啊』，你是忘了吗，智纱？」"
    "我是因为老爸和香里阿姨也一起来了所以不用买了，智纱不给父母买土特产可不行。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB01"),"not F103==0","img/CH_LLB01A@2x.png","True","img/CH_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH146"
    智纱 "「啊，啊哈哈……」"
    "忘记了吗……。真新奇啊，这种不注意的失误。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB04"),"not F103==0","img/CH_LLB04A@2x.png","True","img/CH_LBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH147"
    智纱 "「是，是呢。嗯嗯，爸爸和妈妈的份也必须准备好呢。一会儿去买吧」"
    志雄 "「……？　为什么那么慌张呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA03"),"not F103==0","img/CH_LLA03A@2x.png","True","img/CH_LBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCH06A_CH148"
    智纱 "「没，我没有在慌张啊？」"
#REMOVE_REEK_CHR 0
    "……是吗？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB06"),"not F103==0","img/CH_LLB06A@2x.png","True","img/CH_LBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH149"
    智纱 "「啊，志雄君，那个！」"
    "智纱指着那一排土特产店的一角。"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "有个写着『甜食处　花咲』的招牌。看起来是咖啡厅。"
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB01"),"not F103==0","img/CH_LLB01A@2x.png","True","img/CH_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCH06A_CH150"
    智纱 "「阳光太强烈了，我觉得还是稍稍休息一下比较好……」"
    "嗯～，总觉得，她是在想蒙混过去。"
    "但是，阳光确实很强烈，天气也很热，在咖啡厅休息下也许会比较好。"
    志雄 "「嗯，那我们走吧」"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,(640/2),(448/8),(640/2),(448/2)
    show expression "img/EXBG06A@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/EXBG06A@2x.jpg" as bg0 with dissolve
    play sound "SE07_22L"
    pause (32/32.0)
    play sound "SE00_38"
#FADE_IN 1
    pause (16/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_SLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_SBB02"),"not F103==0","img/CH_SLB02A@2x.png","True","img/CH_SBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH151"
    智纱 "「哇，好凉快～」"
    "店内的冷气很足，和外面相比完全是另一个世界。身上的汗水也一下子消失得无影无踪。"
    "内装修是日式的，有木纹的桌子和榻榻米的座席。因为平常没进过这样的咖啡厅，所以感到很新鲜。"
    voice "NCH06A_XK000"
    店員Ｄ "「请走这边走」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "在店员的带路下，我俩走到一个双人桌前坐下。"

#BG_OVER_MGNC EXBG06A,0,CH_ZLB02,CH_ZBB02
    scene expression "img/EXBG06A@2x.jpg" as bg0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB02"),"not F103==0","img/CH_ZLB02A@2x.png","True","img/CH_ZBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    
    voice "NCH06A_CH152"
    智纱 "「要什么好呢……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB06"),"not F103==0","img/CH_ZLB06A@2x.png","True","img/CH_ZBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH153A"
    智纱 "「嗯～，冰激凌也挺好……{w=3}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB05"),"not F103==0","img/CH_ZLB05A@2x.png","True","img/CH_ZBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH153B"
    extend "不对不对，还是点抹茶帕菲吧……」"
    "智纱对着菜单做了个鬼脸。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB06"),"not F103==0","img/CH_ZLB06A@2x.png","True","img/CH_ZBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH154"
    智纱 "「冰激凌就算不在这里也吃的到……可是，从价格和卡路里数考虑到话帕菲又很危险……」"
    "要选哪一个呢，心中好像起了很大的纠葛。"
    志雄 "「我就先来杯冰咖啡吧」"
    志雄 "「在意卡路里数，莫非是在减肥中吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB04"),"not F103==0","img/CH_ZLB04A@2x.png","True","img/CH_ZBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH155A"
    智纱 "「哎？　{w=3}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBA03"),"not F103==0","img/CH_ZLA03A@2x.png","True","img/CH_ZBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH155B"
    extend "没、没有，不是那回事的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBC02"),"not F103==0","img/CH_ZLC02A@2x.png","True","img/CH_ZBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH156"
    智纱 "「发胖了的话，穿起……」"
    "穿起？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBC05"),"not F103==0","img/CH_ZLC05A@2x.png","True","img/CH_ZBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH157"
    智纱 "「啊」"
    "这是，智纱的视线忽然停在菜单的一点上了。"
    "智纱皱起了眉头，凝视着那一点。"
    志雄 "「怎么了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLA05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBA05"),"not F103==0","img/CH_ZLA05A@2x.png","True","img/CH_ZBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH158"
    智纱 "「志雄君……」"
    voice "NCH06A_CH159"
    智纱 "「点这个，可以吗……？」"
    志雄 "「我看看，是什么？」"
    "看着智纱指着的菜单。"
    "那里有一张照片，照片上是一大杯果汁，上面插着两根吸管。照片的上面写着『推荐给情侣！』。"
    志雄 "「这个……」"
    "对日式咖啡厅里有这个有点意外，难道你想要这个吗，智纱！？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLC06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBC06"),"not F103==0","img/CH_ZLC06A@2x.png","True","img/CH_ZBC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH160"
    智纱 "「啊、不、不不！　不喜欢就算了，不喜欢的话！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBC05"),"not F103==0","img/CH_ZLC05A@2x.png","True","img/CH_ZBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE03_44"
    "好像是看出了我脸上显出的，犹豫的神情，智纱慌张地打开了菜单的其它页。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB03"),"not F103==0","img/CH_ZLB03A@2x.png","True","img/CH_ZBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH161"
    智纱 "「唉，点什么好呢～？」"
    "刚才说过的话不算，智纱敷衍着，又开始在菜单上找其他的东西了。"
    志雄 "「……」"
    "确实，挑战那个菜单真的很不好意思……虽说有些不好意思，如果是智纱想要点的话……！"
    志雄 "「好啊。就点刚才那个果汁吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBC04"),"not F103==0","img/CH_ZLC04A@2x.png","True","img/CH_ZBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH162"
    智纱 "「啊，怎么，可是……」"
    志雄 "「没事没事，我也正好想喝点果汁」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBC02"),"not F103==0","img/CH_ZLC02A@2x.png","True","img/CH_ZBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH163"
    智纱 "「可是，刚才，你点的是冰咖啡」"
    志雄 "「那是错觉、错觉」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "用手拦住了还在客气的智纱，对路过的服务生打了个招呼。"
    志雄 "「就这样，服务生，点单！」"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB03"),"not F103==0","img/CH_ZLB03A@2x.png","True","img/CH_ZBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    pause (32/32.0)
#SE_VOLC 1
#FADE_IN 1
    voice "NCH06A_CH164"
    智纱 "「啊哈哈……」"
    志雄 "「哈哈……」"
    "我和智纱呆板地笑了笑。"
    "点了面向情侣的果汁，和智纱一起喝……果然还是很不好意思。"
    "不过，智纱看上去虽然有些害羞，但还是很高兴。所以说，我觉得这样做还是很好的。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    志雄 "「嗯？」"
    "智纱不好意思地移开了视线，看到了桌旁墙壁上贴着的海报。"
    if not persistent.dictlist[51] and persistent.show_dict:
        $persistent.dictlist[51]=True
        show screen dict_pop(i=51)
    
    志雄 "「泉龙神社夏日祭典？」"
    if not persistent.dictlist[55] and persistent.show_dict:
        $persistent.dictlist[55]=True
        show screen dict_pop(i=55)
#IF F105!0, GOTO L_NCH06A_BRA01_A
    jump L_NCH06A_BRA01_B
label L_NCH06A_BRA01_A:
    "这么说来，在来商店街的路上的那间神社，好像也在为搭帐篷做着什么准备。"
    "所谓泉龙神社，也许指的就是那个神社。神社境内在做祭典的准备吧。"
    jump L_NCH06A_BRA01_X
label L_NCH06A_BRA01_B:
    "这么说来，从旅馆来商店街的路上有神社的台阶。要说泉龙神社就是那里吧。"
    jump L_NCH06A_BRA01_X
label L_NCH06A_BRA01_X:
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBA01"),"not F103==0","img/CH_ZLA01A@2x.png","True","img/CH_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH165"
    智纱 "「啊，有祭典啊」"
    "智纱也盯着那个海报。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB06"),"not F103==0","img/CH_ZLB06A@2x.png","True","img/CH_ZBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH166A"
    智纱 "「旅行目的地的祭典吗……{w=3}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB05"),"not F103==0","img/CH_ZLB05A@2x.png","True","img/CH_ZBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH166B"
    extend "好期待……」"
    志雄 "「去看看吗？」"
    "举办日好像是后天，星期日。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBA04"),"not F103==0","img/CH_ZLA04A@2x.png","True","img/CH_ZBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH167"
    智纱 "「可以吗？」"
    志雄 "「当然了。好不容易的祭典，我也想和智纱一起去」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB02"),"not F103==0","img/CH_ZLB02A@2x.png","True","img/CH_ZBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH168"
    智纱 "「嗯！　那，我们一起去吧」"
    voice "NCH06A_CH169"
    智纱 "「祭典啊……好期待啊」"
    "智纱好像是在想着后天的事情，看起来非常高兴。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "看看那张海报，上面也有夜空中焰火闪耀的照片。好像也要放焰火的样子。"
    "嗯，我也很期待呢。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG68EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG68EA@2x.jpg" as bg0 with dissolve
    play sound "SE08_17L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1
    "我们走出了咖啡厅，天色已经开始有些变红了。"
    志雄 "「差不多是该回去了吧」"
    window hide
    play sound "SE02_11L"
    pause (16/32.0)
#SE_VOLC 1
#CHR_INIC 0
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA03"),"not F103==0","img/CH_LLA03A@2x.png","True","img/CH_LBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
#REEK_CHR 0
    voice "NCH06A_CH170"
    智纱 "「啊，手机」"
#REMOVE_REEK_CHR 0
    "智纱从口袋里取出了手机。"
    window hide
    play sound "SE02_10"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB01"),"not F103==0","img/CH_LLB01A@2x.png","True","img/CH_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH171"
    智纱 "「喂喂」"
    stop music fadeout 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB04"),"not F103==0","img/CH_LLB04A@2x.png","True","img/CH_LBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH172"
    智纱 "「哎，妈，妈妈？」"
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
#CHR_POSC 0,(320+250)
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_SLC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_SBC02"),"not F103==0","img/CH_SLC02A@2x.png","True","img/CH_SBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter 570/640.0
    with dissolve
    "智纱把手机放在耳边，和我稍稍保持了距离。"
    voice "NCH06A_CH173"
    智纱 "「……真是的，没事的啊，不用您那么操心的…………嗯……嗯」"
    "是怎么了？　怎么不时地还往这边看呢……。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_SLC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_SBC05"),"not F103==0","img/CH_SLC05A@2x.png","True","img/CH_SBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH174"
    智纱 "「……在莉莉丝的家里啊……以前也在那里住过几次的……嗯……那，我挂了啊」"
    window hide
    play sound "SE02_10"
    play music "OBGM14"
    "莉莉丝的家？　住过几次？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_SLB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_SBB03"),"not F103==0","img/CH_SLB03A@2x.png","True","img/CH_SBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "智纱把手机从耳边拿开，收回了口袋里。"
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
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB03"),"not F103==0","img/CH_LLB03A@2x.png","True","img/CH_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
    志雄 "「家里人打来的？」"
    voice "NCH06A_CH175"
    智纱 "「嗯、嗯。打电话来问我有没有添麻烦」"
    志雄 "「一定是在担心智纱啊。但是，莉莉丝是怎么回事呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB04"),"not F103==0","img/CH_LLB04A@2x.png","True","img/CH_LBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH176"
    智纱 "「哎？」"
    志雄 "「那个，刚才你提到了吧，住在莉莉丝家里什么的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA03"),"not F103==0","img/CH_LLA03A@2x.png","True","img/CH_LBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCH06A_CH177A"
    智纱 "「啊、那、那个……{w=3}{nw}"
#VO_WAT VO_WAIT_START
#REMOVE_REEK_CHR 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC04"),"not F103==0","img/CH_LLC04A@2x.png","True","img/CH_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH177B"
    extend "什么事也没有啊？」"
    "为什么是疑问句呢？　智纱那平静不下来的视线游移着，总觉得有些可疑。"
    "这么说来，刚才在店里说给父母亲买土特产的时候，她特别的慌张。"
    "嗯～，好奇怪。"
    志雄 "「智纱，没有在隐瞒什么吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC06"),"not F103==0","img/CH_LLC06A@2x.png","True","img/CH_LBC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH178"
    智纱 "「没，没有隐瞒什么啦！」"
    志雄 "「智纱」"
    stop music fadeout 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC05"),"not F103==0","img/CH_LLC05A@2x.png","True","img/CH_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH179"
    智纱 "「呜……」"
    "听我的口气有些强硬，智纱沮丧地低下了头。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC02"),"not F103==0","img/CH_LLC02A@2x.png","True","img/CH_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH180"
    智纱 "「……不会发火吗？」"
    志雄 "「嗯，不发火的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC03"),"not F103==0","img/CH_LLC03A@2x.png","True","img/CH_LBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "智纱闭着嘴犹豫一会儿，终于开始说了。"
    window hide
    play music "OBGM06"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC05"),"not F103==0","img/CH_LLC05A@2x.png","True","img/CH_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH181"
    智纱 "「那个……其实和志雄君一起去旅行的事情，我没有跟父亲和母亲说」"
    志雄 "「哎？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC03"),"not F103==0","img/CH_LLC03A@2x.png","True","img/CH_LBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH182"
    智纱 "「我撒了个谎，说是住在了莉莉丝家，才出来的。也跟莉莉丝说好，跟我口径一致」"
    "这样啊。刚才智纱在电话里说的，是这么回事啊……。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC02"),"not F103==0","img/CH_LLC02A@2x.png","True","img/CH_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH183"
    智纱 "「因为……我想，和志雄君一起去旅行」"
    voice "NCH06A_CH184"
    智纱 "「好不容易志雄君邀请我的啊？　所以呢，不管怎么样都想来」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC05"),"not F103==0","img/CH_LLC05A@2x.png","True","img/CH_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH185A"
    智纱 "「但是，父亲和母亲也说，因为是快要考试了，必须要学习……{w=3}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC03"),"not F103==0","img/CH_LLC03A@2x.png","True","img/CH_LBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH185B"
    extend "然后，我就说要住在莉莉丝的家里学习了」"
    "用着最后仿佛要消失了一般的声音，智纱说道。"
    "如果是这样，那就找我来商量啊……。那样的话，我们一起去恳求智纱的父母亲，也许我还能帮上些忙……。"
    志雄 "「真是的……拿你没办法啊—」"
    "我轻轻地握住了智纱的手。她的手好小、好柔弱，仿佛用力一握就会碎掉。"
    志雄 "「来吧，难道要一直失落下去吗。差不多该回去了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA03"),"not F103==0","img/CH_LLA03A@2x.png","True","img/CH_LBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCH06A_CH186"
    智纱 "「哎……？」"
#REMOVE_REEK_CHR 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC02"),"not F103==0","img/CH_LLC02A@2x.png","True","img/CH_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH187"
    智纱 "「志雄君，你不发火？」"
    志雄 "「没，我不发火啊。我不是说过了嘛。我不发火」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC05"),"not F103==0","img/CH_LLC05A@2x.png","True","img/CH_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH188"
    智纱 "「但是……」"
    志雄 "「而且，没有发火的必要吧？　不如说，我还很高兴呢。因为智纱你是如此地重视着，和我一起度过的时间」"
    "如果说有要发火的对象，那就是没能和智纱商量这件事的我自己。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC01"),"not F103==0","img/CH_LLC01A@2x.png","True","img/CH_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH189"
    智纱 "「……谢谢」"
    "虽然只有一点点，智纱对我露出了笑容。"
    stop music fadeout 1
    志雄 "「对了，智纱。把手伸出来」"
    "本来是想之后给她一个惊喜的，还是现在就给她吧。因为我想让智纱打起精神来。"
    hide lh0 with dissolve
#CHR_POSC 0
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBC04"),"not F103==0","img/CH_XLC04A@2x.png","True","img/CH_XBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH190"
    智纱 "「怎么了？」"
    "智纱很诧异地伸出了手。"
    志雄 "「给」"
    window hide
#BG_INIC 1
    play sound "SE03_03"
    show expression "img/NIMG16C@2x.png" as bg1 zorder 100 with dissolve
    pause (64/32.0)
#THING_DISAP 1,0,400,10
    hide bg1 with dissolve
    play music "OBGM29"
    "在她的手心里，我把刚才智纱没有买下来的最后一个——小狗的钥匙链放了上去。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBA04"),"not F103==0","img/CH_XLA04A@2x.png","True","img/CH_XBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH191"
    智纱 "「这个……」"
    window hide
    志雄 "「这是给智纱的土特产。虽说土特产本来是要到旅行结束之后再给的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBA01"),"not F103==0","img/CH_XLA01A@2x.png","True","img/CH_XBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH192"
    智纱 "「……谢，谢谢你」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBC01"),"not F103==0","img/CH_XLC01A@2x.png","True","img/CH_XBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH193"
    智纱 "「我真的，很想要它……好高兴」"
    "智纱轻轻地把那个钥匙链抱在怀里。"
    "她在刚才的店里一直犹豫着。买下来果然太好了。"
    "看着智纱那洋溢着害羞和欣喜的笑容，我也感觉到有些温暖了。"
    志雄 "「……那，差不多该回去了吧。现在开始返回旅馆时间好像正好」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBB02"),"not F103==0","img/CH_XLB02A@2x.png","True","img/CH_XBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH194"
    智纱 "「嗯」"
    voice "NCH06A_CH195"
    智纱 "「我会很珍惜它的。这个钥匙链」"
    window hide
#BG_SET_BACK
#ROUTINE_STA
#BG_PRIC 0
#CHR_PRIC 0
#BG_INIC 3
#BG_PRIC 3
#EFF_PRI 0
#ROUTINE_STP
    scene expression "img/NIMG01C@2x.png" as bg3 zorder 3 with dissolve
    show expression "img/CloudC1_0@2x.png" as cloud0 zorder 5:
        ycenter .55
        xcenter .75
        linear 500 xcenter .0
    show expression "img/CloudC1_1@2x.png" as cloud1 zorder 5:
        ycenter .55
        xcenter .65
        linear 500 xcenter .0
    show expression "img/CloudC2_0@2x.png" as cloud2 zorder 8:
        yalign .0
        block:
            xcenter 1.0
            linear 140 xcenter .0
            repeat
    show expression "img/CloudC2_1@2x.png" as cloud3 zorder 8:
        ycenter .2
        block:
            xcenter 1.0
            linear 100 xcenter .0
            repeat
    show expression "img/CloudC2_2@2x.png" as cloud4 zorder 8:
        yalign .0
        block:
            xcenter 1.0
            linear 120 xcenter .0
            repeat
    show expression "img/CloudC2_3@2x.png" as cloud8 zorder 8:
        ycenter .0
        block:
            xcenter 1.0
            linear 135 xcenter .0
            repeat
    show expression "img/CloudC3_0@2x.png" as cloud5 zorder 10:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.5
            linear 50 xpos .0
            xpos 1.0
            linear 50 xpos .5
            repeat
    show expression "img/CloudC3_1@2x.png" as cloud6 zorder 12:
        xanchor 1.0
        yalign 1.0
        block:
            xpos .6
            linear 78 xpos .0
            xpos 1.0
            linear 52 xpos .6
            repeat
    show expression "img/CloudC4@2x.png" as cloud7 zorder 15:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.2
            linear 20 xpos .0
            xpos 1.0
            linear 100 xpos .2
            repeat
    with dissolve
#EFF_STAC 0,CLOUD_C,EFF_SKIP
#SE_VOLC 1,255
    play sound "SE01_12L"
#ROUTINE_STA
#BG_BLUR 0
#BG_ALP_AUTOC 0,0,0,1
#CHR_ALP_AUTOC 0,0,0,1
#ROUTINE_STP
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "然后，在回去的路上，智纱把那个钥匙链取出来了好几次，很高兴地看着它。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    scene expression Solid("000") with fade
    stop se
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG63NA1@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG63NA1@2x.jpg" as bg0 with dissolve
    play sound "SE06_29L"
    pause (32/32.0)
    play sound "SE05_16L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,
    "在食堂吃过晚饭之后，我们就这样回到了房间里。"
#SE_VOLC 1,(64/4)
#BG_OVER_MGNC EXBG04N,0,CH_ZLB02,CH_ZBB02
    scene expression "img/EXBG04N@2x.jpg" as bg0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB02"),"not F103==0","img/CH_ZLB02A@2x.png","True","img/CH_ZBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "BGM13"
    voice "NCH06A_CH196"
    智纱 "「啊哈哈，总觉得有点窘迫呢」"
    志雄 "「算是吧……」"
    "在食堂里，我们的周围都是些大人，高中生年纪的组合除了我们以外就没有了。正因为这个，我们在那里显得比较显眼。"
    "并不是说被周围的人们围观了。可是，总觉得很不好意思，感觉在那里呆着有些不自在。"
#MUS_VOL 0
#SE_VOLC 0
#SE_VOLC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB03"),"not F103==0","img/CH_ZLB03A@2x.png","True","img/CH_ZBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH197"
    智纱 "「……」"
    志雄 "「……」"
    "……对话停了下来。"
    "现在，时间是晚上7点半。夏天的太阳终于落山了，窗户外面暗了下来。"
    "平常智纱来我家的时候，有时会打扫打扫房间，有时会给我做饭，还有时间的话就是出去买东西。"
    "但是，在这旅馆里打扫也是做饭也是买东西也是，都不需要……。已经这个时间了，再出门也……。"
    stop se fadeout 1
#SE_VOLC 1,(64/4)
#MUS_VOL 128
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB06"),"not F103==0","img/CH_ZLB06A@2x.png","True","img/CH_ZBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH198"
    智纱 "「嗯～……」"
    "智纱好像也有些闲得无聊，在房间里看来看去。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBA01"),"not F103==0","img/CH_ZLA01A@2x.png","True","img/CH_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH199"
    智纱 "「呃，不口渴吗？」"
    志雄 "「啊，嗯，是呢」"
    voice "NCH06A_CH200"
    智纱 "「那样的话，我去准备点喝的东西吧」"
    志雄 "「喝的东西？」"
    "房间里配备好了冰箱，但是里面放的都是酒。不管怎么说，那个是不能喝的。"
    show expression "img/BG63NA1@2x.jpg" as bg_over zorder 2 with dissolve
    play sound "SE03_88"
    play sound "SE03_66"
    "智纱打开了放在房间角落里的旅行包，在里面找了起来。"
    志雄 "「在干什么呢？」"
    voice "NCH06A_CH201"
    智纱 "「那个～……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+224)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBC01"),"not F103==0","img/CH_MLC01A@2x.png","True","img/CH_MBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH202"
    智纱 "「找到了，是这个」"
    "智纱从包中取出的是，红茶的茶包。"
    志雄 "「特地带来的吗？」"
    voice "NCH06A_CH203"
    智纱 "「嗯」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_OVER_MGNC EXBG04N,0,CH_ZLB05,CH_ZBB05
    scene expression "img/EXBG04N@2x.jpg" as bg0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB05"),"not F103==0","img/CH_ZLB05A@2x.png","True","img/CH_ZBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "智纱把红茶的茶包放进了桌子上的茶杯里。房间里配备的热水壶，一直是保温状态。"
    play sound "SE03_74"
    "我把热水从壶里倒进了茶杯里。从茶包里渗出的红色，在茶杯中扩散开来。"
    play sound "SE03_20"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBA01"),"not F103==0","img/CH_ZLA01A@2x.png","True","img/CH_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH204"
    智纱 "「来，给你。用茶碗来泡红茶，有点奇怪呢」"
    志雄 "「完全没关系的，谢谢你」"
    "从智纱手里接过红茶。温暖的蒸汽和独特的香味飘了出来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB06"),"not F103==0","img/CH_ZLB06A@2x.png","True","img/CH_ZBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH205"
    智纱 "「有什么茶点之类的东西吗……」"
    show expression "img/BG63NA1@2x.jpg" as bg_over zorder 2 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBB01"),"not F103==0","img/CH_MLB01A@2x.png","True","img/CH_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCH06A_CH206"
    智纱 "「我、我去买些回来！」"
    "很慌张地说着，智纱站了起来。"
    志雄 "「等一下，智纱！　不用特地去买的啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBB03"),"not F103==0","img/CH_MLB03A@2x.png","True","img/CH_MBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH207"
    智纱 "「是、是吗？」"
    志雄 "「嗯。没关系没关系」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "一边这么说着，一边喝了一口智纱泡的红茶。嗯，就算是袋茶，也够好喝了。"
#BG_OVER_MGNC EXBG04N,0,CH_ZLC04,CH_ZBC04
    scene expression "img/EXBG04N@2x.jpg" as bg0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBC04"),"not F103==0","img/CH_ZLC04A@2x.png","True","img/CH_ZBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH208"
    智纱 "「志雄君，没有什么其他想做的事情吗？」"
    志雄 "「想做的事情？　……嗯～，并没有什么啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBC02"),"not F103==0","img/CH_ZLC02A@2x.png","True","img/CH_ZBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH209"
    智纱 "「是吗？」"
    voice "NCH06A_CH210"
    智纱 "「这样的话，那个」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBC05"),"not F103==0","img/CH_ZLC05A@2x.png","True","img/CH_ZBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "智纱闭着口不作声，视线游移着，好像在找什么东西。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBA01"),"not F103==0","img/CH_ZLA01A@2x.png","True","img/CH_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#THREAD_STA 1,THREAD_CHISA_NEAR
    voice "NCH06A_CH211"
    智纱 "「这样的话，肩膀有没有不舒服？　给你按摩一下好吗？」"
#THREAD_WAT 1
#MESX "%K%P"
    "智纱向前探出身子问道。好像是被她的气势给压倒了，我摆着手。"
    志雄 "「没事没事，没关系的啊。肩膀一点也没有不舒服的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBC04"),"not F103==0","img/CH_ZLC04A@2x.png","True","img/CH_ZBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#THREAD_STA 1,THREAD_CHISA_FAR
    voice "NCH06A_CH212"
    智纱 "「这样啊……」"
    "从刚才开始总觉得智纱冷静不下来。莫非，果然对这个双人房的状况感到有些困惑。"
    "一边这样想着，一边为了掩盖我的无聊，我把手伸向杯子。"
    志雄 "「啊」"
    "茶碗里已经空了。"
    "智纱立刻就来问我。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBA01"),"not F103==0","img/CH_ZLA01A@2x.png","True","img/CH_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH213"
    智纱 "「红茶，要再喝一杯吗？」"
    志雄 "「啊，嗯」"
    "就好像是在等待我的回答一样，智纱立刻站了起来。"
    志雄 "「不用那么着急的啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB01"),"not F103==0","img/CH_ZLB01A@2x.png","True","img/CH_ZBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH214"
    智纱 "「没有着急啊。没关系的」"
    "是吗？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB05"),"not F103==0","img/CH_ZLB05A@2x.png","True","img/CH_ZBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE03_74"
    "智纱从我手里接过茶碗，兴冲冲地去准备下一碗红茶。"
    stop se
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBA01"),"not F103==0","img/CH_ZLA01A@2x.png","True","img/CH_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH215"
    智纱 "「给，请用」"
    "智纱把茶包从茶碗中拉了起来，正要把泡好的第二杯红茶交到我的手上——。"
    stop music fadeout 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBA03"),"not F103==0","img/CH_ZLA03A@2x.png","True","img/CH_ZBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCH06A_CH216"
    智纱 "「——哇！？」"
#REMOVE_REEK_CHR 0
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "就在这时，智纱的身体倾斜了一下。盛着红茶的茶碗从她的手里滑落……。"
    play sound "SE03_48"
    志雄 "「啊！？」"
#THREAD_STA 1,THREAD_QUA_WIN
#VIB_DOKA 
#MESA A_CH_SI,"【志雄】「啊！？」"
#THREAD_WAT 1
#WIN_POS 0,0
#VIB_STP 5
#MESX "%K%P"
    "下一个瞬间，红茶的颜色在我的衣服上扩展了开来。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLC06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBC06"),"not F103==0","img/CH_ZLC06A@2x.png","True","img/CH_ZBC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH217"
    智纱 "「没、没关系吧！？　对不起！」"
    志雄 "「没、没事没事，这点小事。只是在衣服的上面，大概是不会烫伤的」"
    show expression "img/BG63NA1@2x.jpg" as bg_over zorder 2 with dissolve
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLA05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBA05"),"not F103==0","img/CH_MLA05A@2x.png","True","img/CH_MBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH218"
    智纱 "「『大概』可不行啊！　不用水冷却下可不行！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA05"),"not F103==0","img/CH_LLA05A@2x.png","True","img/CH_LBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH219"
    智纱 "「不管怎么样，先把衣服脱了！」"
    志雄 "「哇，智、智纱！？　等、等一下」"
    "智纱用手抓住了我的衣服。然后，手去拧衬衫的纽扣……。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#SE_VOLC 1,
    play music "BGM14"
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBA04"),"not F103==0","img/CH_XLA04A@2x.png","True","img/CH_XBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH220"
    智纱 "「……啊」"
    "在极近的距离上和智纱四目相对。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBB03"),"not F103==0","img/CH_XLB03A@2x.png","True","img/CH_XBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "一瞬间，智纱的脸像沸腾了一样红了起来。"
    "客观地看下现在的状况——时间是夜里，有人在脱我的上衣，在脱它的是智纱……。"
    志雄 "「没、没关系的，真的。擦一下就好了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB03"),"not F103==0","img/CH_LLB03A@2x.png","True","img/CH_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "一边说着一边从智纱那里离开，正要把手伸向桌子上的抹布——。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLA05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBA05"),"not F103==0","img/CH_XLA05A@2x.png","True","img/CH_XBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH221"
    智纱 "「不行！」"
    "智纱的手没有放开我的衣服。"
    voice "NCH06A_CH222"
    智纱 "「说不定还是会烫伤了，而且就那样放着衣服上也会有污渍的了。所以呢，赶快脱下来！」"
    志雄 "「我、我知道、知道了啊。我会好好确认的！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XLC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XBC02"),"not F103==0","img/CH_XLC02A@2x.png","True","img/CH_XBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH223"
    智纱 "「真的？」"
    志雄 "「啊，真的真的」"
    voice "NCH06A_CH224"
    智纱 "「这样的话……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC02"),"not F103==0","img/CH_LLC02A@2x.png","True","img/CH_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "智纱手上的力道缓和了。现在可以从智纱那里离开了。"
    voice "NCH06A_CH225"
    智纱 "「……」"
    "呜，还在看着这里……。看来多半是直到确认我没有烫伤为止是不想放我走了。"
    志雄 "「……那，我先去洗澡了！」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我快速地抓起事先从包里拿出来的毛巾，快步走向门的方向。"
    voice "NCH06A_CH226B"
    智纱 "「啊！？　志雄君！？」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    show expression "img/BG62NA@2x.jpg" as bg1 zorder 1 with dissolve
    stop sound fadeout 1
    stop music fadeout 1
    play sound "SE00_47"
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
#BG_SWPC 0
    hide bg1 with dissolve
#BG_ALPC 1
#BG_PRI 0
#BG_PRI 1
    scene expression "img/BG62NA@2x.jpg" as bg0 with dissolve
#SE_WATC 0
    stop sound
    stop music fadeout 1
    "把智纱的声音留在了身后，我离开了房间。"
    "……果然在智纱面前脱衣服，总还是觉得不好意思的。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG64NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression Solid("000") with None
#FADE_IN 0
    "在浴场的更衣室里脱下上衣，确认了一下，果然没有烫伤。"
    "衣服……弄上了一些污渍。这也没办法。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128
    play sound "SE03_78"
    play sound "SE05_16L"
    pause (16/32.0)
#EFF_STAC 0,YUGE,EFF_SKIP
#FADE_IN 1
#SE_VOLC 1
    play music "BGM11"
    志雄 "「啊～。热水真不错」"
    "是因为时机正好吗，除了我之外没有一个客人。以包场的状态，舒舒服服地泡在宽阔的浴池里。"
    play sound "SE03_66"
    "……正在这么想着，好像有人进到更衣室里来了。"
    "嘛，因为也不是真的包场，所以也没办法。"
    play sound "SE00_49"
    voice "NCH06A_CH227_K"
    智纱？ "「……打扰了」"
    "一边开门一边客客气气地说『打扰了』。我也并没有什么拒绝的必要……。"
    window hide
#SE_VOLC 1,255
    stop music fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    scene expression Solid("000") with None
#FADE_IN 0
    play sound "SE03_64"
    "……有必要。"
    window hide
#FADE_OUT 0
#BG_SET_BACK 
#BG_INIC 1
#BG_INIC 3
#BG_PRI 3
#BG_POSC 1,0,-448,640,448
    show expression "img/NIMG18B@2x.jpg" as bg1 zorder 1:
        yalign 1.0
        linear 1 yalign 0.0
#SE_VOLC 1
#FADE_IN 1
    voice "NCH06A_CH228_K"
    智纱 "「晚、晚上好……」"
    window hide
    play sound "SE07_23"
#BG_POS_AUTOC 1,,F24,192
#BG_POS_SAVEC 1
#BG_POS_SAVEC 3
    hide bg3 with dissolve
#BG_PRI 3
#BG_POSC 3,0,0,640,448
    pause (192/32.0)
    play sound "SE07_02"
    志雄 "「智、智纱！？」"
#THREAD_STA 1,THREAD_CHISA_UP
#MESA A_CH_SI,"【志雄】「智、智纱！？」"
#THREAD_WAT 1
#MESX "%K%P"
    "为、为什么智纱会在这里！？　我把男浴室和女浴室搞错了吗！？"
    "不，没有那回事的，不可能的。"
    "那，是智纱搞错了吗？"
    "不对，假如是把男浴室和女浴室搞错了的话，为什么会穿着泳装！？"
    window hide
    scene expression "img/BG64NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,112,96
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MPA06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MFA06"),"not F103==0","img/CH_MPA06A@2x.png","True","img/CH_MFA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#EFF_STAC 0,YUGE2,EFF_SKIP
#BG_COLC 0,128,128,128
    hide bg1 with dissolve
    志雄 "「那，那～个……为什么会在这里，智纱？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MPC06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MFC06"),"not F103==0","img/CH_MPC06A@2x.png","True","img/CH_MFC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "刷地一下，智纱的脸红了。"
    志雄 "「莫非是，把男浴池和女浴池，搞错了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MPC03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MFC03"),"not F103==0","img/CH_MPC03A@2x.png","True","img/CH_MFC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "智纱一个劲地摇着头。"
    "那，为什么？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MPC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MFC02"),"not F103==0","img/CH_MPC02A@2x.png","True","img/CH_MFC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH229_K"
    智纱 "「总、总之，我是想来检查一下，志雄君有没有被烫伤的……」"
    志雄 "「为了这个特地……？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MPC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MFC05"),"not F103==0","img/CH_MPC05A@2x.png","True","img/CH_MFC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH230_K"
    智纱 "「还有……」"
    "还有？"
    window hide
    play music "BGM16"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MPA05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MFA05"),"not F103==0","img/CH_MPA05A@2x.png","True","img/CH_MFA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH231_K"
    智纱 "「我，我来为你擦背吧！」"
    "智纱好像是在给自己鼓劲一样，握紧了拳头。"
    "哎哎！？"
    志雄 "「等等，智纱！」"
    "智纱拿着盥洗用具，一步步地接近我。另一方面，我没法从浴池里出来。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve

#BG_SET_BACK 
#BG_INIC 3
#BG_UVC 3,0,0,640,448

#BG_UVC 0,0,512,640,448
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,112,96
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LPA05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LFA05"),"not F103==0","img/CH_LPA05A@2x.png","True","img/CH_LFA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    hide bg3 with dissolve
    voice "NCH06A_CH232_K"
    智纱 "「来，志雄君，从浴池里出来！」"
    志雄 "「怎、怎么可能出来啊！」"
    voice "NCH06A_CH233_K"
    智纱 "「不用在意！　我，不会去看的！」"
    志雄 "「不是，不是那种问题！」"
    voice "NCH06A_CH234_K"
    智纱 "「没关系的，志雄君你坐在那里就好了！」"
    志雄 "「这完全，不是什么没关系吧！」"
    "您是凭着什么说没关系的啊，箱崎智纱小姐！？"
    "这么说来，有别的客人进来的话该怎么办啊！？"
    window hide
    stop music fadeout 1
    play sound "SE03_66"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LPC06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LFC06"),"not F103==0","img/CH_LPC06A@2x.png","True","img/CH_LFC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "哇，为什么机会这么不巧啊！？　有什么人进到更衣室里来了！"
    window hide
    play music "OBGM13"

#BG_SET_BACK 
#BG_INIC 3
#BG_UVC 3,0,0,640,448

    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_UVC 0,0,0,640,448
    hide bg3 with dissolve
    "向周围看看。就没有一个能把智纱藏起来的地方吗！？"
    "更衣室以外的出入口……没有。"
    "窗户……打不开。"
    "地板……既没有陷阱也没有地下道。"
    "天花板……又不是忍者，怎么才能躲在天花板上啊！？"
    "其他能躲起来的地方……啊，只有『这里』了吗……！"
#THREAD_STA 1,THREAD_EXIT
#MES "更衣室以外的出入口……没有。"
#THREAD_WAT 1
#MESX "%K%P"
#THREAD_STA 1,THREAD_WINDOW
#MES "窗户……打不开。"
#THREAD_WAT 1
#MESX "%K%P"
#THREAD_STA 1,THREAD_FLOOR
#MES "地板……既没有陷阱也没有地下道。"
#THREAD_WAT 1
#MESX "%K%P"
#THREAD_STA 1,THREAD_ROOF
#MES "天花板……又不是忍者，怎么才能躲在天花板上啊！？"
#THREAD_WAT 1
#MESX "%K%P"
#THREAD_STA 1,THREAD_TUB
#MES "其他能躲起来的地方……啊，只有『这里』了吗……！"
#THREAD_WAT 1
#MESX "%K%P"
    window hide
#BG_UV_AUTOC 0,0,0,640,448,1,F24,48
#BG_UV_SAVEC 0
    志雄 "「智纱！　浴池。快跑到浴池里来！」"
    window hide

#BG_SET_BACK 
#BG_INIC 3
#BG_UVC 3,0,0,640,448

#BG_UVC 0,0,512,640,448
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,112,96
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LPC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LFC04"),"not F103==0","img/CH_LPC04A@2x.png","True","img/CH_LFC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    hide bg3 with dissolve
    voice "NCH06A_CH235_K"
    智纱 "「哎哎！？」"
    志雄 "「一直潜在浴池里的话，可能能躲过去！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LPC06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LFC06"),"not F103==0","img/CH_LPC06A@2x.png","True","img/CH_LFC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH236_K"
    智纱 "「办，办不到的啦！　会窒息的！」"
    play sound "SE00_49"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LPA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LFA03"),"not F103==0","img/CH_LPA03A@2x.png","True","img/CH_LFA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "这个时候，门无情地打开了。Ｔｉｍｅ　ｕｐ…………。"
    voice "NCH06A_SN000_K"
    信？ "「这位客官，这里可不是混浴哟」"
    志雄 "「对，对不起！　马上就出……去……？」"
    window hide
    stop music fadeout 1

#BG_SET_BACK 
#BG_INIC 3
#BG_UVC 3,0,0,640,448

    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_UVC 0,0,0,640,448
    hide bg3 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
#CHR_COLC 1,128,112,96
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA06"),"True","img/SN_MBA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    志雄 "「稻、稻穗先生！？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA02"),"True","img/SN_MBA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH06A_SN001_K"
    信 "「对，就是我～。爱的传道师，大家的稻穗信君」"
    if F105:
        jump L_NCH06A_BRA02_A
    jump L_NCH06A_BRA02_B
label L_NCH06A_BRA02_A:
    "果然……。"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG62AA@2x.jpg" as bg2 zorder 2 with dissolve
#SE_VOLC 1,0
#BG_INIC 1
#BG_PRI 1
#EFF_STPC 0,EFF_SKIP
    scene expression "img/BG62AA@2x.jpg" as bg0 with dissolve
#BG_ALPC 0
#BG_ALPC 2
#CHR_ALPC 1
    hide bg1 with dissolve
    play music "BGM13"
    志雄 "「唉？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB04"),"not F103==0","img/CH_LLB04A@2x.png","True","img/CH_LBB04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH093_K"
    智纱 "「怎么了？」"
    志雄 "「没事……」"
    志雄 "「刚才总觉得，有个本不应该在这里的人……」"
    window hide
    stop music fadeout 1
#BG_INIC 1
#BG_PRI 1
    scene expression "img/BG64NA@2x.jpg" as bg0 with dissolve
    hide bg2 with dissolve
#BG_UVC 2,0,0,640,448
    hide lh2 with dissolve
#BG_ALPC 0
#CHR_ALPC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA02"),"True","img/SN_MBA02A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#EFF_STAC 0,YUGE,EFF_SKIP
#SE_VOLC 1
    hide bg1 with dissolve
    志雄 "「果然，白天在旅馆里转悠的时候看见的就是稻穗先生吗！？」"
    jump L_NCH06A_BRA02_X
label L_NCH06A_BRA02_B:
    志雄 "「为，为什么稻穗先生会在这里！？」"
    jump L_NCH06A_BRA02_X
label L_NCH06A_BRA02_X:
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop se
    stop sound
    stop music fadeout 1
#FADE_IN 0
    return
#label THREAD_QUA_WIN
#TH_QUAKE_WIN 4
#EOT
#label THREAD_QUA_WIN_L
#TH_QUAKE_WIN_L	2
#EOT
#label THREAD_EXIT
#BG_UV_AUTOC 0,,(448/4),(640/2),(448/2),1,F123,48
#BG_UV_SAVEC 0
#BG_UV_AUTOC 0,(640/2),(448/4),(640/2),(448/2),1,F123,48
#BG_UV_SAVEC 0
#EOT
#label THREAD_WINDOW
#BG_UV_AUTOC 0,((640/10)*4),(448/4),(640/2),(448/2),1,F123,48
#BG_UV_SAVEC 0
#EOT
#label THREAD_FLOOR
#BG_UV_AUTOC 0,((640/10)*4),(448/2),(640/2),(448/2),1,F123,48
#BG_UV_SAVEC 0
#EOT
#label THREAD_ROOF
#BG_UV_AUTOC 0,((640/10)*4),0,(640/2),(448/2),1,F123,48
#BG_UV_SAVEC 0
#EOT
#label THREAD_TUB
#BG_UV_AUTOC 0,((640/10)*4),(448/4),(640/2),(448/2),1,F123,48
#BG_UV_SAVEC 0
#EOT
#label THREAD_CHISA_NEAR
#CHR_SCL_AUTOC 0,272,272,1,F123
#CHR_SCL_SAVEC 0
#EOT
#label THREAD_CHISA_FAR
#CHR_SCL_AUTOC 0,241,241,1,F123
#CHR_SCL_SAVEC 0
#EOT
#label THREAD_CHISA_UP
#BG_UV_AUTOC 1,(640/4),(448/4),(640/2),(448/2),1,F123,4
#BG_UV_SAVEC 1
#BG_UV_AUTOC 1,0,0,640,448,1,F123,28
#BG_UV_SAVEC 1
#EOT