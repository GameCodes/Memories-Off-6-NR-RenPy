label NSU09A:
    $currentlabel = "NSU09A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    play music "BGM05"
#label START
    $month = '07'
    $day = '28'
    $date = '5'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG61AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG61AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_15L"
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
    voice "NSU09A_XS000"
    仲居のおばさん "「您慢走」"
    "我们向女招待打听了几处观光地点之后走出了旅馆。"
    window hide
#SE_VOLC 1,64
    show expression "img/BG60AA@2x.jpg" as bg_over zorder 5
    show expression "img/SU_LCA01A@2x.png" as lh0 zorder (10+0):
        xcenter ((320)/640.0)
    with dissolve
    志雄 "「我本来以为只有温泉，看来有不少东西啊」"
    voice "NSU09A_SU000"
    铃 "「是啊，山和湖也是重点」"
    志雄 "「简直就是旅游胜地啊，刚才的服务员说在湖里可以游泳」"
    voice "NSU09A_SU001"
    铃 "「我感觉垂钓的人倒比较多，不过游泳区域也很正规，就尽情地游吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU002"
    铃 "「而且也不止是这些。骑着摩托车如此尽情地在山路中四处行驶，还可以在山顶上的高台边休息一下」"
    "一边看着地图一遍考虑着这些那些的时候，我们的情绪一下子就高涨了起来。"
    "铃也一反常态地兴致勃勃，像孩子一样双眼闪闪发光。"
    志雄 "「我们先围着这一带绕一圈怎么样？然后在觉得喜欢的地方认真地留意一下」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU004"
    铃 "「这样也行，知道什么地方都有什么，就容易行动了」"
    window hide
#BG_SET_BACK 
    stop sound fadeout 1
    play sound "SE06_12"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#SE_WATC 0
    play sound "SE06_13L"
    "熟悉的引擎声发动了。"
    "最初只觉得这是种噪音，现在越听越觉得心情舒畅。"
    "嗯……自己果真是被洗过脑了，对摩托产生好感了。"
    voice "NSU09A_SU005"
    铃 "「那么，赶在气温变高之前出发吧」"
    window hide
    play sound "SE06_14L"
#BG_INIC 3
    #show expression "img/BG_WHITE@2x.jpg" as bg1 zorder 1 with dissolve
#ROUTINE_STA
#BG_POSC 3,30,-60,749,450
    scene expression "img/EVC_SU02A1@2x.png" as bg3 zorder 100:
        block:
            align (.5,.5)
            parallel:
                linear 0.03 xalign 0.53
            parallel:
                linear 0.03 yalign 0.53
            repeat
    show expression "img/Motor_EF_BG@2x.png" as motor_eff_bg zorder -10
    show expression "img/Motor_EF_Building1@2x.png" as motor_eff_down_s zorder -8:
        xcenter .25
        ycenter .7
    show expression "img/Motor_EF_Building2@2x.png" as motor_eff_up_s zorder -7:
        xcenter .75
        ycenter .7
    show expression im.Scale("img/Motor_EF_Wood1@2x.png",1136,263) as motor_eff_up zorder -6 at motor_eff_movein:
        yalign 1.0
    show expression im.Scale("img/Motor_EF_Wood1@2x.png",1136,263) as motor_eff_up2 zorder -6 at motor_eff_moveout:
        yalign 1.0
    show expression "img/Motor_EF_Wood2@2x.png" at motor_eff_moveout as motor_eff_down zorder -5:
        yalign 1.0
    show expression "img/Motor_EF_Wood3@2x.png" at motor_eff_movein as motor_eff_down2 zorder -5:
        yalign 1.0
    with dissolve
    
#EFF_PRI 0
#EFF_STAC 0,MOTOR_RIDE_EF,EFF_NOSKIP
#ROUTINE_STP
    hide bg1 with dissolve
    
    "由于卸下了行李，摩托行驶时轻快了许多。"
    "和来时的高速路不同，这次行驶的是宽敞的山路。"
    "在微风和清新的空气中，我们的心情十分愉快。"
    志雄 "「感觉好舒服！」"
    show expression "img/EVC_SU02A2@2x.png" as bg3 zorder 100 with dissolve
    voice "NSU09A_SU006"
    铃 "「是啊～，空气一干净，道路也看得清楚了」"
    window hide
    stop se fadeout 1
    stop music
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
    stop music
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG67AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG67AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_15L"
    #TODO
#EFF_STAC 0,SUNLIGHT_BG67_FRONT,EFF_SKIP
#EFF_STAC 1,SUNLIGHT_BG67_BACK,EFF_SKIP
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,64
    play music "BGM12"
    "我们爬到一定的高度，进入了岔路，铃停下了摩托。"
    "将引擎停止后，可以听到嘈杂的蝉鸣声。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU007"
    铃 "「是啊，景色也好，车辆也少，路面也宽敞，行驶起来也更便利」"
    志雄 "「就是呢，没有红绿灯，可以放心地奔驰，确实开心」"
    "在前后没有车辆的状态下，如此顺畅地飞驰着，对于坐在身后的人而言是非常愉悦的事情。"
    "……不必进行危险的驾驶，这点很让人感到欣慰。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA01"),"True","img/SU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU008"
    铃 "「说起这个啊，在城市里有各种各样的障碍物，不知道从哪里会突然跳出些什么，挺吓人的」"
    voice "NSU09A_SU009"
    铃 "「那就先沿着湖边慢慢地绕行吧？」"
    志雄 "「怎么？前面先不去吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU010"
    铃 "「今天只是预习，如果什么地方都跑遍了就没意思了」"
    志雄 "「原来如此，是这么回事」"
    "的确，我们才刚刚来到这里。"
    "要把快乐留到最后，这样的心情我能理解。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_SET_BACK 
#BG_INIC 1
    stop sound fadeout 1
    play sound "SE06_47L"
#BG_INIC 3
    #show expression "img/BG_WHITE@2x.jpg" as bg1 zorder 1 with dissolve
#ROUTINE_STA
#EFF_STPC 0,EFF_NOSKIP
#EFF_STPC 1,EFF_NOSKIP
#BG_POSC 3,30,-60,749,450
    scene expression "img/EVC_SU02A1@2x.png" as bg3 with dissolve:
        block:
            align (.5,.5)
            parallel:
                linear 0.03 xalign 0.53
            parallel:
                linear 0.03 yalign 0.53
            repeat
    show expression "img/Motor_EF_BG@2x.png" as motor_eff_bg zorder -10
    show expression "img/Motor_EF_Building1@2x.png" as motor_eff_down_s zorder -8:
        xcenter .25
        ycenter .7
    show expression "img/Motor_EF_Building2@2x.png" as motor_eff_up_s zorder -7:
        xcenter .75
        ycenter .7
    show expression im.Scale("img/Motor_EF_Wood1@2x.png",1136,263) as motor_eff_up zorder -6 at motor_eff_movein:
        yalign 1.0
    show expression im.Scale("img/Motor_EF_Wood1@2x.png",1136,263) as motor_eff_up2 zorder -6 at motor_eff_moveout:
        yalign 1.0
    show expression "img/Motor_EF_Wood2@2x.png" at motor_eff_moveout as motor_eff_down zorder -5:
        yalign 1.0
    show expression "img/Motor_EF_Wood3@2x.png" at motor_eff_movein as motor_eff_down2 zorder -5:
        yalign 1.0
    with dissolve
#EFF_PRI 0
#EFF_STAC 0,MOTOR_RIDE_EF,EFF_NOSKIP
#ROUTINE_STP
    hide bg1 with dissolve
    "铃沿着另一条山路缓缓地向湖边驶去。"
    "习惯了一直铃飞速行驶的速度后，我坐在后面也不会感到害怕了。"
    window hide
    stop se fadeout 1
    #TODO
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#EFF_STPC 1,EFF_SKIP
    scene expression Solid("000") with fade
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG69AA1@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG69AA1@2x.jpg" as bg0 with dissolve
    play sound "SE05_12"
    pause (32/32.0)
#EFF_STAC 0,TWINKLE4,EFF_NOSKIP
#FADE_IN 1
    "不久后我们来到了湖的周围，就这样沿湖而行，直到可以在水边停歇的地方才停下车。"
    "轻风静静地吹拂过水面，为炽热的身体带来一阵凉意。"
#CHR_INIC 0
#EFF_STPC 0,EFF_NOSKIP
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NSU09A_SU011"
    铃 "「呼，好凉快啊」"
    "附近的向导板上写着对湖的简单介绍。"
    if not persistent.dictlist[50] and persistent.show_dict:
        $persistent.dictlist[50]=True
        show screen dict_pop(i=50)
    "眼前的湖水，好像叫做门亚湖。"
    志雄 "「哎，湖底好像有龙在沉睡哦」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU012"
    铃 "「是个有着神龙的湖吗。就算是这样，这湖也相当大了」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA01"),"True","img/SU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU013"
    铃 "「那、那是……天鹅船吗？」"
    window hide
#BG_SET_BACK 
#BG_INIC 2
    show expression "img/BG69AA1@2x.jpg" as bg2 zorder 2
#ROUTINE_STA
#BG_UV_AUTOC 0,(640/2),((448/4)+512),(640/2),(448/2),1,F24
#BG_UV_AUTOC 2,(640/2),(448/4),(640/2),(448/2),1,F24
#BG_ALP_AUTOC 0,0,1,F24
#CHR_SCL_AUTOC 0,512,512,1,F24
#CHR_POS_AUTOC 0,((320-160)-((640/4)*3)),(0),1,F24
#CHR_ALP_AUTOC 0,0,1,F24
#BG_UV_SAVEC 0
#BG_UV_SAVEC 2
#BG_ALP_SAVEC 0
#CHR_SCL_SAVEC 0
#CHR_POS_SAVEC 0
#CHR_ALP_SAVEC 0
#ROUTINE_STP
    hide lh0
    with dissolve
    pause 1
#CHR_ALPC 0,128
#CHR_SCLC 0,256,256
#BG_SWPC 0
    hide bg2 with dissolve
#BG_PRI 0
#BG_PRI 2
#BG_ALPC 2,128
    "铃眯起眼睛，凝视着远处停泊船只的地方，看起来确实像是游船。"
    志雄 "「……铃你很感兴趣吗，一直盯着」"
    window hide
    hide bg1 with dissolve
#BG_SWPC 0
    hide bg0 with dissolve
#BG_PRI 1
#BG_PRI 0
#BG_UVC 0,0,0,640,448
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG69AA1@2x.jpg" as bg0 zorder 0 with dissolve
#BG_BLUR 0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    hide bg1 with dissolve
    voice "NSU09A_SU014"
    铃 "「因为我们约好在这里乘船的啊，不过普通的船划起来太累了」"
    志雄 "「那就由我来划吧，好歹我是男人嘛」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA04"),"True","img/SU_LCA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU015"
    铃 "「哼哼……这倒也不错」"
    "是啊是啊，这样就更像恋人了。"
    "就在我这么想的时候……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCC01"),"True","img/SU_LCC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU016"
    铃 "「不过说实在的我真的想坐天鹅船」"
    "果真还是想坐船啊。"
    "从我的角度来说，虽然不太好意思……唉，算了吧。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU017"
    铃 "「嗯～，说起来空气很清新啊，有一种重新焕发生气的感觉」"
    "铃伸了伸腰，满意地点了点头。"
    window hide
    play sound "SE06_22L"
    #TODO
#BG_BLUR 0
#EFF_STAC 0,TWINKLE4,EFF_NOSKIP
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "正在这时，从远处传来了引擎声，紧接着水花飞溅开来。"
    志雄 "「那是……」"
    "扬起激烈的水花，在湖面上疾速奔驰的是水上摩托。"
#CHR_INIC 0
#EFF_STPC 0,EFF_NOSKIP
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCA01"),"True","img/SU_LCA01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    "一直看着周围的铃，这次向那辆水上摩托投去羡慕的眼光。"
    voice "NSU09A_SU018"
    铃 "「水上摩托也不错，不过还是帆板冲浪更有意思」"
    "这个湖那么大，在里面想玩什么都可以吧。"
    "不过如果什么都想玩，只有这么点时间是不够的……"
    志雄 "「可哪个都挺难的啊，铃有试过吗？」"
    voice "NSU09A_SU019"
    铃 "「这就退缩了吗？正因为困难才有挑战的乐趣啊。这么说来，志雄没冲过浪吗？」"
    志雄 "「有认识的朋友会玩的呢」"
    if not persistent.dictlist[24] and persistent.show_dict:
        $persistent.dictlist[24]=True
        show screen dict_pop(i=24)
    "因为澄空离海比较近，所以冲浪的人有不少。"
    if not persistent.dictlist[38] and persistent.show_dict:
        $persistent.dictlist[38]=True
        show screen dict_pop(i=38)
    "然而不知为何，我无法适应这样的气氛，毕竟没有经历过。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB01"),"True","img/SU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU020"
    铃 "「哎呀，志雄没有享受过冲浪的感觉呢啊」"
    "听铃这么一说，我想起莉莉丝也曾经说过我不适合海。"
    "不过，我也并不是如此的“室内派”吧。"
    志雄 "「虽说是住在海边的人，但也不是所有的人都冲浪的啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LCB02"),"True","img/SU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU021"
    铃 "「这么说也是呢」"
    "铃耸耸肩笑了笑，随即向摩托走去。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG68AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG68AA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
#FADE_IN 1
    if not persistent.dictlist[47] and persistent.show_dict:
        $persistent.dictlist[47]=True
        show screen dict_pop(i=47)
    "总之，在湖这里游玩的计划要往后延，我们紧接着将摩托停在了下龙境车站，决定顺便去逛满是土特产店的商店街。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBA01"),"True","img/SU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU022"
    铃 "「没想到可以逛的地方，比想像中还要多啊」"
    "我们边走边端详着一排排土特产店。"
    "我们两人就这样在未知的地方……总觉得像是真在约会。"
    "铃一直是那么朝气蓬勃。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB02"),"True","img/SU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU023"
    铃 "「有海，有山，有湖，但还不够～，接着还要吃山珍海味」"
    志雄 "「这边有好的饭店么？」"
    "环视了一下周围，倒是有快餐店……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBA02"),"True","img/SU_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU024"
    铃 "「来到这里为止，确实没有」"
    "去吃那些到哪里都能吃的东西，的确可惜了些。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBA01"),"True","img/SU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU025"
    铃 "「去当地人才吃的套餐店，或者和土特产店连锁的饭店比较好吧」"
    志雄 "「氛围真的很重要，的确如此呢。再往深处走走应该会有吧？」"
    window hide
#FADE_OUT 1
    hide lh0 with dissolve
    pause (32/32.0)
#FADE_IN 1
    "就这样悠闲地向前走去，一家小小的餐馆呈现在眼前。"
    "虽然像是日本式的咖啡馆，却也张贴着午餐的招牌。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+96)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB01"),"True","img/SU_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320+96)/640.0
    with dissolve
    voice "NSU09A_SU026"
    铃 "「看起来挺不错？这里和莉莉丝那里的氛围很相似」"
    志雄 "「要说这种感觉的话，确实是有点相似」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBB02"),"True","img/SU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter (320+96)/640.0
    with dissolve
    voice "NSU09A_SU027"
    铃 "「嗯，要是味道也很像就好了～」"
    window hide
    play sound "SE00_10"
    scene expression Solid("000") with dissolve
#FADE_OUT 1
#BG_UVC 0,0,0,640,448
#FADE_IN 0
    voice "NSU09A_XM000"
    店員Ｆ "「欢迎光临，请坐在这边」"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
    scene expression "img/EXBG06A@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAB01"),"True","img/SU_ZAB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (32/32.0)
#FADE_IN 1
    voice "NSU09A_SU028"
    铃 "「话～说，这里有什么菜肴呢？」"
    志雄 "「请，给您菜单」"
    "回头望去，墙上贴着一些写的菜单的纸张。"
    "张贴着沙鮻鱼天妇罗、剌鲅鱼肉、盐烤香鱼等季节性菜单。"
    "比起咖啡厅，更充满了套餐的风格，只是觉得味道很鲜美。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAB02"),"True","img/SU_ZAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU029"
    铃 "「哇，哪个看上去都很好吃，说起来，想在这喝点酒」"
    志雄 "「我觉得你应该知道，这是不可能的吧？」"
    voice "NSU09A_SU030"
    铃 "「呵呵呵，我当然知道。不过比较下酒的食物，就着饭也挺合适」"
    志雄 "「好了，骑车就别喝酒，喝酒就别骑车了。怎么样，决定了么？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAA01"),"True","img/SU_ZAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU031"
    铃 "「我要份剌鲅生鱼片和沙丁鱼套餐，志雄呢？」"
    志雄 "「我要沙丁鱼套餐」"
    voice "NSU09A_SU032"
    铃 "「这个好像也很好吃，分给我一点吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAB01"),"True","img/SU_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU033"
    铃 "「请问」"
    "铃在叫店员点菜的期间也在闲聊，询问着这里的美食。"
    志雄 "「看你果真习惯了旅游的感觉呢」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAC01"),"True","img/SU_ZAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU034"
    铃 "「是啊，驾车远游的时候，在这种地方收集信息是最基本的行动」"
    志雄 "「不看旅游指南么？现在的话上网也行」"
    voice "NSU09A_SU035"
    铃 "「当然有时候也有事先调查，但向当地的人询问还是既准确又迅速的啊」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAB01"),"True","img/SU_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU036"
    铃 "「而且就算从网上查，在乡村还有许多地方很难检索出来吧」"
    voice "NSU09A_SU037"
    铃 "「再有，想在去了当地之后再让自己吃惊。也想和这片区域和这里的人交流」"
    "铃掰着手指做出说明的姿势，看上去很开心。"
    "虽然是很简单一次旅行，不过玩也需要一些要领的。"
    "就这样，在听铃讲解着驾车远游的心得时，点好的饭菜已经摆放在桌前。"
    voice "NSU09A_XM001"
    店員Ｆ "「让您久等了，剌鲅生鱼片、鱼肉套餐和生鱼片套餐」"
    play sound "SE03_33"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAB02"),"True","img/SU_ZAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU038"
    铃 "「看起来很好吃呢，不过量太大了」"
    志雄 "「的确……」"
    "摆放在铃面前的饭量远超过所预想的。剌鲅生鱼片和鱼肉套餐盛了满满一盘，还有饭和味噌汤。"
    "摆在我面前的是以沙丁鱼片为主的南蛮腌，盛满一盘的沙丁鱼汉堡牛肉饼，同样有饭和味噌汤。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAB01"),"True","img/SU_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU039"
    铃 "「那么，我开动了」"
    志雄 "「我开动了」"
    "铃一副等不及的样子，合掌说完后，大口吃起了剌鲅生鱼片。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAB02"),"True","img/SU_ZAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU040"
    铃 "「嗯，嗯，这个不错」"
    "铃吞下整个生鱼片后，笑逐颜开地点了点头。"
    志雄 "「啊呜，啊呜」"
    "的确很好吃。虽然装盘不够细致，但食物的鲜美程度出类拔萃。"
    "我能感觉到材料在料理中丝毫没有被浪费，充分地将食材的鲜味引导了出来。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAC01"),"True","img/SU_ZAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU041"
    铃 "「啊，尝一下沙丁鱼」"
    志雄 "「这个也不错，尝尝吧」"
    "我把沙丁鱼片和南蛮腌摆在铃面前。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAB03"),"True","img/SU_ZAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#ROUTINE_STA
#BG_UV_AUTOC 0,(640/8),(448/8),((640/4)*3),((448/4)*3),1,F24
#CHR_SCL_AUTOC 0,320,320,1,F24
#ROUTINE_STP
#MESEX_A M_NOA,A_CH_SU,NSU09A_SU042,"【鈴】「……」%K%P"
    铃 "「……」"
    "铃忽然放下筷子，陷入沉默中。"
    "取而代之的，是将视线转移到我这里，仿佛在期待着什么。"
    "怎、怎么……怎么回事？"
    志雄 "「怎么不吃了？很好吃啊？」"
#ROUTINE_STA
#BG_UV_AUTOC 0,(0),(0),(640),(448),1,F24
#CHR_SCL_AUTOC 0,205,205,1,F24
#ROUTINE_STP
    "然而铃依然默不作声，直直盯着我。"
    "难、难道……这是……"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "啊、啊～嗯":
            $F7=0
        "不要故意捉弄我":
            $F7=1
    if F7==0:
        jump L_NSU09A_SEL00_A
    if F7==1:
        jump L_NSU09A_SEL00_B
label L_NSU09A_SEL00_A:
    $F4+=1
    "不知不觉，我对铃的眼神失去了耐心。"
    志雄 "「给」"
    "我接过沙丁鱼片，送到铃的嘴边，但“啊”这样的话，我是撕破嘴也不能说。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAB02"),"True","img/SU_ZAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#ROUTINE_STA
#BG_UV_AUTOC 0,(640/8),(448/8),((640/4)*3),((448/4)*3),1,F24,48
#CHR_SCL_AUTOC 0,320,320,1,F24,48
#ROUTINE_STP
    voice "NSU09A_SU043"
    铃 "「呵呵」"
    "铃露出满面的笑容，吞下了我递过去的生鱼片。"
#ROUTINE_STA
#BG_UV_AUTOC 0,(0),(0),(640),(448),1,F24
#CHR_SCL_AUTOC 0,205,205,1,F24
#ROUTINE_STP
    "这、这太难为情了。"
    "不被店员他们看见就好了……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAB01"),"True","img/SU_ZAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU044"
    铃 "「南蛮腌也很好吃」"
    志雄 "「……」"
#ROUTINE_STA
#BG_UV_AUTOC 0,(640/8),(448/8),((640/4)*3),((448/4)*3),1,F24,48
#CHR_SCL_AUTOC 0,320,320,1,F24,48
#ROUTINE_STP
#MESEX_A M_NOA,A_CH_SU,NSU09A_SU045,"【鈴】「……」%K%P"
    铃 "「……」"
    志雄 "「我，我知道了，好了……」"
    "没有辜负我的期待，最后沙丁鱼和南蛮腌都同时让她吃了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAB02"),"True","img/SU_ZAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU046"
    铃 "「哼哼～太好吃了」"
    "铃心情应该不错吧。算了，就暂且做一回恋人的举动吧……"
    "但是这样的话……"
    志雄 "「这样就是所谓的，笨蛋情侣了吧……」"
#CHR_GET_POSC 0,F24,F25
#RSUB F24,(320)
#BG_LAY 3,SU_ZXB04,2,F24
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAB04"),"True","img/SU_ZAB04A@2x.png") as lh0 zorder (10+0):
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
    voice "NSU09A_SU047"
    铃 "「喂，别说多余的话！」"
#THREAD_STP 1
    hide bg3 with dissolve
    "果真是不好意思啊……"
    "尽管如此做了这样的事情，在这次旅行中的紧张度大概要更加提高了吧？"
    window hide
#FADE_OUT 1
#BG_UV_AUTOC 0,(0),(0),(640),(448),1,F24,0
#CHR_SCL_AUTOC 0,205,205,1,F24,0
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAB02"),"True","img/SU_ZAB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_IN 1
    voice "NSU09A_SU048"
    铃 "「呼，我吃饱了～」"
    志雄 "「我吃饱了」"
    "结果在中途不知不觉地忘记了食物的味道……"
    jump L_NSU09A_SEL00_X
label L_NSU09A_SEL00_B:
#ROUTINE_STA
#BG_UV_AUTOC 0,(640/8),(448/8),((640/4)*3),((448/4)*3),1,F24
#CHR_SCL_AUTOC 0,320,320,1,F24
#ROUTINE_STP
    志雄 "「……」"
    铃 "「……」"
    志雄 "「……」"
    "喂，不要粘着我……"
#ROUTINE_STA
#BG_UV_AUTOC 0,(0),(0),(640),(448),1,F24
#CHR_SCL_AUTOC 0,205,205,1,F24
#ROUTINE_STP
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAC03"),"True","img/SU_ZAC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU050"
    铃 "「呼，紫菜好恶心！」"
    "铃终于要放弃了么，忽然将沙丁鱼和南蛮腌吃进口中。"
    "果真还是想让我喂她么……"
    志雄 "「不不不，这个真的办不到！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAC05"),"True","img/SU_ZAC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU051"
    铃 "「如果错过这个机会，可能一生都不会有了」"
    志雄 "「不要做不着边际的事情」"
    "但是仔细想一想，如果现在这样做的话，可是最有恋人感觉的啊。"
    "失败了吧？但不要难为情啊……"
    window hide
#FADE_OUT 1
#BG_PRI 0
    "正当我想着这些事的时候，餐盘中的饭菜已不知不觉一扫而空。"
    window hide
#BG_PRI 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAB02"),"True","img/SU_ZAB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#FADE_IN 1
    voice "NSU09A_SU052"
    铃 "「我吃饱了」"
    志雄 "「我吃饱了」"
    jump L_NSU09A_SEL00_X
label L_NSU09A_SEL00_X:
    window hide
    play sound "SE03_20"
    志雄 "「差不多该走了吧」"
    "我提议先去喝点水稍作休息。"
    "注意到周围的客人逐渐增多，再待在这里会给别人带来麻烦的。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_ZAA01"),"True","img/SU_ZAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU053"
    铃 "「嗯，我这份的钱放在这里了，先出去了」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "铃将自己那份的钱放下之后就走出去了。"
    "这种时候，铃不让我请客，也不打算请我的客。"
    "而且付帐的事情让我来做，给我个机会耍帅……嗯，也许是这样。"
    window hide
    play sound "SE00_10"
    stop music
#FADE_OUT 1
    stop music
    scene expression Solid("000") with dissolve
#BG_SET_BACK 
#BG_INIC 0
#FADE_IN 0
    voice "NSU09A_XM002"
    店員Ｆ "「谢谢惠顾」"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
    scene expression "img/BG68AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    play sound "SE05_15L"
    "付完帐走出店门，一股热气顿时袭来。"
    "太阳已高高升起，现在是一天中最热的时候。"
    志雄 "「好热啊……」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,(320-256)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SN'",DynamicDisplayable(mouthanime,"SN_SAA01"),"True","img/SN_SAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#MOV_CHR_INIT 32
#MOV_CHR1 0
#MOV_CHR_GO 1
    hide lh1 with dissolve
#CHR_ALPC 1,128
    "擦去了很早就渗出的汗，发现在视野的另一端好像有一个熟悉的人影。"
    志雄 "「怎么？刚才的……？」"
    "但是，那个人影一闪而过，然后便消失了。"
    志雄 "「是我产生了幻觉么……？」"
    window hide
    play sound "SE00_11"
    play sound "SE03_90"
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBA02"),"True","img/SU_LBA02A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NSU09A_SU054"
    铃 "「嗯……？东张西望在看什么？」"
    志雄 "「没、没什么」"
    "是心理作用吧。"
    "在这个世界上，据说一模一样的人会有三个呢。要说稻穗的话，他现在应该是和女朋友在旅行中吧。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LBA01"),"True","img/SU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU09A_SU055"
    铃 "「呼，趁着天气还不热，就再沿着海边转一圈再回旅馆吧」"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music
#FADE_OUT 1
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop se
    stop sound
    stop music
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT