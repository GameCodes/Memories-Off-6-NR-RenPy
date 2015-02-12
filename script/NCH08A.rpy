label NCH08A:
    $currentlabel = "NCH08A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '30'
    $date = '0'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#FADE_IN 0
#CAL_DSP_BG NIMG15N,CAL_0730
    show expression "img/NIMG15N-568h@2x.jpg" as cal zorder 5
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
    show expression "img/BG60NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG60NA@2x.jpg" as bg0 with dissolve
    play sound "SE05_16L"
    pause (16/32.0)
    play sound "SE08_16L"
    pause (16/32.0)
#FADE_IN 1
#SE_VOLC 0
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "嗯～……。"
    志雄 "「智纱，还不来啊……」"
    "在庭院里的椅子上坐了下来，我无意中把心声从嘴里说了出来。"
    "从远处不时传来太鼓的声音。神社里已经挤满了人，小店什么的，现在也差不多开始营业了吧。"
    "我和智纱本来也应该在那个人群之中的……。"
    voice "NCH08A_SN000"
    信？ "「哟，这不是塚本君嘛」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_SBA01"),"True","img/SN_SBA01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    play music "OBGM25"
    "听到后面传来的声音，我回过头去，是稻穗先生从旅馆里走了出来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN_MBA01'",DynamicDisplayable(mouthanime,"SN_MBA01"),"True","img/SN_MBA01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCH08A_SN001"
    信 "「在这种地方，干什么呢？」"
    志雄 "「没什么，今天在神社有祭典，我打算和智纱一起去」"
    voice "NCH08A_SN002"
    信 "「啊，原来如此。但是，最重要的智纱，好像没有看到啊」"
    志雄 "「就是这样啊。从房间出来的时候，不知怎么被香里阿姨叫住了……」"
    "补充一句，香里阿姨是我们的监护人。"
    志雄 "「她说了马上就好，然后就把智纱一个人带走了。我没办法，只能在这里等智纱——」"
    stop music fadeout 1
    voice "NCH08A_CH000"
    智纱？ "「久、久等了！」"
    window hide
#SE_VOLC 1,0
#BG_SET_BACK 
#BG_INIC 1
#BG_UVC 1,((640/64)*9),0,((640/16)*7),((448/16)*7)
#IF F103!0, GOTO IF_ELSE1
    if F103:
        jump NCH08A_IF_ELSE1
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH09A")]=True
    show expression "img/EVN_CH09A@2x.jpg" as bg1 with dissolve
    jump NCH08A_IF_END1
label NCH08A_IF_ELSE1:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH09D")]=True
    show expression "img/EVN_CH09D@2x.jpg" as bg1 with dissolve
label NCH08A_IF_END1:
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play music "BGM13"
    "听到突然传来的声音，我回过头去，出现在那里的是……智纱。"
#THREAD_STA 1,THREAD_CHISA_PAN
    "但是她穿的衣服，和从房间出来的时候完全不一样。"
#MES "但是她穿的衣服，和从房间出来的时候完全不一样。"
#THREAD_WAT 1
#MESX "%K%P"
    window hide
#BG_UV_AUTOC 1,0,0,640,448,1,F24,96
#BG_UV_SAVEC 1
    志雄 "「你带着浴衣来了啊」"
    voice "NCH08A_CH001"
    智纱 "「嗯，不是，不是的哦。是志雄君的母亲借给我的」"
    志雄 "「香里阿姨吗？」"
    "难道香里阿姨，考虑到祭典的事情，提前给我们准备好了吗。"
    window hide
    if F103:
        jump NCH08A_IF_ELSE2
#IF F103!0, GOTO IF_ELSE2
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH09B")]=True
    show expression "img/EVN_CH09B@2x.jpg" as bg1 with dissolve
    jump NCH08A_IF_END2
label NCH08A_IF_ELSE2:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH09E")]=True
    show expression "img/EVN_CH09E@2x.jpg" as bg1 with dissolve
label NCH08A_IF_END2:
    voice "NCH08A_CH002"
    智纱 "「怎么样？　合适吗？」"
    "智纱一边不安地确认着自己的服装，一边呆板地转了一圈。"
    志雄 "「嗯，很合适。相当的，那个……可爱啊」"
    window hide
    if F103:
        jump NCH08A_IF_ELSE3
#IF F103!0, GOTO IF_ELSE3
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH09C")]=True
    show expression "img/EVN_CH09C@2x.jpg" as bg1 with dissolve
    jump NCH08A_IF_END3
label NCH08A_IF_ELSE3:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH09F")]=True
    show expression "img/EVN_CH09F@2x.jpg" as bg1 with dissolve
label NCH08A_IF_END3:
    voice "NCH08A_CH003"
    智纱 "「谢、谢谢」"
    "智纱的脸红到了耳根子。"
    "真的……穿着浴衣的智纱，仿佛是从画之类的里边出来的一样。"
    window hide
#BG_UVC 0,(640/4),0,((640/4)*3),((448/4)*3)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_SCLC 0,384,384
#CHR_POSC 0,(24)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIA01"),"not F103==0","img/CH_LSA01A@2x.png","True","img/CH_LIA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    hide bg1 with dissolve
    voice "NCH08A_CH004"
    智纱 "「志雄君也是……很帅气哦」"
    志雄 "「哈哈，我和平常没什么不同啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIB03"),"not F103==0","img/CH_LSB03A@2x.png","True","img/CH_LIB03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH005"
    智纱 "「平常，就很帅了……」"
    志雄 "「哎，啊……」"
    "出乎意料的突然袭击，这次该轮到我脸红了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSA06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIA06"),"not F103==0","img/CH_LSA06A@2x.png","True","img/CH_LIA06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH006"
    智纱 "「啊、啊哈哈……」"
    "面对面总觉得很不好意思，我们俩相对着，低着头。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,0,(448/2)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSA06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIA06"),"not F103==0","img/CH_LSA06A@2x.png","True","img/CH_LIA06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
        xcenter .65
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBB02"),"True","img/SN_MBB02A@2x.png") as lh11 zorder (10-1):
        ypos 0.0
        xcenter .25
    with dissolve
    stop music fadeout 1
#SE_VOLC 1,
#ROUTINE_STA
#BG_UV_AUTOC 0,0,0,640,448,1,F123,24
#CHR_ALP_AUTOC 1,128,1,F123,24
#CHR_POS_AUTOC 1,(320-160),0,1,F123,24
#CHR_SCL_AUTOC 1,256,256,1,F123,24
#CHR_POS_AUTOC 0,(320+96),0,1,F123,24
#CHR_SCL_AUTOC 0,170,170,1,F123,24
#ROUTINE_STP
    voice "NCH08A_SN003"
    信 "「喂～。你们，忘了我还在这里吗」"
#MESA A_CH_SN,NCH08A_SN003,"【信】「喂～。你们，忘了我还在这里吗」"
#THREAD_WAT 1
#MESX "%K%P"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIA03"),"not F103==0","img/CH_LSA03A@2x.png","True","img/CH_LIA03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
#THREAD_STA 1,TH_YUSURU
#MES_SYNC2
#REEK_CHR 0
    voice "NCH08A_CH007"
    "智纱「啊！」"
#REMOVE_REEK_CHR 0
    "对、对啊。有稻穗先生——有别人在的时候我竟然……。"
    window hide
#SE_VOLC 1,(64/4)
    play music "OBGM25"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA06"),"True","img/SN_MBA06A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCH08A_SN004"
    信 "「感情好倒是挺不错的，不怎么注意周围，尽情展现你们仿佛笨蛋情侣一般的样子，你们觉得怎么样呢？二位」"
    "稻穗先生的脸上，浮现出了既像开玩笑、又像苦笑一样的笑容。"
    "啊啊啊啊啊！　我想起了自己说过的台词，郁闷得想倒在地上。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIB03"),"not F103==0","img/CH_LSB03A@2x.png","True","img/CH_LIB03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH008"
    智纱 "「呜呜……」"
    "智纱的脸更红了，仿佛是煮熟了一样。"
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
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320+160)
#CHR_POSC 1,(320-160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MSB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MIB03"),"not F103==0","img/CH_MSB03A@2x.png","True","img/CH_MIB03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
        xcenter .75
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA02"),"True","img/SN_MBA02A@2x.png") as lh11 zorder (10+1):
        ypos 0.0
        xcenter .25

    with dissolve
    voice "NCH08A_SN005"
    信 "「哈，算了。嗯，你们俩等下要去祭典是吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MSB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MIB01"),"not F103==0","img/CH_MSB01A@2x.png","True","img/CH_MIB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH009"
    智纱 "「啊，是」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA01"),"True","img/SN_MBA01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCH08A_SN006"
    信 "「那样的话，告诉你们一件好事吧」"
    "……。"
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
    show expression "img/BG74NA@2x.jpg" as bg0 zorder 0 with dissolve
