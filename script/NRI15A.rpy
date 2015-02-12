label NRI15A:
    $currentlabel = "NRI15A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '30'
    $date = '0'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 6,CAL_0730
    show expression "img/NIMG15J-568h@2x.jpg" as cal zorder 5
    show expression "img/07_30_SUNDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG68AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG68AA@2x.jpg" as bg0 with dissolve
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
    "第二天，我和莉莉丝来到了位于车站与旅馆之间的土产店。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 1,((320)-48)
#CHR_POSC 2,((320)+32)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_SAA01"),"True","img/KR_SAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .6
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_SAA01"),"True","img/SF_SAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .425
    "……与老爸和香里阿姨一起。"
    "离开旅馆时偶然碰到，而且目的地都是土产店，所以就一起来了……"
    voice "NRI15A_YG000"
    雄吾 "「怎么样，这把扇子？　很适合你哟。」"
    voice "NRI15A_KR000"
    香里 "「可是，会不会太显眼啊？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SF'",DynamicDisplayable(mouthanime,"SF_SAA02"),"True","img/SF_SAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NRI15A_YG001"
    雄吾 "「用来衬托你的美貌不是正好吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KR'",DynamicDisplayable(mouthanime,"KR_SAA02"),"True","img/KR_SAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI15A_KR001"
    香里 "「真是，说什么呢，雄吾！」"
    "香里阿姨啪啪地拍着老爸的肩膀。可是，她的表情却喜出望外。"
    "什、什么啊，这对笨蛋夫妻。"
    "也许由于是自己的父母的关系，完全无法笑脸相对……"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBH06"),"True","img/RI_LBH06A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NRI15A_RI000"
    莉莉丝 "「哈……」"
    "莉莉丝也无奈地叹了口气。"
    志雄 "「不管他们，我们自己去逛吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBH04"),"True","img/RI_LBH04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI001"
    莉莉丝 "「是呢，就这么办吧。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我们悄悄地离开了沉浸在二人世界里的选购土产的夫妇。"
    志雄 "「说起土产，需要买的人是……」"
    "老爸和香里阿姨也来了所以没必要。亨和箱崎，还有学生会的各位都要买……"
    if not persistent.dictlist[46] and persistent.show_dict:
        $persistent.dictlist[46]=True
        show screen dict_pop(i=46)
    "啊，还有铃等人也算上比较好。房子一直空着，去旅行的事一定暴露了吧。"
    voice "NRI15A_RI002"
    莉莉丝 "「总之我要帮婆婆，还有智纱……」"
    "买什么好呢，最普通的就是点心了。"
    "不过，也有『名不副实』这种说法……"
    志雄 "「嗯？　莉莉丝，这是……？」"
    "我的视线停留在土产店墙壁上的招贴上。招贴上写着『泉龙神社夏日祭的通知』。"
    "会摆出摊位，海边似乎还会放烟花。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBF01"),"True","img/RI_MBF01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI003"
    莉莉丝 "「啊，夏日祭的通知呢。」"
    "莉莉丝的口吻就像是在确认已经知道的事一样。"
    志雄 "「……？　你早就知道了吗？」"
    voice "NRI15A_RI004"
    莉莉丝 "「嗯。我听婆婆说的……忘记跟志雄说了。」"
    志雄 "「原来是这样啊。」"
    志雄 "「泉龙神社就是我们之前去过的那个神社吗？」"
    voice "NRI15A_RI005"
    莉莉丝 "「多半是。」"
    志雄 "「啊，开幕日……就是今天晚上吗？真是来得早不如来得巧。」"
    "好险。要是刚才没注意到招贴的话，就会错过难得的集会了。"
    "在旅馆的房间里一如既往地被紧张感包围着的我和莉莉丝，听着窗外飘渺的夏日祭的伴奏声。这情节也不免太惆怅了呀。"
    志雄 "「那么，既然是难得的机会，那我们去看看吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBI01"),"True","img/RI_MBI01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI006"
    莉莉丝 "「嗯，我一开始就是这么打算的。」"
    voice "NRI15A_RI007"
    莉莉丝 "「但是在开始之前，我们得快点把所有人的土产都买完才行。」"
    志雄 "「噢。」"
    window hide
    stop music fadeout 132
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG61EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG61EA@2x.jpg" as bg0 with dissolve
    pause (64/32.0)
#FADE_IN 1
    play music  "BGM16"
    志雄 "「……怎么会这样？」"
    "我独自一人眺望着夕阳西下的景色。"
    "买完了全员份的土产，在房间悠闲地休息的时候，我突然被莉莉丝赶了出来。"
    "本来打算要一起去夏日祭的……现在该如何是好。"
    "我并不记得自己有做过什么惹她生气的事……"
    志雄 "「我为什么会被赶出来呢？」"
    "我小声抱怨着，不过依然想不明白为什么。"
    "我再一次没能察觉自己做了什么……"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA02"),"True","img/SN_MBA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI15A_SN000B"
    信 "「哦？　塚本君，你在这里做什么？」"
    voice "NRI15A_SN001"
    信 "「你现在就像一个在休息日妨碍扫除，被妻子从房间里赶出来的丈夫一样啊。」"
    志雄 "「真过分。我又不是稻穗。」"
    志雄 "「……嘛，不过被莉莉丝从房间里赶出来，确实是事实没错。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA01"),"True","img/SN_MBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI15A_SN002"
    信 "「怎么，夫妻之间吵架了吗？　这么快就进入倦怠期了吗？」"
    志雄 "「没、没这回事吧……大概……」"
    voice "NRI15A_SN003"
    信 "「没什么自信啊你。在自己也没察觉的时候做了什么惹莉莉丝生气的事了吗？」"
    志雄 "「我也不能排除这种可能性，正因为如此我才在这里烦恼呢……」"
    stop music fadeout 1
    voice "NRI15A_RI008"
    りりす？ "「没、没这回事啦！」"
    window hide
#ROUTINE_STA
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_GET_NOC 0,F24
#BG_SET_BACK 
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,320
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MFA04"),"True","img/RI_MFA04A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#ROUTINE_STP
#FADE_OUT 1,8,COL_WHITE
    hide lh0 with dissolve
#FADE_IN 0
    play sound "SE07_00"
#BG_ZOOM_AUTOC 0,0,20,0
#CHR_ZOOM_RATE 1,20,0
#ROUTINE_STA
#BG_ZOOM_AUTOC 0,0,10
#CHR_ZOOM_RATE 1,10
#ROUTINE_STP
    pause (24/32.0)
#FADE_OUT 1,6,COL_WHITE
    hide lh0 with dissolve
#FADE_IN 0
    play sound "SE07_00"
#BG_ZOOM_AUTOC 0,0,20,0
#CHR_ZOOM_RATE 1,20,0
#ROUTINE_STA
#BG_ZOOM_AUTOC 0,0,10
#CHR_ZOOM_RATE 1,10
#ROUTINE_STP
    pause (24/32.0)
#FADE_OUT 1,4,COL_WHITE
    hide lh0 with dissolve
#FADE_IN 0
    play sound "SE07_00"
#BG_ZOOM_AUTOC 0,0,20,0
#CHR_ZOOM_RATE 1,20,0
#ROUTINE_STA
#BG_ZOOM_AUTOC 0,0,10
#CHR_ZOOM_RATE 1,10
#ROUTINE_STP
#BG_UVC 0,0,0,640,448
    "背后传来声音，我立刻回过头去，一个似曾相识的少女站在我面前。"
    "之所以似曾相识，是因为看身材和脸蛋毫无疑问是莉莉丝，但那身衣服不由得使我心生疑惑。"
    window hide
#BG_PRI 2
#CHR_PRIC 1
#BG_COLC 0,128,128,128
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_POSC 0
    hide lh0
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MFA04"),"True","img/RI_MFA04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#BG_ALP_AUTOC 2,0,1,F24,96
#CHR_ALP_AUTOC 1,0,1,F24,96
#ROUTINE_STA
#BG_ALP_SAVEC 0
#CHR_ALP_SAVEC 0
#BG_PRI 0
#BG_PRI 2
#BG_ALPC 2
#CHR_PRIC 0
#CHR_PRIC 1
#CHR_ALPC 1
#ROUTINE_STP
    play music  "BGM02"
    voice "NRI15A_RI009"
    莉莉丝 "「稻穗！　不要用一些奇怪的言论来误导志雄！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+192)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA01"),"True","img/SN_MBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .8
    with dissolve
    voice "NRI15A_SN004"
    信 "「好了好了。你的丈夫物归原主～」"
    window hide
    hide lh1 with dissolve
    "即使被莉莉丝呵斥也毫不在乎，依然是一副随意的样子的稻穗离开了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MFD04"),"True","img/RI_MFD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI010"
    莉莉丝 "「真是的……」"
    志雄 "「莉莉丝，这浴衣是？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MFB02"),"True","img/RI_MFB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI011"
    莉莉丝 "「怎、怎么样？　合适吗？」"
    "莉莉丝有些诚惶诚恐地展开双手，布满花梗的的浴衣呈现在我面前。"
    "这幅画面即使不是奉承，也真的很漂亮。"
    志雄 "「啊啊，很合适……真的」"
    voice "NRI15A_RI012"
    莉莉丝 "「谢、谢谢……」"
    voice "NRI15A_RI013"
    莉莉丝 "「这是母亲为我准备的。在之前的芦鹿岛焰火大会的时候没来得及穿……」"
    "两人都十分害羞。路过旅馆走廊的人们似乎都在用奇异的眼光看着我们。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MFD04"),"True","img/RI_MFD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI014"
    莉莉丝 "「志雄你看智纱的浴衣时看得很入迷吧～」"
    志雄 "「没、没这回事……」"
    "对不起。稍微有点看得入迷是事实没错。"
    "可是……"
    志雄 "「我觉得莉莉丝要更加合适。嗯。非常、那个……可、可爱」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MFB02"),"True","img/RI_MFB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI015"
    莉莉丝 "「不、不要一脸严肃地说出那种话啦……」"
    voice "NRI15A_RI016"
    莉莉丝 "「嗯……不过……谢谢。」"
    志雄 "「这花梗的花，叫什么呢？　似乎在哪里见过……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MFA05"),"True","img/RI_MFA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    if not persistent.dictlist[57] and persistent.show_dict:
        $persistent.dictlist[57]=True
        show screen dict_pop(i=57)
    voice "NRI15A_RI017"
    莉莉丝 "「真是的。这种事情给我记住啦。孤挺花，孤挺花啦」"
    志雄 "「啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MFA01"),"True","img/RI_MFA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI018"
    莉莉丝 "「嗯哼。我的名字就是根据这花名取的。」"
    志雄 "「我知道了，不会再忘记了。孤挺花是吧？」"
    voice "NRI15A_RI019"
    莉莉丝 "「呵呵，那，我们出发咯。」"
    "自豪，内在美，爱说话。还有……虚荣。"
    "孤挺花。就像莉莉丝一样的花。"
    志雄 "「穿着不习惯穿的浴衣，小心不要摔倒了。」"
    voice "NRI15A_RI020"
    莉莉丝 "「到那时就靠你了。」"
    志雄 "「……真没办法呀」"
    "由于走廊比较狭窄，莉莉丝显得格外显眼。我们尽量躲避着别人的视线，离开了旅馆。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG74NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG74NA@2x.jpg" as bg0 with dissolve
    play sound "SE08_16L"
    pause (32/32.0)
    play sound "SE01_19L"
#FADE_IN 1
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MFB01"),"True","img/RI_MFB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI021"
    莉莉丝 "「人已经开始聚集了呢」"
    志雄 "「是呢。看样子上面已经有些店面摆出来了吧。」"
    志雄 "「莉莉丝，这样走路会不方便吗？」"
    "我向莉莉丝伸出手。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MFB02"),"True","img/RI_MFB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI022"
    莉莉丝 "「啊……」"
    "莉莉丝也把手伸了过来，可一瞬间，她似乎有点犹豫地停住了手……"
    window hide
#CHR_SORT 1
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XFB07"),"True","img/RI_XFB07A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 32
#MOV_CHR0 0
#MOV_CHR1 128
#MOV_FOCUS_BG 512
#MOV_CHR_GO 0
    voice "NRI15A_RI023"
    莉莉丝 "「……谢谢。」"
    "最终我们还是牵起了手。"
    "然后两人并排着爬上石阶。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG76NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG76NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,112,96
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LFD01"),"True","img/RI_LFD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE08_15L"
#FADE_IN 1
    if not persistent.dictlist[55] and persistent.show_dict:
        $persistent.dictlist[55]=True
        show screen dict_pop(i=55)
    play music  "BGM12"
    voice "NRI15A_RI024"
    莉莉丝 "「距离放烟花还有段时间，总之先逛逛看有什么店面吧？」"
    志雄 "「是呢。到哪儿去呢？」"
    "莉莉丝在境内环视了一周。一个一个看板确认下来——。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LFD01"),"True","img/RI_LFD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI025"
    莉莉丝 "「店面的数量也不多，从头到尾逛一圈怎么样？」"
    志雄 "「你想玩个痛快是吧……好的，我奉陪！」"
    voice "NRI15A_RI026"
    莉莉丝 "「好，那我们先去那边的射击店去看看吧！」"
    voice "NRI15A_RI027"
    莉莉丝 "「来，快点走呀！」"
    window hide
    play sound "SE01_19L"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    志雄 "「喂！　跑着去又会摔倒的！」"
    "我苦笑着追上十分愉快地走在前面的莉莉丝。"
    window hide
    stop se fadeout 1
#SE_VOLC 1,0
#FADE_OUT 1
    stop se
    pause (32/32.0)
#SE_VOLC 1,255
    play sound "SE03_89"
#FADE_IN 1
    voice "EV99_ET005"
    射的屋の店主 "「欢迎再来～」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,112,96
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LFA05"),"True","img/RI_LFA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI028"
    莉莉丝 "「唔～好不甘心！」"
    voice "NRI15A_RI029"
    莉莉丝 "「那是犯规的！　是枪不好！　每射击一次准心就会偏离一点！」"
    志雄 "「呵，要把弹道微妙的偏差也考虑进去瞄准射击才行呢」"
    "我一边把刚才从射击店里拿到的玩偶给莉莉丝看，一边骄傲地说道。"
    voice "NRI15A_RI030"
    莉莉丝 "「唔唔唔……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LFD02"),"True","img/RI_LFD02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI031"
    莉莉丝 "「论、论实力的话是我更胜一筹！」"
    voice "NRI15A_RI032"
    莉莉丝 "「下面我们用套圈来决一胜负吧！」"
    志雄 "「哦哦，这次我也不会输的。」"
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
    play sound "SE03_81"
#FADE_IN 1
    voice "EV99_ET006"
    輪投げ屋の店主 "「真可惜呢～下次再来～」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,112,96
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LFA05"),"True","img/RI_LFA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI033"
    莉莉丝 "「又、又失败了……」"
    voice "NRI15A_RI034"
    莉莉丝 "「是那个环不好啦！」"
    志雄 "「那个，套圈和道具没什么关系吧……」"
    voice "NRI15A_RI035"
    莉莉丝 "「我扔的那个环一定小一号。嗯，一定是这样的！」"
    voice "NRI15A_RI036"
    莉莉丝 "「说不定那个环故意做得有些扭曲，不能笔直飞行呢……连空气阻力也计算在内了，真是高招呢。」"
    "指着手拿玩偶赠品的我，莉莉丝尽说着一些埋怨的话。"
    志雄 "「谁会这么做啊！」"
    "真是的，莉莉丝也真会闹别扭。不过，她的这种个性我倒也并不讨厌。"
    "我不禁露出了微笑。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LFD04"),"True","img/RI_LFD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI037"
    莉莉丝 "「什、什么呀，有什么好笑的？」"
    志雄 "「不，没什么。对了，给。」"
    "我把套圈和射击获得的玩偶递给莉莉丝。"
    志雄 "「我拿着也没用，给你了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LFA03"),"True","img/RI_LFA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI038"
    莉莉丝 "「啊……」"
    voice "NRI15A_RI039"
    莉莉丝 "「我、我对玩偶一点也……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LFA02"),"True","img/RI_LFA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI040"
    莉莉丝 "「不过……难得你这么好心，我就收下了。」"
    voice "NRI15A_RI041"
    莉莉丝 "「不接受别人的好意也不太好，要是扔了的话，这玩偶也挺可怜的。」"
    "脸侧向一边，莉莉丝收下了玩偶。"
    志雄 "「嗯，感谢你能收下。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LFD01"),"True","img/RI_LFD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "收下玩偶后，莉莉丝紧紧地抱住它们。"
    voice "NRI15A_RI042"
    莉莉丝 "「不客气～」"
    "然后，高兴地笑了起来。"
    "真是的，一开始能这么坦率地说，那不就好了。"
    志雄 "「肚子开始有点饿了……」"
    "我像是为了掩饰害羞一样，改变了话题。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LFB01"),"True","img/RI_LFB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI043"
    莉莉丝 "「是呢，那我们去吃点东西吧？」"
    志雄 "「嗯，刚才那边有炒面。」"
    voice "NRI15A_RI044"
    莉莉丝 "「啊，海鲜炒面是吗。我也看到了～♪」"
    window hide
    play sound "SE01_18L"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "莉莉丝马上朝炒面店走去。"
    "那享受着现在时光的表情毫不做作。"
    "这次旅行自从来到这里，我和莉莉丝就不由自主地相互在意着对方。"
    "能像这样和往常一样笑着度过，使我感到很高兴。"
    window hide
    stop se fadeout 1
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG75NA@2x.jpg" as bg0 zorder 100 with dissolve
#EFF_STAC 0,NEONLIGHT,EFF_SKIP
#FADE_IN 1
    "我和莉莉丝仰望着夜空中绚烂的烟花。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LFA01"),"True","img/RI_LFA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI045"
    莉莉丝 "「芦鹿岛虽然很漂亮，不过这里也不错呢！」"
    window hide
    stop se fadeout 1
#EFF_STPC 0,EFF_NOSKIP
#BG_SET_BACK 
#BG_INIC 0
#BG_PRI 1
    show expression "img/NIMG07A@2x.jpg" as bg1 zorder 100 with dissolve
    "……"
    window hide
#FADE_OUT 1
    hide bg1 with dissolve
#BG_PRI 1
#EFF_STPC 0,EFF_SKIP
    play sound "SE08_04L"
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG75NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG75NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LFA01"),"True","img/RI_LFA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
#FADE_IN 1
    "伴随着最后一轮火花的残像，夜空回归了平静。"
    voice "NRI15A_RI046"
    莉莉丝 "「……刚才那一响似乎是最后了。」"
    志雄 "「是啊。」"
#SE_VOLC 1,64
    "环顾周围，其他的观光客也差不多准备走了。"
    "一般在这种集会之后的气氛总有一些寂寞。不过——"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LFD01"),"True","img/RI_LFD01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI047"
    莉莉丝 "「那么，我们也差不多该回去了吧？」"
    play music  "BGM16"
    "莉莉丝依然带着笑脸。"
    志雄 "「啊啊，是啊。」"
    "所以即使集会结束了也不觉得寂寞。"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LFB01"),"True","img/RI_LFB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI048"
    莉莉丝 "「怎么了？　发生了什么好事情吗？」"
    志雄 "「诶？　为什么这么问？」"
    voice "NRI15A_RI049"
    莉莉丝 "「总觉得志雄很高兴的样子。」"
    "……不知不觉表现在脸上了吗。"
    志雄 "「嗯。自从来这里旅行之后，就有点……」"
    "无论是在特快列车中，还是在旅馆的房间里。也许只是因为我太在意身边的莉莉丝而已。"
    志雄 "「不过，现在看到莉莉丝高兴的样子。我总觉得自己也很高兴。」"
    志雄 "「……嘿，我自己也不知自己在说些什么了。」"
    "不能很好地组织语言使我有些急躁。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LFB02"),"True","img/RI_LFB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI050"
    莉莉丝 "「……嗯，没关系」"
    voice "NRI15A_RI051"
    莉莉丝 "「志雄想说的……我明白」"
    "莉莉丝红着脸说道。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LFD01"),"True","img/RI_LFD01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI052"
    莉莉丝 "「那、那么，总之！　我们回旅馆吧」"
    "掩饰着羞涩的莉莉丝显得十分可爱。"
    志雄 "「啊啊，是啊」"
    window hide
    show expression "img/BG74NA@2x.jpg" as bg_over zorder 2 with dissolve
    stop sound
    play sound "SE01_19L"
    "融入从神社境内离去的人流里，我们走下台阶。"
    stop se
    stop music fadeout 132
#SE_VOLC 1,255
    voice "NRI15A_RI053"
    莉莉丝 "「哇！」"
    志雄 "「莉莉丝！？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_PRIC ID_ALL
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XFB03"),"True","img/RI_XFB03A@2x.png") as lh10 zorder (10+11):
        ypos 0.0
    with dissolve
#BG_GET_NOC 0,F24
#BG_SET_BACK 
#BG_INIC 2
#BG_PRI 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    play sound "SE07_14"
#CHR_ALP_AUTOC 1,128,0,F24
#BG_ALP_AUTOC 2,128,0,F24
#QUA_BG 2
#QUA_BG 2
#CHR_ALP_SAVEC 1
#BG_ALP_SAVEC 2
#QUA_ALL
#CHR_POSC 1
#BG_POSC 0,0
#BG_POSC 2,0
    "踩空最后一格台阶，莉莉丝的身体失去了平衡。我急忙伸出手，抓住了她的手腕。"
    志雄 "「没事吧？」"
    voice "NRI15A_RI054"
    莉莉丝 "「没、没关系……」"
    window hide
#CHR_SORT 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MFB06"),"True","img/RI_MFB06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 32
#MOV_CHR0 128
#MOV_CHR1 0
#MOV_FOCUS_BG 0
#MOV_CHR_GO 0
    hide lh1 with dissolve
    voice "NRI15A_RI055"
    莉莉丝 "「好疼……」"
    "看着自己的脚，莉莉丝皱起了眉头。"
    志雄 "「怎么了？」"
    voice "NRI15A_RI056"
    莉莉丝 "「脚大概稍微扭了一下……」"
    志雄 "「能走吗？」"
    voice "NRI15A_RI057"
    莉莉丝 "「没事的，没事。才这种程度而已。」"
    window hide
    play sound "SE01_18L"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_PRIC ID_ALL
    "像是为了证明自己没事，莉莉丝放开我的手，自己向前走去。可是，马上她就痛苦地停了下来。"
    window hide
    stop se
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SFA06"),"True","img/RI_SFA06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI15A_RI058"
    莉莉丝 "「好疼……」"
    志雄 "「不要逞强啦。」"
    "就这样让莉莉丝走，看来是不行了。即使让她搭着我肩膀，她还是得用到脚。"
    "想要让脚的负担最小的话……只有这样了。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我背向莉莉丝，蹲了下来。"
    志雄 "「来，我来背你。」"
    voice "NRI15A_RI059"
    莉莉丝 "「什、不、不用背啦……」"
    "从我身后传来莉莉丝困惑的声音。"
    志雄 "「好了啦，不要逞强了。而且，要我一直维持着这种姿势我也会不好意思的，快点儿」"
    voice "NRI15A_RI060"
    莉莉丝 "「知、知道了啦。」"
    "莉莉丝有些不高兴地说着，把她的体重依托在我背上。"
    voice "NRI15A_RI061"
    莉莉丝 "「嗯……」"
#MESEX_A M_NOA,A_CH_RI,NRI15A_RI061,"【りりす】「嗯……」%K%P"
    "背后感受到莉莉丝的温暖。微弱的气息传到我的颈部，这进一步加剧了我害羞的心情。"
    voice "NRI15A_RI062"
    莉莉丝 "「……谢谢……」"
    志雄 "「不客气～」"
    "我腰部一使劲，站了起来。"
    window hide
#BG_FLG EVN_RI09A
#BG_SET_BACK 
#BG_INIC 1
#BG_INIC 2
#BG_PRI 1
#BG_PRI 2
#BG_ALPC 1
#BG_ALPC 2
#BG_POSC 1,0,-150
#BG_POSC 2,0
#BG_SETWC 1,2,EVN_RI09A,EVN_RI09A
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI09A")]=True
    show expression "img/EVN_RI09A@2x.jpg" as bg2 zorder 2:
        yalign 1.0
        linear 1 yalign 0.0
    with dissolve
    play music  "BGM13"
#BG_UVC 1,((640/16)*3),150*1.6,640/1.6,448/1.6
#BG_POS_SAVEC 1
    stop sound fadeout 1
    play sound "SE05_16L"
##BG_SHOWC 4
##BG_SHOWC 4
#ROUTINE_STA
#BG_ALP_AUTOC 1,128,0,F123,80
#BG_UV_AUTOC 1,((640/16)*3),0,640/1.6,448/1.6,1,F123,440
#ROUTINE_STP
    pause (80/32.0)
    志雄 "「嘿咻……」"
#BG_ALP_AUTOC 2,128,0,F123
#BG_ALP_AUTOC 1,0,0,F123
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESA A_CH_SI,"【志雄】「嘿咻……」"
    hide bg1 with dissolve
#MESX "%K%P"
    志雄 "「那我们走吧。」"
    voice "NRI15A_RI063"
    莉莉丝 "「嗯。」"
    play sound "SE01_04L"
    "感受着背后重要的人的存在，我向前走着。"
    voice "NRI15A_RI064"
    莉莉丝 "「像这样被背着，视线比平时要高，感觉很奇怪。」"
    "现在被背着的莉莉丝的视线和我一样高。我的身高绝对算不上高，只不过莉莉丝的身材比较娇小罢了。"
    voice "NRI15A_RI065"
    莉莉丝 "「是吗，这样的高度就是志雄的高度吗？」"
    "背后传来的声音总觉得充满着愉悦。"
    志雄 "「有这么大差别吗？　对我自己来说，这种高度是理所当然的，所以不太明白。」"
    voice "NRI15A_RI066"
    莉莉丝 "「哎嘿嘿……」"
    voice "NRI15A_RI067"
    莉莉丝 "「你果然是个笨蛋。」"
    志雄 "「唔，干吗啦，突然把别人当成笨蛋？」"
    voice "NRI15A_RI068"
    莉莉丝 "「因为你是笨蛋所以才叫你笨蛋呢。笨蛋～」"
    志雄 "「说别人笨蛋的人才是笨蛋。」"
    "……我们怎么像孩子一样。"
    "就这样吵着吵着，莉莉丝也笑了起来。"
    "我不再说多余的话，只是朝着旅馆走去。"
    voice "NRI15A_RI069"
    莉莉丝 "「不过志雄也变得有些强壮了呢。」"
    "莉莉丝把头靠在我的背上嘟哝着。"
    志雄 "「『有些』这个词是多余的。」"
    "确实我不属于体力很充沛的类型。"
    "尽管如此。"
    "背着莉莉丝走路，还是做得到的。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop se
    stop sound
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_PAN_EVN_RI09A
#BG_ALP_AUTOC 1,128,0,F123,80
#BG_POS_AUTOC 1,,F123,80
#BG_ALP_SAVEC 1
#BG_POS_SAVEC 1
#EOT