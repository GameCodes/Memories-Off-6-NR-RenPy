label NSU19A:
    $currentlabel = "NSU19A"
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
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09C")]=True
    show expression "img/EVN_SU09C@2x.jpg" as bg0 zorder 0 with dissolve
    play sound "SE05_17L"
    pause (32/32.0)
#EFF_STAC 0,YUGE,EFF_SKIP
#FADE_IN 1
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
#SE_VOLC 1,(64/2)
    志雄 "「差不多该上去了吧？」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09B")]=True
    show expression "img/EVN_SU09B@2x.jpg" as bg0 with dissolve
    voice "NSU19A_SU000"
    铃 "「是啊～，在这里待久了说不定会头晕的」"
    志雄 "「那……」"
    voice "NSU19A_SU001"
    铃 "「志雄，闭上眼睛」"
    "嗯，是这样啊。不可能突然发展到这一步的。"
    志雄 "「知道了」"
    window hide
    play sound "SE03_87"
#SE_VOLC 1,128
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#FADE_IN 0
#SE_WATC 0
    志雄 "「铃，好了吗？」"
    "再次闭上眼睛，等着铃先上去。"
    voice "NSU19A_SU002"
    铃 "「ＯＫ，已经可以睁开眼睛了」"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
    scene expression "img/BG99NA@2x.jpg" as bg0 with dissolve
#EFF_STAC 0,YUGE,EFF_SKIP
#SE_VOLC 1,64
#FADE_IN 1
    志雄 "「那我也上去了」"
    "泡久了似乎真的很难受。一进更衣室，我便赶快用从铃那里拿来的毛巾擦拭身体，穿上衣服。"
    window hide
#SE_VOLC 1,128
    stop music fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG67NA@2x.jpg" as bg0 zorder 0 with dissolve
#FADE_IN 0
    志雄 "「换好衣服了吗？」"
    voice "NSU19A_SU003"
    铃 "「抱、抱歉。还没呢……为什么男生换衣服这么快呢？」"
    "或许是因为本身穿的、戴的东西就比较少吧。"
    "想尽快把头发弄干，我拿起了这里预备的吹风机。"
    "就在这时，从更衣室外传来了自言自语的声音。"
    voice "NSU19A_SN000"
    信 "「哎呀，该怎么办才好。又联系不上，是不是该关门了呢？」"
    voice "NSU19A_SN001"
    信 "「本来想让他们吃一惊的，也不知道怎么样了……」"
    "这个声音是稻穗吧 ……？"
    "啊不妙，忘记告诉稻穗已经找到铃的事了……"
    voice "NSU19A_SN002"
    信 "「哎，今天就到这吧」"
    voice "NSU19A_SU004"
    铃 "「嘿～吃一惊说的是啥～？」"
    window hide
    play music "OBGM13"
    "不妙，刚想到这，铃低沉吓人的声音已经响了起来。"
    "快跑啊！稻穗你快跑啊！"
    voice "NSU19A_SN003"
    信 "「诶，这个声音！？怎么回事！塚本君在吗！？都没联系一下，喂！」"
    志雄 "「对不起！我忘记了！」"
    "我慌张地向外喊道……好像已经晚了。"
    voice "NSU19A_SN004"
    信 "「塚本君……，这也太过分了」"
    voice "NSU19A_SU005"
    铃 "「能拿别人的吵架来开玩笑，也只有你这家伙说得出来！」"
    voice "NSU19A_SN005"
    信 "「呵呵，对于胆小的你倒是剂良药呢！」"
    "明明停手就可以了啊，你还要调拨她……"
    voice "NSU19A_SU006"
    铃 "「真是多管闲事啊！」"
    window hide
    play sound "SE00_33"
    "铃好像已经跑到屋外去了，我也慌慌张张地跟在后面。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
    scene expression "img/BG67NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320)
#CHR_POSC 1,(320-96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SBC03"),"True","img/SU_SBC03A@2x.png") as lh0 zorder (10-0):
        xcenter .5
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_SBA04"),"True","img/SN_SBA04A@2x.png") as lh1 zorder (10-1):
        xcenter (320-96)/640.0
        ypos 0.0

#SE_VOLC 1,64
#FADE_IN 1
#MESA A_CH_SN,NSU19A_SN006A,"【信】「哇！已经出来了！"
#VO_WAT VO_WAIT_START
    voice "NSU19A_SN006A"
    信 "「哇！已经出来了！{w=4}{nw}"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_SBA02"),"True","img/SN_SBA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    voice "NSU19A_SN006B"
    extend "……噢，那不是我的流星号吗！」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_SBA02"),"True","img/SN_SBA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter (320-96)/640.0
        parallel:
            linear 1 alpha 0
        parallel:
            linear 1 xcenter 1.0
#MOV_CHR_INIT 16
#MOV_CHR0 ,(320-96)
#MOV_CHR1 0,640
#MOV_CHR_GO 1
    hide lh1 with dissolve
#CHR_ALPC 1,128
    "稻穗君轻轻躲开铃的手，骑上我来时骑的女士自行车逃跑了。"
    voice "NSU19A_SU007"
    铃 "「啊，站住！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,(320-96)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SBA05"),"True","img/SU_SBA05A@2x.png") as lh0 zorder (10-11):
        ypos 0.0
        linear 1 xcenter (320-96)/640.0
        pause 1
        parallel:
            linear 1 alpha 0
        parallel:
            linear 1 xcenter 1.0
#MOV_CHR_INIT 16
#MOV_CHR0 0,(320)
#MOV_CHR1 128,(320)
#MOV_CHR_GO 1
    hide lh0 with dissolve
#CHR_ALPC 0,128
    "铃也骑起了摩托车，想要追过去，愤怒声很快变成了后悔声。"
    voice "NSU19A_SU008"
    铃 "「啊，引擎已经坏了！」"
    window hide
    play sound "SE06_12"
    play sound "SE06_13L"
    "但是，铃还是按下启动开关，结果引擎一下子发动了。"
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SBC03"),"True","img/SU_SBC03A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NSU19A_SU009"
    铃 "「全力一击！　好！」"
    "全、全力一击？"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC01"),"True","img/SU_LCC01A@2x.png") as lh10 zorder 100:
        ypos 0.0
    with dissolve
    "很快便将东西收拾好的铃，突然望向我这边。"
    "那个眼神，像是在问我要乘吗。"
    志雄 "「当然！」"
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
    "边回答边跑向摩托车，突然铃伸出左手，揪住我的前襟。"
    window hide
#SE_VOLC 0,64
#BG_SET_BACK 
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU10D")]=True
    show expression "img/EVN_SU10D@2x.jpg" as bg1 with dissolve
    play music "BGM13"
    志雄 "「诶？」"
    "就这样，我的脸被拉到铃面前……"
#THREAD_STA 1,THREAD_NEAR
#MES "就这样，我的脸被拉到铃面前……"
#THREAD_WAT 1
#MESX "%K%P"
    "……"
    "…………"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU10B")]=True
    show expression "img/EVN_SU10B@2x.jpg" as bg1 with dissolve
    "………………？"
    voice "NSU19A_SU010"
    铃 "「…………」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU10C")]=True
    show expression "img/EVN_SU10C@2x.jpg" as bg1 with dissolve
    "就在我的脸贴到面前的时候，铃的气势却突然消失了，我们一下子变成了近距离的对视。"
    "铃的脸色突然变得通红，将视线移向其它地方。"
    志雄 "「铃……？」"
#THREAD_STA 1,THREAD_FAR
    voice "NSU19A_SU011"
    铃 "「嗯，果然……稍等一下……」{w=3}{nw}"
#THREAD_WAT 1
#MESX "%K%P"
    "……真没办法啊。"
    window hide
#BG_UV_AUTOC 1,(640/8),,((640/4)*3),((448/4)*3),1,F24,48
#BG_UV_SAVEC 1
#SE_VOLC 0,0
#SE_VOLC 1,0
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU10A")]=True
    show expression "img/EVN_SU10A@2x.jpg" as bg1 with dissolve
    voice "NSU19A_SU012"
    铃 "「嗯……」"
#MESEX_A M_NOA,A_CH_SU,NSU19A_SU012,"【鈴】「嗯……」%K%P"
    window hide
#BG_UV_AUTOC 1,0,0,640,448,1,F24
#BG_UV_SAVEC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU10B")]=True
    show expression "img/EVN_SU10B@2x.jpg" as bg1 with dissolve
    voice "NSU19A_SU013"
    铃 "「志雄……」"
    "铃的脸颊更红了，眼睛也有些湿润。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU10D")]=True
    show expression "img/EVN_SU10D@2x.jpg" as bg1 with dissolve
#THREAD_STA 1,THREAD_NEAR
    "就这样凝视着，再一次……"
#MES "就这样凝视着，再一次……"
#THREAD_WAT 1
#MESX "%K%P"
    window hide
#SE_VOLC 0,255
#SE_VOLC 1,64
#BG_UVC 0,0,512,640,448
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XCA01"),"True","img/SU_XCA01A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    hide bg1
    with dissolve
    "就在我这样想着的时候，铃好像想到了什么似的，突然提高了声音。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XCA03"),"True","img/SU_XCA03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU19A_SU014"
    铃 "「啊！快点上来，别让那家伙逃了！」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "或许是为了掩饰害羞，铃慌张地戴上了头盔。"
    "看到这些，我苦笑着也坐上了后面的座位。"
    "只是忘记了必须说要说的话。"
    window hide
    stop sound
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/NIMG01D2@2x.png" as bg1 with dissolve
#SE_WATC 1
    play sound "SE06_44"
    志雄 "「铃！」"
    "摩托车的引擎发动了起来，我用超过了它的高声喊着。"
    voice "NSU19A_SU015"
    铃 "「什么！？」"
    志雄 "「忘记说了！」"
    voice "NSU19A_SU016"
    铃 "「说什么！？」"
    志雄 "「我喜欢和铃一起骑摩托车！」"
    志雄 "「而且……我也超喜欢铃！」"
    voice "NSU19A_SU017"
    铃 "「谢、谢谢」"
    "铃的脸上，那孩子般的天真无邪的笑容迅速荡漾开来。"
    voice "NSU19A_SU018"
    铃 "「志雄，那我们出发吧！」"
    志雄 "「ＯＫ！」"
    window hide
#BG_INIC 3
#ROUTINE_STA
#BG_POSC 3,30,-60,749,450
    scene expression "img/EVC_SU02B1@2x.png" as bg3:
        block:
            align (.5,.5)
            parallel:
                linear 0.03 xalign 0.53
            parallel:
                linear 0.03 yalign 0.53
            repeat
    show expression "img/Motor_GH_BG@2x.png" as motor_eff_bg zorder -10
    show expression im.Scale("img/Motor_GH_Wood1@2x.png",1136,263) as motor_eff_up zorder -6 at motor_eff_movein:
        yalign 1.0
    show expression im.Scale("img/Motor_GH_Wood1@2x.png",1136,263) as motor_eff_up2 zorder -6 at motor_eff_moveout:
        yalign 1.0
    show expression "img/Motor_GH_Wood2@2x.png" at motor_eff_moveout as motor_eff_down zorder -5:
        yalign 1.0
    show expression "img/Motor_GH_Wood3@2x.png" at motor_eff_movein as motor_eff_down2 zorder -5:
        yalign 1.0
    with dissolve
#EFF_PRI 0
#EFF_STAC 0,MOTOR_RIDE_GH,EFF_NOSKIP
#ROUTINE_STP
    hide bg1 with dissolve
    play sound "SE06_14L"
    "昏暗的灯光中，在平时走起来很可怕的山道上，铃的摩托车平稳地行驶着。"
    "并不是那些飚车手所追求的极限，而是非常从容地行驶着，连我这个外行也感觉的到。"
    "铃和摩托车，还有我……从来没有过的一体感……"
    window hide
    show expression "img/EVC_SU02B2@2x.png" as bg3 with dissolve
    voice "NSU19A_SU019"
    铃 "「志雄。下次再一起骑摩托车吧」"
    "原以为会被风和引擎掩盖住的微小的声音，却能很清楚听到。"
    志雄 "「当然了 ！」"
    "回答的同时，我做了一个决定。"
    "没错。下次，和铃一起骑摩托车……！"
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
#MOV_PLY 4
#BG_FLG EVN_SU12A
#RSET S101
#FADE_OUT 0
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_NEAR
#BG_UV_AUTOC 1,(640/16),,((640/8)*7),((448/8)*7),1,F123
#BG_UV_SAVEC 1
#EOT
#label THREAD_FAR
#BG_UV_AUTOC 1,0,0,640,448,1,F123,48
#BG_UV_SAVEC 1
#EOT