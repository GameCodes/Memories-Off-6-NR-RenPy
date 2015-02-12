label NCL01A2:
    $currentlabel = "NCL01A2"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    play sound "SE05_15L"
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    scene expression Solid("000") with None
    show expression "img/BG06AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG06AA@2x.jpg" as bg0 with dissolve
#FADE_IN 0
    $month = '07'
    $day = '18'
    $date = '2'
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    show expression Solid("000") as hand with None
    voice "NCL01A_KU000"
    クロエ？ "「猜猜我是～谁？」"
    志雄 "「哇！？」"
    "突然被人从身后蒙住了眼睛。"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "克罗艾学姐":
            $F7=0
        "莉莉丝":
            $F7=1
    if F7==0:
        jump L_NCL01A_SEL00_A
    if F7==1:
        jump L_NCL01A_SEL00_B
label L_NCL01A_SEL00_A:
    "一听声音就知道是谁了，我用很平静的声音回答。"
    志雄 "「那个、克、克罗艾学姐……」"
    voice "NCL01A_KU001"
    克罗艾 "「真厉害，你怎么知道的？」"
    "从耳边传来开心的声音，气息让耳朵痒痒的。也就是说，学姐从背后抱住了我……"
    志雄 "「那、那个，可以不用贴得那么紧。」"
    voice "NCL01A_KU002"
    克罗艾 "「咦？……啊。」"
    window hide
    play sound "SE01_00A"
    hide hand
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB04"),"True","img/CL_MAB04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#SE_VOLC 1,(64/4)
#FADE_IN 1,16
    play music "BGM04"
    "听我一说，克罗艾学姐立刻退开了……看来她自己都没发觉。"
    voice "NCL01A_KU003"
    克罗艾 "「真、真巧啊。竟然在这里遇到你」"
    志雄 "「什么竟然啊，这里是校门口哦？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB02"),"True","img/CL_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU004"
    克罗艾 "「啊呀、还真是。我都没注意」"
    "学姐一脸镇定地说。"
    "刚才慌忙的样子仿佛是空气中掠过的浮影一般，还没眨眼就已经消逝的无影无踪了。"
    志雄 "「你好像心情很好呢。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU005"
    克罗艾 "「啊呀，看得出来吗？」"
    "虽说学姐总是喜欢在我毫无防备的时候恶作剧，但大多是两个人单独在一起的时候。她竟然当众贴到我身上来，实在很少见。"
    "……我倒是相当不好意思啊。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA01"),"True","img/CL_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    jump L_NCL01A_SEL00_X
label L_NCL01A_SEL00_B:
    "这声音我是不可能听错……不过突然产生了一个恶作剧的想法。"
    志雄 "「呃……莉莉丝？」"
#SE_VOLC 1,255
    voice "NCL01X_KU000"
    克罗艾 "「诶……？」"
    "……"
    "…………"
    "时间仿佛凝固了。"
    voice "NCL01X_KU001"
    克罗艾 "「………………呼。」"
    hide hand
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC02"),"True","img/CL_MAC02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#SE_VOLC 1,(64/4)
#FADE_IN 1,16
    play music "OBGM27"
    志雄 "「学姐？」"
    voice "NCL01X_KU002"
    克罗艾 "「恩恩……」"
    志雄 "「啊，那个。我、我开玩笑的。我当然立刻就知道是克罗艾学姐了——」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC03"),"True","img/CL_MAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01X_KU003"
    克罗艾 "「…………呼。」"
    志雄 "「另、另外，学姐。你怎么会在这里？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA05"),"True","img/CL_MAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01X_KU004"
    克罗艾 "「啊呀，真的是太巧了。竟然在这里遇到你。」"
    "……不妙。"
    "本只是打算胡闹一下，结果却惹得她相当地不高兴了。"
    志雄 "「对、对了。学姐，你好像心情很好似的，出什么事了吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA02"),"True","img/CL_MAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01X_KU005"
    克罗艾 "「啊呀，志雄，你看我现在的样子，感觉我心情好吗？」"
    志雄 "「啊、不不不。不是说现在，是刚才……」"
    志雄 "「那个，我只是胡闹了一下……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA06"),"True","img/CL_MAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01X_KU006"
    克罗艾 "「呼……」"
    voice "NCL01X_KU007"
    克罗艾 "「也对呢。反正我对志雄也就是一般的学姐。不像远峰那样有青梅竹马的先天优势，也比不上远峰生来的可爱，还不像远峰那样——」"
    志雄 "「啊—！抱歉！对不起！」"
    stop music fadeout 1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB02"),"True","img/CL_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01X_KU008"
    克罗艾 "「哈哈……」"
    "……诶？"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB06"),"True","img/CL_MAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01X_KU009"
    克罗艾 "「哈哈哈……志雄啊，你真的慌成这样。」"
    window hide
    play music "BGM04"
    "啊……到头来被捉弄的还是我啊。不愧是克罗艾学姐。"
    志雄 "「急死我了……我还以为你真的生气了。」"
#MUS_VOL 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA03"),"True","img/CL_MAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01X_KU010"
    克罗艾 "「我真的很生气哦。那一秒。」"
    志雄 "「对不起……」"
#MUS_VOL 128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA01"),"True","img/CL_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01X_KU011"
    克罗艾 "「算了啦。另外，我有个好消息要和你分享。」"
    jump L_NCL01A_SEL00_X
label L_NCL01A_SEL00_X:
    voice "NCL01A_KU006"
    克罗艾 "「最新消息，我爸爸不久之后就不用再去医院了。」"
    "学姐的父亲自那以后也多次住院检查过。"
    if not persistent.dictlist[59] and persistent.show_dict:
        $persistent.dictlist[59]=True
        show screen dict_pop(i=59)
    "再算上累积下来的公司的事，一定在各方面都很辛苦吧。"
    志雄 "「真的嘛！？恭喜了！」"
    voice "NCL01A_KU007"
    克罗艾 "「嗯。康复比预期中快，连医生都很意外呢。」"
    "学姐满脸笑意地说着，发自内心的开心，从每一个地方溢了出来。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU008"
    克罗艾 "「对了，志雄你现在要回家了吧？」"
    志雄 "「嗯，是的……你是特意在等我的吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB02"),"True","img/CL_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU009"
    克罗艾 "「不是，我只是偶然路过。然后就看到了志雄的身影。」"
    志雄 "「偶然路过吗？车站在更那边啊……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC01"),"True","img/CL_MAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU010"
    克罗艾 "「我陪爸爸去医院刚回来啦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC04"),"True","img/CL_MAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU011"
    克罗艾 "「可爸爸却说他自己一个人能回去，就先走了。」"
    志雄 "「那个，他这样不要紧吗？」"
    "也许是戳中了学姐内心的忧虑，学姐脸上露出了些许忧郁。"
    voice "NCL01A_KU012"
    克罗艾 "「我就是有些担心，可他很顽固……」"
    志雄 "「可就算如此，走的方向也完全不对哦？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC05"),"True","img/CL_MAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#REEK_CHR 0
    voice "NCL01A_KU013"
    克罗艾 "「唔……这个嘛，我觉得……说不定会遇到志雄，所以……」"
#REMOVE_REEK_CHR 0
    "哈，终于老实交代了。这真是最令人期待的回答了吧。"
    志雄 "「这样可不能叫偶然哟。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB05"),"True","img/CL_MAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU014"
    克罗艾 "「我们错过的可能性更大，所以也算是某种程度上的偶然咯。」"
    志雄 "「这么说倒也是。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB04"),"True","img/CL_MAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU015"
    克罗艾 "「别说这个了，我现在要去商店街买东西，要一起去吗？」"
    志雄 "「乐意之极。」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC01"),"True","img/CL_LAC01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCL01A_KU016"
    克罗艾 "「那就这么决定了。好了，走吧。」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    play sound "SE01_12L"
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
#BG_ALPC 1,128
#BG_PRI 0
#BG_PRI 1
    scene expression "img/BG04AA@2x.jpg" as bg0 with dissolve
    "话音刚落，克罗艾学姐就抓起我的手，朝商店街的方向走去。"
    志雄 "「哇、等等。」"
    志雄 "「真——没办法啊。」"
    "刚才还有些苦恼阴郁的心情，稍稍有些转晴了。"
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
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01A")]=True
    show expression "img/EVN_CL01A@2x.jpg" as bg0 zorder 0 with dissolve
##BG_ANM_ONC 0,0,CHRID_CL
    play sound "SE08_17L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,(64/2)
    play music "BGM13"
    志雄 "「好了，先从什么开始？」"
    "我们进了超市，并肩走在一起，看着两旁的各种食材。"
    voice "NCL01A_KU017"
    克罗艾 "「我看看，总之先买咖喱块，土豆，然后是……」"
    志雄 "「学姐家今天吃咖喱吗？」"
    voice "NCL01A_KU018"
    克罗艾 "「对。本来我是想做点丰盛点的东西，可是太突然了。」"
    "克罗艾学姐有些难为情地回应道。"
    voice "NCL01A_KU019"
    克罗艾 "「而且，这也是爸爸提议的。」"
    "学姐一面清点着篮子里的东西，一面很仔细地挑选着其他食材。"
    "看了一眼她的篮子，一阵强烈违和感扑面而来。"
    志雄 "「那个……篮子里放了胡萝卜哦。」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01D")]=True
    show expression "img/EVN_CL01D@2x.jpg" as bg0 with dissolve
    voice "NCL01A_KU020"
    克罗艾 "「那、那又怎么了……」"
    "学姐略显无奈的拿起篮子里的胡萝卜，原地站了一会儿，最后还是又放进了篮子。"
    志雄 "「……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01E")]=True
    show expression "img/EVN_CL01E@2x.jpg" as bg0 with dissolve
    voice "NCL01A_KU021"
    克罗艾 "「……呼。」"
    "再望向她，她便无奈地叹了口气，开口说道。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01D")]=True
    show expression "img/EVN_CL01D@2x.jpg" as bg0 with dissolve
    voice "NCL01A_KU022"
    克罗艾 "「因为我爸爸他喜欢胡萝卜啦……和我以前一样。」"
    志雄 "「哦……」"
    "学姐讨厌胡萝卜是个很漫长而沉重的故事，这我知道。"
    "还是赶快换个话题吧。"
    志雄 "「这让我想起了不少事情呢。」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01A")]=True
    show expression "img/EVN_CL01A@2x.jpg" as bg0 with dissolve
    voice "NCL01A_KU023"
    克罗艾 "「什么？」"
    志雄 "「学姐住在我家时候的事。那时我们也经常一起出门买东西的。」"
    voice "NCL01A_KU024"
    克罗艾 "「嗯……」"
    "那时候每天都能见到学姐，真是开心得不得了。"
    "可是现在，克罗艾学姐考进了大学，而我还在准备着考试。"
    "虽然学姐偶尔还是会在周末到我家来，我们的感情也一路顺风，但见面的机会和时间都多少受到了很大的制约……"
    "不管怎样，住在一起的那段美妙时光，即使现在回忆起来，也让人觉得美得和梦一样。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01B")]=True
    show expression "img/EVN_CL01B@2x.jpg" as bg0 with dissolve
    voice "NCL01A_KU025"
    克罗艾 "「是啊。真的很久没像这样两个人一起来买晚饭的材料了。」"
    志雄 "「学姐到我家来的时候，也大多会在路上就买好东西嘛。」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01A")]=True
    show expression "img/EVN_CL01A@2x.jpg" as bg0 with dissolve
    voice "NCL01A_KU026"
    克罗艾 "「那是因为想尽享和志雄在一起的时间，早知道这样平时也一起来就好了。」"
    志雄 "「诶？」"
    voice "NCL01A_KU027"
    克罗艾 "「因为买东西的时候我们也在一起嘛？」"
    voice "NCL01A_KU028"
    克罗艾 "「而且还能让你来拿东西哦～」"
    "说着，她将装满食材的篮子递到我手里。"
    志雄 "「嗯，作为男生，这点小事是必须的。」"
    "嘴上这么逞强，其实手里的篮子比想象中要重好多。"
    voice "NCL01A_KU029"
    克罗艾 "「太好了。那我们再多逛两三家吧？」"
    志雄 "「请你饶了我吧……」"
    "刚刚还男子气概十足的我，真的是认输了。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01B")]=True
    show expression "img/EVN_CL01B@2x.jpg" as bg0 with dissolve
    voice "NCL01A_KU030"
    克罗艾 "「呵呵，说着玩的啦。」"
    "克罗艾学姐对我笑了笑，把脸稍微靠过来了一些。"
    "这种情况到现在依然让我心跳不已。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01A")]=True
    show expression "img/EVN_CL01A@2x.jpg" as bg0 with dissolve
    voice "NCL01A_KU031"
    克罗艾 "「呐、志雄。」"
    志雄 "「什、什么？」"
    voice "NCL01A_KU032"
    克罗艾 "「周围的人会怎么看我们呢？」"
    志雄 "「怎么看啊……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01C")]=True
    show expression "img/EVN_CL01C@2x.jpg" as bg0 with dissolve
    voice "NCL01A_KU033"
    克罗艾 "「姐弟？　情侣？　还是夫妇呢？」"
    "看样子不是在捉弄我。有种仿佛在玩味什么重要的东西的感觉。"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "姐弟":
            $F7=0
        "情侣":
            $F7=1
        "夫妇":
            $F7=2
    if F7==0:
        jump L_NCL01A_SEL01_A
    if F7==1:
        jump L_NCL01A_SEL01_B
    if F7==2:
        jump L_NCL01A_SEL01_C
label L_NCL01A_SEL01_A:
    "我稍微犹豫了一下，随口回答道。"
    志雄 "「可能认为我们是姐弟吧……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01A")]=True
    show expression "img/EVN_CL01A@2x.jpg" as bg0 with dissolve
    voice "NCL01Y_KU000"
    克罗艾 "「这是为什么？」"
    "听了我的回答，学姐露出诧异的表情。"
    "看上去她似乎有那么一点点遗憾。"
    志雄 "「啊，怎么说呢……我还是高中生嘛。」"
    voice "NCL01Y_KU001"
    克罗艾 "「哎呀，那我也还是大学生咯？」"
    志雄 "「不是这个意思。该说是立场的问题还是别的……」"
    voice "NCL01Y_KU002"
    克罗艾 "「志雄对自己没自信吗？」"
    "我无言地点头肯定了学姐的话。"
    "我认为自己有好好地在和学姐交往，这一点我有自信。"
    "可是要说现在我们周围的人是否有相同的感想的话……"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01E")]=True
    show expression "img/EVN_CL01E@2x.jpg" as bg0 with dissolve
    voice "NCL01Y_KU003"
    克罗艾 "「真拿你没办法。」"
    "学姐轻轻叹了口气，和我四目相对。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01A")]=True
    show expression "img/EVN_CL01A@2x.jpg" as bg0 with dissolve
    voice "NCL01Y_KU004"
    克罗艾 "「志雄这么消极，不仅周围的人，连我也会不安起来的。这种时候必须得说得坚决一点。」"
    志雄 "「说得……也是呢。」"
    voice "NCL01Y_KU005"
    克罗艾 "「那我再问一次。周围的人是怎么看我们的？」"
    志雄 "「情侣。」"
    "我看着学姐的眼睛断言道。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01C")]=True
    show expression "img/EVN_CL01C@2x.jpg" as bg0 with dissolve
    "紧接着，刚才还看上去游刃有余的学姐一下子就满脸通红。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01F")]=True
    show expression "img/EVN_CL01F@2x.jpg" as bg0 with dissolve
    jump L_NCL01A_SEL01_X
label L_NCL01A_SEL01_B:
    "面对她的提问，我尽可能严肃地做出了回答。"
    志雄 "「应该还是情侣吧……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01F")]=True
    show expression "img/EVN_CL01F@2x.jpg" as bg0 with dissolve
    voice "NCL01A_KU034"
    克罗艾 "「对、对啊。就是。」"
    "明明是她自己说起的话题，学姐却面红耳赤。"
    voice "NCL01A_KU034A"
    克罗艾 "「情侣……情侣……」"
    "这样的反应，反倒让我不好意思起来了……"
    jump L_NCL01A_SEL01_X
label L_NCL01A_SEL01_C:
    志雄 "「说不定会觉得我们是夫妇哦。」"
    voice "NCL01Y_KU006"
    克罗艾 "「咦！？是，是嘛……？」"
    "学姐听了我的回答，很罕见的乱了阵脚。"
    志雄 "「你看，我们不是在一起买晚饭的材料么」"
    "我不禁高兴起来，又多说了一句。"
    "实际上我还穿着校服，顶多就把我们看成是情侣吧。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01F")]=True
    show expression "img/EVN_CL01F@2x.jpg" as bg0 with dissolve
    voice "NCL01Y_KU007"
    克罗艾 "「那还……有些……有些早了，嗯。早了一点点。」"
    志雄 "「那学姐你认为别人怎么看我们？」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01C")]=True
    show expression "img/EVN_CL01C@2x.jpg" as bg0 with dissolve
    voice "NCL01Y_KU008"
    克罗艾 "「这个嘛……大概就……情、情侣吧？」"
    "话刚说完，学姐的脸就变得通红。"
    "我再继续捉弄她的话，那就有些坏心眼了。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01F")]=True
    show expression "img/EVN_CL01F@2x.jpg" as bg0 with dissolve
    jump L_NCL01A_SEL01_X
label L_NCL01A_SEL01_X:
    voice "NCL01A_KU035"
    克罗艾 "「总觉得事到如今再用语言表达出来，真是很难为情呢……」"
    志雄 "「话说，还有别的东西要买么？」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01C")]=True
    show expression "img/EVN_CL01C@2x.jpg" as bg0 with dissolve
    voice "NCL01A_KU036"
    克罗艾 "「诶？啊、嗯，已经够了。」"
    志雄 "「那我们去结账吧。」"
    "我说着向克罗艾学姐伸出了没有拿东西的那只空手。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL01B")]=True
    show expression "img/EVN_CL01B@2x.jpg" as bg0 with dissolve
    voice "NCL01A_KU037"
    克罗艾 "「好啊。」"
    "克罗艾学姐握住了我的手。仅仅如此，我都紧张得跟刚开始交往时一样，心脏扑通扑通，猛跳个不停。"
    "不用说，虽然只是朝着收银台走去，我们彼此却都红着脸。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
#BG_ANM_OFFC 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 1
#BG_SETWC 0,1,BG03EA,NIMG01C
#EFF_STAC 0,CLOUD_C,EFF_NOSKIP
    show expression "img/NIMG01C@2x.png" as bg_over zorder 2
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
    pause 2
    scene expression "img/BG03EA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC01"),"True","img/CL_MAC01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE01_12L"
    pause (16/32.0)
    play sound "SE05_13L"
    pause (16/32.0)
#FADE_IN 1
#SE_VOLC 1,(64/2)
    play music "BGM04"
    "和克罗艾学姐一起走在放学回家的路上。"
    "回想起来，学姐毕业后，我们也有见过很多次面，但却很少像这样一起回家。"
    window hide
#FADE_OUT 1
#SE_VOLC 0,0
#BG_ALP_AUTOC 1,128,0,F24
#EFF_STPC 0,EFF_SKIP
    hide bg1 with dissolve
#BG_ALPC 1,128
#FADE_IN 1
    voice "NCL01A_KU038"
    克罗艾 "「也就是说，积分是微分的逆运算。按照这个规则来解的话……」"
    志雄 "「原来如此。」"
    "回家的路上，我让克罗艾学姐教我上上周期末考试中没搞懂的问题。"
    "老实说，对于一对走在归家路途上的情侣来说，这实在是没什么情调的话题。好在学姐的讲解简单易懂，就我备考生的身份而言，确实很受益。"
    志雄 "「抱歉，总是问你这些。」"
    "总是不小心就说起学习的话题，这是考生的习性在作怪吗……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU039"
    克罗艾 "「我不介意呀。能帮上志雄的忙，我也很开心。」"
    志雄 "「真是在克罗艾学姐面前抬不起头来啊。」"
    window hide
#SE_VOLC 0,128
#BG_SET_BACK 
#BG_INIC 1
    #show expression "img/BG_BLACK@2x.jpg" as bg1 with dissolveBG_LINEAR_SLIDE
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    show expression "img/BG04EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG04EA@2x.jpg" as bg0 with dissolve
#SE_VOLC 0,0
    hide bg1 with dissolve
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB05"),"True","img/CL_MAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU040"
    克罗艾 "「呐、志雄。我有一个请求。」"
    志雄 "「是什么？」"
    "学姐看着我的脸，露出复杂的表情。"
    stop music fadeout 1
    志雄 "「那个……学姐？」"
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
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB05"),"True","img/CL_LAB05A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCL01A_KU041"
    克罗艾 "「对，就是学姐这个称呼」"
    志雄 "「诶？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC04"),"True","img/CL_LAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU042"
    克罗艾 "「你叫我学姐总觉得很刻板。」"
    voice "NCL01A_KU043"
    克罗艾 "「因为我已经毕业了呀。」"
    志雄 "「话虽是这么说……」"
    window hide
    play music "BGM13"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC03"),"True","img/CL_LAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU044"
    克罗艾 "「而且我们，那个……在、在交往嘛」"
    "说完，克罗艾学姐红着脸低下头。"
    志雄 "「啊、那个……」"
    "我也不禁脸红起来。"
    志雄 "「这个，那怎么称呼好呢？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU045"
    克罗艾 "「我都直接叫你志雄，你也直呼我的名字就好了啊」"
    志雄 "「诶？这有点……」"
    "对我来说，克罗艾学姐就是克罗艾学姐……突然要我直呼其名实在是太不好意思了……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB04"),"True","img/CL_LAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU046"
    克罗艾 "「那你叫叫看～」"
    志雄 "「唔。」"
    "克罗艾学姐用满怀期待的目光凝视着我。"
    "我咬了咬牙叫出了她的名字。"
    志雄 "「克罗艾……学姐……」"
    window hide
#SE_VOLC 1,64
#MUS_VOL 64
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB03"),"True","img/CL_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    pause (16/32.0)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA02"),"True","img/CL_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU047"
    克罗艾 "「志雄～？」"
    "……不是我有心恶作剧，这么突然，实在是办不到的啦。"
#SE_VOLC 1,(64/2)
#MUS_VOL 128
    志雄 "「对突然就这样直呼名字，还是有些抵触感……」"
    voice "NCL01A_KU048"
    克罗艾 "「那接一个『小姐』也行吧」"
    志雄 "「呃、这个……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA03"),"True","img/CL_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU049"
    克罗艾 "「行了，快点快点。」"
    "在她的催促下，我忍住了害羞的情绪再一次叫道。"
    志雄 "「克罗艾、学姐……」"
#SE_VOLC 1,255
    stop music fadeout 1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA02"),"True","img/CL_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU050"
    克罗艾 "「呼」"
    "她深深地叹了口气。"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#SE_VOLC 1,(64/2)
    play music "OBGM20"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC02"),"True","img/CL_MAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    voice "NCL01A_KU051"
    克罗艾 "「对志雄来说，我还是那么有距离感啊。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC03"),"True","img/CL_MAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    "克罗艾学姐带着满满的无奈看了看我，随后立刻甩开了视线。"
    志雄 "「啊，那个……」"
    voice "NCL01A_KU052"
    克罗艾 "「有些受打击呢。」"
    "学姐的肩膀有些微微颤抖。糟糕，她真的生气了……？"
    志雄 "「不是的，这种情况是我对学姐很尊敬，所以称呼学姐……」"
    "我慌忙组织着语言，而克罗艾学姐的肩膀颤抖得更大了——。"
    stop music fadeout 1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB02"),"True","img/CL_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    voice "NCL01A_KU053"
    克罗艾 "「哈哈哈。」"
    志雄 "「诶？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB06"),"True","img/CL_MAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-96)/640.0
    with dissolve
    voice "NCL01A_KU054"
    克罗艾 "「哈哈，对不起。我开玩笑的」"
    志雄 "「啊……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play music "BGM04"
#CHR_INIC 0
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCL01A_KU055"
    克罗艾 "「要突然改变称呼的确有点难了。」"
    voice "NCL01A_KU056"
    克罗艾 "「虽说有些不满，不过现在还是不予追究吧～」"
    志雄 "「感、感激不尽。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB02"),"True","img/CL_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU057"
    克罗艾 "「那首先改改你这用敬语的习惯吧」"
    志雄 "「咦？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU058"
    克罗艾 "「可以不用敬语了，再改变对我的称呼，这样可以吧？」"
    志雄 "「咦，请等一下啊！？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB06"),"True","img/CL_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU059"
    克罗艾 "「好，违禁一次～♪」"
    "克罗艾学姐笑着说道。一时间，我也什么都说不出口了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU060"
    克罗艾 "「嗯？快呀快呀，下一个话题是？」"
    志雄 "「啊……唔……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA02"),"True","img/CL_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU061"
    克罗艾 "「真是的，拿你没办法。真的改不掉吗？」"
    志雄 "「我会努力的……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA01"),"True","img/CL_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU062"
    克罗艾 "「我期待着哦。」"
    window hide
    show expression Solid("000") as filter zorder 5:
        alpha 0.5
    with dissolve
#FILT_PRI 5
#FILT_IN 48,0,COL_DARK2
    "学姐总是这么开朗，可靠。"
    "去年背负着家庭的压力，仍不停地对学生会进行各方面的指导。"
    "现在不仅要看护住院的爸爸，最近还开始打工了。"
    "我不想让她再来操心的我的志愿问题。"
    "再说，将来的事必须由我自己来决定……"
    window hide
    hide filter with dissolve
#FILT_OUT 48
#FILT_PRI 1
    voice "NCL01A_KU063"
    克罗艾 "「——志愿校你决定了吗？」"
    志雄 "「诶？」"
    "学姐很干脆地就问了出来，我差点听岔了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA02"),"True","img/CL_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU064"
    克罗艾 "「已经暑假了吧。可志雄还总是皱着眉头，考试的事也只字不提。」"
    志雄 "「这个……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU065"
    克罗艾 "「你不介意的话，你可以和我商量商量哦？」"
    志雄 "「真的服了呢……」"
    "实在敌不过学姐，我再次这么认为。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB02"),"True","img/CL_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU066"
    克罗艾 "「我呢——」"
    "克罗艾学姐思考片刻后，开口说道。"
    voice "NCL01A_KU067"
    克罗艾 "「还是想大学毕业后到爸爸的公司去帮忙。」"
    志雄 "「这样啊。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "和我预想中一样。克罗艾学姐为了自己的目标正在不断努力着。"
    "而相对的，我却——"
    "不禁有些妄自菲薄了。学姐又继续说了下去，那言语将我拉回了现实当中。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB02"),"True","img/CL_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU068"
    克罗艾 "「还有呢。」"
    志雄 "「咦？还有别的吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB03"),"True","img/CL_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU069"
    克罗艾 "「又不是只能有一种想法吧？」"
    志雄 "「这倒是没错……」"
    stop music fadeout 1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB04"),"True","img/CL_LAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU070"
    克罗艾 "「我要和志雄长久地交往下去～！」"
    志雄 "「啊……？」"
    window hide
    play music "OBGM29"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB06"),"True","img/CL_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU071"
    克罗艾 "「这就是我对未来的展望。很棒吧～」"
    志雄 "「嗯，是的，当然！」"
    "我头脑中变得一片空白，勉强挤出了这一句话。"
    "克罗艾学姐连我们的将来都考虑到了……仅仅如此就让我感动得想要落泪。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA01"),"True","img/CL_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU072"
    克罗艾 "「总之我们先去焰火大会吧～」"
    志雄 "「诶？什么？」"
    "话题突然转换到身边的事，我没跟上步调不由得发出反问。"
    voice "NCL01A_KU073"
    克罗艾 "「芦鹿岛的焰火大会。毎年都有很多人聚集在一起办得很热闹的呀？」"
    志雄 "「嗯，是啊。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU074"
    克罗艾 "「作为长久交往的第一步，我们先去焰火大会约会吧～」"
    志雄 "「好、好的！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB05"),"True","img/CL_LAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU075"
    克罗艾 "「既然这么决定了，那首先就要浴衣……我家里有没有呢……」"
    "……克罗艾学姐穿浴衣的样子。"
    "这怎么说呢，实在叫人期待啊。"
    voice "NCL01A_KU076"
    克罗艾 "「可是男式的话……」"
    志雄 "「那个，难道我也要穿吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB03"),"True","img/CL_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU077"
    克罗艾 "「那当然了。难得的祭典嘛。」"
    志雄 "「那个，请手下留情。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB06"),"True","img/CL_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL01A_KU078"
    克罗艾 "「包在我身上～」"
    "说着，学姐开心地笑了。"
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
    show expression "img/BG01EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG01EA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC01"),"True","img/CL_MAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE08_17L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,128
    voice "NCL01A_KU079"
    克罗艾 "「那我今天就回去了。」"
    志雄 "「啊、好的。」"
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
#CHR_SCLC 0,400,400
#CHR_POSC 0,(320-140),(100)
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XAB04"),"True","img/CL_XAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320-140)/640.0
    with dissolve
#BG_BLUR 0
    voice "NCL01A_KU080"
    克罗艾 "「志雄……」"
    "脸颊上感受到柔软的嘴唇的触感。"
    hide lh0 with dissolve
#CHR_SCLC 0,256,256
#CHR_POSC 0
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA07"),"True","img/CL_LAA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "触感很快消失，映入眼帘的是克罗艾学姐的红红的脸颊。"
    voice "NCL01A_KU081"
    克罗艾 "「那明天见吧。」"
    window hide
#BG_BLUR 0
#SE_VOLC 1,255
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "克罗艾学姐说完这一句，从我手里接过购物袋，消失在检票口的人群当中。"
    志雄 "「……」"
    "而我站在原地动弹不得，唯有呆呆地目送着学姐离去的背影。"
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
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT