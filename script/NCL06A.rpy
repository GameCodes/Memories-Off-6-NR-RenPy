label NCL06A:
    $currentlabel = "NCL06A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '08'
    $day = '03'
    $date = '4'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    #show expression "img/BG_BLACK@2x.jpg" as bg0 zorder 0 with dissolve
#FADE_IN 0
    play music "BGM14"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "久违的做了个梦。"
    "在一座从来没有见过的大宅子里，摆着一张桌子。"
    "周围虽然坐着许多人，大家都围着桌子聊天、游戏，只有我一个人被孤立在一边。"
    "这时，从旁边伸过来一只手，把一张纸放在了我的面前。"
    "我很在意就伸手去拿，结果发现是打印出来的『志愿调查表』……"
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 5,CAL_0803
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 1
#BG_SETWC 0,1,BG15MA,NIMG03A
    scene expression "img/BG15MA@2x.jpg" as bg0 with dissolve
    play sound "SE03_09L"
    pause (32/32.0)
#MUS_VOL 128
#FADE_IN 1,128
    "瞬间惊醒，眼前依旧是熟悉的天花板。"
    "同时仿佛有听起来心情很好的『咚咚』的切菜声环绕在耳边。"
    "竟然连梦里都是志愿的事情，还真是不可想象啊。"
    志雄 "「我想要做的事情……」"
    "我一边嘟囔着，一边靠着不完全清醒的意识摸索着，把闹钟拿了起来。"
    志雄 "「那个……」"
    "现在的时间是８点２６分。"
    "要是在上学的日子，这已经是注定会迟到的时间了。"
    stop se
    志雄 "「还真是变成夜猫子了……」"
    "一直这样下去的话，开学之后就麻烦了。还是注意调整一下作息，早点恢复到原来的样子吧……"
    window hide
    play sound "SE00_08"
    hide bg1 with dissolve
    "就在我考虑这些事的时候，有人敲了敲我的房门。"
    window hide
    stop music fadeout 1
    play sound "SE00_05"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA01"),"True","img/CL_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL06A_KU000"
    克罗艾 "「志雄，已经起来了吗？」"
    志雄 "「咦？」"
    "看着进到我房间里的克罗艾学姐，我不禁惊讶地叫出声来。"
    志雄 "「学姐，你为什么会在这里！？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA05"),"True","img/CL_MAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU001"
    克罗艾 "「看来还没清醒呢……」"
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
    "这才想起来，两天前学姐就住到我家里来了。"
    if not persistent.dictlist[10] and persistent.show_dict:
        $persistent.dictlist[10]=True
        show screen dict_pop(i=10)
    "我让学姐住在以前父母住的房间。"
    if not persistent.dictlist[11] and persistent.show_dict:
        $persistent.dictlist[11]=True
        show screen dict_pop(i=10)
    "情况和第一次住在一起的时候大不相同了，作为备考生，熬夜是家常便饭。"
    if not persistent.dictlist[12] and persistent.show_dict:
        $persistent.dictlist[12]=True
        show screen dict_pop(i=12)
        
    "好在，老爸和香里阿姨现在住在蓝之丘，应该不会突然回到这里了。"
    if not persistent.dictlist[26] and persistent.show_dict:
        $persistent.dictlist[26]=True
        show screen dict_pop(i=26)
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA01"),"True","img/CL_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "BGM10"
    志雄 "「早上好，克罗艾学姐。」"
    voice "NCL06A_KU002"
    克罗艾 "「嗯，早上好。早饭马上就做好了～」"
    志雄 "「抱歉，都没有去帮忙……」"
    voice "NCL06A_KU003"
    克罗艾 "「没关系的，是我自己打算晚点叫志雄起来的……」"
    "说到这里，学姐的脸上浮现出了害羞的笑容。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA07"),"True","img/CL_MAA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU004"
    克罗艾 "「……能像这样看着你起床，感觉很开心呢～」"
    志雄 "「是，是那样吗？」"
    "迷迷糊糊的意识一下就清醒过来。而且相比意识，浑身上下更是充满了一种很棒的感觉。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB04"),"True","img/CL_MAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU005"
    克罗艾 "「那我就在客厅里等着你了～」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE00_01"
    "学姐留下我在房间里，匆匆忙忙地返回了客厅。"
    志雄 "「感觉还不错呢。」"
    "克罗艾学姐在我家住下这种事，想想也只有奏云祭那个时候了。"
    "换句话说，是学姐在和我正式交往之后第一次住在我家。这两天的经历，让我有了很特别的感觉。"
    志雄 "「我还真是多愁善感呢啊……」"
    "我不禁拍了拍自己的脸，借此来安定住自己躁动的心情。"
    "想想学姐住到我家来的经过和理由，根本就不是能让人高兴的事情。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG33AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG33AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    "洗漱完毕，桌子上已经摆满了克罗艾学姐亲手做的料理。"
    show expression "img/EXBG09A@2x.jpg" as bg_over zorder 5
    show expression "img/CL_ZAB01A@2x.png" as lh0 zorder (10+0):
        xcenter ((320)/640.0)
    with dissolve
    voice "NCL06A_KU006"
    克罗艾 "「开始吃早饭吧。」"
    志雄 "「那我开动了。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB02"),"True","img/CL_ZAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU007"
    克罗艾 "「我开动了。」"
    "我和学姐对着姗姗来迟的早饭拿起筷子。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB04"),"True","img/CL_ZAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU008"
    克罗艾 "「喂，志雄……」"
    志雄 "「怎么了？」"
    voice "NCL06A_KU009"
    克罗艾 "「我不请自来，还那么突然，是不是给你添麻烦了？」"
    "听到克罗艾学姐这样说，我不由得一愣。"
    志雄 "「我倒没什么……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB05"),"True","img/CL_ZAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU010"
    克罗艾 "「但是，这就完全像是，我一有什么事情就逃到志雄这里的样子……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC03"),"True","img/CL_ZAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "说着，学姐低下了头。"
    志雄 "「才没有那回事呢。多亏了学姐能够住到我家来，你看，还要麻烦你给我做早餐……」"
    voice "NCL06A_KU011"
    克罗艾 "「嗯……」"
    "学姐无精打采地点着头。"
    "学姐来了之后给我很大帮助倒是实话，而且只要学姐待在这里我就很高兴了。不过，显然这并不是她真正的心结所在。"
    "但是，让学姐这样继续下去的话……"
    志雄 "「对了！　学姐，其实我有个请求！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC05"),"True","img/CL_ZAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#REEK_CHR 0
    voice "NCL06A_KU012"
    克罗艾 "「咦？」"
#REMOVE_REEK_CHR 0
    "我尽可能地提高了声音。被我稍稍吓到的学姐，抬起了低着的头。"
    志雄 "「难得的机会，能教教我功课吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB03"),"True","img/CL_ZAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU013"
    克罗艾 "「功课？」"
    志雄 "「对。有些弄不懂的地方。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB06"),"True","img/CL_ZAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU014"
    克罗艾 "「嗯，当然可以……」"
    "学姐接受了我的请求。"
    "克罗艾学姐学习要比我好很多，并且去年的考试中也取得了相当优异的成绩。"
    "学姐来辅导我学习是再合适不过的了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU015"
    克罗艾 "「不过，今天要去打工的地方替班哦，所以估计也没有多少时间呢……」"
    志雄 "「一会儿就足够了。谢谢学姐～」"
    "就这样，克罗艾学姐辅导我学习这件事定了下来。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 2
##BG_POSC 0,(60),0,640,448
    show expression "img/EXBG10AA@2x.png" as bg0 zorder 0 with dissolve
    pause (32/32.0)
#FADE_IN 1
    "吃完早饭之后，等不及收拾完餐具，我就立刻就把参考书摊在了桌子上，接受学姐的个人授课。"
    voice "NCL06A_KU016"
    克罗艾 "「……这两个在不同直线上的点是同一个点，所以，答案是在Ｘ轴上有交点的任意两条直线哦。」"
    志雄 "「原来是这样！」"
    voice "NCL06A_KU017"
    克罗艾 "「啊，这个地方答错了」"
    志雄 "「咦？　哪里？」"
    voice "NCL06A_KU018"
    克罗艾 "「你看，是这里。右面那页的第二问哦」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,640
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC01"),"True","img/CL_ZAC01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR0 128,(320+224)
#MOV_CHR_GO 1
    "学姐的手指伸了过来，同时身体也向我这边靠过来。"
    志雄 "「噗！」"
    "由于克罗艾学姐的脸突然间就贴到我的面前，我的心脏一阵狂跳。"
    voice "NCL06A_KU019A"
    克罗艾 "「是这里的问题呢——{w=4}{nw}"
#MESA A_CH_KU,NCL06A_KU019A,"【クロエ】「是这里的问题呢——"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC04"),"True","img/CL_ZAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU019B"
    extend "喂？　你在听吗？」"
    志雄 "「嗯，在，在听……」"
    "学姐头发散发出来的香气让我心跳加速，我努力控制自己把精神集中在参考书上。"
    "不过，不管我怎么努力，心神都会再次被学姐飘逸的秀发给打乱。"
    voice "NCL06A_KU020"
    克罗艾 "「怎么了？」"
    志雄 "「不好意思，好像精神有些集中不了……」"
    "不得已之下，我只好如实说道。"
    "学姐看了看墙上的表，从开始学习已经过了两个小时了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC01"),"True","img/CL_ZAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU021"
    克罗艾 "「是呢，那就稍微休息下吧……」"
    window hide
    play sound "SE03_30"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC01"),"True","img/CL_ZAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with move
    with vpunch
#MOV_CHR_INIT 24
#MOV_CHR0 ,(320+96)
#MOV_CHR_GO 1
#QUA3_ALL 
    "说着，学姐突然地抱住了我。"
    志雄 "「喂，学姐！？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB06"),"True","img/CL_ZAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU022"
    克罗艾 "「休息，休息～♪」"
    "学姐一副很高兴的表情，紧紧地贴在我的胳膊上。"
    "这个样子，简直就像是猫咪在蹭着主人玩耍一样，让人好想伸手去摸摸头。"
    志雄 "「这只猫还真大呢」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB03"),"True","img/CL_ZAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU023"
    克罗艾 "「……猫？」"
    "被胳膊上传来的柔软触感所动摇，我不禁把脑中所想的事情说了出来。"
    "听到我的嘟囔，克罗艾学姐做出一副惊讶的表情。"
    志雄 "「啊，没什么，自言自语哦。自言自语～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB05"),"True","img/CL_ZAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "我为了掩饰，啪嗒啪嗒地翻着手边的参考书。"
    play sound "SE03_29"
    "就在这时，参考书里夹着的纸张轻轻飘落下来。"
    window hide
    hide lh0 with dissolve
#CHR_POSC 0,(320+224)
    pause (32/32.0)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB03"),"True","img/CL_ZAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU024"
    克罗艾 "「这是什么？　『志愿调查表』……？」"
    stop music fadeout 1
    "瞬间，脑中嗡地响了起来，完全被混乱所占据。"
    志雄 "「那个是，呃……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC01"),"True","img/CL_ZAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU025"
    克罗艾 "「我一年前也写过这个呢。说起来，志雄打算考哪里的大学？」"
    "我以后打算怎样。学姐的意思是在问我这个。"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "还没有决定":
            $F7=0
        "和学姐上同一所大学":
            $F7=1
        "毕业之后直接工作":
            $F7=2
    window hide
    play music "BGM13"
    if F7==0:
        jump L_NCL06A_SEL00_A
    if F7==1:
        jump L_NCL06A_SEL00_B
    if F7==2:
        jump L_NCL06A_SEL00_C
label L_NCL06A_SEL00_A:
    志雄 "「虽然打算继续上学，不过还没有考虑好……」"
    jump L_NCL06A_SEL00_X
label L_NCL06A_SEL00_B:
    志雄 "「可以的话，希望能和学姐上同一所大学。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB06"),"True","img/CL_ZAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06X_KU000"
    克罗艾 "「咦？　真的吗？」"
    "听到我的话，学姐很高兴地问道。看到学姐的样子，我从心底里感到高兴。"
    "所以，接下来的话要怎样说才能让学姐接受呢，我心里感觉很害怕。"
    志雄 "「不过，我却看不到未来……而且真的已经到了必须要决定未来道路的时候了……」"
    jump L_NCL06A_SEL00_X
label L_NCL06A_SEL00_C:
    志雄 "「事实上，我打算高中一毕业就去工作。感觉已经学不下去了……」"
    "我用开玩笑的语气打着马虎眼。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC05"),"True","img/CL_ZAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#REEK_CHR 0
    voice "NCL06X_KU001"
    克罗艾 "「是吗？要工作……啊。那个，有目标了吗？」"
#REMOVE_REEK_CHR 0
    "果然，就算是学姐也会感到惊讶的……咦？"
    志雄 "「呃，目标？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC01"),"True","img/CL_ZAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06X_KU002"
    克罗艾 "「还没有吧？　不过也是呢。如果可以的话，志雄要不要试着去父亲的公司工作？　当然的，面试还是要进行的！」"
    志雄 "「啊，不，那个……」"
    "……咦？　学姐好像是在十分认真地考虑这件事。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC03"),"True","img/CL_ZAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06X_KU003"
    克罗艾 "「嗯……志雄还是未成年人，既然没有就业经验我觉得还是从打工开始积累比较好……接下来会往上升到什么地方，就看志雄自己的努力了……」"
    志雄 "「那个，学姐……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC01"),"True","img/CL_ZAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06X_KU004"
    克罗艾 "「不过，志雄如果认真的话，我觉得这些都不成问题的！」"
    window hide
#MUS_VOL 0
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    志雄 "「啊～十分抱歉！」"
    "看着学姐因为烦恼而认真起来的表情，我不禁低下了头。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+224)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC05"),"True","img/CL_ZAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#REEK_CHR 0
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NCL06X_KU005"
    克罗艾 "「志，志雄？　突然间怎么了」"
#THREAD_STP 1
#REMOVE_REEK_CHR 0
#MUS_VOL 128
    志雄 "「说就业是开玩笑的。我还是打算继续上学的……」"
    voice "NCL06X_KU006"
    克罗艾 "「咦？　是那样吗？　嗯，也是呢……要是就业的话就不会进行考前复习了呢。」"
    志雄 "「不过，具体的还没有想好……我也觉得这样优柔寡断的自己很差劲……」"
    jump L_NCL06A_SEL00_X
label L_NCL06A_SEL00_X:
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB05"),"True","img/CL_ZAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "也许，学姐会因此对我很失望吧。这样的想法在我的脑中充斥着。"
    "克罗艾学姐，已经找到了自己的梦想，而我却只是一个人在原地踏步。"
    "如果我继续这样停滞不前的话，结果就只可能是我被抛弃在原地……"
    "可是，学姐的回答，却不含一丝一毫的失望。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU026"
    克罗艾 "「是啊，要选择决定以后的人生道路了。会烦恼是当然的。」"
    志雄 "「咦？」"
    voice "NCL06A_KU027"
    克罗艾 "「志雄有想做的事情的话，就向着能学习那方面知识的道路前进好了！」"
    志雄 "「那个，学姐？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB03"),"True","img/CL_ZAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU028"
    克罗艾 "「嗯，怎么了？」"
    志雄 "「那个，对于还没有决定未来方向的我，会不会觉得我很没用……」"
    voice "NCL06A_KU029"
    克罗艾 "「为什么？　被自己的未来的事情所困扰，这不是很正常的吗？」"
    志雄 "「虽然话是那么说……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU030"
    克罗艾 "「我的话，去年也烦恼了很久的……」"
    志雄 "「学姐也是吗？」"
    "意外的回答。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB02"),"True","img/CL_ZAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU031"
    克罗艾 "「嗯。一开始虽然对父亲的工作有点兴趣。不过也不是唯一的选择。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU032"
    克罗艾 "「成为契机的事情是去年父亲的病。我就是那个时候决定的，要在工作上帮助父亲。」"
    "说着，克罗艾学姐有些得意地笑着。"
    voice "NCL06A_KU033"
    克罗艾 "「所以说，志雄会烦恼也没什么。」"
    志雄 "「这样啊……」"
    voice "NCL06A_KU034"
    克罗艾 "「不断地寻找。如果最后依旧没有找到想要做的事情的话，就让我们一起来寻找吧～」"
    志雄 "「一起吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB06"),"True","img/CL_ZAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU035"
    克罗艾 "「一个人找不到的话，两个人的话应该更容易找到吧？」"
    志雄 "「是那样呢。」"
    "看着克罗艾学姐的笑脸，我感觉自己被注入了力量。"
    志雄 "「但是，既然是我自己的问题，还是让我用自己的肩膀来承担吧～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC02"),"True","img/CL_ZAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU036"
    克罗艾 "「啊呀，我就那么的无法信赖吗？」"
    志雄 "「没有。反倒是我有些过于依赖学姐了，总是受到学姐的照顾……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC04"),"True","img/CL_ZAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU037"
    克罗艾 "「我倒觉得没什么。」"
    志雄 "「不不，比起依靠别人，我还是想要成为一个被人依靠的男人的。」"
    voice "NCL06A_KU038"
    克罗艾 "「现在志雄也非常可靠的哦～」"
    "克罗艾学姐说了那样郑重的话语后，露出害羞的神情……"
    志雄 "「从今以后都会是！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAC01"),"True","img/CL_ZAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU039"
    克罗艾 "「那样的话，学习上完全依靠我也是不行的哦？」"
    志雄 "「咦？　那个和这个是两码事啦」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB01"),"True","img/CL_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU040"
    克罗艾 "「那么，现在要开始测验了！　好了，把教科书和笔记本都收起来～」"
    志雄 "「哇，等一下！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZAB06"),"True","img/CL_ZAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL06A_KU041"
    克罗艾 "「好，第一问！」"
    "那之后的一小时，学姐带着天使般的笑容，着提出的各种问题，让我完全陷入了解题的地狱中。"
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