label NCH01A:
    $currentlabel = "NCH01A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#label START
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    $month = '07'
    $day = '17'
    $date = '1'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/NIMG19B-568h@2x.jpg" as bg1 with dissolve
    pause (180/32.0)
    hide bg1 with dissolve
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG15MA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG15MA@2x.jpg" as bg0 with dissolve
    play sound "SE05_14L"
    pause (32/32.0)
#FADE_IN 1
    window hide
    stop sound
    play sound "SE02_00L"
    pause (32/32.0)
    志雄 "「啊」"
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XDA02"),"True","img/SU_XDA02A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCH01A_SU000"
    铃 "「嗯？　电话？」"
    "听到了电话铃声，铃的关节技一瞬间松了一下。"
    "就是现在！"
    play sound "SE03_15"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_XDB04"),"True","img/SU_XDB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH01A_SU001"
    铃 "「啊！？」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我从铃的束缚中挣脱了出来，一把抄起放在桌子上的手机。"
    "打来电话的人，和预想的一样。"
    if not persistent.dictlist[2] and persistent.show_dict:
        $persistent.dictlist[2]=True
        show screen dict_pop(i=2)
    志雄 "「……果然是智纱啊」"
    window hide
    play sound "SE02_03"
    play music "OBGM05"
    志雄 "「喂喂」"
    if not persistent.dictlist[0] and persistent.show_dict:
        $persistent.dictlist[0]=True
        show screen dict_pop(i=0)
    voice "NCH01A_CH000_K"
    智纱 "「早上好，志雄君」"
    window hide
#MUS_VOL 64
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDA06"),"True","img/SU_MDA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    铃 "「……」"
#MESEX_A M_NOA,A_CH_SU,NCH01A_SU002,"【鈴】「……」%K%P"
    "是对自己的关节技被挣脱感到不满吗，感觉铃一直盯着我这边……。"
    window hide
#MUS_VOL 128
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "但是，那种事情怎样都好！"
    voice "NCH01A_CH001_K"
    智纱 "「已经起来了？」"
    志雄 "「当然了。因为我知道智纱要来的啊」"
    "最近，智纱来我家这件事已经变得一点都不稀奇了。"
    voice "NCH01A_CH002_K"
    智纱 "「嘿嘿，听你这么说我真是高兴啊」"
    "智纱单纯地相信了我所说的话，并因此感到高兴。"
    "这让我感到一丝罪恶感，其实直到刚才还在睡觉……。"
    志雄 "「难道智纱你，已经到澄空站了？」"
    voice "NCH01A_CH003_K"
    智纱 "「嗯」"
    志雄 "「这样啊。那我现在去车站，你在那边等我吧」"
    voice "NCH01A_CH004_K"
    智纱 "「啊，没关系的，不那么做也可以」"
    play sound "SE05_14L"
    stop music fadeout 1
    志雄 "「哎？」"
    voice "NCH01A_CH005_K"
    智纱 "「看看窗户外面」"
    "怎么了？　我一只手拿着手机，用另一只手推开门走到阳台上。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH01A")]=True
    show expression "img/EVN_CH01A@2x.jpg" as bg1 zorder 1 with dissolve
#SE_VOLC 1,255
    play sound "SE00_42"
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
#BG_SET_BACK 
#BG_INIC 3
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH01B")]=True
    show expression "img/EVN_CH01B@2x.jpg" as bg3 zorder 3 with dissolve
    "啊！"
    window hide
#BG_ALP_AUTOC 1,0,0,F24,24
#BG_UV_AUTOC 1,(640/4),(448/4),(640/2),(448/2),1,F24,24
#BG_ALP_SAVEC 1
#BG_ALP_SAVEC 1
#BG_SWPC 1
    hide bg3 with dissolve
#BG_PRI 1
#BG_PRI 3
#BG_ALPC 3
#SE_VOLC 1
    play music "BGM03"
    voice "NCH01A_CH006"
    智纱 "「志雄君～！」"
    if not persistent.dictlist[46] and persistent.show_dict:
        $persistent.dictlist[46]=True
        show screen dict_pop(i=46)
    "在公寓的下面，智纱大声向我这边叫喊着。她穿着凉爽的连衣裙，颇有夏日风味。智纱每挥一下手，马尾辫就随着摇动一下。"
    "已经到这里了吗！？"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH01C")]=True
    show expression "img/EVN_CH01C@2x.jpg" as bg1 with dissolve
    voice "NCH01A_CH007"
    智纱 "「……啊，对，对不起」"
    "她喊的声音，４楼都能听到，因此引来了周围路人的围观。智纱红着脸低下了头。"
    voice "NCH01A_CH008_K"
    智纱 "「呜，不由自主地大声喊了出来……好难为情……」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CH01B")]=True
    show expression "img/EVN_CH01B@2x.jpg" as bg1 with dissolve
    voice "NCH01A_CH009_K"
    智纱 "「那，那个。志雄已经吃过早饭了吗？」"
    志雄 "「没，还没吃呢」"
    voice "NCH01A_CH010_K"
    智纱 "「太好了，我就想着来给你做饭，材料都带来了」"
    志雄 "「……一直以来谢谢你了。帮大忙了」"
    "最近智纱来到我家的时候，经常给我做饭，或是帮我打扫房间。她一直对于我一个人生活这件事有所牵挂。"
    voice "NCH01A_CH011_K"
    智纱 "「那，我现在就去你房间里」"
    志雄 "「嗯，我知道了。我等你过来」"
    stop music fadeout 1
    play sound "SE02_08"
    "挂断了电话，智纱的身影向着公寓的大门走去。"
    window hide
#SE_VOLC 1,0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDA01"),"True","img/SU_MDA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    hide bg1
    with dissolve
#BG_ANM_OFFC 1
    play music "BGM10"
    voice "NCH01A_SU003"
    铃 "「刚才的声音，莫非是智纱？　是来给你做饭的吗？」"
    志雄 "「嗯，是这样的。所以呢……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDB01"),"True","img/SU_MDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH01A_SU004A"
    铃 "「哈哈～，志雄你是想说，“我女朋友来了，你赶紧出去吧。{w=3}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDB02"),"True","img/SU_MDB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH01A_SU004B"
    extend "哼哼……」"
    "铃的脸上浮现了一丝笑容。那个笑容，让我有一种非常不好的预感……。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDC01"),"True","img/SU_MDC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH01A_SU005"
    铃 "「刚才以那种方式对待我，让我有点不太爽呢。不想就这么乖乖地出去了」"
    志雄 "「哎！？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDA04"),"True","img/SU_MDA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH01A_SU006"
    铃 "「还是说，志雄你打算做些什么有我在就做不得的事情吗？」"
    志雄 "「没！　才没有那种事情呢！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDA06"),"True","img/SU_MDA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH01A_SU007"
    铃 "「拼了命地否定这一点才让人感觉奇怪呢～」"
    if not persistent.dictlist[9] and persistent.show_dict:
        $persistent.dictlist[9]=True
        show screen dict_pop(i=9)
    voice "NCH01A_SU008"
    铃 "「我是不是要告诉富美子婆婆，志雄他做了什么坏事了呢～？」"
    志雄 "「请不要这样！　万一她真信了该怎么办啊！？」"
    "富美子婆婆发火很可怕啊。"
    window hide
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 0
#CHR_ALPC 0
#BG_SET_BACK 
#BG_INIC 2
#CHR_SET_BACK
#CHR_INIC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'FU'",DynamicDisplayable(mouthanime,"FU_LAA04"),"True","img/FU_LAA04A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
#BG_PRI 2
#CHR_PRIC 1
#BG_UVC 2,0,512,640,448
    show expression "img/BG17NA@2x.jpg" as bg2 zorder 8
    with dissolve
#BG_BLUR 2
#MUS_VOL 0
    play sound "SE05_09"
    voice "NCH01A_FU000_K"
    富美子 "「学生就要像个学生的样子，要健康地交往！」"
    window hide
    stop se
#BG_INIC 1
#BG_PRI 1
    scene expression "img/BG15MA@2x.jpg" as bg0 with dissolve
#BG_PRI 2
    hide bg2 with dissolve
#BG_UVC 2,0,0,640,448
    hide lh1 with dissolve
    stop se
#BG_ALPC 0
#CHR_ALPC 0
    hide bg1 with dissolve
#MUS_VOL 128
    "脑子里想像出了自己被正座的文子婆婆说教时的样子。才不要变成那样咧。"
    志雄 "「话说回来，真的不会做什么奇怪的事情啦！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDA02"),"True","img/SU_MDA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "我当然不会做那些对别人说不出口的事情。"
    "但是，好不容易智纱来了，就想两个人单独在一起……这个才是真心话。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDA04"),"True","img/SU_MDA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH01A_SU009"
    铃 "「嗯～……」"
#MESEX_A M_NOA,A_CH_SU,NCH01A_SU009,"【鈴】「嗯～……」%K%P"
    志雄 "「……」"
    "铃双臂交叉着，好像在沉思着什么。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDA01"),"True","img/SU_MDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "但是下一个瞬间，她的嘴角又浮现出恶作剧一般的笑容。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDB02"),"True","img/SU_MDB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH01A_SU010A"
    铃 "「呵呵、别做出一副那么{w=3}{nw}"
#VO_WAT VO_WAIT_START
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDB01"),"True","img/SU_MDB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH01A_SU010B"
    extend "害怕的表情嘛。不会真的打扰你俩单独在一起的时间的，我可没那么不知趣」"
    play sound "SE00_44"
    voice "NCH01A_RI000"
    莉莉丝 "「快～开～门～！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_MDB05"),"True","img/SU_MDB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH01A_SU011"
    铃 "「而且，门外的莉莉丝，好像也在等着呢」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "铃从床上下来，轻松地笑着，回自己的房间去了。"
    "……从窗户。"
    window hide
    play sound "SE00_20"
    play sound "SE01_05L"
#CHECK_NOWSKIP L_SKIP_00
label L_SKIP_00:
    stop se
    voice "NCH01A_SU011B"
    铃 "「莉莉丝，太大声的话可是会妨害四邻的哟？」"
    voice "NCH01A_RI001"
    莉莉丝 "「啊，终于给我出来了啊。那么，写得怎么样了，原稿？」"
    voice "NCH01A_SU012"
    铃 "「啊哈哈哈。莉莉丝，肚子不饿吗？　我是有点饿了啊，去莉莉丝家吃点……」"
    voice "NCH01A_RI002"
    莉莉丝 "「喂，别搪塞了好不好啊」"
    voice "NCH01A_CH012"
    智纱 "「哎，莉莉丝？　就连铃也在」"
    "智纱好像已经到了房间前面了。"
    voice "NCH01A_RI003"
    莉莉丝 "「啊，今天也是来照顾志雄的吗？」"
    voice "NCH01A_SU013"
    铃 "「已经和未婚妻上门差不多了呐～」"
    voice "NCH01A_CH013"
    智纱 "「那，那种事……」"
    "看来已经害羞了。"
#CHR_PRIC ID_ALL
#BG_OVER_CHRTC OIBG012A,0,CH_SBA01,1,SU_SDA01,(320-160),2,RI_SBA01,(320+160)
    show expression "img/OIBG012A@2x.png" as bg_over zorder 8
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SBA01"),"True","img/RI_SBA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .75
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_SBA01"),"True","img/CH_SBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter 0.5
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SDA01"),"True","img/SU_SDA01A@2x.png") as lh1 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NCH01A_RI004"
    莉莉丝 "「志雄，智纱来了哦」"
    志雄 "「我知道了啊。话说回来，你们站在门口说的话连我这里都能听见」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SBA04"),"True","img/RI_SBA04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCH01A_RI005"
    莉莉丝 "「啊。知道就好」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SBD06"),"True","img/RI_SBD06A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCH01A_RI006"
    莉莉丝 "「那，志雄就拜托你了哦。现在的这家伙，如果没有智纱的照顾差不多一个星期就会死掉了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_SBA01"),"True","img/CH_SBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH01A_CH014"
    智纱 "「啊，嗯」"
    志雄 "「没那回事。一个月左右应该还能撑得下去，大概」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SDA02"),"True","img/SU_SDA02A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SBA06"),"True","img/RI_SBA06A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    voice "NCH01A_SU014"
    铃 "「只能撑一个月啊……。还说什么大概的，没自信啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_SBA05"),"True","img/RI_SBA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NCH01A_RI007A"
    莉莉丝 "「哈……。{w=3}{nw}"
#MESA A_CH_RI,NCH01A_RI007A,"【りりす】「哈……。"
    voice "NCH01A_RI007B"
    extend "就是这样，这个废男就拜托您了，夫人」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_SBC06"),"True","img/CH_SBC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH01A_CH015"
    智纱 "「夫、夫人！？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'SU'",DynamicDisplayable(mouthanime,"SU_SDC01"),"True","img/SU_SDC01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH01A_SU015"
    铃 "「那就再见了啊，塚本智纱」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_SBB04"),"True","img/CH_SBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH01A_CH016"
    智纱 "「塚本！？」"
    window hide
    stop music fadeout 1
#SE_VOLC 1,
#CHR_ERSWC 1
    hide lh1
    hide lh2
    with dissolve
    play sound "SE00_01"
    "铃和莉莉丝，各自留下了一句随便的话就走掉了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBB03"),"True","img/CH_MBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#MESEX_A M_NOA,A_CH_CH,NCH01A_CH017,"【智紗】「……」%K%P"
    志雄 "「那～个……」"
    "就因为那两个人说了奇怪的话，总觉得有点窘迫。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MBA03"),"True","img/CH_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NCH01A_CH018"
    智纱 "「那，那我先去，准备早饭了哦。用一下厨房，可以吗？」"
#REMOVE_REEK_CHR 0
    志雄 "「啊，当然」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_PRIC ID_ALL
    "那样说着，为了掩饰自己的难为情，我把视线投向了窗外。"
    window hide
#BG_PRIC 0
#EFF_PRI 0
#BG_INIC 2
    scene expression "img/NIMG01B@2x.png" as bg2 zorder 2
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
#EFF_STAC 0,CLOUD_B,EFF_NOSKIP
#BG_ALP_AUTOC 0,0,0,1
    hide bg0 with dissolve
#BG_PRIC 0
#EFF_PRI 0
    "外面的空气，已经充满了盛夏的炽热。"
    "高中３年级的７月——我和智纱从开始交往到现在，已经过了半年以上。"
    window hide
    scene expression Solid("000") with fade
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
#GRAPH_ERS
#GRAPH_INI 
    stop se
    stop sound
    stop music fadeout 1
#FADE_IN 0
    $ renpy.end_replay()
    return