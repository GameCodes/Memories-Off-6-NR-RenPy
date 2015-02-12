label NCH06A3:
    $month = '07'
    $day = '28'
    $date = '5'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG61NA@2x.jpg" as bg0 zorder 0 with dissolve

#BG_SET_BACK 
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 1
#BG_UVC 1,((640/2)+(640/8)),(448/8),(640/4),(448/4)

#CHR_SET_BACK
#CHR_INIC 2
#CHR_PRIC 2
#CHR_ALPC 2
#CHR_SCLC 2,512,512
#CHR_POSC 2,(448/2)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA05"),"True","img/SN_LBA05A@2x.png") as lh1 zorder (10-12):
        ypos 0.0
    with dissolve
#FADE_IN 1
    play music "OBGM25"
    "总之是多亏了稻穗先生，我和智纱才能不被人看见地从浴场出来。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHC02"),"not F103==0","img/CH_MRC02A@2x.png","True","img/CH_MHC02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
        xcenter .75
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBB01"),"True","img/SN_MBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25

    with dissolve
    
    "从浴室回房间的路上，我向稻穗先生提出了疑问。"
    voice "NCH06A_SN002"
    信 "「要说为什么我会在这家旅馆里，可就说来话长了啊？」"
    志雄 "「嗯，没关系的」"
#MUS_VOL 0
    window hide
    hide lh1
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA05"),"True","img/SN_LBA05A@2x.png") as lh1 zorder 10:
        ypos 0.0
    with dissolve
    play sound "SE07_18"
#BG_ALP_AUTOC 1,128,1,F24,24
#BG_UV_AUTOC 1,(640/2),0,(640/2),(448/2),1,F24,24
#CHR_ALP_AUTOC 2,128,1,F24,24
#CHR_SCL_AUTOC 2,128,128,1,F24,24
#CHR_POS_AUTOC 2,1,F24,24
    stop se
    voice "NCH06A_SN003"
    信 "「因为我在这里打工啊」"
#MESA A_CH_SN,NCH06A_SN003,"【信】「因为我在这里打工啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA06"),"True","img/SN_LBA06A@2x.png") as lh1 zorder (10+12):
        ypos 0.0
    with dissolve
#MESX "%K%P"
    play sound "SE07_20"
    "……。"
    志雄 "「就这些？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA01"),"True","img/SN_LBA01A@2x.png") as lh1 zorder (10+12):
        ypos 0.0
    with dissolve
    voice "NCH06A_SN004"
    信 "「啊，就这些」"
    "2秒就完了。"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA01"),"True","img/SN_MBA01A@2x.png") as lh1 zorder (10-11):
        ypos 0.0
    with dissolve
#MUS_VOL 128
#BG_ALP_AUTOC 1,0,1,F24,48
#CHR_ALP_AUTOC 2,0,1,F24,48
#BG_ALP_SAVEC 1
#CHR_ALP_SAVEC 2
    hide bg1 with dissolve
#BG_PRI 1
#BG_ALPC 1,128
#BG_UVC 1,0,0,640,448
    hide lh2 with dissolve
#CHR_PRIC 2
#CHR_SCLC 2,256,256
#CHR_ALPC 2,128
    if not persistent.dictlist[35] and persistent.show_dict:
        $persistent.dictlist[35]=True
        show screen dict_pop(i=35)
    志雄 "「稻穗先生，是被酪萨克解雇了吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA04"),"True","img/SN_MBA04A@2x.png") as lh1 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCH06A_SN005"
    信 "「不是！　没有那回事的啊！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRB06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHB06"),"not F103==0","img/CH_MRB06A@2x.png","True","img/CH_MHB06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH237"
    智纱 "「可是，为什么会在这里工作呢？」"
    window hide
#MUS_VOL 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA05"),"True","img/SN_MBA05A@2x.png") as lh1 zorder (10+11):
        ypos 0.0
    with dissolve
    pause (4/32.0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBB01"),"True","img/SN_MBB01A@2x.png") as lh1 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCH06A_SN006"
    信 "「这座小镇的空气，在呼唤着我」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHA04"),"not F103==0","img/CH_MRA04A@2x.png","True","img/CH_MHA04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    "……想想看，想问这个人行动的合理性也不现实。因为他是突然退了学，然后去了印度的人。"
#MUS_VOL 128
    志雄 "「但是，谢谢你了。多亏了稻穗先生挂上了一个清扫中的牌子，别人才没有进来」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHC02"),"not F103==0","img/CH_MRC02A@2x.png","True","img/CH_MHC02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH238"
    智纱 "「对不起」"
    "智纱有些耷拉着脑袋。或许是觉得，自己做得有些过火了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA01"),"True","img/SN_MBA01A@2x.png") as lh1 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCH06A_SN007"
    信 "「没事没事，不用行此大礼，年轻人」"
    voice "NCH06A_SN008"
    信 "「我看见了智纱跟在塚本君的后面走进了浴场，但没有阻止她」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHA04"),"not F103==0","img/CH_MRA04A@2x.png","True","img/CH_MHA04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    志雄 "「……啊？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHB04"),"not F103==0","img/CH_MRB04A@2x.png","True","img/CH_MHB04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    志雄 "「那，为、为什么没有去阻止呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA06"),"True","img/SN_MBA06A@2x.png") as lh1 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCH06A_SN009"
    信 "「嗯，因为我觉得会很有趣」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHB03"),"not F103==0","img/CH_MRB03A@2x.png","True","img/CH_MHB03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    "毫不犹豫，立即回答。"
    志雄 "「说实在的，你这个人真是……」"
    "叹了口气，我用一种带着怨恨的眼神看着他，但是稻穗先生一点也没在意。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBB01"),"True","img/SN_MBB01A@2x.png") as lh1 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCH06A_SN010"
    信 "「那，我差不多该回去工作了」"
    voice "NCH06A_SN011"
    信 "「啊，如果有什么事的话就不要介意跟我说吧。我们又不是不认识」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHB01"),"not F103==0","img/CH_MRB01A@2x.png","True","img/CH_MHB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA02"),"True","img/SN_MBA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0

    with dissolve
    voice "NCH06A_SN012"
    信 "「智纱的旅行，也玩得高兴哦」"
    window hide
#MUS_VOL 0
#MOV_CHR_INIT 48
#MOV_CHR0 
#MOV_CHR1 0,640
#MOV_CHR_GO 1
    "稻穗先生笑容满面地说着，转过了身去。"
    "看着慢慢消失在走廊里的稻穗先生的身影，有那么一点不祥的预感。"
    "……这个人，不会再打什么别的坏主意吧。"
    "……。"
#MUS_VOL 128
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA01"),"True","img/SN_MBA01A@2x.png") as lh1 zorder (10-11):
        ypos 0.0
    with dissolve
    信 "「啊，对了。有句话忘了说了」"
#THREAD_STA 1,THREAD_SHIN_IN
#MESA A_CH_SN,NCH06A_SN013,"【信】「啊，对了。有句话忘了说了」"
#THREAD_WAT 1
#MESX "%K%P"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHB04"),"not F103==0","img/CH_MRB04A@2x.png","True","img/CH_MHB04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    志雄 "「？　是什么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA06"),"True","img/SN_MBA06A@2x.png") as lh1 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCH06A_SN014"
    信 "「敬请期待」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHA04"),"not F103==0","img/CH_MRA04A@2x.png","True","img/CH_MHA04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    志雄 "「啊？」"
    window hide
    stop music fadeout 1
#MOV_CHR_INIT 48
#MOV_CHR0 
#MOV_CHR1 0,640
#MOV_CHR_GO 1
    "稻穗先生扔下了一脸呆像的我，走开了。"
    voice "NCH06A_CH239"
    智纱 "「敬请期待，指的是怎么一回事呢？」"
    志雄 "「……谁知道啊？」"
    window hide
#FADE_OUT 1
    hide lh1 with dissolve
#CHR_ALPC 1,128
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 1
#BG_UVC 0,((640/16)*7),((448/8)*7),(640/8),(448/8)
#BG_SETWC 0,1,BG63NA2,NIMG01D
#BG_COLC 1,0,0,0,128
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
    "……。"
    "…………。"
    window hide
#BG_COLC 1,128,128,128,128
    scene expression "img/BG63NA2@2x.jpg" as bg0 with dissolve
#BG_SET_BACK
#EFF_STAC 0,CLOUD_D,EFF_NOSKIP
    play sound "SE05_16L"
    pause (32/32.0)
#FADE_IN 1
    "没用多长时间，我们就明白了稻穗先生话里的意思。"
    window hide
#SE_VOLC 1,0
    play sound "SE07_25"
#FADE_OUT 1,16
#BG_ALPC 1
#EFF_STPC 0,EFF_SKIP
    hide bg1 with dissolve
#FADE_IN 1,16
#BG_UV_AUTOC 0,((640/8)*3),((448/4)*3),(640/4),(448/4),1,F24,16
#BG_UV_SAVEC 0
    pause (12/32.0)
    play sound "SE07_25"
#BG_UVC 0,(640/4),(448/2),(640/2),(448/2)
#BG_UV_AUTOC 0,0,0,640,448,1,F24,16
#BG_UV_SAVEC 0
    pause (12/32.0)
#SE_VOLC 1,64
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LRA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LHA04"),"not F103==0","img/CH_LRA04A@2x.png","True","img/CH_LHA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCH06A_CH240"
    智纱 "「那、那个……这是……？」"
    "房间里，铺着双人用的，宽大的一床被子。"
    志雄 "「……」"
    window hide
    play music "OBGM13"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我一言不发地往回走。"
    voice "NCH06A_CH241"
    智纱 "「……志雄君？」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    show expression "img/BG62NA@2x.jpg" as bg1 zorder 1 with dissolve
    stop sound fadeout 1
    play sound "SE00_47"
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
#BG_SWPC 0
    hide bg1 with dissolve
#BG_ALPC 1,128
#BG_PRI 0
#BG_PRI 1
    scene expression "img/BG62NA@2x.jpg" as bg0 with dissolve
    stop sound
#SE_WATC 0
    play sound "SE01_03L"
    "呜哦～～～～！"
    window hide
#BG_INIC 1
    show expression "img/BG61NA@2x.jpg" as bg0 with dissolve
    hide bg1 with dissolve
    "啊～～～～！"
    window hide
#BG_INIC 1
    show expression "img/BG62NA@2x.jpg" as bg0 with dissolve
    hide bg1 with dissolve
    "呀啊～～～～！"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA01"),"True","img/SN_MBA01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCH06A_SN015"
    信 "「哦，塚本君——」"
    志雄 "「稻穗先生！」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_INIC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBB04"),"True","img/SN_LBB04A@2x.png") as lh11 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCH06A_SN016"
    信 "「哦！？」"
    stop sound
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_XBB04"),"True","img/SN_XBB04A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
#RSET F121
#THREAD_STA 1,THREAD_ROCK_SHIN
    "抓着稻穗先生的肩膀，用力地摇晃着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_XBA04"),"True","img/SN_XBA04A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCH06A_SN017"
    信 "「喂喂喂，冷静！」"
    志雄 "「能冷静得下来吗！　那是什么啊，房间里的那个！？　那床被子！？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_XBA06"),"True","img/SN_XBA06A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCH06A_SN018"
    信 "「啊，那个吗？　为了你们两人准备的。是特别服务。」"
#STOP_NCH06A3_EFFECT
    志雄 "「完全不需要，那种服务！　请您别做多余的事！」"
#RSET F121
#THREAD_WAT 1
    stop music fadeout 1
    志雄 "「话说回来，为什么知道我们住在那个房间……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA01"),"True","img/SN_LBA01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCH06A_SN019"
    信 "「那个嘛，我在这个旅馆工作啊，看看住宿客人表就知道了啊。说实话，塚本君来这里我倒是挺吃惊的」"
    志雄 "「这样啊，原来如此……」"
    "——喂，这不是该钦佩的时候！"
    志雄 "「够了！　与其在这管我们的闲事，不如去干好您的工作吧！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBB02"),"True","img/SN_LBB02A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NCH06A_SN020"
    信 "「好好」"
    "稻穗先生耸了耸肩。"
    "他是真的明白了吗？"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG63NA2@2x.jpg" as bg0 zorder 0 with dissolve
#BG_SET_BACK 
#BG_INIC 1
#BG_COLC 1,0,0,0,128
#IF F103!0, GOTO IF_ELSE1
    if F103!=0:
        jump NCH06A3_IF_ELSE1
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH06A")]=True
    show expression "img/EVN_CH06A@2x.jpg" as bg1 zorder 1 with dissolve
    jump NCH06A3_IF_END1
label NCH06A3_IF_ELSE1:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH06D")]=True
    show expression "img/EVN_CH06D@2x.jpg" as bg1 zorder 1 with dissolve
label NCH06A3_IF_END1:
    "…………。"
    "……。"
    window hide
#BG_COLC 1,128,128,128,128
    scene expression "img/BG63NA2@2x.jpg" as bg0 with dissolve
    play sound "SE00_48"
    play sound "SE05_16L"
#FADE_IN 1
    "回到了房间里，看到智纱一个人坐在那个双人用的被子上。"
    voice "NCH06A_CH242"
    智纱 "「好大的被子……」"
    window hide
#SE_VOLC 1,64
#IF F103!0, GOTO IF_ELSE2
    if F103:
        jump NCH06A3_IF_ELSE2
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH06B")]=True
    show expression "img/EVN_CH06B@2x.jpg" as bg1 with dissolve
    jump NCH06A3_IF_END2
label NCH06A3_IF_ELSE2:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH06E")]=True
    show expression "img/EVN_CH06E@2x.jpg" as bg1 with dissolve
label NCH06A3_IF_END2:
    play music "BGM13"
    voice "NCH06A_CH243"
    智纱 "「啊，你回来了」"
    "智纱向我这边看了过来，表情变得温和了起来。"
    voice "NCH06A_CH244"
    智纱 "「看你突然就跑了出去，还在想发生了什么事呢。不会是肚子痛吧？」"
    志雄 "「没事，我的身体完全没问题。只是突然想起来，和稻穗先生有点事情要说」"
    voice "NCH06A_CH245"
    智纱 "「什么事情呢？」"
    志雄 "「没事，不是什么大不了的事，不用在意的」"
    志雄 "「先不说这个……」"
    志雄 "「只放了一床被子，大概是旅馆的人搞错了吧。以为这房间里住的是一个人了」"
    志雄 "「可是又准备这么大的被子，不会是当成相扑手了吧。哈哈哈」"
    "尽可能地，装出笑容来。"
    voice "NCH06A_CH246"
    智纱 "「哎？　啊，嗯」"
    志雄 "「来，把那个被子收拾起来，重新铺上两个人的吧」"
    window hide
    if F103:
        jump NCH06A3_IF_ELSE3
#IF F103!0, GOTO IF_ELSE3
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH06C")]=True
    show expression "img/EVN_CH06C@2x.jpg" as bg1 with dissolve
    jump NCH06A3_IF_END3
label NCH06A3_IF_ELSE3:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH06F")]=True
    show expression "img/EVN_CH06F@2x.jpg" as bg1 with dissolve
label NCH06A3_IF_END3:
    voice "NCH06A_CH247"
    智纱 "「……哎？　要收起来吗？」"
    志雄 "「……」"
    "……哎。"
    "怎么一副有些遗憾的表情？"
    "我还没琢磨透智纱表情里的含义，她就红着脸，慌慌张张地从被子上站了起来。"
    window hide
#SE_VOLC 1,(64/2)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHB04"),"not F103==0","img/CH_MRB04A@2x.png","True","img/CH_MHB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    hide bg1 with dissolve
    voice "NCH06A_CH248"
    智纱 "「嗯、嗯，是呢！」"
    voice "NCH06A_CH249"
    智纱 "「必须重新铺好！」"
    志雄 "「啊、啊……」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG63NA3@2x.jpg" as bg0 zorder 0 with dissolve
    pause (32/32.0)
#FADE_IN 1
    "我们把被子叠好，塞回了壁橱里，然后把两个普通大小的被子铺了出来。"
    "在收拾的时候，我还是注意到了刚才智纱的嘟哝。在说要收拾被子的时候，看上去很失望的样子……。"
    window hide
#SE_VOLC 1,64
#MUS_VOL 64
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHA03"),"not F103==0","img/CH_MRA03A@2x.png","True","img/CH_MHA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH250"
    智纱 "「怎、怎么了？一直盯着我看？」"
    志雄 "「没事没事，什么事也没有」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我条件反射般地把视线从智纱那里移开。啊啊，没法直视智纱的眼睛。"
    志雄 "「哎～、咳」"
    "为了重新打起精神，我先咳嗽了一声。"
    window hide
#SE_VOLC 1,(64/2)
#MUS_VOL 128
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHA01"),"not F103==0","img/CH_MRA01A@2x.png","True","img/CH_MHA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH251"
    智纱 "「……」"
    "呜，好尴尬……。该怎么办才好呢……？"
    "啊。对了。这么说来旅行之前，和亨一起去玩的时候，他这样说过……。"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG05EA@2x.jpg" as bg2 zorder 18 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
#CHR_COLC 1,128,120,112,128
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA01"),"True","img/TO_LBA01A@2x.png") as lh1 zorder (20-1):
        ypos 0.0
    with dissolve
