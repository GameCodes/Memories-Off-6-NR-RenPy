label NSU17A:
    $currentlabel = "NSU17A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '30'
    $date = '0'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG63EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG63EA@2x.jpg" as bg0 with dissolve
    play sound "SE05_13L"
    pause (32/32.0)
#FADE_IN 1
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
    voice "NSU17A_XU000_K"
    電話 "「您拨打的电话现在已关机或不在服务区」"
    "咦？奇怪啊……"
    "或许是在骑车吧，又或是还在生气因此关了机，我这样想着回到了房间。"
    "只是因为长时间联系不上，我又开始担心起来。"
    play sound "SE07_02"
    志雄 "「不会出什么事了吧……？」"
    "之前在焰火大会上联系不上她时自己也是非常焦急，幸好平安无事。"
    志雄 "「这次也是自己太多虑了……吧？」"
    window hide
#BG_SET_BACK 
#FADE_OUT 1
#BG_INIC 1
    show expression "img/NIMG01C@2x.png" as bg1 zorder 1
    show expression "img/NIMG01C@2x.png" as bg_over zorder 2
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
#FADE_IN 1
    "向窗外望去，天色已经开始黑了。"
    "如此算来，铃和我分开已经好几个小时了。"
    window hide
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    stop sound
    hide bg1 with dissolve
#FADE_IN 1
    play sound "SE07_02"
    play music "OBGM13"
    "不管怎么说都已经很晚了。"
    "不会真的发生什么事了吧？会不会骑摩托车滑倒了，会不会中暑了呢……"
    "越这么考虑，脑子里想到的越是糟糕的事态。"
    志雄 "「还是去找她吧」"
    "是自己想太多的话，也就算了。不如说是自己多虑的话更好。"
    window hide
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
#BG_ALPC 1,128
#BG_PRI 0
#BG_PRI 1
    scene expression "img/BG62EA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA01"),"True","img/SN_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "从屋子里飞奔出来的时候，刚好稻穗向这个方向走过来。"
    志雄 "「稻穗！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA01"),"True","img/SN_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU17A_SN000"
    信 "「诶？塚本君，温泉的更衣室，我已经打开了」"
    志雄 "「先不说这个，铃那边联系你了吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA04"),"True","img/SN_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU17A_SN001"
    信 "「老姐吗？没有特意联系我，怎么了？」"
    志雄 "「从刚才开始，就完全联系不上她」"
    voice "NSU17A_SN002"
    信 "「是不是手机没电了，或是山里收不到信号呢？」"
    "一般情况下是会这么认为。只是……"
    志雄 "「联系不上已经有很长时间了吧？难道，出了什么事！」"
    "说着说着，又开始担心起来。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA05"),"True","img/SN_LBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU17A_SN003"
    信 "「塚本君，先冷静下来」"
    志雄 "「但是……」"
    voice "NSU17A_SN004"
    信 "「如果出了事故的话，我想会有人来联系的。依我看，我先去附近的急救中心或是警察局问问看吧」"
    志雄 "「那我该做些什么呢……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBB01"),"True","img/SN_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU17A_SN005"
    信 "「你就在这里耐心等消息吧，万一老姐突然回来了呢」"
    "的确是往不好的方向想多了……"
    "可就是有种让人心绪不宁的预感。"
    志雄 "「……我还是，去找找看吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBB02"),"True","img/SN_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU17A_SN006"
    信 "「说到找的话该去哪呢。有目标吗？」"
    志雄 "「还不清楚，或许在山里吧……」"
    "既然吵架的原因是在山路上骑摩托车，或许是在开往山里的路上摔倒了……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA01"),"True","img/SN_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU17A_SN007"
    信 "「明白了。万一有人联系这里，我就在这里等消息吧」"
    志雄 "「那就拜托了」"
    voice "NSU17A_SN008"
    信 "「没什么，再怎么说也是我老姐啊」"
    志雄 "「那我就……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA05"),"True","img/SN_LBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU17A_SN009"
    信 "「等一下！」"
    "就在我走向玄关的时候，稻穗突然叫住了我。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA01"),"True","img/SN_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU17A_SN010"
    信 "「旅馆的后面有自行车，骑那个去吧」"
    志雄 "「可以吗？」"
    voice "NSU17A_SN011"
    信 "「今天已经用不到了。另外，你再稍微冷静一点。塚本君要是出什么事的话，就真的是全军覆没了」"
    志雄 "「知道了！感激不尽」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "向稻穗君道谢后，我便急切地向旅馆后面走去。"
    window hide
#SE_VOLC 1,64
#BG_SET_BACK 
#BG_INIC 1
    show expression Solid("000") as bg1 with ImageDissolve("img/BG_MASK18@2x.png",1)
    show expression "img/BG60EA@2x.jpg" as bg0 zorder 0 with dissolve
    hide bg1 with dissolve
    "自行车……在那！"
    "绕到了后面，发现有辆充满怀旧感的女士自行车。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG67NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG67NA@2x.jpg" as bg0 with dissolve
    play sound "SE05_17L"
    pause (32/32.0)
    play sound "SE06_43L"
#FADE_IN 1
#SE_VOLC 1,64
    志雄 "「哈啊啊啊啊啊！」"
    "不要说电动助力了，就连变速器也没有。我就这样骑着自行车上了山路。"
    "四周已经一片漆黑了，只有孤零零的街道还亮着光。"
    志雄 "「呼、呼……」"
    "艰难地攀登着上午铃经过的道路。"
    "坡道虽说不是很陡，可一直这么骑很快就会气喘吁吁。"
    "即使如此，我依然片刻不停歇地赶路。"
    "可就是看不到铃的身影，摩托车的引擎声也听不到……"
    if F4>=6:
        jump L_NSU17A_BRA00_A
#IF F21>=6, GOTO L_NSU17A_BRA00_A
    jump L_NSU17A_BRA00_B
label L_NSU17A_BRA00_A:
    $F108=1
    window hide
    stop se fadeout 1
    stop sound
    stop music fadeout 1
    show expression "img/BG66NA@2x.jpg" as bg_over zorder 2 with dissolve
    play sound "SE06_26"
    pause (32/32.0)
    play sound "SE07_02"
    志雄 "「！？」"
#THREAD_STA 1,THREAD_QUA_WIN
#THREAD_WAT 1
#WIN_POS 0,0
#MESX "%K%P"
    "心跳开始加快。"
    stop se
    "感觉能听到到救护车的声音从山顶上传来。"
    "什么也没有，不是这样的！虽然在心里如此呼喊着，不妙的感觉却在心中扩大……"
    志雄 "「该死！」"
    window hide
    play sound "SE06_43L"
    "像是要甩去这个消极的念头一般，我用力向前骑行。"
    window hide
    show expression "img/EVN_SU02B@2x.jpg" as bg_over zorder 100
    with dissolve
    pause 1
    hide bg_over
    with dissolve
#BG_SET_BACK 
#BG_INIC 1
#BG_INIC 2
#BG_ALPC 1
#BG_COLC 2,160,160,160
#BG_SETWC 1,2,FT_KAI1,EVN_SU02B
#SE_VOLC 0,0,16
#FADE_OUT 1,8,COL_WHITE
#BG_COLC 2,128,128,128,128
#BG_ALPC 0
#BG_ALPC 1
#BG_ALPC 2,128
#FADE_IN 1
#FADE_OUT 1,8,COL_WHITE
#BG_ERSWC 1,2,BG_NOFADE
#BG_COLC 2,128,128,128,128
#BG_ALPC 0,128
#SE_VOLC 0,255,16
#FADE_IN 1
    "我们还在吵架。"
    window hide
    show expression "img/EVN_SU04E@2x.jpg" as bg_over zorder 100
    with dissolve
    pause 1
    hide bg_over
    with dissolve
#BG_SET_BACK 
#BG_INIC 1
#BG_INIC 2
#BG_ALPC 1
#BG_COLC 2,160,160,160
#BG_SETWC 1,2,FT_KAI1,EVN_SU04E
#SE_VOLC 0,0,16
#FADE_OUT 1,8,COL_WHITE
#BG_COLC 2,128,128,128,128
#BG_ALPC 0
#BG_ALPC 1
#BG_ALPC 2,128
#FADE_IN 1
#FADE_OUT 1,8,COL_WHITE
#BG_ERSWC 1,2,BG_NOFADE
#BG_COLC 2,128,128,128,128
#BG_ALPC 0,128
#SE_VOLC 0,255,16
#FADE_IN 1
    "还有想说的话要告诉她！"
    window hide
    show expression "img/EVN_SU08A@2x.jpg" as bg_over zorder 100
    with dissolve
    pause 1
    hide bg_over
    with dissolve
#BG_SET_BACK 
#BG_INIC 1
#BG_INIC 2
#BG_ALPC 1
#BG_COLC 2,192,192,192
#BG_SETWC 1,2,FT_KAI1,EVN_SU08A
#SE_VOLC 0,0,16
#FADE_OUT 1,8,COL_WHITE
#BG_COLC 2,128,128,128,128
#BG_ALPC 0
#BG_ALPC 1
#BG_ALPC 2,128
#FADE_IN 1
#FADE_OUT 1,8,COL_WHITE
#BG_ERSWC 1,2,BG_NOFADE
#BG_COLC 2,128,128,128,128
#BG_ALPC 0,128
#SE_VOLC 0,255,16
#FADE_IN 1
    "所以！"
    "拼命地骑着，不知不觉进入视线不太好的弯道上。"
    志雄 "「！！」"
    "正当拐弯的时候，在昏暗的灯光下照射下，突然有什么东西闯入我的眼帘。"
    play sound "SE06_27"
    志雄 "「喂！？」"
    voice "NSU17A_SU000"
    铃 "「哎 ！」"
    window hide
    play sound "SE06_28"
#VIB_DOKA 
#QUA_ALL 
#VIB_STP 
    "为了要避开突然出现的紧急状况，我急刹车了一下，结果因为后轮打滑摔了下去。"
    "但是，刚才看见的是……！"
    志雄 "「铃！？」"
    window hide
    play sound "SE03_90"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SCA03"),"True","img/SU_SCA03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU17A_SU001"
    铃 "「志、志雄！？」"
    window hide
    play music "OBGM10"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA03"),"True","img/SU_LCA03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    "在昏暗的灯光中，是推着摩托车的铃。"
    志雄 "「铃！没事吧！？受伤了吗？」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA02"),"True","img/SU_LCA02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU17A_SU002"
    铃 "「诶？啊，没事没事，什么事都没有。倒是志雄你，不要紧吧？」"
    "太好了……"
    志雄 "「比起我的问题，你到底怎么了啊？」"
    voice "NSU17A_SU003"
    铃 "「并没有翻车。只是，引擎发动不了了」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA05"),"True","img/SU_LCA05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU17A_SU004"
    铃 "「我还在想是不是该去做车检了，就变成这副样子了」"
    志雄 "「咳……算了，要是联系过我就好了」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC04"),"True","img/SU_LCC04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU17A_SU005"
    铃 "「忘记给手机充电，电池没电了。真是祸不单行啊」"
    志雄 "「原来如此。不过……真的很担心你是不是出事了呢……」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC02"),"True","img/SU_LCC02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU17A_SU006"
    铃 "「志雄……对不起。让你担心了」"
    志雄 "「嗯。不过，没事就好……没事就好……」"
    jump L_NSU17A_BRA00_X
label L_NSU17A_BRA00_B:
    $F108=0
    window hide
    stop se fadeout 1
    show expression "img/BG66NA@2x.jpg" as bg_over zorder 2 with dissolve
    志雄 "「不在吗……」"
    "好不容易到了上午休息的地方，却找不到铃。"
    window hide
    stop music fadeout 1
    play sound "SE02_00L"
    志雄 "「！」"
    "从稻穗那边？不会是……"
    window hide
    play sound "SE02_03"
    志雄 "「喂！铃吗！？」"
    voice "NSU17A_SN012"
    信 "「啊～，冷静一下。老姐刚刚回来了」"
    志雄 "「真的吗！？太好了……」"
    voice "NSU17A_SN013"
    信 "「摩托车出了故障所以推了回来，再加上手机又没电了。真是让人担心啊」"
    志雄 "「故障？没出什么事吧？没受伤吧？」"
    voice "NSU17A_SN014"
    信 "「放心放心，毫发无伤」"
    志雄 "「铃在那里吗？」"
    voice "NSU17A_SN015"
    信 "「没有，说是累了就休息了。不过，推着那么大的摩托车累了也很正常」"
    志雄 "「联系我一下也好啊……」"
    voice "NSU17A_SN016"
    信 "「老姐那家伙啊，好像很低落的样子啊。似乎也觉得是自己对塚本君太过分了，不太好找她说话。现在，大概在想着该怎么道歉才好吧」"
    志雄 "「这样啊。不过没事就好」"
    voice "NSU17A_SN017"
    信 "「嗯。塚本君也快点回来吧」"
    志雄 "「嗯」"
    "结果，是我白操心啊。"
    "不过，铃什么事都没有，实在是太好了。"
    jump L_NSU17A_BRA00_X
label L_NSU17A_BRA00_X:
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
#label THREAD_QUA_WIN
#TH_QUAKE_WIN 4
#EOT