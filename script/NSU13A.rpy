label NSU13A:
    $currentlabel = "NSU13A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    play music "BGM13"
#label START
    $month = '07'
    $day = '29'
    $date = '6'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG64NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG64NA@2x.jpg" as bg0 with dissolve
    play sound "SE05_16L"
    pause (32/32.0)
#EFF_STAC 0,YUGE,EFF_NOSKIP
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
#SE_VOLC 1,128
    play sound "SE03_78"
    志雄 "「好痛～～～」"
    "只不过玩了一天，我就已经被晒伤得相当严重。"
    "皮肤一沾到水，痛得不禁泪流满面。"
    if F106!=0:
        jump L_NSU13A_BRA00_A
    jump L_NSU13A_BRA00_B
label L_NSU13A_BRA00_A:
    "不过，从皮肤的暴露情况来看，铃应该更严重。"
    "防晒油虽然涂了……但真的没事吗？"
    jump L_NSU13A_BRA00_X
label L_NSU13A_BRA00_B:
    "从皮肤的暴露情况来看，铃应该更严重。"
    "不过，为了防止晒伤好像已经涂了防晒霜，但真的没关系吗？"
    jump L_NSU13A_BRA00_X
label L_NSU13A_BRA00_X:
    志雄 "「确实玩的很尽兴……只是……」"
    "没错，在湖边玩的确实很开心，但果然是那种和朋友出来玩的感觉。"
    "可无论如何，我也希望能有一丝丝那种像莉莉丝说的那种恋人的感觉。"
    "想着想着，身体又开始发热，被晒伤的皮肤像针扎一样疼。"
    "那疼痛感仿佛在对我说，要再加把劲才行啊"
    window hide
#SE_VOLC 1,0
    stop se fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_NOSKIP
    stop se
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG63NA1@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG63NA1@2x.jpg" as bg0 with dissolve
#SE_VOLC 1,64
#FADE_IN 1
    志雄 "「铃还没好吗……？」"
    "因为洗澡出汗的缘故吧，想喝点冷饮。"
    "我想去买点果汁之类的东西，于是站了起来。"
    window hide
#FADE_OUT 1
#FADE_IN 0
    play sound "SE00_47"
    "就在我正要走出去的时候，门从外面开了。"
    志雄 "「诶？啊？对不起」"
    window hide
#MUS_VOL 0
#FADE_OUT 0
#BG_GET_NOC 0,F34
#BG_PRI 0
#BG_UVC 0,(640/8),(448/4),(640-640/4),(448-448/4)
#BG_COLC 0,128,128,128,128
#BG_SET_BACK 
#BG_INIC 2
#BG_PRI 2
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_SCLC 0,602,602
#CHR_POSC 0,((320)-3),-130
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MHA01"),"True","img/SU_MHA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_PRIC 1
#CHR_ALPC 1
#CHR_POSC 1
    hide lh0
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XHA01"),"True","img/SU_XHA01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#BG_BLUR 0
#FADE_IN 1
    "在门口的，是一个不太熟悉的浴衣穿着的女生。"
    voice "NSU13A_SU000"
    铃 "「为什么要道歉呢？」"
    window hide
    stop sound fadeout 1
    play sound "SE07_23"
#BG_UV_AUTOC 0,(640/8),512,(640-640/4),(448-448/4),0,F24,256
#CHR_POS_AUTOC 0,,346,1,F24,256
#BG_UV_SAVEC 0
#CHR_POS_SAVEC 0
#BG_BLUR 0
#BG_ALP_SAVEC 0
#CHR_ALP_SAVEC 1
#CHR_ALP_SAVEC 0
#MUS_VOL 64
    志雄 "「咦……是铃吗！？」"
    voice "NSU13A_SU001"
    铃 "「不是我还能是谁呢」"
    志雄 "「不……只是吓了一跳。这身浴衣是怎么回事？」"
    window hide
#BG_ALP_AUTOC 0,0,1,F24,96
#BG_ALP_AUTOC 2,128,1,F24,96
#CHR_ALP_AUTOC 1,128,1,F24,96
#CHR_ALP_AUTOC 0,0,1,F24,48
#MUS_VOL 128
#BG_ALP_SAVEC 2
    "站在门前的是身着浴衣的铃。"
    "让我惊讶的是，身着华丽端庄的浴衣的铃……看上去非常合适她。"
    "铃虽然嘴上显得娇嗔，不过脸上却满是笑意。"
    "铃真是喜欢出其不意地给人带来惊喜啊……"
    voice "NSU13A_SU002"
    铃 "「这是之前放在行李里面带来的」"
    if not persistent.dictlist[51] and persistent.show_dict:
        $persistent.dictlist[51]=True
        show screen dict_pop(i=51)
    voice "NSU13A_SU003"
    铃 "「对了，附近不是有个泉龙神社吗，应该有庙会的。一起去看看吧」"
    志雄 "「应该会有吧。不过铃对这儿很熟啊」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHB01"),"True","img/SU_LHB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU004"
    铃 "「是订房间的时候听房东太太说的。另外这浴衣也是她帮我穿上的」"
    "原来如此。原本还以为是毫无计划的旅行，原来各种事情都考虑过了。"
    voice "NSU13A_SU005"
    铃 "「喂，志雄也快点准备吧。对面的店已经开了，去吃点什么吧」"
    志雄 "「没问题。从早上起来就没吃过东西了呢……」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHB02"),"True","img/SU_LHB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU006"
    铃 "「我也是呢」"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG74NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG74NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-160)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHA01"),"True","img/SU_LHA01A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
    play sound "SE08_15L"
    pause (32/32.0)
#FADE_IN 1
    play music "BGM11"
    志雄 "「肚子也要抗议了吧」"
    "一到神社，发现不只我们，许多身着浴衣的人也来了。"
    "从石阶上传来了热闹的音乐。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHB01"),"True","img/SU_LHB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU007"
    铃 "「真是令人怀念啊～」"
    "说着铃眯起了眼睛。"
    志雄 "「在我小时候，常常会去祭典和庙会」"
    voice "NSU13A_SU008"
    铃 "「穿浴衣参加祭典的话，我从小时候就开始那么做了」"
    志雄 "「如此说来，有参加过什么有名的祭典了吗？」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHA01"),"True","img/SU_LHA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU009"
    铃 "「没有，家乡都只有普通的娱乐而已，并没有这样的祭典呢」"
    "原来如此。"
    "因此才会觉得怀念，才会有种无拘无束的感觉吧。"
    志雄 "「不管怎样，先过去看看吧」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHB01"),"True","img/SU_LHB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU010"
    铃 "「那……给」"
    "突然，铃伸出了手。"
    "……咦？手里什么也没有啊，不像是要递给我什么的样子。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHB02"),"True","img/SU_LHB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU011"
    铃 "「穿浴衣走路很不方便啊。能牵着我的手吗，免得在台阶上摔倒」"
    志雄 "「诶！？哦……好」"
    "当然，没有拒绝的理由。"
    "只是，突然说出这样的话，有点难为情啊……"
    志雄 "「嗯，那就……牵手吧」"
    "对于我再一次的确认，铃扑哧笑了出来。"
    "不过与这种羞赧相比，从指尖传来的铃的温度更让自己无法抑制内心的激动。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    show expression "img/BG76NA@2x.jpg" as bg1 zorder 1 with dissolve
#SE_VOLC 1,128
    play sound "SE01_19L"
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
    hide bg1 with dissolve
#BG_ALPC 1,128
#BG_PRI 0
#BG_PRI 1
    scene expression "img/BG76NA@2x.jpg" as bg0 with dissolve
    "神社里有些店已经开了，很多人聚在一起。"
    志雄 "「的确不是很大的规模」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,112,96,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHA01"),"True","img/SU_LHA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU012"
    铃 "「是啊。但气氛很好呢」"
    "我们向周围望去，大家在参拜了大殿之后，有的在院内谈笑，有的则在各个摊位上转悠。"
    "正如铃所言，很有小地方集会的气氛呢。"
    志雄 "「先去祭拜神明吧」"
    voice "NSU13A_SU013"
    铃 "「好呀」"
    window hide
    stop se fadeout 1
#SE_VOLC 1,64
    show expression "img/BG75NA@2x.jpg" as bg_over zorder 2 with dissolve
    pause (32/32.0)
#BG_GET_NOC 0,F34
#BG_SET_BACK 
#BG_INIC 1
#BG_UVC 1,(640/2),(448/8),(640/2),(448/2)
#BG_ALPC 1
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
    hide bg1 with dissolve
#BG_ALPC 1,128
#BG_PRI 0
#BG_PRI 1
    play sound "SE03_35"
    play sound "SE03_27"
    "按照铃教的方法，两拜两拍手一拜地做。"
    "据铃所说，参拜并不是为了祈愿，更像是为了感谢过去的一年。"
    "在过去的一年里，说到感谢的话……只有一个。"
    voice "NSU13A_SU014"
    铃 "「……」"
    "偷偷往旁边瞄去，铃闭着眼睛，低下了头。铃在感谢什么吗？"
    window hide
#SE_VOLC 1,0
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG76NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG76NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,(320+160)
#CHR_COLC 0,128,112,96,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MHB01"),"True","img/SU_MHB01A@2x.png") as lh0 zorder (10-0):
        xcenter .75
        ypos 0.0
    with dissolve
    pause (32/32.0)
#SE_VOLC 1,128
#FADE_IN 1
    play music "BGM12"
#THREAD_STA 1,THREAD_YAKISOBA
    voice "NSU13A_SU015"
    铃 "「果然还是要炒面啊！这个是庙会的固定项目」"
#THREAD_WAT 1
#MESX "%K%P"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MHC04"),"True","img/SU_MHC04A@2x.png") as lh0 zorder (10-0):
        xcenter .75
        ypos 0.0
    with dissolve
#THREAD_STA 1,THREAD_TAKOYAKI
    voice "NSU13A_SU016"
    铃 "「不过，还是说章鱼烧和什锦烧比较好呢？」"
#THREAD_WAT 1
#MESX "%K%P"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MHB02"),"True","img/SU_MHB02A@2x.png") as lh0 zorder (10-0):
        xcenter .75
        ypos 0.0
    with dissolve
#THREAD_STA 1,THREAD_RINGOAME
    voice "NSU13A_SU017"
    铃 "「苹果糖！这个可不能错过啊！」"
#THREAD_WAT 1
#MESX "%K%P"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/BG76NA@2x.jpg" as bg1 with dissolve
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_ALPC 0,128
    "铃几乎每到一处，都会停下来买吃的。"
    志雄 "「喂，稍等下，铃。是不是买太多了？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,640
#CHR_COLC 0,128,112,96,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHB02"),"True","img/SU_LHB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#ROUTINE_STA
#BG_SWPC 0
    hide bg1 with dissolve
#BG_PRI 1
#BG_PRI 0
#BG_BLUR 0
#CHR_POS_AUTOC 0,F24,96
#CHR_ALP_AUTOC 0,128,1,F24,96
#ROUTINE_STP
    voice "NSU13A_SU018"
    铃 "「哈哈，哪有啊，不是很开心嘛。给，志雄也吃点吧」"
    "看到这样的笑容我就已经满足了……我还没说出口，就已经被铃递过来的炒面塞满了嘴巴。"
    window hide
#MOV_CHR_INIT 96
#MOV_CHR0 0
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
#BG_BLUR 0
    hide lh0 with dissolve
#CHR_ALPC 0,128
    "趁这个时候铃又去买了烤墨鱼。"
    "……这些，能全部吃掉吗。"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,112,96,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHA01"),"True","img/SU_LHA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (32/32.0)
#SE_VOLC 1,128
#FADE_IN 1
    voice "NSU13A_SU019"
    铃 "「哈哈～，放心吧。不过，好吃的东西热量都是相当高啊」"
    "说归说，铃仍然是一副不当回事的样子。"
    "面前堆得像小山一样的食物，竟然全部被两人吃光了。"
    志雄 "「哎，平时都是自己做饭吃，旅行中这样不是很好吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHB01"),"True","img/SU_LHB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU020"
    铃 "「呵呵，不愧是志雄，能明白这点呢。趁着这气氛就该饱餐一顿。考虑卡路里这样多余的事情等回去再想吧」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHB02"),"True","img/SU_LHB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU021"
    铃 "「那我们接着逛吧！」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE01_18L"
    "确实，铃是那种要玩就要玩得尽兴的人。"
    "能把这些事分的那么清楚，也许因为她是作家才能做到吧。"
    志雄 "「好啊。那我们在摊位上再逛一会儿吧」"
    window hide
    stop se fadeout 1
#SE_VOLC 1,0
#MUS_VOL 32
#FADE_OUT 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,112,96,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHA01"),"True","img/SU_LHA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (32/32.0)
    stop se
#SE_VOLC 1,128
#FADE_IN 1
    voice "NSU13A_SU022"
    铃 "「接下来会是什么呢？」"
    "铃拿苹果糖作为甜点，一边吃一边眺望前面。"
    志雄 "「除了吃的也看看其他的吧。你看，对面好像有玩的地方」"
    voice "NSU13A_SU023"
    铃 "「哎，那边是套圈吗？」"
    志雄 "「好像是呢」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE01_19L"
#BG_GET_NOC 0,F24
#BG_CHG_FWD F24,48
    stop se
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,112,96,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHA01"),"True","img/SU_LHA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "这个店铺在过道靠里较宽的一个角落，在里面有个像人偶台子一样的架子，上面并排摆放着各种奖品。"
    voice "NSU13A_SU024"
    铃 "「唔咕唔咕，那个像是吉祥物的东西看上去很好玩啊」"
    "铃花钱买了套圈，瞄准了位于里侧的一个手持扫把、有些中华风格的少女玩偶。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHB01"),"True","img/SU_LHB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU025"
    铃 "「套中吧」"
    window hide
    play sound "SE03_81"
    "真遗憾！套圈没有套中，掉到了一旁。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHC05"),"True","img/SU_LHC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU026"
    铃 "「咦？有些偏差呢……好吧！」"
    window hide
    play sound "SE03_81"
    "这次又落空了。又掉到离设定的距离更远的地方去了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHC04"),"True","img/SU_LHC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU027"
    铃 "「完全没有手感呢～」"
    "一次只有三个套圈，接下来就是最后的挑战了。铃眯起一只眼睛，非常谨慎地瞄准着目标……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHB01"),"True","img/SU_LHB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU028"
    铃 "「误，没办法了……志雄你试一下吧？」"
    志雄 "「什么，让我来吗？　……套不中的话不许怪我啊？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHB02"),"True","img/SU_LHB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU029"
    铃 "「嗯。不过即使我说了也不要介意哟」"
    "果然……"
    "虽然这么说，如果中的了话，我在铃心里的位置会迅速提高的吧！（或许是吧）"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHB01"),"True","img/SU_LHB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "我谨慎地瞄准了目标……"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "稍微往右一点":
            $F7=0
        "稍微往左一点":
            $F7=1
    if F7==0:
        jump L_NSU13A_SEL00_A
    if F7==1:
        jump L_NSU13A_SEL00_B
label L_NSU13A_SEL00_A:
    "稍微再往右一点吗？"
    志雄 "「好，去吧！」"
    window hide
    play sound "SE03_81"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHC02"),"True","img/SU_LHC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「……」"
    voice "NSU13A_SU030"
    铃 "「……没中啊」"
    "耳边传来铃难过的声音。与其这样，还不如抱怨我几句呢。"
    志雄 "「再试一回！」"
    "不能就这么结束啊。"
    "就在我下定决心，准备拿出钱包的时候……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHB02"),"True","img/SU_LHB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU031"
    铃 "「呵呵呵，我开玩笑啦。这样就好了，不用了」"
    "铃笑着制止了我。"
    "话虽如此，自己却觉得有点不甘心。"
    志雄 "「不，再试一下！这么就放弃的话，作为男人也太没用了！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHB05"),"True","img/SU_LHB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU032"
    铃 "「没有这么严重啊……」"
    志雄 "「大叔！」"
    "大叔以一脸明白的表情，收了钱后就把套圈递给了我。"
    志雄 "「好，去吧！」"
    "这次更是谨慎地瞄准……！"
    window hide
#SE_VOLC 1,0
    play sound "SE03_81"
#FADE_OUT 1
    scene expression Solid("000") with fade
#SE_WATC 0
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG74NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression Solid("000") with None
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#FADE_IN 0
    "……结果，一直到花完身上所有的零钱，也没有套到想要的玩偶。"
    window hide
#FADE_OUT 0
#MUS_VOL 128
#BG_COLC 0,128,128,128,128
    scene expression "img/BG74NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHA01"),"True","img/SU_LHA01A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
#SE_VOLC 1,64
    play sound "SE01_19L"
#FADE_IN 1
    志雄 "「唉……」"
    voice "NSU13A_SU033"
    铃 "「有点遗憾呢」"
    志雄 "「似乎到后来才稍稍掌握到窍门呢」"
    "一边走下神社的台阶，一边确认着套圈的动作。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHA04"),"True","img/SU_LHA04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU034"
    铃 "「是这样么～。从我看来，一千日元的投资恐怕还不够吧」"
    志雄 "「呜……或许是因为有风的缘故」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHB02"),"True","img/SU_LHB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU035"
    铃 "「哪有哪有」"
    "并肩走着的铃不由地笑了。"
    "虽然稍微有点遗憾，算了，只要两个人能开心的话就够了。"
    jump L_NSU13A_SEL00_X
label L_NSU13A_SEL00_B:
    $F4+=1
    "再稍微往左一点……"
    志雄 "「就是这儿吧！」"
    window hide
    play sound "SE03_81"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHB02"),"True","img/SU_LHB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「去吧！」"
    "我扔出去的圈划了一道理想的抛物线，套上了目标的人偶。"
    voice "NSU13A_SU036"
    铃 "「中啦！」"
    志雄 "「铃，送给你」"
    "我把店里大叔拿过来的玩偶，就这样递到铃的手上。"
    voice "NSU13A_SU037"
    铃 "「谢谢！」"
    "铃像个孩子一样，敞开心扉，露出了天真无邪的笑容。"
    "真是……太好了。"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG74NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG74NA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHA07"),"True","img/SU_LHA07A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
#SE_VOLC 1,64
    play sound "SE01_19L"
    pause (32/32.0)
#FADE_IN 1
    "顺着石阶回去，铃依然目不转睛地盯着玩偶。"
    voice "NSU13A_SU038"
    铃 "「唔，或许是因为太可爱了吧，有种很奇妙的感觉呢～」"
    志雄 "「说起来，这个人偶是什么呢？」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHB01"),"True","img/SU_LHB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU039"
    铃 "「嗯？店主或许都不知道吧。不过有什么关系」"
    "铃能如此开心，努力总算是值得的。这么认真地套圈，还是有生以来头一次呢。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHB02"),"True","img/SU_LHB02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU040"
    铃 "「呵呵呵！」"
    jump L_NSU13A_SEL00_X
label L_NSU13A_SEL00_X:
    stop music fadeout 1
    志雄 "「这么看来，祭典真的很有趣啊」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHA01"),"True","img/SU_LHA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU041"
    铃 "「嗯，相当有意思呢」"
    "咦，比我预想的要冷静啊……虽然还是一副乐在其中的样子。"
    志雄 "「怎么了，还有什么在意的事吗？」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHA04"),"True","img/SU_LHA04A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU042A"
    铃 "「嗯～，{w=3}{nw}"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_LHA06"),"True","img/SU_LHA06A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NSU13A_SU042B"
    extend "这样的祭典是很快乐没错，只是……」"
    志雄 "「……？」"
    window hide
    stop se fadeout 1
#SE_VOLC 1,(64/4)
#BG_SET_BACK 
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU08A")]=True
    show expression "img/EVN_SU08A@2x.jpg" as bg1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play music "BGM16"
    voice "NSU13A_SU043"
    铃 "「还不明白吗？」"
    "铃轻轻地摆了摆浴衣的袖子。说实话，这身浴衣铃穿起来……"
    "啊！"
    志雄 "「啊，对不起。差点忘了！是我没有好好说！」"
    voice "NSU13A_SU044"
    铃 "「嗯……」"
    志雄 "「这身浴衣，真的很适合铃，非常的漂亮」"
    "虽然有点难为情，但能这么轻易说出来，不是奉承，而是因为内心真正的感觉。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU08B")]=True
    show expression "img/EVN_SU08B@2x.jpg" as bg1 with dissolve
    voice "NSU13A_SU045"
    铃 "「呵呵，谢谢。这件浴衣，就连焰火大会也没有穿呢，这次算是了了心愿吧」"
    志雄 "「是这样啊……」"
    "这就是说是为我而穿的吧。"
    "有点……不，是相当的开心。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_SU08A")]=True
    show expression "img/EVN_SU08A@2x.jpg" as bg1 with dissolve
    voice "NSU13A_SU046"
    铃 "「嗯，这样一来，心里的疙瘩一下子就解开了」"
    voice "NSU13A_SU047"
    铃 "「从看焰火的时候开始就一直很在意。该说是有还未做的事情呢还是别的什么呢」"
    志雄 "「即使不这么在意也……嗯，我很高兴铃这样在意我。我很开心能看到铃穿浴衣的样子」"
    铃 "「……」"
#MESEX_A M_NOA,A_CH_SU,"【鈴】「……」%K%P"
    "对于我的话，铃无声地笑了。"
    "同时，作为回答，她握住了我的手。"
    "此刻，不要说铃那略显高涨的情绪，就连她脉搏的跳动似乎也一并传递给了我……"
    "我就这样紧紧地执着铃的手，一同走在夜晚的道路上。"
    window hide
    play sound "SE01_19L"
    pause (128/32.0)
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
#label THREAD_YAKISOBA
#BG_UV_AUTOC 0,,(448/4),(640/2),(448/2),1,F123
#CHR_ALP_AUTOC 0,128,1,F123
#BG_UV_SAVEC 0
#CHR_ALP_SAVEC 0
#EOT
#label THREAD_TAKOYAKI
#BG_UV_AUTOC 0,(640/8),(448/4),(640/2),(448/2),1,F123,96
#CHR_POS_AUTOC 0,0,1,F123,96
#BG_UV_SAVEC 0
#CHR_POS_SAVEC 0
#EOT
#label THREAD_RINGOAME
#BG_UV_AUTOC 0,(640/2),(448/4),(640/2),(448/2),1,F123,128
#CHR_POS_AUTOC 0,(320-192),0,1,F123,128
#BG_UV_SAVEC 0
#CHR_POS_SAVEC 0
#EOT