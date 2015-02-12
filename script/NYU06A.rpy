label NYU06A:
    $currentlabel = "NYU06A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '29'
    $date = '6'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 3,CAL_0729
    scene expression Solid("000") with fade
    show expression "img/NIMG15F-568h@2x.jpg" as cal zorder 5
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
    play music  "BGM06"
    play sound "SE08_17L"
#EFF_STAC 1,SUN_LE,EFF_SKIP
#FADE_IN 1
    play sound "SE05_14L"
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    voice "NYU06A_YU000"
    结乃 "「让你久等了，志雄学长。」"
    志雄 "「没有等多久哦，和平时一样的。」"
    "也许是因为昨天的事情，我的回答僵硬得连自己都觉得很别扭。"
    "意识到这点，我补偿似地对结乃笑了笑。"
    "结乃也以微笑回应我。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA04"),"True","img/YU_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU001"
    结乃 "「以前也都是在约定时间之前就碰面了呢。」"
    "我掏出手机确认，正如结乃所说，现在比约定的时间还早１０分钟。"
    "喜欢早早到达约定地点的坏习惯，看来还没改掉。"
    志雄 "（虽然，这也不是什么坏事……）"
    "如果告诉结乃这是因为给莉莉丝做仆人而养成的习惯，也太没面子了。"
    志雄 "「提前留出应对突发事件的时间可是成熟的表现啊。」"
    "对结乃先这么搪塞过去吧，今天的状态不错，可不要再找什么不合适的话题了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU002"
    结乃 "「那么，今天要去哪里呢？」"
    "明明距离比赛的投稿截止还有3天，但我们的行动却和节目制作完全扯不上关系。"
    "为了转换心情，暂时把令人烦恼的比赛抛在脑后，所以决定今天约会。"
    "其实我们并没有充足的时间用来如此浪费，不过既然已经约定好了，反悔的话是肯定不能说的。"
    "就算现在突然有了灵感，在明天商量之前也先埋在心里吧。"
    "『隔夜的灵感会更加美味』……记得有这种说法吧。"
    "如果亨听到的话，肯定会吐糟『这又不是咖喱』之类的吧。"
    "要避免昨天那种无意义的讨论，必须摆出强硬的态度，我想结乃也能理解其中的必要性吧。"
    志雄 "「嗯，要再去一次卡拉ＯＫ吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB06"),"True","img/YU_LBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU003"
    结乃 "「唉？啊……那个。」"
    志雄 "「呃……有什么问题么？」"
    "本来已经在心里计划好了的，但是结乃的回答却并不怎么干脆。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB04"),"True","img/YU_LBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU004"
    结乃 "「卡拉ＯＫ上次已经去过了，还是去没有去过的地方吧？」"
    "结乃想了一下，提出了另一个建议。"
    "当时她的语气变得客气时，一般都是为了隐藏难以启齿的真心话。"
    志雄 "「那么，该不会是想要去取材吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC04"),"True","img/YU_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU005"
    结乃 "「唉？那个，那个……」"
    "稍微试探了一下，结乃忽然慌了起来。看来，问题的根源猜对了。"
    志雄 "「今天说好了是要转换心情的吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU006"
    结乃 "「是的，转换心情。所以今天就去看看新鲜的景色吧。」"
    志雄 "「…………」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB03"),"True","img/YU_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU007"
    结乃 "「学长……？」"
    志雄 "「啊，没什么……只是在想去哪里，有没有想去的地方？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA05"),"True","img/YU_LBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    if not persistent.dictlist[41] and persistent.show_dict:
        $persistent.dictlist[41]=True
        show screen dict_pop(i=41)
    voice "NYU06A_YU008"
    结乃 "「去水族馆吧。」"
    志雄 "「早有预谋吧……竟然想都不想就回答了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU009"
    结乃 "「嗯，算是吧，之前就有想去的。」"
    voice "NYU06A_YU010"
    结乃 "「可以么，水族馆？」"
    志雄 "「真没办法呢，你想去哪里我当然都奉陪。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA02"),"True","img/YU_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU011"
    结乃 "「太好了——！那么，Ｌｅｔ＇ｓ　Ｇｏ！」"
    志雄 "「喂，都什么年代了，还用这么古老的词汇……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU012"
    结乃 "「这就叫做，『温故而知新』。」"
    志雄 "「好吧，看来你真的比我更适合去当备考生呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB02"),"True","img/YU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU013"
    结乃 "「都说流行的规律是２０年一轮回，这样的词汇今后流行回来的可能性很大哦。」"
    志雄 "「哇，那是真的么。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA02"),"True","img/YU_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU014"
    结乃 "「好了好了，Ｌｅｔ＇ｓ　Ｇｏ！Ｌｅｔ＇ｓ　Ｇｏ！」"
    "说是温故知新，但其实是固执吧。"
    "不过话说回来，都到了这个时候，她还是一个劲地在思考广播内容。"
    "『收集新的材料』，这句话大概都快变成了她的口头禅了。"
    "选择了一个没有去过的地方约会，想要到水族馆取材的小心思真是一目了然。"
    志雄 "（以现在的状态，真能转换心情么？）"
    "如果中途发现她有什么暴走倾向的话，必须抢先阻止。"
    window hide
    stop se
    stop sound
    stop music fadeout 1
#FADE_OUT 1
#EFF_STPC 1,EFF_SKIP
    scene expression Solid("000") with fade
    stop se
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG32AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG32AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,136,136
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB06"),"True","img/YU_LBB06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    pause (32/32.0)
    play music  "OBGM18"
#FADE_IN 1
    voice "NYU06A_YU015"
    结乃 "「哈～还是蛮热闹的嘛。」"
    "结乃朝管内看了看，用佩服的语气感叹道。"
    "毫不夸张的说，水族馆里的人比鱼还要多。"
    志雄 "「也到了这个季节了呢，不同于学生，对于条件不允许远足的人来说，来这里就感觉好像到了大海一样吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU016"
    结乃 "「这里是附近出名的约会场所之一吧，志雄学长来过这里么？」"
    志雄 "「哦，算是有吧……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU017"
    结乃 "「是和女孩子么？」"
    志雄 "「嗯……嗯？」"
    "如果是平时的话，结乃察觉到我的尴尬后，都不会再追问下去……但今天……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA04"),"True","img/YU_LBA04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU018"
    结乃 "「啊，我没想窥探你隐私的……」"
    "结乃自己也察觉到了这点，将视线移开。"
#SET_PRVPNT
    menu:
        "将一切都说清楚":
            $F7=0
        "找个借口搪塞过去":
            $F7=1
    if F7==0:
        jump L_NYU06A_SEL00_A
    if F7==1:
        jump L_NYU06A_SEL00_B
label L_NYU06A_SEL00_A:
    $F3+=1
    "对水族馆的印象还保留在很多年前，那时是和母亲与莉莉丝一起来的。"
    "没有必要隐瞒吧，我对结乃说出了这件事。"
    志雄 "「在小时候和母亲一起来过。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA05"),"True","img/YU_LBA05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU019"
    结乃 "「小时候？这么说的话那时远峰学姐也在一起吧？」"
    志雄 "「啊，难道说，从莉莉丝那里听说的么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU020"
    结乃 "「没—有—。女孩子的直觉，直觉啦。」"
    "结乃微笑着说道，但我总觉得，她的笑容背后好像隐藏了什么。"
    jump L_NYU06A_SEL00_X
label L_NYU06A_SEL00_B:
    $F5+=1
    志雄 "「啊，没有的，之前没有和女孩子正式的来过这种地方哦。」"
    "以往提起莉莉丝的事情，结乃的表情就会变得有些寂寞"
    "还是稍微蒙混一下比较好吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA03"),"True","img/YU_LBA03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU021"
    结乃 "「……正式是指？」"
    "结乃投来了怀疑的目光。"
    "难道说已经从莉莉丝或亨那里听到过类似的事情了吗？"
    "不过，事已至此，只能继续装傻了。"
    志雄 "「是学校集体活动的时候来的哦，那样的话就算有女孩子，也不能算作约会吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA05"),"True","img/YU_LBA05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU022"
    结乃 "「啊，集体活动……是这样啊。」"
    志雄 "「嗯，集体活动……就是这样。」"
    "显然她看穿了我的谎言。"
    "早知道，还是老实说出来比较好吧？"
    "本来就是小时候的事情，没什么大不了的，要是因为刻意隐瞒而导致更大的误会就不好了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    jump L_NYU06A_SEL00_X
label L_NYU06A_SEL00_X:
    voice "NYU06A_YU023"
    结乃 "「你说，这附近的恋人们都会到这个水族馆来约会么？」"
    志雄 "「虽然每个人的想法都不一样……但是，至少我们自己已经证明这个情况哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA02"),"True","img/YU_LBA02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU024"
    结乃 "「啊，说的也是呢，我们也来到这里了呢。」"
    "是不是每对情侣都会来水族馆先不说，但如果是这附近的高中生，多多少少会来一次这里吧？"
    "相比于其他的活动的劳民伤财，这里的入馆费，纪念品……无论哪一项都是高中生可以轻易承担的。"
    "再加上，应该没有人会刻意讨厌水族馆。"
    志雄 "「不管怎么说，这个水族馆还是相当受欢迎的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA04"),"True","img/YU_LBA04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU025"
    结乃 "「原来如此，这样的话……」"
    "结乃开始自言自语，我突然有了不好的预感，难道说……"
    志雄 "「呐，难道说，在考虑广播的事情么？」"
    stop music fadeout 132
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB06"),"True","img/YU_LBB06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU026"
    结乃 "「唉？」"
    志雄 "「在节目中用到这里的话，说不定能得到一定同龄人的支持，是不是这样想的？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB04"),"True","img/YU_LBB04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU027"
    结乃 "「啊……啊……那个。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC03"),"True","img/YU_LBC03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU028"
    结乃 "「……被志雄学长完全看透了呢。」"
    志雄 "「因为都写在你脸上了。」"
    window hide
    play music  "OBGM12"
    志雄 "「呐，今天是来转换心情的吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC05"),"True","img/YU_LBC05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU029"
    结乃 "「唉，是这样的。」"
    志雄 "「既然如此，为什么光顾着考虑广播的事情啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC01"),"True","img/YU_LBC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU030"
    结乃 "「为什么……」"
    "结乃一时语塞，但是，马上又将头抬了起来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB03"),"True","img/YU_LBB03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU031"
    结乃 "「因为，明明马上就要到截止日期了……」"
    志雄 "「我知道哦，为了重新开始，所以今天才要约会的吧？」"
    "结乃现在所做的事情完全是本未倒置。"
    志雄 "「今天不谈广播的事，不是这样说好了么？但是结乃满脑子都是取材，这样不好哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC03"),"True","img/YU_LBC03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU032"
    结乃 "「这……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC02"),"True","img/YU_LBC02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU033"
    结乃 "「这不是没办法了么……！」"
    志雄 "「……」"
    "结乃抓住我的袖子，被她那渐渐高涨的气势所压倒，我不由自主的后退。"
    voice "NYU06A_YU034"
    结乃 "「因为，没有办法了啊！」"
    voice "NYU06A_YU035"
    结乃 "「并不是到了水族馆才变成这样的，我一直在寻找广播的素材，一路上就是这么过来的。」"
    voice "NYU06A_YU036"
    结乃 "「现在，全身都被这种思考占满了。」"
    voice "NYU06A_YU037"
    结乃 "「就算志雄学长，不也是这样的么？」"
    志雄 "「……那个。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC04"),"True","img/YU_LBC04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU038"
    结乃 "「学长……」"
    "面对着不知道怎么回答她的我，结乃的视线充满了寂寞。"
    "生活的重心全部放在了广播上，要是以前在２年级的时候，肯定可以理解。"
    "只是和结乃现在相比又不尽相同。那时的我在发出投稿之前，会完整的回忆一遍一天发生的事情。"
    志雄 "（好久不投稿，已经几乎快要忘记那种感觉了。）"
    "最近忙的连投稿都不去管了，我是不是稍微有点冷静过头了。"
    "你的那份热情到底去哪了？结乃一副要哭出来的表情，好像在质问着我。"
    志雄 "「对不起，又变成这样了，我没想争论的。」"
    "听到我的回答，结乃睁大眼睛，放开了我。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC03"),"True","img/YU_LBC03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU039"
    结乃 "「对不起……我才是……」"
    "结乃的声音很消沉。"
    "带着寂寞与焦躁，还有一些悲伤。"
    "她的痛苦，重重地砸在了我心头。"
    stop music fadeout 132
    "不行……"
    "我并不是要让结乃产生这样的表情才来到这里的。"
    志雄 "「……好了，来，笑一笑。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC04"),"True","img/YU_LBC04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU040"
    结乃 "「唉？」"
    志雄 "「关于现在的事情，先放在一边。」"
    "将我与结乃之间那个『看不见的箱子』用两只手抓住，然后抬起来，放到一边。"
    "结乃的眼睛一直跟着箱子的去向。"
    "像是魔术师一瞬间让东西消失一样的张开双手，让原本就看不见的箱子消失了。"
    志雄 "「然后我们微笑着将约会继续下去吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA02"),"True","img/YU_LBA02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU041"
    结乃 "「嗤……」"
    志雄 "「哈哈……」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    play music  "BGM13"
    voice "NYU06A_YU042"
    结乃 "「啊哈哈，了解了，到明天之前先将这些放在一边吧。」"
    志雄 "「好了，那么，就把我最喜欢的那个地方告诉你吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU043"
    结乃 "「是哪里哪里？」"
    志雄 "「这边这边。」"
    "我说着向结乃伸出手，但时运不济。一家三口正好从我们两人之间穿过。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB06"),"True","img/YU_LBB06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU044"
    结乃 "「哇……！好险。」"
    "差点和小孩子撞在一起的结乃飞一般的向后退去。"
    "拜这所赐，我伸出的手并没有进入她的视线里。"
    "总觉得，伸出手的时机已经错过了，结果，我和结乃只是并肩前行。"
    "试着将落空的右手握紧，却反而感觉更加缺少了些什么。"
    志雄 "「哦，到了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU045"
    结乃 "「诶～？是哪一个啊？」"
    "我喜欢的水槽依旧在那里，一条大鱼悠闲的，摆出一副很伟大的表情在水中摇着尾巴。"
    志雄 "（哦，好怀念啊～）"
    voice "NYU06A_YU046"
    结乃 "「志雄学长，喜欢这条鱼么？」"
    志雄 "「是说喜欢好呢，还是说有意思好呢。这家伙对于我来说，还是和莉莉----？」"
    window hide
    play sound "SE02_18L"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB06"),"True","img/YU_LBB06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    "——？"
    "在我要开始解说这条鱼的瞬间，结乃的手机响了。"
    voice "NYU06A_YU047"
    结乃 "「哇，吓我一跳～」"
    window hide
    play sound "SE02_03"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC01"),"True","img/YU_LBC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU048"
    结乃 "「啊，啊，我忘了静音了，在水族馆里，使用手机没关系么？」"
    "结乃慌慌张张地看着周围，寻找着禁止使用手机的标志。"
    "虽然没看到类似的标记，但一般来说，在展品前不能使用手机应该是常识吧。"
    voice "NYU06A_YU049"
    结乃 "「喂，啊，神奈？」"
    志雄 "「哎，就这样接了啊？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB06"),"True","img/YU_LBB06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU050"
    结乃 "「诶？广播的计划？那个，现在，这个……」"
    "神奈有精神的声音，就算不把听筒贴在耳边也能听得清清楚楚。"
    "听起来是为在突然想起的点子还没被忘记前告诉结乃，再怎么说也是好心的建议。不过——"
    "结乃使用手机这件事本身，并没有任何人在意。"
    "但是，从手机里漏出来的神奈的声音比想象中的还要大。"
    "我交叉食指做了个叉的标志，放在嘴前向她示意。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC01"),"True","img/YU_LBC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU051"
    结乃 "「对不起。那个，现在我手边没有可以记录的东西……等下我会给你打过去的，对不起呢。」"
    "之后，结乃的话语里流露出些许冰冷的感觉。"
    voice "NYU06A_YU052"
    结乃 "「真的是对不起，神奈。」"
    voice "NYU06A_KA000_K"
    神奈 "「嗯。知道了知道了，那么冷静了之后在打过来吧，再见——」"
    window hide
    play sound "SE02_03"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB03"),"True","img/YU_LBB03A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU053"
    结乃 "「对不起，要遵守规矩呢。」"
    "匆匆忙忙的将手机放好，结乃对我低下头。"
    志雄 "「没什么，也没造成什么影响……神奈真的很有精神呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU054"
    结乃 "「啊哈哈，真是精神好过头了哦。」"
    "结乃的脸上浮现出苦笑。"
    "明明要将广播的事情忘记，却没想到会出这样的事。"
    "不对不对，其实根本算不上什么麻烦，和神奈探讨新点子，才是结乃现在的真心吧。"
    志雄 "「是怎么样的建议啊？就先作为参与听一下吧。」"
    "当我没经过大脑就把这句话说出去时，才突然意识到大事不妙。"
    "不出所料，结乃把我刚才的台词原样奉还。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA04"),"True","img/YU_LBA04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU055"
    结乃 "「志雄学长。今天不是要将这些事情放在一边嘛？」"
    "结乃一副得意的样子。"
    志雄 "「咳咳。这下真是失敬了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU056"
    结乃 "「不管怎么说，学长果然还是在意截止日期渐渐临近吧。」"
    "的确，结乃是最了解我的。"
    "要是说关于投稿截止日期我一点也不在意那肯定是说谎。"
    "刚才神奈的电话，比起结乃，也许我更希望她们能说完吧。"
    "但是……"
    志雄 "「再怎么说今天也只是转换心情，已经确定了好几次了吧？」"
    "在这里将今天约会的目的给忘了的话，就失去意义了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC05"),"True","img/YU_LBC05A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU057"
    结乃 "「是这样么……」"
    "结乃也和我一样吧，想马上就开始商量广播的事情。"
    志雄 "「要将约会中止，进行广播的计划吗？」"
    "……我只要这么说，我们之间的心结就能消除吧。"
    "我相信结乃也是这么期待的，并且，某种意义上，我也在等着她说出这句话。"
    "但是，另一方面，我也不想改变自己已经下定的决心。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC01"),"True","img/YU_LBC01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU058"
    结乃 "「是呢，已经得到新的点子了吧。」"
    "不对哦，结乃。快点提议现在就讨论广播的事情。"
    voice "NYU06A_YU059"
    结乃 "「志雄学长！果然还是想讨论广播的事情呢！」"
#MESEX_A M_NOA,A_CH_YU,NYU06A_YU059,"【結乃】「志雄学长！果然还是想讨论广播的事情呢！」%K%P"
    志雄 "「真没有办法呢。」"
    "这就是理想中的发展啊。"
    "但因为结乃的要求并不强烈，所以我也只能含糊地做出回答。"
    志雄 "「是那个吧，因为很难得可以和神奈一起商量商量，我是这个意思。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU060"
    结乃 "「嗯？和神奈？……嗯？」"
    "不好了，含糊的方向完全选错了。"
    "结乃的情绪好像有些低落，虽然还是微笑着，但明显因为我的话而受到了打击。"
    "今天实在是太糟糕了。"
    "志在必得的事情却没有做好，结果变成这样的恶性循环。"
    "再这样狡辩搪塞下去的话，事情只会变得更糟糕吧……"
    志雄 "「呐，还要说一些关于广播的事情，这个家伙再稍微挪开一些吧。」"
    "将刚才的『看不到的箱子』，推到更远的地方。"
    志雄 "「呐，结乃？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB02"),"True","img/YU_LBB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU061"
    结乃 "「唉？好的，没关系哦，我们走吧う」"
    window hide
    stop music fadeout 132
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "笑嘻嘻的将话题转移，结乃一如常往地走在我的身边。"
    "满脸笑容的背后，能感到她沉郁的心情。"
    "刚才还没有绝对的把握确认，现在我已经可以肯定她的真实心情了。"
    "现在结乃的心情，也是和我一样矛盾吧。"
    "打破僵局只需要一句话，只需要我们一方把那句话说出来就可以了。"
    "一边默默思考着，一边注视着鱼儿们的结乃。"
    "在她后面的我，一样一边跟随这她的脚步，一边考虑着广播的事情。"
    "突然发现，自己已经和结乃拉开了好几米的距离。"
    "在结乃察觉到之前将距离缩短，然后又慢慢地拉开……这种事情已经重复了好几次。"
    "结果，我们只是在围着水族馆兜圈子，心思完全没有放在参观和约会上，就这样熬到了闭馆时间。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG38EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG38EA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    play sound "SE05_13L"
    play music  "BGM06"
#FADE_IN 1
    "不得不承认，约会和广播的企划都没有进展……"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「肚子饿了吗？」"
    "至少吃饭的时候要开心点！我带着这份期待试着邀请结乃。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA06"),"True","img/YU_LBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU062"
    结乃 "「是的，很饿了，已经咕咕叫了。」"
    "结乃的脸上浮现出『等你这句话好久了』的表情，开心的笑容也回到了她的脸上。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA02"),"True","img/YU_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU063"
    结乃 "「要吃点什么呢？」"
    志雄 "「我想想……」"
#SET_PRVPNT
    menu:
        "放满奶酪的ＰＩＺＺＡ":
            $F7=0
        "回转寿司":
            $F7=1
    if F7==0:
        jump L_NYU06A_SEL01_A
    if F7==1:
        jump L_NYU06A_SEL01_B
label L_NYU06A_SEL01_A:
    $F3+=1
    志雄 "「放满奶酪的ＰＩＺＺＡ，怎么样？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB02"),"True","img/YU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU064"
    结乃 "「太棒了，志雄学长！」"
    志雄 "「是呢，嗯。看完这个后再去吃回转寿司得话，怎么说呢……没这心情。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA04"),"True","img/YU_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU065"
    结乃 "「的确呢。看到这么多在水里畅游的鱼儿再去吃寿司，稍微有点残酷呢。」"
    jump L_NYU06A_SEL01_X
label L_NYU06A_SEL01_B:
    $F5+=1
    志雄 "「吃回转寿司吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA04"),"True","img/YU_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU066"
    结乃 "「唉……？寿司？」"
    志雄 "「啊？不喜欢吃寿司么？」"
    voice "NYU06A_YU067"
    结乃 "「不，并不是讨厌，我很喜欢。」"
    志雄 "「那就是不想吃咯？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC03"),"True","img/YU_LBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU068"
    结乃 "「也不是了，只是，我的肚子现在特别想要放满奶酪的ＰＩＺＺＡ来填满……」"
    志雄 "「ＰＩＺＺＡ？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC01"),"True","img/YU_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU069"
    结乃 "「嗯，逛完水族馆之后立刻吃寿司的话……是不是有点太残酷了？」"
    志雄 "「……这样说的话……也是呢。」"
    "是啊，下意识地将水族馆里的鱼和寿司里的鱼联想到一起，谁也难以下口吧。"
    志雄 "「的确不能吃呢……你这么一提醒我对寿司也没什么胃口了。」"
    "水族馆的鱼儿们，真是抱歉呐。"
    jump L_NYU06A_SEL01_X
label L_NYU06A_SEL01_X:
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU070"
    结乃 "「那么，为了将ＰＩＺＺＡ塞进肚子里，我们快点走吧」"
    志雄 "「如果到时候点海鲜披萨那不是适得其反了么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB02"),"True","img/YU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU071"
    结乃 "「怎么会……这种艰巨的任务就交给志雄学长你了。」"
    志雄 "「哈，这也会被你当做材料么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU06A_YU072"
    结乃 "「做的到的话可以帮你给『我们的Ｔ－ｗａｖｅ』投稿哦。」"
    志雄 "「……真没办法呢。」"
    window hide
    stop sound
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG01NA@2x.jpg" as bg0 zorder 0 with dissolve
#FADE_IN 0
    "之后我们找到一家餐厅，没有犹豫地点了款普通的招牌ＰＩＺＺＡ。"
    "我才不会这么容易就成为投稿的材料呢。"
    志雄 "（好吧，先把这件事放在一边……）"
    "期待着能够愉快用餐的我，又一次失算了。"
    "虽然ＰＩＺＺＡ很美味，价格也合理，但问题是我们之间的对话。"
    "不知道是无意识还是刻意，我们很有默契地避开了关于广播的话题。"
    "当然节目制作的事情也没说，就连Ｔ－ｗａｖｅ的话题都没说，这在我们之间好像还是第一次。"
    "当然，广播以外的话题平平淡淡。"
    "用餐的大部分时间里，都被无言的沉默压的透不过气来。"
    "明明两个人考虑的都是同一件事，但没有人先开口打破僵局。"
    "直到我们从店里走了出来，除了时间在推进外，似乎没有获得任何进展。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU04A")]=True
    show expression "img/EVN_YU04A@2x.jpg" as bg1 with dissolve
    play music  "OBGM20"
    voice "NYU06A_YU073"
    结乃 "「今天承蒙招待了，一定会回礼的。」"
    志雄 "「嗯，这我可要好好考虑一下要什么。」"
    voice "NYU06A_YU074"
    结乃 "「……但是，轻描淡写地就将海鲜ＰＩＺＺＡ给回避掉了，这真是可惜啊。」"
    志雄 "「就这么想把我塑造成一个残酷的男人么？」"
    voice "NYU06A_YU075"
    结乃 "「果然，水族馆之后直接就是海鲜的话，心里还是有些抵抗啊。」"
    志雄 "「嗯，今天的这个经历应该可以算作教训吧。」"
    voice "NYU06A_YU076"
    结乃 "「学长……那个……」"
    voice "NYU06A_YU077"
    结乃 "「关于广播的事情……」"
    志雄 "「那个就放在明天再说吧。」"
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU04B")]=True
    show expression "img/EVN_YU04B@2x.jpg" as bg1 with dissolve
    voice "NYU06A_YU078"
    结乃 "「啊……」"
    "现在结乃的脑子里，应该正在把新的点子结合起来吧。"
    "但比起现在就商议，我希望她先回去好好整理一下思维和心绪，今天原本的目的就是这个。"
    "到了明天，所有问题肯定就会迎刃而解的。"
    "我如此坚信着。"
    志雄 "「今天，就先把广播的事情忘记吧。」"
    voice "NYU06A_YU079"
    结乃 "「……是……这样么。」"
    志雄 "「那么，明天再见。」"
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU04A")]=True
    show expression "img/EVN_YU04A@2x.jpg" as bg1 with dissolve
    voice "NYU06A_YU080"
    结乃 "「好的……」"
    stop music fadeout 116
    voice "NYU06A_YU081"
    结乃 "「别了。」"
    window hide
#FADE_OUT 1
#BG_COLC 0,128,128,128
    hide bg1 with dissolve
#FADE_IN 1
    "结乃乘坐的电车，从月台开走了。"
    "一边回忆今天所发生的事情，一边目送着电车的远去，然后从手机上确定时间。"
    "『Ｔ－ｗａｖｅ』的播放时间已经错过了。"
    "两个人在一起还错过收听『Ｔ－ｗａｖｅ』这种事，至今为止还是第一次。"
    "虽然回到房间的话也能听到录音，但我们明明都认为直播才有意义……"
    voice "NYU06A_YU082_K"
    结乃 "「别了。」"
    志雄 "「…………？」"
    志雄 "（别了……？）"
    "暮然间，我转身看向车站的检票口。"
    "当然，那里空空的，并没有结乃的身影。"
    志雄 "（我想太多了吧，不会的。）"
    "大概是因为本就焦躁的心情又遇上今天不顺利的约会，所以才会产生这种奇怪的幻觉吧。"
    志雄 "（总而言之，明天啊，明天！）"
    "到了明天的话所有事情都会顺利的。"
    "我一边祈愿着，一边迈动有气无力的双脚，向家的方向走去。"
#label QJUMP
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG15NA1@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG15NA1@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    play music  "OBGM17"
#FADE_IN 1
    志雄 "「啊……这么说来中午的时候，神奈有打过电话吧。」"
    志雄 "「好像是想到了新的点子，嗯，到底是什么样的主意呢？要不要去问一下？」"
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    menu:
        "去问":
            $F7=0
        "不去问":
            $F7=1
    if F7==0:
        jump L_NYU06A_SEL02_A
    if F7==1:
        jump L_NYU06A_SEL02_B
label L_NYU06A_SEL02_A:
    $F5+=1
#CHAT_STA
#BG_SET_BACK 
#BG_INIC 2
#BG_PRI 2
    show expression "img/NIMG14A@2x.jpg" as bg2 zorder 2
    with dissolve
    
    pause 1
#BG_HIDEC 3
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
#BG_SETWC 0,1,NIMG14C,CHAT_6A_00
#BG_COLC 0,128,128,128
    show expression "img/NIMG14C@2x.jpg" as bg0
    show expression "img/CHAT_6A_00@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"


#BG_ALP_SAVEC 0
#BG_ALP_SAVEC 1
#BG_ALPC 0
#BG_ALPC 1
    hide bg2 with dissolve
#CHAT_STR "〈神奈：〉%N欢迎回家，约会开心么?"
#WAIT_KEY 96
    show expression "img/CHAT_6A_01@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N今天好像打扰你们了，对不起。"
#WAIT_KEY 96
    show expression "img/CHAT_6A_02@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N不会的，没什么。"
#WAIT_KEY 96
#CHAT_END
    "神奈的语气似乎有些微妙，是我多心了吧？"
#CHAT_STA
    show expression "img/CHAT_6A_03@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N是我们这边不好，抱歉。是因为广播的事情才打电话来的对吧？"
#WAIT_KEY 96
    show expression "img/CHAT_6A_04@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N是的是的，那个想法刚才在电话里和结乃说过了……情况怎么样？"
#WAIT_KEY 96
    show expression "img/CHAT_6A_05@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N不好也不坏……这样的感觉吧。"
#WAIT_KEY 96
#CHAT_END
    "我毫不隐瞒地把今天发生的事情告诉了神奈，无论是作为心情转换的约会还是约会并没有成功的事情。"
    window hide
#FADE_OUT 1
    pause (32/32.0)
    show expression "img/CHAT_6A_06@2x.png" as bg_chat
#FADE_IN 1
#CHAT_STA
    show expression "img/CHAT_6A_07@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N哈～是转换心情啊。"
#WAIT_KEY 96
    show expression "img/CHAT_6A_08@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N结乃看起来好像也有新想法，明天的商讨应该会有些进展吧。"
#WAIT_KEY 96
    show expression "img/CHAT_6A_09@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N这样么，那么……志雄也什么都没有考虑？"
#WAIT_KEY 96
    show expression "img/CHAT_6A_0A@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N……是的，惭愧。"
#WAIT_KEY 96
    show expression "img/CHAT_6A_0B@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N…………"
#WAIT_KEY 96
    show expression "img/CHAT_6A_0C@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N别无语啊，是我不好啦。我现在正打算要考虑的……"
#WAIT_KEY 96
#CHAT_END
    "平时都是一直说个不停的神奈，一下子沉默起来，感觉很恐怖。"
#CHAT_STA
    show expression "img/CHAT_6A_0D@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N不是啊，我并不是指这个。"
#WAIT_KEY 96
    show expression "img/CHAT_6A_0E@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N嗯？"
#WAIT_KEY 96
    show expression "img/CHAT_6A_0F@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N怎么说呢，我觉得你们两个人的话好像没有交集，这样下去没问题吧……"
#WAIT_KEY 96
    show expression "img/CHAT_6A_10@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N诶？"
#WAIT_KEY 96
    show expression "img/CHAT_6A_11@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N在听她说话的时候，总觉得气氛有些微妙的错位。"
#WAIT_KEY 96
#CHAT_END
    志雄 "「…………」"
    "这次，轮到我开始无言以对了。"
#CHAT_STA
    show expression "img/CHAT_6A_12@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N啊，对不起，不是的，并不是什么奇怪的意思……"
#WAIT_KEY 96
#CHAT_END
    "神奈慌慌忙忙解释的态度，反而让我的不安又加重了。"
#CHAT_STA
    show expression "img/CHAT_6A_13@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N是这样的么？"
#WAIT_KEY 96
#CHAT_END
    "神奈比任何人更了解我们，比任何人都理解我们，又是我们最好的后援。"
    "连她都如此担心，我们的事态真的已经如此严重了么？"
    window hide
#BG_ERSWC 2,3,BG_NOFADE
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU04B")]=True
    show expression "img/EVN_YU04B@2x.jpg" as bg2 zorder 2 with dissolve
    stop music fadeout 116
#BG_INIC 3
#BG_PRIC 3
#BG_ALPC 0
#BG_ALPC 2
#BG_ALPC 1
    hide bg3 with dissolve
    结乃 "「别了。」"
#SCRMODE_SPC SCR_FULL
#MESA A_CH_YU,NYU06A_YU083_K,"【結乃】%S001%n%n%n%n%n%n%n%S060%FS%LC%t018「别了。」%LE%FE%K%O016"
    window hide
#SCRMODE_SPC SCR_WINDOW
#BG_INIC 3
#BG_PRIC 3
#BG_ALPC 1
    hide bg2 with dissolve
#BG_ALPC 0
    hide bg3 with dissolve
#BG_PRIC 3
    "讨厌的场景一闪而过。"
    志雄 "（今天真是不行啊，怎么总是往坏的方向想。）"
#CHAT_STA
    show expression "img/CHAT_6A_14@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N那个，志雄？"
#WAIT_KEY 96
#CHAT_END
    "被神奈叫住名字，我回过神来。"
#CHAT_STA
    play music  "OBGM17"
    show expression "img/CHAT_6A_15@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N别这么悲观困惑啊，没关系的，你们两个人的事情，有我看着，一定会平安的啦！"
#WAIT_KEY 96
#CHAT_END
    "从她的话中，刚才的那种话里有话的感觉消失了。"
#CHAT_STA
    show expression "img/CHAT_6A_16@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N那真是麻烦你了。"
#WAIT_KEY 96
    show expression "img/CHAT_6A_17@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N要加油啊，因为我很期待哦，你们两人的广播。"
#WAIT_KEY 96
#CHAT_END
    "我知道，她真的是从心底里担心着我们。"
    "现在的我，对她的担心感到很高兴。"
    "为了答复她的这份心意，明天一定要好好努力。"
    "离截止日没有几天了。"
#CHAT_STA
    show expression "img/CHAT_6A_18@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N好的，绝对会成功。"
#WAIT_KEY 96
    show expression "img/CHAT_6A_19@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N嗯，就是这样，就是这样～♪"
#WAIT_KEY 96
#CHAT_END
    jump L_NYU06A_SEL02_X
label L_NYU06A_SEL02_B:
    $F3+=1
    志雄 "「算了，明天直接问问结乃就好了……」"
    志雄 "「今天也很晚了，就不要再打扰她了吧。」"
    jump L_NYU06A_SEL02_X
label L_NYU06A_SEL02_X:
    if F3>=F5:
        $F16=4
    else:
        $F16=6
#IF F20>=F22, GOTO L_NYU06A_NEXT_END
#RSET F16
label L_NYU06A_NEXT_END:
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
