label NSU11A:
    $currentlabel = "NSU11A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '28'
    $date = '5'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/EXBG04N@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGB02"),"True","img/SU_ZGB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_IN 1
    play music "BGM12"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    voice "NSU11A_SU000"
    铃 "「太～好了，早就想试着吃一次这样的美食了」"
    志雄 "「真、真豪华啊……」"
    "房间的餐桌上，拥挤地摆放着使用各种山珍海味制成的料理，正中央更是丰盛的生鱼片拼盘。"
    "虽然旅馆里也有餐厅，不过可以要求送到房间里来。"
    "顺便说一下……这一切都由稻穗请客。"
    志雄 "「稻穗也真可怜啊……」"
    "复活过来的稻穗作出让步，看来是以豪华的晚餐作为交换才得以解放。"
    "因为铃告诉我暂时不要回到房间里，所以自己一直在前厅休息，他们两人说了些什么全然不知。"
    "不过，稻穗的打工费相当一部分要因此泡汤了吧……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGA01"),"True","img/SU_ZGA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU001"
    铃 "「没关系没关系，他这是自作自受」"
    志雄 "「但也不至于到这地步……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGA05"),"True","img/SU_ZGA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU003"
    铃 "「明明自己的人生就很乏味，还摆出一副多伟大的样子对别人说教……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGB03"),"True","img/SU_ZGB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NSU11A_SU004"
    铃 "「……唔～抱歉抱歉，不说这些了！」"
#REMOVE_REEK_CHR 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGB02"),"True","img/SU_ZGB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "铃使劲摇摇头，为了转换心情露出了笑容。"
    志雄 "「也、也是呢」"
    voice "NSU11A_SU005"
    铃 "「好了，志雄快吃吧！」"
    志雄 "「嗯，难得享受这待遇，我们就趁热吃吧。来，请给我杯子」"
    play sound "SE03_95"
    "我迅速向铃的杯子里倒满了啤酒。"
    "如果再跟稻穗闹出不愉快的事态会很麻烦，还是让她赶快喝酒转移话题吧。"
    stop se
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGB01"),"True","img/SU_ZGB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU006A"
    铃 "「哦，谢谢了。{w=3}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGB02"),"True","img/SU_ZGB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU006B"
    extend "那么，干～杯」"
    志雄 "「干杯！」"
    window hide
    play sound "SE03_36"
    voice "NSU11A_SU007"
    铃 "「呜咕呜咕……哈。骑着摩托四处跑后泡了温泉，然后再来上一杯啤酒，真是舒畅啊！」"
    play sound "SE03_20"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGB01"),"True","img/SU_ZGB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU008"
    铃 "「最近驾车旅行必须当天返回，不能喝酒啊～」"
    志雄 "「酒后当然不能驾车」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGB02"),"True","img/SU_ZGB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU009"
    铃 "「说的没错！」"
    "喝酒时的铃真的很兴奋，我平常就如此觉得，而眼前的景象更加深了这一认识。"
    play sound "SE03_95"
    "我向转眼间就空空如也的杯子里再次注满啤酒。"
    voice "NSU11A_SU010"
    铃 "「呜～，喝酒的畅快心情不能让志雄也体会到，真可惜啊」"
    "未成年的我喝着乌龙茶。"
    stop se
    "不过，看到铃这么开心的样子，我也自然地觉得很开心。"
    志雄 "「能吃到这么美味的料理我已经很满足了」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGA06"),"True","img/SU_ZGA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU011A"
    铃 "「呜哇～你无法理解啊！{w=3}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGA01"),"True","img/SU_ZGA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU011B"
    extend "不过，也只能这样了」"
    "哇，杯子立刻又见底了！？喝的太快了吧！"
    voice "NSU11A_SU012"
    铃 "「嗯，确实相当不错呢，那家伙做饭是有一手」"
    志雄 "「哎？这些是稻穗做的！？」"
    voice "NSU11A_SU013"
    铃 "「不全是，但似乎帮了不少忙」"
    if not persistent.dictlist[35] and persistent.show_dict:
        $persistent.dictlist[35]=True
        show screen dict_pop(i=35)
    志雄 "「是吗……话说回来，他既然是酪萨克的名人，应该很有厨师的才能吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGA02"),"True","img/SU_ZGA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU014"
    铃 "「厨师？水平哪有那么高啊。不管是哪种地方，在餐馆工作的话总归饿不死，反正大概就是这种理由吧」"
    志雄 "「是、是这样么？」"
    voice "NSU11A_SU015A"
    铃 "「嗯。话说回来，{w=3}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGA06"),"True","img/SU_ZGA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU015B"
    extend "禁止在我的耳边说那家伙的好话！」"
    志雄 "「对、对不起……」"
    "这一对话的过程中，杯子再次变得空空如也。"
    "这人这么快就把一杯都喝完了……"
    志雄 "「铃喝的速度也太快了吧？没关系吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGB02"),"True","img/SU_ZGB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU016"
    铃 "「没事没事，就这么点完全不够！」"
    play sound "SE03_74"
    志雄 "「好吧好吧」"
    "这种说话方式，似乎已经喝醉了。"
    stop se
    "我决定让铃保存一点体力，于是这次倒的少了些。"
    "醉到这个程度，已经不清楚自己到底喝了多少吧。"
    "以前老爸喝多的时候，也经常这个样子。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGC02"),"True","img/SU_ZGC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU017"
    铃 "「喂……志雄？」"
    志雄 "「？」"
    voice "NSU11A_SU018"
    铃 "「突然带你出来旅行，开心吗？」"
    志雄 "「嗯？当然很开心啊」"
    voice "NSU11A_SU019"
    铃 "「真的？」"
    志雄 "「真的」"
    "这是怎么了，好像一下失去自信似的。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGC06"),"True","img/SU_ZGC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU020"
    铃 "「嗯……啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGC01"),"True","img/SU_ZGC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU021"
    铃 "「志雄，到这边来一下」"
    "铃嘀咕了一会儿，随即不停地向我招手。有什么事呢……？"
    志雄 "「好吧好吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGC05"),"True","img/SU_ZGC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU022"
    铃 "「回答一次就够了！」"
    "我放下筷子，坐到铃的身边。"
    window hide
#FADE_OUT 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGC05"),"True","img/SU_ZGC05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (32/32.0)
#FADE_IN 1
    voice "NSU11A_SU023"
    铃 "「真的、很开心？」"
    "铃是怎么了？难以想像的唠叨……"
    "大概真的是喝多了吧。"
    志雄 "「真的啊，你这是怎么了？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGC04"),"True","img/SU_ZGC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU024"
    铃 "「没什么，只是，总觉得好像是我把你绑架出来的一样」"
    "到现在才在意起这些……"
    "基本上，如果不是自己喜欢就不会来的。"
    voice "NSU11A_SU025"
    铃 "「而且不是普通的旅行，而是驾车远游，只是因为我的兴趣。你真的不讨厌吗？不累吗？没觉得麻烦吗？没想过这些吗？」"
    志雄 "「真的没想过这些。虽然一开始的确吃了一惊……」"
    voice "NSU11A_SU026"
    铃 "「虽然？」"
    "铃毫无疑问已经醉了。所以就算现在自己老老实实说出心里话，过后她也说不定就会忘记了吧……"
    志雄 "「我和铃两人在一起很开心，尽管不习惯摩托造成很多麻烦，但去过这么多地方，从中享受到了诸多的乐趣」"
    志雄 "「虽然还是第一天，但我能参加这次旅行，真是太好了，所以……非常感谢」"
    "这一瞬间，铃甜甜地，就像是无法控制般地笑了笑。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGB03"),"True","img/SU_ZGB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NSU11A_SU027"
    铃 "「哎……嗯。你能这么说……我很高兴，嗯」"
    志雄 "「……」"
    stop music fadeout 1
    voice "NSU11A_SU028"
    铃 "「嗯？志雄，怎么了？」"
#REMOVE_REEK_CHR 0
    "铃的眼睛微微仰视，流露出湿润而娇媚的感觉。"
    "就在我触手可及的距离，她用这样的眼神看着我……"
    志雄 "「唔，没什么……」"
    voice "NSU11A_SU029"
    铃 "「嗯？」"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "轻轻抱住她":
            $F7=0
        "继续倒酒":
            $F7=1
    if F7==0:
        jump L_NSU11A_SEL00_A
    if F7==1:
        jump L_NSU11A_SEL00_B
label L_NSU11A_SEL00_A:
    $F4+=1
    志雄 "「铃……」"
    window hide
    play music "BGM16"
    "我凝视着铃，仿佛要被吸入其中。"
    "抑制不住内心中涌出的爱意的我，自然而然将手搭在铃的肩膀上。"
#CHR_GET_POSC 0,F24,F25
#RSUB F24,(320)
#BG_LAY 3,SU_ZXB04,2,F24
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGB04"),"True","img/SU_ZGB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NSU11A_SU030"
    铃 "「哎？志、志雄？」"
#THREAD_STP 1
    hide bg3 with dissolve
    "铃稍微有些吃惊。"
    "抱歉吓到你了……但是，就算我想止步，手也停不下来。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGA07"),"True","img/SU_ZGA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU031"
    铃 "「啊……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "大概是因为喝醉了吧，掌握不住平衡的铃向我身上倒去。"
    志雄 "「哇……」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU04A")]=True
    show expression "img/EVN_SU04A@2x.jpg" as bg1 zorder 1 with dissolve
    play sound "SE04_19"
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
    "从紧握住铃的手中，可以直接感受到她的体温。"
    志雄 "「对、对不起！」"
    "面对慌忙松手的我，铃倚在了我的身上。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU04E")]=True
    show expression "img/EVN_SU04E@2x.jpg" as bg1 with dissolve
    voice "NSU11A_SU032"
    铃 "「哼哼」"
    "铃就这样靠着我的手臂，继续喝着啤酒。"
    志雄 "「……」"
    "这种状况……怎、怎么办啊……"
    "而且，这种状态下手也拿不出来。我的视线变得迷茫。"
    "无奈之下只能用空着的左手喝乌龙茶，挑些够得着的东西送到嘴里。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU04B")]=True
    show expression "img/EVN_SU04B@2x.jpg" as bg1 with dissolve
    voice "NSU11A_SU033"
    铃 "「志雄～」"
    志雄 "「嗯？什、什么事？」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU04C")]=True
    show expression "img/EVN_SU04C@2x.jpg" as bg1 with dissolve
    voice "NSU11A_SU034"
    铃 "「这个，吃吗？」"
    "铃指着炖猪蹄，好像注意到了我只能用左手。"
    志雄 "「我、我吃……」"
    "这个，果然是……“那个”吧？"
    "过于紧张，我不经意间喊了出来，铃于是露出了顽皮的笑容。"
    voice "NSU11A_SU035"
    铃 "「嗯……好的～」"
    "铃用筷子夹起炖猪蹄，用左手接着，往我的嘴里送。"
    "谁也不会看见吧……好吧。"
    志雄 "「啊呜……呜」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU04D")]=True
    show expression "img/EVN_SU04D@2x.jpg" as bg1 with dissolve
    "好烫！"
    "我一口气吞下了炖猪蹄，咀嚼的瞬间从中迸出了灼热的肉汁。"
    "很烫！很烫但很好吃！很好吃但还是很烫！"
    志雄 "「嗯～嗯～～！」"
    voice "NSU11A_SU036"
    铃 "「怎、怎么了？很烫吗？」"
    "铃察觉到的我的反常动作，连忙问道。"
    "我慌忙点了点头，铃于是将乌龙茶的杯子递给我。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU04B")]=True
    show expression "img/EVN_SU04B@2x.jpg" as bg1 with dissolve
    voice "NSU11A_SU037"
    铃 "「呵呵呵，吃得这么急可不行哟？」"
    play sound "SE03_20"
    志雄 "「不是这个问题……而且明明是你递过来的，却成了我的错，好过分」"
    voice "NSU11A_SU039"
    铃 "「所以说对不起啦」"
    "铃丝毫没有不觉得是自己的原因，爽快地道了歉。"
    "可恶……醉成这样说什么都白费力气。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU04A")]=True
    show expression "img/EVN_SU04A@2x.jpg" as bg1 with dissolve
    voice "NSU11A_SU040"
    铃 "「是你太死板了，都开始紧张了啊」"
    志雄 "「呼……饶了我吧」"
    "听到我深深地叹起气，铃的眼神顿时充满怒意。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU04B")]=True
    show expression "img/EVN_SU04B@2x.jpg" as bg1 with dissolve
    voice "NSU11A_SU041"
    铃 "「难得这么开心，别总是唉声叹气的，叹气的话，幸福不就从身边溜走了么？」"
    志雄 "「嗯」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU04E")]=True
    show expression "img/EVN_SU04E@2x.jpg" as bg1 with dissolve
    "铃的身体再次靠向我。"
    "虽然没有紧贴在一起，但多多少少有所接触，就处在这种微妙的距离中。"
    "确实不想让幸福就这么逃走啊。"
    voice "NSU11A_SU042"
    铃 "「志雄……我很开心啊」"
    "铃的脸颊微微泛红，边说边哧哧地笑了。"
    志雄 "「……是啊」"
    jump L_NSU11A_SEL00_X
label L_NSU11A_SEL00_B:
    志雄 "「啤、啤酒没有了」"
    window hide
    play music "OBGM17"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGB01"),"True","img/SU_ZGB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU043"
    铃 "「嗯？」"
    "铃看了看，又将空酒杯凑到嘴边。"
    "都不知道自己喝的是什么了啊……"
    play sound "SE03_95"
    志雄 "「好，请用」"
    voice "NSU11A_SU044"
    铃 "「哦、哦、好的」"
    stop se
    "我遵从铃的眼神的指示，将啤酒倒出合适的分量。"
    "啤酒和气泡的比率大体是７：３。"
    "……等等，我可不是来练习倒酒的啊。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGB02"),"True","img/SU_ZGB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU045"
    铃 "「呵呵～，志雄真的很聪明～，能当个好新娘哟」"
    "又在说些莫名其妙的话……"
    "果然醉得不行了……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGA01"),"True","img/SU_ZGA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU046"
    铃 "「心地善良，头脑聪明，又会做饭，也能干体力活。再加上还是房东，真想一家配一个啊」"
    "我是家用电器么。"
    "还是说，我只是那种简单便利能被人使用的东西……"
    志雄 "「听了这话，我应该高兴吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGA06"),"True","img/SU_ZGA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU047"
    铃 "「哎，为什么不呢～？这么说吧，无论志雄受到什么样的表扬，都会高兴的吧？」"
    "铃侧头倾听着。"
    志雄 "「是啊，作为男人，果然要……帅气、可靠、能干、学习优秀？」"
    志雄 "「而且要性格善良，头脑聪明？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGB01"),"True","img/SU_ZGB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU048"
    铃 "「呵呵，志雄君～，你不明白么！」"
    "铃将脸转向我，伸出手猛地指向我。"
    "……手指略微颤动着。"
    voice "NSU11A_SU049"
    铃 "「帅气什么的，这些不久都会习惯，如果开始交往以后，这些都没有关系」"
    志雄 "「是这样啊……」"
    "虽然我并不是单单被铃的外表所吸引，不过直到现在，依然会有被她的容颜吸引住的瞬间。"
    "铃难道不是这样的么……？"
    voice "NSU11A_SU050"
    铃 "「可靠什么的能有一点是最好不过的，但如果习惯了就会变得依赖对方哟」"
    志雄 "「原、原来如此，确实也有道理的」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGA01"),"True","img/SU_ZGA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU051"
    铃 "「要是能干和学习优秀的话是很好，但要做到什么程度才能满足？现在优秀的女人很多，自己很能挣钱的也很多啊？」"
    voice "NSU11A_SU052"
    铃 "「如果和她相互竞争，要是输了该怎么办？」"
    志雄 "「能怎么办，如果对方比自己优秀的话，尊敬她就是了……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGA02"),"True","img/SU_ZGA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "铃轻轻地叹了口气，晃了晃手指。"
    voice "NSU11A_SU053"
    铃 "「这样的人很少的」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGA05"),"True","img/SU_ZGA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU054"
    铃 "「那些炫耀自己工作出色的男性，如果女朋友比自己优秀，他们打心底不愿意承认这个事实，于是态度变得很恶劣」"
    志雄 "「是么……」"
    "这是铃的偏见吗？不过，总觉得有亲身的体会在其中，难道过去发生过这样的事情？"
    "说起来，总觉得有种虽然是工作疲倦的女白领的牢骚话却还是要听着的感觉……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGA01"),"True","img/SU_ZGA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU055"
    铃 "「所以说，男人最重要的并不是这些，明白了吧？」"
    "就算你滔滔不绝地说着话，我也无法理解的吧……"
    "总之，先点头同意，不能再像稻穗一样重蹈覆辙了。"
    志雄 "「这么说来，善良是最重要的？」"
    voice "NSU11A_SU056"
    铃 "「不能说是最重要，但也是与人相处的基本条件吧？」"
    voice "NSU11A_SU057"
    铃 "「当然，其它方面要是都做不好也不行，但还是个程度的问题吧？」"
    voice "NSU11A_SU058"
    铃 "「也就是说，懂得把握平衡的人是最好的」"
    "结果，这些话我一句也没能理解。"
    "然而，我非常明白铃没有太过意识到我所认为的男性立场。"
    志雄 "「把握平衡啊……」"
    "从工作和社会的立场而言，如今的我怎么做也无法和铃匹敌。"
    "不过，铃完全没在意这一点。"
    "话虽如此……总有一种想被铃认同的感觉。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGC04"),"True","img/SU_ZGC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU059"
    铃 "「喂，志雄～？怎么这么消沉啊～」"
    "反应过来时，铃正注视着我的脸，担心地望向我。"
    志雄 "「没、没什么，我们还是多吃点吧，看，啤酒还有呢」"
    "先不管这些了，现在应该做的是一起开心地享受当下的一切。"
    "守在铃身边的人，一定要是能做到这一点的男人。"
    jump L_NSU11A_SEL00_X
label L_NSU11A_SEL00_X:
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 2
#BG_PRI 0
#BG_SETWC 0,2,EXBG04N,BG63NA6
    scene expression "img/EXBG04N@2x.jpg" as bg0 with dissolve
    play sound "SE05_16L"
    pause (32/32.0)
#FADE_IN 1
    志雄 "「铃，还要啤酒么？」"
    "一开始放在桌子上的啤酒已经彻底喝光了。"
    "照着这种状态喝酒，连冰箱里的那些都能全部喝完。"
    志雄 "「还是稍微休息一下？」"
    铃 "「……」"
#MESEX_A M_NOA,A_CH_SU,"【鈴】「……」%K%P"
    "怎么？没有回复……"
    志雄 "「铃？」"
    "定睛一看，铃低着头坐在那里，身体摇摇摆摆打起了盹。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZGA04"),"True","img/SU_ZGA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU060"
    铃 "「嗯？没事没事，我没睡哟」"
    志雄 "「可是，怎么看都觉得你睡着了……」"
    "明天还有明天的计划，也是时候让她舒舒服服睡一觉了。"
    "说起来，铃喝得太得意忘形，竟然喝过头了……"
    scene expression "img/BG63NA1@2x.jpg" as bg1 with dissolve
    hide lh0 with dissolve
    play sound "SE00_27"
    志雄 "「有什么事吗？」"
    voice "NSU11A_XR000"
    仲居のおじさん "「用过的餐具需要为您撤下吗？」"
    志雄 "「好的，拜托了」"
    play sound "SE03_53"
    voice "NSU11A_XR001"
    仲居のおじさん "「您的同伴是要休息了吗？」"
    志雄 "「好像是呢」"
    "铃现在靠着我的肩膀已经彻底睡着了。"
    voice "NSU11A_XR002"
    仲居のおじさん "「那么我来为您铺好被子吧」"
    志雄 "「好的，有劳了」"
    "那么，该怎么安置铃才好呢……"
    stop se
    voice "NSU11A_XR003"
    仲居のおじさん "「那么我就开始铺了……」"
    志雄 "「哎？啊，好的」"
    play sound "SE03_97"
    "服务员们熟练地开始把被子并排摆在一起。"
    "……咦、咦？怎么办，要去让他们改过来吗？"
    "至少要在中间立个屏风，或是去别的房间……"
    window hide
    stop se
    scene expression "img/BG63NA3@2x.jpg" as bg_over zorder 2 with dissolve
    "在我还陷入苦恼中的时候，服务员已经把被子铺好了。"
    voice "NSU11A_XR005"
    仲居のおじさん "「另外浴室会在十点钟关闭，如有需要请在那时间之前离开」"
    志雄 "「好、好的，我知道了」"
    voice "NSU11A_XR006"
    仲居のおじさん "「那么，我告辞了」"
    window hide
    play sound "SE00_48"
    "总之，先让铃盖上被子睡吧。"
    志雄 "「铃，铃？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGA04"),"True","img/SU_LGA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU061A"
    铃 "「嗯嗯～{w=3}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGA06"),"True","img/SU_LGA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU061B"
    extend "什么事？」"
    志雄 "「被子在这里，盖上再睡吧」"
    voice "NSU11A_SU062"
    铃 "「……嗯，知道了」"
    "我勉强让铃站起来，她支撑着摇摇晃晃的身体就倒在了枕头上。"
    志雄 "「好的，再稍微过去……铃，枕头在这」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LGA04"),"True","img/SU_LGA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU11A_SU063"
    铃 "「嗯……志雄」"
    window hide
    play sound "SE04_19"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    志雄 "「哇！」"
    voice "NSU11A_SU064"
    铃 "「呜哇」"
    志雄 "「啊哈哈……铃真是的……」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU05A")]=True
    scene expression "img/EVN_SU05A@2x.jpg" as bg1 with dissolve
    voice "NSU11A_SU065"
    铃 "「呜～嗯……」"
    "倒在被子上的铃发出轻微的呻吟。"
    "不过，问题不是这个……而是，衣领都松掉了……"
    window hide
