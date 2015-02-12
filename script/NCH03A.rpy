label NCH03A:
    $currentlabel = "NCH03A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '19'
    $date = '3'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG15MA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG15MA@2x.jpg" as bg0 with dissolve
    play sound "SE06_11"
    pause (128/32.0)
#BG_BLUR 0
#FADE_IN 1,128
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
    志雄 "「嗯……」"
    "嘈杂的声音传到了耳朵里。我反射性地把手伸过去，抓住了铃声的来源——闹钟。"
    window hide
    stop se
#MUS_VOL 0


    志雄 "「哎！？」"
    "闹钟上显示的时间，是平时完成了早晨的准备，从家里出去的时间了。"
    if not persistent.dictlist[16] and persistent.show_dict:
        $persistent.dictlist[16]=True
        show screen dict_pop(i=16)
    "是因为昨天听ＫＡＮＡＴＡ的特别广播听到很晚的缘故吗！？"
#MUS_VOL 128
    志雄 "「糟了，不快点的话！」"
    "没时间吃早饭了！"
    "我抓起挂在衣架上的制服，换上衣服。"
    window hide
    play sound "SE00_07"
#FADE_OUT 1,16
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#FADE_IN 0
    "然后拿上提包立刻从房间里冲出去。"
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 5,CAL_0719
#FADE_OUT 0
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG39AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG39AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_14L"
    pause (32/32.0)
    play sound "SE00_03"
#FADE_IN 1,16
#SE_WATC 0
    play sound "SE01_02L"
    "不快点的话——！"
    window hide
#SE_VOLC 1,128
    show expression "img/BG14AA@2x.jpg" as bg0 with dissolve
    "就会让智纱等着我了！"
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
    show expression "img/BG01AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG01AA@2x.jpg" as bg0 with dissolve
    play sound "SE08_17L"
    pause (32/32.0)
#FADE_IN 1
    志雄 "「智纱！」"
    "我上气不接下气地跑到了车站，智纱的身影已经在那里了。"
    window hide
#SE_VOLC 1,128
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA01"),"True","img/CH_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music "BGM03"
    voice "NCH03A_CH000"
    智纱 "「啊，志雄君」"
    志雄 "「抱歉，我来晚了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAB02"),"True","img/CH_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH001"
    智纱 "「没事，时间还来得及」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAB01"),"True","img/CH_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "每天，我都和智纱在车站碰面，一起去学校。"
    "智纱在我到之前会一直很老实地等着我，我可不能迟到了。"
    志雄 "「那好，走吧」"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG04AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG04AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_14L"
    pause (32/32.0)
    play sound "SE01_12L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,64
    "啊啊……是受昨天熬夜的影响吧，我现在相当地困。"
    window hide
#SE_VOLC 1,(64/2)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_ALPC 0
#CHR_ALPC 1
#CHR_POSC 0,((640)-104)
#CHR_POSC 1,((320)-104)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC06"),"True","img/CH_MAC06A@2x.png") as lh1 zorder (10+0):
        xcenter .25
        ypos 0.0
    with dissolve
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC05"),"True","img/CH_MAC05A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
    with dissolve

#RSET F121
##THREAD_STA 1,THREAD_CHISA_FURAFURA
#NCH03A_EFFECT
#CHR_ALP_AUTOC 1,128,0,F24,48
#CHR_ALP_SAVEC 1
    voice "NCH03A_CH002"
    智纱 "「呼啊……」"
    "犯困的看来不只我一个。智纱用手掩着嘴，轻轻地打着哈欠。"
    志雄 "「怎么了？　睡眠不足？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC03"),"True","img/CH_MAC03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH003"
    智纱 "「嗯，嗯嗯……」"
    voice "NCH03A_CH003"
    智纱 "「嗯，嗯嗯……」"
    "不知是听见了还是没听见，智纱哼哼唧唧地，用不成句子的语调回答着。"
    "她的身体晃晃悠悠的，看上去很危险地摇摆着，完全没法走直线。"
    志雄 "「喂，一边走一边睡觉可是很危险的呐」"
    "智纱变成这种样子，可是很少见的。这么说来，至今为止是一次也没有见到过。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC02"),"True","img/CH_MAC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH004"
    智纱 "「嗯……我没有在睡觉啦……志雄君」"
    "用那样的步伐和困倦的语气说着什么「没有在睡觉」，就像醉汉烂醉如泥地说着「我……没醉」一样没有任何说服力。"
    stop se
#RSET F121
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
#STOP_NCH03A_EFFECT
#CHR_POS_AUTOC 1,((640)-104),0,1,0
#CHR_POSC 0,((640)-104)
    志雄 "「啊，智纱。走那边的话……」"
    window hide
#THREAD_WAT 1
    play sound "SE04_04"
#CHR_ALPC 0,128
#CHR_ALPC 1
#QUA2_CHR 0
    voice "NCH03A_CH005"
    智纱 "「好痛！？」"
    hide lh1 with dissolve
#CHR_ALPC 1,128
    voice "NCH03A_CH006"
    智纱 "「什、什么！？」"
    "智纱撞在了路边的招牌上。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAB03"),"True","img/CH_MAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter 1-104/640.0
    with dissolve
    voice "NCH03A_CH007"
    智纱 "「吓了一大跳啊……。醒过来了……」"
    志雄 "「果然是睡着了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA03"),"True","img/CH_MAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#CHR_GET_POSC 0,F24,F25
#RSUB F24,(640/2)
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
    voice "NCH03A_CH008"
    智纱 "「没，没有！　没那回事的！」"
#THREAD_STP 1
#REMOVE_REEK_CHR 0
    志雄 "「不是吧，怎么看，都觉得你是睡着了」"
    志雄 "「到底是怎么了？　是熬夜了吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC02"),"True","img/CH_MAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH009"
    智纱 "「有点……」"
    "智纱的说法有些含糊。"
    志雄 "「熬夜看电视看到很晚？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA01"),"True","img/CH_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH010"
    智纱 "「嗯，对，就是那样的」"
    "什么啊，跟我一样嘛。只是广播和电视的区别。"
    "话虽然这么说，现在智纱的样子好危险啊～。"
    "因为刚才撞上的只是个招牌，所以可以就一笑而过了，但是如果那是汽车或者自行车的话——想想就脊背发凉。"
    "好！"
    "周围也有几个在上学路上的的学生。在这里做这种事还是不好意思，不过……。"
    "我轻轻地握住了智纱的手。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB04"),"True","img/CH_LAB04A@2x.png") as lh0 zorder 100:
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCH03A_CH011"
    智纱 "「啊……」"
    志雄 "「脚底下晃晃悠悠的，可是很危险的哦。手拉着手走吧」"
    "这样的话，我就可以支撑着她了。就算有汽车或者自行车过来我也能保护她了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB03"),"True","img/CH_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH012"
    智纱 "「……嗯」"
    "智纱红着脸点了点头。和夏天的暑热不一样的热气，在我们周围扩散开来。"
    window hide
    play sound "SE01_12L"
    "我拉着智纱的小手，向前走着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA06"),"True","img/CH_LAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH013"
    智纱 "「总觉得是在被王子大人护送着一样……」"
    志雄 "「呃，被称为『王子大人』什么的，我还不够格呢」"
    "听了这些话，我更加地不好意思了。"
    志雄 "「要是太困的话，去保健室休息一下如何？　如果说是天热感觉不舒服的话，一定会同意你用那里的床小憩一会的」"
    "在男生中，这是经常使用的手段。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA01"),"True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH014"
    智纱 "「不用，没关系，没关系」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB01"),"True","img/CH_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH015"
    智纱 "「而且，保健室对于受伤的人、身体不舒服的人来说是必需的地方。如果我占用了床的话，真正生病的人或者受伤的人恐怕就该为难了」"
    "是该说守规矩呢，还是认真呢。很像智纱呢。"
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
    show expression "img/BG06AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG06AA@2x.jpg" as bg0 with dissolve
    play sound "SE08_10L"
    pause (32/32.0)
#FADE_IN 1
    voice "NCH03A_YU000"
    结乃？ "「早—上—好，塚本学长」"
    window hide
#SE_VOLC 1,64
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB02"),"True","img/YU_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    with dissolve
    play music "BGM10"
    "回过头去，那里是春日同学的身影。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB01"),"True","img/YU_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_YU001"
    结乃 "「今天也是和智纱学姐一起上学啊。感情还是和往常一样的好呢～{w=7}{nw}"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB03"),"True","img/YU_MAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    extend "……"
#MESX "……」%K%P"
    "春日同学的话说到一半，中断了。她的视线，落在了我和智纱的手——握在一起的两只手上。"
    voice "NCH03A_YU002"
    结乃 "「……塚本学长，智纱学姐。看来我是，小看了你们的关系呢」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAA02"),"True","img/YU_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    if not persistent.dictlist[43] and persistent.show_dict:
        $persistent.dictlist[43]=True
        show screen dict_pop(i=43)
    voice "NCH03A_YU003"
    结乃 "「学长和学姐的话，一定能和浜咲的那对传说中的情侣一较高下呢」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB01"),"True","img/YU_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_YU004"
    结乃 "「首先是作为传说的第一步，手牵手上学，把这个用广播告诉给全校吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB02"),"True","img/YU_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_YU005"
    结乃 "「再见！」"
    window hide
#MUS_VOL 0
#SE_VOLC 1,128
    play sound "SE01_00A"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    志雄 "「春日同学！？」"
    "我和智纱连忙叫住春日同学。"
    window hide
#SE_VOLC 1,64
#MUS_VOL 128
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAA01"),"True","img/YU_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_YU006"
    结乃 "「没关系的，我不会做坏事的」"
    志雄 "「不对不对不对，把它播出的那个时候就已经是做了坏事了！」"
    志雄 "「真的，请你饶了我吧」"
    "身为学长一再恳求学妹……我一点威严都没有了啊。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAA05"),"True","img/YU_MAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_YU007"
    结乃 "「嗯～，既然塚本学长都那么说了……没办法了啊"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAA04"),"True","img/YU_MAA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_YU008"
    结乃 "「而且，一旦播出的话智纱学姐说不定一发热就倒下去了」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC06"),"True","img/CH_LAC06A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAA04"),"True","img/YU_MAA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with move
#MOV_CHR_INIT 48
#MOV_CHR0 128,(320-224)
#MOV_CHR1 ,(320+96)
#MOV_CHR_GO 1
    "这么说着，看了看智纱那边，她嘴里哇哇地，一边说着不成句子的话，一边红着脸。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB01"),"True","img/YU_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_YU009"
    结乃 "「智纱学姐，没关系的啦。广播什么的是开玩笑的啦」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAC04"),"True","img/CH_LAC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH016"
    智纱 "「真，真的？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB02"),"True","img/YU_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_YU010"
    结乃 "「是真的。所以请你安心吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB01"),"True","img/YU_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_YU011"
    结乃 "「就这样，我早晨还有广播部的工作，再见了！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAC01"),"True","img/YU_MAC01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_YU012"
    结乃 "「还有，智纱学姐，关于那件事情，就请多多关照了哦！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA01"),"True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH017"
    智纱 "「啊，嗯。没问题的」"
    window hide
#MOV_CHR_INIT 48
#MOV_CHR0 ,(320-96)
#MOV_CHR1 0
#MOV_FOCUS_BG 512
#MOV_CHR_GO 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAA01"),"True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        xcenter 0.35
    with dissolve
#CHR_ALPC 1,128
    "春日同学听了智纱的回答，向着楼梯口那边走去了。"
    志雄 "「那件事是？」"
    voice "NCH03A_CH018"
    智纱 "「嗯。结乃说在暑假要做一个自主制作的广播节目，我已经决定帮她的忙了」"
    "两人都是广播部的成员，最近，智纱和春日同学的关系好像很好。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB06"),"True","img/CH_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    if not persistent.dictlist[60] and persistent.show_dict:
        $persistent.dictlist[60]=True
        show screen dict_pop(i=60)
    voice "NCH03A_CH019"
    智纱 "「好像结乃，是要报名参加浜咲FM的小广播竞赛呢」{w=3}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB01"),"True","img/CH_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#MESX "%K%P"
    志雄 "「啊，那个广播竞赛的话，我也知道的」"
    "虽说她也是广播部的成员，但要参加那个莫非是因为对广播有兴趣吗？"
    "或许，春日同学可能也在给某个广播节目投稿。"
    scene expression "img/BG83AA@2x.jpg" as bg_over zorder 2 with dissolve
    "在鞋柜换好鞋子。"
    play sound "SE07_03"
    "啊，因为没吃早饭就过来了，肚子……。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA01"),"True","img/CH_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH020"
    智纱 "「志雄君，是肚子饿了吗？」"
    志雄 "「早上没吃早饭就来了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA04"),"True","img/CH_MAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH021"
    智纱 "「哎？　为什么？」"
    志雄 "「那～个、有点睡过头了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAB05"),"True","img/CH_MAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    智纱 "「……」"
    voice "NCH03A_CH022"
    智纱 "「……」"
    "智纱闭口沉思了一小会，抬着眼，注视着我问到。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAB01"),"True","img/CH_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH023"
    智纱 "「还是让我，去给你做早饭吧？」"
    "虽说我们现在是在车站碰头，但这是第一次智纱说要每天早晨来我家给我做早饭。"
    志雄 "「不用，没关系的。为我做到那种程度的话，怎么说都不好吧」"
    "一早就来到我家叫我起床，还要为我做早饭，智纱可就必须起得相当早了。那对她来说负担太大了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA01"),"True","img/CH_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH024"
    智纱 "「不用客气的哦？」"
    志雄 "「没有没有，真的没关系的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC02"),"True","img/CH_MAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH025"
    智纱 "「可是……」"
    志雄 "「没事的啦」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC05"),"True","img/CH_MAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH026"
    智纱 "「那样啊……」"
    "总觉得智纱有些伤心，但是如果不坚持这么说的话，对她来说也太过于勉强了吧。"
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
#FADE_IN 0
    "…………。"
    "……。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
    scene expression "img/BG07AA3@2x.jpg" as bg0 with dissolve
    play sound "SE06_02"
    pause (128/32.0)
    play sound "SE08_09L"
    pause (32/32.0)
#FADE_IN 1
    "今天的课程在上午就结束了。"
    window hide
#SE_VOLC 1,64
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB01"),"True","img/TO_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    play music "BGM09"
    voice "NCH03A_TO000"
    亨 "「今天你也是，和智纱一起回去吗？　偶尔也绕道去玩玩嘛」"
    "轻浮的好友，用着轻浮的口气说着轻浮的事情。"
    志雄 "「在３年级的这种时期，公然说这种话，马上就会挨揍的啊」"
    "也许是心理作用，我感到周围杀气一般的视线向我们这里集中起来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_TO001"
    亨 "「不是挺好的嘛，偶尔也要把什么都忘掉，痛快地去玩吧。游戏中心的『Fighting Memories』的新作，好像已经出了」"
    志雄 "「说什么偶尔，总觉得亨你好像是每天都在玩……」"
    志雄 "「但是，总之今天不行。因为要去学习的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_TO002"
    亨 "「哈？　学习？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB04"),"True","img/TO_MAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_TO003"
    亨 "「你是认真的！？」"
    志雄 "「为啥你会那么吃惊啊。我都３年级了，为了应试做准备是当然的咯」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_TO004"
    亨 "「……这种话居然是从志雄你的嘴里说出来的，没想到啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA03"),"True","img/TO_MAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_TO005"
    亨 "「咳～。总觉得有种被晾在一边的感觉。我明明只把你一个人当成好伙伴的啊」"
    志雄 "「不要随便产生这种让人讨厌的连带意识啊」"
    志雄 "「今天是和智纱约好了要一起学习的啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA06"),"True","img/TO_MAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_TO006"
    亨 "「而且还是和恋人一起学习……在双重的意义上，我都被晾在一边了啊……」"
    window hide
    stop se
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,640
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA06"),"True","img/TO_MAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAA01"),"True","img/RI_MAA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter .75
    with move
#ROUTINE_STA
#CHR_POS_AUTOC 1,(320-160),F24,48
#CHR_POS_AUTOC 0,(320+160),F24,48
#CHR_ALP_AUTOC 0,128,1,F24,48
#ROUTINE_STP
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH03A_RI000"
    莉莉丝 "「志雄～、智纱来了啊」"
    "莉莉丝说着，眼睛看向门口的方向，智纱就站在那里。"
    志雄 "「啊，谢谢了。那就明天见了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAB01"),"True","img/RI_MAB01A@2x.png") as lh0 zorder (10+0):
        xcenter .75
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB01"),"True","img/TO_MAB01A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    voice "NCH03A_RI001"
    莉莉丝 "「嗯。明天见」"
    window hide
    stop music fadeout 1
#SE_VOLC 1,128
    play sound "SE03_12"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我已经做好了回去的准备，提起书包，站了起来。"
    window hide
#SE_VOLC 1,64
#BG_OVER_CHRC_F BG08AA,0,CH_LKA01
    play music "BGM03"
    voice "NCH03A_CH027"
    智纱 "「辛苦了」"
    志雄 "「嗯。那就一起回去吧……嗯？」"
    志雄 "「眼镜？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LKB04"),"True","img/CH_LKB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH028"
    智纱 "「啊，这个？」"
    "智纱很不好意思地摸着眼镜。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LKB03"),"True","img/CH_LKB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH029"
    智纱 "「隐形眼镜掉在地上了。沾上了些灰尘，正在清洗中」"
    voice "NCH03A_CH030"
    智纱 "「所以现在才戴眼镜了」"
    志雄 "「啊，是这样啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LKC04"),"True","img/CH_LKC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH031"
    智纱 "「……果然，很奇怪么？」"
    志雄 "「没，并没有那回事啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LKB03"),"True","img/CH_LKB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH032A"
    智纱 "「那样啊……{w=3}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LKB01"),"True","img/CH_LKB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH032B"
    extend "太好了」"
    "智纱从心底安心地叹了口气。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG03AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG03AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LKC01"),"True","img/CH_LKC01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
        xcenter .35
    with dissolve
    pause (32/32.0)
    play sound "SE05_15L"
    pause (32/32.0)
#FADE_IN 1
#BG_BLUR 0
#SE_VOLC 1,(64/2)
    志雄 "「即使这样，你也有不戴隐形眼镜的时候呢」"
    voice "NCH03A_CH033"
    智纱 "「嗯，有时候呢。掉下来的时候可不得了呢」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LKC02"),"True","img/CH_LKC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH034"
    智纱 "「没有戴着镜片本来就看不清楚，又小，还是透明的，就更难找到了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LKC04"),"True","img/CH_LKC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH035"
    智纱 "「而且，脸贴在地上，去找一个镜片让人多不好意思啊……」"
    "智纱苦笑着。这次找隐形眼镜好像也十分辛苦。"
    "……我如果在那的话，也能给她帮忙的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LKC01"),"True","img/CH_LKC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH036"
    智纱 "「这种时候，果然还是觉得眼镜也挺方便的啊」"
    志雄 "「这么说来，智纱你也说过，隐形眼镜很难用的」"
    "确实有着怕放进眼睛里啊，忘记戴隐形眼镜啊，之类的问题。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LKA01"),"True","img/CH_LKA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH037"
    智纱 "「嗯。不过最近已经习惯了」"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "推荐她戴眼镜":
            $F7=0
        "戴隐形眼镜就好":
            $F7=1
    if F7==0:
        jump L_NCH03A_SEL00_A
    if F7==1:
        jump L_NCH03A_SEL00_B
label L_NCH03A_SEL00_A:
    $F103=1
#RSET F103
##SETACHIEVE 27
    志雄 "「如果隐形眼镜难用的话，换成眼镜怎么样？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LKC03"),"True","img/CH_LKC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH038A"
    智纱 "「嗯～……{w=3}{nw}"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LKC04"),"True","img/CH_LKC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH038B"
    extend "可是，我觉得我不太适合戴眼镜的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LKC02"),"True","img/CH_LKC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH039"
    智纱 "「我担心戴上了眼镜是不是会变得有点奇怪」"
    志雄 "「是吗？　我倒是没那么觉得」"
    志雄 "「我觉得和你挺合适的呢。戴着眼镜的智纱，我也很喜欢呢」"
    "智纱是因为本身就很漂亮了所以戴什么都好看……我是这样想的，这是作为男朋友的偏爱吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LKB03"),"True","img/CH_LKB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH040"
    智纱 "「这，这样啊……喜欢眼镜啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LKB01"),"True","img/CH_LKB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH041"
    智纱 "「这样的话，就戴回眼镜看看吧……」"
    jump L_NCH03A_SEL00_X
label L_NCH03A_SEL00_B:
#RSET F103
    志雄 "「这样啊。能习惯就好了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LKB01"),"True","img/CH_LKB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH042"
    智纱 "「嗯。最近比起眼镜来说，可能隐形眼镜用起来更方便了。戴眼镜的话，视野就狭窄了，有点不太好走路了」"
    "哎，是那样的吗。"
    志雄 "「不过如果走起路来不方便的话，就像早晨一样牵着你的手如何？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LKA03"),"True","img/CH_LKA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCH03A_CH043"
    智纱 "「不，不用！　没关系的啦！」"
#REMOVE_REEK_CHR 0
    "智纱连忙摇了摇头。"
    jump L_NCH03A_SEL00_X
label L_NCH03A_SEL00_X:
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG15AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG15AA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
#FADE_IN 1
    "和智纱暂且在澄空车站分开，我回到家里整理学习用品。"
    window hide
    play sound "SE00_04"
    pause (32/32.0)
    "啊，来得好快。"
    志雄 "「来了来～了」"
    window hide
    stop se fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/OIBG012A@2x.png" as bg0 zorder 0 with dissolve
    scene expression "img/BG33AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA05"),"True","img/CH_MBA05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_IN 1
    voice "NCH03A_CH044"
    智纱 "「呜……诶」"
    "智纱把抱着的大旅行袋放到了地上。"
    window hide
    play sound "SE03_47"
    with vpunch
#QUA3_BG 
    "声音听起来相当有分量，地板摇晃的震动声，在脚下响动着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBC03"),"True","img/CH_MBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH045"
    智纱 "「哈……」"
    "智纱从书包的重量中解放了出来，大声地叹着气。"
    志雄 "「那个，这是要去哪里旅游啊？」"
    window hide
    play music "BGM03"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA04"),"True","img/CH_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH046"
    智纱 "「哎？　是要学习的啊？」"
    "这样啊，看到这个包不由得就想问去哪里旅游了。"
    志雄 "「这个包里装了什么？」"
    "一边说着，我一边去拿书包的提手。在要提起来的瞬间，感到了沉甸甸的感觉。"
    "虽说没到拿着它就走不了路的程度，但是让女孩子来搬运的话也是相当地费力了。更不用说在这火热的天气里。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA01"),"True","img/CH_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH047A"
    智纱 "「一想到是有用的东西，就塞了进去，{w=3}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBB06"),"True","img/CH_MBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH047B"
    extend "这个也要呢，这个也用得到啊，"
#MESA A_CH_CH,NCH03A_CH047B,"这个也要呢，这个也用得到啊，"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBB01"),"True","img/CH_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH047C"
    extend "然后就越来越多了」"
    志雄 "「有用……？」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE03_88"
    pause (32/32.0)
    "我捏住书包的拉链，慢慢地拉开一个口……。"
    stop se
    志雄 "「哇」"
    "从打开的口子往里看，参考书、参考书、大学向导书、参考书……。到底有多少本啊？"
    "特别是大学向导书，因为一本一本的都有词典那么厚，难怪相当地重了。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBB02"),"True","img/CH_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH048"
    智纱 "「因为志雄君说过，还没有决定志愿。为了帮你选志愿，我把资料都拿来了哟」"
    "智纱擦着额头上的汗。她的手心，有一道因为握着书包提手，而压出的显眼痕迹，已经有点发红了。"
    志雄 "「拿这么多东西过来，一定很辛苦吧？　告诉我的话，我就会去接你的啊」"
    "那样的话，搬运个东西之类的活我应该还是能办到的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA03"),"True","img/CH_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCH03A_CH049"
    智纱 "「没事，不用在意的！　完全没事的啊」"
#REMOVE_REEK_CHR 0
    "智纱摆着双手，表示自己没事。"
    "但是，智纱越是在那里假装自己没事，我的心就越是因为罪恶感而一点一点地疼了起来。"
    "真的……。"
    window hide
#FILT_PRI 5
#FILT_IN 48,0,COL_DARK2
#BG_BLUR 0
    "智纱真的是一个人过于努力了。明明不管是打电话还是发短信，告诉我一声我就会去帮忙的。"
    "难道我，真的是靠不住么？　如果是这样的话，我还是有点失落的。"
    window hide
#FILT_OUT 48
#FILT_PRI 1
    志雄 "「哈……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA04"),"True","img/CH_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "就像是要把体内积存的毒素吐出来一样，我重重地叹了口气。"
    志雄 "「那，我把这些东西搬到房间里去」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBB04"),"True","img/CH_MBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH050"
    智纱 "「啊，那个让我……」"
    志雄 "「好啦，智纱你就稍微休息会吧」"
    "我拿起提包，打断了智纱的话。我不想再让自己有罪恶感了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBB06"),"True","img/CH_MBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH051"
    智纱 "「啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBB01"),"True","img/CH_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH052"
    智纱 "「那，我去做午饭了。还没吃吧？」"
    志雄 "「好了啦，喝点什么休息会」"
    "如果说是出现了脱水症状确实有些夸张，不过我认为她还是先摄取一点水份比较好。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBC04"),"True","img/CH_MBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH053"
    智纱 "「可是……」"
    志雄 "「没有什么可是的！　懂了吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBC03"),"True","img/CH_MBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH054"
    智纱 "「……是」"
    "智纱的肩膀耷拉了下来，点了点头。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#FADE_IN 0
    "我一边把书包搬到房间里，一边在心里叹着气。"
    "…………。"
    "……。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
    scene expression "img/BG15AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
#IF F103!0, GOTO L_NCH03A_BRA00_A
    if F103!=0:
        jump L_NCH03A_BRA00_A
    jump L_NCH03A_BRA00_B
label L_NCH03A_BRA00_A:
    "吃过午饭以后，我们转移到了我的房间。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBB06"),"True","img/CH_MBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH055A"
    智纱 "「啊，对了。{w=3}{nw}"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBB01"),"True","img/CH_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH055B"
    extend "用下洗脸池可以吗？」"
    志雄 "「？　是可以」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBB03"),"True","img/CH_MBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH056"
    智纱 "「那……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE00_06"
    "……？"
    window hide
#FADE_OUT 1
    pause (64/32.0)
#FADE_IN 1
    play sound "SE00_05"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MLC04"),"True","img/CH_MLC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「嗯？　换成眼镜了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MLC01"),"True","img/CH_MLC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH057"
    智纱 "「嗯。我觉得在学习的时候，戴眼镜的话眼睛比较不容易疲劳吧」"
    "啊哈哈，智纱的脸上不知怎地，浮现了在敷衍一般的做作的笑容。"
    "但是，智纱在学习的时候戴着眼镜的样子可是从来没见过啊……。难道是在从学校回家的路上，我说过比较喜欢戴眼镜的样子的缘故吗？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MLA03"),"True","img/CH_MLA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH058A"
    智纱 "「那～个，{w=3}{nw}"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MLB05"),"True","img/CH_MLB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH058B"
    extend "咳。"
#MESA A_CH_CH,NCH03A_CH058B,"咳。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MLB01"),"True","img/CH_MLB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH058C"
    extend "那，我们开始学习吧」"
    "以这仿佛是故意的一声咳嗽为转折，话题改变了。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    voice "NCH03A_CH059"
    智纱 "「那～个，首先是……」"
    "智纱把放在房间角落里的旅行包打开。然后从里面取出了几本参考书，摆在了桌子上。"
    jump L_NCH03A_BRA00_X
label L_NCH03A_BRA00_B:
    "吃过午饭以后，我们来到了我的房间里。智纱把装在旅行包里的参考书一本一本地取了出来，摊在了桌子上。"
    jump L_NCH03A_BRA00_X
label L_NCH03A_BRA00_X:
    window hide
#BG_ERSWC 1,3,BG_NOFADE
#BG_CROSS_OVER 0,2,EXBG10AB,(60),0,640,448
#BG_PRIC 0
#BG_PRIC 2
    scene expression "img/EXBG10AB@2x.png" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_MGNC 0,CH_ZLA01,CH_ZBA01
#BG_ERSWC 1,3
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBA01"),"not F103==0","img/CH_ZLA01A@2x.png","True","img/CH_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH060"
    智纱 "「志雄君的志愿是上国立、公立大学吧？」"
    志雄 "「嗯～，是的」"
    "理由非常地单纯，因为国立、公立大学的学费比较便宜，在经济上比较轻松。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB05"),"not F103==0","img/CH_ZLB05A@2x.png","True","img/CH_ZBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH061"
    智纱 "「然后因为你是理科，需要的就是数学、理科和英语了」"
    "智纱从摊在桌子上的参考书中，拣起了几本。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB01"),"not F103==0","img/CH_ZLB01A@2x.png","True","img/CH_ZBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH062"
    智纱 "「数学照着这本参考书复习是最好的了」"
    voice "NCH03A_CH063"
    智纱 "「还有，志雄君的理科选的是物理和化学吧？」"
    志雄 "「嗯」"
    "理科必须从物理、生物、化学中选择两科进行学习。"
    "智纱选择的是物理和生物，但我选择的是物理和化学。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB05"),"not F103==0","img/CH_ZLB05A@2x.png","True","img/CH_ZBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH064"
    智纱 "「物理的话用这本参考书，化学是这边这个吧……」"
    "然后智纱又伸手去拿别的参考书了。"
    志雄 "「智纱，相当地清楚呢。好厉害啊」"
    "像我这样的，不管是参考书还是习题集，都只有从学校拿到的那一部分。学习用的教材，有这么多种类的啊……。"
    "而且，带来的参考书的内容，智纱好像基本上都理解了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB01"),"not F103==0","img/CH_ZLB01A@2x.png","True","img/CH_ZBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH065"
    智纱 "「嗯，我有时会在网上查找报考相关的东西。在网页上读些报考的体验记录什么的，那里面记载了有哪些参考书比较好」"
    "智纱像是在好好地收集着报考相关的信息啊。果然和我不一样。"
    "可是，如果是这样的话为什么到现在她还没有决定志愿呢……。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB05"),"not F103==0","img/CH_ZLB05A@2x.png","True","img/CH_ZBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH066"
    智纱 "「还有」"
    "智纱这次从旅行包里取出的，是装点心的盒子。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB01"),"not F103==0","img/CH_ZLB01A@2x.png","True","img/CH_ZBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH067"
    智纱 "「学习的时候需要适量的糖分」"
    if not persistent.dictlist[63] and persistent.show_dict:
        $persistent.dictlist[63]=True
        show screen dict_pop(i=63)
    "在便利店一类的地方经常有卖的巧克力点心。好像是一个叫『Monsieur゛MushWorld』的动画的关联商品。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB05"),"not F103==0","img/CH_ZLB05A@2x.png","True","img/CH_ZBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH068"
    智纱 "「大脑在活动的时候需要的营养只是糖分，所以在学习之类的时候补充一些糖分效率会更高的」"
    志雄 "「是那样的吗？　还特意为我买来」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB02"),"not F103==0","img/CH_ZLB02A@2x.png","True","img/CH_ZBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH069"
    智纱 "「嗯」"
    志雄 "「……但是，其实只是为了买那些赠品才买了的吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBB03"),"not F103==0","img/CH_ZLB03A@2x.png","True","img/CH_ZBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#CHR_MGNC 0,CH_ZLA03,CH_ZBA03
#REEK_CHR 0
    voice "NCH03A_CH070"
    智纱 "「没，没有那种事啊！」"
#REMOVE_REEK_CHR 0
    "现在大概是在促销期间，购买后好像能得到蘑菇ＰＯＫＯ手机链的赠品。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBC01"),"not F103==0","img/CH_ZLC01A@2x.png","True","img/CH_ZBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#CHR_MGNC 0,CH_ZLC01,CH_ZBC01
    voice "NCH03A_CH071"
    智纱 "「那。就，就开始学习吧」"
    "像是要敷衍过去似的，智纱取出了笔记用具。"
    志雄 "「啊，那就开始吧」"
    "我忍住苦笑地点了点头，还是不要再继续为难她比较好。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "意识回到了参考书这边。智纱给我带来的，比我一直以来用过的要易懂得多。"
    play sound "SE03_44"
    "而且在例题和解说之中，还特别用容易理解的话写了出来。"
    "再加上智纱给我带来的笔记本，都总结得很好，很有用。有英语、数学、物理、化学４科的份。"
    志雄 "「好的，那就从数学开始吧……」"
    志雄 "「……」"
    "在这里用三角函数的定理，ｓｉｎ、ｃｏｓ、ｔａｎ……。"
    志雄 "「……智纱，这个问题的解法你知道吗？」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLA02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBA02"),"not F103==0","img/CH_ZLA02A@2x.png","True","img/CH_ZBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    if F103!=0:
        jump L_NCH03A_BRA01_A
    jump L_NCH03A_BRA01_B
label L_NCH03A_BRA01_A:
    "智纱稍稍调整了一下眼镜的位置，看向参考书上我指的地方。"
    jump L_NCH03A_BRA01_X
label L_NCH03A_BRA01_B:
    "智纱抬起头，看向参考书上我指的地方。"
    jump L_NCH03A_BRA01_X
label L_NCH03A_BRA01_X:
#CHR_MGNC 0,CH_ZLA01,CH_ZBA01
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_ZLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_ZBA01"),"not F103==0","img/CH_ZLA01A@2x.png","True","img/CH_ZBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH072"
    智纱 "「啊，这题。这个是这样……」"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with dissolve
#BG_COLC 2,0,0,0,128
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    stop music fadeout 1
#FADE_IN 0
    "……。"
    "…………。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
#BG_COLC 2,128,128,128,128
#FADE_IN 1
    志雄 "「啊，好累啊～」"
    "用力地伸了伸绷紧的身体。看了看表，从开始学习到现在已经差不多有２个小时了。"
    "平常没有这么长时间地学习过，现在已经相当累了。"
    志雄 "「……嗯？」"
    window hide
#BG_SET_BACK
#BG_PRIC 0
#BG_INIC 1
#IF F103!0, GOTO IF_ELSE1
    if F103!=0:
        jump NCH03A_IF_ELSE1
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH03A")]=True
    show expression "img/EVN_CH03A@2x.jpg" as bg1 with dissolve
    jump NCH03A_IF_END1
label NCH03A_IF_ELSE1:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH03B")]=True
    show expression "img/EVN_CH03B@2x.jpg" as bg1 with dissolve
label NCH03A_IF_END1:
    play music "BGM13"
    voice "NCH03A_CH073"
    智纱 "「……呼～，呼……」"
    "注意到的时候，智纱已经趴在了桌子上，呼呼地睡着了。"
    志雄 "「睡着了，吗……」"
    "好像是昨天熬夜了的缘故啊。"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "叫智纱起来":
            $F7=0
        "就先让她继续睡":
            $F7=1
    if F7==0:
        jump L_NCH03A_SEL01_A
    if F7==1:
        jump L_NCH03A_SEL01_B
label L_NCH03A_SEL01_A:
    志雄 "「智纱」"
    "我把手伸向智纱，想要叫醒她……。"
    window hide
#BG_HIDEC 3
    "在那里注意到了，智纱手边的教科书的下面，放着一张活页纸。"
    志雄 "「这个是……？」"
    "我尽量不吵醒智纱，轻轻地把活页纸用手拉了出来。"
    jump L_NCH03A_SEL01_X
label L_NCH03A_SEL01_B:
    $F1+=1
    "没有必要不讲道理地把她叫起来。智纱也很累了吧。"
    "我就让智纱继续睡着，一个人接着学习下去了。光是依靠智纱也不好。"
    window hide
#FADE_OUT 1
#BG_COLC 1,0,0,0,128
#FADE_IN 0
    "…………。"
    "……。"
    window hide
#FADE_OUT 0
#BG_COLC 1,128,128,128
#FADE_IN 1
    voice "NCH03A_CH074"
    智纱 "「……呼，呼……」"
    
    志雄 "「……」"
    voice "NCH03A_CH075"
    智纱 "「……呼，呼……」"
    志雄 "「……」"
    "呜，没法集中啊……。"
    "在眼前有人睡觉的情况下，想不到自己一个人继续学习这种事，竟然是那么的困难。"
    "至今为止我在图书室多次睡着过，认真学习的人们，真是对不起了。"
    window hide
#BG_SHOWC 3
    志雄 "「……」"
    "我望着智纱的睡脸。"
    "先捅一下她的脸试试。"
    window hide
    voice "NCH03A_CH076"
    智纱 "「嗯嗯……」"
    "没有要起来的样子。"
    voice "NCH03A_CH077"
    智纱 "「莉莉丝……那样踢的话……佐贺君好可怜……」"
    "到底，做了什么样的梦啊？"
    "忽然想了起来。以前，在广播上有人发了以睡眠学习为内容的邮件。根据那个，用声音把信息传给睡着的人……。"
    "我把嘴凑到智纱的耳边，小声说。"
    志雄 "「其实佐贺亨，被莉莉丝踢了他会高兴的。他就是有这种兴趣……」"
    window hide
    voice "NCH03A_CH078"
    智纱 "「……这样啊……佐贺君……好可怜……」"
    "虽然同是「好可怜」，但也已经和前面说的那个「好可怜」意思不一样。"
    志雄 "「好了」"
    "有点好玩。嗯，满足了。"
    志雄 "「切，我在做什么无聊的事情浪费时间啊」"
    window hide
#BG_HIDEC 32
    "赶快继续学……。"
    "就在这样想的时候，忽然注意到了智纱手里的活页本。"
    "这个是什么啊？"
    jump L_NCH03A_SEL01_X
label L_NCH03A_SEL01_X:
    "那个活页本，好像是上课用的笔记。打开来看看，所有的科目的课程内容，智纱都用小小的字写在了上面。"
    "那个，等等？　这个是上课用的笔记？"
    "可是……。"
    "我看了看自己手边的笔记。那，这边的不是上课用的笔记吗？"
    window hide
#BG_SHOWC 4
    voice "NCH03A_CH079"
    智纱 "「……志雄君的……科目是……数学和……物理……」"
    "从睡着的智纱的口中，透出了我要备考的科目。"
    "啊，这样啊。"
    "倏地一下，我明白了。"
    window hide
    hide bg1 with dissolve
    "这个不是上课用的笔记，是塚本志雄专用的笔记本啊。智纱为了我，特地做的……。"
    "想想看，智纱没有选择化学这门课。所以化学课上用的笔记什么的是不可能存在的。"
    "莫非昨天智纱熬了夜，是为了做这本笔记的吗……。"
    window hide
#BG_SET_BACK 
#BG_INIC 3
#BG_PRI 3
#BG_ALPC 3
#BG_UVC 3,0,512,640,448
    show expression "img/BG01EA@2x.jpg" as bg3 zorder 8
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112,128
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB06"),"True","img/CH_LAB06A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#MUS_VOL 64,16
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 0
#BG_ALPC 2
#BG_ALPC 3,128
#CHR_ALPC 0,128
    hide bg1 with dissolve
#BG_BLUR 3
    voice "NCH02A_CH073_K"
    智纱 "「啊，可是，因为需要做很多的准备，是不是从明天开始比较好……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_LAB01"),"True","img/CH_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH02A_CH074_K"
    智纱 "「那么，我得早点回去了」"
    window hide
#BG_INIC 1
#BG_PRI 1
    hide bg3
#BG_PRI 3
#BG_UVC 3,0,0,640,448
    hide lh0
#BG_ALPC 0,128
#BG_ALPC 2,128
    hide bg1
    scene expression "img/BG15AA@2x.jpg" as bg0 with dissolve
#MUS_VOL 128
    "轻轻地叹了口气。智纱真是，为什么要这样……。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#IF F103!0, GOTO IF_ELSE2
    if F103!=0:
        jump NCH03A_IF_ELSE2
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH03A")]=True
    show expression "img/EVN_CH03A@2x.jpg" as bg1 with dissolve
    jump NCH03A_IF_END2
label NCH03A_IF_ELSE2:
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH03B")]=True
    show expression "img/EVN_CH03B@2x.jpg" as bg1 with dissolve
label NCH03A_IF_END2:
    "我轻轻地碰了下智纱的身体。果然是很累了吗，智纱没有要醒来的样子。"
    "如果趴在桌子上睡觉的话，疲劳和睡眠不足也得不到恢复吧。至少也得让她睡在床上吧。"
    志雄 "「……」"
    "但是，擅自接触女生的身体，这样做好吗。"
    voice "NCH03A_CH080"
    智纱 "「呼……呼……」"
    "智纱呼呼地，睡得正香，一点防备都没有。"
    志雄 "「……」"
    window hide
#BG_ERSWC 0,3,BG_NOFADE
#BG_POSC 0,0,0,640,448
#BG_POSC 3,0,0,640,448
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG15AA@2x.jpg" as bg0 zorder 0 with dissolve
    hide bg1
    with dissolve
    "哎，这么犹豫着也不是办法！"
    "我尽可能轻的接触着智纱的身体，把她抱了起来。"
    voice "NCH03A_CH081"
    智纱 "「嗯嗯……」"
    "智纱的嘴里发出了声音。醒了吗……我这么想着，但是她没有睁开眼。"
    play sound "SE03_92"
    "我把智纱横放在了床上，并给她盖上了毛巾毯。"
    志雄 "「好了」"
    "继续学习吧。智纱为我准备了这么多，我也必须做出相应的努力啊。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
#FADE_IN 0
    "……。"
    "…………。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
    scene expression "img/BG15EA@2x.jpg" as bg0 with dissolve
    play sound "SE02_00L"
#FADE_IN 1
    pause (32/32.0)
    "电话？"
    if not persistent.dictlist[10] and persistent.show_dict:
        $persistent.dictlist[10]=True
        show screen dict_pop(i=10)
    "看了看手机的画面，显示的名字是『塚本雄吾』。是老爸。有什么事情吗？"
    "我为了不吵醒智纱，走出了房间。"
    window hide
    show expression "img/BG33AA@2x.jpg" as bg0 with dissolve
    scene expression "img/BG33AA@2x.jpg" as bg0 with dissolve
    pause (16/32.0)
    play sound "SE02_03"
    play music "OBGM17"
    voice "NCH03A_YG000_K"
    雄吾 "「喂，喂，是志雄吗？」"
    志雄 "「什么事啊，老爸？」"
    voice "NCH03A_YG001_K"
    雄吾 "「喔，光听声音就能认出来是我了吗。我很高兴哦」"
    志雄 "「光听声音……手机可是能把打来电话的人的名字显示出来的好吧」"
    voice "NCH03A_YG002_K"
    雄吾 "「啊，是那样啊」"
    "我知道老爸在苦笑。"
    志雄 "「那，有什么事？」"
    if not persistent.dictlist[12] and persistent.show_dict:
        $persistent.dictlist[12]=True
        show screen dict_pop(i=12)
    voice "NCH03A_YG003_K"
    雄吾 "「其实，我和香里，正计划着一次旅行」"
    志雄 "「旅行？」"
    voice "NCH03A_YG004_K"
    雄吾 "「啊。香里的熟人里，有人在一个旅游胜地的镇上开了一间旅馆。准备要去那边看看」"
    志雄 "「就像新婚旅行一样？」"
    voice "NCH03A_YG005_K"
    雄吾 "「新婚旅行么。嘛，就算是吧。只是和最近流行的海外旅行相比，是个令人惭愧的小旅行」"
    "我仿佛能看见，电话对面的老爸的脸上，浮现了不好意思的神色。"
    志雄 "「不是挺好嘛。玩得高兴点啊」"
    "老爸和香里阿姨——莉莉丝的母亲——再婚这件事，我有过很多想法。"
    "但是现在，我觉得，只要他们两人能幸福就好了。"
    voice "NCH03A_YG006_K"
    雄吾 "「啊，还有呢。如果没有什么预定的话，你和莉莉丝也都一起来吧，我是这么想的」"
    志雄 "「我和莉莉丝也去？」"
    "这么看来，与其说是新婚旅行不如说是家族旅行了。由于香里阿姨和老爸结婚了，从旁人看来我和莉莉丝也像姐弟一样了。"
    "虽然这么说但是年级也都一样，莉莉丝作为姐姐的感觉是一点也没有。"
    志雄 "「什么时候出发？」"
    voice "NCH03A_YG007_K"
    雄吾 "「28日。怎么样，你也来吗？」"
    志雄 "「这样啊……我是没关系的，莉莉丝就不知道了。旅行的事情，已经告诉她了吗？」"
    voice "NCH03A_YG008_K"
    雄吾 "「不，还没。就由你来问问，莉莉丝是来还是不来，好吗」"
    志雄 "「啊，可以啊」"
    voice "NCH03A_YG009_K"
    雄吾 "「那就拜托了」"
    window hide
    play sound "SE02_03"
#FADE_OUT 1
#FADE_IN 0
    "我挂断了和老爸的电话，给莉莉丝打了电话过去。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
    play sound "SE02_02L"
    pause (128/32.0)
#FADE_IN 1
    stop se
    voice "NCH03A_RI002_K"
    莉莉丝 "「志雄？」"
    志雄 "「现在，方便说话吗？」"
    "莉莉丝经常在文子婆婆开的小饭店帮忙，所以如果是正在帮忙的话就不好了。"
    voice "NCH03A_RI003_K"
    莉莉丝 "「没关系的哦，现在店里也是在休息。那么，什么事？」"
    志雄 "「莉莉丝你28日开始有空吗？」"
    志雄 "「老爸和香里阿姨，好像在计划一个带住宿的旅行。他们说，如果方便的话，莉莉丝和我也一起去」"
    voice "NCH03A_RI004_K"
    莉莉丝 "「啊，所以说是从28日开始啊」"
    voice "NCH03A_RI005_K"
    莉莉丝 "「嗯～……对不起。那天出发好像正好不行」"
    志雄 "「是有什么安排吗？」"
    voice "NCH03A_RI006_K"
    莉莉丝 "「和佐贺君约好了，28日的晚上一起去演唱会的。以一种快要跪下来的势头求我的，取消了的话还是有点不好呢」"
    志雄 "「这样啊。这就没办法了啊」"
    "这么说来，亨是说过他为了在这个暑假增进和莉莉丝的关系已经制定好了计划。邀请她去演唱会，也是其中的一环吧。"
    "因为音乐是莉莉丝和亨共同的兴趣，所以从那里突破吗。你还真考虑过啊，亨。"
    voice "NCH03A_RI007_K"
    莉莉丝 "「因此，我就没法去了。可是，好不容易空出来的人选，把智纱叫上怎么样？」"
    voice "NCH03A_RI008_K"
    莉莉丝 "「我想智纱，能和你一起去旅行的话，一定会非常地高兴的」"
    "邀请智纱去旅行，吗。"
    "嗯，确实是那样的。以前亨也说过，这是对智纱的报恩。"
    志雄 "「啊，我去约她试试吧」"
    voice "NCH03A_RI009_K"
    莉莉丝 "「嗯。再见」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_PRIC 0
#BG_PRIC 1
#EFF_PRI 0
    scene expression "img/NIMG01C@2x.png" as bg1 zorder 1 with dissolve
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
#EFF_STAC 0,CLOUD_C,EFF_SKIP

#ROUTINE_STA
    hide bg0 with dissolve
#BG_PRIC 0
#BG_PRIC 1
#EFF_PRI 0
#ROUTINE_STP
    "挂断了电话，再一次给老爸拨去电话。"
    "告诉他莉莉丝不去了，还问了他邀请智纱一起去可不可以，他简简单单地回答了一句「不介意的」。"
    "和智纱去旅行……。"
    "虽说交往开始已经半年以上了，但是也没有和智纱一起出过，需要在外面过夜的远门。这么一想，我心里非常高兴。"
    "当然，不能不问问智纱的意见，是不是也打算去。"
    window hide
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,(640/8),(448/8),((640/8)*7),((448/8)*7)
    scene expression "img/BG15EA@2x.jpg" as bg0 zorder 0 with dissolve
    play sound "SE00_05"
#FADE_IN 1
    voice "NCH03A_CH082"
    智纱 "「嗯……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+224)
#CHR_MGNC 0,CH_MLC03,CH_MBC03
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLC03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBC03"),"not F103==0","img/CH_MLC03A@2x.png","True","img/CH_MBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「抱歉，吵醒你了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBC05"),"not F103==0","img/CH_MLC05A@2x.png","True","img/CH_MBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH03A_CH083"
    智纱 "「嗯……？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBA03"),"not F103==0","img/CH_MLA03A@2x.png","True","img/CH_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#CHR_MGNC 0,CH_MLA03,CH_MBA03
#REEK_CHR 0
    voice "NCH03A_CH084"
    智纱 "「啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLC06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBC06"),"not F103==0","img/CH_MLC06A@2x.png","True","img/CH_MBC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REMOVE_REEK_CHR 0
#CHR_MGNC 0,CH_MLC06,CH_MBC06
    voice "NCH03A_CH085"
    智纱 "「我，难道是睡着了？」"
    志雄 "「嗯」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBB03"),"not F103==0","img/CH_MLB03A@2x.png","True","img/CH_MBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#CHR_MGNC 0,CH_MLB03,CH_MBB03
    "是对自己睡着了感到不好意思吗，智纱红着脸低下了头。"
    voice "NCH03A_CH086"
    智纱 "「对，对不起……。明明是我说过要一起复习的……」"
    志雄 "「别在意。多亏了你借给我的笔记和参考书，已经有很大的进展了」"
    "当然，如果有智纱教给我的话说不定就会更容易懂了。"
    "但是，智纱为我准备这些准备到那么晚。所以说要感谢她，完全没有责备她的理由。"
    志雄 "「还有呢，很少有机会能看到智纱的睡颜的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBB04"),"not F103==0","img/CH_MLB04A@2x.png","True","img/CH_MBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#CHR_MGNC 0,CH_MLB04,CH_MBB04
    voice "NCH03A_CH087"
    智纱 "「那，那个是……」"
    "智纱的脸红度，又上升了。"
    志雄 "「先不说那个，差不多到该回去的时候了吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBA04"),"not F103==0","img/CH_MLA04A@2x.png","True","img/CH_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#CHR_MGNC 0,CH_MLA04,CH_MBA04
    voice "NCH03A_CH088"
    智纱 "「啊」"
    "看到窗外的景色还有时钟，看来是注意到了现在大概是什么时候了。"
    "已经到了差不多该回去的时间了。太晚的话，智纱的父母会担心的吧。"
    志雄 "「那，我送你到车站吧」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MBA01"),"not F103==0","img/CH_MLA01A@2x.png","True","img/CH_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#CHR_MGNC 0,CH_MLA01,CH_MBA01
    voice "NCH03A_CH089"
    智纱 "「嗯」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG03EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG03EA@2x.jpg" as bg0 with dissolve
    play sound "SE05_13L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,64
    "现在的天气仍然很热，就算是到了傍晚，仅仅走几步也会出汗。"
    window hide
#SE_VOLC 1,(64/2)
#CHR_INIC 0
#CHR_COLC 0,128,120,112,128
#CHR_MGNC_F 0,CH_LLB01,CH_LBB01,(320+96)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB01"),"not F103==0","img/CH_LLB01A@2x.png","True","img/CH_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
    志雄 "「智纱你月底的时候有空吗？」"
    voice "NCH03A_CH090"
    智纱 "「月底？」"
    志雄 "「嗯，28日。我父母暂且是定下了一个，从那天开始，去旅行的计划」"
    志雄 "「而且还问我要不要也一起去，我想如果方便的话，智纱也一起去怎么样」"
    "关于老爸和香里阿姨的事情，也已经在一定程度上和智纱讲过了。因为也有香里阿姨是莉莉丝的母亲这一层关系，所以我觉得告诉智纱会比较好。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB02"),"not F103==0","img/CH_LLB02A@2x.png","True","img/CH_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
#CHR_MGNC 0,CH_LLB02,CH_LBB02
    voice "NCH03A_CH091"
    智纱 "「和志雄君去旅行？　嗯，我去{w=3}{nw}"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBB03"),"not F103==0","img/CH_LLB03A@2x.png","True","img/CH_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
    extend "——"
#VO_WAT VO_WAIT_START
#CHR_MGNC 0,CH_LLB03,CH_LBB03
#MESX "├┤」%K%P"
    "智纱的话没有说完，又咽了回去。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC02"),"not F103==0","img/CH_LLC02A@2x.png","True","img/CH_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
#CHR_MGNC 0,CH_LLC02,CH_LBC02
    voice "NCH03A_CH092"
    智纱 "「但是，我去的话好吗？　那个是家庭旅行的吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC01"),"not F103==0","img/CH_LLC01A@2x.png","True","img/CH_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
#CHR_MGNC 0,CH_LLC01,CH_LBC01
    voice "NCH03A_CH093"
    智纱 "「好不容易有个只有自家人的旅行……」"
    "智纱这样讲话的口气，总觉得有些寂寞。"
    "明明不用这么客气的……。"
    志雄 "「没事，我已经问过老爸了，他说完全不介意的。而且智纱已经……」"
    "本想说我们不是已经像家人一样了嘛，却又把话咽了下去。那句台词还是太不好意思了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC04"),"not F103==0","img/CH_LLC04A@2x.png","True","img/CH_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
#CHR_MGNC 0,CH_LLC04,CH_LBC04
    voice "NCH03A_CH094"
    智纱 "「怎么了？」"
    志雄 "「没，什么事也没有。不说这个，你觉得怎样？」"
    志雄 "「智纱如果能来的话，我也会很高兴的」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA05"),"not F103==0","img/CH_LLA05A@2x.png","True","img/CH_LBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
#CHR_MGNC 0,CH_LLA05,CH_LBA05
    voice "NCH03A_CH095"
    智纱 "「所、所以我要去的！」"
    "智纱兴高采烈地回答着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLC05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBC05"),"not F103==0","img/CH_LLC05A@2x.png","True","img/CH_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
#CHR_MGNC 0,CH_LLC05,CH_LBC05
    voice "NCH03A_CH096"
    智纱 "「啊，但还是要找爸爸妈妈问一问……」"
    "但是，智纱在刚才那一瞬间展现出来的势头，已经像开了一个洞的气球一样，瘪了。"
    "果然还是因为要在外面过夜……也许从父母那里不是那么容易就能得到一句ＯＫ的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LLA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LBA01"),"not F103==0","img/CH_LLA01A@2x.png","True","img/CH_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
#CHR_MGNC 0,CH_LLA01,CH_LBA01
    voice "NCH03A_CH097"
    智纱 "「答复还要再等一等」"
    voice "NCH03A_CH098"
    智纱 "「我想，大概是没问题的。我绝对会去！」"
    志雄 "「嗯。但是，不要勉强呢。突然跟你说这些」"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG01EA@2x.jpg" as bg0 zorder 0 with dissolve
#BG_BLUR 0
    scene expression "img/BG01EA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_COLC 0,128,120,112,128
#CHR_POSC 0
#CHR_MGNC 0,CH_LLB01,CH_LBB01
    play sound "SE08_17L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,128
    志雄 "「那，明天见」"
#CHR_MGNC 0,CH_LLB02,CH_LBB02
    voice "NCH03A_CH099"
    智纱 "「嗯，再见」"
    window hide
#SE_VOLC 1,255
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我目送着智纱走过检票口，直到她的背影消失。"
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
#label THREAD_CHISA_FURAFURA
#NCH03A_EFFECT
#CHR_POS_SAVEC 0
#CHR_POS_SAVEC 1
#EOT
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT