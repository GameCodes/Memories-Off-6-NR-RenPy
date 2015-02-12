label NYU09A:
    $currentlabel = "NYU09A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '08'
    $day = '01'
    $date = '2'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 3,CAL_0801
    scene expression Solid("000") with fade
    show expression "img/NIMG15I-568h@2x.jpg" as cal zorder 5
    show expression "img/08_01_TUESDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG07AA1@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG07AA1@2x.jpg" as bg0 with dissolve
    play sound "SE05_14L"
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
    "已经是截止日的当天早上。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA02"),"True","img/TO_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO000"
    亨 "「各位——！都准备就绪了吗——！」"
    志雄 "「真够精神呢，亨。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAB03"),"True","img/MH_LAB03A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    
    with dissolve
#MESEX_A M_NOA,A_CH_MA,NYU09A_MA000,"【麻尋】「…………」%K%P"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC01"),"True","img/YU_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU000"
    结乃 "「怎么了？麻寻。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAB04"),"True","img/MH_LAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA001"
    麻寻 "「啊？没啥……没事，啥都没有。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "一大早开始就让亨和麻寻集合过来，我们终于决定要开始节目的录音了。"
    "录音完成，再编辑成10分钟的节目，录到磁带上，在下午5点前送到浜咲ＦＭ的接待处。"
    "这样一来能做的就都做完、然后就是一边等一边向神祈祷了。"
    志雄 "（真想赶快完成……已经有点紧张了……）"
    "这么想来，自己一直都是擅长听广播而已。"
    "结乃也和我这么说过，到了真主持的时候，那种紧张感真不是等投稿的稿件被选上的感觉能比的。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA01"),"True","img/TO_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM10"
    stop sound fadeout 1
    voice "NYU09A_TO001"
    亨 "「嗯，那么，开始咯！」"
    "真羡慕这家伙能这么轻松开朗。"
    志雄 "「那么说来最后，亨你也接受了采访吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB02"),"True","img/TO_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO002"
    亨 "「那当然！相信我，那错不了一定会成为传说的。」"
    "亨自信满满地挺起胸膛。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAB03"),"True","img/MH_LAB03A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NYU09A_MA002"
    麻寻 "「嗯。传说，是呢。」"
    voice "NYU09A_YU001"
    结乃 "「佐贺学长都说了些什么呢？」"
    voice "NYU09A_MA003"
    麻寻 "「想听？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC04"),"True","img/YU_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU002"
    结乃 "「诶？」"
    voice "NYU09A_MA004"
    麻寻 "「稍微把耳朵靠过来。」"
    voice "NYU09A_YU003"
    结乃 "「是……是！」"
    "麻寻在结乃耳边说了很长时间的一段悄悄话。"
    voice "NYU09A_MA005"
    麻寻 "「这个和那个啦，还有就是这个，那个和这个居然……」"
    "怎么说了这么久啊……"
    "亨，你这家伙到底干了些啥呢？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB06"),"True","img/YU_LBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU004"
    结乃 "「呵呵……诶？哈哈哈哈哈？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB05"),"True","img/YU_LBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "结乃终于听完了，惊讶和诧异以及各种各样的复杂表情同时浮现出她的脸上。"
    "连脸都红了，相比亨是作出了相当羞耻的事情吧？"
    志雄 "「我说，都干了些什么啊，亨那家伙。」"
    "都表现出这种反应了，我也只能问她。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC02"),"True","img/YU_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU005"
    结乃 "「想听吗？就那么想听吗？」"
    志雄 "「别逗我了。什么嘛，都说了那样的话能不在意吗？」"
    voice "NYU09A_YU006"
    结乃 "「我只是确认一下而已。志雄学长说了想听吧？」"
    志雄 "「ＯＫ、ＯＫ！没关系的所以告诉我吧～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC03"),"True","img/YU_LBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU007"
    结乃 "「啊，果然，我觉得还是不要问比较好。」"
    志雄 "「怎，怎么突然就。快点告诉我吧~」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC05"),"True","img/YU_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU008"
    结乃 "「要从我口中说出来实在太……」"
    志雄 "「那么，麻寻，请再和我说一遍吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA04"),"True","img/MH_LAA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA006"
    麻寻 "「诶诶？你去问他本人啦。」"
    志雄 "「嗯那么，亨！」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB01"),"True","img/TO_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO003"
    亨 "「哈哈哈，请听下回分解！」"
    志雄 "「什么嘛，大家都这样～」"
    "即使我紧紧追问，结乃和麻寻好像羞于某事而不肯开口。"
    "当然亨装模作样地不肯告诉我。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA02"),"True","img/TO_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO004"
    亨 "「呵。大概不得不用了吧，这份期待感！」"
    志雄 "「可恶，快点告诉我啊！」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA01"),"True","img/MH_LAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NYU09A_MA007"
    麻寻 "「好了，这个先不谈，其他的投稿如何了，收集得怎么样？」"
    voice "NYU09A_YU009"
    结乃 "「啊，是！借用了学校的打印机打印出来了。」"
    play sound "SE03_18"
    "结乃把放进信封里一叠纸重重的摆在了桌子上。"
    "比想象中还要多的数量。纸叠的厚度大概有1厘米吧？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA02"),"True","img/MH_LAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA008"
    麻寻 "「有很多啊，这下投稿数量足够了吧？」"
    voice "NYU09A_YU010"
    结乃 "「有一半是神奈的投稿，剩下的量中又有一半是远峰学姐那里发来的。」"
    志雄 "「这个量的一半还有，一半的一半的话……占了好多啊？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB04"),"True","img/TO_LBB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO005"
    亨 "「真是胡闹呢，那个叫神奈的孩子。」"
    志雄 "「但是，亨，胡闹榜第二名是莉莉丝吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA02"),"True","img/TO_LBA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO006"
    亨 "「哦哦，是的。让我来审核莉莉丝投稿的那部分！快点！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA04"),"True","img/YU_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU011"
    结乃 "「是，是，请吧。」"
    window hide
    hide lh1 with dissolve
    "亨大喝一声将印有莉莉丝那部分投稿的纸夺了过去，哗啦哗啦地开始翻起来看。"
    voice "NYU09A_TO007"
    亨 "「呵呵呵。就让我看看那莉莉丝是不是有什么给我的讯息吧！」"
    志雄 "「要是不是什么『爱的讯息』，那亨就很可怜了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU012"
    结乃 "「是的呢。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA01"),"True","img/MH_LAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NYU09A_MA009"
    麻寻 "「诶，为了让亨君能因此更为成熟，如果有的话就选上吧。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "听了麻寻的话，我和结乃互相点头。"
    "就这样，亨抽走了所有莉莉丝的投稿，我们大概地看了一下其他的。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA06"),"True","img/MH_LAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA010"
    麻寻 "「喂，这个人写的『愚弟』指的是谁？」"
    志雄 "「啊，那个的话、稻穗先生知道得比较清楚喔。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA02"),"True","img/MH_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA011"
    麻寻 "「啊，是吗？下次试试问他～♪」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "铃小姐给稻穗先生的讯息。"
    "我看了一下，完全是嘲笑他取乐，还是别用了。"
    "不过她给编辑的『祈求书』就特别的诚恳，很有意思，就选这个吧。"
    "不过没有稍微，那种……感动类的讯息吗？"
    "我期待着能有新的发现，伸手去拿其他的投稿。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA02"),"True","img/TO_LBA02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NYU09A_YU013"
    结乃 "「远峰学姐的投稿，怎么样？」"
    voice "NYU09A_TO008"
    亨 "「嗯。现在还没有看见写给我的。」"
    voice "NYU09A_YU014"
    结乃 "「是的吗。那么，其他的短信呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB04"),"True","img/TO_LBB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO009"
    亨 "「诶？」"
    "亨似乎没听懂似的，呆呆地回答道。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA06"),"True","img/TO_LBA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO010"
    亨 "「其他的……啥？」"
    "我抬起闷声看文件的头，结乃正笑眯眯地逼近亨。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB02"),"True","img/YU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU015"
    结乃 "「那么，不是写给佐贺学长的投稿也看了一遍了吧？」"
    voice "NYU09A_TO011"
    亨 "「当，当然！」"
    voice "NYU09A_YU016"
    结乃 "「看、了、吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA03"),"True","img/TO_LBA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO012"
    亨 "「我只是在找我的名字……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC02"),"True","img/YU_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU017"
    结乃 "「佐贺学长。有干劲是很好，不过请认真一些喔。」"
    "结乃的语气很温和，但是眼神里一点笑容都没有，连我都看的汗毛倒竖，更别说亨了。"
    voice "NYU09A_TO013"
    亨 "「明，明白了。」"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
#FADE_IN 0
    "之后，大家一边各自说着对投稿短信的感想，一边从庞大数量的投稿中检索出节目需要的部分。"
    "虽然很感谢大家的支持，想全都用上的，但节目只有十分钟。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC03"),"True","img/YU_LBC03A@2x.png") as lh0 zorder (10+0):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA01"),"True","img/MH_LAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
        ypos 0.0
    with dissolve
    play sound "SE05_14L"
#FADE_IN 1
    voice "NYU09A_MA012"
    麻寻 "「就这么多吧。」"
    voice "NYU09A_YU018"
    结乃 "「虽然说是就这么多，但绝对算很多了哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB03"),"True","img/TO_LBB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO014"
    亨 "「是呢。这可不是１０分钟就能读完的量。」"
    "本来厚１厘米纸张，现在也只有５毫米了……但正如亨所说，这怎么看都不是１０分钟能够全部介绍的。"
    志雄 "「没办法啦。时间也没有了，总之就先都录下。然后后期剪成合适的长度吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA04"),"True","img/YU_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU019"
    结乃 "「靠后期编辑来压缩节目内容，可没有那么容易的喔。」"
    "也许是因为有着制作广播剧的经验，结乃的语气里充满了无奈。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAB04"),"True","img/MH_LAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA013"
    麻寻 "「节目的长度什么的，一定要正好10分钟吗，不能想办法糊弄一下嘛？」"
    志雄 "「那样的妥协方案是不可行的哦。要是在实际的节目里发生可就成了『放送事故』了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAB03"),"True","img/MH_LAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA014"
    麻寻 "「原来如此，那真的是不行了。」"
    "明白了我的意思后，麻寻用手托着下巴陷入了深思。"
    "大家都学着她，都一边口中念念有词一边继续思考，又过了一会……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU020"
    结乃 "「我和志雄学长，按想介绍的顺序选择短信，然后读到时间差不多为止，这样行吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB01"),"True","img/TO_LBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO015"
    亨 "「哦哦，好方法！比起后期编辑、这样更容易控制。对吧，志雄？」"
    志雄 "「嗯。我也觉得这不错。」"
    "这正如ＫＡＮＡＴＡ在节目的尾声经常说的，『有一封，读不读好呢～』这样的话。"
    "做出现场播送的气氛也许会不错。"
    "更重要的是，真正到了在浜咲海岸的时候，也方便把我的讯息夹进去了。"
    "向结乃的表达感谢之情的讯息。为了要得到读它的机会，我们就必须要通过初赛……"
    "虽然我对结乃说过，广播节目不是为了取胜而采取的手段……之类……嗯。"
    志雄 "（还是先处理好眼前的事情吧！）"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB02"),"True","img/TO_LBB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO016"
    亨 "「好。那就收录吧，要开始咯。」"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG90AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG90AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU021"
    结乃 "「那就开始吧，麻寻，拜托你叫开始咯。」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAC03"),"True","img/MH_MAC03A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    voice "NYU09A_MA015"
    麻寻 "「嗯。不过不是学生的我进入也没关系吗？这里？」"
    "被我们带到澄空学院里麻寻，一反常态的拘谨，脸上带着紧张的表情。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO017"
    亨 "「没事的。能进入学校是因为……那个，得到学生会会长的首肯，能进入广播室则是得到了广播部员的认可呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA03"),"True","img/MH_MAA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA016"
    麻寻 "「是嘛。这样的话，我也以回到高中生时代的心情努力吧。」"
    "麻寻果然还是还是老样子，让她带点轻松的气氛会比较好。"
    "这样就貌似能以良好的态度去面对收录了。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU022"
    结乃 "「佐贺学长，准备ＯＫ了吗？」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA01"),"True","img/MH_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    voice "NYU09A_TO018"
    亨 "「完全可以了！」"
    voice "NYU09A_MA017"
    麻寻 "「那就要，开始了。3——2——1——」"
    "麻寻给了我们一个ＯＫ的手势，示意我和结乃做开始。"
    "嗯。已经开始不自觉的紧张了呢。"
    志雄 "（开始了！）"
    "亨开始操作机器，节目的开场主题曲就开始播放了。"
    window hide
    play sound "SE07_06"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA04"),"True","img/MH_MAA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA018"
    麻寻 "「……哈！？这是啥！？」"
    志雄 "「呜哇啊啊，又是这首曲子吗！」"
    stop sound
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB05"),"True","img/TO_MBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO019"
    亨 "「啊，对不起。弄错了。」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC03"),"True","img/YU_LBC03A@2x.png") as lh0 zorder (10+5):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU023"
    结乃 "「太失败了！佐贺学长，你行不行啊！」"
    "结乃一边捂着耳一边大喊着。"
    "结乃……你是不是对亨特别苛刻了些？"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+192)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAB01"),"True","img/MH_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .8
    with dissolve
    voice "NYU09A_MA019"
    麻寻 "「这边也抱歉了。没有放录音带！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB06"),"True","img/YU_LBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU024"
    結乃・志雄 "「连麻寻都这样！？」"
    hide lh1 with dissolve
    "总觉得前途一片黑暗……"
    "我和结乃就像过于紧绷而断了的弦，耸搭着脑袋，一边把复印纸当做扇子来扇风，一边继续等着麻寻和亨他们做好准备。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAC02"),"True","img/MH_MAC02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    voice "NYU09A_MA020"
    麻寻 "「好，重新鼓劲再次上吧。亨君，ＯＫ？」"
    voice "NYU09A_TO020"
    亨 "「ＯＫ、ＯＫ！」"
    志雄 "「是不是真的啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAB01"),"True","img/MH_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA021"
    麻寻 "「这次我可是有好好地放进录音带了呢！」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU025"
    结乃 "「拜托你了。」"
    "仿佛从天边传来的，结乃有气无力的声音。"
    "好像我的激情也已经莫名的消失了……也许吧。"
    "这次才是，要正式开始了！"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA02"),"True","img/TO_MBA02A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAC02"),"True","img/MH_MAC02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NYU09A_MA022"
    麻寻 "「３——２——１——GO～」"
    play sound "SE07_07"
    "好像真的有反省过的样子，亨带来的曲子和我们的期望变得相一致了。"
    "被过分破坏的气氛在一点点恢复过来。。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBB01"),"True","img/YU_XBB01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    "我和结乃视线交错，终于喊出了第一声。"
    志雄 "「志雄和！」"
    voice "NYU09A_YU026"
    结乃 "「结乃的！」"
    志雄 "「…………」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBB06"),"True","img/YU_XBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#MESEX_A M_NOA,A_CH_YU,NYU09A_YU027,"【結乃】「…………」%K%P"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA06"),"True","img/MH_MAA06A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NYU09A_TO021"
    亨 "「……嗯？」"
    voice "NYU09A_MA023"
    麻寻 "「……诶？」"
    "我们僵在原地，亨和麻寻不解地望着我们。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBB05"),"True","img/YU_XBB05A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,YU_XXB05,3,F24
#REEK_CHR 0
    voice "NYU09A_YU028"
    结乃 "「标……忘记想标题了啊！」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
#BG_PRI 3
    voice "NYU09A_MIX00"
    亨 "「诶诶……？」"
    麻寻 "「诶诶……？」"
    志雄 "「是嘛，糟了……的确是这样。」"
    play music  "OBGM18"
    "光想着计划的事情，完全忘了标题的事了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBC04"),"True","img/YU_XBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU029"
    结乃 "「怎么办，志雄学长！？」"
    "结乃少有地惊慌失措地呜咽了起来。"
    voice "NYU09A_YU030"
    结乃 "「志雄学长怎么办，怎么办，怎么办啊志雄学长！？」"
    志雄 "「先冷静下来，结乃。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBC03"),"True","img/YU_XBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU031"
    结乃 "「是，是……！」"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC03"),"True","img/YU_LBC03A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAB03"),"True","img/MH_LAB03A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NYU09A_MA025"
    麻寻 "「我说，有没有什么备用的方案么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC05"),"True","img/YU_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU032"
    结乃 "「那个的话……呃，事情太多了，就没想过标题……」"
    志雄 "「嗯，一直都没时间去想。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC04"),"True","img/YU_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU033"
    结乃 "「怎么办呢？倒不如干脆，不要标题……啊，不行不行，那样的话不行。」"
    "结乃捂着脑袋，自问自答……"
    "作为一向冷静能干的学生会干事的她，很少见的如此混乱。"
    "这样的动作也很可爱——虽然我这么想，但是当着亨和麻寻的面，我决定还是不说出来了。"
    志雄 "「也许只能现在开始想了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA04"),"True","img/YU_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU034"
    结乃 "「是那样的呢。是那样的。嗯嗯，该叫什么好呢……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA02"),"True","img/TO_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO023"
    亨 "「佐贺亨的，真爱骑士～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA05"),"True","img/MH_LAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA026"
    麻寻 "「无视他。再华丽点吧，用你们名字，志雄和结乃的谐音，『Ｓｏｕｌ，Ｙｏｕ　ｋｎｏｗ』怎么样？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB05"),"True","img/TO_LBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO024"
    亨 "「哎……这哪里比我的噩耗，而且念起来又难听。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAC05"),"True","img/MH_LAC05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA027"
    麻寻 "「什么嘛，你这是嫉妒我的文采！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA04"),"True","img/TO_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO025"
    亨 "「你说什么！」"
    志雄 "「啊，消停消停吧两位。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "亨的方案不在考虑范围内。『Ｓｏｕｌ，Ｙｏｕ　ｋｎｏｗ』，麻寻的方案则让人完全想不出是什么样的节目……"
    "１０分钟的，而且是公开募集的作品。觉得更简洁一点的名字会更好……那么。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA04"),"True","img/YU_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "『要怎么做？』，我看着结乃，眼神里带着这样的疑问，"
    voice "NYU09A_YU035"
    结乃 "「嗯……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU036"
    结乃 "「明白了。标题的事就录音的时候再想吧。等节目结束以后，再剪一段喊标题的部分加进去。」"
    志雄 "「结果，还是要靠后期编辑操作啊……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC04"),"True","img/YU_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU037"
    结乃 "「对不起呢。我……」"
    志雄 "「小事就别在意了。主持人可要打起精神来。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC01"),"True","img/YU_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU038"
    结乃 "「嗯！」"
    "但是，考虑到编辑处理需要的时间，还要思考标题的时间，真的是在和时间赛跑。"
#MESA A_CH_SI,"【志雄】「总之先继续吧。这样的话也不会浪费时间。」%K%P"
    志雄 "「总之先继续吧。这样的话也不会浪费时间。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA01"),"True","img/MH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA028"
    麻寻 "「明白。那就各自预备。OK？」"
    stop music fadeout 132
    "麻寻话音未落，3个人一起点头回应。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA01"),"True","img/MH_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    voice "NYU09A_MA029"
    麻寻 "「３——２——１——GO～」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    play sound "SE07_07"
    pause (32/32.0)
#CHR_INIC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBB01"),"True","img/YU_XBB01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    志雄 "「志雄和……！」"
    voice "NYU09A_YU039_K"
    结乃 "「结乃的！」"
    voice "NYU09A_YU040_K"
    結乃・志雄 "「为您带来的，暂时没考虑好叫什么的节目！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBB02"),"True","img/YU_XBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "OBGM02"
    voice "NYU09A_YU041"
    结乃 "「开始了呢，塚本同学。」"
    志雄 "「开始了哦，春日同学。」"
    "没有名字就这样开始了。"
    "由于这样哗啦呼啦地喊出了标题，我和结乃都拼命地忍住笑。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBA01"),"True","img/YU_XBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU042"
    结乃 "「那么就让我们快一点，来给这个节目的主要内容做个说明吧。」"
    志雄 "「请言简意赅哦，毕竟我们只有１０分钟的时间呢。」"
    "两个人你一句我一句，照着结乃整理的剧本进行着节目。"
    "虽说是剧本，其实也就是一开始的对话、之后读投稿的部分，以及读后的感想，就完全靠即兴发挥了。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAB04"),"True","img/MH_MAB04A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    "亨和麻寻虽然有些显得手忙脚乱，但也都在做好自己的工作。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBB01"),"True","img/YU_XBB01A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    "结乃则显得游刃有余，看来平时在广播部就一直很活跃的她，现在更是驾轻就熟。"
    "然后在最后，说道我的话……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBB02"),"True","img/YU_XBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU043A"
    结乃 "「然后是今天为您主持的——」"
    志雄 "「塚本志雄和——」"
    voice "NYU09A_YU043B"
    结乃 "「春日结乃。」"
    voice "NYU09A_YU044"
    结乃 "「Ｓｅｅ　ｙｏｕ　ｎｅｘｔ　ｔｉｍｅ．　拜～拜♪」"
    window hide
    stop music fadeout 132
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA02"),"True","img/MH_MAA02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    voice "NYU09A_MA030"
    麻寻 "「好，OK。终于完结了啊~」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA04"),"True","img/TO_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM06"
    voice "NYU09A_TO026"
    亨 "「志雄！你怎么老是卡壳啊！」"
    志雄 "「嗯，在这件事上真的给大家带来了很大的麻烦……」"
    "我才发现自己紧张的时候就容易说话卡壳，中断了好几次。"
    "结果害麻寻中断录音了好几次。"
    "真的很抱歉。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA01"),"True","img/MH_MAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA031"
    麻寻 "「喂喂，亨君，那些小事就原谅他吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「麻寻，感谢。你真是个温柔的人～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA05"),"True","img/MH_MAA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA032"
    麻寻 "「志雄，你的声音挺好的。如果完全不卡壳就更好了。」"
    志雄 "「对不起呢~」"
    "我低下头抵着桌面，虽然只是１０分钟，但也算是筋疲力尽了。"
    "多亏了结乃优秀的表现，才能顺利地完成录音。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA04"),"True","img/YU_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "不过这么说来，结乃在麻寻说了ＯＫ后就一直就沉默着。"
    志雄 "「……结乃？」"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,YU_LXB05,3,F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB05"),"True","img/YU_LBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NYU09A_YU045"
    结乃 "「志雄学长！」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
#BG_PRI 3
    "还以为她呆住了，结果一喊名字，她就激动地跳了起来。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB02"),"True","img/YU_LBB02A@2x.png") as lh0 zorder (20+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU046"
    结乃 "「学长，学长，学长！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 1,(320-192)
#CHR_POSC 2,(320+192)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA06"),"True","img/MH_MAA06A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    with dissolve
    志雄 "「噢哇，等等，那两个人在看着呢！」"
    "结乃抓住我的手开始欢蹦乱跳，费了我好大劲才稳住她。"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,YU_LXB05,3,F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB05"),"True","img/YU_LBB05A@2x.png") as lh0 zorder (20+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NYU09A_YU047"
    结乃 "「啊……对，对不起！」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
#BG_PRI 3
    "察觉到亨他们的视线，结乃也恢复了正常。"
    "松了一口气之后、结乃又一次牵起我的手。"
    window hide
#CHR_ERSWC 1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh0 zorder (20+0):
        ypos 0.0
    with dissolve
    "这次是冷静地，脸上浮出了平日的笑容……"
    voice "NYU09A_YU048"
    结乃 "「那个……真是不错啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB02"),"True","img/YU_LBB02A@2x.png") as lh0 zorder (20+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU049"
    结乃 "「非常有趣呢。」"
    志雄 "「嗯，我也是。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2,(320+192)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA01"),"True","img/MH_MAA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .8
    with dissolve
    voice "NYU09A_MA033"
    麻寻 "「两位同志。在你们亲热的时候打扰你们真是不好意思，是不是忘了标题待定的事情呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC05"),"True","img/YU_LBC05A@2x.png") as lh0 zorder (20+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU050"
    结乃 "「啊，是啊……我，兴奋的完全忘记了……怎么办……！」"
    志雄 "「啊，那样的话我呢，倒是有个方案……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB06"),"True","img/YU_LBB06A@2x.png") as lh0 zorder (20+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU051"
    结乃 "「！……真的吗？」"
    志雄 "「嗯。虽然一边在说的时候一边在想了，但还是不怎么容易想出来……结果……」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "我拿起桌子上面的签字笔，在复印纸的背面写上标题的名字。"
    志雄 "「就叫做『浜咲讯息』！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 0
#CHR_POSC 1,(320-192)
#CHR_POSC 2,(320+192)
#CHR_DSPTC 0,1,2,YU_MBA04,TO_MBA04,MH_MAA06
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA04"),"True","img/YU_MBA04A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA04"),"True","img/TO_MBA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA06"),"True","img/MH_MAA06A@2x.png") as lh2 zorder (10+0):
        ypos 0.0
        xcenter .8
    with dissolve
    voice "NYU09A_TO027"
    亨 "「很老套呢。」"
    voice "NYU09A_MA034"
    麻寻 "「很普通呢。」"
    voice "NYU09A_YU052"
    结乃 "「也的确是这样呢。」"
    "大家盯着我的视线如同冰雪一般寒冷。"
    志雄 "「所以我才说是想不出来好的啦。」"
    "我悲伤地辩解着……但是这个标题真的这么烂吗？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA01"),"True","img/YU_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU053"
    结乃 "「但是，感觉到有点朴素的美好呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA01"),"True","img/MH_MAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    voice "NYU09A_MA035"
    麻寻 "「还很容易被理解。」"
    voice "NYU09A_TO028"
    亨 "「反正也没有其他方案了。」"
    志雄 "「你们……」"
    "被这么一说，我反倒对这个名字产生了感情。"
    "之后大家那里也没有想到好的方案，由于时间已经不够，最后决定还是采用我的方案。"
    "不过，那名字有那么老套吗……"
    "也许是过于在意了，重新录音标题那段的时候，两次因为我情绪过导致低录音效果太差而重录。"
    "不过回过头来看，这下，我们的节目总算到了完成的一刻了……"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG02AA@2x.jpg" as bg0 zorder 0 with dissolve
    pause (32/32.0)
    scene expression "img/BG02AA@2x.jpg" as bg0 with dissolve
    play sound "SE01_10L"
    pause (16/32.0)
#FADE_IN 1
    play sound "SE05_15L"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA04"),"True","img/YU_LBA04A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAC02"),"True","img/MH_LAC02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    stop se
    voice "NYU09A_MA036"
    麻寻 "「志雄，现在几点了？」"
    志雄 "「又干这个又干那个的，已经过了4点啦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA04"),"True","img/MH_LAA04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA037"
    麻寻 "「不是吧，已经这么晚了？」"
    voice "NYU09A_YU054"
    结乃 "「截止时间真的快要到了呢。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAC02"),"True","img/MH_LAC02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA038"
    麻寻 "「赶快。万一没赶上时间就全白费了。」"
    window hide
    play sound "SE01_10L"
#FADE_OUT 1
    show expression "img/BG01AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG01AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    stop se
    "只要赶到浜咲ＦＭ所在的芦鹿岛站，那么，我们的工作可就算完结了。"
    voice "NYU09A_MA039"
    麻寻 "「亨君，能按时来这汇合吗？」"
    志雄 "「他也不是小孩子了……」"
    "亨骑着摩托车……『猫大人』应该会先来到车站吧。"
    play sound "SE08_01"
    "时间已经过了4点……虽然说是暑假，但感觉走向车站的人却比往常多很多，是错觉吗？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA06"),"True","img/MH_LAA06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA040"
    麻寻 "「我说，这到底什么回事？」"
    志雄 "「什么……？」"
    "不是错觉，车站的验票口前走出来很多人。"
    "从售票机前，到车站入口到处都是人，人，人。。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_SBB04"),"True","img/TO_SBB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO029"
    亨 "「喂，不好啦不好啦，不好啦！」"
    "发现了我们的亨，拨开人群的波浪向我们这边靠拢。"
    "看他非常慌张的样子……果然车站那里是发生了什么吗？"
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
#CHR_POSC 0
#CHR_POSC 1,(320-192)
#CHR_POSC 2,(320+192)
#CHR_DSPTC 0,1,2,YU_MBC02,TO_MBB04,MH_MAA06
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBC02"),"True","img/YU_MBC02A@2x.png") as lh0 zorder (10+2):
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh1 zorder (10+0):
        ypos 0.0
        xcenter .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA06"),"True","img/MH_MAA06A@2x.png") as lh2 zorder (10+0):
        ypos 0.0
        xcenter .8
    with dissolve
    "我们三人面面相觑，无助地等待着亨给我们带来的信息。"
    志雄 "「你说什么发生什么事不好了？」"
    if not persistent.dictlist[56] and persistent.show_dict:
        $persistent.dictlist[56]=True
        show screen dict_pop(i=56)
#DICT_FLG 19
#DICT_FLG 20
#DICT_FLG 21
#DICT_FLG 22
#DICT_FLG 23
#DICT_FLG 25
#DICT_FLG 27
#DICT_FLG 28
#DICT_FLG 31
#DICT_FLG 32
#DICT_FLG 36
#DICT_FLG 44
#DICT_FLG 45
    voice "NYU09A_TO030"
    亨 "「呼呼……前往芦鹿的电车，在交叉路口发生事故而停止运作。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBB06"),"True","img/YU_MBB06A@2x.png") as lh0 zorder (10+0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA04"),"True","img/MH_MAA04A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    志雄 "「什么！？」"
    window hide
    stop sound
    play music  "OBGM13"
    voice "NYU09A_TO031"
    亨 "「交叉路口那里有一辆卡车突然冲了进来……只是一起单独事故，貌似没有人受伤……」"
    志雄 "「那倒还好……什么时候能恢复？」"
    voice "NYU09A_TO032"
    亨 "「２，３个小时之内是没办法了，车站工作人员大喊着和我说的。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBC04"),"True","img/YU_MBC04A@2x.png") as lh0 zorder (10+0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAB03"),"True","img/MH_MAB03A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    "这怎么办！在这种时候，路口事故！？"
    "往车站内里一撇，涌向验票口的乘客们，正在向拿着扩声器的工作人员发难。"
    "仔细地听听不断重复播放的广播内容，和亨反馈的情报一样。"
    "怎么办……？距离截止还有1小时不到。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAC02"),"True","img/MH_MAC02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA041"
    麻寻 "「我去截出租车！」"
    window hide
    play sound "SE01_00B"
    hide lh2 with dissolve
    志雄 "「啊……麻寻！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA05"),"True","img/TO_MBA05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO033"
    亨 "「出租车吗。一定要截到啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBC03"),"True","img/YU_MBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    结乃 "「…………」"
#MESEX_A M_NOA,A_CH_YU,NYU09A_YU055,"【結乃】「…………」%K%P"
    志雄 "「没事的，结乃。一定赶得上的。」"
    voice "NYU09A_YU056"
    结乃 "「……是。」"
    "我把手轻轻地放在了露出了不安地眼神的结乃的头上，对她笑着。"
    "没一会儿，去找出租车的麻寻小跑着回来了。"
    "看见她那阴沉的表情……难道又发生了什么问题吗？"
    window hide
    play sound "SE01_01"
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2,(320+192),00
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAB03"),"True","img/MH_MAB03A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .8
    with dissolve
    stop sound
    voice "NYU09A_MA042"
    麻寻 "「……公路也不行，因为那个路口事故的影响，整个芦鹿岛地区都处于阻塞状态。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB05"),"True","img/TO_MBB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO034"
    亨 "「啊？怎么会这样……！」"
    志雄 "「电车不行，出租车也不行的话……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA05"),"True","img/YU_MBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU057"
    结乃 "「佐贺学长！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO035"
    亨 "「是，什么事？」"
    "低着脸的结乃抬起了头。她的眼神里闪着强有力的光辉。"
    voice "NYU09A_YU058"
    结乃 "「学长的摩托车的话就能穿过这个大阻塞，应该能直达浜咲ＦＭ的！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA04"),"True","img/MH_MAA04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    志雄 "「啊，是吗？」"
    "如果能乘上亨的爱车『猫大人』，5点之前应该有办法将带子送达。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO036"
    亨 "「但是我不知道广播局在哪啊！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAB04"),"True","img/MH_MAB04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    志雄 "「呃……是吗？」"
    voice "NYU09A_TO037"
    亨 "「但是，我认为志雄你们会知道的。」"
    志雄 "「我会告诉你怎么走的了，所以拜托了，去吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA03"),"True","img/TO_MBA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO038"
    亨 "「啊，不要，那个啊……我，对于没走过的路有些不安……」"
    voice "NYU09A_MA043"
    麻寻 "「……诶，这样下去可不行。」"
    voice "NYU09A_YU059"
    结乃 "「……那个。」"
    voice "NYU09A_TO039"
    亨 "「嗯？」"
    voice "NYU09A_YU060"
    结乃 "「那个……我来驾驶。请把『猫大人』借给我吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB04"),"True","img/TO_MBB04A@2x.png") as lh1 zorder (10+1)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA04"),"True","img/MH_MAA04A@2x.png") as lh2 zorder (10+2)
    志雄 "「诶？」"
    voice "NYU09A_TO040"
    亨 "「哦？」"
    voice "NYU09A_MA044"
    麻寻 "「诶诶诶？」"
#MES_SYNC2
    voice "NYU09A_MIX01"
    亨 "「你能驾驶吗？」"
    麻寻 "「你能驾驶吗？」"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,YU_MXB05,3,F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBB05"),"True","img/YU_MBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NYU09A_YU061"
    结乃 "「…………是。」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
#BG_PRI 3
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB01"),"True","img/TO_MBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO042"
    亨 "「啊，原来如此，怪不得之前的想法这么专业。」"
    voice "NYU09A_MA046"
    麻寻 "「呜哇，怎么就完全没有认识到过。志雄你知道这事吗？」"
    志雄 "「我也和你一样吃了一惊……」"
    "不仅吃了一惊，还完全没想象过。"
    "兴趣是广播，在广播部制作广播剧，将精力集中于学生会干事的工作上的结乃居然拿到了中型摩托车的驾驶执照？"
    "到底是什么时候……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA04"),"True","img/YU_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU062"
    结乃 "「……对不起，不应该对大家隐瞒的……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB02"),"True","img/TO_MBB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO043"
    亨 "「那好。要是结乃的话我就放心了。我的『猫大人』就托付给你了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA01"),"True","img/YU_MBA01A@2x.png") as lh0 zorder (10+0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA01"),"True","img/MH_MAA01A@2x.png") as lh2 zorder (10+2)
    "与我的冲击形成对比，亨却非常爽快地接受了结乃的要求，"
    "同是乘摩托的人，难道连所见都略同了吗？"
    voice "NYU09A_YU063"
    结乃 "「那个，『猫大人』在哪里停着呢？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBA01"),"True","img/TO_MBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO044"
    亨 "「哦，现在给你取去，稍等。」"
    window hide
    play sound "SE01_00B"
    hide lh1 with dissolve
    voice "NYU09A_MA047"
    麻寻 "「快去快回～」"
    voice "NYU09A_TO045"
    亨 "「哦~」"
    voice "NYU09A_MA048"
    麻寻 "「都变得慌慌张张的呢。是吧。」"
    "麻寻目送着亨，他再次拨开人群的波浪向车站跑去。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA05"),"True","img/YU_MBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#MESEX_A M_NOA,A_CH_YU,NYU09A_YU064,"【結乃】「…………」%K%P"
    "结乃也默然地往亨过去了的地方看去。"
    "……我呢，想要说些什么缓解一下气氛，但是事实再次证明，我真的很没有这种天赋。"
    志雄 "「你能骑摩托吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBA02"),"True","img/YU_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU065"
    结乃 "「什么……」"
    "结乃吐着舌头，不好意思地笑了。"
    "这么想来，结乃的运动神经确实比一般人要好，所以会开个摩托车也没什么不可思议的。"
    "我们在互相沟通，相互理解，本来觉得对对方的事情都知道得一清二楚了，其实知道得根本还不够……"
    voice "NYU09A_MA049"
    麻寻 "「喂，志雄君。能给我一下亨君的手机号码吗？」"
    志雄 "「诶？当然可以……怎么了？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_MAA02"),"True","img/MH_MAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA050"
    麻寻 "「呵呵。给我吧～♪」"
    window hide
    hide lh2 with dissolve
    "麻寻把亨的号码打进了手机里，给我们抛了一个媚眼，慌慌忙忙地走了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MBC01"),"True","img/YU_MBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「？」"
    voice "NYU09A_YU066"
    结乃 "「她想干什么？」"
    志雄 "「谁知道呢。」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "在麻寻回来之时，我们都陷入沉默。"
    "第一次觉得，时间的流逝是如此的煎熬。"
    play sound "SE06_35"
    "本来以为亨能很快回来的，但亨意料之外的过了很长时间后才现身。"
    window hide
    play sound "SE06_36"
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA01"),"True","img/TO_LBA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA01"),"True","img/MH_LAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    voice "NYU09A_TO046"
    亨 "「我把她带过来了，我的『猫大人』!」"
    志雄 "「你去了哪里啊？明明不就停在车站那方向吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA02"),"True","img/MH_LAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA051"
    麻寻 "「诶诶，好啦好啦。」"
    "究竟怎么了？"
    "为什么连麻寻也忽然帮起了亨？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB01"),"True","img/TO_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO047"
    亨 "「那么，结乃，拜托你了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU067"
    结乃 "「是。」"
    "结乃拿过亨的头盔，底气十足的回答道。"
    window hide
    hide lh1 with dissolve
    "今天这盛夏一般的天气，虽然担心就这样穿着非常轻便的服装乘着摩托车会有问题……但眼下也顾不了那么多了。"
    志雄 "「靠你了，结乃。」"
    voice "NYU09A_TO048"
    亨 "「你也是啊，志雄。」"
    "亨如此说道，并把另一个头盔推了给我。"
    志雄 "「诶？我也要？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA02"),"True","img/MH_LAA02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .8
    with dissolve
#MES_SYNC2
    voice "NYU09A_MIX02"
    亨 "「当然啦！」"
    麻寻 "「当然哟！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA01"),"True","img/MH_LAA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU09A_MA053"
    麻寻 "「能让结乃一个人去吗，这到底是谁和谁做的节目啊？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA01"),"True","img/TO_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_TO050"
    亨 "「就是这样。我为了拿这个备用头盔来，我还回了一趟家。」"
    志雄 "「啊……」"
    "恍然大悟。"
    "麻寻向我问亨的手机号码，就是为了让这家伙去拿头盔啊。"
    voice "NYU09A_YU068"
    结乃 "「佐贺学长……麻寻……」"
    voice "NYU09A_TO051"
    亨 "「去吧，志雄。除了你还有谁能承担此重任？」"
    "亨狠狠地拍了我的背脊一下。"
    "完全不知轻重的亨此刻却显得格外高大。"
    "麻寻也……一直守护着我们。"
    "在我和结乃制作的这个节目时，给予了最大的支援的这两位。"
    "他们直率的心意，暖暖的，流遍了我的全身。"
    志雄 "「真是的，拿你们没办法！」"
    "我认真地戴好了头盔，一跃坐在了结乃的身后。"
    voice "NYU09A_YU069"
    结乃 "「谢谢你们两位！」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB02"),"True","img/TO_LBB02A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA02"),"True","img/MH_LAA02A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    voice "NYU09A_TO052"
    亨 "「快去吧！啊，还有，别弄伤了我的『猫大人』啊志雄！」"
    志雄 "「为什么只对我忠告啊。」"
    voice "NYU09A_TO053"
    亨 "「必须的～！」"
    "可恶……对结乃说放心地交给她，对我却……亨到底是谁的朋友呐。"
    voice "NYU09A_MA054"
    麻寻 "「一路走好。」"
    play sound "SE06_32"
    voice "NYU09A_YU070"
    结乃 "「志雄学长，出发啦！」"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU09A")]=True
    show expression "img/EVN_YU09A@2x.jpg" as bg1 zorder 1 with dissolve
    play sound "SE06_48L"
    stop se
    pause (16/32.0)
#BG_SHOWC 3
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    志雄 "「哦……呜哦！？」"
    "结乃完全不顾正常加速的法则，便急忙地起动了『猫大人』。"
    "身体因此大幅度后仰的我，拼命地抱紧了结乃的腰！"
    voice "NYU09A_YU071"
    结乃 "「要是觉得不舒服的话抓紧我就好！」"
    "结乃一边全力加速一边大喊着，可惜在混乱中的我却什么都听不到。"
    "在这飞驰的空间里，『猫大人』穿过了车站人群的堵塞，跃上了大马路。"
    志雄 "（喂！请遵守交通规则啊！）"
    "不过毕竟是可爱的结乃，肯定有遵纪守法地驾驶的吧。"
    "只是还没习惯摩托车的冲力。嗯，别说摩托车，就连电动自行车的驾照都没有的我完全不会习惯吧。"
    voice "NYU09A_YU072"
    结乃 "「要飞起来了！」"
    "刚听见一声喊叫，『猫大人』又再次加速了！"
    志雄 "「这个速度，和铃小姐的有得一拼啊……！！！！！！」"
    "『猫大人』以这路段超速定义的临界速度，沿着芦鹿电车沿线疾驰！"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
#BG_ALPC 1
    show expression "img/BG102AA@2x.jpg" as bg0 zorder 0 with dissolve
    pause (32/32.0)
#SE_VOLC 1,255
#FADE_IN 1
    if not persistent.dictlist[33] and persistent.show_dict:
        $persistent.dictlist[33]=True
        show screen dict_pop(i=33)
#DICT_FLG 34
    "可以想象……现在的『猫大人』肯定是以用肉眼跟不上的速度跨过嘉神川。"
    "飞驰到这里，堵塞的道路也渐渐的宽敞了起来。"
    window hide
#BG_SHOWC 3
    "绕过阻塞的路段前进，结乃驾驶着的『猫大人』以良好的速度走过了海岸线，穿过了浜咲。"
    志雄 "「浜咲FM在哪里呢！？」"
    "看起来我也没什么资格嘲讽亨的路痴……"
    "我其实也不是很清楚ＦＭ的所在地点。只知道是靠近芦鹿岛附近……"
    "虽然在电车里见过几次……但，现在在摩托车的后座上看，街景完全是另一番世界，所以完全搞不懂这是哪里。"
    voice "NYU09A_YU073"
    结乃 "「已经在眼前了！学长，还有多少时间！」"
    "听见前排结乃的声音，我立刻拿出手机确认时间。"
    "同时我也要为不被摔下去拼命努力着，貌似结乃也察觉到了这一点而将速度放慢了下来。"
    志雄 "「57分了！赶快！」"
    "片刻的减速在我说完后就结束了，结乃再次全速驾驶。"
    "我把头探过结乃的背后，往前进方向偷看了一下。"
    "沿着海岸的车道上，大块的浜咲ＦＭ的广告板隐约可见。"
    "随着距离的推进，广告板的内容逐渐清晰了起来！"
    voice "NYU09A_YU074"
    结乃 "「虽然有点乱来！请将身体重心，侧向内侧!」"
    志雄 "「不，别蛮干啊！」"
    "结乃将『猫大人』的车身几乎水平地放倒着，往浜咲FM广告版的下方拐了一个接近90度的弯！"
    志雄 "「都说了不要蛮干！哇！！」"
    "有一瞬间，感觉到后轮貌似打滑了，是错觉吗？"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG29AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG29AA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
#FADE_IN 1
    "几乎是横着滑进浜咲ＦＭ的『猫大人』恢复了垂直，始终保持那样的速度直奔停车场。"
    志雄 "「好危险，感觉脸都要擦到地了。」"
    "终于到达了，我如释重负。"
    "以后如果还有机会和结乃两人同乘摩托的时候，一定要非常小心……不，我还是自己去考一个驾照比较好吧……？"
    "想的有些远了……"
    志雄 "「５８分！总算赶上了！」"
    voice "NYU09A_YU075"
    结乃 "「太好了！」"
    play sound "SE09_33"
    野良猫 "「喵！」"
    stop se
    "！"
    "正在我们欢呼雀跃的时候，一只白色斑纹的猫忽然出现在了『猫大人』的轮子前方！"
    voice "NYU09A_YU076"
    结乃 "「危险！」"
    play sound "SE06_36"
    志雄 "「——啊！！！！！！」"
    "『猫大人』失去了平衡。"
    "我像是被从车上抛了出去，周围的景色天旋地转。"
    window hide
#BG_PRIC 0
#EFF_PRI 0
#BG_INIC 2
    show expression "img/NIMG01B@2x.png" as bg2 zorder 2
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
#EFF_STAC 0,CLOUD_B,EFF_SKIP
#BG_ALP_AUTOC 0,0,0,1
#ROUTINE_STA
#BG_SWPC 0
    scene expression "img/BG29AA@2x.jpg" as bg0 with dissolve
#BG_ALPC 0
#BG_ALPC 2
#BG_PRIC 0
#EFF_PRI 0
#ROUTINE_STP
#VIB_DOKA 
##QUA_ALL 
#VIB_STP 
    with vpunch
    "鼻尖擦过沥青路面，背部则重重地撞上了地面。"
    志雄 "「喔喔喔……好痛……」"
    "我拼命地忍住疼痛……！"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBC03"),"True","img/YU_XBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "好一段时间才反应过来，有个貌似在哪里见过的女生压在我的身上。"
    voice "NYU09A_YU077"
    结乃 "「对不起，学长。」"
    "是结乃……！看起来我的记忆有些混乱，一瞬间无法理解了吧。"
    志雄 "「结乃，没有受伤吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBA04"),"True","img/YU_XBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU078"
    结乃 "「是，还算安好……」"
    "虽然觉得结乃与『猫大人』的命运并不会比我好，但不知道为什么她一点事情都没有……"
    "这就是运动神经的差别……？"
    play sound "SE09_34"
    野良猫"「呜喵～呜。」"
    stop se
    "白色斑纹的猫扬起鼻尖像是在笑着，把屁股和尾巴对着我们。"
    "优雅地步行着，消失在茂密的矮树丛中。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBA01"),"True","img/YU_XBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU079"
    结乃 "「小猫也好像没有事呢。」"
    志雄 "「那就好了……啊，比起这个，受理处！」"
    "幸运的是结乃没有受伤，要是把原本的目的忘了就完蛋了。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBB06"),"True","img/YU_XBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU080"
    结乃 "「啊……是啊！学长，时间是？」"
    志雄 "「正好5点！结乃，快点去吧。」"
    "我现在还痛得不行，要等我的话就肯定赶不上了。"
    "现在只能让结乃完成最后的冲刺了！"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_XBA05"),"True","img/YU_XBA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU081"
    结乃 "「是！！」"
    window hide
    play sound "SE01_00B"
    hide lh0 with dissolve
    pause (32/32.0)
    stop music fadeout 132
    "……。"
    "…………。"
    "……………………。"
    "大概１分钟左右，一边听着结乃的脚步声渐远，一边等待我的背部疼痛消失。"
    show expression "img/BG29AA@2x.jpg" as bg_over zorder 2 with dissolve
#EFF_STPC 0,EFF_NOSKIP
    "想办法要动起来……这么想着站了起来，但果然与地面亲密接触的地方还是痛。"
    "每次向前踏步，身体里就仿佛有电流在游走一样。我一瘸一拐地广播局的大门走去。"
    "距离我摔倒的地方数米处横躺着『猫大人』。"
    "诡异的刹车痕上，还有车身与沥青路面相刮所留下的白色油漆。"
    "亨……对不起了。"
    "背对着『猫大人』，我再次向大门开始走去。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_SBC01"),"True","img/YU_SBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "终于在自动门前看到了结乃的背影。"
    "在她面向的应该是广播局的工作人员吧？"
    "给人的感觉是一位中年大叔。"
    voice "NYU09A_YU082"
    结乃 "「拜托您了！」"
    "结乃深深地向工作人员低头鞠躬。"
    志雄 "「结乃……」"
    "我忍着痛，一边跑向两人所在的地方。"
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
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC04"),"True","img/YU_LBC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「赶不上时间吗？」"
    voice "NYU09A_YU083"
    结乃 "「学长……」"
    "结乃又这样了。"
    "我看着她的眼睛，大滴大滴的泪水溢了出来。"
    志雄 "「不肯收吗！？」"
    "结乃抱住想要过去追问工作人员的我，想要挽留住我。"
    voice "NYU09A_YU084"
    结乃 "「学长，已经，没关系了。没事了。」"
    志雄 "「怎么会没关系，绝对会让他受理我们的作品！」"
    "带着从肚子里涌上来的怒火，就此走向工作人员追问。"
    "但是，工作人员大叔摆出不明就里的表情。"
    voice "NYU09A_XV000"
    工作人員 "「不，我们收下了啊？」"
    志雄 "「诶？」"
    "那么……？"
    "眼前的状况真是叫我愕然了。"
    "如果已经受理了的话，刚才结乃的眼泪是怎么回事？"
    voice "NYU09A_XV001"
    工作人員 "「是你太着急啦，虽然迟了一分钟，但是毕竟是直接送来的，我们怎么可能会不收呢。」"
    voice "NYU09A_YU085"
    结乃 "「是的。很郑重地收下了……」"
    志雄 "「什么嘛，我还以为那样的表情一定是！」"
    voice "NYU09A_YU086"
    结乃 "「很抱歉，我一时激动得忘神了……」"
    window hide
    play music  "OBGM11"
    "结乃的脸颊零落地流下泪水。"
    "这应该是喜悦和安心的泪水吧。"
    "真是让人怜爱的女孩呐……"
    "我用手指轻触结乃的脸颊，慢慢地替她拭去泪水。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA06"),"True","img/YU_LBA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "结乃猛地握住了我的手，认真地抬起头。"
    "在她脸上的是，真正安心的，让人看起来觉得纯洁无比的笑容。"
    志雄 "「我们成功了，结乃。」"
    "举起手掌。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB02"),"True","img/YU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU087"
    结乃 "「是！」"
    play sound "SE03_06"
    "结乃也同样伸出了手掌，我们满意地互相击掌。"
    "之后要做的，就是耐心等待选拔结果了。"
    "我们的波澜万丈的节目制作，终于告一段落了。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
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
    "……………………。"
    window hide
#FADE_OUT 0
#BG_COLC 0,128,128,128
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play music  "BGM10"
#FADE_IN 1
    voice "NYU09A_XV002"
    工作人員 "「好像发生了什么了不得的事情，你们从哪里来的？」"
    志雄 "「诶？我们从澄空……」"
    voice "NYU09A_YU088"
    结乃 "「我们是澄空学院的学生。」"
    voice "NYU09A_XV003"
    工作人員 "「诶～那么远的地方赶过来吗……那样的话邮寄也可以的啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB06"),"True","img/YU_LBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    stop music fadeout 132
    志雄 "「……哈？」"
    voice "NYU09A_YU089"
    结乃 "「……邮寄……？」"
    voice "NYU09A_XV004"
    工作人員 "「只是邮戳是今天的就行了，征集通知里应该有写的。」"
    志雄 "「…………」"
#MESEX_A M_NOA,A_CH_YU,NYU09A_YU090,"【結乃】「…………」%K%P"
    voice "NYU09A_XV005"
    工作人員 "「虽然５点钟事务所就会关门，但里面一般都有人２４小时值守的，所以到了５点整也不用这么焦急啊。」"
    志雄 "「……是，原来如此。」"
    voice "NYU09A_YU091"
    结乃 "「是这样的……」"
    voice "NYU09A_XV006"
    工作人員 "「总之我们将你们的节目收存保管了哦。期待你们的表现。就这样吧！」"
    志雄 "「…………」"
#MESEX_A M_NOA,A_CH_YU,NYU09A_YU092,"【結乃】「…………」%K%P"
    "…………。"
    "略带尴尬的无语状态……"
    "在大门前呆呆地站立了一会，不久后结乃嘟囔了一句。"
    voice "NYU09A_YU093"
    结乃 "「回去吧……」"
    志雄 "「是啊。」"
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/NIMG01B@2x.png" as bg1 zorder 1
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
#EFF_STAC 0,CLOUD_B,EFF_SKIP
    play sound "SE01_12L"
    play music  "BGM13"
#FADE_IN 1
    志雄 "「车子，没问题吧。」"
    voice "NYU09A_YU094"
    结乃 "「方向有些往右边偏了……」"
    志雄 "「『猫大人』……光荣牺牲了呢。」"
    voice "NYU09A_YU095"
    结乃 "「我说，一起去向佐贺学长道歉吧？」"
    志雄 "「别担心。那家伙的话一定会笑着原谅我们的。」"
    voice "NYU09A_YU096"
    结乃 "「会那样的吗……」"
    志雄 "「啊，是酪萨克。要顺便去看看吗？」"
    voice "NYU09A_YU097"
    结乃 "「不行啦。」"
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
    show expression "img/BG14EA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG14EA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    play sound "SE05_13L"
#FADE_IN 1
    "我打电话让亨到我的房间前等，然后让结乃开过去。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC05"),"True","img/YU_LBC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU09A_YU098"
    结乃 "「啊，是佐贺学长……怎么办？」"
    "在前面的路口，亨正向这边挥手。"
    志雄 "「……怎么办呢？」"
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
#CHR_POSC 0,20
#CHR_COLC 0,128,120,112
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_SBB02"),"True","img/TO_SBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "我们慢慢地走近，连亨的表情都仿佛变得清晰可见。"
    "当然，我们这边的情况对面也应该看得很清楚了……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MBB05"),"True","img/TO_MBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "亨挥舞的双手逐渐停了下来……表情也越来越青了。"
    "最后变成惨叫……"
    voice "NYU09A_TO054"
    亨 "「『猫——大——人——』！」"
    window hide
#ROUTINE_STA
#BG_PRIC 0
#EFF_PRI 0
#BG_INIC 2
    show expression "img/NIMG01C@2x.png" as bg2
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
#EFF_STAC 0,CLOUD_C,EFF_SKIP
#CHR_ALP_AUTOC 0,0,0,1
#BG_ALP_AUTOC 0,0,0,1
#ROUTINE_STP
#ROUTINE_STA
#BG_SWPC 0
#BG_ALPC 0
#BG_ALPC 2
#BG_PRIC 0
#EFF_PRI 0
#ROUTINE_STP
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "亨，真的很对不起啦。"
    "这样就真的，我们的录音节目的制作的事算是彻底『圆满』了……"
    "起码，从根本目的上来说……"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
#EFF_STPC 0,EFF_SKIP
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
