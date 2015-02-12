label NSU06A:
    $currentlabel = "NSU06A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '25'
    $date = '2'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_BG NIMG15K,CAL_0725
    show expression "img/NIMG15K-568h@2x.jpg" as cal zorder 5
    show expression "img/07_25_TUESDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG15AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG15AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_15L"
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
    志雄 "「唔……呼啊啊啊啊啊……」"
    "大大地伸了个懒腰，睁开眼睛一看，早已是日上三竿的时间了。"
    "今天学生会没有什么要事，就没有上闹钟。事先也告诉过铃不用过来准备早饭，所以能尽情地睡个痛快。"
    志雄 "「好渴啊……」"
    window hide
    stop sound fadeout 1
    show expression "img/BG33AA@2x.jpg" as bg_over zorder 2 with dissolve
    play sound "SE03_74"
    "我走进厨房，一口气喝干了泡好的麦茶。"
    play sound "SE03_20"
    "口渴缓和的同时，饥饿的感觉顿时袭来。"
    "可现在做饭的话也太麻烦了啊……"
    志雄 "「现在的话……」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with None
    play sound "SE03_05"
#FADE_IN 0
    "我稍稍冲了个澡，换好衣服便准备到店里去。"
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG16AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG16AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_15L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,128
    志雄 "「吃什么好呢……」"
    "天气很热，还是吃中华冷面吧……虽然上次已经吃过了……"
    "我正思索着这些事情，就听到了从店中传来熟悉的声音。"
    window hide
#SE_VOLC 1,(64/2)
    play music "OBGM14"
    voice "NSU06A_SU000"
    铃 "「那种事情绝对不可能！」"
    voice "NSU06A_SN000"
    信 "「不不不，我看见了哦，老姐把他拉过来时他慌慌张张的样子」"
    voice "NSU06A_SU001"
    铃 "「才不是那样的呢，我只是想好好地约会一次啊。喂，莉莉丝也是这么想的吧？」"
    voice "NSU06A_RI000"
    莉莉丝 "「那个，那好像并不是“普通”的感觉吧……」"
    voice "NSU06A_SN001"
    信 "「看吧看吧！老姐你是营造不了那种甜蜜气氛的。哎，他也真可怜呢」"
    "不用确认，稻穗和铃他们俩姐弟间的吵架已经白热化了。"
    "而且，不管怎么看都似乎有我和铃的原因。"
#CHR_PRIC ID_ALL
#BG_OVER_CHRTC BG17AA1,0,SU_MAC03,(320-224),1,SN_MAB02,(320),2,RI_MBB06,(320+192)
    scene expression "img/BG17AA1@2x.jpg" as bg0 with dissolve
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAC03"),"True","img/SU_MAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-224)/640.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MAB02"),"True","img/SN_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter 320/640.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBB06"),"True","img/RI_MBB06A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter (320+192)/640.0
    with dissolve
    "看来进不去了……但是就这么站在门口发呆也有点……"
    voice "NSU06A_SU002"
    铃 "「吵死了！再说，你光顾说我的事，自己又怎么样呢！」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MAB04"),"True","img/SN_MAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter 320/640.0
    with dissolve
    voice "NSU06A_SN002"
    信 "「什、什么？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAA02"),"True","img/SU_MAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-224)/640.0
    with dissolve
    voice "NSU06A_SU003"
    铃 "「一年到头晃晃悠悠，明明一句讨人开心的话都不会说，啊～啊」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MAA06"),"True","img/SN_MAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter 320/640.0
    with dissolve
    voice "NSU06A_SN003"
    信 "「哼、哼……被你当成傻瓜我可是无法接受的呢，我当然有女朋友啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAA05"),"True","img/SU_MAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-224)/640.0
    with dissolve
    voice "NSU06A_SU004"
    铃 "「胡说！」"
    "稻穗竟然有女朋友，这我还是第一次听到。"
    "那个人总是一副晃晃悠悠的样子……这么说来，他多大了？"
    voice "NSU06A_SN004"
    信 "「怎么可能是胡说。我都和她去旅行过，度过了两个人的甜蜜时光。这是铃姐你所不会的手段」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAA03"),"True","img/SU_MAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-224)/640.0
    with dissolve
#SET_SAVPNT
    voice "NSU06A_SU005A"
    铃 "「什……"
    play sound "SE04_38"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAA05"),"True","img/SU_MAA05A@2x.png") as lh0 zorder (10+0):
        xcenter (320-224)/640.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA03"),"True","img/RI_MBA03A@2x.png") as lh2 zorder (10+2):
        xcenter (320+192)/640.0
    voice "NSU06A_SU005B"
    extend "这个……」"
#CLR_SAVPNT
    "铃压低了声音，仿佛在小声嘟哝着什么。"
    "不好了，这种模式我已经有几次经验了。"
    "这样下去的话，店里会被鲜血染红的……！"
    show expression "img/BG16AA@2x.jpg" as bg_over zorder 2 with dissolve
#SET_SAVPNT
    voice "NSU06A_SN005"
    信 "「喂，等、等等……」"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "进去阻止他们":
            $F7=0
        "有富美子婆婆在不要紧的":
            $F7=1
#CLR_SAVPNT
    if F7==0:
        jump L_NSU06A_SEL00_A
    if F7==1:
        jump L_NSU06A_SEL00_B
label L_NSU06A_SEL00_A:
    $F4+=1
    "既然如此，我也只能去阻止他们了……"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    show expression "img/BG17AA1@2x.jpg" as bg1 zorder 1 with dissolve
    stop sound fadeout 1
    play sound "SE00_10"
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
#BG_SWPC 0
    hide bg1 with dissolve
#BG_PRI 0
#BG_PRI 1
#BG_ALPC 1,128
    scene expression "img/BG17AA1@2x.jpg" as bg0 with dissolve
    stop sound
    志雄 "「你、你们好～」"
    "我尽量放开嗓门打招呼，提心吊胆地将脚踏入店里。"
    window hide
    stop music
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SAA03"),"True","img/SU_SAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter (320-96)/640.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_SAA04"),"True","img/SN_SAA04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter 320/640.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SBA03"),"True","img/RI_SBA03A@2x.png") as lh3 zorder (10+3):
        ypos 0.0
        xcenter (320+160)/640.0
    with dissolve
    voice "NSU06A_SU006"
    铃 "「哎……志、志雄！？」"
    "店中，铃、稻穗和莉莉丝三人围坐在餐桌前，铃正抓着对面稻穗的胸口。"
    window hide
    play music "OBGM13"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_SAA02"),"True","img/SN_SAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NSU06A_SN006"
    信 "「啊！？塚本、塚本君！来的正好！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,0
    hide lh0
    hide lh2
    hide lh1
    hide lh3
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LAA02"),"True","img/SN_LAA02A@2x.png") as lh0 zorder (20-0):
        ypos 0.0
    with dissolve
#TODO
#MOV_CHR_INIT 24
#MOV_CHR1 ,(320+96)
#MOV_CHR2 0
#MOV_CHR3 0,640
#MOV_CHR_GO 1
#CHR_ERSWC 2,3
#CHR_ALPC 2,128
#CHR_ALPC 3,128
#MOV_CHR_INIT 24
#MOV_CHR0 128,(320-224)
#MOV_CHR_GO 1
    "对突然到来的我，铃惊讶地呆住了，稻穗马上从铃的手中挣脱出来。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LAA05"),"True","img/SN_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SN007"
    信 "「塚本君……我会度过一个寂寞的夏天已成既定的事实，照顾我姐姐的事情，就都交给你了」"
    play sound "SE04_24"
    "稻穗就这样从座位上站了起来，拍了拍我的肩膀随即准备离开。"
    志雄 "「喂？等、等等稻穗！？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SAA05"),"True","img/SU_SAA05A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    voice "NSU06A_SU007"
    铃 "「喂，你在说什么啊？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LAA06"),"True","img/SN_LAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SN008"
    信 "「呵呵，我从今天开始就要尽情享受幸福的夏天了。姐姐就等着回家的时候被亲戚问及什么时候结婚之类的头疼的问题吧！」"
    window hide
#MOV_CHR_INIT 24
#MOV_CHR0 0
#MOV_CHR_GO 1
    hide lh0 with dissolve
#CHR_ALPC 0,128
    play sound "SE00_10"
    play sound "SE01_00B"
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2,(320+96)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SAC03"),"True","img/SU_SAC03A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
        xcenter (320+96)/640.0
    with move
#MOV_CHR_INIT 24
#MOV_CHR1 0,(320)
#MOV_CHR2 128,(320)
#MOV_CHR_GO 1
    hide lh1 with dissolve
#CHR_ALPC 1,128
    voice "NSU06A_SU008"
    铃 "「信！你给我站住！」"
    "稻穗扔下了一句既微妙又很真实的台词便扬长而去了。"
    "铃正准备追上去的时候……"
    window hide
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAA03"),"True","img/SU_LAA03A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
    with dissolve
    play sound "SE04_19"
    stop music
    with hpunch
#QUA2_ALL 
    voice "NSU06A_SU009"
    铃 "「啊呀！」"
    "和站在门口的我撞了个满怀。"
    "铃发出了既感到意外却也不乏可爱的叫声，我抱住了步履蹒跚的铃来支撑住她的身体。"
    志雄 "「没事吧？」"
    window hide
    play music "BGM05"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAA02"),"True","img/SU_LAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU010"
    铃 "「对、对不起……啊，嗯，我没事」"
    志雄 "「那就好。关于稻穗，我之后会说他的，你先冷静一下」"
    志雄 "「闹得太过火了的话，会把富美子婆婆惹怒的哦？」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC02"),"True","img/SU_LAC02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU011"
    铃 "「这、这倒是呀……」"
    window hide
#CHR_SET_BACK
#CHR_SORT 2,0
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,640
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA06"),"True","img/RI_MBA06A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter 0.75
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC02"),"True","img/SU_LAC02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter 0.25
    with move
#MOV_CHR_INIT 64
#MOV_CHR1 128,(320+160)
#MOV_CHR2 ,(320-160)
#MOV_CHR_GO 1
    "看着这样子的我们，莉莉丝“哎呀哎呀”地念叨起来。"
    voice "NSU06A_RI001"
    莉莉丝 "「争执能停止是件好事，不过你们也别在那卿卿我我个没完啊」"
    hide lh2 with dissolve
    play sound "SE03_15"
#CHR_POSC 0,(320-160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAB04"),"True","img/SU_MAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter 0.25
    with dissolve
    铃 "「…………！」"
    志雄 "「哪、哪里卿卿我我了」"
    "我和铃慌忙放开了紧抱着的身体。"
    志雄 "「话、话说，为什么要在这里吵架？外边都能听得见啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAC06"),"True","img/SU_MAC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter 0.25
    with dissolve
    voice "NSU06A_SU013"
    铃 "「没、没什么啊。只是在谈论今年夏天要计划做些什么」"
    "就算这么说，我也觉得语气似乎太激烈了。"
    "说起来，关于我和铃交往的事，总感觉在被稻穗戏弄着。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD01"),"True","img/RI_MBD01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter 0.75
    with dissolve
    voice "NSU06A_RI002"
    莉莉丝 "「喂，志雄是来干什么的？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MAC02"),"True","img/SU_MAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter 0.25
    with dissolve
    志雄 "「啊，我还没吃早饭，肚子都饿扁了」"
    voice "NSU06A_RI003"
    莉莉丝 "「不介意的话，还有刚才做的炒面行吗？还是让奶奶给你做点什么？」"
    志雄 "「嗯，那就吃炒面吧」"
    "富美子婆婆做的饭是很吸引人的，好不容易做出来的饭菜虽然是剩下的那也足够了。"
    "比起这些，我已经饿得不行了。"
    志雄 "「话说，富美子婆婆呢？」"
    "虽说没有其他的客人，但店里发生了争吵还不露面就太罕见了。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA06"),"True","img/RI_MBA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter 0.75
    with dissolve
    voice "NSU06A_RI004"
    莉莉丝 "「好像每天只要一有好节目，她就会到屋里去」"
    "的确这个时候似乎是在播放着很受欢迎的海外电视剧……"
    "富美子婆婆对手机的运用简直是轻松自如，对流行的事物也很敏感。"
    "起初收到她附带着图片的邮件时，还真是吃了一惊。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBB01"),"True","img/RI_MBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter 0.75
    with dissolve
    voice "NSU06A_RI005"
    莉莉丝 "「那我给你热一下炒面」"
    志雄 "「这些我自己做吧」"
    voice "NSU06A_RI006"
    莉莉丝 "「好了好了，奶奶要是看到让客人待在厨房，会生气的」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SORT 0,1
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAA01"),"True","img/SU_LAA01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    "将炒面的任务交给莉莉丝后，我面向铃坐到餐桌前。"
    志雄 "「话说，铃这个夏天打算做什么？」"
    "刚才稻穗说的话让我也有种预感。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC04"),"True","img/SU_LAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU014"
    铃 "「工作是当然要做的，其它的还暂时不知道……」"
    "铃吞吞吐吐回答道，仿佛在考虑着什么事情。"
    "果然还是忙于工作么？"
    jump L_NSU06A_SEL00_X
label L_NSU06A_SEL00_B:
    "好像在店外待一下更好吧。"
    "卷进这对姐弟的吵架还是很危险的。"
    window hide
    stop music
    play sound "SE03_12"
    play music "OBGM13"
    voice "NSU06A_SU015"
    铃 "「就会趁机说那些顺情的好话」"
    voice "NSU06A_SN009"
    信 "「呜呜呜，好苦……这样的话，就要开始胡闹了……」"
    voice "NSU06A_SU016"
    铃 "「啊，喂！」"
    window hide
    play sound "SE00_10"
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LAA04"),"True","img/SN_LAA04A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    志雄 "「哇！？」"
    "稻穗忽然从里面飞奔了出去。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LAB04"),"True","img/SN_LAB04A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NSU06A_SN010"
    信 "「哇！对不起……塚本君」"
    志雄 "「这是怎么了啊，这反应好像是在说『塚本君怎样都好』似的」"
    "我目不转睛地盯着稻穗……自己这么简单就被忽略了。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LAB01"),"True","img/SN_LAB01A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NSU06A_SN011"
    信 "「啊，正好！里面需要处理的危险物品就交给你了」"
    志雄 "「等、等等啊！」"
    "突然这样逼人强制遵从，是很头疼的啊！"
    voice "NSU06A_SN012"
    信 "「那么，再见了少年，我不会忘记自己的和平是经由你的手实现的！」"
    志雄 "「不，等等……」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LAA06"),"True","img/SN_LAA06A@2x.png") as lh1 zorder (20+1):
        ypos 0.0
    with dissolve
    voice "NSU06A_SN013"
    信 "「ａｄｉｏｓ！！」"
    window hide
    play sound "SE01_00B"
#MOV_CHR_INIT 24
#MOV_CHR1 0
#MOV_CHR_GO 1
    hide lh1 with dissolve
#CHR_ALPC 0,128
    "稻穗就这么跑了出去，转眼就不见了踪影。"
    "他也就逃跑的时候会这么迅速……"
    window hide
    play sound "SE01_00A"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC03"),"True","img/SU_LAC03A@2x.png") as lh0 zorder (20+0):
        ypos 0.0
    with dissolve
    play sound "SE03_90"
    voice "NSU06A_SU017"
    铃 "「想逃啊……」"
    志雄 "「等等！」"
    "这次换成铃跑出去了。"
    window hide
    stop music
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAA03"),"True","img/SU_LAA03A@2x.png") as lh0 zorder (20+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU018"
    铃 "「哎！？志雄！？」"
    志雄 "「早、早上好」"
    "铃看着差点被撞到的我，一副目瞪口呆的样子。"
    window hide
    play music "BGM05"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC04"),"True","img/SU_LAC04A@2x.png") as lh0 zorder (20+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU019"
    铃 "「哎，啊？早上好……啊，已经逃走了」"
    "稻穗的身影不久便从视线中消失了。"
    "铃后悔地叹了口气。"
    志雄 "「到底怎么了，铃？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC06"),"True","img/SU_LAC06A@2x.png") as lh0 zorder (20+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU020"
    铃 "「没事，没什么大不了的」"
    "……铃装作若无其事的样子，不过刚才那怒吼连店外都能听的到。"
    "唉，姐弟之间还是不要吵得那么激烈比较好吧？"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAB01"),"True","img/SU_LAB01A@2x.png") as lh0 zorder (20+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU021"
    铃 "「志雄，你怎么会来这里？」"
    志雄 "「我有些饿了，想来这里吃饭」"
    voice "NSU06A_SU022"
    铃 "「原来已经到中午了呢」"
    志雄 "「啊哈哈，果真是有点睡过头了，铃吃过午饭了吗？」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "总之，就在这里站着说话也不太好。"
    "我和铃一起拨开门帘进入店内。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    show expression "img/BG17AA1@2x.jpg" as bg1 zorder 1 with dissolve
    stop sound fadeout 1
    play sound "SE00_11"
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
    scene expression "img/BG17AA1@2x.jpg" as bg0 with dissolve
    stop sound
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAA01"),"True","img/SU_LAA01A@2x.png") as lh0 zorder 100:
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    voice "NSU06A_SU023"
    铃 "「很遗憾，刚刚吃完」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_PRIC ID_ALL
#CHR_ALPC 1
#CHR_POSC 1,(320)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA01"),"True","img/RI_MBA01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter (320+96)/640.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAA01"),"True","img/SU_LAA01A@2x.png") as lh0 zorder 100:
        ypos 0.0
        xcenter (320-96)/640.0
    with move
#ROUTINE_STA
#CHR_POS_AUTOC 1,(320+96),F24,48
#CHR_ALP_AUTOC 1,128,1,F24,48
#ROUTINE_STP
    voice "NSU06A_RI007"
    莉莉丝 "「咦，你来了啊，吃午饭么？」"
    志雄 "「嗯，刚才一直在睡觉，肚子都扁了」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD01"),"True","img/RI_MBD01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter (320+96)/640.0
    with dissolve
    voice "NSU06A_RI008"
    莉莉丝 "「哼哼，有刚才做的炒面，你能吃么？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAB01"),"True","img/SU_LAB01A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    voice "NSU06A_SU024"
    铃 "「炒面很好吃哦」"
    志雄 "「那就吃炒面吧，富美子婆婆呢？」"
    voice "NSU06A_RI009"
    莉莉丝 "「在里面看电视」"
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
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAA01"),"True","img/SU_LAA01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    "将炒面的任务交给莉莉丝后，我面向铃坐到餐桌前。"
    志雄 "「你们在说什么呢，这么争执不休？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAB05"),"True","img/SU_LAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU025"
    铃 "「没、没什么，没什么大不了的事，只是在谈暑假的计划」"
    志雄 "「暑假的计划……吗」"
    "直到现在，我也只安排了学生会的工作和审核培训。"
    "虽然很无奈，但也想稍稍放松一下，毕竟无论如何都是高中生涯中最后的暑假了。"
    "虽然如果能和铃一起度过的话更好……"
    志雄 "「话说，铃有什么计划？还是工作？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC04"),"True","img/SU_LAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU026"
    铃 "「工作是当然的，其它的还不知道……」"
    "铃吞吞吐吐回答道，仿佛在想着什么事情。"
    "果然还是忙于工作么？"
    jump L_NSU06A_SEL00_X
label L_NSU06A_SEL00_X:
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC05"),"True","img/SU_LAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU027"
    铃 "「那个，现在在构思新作品，虽然有些费力」"
    "铃低下头陷入深思中，然后慢慢地抬起了头。"
    志雄 "「嗯，嗯」"
    voice "NSU06A_SU028"
    铃 "「那个，所以想稍微听一下志雄的意见，可以吗？」"
    志雄 "「可以，不过你要参考我的意见吗？」"
    "……话说回来，这和暑假的计划有关系么？"
    play sound "SE03_12"
    window hide
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XAC05"),"True","img/SU_XAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU029"
    铃 "「想听！非常极其格外十分地想听！」"
    "铃探出身子，将脸贴近我。"
    志雄 "「这、这倒是可以……铃、铃，离的太近了」"
    play sound "SE03_15"
#CHR_POSC 0,(320-192)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAB03"),"True","img/SU_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE03_14"
    铃 "「……！」"
    "铃慌忙坐了下来，稍稍思索了一下，然后开口说道。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAA04"),"True","img/SU_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#SET_SAVPNT
    voice "NSU06A_SU030A"
    铃 "「我说，{w=3}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAA02"),"True","img/SU_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU030B"
    extend "约会果然是要男孩子主动提出的吧？」"
#CLR_SAVPNT
    志雄 "「哎？我觉得是因人而异的……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC06"),"True","img/SU_LAC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU031"
    铃 "「不、不要一概而论，就说志雄自己的意见，我要听听志雄怎么想」"
    志雄 "「我？我没什么意见，毕竟没有这方面的经验，也要做参考么……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC03"),"True","img/SU_LAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU032"
    铃 "「这就足够了」"
    志雄 "「哎？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAB05"),"True","img/SU_LAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU033"
    铃 "「看吧，志雄无论在哪，无论说什么，也都还是个高中生，是个好榜样哦」"
    "这不是什么表扬的话吧……"
    "不过，还是先好好回答问题吧。"
    "也许稻穗和铃的争吵，和这个也有关系。"
    志雄 "「这个，然后呢……对于我来说，并不在意这一点」"
    志雄 "「只要自己邀请对方能让对方开心的话，这就足够了」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC04"),"True","img/SU_LAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU034"
    铃 "「……是这样呢」"
    "怎么？铃看上去有些不开心啊……"
    "难道是我说错了什么？"
    志雄 "「这些全部全部都是我的个人意见，你不要介意」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC02"),"True","img/SU_LAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU035"
    铃 "「什么？」"
    "铃不安地望着我。"
    "莫非……之前看焰火的时候就已经意识到了？"
    "那时，我的确有接近铃的意思。"
    "但那只是为了营造快乐的气氛……"
    志雄 "「不过，太按照我的想法做就没意思了吧……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAA04"),"True","img/SU_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU036"
    铃 "「嗯，适当地有所调整最好」"
    志雄 "「对啊。这样的话其中也包含着乐趣，才算是交往吧？」"
    "铃听了我的话，露出甜美的笑容。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAB01"),"True","img/SU_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU037"
    铃 "「呵呵，志雄可真是有本事的人啊，嗯」"
    "铃的心情似乎完全恢复了，这样一来我也能安心了。"
    志雄 "「那么，老师还有其它的问题么？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC02"),"True","img/SU_LAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU038"
    铃 "「其它的……譬如，恋爱中的活动会有什么忌讳的吗？」"
    志雄 "「活动啊……这个，我想没有女生那么多的忌讳，像之前看焰火的季节性出游就不错，但是说想创造美好的回忆，也有些太夸张了」"
    voice "NSU06A_SU040"
    铃 "「是吗。话说回来，夏天果然是要去海边玩吗？」"
    志雄 "「倒也不是非去不可，不过夏天不去海边玩的话，是不是就感觉少了些什么呢？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC05"),"True","img/SU_LAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU041"
    铃 "「海啊～」"
    志雄 "「去山中露营好像也很不错，我是在海边长大的，对去山里游玩没什么经验」"
    voice "NSU06A_SU042"
    铃 "「山也可以么」"
    志雄 "「其实去哪都可以的，总之这么长的假期，去平时去不了的、玩不了的地方不是很开心吗」"
    voice "NSU06A_SU043"
    铃 "「呵呵。跳出日常吗……的确，塑造恋爱事件才是正统做法」"
    "铃将手臂交叉起来，陷入了沉思。"
    "我很小心地把握着尺度说出了自己的见解，但真的有参考价值么？"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,640
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC05"),"True","img/SU_LAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA01"),"True","img/RI_LBA01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .75
    with move
#MOV_CHR_INIT 64
#MOV_CHR1 128,(320+160)
#MOV_CHR_GO 1
    voice "NSU06A_RI010"
    莉莉丝 "「给，炒面做好了」"
    志雄 "「哦，谢谢」"
    window hide
    play sound "SE03_33"
    play sound "SE03_20"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBB01"),"True","img/RI_LBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
        parallel:
            linear 1 alpha 0
        parallel:
            linear 1 xcenter 1.0
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR1 0,640
#MOV_CHR_GO 1
    hide lh1 with dissolve
#CHR_ALPC 1,128
    "莉莉丝把炒面和水放在我面前，又回到了厨房里。"
    voice "NSU06A_SU044"
    铃 "「呵呵」"
    志雄 "「我开动了」"
    "我一个劲地把炒面往嘴里塞，同时望着一直在思考的铃。"
    "铃烦恼地皱紧了眉头，不久轻轻地点了点头。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAA01"),"True","img/SU_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU045"
    铃 "「好吧，志雄」"
    志雄 "「什、什么？」"
    voice "NSU06A_SU046"
    铃 "「说起学生会的工作，暑假里忙碌的日子要从后半段才开始吧？」"
    志雄 "「唔？嗯」"
    "我就这样狼吞虎咽地吃着炒面，点头应声道。"
    "说起奏云祭的准备，的确是这样。随着第二学期的临近，各种各样的商议和准备就有必要提前进行了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAB01"),"True","img/SU_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU047"
    铃 "「之后也不去补习学校了吗？」"
    志雄 "「如果去的话，也就想稍微听一下短期课程。这样就可以和学生会的工作轮流进行，是吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC05"),"True","img/SU_LAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU048"
    铃 "「ＯＫ，然后就取决于我了吧……」"
    志雄 "「……？什么事情？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAC01"),"True","img/SU_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU049"
    铃 "「不，现在的这个阶段还不能确定……等更清楚了点再说吧」"
    志雄 "「是么……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LAB01"),"True","img/SU_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU06A_SU050"
    铃 "「莉莉丝，我吃好了」"
    window hide
    stop music
#MOV_CHR_INIT 48
#MOV_CHR0 0
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
    hide lh0 with dissolve
#CHR_ALPC 0,128
    play sound "SE00_11"
    "铃向正在洗碗的莉莉丝打了声招呼，便立刻从店中走了出去。"
    志雄 "「……这是怎么了啊？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD01"),"True","img/RI_LBD01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NSU06A_RI012"
    莉莉丝 "「你呀，最好感谢一下我和稻穗吧？」"
    志雄 "「感谢什么？」"
    window hide
    play music "BGM10"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBC02"),"True","img/RI_LBC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NSU06A_RI013"
    莉莉丝 "「让铃打起精神的就是我们啊」"
    志雄 "「我说啊……你们和铃都讲了些什么啊？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD06"),"True","img/RI_LBD06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NSU06A_RI014"
    莉莉丝 "「这个嘛」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "莉莉丝坏心眼地笑了笑，然后又走回了厨房。"
    "我明白铃是在考虑暑假约会的事情。"
    "但是，就这么把事情推给她也不好，我也应该想着做些什么。"
    window hide
    stop music
#FADE_OUT 1
    scene expression Solid("000") with None
#FADE_IN 0
    "然而……"
    "之后的几天，不知为什么和铃再也联系不上了。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music
#FADE_OUT 1,128
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop se
    stop sound
    stop music
    $ renpy.end_replay()
#FADE_IN 0
    return