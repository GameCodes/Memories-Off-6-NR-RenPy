label NCH07A:
    $currentlabel = "NCH07A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '29'
    $date = '6'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    
#FADE_IN 0
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    play sound "SE03_85"
    voice "NCH07A_CH000"
    智纱？ "「……雄君……君……」"
#TH_QUA1_WIN
#MESA A_CH_CH,NCH07A_CH000,"【智紗？】「……雄君……君……」"
#THREAD_WAT 1
#WIN_POS 0,0
#MESX "%K%P"
    stop se
    play sound "SE03_85"
#TH_QUA1_WIN=
    voice "NCH07A_CH001"
    智纱 "「志雄……起来……」{w=3}{nw}"
#THREAD_WAT 1
#WIN_POS 0,0
#MESX "%K%P"
    stop se
    志雄 "「呜呜……嗯」"
    play sound "SE03_85"
#TH_QUA1_WIN
    voice "NCH07A_CH002"
    智纱 "「志雄君，起来吧。已经是早上了」{w=3}{nw}"
#THREAD_WAT 1
#WIN_POS 0,0
#MESX "%K%P"
    stop se
    志雄 "「智纱……？」"
    show expression "img/NIMG02A@2x.jpg" as bg0 zorder 0 with dissolve
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128
#    scene expression "img/NIMG02A@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+192)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XQB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XGB01"),"not F103==0","img/CH_XQB01A@2x.png","True","img/CH_XGB01A@2x.png") as lh0 zorder (10+0):
        xcenter .8
        ypos 0.0
    with dissolve
#BG_DSPC_F 0
#FILT_IN 0,0,COL_FOGEYE
    play sound "SE05_14L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,
    "坐了起来。周围是不熟悉的风景。"
    "……这里，是哪？"
    志雄 "「学生会室……也不是呢」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XQB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XGB02"),"not F103==0","img/CH_XQB02A@2x.png","True","img/CH_XGB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#CHR_BLUR 0
    voice "NCH07A_CH003"
    智纱 "「不对，不是的哦」"
    志雄 "「……」"
    window hide
#BG_BLUR 0
#CHR_BLUR 0
#FILT_OUT 96
    "……对了，我想起来了。我是和智纱一起来旅行的。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 6,CAL_0729
#FADE_OUT 1,32,COL_WHITE
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
#BG_BLUR 0
    scene expression "img/BG63MA3@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGA01"),"not F103==0","img/CH_LQA01A@2x.png","True","img/CH_LGA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#SE_VOLC 1,(64/4)
#FADE_IN 1
    play music "BGM03"
    志雄 "「抱歉，我睡迷糊了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGB02"),"not F103==0","img/CH_LQB02A@2x.png","True","img/CH_LGB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "智纱看着这样的我微微一笑。总觉得有些不好意思。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGB01"),"not F103==0","img/CH_LQB01A@2x.png","True","img/CH_LGB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH004"
    智纱 "「差不多该起来了啊。要赶不上吃早饭的时间了」"
    志雄 "「啊……现在是几点？」"
    voice "NCH07A_CH005"
    智纱 "「已经７点半了哦」"
    "食堂的早饭是到8点半。确实是差不多该起了。"
    志雄 "「谢谢你叫我起来」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGB02"),"not F103==0","img/CH_LQB02A@2x.png","True","img/CH_LGB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH006"
    智纱 "「不用谢」"
    "那样简单的一举一动，在哪里都可以听到的平凡话语，感觉还是非常的新鲜。"
    "拉着智纱的手坐起身来。从互相接触的手掌中，传来了智纱的温暖。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGA01"),"not F103==0","img/CH_LQA01A@2x.png","True","img/CH_LGA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH007"
    智纱 "「那，我来收拾被子吧」"
    志雄 "「啊，对不起。我来干吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQA06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGA06"),"not F103==0","img/CH_LQA06A@2x.png","True","img/CH_LGA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH008"
    智纱 "「好啦，我想这样做的」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "智纱干脆利落地叠好被子。"
    "早上，叫我起来。给我叠被子。然后，一起吃早饭……。这样也许是第一次呢。"
#MUS_VOL 0
    "嗯～，这算什么呢……。"
    menu:
        "像新婚妻子一样":
            $F7=0
        "像女仆一样":
            $F7=1
        "像姐姐一样":
            $F7=2
    if F7==0:
        jump L_NCH07A_SEL00_A
    if F7==1:
        jump L_NCH07A_SEL00_B
    if F7==2:
        jump L_NCH07A_SEL00_C
label L_NCH07A_SEL00_A:
    $F1+=1
    "……。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MQA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MGA04"),"not F103==0","img/CH_MQA04A@2x.png","True","img/CH_MGA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCH07A_CH009"
    智纱 "「嗯？　怎么了？」"
    "智纱一副很诧异的表情。"
    window hide
#MUS_VOL 128
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    志雄 "「没、没有、什么事都没有」"
    "我一下子错开了视线。好像无意识之中就盯着她看起来了。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MQA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MGA04"),"not F103==0","img/CH_MQA04A@2x.png","True","img/CH_MGA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCH07A_CH010"
    智纱 "「嗯？　那就好」"
    "……总觉得智纱像新婚的妻子一样，这种话不可能说得出口啊。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NCH07A_CH011"
    智纱 "「唉，嘿，哟」"
    window hide

#BG_SET_BACK 
#BG_INIC 1
#BG_UVC 1,0,(448/4),(640/2),(448/2)

#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,(448/4),(640/2),(448/2)
    show expression "img/BG63MA1@2x.jpg" as bg0 zorder 0 with dissolve
    hide bg1 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XQA05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XGA05"),"not F103==0","img/CH_XQA05A@2x.png","True","img/CH_XGA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「好了」"
    "我从侧面帮着智纱，将那准备放进壁橱的被子抬了起来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XQA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XGA03"),"not F103==0","img/CH_XQA03A@2x.png","True","img/CH_XGA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH012"
    智纱 "「啊……」"
    "在那一瞬间，两人的手碰到了一起。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XQB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XGB02"),"not F103==0","img/CH_XQB02A@2x.png","True","img/CH_XGB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH013"
    智纱 "「啊、啊哈哈……」"
    "我和智纱呆板地笑着，接连用着力，两人一起把被子塞进壁橱里。"
    window hide
#SE_VOLC 1
#ROUTINE_STA
#BG_SET_BACK 
#BG_PRIC 0
#BG_PRIC 3
#CHR_PRIC 0
#EFF_PRI 0
#EFF_PRI 1
#BG_INIC 3
    scene expression "img/NIMG01A@2x.png" as bg1 zorder 1
    show expression "img/CloudA1@2x.png" as cloud0 zorder 5:
        yalign 1.0
        xcenter .75
        linear 100 xcenter .0
    show expression "img/CloudA2_0@2x.png" as cloud2 zorder 8:
        yalign .0
        block:
            xcenter 1.0
            linear 140 xcenter .0
            repeat
    show expression "img/CloudA2_1@2x.png" as cloud3 zorder 8:
        ycenter .2
        block:
            xcenter 1.0
            linear 100 xcenter .0
            repeat
    show expression "img/CloudA2_2@2x.png" as cloud4 zorder 8:
        yalign .0
        block:
            xcenter 1.0
            linear 120 xcenter .0
            repeat
    show expression "img/CloudA3_3@2x.png" as cloud8 zorder 10:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.5
            linear 50 xpos .0
            xpos 1.0
            linear 50 xpos .5
            repeat
    show expression "img/CloudA3_0@2x.png" as cloud5 zorder 10:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.8
            linear 80 xpos .0
            xpos 1.0
            linear 20 xpos .8
            repeat
    show expression "img/CloudA3_1@2x.png" as cloud6 zorder 12:
        xanchor 1.0
        yalign 1.0
        block:
            xpos .6
            linear 78 xpos .0
            xpos 1.0
            linear 52 xpos .6
            repeat
    show expression "img/CloudA3_2@2x.png" as cloud7 zorder 15:
        xanchor .0
        yalign 1.0
        block:
            xpos 0.2
            linear 20 xpos .0
            xpos 1.0
            linear 100 xpos .2
            repeat
    with dissolve
#EFF_STAC 0,CLOUD_A,EFF_NOSKIP
#ROUTINE_STP
#ROUTINE_STA
#BG_ALP_AUTOC 0,0,0,1
#CHR_ALP_AUTOC 0,0,0,1
#EFF_STAC 1,LENZ,EFF_NOSKIP
#ROUTINE_STP
    "眼睛转到了窗户那边。外面的天空一片晴朗。"
    window hide
#BG_UVC 0,0,0,640,448
#SE_VOLC 1,(64/4)
#ROUTINE_STA
#BG_ALP_AUTOC 0,128,0,1
#CHR_ALP_AUTOC 0,128,0,1
#ROUTINE_STP
#ROUTINE_STA
#EFF_STPC 0,EFF_NOSKIP
#EFF_STPC 1,EFF_NOSKIP
#EFF_PRI 0
#EFF_PRI 1
    hide bg3 with dissolve
#BG_PRIC 3
#ROUTINE_STP
#BG_PRIC 0
#CHR_PRIC 0
#BG_BLUR 0
#SE_VOLC 1,(64/4)
    jump L_NCH07A_SEL00_X
label L_NCH07A_SEL00_B:
    "总觉得智纱，好像女仆一样啊……。"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
    show expression "img/NIMG13A@2x.jpg" as bg2 zorder 2 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB01"),"not F103==0","img/CH_LLB01A@2x.png","True","img/CH_LBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#SE_VOLC 1,0
#MUS_VOL 0
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 2
#CHR_ALPC 1
#BG_PRI 2
#CHR_PRIC 1
    hide bg1 with dissolve
    voice "NCH07A_CH014_K"
    智纱 "「早上好，主人」"
    window hide
    play sound "SE07_19"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB02"),"not F103==0","img/CH_LLB02A@2x.png","True","img/CH_LBB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    pause (64/32.0)
    "这样的感觉……。"
    "不对不对！　我在想什么啊！？"
    play sound "SE07_19"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA06"),"not F103==0","img/CH_LLA06A@2x.png","True","img/CH_LBA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    "确实，智纱在照顾着我的日常生活，我总觉得，她穿女仆装会很合适但是！"
    window hide
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,(640/4),((448/4)+512),(640/2),(448/2)
    scene expression "img/BG63MA1@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_SCLC 0,512,512
#CHR_POSC 0,(448/4)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XQA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XGA03"),"not F103==0","img/CH_XQA03A@2x.png","True","img/CH_XGA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCH07A_CH015"
    智纱 "「怎么了，志雄君！？　怎么抱着头呢！？」"
#REMOVE_REEK_CHR 0
    window hide
    stop se
#SE_VOLC 1,(64/4)
#MUS_VOL 128
#ROUTINE_STA
#BG_ALP_AUTOC 1,0,1,F24,24
#BG_ALP_AUTOC 2,0,1,F24,24
#CHR_ALP_AUTOC 1,0,1,F24,24
#BG_UV_AUTOC 0,0,512,640,448,1,F24,24
#CHR_SCL_AUTOC 0,128,128,1,F24,24
#CHR_POS_AUTOC 0,1,F24,24
#ROUTINE_STP
#BG_ALP_SAVEC 1
#BG_ALP_SAVEC 2
#CHR_ALP_SAVEC 1
#BG_UV_SAVEC 0
#CHR_SCL_SAVEC 0
#CHR_POS_SAVEC 0
#BG_ERSWC 1,2,BG_NOFADE
#ROUTINE_STA
#BG_ALPC 1
#BG_ALPC 2
#BG_PRI 0
#BG_PRI 1
#BG_PRI 2
#ROUTINE_STP
    hide lh1 with dissolve
#CHR_ALPC 1
#CHR_PRIC 0
#CHR_PRIC 1
    志雄 "「啊！？」"
    "好险……可能是环境的变化和天气热的原因吧，我的想法也变得有些奇怪了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XQC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XGC02"),"not F103==0","img/CH_XQC02A@2x.png","True","img/CH_XGC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH016"
    智纱 "「发生什么了吗？」"
    "智纱很不安地向我的脸看过来，好像是真的在担心我。"
    志雄 "「没事，没关系。什么事都没有啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XQC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XGC04"),"not F103==0","img/CH_XQC04A@2x.png","True","img/CH_XGC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH017"
    智纱 "「真的是什么事都没有？」"
    "智纱看上去还是不能接受的样子，但我还是强硬地坚持说「什么事都没有」。"
    "我心中的想法，还是没法对智纱说出口……。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGC02"),"not F103==0","img/CH_LQC02A@2x.png","True","img/CH_LGC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH018"
    智纱 "「那样的话倒还好……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGA01"),"not F103==0","img/CH_LQA01A@2x.png","True","img/CH_LGA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    jump L_NCH07A_SEL00_X
label L_NCH07A_SEL00_C:
    "为我做饭、照顾着我……总觉得智纱，感觉就像姐姐一样。至少，比莉莉丝要强得多。"
    "不对，等等，这么说来，我总是给智纱添麻烦，那我不就是个没用的弟弟吗！？"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
    show expression "img/NIMG13A@2x.jpg" as bg2 zorder 2 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LBA05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LLA05"),"not F103==0","img/CH_LBA05A@2x.png","True","img/CH_LLA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#SE_VOLC 1,0
#MUS_VOL 0
#BG_INIC 1
#BG_PRI 1
    show expression "img/BG_WHITE@2x.jpg" as bg1 with dissolve
#BG_ALPC 0
#BG_ALPC 2
#CHR_ALPC 0
#CHR_ALPC 1
    hide bg1 with dissolve
    voice "NCH07A_CH019_K"
    智纱 "「真是的。这种事情都做不好？　真没办法呢」"
    window hide
    play sound "SE07_20"
#BG_COL_AUTOC 2,160,160,160,F24,12
#BG_COL_SAVEC 2
#BG_COL_AUTOC 2,128,128,128,F24,36
#BG_COL_SAVEC 2
    "可是，那样的智纱……呜，有点讨厌呢。"
    window hide
    scene expression "img/BG63MA1@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGB02"),"not F103==0","img/CH_LQB02A@2x.png","True","img/CH_LGB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    stop se
#BG_INIC 1
#BG_PRI 1
    hide bg2 with dissolve
    hide lh1 with dissolve
#BG_ALPC 0
#BG_UVC 0,0,512,640,448
#CHR_ALPC 0
#SE_VOLC 1,(64/4)
#MUS_VOL 128
    hide bg1 with dissolve
    voice "NCH07A_CH020"
    智纱 "「好了，被子收拾好了」"
    "啊……。在考虑那些事情的时候，智纱早已把我的被子也收拾好了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGA01"),"not F103==0","img/CH_LQA01A@2x.png","True","img/CH_LGA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    jump L_NCH07A_SEL00_X
label L_NCH07A_SEL00_X:
    voice "NCH07A_CH021"
    智纱 "「志雄君，换的衣服我放在这里了」"
    "智纱把叠得整整齐齐的衬衫和牛仔裤递给了我。"
    志雄 "「谢谢」"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
    play sound "SE00_27"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGA04"),"not F103==0","img/CH_LQA04A@2x.png","True","img/CH_LGA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_YG000B"
    雄吾？ "「起来了吗？　我们进来了啊」"
    志雄 "「老爸？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_PRIC 1
#CHR_POSC 1,640
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGA04"),"not F103==0","img/CH_LQA04A@2x.png","True","img/CH_LGA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter 170/640.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter 400/640.0
    with move
    play sound "SE00_47"
#MOV_CHR_INIT 64
#MOV_CHR0 ,(320-150)
#MOV_CHR1 128,(320+180)
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
#CHR_PRIC 1
    play music "BGM12"
    voice "NCH07A_YG001"
    雄吾 "「哦，已经起来了啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGA01"),"not F103==0","img/CH_LQA01A@2x.png","True","img/CH_LGA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「怎么了啊，一大早就过来？　是有什么事吗？」"
    voice "NCH07A_YG002"
    雄吾 "「啊，并没有什么特别的事。就是已经到吃饭的时间了，来看看你们有没有起来而已」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA02"),"True","img/SF_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH07A_YG003"
    雄吾 "「如果还在睡的话，就想是不是要把你打起来。也是作为好久没有过的，和我儿子的身体接触」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGB02"),"not F103==0","img/CH_LQB02A@2x.png","True","img/CH_LGB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「好久没有过的身体接触，为什么要拿把我打起来作为身体接触啊？」"
    "这个老爸啊……。"
    志雄 "「而且，有智纱叫我的，已经好好地起来了啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGA01"),"not F103==0","img/CH_LQA01A@2x.png","True","img/CH_LGA01A@2x.png") as lh0 zorder (12+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH022"
    智纱 "「是的，没问题的！」"
    "智纱挺直了身子，严肃地回答着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA06"),"True","img/SF_MAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH07A_YG004"
    雄吾 "「嗯……」"
    "就像是在比较一般，老爸的视线中我和智纱之间往返移动着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA05"),"True","img/SF_MAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    "然后，抿嘴一笑。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA02"),"True","img/SF_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH07A_YG005"
    雄吾 "「哎呀哎呀，我来叫你起来看来真是不懂风趣了啊。今后志雄的事情，我就全交给智纱吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQA05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGA05"),"not F103==0","img/CH_LQA05A@2x.png","True","img/CH_LGA05A@2x.png") as lh0 zorder (12+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH023"
    智纱 "「是、是！　就请交给我吧，父亲大人！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA06"),"True","img/SF_MAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    "智纱满怀信心地回答着，老爸「嗯嗯」地沉思着，皱起了眉头。"
    window hide
#BG_UV_AUTOC 0,(640/2),0,(640/2),(448/2),1,F24,48
#CHR_SCL_AUTOC 1,512,512,1,F24,48
#CHR_POS_AUTOC 1,248,1,F24,48
#CHR_SCL_AUTOC 0,512,512,1,F24,48
#CHR_POS_DISAP 0,((320-160)-((640/4)*3)),248,1,F24,48
#BG_UV_SAVEC 0
#CHR_SCL_SAVEC 1
#CHR_POS_SAVEC 1
#CHR_SCL_SAVEC 0
#CHR_POS_SAVEC 0
#CHR_ALP_SAVEC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGA04"),"not F103==0","img/CH_LQA04A@2x.png","True","img/CH_LGA04A@2x.png") as lh0 zorder (12+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_YG006A"
    雄吾 "「『父亲大人』吗。{w=4}{nw}"
#MESA A_CH_YG,NCH07A_YG006A,"【雄吾】「『父亲大人』吗。"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA05"),"True","img/SF_MAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH07A_YG006B"
    extend "听起来真不错呢……」"
    voice "NCH07A_KR000"
    香里？ "「你，说什么蠢话呢」"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_SCLC 2,512,512
#CHR_POSC 2,448
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGA04"),"not F103==0","img/CH_LQA04A@2x.png","True","img/CH_LGA04A@2x.png") as lh0 zorder (12+0):
        ypos 0.0
        xcenter .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA05"),"True","img/SF_MAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA02"),"True","img/KR_MAA02A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
        xcenter .9
    with dissolve
#BG_UV_AUTOC 0,0,0,(640),(448),1,F24,48
#CHR_SCL_AUTOC 1,128,128,1,F24,48
#CHR_POS_AUTOC 1,(320+96),0,1,F24,48
#CHR_ALPC 0
#CHR_SCL_AUTOC 0,128,128,1,F24,48
#CHR_POS_AUTOC 0,(320-192),0,1,F24,48
#CHR_ALP_AUTOC 0,128,1,F24,48
#CHR_SCL_AUTOC 2,128,128,1,F24,48
#CHR_POS_AUTOC 2,(320+224),0,1,F24,48
#CHR_ALP_AUTOC 2,128,1,F24,48
#BG_UV_SAVEC 0
#CHR_SCL_SAVEC 1
#CHR_POS_SAVEC 1
#CHR_SCL_SAVEC 0
#CHR_POS_SAVEC 0
#CHR_ALP_SAVEC 0
#CHR_SCL_SAVEC 2
#CHR_POS_SAVEC 2
#CHR_ALP_SAVEC 2
    "不知什么时候，香里阿姨已经站到了老爸的身后。"
#CHR_SCLC 1,256,256
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA03"),"True","img/SF_MAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH07A_YG007"
    雄吾 "「香、香里」"
    voice "NCH07A_YG008"
    雄吾 "「什么傻话，只是在体会一下，智纱将来成了儿媳妇之后的样子」"
#CHR_SCLC 0,256,256
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGA03"),"not F103==0","img/CH_LQA03A@2x.png","True","img/CH_LGA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCH07A_CH024A"
    智纱 "「媳！？　媳、{w=3}{nw}"
#VO_WAT VO_WAIT_START
#REMOVE_REEK_CHR 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGB03"),"not F103==0","img/CH_LQB03A@2x.png","True","img/CH_LGB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH024B"
    extend "媳妇……」"
    "智纱对那句话起了反应，低下了头。但是又马上抬起了头，坚定地注视着老爸和香里阿姨的眼睛。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGA03"),"not F103==0","img/CH_LQA03A@2x.png","True","img/CH_LGA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCH07A_CH025"
    智纱 "「请、请多关照！ 父亲大人、母亲大人！　我，会加油的！」"
#REMOVE_REEK_CHR 0
    window hide
#ROUTINE_STA
#CHR_PRIC ID_ALL
#CHR_SORT 0,1
#ROUTINE_STP
#MOV_CHR_INIT 48
#MOV_CHR0 
#MOV_CHR1 0,((320+96)+640/4)
#MOV_CHR2 0,((320+224)+640/4)
#MOV_FOCUS_BG 512
#MOV_CHR_GO 1
#CHR_ERSWC 1,2
#ROUTINE_STA
#CHR_ALPC 1
#CHR_ALPC 2
#CHR_PRIC ID_ALL
#ROUTINE_STP
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQA05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGA05"),"not F103==0","img/CH_LQA05A@2x.png","True","img/CH_LGA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "然后智纱转向我的方向。"
    "噢噢……总觉得从智纱的眼中，冒出了非常多的热气。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGA01"),"not F103==0","img/CH_LQA01A@2x.png","True","img/CH_LGA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH026"
    智纱 "「来，志雄君。换好衣服刷牙洗脸。这会儿，我会去给你准备手帕和纸巾，还有钱包」"
    志雄 "「哦、哦」"
    "对麻利地开始行动的智纱，感到气势上有些被压倒了。"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2,(320+224)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA02"),"True","img/KR_MAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .9
    with dissolve
    voice "NCH07A_KR001"
    香里 "「呵呵，智纱已经完全是一位妻子了呢」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LQB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LGB02"),"not F103==0","img/CH_LQB02A@2x.png","True","img/CH_LGB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH027"
    智纱 "「是！」"
    "智纱就像是现在开始要去战斗一样，充满了气势地回答道。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "好了，要做些什么来度过今天呢……。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG66AA@2x.jpg" as bg0 zorder 0 with dissolve
#BG_SET_BACK 
#BG_INIC 1
    if F103:
        jump NCH07A_IF_ELSE1
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH07A")]=True
    show expression "img/EVN_CH07A@2x.jpg" as bg1 zorder 1 with dissolve
    jump NCH07A_IF_END1
label NCH07A_IF_ELSE1:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH07B")]=True
    show expression "img/EVN_CH07B@2x.jpg" as bg1 zorder 1 with dissolve
label NCH07A_IF_END1:
#BG_COLC 1,0,0,0
    "…………。"
    "……。"
    window hide
#BG_COLC 1,128,128,128
    scene expression "img/BG66AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_14L"
    play sound "SE01_12L"
    pause (32/32.0)
#FADE_IN 1
    stop se fadeout 1
#SE_VOLC 1
    voice "NCH07A_CH028"
    智纱 "「哇……风好舒服。景色也好棒」"
    "智纱像小孩子一样，很高兴地喧闹着。"
    "现在，我和智纱走在通往湖的山路上。"
    "从稻穗先生那听说，去到湖的路会可以作为一条远足的路线。就算不去游泳，去远足也很令人高兴。"
    voice "NCH07A_CH029"
    智纱 "「快看快看，那边的那个小小的建筑物，不就是我们住的那个旅馆吗？」"
    志雄 "「啊，一定是那样的呢」"
    "从路边的树林的缝隙间，能看到缩微模型一般的，镇上的风景。"
    voice "NCH07A_CH030"
    智纱 "「从山顶上能看到更宽广的景色吧？」"
    window hide
    play sound "SE01_20"

#BG_SET_BACK 
#BG_INIC 2

#EFF_STAC 0,SUNLIGHT_BG66_FRONT,EFF_SKIP
#EFF_STAC 1,SUNLIGHT_BG66_BACK,EFF_SKIP
    hide bg1 with dissolve
    "智纱迈着轻快的脚步，走在了前面。"
    stop se
    "向这边转过身来。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_POSC 0,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_SNB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_SDB01"),"not F103==0","img/CH_SNB01A@2x.png","True","img/CH_SDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH031"
    智纱 "「志雄君不累吗？　如果累了的话……」"
    志雄 "「没事，我不累的」"
    voice "NCH07A_CH032"
    智纱 "「是吗？　如果累了或者感到不舒服了的话，马上要说啊。中暑了的话可就麻烦了」"
    志雄 "「知道了啊。这么说来，智纱你才是，没关系吗？　走得太快了的话，后面就会累了啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_SNB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_SDB02"),"not F103==0","img/CH_SNB02A@2x.png","True","img/CH_SDB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH033"
    智纱 "「没事、没事」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_SNA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_SDA01"),"not F103==0","img/CH_SNA01A@2x.png","True","img/CH_SDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH034"
    智纱 "「先不说这个，有什么事的话，真的别客气，尽管说啊。我会马上去叫人的」"
    "嗯～，对我来说，我倒希望比起担心别人，她还是多担心担心自己吧……。"
    "一开始就走得如此地起劲，会不会在哪里摔倒呢，过会儿一定会很累的吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_SNB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_SDB02"),"not F103==0","img/CH_SNB02A@2x.png","True","img/CH_SDB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH035"
    智纱 "「那就快走吧」"
    志雄 "「啊……」"
    window hide
    play sound "SE01_12L"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_SNB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_SDB01"),"not F103==0","img/CH_SNB01A@2x.png","True","img/CH_SDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "智纱走在前面，我跟在后面……。"
    stop se
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_SNB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_SDB04"),"not F103==0","img/CH_SNB04A@2x.png","True","img/CH_SDB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#CHR_ALP_AUTOC 0,0,1,F123
    voice "NCH07A_CH036"
    智纱 "「哇」{w=3}{nw}"
#MESX "%K%P"
    hide lh0 with dissolve
#CHR_ALPC 0
    play sound "SE07_14"
#THREAD_STA 1,THREAD_HELP_CHISA
    志雄 "「智纱！？」"
#MESA A_CH_SI,"【志雄】「智纱！？」"
#THREAD_WAT 1
#MESX "%K%P"
    hide bg2 with dissolve
#BG_ALPC 2
    "抓住了被地上的石头绊倒的智纱的手，快速地把她拉了起来。"
#CHR_INIC 0
#CHR_PRIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDB03"),"not F103==0","img/CH_LNB03A@2x.png","True","img/CH_LDB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_BLUR 0
    voice "NCH07A_CH037"
    智纱 "「谢、谢谢」"
    志雄 "「不用谢」"
    "智纱很不好意思地笑着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDC01"),"not F103==0","img/CH_LNC01A@2x.png","True","img/CH_LDC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH038"
    智纱 "「那么，就重新打起精神来」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE01_12L"
    "智纱重整好姿势之后，又向前大步走去。"
    志雄 "「真是的。没办法－呢」"
    "对这样的智纱，我只能苦笑。"
    志雄 "「嘛，既然智纱高兴，就没问题……吧」"
    "有那么一点点担心。"
    window hide
    stop se fadeout 1
#SE_VOLC 1,0
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#EFF_STPC 1,EFF_SKIP
    scene expression Solid("000") with fade
    stop se
#BG_SET_BACK 
#BG_INIC 0
#FADE_IN 0
    "…………。"
    "……。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128
    scene expression "img/BG67AA@2x.jpg" as bg0 with dissolve
#SE_VOLC 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDC05"),"not F103==0","img/CH_MNC05A@2x.png","True","img/CH_MDC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .35
    with dissolve
#EFF_STAC 0,SUNLIGHT_BG67_FRONT,EFF_SKIP
#EFF_STAC 1,SUNLIGHT_BG67_BACK,EFF_SKIP
#FADE_IN 1
    voice "NCH07A_CH039"
    智纱 "「哈……」"
    "智纱的话，从大约３０分钟之前开始就变得非常少了。脚步也沉重了起来。"
    "从刚才开始就配合着智纱，特地地把自己的步调放缓。刚才还在我前面的马尾辫，现在已经在我旁边了。"
    志雄 "「智纱，是不是累了呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDC02"),"not F103==0","img/CH_MNC02A@2x.png","True","img/CH_MDC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH040"
    智纱 "「嗯，不，没那回事的」"
    "智纱一个劲地摇着头。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDC05"),"not F103==0","img/CH_MNC05A@2x.png","True","img/CH_MDC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "是刚才闹得太过头了以至于疲劳了吧……但是我还是不好意思这么说啊。"
    menu:
        "背智纱":
            $F7=0
        "在这里休息一下":
            $F7=1
    if F7==0:
        jump L_NCH07A_SEL01_A
    if F7==1:
        jump L_NCH07A_SEL01_B
label L_NCH07A_SEL01_A:
    $F1+=1
    "呜～，老实说是很不好意思，不过智纱好像已经再也走不动了……。"
    志雄 "「让我来背你吧，智纱？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDC04"),"not F103==0","img/CH_MNC04A@2x.png","True","img/CH_MDC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH041"
    智纱 "「哎哎！？　没、没关系！　没关系的啊」"
    志雄 "「啊，可是这么看完全不是没关系啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNC06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDC06"),"not F103==0","img/CH_MNC06A@2x.png","True","img/CH_MDC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH042"
    智纱 "「可是，很、很不好意思……」"
    "确实我也很不好意思，不过总感觉，昨天在咖啡店，智纱还说了『来、啊～』那种更让人不好意思的话……。"
    "喂食就ＯＫ，背着走就不行么。在这方面智纱的标准到底是怎样的呢？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDC02"),"not F103==0","img/CH_MNC02A@2x.png","True","img/CH_MDC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH043"
    智纱 "「而且……会给志雄君添麻烦的啊」"
    "难道比起自己的不好意思，她更在意会不会给我添麻烦的吗。"
    "智纱总是太把我的事情看得太重了……。在这些小事上费心思……。"
    志雄 "「真没办法呢」"
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
    "我在智纱的前面，背对着她蹲了下来。"
    志雄 "「来，我背你走」"
    voice "NCH07A_CH044"
    智纱 "「哎，怎么会这样，太不好意思了吧」"
    志雄 "「不用客气啦。快点，上来」"
    voice "NCH07A_CH045"
    智纱 "「可是……」"
    window hide
#SE_VOLC 1,0
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
#SE_VOLC 1
    play sound "SE01_04L"
#FADE_IN 1
    play music "OBGM06"
    voice "NCH07A_CH046"
    智纱 "「对不起……」"
    "从后背的方向，传来智纱带着歉意的声音。"
    志雄 "「没关系啊。因为是我自己说要背你的啊」"
    "结果，我硬是背着智纱，沿着山路向前走了上去。"
    voice "NCH07A_CH047"
    智纱 "「可是，真的是很对不起」"
    "从刚才开始智纱就一直是这种状态。"
    志雄 "「没有什么要道歉的了。看，在那边能看见一个休息处。在那边先休息一下？」"
    voice "NCH07A_CH048"
    智纱 "「嗯……」"
    "从智纱的嘴里轻轻传来的回答，仿佛会突然消失一般地弱不禁风。"
    window hide
    stop se fadeout 1
#SE_VOLC 1,0
#BG_SET_BACK 
#BG_INIC 1
#EFF_STPC 0,EFF_SKIP
#EFF_STPC 1,EFF_SKIP
    show expression "img/BG77AA1@2x.jpg" as bg0 zorder 0 with dissolve
    stop se
#SE_VOLC 1
    hide bg1 with dissolve
    "运气真好，没走一百米就看到了一个，有小卖部的休息所。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 2
#BG_SETWC 0,2,EXBG07A,EXBG07A
    scene expression "img/EXBG07A@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCC02"),"not F103==0","img/CH_ZMC02A@2x.png","True","img/CH_ZCC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE07_21L"
#BG_BLUR 0
#FADE_IN 1
    voice "NCH07A_CH049"
    智纱 "「真是很抱歉呢。光给你添麻烦」"
    "智纱饱含歉意地，轻声说着。"
    志雄 "「够了……不用在意的啊」"
    jump L_NCH07A_SEL01_X
label L_NCH07A_SEL01_B:
    志雄 "「那就在这边休息一下吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDC02"),"not F103==0","img/CH_MNC02A@2x.png","True","img/CH_MDC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH050"
    智纱 "「可是，志雄君还能继续往前走的吧……？」"
    voice "NCH07A_CH051"
    智纱 "「就是因为我，连志雄君都停了下来啊。没有困扰你吗？」"
    志雄 "「没有那回事啦」"
    "一下子丢开智纱那些无聊的担心。"
    志雄 "「因为登到山顶上并不是目的。重要的是，和智纱在一起就很开心了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDC04"),"not F103==0","img/CH_MNC04A@2x.png","True","img/CH_MDC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH052"
    智纱 "「可是，在这种地方休息，志雄君只会感到很无聊吧……」"
    志雄 "「那些事情，不用在意的」"
    voice "NCH07A_CH053"
    智纱 "「真的……？」"
    志雄 "「那是当然的啦」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDC05"),"not F103==0","img/CH_MNC05A@2x.png","True","img/CH_MDC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH054"
    智纱 "「……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "环视了一下四周。"
    志雄 "「有没有什么可以休息的地方呢」"
    "因为已经完全地进了山里，凳子一样的东西是找不到的。"
    志雄 "「如果带张单子的话就好了啊。现在只能是直接坐在地面上，或者是找块石头坐上了啊」"
    "那，怎么办好呢。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDA01"),"not F103==0","img/CH_MNA01A@2x.png","True","img/CH_MDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCH07A_CH055"
    智纱 "「志雄君，还是算了吧。我，还能走的」"
    "正在寻找休息处的时候，智纱突然那么说了一句。"
    志雄 "「你这是在说什么呢，刚才你不是还走得很辛苦嘛」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDB01"),"not F103==0","img/CH_MNB01A@2x.png","True","img/CH_MDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH056"
    智纱 "「没关系没关系。你看，稍微站在这休息一下，就又能继续走了哦」"
    window hide
    play sound "SE01_20"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "智纱像是要展示自己很有精神似的，面带笑容地开始向前走。"
    "就这么短的时间，不可能消除了疲劳的吧……。"
    志雄 "「不用勉强自己的」"
    window hide
    stop se
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDB02"),"not F103==0","img/CH_MNB02A@2x.png","True","img/CH_MDB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCH07A_CH057"
    智纱 "「勉强什么的，才没有呢」"
    "智纱虽然这样说着，但是很明显，她的脚步很沉重。"
    "既然这样……。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我站到智纱的旁边，握住了她的手。"
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDB03"),"not F103==0","img/CH_LNB03A@2x.png","True","img/CH_LDB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCH07A_CH058"
    智纱 "「啊……」"
    志雄 "「所以至少，让我来支撑着智纱吧」"
    voice "NCH07A_CH059"
    智纱 "「谢谢……」"
    "在路上，智纱提出要把我的手放开，可能她还是有些不好意思。"
    志雄 "「如果我真的觉得你再也走不了了的话，就算强迫我也得让你休息」"
    voice "NCH07A_CH060"
    智纱 "「嗯……」"
    window hide
#SE_VOLC 1,0
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 1
#BG_PRIC 1
#EFF_STPC 0,EFF_SKIP
#EFF_STPC 1,EFF_SKIP
#BG_UVC 0,0,0,640,448
    show expression "img/BG77AA1@2x.jpg" as bg0 zorder 0 with dissolve
    stop se
    stop music fadeout 1
#SE_VOLC 1
#BG_BLUR 0
    hide bg1 with dissolve
#BG_PRIC 1
    "运气真好，没走一百米就看到了一个有小卖部的休息所。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 2
#BG_UVC 0,0,512,640,448
    show expression "img/EXBG07A@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCC02"),"not F103==0","img/CH_ZMC02A@2x.png","True","img/CH_ZCC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_BLUR 0
    play sound "SE07_21L"
#FADE_IN 1
    play music "OBGM06"
    voice "NCH07A_CH061"
    智纱 "「真是很抱歉呢。一次又一次地给你添麻烦」"
    "智纱饱含歉意地轻声说着。"
    "走到这个茶屋的路上，智纱有几次脚下一滑，险些摔倒。虽然我每次都扶住了她……。"
    志雄 "「没事的，那种事情不用在意的」"
    jump L_NCH07A_SEL01_X
label L_NCH07A_SEL01_X:
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCC05"),"not F103==0","img/CH_ZMC05A@2x.png","True","img/CH_ZCC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH062"
    智纱 "「……」"
    "好像是有些在意刚才的事情，智纱看起来有些失落。"
    志雄 "「对了，智纱你肚子不饿吗？」"
    "时间已经到了午饭的时候。登山很花体力的，我也感觉到饿了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCC01"),"not F103==0","img/CH_ZMC01A@2x.png","True","img/CH_ZCC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH063"
    智纱 "「啊，嗯。有点……」"
    志雄 "「那，就去那边的店里买点什么吃的东西吧。三明治或者是饭团什么的，会有卖的吧」"
    志雄 "「智纱就坐在那等着吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCA01"),"not F103==0","img/CH_ZMA01A@2x.png","True","img/CH_ZCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH064"
    智纱 "「啊，那样的话我去买好了！」"
    志雄 "「等等」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCA04"),"not F103==0","img/CH_ZMA04A@2x.png","True","img/CH_ZCA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "智纱急忙站起来要走向小卖部，而我一把抓住她的手。"
    志雄 "「我去买就好。智纱你累了吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCC05"),"not F103==0","img/CH_ZMC05A@2x.png","True","img/CH_ZCC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH065"
    智纱 "「可是……」"
    "智纱有些犹豫地低下了头。"
    志雄 "「那，我去买了啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCC02"),"not F103==0","img/CH_ZMC02A@2x.png","True","img/CH_ZCC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH066"
    智纱 "「……」"
    window hide
#FADE_OUT 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    pause (64/32.0)
#FADE_IN 1
    志雄 "「智纱，午饭买来了啊」"
    "我把混装着小卖部里各种三明治的袋子，放在了桌子上。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCC02"),"not F103==0","img/CH_ZMC02A@2x.png","True","img/CH_ZCC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH067"
    智纱 "「对不起……」"
    志雄 "「智纱你没有什么要道歉的啦」"
    志雄 "「……啊，不好了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCC04"),"not F103==0","img/CH_ZMC04A@2x.png","True","img/CH_ZCC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH068"
    智纱 "「怎么了？」"
    志雄 "「没事，只是想着要是把饮料也一起买来就好了。但是忘了」"
    志雄 "「我去买一点回来」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCA01"),"not F103==0","img/CH_ZMA01A@2x.png","True","img/CH_ZCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH069"
    智纱 "「啊，等等。那个的话！」"
    "智纱一下子露出了快活的笑容。"
    voice "NCH07A_CH070"
    智纱 "「要说饮料的话，我带着呢」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMB05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCB05"),"not F103==0","img/CH_ZMB05A@2x.png","True","img/CH_ZCB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE03_88"
    "这么说着，智纱打开了肩上的背包。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCB02"),"not F103==0","img/CH_ZMB02A@2x.png","True","img/CH_ZCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH071"
    智纱 "「给」"
    "她从包里取出了装了2升茶水的塑料瓶。还有，一袋纸杯。"
    志雄 "「……不是很重的吗，那个？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCB01"),"not F103==0","img/CH_ZMB01A@2x.png","True","img/CH_ZCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH072"
    智纱 "「没事，没什么大不了的」"
    voice "NCH07A_CH073"
    智纱 "「我想着路上可能会没有买饮料的地方，所以就带来了」"
    play sound "SE03_74"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCA01"),"not F103==0","img/CH_ZMA01A@2x.png","True","img/CH_ZCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "智纱取出了纸杯，满脸笑容地，给我倒上了茶水。"
    "智纱消耗了体力的原因之一，不就是这个吗。说起来，2升的水还是真有些重。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCC01"),"not F103==0","img/CH_ZMC01A@2x.png","True","img/CH_ZCC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH074"
    智纱 "「怎么了？　一副这么不高兴的脸」"
    stop se
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCC02"),"not F103==0","img/CH_ZMC02A@2x.png","True","img/CH_ZCC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH075"
    智纱 "「……啊。难道，不要茶，要别的饮料会比较好？」"
    志雄 "「不是，倒不是这回事……」"
    "我只是觉得，告诉我的话，我就会拿着它了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCC04"),"not F103==0","img/CH_ZMC04A@2x.png","True","img/CH_ZCC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH076"
    智纱 "「啊，抱、抱歉，总觉得是自己做了什么让你不高兴的事情了一样……」"
    志雄 "「不不、不是的啊，我并没有在发火啊！」"
    "因为不好的是我啊。"
    志雄 "「……来，吃午饭吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCC05"),"not F103==0","img/CH_ZMC05A@2x.png","True","img/CH_ZCC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH077"
    智纱 "「嗯……」"
    window hide
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
    "对智纱无论怎样都要逞强感到很在意，我的话也变得少了……。"
    "而且智纱好像也很在意着我，没有自己主动开口说话。"
    window hide
#BG_COLC 0,128,128,128
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCC05"),"not F103==0","img/CH_ZMC05A@2x.png","True","img/CH_ZCC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    pause (32/32.0)
#FADE_IN 1
    voice "NCH07A_CH078"
    智纱 "「我吃饱了……」"
    志雄 "「我吃饱了」"
    "在吃午饭的过程中，我们基本没说什么话。"
    "本来觉得这会是更加快乐的远足……为什么会变成这个样子呢？"
    "不好。得想办法，能不能摆脱掉现在的气氛呢……。"
    stop music fadeout 1
    play sound "SE09_29"
    犬２"「汪、汪！」"
    stop se
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCA04"),"not F103==0","img/CH_ZMA04A@2x.png","True","img/CH_ZCA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「嗯？」"
    window hide
#SE_VOLC 1,0
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/NIMG10A@2x.jpg" as bg1 zorder 200 with dissolve
    "听到脚下传来的声音，我放低了视线，那里是一只栗色毛的小狗。"
    play sound "SE09_29"
    犬 "「汪、汪！」"
    stop se
    voice "NCH07A_CH079"
    智纱 "「啊，是小狗」"
    "智纱立刻满脸放光地站了起来。"
    play sound "SE09_30"
    犬 "「呜」"
    stop se
    "在我脚下的小狗，看向了智纱那边。"
    window hide
#SE_VOLC 1,
    play music "BGM03"
    hide bg1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCB02"),"not F103==0","img/CH_ZMB02A@2x.png","True","img/CH_ZCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    hide bg1 with dissolve
    voice "NCH07A_CH080"
    智纱 "「来这边」"
    "智纱靠近小狗的方向，蹲下伸出了手。小狗把自己的脸向伸到眼前的手靠了过去，仿佛在调查一般地，动着鼻子。"
    "但是也并没有更加地戒备，把前爪放到了智纱的手上。"
    play sound "SE09_29"
    犬 "「汪、汪！」"
    stop se
    voice "NCH07A_CH081"
    智纱 "「伸、伸手了啊！　志雄君，快看快看！　看这里」"
    志雄 "「真、真的呢……」"
    "就仿佛是实现了谁也没有完成过的表演一样，智纱的眼睛里闪着光。"
    "……刚才的沉重的气氛已经消失了，我也稍微松了一口气。"
    voice "NCH07A_CH082"
    智纱 "「啊哈哈，好痒啊～」"
    "小狗呜呜地叫着，舔着刚才前爪搭过的那只手。智纱像小孩子一样，快活地笑着。"
    "总觉得有种让这只狗抢走了我的智纱的感觉……不对，我嫉妒动物个什么劲呢。"
    志雄 "「就算是这样，它还真是一点都不怕生呢。大概不是野狗吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCB01"),"not F103==0","img/CH_ZMB01A@2x.png","True","img/CH_ZCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH083"
    智纱 "「是啊，还戴着项圈呢」"
    "确实，在这只狗的脖子上，绕着一个作为家犬的证明。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMB06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCB06"),"not F103==0","img/CH_ZMB06A@2x.png","True","img/CH_ZCB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH084"
    智纱 "「是这家店的狗吗？」"
    "在店面的店员看了看这边，摇了摇头。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCB01"),"not F103==0","img/CH_ZMB01A@2x.png","True","img/CH_ZCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_XI000"
    店員Ｂ "「那只狗，是来溪钓的客人带来的，不过好像自己一个人回来了呢」"
    志雄 "「这里，能溪钓的吗？」"
    voice "NCH07A_XI001"
    店員Ｂ "「啊，就在旁边，有条河从湖那边流过来的。去那钓鱼的人还挺多呢」"
    "啊，所以说在这里有小卖部和休息所啊。"
    window hide
#SE_VOLC 1,0
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/NIMG10A@2x.jpg" as bg1 zorder 200 with dissolve
    play sound "SE09_30"
    犬 "「汪！」"
    stop se
    voice "NCH07A_CH085"
    智纱 "「小狗君，是和你的主人走散了吗？」"
    play sound "SE09_29"
    犬 "「汪、汪！」"
    stop se
    "当然它不可能理解人类的语言，小狗天真无邪地，蹭着智纱的手。"
    window hide
#SE_VOLC 1,
    hide bg1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCC04"),"not F103==0","img/CH_ZMC04A@2x.png","True","img/CH_ZCC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    hide bg1 with dissolve
    voice "NCH07A_CH086"
    智纱 "「志雄君」"
    "智纱把视线从来找她嬉闹的小狗那里，转到了我这边。"
    voice "NCH07A_CH087"
    智纱 "「还是……去找下这只狗的主人比较好吧？」"
    志雄 "「是呢……」"
    "如果误入了山路上，成了野狗那可就太可怜了。而且狗的主人，现在或许也在寻找它。"
    志雄 "「那，就去小溪的那边看看吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZMC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZCC01"),"not F103==0","img/CH_ZMC01A@2x.png","True","img/CH_ZCC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH088"
    智纱 "「嗯」"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG78AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression Solid("000") with None
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#FADE_IN 0
    "…………。"
    "……。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128
    scene expression "img/BG78AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_18L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1
    "从休息所的茶屋，走几分钟所到的地方，有一条小溪在流淌着。"
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDC01"),"not F103==0","img/CH_LNC01A@2x.png","True","img/CH_LDC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCH07A_CH089"
    智纱 "「哇……水好清澈呢」"
    "智纱的声音里，带着赞叹和惊讶。"
    "在河边，零零落落地看到一些在愉快地钓着鱼的人们。"
    志雄 "「智纱，走到水边来了，没关系的吗？」"
    voice "NCH07A_CH090"
    智纱 "「嗯，有落脚的地方就没问题的。谢谢你担心我」"
    play sound "SE09_30"
    犬 "「汪！」"
    stop se
    "小狗迅速地从智纱的手中逃了出去，降落在了地面上。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDA03"),"not F103==0","img/CH_LNA03A@2x.png","True","img/CH_LDA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCH07A_CH091"
    智纱 "「啊！？」"
#REMOVE_REEK_CHR 0
    window hide
    play sound "SE01_15"
#MOV_CHR_INIT 48
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
    play sound "SE09_29"
    犬 "「汪、汪！」"
    stop se
    play sound "SE01_15"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDC04"),"not F103==0","img/CH_LNC04A@2x.png","True","img/CH_LDC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH092"
    智纱 "「等等！　你要去哪里！？」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "小狗降落到了地面上，沿着小溪的岸边，向着上游的方向跑去。"
    "不时地停下来，向着对岸汪汪地吠叫着。"
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDC02"),"not F103==0","img/CH_LNC02A@2x.png","True","img/CH_LDC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCH07A_CH093"
    智纱 "「难道是，打算渡到对岸去的吗」"
    志雄 "「可能是吧。它的主人在河对岸吗……？」"
    window hide
    play sound "SE01_16L"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNC06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDC06"),"not F103==0","img/CH_LNC06A@2x.png","True","img/CH_LDC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH094"
    智纱 "「啊！」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "从智纱的嘴里，发出了格外大的惊讶声。她视线的方向——刚才的小狗从岸边走下了水。它在浅滩上发现了能渡过去的地方了吗。"
    志雄 "「可是，那家伙，能渡得过去吗？」"
    "小狗那小小的身体，向着河中央前进着……。"
    stop music fadeout 1
    play sound "SE01_17"
    "然后在下个瞬间，它的身影沉到了水下了！"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNA05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDA05"),"not F103==0","img/CH_MNA05A@2x.png","True","img/CH_MDA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCH07A_CH095"
    智纱 "「不、不去救它的话！！」"
    window hide
    play sound "SE01_00A"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    志雄 "「智纱！？」"
    "智纱就像要弹出去一样，向着小狗沉下去的方向——小溪中迈出了一步。"
    "但是——。"
    window hide

#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
#BG_UVC 1,(640/8),(448/8),((640/4)*3),((448/4)*3)

#SE_VOLC 1
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
#BG_SWPC 0
    hide bg1 with dissolve
#BG_ALPC 1
#BG_PRI 0
#BG_PRI 1

    play sound "SE01_14"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNC03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDC03"),"not F103==0","img/CH_MNC03A@2x.png","True","img/CH_MDC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "OBGM14"
    voice "NCH07A_CH096"
    智纱 "「啊……」"
    "智纱的脚，刚踏进水里一步，就停止住了。她的身体开始摇摇晃晃地震动了起来。脸色也变得苍白。"
    "那只小狗被冲走的地方的深度，不是智纱能承受得了的！"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDA04"),"not F103==0","img/CH_MNA04A@2x.png","True","img/CH_MDA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH097"
    智纱 "「但是，不去的话」"
    window hide

#BG_SET_BACK 
#BG_INIC 2
#BG_UVC 2,(640/4),(448/4),(640/2),(448/2)

#SE_VOLC 1,255
    play sound "SE01_14"
#BG_SWPC 0
    hide bg2 with dissolve
#BG_PRI 0
#BG_PRI 2
#BG_UVC 2,0,0,640,448
    "智纱慢慢地，向水里，踏出了一步。"
    志雄 "「等等，智纱！」"
    "智纱的恐水症，不是努力一下就能解决的问题。"
    "明明是办不到的。明明智纱自己也应该知道的……。靠她自己是无法走到沉下去的小狗身边的，无法救它起来的——。"
    "就算是这样，智纱也决定向前走。"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
    show expression "img/EV_CH04B@2x.png" as bg2 zorder 2 with dissolve
#SE_VOLC 1,0
#MUS_VOL 0
#BG_INIC 1
#BG_PRI 1
    hide lh0 with dissolve
#BG_ALPC 0
#BG_ALPC 2
    hide bg1 with dissolve
    "那个时候——我们第一次约会的时候，不也是这个样子的吗。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MNA05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MDA05"),"not F103==0","img/CH_MNA05A@2x.png","True","img/CH_MDA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_INIC 1
#BG_PRI 1
    hide bg2 with dissolve
#BG_ALPC 0
#CHR_ALPC 0
#SE_VOLC 1,255
#MUS_VOL 128
    hide bg1 with dissolve
    voice "NCH07A_CH098"
    智纱 "「除了我们以外，没有人注意到它溺水了啊」"
    voice "NCH07A_CH099"
    智纱 "「所以，我不去救它的话……」"
    "明明头脑很好。理性一点考虑的话，明明能知道，自己的行动完全是什么也救不了的——当有了什么目标的时候，打算之类的理性就全被吹飞了。"
    "某种的盲目性。某种意义上的危险性。"
    if F1<6:
        jump L_NCH07A_BRA00_A
#IF F18<6, GOTO L_NCH07A_BRA00_A
    jump L_NCH07A_BRA00_B
label L_NCH07A_BRA00_A:
#MSGNO_SAV 1
    "同时具有这些特点，娇小、无力的一个少女——这就是智纱。"
    jump L_NCH07A_SEL02_A
label L_NCH07A_BRA00_B:
#MSGNO_RET 1
    stop music fadeout 1
    "同时具有这些特点，娇小、无力的一个少女——这就是智纱。"
    menu:
        "寻找小狗的主人":
            $F7=0
        "跳进河里，去救小狗":
            $F7=1
    stop music fadeout 1
    if F7==0:
        jump L_NCH07A_SEL02_A
    if F7==1:
        jump L_NCH07A_SEL02_B
label L_NCH07A_SEL02_A:
    $F108=1
#RSET F108
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    $ renpy.end_replay()
    return
label L_NCH07A_SEL02_B:
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNA05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDA05"),"not F103==0","img/CH_LNA05A@2x.png","True","img/CH_LDA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "我把手放在了，颤颤发抖的智纱的肩上。"
    window hide
    play music "OBGM26"
    志雄 "「智纱，待在这里」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDA04"),"not F103==0","img/CH_LNA04A@2x.png","True","img/CH_LDA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH100"
    智纱 "「哎……」"
    志雄 "「知道吗，智纱。绝对不要走进水里。就在这里别动！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNC06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDC06"),"not F103==0","img/CH_LNC06A@2x.png","True","img/CH_LDC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH07A_CH101"
    智纱 "「等、等等，志雄君！」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE01_02L"
#BG_GET_NOC 0,F26
#BG_SET_BACK 
#BG_INIC 2
#BG_UVC 2,(640/4),(448/4),(640/2),(448/2)
#BG_ALP_AUTOC 0,0,0,F25,24
#BG_SWPC 0
    hide bg2 with dissolve
#BG_PRI 0
#BG_PRI 2
#BG_UVC 2,0,0,640,448
#BG_POSC 2,0,0,640,448
#BG_ALPC 2
    "没有去听智纱的制止，我向着小溪的方向冲了过去。"
    window hide
    stop sound
    play sound "SE03_52"
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/NIMG04A@2x.jpg" as bg1 with dissolve
    hide bg0 with dissolve
#BG_UVC 0,0,0,640,448
#SE_WATC 1
    play sound "SE07_05L"
    "然后，向着小狗被冲走的的地方——更深一层的水里跳了进去。"
    "水流的速度也并不是那么的快。和那只小狗的距离也并没有离得那么远，想追上它并不难……。"
    "我是那么想的。"
    "虽然是那样，但是为什么游起来那么困难？　身体没法像想象的那样活动！"
    "是因为虽说很缓慢，但还是有水流动的缘故？　不对，是衣服吸了水变重了的缘故？　而且鞋子也必须脱掉。好难走。"
    "可恶，现在再后悔也没办法了。总之，必须快点救出那只小狗！"
    "我为了确认位置，在水面上抬起了头，向周围张望着。在大约5米的前方，看到了那只小狗的头。"
    "那里吗。"
    "手和脚划着水，产生了推进力，接近着小狗的位置。"
    "在水中变得沉重的衣服，削弱着手脚的力量。但是，现在不是注意这些的时候。"
    "我向着小狗的方向伸出了手——。"
    "好了，抓住了！"
    "把这只小小的狗，拉到我的胸前。然后只要是回到浅滩上就……。"
    stop music fadeout 1
#SE_VOLC 1,255
    play sound "SE07_02"
#THREAD_STA 1,THREAD_QUA_WIN
#VIB_DOUKI 
    with vpunch
    志雄 "「呃！？」"
#MESA A_CH_SI,"【志雄】「呃！？」"
#THREAD_WAT 1
#WIN_POS 0,0
#VIB_STP 5
#MESX "%K%P"
    "腿上传来了筋肉被拉断一样的疼痛。"
    "麻烦了，腿，抽筋了……。"
    志雄 "「呃、呃……！」"
    "因为腿的疼痛，很难活动。而且因为单手抱着这只小狗，更没法动了。"
    "脚下滑了一下，身体就要被冲走了。"
    "可恶！　这样的话……！"
    "身体正在向水里下沉，只用一只手想办法控制住。"
    "看了看河边。直到刚才智纱还在的那个地方，现在她已经不在了。智纱……我明明跟你说过了待在那里不要动的。你去哪里了……？"
    "浅滩应该离这不是很远的距离，可为什么感觉就是这么远呢。"
    "哈哈哈。无意识地发出空虚的笑声。这次可不是开玩笑了，真的是很不妙了……。"
    "我——"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    scene expression Solid("000") with None
    show expression "img/BG78AA@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_COLC 0,24,24,48
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XNC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XDC02"),"not F103==0","img/CH_XNC02A@2x.png","True","img/CH_XDC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#SE_VOLC 1,
#FADE_IN 1
    "脑海中浮现的，是智纱哭泣的脸。如果我发生了什么事情，智纱她……。"
    window hide
#FADE_OUT 1
    hide bg1 with dissolve
#CHR_COLC 1,128,128,128
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_COLC 0,128,128,128
#FADE_IN 0
    "那样可……不行啊。"
    "如果发生了那种事情，智纱心里的伤就会更深了。说不定，就再也无法从对水的恐怖中，站起来了。"
    "所以，绝对。"
    "这只狗，还有我——必须都平安地回去。"
    voice "NCH07A_CH102_K"
    智纱？ "「志雄君！」"
    "听到了声音。"
    voice "NCH07A_CH103_K"
    智纱？ "「这个！　抓住这个！」"
    "这个？　这个是什么？"
    window hide
#FADE_OUT 0
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/NIMG04A@2x.jpg" as bg1 zorder 1 with dissolve
#SE_VOLC 1
#FADE_IN 1
    "我在睁开眼的同时，本能地抓住了一根伸到我眼前的棍子一样的东西。"
    "……。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    hide bg1 with dissolve
#BG_COLC 0,128,128,128
    scene expression "img/BG78AA@2x.jpg" as bg0 with dissolve
#SE_WATC 1
    play sound "SE05_18L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1
    "在赶过来的钓鱼人以及智纱伸过来的木头的帮助下，我总算摆脱了溺水的困境，回到了河边的陆地上。"
    "钓鱼的人，一边面对我们的道谢不好意思地笑着，一边回到了钓鱼场。"
    "小狗也平安地得救了，然后把它还到了匆匆赶到的主人手里。"
    "……。"
    voice "NCH07A_CH104"
    智纱 "「真的、太好了、平安无事……」"
    window hide
#SE_VOLC 1,
#CHR_INIC 0
#CHR_POSC 0,-63
#IF F103!0, GOTO IF_ELSE2
    if F103:
        jump NCH07A_IF_ELSE2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'EVN'",DynamicDisplayable(mouthanime,"EVN_CH08A"),"True","img/EVN_CH08AA@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH08AA")]=True
#    show expression "img/EVN_CH08A@2x.jpg" as bg0 with dissolve
#BG_FLG EVN_CH08AA
    jump NCH07A_IF_END2
label NCH07A_IF_ELSE2:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH08BA")]=True
#    show expression "img/EVN_CH08B@2x.jpg" as bg0 with dissolve
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"EVN_CH08B"),"True","img/EVN_CH08BA@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_FLG EVN_CH08BA
label NCH07A_IF_END2:
    play music "BGM16"
    "把狗还给了它的主人之后，迎接我的，是智纱的泪水。"
    志雄 "「抱着我，衣服会湿哦，智纱」"
    "因为我的衣服已经湿透了。"
    voice "NCH07A_CH105"
    智纱 "「那种事情，怎么都好！」"
    voice "NCH07A_CH106"
    智纱 "「平安无事，太好了……」"
    志雄 "「让你担心了，对不起。那只狗的地方并不是很远……只是有些计算失误，差点就溺水了」"
    "没想到穿着衣服在流动的水中游泳是这么困难、脚抽筋这些，只是些计算失误而已。"
    志雄 "「因为如果不那样的话，智纱就又会乱来的。明明是下不了水的，还是想要救那只狗」"
    志雄 "「你真是太乱来了……一直以来」"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG12AA@2x.jpg" as bg0 zorder 2 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA01"),"True","img/CH_LAA01A@2x.png") as lh0 zorder (10-1):
        ypos 0.0
    with dissolve
#SE_VOLC 1,0
#BG_INIC 1
#BG_PRI 1
#BG_ANM_OFFC 0
#BG_BLUR 2
#BG_ALPC 2
#CHR_ALPC 1
    "总是为了我，做好便当。"
#SCRMODE_SPC SCR_FULL
#MES "%n%n%n%n%n%n%n%n%n%n%S032%LC%FS总是为了我，做好便当。%FE%LE%K%O032"
#CHR_PRIC 1
#BG_PRI 2
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB02"),"not F103==0","img/CH_LLB02A@2x.png","True","img/CH_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
#BG_PRI 0
    show expression "img/BG33AA@2x.jpg" as bg0 zorder 0 with dissolve
#BG_BLUR 0
#CHR_PAL_BGC 0,BG33AA
#BG_ALP_AUTOC 2,0,0,F24,48
#CHR_ALP_AUTOC 1,0,0,F24,48
#BG_ALP_SAVEC 2
#CHR_ALP_SAVEC 1
#CHR_SWPC 0
#CHR_PRIC 1
#CHR_PRIC 0
#BG_SWPC 0
    "来我家里给我打扫、为我做饭。"
#BG_PRI 2
#BG_PRI 0
#MES "%n%n%n%n%n%n%n%n%n%n%S032%LC%FS来我家里给我打扫、为我做饭。%FE%LE%K%O032"
#CHR_PRIC 1
#BG_PRI 2
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAA01"),"not F103==0","img/CH_LKA01A@2x.png","True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
#BG_PRI 0
    show expression "img/BG09EA@2x.jpg" as bg0 zorder 0 with dissolve
#BG_BLUR 0
#CHR_PAL_BGC 0,BG09EA
#BG_ALP_AUTOC 2,0,0,F24,48
#CHR_ALP_AUTOC 1,0,0,F24,48
#BG_ALP_SAVEC 2
#CHR_ALP_SAVEC 1
#CHR_SWPC 0
#CHR_PRIC 1
#CHR_PRIC 0
#BG_SWPC 0
    "帮我完成学生会的工作。"
#BG_PRI 2
#BG_PRI 0
#MES "%n%n%n%n%n%n%n%n%n%n%S032%LC%FS帮我完成学生会的工作。%FE%LE%K%O032"
#CHR_PRIC 1
#BG_PRI 2
#BG_SET_BACK 
#BG_INIC 0
#BG_PRI 0
#IF F103!0, GOTO _10
    if F103:
        jump _10
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH03A")]=True
    scene expression "img/EVN_CH03A@2x.jpg" as bg0 zorder 0 with dissolve
    jump _20
label _10:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH03B")]=True
    scene expression "img/EVN_CH03B@2x.jpg" as bg0 zorder 0 with dissolve
label _20:
#BG_ALP_AUTOC 2,0,0,F24,48
#CHR_ALP_AUTOC 1,0,0,F24,48
#BG_ALP_SAVEC 2
#CHR_ALP_SAVEC 1
#CHR_SWPC 0
#CHR_PRIC 1
#CHR_PRIC 0
#BG_SWPC 0
    "为了整理我专用的复习要点，弄得睡眠不足。"
#BG_PRI 2
#BG_PRI 0
#MES "%n%n%n%n%n%n%n%n%n%n%S032%LC%FS为了整理我专用的复习要点，弄得睡眠不足。%FE%LE%K%O032"
#CHR_PRIC 1
#BG_PRI 2
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC05"),"not F103==0","img/CH_LLC05A@2x.png","True","img/CH_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
#BG_PRI 0
    show expression "img/BG68AA@2x.jpg" as bg0 zorder 0 with dissolve
#BG_BLUR 0
#CHR_PAL_BGC 0,BG68AA
#BG_ALP_AUTOC 2,0,0,F24,48
#CHR_ALP_AUTOC 1,0,0,F24,48
#BG_ALP_SAVEC 2
#CHR_ALP_SAVEC 1
#CHR_SWPC 0
#CHR_PRIC 1
#CHR_PRIC 0
#BG_SWPC 0
    "因为我邀请了她，跟家长撒了谎，来了这次旅游。"
#BG_PRI 2
#BG_PRI 0
#MES "%n%n%n%n%n%n%n%n%n%n%S032%LC%FS因为我邀请了她，跟家长撒了谎，来了这次旅游。%FE%LE%K%O032"
#CHR_PRIC 1
#BG_PRI 2
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA01"),"not F103==0","img/CH_LLA01A@2x.png","True","img/CH_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
#BG_PRI 0
    show expression "img/BG61AA@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_PAL_BGC 0,BG61AA
#BG_BLUR 0
#BG_ALP_AUTOC 2,0,0,F24,48
#CHR_ALP_AUTOC 1,0,0,F24,48
#BG_ALP_SAVEC 2
#CHR_ALP_SAVEC 1
#CHR_SWPC 0
#CHR_PRIC 1
#CHR_PRIC 0
#BG_SWPC 0
    "说什么好不容易有个能游泳的地方，就要去湖边。"
#BG_PRI 2
#BG_PRI 0
#MES "%n%n%n%n%n%n%n%n%n%n%S032%LC%FS说什么好不容易有个能游泳的地方，就要去湖边。%FE%LE%K%O032"
#CHR_PRIC 1
#BG_PRI 2
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH_LFB03'",DynamicDisplayable(mouthanime,"CH_LFB03,0"),"True","img/CH_LFB03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
#BG_PRI 0
    show expression "img/BG64NA@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_PAL_BGC 0,BG64NA
#EFF_STAC 0,YUGE2,EFF_SKIP
#BG_BLUR 0
#BG_ALP_AUTOC 2,0,0,F24,48
#CHR_ALP_AUTOC 1,0,0,F24,48
#BG_ALP_SAVEC 2
#CHR_ALP_SAVEC 1
#CHR_SWPC 0
#BG_SWPC 0
    "明明是如此的腼腆，还进了男浴室。"
#MES "%n%n%n%n%n%n%n%n%n%n%S032%LC%FS明明是如此的腼腆，还进了男浴室。%FE%LE%K%O032"
#BG_PRI 2
#CHR_PRIC 1
#BG_SET_BACK 
#BG_INIC 0
#BG_PRI 0
#IF F103!0, GOTO _1110
    if F103:
        jump _1110
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH06A")]=True
    scene expression "img/EVN_CH06A@2x.jpg" as bg0 with dissolve
    jump _1120
label _1110:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH06D")]=True
    scene expression "img/EVN_CH06D@2x.jpg" as bg0 with dissolve
label _1120:
#EFF_STPC 0,EFF_SKIP
#BG_ALPC 2
#CHR_ALPC 1
#BG_SWPC 0
#BG_PRI 2
#BG_PRI 0
#CHR_SWPC 0
    "听说那样做能让我高兴，就潜入了我的被窝里。"
#CHR_PRIC 1
#CHR_PRIC 0
#MES "%n%n%n%n%n%n%n%n%n%n%S032%LC%FS听说那样做能让我高兴，就潜入了我的被窝里。%FE%LE%K%O032"
#CHR_PRIC 1
#BG_PRI 2
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDC02"),"not F103==0","img/CH_LNC02A@2x.png","True","img/CH_LDC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
#BG_PRI 0
    show expression "img/BG66AA@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_PAL_BGC 0,BG66AA
#BG_BLUR 0
#BG_ALP_AUTOC 2,0,0,F24,48
#CHR_ALP_AUTOC 1,0,0,F24,48
#BG_ALP_SAVEC 2
#CHR_ALP_SAVEC 1
#CHR_SWPC 0
#CHR_PRIC 1
#CHR_PRIC 0
#BG_SWPC 0
    "明明已经很累了，却不想添我的麻烦拒绝我的帮助。"
#BG_PRI 2
#BG_PRI 0
#MES "%n%n%n%n%n%n%n%n%n%n%S032%LC%FS明明已经很累了，却不想添我的麻烦拒绝我的帮助。%FE%LE%K%O032"
    window hide
#SCRMODE_SPC SCR_WINDOW
#BG_SET_BACK 
#BG_INIC 0
#BG_ALPC 0
#CHR_INIC 0
#CHR_POSC 0,-63
#IF F103!0, GOTO IF_ELSE3
    if F103:
        jump NCH07A_IF_ELSE3
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'EVN'",DynamicDisplayable(mouthanime,"EVN_CH08A"),"True","img/EVN_CH08AA@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    jump NCH07A_IF_END3
label NCH07A_IF_ELSE3:
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'EVN'",DynamicDisplayable(mouthanime,"EVN_CH08B"),"True","img/EVN_CH08BA@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
label NCH07A_IF_END3:
#BG_INIC 1
#BG_PRI 1
#FILT_OUT 0
    hide bg2 with dissolve
    hide lh1 with dissolve
#BG_PRI 0
#BG_PRI 1
#BG_PRI 2
#CHR_PRIC 0
#CHR_PRIC 1
#BG_UVC 0,0,0,640,448
#BG_UVC 2,0,0,640,448
#BG_ALPC 0
#SE_VOLC 1,
    hide bg1 with dissolve
    "这样的智纱，总是在牺牲着自己，牺牲着自己去做一些勉强自己的事。"
    "明明可以活得更轻松一点的。明明可以活得更快乐一些的。"
    "但是那种事情，智纱一定是不可能做得到的吧。"
    "所以……。"
    志雄 "「智纱总是为我做了很多的事情」"
    志雄 "「总是在我的身边，支持着我」"
    志雄 "「所以我也是，不管什么时候，都希望能为智纱去做些什么」"
    voice "NCH07A_CH107"
    智纱 "「明明……明明不是那样子的」"
    "智纱一边满脸泪水，一边从口袋里取出了一个小小的钥匙链。"
    "做成大波斯菊样式的钥匙链，是去年的圣诞节——智纱的生日时，我送给她的生日礼物。"
    voice "NCH07A_CH108"
    智纱 "「我——我也已经从志雄君这里获得了太多的东西。多到已经没有办法偿还了」"
    "是大波斯菊，将我们两人第一次联结起来。而且当智纱和我陷进了无法逃出的死胡同的时候，它就是我们的路标。"
    voice "NCH07A_CH109"
    智纱 "「我才是，直到现在，一直依靠着志雄君……一定给志雄君添了很多麻烦的」"
    voice "NCH07A_CH110"
    智纱 "「就算是那样，志雄君你还是一次也没有露出过厌烦的表情，陪在我的身边……」"
    "啊，这样啊……终于知道了。至今为止的我们之间，各有那么一点点的偏差。智纱过于担心我的事情了……。"
    window hide
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/NIMG01B@2x.png" as bg0 zorder 0
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
#EFF_PRI 0
#EFF_STAC 0,CLOUD_B,EFF_SKIP

    hide lh0 with dissolve
#BG_ANM_OFFC 0
    "我，抱紧了智纱。"
    "智纱的衣服已经湿了，但是我现在就想要抱紧她。抱紧我喜欢的，这个少女。"
    jump L_NCH07A_SEL02_X
label L_NCH07A_SEL02_X:
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
    $ renpy.end_replay()
    return
#label THREAD_QUA_WIN
#TH_QUAKE_WIN 4
#EOT
#label TH_YUSURU
#INFINITEYUSURU 16
#EOT
#label THREAD_HELP_CHISA
#BG_UV_AUTOC 0,(640/4),(448/4),(640/2),(448/2),1,F24,12
#BG_ALP_AUTOC 0,0,0,F124,24
#BG_SWPC 0
    hide bg2 with dissolve
#BG_PRI 0
#BG_PRI 2
#BG_UVC 2,0,0,640,448
#BG_POSC 2,0,0,448,448
#BG_ALPC 2
#EOT