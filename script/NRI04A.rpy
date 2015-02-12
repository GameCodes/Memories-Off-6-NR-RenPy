label NRI04A:
    $currentlabel = "NRI04A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '19'
    $date = '3'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG17EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG17EA@2x.jpg" as bg0 with dissolve
    play sound "SE00_10"
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
    voice "NRI04A_RI000"
    莉莉丝 "「我回来了。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA01"),"True","img/FU_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    if not persistent.dictlist[9] and persistent.show_dict:
        $persistent.dictlist[9]=True
        show screen dict_pop(i=9)
    voice "NRI04A_FU000"
    富美子 "「欢迎回来。志雄也欢迎。」"
    志雄 "「打扰了。」"
    "已经到了客人较少的时段，现在只有我们在店里。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,(320-160)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAB01"),"True","img/RI_MAB01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA01"),"True","img/FU_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .75
    with move
#CHR_ALP_AUTOC 1,128,0,F25
#CHR_POS_AUTOC 0,(320+160),F24,48
#CHR_POS_SAVEC 0
#CHR_ALP_SAVEC 1
    voice "NRI04A_RI001"
    莉莉丝 "「婆婆，发生了什么事吗？」"
    "刚走进店里，莉莉丝把包放在手边的桌子上，向富美子婆婆问道。"
    "当然，这也是我想知道的。"
    voice "NRI04A_FU001"
    富美子 "「其实是这样的，我朋友在龙境开了一个旅馆。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA04"),"True","img/RI_MAA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI04A_RI002"
    莉莉丝 "「龙境？」"
    play music  "BGM11"
    voice "NRI04A_FU002"
    富美子 "「听说过吗？那是个被山和海包围，能令人心情平静的地方，去过自然知道它的超凡之处。」"
    if not persistent.dictlist[48] and persistent.show_dict:
        $persistent.dictlist[48]=True
        show screen dict_pop(i=48)
    志雄 "「啊，好像，我之前在电视里看到过。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA02"),"True","img/FU_MAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI04A_FU003"
    富美子 "「对对，应该就是那个。最近，那边游客也开始增多了。」"
    voice "NRI04A_FU004"
    富美子 "「然后呢，我的朋友邀请我去玩。怎么样，我们三个一起？」"
    志雄 "「三人，我也去吗？」"
    voice "NRI04A_FU005B"
    富美子 "「当然。志雄已经像是我们家族一员的存在了。」"
    志雄 "「婆婆……」"
    "家族……吗？"
    "能被这样看待，我稍稍有些高兴。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA01"),"True","img/FU_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI04A_FU006"
    富美子 "「莉莉丝也没关系吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC04"),"True","img/RI_MAC04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI04A_RI003"
    莉莉丝 "「哎？嗯、嗯……」"
    voice "NRI04A_FU007"
    富美子 "「怎么了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC06"),"True","img/RI_MAC06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI04A_RI004"
    莉莉丝 "「啊……那个……对、对了，我们还是备考生吧。那样大玩特玩没关系吗？」"
    voice "NRI04A_FU008"
    富美子 "「那样的话，在旅行之前以及回来之后好好看书吧。反正现在是暑假中，也不可能一直都集中精神看书的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA02"),"True","img/FU_MAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI04A_FU009"
    富美子 "「那么志雄，你要好好看着这孩子复习哟。」"
    志雄 "「了解，不过我的成绩也没有多好呢……」"
    voice "NRI04A_FU010"
    富美子 "「没关系。只要有志雄在，那孩子就不会逃走的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA03"),"True","img/RI_MAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI04A_RI005"
    莉莉丝 "「说、说什么呢婆婆！」"
    voice "NRI04A_FU011"
    富美子 "「哈哈哈。店里有我在，你不用操心，专心看书吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA06"),"True","img/RI_MAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI04A_RI006"
    莉莉丝 "「真是的，那么，具体是什么时候呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA01"),"True","img/FU_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI04A_FU012"
    富美子 "「嗯……２８号到３１号，这个时间，那边似乎比较方便。」"
    play sound "SE02_05"
    "拿出手机的富美子婆婆眯起眼睛仔细确认邮件的内容。"
    window hide
    play sound "SE02_05"
    pause (16/32.0)
    play sound "SE02_05"
    "看来她在和她的朋友发短信。"
    志雄 "「２８号吗……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA04"),"True","img/RI_MAA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    莉莉丝 "「……」"
    志雄 "「嗯？怎么了，莉莉丝？」"
    voice "NRI04A_RI008"
    莉莉丝 "「没，没什么。对了，志雄呢？你去吗？」"
    $F83=0
    $F84=0
#RSET F83
#RSET F84
    志雄 "「我吗……」"
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    menu:
        "一起去家族旅行":
            $F7=0
        "还是不去了":
            $F7=1
    if F7==0:
        jump L_NRI04A_SEL00_A
    if F7==1:
        jump L_NRI04A_SEL00_B
label L_NRI04A_SEL00_A:
    "是呢，这种机会也很少才有。"
    "就接受婆婆的好意吧。"
    志雄 "「嗯。我也一起去吧。」"
    if F83==0:
        jump L_BRA_01_A
    jump L_BRA_01_B
label L_BRA_01_A:
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA02"),"True","img/FU_MAA02A@2x.png") as lh0 zorder (10+0):
        xcenter .75
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAB02"),"True","img/RI_MAB02A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    with dissolve
    jump L_BRA_01_X
label L_BRA_01_B:
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA02"),"True","img/FU_MAA02A@2x.png") as lh0 zorder (10+0):
        xcenter .75
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAB01"),"True","img/RI_MAB01A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    with dissolve
    jump L_BRA_01_X
label L_BRA_01_X:
    voice "NRI04A_RI009"
    莉莉丝 "「真的？」"
    志雄 "「嗯，机会难得。我也没怎么旅游过。」"
    "对我这种母亲很早就去世了，老爸又不怎么在家的人来说，基本上是无缘『家族旅行』的。"
    "很小的时候似乎也被带去旅游过，不过基本不记得了。"
    "而且……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA04"),"True","img/RI_MAA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    莉莉丝 "「……？」"
#MESEX_A M_NOA,A_CH_RI,NRI04A_RI010,"【りりす】「……？」%K%P"
    "就算作为同行的保护者，能和莉莉丝一起旅行还是很愉快的。"
    "至少不会觉得无聊。"
    voice "NRI04A_FU013"
    富美子 "「那就好。如果志雄觉得不方便的话，我还打算改天呢。」"
    志雄 "「诶？明明是婆婆邀请的我，因为我的关系而改天不是说不过去了吗。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA01"),"True","img/FU_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI04A_FU014"
    富美子 "「你不去莉莉丝会很困扰的哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC06"),"True","img/RI_MAC06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI04A_RI011"
    莉莉丝 "「哎？我、我吗？为什么？」"
    "莉莉丝的视线有些飘忽不定。"
    voice "NRI04A_FU015"
    富美子 "「志雄不来你不会很无聊吗，我们两个反正一直都是在一起的。」"
#CHR_GET_POSC 1,F24,F25
#RSUB F24
#BG_LAY 3,RI_MXC03,3,F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAC03"),"True","img/RI_MAC03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#REEK_CHR 1
    voice "NRI04A_RI012"
    莉莉丝 "「没，没这回事！我和婆婆两个人就很高兴了！」"
#REMOVE_REEK_CHR 1
    hide bg3 with dissolve
#BG_PRI 3
    voice "NRI04A_FU016"
    富美子 "「好啦好啦。那么我就告诉他们２８号到３１号去了。」"
    志雄 "「不过，婆婆这样子没关系吗？店里还要忙的吧……」"
    voice "NRI04A_FU017"
    富美子 "「没关系的，也不是要连续休息几个月。让客人偶尔尝尝别的餐馆的东西，才能更了解到我们店里料理的美味呢。」"
    志雄 "「啊，嗯，也许是这样吧……不过，铃她每天都要来吃的，没关系吗？」"
    voice "NRI04A_FU018"
    富美子 "「啊，那孩子啊。没关系的，她也不小了。关键时候也该学会自己煮饭了。」"
    "她应该会煮饭的。应该是总被催稿，自己没时间做饭而已吧……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAB01"),"True","img/RI_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    if not persistent.dictlist[35] and persistent.show_dict:
        $persistent.dictlist[35]=True
        show screen dict_pop(i=35)
    voice "NRI04A_RI013"
    莉莉丝 "「铃也可以去酪萨克吃的吧？」"
    "莉莉丝恶作剧般的笑了笑。"
    "当然，莉莉丝是知道铃的弟弟，稻穗信，在酪萨克打工才这么说的。"
    "不过，信则一直在逃避着和铃的关系……"
    志雄 "「应该没问题的……」"
    jump L_NRI04A_SEL00_X
label L_NRI04A_SEL00_B:
    $F0-=1
    $F83=1
#RSET F83
    "嗯……"
    "思考了许久，我还是慢慢地开口说出我的决定。"
    志雄 "「我还是不去了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_MAA06"),"True","img/FU_MAA06A@2x.png") as lh0 zorder (10+0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA03"),"True","img/RI_MAA03A@2x.png") as lh1 zorder (10+1)
    voice "NRI04A_RI014"
    莉莉丝 "「诶！？为什么？」"
    志雄 "「刚才已经说过了，还需要复习，志愿方向也不得不考虑……」"
    志雄 "「而且，妨碍你们一家人的家族旅行也不大好……」"
    voice "NRI04A_FU019"
    富美子 "「志雄，在这里坐下。」"
    志雄 "「啊？」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SORT 2,0
#CHR_INIC 2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_XAA06"),"True","img/FU_XAA06A@2x.png") as lh2 zorder 100:
        ypos 0.0
    with dissolve
    voice "NRI04A_FU020"
    富美子 "「我说过了吧。志雄已经是我们的家人了。」"
    志雄 "「是，是的……」"
    voice "NRI04A_FU021"
    富美子 "「志雄如果真的很忙，或者有别的理由的话，我也不会强求。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_XAA05"),"True","img/FU_XAA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI04A_FU022"
    富美子 "「不过，只是顾虑这些的话，我觉得很遗憾。」"
    志雄 "「婆婆……」"
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    menu:
        "一起去家族旅行":
            $F7=0
        "无论如何都拒绝":
            $F7=1
    if F7==0:
        jump L_NRI04A_SEL01_A
    if F7==1:
        jump L_NRI04A_SEL01_B
label L_NRI04A_SEL01_A:
    jump L_NRI04A_SEL00_A
label L_NRI04A_SEL01_B:
    $F0-=1
    $F84=0
#RSET F84
    志雄 "「即使这样，我还是……」"
#CHR_DSPC_L 1,RI_MAD03,(320-192),0,,
    "正当我想这么说是，我留意到了莉莉丝的视线。"
    voice "NRI04A_RI015"
    莉莉丝 "「志雄…………」"
    "莉莉丝不再说什么了。"
    "不过，交往了这么长时间，我知道。"
    "那是真正想要某种东西的时候，忍耐的眼神。"
    "莉莉丝和我一样，家庭环境有些复杂。"
    "因此，为了不给富美子婆婆添麻烦，很多苦她只会自己忍住。"
    "这种时候给与她力量……这不正是我的责任吗？"
    jump L_NRI04A_SEL00_A
label L_NRI04A_SEL00_X:
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
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT