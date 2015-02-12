label NSU18A:
    $currentlabel = "NSU18A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '30'
    $date = '0'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG66NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG66NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC06"),"True","img/SU_LCC06A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
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
#SE_VOLC 1,64
    "我推着自行车，和推着摩托车的铃并肩行走。"
    "虽然真的很想和她换一下，但铃一句自己应付的来便拒绝了我。"
    "不过因为是下坡路，倒也不是太大的负担。"
    志雄 "「……」"
    voice "NSU18A_SU000"
    铃 "「……」"
    "两个人一言不发走在山路上。"
    "明明有那么多想说的话，但因为不知道该说些什么好，索性就这样一直沉默下去。"
    "我也好，铃也好……或许都是相同的心情……"
    志雄 "「啊……」"
    "在道路一侧，可以看到灯光映照着的小路。"
    "小路……莫非稻穗所说的露天浴池，就是这里？"
    志雄 "「喂，铃」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC01"),"True","img/SU_LCC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU18A_SU001"
    铃 "「怎么？」"
    志雄 "「带着毛巾吗？」"
    voice "NSU18A_SU002"
    铃 "「毛巾？擦汗用的倒是带了几块」"
    "这样应该可以……吧？"
    志雄 "「这条路的前面，有个露天浴池，要不要去一下？」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC05"),"True","img/SU_LCC05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU18A_SU003"
    铃 "「露天浴池？有这样的地方？」"
    志雄 "「嗯」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC02"),"True","img/SU_LCC02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU18A_SU004"
    铃 "「……嗯，可以啊」"
    "尽管给了肯定的答案，不过听上去相当疲惫，声音有点虚弱。"
    志雄 "「那就走吧」"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG67NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG67NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC02"),"True","img/SU_LCC02A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
#SE_VOLC 1,64
#FADE_IN 1
    play music "BGM11"
    "就如稻穗所言，进入小路稍走一段后，我们看到一栋很小的房子。"
    志雄 "「就是这了」"
    "似乎比想像的要小一些，不禁有些不安。但既来之则安之……"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC04"),"True","img/SU_LCC04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU18A_SU005"
    铃 "「这个时间，随便用也没关系吧」"
    志雄 "「肯定没问题的」"
    voice "NSU18A_SU006"
    铃 "「呼」"
    "将摩托车和自行车停在小屋的一侧后，我望向小屋里面。"
    "小屋中有简单的门槛，将男女的更衣场所分开。"
    志雄 "「嗯，好像没什么问题，也没有其他人」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU18A_SU007"
    铃 "「就像是包场一样，真好呢。那好，我们进去吧」"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG99NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG99NA@2x.jpg" as bg0 with dissolve
#SE_VOLC 1,64
#EFF_STAC 0,YUGE,EFF_SKIP
#FADE_IN 1
    "从更衣室里面的出口出去，出现在眼前的是岩石围成的露天浴池。"
    志雄 "「原来是天然的露天浴池啊」"
    "洗澡的地方很小，后面便是岩石围成的露天温泉。"
    "用木板做成简单的屏风，将周围环抱起来。"
    "到底是在山上，光着身子还是感觉有些寒冷。"
    "一直这样看下去也不是办法，我简单冲洗了下后，就钻进了温泉中。"
    play sound "SE03_77"
    "一口气将身体浸到及肩的位置，用热水洗着脸。"
    "温泉水稍微有些烫，可以有效舒缓身体的疲劳。"
    志雄 "「啊……」"
    "环视周围，从没有屏风的地方，可以看到远处的海。"
    志雄 "「白天的话，景色会很好吧」"
    "晚上无法看清楚虽然有点遗憾，但山脚下街上的亮光还是可以隐约看到，这般景致也是不错的。"
    stop music fadeout 1
    志雄 "「诶？」"
    "不经意地环视了一下浴池，感觉到有种不协调的感觉。"
    "温泉只有一个，男浴池和女浴池并没有分隔开来。"
    "我慌忙往小屋方向看去……"
    志雄 "「莫非，男浴池和女浴池是在同一个地方！？」"
    "这样的话，难道是……混浴吗！？"
    "稻穗啊～！这么重要的事怎么也不告诉我！"
    voice "NSU18A_SU008"
    铃 "「哎～！这不是混浴吗！」"
    "铃终于发现了这点，她的声音从更衣室传出来。"
    window hide
    play sound "SE00_49"
    voice "NSU18A_SU009"
    铃 "「志雄～！这是怎么回事！？」"
    志雄 "「啊，对不起！之前并不知道，我只听说是露天的浴池！」"
    "虽然铃那里看不到我，我却还是拼命点头辩解道。"
    voice "NSU18A_SU010"
    铃 "「真的吗～？」"
    志雄 "「是真的啊！」"
    voice "NSU18A_SU011"
    铃 "「真是的，这么重要的事也不说。说起来，是谁告诉你的呢？」"
    志雄 "「是、是稻穗他……」"
    voice "NSU18A_SU012"
    铃 "「那、那家伙……」"
    "对不起，稻穗。我会为你收尸的！"
    "我在心里，向着穿着工作服的稻穗双手合十。"
    志雄 "「抱、抱歉……那回去吧？」"
    voice "NSU18A_SU013"
    铃 "「……志雄，已经进去了吧？」"
    志雄 "「嗯」"
    voice "NSU18A_SU014"
    铃 "「……等等」"
    志雄 "「诶？怎么了？」"
    voice "NSU18A_SU015"
    铃 "「稍微闭一下眼睛！」"
    window hide
#SE_VOLC 1,255
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09A")]=True
    
#BG_COLC 2,0,0,0,128
#FADE_IN 0
    "我听话地闭上眼睛。"
    "诶？难道，铃要进来吗？"
    voice "NSU18A_SU016"
    铃 "「要一直闭着眼睛，直到我说可以为止」"
    志雄 "「知、知道了……」"
    play sound "SE03_78"
    "透过轻微的水声以及水流的触感，我知道铃已经走进来了。"
    志雄 "「……我说」"
    voice "NSU18A_SU017"
    铃 "「啊，还不行！」"
    志雄 "「是」"
    voice "NSU18A_SU018"
    铃 "「嗯……可以睁开了」"
    window hide
    show expression "img/EVN_SU09A@2x.jpg" as bg2 zorder 2 with dissolve
#FADE_OUT 0
#BG_COLC 2,128,128,128,128
#BG_FLG EVN_SU09A0
#EFF_STAC 0,YUGE,EFF_SKIP
#SE_VOLC 1,(64/2)
#FADE_IN 1
    play music "BGM13"
    "睁开眼睛后，我看到在浴池的另一侧，是用毛巾裹到胸部，蜷缩着身体在玩水的铃。"
    voice "NSU18A_SU019"
    铃 "「喂，不要光往这边看啊」"
    志雄 "「啊，对不起」"
    "慌忙之间想把视线移开，却怎么也做不到。"
    "不由自主地偷偷向铃那边瞄去。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09D")]=True
    show expression "img/EVN_SU09D@2x.jpg" as bg2 with dissolve
#BG_FLG EVN_SU09D0
    voice "NSU18A_SU020"
    铃 "「这、这么好的浴池，只供志雄享用的话，实在太狡猾。而且，刚刚一直推着摩托车，已经浑身是汗了」"
    "尽管有些结巴，铃仍然是那么快言快语。"
    "虽然感觉这样子的她很可爱，不过这句话还是先不说了。"
    "算了，换个话题吧。"
    志雄 "「天上，星星很漂亮啊」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09B")]=True
    show expression "img/EVN_SU09B@2x.jpg" as bg2 with dissolve
#BG_FLG EVN_SU09B0
    voice "NSU18A_SU021"
    铃 "「嗯，真的啊……」"
    window hide
#EFF_PRI 0
    show expression Solid("000") as bg1 with ImageDissolve("img/BG_MASK03_1@2x.png",1)
    hide bg2 with dissolve
    show expression "img/NIMG01D2@2x.png" as bg0 zorder 0 with dissolve
#EFF_STAC 0,YUGE4,EFF_SKIP
#EFF_STAC 1,STAR,EFF_SKIP
#SE_VOLC 1,128
    hide bg1 with dissolve
    "抬头望去，看见的是一片布满星星的天空。"
    "明明离开澄空还没多远，眼前的星空却是完全不同的感觉。"
    play sound "SE07_17"
    voice "NSU18A_SU022"
    铃 "「……」"
    志雄 "「……」"
    window hide
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#EFF_STPC 1,EFF_SKIP
    pause (32/32.0)
#FADE_IN 0
    "就这样过了很久，我们两人静静地一边欣赏着夜空和夜景，一边享受着温泉。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09A")]=True
    show expression "img/EVN_SU09A@2x.jpg" as bg0 zorder 0 with dissolve
#EFF_STAC 0,YUGE,EFF_SKIP
    pause (32/32.0)
#SE_VOLC 1,(64/2)
#FADE_IN 1
    voice "NSU18A_SU023"
    铃 "「志雄……我说」"
    志雄 "「怎么了？」"
    voice "NSU18A_SU024"
    铃 "「今天的事，对不起」"
    志雄 "「我也该道歉」"
    voice "NSU18A_SU025"
    铃 "「不，志雄生气是情有可原的。我该早点意识到骑摩托车的危险性」"
    志雄 "「我也有错。我……并不是担心我自己，而是在担心铃。但说出口的，却是我的生命如何重要的话……」"
    voice "NSU18A_SU026"
    铃 "「我知道的，谢谢」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09C")]=True
    show expression "img/EVN_SU09C@2x.jpg" as bg0 with dissolve
#BG_FLG EVN_SU09C0
    voice "NSU18A_SU027"
    铃 "「我自己呢，看来还不习惯被被人担心。说是自己的问题自己来解决，不由得较起了劲」"
    voice "NSU18A_SU028"
    铃 "「还有后来，说是学生就怎样之类的话也要和你道歉。对不起」"
    志雄 "「啊哈哈哈哈，那些话也没有错啊」"
    "事实上，我确实也还是孩子。"
    "通过这次的旅行，才深切地感受到这点。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09A")]=True
    show expression "img/EVN_SU09A@2x.jpg" as bg0 with dissolve
    voice "NSU18A_SU029"
    铃 "「不是这样的。话语的正确与否，并不是谁对谁说，而是由说话的内容所决定的。由此看来，志雄的话是对的」"
    志雄 "「不过，我也确实说过了头，像个孩子似的。对不起」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09C")]=True
    show expression "img/EVN_SU09C@2x.jpg" as bg0 with dissolve
    voice "NSU18A_SU030"
    铃 "「不过，才发觉已经很久没有听过志雄这样的真心话了」"
    志雄 "「是呢。单纯是感情用事的发泄吧」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09A")]=True
    show expression "img/EVN_SU09A@2x.jpg" as bg0 with dissolve
    "对于我的话，铃不由得苦笑了一下。"
    voice "NSU18A_SU031"
    铃 "「志雄呀，该说你是个好人呢，还是说你不够成熟呢，总是自顾自地说话的感觉」"
    "或许是这样没错。只是，那是……"
    志雄 "「想早点成为大人……因为，想配得上铃」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09B")]=True
    show expression "img/EVN_SU09B@2x.jpg" as bg0 with dissolve
    voice "NSU18A_SU032"
    铃 "「呵呵。我也得相当努力了，不想就这么简单能让人配得上呢」"
    志雄 "「啊，又是这样，突然就摆出一副大人的架子」"
    voice "NSU18A_SU033"
    铃 "「……不过，你这样想的话我很高兴。我……对现在的志雄，非常地……」"
    志雄 "「？」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09D")]=True
    show expression "img/EVN_SU09D@2x.jpg" as bg0 with dissolve
    voice "NSU18A_SU034"
    铃 "「非常地喜……」"
    "……喜？"
    voice "NSU18A_SU035"
    铃 "「喜……在意啊！」"
    "『喜』到底跑到哪去了……"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09A")]=True
    show expression "img/EVN_SU09A@2x.jpg" as bg0 with dissolve
    voice "NSU18A_SU036"
    铃 "「啊，抱歉……」"
    "铃把脸浸在水里吐起泡泡。"
    "这个人啊，该说她是个大人呢，还是个孩子呢……"
    "不过……"
    志雄 "「现在，这样就足够了」"
    voice "NSU18A_SU037"
    铃 "「怎么变成这个样子……抱歉」"
    志雄 "「不用太在意的」"
    voice "NSU18A_SU038"
    铃 "「或许是因为还不习惯吧？不知为何就在这种气氛下，说些多余的话，还开起玩笑……并不是在刻意地逃避志雄」"
    志雄 "「嗯」"
    voice "NSU18A_SU039"
    铃 "「再稍微等一下……」"
    志雄 "「嗯。我可是很有耐性的呢」"
    voice "NSU18A_SU040"
    铃 "「是吗？」"
    "心与心的隔阂，似乎被温泉水融化了。"
    "我抱着坦诚的心情，面向了铃。"
    志雄 "「对了……可以问一些基本的事情吗？」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09B")]=True
    show expression "img/EVN_SU09B@2x.jpg" as bg0 with dissolve
    voice "NSU18A_SU041"
    铃 "「基本的？」"
    志雄 "「铃为什么会骑摩托车？」"
    voice "NSU18A_SU042"
    铃 "「说到为什么，是因为喜欢吧」"
    志雄 "「是因为喜欢吗？对摩托车感兴趣的女生，身边还真没有见过」"
    "旅行途中也有不少人骑着摩托车，不过并没有发现女生。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09A")]=True
    show expression "img/EVN_SU09A@2x.jpg" as bg0 with dissolve
    voice "NSU18A_SU043"
    铃 "「……为什么会这么问呢」"
    志雄 "「因为我很想知道铃所执着的那些事情」"
    voice "NSU18A_SU044"
    铃 "「唔……唔……」"
    "铃低声呢喃着什么。是这么不好意思的事情吗？"
    voice "NSU18A_SU045"
    铃 "「这么想知道吗？」"
    志雄 "「如果可以的话……」"
    voice "NSU18A_SU046"
    铃 "「不、不是太有趣的事哟？」"
    志雄 "「那就请讲吧」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09C")]=True
    show expression "img/EVN_SU09C@2x.jpg" as bg0 with dissolve
    voice "NSU18A_SU047"
    铃 "「是以前的事了……上高中的时候，有个喜欢的人」"
    "以年龄的差距为理由甩掉铃的那个人。是她的老师吧……？"
    voice "NSU18A_SU048"
    铃 "「那个人喜欢摩托车。为了能说上话，哪怕被甩也想有所交集，于是去考取了驾照」"
    志雄 "「……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09A")]=True
    show expression "img/EVN_SU09A@2x.jpg" as bg0 with dissolve
    voice "NSU18A_SU049A"
    铃 "「当然了，现在骑车是因为自己喜欢」"
    voice "NSU18A_SU049B"
    铃 "「自己来驾驶，有种运动的感觉。气味和光线等信息能直接地传达给我，感觉非常棒……」"
    志雄 "「嗯。我能了解那种驾驶的快感」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09C")]=True
    show expression "img/EVN_SU09C@2x.jpg" as bg0 with dissolve
    voice "NSU18A_SU050"
    铃 "「还有就是因为我在写东西啊。有时候会有一种，故事在脑子里结束了，这样的缺乏真实感的时候」"
    voice "NSU18A_SU051"
    铃 "「害怕失去这份真实感，于是让摩托车浸入了身体里」"
    志雄 "「呵呵呵呵，这才像铃啊。不过，如果可以的话不要这么隐藏着比较好吧」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09A")]=True
    show expression "img/EVN_SU09A@2x.jpg" as bg0 with dissolve
    voice "NSU18A_SU052"
    铃 "「现在姑且不说，从一开始的契机上看有些没出息，可能是因为有些留恋吧」"
    "明明不需要在意的啊，不如说是感觉很可爱。"
    "算了，说了的话，也许又会生气吧。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09D")]=True
    show expression "img/EVN_SU09D@2x.jpg" as bg0 with dissolve
    voice "NSU18A_SU053"
    铃 "「啊……这种话志雄还是头一次说呢」"
    志雄 "「这样很好啊。话说回来，也很久没这么认真地交谈了呢」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09B")]=True
    show expression "img/EVN_SU09B@2x.jpg" as bg0 with dissolve
    voice "NSU18A_SU054"
    铃 "「嗯。谢谢」"
    志雄 "「……？」"
    voice "NSU18A_SU055"
    铃 "「没什么」"
    志雄 "「那么，再多说些其他事吧」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU09C")]=True
    show expression "img/EVN_SU09C@2x.jpg" as bg0 with dissolve
    voice "NSU18A_SU056"
    铃 "「是啊……」"
    "今天，感觉与以往相比，与铃变得亲近了。"
    "光是普普通通地去享受旅行，或许也是做不到现在这样的吧。"
    "正是因为吵架了，才能变成这样啊。"
    "最后还是被稻穗言中了……"
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