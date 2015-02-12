label NYU13A:
    $currentlabel = "NYU13A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '31'
    $date = '1'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 3,CAL_0731
    show expression "img/NIMG15G-568h@2x.jpg" as cal zorder 5
    show expression "img/07_31_MONDAY@2x.png" as cal_date zorder 6:
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
    scene expression "img/BG14AA@2x.jpg" as bg0 with dissolve
    play sound "SE02_02L"
#FADE_IN 1
    play sound "SE05_14L"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    "从手机中传来的，仍然只有不变的铃声。"
    "最后一次听到这个号码对面的声音，到底是什么时候呢？"
    play sound "SE02_03"
    "明明只是几天前的事情而已，不知道为什么却感觉特别遥远。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM10"
#SE_VOLC 1,32
    voice "NYU13A_KA000"
    神奈 "「早上好，志雄。谢谢你的毛毯哦。」"
    志雄 "「嗯。没有着凉或是感冒什么吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA02"),"True","img/KA_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA001"
    神奈 "「不要紧哦。要是盖了毛毯后都感冒了的话，那岂不是很对不起志雄。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA05"),"True","img/KA_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "笑着开玩笑的神奈，很快就表现出担心的样子并仔细地打量着我。"
    voice "NYU13A_KA002"
    神奈 "「对不起……结果还是住在志雄的房间里了。」"
    志雄 "「那也是没办法的事情了。毕竟很累了。」"
    "解释清楚的话，谁都能理解的吧……大概吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA003"
    神奈 "「啊，还为我空着床呢。于是我就毫不客气的用了哦。」"
    志雄 "「嗯。睡得还好吧？」"
    "早上醒来的时候，看到神奈在床上平缓地安睡着。"
    "而这时，我被毛毯裹得很好，没有盖到的地方，也被之前我给神奈盖的那条毛毯补了一层。"
    "虽然因此被热得很早就醒了过来，不过对于她的关心我还是很感谢的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA02"),"True","img/KA_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA004"
    神奈 "「当然没有。反而睡得特别安心。所以早早就醒过来了。」"
    志雄 "「你还真是厉害啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA09"),"True","img/KA_LAA09A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA005"
    神奈 "「因为是志雄的床嘛。」"
    "面对着天真地微笑着的神奈，我突然感到了一股异样的悸动。"
    "那应该是信赖的证明吧，不过还是让人感到不好意思……差一点就产生误会了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA05"),"True","img/KA_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA006"
    神奈 "「电话，是打给结乃的吗？」"
    志雄 "「嗯。不过还是联络不上……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA007"
    神奈 "「现在是暑假嘛。我们起得那么早才比较奇怪的哦。」"
    "路上能看见急匆匆上班的上班族。"
    "我们结果还是在和平时上学时间差不多的时候醒来，并开始了行动。"
    "结乃她……或许还在睡着也说不定。"
    志雄 "「是啊。那么，先吃饭再去找吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA02"),"True","img/KA_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA008"
    神奈 "「嗯。俗话说饿着肚子没法战斗的嘛。」"
    "今天也打算找结乃一整天……"
    "就算是找到了，也必须面对在截止前的一点点时间里制作出广播的挑战。"
    "到时候或许连睡觉的时间都没有了，所以现在应该好好地保存一下体力。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA009"
    神奈 "「我看过冰箱了，料理的材料很齐全的样子，那我去做喽。」"
    志雄 "「诶？你擅长料理？」"
    "结乃好像不怎么擅长这个，神奈如何呢？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA03"),"True","img/KA_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA010"
    神奈 "「这个就请吃过了再做评价吧。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "神奈露出让人完全不用担心的笑容，比我先一步进到了公寓内。"
    "过了不一会儿，从房间里传来了神奈的叫声。"
    voice "NYU13A_KA011"
    神奈 "「必杀！闪光之投掷——！」"
    "听到和必杀技名字一般气势满满的神奈的喊声，我上楼赶往自己的房间。"
    志雄 "「真的……是在做料理吗？」"
    voice "NYU13A_KA012"
    神奈 "「还有这里，超绝必杀技闪光之——」"
    "连续不断传来的神奈的叫声，我毫不犹豫地冲进了房间。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG03AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG03AA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE01_12L"
    play sound "SE05_15L"
#FADE_IN 1
    志雄 "「好像很厉害的样子……在放必杀技一样。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA08"),"True","img/KA_LAA08A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA013"
    神奈 "「好像不是在夸奖我的料理吧，这个——」"
    志雄 "「啊，不是。很好吃哦。」"
    "气势十足的叫声，舞动着的平底锅，在空中飞翔着的肉……"
    "就如同料理漫画中一样的帅气的动作，不过做出来的却只是非常普通的生姜烧肉。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA07"),"True","img/KA_LAA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA014"
    神奈 "「的确不是适合早上吃的食物……」"
    "虽然有些微妙地不合时间，但仗着年轻也就无所谓了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA015"
    神奈 "「因为是难得的机会，于是制作了结乃亲手传授的料理，总觉得那个会比较合你胃口。」"
    志雄 "「结乃也是……用的那种作料理的方法？」"
    voice "NYU13A_KA016"
    神奈 "「嗯。比我更加夸张呢。我离结乃的领域还很早呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA04"),"True","img/KA_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA017"
    神奈 "「我和结乃一样……如果不是干劲满满地去做的话，料理就做不好吃的那种类型呢。」"
    志雄 "「这个，好像是又好像不是……」"
    "只是一个生姜烧肉，到底需要使用多么华丽的动作啊。"
    "料理的世界果然是超出我想象的深奥啊。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA05"),"True","img/KA_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA018"
    神奈 "「对了……结乃还没有为你做过吗。对不起，结乃。」"
    志雄 "「不，在这里道歉也……」"
    "看着向空中双手合十的神奈，我不由得露出苦笑。"
    "如果那个方向真的有结乃在的话，一切都将变成多么简单啊……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA08"),"True","img/KA_LAA08A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA019"
    神奈 "「怎么说呢。对于少女来说，自己拿手的料理首先被其他女生曝光这件事，足以让她震惊到扑到哦？」"
    志雄 "「这，这样吗？」"
    "那样的话岂不是不应该在这里公开出来，而是隐藏一下比较好嘛？"
    "做料理的同时还要喊着必杀技……应该不是一种很想给人看的情景吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA020"
    神奈 "「好。这下肚子也填饱了……」"
    "完成了对自己主张阐述的神奈，将手机放到了耳边，走了出去。"
    voice "NYU13A_KA021"
    神奈 "「今天也继续努力的寻找结乃吧。」"
    志雄 "「说起来，神奈打算在这里呆到什么时候呢？」"
    "根据神奈携带的金钱来看，应该并不打算久留的。"
    "广播比赛的截止日也快到了，再加上神奈呆在这里的时间也已经不多了。"
    voice "NYU13A_KA022"
    神奈 "「如果错过明天中午的电车的话，就会比较麻烦了。」"
    志雄 "「不管怎么说，今天不找到结乃的话，应该就算超时了吧。」"
    "比赛，还有好友的相聚，都已经没有时间再等下去了。"
    voice "NYU13A_KA023"
    神奈 "「就是这样。所以，加油吧？见不到结乃我也不想回去的呀。」"
    志雄 "「嗯。比赛也不能不参加啊」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA03"),"True","img/KA_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA024"
    神奈 "「是啊。要向结乃做爱的告白的嘛。」"
    志雄 "「呃……」"
    "忘记了。"
    "我曾经对神奈说过，我参加这次比赛的真的目的。"
    "说是爱的告白……其实更想把对结乃的思念，以这样一种形式传达给她。"
    "我是这么想的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA02"),"True","img/KA_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA025"
    神奈 "「如果找到了，和结乃的好感度就上升了。然后参加比赛，获得一个好成绩，然后好感度更加上升。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA05"),"True","img/KA_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA026"
    神奈 "「但是，如果找不到的话，当初进入的线路就会被重置，然后引爆悲剧炸弹的哦，肯定的。」"
    志雄 "「哪里的恋爱游戏啊……」"
    "虽然比喻很奇怪，但感觉最终结果会和这个相差无几吧。"
    "因为时间的紧迫，寻找结乃的我们，自然而然地加快了脚步。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    with dissolve
#BG_SET_DEFC 0,BG06EA
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/BG05AA@2x.jpg" as bg1 with dissolve
    play sound "SE01_12L"
    play sound "SE05_14L"
#FADE_IN 1
    pause (64/32.0)
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1
    pause (64/32.0)
    play sound "SE05_13L"
#FADE_IN 1
    "直到走到了双腿都失去感觉成了木棒一般，却还是没能找到结乃。"
    "在最后的希望——澄空学园门前，我泄气地垂下了肩。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA05"),"True","img/KA_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「果然……比赛已经不可能了吧。」"
    "就算从现在开始写剧本，录音并制作光盘，就时间上来说也已经来不及了。"
    "虽然很可惜，但是，事实是，我和结乃之间制作一个小小回忆的机会，已经不复存在了。"
    voice "NYU13A_KA027"
    神奈 "「呜呜，果然没人接呢。」"
    "面前仍然举着手机的神奈也是面露难色。"
    "整整两天……我们一次都没能打通结乃的手机。"
    志雄 "「广播制作虽然已经没有希望了，但至少得让神奈和结乃见一次面吧。」"
    "她也陪我找了那么久了。"
    "如果这点都不为神奈做的话，我心里也会过意不去的。"
    志雄 "「还有些时间。去她家一次如何？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA04"),"True","img/KA_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    神奈 "「……」"
#MESEX_A M_NOA,A_CH_KA,NYU13A_KA028,"【神奈】「……」%K%P"
    "神奈好像并没有听见我在说什么，她保持着手握手机的姿势，望向了澄空学园的校舍。"
    志雄 "「神奈？」"
    voice "NYU13A_KA029"
    神奈 "「那个。志雄能够进到这个学校的广播室吗？」"
    志雄 "「啊？嗯。曾经帮着结乃拿过钥匙，估计应该可以进去……」"
    "怎么说我都是学生会长啊。"
    "这方面还是挺受信任的。"
    voice "NYU13A_KA030"
    神奈 "「为了向结乃传递心声，只要作为优秀作品被选拔，进入公开放送阶段就可以了吧？」"
    志雄 "「啊。这是最底线……」"
    "最优秀的８部作品可以获得在海岸特设的录音棚里现场播出的待遇。"
    "优胜作品将在那时通过投票来决出。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA03"),"True","img/KA_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA031"
    神奈 "「那么，这样吧……该做的事情只有一件不是吗？」"
    "神奈的脸上，露出了像爱捣蛋的小鬼一般的笑容。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG90EA@2x.jpg" as bg0 zorder 0 with dissolve
    
    scene expression Solid("000") with None
    "这个鬼主意……"
    "让我们的命运已经被彻底地改变了，\n而此时，我们完全没有意识到这一点。"
#FADE_IN 0
#SCRMODE_SPC SCR_FULL
#MES "%S001%FS%n%n%n%n%FE%S060%FS%LC这个鬼主意……%LE%FE%K%n"
#MESX "%S060%FS%LC让我们的命运已经被彻底地改变了，%n而此时，我们完全没有意识到这一点。%LE%FE%K%O032"
    window hide
#SCRMODE_SPC SCR_WINDOW
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    scene expression "img/BG90EA@2x.jpg" as bg0 with dissolve
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA02"),"True","img/KA_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "OBGM02"
#FADE_IN 1
    voice "NYU13A_KA032"
    神奈 "「嗯。都是我能用的器材。没问题。」"
    "在广播室里看了一圈后，神奈满足地点了点头。"
    志雄 "「那么就是说，节目制作是可能的喽。」"
    "神奈的提案——由自己来代替结乃来参加广播的制作。"
    "为了确认这个方案是否可行，来到广播室考察后的神奈，给了我肯定的答复。"
    志雄 "「但是，明明之前那么严正地拒绝过……现在这样没问题吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA033"
    神奈 "「我不想参加的是，志雄和结乃制作的广播节目哦。」"
    "我和结乃为了创造我们两人的回忆，决定进行广播制作，并且参加这个比赛。"
    "给我带来参加机会的神奈，结果因为了撮合我们两人，退出了比赛。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA04"),"True","img/KA_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA034"
    神奈 "「虽然我不喜欢做假设。」"
    voice "NYU13A_KA035"
    神奈 "「如果最初就说好３个人一起做，又或者结乃或志雄中的谁提出过一起做之类意见的话……」"
    "神奈说到这里停了下来，不过之后的话不用听也已经知道了。"
    "至少现在的我能够明白她的意思。"
    "虽说只是作为『投稿者』，但是从最早开始，神奈其实就很想参加这次广播制作吧。"
    志雄 "「那么，就不要做什么假设了。」"
    "既然不喜欢假设，那么，我们就说些实在的。"
    志雄 "「拜托。请和我一起制作广播节目！」"
    "我向神奈深深地低下了头。"
    志雄 "「一方面是为了向结乃传达思念……但并不仅仅是因为这个。」"
    志雄 "「我也非常想跟神奈两人一起尝试着制作广播节目！」"
    "我很直白地把自己的想法告诉了神奈。"
    "正如结乃所说，或许我所追求的广播节目的确无法在比赛中出成绩。"
    "但即使如此，我还是想要做自己心目中的广播节目。"
    "然后，为了那个目标，对我来说，现在所需要的……正是我面前的神奈。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA036"
    神奈 "「嗯。我也想跟志雄一起做广播节目哦。」"
    "短暂的沉默后，对着抬起头的我，神奈还以开心的微笑。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA02"),"True","img/KA_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA037"
    神奈 "「在电话中谈论广播比赛的时候，其实我的心情一直像蹦蹦跳跳的小鹿一样！」"
    志雄 "「神奈……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA038"
    神奈 "「说实话，去年我独力获得了优胜，本以为没有留下什么遗憾，但……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA03"),"True","img/KA_LAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA039"
    神奈 "「还是不行啊。心里的火焰一旦被点燃，轻易看来是无法扑灭的了。」"
    "最终发展成这样，是因为每天晚上我们都在讨论关于广播制作的事情吧。"
    志雄 "「好。那么，让我们做一个，足以让结乃后悔的……最优秀的节目吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA02"),"True","img/KA_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA040"
    神奈 "「嗯，请多多关照。」"
    "我们的手紧紧地握在了一起。"
    "从对方手中传来的热量，传达了我们对于制作一个最优秀的节目的自信。"
    志雄 "「那么……总之先开始讨论内容吧。」"
    "在有限的时间里，究竟能够做到何种水平呢……对于我们来说，现在最大的敌人就是时间了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA041"
    神奈 "「应该不用了吧。难道目前为止我和志雄关于广播节目的讨论还不够多吗？」"
    志雄 "「是啊……」"
    "从神奈充满自信的笑容中，我也获得了勇气。"
    "互相提出的无聊的创意，收集的素材……现在全部还都在我的脑中。"
    "那些内容的量，制作多少个广播节目都足够啊。"
    voice "NYU13A_KA042"
    神奈 "「没有时间去收集投稿还是有点可惜呢。」"
    志雄 "「关于那个嘛……还是我们自己来投稿？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA07"),"True","img/KA_LAA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA043"
    神奈 "「啊——啊。结果还是变成了自导自演啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA09"),"True","img/KA_LAA09A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "神奈以看上去有点奇怪的动作在本子上沙沙地写着。"
    "不愧是『Ｔ－ｗａｖｅ』传说中的投稿者。"
    "以超乎寻常的手法将各种素材渐渐联系了起来。"
    志雄 "「好——！　我也不会认输哦！」"
    "眼前就是我一直所憧憬着的『凯尔玛妹妹』。"
    "这刺激了我同样作为投稿者的竞争心，于是脑中不停的浮现出以往没有过的高质量的投稿素材。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    show expression "img/BG90NA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG90NA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA04"),"True","img/KA_LAA04A@2x.png") as lh10 zorder (10-10):
        ypos 0.0
    with dissolve
    play music  "BGM13"
#FADE_IN 1
    志雄 "「完成了……吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA044"
    神奈 "「嗯。虽然是突击作业……但是我觉得这已经是最好的节目了。」"
    "经神奈之手完成的节目光碟递到了我的手中。"
    "再次听了一遍后，的确那是包含了所有我想做的东西的令人满意的作品，我可以这么断言。"
    "非要说有什么不满的话，就是因为时间上的原因，我们只能使用亨准备的那个『还算正常』的主题曲了。"
    志雄 "「这么难得的机会，真想整部作品都由我们两个来做呢……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA07"),"True","img/KA_LAA07A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA045"
    神奈 "「志雄……你说的话跟结乃一样了哦？」"
    志雄 "「啊……」"
    "现在，我总算有点理解结乃的想法了。"
    "因为是重要的东西……所以只想和心意相通的人完成。"
    "终于意识到了……结乃的想法原来是这么的纯粹。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA046"
    神奈 "「那么，如果这样就能了解结乃的想法的话，我也没什么要说的了。」"
    志雄 "「啊哈哈哈哈……」"
    "我用了暧昧的笑声想混过去。"
    voice "NYU13A_KA047"
    神奈 "「已经很晚了……快点回去吧。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "早已过了放学时间，我们以极快的速度进行了广播室的整理。"
    stop music fadeout 132
    "望着一件一件整理物品的神奈的侧脸，我的心中涌起了复杂的感情。"
    志雄 "（与结乃所感觉到的相同的想法吗？）"
    "结乃一直执著于要两人单独制作的理由……"
    "我想要和神奈两人单独制作节目的理由……"
    "以及，神奈所说的话……"
    window hide
    神奈 "「那么，如果这样就能了解结乃的想法的话，\n我也没什么要说的了。」"
#SCRMODE_SPC SCR_FULL
#MESA A_CH_KA,NYU13A_KA048_K,"【神奈】%S001%FS%n%n%n%n%n%FE%S060%FS%LC「那么，如果这样就能了解结乃的想法的话，%n我也没什么要说的了。」%LE%FE%K%O032"
    window hide
#SCRMODE_SPC SCR_WINDOW
    "结乃对我的感情，现在不用说也很清楚。"
    "那么，我对神奈的感情，到底是怎么样的呢。"
    "同伴？　还是……"
    voice "NYU13A_KA049"
    神奈 "「喂——！　别在那里偷懒啊——！」"
    志雄 "「对，对不起！」"
    "因为神奈的叫声，我猛地回过了神来。"
    "思考被强行中断，到底是好事，还是坏事呢……"
    "现在的我大概是无法想明白的吧。"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/BG15NA1@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    play music  "BGM10"
#FADE_IN 1
    "回到家以后，我们开了一个小小的庆功会。"
    志雄 "「那么接下来，请举杯。」"
    "桌上，摆放着从便利店里买来的饮料和点心……"
    "狠心之下还买了ＰＩＺＺＡ。"
    "然后，不知为啥神奈做的生姜烧肉也放在一起。"
    window hide
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA02"),"True","img/KA_XAA02A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NYU13A_KA050"
    神奈 "「繁琐的祝词就免了吧。我们干—杯！」"
    "并没有等待我的回应，神奈就把自己的杯子跟我的杯子碰了一下。"
    志雄 "「干——杯。」"
    "但是，现在我对这些事情毫不在意。"
    "本来已经死心了的广播节目，最终以我所期望的形式完成了。"
    "想到这一切都是拜神奈所赐，她稍微不讲礼仪的行为看起来也就觉得可爱了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA03"),"True","img/KA_XAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA051"
    神奈 "「呼哈——！好像就是为了喝这一杯而活着一样～」"
    "一口气喝干一杯的神奈说出了大叔般的台词。"
    "虽说她表现出一副喝醉了的样子，但我可是善良的高中生。"
    "桌上摆着的，都是如假包换的无酒精饮料。"
    志雄 "「嗯。做完一件工作后的干杯最棒了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA01"),"True","img/KA_XAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA052"
    神奈 "「现在也能理解父亲他们喝啤酒喝得那么愉快是为什么了～」"
    "再重复一遍，神奈现在在喝的是，姜汁清凉饮料。"
    "完全没有酒精成分。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA02"),"True","img/KA_XAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA053"
    神奈 "「明天就不得不回去了。今天我们我们闹个通宵吧——！」"
    志雄 "「遵命！大姐头！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA03"),"True","img/KA_XAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU13A_KA054"
    神奈 "「嗯嗯，态度很好啊。」"
    "我向已经喝干的杯子中倒入新的饮料。"
    "属于我们的长夜，才刚刚开始。"
    window hide
#FADE_OUT 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    pause (32/32.0)
#FADE_IN 1
    "长夜才刚刚……应该是刚刚才开始的。"
    voice "NYU13A_KA055"
    神奈 "「呜咕……已经喝不了了～」"
    "和昨天一样，神奈很快就被击沉了，一头趴在了桌子上。"
    "……把饮料和食物大部分都整理掉之后。"
    志雄 "「全都是无酒精的，却……」"
    "带着醉酒的精神状态，以及醉酒之后的表现，神奈呼呼地入睡了。"
    志雄 "「接下来。」"
    "我和昨天一样，给神奈盖上毛毯。"
    "昨天也好，今天也好，真是艰苦波折的一天呢。"
    "或许是因为身处不熟悉的地方吧，总之，神奈肯定是非常累了吧。"
    志雄 "「今天，我还是去别处睡好了……」"
    "因为今天起床很早，就事先把空房间整理了一下。"
    "床是房间自带的……睡一晚应该没什么问题吧。"
    志雄 "「真是没办法呢。」"
    voice "NYU13A_KA056"
    神奈 "「是、是没有办法啊。」"
    "可能是因为睡得比较浅，神奈对我的口癖产生了反映。"
    "不过，她并没有醒过来，接着就继续发出了呼呼的睡声。"
    志雄 "「关于结乃的事情，我一定会想办法搞定的……」"
    "神奈为了我们，已经做了所有她能做的了。"
    "接下来，就该轮到我的应对了……只剩下这个了。"
    voice "NYU13A_KA057"
    神奈 "「是啊。不想点办法的话……」"
    志雄 "「还在说梦话啊……」"
    "既然知道她是在说梦话，那也就没什么好惊奇的了。"
    "看来她在梦中都为我们担心，不过，总觉得神奈就应该是这样的。"
    voice "NYU13A_KA058"
    神奈 "「如果不做些什么的话……不这样的话，我……已经……」"
    stop music fadeout 1
    志雄 "「嗯？」"
    "不经意间，我听到了意外的话语，可当我靠近神奈再想仔细听听时，她除了呼呼的睡声之外，再也没有吐出一个字。"
    志雄 "「神奈……」"
    "即使之后还有其他的话语，那也不是我应该听到的内容吧。"
    "如果听到了的话……或许会让我做出背叛自己至今为止的回忆的行为吧。"
    window hide
    show expression "img/BG15NA2@2x.jpg" as bg0 with dissolve
    scene expression "img/BG15NA2@2x.jpg" as bg0 with dissolve
    志雄 "「晚安。明天见。」"
    "就如同想要切断自己的思考和那即将萌芽的感情一般……"
    "我静静地关上了房门，走向了空着的房间。"
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