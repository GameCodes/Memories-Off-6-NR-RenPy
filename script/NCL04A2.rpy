label NCL04A2:
    $currentlabel = "NCL04A2"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '24'
    $date = '1'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG31AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG31AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_08L"
    pause (32/32.0)
#FADE_IN 1
    play music "BGM10"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    志雄 "「还是老样子呢。」"
    "很久没有来过的骑乘俱乐部，和原来相比一点没变。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB01"),"True","img/CL_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU069"
    克罗艾 "「说起来，很久很久没有和志雄一起来了。」"
    "回过神来，学姐正牵着一匹黑色的马向我走来。"
    志雄 "「学姐经常自己一个人到这里来吗？」"
    voice "NCL04A_KU070"
    克罗艾 "「嗯，为了转换一下心情呗。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB02"),"True","img/CL_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU071"
    克罗艾 "「比如最近，打工时受到委屈的时候……」"
    志雄 "「学姐也会有那样的情况啊……」"
    "学姐笑了笑，回应了我的玩笑之言。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB04"),"True","img/CL_MBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU072"
    克罗艾 "「当然了啊。我也只是普通人而已。」"
    志雄 "「可是，我并没有看到学姐有任何称得上失败的地方呢……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBA05"),"True","img/CL_MBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU073"
    克罗艾 "「说得好像我除了在你面前，在别的地方都到处出问题似的！」"
    "学姐很不高兴地的样子，手叉腰地瞪着我。"
    "不过，比起学姐那有魄力的身姿，在她身上忽隐忽现的孩子气倒更是可爱，想到这我不禁笑了出来。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBA05"),"True","img/CL_LBA05A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCL04A_KU074"
    克罗艾 "「志～雄～？」"
    志雄 "「对不起！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBA02"),"True","img/CL_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU075"
    克罗艾 "「啊！」"
    "对着拼命忍耐住笑的我，学姐嘟起了脸颊。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBA04"),"True","img/CL_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU076"
    克罗艾 "「那些事情过后再慢慢说……」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "还没有来得及恢复情绪，学姐已经站在马的旁边向我招手了。"
#BG_GET_NOC 0,F26
#BG_CHG_FWD F26,48
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBA01"),"True","img/CL_LBA01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    志雄 "「怎么了？」"
    voice "NCL04A_KU077"
    克罗艾 "「那么，就先从志雄开始吧～」"
    志雄 "「啊？」"
    voice "NCL04A_KU078"
    克罗艾 "「骑给我看看吧～」"
    "既然决定了陪学姐来骑马，对于这样的要求也是早就有所觉悟的……"
    "但实际上，我全部骑马的经历也只有去年被克罗艾学姐邀请的那一次而已。"
    "只有那一次的骑乘经验，对于我这只属于及格水平的运动神经而言，完全没有什么实质性的意义。"
    "我目不转睛地注视着学姐。学姐则用一副小孩子恶作剧般的目光凝视着我。"
    志雄 "「学姐……」"
    voice "NCL04A_KU079"
    克罗艾 "「怎么了？」"
    志雄 "「果然是生我刚才笑学姐的气了吧？」"
    play sound "SE05_07"
    voice "NCL04A_KU080"
    克罗艾 "「当然是不会那样的啦～」"
    "学姐笑着否定了。"
    "与此同时，黑马也长嘶了一声。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB05"),"True","img/CL_LBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU081"
    克罗艾 "「让它等久了的话，会伤心的哦。」"
    志雄 "「唉——」"
    window hide
#MOV_CHR_INIT 48
#MOV_CHR0 128,(320+160)
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
    "走投无路的我，只好放弃反抗，把手放到了马鞍上。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB06"),"True","img/CL_LBB06A@2x.png") as lh0 zorder (10+0):
        xcenter .75
        ypos 0.0
    with dissolve
    voice "NCL04A_KU082"
    克罗艾 "「喂，加油哦！」"
    window hide
#CHR_PRIC 0
#BG_PRIC 0
#BG_INIC 3
#BG_PRIC 3
    scene expression "img/NIMG01B@2x.png" as bg3 zorder 3 with dissolve
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
#CHR_ALP_AUTOC 0,0,0,1
#BG_ALP_AUTOC 0,0,0,1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_ALPC 0,128
#CHR_PRIC 0
    "克罗艾学姐不停地催促着我，我像被赶的鸭子一般，急忙翻上了马背。"
    志雄 "「那个……」"
    "我努力唤醒脑中那个模糊的记忆，抓紧了缰绳。"
    window hide
    play sound "SE03_93L"
    with vpunch
    with hpunch
#EFF_STAC 0,QUAKE_AFTER_ZOOM,EFF_NOSKIP,0,120
    志雄 "「啊啊！？」"
    "在我做出反应前，马儿已经做出了相应的反应，开始慢慢前进，我不禁感叹起我的天资来。"
    voice "NCL04A_KU083"
    克罗艾 "「对对，缰绳要慢慢的拉住，志雄记住了呢。」"
    "听到克罗艾学姐的话，我稍微有些骄傲。"
#EFF_STAC 0,QUAKE_AFTER_ZOOM,EFF_NOSKIP,0,120
    "照这个状态的话，纵横驰骋于马场的那一天也离我不远了吧。"
    "不过，做出过分从容姿态的我，很快就因为陷入大危机而开始后悔了……"
    "地面突然变得崎岖起来。黑马的身体开始剧烈地颠簸，失去平衡的我，只能死死地抓住缰绳。"
    window hide
    play sound "SE05_07"
    play sound "SE05_05L"
#EFF_STAC 0,QUAKE_AFTER_ZOOM,EFF_NOSKIP,0,120
    志雄 "「哇啊！」"
    "黑马极其嘹亮地长嘶了一声后，就如同离弦之箭一般冲了出去。"
#EFF_STAC 0,QUAKE_AFTER_ZOOM,EFF_NOSKIP,0,120
    志雄 "「呃，哇！该怎么办……」"
    "我急忙调整姿势，但是怎么也无法做到。在视野的尽头，我看到了脸上浮现出笑容的学姐。"
    stop se
    "我紧缩着四肢趴在马背上，努力想让马儿安定下来，不过使出浑身解数也毫无收效。"
    "没有丝毫准备，一阵强烈的疼痛感从全身各处传来。"
    window hide
#BG_PRIC 1
    scene expression "img/BG31AA@2x.jpg" as bg1 with dissolve
#EFF_STPC 0,EFF_NOSKIP
#EFF_PRI 0
#ROUTINE_STA
    hide bg3 with dissolve
#BG_PRIC 3
#BG_PRIC 0
#ROUTINE_STP
#BG_SWPC 0
#BG_PRIC 1
#BG_COLC 0,128,128,128,128
    play sound "SE03_99"
    "看到我从马背上转着圈摔了下来，学姐急忙靠过来查看我的状况。"
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB01"),"True","img/CL_LBB01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCL04A_KU084"
    克罗艾 "「看起来好像不应该让你一个人呢……」"
    志雄 "「别看了，先帮帮我吧。我都摔下来了……」"
    "我视图通过悲愤的眼神表达抗议，不过学姐巧妙地无视了。"
    voice "NCL04A_KU085"
    克罗艾 "「我相信是志雄的话一定没问题的！」"
    "克罗艾学姐拿起黑马的缰绳，向我的方向回过头来。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB02"),"True","img/CL_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU086"
    克罗艾 "「那么，稍微做个示范好了～」"
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
    play sound "SE02_12L"
    pause (32/32.0)
    "不过，就在学姐翻身上马的时候，口袋里手机的铃声响了起来。"
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB03"),"True","img/CL_LBB03A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCL04A_KU087"
    克罗艾 "「会是什么事呢？」"
    window hide
    play sound "SE02_05"
    "从马背上跳下来的学姐，从口袋里拿出手机放到了耳边。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC01"),"True","img/CL_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU088A"
    克罗艾 "「是，我是嘉神川。嗯，是……{w=5}{nw}"
#MESA A_CH_KU,NCL04A_KU088A,"【クロエ】「是，我是嘉神川。嗯，是……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC05"),"True","img/CL_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCL04A_KU088B"
    extend "诶！？」"
#REMOVE_REEK_CHR 0
    window hide
    play music "OBGM14"
    "克罗艾学姐霎时变了脸色。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC03"),"True","img/CL_LBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU089"
    克罗艾 "「是，我知道了。马上就过去！」"
    window hide
    play sound "SE02_05"
    "学姐用十分凝重的语气讲完之后便挂断了电话。"
    "学姐那慌乱的样子真是少见，我不禁心里也一紧。"
    志雄 "「发生了什么？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC02"),"True","img/CL_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU090"
    克罗艾 "「爸爸他……晕倒了……」"
    志雄 "「诶！？」"
    "可是，刚才见面的时候还是很健康的样子啊……"
    voice "NCL04A_KU091"
    克罗艾 "「该怎么办啊，我……」"
    "学姐苍白着脸，紧握着手机踱来踱去。我急忙去扶住学姐。"
    志雄 "「学姐，冷静一点儿！我去叫出租车。」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我让学姐在原地等我，用最快的速度跑向附近的建筑物。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG80AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG80AA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
#FADE_IN 1
    play music "OBGM16"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBA02"),"True","img/CL_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU092"
    克罗艾 "「……」"
#MESEX_A M_NOA,A_CH_KU,NCL04A_KU092,"【クロエ】「……」%K%P"
    志雄 "「现在怎样了？」"
    "听了医生说明的学姐，表情明显舒缓了许多。"
    voice "NCL04A_KU093"
    克罗艾 "「没什么大碍，只是稍微有点劳累……不过看起来需要住院观察了。」"
    志雄 "「这样……」"
    "我不禁安心地长出了一口气。"
    "据说，学姐的父亲是接受完医院检查，在回去的时候，晕倒在了医院的门口的。"
    "所幸的是，附近刚好有路过的护士发现了，所以及时送到了医院里……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBA05"),"True","img/CL_MBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU094"
    克罗艾 "「如果我那个时候有好好照顾爸爸的话……」"
    "学姐在后悔那个时候让父亲一个人去医院的事情了吧。"
    "学姐的声音颤抖着，一副快要哭出来的样子。"
    志雄 "「学姐，请不要责怪自己」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBA04"),"True","img/CL_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU095"
    克罗艾 "「可是！好好陪着爸爸的话就不会这样了啊！？」"
    志雄 "「……已经过去的事情就算再怎么说也于事无补了。」"
    "我正视着克罗艾学姐的双眼。"
    "学姐的眼中噙满泪水，晶莹的泪珠随时都会落下。"
    "真想马上抱住学姐。我心中的每一个角落都充满着这样的想法。可是，现在不是做这种事情的时候。"
    志雄 "「来考虑今后该怎么办吧。住院的话，需要准备很多东西呢。」"
    "我尽可能平静地说着。"
    "学姐听了我的话微微地点了点头，擦掉了眼角的泪水。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBA02"),"True","img/CL_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU096"
    克罗艾 "「对不起，完全不知所措了……」"
    志雄 "「学姐不要道歉啦……这种时候任谁都会如此的。」"
    voice "NCL04A_KU097"
    克罗艾 "「谢谢……」"
    "太好了，学姐恢复了精神。"
    voice "NCL04A_KU098"
    克罗艾 "「不过，我想先去看一下父亲可以吗？」"
    志雄 "「好的。」"
    window hide
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
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+160)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_SBA01"),"True","img/NO_SBA01A@2x.png") as lh1 zorder (10-1):
        ypos 0.3
        xcenter .75
    with dissolve
    pause (32/32.0)
#MUS_VOL 0
#THREAD_STA 1,THREAD_NOEL_HIDE
    #hide bg1 with dissolve
#THREAD_WAT 1
    hide lh1 with dissolve
##CHR_ALPC 1,128
    志雄 "「……咦？」"
    "走到病房跟前的时候，我不禁疑惑了起来。"
    "刚才，好像有个小女孩儿进到了学姐父亲的病房里的样子……"
    "看错了吗？"
    志雄 "「那个，学姐……」"
    克罗艾 "「……」"
#MESEX_A M_NOA,A_CH_KU,NCL04A_KU099,"【クロエ】「……」%K%P"
    "我向走到病房门口的克罗艾学姐搭话，可是学姐没有回应。"
    志雄 "「学姐？」"
    window hide
#MUS_VOL 128
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC05"),"True","img/CL_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#REEK_CHR 0
    voice "NCL04A_KU100"
    克罗艾 "「啊，怎么了？」"
#REMOVE_REEK_CHR 0
    "我再一次问道，学姐终于有了回应。"
    志雄 "「不要紧吧？学姐一副心不在焉的样子」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC04"),"True","img/CL_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU101"
    克罗艾 "「啊，诶。没关系」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC02"),"True","img/CL_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "虽然这么说，但学姐的脸色很不好。"
    "本来学姐的父亲会晕倒并不是太让人出乎意料的，可是再这样下去连学姐都要一起病倒了。"
    志雄 "「要不然，我来背学姐走吧？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC01"),"True","img/CL_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU102"
    克罗艾 "「噗，真的不要紧啦～」"
    "想和学姐开个玩笑。结果学姐却当真了……"
    "不过，看反应的话应该没什么大问题了吧。"
    "不知道是不是在走到病房的这段时间里平静了一些，不过看起来学姐至少已经能微笑出来了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB03"),"True","img/CL_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU103"
    克罗艾 "「对了，刚才怎么了，好像有急着想说什么吗？」"
    志雄 "「啊，对了。刚才看没看见有个小女孩儿？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB05"),"True","img/CL_LBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU104"
    克罗艾 "「诶？对不起，没看见呢……」"
    志雄 "「应该没看错……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB03"),"True","img/CL_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL04A_KU105"
    克罗艾 "「那个女孩儿怎么了？」"
    志雄 "「我看到那个女孩儿走进了学姐父亲的病房里……」"
    voice "NCL04A_KU106"
    克罗艾 "「真的吗？大概是谁家的孩子迷路了吧。」"
    "也是，不管怎样进去的话就清楚了。"
    window hide
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB02"),"True","img/CL_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    pause (16/32.0)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB01"),"True","img/CL_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "走到病房前，学姐深呼吸了一下，极其小心地敲了敲门。"
    window hide
    play sound "SE00_27"
    voice "NCL04A_KU107"
    克罗艾 "「爸爸，我进来了哦。」"
    window hide
    play sound "SE00_53"
    "很有礼貌地等待了一下后，学姐打开了房门。就在那一秒，学姐像被石化了一样，完完全全地怔在了原地。"
    stop music fadeout 1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC05"),"True","img/CL_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    克罗艾 "「……」"
#MESEX_A M_NOA,A_CH_KU,NCL04A_KU108,"【クロエ】「……」%K%P"
    stop se
    志雄 "「学姐？」"
    "学姐的脸上浮现出惊恐和困惑的神情。"
#REEK_CHR 0
    voice "NCL04A_KU109"
    克罗艾 "「……为什么？」"
#REMOVE_REEK_CHR 0
    "学姐小声地嘟囔着。"
    "我很想知道学姐到底看到了什么，于是我凑上前去，从学姐的身后窥视病房里的情况。"
    show expression "img/BG40AA@2x.jpg" as bg_over zorder 2 with dissolve
    "在病房里的是躺在病床上上半身坐起来的嘉神川先生，还有坐在他身旁客用椅子上的白发女士。"
    "外国人……？难道是……"
    "学姐的动作一直凝固在打开房门的那一刹那，一动不动地凝视着与自己脸庞相似的那个人。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+224)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC04"),"True","img/CL_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320+224)/640.0
    with dissolve
    voice "NCL04A_KU110"
    克罗艾 "「……妈妈？」"
    "从学姐口中发出的那个声音里，一种微妙的感觉在四处扩散。"
    "看到那个女人的一刹那，我也有了和克罗艾学姐相似的感受。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    pause (32/32.0)
#BG_PRI 0
#BG_GET_NOC 0,F24
#BG_SET_BACK 
#BG_INIC 2
#BG_UVC 2,(640/4),0,(640/2),(448/2)
#CHR_SET_BACK
#CHR_INIC 1
#CHR_INIC 2
#CHR_PRIC 1
#CHR_PRIC 2
#CHR_POSC 1
#CHR_POSC 2,(320-224)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA01"),"True","img/YS_LAA01A@2x.png") as lh1 zorder (10+1):
        xcenter (320-224)/640.0
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA01"),"True","img/YZ_LAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .5
        ypos 0.0
    with dissolve
#BG_ALP_AUTOC 0,0,0,1
#BG_SWPC 0
    hide bg2 with dissolve
#BG_PRI 0
#BG_PRI 2
#CHR_PRIC 1
#CHR_PRIC 2
    play music "OBGM08"
    voice "NCL04A_EL000"
    エリーズ２ "「好久不见了呢，克罗艾……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+224)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XBC04"),"True","img/CL_XBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320+224)/640.0
    with dissolve
    voice "NCL04A_KU111"
    克罗艾 "「……」"
#MESEX_A M_NOA,A_CH_KU,NCL04A_KU111,"【クロエ】「……」%K%P"
    "学姐没有回应母亲的话，而是依然像看着什么难以置信的东西一样呆在原地。"
    voice "NCL04A_KU112"
    克罗艾 "「妈妈……为什么？」"
    voice "NCL04A_EL001"
    エリーズ２ "「医院也有联系我这边呢……」"
    "面对学姐的母亲掺杂着苦笑的话语，学姐的父亲为难似地挠了挠头。"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB03"),"True","img/YZ_LAB03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCL04A_KZ010"
    幸蔵 "「抱歉，克罗艾。让你担心了……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XBC02"),"True","img/CL_XBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320+224)/640.0
    with dissolve
    voice "NCL04A_KU113"
    克罗艾 "「嗯……不用在意……」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA03"),"True","img/YZ_LAA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    "学姐心不在焉地回答着。然后用含糊的语气继续说道。"
    voice "NCL04A_KU114"
    克罗艾 "「回到……日本了呢？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA03"),"True","img/YS_LAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter (320-224)/640.0
    with dissolve
    voice "NCL04A_EL002"
    エリーズ２ "「嗯，大概是这个月初的时候……」"
    "说完这样的话，学姐的妈妈脸上又浮现出了一丝苦笑。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA01"),"True","img/YS_LAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter (320-224)/640.0
    with dissolve
    voice "NCL04A_EL003"
    エリーズ２ "「吓了一跳呢，听到爸爸住院的消息」"
    voice "NCL04A_KU115"
    克罗艾 "「为什么……？」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA06"),"True","img/YZ_LAA06A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCL04A_KZ011"
    幸蔵 "「克罗艾？」"
    voice "NCL04A_KU116"
    克罗艾 "「回来了的话，为什么不马上联系呢！？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_LAA03"),"True","img/YS_LAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter (320-224)/640.0
    with dissolve
    voice "NCL04A_EL004"
    エリーズ２ "「对不起……」"
    "对语气严厉的学姐，学姐的妈妈用道歉的语气回答道。"
#MESEX_A M_NOA,A_CH_KU,NCL04A_KU117,"【クロエ】「……」%K%P"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA03"),"True","img/YZ_LAA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCL04A_KZ012"
    幸蔵 "「妈妈她有联系过我的。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XBC04"),"True","img/CL_XBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320+224)/640.0
    with dissolve
    voice "NCL04A_KU118"
    克罗艾 "「爸爸？」"
    voice "NCL04A_KZ013"
    幸蔵 "「抱歉。本来是准备今天回家之后好好引见的——」"
    "说到这里，学姐的父亲微微地叹了一口气。"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA05"),"True","img/YZ_LAA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCL04A_KZ014"
    幸蔵 "「没想到……变成这个样子。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XBC06"),"True","img/CL_XBC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320+224)/640.0
    with dissolve
    voice "NCL04A_KU119"
    克罗艾 "「这样，啊……」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA03"),"True","img/YZ_LAA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    "对话到这里便停止了，病房里充满了凝重的沉默。"
    stop music fadeout 1
    voice "NCL04A_NO000"
    ノエル？ "「呐，妈妈……」"
    "一个不同于在场任何一个人的声音，挤进了三人的对话中。"
#BG_GET_NOC 0,F24
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter (320-224)/640.0
    with dissolve
    if not persistent.dictlist[15] and persistent.show_dict:
        $persistent.dictlist[15]=True
        show screen dict_pop(i=15)
    voice "NCL04A_EL005"
    エリーズ２ "「咦，怎么了，诺艾儿？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA04"),"True","img/NO_MBA04A@2x.png") as lh2 zorder (10-2):
        ypos 0.2
        xcenter .35
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR2 128,(320-96)
#MOV_CHR_GO 1
    "把目光投向发出声音的源头，是刚才进入病房的那个小女孩儿。她藏匿在学姐母亲的身后，偷偷地窥视着这边。"
    "初中生……不，大概还是小学生吧。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+224)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC04"),"True","img/CL_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320+224)/640.0
    with dissolve
    voice "NCL04A_KU120"
    克罗艾 "「这孩子是……？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA08"),"True","img/NO_MBA08A@2x.png") as lh2 zorder (10+2):
        ypos .2
        xcenter .35
    "在我浮现出疑惑之际，学姐也歪着脑袋疑惑着。对学姐这样的神情，学姐的父母为难般地相互看了看。"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA03"),"True","img/NO_MBA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.2
        xcenter .5
    with dissolve
    voice "NCL04A_EL006"
    エリーズ２ "「虽然真的是不应该用这种方式来介绍……」"
    hide lh2 with dissolve
#CHR_POSC 2,(320-96)
#CHR_SORT 0,2
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA03"),"True","img/NO_MBA03A@2x.png") as lh2 zorder (10+2):
        ypos .2
        xcenter .5
    with move
    "说完这话，她便把身后的小女孩拉到了我们跟前。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL04A_EL007"
    エリーズ２ "「她叫诺艾儿，是你的妹妹哦……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC05"),"True","img/CL_LBC05A@2x.png") as lh0 zorder (10+0):
        xcenter (320+224)/640.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA07"),"True","img/NO_MBA07A@2x.png") as lh2 zorder (10+2):
        ypos .2
        xcenter .5
#REEK_CHR 0
    voice "NCL04A_KU121"
    克罗艾 "「妹、妹妹……？」"
#REMOVE_REEK_CHR 0
    "妹妹？克罗艾学姐的？"
#    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA02"),"True","img/YS_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL04A_EL008"
    エリーズ２ "「呐，打个招呼吧？」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB02"),"True","img/NO_MBB02A@2x.png") as lh2 zorder (10+2):
        ypos .2
        xcenter .5
    with dissolve
    voice "NCL04A_NO001"
    诺艾儿 "「初次见面。我叫嘉神川诺艾儿……」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB01"),"True","img/NO_MBB01A@2x.png") as lh2 zorder (10+2):
        ypos .2
        xcenter .5
    with dissolve
    "学姐显然被突如其来的『妹妹』给惊呆了，诺艾儿也低下来了头。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCL04A_EL009"
    エリーズ２ "「然后呢，诺艾儿。这位是克罗艾姐姐和……咦？」"
    "似乎此时才发现我的存在。"
    志雄 "「那个，您好，初次见面……」"
    window hide
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA04"),"True","img/NO_MBA04A@2x.png") as lh2 zorder (10-2):
        ypos 0.2
        xcenter (320-192)/640.0
    with move
#MOV_CHR_INIT 32
#MOV_CHR2 ,(320-192)
#MOV_CHR_GO 1
#CHR_SORT 0,1
#MOV_CHR_INIT 32
#MOV_CHR2 ,(320-96)
#MOV_CHR_GO 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA03"),"True","img/YS_MAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    "我带着略显尴尬的微笑向她们打了招呼。"
    "那个小女孩则是躲回了母亲的身后。"
    "学姐也突然意识到还没有介绍我，慌忙插话进来。"
#REEK_CHR 0
    voice "NCL04A_KU122"
    克罗艾 "「他是塚本志雄。他是，那个——」"
#REMOVE_REEK_CHR 0
    "学姐话说到此便顿住了，脸上也泛起了红晕。"
    window hide
    play music "BGM13"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB04"),"True","img/CL_LBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320+224)/640.0
    with dissolve
    voice "NCL04A_KU123"
    克罗艾 "「恋人……」"
    window hide
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA08"),"True","img/NO_MBA08A@2x.png") as lh2 zorder (10-2):
        ypos 0.2
        xcenter .4
    with move
#MOV_CHR_INIT 48
#MOV_CHR2 ,(320-160)
#MOV_CHR_GO 1
    "话刚说完，到刚才为止一直保持警戒感的小女孩眼中一下子放出了奇异的光芒。"
    voice "NCL04A_NO002"
    诺艾儿 "「大哥哥是克罗艾姐姐的丈夫吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB03"),"True","img/CL_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320+224)/640.0
    with dissolve
    voice "NCL04A_KU124"
    克罗艾 "「……！？」"
#MESEX_A M_NOA,A_CH_KU,NCL04A_KU124,"【クロエ】「……！？」%K%P"
    志雄 "「呃？不，该怎么说呢……」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB09"),"True","img/NO_MBB09A@2x.png") as lh2 zorder (10+2):
        ypos .2
        xcenter .5
    with dissolve
    voice "NCL04A_NO003"
    诺艾儿 "「不是吗？」"
    window hide
#CHR_PRIC ID_ALL
#BG_ALP_AUTOC 3,0,0,1,48
#BG_SWPC 0
    hide bg0 with dissolve
#BG_PRI 3
#BG_PRI 0
#BG_GET_NOC 3,F34
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,(640/8),(448/8),((640/4)*3),((448/4)*3)
    #show expression "img/F34@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 3
#CHR_PRIC 3
#CHR_POSC 3
    hide lh2
    hide lh3
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB09"),"True","img/NO_LBB09A@2x.png") as lh3 zorder (10-3):
        ypos 0.2
    with dissolve
#BG_ALP_AUTOC 3,0,0,F24,48
#CHR_ALP_AUTOC 0,0,0,F24,48
#CHR_ALP_AUTOC 1,0,0,F24,48
#CHR_ALP_AUTOC 2,0,0,F24,48
#BG_ALP_SAVEC 3
#CHR_ALP_SAVEC 0
#CHR_ALP_SAVEC 1
#CHR_ALP_SAVEC 2
    hide bg3 with dissolve
#BG_ALPC 3,128
#CHR_SWPC 1
#CHR_ERSTC 0,2,3
#CHR_PRIC ID_ALL
#CHR_SORT 0,1,2
#CHR_ALPC 0,128
#CHR_ALPC 2,128
#CHR_ALPC 3,128
    志雄 "「那个，诺艾儿，这样说吧。」"
    hide lh2
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB01"),"True","img/NO_LBB01A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .5
    with dissolve
    voice "NCL04A_NO004"
    诺艾儿 "「嗯。」"
    "看到诺艾儿——点了点头后，我继续说道。"
    志雄 "「丈夫呢，是结婚之后才能算作是的哦，我和学姐还是在那之前的那个阶段呢……」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB04"),"True","img/NO_LBB04A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .5
    with dissolve
    voice "NCL04A_NO005"
    诺艾儿 "「……我不是很明白呢……」"
    "对我竭尽所能的说明，诺艾儿依旧歪着脑袋若有所思。"
    "呃，这个时候该怎么办才好呢？"
    window hide
#BG_GET_NOC 0,F34
#BG_SET_BACK 
#BG_INIC 2
#BG_UVC 2,(640/8),((448/8)+512),((640/4)*3),((448/4)*3)
    #show expression "img/F34@2x.jpg" as bg2 zorder 2 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,640
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XBB04"),"True","img/CL_XBB04A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter (320+224)/640.0
    with dissolve
#ROUTINE_STA
#BG_UV_AUTOC 0,(640/4),((448/8)+512),((640/4)*3),((448/4)*3),1,F24,48
#BG_UV_AUTOC 2,(640/4),(448/8),((640/4)*3),((448/4)*3),1,F24,48
#BG_ALP_AUTOC 0,0,0,F24,48
#CHR_ALP_AUTOC 0,128,0,F24,48
#CHR_ALP_AUTOC 1,0,0,F24,48
#CHR_POS_AUTOC 0,(320+192),F24,48
#CHR_POS_AUTOC 1,(320-96),F24,48
#ROUTINE_STP
#BG_UV_SAVEC 0
#BG_UV_SAVEC 2
#BG_ALP_SAVEC 0
#CHR_ALP_SAVEC 0
#CHR_ALP_SAVEC 1
#CHR_POS_SAVEC 0
#CHR_POS_SAVEC 1
    "我抬起头望向学姐，试图发出求救的信号。"
    "不过，学姐却依旧红着脸愣在那里，完全没有注意到我的小动作。"
    window hide
#ROUTINE_STA
#BG_UV_AUTOC 0,(640/8),(448/8),((640/4)*3),((448/4)*3),1,F24,48
#BG_UV_AUTOC 2,(640/8),(448/8),((640/4)*3),((448/4)*3),1,F24,48
#BG_ALP_AUTOC 0,128,0,F24,48
#CHR_ALP_AUTOC 0,0,0,F24,48
#CHR_ALP_AUTOC 1,128,0,F24,48
#CHR_POS_AUTOC 0,640,F24,48
#CHR_POS_AUTOC 1,F24,48
#ROUTINE_STP
#BG_UV_SAVEC 0
#BG_UV_SAVEC 2
#BG_ALP_SAVEC 0
#CHR_ALP_SAVEC 0
#CHR_ALP_SAVEC 1
#CHR_POS_SAVEC 0
#CHR_POS_SAVEC 1
    hide bg2 with dissolve
#BG_ALPC 2,128
#CHR_SWPC 0
    hide lh1 with dissolve
#CHR_ALPC 1,128
#CHR_SORT 0,1,2
#MESA A_CH_NO,NCL04A_NO006A,"【ノエル】「恋人？"
    voice "NCL04A_NO006A"
    诺艾儿 "「恋人？{w=2}{nw}"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB01"),"True","img/NO_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .5
    with dissolve
    voice "NCL04A_NO006B"
    extend "再多告诉我一些嘛！」"
    "说起来那个时候克罗艾学姐的母亲是回到了法国的娘家了。"
    "这么说的话，这个孩子是接受法国教育长大的……"
    "虽然日语说得这么好……也还是有些词语不能弄明白吧。"
    "该怎么说明才好呢……"
    voice "NCL04A_EL010"
    エリーズ２ "「诺艾儿……」"
    window hide
#CHR_PRIC ID_ALL
#CHR_SORT 0,3,1
#BG_ALP_AUTOC 3,0,0,1,48
#BG_SWPC 0
    hide bg0 with dissolve
#BG_PRI 3
#BG_PRI 0
#BG_GET_NOC 3,F34
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,0,640,448
#CHR_SET_BACK
#CHR_INIC 1
#CHR_INIC 2
#CHR_PRIC 1
#CHR_PRIC 2
#CHR_POSC 1,(320-96)
#CHR_POSC 2,(320+96)
    hide lh0
    hide lh3
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB09"),"True","img/NO_MBB09A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .35
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .65
        ypos 0.0

#BG_ALP_AUTOC 3,0,0,F24,48
#CHR_ALP_AUTOC 0,0,0,F24,48
#BG_ALP_SAVEC 3
#CHR_ALP_SAVEC 0
    hide bg3 with dissolve
#BG_ALPC 3,128
    hide lh0 with dissolve
#CHR_PRIC ID_ALL
#CHR_SORT 0,1,2
#CHR_ALPC 0,128
    "这个时候，学姐的母亲开口了。"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA02"),"True","img/YS_MAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL04A_EL011"
    エリーズ２ "「过后妈妈来告诉你，好吗？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA03"),"True","img/NO_MBA03A@2x.png") as lh1 zorder (10+1):
        ypos .2
        xcenter .35
    with dissolve
    voice "NCL04A_NO007"
    诺艾儿 "「好……」"
    "被母亲制止之后，诺艾儿好像很勉强的放弃了提问。"
    window hide
    hide lh1 with dissolve
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL04A_EL011A"
    エリーズ２ "「那个……」"
    志雄 "「我是塚本志雄。初次见面。平时一直承蒙克罗艾学姐的关照。」"
    if not persistent.dictlist[14] and persistent.show_dict:
        $persistent.dictlist[14]=True
        show screen dict_pop(i=14)
    voice "NCL04A_EL011B"
    エリーズ２ "「初次见面。我是克罗艾的母亲，嘉神川爱丽丝。」"
    voice "NCL04A_EL011C"
    爱丽丝 "「塚本……志雄。记住了。平时克罗艾承蒙你的关照了。今后女儿的事情也请多关照。」"
    志雄 "「啊，那个……请多关照。」"
    "不知因为紧张，还是这里的气氛的缘故……我完全笑不出来。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    志雄 "「那个，我就先告辞了……」"
    "这种情境下，有我这个外人在，他们一家人会无法敞开心扉说话吧。就算没有什么隔阂，许久不见的一家人也差不多该团圆一下了。"
    window hide
#BG_PRI 0
#BG_GET_NOC 0,F24
#BG_SET_BACK 
#BG_INIC 2
#BG_UVC 2,(640/4),0,(640/2),(448/2)
    #show expression "img/F24@2x.jpg" as bg2 zorder 2 with dissolve
#CHR_SET_BACK
#CHR_INIC 2
#CHR_PRIC 2
#CHR_POSC 2,(320-224)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAB03"),"True","img/YZ_LAB03A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
    with dissolve
#BG_ALP_AUTOC 0,0,0,1
#BG_SWPC 0
    hide bg2 with dissolve
#BG_PRI 0
#BG_PRI 2
#CHR_PRIC 2
    voice "NCL04A_KZ015"
    幸蔵 "「啊，让你困扰了，抱歉啊。」"
    志雄 "「不，没有啦。」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA03"),"True","img/YZ_LAA03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    "学姐的父亲一脸抱歉的表情，这反倒让我诚惶诚恐。"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(448/8)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB03"),"True","img/NO_LBB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter (448/8)/640.0
    with dissolve
    voice "NCL04A_NO008"
    诺艾儿 "「大哥哥，要回去了吗？」"
    志雄 "「嗯，天色也不早了呢。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB01"),"True","img/NO_LBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter (448/8)/640.0
    with dissolve
    voice "NCL04A_NO009"
    诺艾儿 "「这样……还能再见面吗？」"
    志雄 "「当然了。」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA02"),"True","img/NO_LBA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.2
        xcenter (448/8)/640.0
    with dissolve
    voice "NCL04A_NO010"
    诺艾儿 "「那，哥哥再见～」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YZ'",DynamicDisplayable(mouthanime,"YZ_LAA01"),"True","img/YZ_LAA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter 0.5
    with dissolve
    志雄 "「再见哦，诺艾儿。」"
#BG_GET_NOC 0,F24
    #show expression "img/F24@2x.jpg" as bg_over zorder 2 with dissolve
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB04"),"True","img/CL_MBB04A@2x.png") as lh0 zorder (10+0):
        xcenter 0.75
    with dissolve
    志雄 "「那我先走了。」"
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
    "最后向学姐告别之后，我走出了病房。"
    voice "NCL04A_KU125"
    克罗艾 "「志雄……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBC02"),"True","img/CL_MBC02A@2x.png") as lh0 zorder (10+0):
        xcenter 0.75
    with dissolve
    "刚走到门口便被学姐叫住了。"
    志雄 "「怎么了？」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC03"),"True","img/CL_LBC03A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCL04A_KU126"
    克罗艾 "「我送你吧……」"
    志雄 "「呃？可是……」"
    "难得，一家人在一起……"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE00_53"
    pause (32/32.0)
    "我的话还没说完，学姐便拉着我的手走出了病房。"
    show expression "img/BG80AA@2x.jpg" as bg_over zorder 2 with dissolve
    志雄 "「学姐？等等我啊……」"
    克罗艾 "「……」"
#MESEX_A M_NOA,A_CH_KU,NCL04A_KU127,"【クロエ】「……」%K%P"
    志雄 "「学姐？学——姐——！？」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG01AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG01AA@2x.jpg" as bg0 with dissolve
    play sound "SE08_17L"
    pause (32/32.0)
#FADE_IN 1
    "走到医院外面，学姐终于停止了脚步。"
    window hide
#SE_VOLC 1,64
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC06"),"True","img/CL_LBC06A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    志雄 "「怎么这么慌张的跑出来？」"
    voice "NCL04A_KU128"
    克罗艾 "「对不起……」"
    志雄 "「倒不用道歉啦，可是……」"
    "想说点什么，可是思来想去都没有找到能说出口的话来。"
    志雄 "「太好了呢。一家人终于团聚了。」"
    voice "NCL04A_KU129"
    克罗艾 "「是呢……」"
    "学姐面无表情地微微点了点头。"
    "就这样，对话再一次中断了。"
    window hide
#SE_VOLC 1,128
    play sound "SE01_12L"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "而后，沉默蔓延在了一整个离开的途中……"
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
#label THREAD_NOEL_HIDE
#CHR_POS_AUTOC 1,(640+(320-160)),0,0,F123
##CHR_ALP_AUTOC 1,0,0,F123
#CHR_POS_SAVEC 1
#CHR_ALP_SAVEC 1
#EOT
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT