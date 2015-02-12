label NRI03A:
    $currentlabel = "NRI03A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '19'
    $date = '3'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 5,CAL_0719
    show expression "img/NIMG15E-568h@2x.jpg" as cal zorder 5
    show expression "img/07_19_WEDNESDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG09EA@2x.jpg" as bg0 zorder 0 with dissolve
    play sound "SE06_29L"
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
    志雄 "「嗯……」"
    "伸了一个大懒腰，舒展了一下僵硬的身体。"
    if not persistent.dictlist[16] and persistent.show_dict:
        $persistent.dictlist[16]=True
        show screen dict_pop(i=16)
    "ＫＡＮＡＴＡ的特别节目终于听到尾声了……"
    "但本应做的学生会工作却丝毫没有进展。"
    "一学期已经结束了，一定要把这期间举办的活动资料整理出来才行。"
    "不过，这时候还是把精力花在学习上，考虑自己的前途才好吧……"
    window hide
    stop sound
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG09AA@2x.jpg" as bg2 zorder 2 with dissolve
#BG_BLUR 2
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LFA01"),"True","img/CL_LFA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    stop sound
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 0
#BG_ALPC 2
#CHR_ALPC 0
    play music  "BGM14"
    if not persistent.dictlist[42] and persistent.show_dict:
        $persistent.dictlist[42]=True
        show screen dict_pop(i=42)
    if not persistent.dictlist[3] and persistent.show_dict:
        $persistent.dictlist[3]=True
        show screen dict_pop(i=3)
    voice "NRI03A_KU000_K"
    克罗艾 "「塚本。从今天起你就是澄空学园的学生会会长了。」"
    voice "NRI03A_KU001_K"
    克罗艾 "「以后就交给你了，好好干哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LFB01"),"True","img/CL_LFB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_KU002_K"
    克罗艾 "「哈哈哈，不必这么兴奋，你没问题的。我相信我看人的眼光，你一定能做的很好的……」"
    window hide
#BG_INIC 1
#BG_PRI 1
#BG_BLUR 2
    scene expression "img/BG09EA@2x.jpg" as bg0 with dissolve
    hide bg2 with dissolve
#BG_UVC 2,0,0,640,448
    hide lh0 with dissolve
#BG_ALPC 0
    hide bg1 with dissolve
    "没错，克罗艾学姐都这么说了，一定要好好干才行。"
    stop music fadeout 1
    voice "NRI03A_YU000"
    结乃？ "「累了吗？」"
    "忽然，一只手放在了我肩膀上。还没回过神，那只手便开始在我的肩膀上发力……最终力量传到了我的穴位上。"
    play sound "SE04_23"
    志雄 "「疼！好疼！喂，春日！？」"
    "忍着肩膀的疼痛，我皱着眉头转过头……不出所料，春日像小恶魔一样，站在那里。"
    window hide
    stop se
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAC01"),"True","img/YU_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM06"
    if not persistent.dictlist[4] and persistent.show_dict:
        $persistent.dictlist[4]=True
        show screen dict_pop(i=4)
    voice "NRI03A_YU001"
    结乃 "「诶？……这么疼吗？我还在想学长的肩膀是不是僵硬了，想帮忙揉一揉呢。」"
    志雄 "「啊，啊啊，刚才是在帮我揉肩膀吗……」"
    "春日虽然外表上看上去弱不禁风，但实际上力气大的惊人。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU002"
    结乃 "「对了，工作完成了吗？」"
    志雄 "「啊，今天的任务差不多结束了。」"
    "说着，我开始整理起桌上的文件和书本。"
    "其它干事的工作早就已经完成了，留在学生会室里的，也只有我一个人。"
    voice "NRI03A_YU003"
    结乃 "「那个……那么，在回去之前，我想找你商量一点事情……」"
    志雄 "「我吗？可以啊，怎么了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB02"),"True","img/YU_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU004"
    结乃 "「谢谢你。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU005"
    结乃 "「其实是这样的……」"
    play sound "SE03_29"
    "春日从书包里取出一张打印纸放在我的桌上。"
    "『文理分科志愿调查表』。"
    "一年前，我也曾填写过的东西。"
    志雄 "「现在的２年级就要开始选择文科和理科了吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA05"),"True","img/YU_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU006"
    结乃 "「是的。理科和文科，究竟选哪个……？我有点不知如何是好。」"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,YU_LXB05,2,F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB05"),"True","img/YU_LAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NRI03A_YU007"
    结乃 "「……诶，塚本学长，怎么看上去这么失落呢？」"
#REMOVE_REEK_CHR 0
#BG_ALP 3
    志雄 "「啊，没有……」"
    "春日一向善于察言观色，只是那一瞬间的失落也被她捕捉到了。连２年级生都要决定自己前程了，我却……"
    志雄 "「嗯……」"
    "我姑且算是文科志愿吧。可是，那也只是因为我不擅长数学……只是这种消极的理由罢了。"
    志雄 "「我也不知道自己能不能帮上忙……」"
#REEK_CHR 0
    voice "NRI03A_YU008"
    结乃 "「诶，为什么？」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
    志雄 "「因为我自己的方向也几乎没有定下来。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB06"),"True","img/YU_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU009"
    结乃 "「啊！？」"
    voice "NRI03A_YU010"
    结乃 "「等一下，塚本学长已经３年级了吧。」"
    志雄 "「没错，很遗憾，我已经３年级了。」"
    voice "NRI03A_YU011"
    结乃 "「啊，那个……已经到了这个关头还没决定会不会有些危险？」"
    志雄 "「啊，的确非常危险呢，昨天刚被老师说过……」"
    voice "NRI03A_YU012"
    结乃 "「为什么决定不了呢？」"
    志雄 "「我也不知道该怎么回答这个问题……」"
    志雄 "「面对自己的未来，完全摸不清方向，我也没什么梦想和特别想做的事。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA04"),"True","img/YU_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU013"
    结乃 "「嗯，那可真是难以决定呢。梦想和想做的事吗……这些事的确不是这么简单就可以下定论的。」"
    志雄 "「哈，是呢……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU014"
    结乃 "「不过，说对自己的未来没有方向，那是骗人的吧～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB02"),"True","img/YU_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU015"
    结乃 "「因为，志雄学长的未来，不就是和莉莉丝学姐在一起吗？」"
    voice "NRI03A_YU016"
    结乃 "「你和远峰学姐的『结婚典礼』已经是大家心中象征爱情的典范了～」"
    志雄 "「饶了我吧……」"
    "那时，我还真是够大胆的……当然，我并不后悔。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU017"
    结乃 "「你在说什么呀！？有什么不好意思的。」"
    "春日的眼神缥缈了起来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA02"),"True","img/YU_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU018"
    结乃 "「洁白的婚纱，热恋后走到一起的出色新郎……嗯，真浪漫，好羡慕远峰学姐～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA04"),"True","img/YU_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU019"
    结乃 "「我能找到这么好的男友就好了。」"
    "说着春日吐着舌头笑了笑。"
    "不过，实话说，如果春日想要的话，一定马上能找到的。"
    "她性格开朗，长的可爱，做什么事也都很积极。真是令我感到骄傲的学妹呢。"
    "她要是有了男朋友，我反而会觉得有些不舍吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU020"
    结乃 "「啊，对了，马上就是远峰学姐的生日了吧，你准备生日礼物了吗？」"
    志雄 "「那个，目前还没有。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB03"),"True","img/YU_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU021"
    结乃 "「这样可不行哟！」"
    志雄 "「你这么说我也——」"
    "可能的话，我想先决定自己的升学方向，等一切都有着落了，再给莉莉丝庆祝生日……"
    stop music fadeout 132
    play sound "SE00_25"
    "嗯！？　学生会室的门突然打开了。"
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
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SAB01"),"True","img/RI_SAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.2
    with dissolve
    play music  "BGM02"
    "站在门口的是莉莉丝。"
    voice "NRI03A_RI000"
    莉莉丝 "「啊，志雄。」"
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
#CHR_PRIC 0
#CHR_PRIC 1
#CHR_ALPC 0
#CHR_ALPC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,((320+160)+(640/8))
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB01"),"True","img/YU_MAB01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAB01"),"True","img/RI_MAB01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
    with dissolve
#CHR_ALP_AUTOC 0,128,0,F24
#CHR_ALP_AUTOC 1,128,0,F24
#CHR_POS_AUTOC 1,(320+160),F24
#CHR_ALP_SAVEC 0
#CHR_ALP_SAVEC 1
#CHR_POS_SAVEC 1
    "莉莉丝看到我就快步走了过来。"
    志雄 "「怎么了？我还以为你已经回去了。」"
#CHR_GET_POSC 1,F24,F25
#RSUB F24
#BG_LAY 3,RI_MXC03,3,F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC03"),"True","img/RI_MAC03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#REEK_CHR 1
    voice "NRI03A_RI001"
    莉莉丝 "「啊，那个……我有些话和智纱说就留下了。」"
#REMOVE_REEK_CHR 1
    hide bg3 with dissolve
#BG_PRI 3
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAB02"),"True","img/RI_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI03A_RI002"
    莉莉丝 "「然后聊了很长时间，我想你学生会的工作也差不多做完了吧，就……」"
    voice "NRI03A_RI003"
    莉莉丝 "「嗯。果然不出所料，时间刚刚好呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB02"),"True","img/YU_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU022"
    结乃 "「哈～？　哈哈。」"
    志雄 "「春日……？」"
    "总觉得有些意味的笑声……"
    voice "NRI03A_YU023"
    结乃 "「不不，没什么，你们两个还是关系这么好呢～」"
    志雄 "「……？」"
#MESEX_A M_NOA,A_CH_SI,"【志雄】「……？」%K%P"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAA01"),"True","img/YU_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU024"
    结乃 "「远峰学姐是在等塚本学长呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA03"),"True","img/RI_MAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI03A_RI004"
    莉莉丝 "「什……结、结乃！？」"
    志雄 "「诶，这样吗？」"
    "那样的话，我还真是让她久等了呢。"
    voice "NRI03A_RI005"
    莉莉丝 "「说、说什么呢，不是的！我不是说了有话和智纱说吗！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAA02"),"True","img/YU_MAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU025"
    结乃 "「又来了，不用害羞嘛～」"
    voice "NRI03A_RI006"
    莉莉丝 "「结乃！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB02"),"True","img/YU_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU026"
    结乃 "「啊哈哈。不要一副这么恐怖的表情嘛，这样会被塚本学长讨厌的哟？」"
    voice "NRI03A_RI007"
    莉莉丝 "「啊，啊，啊啊，真是的。」"
    "莉莉丝红着脸，来回地看着我和春日，完全静不下来。"
    志雄 "「总之先冷静下来啦，莉莉丝。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD04"),"True","img/RI_MAD04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI03A_RI008"
    莉莉丝 "「我很冷静啦！」"
#ROUTINE_STA
#CHR_SORT 2,0
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2
#ROUTINE_STP
    hide lh1
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XAE02"),"True","img/RI_XAE02A@2x.png") as lh2 zorder (100-2):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 8
#MOV_CHR0 0
#MOV_CHR1 0
#MOV_CHR2 128
#MOV_CHR_GO 0
#CHR_ERSWC 0,1
#BG_BLUR 0
    play sound "SE04_06"
    "啊！"
#THREAD_STA 1,THREAD_QUA_WIN
#VIB_DOKA 
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MES "啊！"
#THREAD_WAT 1
#WIN_POS 0,0
#VIB_STP 5
#MESX "%K%P"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_ALPC 0
#CHR_ALPC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB06"),"True","img/YU_MAB06A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA05"),"True","img/RI_MAA05A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
#MOV_CHR_INIT 16
#MOV_CHR0 128
#MOV_CHR1 128
#MOV_CHR2 0
#MOV_CHR_GO 0
    hide lh2
    with dissolve
#BG_BLUR 0
    志雄 "「你这么突然我避不开啦……好疼……」"
    voice "NRI03A_YU027"
    结乃 "「没，没事吧！？」"
    "最近都手下留情了吗，即使被踢了也完全不会疼。可刚才那下……有点认真了……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAD05"),"True","img/RI_MAD05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI03A_RI009"
    莉莉丝 "「没事，我很好。」"
    志雄 "「等一下，谁也没在担心你吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB02"),"True","img/YU_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU028"
    结乃 "「啊哈哈。真是的，不要总是把这种令人羡慕的场景给别人看嘛～」"
    voice "NRI03A_YU029"
    结乃 "「我知道了啦。不妨碍你们了～」"
    "说着，春日把放在桌上的志愿方向用纸塞在包里，然后站了起来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAA01"),"True","img/YU_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_YU030"
    结乃 "「那么我就先回去了，两位慢聊～」"
    window hide
    stop music fadeout 1
    hide lh0 with dissolve
    play sound "SE00_26"
    志雄 "「慢聊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAB02"),"True","img/RI_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    莉莉丝 "「……」"
#MESEX_A M_NOA,A_CH_RI,NRI03A_RI010,"【りりす】「……」%K%P"
    志雄 "「那个～」"
    "虽然两人独处，但也不意味着就会发生什么……"
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
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAB02"),"True","img/RI_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「那么，我们也差不多该回去了吧？」"
    voice "NRI03A_RI011"
    莉莉丝 "「嗯，嗯……」"
    "不知道是不是窗外夕阳照射进来的缘故，莉莉丝的侧脸有些泛红。"
    "这表情令我想起了那时的事。"
    window hide
#BG_SET_BACK
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 0,0 
#CHR_ALPC 0
#BG_INIC 2
#BG_ALPC 2
    show expression "img/EV_RI11B@2x.png" as bg2 zorder 200 with dissolve
    stop sound
    hide bg1 with dissolve
    "在大家的注目下，我和莉莉丝……"
    window hide
#BG_INIC 1
#BG_PRI 1
    hide bg2 with dissolve
#BG_ALPC 0
#CHR_ALPC 0
    hide bg1 with dissolve
    play music  "BGM13"
    志雄 "「呐，莉莉丝。」"
    "我的声音显得有些高。"
    "都是因为春日说了那些话，弄得我也不好意思了……"
    voice "NRI03A_RI012"
    莉莉丝 "「哎……？」"
    志雄 "「啊，那个……」"
    "不知不觉相互对视着的我们之间的距离在逐渐缩短。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XAB02"),"True","img/RI_XAB02A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NRI03A_RI013"
    莉莉丝 "「怎，怎么了？」"
    志雄 "「嗯……怎么说呢……现在，只有我们两个了呢。」"
    voice "NRI03A_RI014"
    莉莉丝 "「嗯……嗯。」"
    志雄 "「真安静啊……」"
    voice "NRI03A_RI015"
    莉莉丝 "「嗯……」"
    志雄 "「……」"
    莉莉丝 "「……」"
#MESEX_A M_NOA,A_CH_SI,"【志雄】「……」%K%P"
#MESEX_A M_NOA,A_CH_RI,NRI03A_RI016,"【りりす】「……」%K%P"
    stop music fadeout 132
    play sound "SE02_20"
    with hpunch
    志雄 "「哇！？」"
#THREAD_STA 1,THREAD_QUA_WIN
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESA A_CH_SI,"【志雄】「哇！？」"
#THREAD_WAT 1
#WIN_POS 0,0
#MESX "%K%P"
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
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA03"),"True","img/RI_MAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "谁，谁！？"
    "竟然在这种时候收到短信，难道被谁看到了吗！？"
    "我匆忙从口袋中掏出手机。"
    "同时，我面前的莉莉丝也在看着自己的手机。"
    voice "NRI03A_RI017"
    莉莉丝 "「哎？　志雄也？」"
    志雄 "「啊啊。」"
    "手机画面上显示的是富美子婆婆。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAA04"),"True","img/RI_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_RI018"
    莉莉丝 "「原来是婆婆的短信的。」"
    志雄 "「诶？　我也是。」"
    window hide
#SCRMODE_SPC SCR_FULL
    play sound "SE02_03"
    "Ｆｒｏｍ：　　富美子婆婆{p}内容　　：{p}我有些话想对你说，回家的时候{p}顺便到店里来。"
#FILT_PRI 1
#FILT_IN 48,0,COL_DARK
#MES "%S032%FS%t002Ｆｒｏｍ：　　富美子婆婆%N%t002内容　　：%N%t007我有些话想对你说，回家的时候%N%t007顺便到店里来。%FE%K"
    play sound "SE02_03"
#MESX "%O032"
    window hide
#FILT_OUT 48
#SCRMODE_SPC SCR_WINDOW
    voice "NRI03A_RI019"
    莉莉丝 "「……婆婆说，她有些话想对你说，让我回家的时候带你一起去。」"
    "能在几乎同一时间发出不同的两条短信……婆婆的打字速度究竟有多快啊。"
    志雄 "「想对我说的话吗。会是什么呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAC04"),"True","img/RI_LAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_RI020"
    莉莉丝 "「谁知道……？」"
    志雄 "「总之先回去吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LAB01"),"True","img/RI_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI03A_RI021"
    莉莉丝 "「嗯。」"
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
#label THREAD_QUA2_WIN
#TH_QUA2_WIN
#EOT
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT