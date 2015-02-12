label NCH06A1B:
    $currentlabel = "NCH06A1B"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG65AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG65AA@2x.jpg" as bg0 with dissolve
    play sound "SE06_17L"
    play sound "RAILWAY_008"
    stop sound fadeout 1
#SE_WATC 1
    pause (32/32.0)
    play sound "SE08_18L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1
    play music "BGM11"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    if not persistent.dictlist[47] and persistent.show_dict:
        $persistent.dictlist[47]=True
        show screen dict_pop(i=47)
    "然后，我们在摇晃的特快列车坐了不到2个小时，便在一个叫下龙境的车站下了车。从那里打车，我们来到了作为目的地的旅馆。"
    window hide
    stop sound fadeout 1
    play sound "SE06_19L"
    show expression "img/BG68AA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    show expression "img/BG66AA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    stop se fadeout 1
#FADE_OUT 1
    show expression "img/BG60AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG60AA@2x.jpg" as bg0 with dissolve
#SE_WATC 0
    play sound "SE05_15L"
    play sound "SE06_20"
#FADE_IN 1
    play sound "SE06_21"
    if not persistent.dictlist[49] and persistent.show_dict:
        $persistent.dictlist[49]=True
        show screen dict_pop(i=49)
    "旅馆的名字叫『宝树庵』。"
    window hide
#SE_VOLC 1
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC01"),"not F103==0","img/CH_LLC01A@2x.png","True","img/CH_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCH06A_CH065"
    智纱 "「哇，很漂亮的旅馆呢」"
    window hide
#MOV_CHR_INIT 48
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
    "智纱环视着整个旅馆。"
    "我和智纱的感想一样。老实说，本以为是个更小的旅馆呢。"
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
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 1,(320+72)
#CHR_POSC 2,(320-72)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA02"),"True","img/KR_MAA02A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    voice "NCH06A_KR016"
    香里 "「呵呵，谢谢」"
    voice "NCH06A_YG025"
    雄吾 "「计划这次旅行的是香里。这个旅馆也是，是香里说一定要来的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH06A_KR017"
    香里 "「嗯，这个旅馆，是我母亲的熟人在经营着。这次是招待她去的，但是她好像是有事，去不成了」"
    "店里很忙吧。确实，如果富美子婆婆不在的话，小店就转不动了。"
    voice "NCH06A_KR018"
    香里 "「于是，我们就以新婚旅行的名义，代替她来了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA03"),"True","img/SF_MAA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCH06A_YG026"
    雄吾 "「从我们结婚已经超过半年了，再说什么新婚旅行总觉得有点晚了啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA02"),"True","img/KR_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH06A_KR019"
    香里 "「哎呀，这不挺好的嘛。好不容易有几乎免费的住店机会」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    "……这两个人，关系真好啊。在车上也是这样，相处得非常地自然融洽。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA01"),"not F103==0","img/CH_LLA01A@2x.png","True","img/CH_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    "看看智纱那边。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA04"),"not F103==0","img/CH_LLA04A@2x.png","True","img/CH_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH066"
    智纱 "「嗯？　怎么了？志雄君？」"
    志雄 "「没事，只是有点」"
    "我们什么时候也能够像这个样子，自然地相处呢……？"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG61AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG61AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA04"),"not F103==0","img/CH_LLA04A@2x.png","True","img/CH_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_BLUR 0
#FADE_IN 1
#MUS_VOL 0
    志雄 "「哎？」"
    "在大厅的前面，我看着递到手里的钥匙。智纱也是一脸的惊愕。"
    window hide
#CHR_SET_BACK
#BG_BLUR 0
#CHR_INIC 1
#CHR_INIC 2
#CHR_ALPC 1
#CHR_ALPC 2
#CHR_POSC 1,(320+256)
#CHR_POSC 2,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA04"),"not F103==0","img/CH_LLA04A@2x.png","True","img/CH_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA02"),"True","img/KR_MAA02A@2x.png") as lh1 zorder (10+1):
        xcenter .9
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .65
        ypos 0.0

#ROUTINE_STA
#CHR_ALP_AUTOC 1,128,1,F24,48
#CHR_ALP_AUTOC 2,128,1,F24,48
#CHR_POS_AUTOC 0,(320-160),F24,48
#ROUTINE_STP
    "另一方面，老爸的手里也有钥匙。"
    志雄 "「为什么有两把钥匙啊？」"
    "不可能是通用的钥匙啊。老爸拿着的钥匙是「葵之间」，我拿着的是「桔梗之间」，上面写着不同的名字。"
    "然后，老爸摆出了一副「理所当然的事情你还说什么呢？」的表情。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh1 zorder (10+1)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA02"),"True","img/SF_MAA02A@2x.png") as lh2 zorder (10+2)
    voice "NCH06A_YG027"
    雄吾 "「那个啊，要两个房间那是当然的啊？　我和香里一间，你和智纱一间」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC06"),"not F103==0","img/CH_LLC06A@2x.png","True","img/CH_LBC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH067"
    智纱 "「哎哎！？」"
    志雄 "「等、等一下啊，老爸。不是四个人住在一起的房间吗？」"
#MUS_VOL 128
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCH06A_YG028"
    雄吾 "「有谁那样说过吗？」"
    "老爸平静地回答着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC04"),"not F103==0","img/CH_LLC04A@2x.png","True","img/CH_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH068"
    智纱 "「可、可是……」"
    "两个人一个房间，这么说也就是和智纱两个人单独相处了。"
    "不对，和智纱两个人单独相处，也并不是什么新鲜的事情。"
    "但是——过夜的话就另说了。智纱在我家住下来这种事，到现在为止一次都没有……。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA05"),"True","img/SF_MAA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCH06A_YG029"
    雄吾 "「唉，别说什么不懂风趣的话啊，志雄。我和香里可是新婚啊？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA01"),"True","img/SF_MAA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCH06A_YG030"
    雄吾 "「而且，住在不同的房间更轻松一些吧？　别跟我们这些上了年纪的人在一块，自由自在地去玩吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA01"),"True","img/KR_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH06A_KR020"
    香里 "「对对，年轻人就要和年轻人在一起，是吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB03"),"not F103==0","img/CH_LLB03A@2x.png","True","img/CH_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "香里阿姨的脸上浮现了恶作剧般的笑容……莫非这个情况，是你干的好事吗？"
    "我好像在香里阿姨的身上看见了莉莉丝的影子。在这种场合下想到『有其母必有其女』，总觉得有点讨厌。"
    voice "NCH06A_YG031"
    雄吾 "「好了，现在开始就分头行动了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA05"),"True","img/SF_MAA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCH06A_YG032"
    雄吾 "「啊，但是不管怎样，就算是两个人单独相处也不要玩得太过火，做出些什么奇怪的事情哦」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_MAA02"),"True","img/KR_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH06A_KR021"
    香里 "「是呢。要适可而止哦」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA03"),"not F103==0","img/CH_LLA03A@2x.png","True","img/CH_LBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「什么适可而止啊，我们才不会去做什么奇怪的事情呢」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC04"),"not F103==0","img/CH_LLC04A@2x.png","True","img/CH_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH069"
    智纱 "「就，就是说啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_MAA02"),"True","img/SF_MAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCH06A_YG033"
    雄吾 "「啊哈哈」"
    window hide
    stop music fadeout 1
    hide lh1
    hide lh2
    with dissolve
#MOV_CHR_INIT 64
#MOV_CHR0 
#MOV_CHR1 0,((320+256)+((320)/2))
#MOV_CHR2 0,((320+96)+((320)/2))
#MOV_FOCUS_BG 512
#MOV_CHR_GO 1
#CHR_ERSWC 1,2
#CHR_ALPC 1
#CHR_ALPC 2
    "然后，两个人迈着轻松的脚步，向着走廊里走去了。"
    志雄 "「……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC02"),"not F103==0","img/CH_LLC02A@2x.png","True","img/CH_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "我呆然地看着自己手里的钥匙。智纱以一种困惑的眼神看着我。"
    志雄 "「那～个」"
    志雄 "「总之，先去房间看看吧？」"
    "一直拿着行李愣在这也不是个办法。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC05"),"not F103==0","img/CH_LLC05A@2x.png","True","img/CH_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH070"
    智纱 "「嗯，说的也是呢……」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG62AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG62AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    志雄 "「哎～，是哪个房间呢」"
    "寻找着名叫「桔梗之间」的房间，我们在旅馆的走廊里徘徊着。"
    "按照前台的指点，好像应该是在这一带。"
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB03"),"not F103==0","img/CH_LLB03A@2x.png","True","img/CH_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCH06A_CH071"
    智纱 "「……」"
    "智纱好像有些困惑，眉毛撇成了八字。"
    志雄 "「……还是，不喜欢双人间吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB04"),"not F103==0","img/CH_LLB04A@2x.png","True","img/CH_LBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH072"
    智纱 "「哎？」"
    "这么突然地告诉我们是个双人间，智纱会感到不知所措也是理所当然的。"
    志雄 "「抱歉。我还是和老爸说说，换个房间吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA03"),"not F103==0","img/CH_LLA03A@2x.png","True","img/CH_LBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCH06A_CH073"
    智纱 "「不不，没事的！　我并不是感到讨厌……」"
#REMOVE_REEK_CHR 0
    window hide
    play music "BGM16"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC05"),"not F103==0","img/CH_LLC05A@2x.png","True","img/CH_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH074"
    智纱 "「果然，还是有点不好意思啊」"
    志雄 "「……」"
    "呃，该、该怎么回答才好呢……。"
    志雄 "「啊，那个～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC06"),"not F103==0","img/CH_LLC06A@2x.png","True","img/CH_LBC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH075"
    智纱 "「啊，但是，我很高兴的哦！　能和志雄君两人住在一起！」"
    "至少好像是知道我不好回答，慌忙地辩解着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA05"),"not F103==0","img/CH_LLA05A@2x.png","True","img/CH_LBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH076"
    智纱 "「不如说双人房，正如我所愿呢！」"
    志雄 "「是，是吗？」"
    "智纱辩解时的气势，让我感到了一股压迫感。"
    voice "NCH06A_CH077"
    智纱 "「嗯！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC01"),"not F103==0","img/CH_LLC01A@2x.png","True","img/CH_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH078"
    智纱 "「……啊！　那个，不就是我们的房间吗」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "智纱的手指着的是，挂在门边的一个写着「桔梗之间」的牌子。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    scene expression "img/BG63AA@2x.jpg" as bg1 zorder 1 with dissolve
    play sound "SE00_46"
    pause (32/32.0)
    play sound "SE00_47"
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
#BG_ALPC 1
#BG_PRI 0
#BG_PRI 1
#SE_WATC 0
    "准备好的房间是一间干净地铺好了榻榻米的和室。"
    play sound "SE03_55"
    "装好旅行用品的包已经在房间的角落里堆放好了。"
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC04"),"not F103==0","img/CH_LLC04A@2x.png","True","img/CH_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    "话虽如此，和智纱两个人独处……。"
    voice "NCH06A_CH079"
    智纱 "「……」"
    "智纱冷静不下来，四处张望着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC06"),"not F103==0","img/CH_LLC06A@2x.png","True","img/CH_LBC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH080"
    智纱 "「怎，怎么了？　志雄君？」"
    "是注意到我的视线了吗，智纱慌张地说着。"
    志雄 "「啊，没事，什么都没有」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC04"),"not F103==0","img/CH_LLC04A@2x.png","True","img/CH_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "嗯～……是因为分开的时候老爸说了那些奇怪的话的缘故吗，意识到了些奇妙的事情。"
    "现在的时间是2点半。距离晚饭的时间还很充裕，足够出去哪里转转了。"
    志雄 "「……还有空闲时间的，去哪里转转吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA01"),"not F103==0","img/CH_LLA01A@2x.png","True","img/CH_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH081"
    智纱 "「是呢」"
    voice "NCH06A_CH082"
    智纱 "「要去哪里好呢……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB06"),"not F103==0","img/CH_LLB06A@2x.png","True","img/CH_LBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH083"
    智纱 "「那～个，好像在那边的山里，有个湖可以游泳的……」"
    "这么说来，事先调查旅行目的地的时候，也看过了这样的东西。"
    志雄 "「可是那个……」"
    "考虑到智纱的恐水症，是不可能去游泳的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA01"),"not F103==0","img/CH_LLA01A@2x.png","True","img/CH_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH084"
    智纱 "「……没关系的哦？」"
    志雄 "「哎？」"
    voice "NCH06A_CH085"
    智纱 "「湖……也是可以的哦？　好不容易来到了能游泳的地方，不去一次的话太可惜了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB05"),"not F103==0","img/CH_LLB05A@2x.png","True","img/CH_LBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH086"
    智纱 "「我在水边的话也是没问题的」"
    志雄 "「那个不行」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB04"),"not F103==0","img/CH_LLB04A@2x.png","True","img/CH_LBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「那样的话，智纱不会玩得高兴吧。既然是一起来的，不一起高高兴兴地玩可不行」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB03"),"not F103==0","img/CH_LLB03A@2x.png","True","img/CH_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH06A_CH087"
    智纱 "「……」"
    志雄 "「而且，除了湖以外，哪里都有可以去的地方啊」"
    "先是从旅馆中出去，上街看看吗，还是……。"
    menu:
        "在旅馆中转转看看":
            $F7=0
        "上街":
            $F7=1
    if F7==0:
        jump L_NCH06A_SEL01_A
    if F7==1:
        jump L_NCH06A_SEL01_B
label L_NCH06A_SEL01_A:
    $F14 = "NCH06A1C"
    jump L_NCH06A_SEL01_X
label L_NCH06A_SEL01_B:
    $F14= "NCH06A1D"
    jump L_NCH06A_SEL01_X
label L_NCH06A_SEL01_X:
    $ renpy.end_replay()
    return