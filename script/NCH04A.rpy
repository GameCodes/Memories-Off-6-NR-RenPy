label NCH04A:
    $currentlabel = "NCH04A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '07'
    $day = '20'
    $date = '4'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 5,CAL_0720
    show expression "img/NIMG15L-568h@2x.jpg" as cal zorder 5
    show expression "img/07_20_THURSDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
#FADE_OUT 1,32,COL_WHITE
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG04AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG04AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_14L"
    pause (32/32.0)
#FADE_IN 1,128
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    志雄 "「啊……早上就这么热啊……」"
    "从正上方照射下来的强烈日光。光这一点就让人没心思去学校。"
    "看到一边叹着气一边慢吞吞地走着的我，智纱噗哧一笑。"
    window hide
#SE_VOLC 1,(64/2)
#CHR_INIC 0
#CHR_MGNC_F 0,CH_LKB02,CH_LAB02,(320+96)
    play music "BGM03"
    voice "NCH04A_CH000"
    智纱 "「从明天开始就是暑假了，再加把劲」"
    志雄 "「……是啊」"
    "今天是结业式。从周围的其他学生那里，零零落落地听到「暑假要怎么过呢」之类的话。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKB06"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAB06"),"not F103==0","img/CH_LKB06A@2x.png","True","img/CH_LAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH04A_CH001"
    智纱 "「啊，对了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAB01"),"not F103==0","img/CH_LKB01A@2x.png","True","img/CH_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH04A_CH002"
    智纱 "「昨天说过的，和志雄君一起去旅行的事情。我问过父亲和母亲了，他们说可以去的」"
    志雄 "「真的！？」"
    "如果智纱去不成的话，一个人跟老爸他们去也没什么意思。所以在想是不是就不去了……。"
    志雄 "「太好了。智纱能来的话，一定会是一个非常快乐的旅行的」"
    志雄 "「可是，你父母没有反对吗？」"
    "老实说，我觉得智纱的父母不会允许她在外面住的啊。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKA03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAA03"),"not F103==0","img/CH_LKA03A@2x.png","True","img/CH_LAA03A@2x.png") as lh0 zorder (10+0):
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
    voice "NCH04A_CH003A"
    智纱 "「啊，嗯，{w=3}{nw}"
#MESA A_CH_CH,NCH04A_CH003A,"【智紗】「啊，嗯，"
#THREAD_STP 1
#REMOVE_REEK_CHR 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAA01"),"not F103==0","img/CH_LKA01A@2x.png","True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH04A_CH003B"
    extend "嗯」"
    "哎？　总觉得智纱的反应有点微妙啊……。"
    志雄 "「莫非，果然还是遭到反对了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKB04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAB04"),"not F103==0","img/CH_LKB04A@2x.png","True","img/CH_LAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH04A_CH004"
    智纱 "「没，没，没那回事的！」"
    "智纱一个劲地摇着头否定着。"
    志雄 "「那样的话就好」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKB03"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAB03"),"not F103==0","img/CH_LKB03A@2x.png","True","img/CH_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "话虽如此，和智纱旅行么。"
    "直到刚才还很消沉的心情，现在已经完全转晴了。平常只会让人感到怨恨的暑热，现在反倒感到可爱了，虽然这么说很势利。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG09AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression Solid("000") with None
#FADE_IN 0
    play sound "SE06_02"
    "……。"
    "…………。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128,128
#BG_UVC 0,(640/8),((448/16)*3),(640/2),(448/2)
    scene expression "img/BG09AA@2x.jpg" as bg0 with dissolve
    stop se fadeout 1
#FADE_IN 1
    play music "BGM10"
    "今天是期末典礼，学校相关的事情，在上午就都结束了。但学生会还剩下一些类似学期总结的业务等着我去处理。"
    "必须对本学期的学生会活动做一个汇总，然后提交给学校。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+192),(448/16)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAB01"),"not F103==0","img/CH_LKB01A@2x.png","True","img/CH_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        .8
    with dissolve
    voice "NCH04A_CH005"
    智纱 "「志雄君，这边的收据要怎么办？」"
    志雄 "「那些要和月报进行核对，确认一下是在哪里使用的，然后交给负责会计工作的人就行了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKB05"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAB05"),"not F103==0","img/CH_LKB05A@2x.png","True","img/CH_LAB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH04A_CH006"
    智纱 "「嗯，知道了」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "智纱点了点头，转向汇总着文件的架子。"
    "智纱的身影，已经完全融进这个叫做学生会的地方了。"
    志雄 "「好了。我也去工作吧」"
    "智纱不是学生会成员，都在那努力，我也不能偷懒啊。"
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    menu:
        "考虑旅行的事情":
            $F7=0
        "集中工作":
            $F7=1
    if F7==0:
        jump L_NCH04A_SEL00_A
    if F7==1:
        jump L_NCH04A_SEL00_B
label L_NCH04A_SEL00_A:
    $F1+=1
    "但是，不管怎样，脑海里都是和智纱一起旅行的事。"
    "会是什么样的旅行呢……。替换的衣服之类的，不准备可不行。"
    "这么说来，旅行的目的地是哪里？　只从老爸那里听说了目的地的地名，那里是个什么样的地方，就不知道了。"
    "稍微调查一下看看吧。"
    window hide
    play sound "SE06_38"
    pause (16/32.0)
    play sound "SE06_38"
    pause (16/32.0)
    play sound "SE06_37"
    "在放在学生会室中的电脑上，打开了网上浏览器，在搜索网站上输入了从老爸那里听来的地名。"
    if not persistent.dictlist[48] and persistent.show_dict:
        $persistent.dictlist[48]=True
        show screen dict_pop(i=48)
    "目的地是叫『龙境』……。"
    "然后点击了搜索结果中最上面的网站。"
    window hide
#SE_WATC 0
    play sound "SE06_38"
    "……旅行的目的地，大概是最近作为观光地发展起来的小镇，离海很近，而且有一座有湖的山。风景很美，非常热门。"
    "湖吗。智纱，没关系吧？"
#MUS_VOL 0
    voice "NCH04A_YU000"
    结乃？ "「学长！」"
    play sound "SE03_12"
#THREAD_STA 1,THREAD_QUA_WIN
#VIB_DOKA 
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    志雄 "「呜哇！？」"
#MESA A_CH_SI,"【志雄】「呜哇！？」"
#THREAD_WAT 1
#WIN_POS 0,0
#VIB_STP 5
#MESX "%K%P"
    "什，什么啊！？"
    "耳边突然响起这样一个声音，我差一点从椅子上掉了下来。"
    window hide
#MUS_VOL 128
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,640
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB03"),"True","img/YU_LAB03A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .8
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR1 128,(320+192)
#MOV_CHR_GO 1
    "向声音的方向看去，站在那里的是吃惊的学妹。"
    志雄 "「哈，吓我一跳啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAC02"),"True","img/YU_LAC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH04A_YU001"
    结乃 "「从刚才我就喊你好几次了啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB05"),"True","img/YU_LAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH04A_YU002"
    结乃 "「哎？　在查些什么呢？」"
    志雄 "「没有，也没什么特别的！」"
    window hide
    play sound "SE06_38"
    "我慌忙把电脑的浏览器关上。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA03"),"True","img/YU_LAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH04A_YU003"
    结乃 "「……为什么会那样慌慌张张地呢」"
    "春日同学流露出了一种很诧异的声音。"
    "并没有向她必要去隐瞒我和智纱要一起去旅行的事。但是，总觉得如果说了的话会被他们戏弄，所以下意识就掩饰上了。"
    jump L_NCH04A_SEL00_X
label L_NCH04A_SEL00_B:
    志雄 "「好！　那今天就快点把工作都搞完吧」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+192)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAC02"),"True","img/YU_LAC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH04A_YU004"
    结乃 "「今天可是真的很有劲头呢。是发生什么事了吗？」"
    志雄 "「是吗，我觉得和平常没区别呢」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH04A_YU005"
    结乃 "「是这样吗？　我觉得一定是有什么好事发生了」"
    志雄 "「没，没有，不是什么大不了的事」"
    "好敏锐啊，春日同学……。"
    "自从在智纱那里听说了她父母允许她住在外面以来，心里就高兴个没完。这个好像体现到表面上了。"
    "和智纱去旅行的事并没有必要隐瞒，但是说了的话就会被他们戏弄，所以没怎么跟人提起。"
    志雄 "「但是，有干劲不是挺好的嘛？　一旦调动起了积极性，工作也就有进展了」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAA04"),"True","img/YU_LAA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH04A_YU006"
    结乃 "「话是这么说没错」"
    jump L_NCH04A_SEL00_X
label L_NCH04A_SEL00_X:
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAC02"),"True","img/YU_LAC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH04A_YU007"
    结乃 "「嗯～。总觉得有点可疑呢」"
    志雄 "「心理作用，心理作用。来，工作、工作吧。今天是这个学期最后的学生会工作了……」"
    voice "NCH04A_YU008"
    结乃 "「哼嗯……」"
    "春日同学用一种怀疑的眼神看着我这边。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB01"),"True","img/YU_LAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH04A_YU009"
    结乃 "「这么说来，塚本学长」"
    志雄 "「什么？」"
    stop music fadeout 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB02"),"True","img/YU_LAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NCH04A_YU010"
    结乃 "「和智纱学姐的新婚旅行，希望你们玩得高兴。期待你们谈旅行感想哦」"
    志雄 "「……哎？」"
    "为什么会知道那个的，春日同学！？"
    window hide
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
    scene expression "img/BG83EA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112,128
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MKA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MAA01"),"not F103==0","img/CH_MKA01A@2x.png","True","img/CH_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE05_13L"
    pause (32/32.0)
#FADE_IN 1
#SE_VOLC 1,(64/4)
    play music "BGM03"
    志雄 "「什么啊，是智纱和春日同学说的啊。她知道这件事也是情理之中了」"
    "我说着这些，从鞋箱里取出了鞋子。学生会的工作已经完了，今天也和智纱一起回去。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MKC02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MAC02"),"not F103==0","img/CH_MKC02A@2x.png","True","img/CH_MAC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH04A_CH007"
    智纱 "「莫非，这话说了会很糟糕吗？」"
    志雄 "「不是，并不是想要隐瞒啦。只是觉得，春日同学会知道，有点不可思议」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MKC01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MAC01"),"not F103==0","img/CH_MKC01A@2x.png","True","img/CH_MAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "只是——。"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
##BG_UVC 2,(640/8),((448/16)*3),(640/2),(448/2)
    show expression "img/BG09AA@2x.jpg" as bg2 zorder 8
#BG_BLUR 2
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1,(320+192)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LAB02"),"True","img/YU_LAB02A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .8
    with dissolve
#SE_VOLC 1,0,16
#MUS_VOL 64,16
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 0
#BG_ALPC 2,128
#CHR_ALPC 0
#CHR_ALPC 1,128
    hide bg1 with dissolve
    voice "NCH04A_YU010_K"
    结乃 "「和智纱学姐的新婚旅行，希望你们玩得高兴。期待你们谈旅行感想哦」"
    window hide
#BG_INIC 1
#BG_PRI 1
    scene expression "img/BG83EA@2x.jpg" as bg0
    with dissolve
    hide bg2
#BG_UVC 2,0,0,640,448
    hide lh1
#BG_ALPC 0,128
#CHR_ALPC 0,128
#SE_VOLC 1,(64/4),16
#MUS_VOL 128
    hide bg1 with dissolve
    "听她的那个口气，总觉得她是不是好像有点搞错了什么东西似的……。"
    志雄 "「啊，这么说来」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MKA04"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MAA04"),"not F103==0","img/CH_MKA04A@2x.png","True","img/CH_MAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "还有事情必须要和智纱说呢。"
    志雄 "「旅行目的地的龙境，好像是个被湖和山环绕的地方。智纱，没关系吗？」"
    "智纱因为过去的创伤，有严重的恐水症。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_MKA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_MAA01"),"not F103==0","img/CH_MKA01A@2x.png","True","img/CH_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH04A_CH008"
    智纱 "「啊，嗯。我也在网上调查过了，所以知道的」"
    voice "NCH04A_CH009"
    智纱 "「那里没关系，你不用在意的。不管是海还是湖，只要不靠近就没有问题的」"
    志雄 "「这样啊。这样的话还好」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG06EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG06EA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+96)
#CHR_COLC 0,128,120,112,128
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAB01"),"not F103==0","img/CH_LKB01A@2x.png","True","img/CH_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .65
    with dissolve
#SE_VOLC 1,(64/2),16
#BG_BLUR 0
#FADE_IN 1
    voice "NCH04A_CH010"
    智纱 "「暑假里也有学生会工作的吧？　我也来帮忙吧」"
    志雄 "「嗯，有倒是有——你不用勉强自己来帮忙的吧？　平常让你帮忙就已经觉得不好意思了，连暑假里也……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAB02"),"not F103==0","img/CH_LKB02A@2x.png","True","img/CH_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH04A_CH011"
    智纱 "「没事的，能帮忙做学生会的工作，我也很高兴的」"
    "就算你那么说……。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    show expression "img/BG01EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG01EA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112,128
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKA01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAA01"),"not F103==0","img/CH_LKA01A@2x.png","True","img/CH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE08_17L"
    pause (32/32.0)
#BG_BLUR 0
#FADE_IN 1
#SE_VOLC 1,128
    play music "OBGM17"
    voice "NCH04A_CH012"
    智纱 "「那，明天见」"
    voice "NCH04A_CH013"
    智纱 "「明天下午我和结乃约好去做广播节目，不过还是能来给你做午饭的」"
    志雄 "「你有事情的话，不必勉强自己来啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKB02"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAB02"),"not F103==0","img/CH_LKB02A@2x.png","True","img/CH_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH04A_CH014"
    智纱 "「没关系的，我只是因为想来才来的」"
    志雄 "「……那样的话，倒还好」"
    "见她用那样的笑容在说着这些话，我什么也说不出口了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==0",DynamicDisplayable(mouthanime,"CH_LKB01"),"renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH' and not F103==1",DynamicDisplayable(mouthanime,"CH_LAB01"),"not F103==0","img/CH_LKB01A@2x.png","True","img/CH_LAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCH04A_CH015"
    智纱 "「再见了」"
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
    "智纱转过身去，向着检票口的方向走去。"
    志雄 "「要照顾我，要帮忙做广播的节目，要做学生会的工作……那样的话，智纱自己的时间不就没有了吗」"
    "一边目送着智纱的背影，一边无意识地自言自语道。"
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
#label THREAD_QUA_WIN
#TH_QUAKE_WIN 4
#EOT
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT