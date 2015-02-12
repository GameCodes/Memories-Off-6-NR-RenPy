label NRI16A:
    $currentlabel = "NRI16A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    play music  "BGM13"
#label START
    $month = '07'
    $day = '30'
    $date = '0'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG60NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG60NA@2x.jpg" as bg0 with dissolve
    play sound "SE05_17L"
    pause (32/32.0)
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
    "背着莉莉丝的我走进了旅馆。"
    voice "NRI16A_RI000"
    莉莉丝 "「到这里就行了。」"
    "背后传来稍稍有些焦急的声音。"
    志雄 "「嗯，是吗？　要不要把你背到房间里……」"
    voice "NRI16A_RI001"
    莉莉丝 "「没，没关系的啦！　而且，在这里被别人看到的话……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA02"),"True","img/SN_MBA02A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NRI16A_SN000"
    信 "「哦哦，欢迎回来，塚本君。」"
    "就像是掐准了时机一样，稻穗从旅馆里走了出来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA01"),"True","img/SN_MBA01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NRI16A_SN001C"
    信 "「集会结束了吗……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBB04"),"True","img/SN_MBB04A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NRI16A_SN001D"
    extend "哎，莉莉丝怎么了？」"
    志雄 "「回来时脚受了点伤。」"
    voice "NRI16A_SN002"
    信 "「没事吧？」"
    voice "NRI16A_RI002"
    莉莉丝 "「哎哎，没事。志雄，把我放下来啦。」"
    志雄 "「啊啊，好。」"
    "我有些失望地放下莉莉丝。背后的重量和温度消失了……使我感到有些不舍。"
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
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA04"),"True","img/SN_MBA04A@2x.png") as lh10 zorder (10+10):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MFD01"),"True","img/RI_MFD01A@2x.png") as lh11 zorder (10+1):
        xcenter .75
    with dissolve
    voice "NRI16A_RI003"
    莉莉丝 "「看，能动吧，完全没事。志雄太过担心了。」"
    "现在的莉莉丝确实没有表现出特别疼痛的样子，看起来似乎没什么事……"
    voice "NRI16A_SN003"
    信 "「是扭伤吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_MBA02"),"True","img/SN_MBA02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NRI16A_SN004"
    信 "「对了，那么去露天温泉洗个澡怎么样？」"
    志雄 "「露天温泉？」"
    voice "NRI16A_SN005"
    信 "「啊啊。从这个方向往里面稍微走一段路。有点隐秘温泉的感觉，本地人经常使用的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MFA01"),"True","img/RI_MFA01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NRI16A_RI004"
    莉莉丝 "「温泉吗……」"
    "莉莉丝似乎颇有兴趣地看着稻穗。"
    voice "NRI16A_SN006"
    信 "「一边看着夜空一边洗澡，也别有一番风味吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MFD01"),"True","img/RI_MFD01A@2x.png") as lh11 zorder (10+11):
        ypos 0.0
    with dissolve
    voice "NRI16A_RI005"
    莉莉丝 "「是呢……难得的机会，现在就去吧？」"
    志雄 "「嘛，我是没关系，可你没事吗？　真的能走吗？」"
    voice "NRI16A_RI006"
    莉莉丝 "「嗯。要是实在不行的话……你再背我好了。」"
    "反正之后也要洗澡，那么不如去与昨天不同的露天温泉洗吧。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG63NA1@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG63NA1@2x.jpg" as bg0 with dissolve
    play sound "SE05_16L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,64
    play music  "BGM12"
    "我们从稻穗口中知晓了去露天温泉的道路。似乎是朝着和去湖边不同的道路上稍微走一阵子的地方。"
    "总之先回房间准备一下再出发吧。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBC04"),"True","img/RI_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI16A_RI007"
    莉莉丝 "「露天温泉吗……」"
    "莉莉丝陷入沉思般低语道。"
    志雄 "「怎么了？　果然疼到不能走路了吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD01"),"True","img/RI_LBD01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI16A_RI008"
    莉莉丝 "「不是，脚是没事……」"
    志雄 "「啊啊，对了，和香里阿姨她们也说一声吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA06"),"True","img/RI_LBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI16A_RI009"
    莉莉丝 "「啊，刚才看到她们好像又喝醉了。」"
    志雄 "「真拿他们没办法呢……那两个人。」"
    志雄 "「不过，那还有什么顾虑吗？」"
    stop music fadeout 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBA02"),"True","img/RI_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI16A_RI010"
    莉莉丝 "「嗯……只不过，那个……要是混浴的话该怎么办呢……」"
#MUS_VOL 64
    志雄 "「诶？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_LBD02"),"True","img/RI_LBD02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI16A_RI011"
    莉莉丝 "「不，没什么！」"
    window hide
#MUS_VOL 128
    play sound "SE03_63"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play music  "BGM12"
    "莉莉丝侧过头去，把浴巾扔向我。"
    志雄 "「呃，干什么呢！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MBD04"),"True","img/RI_MBD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI16A_RI012"
    莉莉丝 "「快准备啦！」"
    志雄 "「好好，我知道啦。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "在生什么气啊……不过，这样才像莉莉丝。"
    "我露出似笑非笑的表情，迅速准备起洗澡用具。"
#label QJUMP
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
#BG_INIC 1
    show expression "img/NIMG01D2@2x.png" as bg1 zorder 1 with dissolve
    play sound "SE05_17L"
    pause (32/32.0)
#FADE_IN 1
    "于是，我们来到了露天温泉——"
    志雄 "「『请自由使用』……还真是随便呢。」"
    voice "NRI16A_RI013"
    莉莉丝 "「也没有收钱的地方吧？　那就这样吧。」"
    voice "NRI16A_RI014"
    莉莉丝 "「好像没有其他客人，真幸运呀～♪唱首歌吧～」"
    志雄 "「之后可能会有人来吧……那么，待会见了。想出来时喊一声，这种狭小的空间里能听见的。」"
    voice "NRI16A_RI015"
    莉莉丝 "「嗯，好的。」"
    "之后在男女分开的更衣处我赶紧脱掉衣服，披上毛巾朝温泉走去。"
    window hide
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG99AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG99AA@2x.jpg" as bg0 with dissolve
#EFF_STAC 0,YUGE,EFF_SKIP
    hide bg1 with dissolve
    play music  "BGM11"
    志雄 "「啊……真累啊……」"
    "旅馆的浴室虽然很舒服，不过露天温泉也别有一番风味。"
    "在室外的开放感，山野的气息。"
    "放眼望去繁星点点，真是超级奢侈的空间。"
    "水温也刚刚好，整个身体被这种平稳的感觉治愈了。"
    "这样的话，对莉莉丝疼痛的脚也一定会有好处吧。"
    "回去以后得感谢稻穗呢。"
    voice "NRI16A_RI015A"
    莉莉丝 "「在那里吗，志雄？」"
    "不久，水汽的另一边传来了莉莉丝的声音。"
    "由于蒸汽的关系，只能看到前方数米的距离，果然和女性浴池合在一起的话就显得不那么宽敞了。"
    志雄 "「啊啊，这里只有我一个。你那边呢？」"
    voice "NRI16A_RI015B"
    莉莉丝 "「哎？　嗯，嗯……看来只有我们……两个人而已。」"
    志雄 "「果然是这样吗，太好了，这样就能慢慢享受了。」"
    play sound "SE03_82"
    voice "NRI16A_RI015C"
    莉莉丝 "「嗯，不过……」"
    "是错觉吗，莉莉丝的声音似乎越来越近了。"
    "男女浴池虽说是分开的，仔细想想，莉莉丝的浴池就在我身旁……"
    "总、总觉得有些紧张起来了。"
    window hide
    play sound "SE00_49"
    play sound "SE03_78"
    "……？"
    "似乎有别的客人来了。"
    "这样会不好意思，所以就不游泳了吧。"
    stop music fadeout 132
    voice "NRI16A_RI015D"
    りりす？ "「……打扰了。」"
    志雄 "「哎……！？」"
    "不禁回过头去的我怀疑自己的眼睛。"
    play music  "BGM14"
    志雄 "「为，为什么！？　我搞错浴池了吗！？」"
    voice "NRI16A_RI016"
    莉莉丝 "「不，不是的……这里……中间好像是连在一起的……」"
    志雄 "「哎哎！？　那，那不就是混浴吗！？」"
    voice "NRI16A_RI017"
    莉莉丝 "「好像是的……话说，你不要一直盯着这里看啦！」"
    志雄 "「对，对不起！　没、没关系的，有蒸汽在看不清的！　我没看哟！」"
    voice "NRI16A_RI018"
    莉莉丝 "「没关系啦，我至少还围着毛巾呢。」"
    voice "NRI16A_RI019"
    莉莉丝 "「啊，大概是考虑到这种情况，才允许使用浴盆的」"
    志雄 "「不、不是这问题吧……」"
    voice "NRI16A_RI020"
    莉莉丝 "「咦？　难道志雄脸红了吗？」"
    志雄 "「谁，谁脸红啦！　这是因为温泉太热的关系……！」"
    志雄 "「啊，我差不多要上去了」"
    voice "NRI16A_RI021"
    莉莉丝 "「诶？　难得的机会，再多享受一下嘛。」"
    志雄 "「嗯……嗯……」"
    window hide
    stop se fadeout 1
#BG_SET_BACK 
#BG_INIC 3
#BG_PRI 3
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI10A")]=True
    scene expression "img/EVN_RI10A@2x.jpg" as bg3 with dissolve
#BG_FLG EVN_RI10A0
    hide bg0 with dissolve
    voice "NRI16A_RI022"
    莉莉丝 "「哈……真的好暖和……」"
    "背后传来莉莉丝吐出的气息。"
    "因为她的关系，我慢慢享受温泉乐趣的感觉完全消失了。"
    voice "NRI16A_RI023"
    莉莉丝 "「对了志雄，我帮你擦背吧？」"
    志雄 "「诶？　不，不用了。」"
    voice "NRI16A_RI024"
    莉莉丝 "「就当作是你背我的谢礼吧」"
    voice "NRI16A_RI025"
    莉莉丝 "「你不用这么客气啦。以前不是经常帮你擦背的吗？」"
    志雄 "「这、这么久远的事情谁记得啊！」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI10B")]=True
    show expression "img/EVN_RI10B@2x.jpg" as bg3 with dissolve
#BG_FLG EVN_RI10B0
    voice "NRI16A_RI026"
    莉莉丝 "「啊哈哈哈，其实我也不记得了」"
    志雄 "「什么嘛……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI10A")]=True
    show expression "img/EVN_RI10A@2x.jpg" as bg3 with dissolve
    voice "NRI16A_RI027"
    莉莉丝 "「可是……总觉得很不可思议呢。」"
    志雄 "「……？」"
    voice "NRI16A_RI028"
    莉莉丝 "「能来到这么棒的浴池……志雄就在我身边……」"
    志雄 "「啊啊，对了……」"
    志雄 "「没想到会是混浴，回去一定会被稻穗取笑的。」"
    voice "NRI16A_RI029"
    莉莉丝 "「那么，还是那句口头禅吧？」"
    voice "NRI16A_RI030"
    莉莉丝・志雄 "「真没办法啊。」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI10C")]=True
    show expression "img/EVN_RI10C@2x.jpg" as bg3 with dissolve
#BG_FLG EVN_RI10C0
    voice "NRI16A_RI031"
    莉莉丝 "「啊哈哈哈」"
    play sound "SE03_64"
    志雄 "「真是的，来到这里之后，我们似乎一直在做蠢事呢。」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI10B")]=True
    show expression "img/EVN_RI10B@2x.jpg" as bg3 with dissolve
    voice "NRI16A_RI032"
    莉莉丝 "「不是很好吗，这就是我和志雄交往的方式啊。」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI10D")]=True
    show expression "img/EVN_RI10D@2x.jpg" as bg3 with dissolve
#BG_FLG EVN_RI10D0
    voice "NRI16A_RI033"
    莉莉丝 "「……不喜欢？」"
    志雄 "「没这回事，我……」"
    志雄 "「……我和莉莉丝在一起，很快乐。」"
    window hide
    show expression "img/EVN_RI10A@2x.jpg" as bg3 with dissolve
    voice "NRI16A_RI034"
    莉莉丝 "「嗯。我也是，能来旅行真是太好了。」"
    志雄 "「啊啊。不过下次一定要和富美子婆婆一起来。」"
    voice "NRI16A_RI035"
    莉莉丝 "「是啊。真的很感谢婆婆呢。」"
    志雄 "「然后，我们两个人再到别的地方去旅行吧。嘛，虽然要等很多事都告一段落才行。」"
    window hide
    show expression "img/EVN_RI10B@2x.jpg" as bg3 with dissolve
    voice "NRI16A_RI036"
    莉莉丝 "「嗯！　一定哦，我们说好了～♪」"
    志雄 "「噢噢。为此我们一定要努力才行……」"
    window hide
    show expression "img/EVN_RI10D@2x.jpg" as bg3 with dissolve
    voice "NRI16A_RI037"
    莉莉丝 "「呜……」"
    "莉莉丝的声音一瞬间沉闷了。"
    voice "NRI16A_RI038"
    莉莉丝 "「不、不过这不是很好吗！　考试是考试！　现在是现在！」"
    voice "NRI16A_RI039"
    莉莉丝 "「这种时候不要说一些不解风情的话嘛。旅行时不准想学习的事情！」"
    voice "NRI16A_RI040"
    莉莉丝 "「真是的，你就是在这种奇怪的地方不知变通。」"
    window hide
    show expression "img/EVN_RI10B@2x.jpg" as bg3 with dissolve
    voice "NRI16A_RI041"
    莉莉丝 "「……不过，这才像志雄。」"
    志雄 "「算我错了好吧……那现在就做现在想做的事吧……」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_PRI 1
#EFF_STAC 0,SKYNABE,EFF_SKIP
    show expression "img/NIMG01D2@2x.png" as bg1 with dissolve
    play sound "SE03_78"
    hide bg3 with dissolve
    "我回过头去，吻上了满脸讶异的莉莉丝的脸颊。"
    "她的脸红到了耳根……大概，是因为温泉的关系吧。"
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