#BG_UV_AUTOC 1,(640/8),(448/8),(640-(640/4)),(448-(448/4)),1,F24,48
#BG_UV_SAVEC 1
    play sound "SE07_02"
#QUA3_ALL 
    志雄 "「铃、铃？等等，我说……」"
    window hide
#BG_UV_AUTOC 1,0,0,640,448,1,F24,48
#BG_UV_SAVEC 1
    pause (16/32.0)
    play sound "SE06_29L"
    铃 "「……」"
    志雄 "「铃？」"
    铃 "「……」"
    "无论怎么呼唤，铃都没有睁开眼睛。"
    "怎、怎么办啊？就这么放着不管？还是帮她弄好？还是……"
    志雄 "「这没、没、没办法啊……」"
    "我就像在辩解给谁看一样，自言自语地把手慢慢伸过去。"
    "一直在意着这件事会睡不着的，所以只能这么办了。"
    "不要碰到多余的地方，要慎重地、慎重地……"
    voice "NSU11A_SU066"
    铃 "「嗯……」"
    志雄 "「哇」"
    "吓、吓我一跳……"
    "如果铃现在睁开眼睛，肯定会认为我是一个色狼。"
    志雄 "「那个，失、失礼了……」"
    "我只是、我只是整理了一下领子……"
    window hide
    stop se
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU05B")]=True
    scene expression "img/EVN_SU05B@2x.jpg" as bg1 with dissolve
    voice "NSU11A_SU067"
    铃 "「……你这只手准备干什么～？」"
    play sound "SE07_02"
    志雄 "「呜哇哇！」{w=3}{nw}"
    志雄 "「对对对对对对不起！不、不是这样的，我没别的意思！只、只是，想把弄乱的浴衣帮你整理下……！」"
    window hide
#SE_VOLC 1,0
    play music "BGM13"
    voice "NSU11A_SU068"
    铃 "「哼哼，真的么？」"
    志雄 "「当、当然」"
    "我像坏掉的玩具一样，不停地点着头。"
    voice "NSU11A_SU069"
    铃 "「哼～，很遗憾，更进一步是不行的～」"
    志雄 "「嗯、嗯……所、所以真的什么都没有」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU05C")]=True
    scene expression "img/EVN_SU05C@2x.jpg" as bg1 with dissolve
    voice "NSU11A_SU070"
    铃 "「那就这样吧……呜，我睡了哟～」"
    志雄 "「晚、晚安……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU05A")]=True
    scene expression "img/EVN_SU05A@2x.jpg" as bg1 with dissolve
    voice "NSU11A_SU071"
    铃 "「呼，呼」"
    window hide
#SE_VOLC 1,128
    scene expression "img/BG63NA3@2x.jpg" as bg_over zorder 2 with dissolve
    play sound "SE06_16"
#BG_ALP_AUTOC 0,0,0,F24,2
#BG_ALP_SAVEC 0
#BG_SWPC 0
    hide bg2 with dissolve
#BG_PRI 0
#BG_PRI 2
#BG_ALPC 2,128
    pause (32/32.0)
    "这次彻底睡着了……"
    "深夜的月色，模糊地映照出铃那美丽的容颜。"
    "与发出平稳的呼吸声的她相反，我却迟迟难以入眠。"
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
#label THREAD_QUA_WIN
#TH_QUAKE_WIN 4
#EOT
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT