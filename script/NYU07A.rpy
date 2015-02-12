label NYU07A:
    $currentlabel = "NYU07A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '30'
    $date = '0'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
    scene expression Solid("000") with fade
    show expression "img/NIMG15N-568h@2x.jpg" as cal zorder 5
    show expression "img/07_29_SATURDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG01AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG01AA@2x.jpg" as bg0 with dissolve
    play music  "OBGM27"
#EFF_STAC 1,SUN_LE,EFF_SKIP
#FADE_IN 1
    play sound "SE08_01"
    pause (32/32.0)
    play sound "SE02_02L"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    志雄 "「……不接啊，出什么事了，真是没办法啊。」"
    play sound "SE02_03"
    志雄 "「结乃……到底怎么了？」"
    "离截止日期只有两天了，打算给结乃打电话再商量一下，但不知为什么总是不通。"
    "有种不详的预感。我去了结乃家，没人在，坐电车回来时又打了她电话一次，依旧没人接。"
    "夏天的太阳高高地挂在空中，火辣辣的阳光炙烤着我的皮肤。"
    "走在路上有种要被烤焦的错觉。"
    志雄 "（不早点和结乃联络的话……）"
    "我想起昨天我发的短信，本来今天说好了哪怕不吃午饭也要商量的。"
    "不，确切的说，这只是我单方面的提议，并没有从结乃那里收到确认的回信。"
    "本来我以为她是默认了。"
    "虽然没有写明具体的时间，但是现在已经过了中午。"
    "再不快点决定的话会很麻烦的。"
    "这一点结乃也应该明白……"
    志雄 "「是不是学校里的事情走不开？……或者该不会是一个人先去酪萨克了吧？」"
    "并没有说在哪里集合，发生误解也是有可能的。"
    志雄 "「诶——」"
    志雄 "「这样瞎想也不是办法，总之，找不到线索的话，就从想得到的地方开始找好了。」"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU04B")]=True
    show expression "img/EVN_YU04B@2x.jpg" as bg2 zorder 2 with dissolve
    stop sound
    stop music fadeout 116
#BG_INIC 1
#BG_PRI 1
#EFF_STPC 1,EFF_SKIP
#BG_ALPC 0
#BG_ALPC 2
    hide bg1 with dissolve
    结乃 "「别了」"
#SCRMODE_SPC SCR_FULL
#MESA A_CH_YU,NYU07A_YU000_K,"【結乃】%S001%FS%n%n%n%n%n%n%n%FE%S060%FS%LC　　　　　　　　　　　　　　　　　　「别了」%LE%FE%K%O016"
    window hide
#SCRMODE_SPC SCR_WINDOW
#BG_INIC 1
#BG_PRI 1
    hide bg2 with dissolve
#BG_ALPC 0
#EFF_STAC 1,SUN_LE,EFF_SKIP
    hide bg1 with dissolve
    play sound "SE08_01"
    志雄 "「——诶！？」"
    "想起了讨厌的场景。"
    "虽然我认为不会走到那一步，但只要回忆起这句『再见了』，心里的阴影就无法拂去。"
    志雄 "「……不对不对不对不对。」"
    "为了寻找结乃，我走出车站。"
    voice "NYU07A_SU000"
    铃？ "「那边的少年，等一下。」"
    "……好像是刻意在等我一样，我被一个熟悉的声音喊住。"
    志雄 "「……嗯？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA01"),"True","img/SU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE03_90"
    voice "NYU07A_SU001"
    铃 "「真是好久不见啊。现在一个人么，志雄。」"
    window hide
    play music  "BGM05"
    "转过身，站在那里的是穿着一身紧身夹克的铃。"
    "很久没见过她了，不过还是老样子，骑车摩托车跑着跑那的，并不怎么回房间。"
    "铃摆着一副『不占便宜不罢休』的笑脸靠近过来。"
    "看着她的样子，我不由得感叹果然是那个人的姐姐啊。"
    志雄 "「有什么事么铃，现在稍微有点赶时间。」"
    voice "NYU07A_SU002"
    铃 "「原来有空啊，只是『稍微有点急』的话就先陪我一下吧？」"
    志雄 "「对不起，是非常赶时间。」"
    "不管我的抗议，铃用胳膊钳住我的脖子。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU003"
    铃 "「嗯？别说的这么无情啊。」"
    "边这样说着，一边把我往摩托车那里拉。"
    志雄 "「等等，铃！」"
    voice "NYU07A_SU004"
    铃 "「诶，只不过就在这周围转转罢了。」"
    "麻烦了，现在没有多余的时间和铃一起消磨时间。"
    志雄 "「很无聊么，不用工作吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB03"),"True","img/SU_LCB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NYU07A_SU005"
    铃 "「现实就是为了去逃避而存在的啊。」"
#REMOVE_REEK_CHR 0
    志雄 "「别一边耍帅一边说些不该说的话。」"
    "最近铃一直都在外面，没看到过她有好好工作。"
    "不过进入工作模式的铃都会将自己关在房间里，我看不到也是自然吧。"
    志雄 "（但是，骑着摩托车兜风的话，根本不会去写稿子……真的变成了逃避呢……）"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU006"
    铃 "「赶时间的话我送你好了，这样的话行了吧。」"
    志雄 "「哎，真是的，没办法呢。」"
    "虽然不好意思，将事情向铃说明后，还是请求铃带我一程。"
    stop music fadeout 132
    志雄 "「那个，铃，要送我的话，有一个请求。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU007"
    铃 "「哦，会是什么呢？说说看。」"
    "我的语气非常认真，而铃却像发现了新大陆一样高兴。"
    志雄 "「其实和结乃联络不上……现在准备去找她。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC05"),"True","img/SU_LCC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU008"
    铃 "「原来如此呢……是这样么。」"
    window hide
    play music  "OBGM16"
    "铃也认真起来。"
    "虽然我只是一句话，但她好像意识到事情的严重性了。"
    "没有追问我原委，铃直接把备用头盔塞给了我。"
    志雄 "「谢谢了，铃。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE06_09"
    pause (64/32.0)
    stop se fadeout 1
#FADE_OUT 1
#EFF_STPC 1,EFF_SKIP
    scene expression Solid("000") with fade
    stop se
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
#EFF_STAC 0,CLOUD_B,EFF_NOSKIP
    pause (32/32.0)
    play sound "SE06_15L"
#FADE_IN 1
    志雄 "（哇啊啊啊啊！）"
    "因为害怕铃那粗暴的驾驶，我拼命地抓住铃。"
    "虽然大声请求着把速度降下来，但铃只是笑笑而已。"
    志雄 "（可恶啊……这也太吓人了！！）"
    "我缩在在马路上窜来窜去的铃身后，大声将事情的前因后果说明了一下。"
    "把商议广播时的事情，昨天在水族馆发生的事情和最后的那句『别了』统统都告诉了铃。"
    "「并不是什么好征兆呢」，铃自言自语地说出感想。这句话让我整个后背都好像冻住了一般。"
    "小声嘟哝的铃，语气听起来少见的严肃。"
    voice "NYU07A_SU009"
    铃 "「事情我了解了，那么，想要去哪里？」"
    $F96=1
#RSET F96
    志雄 "「是呢，首先是……」"
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    menu:
        "总之先去澄空学园":
            $F7=0
        "赶去芦鹿岛的岸边":
            $F7=1
        "往酪萨克笔直前行":
            $F7=2
    if F7==0:
        jump L_NYU07A_SEL00_A
    if F7==1:
        jump L_NYU07A_SEL00_B
    if F7==2:
        jump L_NYU07A_SEL00_C
label L_NYU07A_SEL00_A:
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    hide bg3 with dissolve
    hide bg4 with dissolve
    hide bg5 with dissolve
#FADE_OUT 1
#GRAPH_ERS
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/BG08AA@2x.jpg" as bg0 zorder 0
    with dissolve
    pause (32/32.0)
    play sound "SE05_15L"
#FADE_IN 1
    "暑假中的澄空学园比想象中的还要清闲。"
    "虽然在操场上还有学生在练习，但在校舍内一个人都看不到。"
    "校庭里树木上的知了叫声回响在无人的教室里，让人感觉更加炎热。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
#FADE_IN 0
    "我笔直向学生会室走去，之后是广播室，连教室都转了一圈，最后回到等在校门口的铃那里。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128
    scene expression "img/BG06AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_15L"
#FADE_IN 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA01"),"True","img/SU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU010"
    铃 "「看上去花了不少时间，结果徒劳无功么？」"
    "看着我的脸，铃想都不想地这么说道。"
    "铃没有安慰人的习惯也没办法，但这句话还是深深地刺进了我的胸口。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA04"),"True","img/SU_LCA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU011"
    铃 "「别露出这种表情啊，我这边也是，这么热，还等了这么久。」"
    志雄 "「真是不好意思了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB03"),"True","img/SU_LCB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NYU07A_SU012"
    铃 "「去别的地方吧，来，摆出这副表情的话，本能找的到的东西也会找不到的哦。」"
    if F96:
        jump L_NYU07A_FLG00_B
#REMOVE_REEK_CHR 0
#IF F96!0, GOTO L_NYU07A_FLG00_B
label L_NYU07A_FLG00_A:
#MSGNO_SAV 1
    志雄 "「我到底摆着什么表情啊？」"
    jump L_NYU07A_SEL00_X
label L_NYU07A_FLG00_B:
#MSGNO_RET 1
#RSET F71
#RSET F72
#RSET F73
    $F96=0
    $F71=1
    志雄 "「我到底摆着什么表情啊？」"
    jump L_NYU07A_SEL00_D
label L_NYU07A_SEL00_B:
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    scene expression Solid("000") with fade
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/BG21AA@2x.jpg" as bg0 with dissolve
#EFF_PRI 0
#EFF_STAC 0,WATERTWINKLE,EFF_SKIP
    pause (32/32.0)
    play sound "SE06_14L"
#FADE_IN 1
    pause (48/32.0)
    stop sound
    play sound "SE06_31"
    pause (16/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE05_19L"
    play sound "SE08_14L"
    voice "NYU07A_SU013"
    铃 "「嗯，我们到了，真是好棒啊。」"
    志雄 "「铃，跑的太快、跑的太快了！中途好几次都差点掉下来啊！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC04"),"True","img/SU_LCC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU014"
    铃 "「什么啊，别这么没出息。结乃当初坐得很稳哦。」"
    志雄 "「……啊，是啊。结乃……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "环望海边，沙滩上混杂着许多人。"
    "现在是暑假兼周末，一家三口，成群的小学生，出游的中学生和大学生，总之男女老少都聚集海滩上。"
    "因为这里是比赛场地，结乃也许会一个人跑到这里取材。"
    "本来我是这么考虑的，但眼前如此之多的人却是我始料未及的。"
    "人实在是太多了。"
    志雄 "「我稍微在这附近找找看。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU015"
    铃 "「哦，去吧～我在这里等着。」"
    "这样说着，铃一个劲地挥手。"
    "虽然并没有期待能帮忙一起找……"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我对着铃无奈的笑了笑，往沙滩上走去。"
    "就算是一个人，也不能不找。"
    "既然无视了我的电话，就必须当面确认她的真意。"
    "然后，『别了』的意义，如果可以的话，也想问一下。"
    "如果是我想的太多就好了。"
    "是这样就好了……！"
    "从没有过这么强烈的欲望，想要立刻就见到结乃。"
    window hide
#SE_VOLC 0,0
#SE_VOLC 1,0
#EFF_STPC 0,EFF_SKIP
#EFF_PRI 0
#FADE_OUT 1
    pause (32/32.0)
#SE_VOLC 1,64
#SE_VOLC 0,128
#FADE_IN 1
#EFF_PRI 0
#EFF_STAC 0,WATERTWINKLE,EFF_SKIP
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA01"),"True","img/SU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE03_90"
    voice "NYU07A_SU016"
    铃 "「嗯～清爽的海风，湛蓝的天空，金黄的沙滩，潮起潮落之间，少年因为寻找恋人而满头大汗。」"
    voice "NYU07A_SU017"
    铃 "「美妙的夏天啊。」"
    志雄 "「呃……哈……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC04"),"True","img/SU_LCC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU018"
    铃 "「天气这么热，还这样来回跑。诶，结果要找的人不是还没找到嘛，就如字面上的一样，白搭。」"
    志雄 "「哈……哈……」"
    "真的是，无言以对。要调整呼吸都已经很困难了。"
    "虽然并不是一定要跑来跑去，但是一直找不到结乃很着急，双腿就不由自主地奔跑起来。"
    "结果就像铃所言，想在这个人山人海的地方找到一个女孩的确是不可能完成的任务。"
#EFF_STPC 0,EFF_SKIP
#EFF_PRI 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA01"),"True","img/SU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU019"
    铃 "「那么，去别的地方找找看吧。啊，在这之前还是先休息下比较好。」"
    voice "NYU07A_SU020"
    铃 "「喝点水再继续行动吧，中暑了的话就得不偿失了。」"
    if F96:
        jump L_NYU07A_FLG01_B
#IF F96!0, GOTO L_NYU07A_FLG01_B
label L_NYU07A_FLG01_A:
#MSGNO_SAV 1
    志雄 "「嗯……哈……」"
    jump L_NYU07A_SEL00_X
label L_NYU07A_FLG01_B:
#MSGNO_RET 1
#RSET F71
#RSET F72
#RSET F73
    $F96=0
    $F72=1
    志雄 "「嗯……哈……」"
    jump L_NYU07A_SEL00_D
label L_NYU07A_SEL00_C:
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    scene expression Solid("000") with fade
    stop se
    stop sound
#BG_SET_DEFC 0,BG97AA
#BG_SET_BACK 
#BG_INIC 1
    scene expression "img/BG35AA@2x.jpg" as bg1 zorder 1 with dissolve
    pause (32/32.0)
    play sound "SE06_14L"
#FADE_IN 1
    pause (48/32.0)
    stop sound
    play sound "SE06_31"
    pause (32/32.0)
    play sound "SE00_32"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA04"),"True","img/MH_LCA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "铃的摩托车如同飞翔一般的开到酪萨克，麻寻看见我们的时候也吓了一跳。"
    voice "NYU07A_MA000"
    麻寻 "「志雄！？怎么了，这么慌慌张张的？」"
    志雄 "「啊，麻寻，今天结乃有没有来过？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA06"),"True","img/MH_LCA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_MA001"
    麻寻 "「结乃？没有来过哦。比起这个……」"
    "麻寻，用手指着在店外等待我的铃，双眼死死盯着我。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA02"),"True","img/MH_LCA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_MA002"
    麻寻 "「志雄，那边的姐姐是哪位哦？」"
    "麻寻绝对是误会了。"
    志雄 "（真没办法啊……嗯？等一下……）"
    "比起立刻解释些什么，我忽然想到了一个更有趣的方法。"
    志雄 "「那个人……啊～下次再介绍给你，等稻穗回来的时候。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA06"),"True","img/MH_LCA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_MA003"
    麻寻 "「诶？什么？难道说……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA04"),"True","img/MH_LCA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_MA004"
    麻寻 "「是信君的女朋友！！」"
    志雄 "「哈？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LBB03"),"True","img/MH_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_MA005"
    麻寻 "「啊……什么啊，也不用这样卖关子吧。」"
    "虽然我并没有说谎，不过麻寻总是会把事情向着奇怪的方向想象。"
    志雄 "「总之那个人，一定要在稻穗在的时候才能介绍给你哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA02"),"True","img/MH_LCA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_MA006"
    麻寻 "「知道了啊，我会满怀期待的等着的。」"
    "等到稻穗回来的时候，肯定会受到麻寻连珠炮式的追问吧。"
    "看不到这个场景还真是有些可惜。"
    "在我们对话的时候，铃也并没有打算进店里，而是悠闲的在那里做着柔体体操。"
    "果然，就算愿意带我一程，她也没有想要来帮忙一起寻找结乃的意思。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA01"),"True","img/MH_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_MA007"
    麻寻 "「话说回来，结乃怎么了？」"
    志雄 "「是啊！那个，今天结乃有没有联络过你？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA06"),"True","img/MH_LCA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_MA008"
    麻寻 "「嗯？怎么了？难道你找不到她了吗？」"
    志雄 "「……是这么回事吧」"
    "麻寻也一样，马上就了解到了事情的状况。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LBB04"),"True","img/MH_LBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_MA009"
    麻寻 "「原来如此……」"
    "……这个危机般的状况，原来就这么容易被看出来吗。"
    "麻寻一个劲的叹气，耸了耸肩。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LBB03"),"True","img/MH_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_MA010"
    麻寻 "「到底做了些什么啊，前两天明明还是一对让人羡慕的恋人。」"
    志雄 "「请不要现在就使用过去式。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LBC03"),"True","img/MH_LBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_MA011"
    麻寻 "「啊，对不起，我失言了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LBC02"),"True","img/MH_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_MA012"
    麻寻 "「结乃没有和我联络过……你要不要去她家里看看呢？」"
    志雄 "「嗯……」"
    "不在这里啊。"
    "我匆匆离去，准备去找别的地方。"
    "再我推门而出的时候，麻寻在身后叫住了我。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA01"),"True","img/MH_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_MA013"
    麻寻 "「要加油哦，你们两个如果无法和好的话，我们也会寂寞的。」"
    志雄 "「……嗯。」"
    window hide
    show expression "img/BG35AA@2x.jpg" as bg_over zorder 2 with dissolve
    if F96:
        jump L_NYU07A_FLG02_B
#IF F96!0, GOTO L_NYU07A_FLG02_B
label L_NYU07A_FLG02_A:
#MSGNO_SAV 1
    "麻寻的目光里，满是真诚与担忧。"
    jump L_NYU07A_SEL00_X
label L_NYU07A_FLG02_B:
#MSGNO_RET 1
#RSET F71
#RSET F72
#RSET F73
    $F96=0
    $F73=1
    "麻寻的目光里，满是真诚与担忧。"
    jump L_NYU07A_SEL00_D
label L_NYU07A_SEL00_D:
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    menu:
        "总之先去澄空学园" if not F71:
                $F7=0
        "赶去芦鹿岛的岸边" if not F72:
                $F7=1
        "往酪萨克笔直前行" if not F73:
                $F7=2
#RSET F96
#RSET F71
#RSET F72
#RSET F73
    if F7==0:
        jump L_NYU07A_SEL00_A
    if F7==1:
        jump L_NYU07A_SEL00_B
    if F7==2:
        jump L_NYU07A_SEL00_C
label L_NYU07A_SEL00_X:
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
    scene expression "img/NIMG01C@2x.png" as bg0
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
#BG_SET_DEFC 0,NIMG01C
#EFF_STAC 0,CLOUD_C,EFF_NOSKIP
    pause (32/32.0)
    play sound "SE06_15L"
#FADE_IN 1
    "转眼之间，日头已经西斜，已经快到晚上了，天色也渐渐暗了下来。"
    "没时间了。"
    "还是没有收到结乃的任何消息。"
    "今天马上就要结束了……"
    "我焦躁不安地抓着头，可越着急就越想不出结乃还能去的地方。"
    window hide
    stop sound
    play sound "SE06_31"
    stop music fadeout 132
    pause (16/32.0)
#BG_ALPC 1
#EFF_PRI 0
#BG_SET_DEFC 1,BG21EA
    scene expression "img/BG21EA@2x.jpg" as bg1 zorder 1
#ROUTINE_STA
#EFF_STPC 0,EFF_SKIP
#BG_SWPC 0
#BG_PRIC 0
#BG_PRIC 1
#EFF_PRI 0
#ROUTINE_STP
#SE_WATC 0
    play sound "SE05_19L"
    志雄 "「嗯？」"
    "偏偏在这紧急的时刻，铃默默地将摩托车停了下来。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC05"),"True","img/SU_LCC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "她取下头盔从摩托车上跨下来，用难得认真的表情盯着我。"
    志雄 "「铃……？快点到下一……」"
    voice "NYU07A_SU021"
    铃 "「太阳马上就要落山了，今天还是放弃比较好。」"
    志雄 "「为什么，还……」"
    "还有一些时间，在我们交谈的时候，夕阳渐渐变成了橘红色，现在每分每秒都是值得珍惜的。"
    voice "NYU07A_SU022"
    铃 "「你打电话她也不接对吧，就算你们见面了，你到底想要说什么呢？」"
    志雄 "「那是……」"
    voice "NYU07A_SU023"
    铃 "「今天已经骑了很久，想兜风的心情已经满足了。」"
    "虽然觉得她说的很过分，但我也没理由多说什么。"
    "不过铃也并不是一副事不关己的样子……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC04"),"True","img/SU_LCC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU024"
    铃 "「天黑下来就不好找了。相比待在这里，不如回去吧，你不这么认为么？」"
    "她好像很担心我。"
    "正如铃所说，时间已经不允许我再寻找下去。"
    "那句『别了』，依旧回响在我的胸膛里。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC02"),"True","img/SU_LCC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU025"
    铃 "「话说回来，后来就没有再去过她家吧，说不定已经回家了。」"
    window hide
    play music  "OBGM12"
    "铃的建议，好像从很远的地方传来，进不到我的脑子里。"
    "即使找到不肯联络我的结乃，见面之后，又应该说些什么呢？"
    "思绪被打上了死结，我只能呆呆的站着。"
    "一直认为，如果能见面的话，总有办法解决的。"
    "想着只要能见面的话，事态就会得到好转。"
    "这样想……？不对。其实我什么都没有想，只是单纯地想要见到结乃而已。"
    志雄 "（我真是个笨蛋……）"
    "到底要对结乃说些什么啊？"
    "找到结乃之后，就这样开始讨论广播的企划，我就是这么打算的。"
    "为什么结乃不回短信呢？"
    "就算一直思考下去，也无法找出答案。"
    "胸口阵阵发痛，我不自觉地捂住了脸。"
    "身边的铃惊讶地看着我。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC04"),"True","img/SU_LCC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU026"
    铃 "「怎么了？」"
    志雄 "「我……到底该怎么办啊……？」"
    "面对铃的提问，我大脑一片空白，就这样最直白地回答了。"
    志雄 "「和结乃见面，要说些什么话啊？」"
    voice "NYU07A_SU027"
    铃 "「那是我想要问的事哦。」"
    "铃她并没有容许我撒娇。"
    "以前，好像有过指着我说是我的监护人这种事呢……"
    "她的表情非常认真，就像是严厉地望着自己孩子的父母一般。"
    "这些是自己该去思考的东西。"
    "铃想说的话，一定就是这个吧。"
    志雄 "「以前没遇到过这种事情，所以才不知道说什么好，这种事情也没有……！」"
    志雄 "「但是，现在，关于结乃的事情什么都不知道。」"
    voice "NYU07A_SU028"
    铃 "「……真的是这样么？」"
    志雄 "「我认为我了解她……虽然是这样。」"
    志雄 "「有着广播这个共同点，这对我们来说是非常重要的东西。」"
    志雄 "「没想到，我们对广播的看法会不同。」"
    "一直联系着我们的，理所应当的纽带，就这样消失不见。"
    "结乃应该是不想和我见面吧，所以今天才躲着我，没有回复我的短信。"
    "这个简单的理由，直到现在才想到。"
    "连这个都没发现的我，真是糟糕到了极点。"
    志雄 "「说不定，最重要的东西已经崩坏掉了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC03"),"True","img/SU_LCC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU029"
    铃 "「别胡说八道。」"
    志雄 "「铃……」"
    "我压制着胸中涌起的感情，盯着铃的脸。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "铃用平时的笑脸对我说。"
    voice "NYU07A_SU030"
    铃 "「真的是，笨蛋啊。」"
    voice "NYU07A_SU031"
    铃 "「让我来说的话，不了解她这种事，这根本就是说谎嘛。」"
    志雄 "「……诶？」"
    voice "NYU07A_SU032"
    铃 "「对两人来说最重要的事情，你们应该知道那是什么。」"
    志雄 "「……是，这样么。」"
    "铃自信满满地断言道。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "脸上浮现出无畏的笑容，用手指戳着我的额头。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU033"
    铃 "「现在想到的事，就这样说出来试试看，那就是答案。」"
    "最重要的事情。"
    "对我们两个人来说，最重要的事情。"
    "被这样提问，我把现在所想到的事情原封不动的说出口。"
    志雄 "「……广播？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB05"),"True","img/SU_LCB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU034"
    铃 "「５０分」"
    志雄 "「哇，你不是说这就是答案么。」"
    "明明按照她的要求，就这样原封不动的说出来，评分才只有５０分么！？"
    "半错半对么？但是我对于错在哪里完全不知道。"
    "我抓着头开始思考，铃对我奇怪的笑着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA01"),"True","img/SU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU035"
    铃 "「对你们两人来说，广播的哪里才是重要的呢？」"
    voice "NYU07A_SU036"
    铃 "「说到这里的话就是１００分。」"
    志雄 "「…………」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU037"
    铃 "「要以语言的形式表达出来可能有点困难呢，但是，那种感觉和印象至少能想起来吧？」"
    "重要的地方吗？……一下子还想不出来，只是，混沌的前方隐隐出现了光明。"
    voice "NYU07A_SU038"
    铃 "「你们关系肯定能恢复，重要的是，她肯定也和你一样意识到了这一点。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB03"),"True","img/SU_LCB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NYU07A_SU039"
    铃 "「我说的没错吧？」"
#REMOVE_REEK_CHR 0
    "铃自信满满的话语，让我感到安心。"
    "我使劲点了几次头，作为对铃的回应。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU040"
    铃 "「既然如此！说不了解她那就是说谎啊。」"
    "咚的一下，铃的拳头打在我的胸口上。"
    voice "NYU07A_SU041"
    铃 "「好的，就把去她家当做最终手段好了。」"
    志雄 "「诶？」"
    voice "NYU07A_SU042"
    铃 "「再给你一次机会，如你所愿带你一程好了。」"
    志雄 "「我知道了，结乃所在的地方，让我再考虑一次吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU043"
    铃 "「好，那就走吧！」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE06_14L"
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_DEFC 0,NIMG01C
#EFF_STAC 0,CLOUD_C,EFF_NOSKIP
#FADE_IN 1
    "我想让铃向澄空车站方向开，在这段时间里，我的大脑全速运转起来。"
    "当然，考虑的都是我和结乃的事情。"
    "因为ＫＡＮＡＴＡ的『Ｔ－ｗａｖｅ』而意气相投，知道对方就是自己所憧憬的投稿者之后，我们成为了最好的对手。"
    "『Ｔ－ｗａｖｅ』将我们的羁绊链接在了一起。"
    "ＫＡＮＡＴＡ把我们托付的心意，传达出去。"
    "现在的我，也想用广播把这份思念传达出去，但已经没有那么多的时间。"
    "现在，我不得不用自己的双手将结乃找出来。"
    "不然的话，那句『别了』，可能会成为我们记忆中最后的印记。"
    window hide
#BG_ALPC 1
#EFF_PRI 0
#BG_SET_DEFC 1,BG06EA
    scene expression "img/BG06EA@2x.jpg" as bg1
#ROUTINE_STA
#EFF_STPC 0,EFF_SKIP
#BG_SWPC 0
#BG_PRIC 0
#BG_PRIC 1
#EFF_PRI 0
#ROUTINE_STP
    "太阳渐渐沉入地平线，铃的摩托车。飞一般地开过染成了橙色的澄空学园。"
    stop music fadeout 132
    志雄 "「……夕阳……」"
    "望着夕阳的校舍，我灵光一闪。"
    "夕阳下的澄空学园……"
    "我大声叫了起来。"
    志雄 "「铃，停车，停车！」"
    window hide
    stop sound
    play sound "SE06_31"
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA02"),"True","img/SU_LCA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE05_13L"
    voice "NYU07A_SU044"
    铃 "「澄空吗？」"
    "铃向我确认着目的地，短暂而简洁。"
    "一个急刹车，铃转身看向我，复杂的眼神似乎充满了疑惑。"
    志雄 "「想到了一件事情，大概，没问题的。」"
    voice "NYU07A_SU045"
    铃 "「大概啊，真不可靠啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU046"
    铃 "「嗯，不过比起刚才已经算得上认真多了。」"
    "当然，没有确切的保证。"
    "但是，也没其他能够想到的地方了。"
    "所以，我已经不再迷茫，肯定就是这里。"
    志雄 "「谢谢了，铃。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_SU047"
    铃 "「我要回去了，她的事情，要好好处理哦。」"
    志雄 "「当然。」"
    "结乃就在这里。"
    "都走到这一步了，已经不用再着急了。"
    "我慢慢地迈动双腿，向那个地方走去。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_DEFC 0,BG83EA
#FADE_IN 1
    pause (32/32.0)
    window hide
    show expression "img/BG08EA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    window hide
    show expression "img/BG12EA@2x.jpg" as bg0 with dissolve
    scene expression "img/BG12EA@2x.jpg" as bg0 with dissolve
    play sound "SE09_25"
    结乃 "「…………」"
#MESEX_A M_NOA,A_CH_YU,"【結乃】「…………」%K%P"
    "路过学生会室和广播台，一路笔直的前往屋顶。"
    "就犹如我所想的，她就站在那里。"
    window hide
    stop se
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCC01"),"True","img/YU_MCC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    结乃 "「…………」"
#MESEX_A M_NOA,A_CH_YU,"【結乃】「…………」%K%P"
    "看着夕阳，浮现出和昨天离别时一样的寂寞表情。"
    "作为让结乃露出这种表情的罪魁祸首，简直无法原谅。"
    "但是比起后悔，让她恢复笑容才更是我的责任。"
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
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC01"),"True","img/YU_LCC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#SE_VOLC 1,64
    play music  "BGM13"
    志雄 "「诶，结乃。原来在这里啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB06"),"True","img/YU_LCB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_YU003"
    结乃 "「志雄学长……！？」"
    voice "NYU07A_YU004"
    结乃 "「为什么……怎么会知道这里……」"
    志雄 "「心灵的收音机」"
    志雄 "「不断地摆弄着天线打算找到信号好一点的地方，然后就收到了你发来的微弱电波。」"
    voice "NYU07A_YU005"
    结乃 "「啊……」"
    "心里的广播能好好接受到信号的样子……"
    "１年前，结乃是这么对我说的。"
    "我们的心，当然是紧紧相连的。"
    "不安这种事情，本来是完全不应该有的，虽然现在看来并非如此。"
    "可能是我们改变了，或者其实是我们之间还有许多不了解的地方。"
    "既然如此，只要将改变的地方说出来就好了，只要更加了解她就行了。"
    结乃 "「…………」"
#MESEX_A M_NOA,A_CH_YU,NYU07A_YU006,"【結乃】「…………」%K%P"
    志雄 "「关于矿石收音机的那句话，还记得么？」"
    "结乃依旧沉默，我讲起以前的事情。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC02"),"True","img/YU_LCC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_YU007"
    结乃 "「当然还记得哦。」"
    "结乃不服气地回答道。"
    "我并没觉得结乃会忘记这件事。"
    "我的矿石收音机，承载着去世母亲的思念。"
    "当然，现在它也是将我和结乃，神奈连系起来的重要的东西。"
    "不用我再重复一遍，结乃察觉到了我想说的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC03"),"True","img/YU_LCC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_YU008"
    结乃 "「学长母亲所说的话，我还记得。『广播是，能将身在远方的人的心情给传达过来的哦』。」"
    志雄 "「嗯。」"
    "对我们来说广播到底重要到了什么程度？为什么这个重要的东西，是广播？"
    "广播将我们的心联系在了一起。"
    "结果还是回到了我们开始出发的地方。"
    "是因为焦急呢，还是因为有别的理由呢，虽然之前的我对这份最初的宝物已经有点忘记了……"
    志雄 "「结乃，想要获胜的心情，我也有的。」"
    志雄 "「但是，对于我们来说，广播并不是获胜的手段对吧？」"
    志雄 "「传达出无法传达的思念，对于我们来说才是最重要的。」"
    结乃 "「…………」"
#MESEX_A M_NOA,A_CH_YU,NYU07A_YU009,"【結乃】「…………」%K%P"
    "结乃的嘴唇紧闭成一字型，直直地盯着我。"
    "她依旧没有恢复笑脸。"
    志雄 "「一起重新努力吧。说不准我们的节目会帮助到某个人，成就一段奇迹。」"
    志雄 "「啊……当然，因为要请亨和麻寻来帮忙，有可能制作者并不只是我们两个人……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC04"),"True","img/YU_LCC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_YU010"
    结乃 "「……是，这样的么。」"
    志雄 "「……不行么？」"
    "结乃强忍着泪水。"
    "我的胸口被一只无形的巨手紧紧抓住。"
    "好像哪里搞错了……"
    "不对，就算结乃不接受，这也是我真正的想法。"
    "没有说谎和掩饰，也没有虚荣和固执，没有伪装，也没有隐藏的，我的真心话。"
    "听到这些结乃还是无法接受得话……那么我已经，无能为力了。"
    voice "NYU07A_YU011"
    结乃 "「对不起，对不起。」"
    志雄 "「诶？」"
    "面对一下子低下头的结乃，我也不知道该怎么办才好，连现在的情况都无法理解。"
    voice "NYU07A_YU012"
    结乃 "「无论如何，都想要获得优胜，和志雄学长，两个人……」"
    志雄 "「啊……」"
    "被夕阳照射着的眼泪，闪耀出赤色的光辉。"
    志雄 "「……嗯，是这样呢。我的心情也是一样的。」"
    "结乃抬起满脸泪水的脸……恢复笑脸的战略算是失败了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC03"),"True","img/YU_LCC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_YU013"
    结乃 "「我，今天一直在转来转去，一直在考虑着。单靠两个人制作节目，从一开始就是不可能的……」"
    "两个人来制作……这样说的话，就又想起了昨天的那句『别了』。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA05"),"True","img/YU_LCA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_YU014"
    结乃 "「但是，果然还是想做，因为，我喜欢广播。」"
    voice "NYU07A_YU015"
    结乃 "「……就算是一个人也要去做。」"
    "结乃的眼睛认真地盯着我。"
    志雄 "「一个人……你是认真的么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA02"),"True","img/YU_LCA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "我反问道，结乃却忽然笑了起来。"
    voice "NYU07A_YU016"
    结乃 "「是认真的，如果志雄学长不来这里的话，我就真的打算一个人做下去了哦。」"
    "是因为结乃的笑容吗？我现在明白，她的确是认真的。"
    "我们相视而笑。"
    "感觉我们心中的收音机，收听到了对方的信号。"
    "感觉？"
    "不对，我们是完完全全地被名为羁绊的红线栓在了一起！"
    志雄 "「看来，安全上垒非常勉强呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB02"),"True","img/YU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_YU017"
    结乃 "「是的，非常勉强。」"
    "我期盼着的笑脸，现在就在我的眼前。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB01"),"True","img/YU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_YU018"
    结乃 "「果然，我……」"
    voice "NYU07A_YU019"
    结乃 "「想要和志雄学长一起完成广播。」"
    志雄 "「……谢谢，结乃。」"
    "我向结乃伸出右手。"
    志雄 "「再一次，请多指教。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA01"),"True","img/YU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_YU020"
    结乃 "「嗯，请多多指教。」"
    "结乃伸出右手，温柔的握住了我的手。"
    "我紧紧地攥住她的掌心。"
    "生怕一放开就会跑掉似地，紧紧地握住。"
    "然后，下意识地，我将她的身体拉倒我的身边。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB05"),"True","img/YU_LCB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    结乃 "「！」"
#MESEX_A M_NOA,A_CH_YU,NYU07A_YU021,"【結乃】「！」%K%P"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA02"),"True","img/YU_LCA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "结乃落进了我的怀里，我们之间近到能感觉到对方的呼吸。"
    "结乃害羞地把视线移开。我被她微微泛起红晕的侧脸迷住了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA01"),"True","img/YU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_YU022"
    结乃 "「夕阳，沉下去了呢。」"
    "听到结乃小声的嘟囔，我顺着她视线看去。"
    "远方，橙色的太阳慢慢落到的山的另一边。"
    "西边的天空还是亮着的，而东边已经开始转变成紫色，早出的星星已经迫不及待地眨起了眼睛。"
    voice "NYU07A_YU023"
    结乃 "「有没有想过，夏天夕阳的阳光是不是有些太强了？难得的晚霞，感觉好像一瞬间就结束了。」"
    志雄 "「是……这样么？」"
    "大概是因为季节不同而导致的错觉吧。我对结乃所说的事情并没有什么感触，可能结乃的感觉分外敏感吧。"
    "不过的确，这样说来，去年两个人在秋天看到的晚霞，应该是更加鲜艳的红色。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB02"),"True","img/YU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_YU024"
    结乃 "「哈哈，好像好久没有过和志雄学长一起看晚霞了啊。」"
    "看上去结乃也想起了记忆中的那片红色。"
    志雄 "「在忙着执行委员工作时一直都能看到吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA02"),"True","img/YU_LCA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU07A_YU025"
    结乃 "「执行委员……很怀念呢，虽然也有麻烦的时候，可志雄学长无论何时都会在我身边。」"
    "结乃看着我的脸，微微一笑。"
    "我抚摸着她的额发。"
    "这次结乃并没有将目光移开。"
    "纯黑的眸子里，映出我的面容。"
    "若不是被斜阳的余挥映照着的话，或许我们就会知道各自的脸已经红透了吧。"
    "一直牵着的右手传来阵阵热意，大概现在已经由于害羞而变红了吧。"
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    menu:
        "吻下去":
            pass
    window hide
    stop sound
#BG_SET_BACK 
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU05A")]=True
    scene expression "img/EVN_YU05A@2x.jpg" as bg1 with dissolve
    "我们的右手相互配合地变成了十指向交。"
    "我的左手轻轻搂住她的肩膀，结乃一瞬间露出了又些恍惚的神情，然后抬起了头，闭上了眼睛，好像在等待着什么。"
    "我也合上眼，脸慢慢地靠近结乃，知道嘴唇上传来柔软温湿的触感……"
    stop music fadeout 1
    "对于我们来说只有一瞬间的夏日晚霞飞快退去，就像是舞台上放下的幕布一般，将我们包围在黑暗之中。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_DEFC 0,NIMG01D
    show expression "img/NIMG01D@2x.png"
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
#FADE_IN 0
    "……"
    "…………"
    "……………………"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128
#EFF_STAC 0,CLOUD_D,EFF_NOSKIP
#FADE_IN 1
    voice "NYU07A_YU026"
    结乃 "「啊！ 」"
    志雄 "「嗯？怎么了？」"
    voice "NYU07A_YU027"
    结乃 "「时间！『Ｔ－ｗａｖｅ』已经开始了！」"
    志雄 "「哦哦？已经过了这么长时间了？」"
    voice "NYU07A_YU028"
    结乃 "「不仅仅晚霞是一瞬间的事情，之后我和学长待一起的时间也是很快地就过去了呢。」"
    志雄 "「……这种两个人的时间，真是恐怖啊。」"
    voice "NYU07A_YU029"
    结乃 "「在，在说些什么啊！快点，再不快点就要听不到了哦。」"
    志雄 "「啊——今天，忘记带携带收音机了，能借我个耳机么？」"
    voice "NYU07A_YU030"
    结乃 "「真是的，没有办法呢——」"
    志雄 "「但是听完『Ｔ－ｗａｖｅ』再回去的话，就会赶不上末班车了。」"
    voice "NYU07A_YU031"
    结乃 "「啊，的确是这样，那怎么办啊。」"
    志雄 "「要住我家么？」"
    voice "NYU07A_YU032"
    结乃 "「……什！？」"
    志雄 "「…………」"
    结乃 "「…………」"
#MESEX_A M_NOA,A_CH_YU,NYU07A_YU033,"【結乃】「…………」%K%P"
    志雄 "「什？」"
    voice "NYU07A_YU034"
    结乃 "「志雄学长……在说些什么啊……这个，那个……没关系么？」"
    "即使天色已晚，我还是能看到结乃的脸一下子红到了脖子根，看着结乃的这种反应，我也只能说出自己的口头禅了——『真没办法啊』。"
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