#SE_VOLC 1,0,16
    stop music fadeout 1
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 2,128
#CHR_ALPC 1,128
#BG_BLUR 2
    hide bg1 with dissolve
    play music "BGM09"
    voice "NCH06A_TO001_K"
    亨 "「明天开始，你就要和智纱去旅行了吧？」"
    志雄 "「啊？　等等，为什么你会知道那个啊。」"
    voice "NCH06A_TO002_K"
    亨 "「从莉莉丝那听说的。」"
    "呃，是这么回事吗。"
    "莉莉丝知道我们要去旅行的事，现在和那家伙关系很好的亨会知道也没什么奇怪的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB01"),"True","img/TO_LBB01A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NCH06A_TO003_K"
    亨 "「正因为这样，把这个给你」"
    "亨把一个单手可拿、用瓦楞纸板捆起来的『什么东西』递给了我。"
    志雄 "「虽说对你的『正因为这样』是啥完全不明白，这个是，什么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB02"),"True","img/TO_LBB02A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NCH06A_TO004_K"
    亨 "「是能派上用场的东西。如果在你和智纱两人独处的时候用的话，更有效果」"
    志雄 "「嗯」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA04"),"True","img/TO_LBA04A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NCH06A_TO005_K"
    亨 "「你那一点兴趣都没有的反应，算什么啊！」"
    window hide
    stop music fadeout 1
#BG_INIC 1
#BG_PRI 1
    scene expression "img/BG63NA3@2x.jpg" as bg0 with dissolve
    hide bg2 with dissolve
    stop music fadeout 1
    hide lh1 with dissolve
#BG_UVC 2,0,0,640,448
#BG_ALPC 0,128
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHA01"),"not F103==0","img/CH_MRA01A@2x.png","True","img/CH_MHA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#SE_VOLC 1,(64/2)
    hide bg1 with dissolve
    play music "BGM13"
    "虽说对里面放了什么东西并没有太大兴趣，但是总觉得应该带着那个包裹。"
    "回想起来看看，从大小来看说不定是卡片游戏之类的。"
    window hide
    play sound "SE03_88"
    play sound "SE03_66"
    "我打开了旅行包，在里面找着。"
    window hide
#CHR_SET_BACK
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHA04"),"not F103==0","img/CH_MRA04A@2x.png","True","img/CH_MHA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH252"
    智纱 "「怎么了？」"
    "智纱很奇怪地看着我。我先不管智纱，继续在包里翻找着。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    stop se
    志雄 "「……有了，是这个」"
    "从亨那里拿来的包裹，埋在旅行包的最底部，衣服的下面。"
    "说到卡片游戏，那可是旅行时的固定项目了。初中时的修学旅行，大家也是用晚上的时间来打扑克的。"
    "也就是说，玩会儿这个好化解开尴尬的气氛吗？　你有时也会干点有用的事情啊，亨！"
    "我立刻打开了那个包裹，装在里面的是——。"
    window hide
    stop music fadeout 1
    "『Ｓｔｅｐ　Ｕｐ！　教你二倍速变大人』"
    "写着这些字样的袖珍本图书。"
#SE_VOLC 1,64
#SCRMODE_SPC SCR_FULL
#FILT_IN 48,0,COL_PINK
#MES "%n%n%n%n%n%S032%LC%FS　　　　　『Ｓｔｅｐ　Ｕｐ！　教你二倍速变大人』%n　　　　 　　　写着这些字样的袖珍本图书。%FE%LE%K%O032"
    window hide
#FILT_OUT 48
#SCRMODE_SPC SCR_WINDOW
    志雄 "「……」"
    window hide
#SE_VOLC 1,(64/2)
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XRA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XHA04"),"not F103==0","img/CH_XRA04A@2x.png","True","img/CH_XHA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .8
    with dissolve
    voice "NCH06A_CH253"
    智纱 "「志雄君，那个是？」"
    志雄 "「没、没，什么也没有！」"
    play sound "SE03_66"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "智纱正在我的肩膀后面看着，我立刻把那本书塞到了包里面，藏了起来。"
    window hide
    stop se
    play music "OBGM13"
    "佐～贺～亨～～～！　你这家伙为什么要给我这种会让气氛更加尴尬的东西！"
    "我无言地站了起来，走向门的方向。"
    voice "NCH06A_CH254"
    智纱 "「……志、志雄君！？」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    show expression "img/BG62NA@2x.jpg" as bg1 zorder 1 with dissolve
#SE_VOLC 1,0
    play sound "SE00_47"
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
#BG_SWPC 0
    hide bg1 with dissolve
#BG_ALPC 1,128
#BG_PRI 0
#BG_PRI 1
    scene expression "img/BG62NA@2x.jpg" as bg0 with dissolve
#SE_WATC 0
    play sound "SE01_03L"
    "呜哦～～～～！"
    window hide
    show expression "img/BG61NA@2x.jpg" as bg0 with dissolve
    "啊～～～～！"
    window hide
#SE_VOLC 1,255
    show expression "img/BG60NA@2x.jpg" as bg0 with dissolve
    "呀啊～～～～！"
    window hide
#SE_VOLC 1,0
    scene expression "img/BG61NA@2x.jpg" as bg0 with dissolve
    stop se
    "呃，是啊，和稻穗先生不一样，亨可不在这里！　在旅馆里跑也不可能找到他的！"
    "可恶，该怎么办……！"
    "……有了！"
    "我取出手机。把短信的送信人选上亨，开始输入正文。"
    window hide
#SCRMODE_SPC SCR_FULL
#FILT_IN 48,0,COL_DARK2
    play sound "SE02_03"
    pause (4/32.0)
    play sound "SE02_03"
    pause (2/32.0)
    play sound "SE02_03"
    pause (12/32.0)
    play sound "SE02_03"
    pause (8/32.0)
    play sound "SE02_03"
    "Ｔｏ{w}：佐贺亨{w}\n题目：你的那个秘密，我要全部告诉莉莉丝。"
#MES "%S032%FS%t002Ｔｏ%t158：佐贺亨%N%t002题目%t158：%N%t005你的那个秘密，我要全部告诉莉莉丝。%FE%K"
    play sound "SE02_03"
#MESX "%O032"
    window hide
#SCRMODE_SPC SCR_WINDOW
#FILT_OUT 48
    "短信的最后加上了一个骷髅的表情符号，发送了。用这种表情符号我还是头一次。"
    "其实我并不知道亨的什么『秘密』，只是这么写的话，一定能吓那家伙一跳的。"
    "真是的，不光稻穗先生，就连亨都要搞这种事……。最近，亨的行动有时看起来，和稻穗先生重合了。"
    "亨那家伙到底是要干什么。他的目的是什么啊。"
    stop music fadeout 1
    "我、和那个家伙成为朋友真的好吗……。"
    show expression "img/BG62NA@2x.jpg" as bg_over zorder 2 with dissolve
    hide bg1 with dissolve
#BG_SWPC 0
#BG_PRI 1
#BG_PRI 0
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG63NA3@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG63NA3@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHA04"),"not F103==0","img/CH_MRA04A@2x.png","True","img/CH_MHA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE00_47"
#SE_VOLC 1,64
    hide bg1 with dissolve
    "回到房间里，果然智纱是一副发愣的表情，呆坐在那里。"
    voice "NCH06A_CH255"
    智纱 "「啊，回来了啊。究竟是怎么了？」"
    志雄 "「没事，什么事也没有。没关系，没关系」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRA02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHA02"),"not F103==0","img/CH_MRA02A@2x.png","True","img/CH_MHA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH256"
    智纱 "「是吗……？」"
    "智纱很担心地看着我这边。"
    "确实，突然从房间冲了出去，我刚才的行动是不是非常的奇怪啊……。"
    window hide
#SE_VOLC 1,(64/2)
    play music "BGM03"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHA01"),"not F103==0","img/CH_MRA01A@2x.png","True","img/CH_MHA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH257"
    智纱 "「啊，对了」"
    志雄 "「怎么了，智纱？」"
    voice "NCH06A_CH258"
    智纱 "「嗯。想起来有要做的事情了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHC01"),"not F103==0","img/CH_MRC01A@2x.png","True","img/CH_MHC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH259"
    智纱 "「志雄君。如果有空的话，有点事情想找你帮忙……可以吗？」"
    志雄 "「嗯，如果是我能办到的，就没问题」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE03_66"
    "到底是什么呢？"
    "我还在这么想着，智纱就去翻带来的旅行包了。从包里拿出来的，是一台笔记本电脑。"
    window hide
    hide bg1 with dissolve
#BG_SWPC 0
#BG_PRI 1
#BG_PRI 0
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/EXBG04N@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG63NA3@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZRB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZHB01"),"not F103==0","img/CH_ZRB01A@2x.png","True","img/CH_ZHB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE00_47"
#SE_VOLC 1,64
    hide bg1 with dissolve
    stop se
    "智纱把电脑放在桌子上打开，接上了电源。"
    voice "NCH06A_CH260"
    智纱 "「记得以前说过的、结乃要参加广播节目制作的投稿。所以呢，我就给她帮忙了」"
    "这么说来，我以前也听说过这个事情。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZRA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZHA03"),"not F103==0","img/CH_ZRA03A@2x.png","True","img/CH_ZHA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCH06A_CH261"
    智纱 "「其实呢，到截稿的时间已经不多了」"
#REMOVE_REEK_CHR 0
    志雄 "「哎？　那，你来旅行的话……」"
#REEK_CHR 0
    voice "NCH06A_CH262"
    智纱 "「虽然结乃说过让我别在意，快快乐乐地来旅行，但什么都不做果然还是不行」"
#REMOVE_REEK_CHR 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZRA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZHA01"),"not F103==0","img/CH_ZRA01A@2x.png","True","img/CH_ZHA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH263"
    智纱 "「所以呢，我决定在这边的时候，如果能找到空闲时间的话，也给广播节目出点主意」"
    "智纱真是守信啊……。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZRC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZHC04"),"not F103==0","img/CH_ZRC04A@2x.png","True","img/CH_ZHC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH264"
    智纱 "「所以呢……」"
    "智纱带着小小的不安，偷偷地看向我这边。"
    "都说明到这个地步了，智纱在期待着什么我也知道了。"
    志雄 "「好了，我知道了。那，我也来一起考虑广播的点子就好了吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZRC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZHC01"),"not F103==0","img/CH_ZRC01A@2x.png","True","img/CH_ZHC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH265A"
    智纱 "「嗯！　{w=3}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZRC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZHC02"),"not F103==0","img/CH_ZRC02A@2x.png","True","img/CH_ZHC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH265B"
    extend "……这样好吗？」"
    志雄 "「就这点事的话，小菜一碟了」"
    "作为一个广播爱好者来说，不如说我自己想要主动要求帮她的忙呢。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZRB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZHB02"),"not F103==0","img/CH_ZRB02A@2x.png","True","img/CH_ZHB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH266"
    智纱 "「太好了。有志雄君在的话，能顶一百个人呢」"
    志雄 "「我倒是不太清楚自己能起到多大的作用」"
    "对高兴得陶醉了的智纱，我苦笑着。"
    志雄 "「然后呢？广播的点子，要考虑些什么样的东西呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZRB06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZHB06"),"not F103==0","img/CH_ZRB06A@2x.png","True","img/CH_ZHB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH267"
    智纱 "「说的也是呢，果然还是需要那个栏目的企画，还有在里面所需要的素材吧」"
    志雄 "「嗯～，从这是浜咲ＦＭ的广播竞赛这一点来想，果然还是拿出来有地方特色的素材会更好啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZRA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZHA01"),"not F103==0","img/CH_ZRA01A@2x.png","True","img/CH_ZHA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE06_24"
    "从那开始，我和智纱就互相提出意见，商量了片刻，把想出的点子用文字处理软件整理了起来。"
    window hide
    stop se fadeout 1
#SE_VOLC 1,0
    stop music fadeout 1
#FADE_OUT 1
    hide lh0 with dissolve
#BG_SET_BACK 
#BG_INIC 1
#BG_COLC 1,0,0,0,128
    scene expression "img/NIMG01D@2x.png" as bg1 zorder 1
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
    stop se
    stop music fadeout 1
    "……。"
    "…………。"
    window hide
#BG_COLC 1,128,128,128,128
#EFF_STAC 0,CLOUD_D,EFF_NOSKIP
#SE_VOLC 1,255
#FADE_IN 1
    "考虑出来的点子，用手机短信发的话太多了。"
    "所以，我们拜托了稻穗先生，用工作人员用的网络线路，通过电子邮件，把数据发送给了春日同学。"
#MES "所以，我们拜托了稻穗先生，用工作人员用的网络线路，通过电子邮件，把数据发送给了春日同学。%K%P "
    window hide
#SE_VOLC 1,(64/2)
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    scene expression "img/BG63NA3@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZRA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZHA01"),"not F103==0","img/CH_ZRA01A@2x.png","True","img/CH_ZHA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE00_48"
#FADE_IN 1
    play music "OBGM17"
    voice "NCH06A_CH268"
    智纱 "「哈～，能用到网络实在太好了」"
    志雄 "「啊。不感谢稻穗先生可不行呢」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZRB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZHB02"),"not F103==0","img/CH_ZRB02A@2x.png","True","img/CH_ZHB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "给春日同学发送了邮件以后，我们回到了房间里。"
    "想出来的点子已经有足够多的量了，其中一定有能给春日同学的广播节目帮上忙的吧。"
    志雄 "「这么说来，和智纱一起聊广播的事情，真的是很少有啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZRB06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZHB06"),"not F103==0","img/CH_ZRB06A@2x.png","True","img/CH_ZHB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH269"
    智纱 "「啊，这么说来好像真是」"
    "总觉得好像就是和智纱拥有了共同的兴趣，刚才的这段时间，过得真开心。"
    志雄 "「啊……」"
    "我轻轻地打了一个哈欠。"
    "看了看表，时间已经相当晚了。"
    志雄 "「差不多该睡了吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZRB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZHB03"),"not F103==0","img/CH_ZRB03A@2x.png","True","img/CH_ZHB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH270"
    智纱 "「嗯」"
    "智纱也很困倦地点着头。"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 2
#BG_PRI 0
#BG_SETWC 0,2,BG63NA3,BG63NA6
    scene expression "img/BG63NA3@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MRA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MHA01"),"not F103==0","img/CH_MRA01A@2x.png","True","img/CH_MHA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#CHR_PAL_BGC 1,BG63NA6
#CHR_SET_BACK
#CHR_INIC 1
#CHR_PRIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LRA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LHA04"),"not F103==0","img/CH_LRA04A@2x.png","True","img/CH_LHA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    pause (32/32.0)
#SE_VOLC 1,(64/2)
#FADE_IN 1
    "刷了牙，做好了睡觉的准备，我和智纱钻进了各自的被窝里。"
    play sound "SE06_16"
#BG_ALP_SAVEC 0
#CHR_ALP_SAVEC 0
#BG_SWPC 0
    hide bg2 with dissolve
#CHR_COLC 0,64,64,64,128
#BG_PRI 0
#BG_PRI 2
#BG_ALPC 2,128
#SE_VOLC 1,64
    pause (16/32.0)
    scene expression "img/NIMG02D@2x.jpg" as bg_over zorder 2 with dissolve
    志雄 "「晚安」"
    voice "NCH06A_CH271"
    智纱 "「晚安」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with None
#FADE_IN 0
    "哈……。旅行的第一天。虽然说只有半天，今天也发生了很多事情啊。"
    "明天会怎么样呢。一定会有什么有意思的事情吧。我一边想着如果能那样就好了，一边睡……。"
    window hide
#SE_VOLC 1,128
    stop music fadeout 1
    play sound "SE03_46"
    pause (64/32.0)
    extend "……不着。"
#MES "……不着。%K%P  "
    "被子里，有什么在嘎吱嘎吱地动的感觉，是什么啊？"
    "睁开了闭着的眼睛。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
#BG_SET_BACK 
#BG_INIC 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XRB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XHB03"),"not F103==0","img/CH_XRB03A@2x.png","True","img/CH_XHB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter 520/640.0
    with dissolve
#CHR_COLC 0,64,64,64,128
#FADE_IN 1
#BG_ALP_AUTOC 1,96,0,F24
#BG_ALP_SAVEC 1
#BG_ALP_AUTOC 1,0,0,F24,8
#BG_ALP_SAVEC 1
    hide bg1 with dissolve
#BG_ALPC 1,128
    志雄 "「呃，智纱？」"
    window hide
    stop se
#SE_VOLC 1,64
    play music "BGM14"
    voice "NCH06A_CH272"
    智纱 "「嗯、嗯」"
    志雄 "「那～个，在干什么呢？」"
    "尽可能地装出平静的样子，问问她。"
    voice "NCH06A_CH273"
    智纱 "「夜、夜袭……」"
    "智纱满脸通红地回答着我。这孩子，知道自己说的话是什么意思吗？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XRA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XHA03"),"not F103==0","img/CH_XRA03A@2x.png","True","img/CH_XHA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCH06A_CH274"
    智纱 "「那、那个啊。莉莉丝她说，这样做志雄君会高兴的」"
#REMOVE_REEK_CHR 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XRB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XHB03"),"not F103==0","img/CH_XRB03A@2x.png","True","img/CH_XHB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH275"
    智纱 "「她说，恋人一起出去旅游的时候，不做这种事情是绝对不可能的……」"
    "……莉～莉～丝～～！"
    window hide
    stop music fadeout 1
#SE_VOLC 1,(64/2)
    show expression "img/BG63NA6@2x.jpg" as bg_over zorder 2 with dissolve
    "我慢慢地从被子里站起身来。"
    voice "NCH06A_CH276"
    智纱 "「要、要去哪里？志雄君？」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    show expression "img/BG62NA@2x.jpg" as bg1 zorder 1 with dissolve
#SE_VOLC 1,0
    play sound "SE00_47"
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
#BG_SWPC 0
    hide bg1 with dissolve
#BG_ALPC 1,128
#BG_PRI 0
#BG_PRI 1
    scene expression "img/BG62NA@2x.jpg" as bg0 with dissolve
#SE_WATC 0
    play music "OBGM13"
    "我取出了手机，拨了莉莉丝的号码。"
    window hide
    play sound "SE02_03"
    pause (16/32.0)
    play sound "SE02_03"
    pause (16/32.0)
    play sound "SE02_02L"
    pause (96/32.0)
    stop se
    voice "NCH06A_RI001_K"
    莉莉丝 "「喂喂」"
    志雄 "「莉莉丝！」"
    voice "NCH06A_RI002_K"
    莉莉丝 "「哇！？　干、干什么啊、突然这么大声！　不是把人吵醒了吗」"
    志雄 "「你给智纱灌输的到底是什么啊！？」"
    voice "NCH06A_RI003_K"
    莉莉丝"「灌输的？」"
#MESA A_CH_RI,NCH06A_RI003_K,"【りりす】「灌输的？」%K%P "
    voice "NCH06A_RI004_K"
    莉莉丝 "「……啊，那件事情啊」"
    "好像是思考了一下之后，终于从听筒那边，听到了莉莉丝想起来了一般的声音。"
    志雄 "「真是的，别连你也做和亨一样的事情啊」"
    voice "NCH06A_RI005_K"
    莉莉丝 "「呃。别把我跟那家伙相提并论」"
    "两人变得亲密了倒是挺不错，但还是希望她别受什么坏的影响。"
    志雄 "「这件事先回头再说，知道了吗！？　如果下次，你再给智纱灌输些什么奇怪的事情的话……」"
    voice "NCH06A_RI006_K"
    莉莉丝 "「什、什么啊？」"
    志雄 "「我就把你每天早晨起床时的样子到底有多糟糕，都告诉全班人」"
    莉莉丝 "「喂，等、等一{w=3}{nw}"
#MESA A_CH_RI,NCH06A_RI007_K,"【りりす】「喂，等、等一"
#VO_WAT VO_WAIT_START
    stop music fadeout 1
    play sound "SE02_03"
#MESX "├┤」%K%P"
    "我按了挂断键，把手机放回了口袋里。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    show expression "img/BG63NA6@2x.jpg" as bg1 zorder 1 with dissolve
#SE_VOLC 1,(64/2)
    play sound "SE00_47"
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
#BG_SWPC 0
#BG_ALPC 1,128
#BG_PRI 0
#BG_PRI 1
#SE_WATC 0
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_COLC 0,64,64,64,128
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LRA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LHA04"),"not F103==0","img/CH_LRA04A@2x.png","True","img/CH_LHA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "BGM13"
    voice "NCH06A_CH277"
    智纱 "「怎么了？」"
    志雄 "「没、没有！　什么事都没有。总，总之！」"
    志雄 "「莉莉丝就是在那信口开河的！　那家伙说的话，不用相信！」"
    "莉莉丝和亨。真是物以类聚人以群分啊……。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LRC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LHC04"),"not F103==0","img/CH_LRC04A@2x.png","True","img/CH_LHC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH278"
    智纱 "「嗯，是那样啊」"
    "智纱好像很失落地垂下了头。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LRC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LHC05"),"not F103==0","img/CH_LRC05A@2x.png","True","img/CH_LHC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH279"
    智纱 "「明明是好不容易才鼓起勇气的……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LRC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LHC02"),"not F103==0","img/CH_LRC02A@2x.png","True","img/CH_LHC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH280"
    智纱 "「还有泳装……」"
    志雄 "「泳装？」"
    "这么说来，在进浴室的时候，智纱为什么会穿着泳装的呢。"
    "智纱本来是不喜欢水的，带着泳装来这件事本来就很奇怪……。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LRC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LHC05"),"not F103==0","img/CH_LRC05A@2x.png","True","img/CH_LHC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH281"
    智纱 "「那件泳装，是莉莉丝跟我说让我带过来的。她说，就算不下水游泳，说不定能在什么别的地方用上的」"
    "什么别的地方啊！？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LRC03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LHC03"),"not F103==0","img/CH_LRC03A@2x.png","True","img/CH_LHC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH282"
    智纱 "「所以，就和莉莉丝一起去挑选……」"
    if F104:
        jump L_NCH06A_BRA03_A
#IF F104!0, GOTO L_NCH06A_BRA03_A
    jump L_NCH06A_BRA03_B
label L_NCH06A_BRA03_A:
    志雄 "「难道，和莉莉丝一起去买东西就是为了这个？」"
    "智纱点了点头。"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    scene expression "img/BG79AA@2x.jpg" as bg2 zorder 8 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LNA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LDA03"),"not F103==0","img/CH_LNA03A@2x.png","True","img/CH_LDA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2,(320-160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SCA03"),"True","img/RI_SCA03A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
        xcenter .25
    with dissolve
#SE_VOLC 1,0,16
#MUS_VOL 64,16
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 0
#BG_ALPC 2,128
#CHR_ALPC 0
#CHR_ALPC 1,128
#CHR_ALPC 2,128
    "那个时候，智纱拿着的纸袋里面放着的也许就是泳装。"
    window hide
#BG_INIC 1
#BG_PRI 1
    scene expression "img/BG63NA6@2x.jpg" as bg0 with dissolve
    hide bg2 with dissolve
    hide lh1 with dissolve
    hide lh2 with dissolve
#BG_UVC 2,0,0,640,448
#BG_ALPC 0,128
#CHR_ALPC 0,128
#SE_VOLC 1,(64/2)
#MUS_VOL 128
    hide bg1 with dissolve
    jump L_NCH06A_BRA03_X
label L_NCH06A_BRA03_B:
    "这么说来……。"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG02EA@2x.jpg" as bg2 zorder 8 with dissolve
#SE_VOLC 1,0,16
#MUS_VOL 64,16
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 0
#BG_ALPC 2,128
#CHR_ALPC 0
    voice "NCH05A_RI008_KK"
    莉莉丝 "「又不是你，智纱的话才不用担心呢。还有我那美妙的建议在……你就期待着吧，呵呵」"
    window hide
#BG_INIC 1
#BG_PRI 1
    scene expression "img/BG63NA6@2x.jpg" as bg0 with dissolve
    hide bg2 with dissolve
#BG_UVC 2,0,0,640,448
#BG_ALPC 0,128
#CHR_ALPC 0,128
#SE_VOLC 1,(64/2)
#MUS_VOL 128
    hide bg1 with dissolve
    "旅行的前一天，给智纱打电话的时候，莉莉丝说过那样的话。"
    "她说的『万事俱备』『你就期待着吧』，指的是这回事么……。"
    jump L_NCH06A_BRA03_X
label L_NCH06A_BRA03_X:
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LRC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LHC02"),"not F103==0","img/CH_LRC02A@2x.png","True","img/CH_LHC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH283"
    智纱 "「可是结果，还是没有去游泳……」"
    "所以就穿着泳装……。"
    "特地买来的泳装，智纱一定是抱着希望让我看看的心情吧。"
    "但是，不论是偷偷潜入被窝里，还是在浴室做的那件事，感觉在方向上都错得太离谱了。"
    "不对，使她做错了的人，是莉莉丝。"
    "但是，就这样下去不管，智纱的心情可能会越来越低落了。"
    "突然，智纱手里拿着的东西进入了我的视线。是狗的玩偶。"
    志雄 "「智纱，那个是？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LRC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LHC05"),"not F103==0","img/CH_LRC05A@2x.png","True","img/CH_LHC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH284"
    智纱 "「这个？」"
    "智纱的视线落在了玩偶上。"
    window hide
#BG_SET_BACK 
#ROUTINE_STA
#BG_UV_AUTOC 0,(640/8),(448/8),((640/4)*3),((448/4)*3),1,0
#CHR_POS_AUTOC 0,320,-100,1,0
#CHR_SCL_AUTOC 0,320,320,1,0
#BG_INIC 1
    show expression "img/NIMG05A@2x.png"  zorder 100 as bg1 with dissolve
#ROUTINE_STP
    voice "NCH06A_CH285"
    智纱 "「这个，是和莉莉丝一起去商场的时候买的枕头。那个，就是去买泳装的时候」"
    "不是玩偶是枕头吗。"
    "智纱把手放在玩偶的头上，让它点头向我行礼。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LRB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LHB01"),"not F103==0","img/CH_LRB01A@2x.png","True","img/CH_LHB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#QUA_BG_VERT 1
    voice "NCH06A_CH286"
    智纱 "「初次见面～狗。我连同智纱一起，也请你多多关照了～狗」"
    "句尾是『狗』吗。不应该是『汪』之类的吗。"
    "犬枕……不用你说，我也会和智纱顺利地相处下去的。我这边才是，请多关照。"
    志雄 "「我、我才是要请多关照」"
    window hide
    hide bg1 with dissolve
#ROUTINE_STA
#BG_UV_AUTOC 0,0,0,640,448,1,0
#CHR_POS_AUTOC 0,320,0,1,0
#CHR_SCL_AUTOC 0,200,200,1,0
#ROUTINE_STP
    志雄 "「智纱你，真的是很喜欢狗啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LRB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LHB02"),"not F103==0","img/CH_LRB02A@2x.png","True","img/CH_LHB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH287"
    智纱 "「嗯……」"
    "智纱很不好意思地点着头。"
    "嘛，如果说莉莉丝是反复无常的猫的话，那智纱的形象就像聪明乖巧的狗一样了。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XRB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XHB04"),"not F103==0","img/CH_XRB04A@2x.png","True","img/CH_XHB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_BLUR 0
    "轻轻地把手放到了智纱的头上。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XRB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XHB03"),"not F103==0","img/CH_XRB03A@2x.png","True","img/CH_XHB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「这次的旅行，能来太好了」"
    voice "NCH06A_CH288"
    智纱 "「是、是吗？」"
    志雄 "「嗯。因为我见到了很多以前不知道的智纱的另一面」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_XRA06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_XHA06"),"not F103==0","img/CH_XRA06A@2x.png","True","img/CH_XHA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH289"
    智纱 "「……嗯」"
    "抚摸着智纱的头。虽然她很不好意思把头低了下去，却一点没有不快地对我微微一笑。"
    "嗯，虽说发生了很多很多的麻烦，但最后能看到智纱的笑容，真是太好了。"
    "明天会是怎样的一天呢……。"
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
#label THREAD_ROCK_SHIN
#NCH06A3_EFFECT
#EOT
#label THREAD_SHIN_IN
#CHR_POS_AUTOC 0,(320-160),F123,48
#CHR_POS_AUTOC 1,(320+160),F123,48
#CHR_ALP_AUTOC 1,128,1,F123,48
#CHR_POS_SAVEC 0
#CHR_POS_SAVEC 1
#CHR_ALP_SAVEC 1
#EOT