#BG_BLUR 0
    scene expression "img/BG74NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIB02"),"not F103==0","img/CH_LSB02A@2x.png","True","img/CH_LIB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
        xcenter .35
    with dissolve
    play sound "SE08_15L"
    pause (32/32.0)
#FADE_IN 1
    play music "BGM11"
    voice "NCH08A_CH010"
    智纱 "「啊哈哈……刚才真是太不好意思了……」"
    志雄 "「嗯，下次要小心了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIB01"),"not F103==0","img/CH_LSB01A@2x.png","True","img/CH_LIB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    "已经来到了神社附近，智纱的脸上，还留着从旅馆出来时候的害羞。……不过这一点上我也一样。"
    "在路上，看到了三五成群、和智纱一样穿着浴衣的人们。在石阶的上面，能看到好像是从小店发出来的光。"
    志雄 "「来，走吧」"
    "我向智纱伸出了手。"
    志雄 "「穿着浴衣和草鞋，上台阶很困难的吧。所以，手」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIB03"),"not F103==0","img/CH_LSB03A@2x.png","True","img/CH_LIB03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH011"
    智纱 "「啊……」"
    "智纱有那么一瞬间，好像很犹豫地看了看我。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIA01"),"not F103==0","img/CH_LSA01A@2x.png","True","img/CH_LIA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH012"
    智纱 "「嗯。谢谢」"
    "就算不再把手伸过去，智纱那边也将手伸了过来，牵住了我的手。"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE01_19L"
    "然后我们两人就一起走上台阶。"
    window hide
    stop se fadeout 1
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG76NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG76NA@2x.jpg" as bg0 with dissolve
#SE_VOLC 1
#FADE_IN 1
    "爬完台阶，到达了神社境内，那里已经被小店的灯光和人群的声音包围了。"
    if F105:
        jump L_NCH08A_BRA00_A
#IF F105!0, GOTO L_NCH08A_BRA00_A
    jump L_NCH08A_BRA00_B
label L_NCH08A_BRA00_A:
    "和前天顺路来这个神社的时候相比，完全就像是两个地方。"
    jump L_NCH08A_BRA00_X
label L_NCH08A_BRA00_B:
    "路过这个神社的时候，还觉得是个很宁静的神社，只有在祭典的日子里，才展现了一副不一样的面孔。"
    jump L_NCH08A_BRA00_X
label L_NCH08A_BRA00_X:
    window hide
#SE_VOLC 1
#CHR_INIC 0
#CHR_COLC 0,128,112,96
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIA01"),"not F103==0","img/CH_LSA01A@2x.png","True","img/CH_LIA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .35
    with dissolve
    志雄 "「先要去哪家店好呢。智纱希望去哪里？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSB06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIB06"),"not F103==0","img/CH_LSB06A@2x.png","True","img/CH_LIB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH013"
    智纱 "「那～个……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIB01"),"not F103==0","img/CH_LSB01A@2x.png","True","img/CH_LIB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH014"
    智纱 "「对了，志雄君肚子饿了吗？」"
    志雄 "「有点饿了呢」"
    "因为今天有祭典，所以没有在旅馆吃晚饭，直接过来了。"
    voice "NCH08A_CH015A"
    智纱 "「这样的话，就先去吃点什么填饱肚子吧。{w=3}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSB05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIB05"),"not F103==0","img/CH_LSB05A@2x.png","True","img/CH_LIB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH015B"
    extend "像什锦烧、"
#MESA A_CH_CH,NCH08A_CH015B,"像什锦烧、"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIB02"),"not F103==0","img/CH_LSB02A@2x.png","True","img/CH_LIB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH015C"
    extend "炒面一类的……」"
    window hide

#BG_SET_BACK 
#BG_INIC 2
#BG_UVC 2,0,0,640,448

#ROUTINE_STA
#BG_UV_AUTOC 0,(640/4),512,((640/4)*3),((448/4)*3),1,F24,48
#BG_UV_AUTOC 2,(640/4),0,((640/4)*3),((448/4)*3),1,F24,48
#BG_ALP_AUTOC 0,0,1,F24,48
#CHR_ALP_AUTOC 0,0,1,F24,48
#CHR_SCL_AUTOC 0,512,512,1,F24,48
#CHR_POS_DISAP 0,-(640/4),448,1,F24,48
#ROUTINE_STP
#BG_UV_SAVEC 0
#BG_UV_SAVEC 2
#BG_ALP_SAVEC 0
#CHR_ALP_SAVEC 0
#CHR_POS_SAVEC 0
#CHR_SCL_SAVEC 0
#BG_SWPC 0
#BG_PRI 0
#BG_PRI 2
#BG_ALPC 2
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "虽然一边这么说着，一边环视着境内的小店，但智纱的眼睛还是闪闪发光地，盯着一点。"
    "——向着摆出了『苹果糖』招牌的小店那边。"
    voice "NCH08A_CH016A"
    智纱 "「……那，{w=3}{nw}"
#VO_WAT VO_WAIT_START
#THREAD_STA 1,THREAD_YAKISOBA
    voice "NCH08A_CH016B"
    extend "那个店怎么样呢？」"
#MESA A_CH_CH,NCH08A_CH016B,"那个店怎么样呢？」"
#THREAD_WAT 1
#MESX "%K%P"
    "但是，结果智纱指的是另一个卖炒面的店铺。"
    "真是的，我不由自主地苦笑着。"
    window hide

#BG_SET_BACK 
#BG_INIC 2
#BG_UVC 2,0,(((448/16)*3)+512),(640/2),(448/2)

#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,(320+192),((448/4)*3)
#CHR_COLC 0,128,112,96
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIB01"),"not F103==0","img/CH_LSB01A@2x.png","True","img/CH_LIB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#ROUTINE_STA
#CHR_POS_AUTOC 0,(320-96),0,1,F24
#CHR_ALP_AUTOC 0,128,1,F24,48
#BG_UV_AUTOC 0,0,0,640,448,1,F24
#BG_ALP_AUTOC 0,0,1,F24
#BG_UV_AUTOC 2,0,512,640,448,1,F24
#BG_UV_SAVEC 0
#BG_ALP_SAVEC 0
#BG_UV_SAVEC 2
#CHR_ALP_SAVEC 0
#CHR_POS_SAVEC 0
#CHR_SCL_SAVEC 0
#ROUTINE_STP
#BG_SWPC 0
    hide bg2 with dissolve
#BG_ALPC 2
#BG_UVC 2,0,0,640,448
    志雄 "「智纱，昨天我说过了吧。以我为优先这一点，不要再有了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIB04"),"not F103==0","img/CH_LSB04A@2x.png","True","img/CH_LIB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH017"
    智纱 "「哎？」"
    志雄 "「再多讲一些，自己想要做的事情。不对……」"
    "我摇了摇头。"
    志雄 "「我想要为智纱，去做你所期望的事情。所以，我想让你再多讲一些，你想要做的事情」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIB03"),"not F103==0","img/CH_LSB03A@2x.png","True","img/CH_LIB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH018"
    智纱 "「可是，这样的话志雄君你……」"
    志雄 "「没什么『可是』。你是想去那家店吧？」"
    window hide
#MOV_CHR_INIT 48
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
    "我看向卖苹果糖的小店。"
    "有那么一会儿，好像再想要说些什么。但是最后，智纱还是点头了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LSB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LIB02"),"not F103==0","img/CH_LSB02A@2x.png","True","img/CH_LIB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH019"
    智纱 "「嗯……！」"
    "她的笑容，混杂着迷惑和喜悦。"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 1
#BG_UVC 0,0,512,640,448
##BG_COLC 1,96,96,96
#BG_POSC 1,0,(448),640,448
#BG_SETWC 0,1,BG75NA,NIMG17A
    scene expression "img/BG75NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XSB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XIB01"),"not F103==0","img/CH_XSB01A@2x.png","True","img/CH_XIB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
#SE_VOLC 1
#BG_BLUR 0
#FADE_IN 1
    voice "NCH08A_CH020"
    智纱 "「谢谢……」"
    "在店里只买了一根苹果糖。智纱剥开了表面的玻璃纸。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XSA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XIA01"),"not F103==0","img/CH_XSA01A@2x.png","True","img/CH_XIA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
#THREAD_STA 1,THREAD_RINGOAME
    voice "NCH08A_CH021"
    智纱 "「来。志雄君你先吃」{w=3}{nw}"
#THREAD_WAT 1
#MESX "%K%P"
    "她把苹果糖递了过来。上面一阵焦糖的香气。"
    志雄 "「嗯。那，我先来」"
    "只是舔了一口，甜味就在嘴里扩散开来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XSB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XIB02"),"not F103==0","img/CH_XSB02A@2x.png","True","img/CH_XIB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH022"
    智纱 "「嘿嘿……轮到我了」"
    window hide
#BG_ALP_AUTOC 1,0,1,F24
#BG_ALP_SAVEC 1
#BG_POSC 1,0,(448/2),640,448
    "智纱一边这么说着，一边尝了一口苹果糖。"
    "智纱所希望的事情——那就是，两个人一起，舔一根苹果糖。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XSB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XIB03"),"not F103==0","img/CH_XSB03A@2x.png","True","img/CH_XIB03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH023"
    智纱 "「虽然觉得志雄君会不太高兴……能说出来太好了」"
    "智纱这么说着，脸上羞怯地染上了红晕。"
    志雄 "「就这些的话，那是小菜一碟」"
    "老实说，是很不好意思，不过，如果那样能让智纱高兴的话……。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XSA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XIA01"),"not F103==0","img/CH_XSA01A@2x.png","True","img/CH_XIA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
#THREAD_STA 1,THREAD_RINGOAME
#MES "正在这么想着，苹果糖又一次来到了我这边。"
#THREAD_WAT 1
#MESX "%K%P"
    志雄 "「嗯。那我再来一口」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XSB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XIB01"),"not F103==0","img/CH_XSB01A@2x.png","True","img/CH_XIB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH024"
    智纱 "「然后是我……」"
    window hide
#BG_ALP_AUTOC 1,0,1,F24
#BG_ALP_SAVEC 1
#BG_POSC 1,0,(448/2),640,448
    "明明是很廉价的甜味，却让我们感觉到非常的幸福。"
    志雄 "「还有什么其它想做的事情没？　去吃棉花糖、去捞金鱼或者是套圈什么的都可以啊」"
    "智纱把苹果糖从唇边移开，思索了一会，然后回答道。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XSA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XIA01"),"not F103==0","img/CH_XSA01A@2x.png","True","img/CH_XIA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH025"
    智纱 "「那接下来去吃志雄君想吃的东西吧」"
    志雄 "「别，我说了要去做智纱想要做的事情……」"
    window hide
#BG_ALP_AUTOC 1,128,1,F123
#BG_POS_AUTOC 1,0,(448/4),,F123
#BG_ALP_SAVEC 1
#BG_POS_SAVEC 1
    voice "NCH08A_CH026"
    智纱 "「在这一点上我也是一样的呀」"
    "一边把苹果糖递向我这边，她一边说道。"
    voice "NCH08A_CH027"
    智纱 "「果然，我还是想要做志雄君所希望的事情」"
    window hide
    hide bg1 with dissolve
    voice "NCH08A_CH028A"
    智纱 "「因为这是我的愿望。{w=3}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XSB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XIB01"),"not F103==0","img/CH_XSB01A@2x.png","True","img/CH_XIB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH028B"
    extend "就让我……一直抱着这个愿望，可以吗？」"
    "并不只是一方以另一方为优先，两人都同时重视着自己和对方。"
    "是这样啊。这样就很好。"
    voice "NCH08A_CH029"
    智纱 "「所以这次，就轮到去志雄君想要去的地方了」"
    志雄 "「那，那样的话……炒面的摊子怎么样？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XSB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XIB02"),"not F103==0","img/CH_XSB02A@2x.png","True","img/CH_XIB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH08A_CH030"
    智纱 "「嗯」"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
#BG_PRI 0
    scene expression "img/NIMG01D@2x.png"
    show expression "img/CloudD1_0@2x.png" as cloud0 zorder 5:
        ycenter .55
        xcenter .75
        linear 500 xcenter .0
    show expression "img/CloudD1_1@2x.png" as cloud1 zorder 5:
        ycenter .55
        xcenter .65
        linear 500 xcenter .0
    show expression "img/CloudD1_2@2x.png" as cloud2 zorder 8:
        ycenter .3
        block:
            xcenter 1.0
            linear 140 xcenter .0
            repeat
    show expression "img/CloudD2_1@2x.png" as cloud3 zorder 8:
        ycenter .2
        block:
            xcenter 1.0
            linear 100 xcenter .0
            repeat
    show expression "img/CloudD2_0@2x.png" as cloud4 zorder 8:
        ycenter .0
        block:
            xcenter 1.0
            linear 120 xcenter .0
            repeat
    show expression "img/CloudD3@2x.png" as cloud5 zorder 10:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.5
            linear 50 xpos .0
            xpos 1.0
            linear 50 xpos .5
            repeat
    with dissolve
#EFF_STAC 0,CLOUD_D,EFF_NOSKIP
#BG_COLC 0,128,128,128
    pause (32/32.0)
    "在那之后，逛了好几家店……。"
    window hide
#BG_COLC 0,128,128,128
    play sound "SE08_16L"
    pause (32/32.0)
##EFF_STAC 0,CLOUD_N,EFF_SKIP
#FADE_IN 1
    "然后，我和智纱站在神社境内的深处，眺望着从海那边升起的巨大焰火。"
    window hide
    stop se fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    scene expression Solid("000") with fade
    stop se
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 1
#BG_INIC 3
#BG_UVC 0,(640/4),0,(640/2),(448/2)
#BG_UVC 1,(640/4),0,(640/2),(448/2)
#BG_UVC 3,(640/4),0,(640/2),(448/2)
#BG_ALPC 1
#BG_ALPC 3
#BG_SETTC 0,1,3,EVN_CH10D,EVN_CH10B,EVN_CH10C
    play sound "SE03_51"
#FADE_IN 1
    play music "BGM16"
    voice "NCH08A_CH031"
    智纱 "「哇……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH10A")]=True
    scene expression "img/EVN_CH10A@2x.jpg" as bg0 with dissolve
    "五颜六色的花朵绽放在夜空中。"
    window hide
#RSET F121
#TODO
#THREAD_STA 1,THREAD_FIREWORKS1
#RSET F121
    play sound "SE03_51"
#RSET F121
    "智纱的脸被焰火映照着，呈现出各种各样的颜色。"
    志雄 "「稻穗先生告诉我们的地方真不错呢」"
    "从旅馆出来的时候，稻穗先生告诉我们的，便是从这里能很清楚地看见焰火这件事。"
    voice "NCH08A_CH032"
    智纱 "「嗯」"
#THREAD_STA 1,THREAD_FIREWORKS2
#RSET F121
    play sound "SE03_51"
#RSET F121
    "确实，在这个地方的话，也没有周围小店的灯光，能很清楚地看到焰火。"
    "因为远离了祭典的喧嚣，也没有别的人在。"
    voice "NCH08A_CH033"
    智纱 "「这次，能和志雄君两个人单独看了呢，焰火」"
    "像芦鹿岛焰火大会那次，和莉莉丝还有亨一起热热闹闹地看的确很快乐。"
#THREAD_STA 1,THREAD_FIREWORKS1
#RSET F121
    play sound "SE03_51"
#RSET F121
    "不过像这样和智纱两个人一起，安静地抬头看着夜空中的焰火，更是特别。"
    window hide
    hide bg1 with dissolve
    hide bg3 with dissolve
#BG_INIC 1
#BG_ALPC 1
#BG_PRI 1
    show expression "img/EVN_CH10F@2x.jpg" as bg1 zorder 1 with dissolve
#BG_INIC 2
#BG_POSC 2,-40,0,640,448
#BG_ALPC 2
#BG_PRI 2
    show expression "img/EVN_CH10E@2x.png" as bg2 zorder 2 with dissolve
#BG_ALP_AUTOC 1,128,1,F123
#BG_ALP_AUTOC 2,128,1,F123
#BG_POS_AUTOC 2,0,,,F24
#BG_POS_SAVEC 1
#EFF_PRI 0
#EFF_STAC 0,HANABI,EFF_SKIP
    show expression "img/fireworks2_0@2x.png" as firework:
        ypos .2
        xcenter .6
        anchor (0.5,0.5)
        zoom 0.5
        parallel:
            linear 1 zoom 2
        parallel:
            linear 1 alpha 0
    pause 1
    hide firework
    show expression "img/fireworks2_1@2x.png" as firework:
        ypos .1
        xcenter .8
        anchor (0.5,0.5)
        zoom 0.5
        parallel:
            linear 1 zoom 2
        parallel:
            linear 1 alpha 0
    pause 1
    hide firework
    show expression "img/fireworks2_2@2x.png" as firework:
        ypos .25
        xcenter .5
        anchor (0.5,0.5)
        zoom 0.5
        parallel:
            linear 1 zoom 2
        parallel:
            linear 1 alpha 0
    pause 1
    hide firework
    show expression "img/fireworks2_3@2x.png" as firework:
        ypos .15
        xcenter .7
        anchor (0.5,0.5)
        zoom 0.5
        parallel:
            linear 1 zoom 2
        parallel:
            linear 1 alpha 0
    "我握住了身边的智纱的手。"
#RSET F121
    play sound "SE03_51"
#RSET F121
    voice "NCH08A_CH034"
    智纱 "「啊……」"
    "智纱也回握住了我的手。"
    "心爱之人的存在，比任何人、任何东西感觉都要近。"
    志雄 "「我从今以后也会，一直陪在智纱的身边」"
    voice "NCH08A_CH035"
    智纱 "「我也是，一直和志雄君在一起的」"
#RSET F121
    play sound "SE03_51"
#RSET F121
    "所以——。"
    志雄 "「所以我要做个更加可靠的男人。能够支撑起智纱的人」"
    "没能看向智纱，我这样说道。这便是现在的我，竭尽全力所能许下的承诺。虽然没法面向她说这些，但我是认真的。"
    志雄 "「所以呢，如果智纱有什么想要让我做的事，我希望你能说出来。就算是这样的我，也一定能为智纱做点什么的」"
#RSET F121
    play sound "SE03_51"
#RSET F121
    "我这样起誓。"
    "希望智纱能不再勉强自己。希望智纱不用再为我的事情而紧张。"
    "希望我自己能为了这个少女做上些什么。希望我能够支撑起她。"
    "智纱看着这样的我，噗哧一笑。多亏了她这一笑，我俩之间沉重的气氛烟消云散。我真的很感激，她的关心。"
    voice "NCH08A_CH036"
    智纱 "「这样的话，那我就马上向志雄君，提一个愿望吧」"
#RSET F121
    play sound "SE03_51"
#RSET F121
    "智纱看着我这边，脸上浮现出宛如玩笑般的微笑。"
    voice "NCH08A_CH037"
    智纱 "「希望志雄君，能够尽早地决定志愿啊。因为如果志雄君不能决定志愿的话，我也不能决定呢」"
    voice "NCH08A_CH038"
    智纱 "「志雄君前进的道路旁，就一定有我前进的道路」"
    "……这样啊。"
    "终于，我明白了，智纱久久不能决定自己志愿的理由。"
    志雄 "「我明白了，箱崎老师。我会决定好自己的志愿，学习也会好好加油的」"
    voice "NCH08A_CH039"
    智纱 "「很好」"
    "宛如演技一样，智纱装模作样地说道。"
#RSET F121
    play sound "SE03_51"
#RSET F121
    voice "NCH08A_CH040"
    智纱 "「噗……啊哈哈」"
    志雄 "「哈哈哈哈」"
    "两个人都不由自主地笑了出来，在这样满天焰火的夜幕之下。"
    志雄 "「那样的话，我也向智纱提一个愿望吧」"
    voice "NCH08A_CH041"
    智纱 "「嗯。什么？」"
    志雄 "「为了让我从今以后也能努力……奖励就预先支付了吧」"
#RSET F121
    play sound "SE03_51"
    voice "NCH08A_CH042"
    智纱 "「啊……」"
    "我轻轻地抱住了智纱的身体。"
    window hide
#THREAD_WAT 1
#EFF_STPC 0,EFF_SKIP
#BG_INIC 0
#IF F103!0, GOTO IF_ELSE4
    if F103:
        jump NCH08A_IF_ELSE4
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH11A")]=True
    show expression "img/EVN_CH11A@2x.jpg" as bg0 zorder 100 with dissolve
    jump NCH08A_IF_END4
label NCH08A_IF_ELSE4:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH11B")]=True
    show expression "img/EVN_CH11B@2x.jpg" as bg0 zorder 100 with dissolve
label NCH08A_IF_END4:
#ROUTINE_STA
#BG_ALP_AUTOC 1,0,0,1
#BG_ALP_AUTOC 2,0,0,1
#BG_ALP_AUTOC 3,0,0,1
#ROUTINE_STP
#ROUTINE_STA
    hide bg2 with dissolve
#BG_ERSWC 1,3
#EFF_PRI 0
#BG_ALPC 1
#BG_ALPC 3
#BG_PRI 1
#BG_PRI 0
#ROUTINE_STP
    window hide
#MUS_VOL 255
#BG_SET_BACK 
    "这一定是个，微不足道的故事。"
    "这个世界上，有几十亿的人，有几十亿个故事——我和智纱的故事，一定只是这些故事中，被埋没的，很平凡的一个吧。"
    "就算是那样，我和智纱就在这里，把我们已经走过的『至今为止』，和还未见到的『从今以后』，放在心中——。"
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
#MOV_PLY 2
##SETACHIEVE 27
#RSET S101
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_QUA_WIN
#TH_QUAKE_WIN 4
#EOT
#label THREAD_BIKKURI
#BG_UV_AUTOC 0,0,0,640,448,1,F123,24
#CHR_ALP_AUTOC 1,128,1,F123,24
#CHR_POS_AUTOC 1,(320-160),0,1,F123,24
#CHR_SCL_AUTOC 1,256,256,1,F123,24
#CHR_POS_AUTOC 0,(320+96),0,1,F123,24
#CHR_SCL_AUTOC 0,256,256,1,F123,24
#BG_UV_SAVEC 0
#CHR_ALP_SAVEC 1
#CHR_POS_SAVEC 1
#CHR_SCL_SAVEC 1
#CHR_POS_SAVEC 0
#CHR_SCL_SAVEC 0
#EOT
#label THREAD_YAKISOBA
#BG_UV_AUTOC 0,0,((448/16)*3),(640/2),(448/2),1,F123,48
#BG_UV_SAVEC 0
#EOT
#label THREAD_RINGOAME
#BG_ALP_AUTOC 1,128,1,F123
#BG_POS_AUTOC 1,0,130,,F123
#BG_ALP_SAVEC 1
#BG_POS_SAVEC 1
#EOT
#label THREAD_CHISA_PAN
#BG_UV_AUTOC 1,((640/10)*3),(448-((448/8)*5)),((640/8)*5),((448/8)*5),1,F123
#BG_UV_SAVEC 1
#EOT
#label TH_YUSURU
#TH_QUAKE_WIN 4
#EOT
#label THREAD_FIREWORKS1
#BG_ALP_AUTOC 1,128,1,F123
#BG_ALP_AUTOC 1,0,1,F123,48
#EOT
#LABEL THREAD_FIREWORKS2
#BG_ALP_AUTOC 3,128,1,F123
#BG_ALP_AUTOC 3,0,1,F123,48
#EOT