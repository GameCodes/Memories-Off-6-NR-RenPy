label NCL15A:
    $currentlabel = "NCL15A"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '08'
    $day = '31'
    $date = '4'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 2
##BG_POSC 0,(60),0,640,448
    show expression "img/EXBG10AA@2x.png" as bg0 zorder 0 with dissolve
#FADE_IN 1,128
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
    "——恍惚中，暑假已经接近尾声。"
    "偶然间停下手中忙个不停的笔，把视线转移到挂历上。"
    window hide
#MUS_VOL 64
#FADE_OUT 1
#BG_ALPC 0
#BG_ALPC 2
#FADE_IN 0
#CAL_DSP_BG NIMG15F,CAL_0831
    show expression "img/NIMG15G-568h@2x.jpg" as cal zorder 5
    show expression "img/08_31_THURSDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
#FADE_OUT 1
#BG_ALPC 0,128
#BG_ALPC 2,128
#MUS_VOL 128
#FADE_IN 1
    "今天是８月３１日。明天开始将会是新的学期。"
    志雄 "「已经是这个时候了吗？」"
    "克罗艾学姐住回自己家已经过去了数日。"
    "学姐能够和家人团聚，我由衷地为她感到开心。不过，学姐回到了的那个家庭，并没有独属于我的地方，真的是有些寂寞呢。"
    "与学姐见面的时间少了很多。今天学姐也并没有来我家。"
    志雄 "「孤单一人吗……？」"
    "哪怕打个电话也好，我突然很想和谁说说话。不知所措的情绪像野草一样疯长。"
    "这短暂的烦恼也让我意识到，我现在想听到的不是别人的声音，而是学姐的声音。"
    window hide
    stop music fadeout 1
    play sound "SE00_04"
    pause (32/32.0)
    志雄 "「嗯？是谁？」"
    "带着可能是学姐的期待，我迅速起身向门厅走去。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    show expression "img/OIBG012A@2x.png" as bg1 zorder 1 with dissolve
    play sound "SE01_13"
#BG_ALP_AUTOC 1,128,0,F24,48
#BG_ALP_SAVEC 1
#BG_POSC 0,0,0,640,448
#BG_POSC 2,0,0,640,448
#BG_SWPC 0
#BG_ERSWC 1,2,BG_NOFADE
#BG_PRI 1
#BG_PRI 0
#BG_PRI 2
    stop se
    志雄 "「在，这就来了！」"
    window hide
    play sound "SE00_00"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBA01"),"True","img/CL_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU000"
    克罗艾 "「打扰了。」"
    志雄 "「……欢，欢迎光临！」"
    "真的是学姐，一瞬间，我发出了惊讶的声音。"
    window hide
    play music "BGM04"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBA02"),"True","img/CL_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU001"
    克罗艾 "「从现在起，我想要多和你在一起……难道说你在忙吗？」"
    志雄 "「完全没有啦……」"
    "喜悦的心情溢于言表，实在是太好了呢。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB06"),"True","img/CL_MBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU002"
    克罗艾 "「是吗，太好了！那赶紧出发吧～」"
    "学姐拉住我的手臂，把我使劲拽了起来。"
    志雄 "「没问题，不过出发是去哪里？」"
    "我在门厅边穿鞋边说。虽然这样问了，但实际上无论是天涯还是海角我都会和学姐一起去的。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB04"),"True","img/CL_MBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU003"
    克罗艾 "「去哪里还没决定。志雄想去什么地方？」"
    志雄 "「嗯？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB06"),"True","img/CL_MBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU004"
    克罗艾 "「来一次久违了的约会吧～」"
    "学姐开心地说着，又一次紧紧握住了我的手。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG31AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG31AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_08L"
    pause (32/32.0)
#FADE_IN 1
    志雄 "「真是期待呢！」"
    "我千辛万苦才驾驭好马儿赶了上来，与此同时在旁边骑马并行着的学姐向我说道。"
    window hide
