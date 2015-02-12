label NYU10A:
    $currentlabel = "NYU10A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
    $month = '08'
    $day = '06'
    $date = '0'
#CAL_DSP_GRP 3,CAL_0806
    scene expression Solid("000") with fade
    show expression "img/NIMG15O-568h@2x.jpg" as cal zorder 5
    show expression "img/08_06_SUNDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
#FADE_OUT 0
    scene expression Solid("000") with fade
    
#BG_SET_DEFC 0,BG97AA
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/BG35AA@2x.jpg" as bg1 zorder 1 with dissolve
    play music  "BGM10"
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
    "不知不觉暑假也过了一半了，我久违地来到了酪萨克。"
    window hide
    play sound "SE00_32"
    pause (16/32.0)
    show expression "img/BG97AA@2x.jpg" as bg1 zorder 1 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA02"),"True","img/MH_LCA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_MA000"
    麻寻 "「欢迎光临～」"
    志雄 "「你好。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA01"),"True","img/MH_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_MA001"
    麻寻 "「诶？志雄君，今天一个人吗？」"
    志雄 "「不，我在这里等她，结乃约我来的。」"
    voice "NYU10A_MA002"
    麻寻 "「嗯，约会吗？」"
    志雄 "「应该吧。」"
    window hide
    show expression "img/BG36AA@2x.jpg" as bg_over zorder 2 with dissolve
    "在麻寻的引领下，我选择了靠窗边的座位，拉开椅子坐下。"
    "今天是录音完成之后第一次和麻寻见面。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LCA01"),"True","img/MH_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_MA003"
    麻寻 "「点单的话等结乃来了之后可以吗？」"
    志雄 "「好的，就麻烦你了。」"
    voice "NYU10A_MA004"
    麻寻 "「太好了。其实今天有对新招进来的人的面试……」"
    voice "NYU10A_MA005"
    麻寻 "「要去他们那边稍微忙一下呢。结乃来了的话叫我一下吧。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "说完麻寻返回了柜台那边。"
    "麻寻貌似也完全回到了日常生活之中了呢。"
    "而我，也从慌张忙碌的节目制作中解放出来，悠闲自在地过着往返于学校补习的每一天。"
    "从去水族馆那次之后，都没有和结乃好好地约会过了。"
    "今天就把学习的事情抛之脑后，好好地轻松一下吧。"
    志雄 "「打工面试的考官吗……麻寻真的能胜任吗？」"
    "我不认为那是非常合适她的角色。"
    stop music fadeout 132
    "我十分想看一看新人那一副极力讨好麻寻可爱的表情，所以我装作去洗手间的样子，去窥视面试者等待的地方。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「……？为什么你会在这里？」"
    "看到的所谓面试者队列中的最后一位，竟然是一幅不开心的样子排队等候着的亨。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA02"),"True","img/TO_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM09"
    voice "NYU10A_TO000"
    亨 "「必须要挣够摩托的修理费，所以才来面试打工的哦。」"
    志雄 "「真的对不起，十分抱歉，请你原谅。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB03"),"True","img/TO_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO001"
    亨 "「行了行了～再这么婆婆妈妈道歉的话我也会过意不去了。」"
    "亨他……为了挣回被我和结乃跌倒弄伤的爱车的修理费，所以决定要开始在酪萨克打工吗？"
    "在那之后，我和结乃说了要赔偿他。可是亨严词拒绝了『这种小事我自己想办法解决』。"
    "当时还想不出他要用什么办法，不过来酪萨克打工倒是有些出乎意料……"
    志雄 "「可是，你真的一点补习的时间都不打算留了吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB05"),"True","img/TO_LBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO002"
    亨 "「哼……我的夏天，已经结束了。」"
    "望向远方的亨，深深地叹了口气。"
    voice "NYU10A_TO003"
    亨 "「按时薪和劳动时间计算的打工方式，已经确定我的暑假除了去学校和打工之外已经没有任何富裕了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA04"),"True","img/TO_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO004"
    亨 "「我才不会认输呢。」"
    "虽然他是在逞强，不过，亨他挺起胸膛的样子还有几分帅气。"
    "无论如何也要靠自己的努力来实现，我不得不拜服于亨的这种男子气概。不过，这件事我必须要帮忙……"
    "不帮忙的话我也太不男人了。嗯。"
    window hide
    play sound "SE00_32"
    pause (32/32.0)
    voice "NYU10A_YU000"
    结乃 "「啊，来了来了，志雄学长。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCB01"),"True","img/YU_MCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「哦，结乃。」"
    voice "NYU10A_YU001"
    结乃 "「久等了吧？」"
    志雄 "「没有，这次真的是刚刚才到的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCA01"),"True","img/YU_MCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU002"
    结乃 "「是吗……咦？」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCA01"),"True","img/YU_MCA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
    with dissolve
    voice "NYU10A_TO005"
    亨 "「哟！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCB06"),"True","img/YU_MCB06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU003"
    结乃 "「佐、佐贺学长！？」"
    "发现了亨的结乃眼睛瞪得圆圆的。"
    志雄 "「为了挣『猫大人』的修理费呢。」"
    "明白到事态情况的结乃带着歉疚俯下了身子。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCC05"),"True","img/YU_MCC05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU004"
    结乃 "「那、那个……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA02"),"True","img/TO_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO006"
    亨 "「什么都不要说。我是为我自己才那样做的。」"
    志雄 "「就算你这样坚持，我们也实在是过意不去啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO007"
    亨 "「就那么介意吗？」"
    "亨用不能理解我们的目光在我和结乃身上来回扫视……真的是完全没有记恨我们呢。"
    "这家伙骨子里有这么爷们儿的一面。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 0,(320-192)
#CHR_POSC 1,(320+192)
#CHR_POSC 2
#CHR_DSPTC 0,1,2,TO_MBB04,YU_MCC05,MH_MBA01
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCC05"),"True","img/YU_MCC05A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .8
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA01"),"True","img/MH_MBA01A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
    with dissolve
    voice "NYU10A_MA006"
    麻寻 "「啊，看到你们俩还真是让人感觉安心呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCA01"),"True","img/YU_MCA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU005"
    结乃 "「麻寻，你好。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA02"),"True","img/MH_MBA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU10A_MA007"
    麻寻 "「结乃，接下来要约会吧？真叫人羡慕呀~！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCB06"),"True","img/YU_MCB06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU006"
    结乃 "「诶？约会？」"
    "麻寻走过来企图戏弄我们，可是结乃却不断茫然地来回看着我们。"
    志雄 "「呃，喂，不是约会吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCB01"),"True","img/YU_MCB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU007"
    结乃 "「不是哦。是这个啦，这个。」"
    "弄错了吗……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh0 zorder (10+0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA01"),"True","img/MH_MBA01A@2x.png") as lh2 zorder (10+2)
    with dissolve
    "结乃没有用言语来安慰受到打击的我，取而代之的是向我递来一片东西。"
    "左下角有着『浜咲ＦＭ』字样的白色信封。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA02"),"True","img/TO_MBA02A@2x.png") as lh0 zorder (10+0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA04"),"True","img/MH_MBA04A@2x.png") as lh2 zorder (10+2)
    with dissolve
    志雄 "「啊，这是！」"
    voice "NYU10A_MA008"
    麻寻 "「难道说，比赛的结果出来了吗？」"
    亨 "「…………」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCA05"),"True","img/YU_MCA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    stop music fadeout 132
    pause (32/32.0)
    play sound "SE07_02"
    voice "NYU10A_YU008"
    结乃 "「读读看吧～」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MCC02"),"True","img/MH_MCC02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    pause (32/32.0)
    play sound "SE07_02"
    voice "NYU10A_YU009"
    结乃 "「感谢您此次投稿应征参加浜咲广播大赛。评经过我们的评审……」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCB02"),"True","img/YU_MCB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    pause (32/32.0)
    play sound "SE07_02"
    voice "NYU10A_YU010"
    结乃 "「『浜咲讯息』被选为优秀作品，特此通知。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh0 zorder (10+0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA02"),"True","img/MH_MBA02A@2x.png") as lh2 zorder (10+2)
    voice "NYU10A_MA009"
    麻寻 "「啊~！」"
    志雄 "「太好了！」"
    window hide
    play music  "BGM10"
    "麻寻跳了起来，尖叫着欢呼着。"
    "我也情不自禁地喊出声来。"
    "结乃也很开心的微笑着继续说道。"
    voice "NYU10A_YU011"
    结乃 "「获奖的人后天，被邀请参加浜咲海岸特设广播室直接活动。」"
    voice "NYU10A_MA010"
    麻寻 "「呀~！太好了呢，结乃。」"
    voice "NYU10A_YU012"
    结乃 "「嗯。托麻寻的福呢。」"
    "两个女生拉着手蹦了起来。"
    "我和远处听着这个消息的亨也相视一笑。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA01"),"True","img/MH_MBA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU10A_MA011"
    麻寻 "「通过这个活动决出最后的优胜者吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCA01"),"True","img/YU_MCA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU013"
    结乃 "「是的。优胜奖金有１０万日元呢！……啊！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCC03"),"True","img/YU_MCC03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    "大概是考虑到了会打扰到别人，结乃放开了一直牵着麻寻的手，停下来转身走到亨面前。"
    voice "NYU10A_YU014"
    结乃 "「佐贺学长……如果获胜的话就可以用奖金来付修理费了。」"
    "看起来结乃也是十分地在意那件事呢。"
    "其实可以理解，毕竟是两个在摩托车驾驶方面有共同语言的人…"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "不过亨用对我一样的态度，坚决的拒绝了这一提议。"
    voice "NYU10A_TO009"
    亨 "「不，不用，我已经开始打工了，不用放在心上哦。」"
    "今天的亨真的是非常帅气呢。"
    voice "NYU10A_TO010"
    亨 "「况且，还不能确定一定可以获得优胜啊～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCC04"),"True","img/YU_MCC04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU015"
    结乃 "「啊……也，也对呢。」"
    志雄 "「没关系的，结乃。」"
    "我俯下身子拍了拍结乃的肩膀。"
    志雄 "「全力去做的话，一定可以获得成果的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA02"),"True","img/MH_MBA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU10A_MA012"
    麻寻 "「对对。还没开始就考虑会输的话，本来可以获得的胜利也会悄悄溜走的哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCB01"),"True","img/YU_MCB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU016"
    结乃 "「……是，是！对不起。」"
    stop music fadeout 132
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA04"),"True","img/TO_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO011"
    亨 "「不啊，我认为获胜是很难的呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCC04"),"True","img/YU_MCC04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU017"
    结乃 "「诶……？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MCC05"),"True","img/MH_MCC05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU10A_MA013"
    麻寻 "「真是的，不要说那些不吉利的话。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA02"),"True","img/TO_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO012"
    亨 "「你们都忘了。那个节目有着致命的缺点呢……」"
    志雄 "「缺点……？」"
    voice "NYU10A_TO013"
    亨 "「可以说是那个节目唯一的缺点……」"
    "是吗？有吗？一开始不就是因为各方面都比较优秀才被选为优秀作品的吗？"
    "不过，亨那坚定的语气实在让我不能释怀。"
    "究竟，缺点是……？"
    voice "NYU10A_TO014"
    亨 "「就是我的告白不能在节目中使用啊——！」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCB06"),"True","img/YU_MCB06A@2x.png") as lh1 zorder (10+1)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA04"),"True","img/MH_MBA04A@2x.png") as lh2 zorder (10+2)
    with dissolve
    play music  "BGM09"
    志雄 "「啊……」"
    voice "NYU10A_YU018"
    结乃 "「啊，说起来的话！」"
    voice "NYU10A_MA014"
    麻寻 "「完全把这件事给忘干净了呢。」"
    "我也忘记了，不过现在才说出来，大概亨也是彻底忘了吧。"
    "明明是自己的事……"
    voice "NYU10A_TO015"
    亨 "「我也是脑子里一直只想着『猫大人』的事情来着。」"
    voice "NYU10A_TO016"
    亨 "「不过，看见那封信的时候我终于想起来了！」"
    "就想面对真凶指出证据的侦探一般，亨伸手指向那白色信封。"
    "然后，亨从威风凛凛的侦探神情一转，露出一副怨灵一般的表情接近了我。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA02"),"True","img/TO_LBA02A@2x.png") as lh0 zorder (10+5):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO017"
    亨 "「志～雄～，为什么不能用我的信件呢啊～」"
    志雄 "「啊～因为，有主题之类的很多需要考虑到的事情……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBB04"),"True","img/MH_MBB04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU10A_MA015"
    麻寻 "「不过，用不了的话不是也很好吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCB04"),"True","img/YU_MCB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU019"
    结乃 "「确、确实呢！说的就是呢啊！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA03"),"True","img/TO_LBA03A@2x.png") as lh0 zorder (10+5):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO018"
    亨 "「说的太过分了啊！」"
    "连结乃都那样说了……所以说亨究竟做了什么啊？"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    pause (16/32.0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBB03"),"True","img/MH_MBB03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU10A_MA016"
    麻寻 "「亨君。为你好才这么说哦？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA04"),"True","img/TO_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO019"
    亨 "「无法接受啊！！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCA04"),"True","img/YU_MCA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU020"
    结乃 "「直播的时候，我会加油想办法用上的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO020"
    亨 "「真的？就拜托你了哦。」"
    志雄 "「结乃……说那种事情没问题吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MCA01"),"True","img/YU_MCA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU021"
    结乃 "「没关系的。正式播出要经过上局检查，不能通过放送的内容会被删掉的。」"
    "都做到不能通过上局检查这种级别的事情了吗……？"
    "都到了这个地步了，就算是我，也无法对亨说出口如『只管播报，后果我来承担』之类的话语。"
    "还是静观其变吧……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MBA05"),"True","img/MH_MBA05A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU10A_MA017"
    麻寻 "「好好，面试该亨君了哦。快点哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB03"),"True","img/TO_MBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO021"
    亨 "「呜……我那绝世的告白啊……」"
    window hide
#CHR_ERSWC 0
    "还无法接受事实的亨，被麻寻抓着衬衣领子，拖进了店里的后台。"
    "送走了那两人之后，结乃坐到了我旁边的位子来。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XCA01"),"True","img/YU_XCA01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NYU10A_YU022"
    结乃 "「志雄学长，到浜咲ＦＭ正式播出之前还有补习吧，时间上不要紧吗？」"
    志雄 "「嗯，如果和补习班冲突的话，我会做调整的。」"
    voice "NYU10A_YU023"
    结乃 "「嗯，真是谢谢，那就好。」"
    "结乃坐在椅子上，低头道谢着。"
    "在我把手伸向结乃那因动作而摇摆着的头发之前，结乃抬起了头。"
    志雄 "（啊，遗憾……）"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XCB02"),"True","img/YU_XCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU024"
    结乃 "「再加把劲儿吧！」"
    志雄 "「嗯。」"
    "虽然没能碰触到头发，不过我看见了这个夏天里最美的笑容。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    pause (32/32.0)
#FADE_IN 0
    "然后，转眼间，到了正式演出当天……"
#label QJUMP
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
    pause (32/32.0)
#FADE_IN 0
    $month = '08'
    $day = '13'
    $date = '0'
#CAL_DSP_SUB NIMG15H,CAL_0813
    scene expression Solid("000") with fade
    show expression "img/NIMG15H-568h@2x.jpg" as cal zorder 5
    show expression "img/08_13_SUNDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#BG_SET_DEFC 0,BG21AA
    scene expression "img/BG21AA@2x.jpg" as bg0
    pause (32/32.0)
    play sound "SE05_19L"
#EFF_PRI 0
#EFF_STAC 0,WATERTWINKLE,EFF_NOSKIP
#FADE_IN 1
    voice "NYU10A_TO022"
    亨 "「志～雄～♪」"
    "晴朗的青空，白色的沙滩，广阔的大海在遥远的地平线与白云交际……风景如画的盛夏浜咲海岸，我们来了！"
    voice "NYU10A_TO023"
    亨 "「志～雄～♪」"
    志雄 "「请不要再发出那种恶心的声音！」"
    window hide
    play music  "OBGM18"
#SE_VOLC 1,64
    "亨估计多半是被眼前的景色熏陶了，整个人都变得风骚起来了。"
    "如慢镜头一般走到波浪之间，撩起水来泼向我……"
    "饶了我吧……"
    "我可没他那么轻松。因为是直播实录，所以录制的时候可不能重来。"
    "而且，我参加这个比赛最大的目的，是想通过电波将我对结乃的感谢传递出去，时机就在正式播出的时候。"
    "实在是……好紧张。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MDB01"),"True","img/YU_MDB01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    pause (16/32.0)
#BG_SET_BACK 
#BG_INIC 1
#BG_INIC 3
#BG_ALPC 1
#BG_ALPC 3
#BG_UVC 1,0,(448),640,448
    show expression "img/NIMG18E@2x.jpg" as bg1 zorder 100 with dissolve:
        yalign 1.0
        linear 2 yalign 0.0
#EFF_STPC 0

    pause (64/32.0)
#EFF_PRI 0
#EFF_STAC 0,LATHER,EFF_NOSKIP

#BG_POS_SAVEC 1
#BG_POS_SAVEC 3
#BG_ALP_SAVEC 1
#BG_ALP_SAVEC 3
    hide bg3 with dissolve
    play sound "SE07_23"
#EFF_STPC 0,EFF_NOSKIP
#EFF_PRI 0
    voice "NYU10A_YU025"
    结乃 "「你好，佐贺学长。」"
    voice "NYU10A_TO024"
    亨 "「呀，结乃。今天也很可爱哦。」"
    voice "NYU10A_TO025"
    亨 "「泳装实在是美妙绝伦！」"
    window hide
#CHR_GET_POSC 1,F24,F25
#RSUB F24
#BG_LAY 3,YU_MXB05,3,F24
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MDB05"),"True","img/YU_MDB05A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .75
    hide bg1
    with dissolve
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#EFF_PRI 0
#EFF_STAC 0,WATERTWINKLE,EFF_NOSKIP
#REEK_CHR 1
    voice "NYU10A_YU026"
    结乃 "「谢、谢谢啦。」"
#REMOVE_REEK_CHR 1
#THREAD_STP 1
    hide bg3 with dissolve
#BG_PRI 3
    voice "NYU10A_TO026"
    亨 "「如果可以话，露出度再高一些我觉得会更好的……」"
    "不行啊，这家伙现在完全由另一个脑袋支配着，再不制止他指不定又做出什么混蛋举动。"
    志雄 "「亨，其他人都怎样了？」"
    voice "NYU10A_TO027"
    亨 "「麻寻把酪萨克的工作处理完之后过来，莉莉丝和智纱也会赶在在你们出场之前过来的。」"
    "顺便一提，我和结乃因为是比赛选手的缘故，早上就来集合了。"
    "相关事项的商谈已经结束，到出场之前还有很长一段时间的空闲无事可做……"
    "……明明想和结乃两个人单独在海边相处。亨可真是不解风情啊。"
    志雄 "「大家都没来呢的话，为什么你一个人来了啊？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO028"
    亨 "「是为了『猫大人』修理回归的复活纪念特意大爆走而来的！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MDB01"),"True","img/YU_MDB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU027"
    结乃 "「啊，修好了吗？『猫大人』……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB03"),"True","img/TO_MBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO029"
    亨 "「嗯，不过多亏了父母的支持才能搞定啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MDC04"),"True","img/YU_MDC04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    "亨目光深邃地望着远方说道。"
    "最近亨常常露出这样的目光，果然是神经受到了不明刺激吗？"
    志雄 "「能不能正常一点……亨」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB05"),"True","img/TO_MBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO030"
    亨 "「所以才说不要放在心上了啊……」"
    "……如果不想别人在意的话就不要摆出一副那样的脸啦。"
    "想了想，还是决定不说什么了。"
    志雄 "「亨，谢谢你。能够这样去挑战优胜真是多亏了你呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO031"
    亨 "「哇，真肉麻啊……而且，是靠咱们４个人一起努力的结果，才不是靠我１个人呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO032"
    亨 "「是吧，结乃？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MDA01"),"True","img/YU_MDA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU028"
    结乃 "「嗯。当然了。而且，也要感谢所有投稿的朋友呢。」"
    志雄 "「是啊。」"
    "直接参与制作的我们四个，以及所有投稿的朋友们，是我们所有人的努力才抓住了这直播的机会。"
    "不心怀感激的话就无法战胜挑战呢。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB05"),"True","img/TO_MBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO033"
    亨 "「啊——啊，可惜除了主持人以外的人不能参加啊。不过他们放送的水准也会比较专业就是啦。」"
    "大会规定，器材操作等事项将由ＦＭ局的职员负责。"
    "被选为优秀作品的队伍差不多都关心会不会被器材影响，不过在专业人士面前也不可能去多嘴的。"
    "大部分队伍都因为能参加学习到专业的技术而妥协了，不过所谓的每个队伍的技术组也大多是爱好者，并不是专业人员。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO034"
    亨 "「那，志雄你们是第几个出场啊？」"
    志雄 "「啊，抽签抽到最后一个呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_TO035"
    亨 "「好的！这样的话就决定了！先去玩吧！」"
    志雄 "「啊？」"
    "不过亨却完全没有参观学习的心思，完全是想趁着今天这个机会尽情享受夏天的感觉而已。"
    voice "NYU10A_TO036"
    亨 "「只有学习与打工的夏天最讨厌了！朝向大海冲刺~！呀~哈～！」"
    window hide
    play sound "SE01_23L"
    pause (16/32.0)
    hide lh0 with dissolve
    stop se
    "亨一口气脱下外衣冲向了大海。"
    "里面直接穿着泳衣倒是考虑挺周到的。不过，这衣服谁来收拾啊……"
    "无视了我所考虑的问题，亨就那样笔直地朝海冲刺过去，在海上划起了自由泳。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LDB06"),"True","img/YU_LDB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU029"
    结乃 "「真快啊，佐贺学长。」"
    志雄 "「多么惊人的运动潜质啊。」"
    "我也是边捡着亨的衣服边这样佩服到。"
    "连结乃也很佩服的样子，亨也真行呢。"
    "虽说是怀着一种自暴自弃的心情吧，不过怎样才能做到那种神速还真是个疑问。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LDA01"),"True","img/YU_LDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU030"
    结乃 "「我们也过去吧。」"
    "结乃注视着我。"
    "眼神里却显露着有些不安。"
    志雄 "「可以吗？咱们是参赛选手呢。」"
    voice "NYU10A_YU031"
    结乃 "「还有时间呢的，没关系啦！」"
    志雄 "「……怎么了，这么积极的？」"
    "平常说话总是直截了当的结乃，此时好像有难讲的事情，想到这我马上也明白了。"
    "我，等待着她鼓起勇气要说的话。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LDA02"),"True","img/YU_LDA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "转眼结乃的脸颊泛起了红晕，抬头望天着说道。"
    voice "NYU10A_YU032"
    结乃 "「像刚才佐贺学长那样……不去试一试吗？」"
    志雄 "「……游泳吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LDB03"),"True","img/YU_LDB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU033"
    结乃 "「不是那个啦……那个，像慢镜头的那一幕啦。」"
    志雄 "「啊……」"
    "像慢镜头……是刚才亨在海浪里向我撩水的那一幕吧。"
    志雄 "「呵呵……要来一个吗？」"
    voice "NYU10A_YU034"
    结乃 "「不行、吗……」"
    "出乎意料的邀请，不过也是机会难得，亨的身影已经消失在海面上了。"
    志雄 "「可以哦，来吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LDB05"),"True","img/YU_LDB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "想来一直紧张着等比赛的确也没什么意思，就当放松心情，也答应了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LDA06"),"True","img/YU_LDA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU035"
    结乃 "「那，那么就，学长、来……来抓我吧！」"
    window hide
    play sound "SE01_23L"
    pause (16/32.0)
    hide lh0 with dissolve
    stop se
    志雄 "「诶？啊……等等～！」"
    "结乃猛地在海岸上跑了起来。"
    "她跑得非常快。稍微松懈的话会立刻被甩下的。"
    play sound "SE01_25L"
    "我扔掉了亨的衣服，在结乃的后面拼命地追着。"
    "这与其说是在水边嬉戏的恋人，倒不如说是难得一见的田径部集训……"
    voice "NYU10A_YU036"
    结乃 "「啊，呀。」"
    "全力疾跑的结乃，忽然踩空在了一道波浪上，跌倒了。"
    play sound "SE04_27"
    "摔得相当华丽呢。"
    志雄 "「喂，没事吧！？」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU06A")]=True
    show expression "img/EVN_YU06A@2x.jpg" as bg1 zorder 200 with dissolve
    "我急忙跑了过去。结乃则在海浪里揉着与地面亲密接触的屁股。"
    志雄 "「没事吧？」"
    voice "NYU10A_YU037"
    结乃 "「疼疼疼……对不起，结果搞砸了啊。」"
    "结乃拍了拍粘在身上的沙子，不好意思地吐了吐舌头。"
    志雄 "「明明运动细胞很灵敏的，今天怎么了吗？」"
    voice "NYU10A_YU038"
    结乃 "「忘记脚下是沙地了呢，啊哈哈。」"
    "倒在地上坐着愣神的结乃，又被一阵冲来的大浪袭击了。"
    window hide
#BG_SET_BACK 
#BG_INIC 3
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU06B")]=True
    show expression "img/EVN_YU06B@2x.jpg" as bg3 zorder 201 with dissolve
    play sound "SE05_11L"
    pause (16/32.0)
#BG_HIDEC 3
    pause (32/32.0)
    voice "NYU10A_YU039"
    结乃 "「哇，哇啊～」"
    stop se
    "被大浪翻滚没过的结乃手足无措，拼命晃动着四肢。平时轻盈的身体如今却意外的笨拙。"
    "不过，这种自然毫无掩饰的状态才是结乃最动人心弦的地方。没错的。"
    志雄 "「来，手给我。」"
    "虽然看着她呆呆的样子有些乐在其中，不过这样下去溺水就不好了，所以还是赶快拉她一把吧。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU06C")]=True
    show expression "img/EVN_YU06C@2x.jpg" as bg1 zorder 202 with dissolve
#BG_SHOWC 3
    hide bg3 with dissolve
    voice "NYU10A_YU040"
    结乃 "「啊……是。谢谢学长。」"
    "结乃握住了我伸出的手，迅速地站了起来。"
    window hide
    scene expression "img/BG22AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LDC03"),"True","img/YU_LDC03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#EFF_STPC 0,EFF_NOSKIP
#EFF_STAC 0,TWINKLE3,EFF_NOSKIP
    hide bg1 with dissolve
    志雄 "「追逐游戏还要继续吗？」"
    voice "NYU10A_YU041"
    结乃 "「不了，已经很满足了。」"
    志雄 "「也是呢。」"
    "对我来说其实还是微微有些期待那样的慢动作镜头的场景的……"
    "不过结乃奔跑之后华丽地摔倒，现在已经是心有余悸了吧。"
    "今天的结论。不是经常海滨沙滩上玩的人全力奔跑会很危险。"
    "虽然不知道为什么非要全力奔跑就是了……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LDA01"),"True","img/YU_LDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU042"
    结乃 "「不过现在看来的话，佐贺学长还真是精力旺盛呢。」"
    "结乃看着还在海浪之上不肯返回的亨的身影，钦佩地碎碎念到。"
    志雄 "「我想他只不过还是孩子呢。」"
    "不知害怕危险的孩子，和能很平常地做出大人做不出来之事的人，根本就是一样的。"
    voice "NYU10A_YU043"
    结乃 "「是吗？可是他体育成绩也不是也很好吗？」"
    志雄 "「是这样的吗？完全没有印象，难道不是很普通的吗？」"
    志雄 "「体力一般的家伙却那么精力旺盛，总而言之可真是个做事不考虑别人感受的家伙啊。」"
    "连自己的体力多少都不顾在那里忘乎所以地游泳就是个最好的证据。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LDA04"),"True","img/YU_LDA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU044"
    结乃 "「原来如此……」"
    voice "NYU10A_X7000_K"
    アナウンス "「大家好，１年来久疏的问候，今天也一如既往地举行了哦，滨咲广播大赛！」"
    志雄 "「啊，第一个出场的节目要开始了呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LDA01"),"True","img/YU_LDA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU045"
    结乃 "「我们就在海滩上悠闲地听听广播，鉴赏一下别人的节目吧。」"
    志雄 "「嗯，大海就交给亨吧……」"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_NOSKIP
    show expression "img/BG21AA@2x.jpg" as bg0 zorder 0 with dissolve
#EFF_PRI 0
#EFF_STAC 0,WATERTWINKLE,EFF_NOSKIP
    stop music fadeout 1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LEA01"),"True","img/YU_LEA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (64/32.0)
    play sound "SE05_19L"
#FADE_IN 1
    voice "NYU10A_TO037"
    亨 "「衣服～！！我的衣服在哪里啊～～～！！」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LEC03"),"True","img/YU_LEC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「看，那就是不管不顾别人感受的下场。」"
    voice "NYU10A_YU046"
    结乃 "「他的衣服刚才有交给我们吧……不叫他一下吗？」"
    "在我们一通折腾过后，亨的衣服还依然平安地留在我扔掉的地方。"
    "虽然我应该和结乃一起把东西收好给亨送过去……"
    志雄 "「真是个让人没办法的家伙呢啊。」"
    voice "NYU10A_RI000"
    りりす？ "「啊！居然在这种地方！」"
    志雄 "「呃……莉莉丝！」"
    "突然感觉暴风雨仿佛将至。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 0,(320-192)
#CHR_POSC 1,(320+192)
#CHR_POSC 2
#CHR_DSPTC 0,1,2,YU_MEA01,CH_MEA01,RI_MDD02
#RRND F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MEA01"),"True","img/YU_MEA01A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
        xcenter .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MEA01"),"True","img/CH_MEA01A@2x.png") as lh1 zorder (10+0):
        ypos 0.0
        xcenter .8
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDD02"),"True","img/RI_MDD02A@2x.png") as lh2 zorder (10+0):
        ypos 0.0
        
    with dissolve
    play music  "BGM02"
#SE_VOLC 1,64
    "我想那暴风雨的正体就是莉莉丝吧……还真是一点都没变，真热闹呢。"
    voice "NYU10A_RI001"
    莉莉丝 "「什么嘛，明明好久不见，真是不懂礼貌的家伙呢。」"
    "莉莉丝似乎对我刚才那一声『呃』格外介意的样子呢，非常不满地撅起了嘴。"
    voice "NYU10A_YU047"
    结乃 "「辛苦了啊，智纱学姐。」"
    voice "NYU10A_CH000"
    智纱 "「你好啊，结乃，塚木君。」"
    "和莉莉丝一起来的箱崎，认真的回应了结乃的寒暄。"
    "和箱崎这样面对面交谈，还真是勾起了一些久违的回忆呢。"
    "互相没有躲躲闪闪，关系上也算挺友好的，虽然比不上和莉莉丝与结乃之间的关系，但多少还算是和谐了。"
    志雄 "「喂，虽然很不好意思，不过这个能拜托保管一下吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDA01"),"True","img/RI_MDA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU10A_RI002"
    莉莉丝 "「谁的衣服，看起来也不像你的啊。」"
    志雄 "「是亨的哦。他在那边游泳呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDA06"),"True","img/RI_MDA06A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU10A_RI003"
    莉莉丝 "「佐贺君？说是游泳呢，倒不如说像溺水了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MEC01"),"True","img/YU_MEC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU048"
    结乃 "「他自己倒是有说要玩得尽兴来着。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MEC02"),"True","img/CH_MEC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_CH001"
    智纱 "「他没事吧……干吗那么乱来呢。」"
    志雄 "「玩累了呢。我想差不多该回去了，把这个交给他吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MEC04"),"True","img/CH_MEC04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_CH002"
    智纱 "「……是，是吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDB01"),"True","img/RI_MDB01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU10A_RI004"
    莉莉丝 "「过去看看佐贺那家伙吧，咱们也可以顺便玩一会儿。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MEB01"),"True","img/CH_MEB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_CH003"
    智纱 "「嗯，那个怎么看都像是溺水了呢……」"
    志雄 "「亨……」"
    "如果要说个这么做的理由的话，莉莉丝去亨那里的话我就可以安心了。"
    "而且那样的话亨也会很开心的。"
    志雄 "「拜托你了哦。已经到了我们该出场的时候了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MEA01"),"True","img/YU_MEA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU049"
    结乃 "「对呢，差不多该过去了呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MDC02"),"True","img/RI_MDC02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU10A_RI005"
    莉莉丝 "「啊，是吗。那过会儿我要去会场捣乱了。」"
    志雄 "「不该给我应援么我说。」"
    "看着莉莉丝满载恶作剧之心的坏笑，必须得事先嘱咐妥当才行。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MEB02"),"True","img/CH_MEB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_CH004"
    智纱 "「哈哈哈。还真是挺开心的呢，二位。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MEA02"),"True","img/YU_MEA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU050"
    结乃 "「敬请期待哦。一定不会辜负大家的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MEB04"),"True","img/CH_MEB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    "听了结乃坚决的发言之后，箱崎惊讶地看着她。"
#MES "听了结乃坚决的发言之后，箱崎惊讶地看着她。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MEA01"),"True","img/CH_MEA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    extend "但是很快脸上便浮现起了微笑。"
#MESX "但是很快脸上便浮现起了微笑。%K%P"
    "也许是一同在广播台工作的经历，他们也因此产生了强烈的信赖关系吧。"
    志雄 "「那么结乃，咱们走！」"
    "我拍了拍我所最信赖的伙伴的肩膀，时间很充足。"
    voice "NYU10A_YU051"
    结乃 "「是。一起加油吧，志雄学长。」"
    "告别了莉莉丝和箱崎，我和结乃向代替舞台的小帐篷走去。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG95AA@2x.jpg" as bg0 zorder 0 with dissolve
#EFF_PRI 0
#EFF_STAC 0,TWINKLE3,EFF_NOSKIP
    scene expression "img/BG95AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    "我们走向占据了海岸一端的帐篷群，从明显的滨咲ＦＭ标识的地方进去了。"
    "在最大的那顶帐篷上，写着『浜咲广播大赛』的超大字样。"
    "帐篷里坐着的是正在放送节目的选手。他们向着麦克风干脆地讲着话。"
    "作为优秀作品的主持人，他们的言语都非常流利。"
    "完全没有一点新人的感觉……"
    "舞台里接连不断有人来回走动着。"
    "我们呆呆的站在那里，与气势恢宏的现场气氛相比有些格格不入，感觉实在是有些糟糕。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LEA01"),"True","img/YU_LEA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA03"),"True","img/KA_LAA03A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    play music  "BGM10"
    voice "NYU10A_KA000"
    神奈 "「呀，欢迎欢迎。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LEB02"),"True","img/YU_LEB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU052"
    结乃 "「神奈！你来了啊。」"
    voice "NYU10A_KA001"
    神奈 "「那是当然的啦～明明写了那种邮件却还没听过节目呢啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LEA01"),"True","img/YU_LEA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU053"
    结乃 "「啊，是啊。早知道就把录的带子的备份给你送过去了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA02"),"True","img/KA_LAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_KA002"
    神奈 "「啊哈哈，嘛，不过这只是其中一半的理由哦。」"
    志雄 "「一半？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_KA003"
    神奈 "「前天的时候，浜咲ＦＭ这边打来电话，说要邀请前任优胜者来当工作人员。交通费报销，日薪是……保密哦。」"
    "神奈说着，朝我眨了眨眼睛。"
    window hide
    hide lh1 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_PRIC 1
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_XAA01"),"True","img/KA_XAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    "我还在发愣的时候，手忽然一下被握住了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LEC02"),"True","img/YU_LEC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_KA004"
    神奈 "「请好好加油哦，志雄。」"
    志雄 "「诶？啊，那是一定的。」"
    "被握住的手为什么会这么热呢？是不是因天气原因呢？"
    window hide
    play sound "SE04_10"
#QUA2_CHR 1
    "就在这酷暑的恍惚之间，我们相握的手被结乃一个手刀给劈开了。"
    voice "NYU10A_KA005"
    神奈 "「哇，好疼。」"
    window hide
    hide lh1 with dissolve
#CHR_SET_BACK
#CHR_INIC 1
#CHR_PRIC 1
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NYU10A_YU054"
    结乃 "「喂喂，对我就没有什么鼓励的话吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA03"),"True","img/KA_LAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_KA006"
    神奈 "「一看就知道你情绪高涨。在会场上好好地表现给我看吧。」"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,YU_LXB05,3,F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LEB05"),"True","img/YU_LEB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#THREAD_STA 1,THREAD_CHR_ASE
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#REEK_CHR 0
    voice "NYU10A_YU055"
    结乃 "「诶诶……完全没有给我减压的意思～」"
#REMOVE_REEK_CHR 0
#THREAD_STP 1
    hide bg3 with dissolve
#BG_PRI 3
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA02"),"True","img/KA_LAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_KA007"
    神奈 "「啊哈哈哈。」"
    "与神奈交谈时候的结乃，是不是表情要比和我对话的时候丰富得多呢？"
    "……嫉妒女朋友的密友，我好像神经有些过度敏感了吧。不过，这时想插入她们对话也很难就是了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA01"),"True","img/KA_LAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU10A_KA008"
    神奈 "「对了，结乃。我决定暑假期间暂时留在这里了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LEA01"),"True","img/YU_LEA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU056"
    结乃 "「是吗，那要来我家住吗？」"
    voice "NYU10A_KA009"
    神奈 "「嗯，虽然有考虑过那样不过……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_LAA03"),"True","img/KA_LAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    "神奈对结乃的话支支吾吾的一番答应之后，忽然转过身来看着我。"
    "经验告诉我，这恶作剧一般的笑容背后一定有着不同寻常的预谋。"
    "这样的性格和在我身边的某个人还真相似啊。"
    voice "NYU10A_KA010"
    神奈 "「说起来志雄，你是房东来着吧？」"
    志雄 "「嗯？啊，是呢。」"
    voice "NYU10A_KA011"
    神奈 "「房间，还有空着的吗？我已经做好接受志雄好意的准备啦！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LEB06"),"True","img/YU_LEB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「诶？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LEC02"),"True","img/YU_LEC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU057"
    结乃 "「不行，这可不行！你就在我家住，好吧？明白了吗？」"
    voice "NYU10A_KA012"
    神奈 "「啊，好像到时间了哦，那走了走了。」"
    voice "NYU10A_YU058"
    结乃 "「喂，你明白了没有~！？」"
    window hide
    hide lh1 with dissolve
    "第７组的放送时间结束了。"
    "托神奈的福，结乃紧张的神情已经完全消失了。"
    "……而且是完全看不出一丁点紧张的样子了。"
    "好吧，其实该紧张的人是我呢。"
    "我担心在这样的舞台上自己是能否顺利播报，不过，最重要的还是在其中某个地方插入给结乃的讯息。"
    志雄 "「结乃，来，再不快点就要丧失比赛资格了哦。」"
    voice "NYU10A_YU059"
    结乃 "「啊，好的。我知道了。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'KA'",DynamicDisplayable(mouthanime,"KA_MAA02"),"True","img/KA_MAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NYU10A_KA013"
    神奈 "「那么加油咯，志～雄～」"
    "神奈向我挥舞着手臂声援着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LEA03"),"True","img/YU_LEA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "我用余光扫了一眼，发现结乃正直直地瞪着我。"
    "神奈啊，拜托你别再这样戏弄结乃了。"
    window hide
    hide lh1 with dissolve
    "我就这样沉默着，把手放在结乃的头上轻轻地抚摸着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LEA06"),"True","img/YU_LEA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU060"
    结乃 "「！诶嘿嘿～」"
    "不知道为什么，结乃露出了开心的笑容。"
    "……其实我只是想借助抚摸结乃的头来让自己安定下来……看来这个秘密我必须带进坟墓里了。"
    stop music fadeout 132
    "然后，一直以来所期望的直播正式开始了……！"
    window hide
    stop sound
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#CHR_INIC 0
#CHR_POSC 0,-63
    hide lh0
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU07AA")]=True
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"EVN_YU07A"),"True","img/EVN_YU07AA@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#BG_FLG EVN_YU07AA
#BG_SET_BACK 
#BG_INIC 2
    show expression "img/BG95AA@2x.jpg" as bg2 zorder 2 with dissolve
    play sound "SE05_19L"
#FADE_IN 1
    play sound "SE07_07"
    志雄 "「志雄和！」"
    voice "NYU10A_YU061_K"
    结乃 "「结乃的！」"
    voice "NYU10A_YU062_K"
    結乃・志雄 "「浜咲讯息！」"
    window hide
    play music  "BGM06"
    voice "NYU10A_YU063"
    结乃 "「大家好，接下来是最后的节目了，１０分钟的时间，带给大家不一样的心灵陪伴！」"
    "本来在讲稿里，报完标题后面紧接着是这次节目的精彩介绍。"
    "结乃郑重观众打着招呼，十分地机智嘛。"
    "她很清楚，我们正在为谁播送着节目。"
    "我也要认真起来了，要还是过分紧张的话就会拖结乃的后腿了。"
    志雄 "「结乃酱，突然之间就即兴穿插还是饶了我吧~」"
    voice "NYU10A_YU064"
    结乃 "「志雄君，这点程度而已请不要惊慌失措的哦。」"
    志雄 "（哦……？志雄、君？）"
    "我一开始只是即兴地叫了她『结乃酱』，而结乃立刻就以『志雄君』的称呼回应了我。"
    "真的是游刃有余，乐在其中呢。"
    "而作为我来说，对终于从『志雄学长』这个称呼中解脱出来，也感到十分的开心。"
    voice "NYU10A_YU065"
    结乃 "「在这个节目里，平时无法好好传递的，想对对方诉说的秘密或是思念，会由我们用电波帮你送去哦。」"
    志雄 "「听众朋友们的投稿将成为本次节目的主角。」"
    voice "NYU10A_YU066"
    结乃 "「嗯，心动就赶快行动吧。」"
    志雄 "「是的，无论怎样，请抓住这１０分钟，给彼此一个机会吧！」"
    "总算是回到了讲稿的流程里来了，结乃手里已经拿起了第一封投稿。"
    "事前商议的时候，为了选出有价值的素材，全部的讯息都重新过目一遍，不过我并不知道这封的内容会是什么。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU07BA")]=True
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'EVN'",DynamicDisplayable(mouthanime,"EVN_YU07B"),"True","img/EVN_YU07BA@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#BG_FLG EVN_YU07BA
    voice "NYU10A_YU067"
    结乃 "「那么，我来介绍一下第一封讯息。」"
    voice "NYU10A_YU068"
    结乃 "「昵称『小恶魔酱』发来的讯息。」"
    "用了『小悪魔酱』这么可爱十足的昵称，我实在无法相信其实是那个家伙写的。"
    "那家伙也有恶意卖萌的兴趣啊……"
    voice "NYU10A_YU069"
    结乃 "「请将这封讯息传递给我的挚友。」"
    voice "NYU10A_YU070"
    结乃 "「我想将我的两份思绪，传递给挚友……可是，我一直就无法说出来。」"
    voice "NYU10A_YU071"
    结乃 "「非常感谢你一直以来都陪在我的身边。我那时多管闲事伤害到了你，真的对不起。」"
    voice "NYU10A_YU072"
    结乃 "「那个笨蛋现在非常非常幸福的样子，所以，我们也要全力变得幸福起来给那家伙看一看！」"
    voice "NYU10A_YU073"
    结乃 "「……这样。」"
    "流利地读完『小恶魔酱』的讯息，结乃将视线投向了我。"
    "我想自称『小恶魔酱』的那个人，也是彻底地将自己的心声表达了出来。"
    "对于我来说，这份投稿也有着不同一般的意义。"
    "平时绝对无法开口说出的话，可以通过广播投稿的形式完整地表达出来……"
    "这就是广播那神奇的力量吧。"
    "『小恶魔酱』也好好地掌握了广播的魔法呢。"
    "不过，话虽如此……"
    志雄 "「“那个笨蛋”这种话……」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"EVN_YU07A"),"True","img/EVN_YU07AA@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU074"
    结乃 "「是关于谁的事情呢？不过，我想『小恶魔酱』与好友们一定都会非常非常幸福的。」"
    志雄 "「别人的幸福什么的，就这样就断言好吗？」"
    voice "NYU10A_YU075"
    结乃 "「不是『能不能幸福』，而是『一定会幸福』哦！所以说，『小恶魔酱』是会幸福的，谁也无法来防碍。」"
    "是啊，结乃断言了。"
    "不是希望能够幸福就好了，而是为能够幸福而去努力！"
    "结乃完全的理解了『小恶魔酱』这封讯息想要表达的意思呢。"
    志雄 "「『小恶魔酱』她一定可以轻松地做到呢。」"
    voice "NYU10A_YU076"
    结乃 "「嗯，所以才说是那样的嘛。」"
    "我环顾会场，在观众席中看见了『小恶魔酱』她的身影。"
    "与旁边的好友并排坐着，满脸通红地低下着头。"
    "看她一副这样的表情，恐怕这封讯息就是她的真心话吧。"
    "……广播的魔力可真是不容小视呢。"
    voice "NYU10A_YU077"
    结乃 "「接下来请志雄君念一封讯息吧。」"
    "我接过了结乃从讲稿下拿出的第二封讯息。"
    志雄 "「下一封讯息，来自昵称『凯尔玛妹妹』。」"
    志雄 "「这位小姐好像也是要送给挚友的讯息呢。」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"EVN_YU07B"),"True","img/EVN_YU07BA@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU078"
    结乃 "「是，是吗……」"
    "突然就是去年优胜者的稿件了……不过说起来有一半的投稿讯息是『凯尔玛妹妹』发来的，采用率高也是自然的了。"
    "虽然我们都知道内容，但还是明显地感到身边的结乃紧张起来。"
    志雄 "「给幸福的挚友。我不在的时候你一直用我的名义传达着思念，当我们许久不见后再会时，你连男朋友都有了……」"
    志雄 "「我真想找茬和你再吵一架。」"
    志雄 "「可是，最让我懊恼的是，无论怎样争吵，最后我始终都是喜欢着你的。」"
    志雄 "「所以，你可一定要幸福啊。我也会一直作为你最强的后援。要加油哦！」"
    志雄 "「……啊，说得对呢。」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"EVN_YU07A"),"True","img/EVN_YU07AA@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU079"
    结乃 "「『凯尔玛妹妹』可真是个温柔的人啊。」"
    "结乃和我一同装作若无其事地看向帐篷后面。"
    "随着视线，神奈正在特等席那里骄傲的看向我们。"
    "她双手环抱在胸前，脸上挂着非常满足的笑容。"
    "这就是职业投稿老手与自称『小恶魔酱』的普通投稿人的差距呢。"
    志雄 "「可是，从字面上来看，是不是有些不太坦率呢？」"
    voice "NYU10A_YU080"
    结乃 "「也许这就是会争吵的原因吧。改一改的话不好吗？」"
    志雄 "「不，我倒觉得她们彼此彼此呢。」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"EVN_YU07B"),"True","img/EVN_YU07BA@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU081"
    结乃 "「哼，志雄君是这么想的吗？」"
    "结乃直直地盯着我。"
    "不行啊，这样再继续深入下去的话就变成家庭内部问题了。"
    "我慌忙转换到下一个话题。"
    志雄 "「比起这个，在两位延续着友情的讯息之后，我们来更换一下心情吧。」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"EVN_YU07A"),"True","img/EVN_YU07AA@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU082"
    结乃 "「好的。那么接下来的这封讯息，来自昵称『贝尔』的这位朋友。」"
    voice "NYU10A_YU083"
    结乃 "「想对依然是自由职业者的弟弟，进行一下鞭策激励。」"
    志雄 "「啊，这还真是有点意思呢。」"
    "『贝尔』不愧是专职的作家啊，稍微写写就能创作出很多令人捧腹的投稿。"
    "同时，犀利的字里行间也能感受到她特有的关怀，把爽朗的印象完好地传递给听众。"
    "我为了呼应结乃选出的这封讯息，把稻穗…………不，是广播名『菜西』的稿件选了出来。"
    "自由职业者的他把对亲姐姐的血泪控诉全部写进了讯息。"
    "虽然是这样，不过其实还是希望着能成为关系的和睦的姐弟……这也是一封不错的讯息嘛。"
    "在此之后，来自昵称星号先生，寄给小恶魔的讯息被选读了，再然后……"
    "聚集在这里的我们所有的小伙伴都因为自己的讯息被读到而害羞起来……让内心变得温暖的讯息依然在一封一封被读到。"
    志雄 "（诶～，尤其是神奈和箱崎，能够直抒胸臆地写出如此感人泪下的投稿呢～）"
    "观众们的反应也异常热烈。"
    "大概信件的内容让他们产生了共鸣吧。"
    "人群中有人不时使劲地点头，也有人默默地用手擦拭眼角。"
    "我们所传递出去的东西，真是打动了不少人啊。"
    voice "NYU10A_YU084"
    结乃 "「呃，那么接下来的讯……」"
    stop music fadeout 132
    play sound "SE09_28"
    志雄 "「哎呀，快到时间了啊，节目要到这里为止了哦。」"
    voice "NYU10A_YU085"
    结乃 "「唔……现在我们来介绍一下本次节目的片尾曲。」"
    voice "NYU10A_YU086"
    结乃 "「为本次节目画上圆满句号的，是众所周知的，知名主持人ＫＡＮＡＴＡ的歌曲『Ｗａｖｅ！！！』」"
    志雄 "「距离节目结束还有大约１分钟。」"
    voice "NYU10A_YU087"
    结乃 "「各位，感谢您的收听，让我们在悠扬的歌声中，享受讯息带给我们的魅力生活。」"
    志雄 "「…………啊。」"
    "节目非常成功。不过，如果就这样结束的话对我来说绝对不能算优胜。"
    "因为，还有一件最重要的事情还没有做。"
    window hide
    stop se
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"EVN_YU07B"),"True","img/EVN_YU07BA@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU10A_YU088"
    结乃 "「志雄君……？怎么了？」"
    志雄 "「抱歉，各位观众。请允许我再读一封讯息。」"
    voice "NYU10A_YU089"
    结乃 "「诶……？」"
    志雄 "「是来自志雄给结乃的……为了传达这条讯息，这是我努力参加这个比赛的全部理由。」"
    voice "NYU10A_YU090"
    结乃 "「诶？诶？……是、是这样的吗？」"
    志雄 "「对不起，没有提前告诉你，因为我想给你一个惊喜……」"
    "听众、帮忙的职员，所有的人都和结乃一样愣住了。"
    "对于我突然做出这样的发言，大家多多少少都有些意外吧。当然，坐在演播室中的我更是紧张万分，总之现在的气氛很糟糕。"
    voice "NYU10A_TO038"
    亨 "「好的！志雄！快读哦！」"
    window hide
#BG_UVC 2,80,32,400,280
#CHR_SET_BACK
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 1,(320-160)
#CHR_POSC 2,(320+160)
#CHR_ALP_AUTOC 0,0,0,1
    志雄 "（亨……！）"
    voice "NYU10A_MA018"
    麻寻 "「结乃！要认真地听哦！」"
    志雄 "（麻寻！）"
    "在节目开始之前没有见到，不过还是赶来了呢！"
    window hide
#CHR_ALP_AUTOC 0,128,0,1
#CHR_ERSWC 1,2
    志雄 "「那么为答谢这份对我的支持。」"
    "我为了对他们两人表示感谢而站了起来。"
    play music  "BGM14"
    志雄 "「给，结乃。」"
    "结乃伸出手接过了我递过去的麦克风。"
    voice "NYU10A_YU091"
    结乃 "「……是、是！」"
    "结乃似乎不知所措，虽然按照我的要求做了，却一直不安地望着我。"
    "……便签纸和讲稿之类的都不需要。想要传递给结乃的讯息的内容，正源源不断地从我的心中喷涌而出。"
    志雄 "「为了这次的比赛，我们第一次大吵了一架。」"
    志雄 "「可是，广播赐予我们的缘分，并非一点点争吵就可以消除的。」"
    voice "NYU10A_YU092"
    结乃 "「……志雄学长。」"
    志雄 "「也许我要感谢这次的小矛盾，是它让我了解了结乃很多迄今为止我都所不了解的一面。」"
    志雄 "「虽然也有迷惘，不过，我还是乐在其中。」"
    voice "NYU10A_YU093"
    结乃 "「啊哈哈。这个……深有同感呢。」"
    志雄 "「与『凯尔玛妹妹』一样。无论怎样的吵嘴我也喜欢结乃，我绝不会后悔。」"
    志雄 "「我想，从今以后，也许会有很多的事情变化无常。不过，我的感情永远不会变。」"
    志雄 "「我，喜欢春日结乃！」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU07CA")]=True
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"EVN_YU07C"),"True","img/EVN_YU07CA@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    结乃 "「…………！」"
#BG_FLG EVN_YU07CA
#MESEX_A M_NOA,A_CH_YU,NYU10A_YU094,"【結乃】「…………！」%K%P"
    志雄 "「感谢您的聆听！本次节目是由塚本志雄与搭档——」"
    voice "NYU10A_YU095"
    结乃 "「啊……春、春日结乃为您真诚献上！」"
    play sound "SE03_25"
    "观众席上响起了洪亮的掌声，不过这掌声仅仅来自一个人。"
    play sound "SE03_83"
    "亨……那家伙带头拍起了双手。不久，一个接一个的，掌声逐渐热烈起来。"
    play sound "SE03_26"
    "最终，在仿佛要把我们淹没的如雷掌声中，我们的节目落下了帷幕。"
    "独一无二的『浜咲讯息』，传递到了很多人的内心深处。"
    window hide
    pause (64/32.0)
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
#BG_ANM_OFFC 1
    scene expression Solid("000") with fade
    stop se
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG21EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG21EA@2x.jpg" as bg0 with dissolve
#CHR_INIC 0
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XEB01"),"True","img/YU_XEB01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    play music  "OBGM11"
    play sound "SE05_19L"
#FADE_IN 1
    志雄 "「辛苦了，结乃。」"
    voice "NYU10A_YU096"
    结乃 "「志雄学长……啊。」"
    "我将结乃的手牵了起来，一次又一次地用力紧紧握住。"
    志雄 "「真的非常感谢，我真的非常开心。」"
    voice "NYU10A_YU097"
    结乃 "「我也是……特别、特别、特别的开心！」"
    "结乃的眼泪，映射着夏日的阳光，慢慢地落了下来。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU08A")]=True
    show expression "img/EVN_YU08A@2x.jpg" as bg1 zorder 100 with dissolve
    志雄 "「啊~……真难为情~」"
    voice "NYU10A_YU098"
    结乃 "「我也是很难为情的啊。」"
    voice "NYU10A_YU099"
    结乃 "「志雄学长，真厉害……居然又做了这么史无前例的事情。」"
    志雄 "「现在应该说点别的吧？」"
    voice "NYU10A_YU100"
    结乃 "「那是因为……」"
    voice "NYU10A_YU101"
    结乃 "「你都不在乎别人的目光吗？」"
    志雄 "「我非常紧张的啊？没发觉吗？」"
    voice "NYU10A_YU102"
    结乃 "「总觉得没有啊。」"
    志雄 "「结乃在广播台白天也有播放节目吧？那岂不是比现在更引人注目？」"
    voice "NYU10A_YU103"
    结乃 "「普通的对话当然没有问题啦。可是，那个……发言的内容就……那个……」"
    志雄 "「难道不喜欢吗？不会给你添麻烦了吧？」"
    voice "NYU10A_YU104"
    结乃 "「没有没有。」"
    voice "NYU10A_YU105"
    结乃 "「不过，两个人独处的时候，也说说那种话吧……可以吗？」"
    志雄 "「啊，这样啊。」"
    志雄 "「哈哈……不过真的想说些感谢的话呢……」"
    志雄 "「这次发生了很多很多事情，那样的情形下……」"
    voice "NYU10A_YU106"
    结乃 "「感谢的话是指……？」"
    志雄 "「学生会的工作也好，节目的制作也好，结乃都把它们处理得非常好。不止是我，有你的存在大家都轻松了很多。」"
    voice "NYU10A_YU107"
    结乃 "「哪有，没给大家添麻烦就好了……」"
    志雄 "「一直以来谢谢你了，从今以后也拜托你了。」"
    voice "NYU10A_YU108"
    结乃 "「我也是……那个，非常非常谢谢你。」"
    志雄 "「哈哈哈……」"
    voice "NYU10A_YU109"
    结乃 "「傻，傻笑什么，这是？」"
    志雄 "「感谢的话和表达爱意的话，哪一边比较好呢？」"
    voice "NYU10A_YU110"
    结乃 "「怎……怎么这样！肯定是哪边都好啦不是吗？」"
    志雄 "「是，是吗？」"
    voice "NYU10A_YU111"
    结乃 "「那、那个……」"
    志雄 "「嗯？」"
    voice "NYU10A_YU112"
    结乃 "「现在的话，只有我们俩人独处了哦。」"
    志雄 "「诶？」"
    voice "NYU10A_YU113"
    结乃 "「表达爱意的任务，拜托你了。」"
    志雄 "「……明白了！」"
    志雄 "「无论多少回，我都会继续说下去。直到结乃你听够了为止！」"
    志雄 "「我，喜欢春日结乃！」"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU08B")]=True
    show expression "img/EVN_YU08B@2x.jpg" as bg1 zorder 100 with dissolve
    pause (128/32.0)
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1,128,COL_WHITE
    scene expression Solid("000") with fade
#GRAPH_INI 
    stop se
    stop sound
    stop music fadeout 1
#MOV_PLY 5
#RSET S101
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
    $ renpy.end_replay()
    return
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT
