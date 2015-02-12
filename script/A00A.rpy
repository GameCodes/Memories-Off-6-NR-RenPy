label A00A:
    $currentlabel = "A00A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
#label DSTART
#label START
    $month = '07'
    $day = '17'
    $date = '1'
    window hide
#FADE_OUT 0,0
#GRAPH_ERS 
#BG_SET_BACK 
#BG_INIC 0
#BG_SETC 0,NIMG03A
    scene expression Solid("000") with None
    play se "SE05_14L"
#BG_COLC 0,0,0,0,128
#WAIT 32
#FADE_IN 0,0
#TITLE_DSP
#MESLOG_TITLE
    window hide
#FADE_OUT 0,0
#BG_COLC 0,128,128,128,128
#CHR_PAL_BGC ID_ALL,BG15MA
#THREAD_STA 1,THREAD_INIT_SOUND
#FADE_IN 1,128
#ROUTINE_STA
#BG_INIC 1
#BG_SETC 1,BG_BLACK
#BG_ALPC 1,0
#ROUTINE_STP
    play sound "SE00_39"
    pause 4
    play sound "SE00_40"
    show expression "img/NIMG03A@2x.jpg" as bg0 zorder 0
    show expression "img/black@2x.png" as bg1 zorder 1:
        alpha 1
        linear 1 alpha 0
        linear 1 alpha 0.5
        linear 1 alpha 0
        linear 1 alpha 1
    pause 4
    hide bg1
    with ImageDissolve("img/BG_MASK17@2x.png",2,ramp_len=128)
    if persistent.autosave_scene:
        python:
            renpy.take_screenshot()
            savestr="auto-"+str(persistent.auto_slot)
            renpy.save(savestr)
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#BG_ALP_AUTOC 1,64,0,1,64,1
#BG_ALP_AUTOC 1,0,0,1,64,1
#BG_ALP_AUTOC 1,128,0,1,64,1
#BG_ERSC 1,BG_MASK17,5
    "……呃……怎么了？外面怎么这么吵。"
    "嗯，不过听起来不是我家的样子，所以直接无视它好了……"
    window hide
    show expression Solid("000") as bg1
    with fade
#FADE_OUT 1,64
#SE_WATC 0
#WAIT2 32
#BG_COLC 0,0,0,0,128
#FADE_IN 0,0
    play sound "SE00_41"
    voice "A00A_RI000"
    莉莉丝 "「老师！是时候起床了！还活着的话请答应一声！」"
    voice "A00A_RI001"
    莉莉丝 "「截稿的时间到了哦！已经是早晨了！」"
    "是莉莉丝吗……真是的，也不稍微为周围的住户考虑一下啊。"
    "莉莉丝显然知道楼上就是我的房间。"
    "总之，作为我的青梅竹马，她对待我也向来如此罢了。"
    window hide
#FADE_OUT 0,0
#BG_COLC 0,128,128,128,128
#FADE_IN 1,64
    hide bg1
    with fade
    voice "A00A_SI000"
    志雄 "「唔啊啊啊啊……真是没办法啊……明明才这个时候呢……」"
    "看了一眼手表确认时间，我就又把头完全缩进了被窝里。"
    window hide
    window hide
    show expression Solid("000") as bg1
    with fade
#FADE_OUT 1,64
#BG_COLC 0,0,0,0,128
#FADE_IN 0,0
    show expression "img/NIMG15A-568h@2x.jpg" as cal zorder 5
    show expression "img/07_17_MONDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
    "今天是星期一，但是由于是法定节假日，所以不用去学校也没什么关系。"
    "虽然说学生会那边总有不得不过目的文件……不过，拖到明天再去做也没有多大问题啦。"
    "谁也别想来打扰我，我要尽情享受这美妙而舒适的宝贵假期。"
    voice "A00A_RI002B"
    莉莉丝 "「老～师～！」"
    window hide
    play sound "SE00_42"
#WAIT 16
    "……唔？"
    window hide
    pause 2
#SE_WATC 0
    play sound "SE00_43"
    pause 2
    play sound "SE03_46"
    pause 2
    hide bg1
#FADE_OUT 0,0
#BG_COLC 0,160,160,160,128
#SE_VOLC 1,0,64
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ANGC 1,512
##CHR_SCLC 1,448,448
    
#CHR_COLC 1,80,80,80,128
#CHR_POSC 1,(320),-110
#CHR_SETC 1,SU_ZDC05
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC05"),"True","img/SU_ZDC05A@2x.png") as lh1 zorder (10-1):
        pos (-110,-500)
        rotate 180
    with dissolve
#SE_WATC 0
    play sound "SE03_90"
#FADE_IN 1,8
    play music "OBGM13"
    voice "A00A_SI001"
    志雄 "「你……！？」"
    hide lh1
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC05"),"True","img/SU_ZDC05A@2x.png") as lh0 zorder (10-1):
        pos (-110,-500)
        rotate 180
        linear 1 ypos -1000
        yanchor 0.0
        ypos 1.0
        rotate 0
        linear 1 ypos -0.5
    $F25=64
#BG_COL_AUTOC 0,128,128,128,128,,1,F24,48,1
#CHR_POS_AUTOC 1,,-640,1,F24,48,1
#WAIT 16
#CHR_POS_SAVEC 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ANGC 1,0
#CHR_SCLC 1,315,315
#CHR_POSC 0,(320),640
    pause 4
    hide lh0 with None
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC05"),"True","img/SU_ZDC05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#CHR_POS_AUTOC 0,,0,1,F24,50,1
#WAIT 16
    pause 2
    voice "A00A_SI002"
    志雄 "「……你究竟在做什么？」"
    window hide
    show expression Solid("000") as filter zorder 5:
        alpha 0.5
    with dissolve
#FILT_PRI 5
#FILT_IN 48,0,COL_DARK2
    "不仅毫无征兆的从窗户入侵，外加钻进我的被窝的这个人是小说家铃代黎音，本名稻穗铃，现在租住在我楼下的房间里。"
    "这么说来，昨天，作为铃代黎音超级粉丝的莉莉丝有说过早上会来。"
    "因为昨天晚上是铃代黎音新作的截稿日，大概是约好了让她做第一个读者吧……"
    "……好吧，从现在的情形看，不会错了，铃肯定又拖稿了。"
    window hide
    hide filter with dissolve
#SE_STPC 0,64
#FILT_OUT 48
#FILT_PRI 1
    voice "A00A_SU000"
    铃 "「早安实在抱歉如你所见到的因为是突发状况所以之后再好好感谢你现在我打算暂时藏在这里不管怎么样希望你帮帮我吧……」"
    voice "A00A_SI003"
    志雄 "「就算你说藏起来……」"
    voice "A00A_SU001"
    铃 "「你就这样安静下来，不要发出任何声音就好了，什么问题也不会有的！」"
    voice "A00A_SI004"
    志雄 "「当然有问题啊！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDA04"),"True","img/SU_ZDA04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_SU002"
    铃 "「是的……也要充分考虑她找到这个房间的可能性……」"
    voice "A00A_SI005"
    志雄 "「不是！我不是说这个……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC05"),"True","img/SU_ZDC05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_SU003"
    铃 "「明白了，那这样，我就这样在这个被子里屏住呼吸，你代替我从这里溜出去，怎么样？我觉得是个不错的主意……」"
    voice "A00A_SI006"
    志雄 "「别再发神经了！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC02"),"True","img/SU_ZDC02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_SU004"
    铃 "「啊……对不起……」"
    voice "A00A_SI007"
    志雄 "「呵…呵呵……知道了就好。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC06"),"True","img/SU_ZDC06A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_SU005"
    铃 "「既然上了床，至少也要穿着更暴露一点的睡衣对吧……？」"
#MUS_VOL 0,32
#SE_VOLC 1,(64/2),64
    voice "A00A_SI008"
    志雄 "「不！对！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB04"),"True","img/SU_ZDB04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_SU006"
    铃 "「嘘——」"
    voice "A00A_SI009"
    志雄 "「搞什么，还用一副『认真思考』的表情说出这种话！　总之，请不要硬是把我卷进这场无端的麻烦里！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC02"),"True","img/SU_ZDC02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_SU007"
    铃 "「拜托你了……我想尽可能稳妥的搞定。」"
    voice "A00A_SI009B"
    志雄 "「……这么说的话，我的肘部已经快到极限了，请放开吧，真的很痛唉！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC03"),"True","img/SU_ZDC03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#SET_SAVPNT
    voice "A00A_SU008A"
    铃 "「作为一名成年女性，也有各种各样的癖好哦……{w=3.5}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC05"),"True","img/SU_ZDC05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_SU008B" 
    extend "比如，这样地碰上胸部……"
#CLR_SAVPNT
    voice "A00A_SI010"
    志雄 "「别，别，不要这样啊！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC01"),"True","img/SU_ZDC01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#SE_VOLC 1,0,64
#MUS_VOL 128,64
    play sound "SE00_40"
    voice "A00A_RI003"
    莉莉丝 "「真～是～的～还没有起床么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB04"),"True","img/SU_ZDB04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_RI004"
    莉莉丝 "「真是没办法啊……唉？顺便也去把志雄叫起来吧。」"
#SE_STPC 0,32
    voice "A00A_SI011"
    志雄 "「还不快点逃吗？这下可是真要麻烦了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC04"),"True","img/SU_ZDC04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_SU009"
    铃 "「呃……」"
#SET_SAVPNT
    voice "A00A_SI012"
    志雄 "「喂～莉莉{w=2}{nw}"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDB04"),"True","img/SU_ZDB04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    extend "……」"
#CLR_SAVPNT
    voice "A00A_SU010"
    铃 "「！！」"
    "话还没说完，铃便立刻用手死死的捂住我的嘴。"
    "真是的，这么有闲情逸致来折腾我，不如赶紧去写稿子了好不好。"
    play sound "SE00_44"
    voice "A00A_RI005"
    莉莉丝 "「志雄～起床了吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZDC05"),"True","img/SU_ZDC05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    "真是没办法啊……"
    scene expression "img/BG15MA@2x.jpg" as bg0 zorder 0
    with dissolve
    "保持着嘴被铃结实捂着的姿势，慢慢坐起身来。"
    "虽然说也没什么事急着去做，但是一直这样下去也不是个事情。"
#SET_SAVPNT
    "接下来该怎么办呢……"
    if persistent.autosave_choice:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#SELECT 5,HINT_NULL
    menu:
        "让莉莉丝进到屋子里来":
            $F7=0
        "联系一会儿要来的智纱":
            $F7=1
        "看一眼克罗艾学姐的短信":
            $F7=2
        "试着紧紧盯着铃看":
            $F7=3
        "打电话向结乃求助":
            $F7=4
#CLR_SAVPNT
    if F7==0:
        jump L_A00A_SEL00_A
    if F7==1:
        jump L_A00A_SEL00_B
    if F7==2:
        jump L_A00A_SEL00_C
    if F7==4:
        jump L_A00A_SEL00_D
    if F7==3:
        jump L_A00A_SEL00_E
label L_A00A_SEL00_A:
    $F16=1
    voice "A00A_SI013"
    志雄 "「那个，有件事忘了和你说了……」"
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XDC04"),"True","img/SU_XDC04A@2x.png") as lh0 zorder 10:
        ypos 0.0
    with dissolve
    voice "A00A_SU011"
    铃 "「……？」"
    voice "A00A_SI014"
    志雄 "「莉莉丝她有这房子的钥匙。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XDB04"),"True","img/SU_XDB04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_SU012"
    铃 "「！？」"
    voice "A00A_SI015"
    志雄 "「所以说，不快点逃的话……」"
    window hide
    play sound "SE03_28"
#CHR_ERS_F ,1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320),0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDC04"),"True","img/SU_MDC04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#SE_WATC 0
    voice "A00A_SU013"
    铃 "「这种事情你早说啊！」"
    window hide
    stop music
    hide lh0 with dissolve
#SE_VOLC 1,64,32
    play sound "SE00_42"
#SE_VOLC 1,0,32
    play sound "SE00_43"
    "话音未落，铃已然撒开手，身轻如燕地从窗户翻了出去。"
    "不过想想看的话……"
    window hide
#SE_VOLC 1,64,32
    play sound "SE00_42"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96),0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SDC01"),"True","img/SU_SDC01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xpos -320+96
    with dissolve
#SET_SAVPNT
    voice "A00A_SU014A"
    铃 "「塚本也真是挺让人意外的嘛。下次要好好讲给姐姐听哦。{w=8}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SDB01"),"True","img/SU_SDB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xpos -320+96
    with dissolve
    voice "A00A_SU014B"
    extend "啊，放心吧。绝对不会用在小说里的～」"
#CLR_SAVPNT
    voice "A00A_SI016"
    志雄 "「……百分之一百会用的吧，你赶紧回去吧！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SDB02"),"True","img/SU_SDB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xpos -320+96
    with dissolve
    voice "A00A_SU015"
    铃 "「啊哈哈哈哈～」"
    window hide
    hide lh0 with dissolve
#SE_VOLC 1,0,32
    play sound "SE00_43"
    "真是个过分到无解的房客。"
    "就在我深深地叹了一口气的瞬间，莉莉丝进入了房间。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96),0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC05"),"True","img/RI_MBC05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xpos -(320-96)
    with dissolve
    play music "BGM02"
    voice "A00A_RI006"
    莉莉丝 "「诶？已经起来了啊？」"
    voice "A00A_SI017"
    志雄 "「……谁让某人吵得那么厉害」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBC02"),"True","img/RI_MBC02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_RI007"
    莉莉丝 "「有什么不行的，女生的ＭｏｒｎｉｎｇＣａｌｌ对志雄来说简直是浪费呢！」"
    voice "A00A_SI018"
    志雄 "「要是能更温柔一些的话，就是个贤淑的好女生了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD06"),"True","img/RI_MBD06A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_RI008"
    莉莉丝 "「诶……你说什么呢～」"
    "莉莉丝的眼中闪烁着锐利的光芒。同时我立刻就预感到了下一个动作。"
    "来了！莉莉丝的闪电光速踢！"
#SE_VOLC 1,(64/4),32
    "不过！"
    "我也不会再像以前似的永远被当做靶子一样踢了！我已经看穿了！"
#SE_STPC 1,32
    show expression "img/RI_LIE01A@2x.png" as lh0 zorder (10-0):
        ypos (0.0)
    with dissolve
#SET_SAVPNT
    play sound "SE04_09"
#THREAD_STA 1,THREAD_SI_HIRARI
#THREAD_WAT 1
    voice "A00A_SI019"
    志雄 "「太天真了！」"
#MESX "%K%P"
#CLR_SAVPNT
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD06"),"True","img/RI_LBD06A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_RI009"
    莉莉丝 "「天真的是你！」"
    window hide
#CHR_ERSA ,0
#CHR_INIC 0
    #hide lh0,RI_XIE01,(320)
    #show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CHR'",DynamicDisplayable(mouthanime,"CHR_OUTIN"),"True","img/CHR_OUTINA@2x.png") as lh0,RI_XIE01,(320) zorder 100:
    #    ypos 0.0
    #with dissolve
    show expression "img/RI_LIE01A@2x.png" as lh0 zorder (10-0):
        xcenter 0.5
        ypos (0.0)
    with dissolve
    play sound "SE04_08"
    pause 1
    with vpunch
#QUA_ALL 
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBD05"),"True","img/RI_XBD05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_RI010"
    莉莉丝 "「哼……又踢了无聊的东西呢～」"
    voice "A00A_SI020"
    志雄 "「一，一开始的攻击是佯攻吗……莉莉丝你有两下子嘛……」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SDC01"),"True","img/SU_SDC01A@2x.png") as lh1 zorder (10-1):
        ypos 0.2
        xcenter 0.5
        linear 1.0 xcenter 0.25
    with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1,0
#CHR_POSC 1,(320),0
#CHR_SETC 1,SU_SDC01
#CHR_BLUR 1,2
#MOV_CHR_INIT 64
#MOV_CHR0 ,(320+0)
#MOV_CHR1 128,(320-180)
#MOV_CHR_GO 1
    voice "A00A_SU016"
    铃 "「……喂，滑稽小短剧差不多该结束了吧，在这里应该插入甜美的亲热场景才对。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBA03"),"True","img/RI_XBA03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#BG_BLUR 0,0
#CHR_BLUR 1,0
    voice "A00A_RI011"
    莉莉丝 "「老师！？」"
    voice "A00A_SI021"
    志雄 "「铃！？你回来干吗！？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SDB02"),"True","img/SU_SDB02A@2x.png") as lh1 zorder (10-1):
        ypos 0.2
    with dissolve
    voice "A00A_SU017A"
    铃 "「嘛，我觉得看看你们说不定能想出什么好的桥段来。{w=5.5}{nw}"
#SET_SAVPNT
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SDC06"),"True","img/SU_SDC06A@2x.png") as lh1 zorder (10-1):
        ypos 0.2
    with dissolve
    voice "A00A_SU017B"
    extend "你们错过了晨吻的话，难道现在不应该{w=4}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SDC01"),"True","img/SU_SDC01A@2x.png") as lh1 zorder (10-1):
        ypos 0.2
    with dissolve
    voice "A00A_SU017C"
    extend "深情地拥抱一下吗？」"
#CLR_SAVPNT
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBA02"),"True","img/RI_XBA02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_SI022"
    志雄 "「才不会呢！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SDB01"),"True","img/SU_SDB01A@2x.png") as lh1 zorder (10-1):
        ypos 0.2
    with dissolve
    voice "A00A_SU018"
    铃 "「诶诶，不用那么害羞嘛，有什么不好的。又不会少块肉，被人看到的话也会很兴奋的～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBA05"),"True","img/RI_XBA05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_SI023"
    志雄 "「没人想听铃你的个人兴趣！」"
    hide lh0 with dissolve
#CHR_POSC 0,(320),0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SBD04"),"True","img/RI_SBD04A@2x.png") as lh0 zorder (10-0):
        ypos 0.2
    with dissolve
    voice "A00A_RI012"
    莉莉丝 "「……话说回来，老师，原稿呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SDB04"),"True","img/SU_SDB04A@2x.png") as lh1 zorder (10-1):
        ypos 0.2
    with dissolve
    voice "A00A_SU019A"
    铃 "「……！糟糕了！　{w=2}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SDB05"),"True","img/SU_SDB05A@2x.png") as lh1 zorder (10-1):
        ypos 0.2
    with dissolve
    voice "A00A_SU019B"
    extend "再见了二位！后会有期！」"
#VO_WAT VO_WAIT_START
    play sound "SE01_00B"
    hide lh1 with dissolve
#MESX "%K%P"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SBD02"),"True","img/RI_SBD02A@2x.png") as lh0 zorder (10-0):
        ypos 0.2
    with dissolve
    voice "A00A_RI013"
    莉莉丝 "「啊，等、等等！」"
    "铃立刻从窗户……不对，是门庭的方向逃走了"
    "那家伙短时间里不会回来了吧……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA05"),"True","img/RI_LBA05A@2x.png") as lh0 zorder (10-0):
        ypos 0.2
    with dissolve
    voice "A00A_RI014"
    莉莉丝 "「等等志雄，果然老师躲在这里了吗！？」"
    voice "A00A_SI024"
    志雄 "「不是！是误会，误会！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD02"),"True","img/RI_LBD02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_RI015"
    莉莉丝 "「多说无益！」"
    window hide
    stop music
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LIE01"),"True","img/RI_LIE01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE04_07"
    pause 1
    with vpunch
#ROUTINE_STA
#QUA_ALL 
#FADE_OUT 1,32
#ROUTINE_STP
#FADE_WAT 1,
#CHR_ERSA CHR_NOFADE,0
#BG_COLC 0,0,0,0,128
#FADE_IN 1,32
#SE_WATC 0
#MUS_WAT 
    scene expression Solid("000") with dissolve
    play music "BGM14"
    "回头想想的话，从那时起，不知不觉已经过了１年了。"
    "虽然期间发生了很多事，不过感觉就像弹指一瞬。"
    "无论是开心的时间，还是有着些许悲伤的回忆，转身望去，都已经被夕阳涂上了柔软的暖色。"
    "从那时候起，莉莉丝一直陪伴在我的身边。"
    stop music fadeout 1
#MUS_STP 128
    "……不过，我们的关系其实并没有实质的改变……一如既往。"
    window hide
    stop sound fadeout 1
    stop se fadeout 1
#SE_STPC 0,64
#SE_STPC 1,64
    stop music
    scene expression Solid("000") with fade
#FADE_OUT 1,128
#GRAPH_ERS 
#GRAPH_INI 
#SE_STPC 0
#SE_STPC 1
#MUS_STP 
#FADE_IN 0,0
    jump L_A00A_SEL00_X
label L_A00A_SEL00_C:
    $F16=3
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XDC05"),"True","img/SU_XDC05A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "A00A_SI025"
    志雄 "「我会跟莉莉丝说你昨晚去和编辑开会，然后直接就被关在编辑部了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XDB01"),"True","img/SU_XDB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_SU020"
    铃 "「哦，这是个相当棒的借口啊。你已经可以当作家了呢。」"
    voice "A00A_SI026"
    志雄 "「我才不想要那种才能呢，总之你快逃吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XDB02"),"True","img/SU_XDB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#SET_SAVPNT
    voice "A00A_SU021A"
    铃 "「知道了啦知道了啦。{w=2}{nw}"
#CHR_ERS_F 
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320),0
    #show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CHR'",DynamicDisplayable(mouthanime,"CHR_OUTIN"),"True","img/CHR_OUTINA@2x.png") as lh0,SU_MDC01 zorder (10-0,SU_MDC01)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDC01"),"True","img/SU_MDC01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_SU021B"
    extend "那就打扰了哦，下次脱身还靠你了哦～」"
#CLR_SAVPNT
    voice "A00A_SI027"
    志雄 "「……你饶了我吧！」"
    window hide
    stop music
    hide lh0 with dissolve
#CHR_ERS_F 
#SE_VOLC 1,(64/2),32
    play sound "SE00_42"
#SE_STPC 1,32
    play sound "SE00_43"
    "呼……终于走了。"
    "拜她所赐我已经完全清醒了。"
    "我伸手拿起放在枕边的手机，打开收件箱。"
    "在里面，有许多她发来的短信，整整齐齐地排列着。"
    "其中也有几条附带照片的，翻看着那时常看到的笑容，我不禁微微地笑了笑。"
    window hide
    play music "BGM14"
    "回头想想的话，从那时起，不知不觉已经过了１年了。"
    "虽然期间发生了很多事，不过感觉就像弹指一瞬。"
    "无论是开心的时间，还是有着些许悲伤的回忆，转身望去，都已经被夕阳涂上了柔软的暖色。"
    "而从那时起，一直陪伴着我的是……"
    window hide
#SE_STPC 1,64
    stop music
    scene expression Solid("000")
    with dissolve
#FADE_OUT 1,32
#CHR_ERSA CHR_NOFADE,0
#BG_COLC 0,0,0,0,128
#FADE_IN 0,0
#SE_STPC 1
#MUS_WAT 
    "克罗艾学姐……"
    window hide
#SE_STPC 0,64
#SE_STPC 1,64
    stop music
    scene expression Solid("000") with fade
#FADE_OUT 1,128
#GRAPH_ERS 
#GRAPH_INI 
#SE_STPC 0
#SE_STPC 1
#MUS_STP 
#FADE_IN 0,0
    jump L_A00A_SEL00_X
label L_A00A_SEL00_D:
    $F16=4
    window hide
    stop music
    play sound "SE02_03"
    pause 1
#WAIT 32
    play sound "SE02_03"
    pause 1
#WAIT 24
    play sound "SE02_03"
    pause 1
#WAIT 32
    play sound "SE02_02L"
    "我伸手拿起手机，拨出了通讯录里最前面的那个号码。"
    window hide
    play sound "SE02_08"
    play music "OBGM11"
    voice "A00A_YU000_K"
    结乃 "「喂喂？　怎么了，这么早的说……」"
    voice "A00A_SI028"
    志雄 "「救，救救我……我，我快支持不住了……」"
    voice "A00A_YU001_K"
    结乃 "「学长！？　发生什么事了？」"
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XDC01"),"True","img/SU_XDC01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
#SET_SAVPNT
    voice "A00A_SU022A"
    铃 "「啊，早上好结乃，正如你所听到的，塚本我先收下了。{w=5}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XDC05"),"True","img/SU_XDC05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_SU022B"
    extend "想让我还给你的话，就要看门外的莉莉丝她怎么表现了。」"
#CLR_SAVPNT
    voice "A00A_SI029"
    志雄 "「适可而止吧！　干嘛随便打断别人的电话？」"
    voice "A00A_YU002_K"
    结乃 "「……学～长～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XDB02"),"True","img/SU_XDB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_SI030"
    志雄 "「不是你想的那样！　早上铃她自己翻阳台跑到我这里来的！」"
    voice "A00A_YU003_K"
    结乃 "「唉？　很开心的样子呢，没关系，我完全没有在意哦～」"
    voice "A00A_SI031"
    志雄 "「所，所以说不是啦！」"
    voice "A00A_YU004_K"
    结乃 "「……花心大萝卜。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XDB03"),"True","img/SU_XDB03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    voice "A00A_SI032"
    志雄 "「不！　是！　啊！」"
    window hide
#SE_STPC 1,64
    stop music
#FADE_OUT 1,32
#CHR_ERSA CHR_NOFADE,0
#BG_COLC 0,0,0,0,128
#FADE_IN 0,0
#SE_STPC 1
#MUS_WAT 
    scene expression Solid("000") with dissolve
    play music "BGM14"
    "回头想想的话，从那时起，不知不觉已经过了１年了。"
    "虽然期间发生了很多事，不过感觉就像弹指一瞬。"
    "无论是开心的时间，还是有着些许悲伤的回忆，转身望去，都已经被夕阳涂上了柔软的暖色。"
    "而从那时起，一直陪伴着我的是……"
    window hide
#SE_STPC 0,64
#SE_STPC 1,64
    stop music
    
#FADE_OUT 1,128
#GRAPH_ERS 
#GRAPH_INI 
#SE_STPC 0
#SE_STPC 1
#MUS_STP 
#FADE_IN 0,0
    jump L_A00A_SEL00_X
label L_A00A_SEL00_B:
    $F16=2
    "对了，今天智纱要过来呢。"
    "总之先联系一下吧。"
    "这场骚乱之后整理装束的时间是肯定没有了。"
    "正当我这么想的时候……"
    jump L_A00A_SEL00_X
label L_A00A_SEL00_E:
    stop music
    $F16=5
    jump L_A00A_SEL00_X
label L_A00A_SEL00_X:
    scene expression Solid("000") with dissolve
    stop se
    stop sound
    $ renpy.end_replay()
    return