#FADE_OUT 1
#ROUTINE_STA
#CHR_INIC 0
#CHR_POSC 0,50
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'EVN'",DynamicDisplayable(mouthanime,"EVN_CL02A"),"True","img/EVN_CL02AA@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#BG_FLG EVN_CL02A
#EFF_STAC 0,HORSE_RIDE,EFF_NOSKIP
#ROUTINE_STP
#BG_ANM_ONC 0,0,CHRID_CL
#FADE_IN 1
    voice "NCL15A_KU005"
    克罗艾 "「嗯，那些事情，多亏了志雄……」"
    志雄 "「我没做什么啦。」"
    voice "NCL15A_KU006"
    克罗艾 "「不说出口就无法传递心意，你教给了我这一点。」"
    window hide
#BG_INIC 1
    show expression "img/IBG01B@2x.jpg" as bg1 with dissolve
#BG_ANM_OFFC 0
    "学姐的声音停住了，短暂的沉默之后，学姐再次开口却流露出了一副十分寂寞的神情。"
    voice "NCL15A_KU007"
    克罗艾 "「呐，我们……不知不觉也错过了很多东西……」"
    志雄 "「确实是令人悔恨呢。」"
    "心中不愿去回忆这些事。不过我觉得逃避也是不行的。"
    "看到我沉重地深思着，学姐用明快的声音说道。"
    window hide
#BG_ALP_AUTOC 1,0,0,F24
#BG_ALPC 1
    hide bg1 with dissolve
#BG_ANM_ONC 0,0,CHRID_CL
    voice "NCL15A_KU008"
    克罗艾 "「所以，做个约定吧。」"
    志雄 "「约定？」"
    voice "NCL15A_KU009"
    克罗艾 "「嗯。互相之间不能有隐瞒的约定。」"
    志雄 "「我对学姐可从来没什么隐瞒的————」"
    "面对我不假思索的反驳，学姐嘀嘀咕咕地说道。"
    voice "NCL15A_KU010"
    克罗艾 "「放焰火的时候……」"
    志雄 "「呃……」"
    "是指我瞒着学姐和她父母打招呼的事情吧。想不到学姐那么在意那件事。"
    志雄 "「那个，并不是故意而为之的嘛。而且，学姐就没有瞒着我的事情吗？」"
    voice "NCL15A_KU011"
    克罗艾 "「我？我嘛……只有一个哦～」"
    "学姐露出一副十分难为情的笑容……这下，我完全沦陷了。"
    志雄 "「那，是什么呢？」"
    voice "NCL15A_KU012"
    克罗艾 "「那是————」"
    window hide
#BG_INIC 1
    show expression "img/IBG01B@2x.jpg" as bg1 with dissolve
#BG_ANM_OFFC 0
    "就在学姐即将开口之际。"
    "只见学姐骑在心爱的马儿身上脸上闪耀着笑容飞奔了出去……完全失去了追问的时机。"
    志雄 "「真没办法啊……」"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG03EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG03EA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB01"),"True","img/CL_MBB01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE05_13L"
    pause (32/32.0)
#FADE_IN 1
    play music "BGM13"
    "这之后我跟着学姐到处转了一整天，结束时已经筋疲力尽了。"
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
#BG_UVC 2,0,512,640,448
    show expression "img/BG43AA@2x.jpg" as bg2 zorder 2 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_ALPC 1
#CHR_POSC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC01"),"True","img/CL_LBC01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#SE_VOLC 1,0,16
#BG_INIC 1
#BG_PRI 1
    scene expression "img/BG43AA@2x.jpg" as bg0 with dissolve
    hide lh0 with dissolve
#BG_ALPC 2,128
#CHR_ALPC 1,128
#FILT_IN 0,0,COL_DARK2
#BG_BLUR 2
    "在商场一起看各种小玩意、"
#SCRMODE_SPC SCR_FULL_ALT
#MES "%n%n%S032%FS在商场一起看各种小玩意、%FE%K"
#CHR_PRIC 1
#BG_PRI 2
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/EXBG02A@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_PAL_BGC 2,EXBG02A
#CHR_SET_BACK
#CHR_INIC 2
#CHR_PRIC 2
#CHR_POSC 2,320
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_ZBB06"),"True","img/CL_ZBB06A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
    with dissolve
#BG_BLUR 2
#BG_ALP_AUTOC 2,0,0,F24,48
#CHR_ALP_AUTOC 1,0,0,F24,48
#BG_ALP_SAVEC 2
#CHR_ALP_SAVEC 1
#CHR_SWPC 1
#CHR_PRIC 2
#CHR_PRIC 1
#CHR_ALPC 2,128
#BG_SWPC 0
#BG_PRI 0
#BG_PRI 2
#BG_ALPC 2,128
#BG_BLUR 2
    "在咖啡厅一起吃蛋糕、"
#MES "%n%n%n%S032%FS%t002在咖啡厅一起吃蛋糕、%FE%K"
#CHR_PRIC 1
#BG_PRI 2
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG23AA1@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_PAL_BGC 2,BG23AA1
#CHR_SET_BACK
#CHR_INIC 2
#CHR_PRIC 2
#CHR_POSC 2,(320-160)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBA07"),"True","img/CL_LBA07A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
    with dissolve
#BG_BLUR 2
#BG_ALP_AUTOC 2,0,0,F24,48
#CHR_ALP_AUTOC 1,0,0,F24,48
#BG_ALP_SAVEC 2
#CHR_ALP_SAVEC 1
#CHR_SWPC 1
#CHR_PRIC 2
#CHR_PRIC 1
#CHR_ALPC 2,128
#BG_SWPC 0
#BG_PRI 0
#BG_PRI 2
#BG_ALPC 2,128
#BG_BLUR 2
    "在车站的月台上一起眺望大海……"
#MES "%n%n%n%S032%FS%t004在车站的月台上一起眺望大海……%FE%K%O032"
    window hide
#BG_SET_BACK 
#BG_INIC 0
#BG_ALPC 0
#BG_INIC 1
#BG_PRI 1
    scene expression "img/BG03EA@2x.jpg" as bg0 with dissolve
    hide bg2 with dissolve
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#BG_UVC 2,0,0,640,448
#BG_ALPC 0,128
#SE_VOLC 1,64
    hide bg1 with dissolve
    "全部都是最快乐的时光。"
    "这几天积攒的所有寂寞感\n全部一扫而空。"
    "这些全部都是，无法替代的回忆。"
    window hide
#SE_VOLC 1,(64/2)
#FILT_OUT 48
#SCRMODE_SPC SCR_WINDOW
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB06"),"True","img/CL_MBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU013"
    克罗艾 "「嗯～！好久没有玩得这么尽兴了！」"
    志雄 "「拜你所赐，我已经是精疲力尽了呢……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBA01"),"True","img/CL_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU014"
    克罗艾 "「这可不行哦，你可是男生啊。」"
    志雄 "「最近在家一直忙于学习来着……」"
    voice "NCL15A_KU015A"
    克罗艾 "「这样啊……{w=3}{nw}"
#MESA A_CH_KU,NCL15A_KU015A,"【クロエ】「这样啊……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBA03"),"True","img/CL_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU015B"
    extend "那个，说起来志愿的学校决定了没有？」"
    "笑容一转，学姐换了一幅认真的模样。我也让自己的表情变得认真起来，与学姐四目相对。"
    志雄 "「嗯。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBA01"),"True","img/CL_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU016"
    克罗艾 "「哪里呢？」"
    "学姐用带着些许期待的目光看着我。而我将自己已经决定好的志愿，告诉了学姐。"
    志雄 "「希望还能继续做学姐的后辈！」"
    "听了我的回答，学姐的表情舒缓了很多。看到学姐那柔和的笑容，我的心里咚咚直跳。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MBB04"),"True","img/CL_MBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU017"
    克罗艾 "「是、是吗。按照志雄现在的努力的话肯定没问题的。不过，当初明明是一副烦恼样子的，什么让你下定决心了呢？」"
    志雄 "「原因有很多，不过最主要的只有一个。」"
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
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB03"),"True","img/CL_LBB03A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCL15A_KU018"
    克罗艾 "「是什么？」"
    "学姐靠过来询问道。虽然我觉得很不好意思，想放弃继续说下去的念头，不过最后还是说出了口。"
    志雄 "「不想让克罗艾一个人孤零零的……这样啦～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBC05"),"True","img/CL_LBC05A@2x.png") as lh0 zorder (10+0):
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
    voice "NCL15A_KU019"
    克罗艾 "「我？那……」"
#THREAD_STP 1
#REMOVE_REEK_CHR 0
    "学姐的脸一下子泛起了红晕。而我的脸也一定是红红的吧。"
    志雄 "「无论什么事都能比其他人做得好，轮到自己的事情却完全不行。视线离开你一刻都会很担心很担心.」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB04"),"True","img/CL_LBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU020"
    克罗艾 "「志～雄～？」"
    "学姐一副不满的样子看着我。不过，这是我的真心话。"
    志雄 "「所以，如果可以的话，我要陪在克罗艾身边.」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB03"),"True","img/CL_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU021"
    克罗艾 "「永远？」"
    志雄 "「嗯，永远。如果再有停滞不前的时候，无论多少次我都会在背后给你力量，并且会紧紧地握住你的手。」"
    "……啊哈……"
    "不知不觉，说了这么难为情的话。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBA07"),"True","img/CL_LBA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "学姐看着我，已是满脸通红。"
    voice "NCL15A_KU022"
    克罗艾 "「嗯，拜托你了哦……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBA02"),"True","img/CL_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU023"
    克罗艾 "「呐……」"
    志雄 "「嗯？」"
    voice "NCL15A_KU024"
    克罗艾 "「再叫一次我的名字啦。」"
    志雄 "「名字？」"
    "再叫一次？"
    志雄 "「……克罗艾学姐」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBA05"),"True","img/CL_LBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU025"
    克罗艾 "「志～雄～？」"
    window hide
#SE_VOLC 1,0
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG39EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG39EA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
#SE_VOLC 1,64
#FADE_IN 1
    play music "OBGM29"
    pause (32/32.0)
#SE_VOLC 1,(64/4)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBA01"),"True","img/CL_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「忘了这个东西了吧……」"
    "在门厅前，我把参考书递了过去。"
    "这样约会就算结束了。接下来，要送学姐回家……"
    "不经意间，心中被莫名的寂寞充斥。仿佛是寻找让学姐留下来的理由，我说道。"
    志雄 "「说起来，有件事想问你……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB01"),"True","img/CL_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU026"
    克罗艾 "「什么？」"
    志雄 "「对我隐瞒着的那件事？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB04"),"True","img/CL_LBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU027"
    克罗艾 "「啊……想知道吗？」"
    志雄 "「想知道……」"
    voice "NCL15A_KU028"
    克罗艾 "「不是什么重要的事啦……」"
    "在骑马俱乐部的时候让学姐糊弄过去了，可不能再错过了，想到这我立马摆出一副严肃的表情。"
    志雄 "「真狡猾。不是说两人之间不能隐瞒的吗？」"
    voice "NCL15A_KU029"
    克罗艾 "「是呢……」"
    "学姐小声碎碎念着，然后放弃了抵抗，不再躲躲闪闪，直接了当地说道。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBA07"),"True","img/CL_LBA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU030"
    克罗艾 "「其实，我从第一次见到志雄的时候开始，就一见钟情……了……就是这样啦……」"
    志雄 "「————诶？」"
    "比起喜悦的心情，惊讶的成分占了更多。"
    志雄 "「是这样。诶！？是这样的？」"
    "从一开始？一见钟情？第一次见面的时候开始？那就是我加入学生会的时候，刚升上２年级的春天？那不是比奏云祭更早的时候吗！！"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB04"),"True","img/CL_LBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU031"
    克罗艾 "「真，真是的，怎么了嘛。人家都说完了呢……」"
    "学姐使劲地摆着手，看起来是相当害羞的告白一样。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB02"),"True","img/CL_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU032"
    克罗艾 "「不过，现在看来，那份感情是正确的。」"
    志雄 "「学姐……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LBB04"),"True","img/CL_LBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU033"
    克罗艾 "「全部，都多亏了志雄……」"
    voice "NCL15A_KU034"
    克罗艾 "「学生会的活动顺利举行也好，今天我能够站在这里也好，我能和家人融洽地生活在一起也好……这些全部都是托志雄的福呢。」"
    voice "NCL15A_KU035"
    克罗艾 "「谢谢你。」"
    志雄 "「啊，没有啦……」"
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
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XBB02"),"True","img/CL_XBB02A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCL15A_KU036"
    克罗艾 "「比什么都感谢————」"
    "学姐靠上前来挽住了我的手臂。"
    voice "NCL15A_KU037"
    克罗艾 "「嗯，在这里果然就安心多了……」"
    志雄 "「诶？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XBB06"),"True","img/CL_XBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL15A_KU038"
    克罗艾 "「所以……」"
    "看着我惊讶的眼神，学姐报以满脸的笑容。"
    voice "NCL15A_KU039"
    克罗艾 "「只要在这里的话，我就能更加努力。这样我就满足了。在你身边，这是我的另一个家。对我来说，最最幸福的地方。」"
    志雄 "「学姐……」"
    "闭上了眼睛。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XBB02"),"True","img/CL_XBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "学姐轻轻地，闭上了眼睛。"
    window hide
    stop sound
#FADE_OUT 1,16,COL_WHITE
    scene expression Solid("fff") with dissolve
#BG_SET_BACK 
#BG_INIC 0
#FADE_IN 0
    "心跳声宛如锣鼓齐鸣，我们的嘴唇自然地接近了。"
    window hide
#FADE_OUT 0,0,COL_WHITE
#BG_SET_BACK 
#BG_INIC 0
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL12A")]=True
    scene expression "img/EVN_CL12A@2x.jpg" as bg0 zorder 0 with dissolve
#FADE_IN 1,128
    "学姐泛着红晕的脸颊在夕阳的洗礼下，显得格外美丽。"
    voice "NCL15A_KU040B"
    克罗艾 "「嗯……」"
    "转瞬之间，我们的嘴唇并在了一起。"
    "留恋着嘴唇那轻柔的触感，我们，缓缓地分开。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL12B")]=True
    show expression "img/EVN_CL12B@2x.jpg" as bg0 with dissolve
    "学姐，更加用力地挽住了我的手臂。"
    voice "NCL15A_KU041"
    克罗艾 "「今天也好，明天也好，以后的每一天也好，这里都是我最最幸福的家。」"
    voice "NCL15A_KU042"
    克罗艾 "「请永远，陪在我身边！」"
    志雄 "「当然。」"
    志雄 "「今后永远都会，无论何时！」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL12C")]=True
    show expression "img/EVN_CL12C@2x.jpg" as bg0 with dissolve
    voice "NCL15A_KU043"
    克罗艾 "「————嗯。」"
    "漫长的暑假结束了，明天又会是新的一天。"
    "两个人将在一起度过，那崭新的每一天————"
    "永远在一起，朝向更远的地方！"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_CL12D")]=True
    show expression "img/EVN_CL12D@2x.jpg" as bg0 with dissolve
    pause
#MUS_VOL 255
    pause (128/32.0)
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1,128,COL_WHITE
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_FACE_NEAR
#CHR_SCL_AUTOC 0,384,384,1,F123
#CHR_POS_AUTOC 0,,(448/2),1,F123
#CHR_SCL_SAVEC 0
#CHR_POS_SAVEC 0
#EOT
#label THREAD_FACE_FAR
#CHR_SCL_AUTOC 0,256,256,1,F123
#CHR_POS_AUTOC 0,1,F123
#CHR_SCL_SAVEC 0
#CHR_POS_SAVEC 0
#EOT
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT