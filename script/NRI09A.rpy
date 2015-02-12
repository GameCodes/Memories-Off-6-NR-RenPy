label NRI09A:
    $currentlabel = "NRI09A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '28'
    $date = '5'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG65AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG65AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    play music  "BGM12"
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
    "随着电车一路摇晃，２小时不到。我们到达了目的地龙境站。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SBC01"),"True","img/RI_SBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.2
    with dissolve
    voice "NRI09A_RI000"
    莉莉丝 "「志雄～太慢了～！」"
    志雄 "「等等我啊，你的东西都是我在拎，很重的。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我双手拎着自己和莉莉丝的包，拼命追赶着走在我前面的莉莉丝。"
    "莉莉丝出门带了两个包，明显，我要全程负担着其中一个的重量。"
    "真是的，为什么这家伙的行李有这么多啊？"
    志雄 "「哈……」"
    "我一边叹着气，一边钻进了莉莉丝叫来的出租车里。"
    window hide
    play sound "SE06_19L"
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
#BG_PRI 1
#BG_INIC 0
    show expression "img/NIMG01B@2x.png" as bg0 zorder 0
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
#EFF_STAC 0,CLOUD_B,EFF_NOSKIP
    pause (960/32.0)
#EFF_STPC 0,EFF_SKIP
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG66AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG66AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA04"),"True","img/RI_MBA04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE06_20"
    play sound "SE06_21"
    pause (60/32.0)

#EFF_STPC 0,EFF_SKIP
    hide bg1 with dissolve
    voice "NRI09A_RI001"
    莉莉丝 "「难道这里就是那家旅馆吗？」"
    "到了一个建筑物旁，莉莉丝一边比对和从富美子婆婆那儿拿到的地图，一边快步走了进去，我也紧随其后。"
    show expression "img/BG60AA@2x.jpg" as bg_over zorder 2 with dissolve
    if not persistent.dictlist[49] and persistent.show_dict:
        $persistent.dictlist[49]=True
        show screen dict_pop(i=49)
    "我们走近这家旅馆，门口的招牌上写着『宝树庵』几个字。"
    志雄 "「宝树庵……看来没错了」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA01"),"True","img/RI_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI002"
    莉莉丝 "「不会错的。一直站在这里也不是个办法，总之先进去吧。」"
    志雄 "「说的也是。」"
    "希望不要被质问道『你们是谁啊？』之类的话。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
#FADE_IN 0
    "结果确实不是『你们是谁？』这样的质问。"
    window hide
#FADE_OUT 0
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG61AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG61AA@2x.jpg" as bg0 with dissolve
#SE_WATC 0
#FADE_IN 1
    voice "NRI09A_SN000"
    信？ "「欢迎光临宝树庵～」"
    play music  "OBGM25"
    "刚走进旅馆就听到了一个过分熟悉的声音。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA02"),"True","img/SN_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    if not persistent.dictlist[8] and persistent.show_dict:
        $persistent.dictlist[8]=True
        show screen dict_pop(i=8)
    voice "NRI09A_SN001"
    信 "「哦，终于来了吗，塚本君和莉莉丝」"
    志雄 "「诶？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,(320+160)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA02"),"True","img/SN_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA03"),"True","img/RI_MBA03A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .75
    with move
#CHR_POS_AUTOC 0,(320-160),F24,40
    pause (24/32.0)
#CHR_ALP_AUTOC 1,128,0,F25
#CHR_POS_SAVEC 0
#CHR_ALP_SAVEC 1
    voice "NRI09A_RI003"
    莉莉丝 "「啊！？稻穗君的……那个，还是说伪装稻穗君的人？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA03"),"True","img/SN_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_SN002"
    信 "「……为什么会怀疑我是假的啊。我是真的啦，是真的！」"
    志雄 "「可是，你怎么会在这里呢？」"
    window hide
    hide lh0 with dissolve
    hide lh1 with dissolve
#BG_INIC 1
    show expression "img/BG62AA@2x.jpg" as bg0 zorder 0 with dissolve
    hide bg1 with dissolve
    "我和莉莉丝一边跟着信前往二楼的房间，一边对稻穗发问。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBB01"),"True","img/SN_MBB01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA06"),"True","img/RI_MBA06A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    voice "NRI09A_RI004"
    莉莉丝 "「真令人吃惊。」"
    voice "NRI09A_SN003"
    信 "「不好意思啦，富美子婆婆要我保密的。」"
    "按他的说法，他这个夏天在这里打工。"
    "这次也受了富美子婆婆的委托，照顾我们两个。"
    志雄 "「富美子婆婆所说的『她已经安排好了』，就是指这个吗……」"
    "我回想起昨天婆婆所说的话。"
    "多亏了稻穗开门见山的解释，旅馆的人很快理解了莉莉丝是富美子婆婆的孙女，而我则被解释为陪同她一起来的……"
    志雄 "「不过，富美子婆婆也真是爱卖关子。直说稻穗在，不就好了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA02"),"True","img/SN_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_SN004"
    信 "「啊啊，是我提议不要告诉你们的。当然，看来富美子婆婆也确实很乐意地接受了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA03"),"True","img/RI_MBA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI005"
    莉莉丝 "「诶？为什么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA06"),"True","img/SN_MBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_SN005"
    信 "「那样不是更有意思吗？看到我你们两个都吃了一惊吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA06"),"True","img/RI_MBA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    志雄 "「只、只是这样吗……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA05"),"True","img/SN_MBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_SN006"
    信 "「什么只是这样啊，惊喜对人生来说是必不可少的。」"
    "稻穗会出现在这里，不管怎么说都太出人意料了……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBB01"),"True","img/SN_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_SN007"
    信 "「而且，来这里的路上，你们两个一定早就蠢蠢欲动了吧？手牵着手……可恶，年轻真令人嫉妒！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBA02"),"True","img/RI_MBA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    "……这家伙该不会和亨是兄弟吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA02"),"True","img/SN_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_SN008"
    信 "「哦，就是这里了。」"
    "稻穗停在了名为『桔梗之间』的房间前。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    show expression "img/BG63AA@2x.jpg" as bg1 zorder 1 with dissolve
    play sound "SE00_46"
    pause (32/32.0)
    stop music fadeout 1
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
    hide bg1 with dissolve
#BG_ALPC 1
#BG_PRI 0
#BG_PRI 1
    scene expression "img/BG63AA@2x.jpg" as bg0 with dissolve
#SE_WATC 0
    play music  "BGM11"
    voice "NRI09A_SN009"
    信 "「这里就是你们两人的爱之屋了。」"
    志雄 "「诶……？难道说？」"
    voice "NRI09A_RI006"
    莉莉丝 "「难道，我和志雄在同一间……？」"
    voice "NRI09A_SN010"
    信 "「啊啊，这也是为你们着想。没事的，富美子婆婆那边我会保密的。」"
    window hide
#CHR_INIC 0
#CHR_INIC 1
#CHR_DSPWC_F 0,1,SN_LBA01,RI_LBA03
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA01"),"True","img/SN_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA03"),"True","img/RI_LBA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    志雄 "「等、等一下，这样不太好吧！」"
    voice "NRI09A_RI007"
    莉莉丝 "「对、对啊！同一间房间也太……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA04"),"True","img/SN_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_SN011"
    信 "「喂喂，冷静下来。实际上，由于昨天突然来了一个旅游团，现在已经没有别的空房了。」"
    志雄 "「……啊。怎么办，莉莉丝？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD05"),"True","img/RI_LBD05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI008"
    莉莉丝 "「怎么办……没办法了？那么……」"
    志雄 "「只能这样了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA02"),"True","img/RI_LBA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI009"
    莉莉丝 "「是、是呢。没办法了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_LBA02"),"True","img/SN_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_SN012"
    信 "「啊哈，那么，两位请进吧～」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "和风式的屋子，地上铺着榻榻米，满满的都是怀旧的气息。刚铺好的房间很干净，也很漂亮，令人心情舒畅。"
    志雄 "「哈，这屋子不错嘛。」"
    voice "NRI09A_RI010"
    莉莉丝 "「嗯。我也很喜欢和风的味道。」"
    "莉莉丝一边环视着房间一边卖力地点着头。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA02"),"True","img/SN_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_SN013"
    信 "「看来两位顾客都很满意呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBB01"),"True","img/SN_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_SN014"
    信 "「那么，有什么事就直接找我说吧。我带着手机，工作时间也不会走太远的。」"
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
    play sound "SE00_48"
    "等稻穗走出房间，我和莉莉丝把行李放在榻榻米上。"
    play sound "SE03_55"
    志雄 "「哈，好重……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBC04"),"True","img/RI_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM02"
    voice "NRI09A_RI011"
    莉莉丝 "「最近总是在忙学生会的工作，身体素质不行了吧？」"
    志雄 "「重点是……拎着两个旅行用的包，换谁都会累的吧！」"
    志雄 "「你为什么要带这么多东西啊……又不是去海外旅行。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA04"),"True","img/RI_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI012"
    莉莉丝 "「我不是说了么，女孩子有很多东西要准备的！」"
    志雄 "「是这样吗……」"
    "真是的，完全弄不明白女孩子那些所谓的隐私。"
    voice "NRI09A_RI013"
    莉莉丝 "「话说回来，还真是被稻穗吓了一跳……」"
    志雄 "「可不是，虽然大致能猜到会有些什么，没想到等着我们的是稻穗……富美子婆婆也真喜欢恶作剧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBB02"),"True","img/RI_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI014"
    莉莉丝 "「嗯。可是……多亏这样……」"
    志雄 "「……？」"
#MESEX_A M_NOA,A_CH_SI,"【志雄】「……？」%K%P"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD01"),"True","img/RI_LBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI015"
    莉莉丝 "「没、没什么。有这样漂亮的房间真是太好了！」"
    志雄 "「是啊。难得的机会，就慢慢享受吧。」"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    pause (32/32.0)
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/EXBG04A@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBG02"),"True","img/RI_ZBG02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_IN 1
    "接下来……"
    play sound "SE06_29L"
    "看时间，刚过中午，距离晚餐还有很长时间。"
    play sound "SE03_64"
    "然后房间里只有我和莉莉丝。"
    "本来计划中就只有富美子婆婆，莉莉丝和我三个人来，会成为两人独处的情况也是理所当然的……"
    莉莉丝 "「……」"
    "莉莉丝从刚才起就不说话。"
    "两人独处的情况下，要是不说话的话，总觉得很尴尬……"
    "唔唔……像往常一样，有什么无聊的对话也行，根本不必这么紧张嘛……"
    "……"
    window hide
    stop sound
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBH02"),"True","img/RI_ZBH02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#MES_SYNC2
    voice "NRI09A_RI017"
    莉莉丝 "那个！"
    志雄 "我说！"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBF03"),"True","img/RI_ZBF03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE03_64"
    "……两个人竟然同时开口。"
    voice "NRI09A_RI018"
    莉莉丝 "「什，什么？」"
    志雄 "「呃，你有什么话先说吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBF02"),"True","img/RI_ZBF02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI019"
    莉莉丝 "「我也没什么大不了的事。还是你先说吧！」"
    志雄 "「其实我也没什么……」"
    voice "NRI09A_RI020"
    莉莉丝 "「我，我也是……」"
    "我和莉莉丝相互躲闪着。"
    play sound "SE06_29L"
    "……究竟是什么状况！？"
    "简直就像害羞的情侣一样……"
    莉莉丝・志雄 "「……」"
    "不过。仔细想想，我和莉莉丝成为恋人以来，也几乎没有两个人独处的时间。"
    "在学校时和箱崎以及亨在一起的时间居多。学校之外……比如说在『富美』见到莉莉丝的时候也总有富美子婆婆在。"
    "所以说，面对现在这种情景，我们彼此还真是很不习惯。"
    stop sound
    志雄 "「总、总之……」"
    "为了冲淡尴尬的气氛，我刻意提高了说话的声音。"
    志雄 "「既然难得来这里一趟，我们去哪里逛逛吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBI01"),"True","img/RI_ZBI01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI022"
    莉莉丝 "「是、是呢……说的也是。」"
    志雄 "「只要带上钱包和手机就行了……」"
    window hide
    show expression "img/BG63AA@2x.jpg" as bg_over zorder 2 with dissolve
    play sound "SE03_66"
    "正当我站起身的时候，我看到莉莉丝从包里取出什么小东西。"
    志雄 "「……？」"
#MESEX_A M_NOA,A_CH_SI,"【志雄】「……？」%K%P"
    "看起来像是护身符之类的……是什么呢？"
    "虽然有些在意，可碍于这微妙的气氛，实在不知道该怎么问出口。"
    window hide
    stop se fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
    stop music fadeout 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA01"),"True","img/RI_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK
#BG_INIC 0
    show expression "img/BG67AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG67AA@2x.jpg" as bg0 with dissolve
#EFF_STAC 0,SUNLIGHT_BG67_FRONT,EFF_SKIP
#EFF_STAC 1,SUNLIGHT_BG67_BACK,EFF_SKIP
    play sound "SE05_15L"
    pause (32/32.0)
#FADE_IN 1
    play music  "BGM12"
    "我们离开了旅馆，去附近的山里晃了晃。"
    voice "NRI09A_RI023"
    莉莉丝 "「山里面的空气果然很新鲜。」"
    志雄 "「嗯。总觉得气氛很宁静，感觉好舒畅。」"
    "走到外面之后，房间里的那种紧张感几乎完全消失了。"
    "也许，就是因为是那种封闭的空间里才会紧张。像这样走在外面，和平时同莉莉丝一起上学放学没什么区别。"
    "……大概，在房间里的那种紧张感，就是恋人之间才会特有的感觉吧。"
    "不过，这种气氛似乎并不适合我们。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBC05"),"True","img/RI_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI024"
    莉莉丝 "「嗯？怎么了，一直看着我？」"
    志雄 "「啊不，没什么。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBC04"),"True","img/RI_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI025B"
    莉莉丝 "「……？那就好。」"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/BG71AA@2x.jpg" as bg0 with dissolve
#EFF_STAC 0,SUNLIGHT_BG71,EFF_NOSKIP
#SE_VOLC 1,255
#FADE_IN 1
    if not persistent.dictlist[51] and persistent.show_dict:
        $persistent.dictlist[51]=True
        show screen dict_pop(i=51)
    志雄 "「没想到这种地方也有神社呢——」"
    "在我和莉莉丝面前出现了一段台阶。"
    window hide
#CHR_SET_BACK
#EFF_PRI 0
#EFF_PRI 1
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA04"),"True","img/RI_LBA04A@2x.png") as lh0 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI026"
    莉莉丝 "「看起来不是很大的神社。」"
    voice "NRI09A_RI027"
    莉莉丝 "「难得出来玩，要是有那种大红色的气派的建筑，从下到上整齐地排成一排的台阶也就好了。」"
    志雄 "「这里本来似乎也不是特别著名的观光地，这种朴素的感觉倒是比较自然呢。」"
    志雄 "「那么，我们进去看看吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD01"),"True","img/RI_LBD01A@2x.png") as lh0 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI028"
    莉莉丝 "「说的也是。说不定有什么护身符之类的有纪念价值的东西呢。比如说为考试祈福之类的？」"
    志雄 "「一开始就想依靠神明吗……」"
    "果然，莉莉丝从包里拿出来特意带在身上的，是别的什么护身符吧。"
    "不过，只买一个护身符作为给莉莉丝的生日礼物也太寒酸了吧……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD04"),"True","img/RI_LBD04A@2x.png") as lh0 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI029"
    莉莉丝 "「有什么关系。身边的东西能利用则利用嘛。」"
    志雄 "「对你来说，神明还真是随随便便的存在呢。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "莉莉丝和我并排着一步步往上走。"
    "——忽然，我感到了一只柔软又温暖的手。"
    window hide
#EFF_PRI 0
#EFF_PRI 1
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBB07"),"True","img/RI_XBB07A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    "是莉莉丝握住了我的手。"
    志雄 "「莉莉丝……？」"
    "面对我的困惑的语气，莉莉丝并没有回应，取而代之的是略带些兴奋的话语。"
    voice "NRI09A_RI030"
    莉莉丝 "「那、那么，我们走吧！？」"
    志雄 "「啊，喂、喂！」"
    "莉莉丝牵着我的手，向前快步走了起来。而还没搞清楚状况的我则在她的拉拽下勉强赶上了步伐。"
    window hide
#SE_VOLC 1,0
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    scene expression "img/BG73AA@2x.jpg" as bg0 with dissolve
#CHR_SORT 1
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBC05"),"True","img/RI_XBC05A@2x.png") as lh0 zorder (10-1):
        ypos 0.0
    with dissolve
#EFF_PRI 0
#EFF_PRI 1
#EFF_STAC 0,SUNLIGHT_BG50_FRONT,EFF_SKIP
#EFF_STAC 1,SUNLIGHT_BG50_BACK,EFF_SKIP
#SE_VOLC 1,128
    hide bg1 with dissolve
    play music  "BGM11"
    voice "NRI09A_RI031"
    莉莉丝 "「呼……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBC05"),"True","img/RI_LBC05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#ROUTINE_STA
#EFF_PRI 0
#EFF_PRI 1
#CHR_ALP_AUTOC 1,0,1,F24
#CHR_ALP_AUTOC 0,128,1,F24
#ROUTINE_STP
    "莉莉丝疲惫地喘了口气。爬完台阶后，我和莉莉丝把手分开。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA01"),"True","img/RI_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI032"
    莉莉丝 "「里面还是很大的嘛。」"
    志雄 "「是啊……而且很宁静，气氛很不错呢。」"
    voice "NRI09A_RI033"
    莉莉丝 "「是呢。整个人沉浸在其中，有一种心灵在接受到洗礼的感觉。」"
    "听莉莉丝的平静而随意的话语，似乎完全没有被刚才手牵手的行为所影响到。"
    "对莉莉丝来说，与其说这是牵手，还不如说是在爬台阶的时候拉着我吧……"
    "……是我自作多情了吗？"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    show expression "img/BG72AA@2x.jpg" as bg0 zorder 0 with dissolve
#EFF_STPC 0,EFF_NOSKIP
#EFF_STPC 1,EFF_NOSKIP
#EFF_STAC 0,SUNLIGHT_BG50_FRONT,EFF_SKIP
#EFF_STAC 1,SUNLIGHT_BG50_BACK,EFF_SKIP
#EFF_PRI 0
#EFF_PRI 1
    scene expression "img/BG72AA@2x.jpg" as bg0 with dissolve
    hide bg1 with dissolve
    "我们参拜了神社，之后又去画了绘马。"
    "莉莉丝在绘马上写了『商业繁荣』四个字后，又在后面加上了几个字。"
    window hide
#BG_LAY 3,RI_LXC03,2,((320)-(320))
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBC03"),"True","img/RI_LBC03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NRI09A_RI034"
    莉莉丝 "「喂，不要看啦！」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
    志雄 "「什么啊，有什么没关系？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA02"),"True","img/RI_LBA02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI035"
    莉莉丝 "「你才是，写了些什么啊？」"
    志雄 "「我嘛……我随便写什么都行吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA05"),"True","img/RI_LBA05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI036A"
    莉莉丝 "「什么嘛，真狡猾。{w=6}{nw}"
#MESA A_CH_RI,NRI09A_RI036A,"【りりす】「什么嘛，真狡猾。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD01"),"True","img/RI_LBD01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI036B"
    extend "那么我们同时交换看吧」"
#CHR_SORT 1
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBC01"),"True","img/RI_XBC01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    志雄 "「真没办法……一，二……」"
#BG_BLUR 0
#MESA A_CH_SI,"【志雄】「真没办法……一，"
#THREAD_STA 1,THREAD_MOV_CHR0
#MESX "二……」%K%P"
#THREAD_WAT 1
    hide lh0 with dissolve
    "我在自己的绘马上写了『两人能平安无事地通过考试』。"
    "当然，这两人指的是我和莉莉丝。"
    "相对的，莉莉丝写的是……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBC05"),"True","img/RI_XBC05A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    莉莉丝 "「…………」"
    志雄 "「…………」"
    "『希望能永远在一起』"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBA02"),"True","img/RI_XBA02A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI038"
    莉莉丝 "「…………什、什么嘛。谁都没说要和你在一起吧？」"
    志雄 "「是呢。富美子婆婆、箱崎、亨、铃还有春日……大家要是能一直在一起就好了。」"
    志雄 "「可是，我们各自有各自要走的路，以后会怎么样真是没办法预料呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBA04"),"True","img/RI_XBA04A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI039"
    莉莉丝 "「志雄……」"
    志雄 "「不过……」"
    "我轻轻握住莉莉丝的手。"
    志雄 "「至少，我们两个能永远在一起就好了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBA07"),"True","img/RI_XBA07A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI040"
    莉莉丝 "「……嗯。」"
    window hide
#SE_VOLC 1,0
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG66AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG66AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBB01"),"True","img/RI_LBB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#EFF_STAC 0,SUNLIGHT_BG66_FRONT,EFF_SKIP
#EFF_STAC 1,SUNLIGHT_BG66_BACK,EFF_SKIP
#EFF_PRI 0
#EFF_PRI 1
#SE_VOLC 1,255
#FADE_IN 1
    play music  "BGM01NL"
    voice "NRI09A_RI041"
    莉莉丝 "「这条路一直沿着山，铺设到相当靠上的地方呢。」"
    志雄 "「说起来，亨好像也提到过在山上骑车很爽来着。」"
    志雄 "「他还说，要是有了女朋友，就带她一起去远足呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBC02"),"True","img/RI_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI042"
    莉莉丝 "「尽享骑乘人生……一点都不像一个即将升学的学生该说的话。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBC01"),"True","img/RI_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI043"
    莉莉丝 "「说起来，志雄有驾照了吗？」"
    志雄 "「考驾照需要很多钱的吧……不过，考完试后，有时间的话我会考虑的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD01"),"True","img/RI_LBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI044"
    莉莉丝 "「嗯，我很期待的。」"
    志雄 "「你自己不打算考吗，你要比我在行吧？」"
    voice "NRI09A_RI045"
    莉莉丝 "「没关系，我想坐在副驾驶。啊，坐在车后面也行。」"
    志雄 "「哈，那也好……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA01"),"True","img/RI_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI046"
    莉莉丝 "「啊，这条路一直走下去的话，应该能看到湖吧。」"
    "身旁的路标写着，山上有名为『门亚湖』的大湖。从地图上看的话，那应该是个很大的湖。"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG77AA2@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG77AA2@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD01"),"True","img/RI_MBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#SE_VOLC 1,255
#FADE_IN 1
    voice "NRI09A_RI047"
    莉莉丝 "「嘿～景色真是不错呢。」"
    "莉莉丝借着树木间的间隙眺望山脚。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBB01"),"True","img/RI_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI048"
    莉莉丝 "「看，志雄快看！」"
    志雄 "「好、好。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "有些无奈地走到莉莉丝身边。从高处俯视我们刚才所在的小镇，所有的景色一览无余，真是一幅美妙的画卷。"
    志雄 "「到山顶的话，应该连海都能看的到吧。」"
    voice "NRI09A_RI049"
    莉莉丝 "「是啊。有山有湖还有海……总觉得很是奢侈呢。」"
    志雄 "「说起来好像是挺难得的。」"
    "我和莉莉丝再次并排走了起来。"
    "……突然间，右手又有一种被握住的感觉。"
    志雄 "「那个……」"
    "在我身旁走着的莉莉丝握住了我的手。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,((320+192)+80)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBA02"),"True","img/RI_XBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter 0.95
        linear 1 xcenter 0.8
    with dissolve
#MOV_CHR_INIT 40
#MOV_CHR0 128,(320+192)
#MOV_FOCUS_BG 512
#MOV_CHR_GO 0
#MESEX_A M_NOA,A_CH_RI,NRI09A_RI050,"【りりす】「……」%K%P"
    莉莉丝 "「……」"
    "莉莉丝一言不发。只是略微朝向这里。"
    "刚才在神社时，我以为她只是拉着我爬台阶而已。"
    志雄 "「……」"
    莉莉丝 "「……」"
#MESEX_A M_NOA,A_CH_SI,"【志雄】「……」%K%P"
#MESEX_A M_NOA,A_CH_RI,NRI09A_RI051,"【りりす】「……」%K%P"
    window hide
#ROUTINE_STA
#BG_PRIC 0
#CHR_PRIC 0
#BG_INIC 3
    scene expression "img/NIMG01B@2x.png" as bg3 zorder 3
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
#EFF_STAC 0,CLOUD_B,EFF_NOSKIP
#BG_BLUR 0
#ROUTINE_STP
#ROUTINE_STA
#BG_ALP_AUTOC 0,0,0,1
#CHR_ALP_AUTOC 0,0,0,1
#ROUTINE_STP
    "就这样，我们许久都没说话，只是默默地往前走。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
#ROUTINE_STA
#EFF_STPC 0,EFF_SKIP
#EFF_PRI 0
#BG_PRIC 0
#CHR_PRIC 0
#ROUTINE_STP
    stop music fadeout 132
    pause (64/32.0)
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/BG77AA1@2x.jpg" as bg0
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBA02"),"True","img/RI_XBA02A@2x.png") as lh0 zorder 100:
        ypos 0.0
        xcenter .75
    with dissolve
#FADE_IN 1
    志雄 "「……呼，就算是我也开始有点累了。」"
    志雄 "「差不多该回去了吧？」"
    window hide
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBA03"),"True","img/RI_XBA03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#CHR_POSC 0
    voice "NRI09A_RI052"
    莉莉丝 "「诶，那湖呢？」"
    志雄 "「按照我们现在的速度，看完湖回去之后应该已经很晚了。考虑到晚饭的时间，我们还是明天再来吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBA02"),"True","img/RI_XBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI053"
    莉莉丝 "「嗯，嗯……」"
    志雄 "「那我们回去吧。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我和莉莉丝往回走去，返回时我们依旧手牵着手。"
    window hide
    show expression "img/BG77EA1@2x.jpg" as bg0 with dissolve
    scene expression "img/BG77EA1@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
#FADE_OUT 1
    show expression "img/BG67EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG67EA@2x.jpg" as bg0 with dissolve
    play sound "SE05_13L"
    pause (32/32.0)
#FADE_IN 1
    "回去的路上，太阳也不知不觉的黯淡了光芒。果然在那里折返是明智之举呢。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_COLC 0,128,120,112
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBC04"),"True","img/RI_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI054"
    莉莉丝 "「傍晚有些冷呢。」"
    if not persistent.dictlist[24] and persistent.show_dict:
        $persistent.dictlist[24]=True
        show screen dict_pop(i=24)
    志雄 "「因为山上空气比较稀薄的关系吧，天空和气候也有些不同呢。」"
    志雄 "「不过，这样就觉得冷的话，你是不是感冒了？没事吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA03"),"True","img/RI_LBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI055"
    莉莉丝 "「不、不是感冒啦！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA02"),"True","img/RI_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI09A_RI056"
    莉莉丝 "「只是觉得有些冷而已……」"
    "说着。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI04A")]=True
    scene expression "img/EVN_RI04A@2x.jpg" as bg_over zorder 2 with dissolve
    play music  "BGM13"
    "莉莉丝拉住我的胳膊，把身体凑了过来。"
    志雄 "「莉、莉莉丝？」"
    "透过手臂，莉莉丝的心跳传到了我身上。"
    voice "NRI09A_RI057"
    莉莉丝 "「因、因为有些冷。」"
    "莉莉丝的心跳很快。"
    voice "NRI09A_RI058"
    莉莉丝 "「这样子，风能吹到身上的面积就小了」"
    "脸有些微红，莉莉丝有些遮遮掩掩地说道。"
    "还真是非常笨拙的接触方式啊……"
    "明明交往已经半年以上了，可却完全不习惯这种恋人的关系，本以为这正是我们的风格呢。"
    志雄 "「那个～……」"
    "看来我也再靠近莉莉丝一点为好吧？"
    志雄 "「……暖、暖和吗？」"
    voice "NRI09A_RI059"
    莉莉丝 "「嗯……很暖和……」"
    志雄 "「……」"
    莉莉丝 "「……」"
    "不行。至今为止我们一直都是像朋友一样的关系，从没有如现在这般紧靠着过。"
    "结果，我们还是就这样，一言不发地回到了旅馆。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
#BG_ANM_OFFC 0
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop se
    stop sound
    stop music fadeout 1
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_MOV_CHR0
#BG_ALP_AUTOC 2,128,0,F123
#CHR_ALP_AUTOC 0,0,0,F123
#CHR_ALP_AUTOC 1,128,0,F123
#BG_ALP_SAVEC 2
#CHR_ALP_SAVEC 0
#CHR_ALP_SAVEC 1
#EOT
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT