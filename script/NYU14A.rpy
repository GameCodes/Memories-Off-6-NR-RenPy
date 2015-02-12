label NYU14A:
    $currentlabel = "NYU14A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '08'
    $day = '01'
    $date = '2'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 3,CAL_0801
    scene expression Solid("000") with fade
    show expression "img/NIMG15D-568h@2x.jpg" as cal zorder 5
    show expression "img/08_01_TUESDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG29AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG29AA@2x.jpg" as bg0 with dissolve
    play music  "OBGM02"
#FADE_IN 1
    play sound "SE05_15L"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "截止前３０分钟……。"
    "我们成功地用自己的双手，向比赛主办方提交了参赛的广播。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「这样的话，应该算是暂时ＯＫ了吧。」"
    voice "NYU14A_KA000"
    神奈 "「没有因为睡过头而错过时间，实在是太好了。」"
    志雄 "「我可不想变成那种愚蠢的ＢＡＤ　ＥＮＤ哦……」"
    "幸好，昨天神奈早早地就被击沉了，于是今天并没有睡过头。"
    voice "NYU14A_KA001"
    神奈 "「接下来，就是等待结果了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA04"),"True","img/KA_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU14A_KA002"
    神奈 "「嗯～虽说获得优胜还是有些难度的，但我认为取得一个较好的成绩应该没什么问题吧。」"
    "关于这点，我也是同样。"
    "就算没有获得优胜……有了这次制作给予我们的巨大成就感，也不会后悔的。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    scene expression "img/BG01AA@2x.jpg" as bg0 with dissolve
#BG_SET_DEFC 0,BG01AA
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (32/32.0)
    play sound "SE05_15L"
#EFF_STAC 1,SUN_LE,EFF_SKIP
#FADE_IN 1
    志雄 "「最终……还是没能联络到结乃呢。」"
    "在去提交的路上，以及我们提交制作物的时候……"
    "神奈都在不停地给结乃打电话。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA05"),"True","img/KA_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU14A_KA003"
    神奈 "「嗯。没能见面实在是很可惜啊。」"
    "她们是难得见面的好友。肯定还是想见一面的吧。"
    志雄 "「如果我联络上她，会让她立即给神奈打电话的。」"
    "本该用来寻找结乃的重要的时间，结果却为了我消耗了不少，我非常感激神奈。"
    "但是，我不打算道歉。"
    "因为我并不后悔，相信神奈也是这么想的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU14A_KA004"
    神奈 "「差不多……到了回去的时候了。」"
    "已经过了比赛截止的时间，同时也意味着……"
    "已经到了神奈不得不回去的时候了。"
    志雄 "「这样啊。这两天的事，真是谢谢你了。」"
    "我仅仅对神奈表达了自己的感谢之情。"
    "如果……哪怕只是再多说一句……我一定会将神奈留下来的吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA03"),"True","img/KA_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU14A_KA005"
    神奈 "「嗯。虽然时间很短，但是很开心哦。」"
    "我握住神奈伸出的手。"
    "但是，我的手很快就被神奈放开了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA09"),"True","img/KA_LAA09A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU14A_KA006"
    神奈 "「继续待在这里的话，会变得舍不得分开的。」"
    "神奈的笑脸……和那天的结乃重叠了起来。"
    window hide
#BG_SET_BACK 
#BG_INIC 3
#BG_ALPC 3
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU04B")]=True
    show expression "img/EVN_YU04B@2x.jpg" as bg3 zorder 300 with dissolve
#SE_VOLC 1,0
#MUS_VOL 0
#BG_INIC 1
#BG_PRI 1
#EFF_STPC 1,EFF_SKIP
#BG_ALPC 0
#CHR_ALPC 0
#BG_ALPC 3
    hide bg1 with dissolve
    "那种抱有长久分别觉悟的，寂寞的微笑。"
    voice "NYU14A_YU000_K"
    结乃 "「再见……」"
    "结乃那天的话语好像还回响在我耳边，我甚至无法分辨那是否只是我的幻听"
    "从那时起，结乃她……已经知道会变成今天这种情况了。"
    "如果我能够早点注意到的话……一定会有一个不一样的结果吧。"
    window hide
#BG_INIC 1
#BG_PRI 1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA10"),"True","img/KA_LAA10A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    hide bg3
    with dissolve
#BG_ALPC 0
#CHR_ALPC 0
#SE_VOLC 1,64
#MUS_VOL 64
#EFF_STAC 1,SUN_LE,EFF_SKIP
    hide bg1 with dissolve
    voice "NYU14A_KA007"
    神奈 "「志雄？怎么了？」"
    志雄 "「啊，没什么。」"
    "神奈的声音把我拉回了现实。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "面前神奈的表情和平时没有什么特别的差别，我稍稍放下心来。"
    志雄 "「如果作为优秀作品被留下来了的话……公开播出的那天，你会过来吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA03"),"True","img/KA_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU14A_KA008"
    神奈 "「当然。因为志雄一个人可是什么都做不成的哦。」"
    "神奈开玩笑般地说道。"
    "当然，这句话的意思我也很明白。"
    "我和神奈，两人不凑齐的话……想要再现那个节目，是不可能的。"
    志雄 "「这样啊。那么，在那天之前，让我们暂时再见吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA02"),"True","img/KA_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU14A_KA009"
    神奈 "「嗯。再见哦！」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我目送着用力挥着手，消失在车站中的神奈。"
    "直到再也看不到对方的身影为止，我们不停地挥着手。"
    志雄 "「要是能有一个好结果就好了……」"
    "那样的话，向结乃传达思念也，和神奈的再会也……"
    "这些，如果没有一个最低限度的结果的话，都是无法开始的。"
    "在审查结果出来前，可能会失眠一段时间了吧。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
#EFF_STPC 1,EFF_SKIP
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG15NA1@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG15NA1@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    play music  "OBGM17"
#FADE_IN 1
    志雄 "「我回来了～」"
    "完成了补习课程，我回到自己的房间。"
    "为了挽回这两天荒废掉的学习，我在补习班的课上比平时更加认真。"
    "因为如果不这么做的话，脑子里就会被多余的想法占满。"
    志雄 "「真安静……」"
    "即使如此，当一个人回到家后，无论如何不愿意，我还是会想起——"
    "那个直到被睡魔击沉为止，一直在和我说话的神奈的身影。"
    "然后……还有抱着难言之隐从我面前消失的结乃。"
    志雄 "「听广播听广播……了。」"
    "离『Ｔ－ｗａｖｅ』开始还有一段时间，我打开了收音机。"
    "并非ＫＡＮＡＴＡ在说些晦涩难懂的东西，我虽然能够理解字面的意思，但其内容却完全没有进入我的脑子。"
    志雄 "「投稿……好久没做了，试试看吧。」"
    "应该一定在听着吧，结乃或者神奈。"
    "如果能够被读出来的话……多少能够传达一些我的感情吧。"
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    menu:
        "结乃，你在听吗？":
            $F7=0
        "神奈，你在听吗？":
            $F7=1
    if F7==0:
        jump L_NYU14A_SEL00_A
    if F7==1:
        jump L_NYU14A_SEL00_B
label L_NYU14A_SEL00_A:
#RSET F108
    $F108=1
    志雄 "「虽然电话不行……但这个一定是在听的吧？」"
    "现在……我能够理解结乃的想法。"
    "所以，更想再一次和她对话。"
    "就算是为了关心我们两个的神奈，也要……"
    志雄 "「完成了。发送。」"
    "作为久违的投稿，我在里面添加了只有结乃才能明白的暗号。"
    "结乃的话，一定会注意到的吧。"
    "希望这个把我们两人联系在一起的节目，能够再一次把我们联系起来。"
    "抱着这个愿望，我发出了邮件。"
    jump L_NYU14A_SEL00_X
label L_NYU14A_SEL00_B:
    志雄 "「应该已经送到了吧？」"
    "没有了制造热闹气氛的神奈，这个房间真的是十分的安静。"
    "对于一直被吵闹的家伙们包围的我来说，这个安静的房间一直是我用来获得一时安宁的场所，但现在……"
    "现在仅仅靠这种安静，我已经无法满足。"
    志雄 "「你该怎么赔偿我呀，神奈。」"
    "不仅仅是声音，心里有种重要的东西从房间里消失的感觉。"
    "胸前偏左的地方，有些隐隐作痛。"
    志雄 "「如果……你不回来的话，我不会原谅你的哦。」"
    "感谢，和对再会的期待。"
    "向着『Ｔ－ｗａｖｅ』的邮箱地址，我发出了包含着这些感情的，久违的邮件。"
    jump L_NYU14A_SEL00_X
label L_NYU14A_SEL00_X:
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