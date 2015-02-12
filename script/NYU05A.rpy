label NYU05A:
    $currentlabel = "NYU05A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '28'
    $date = '5'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 3,CAL_0728
    scene expression Solid("000") with fade
    show expression "img/NIMG15H-568h@2x.jpg" as cal zorder 5
    show expression "img/07_28_FRIDAY@2x.png" as cal_date zorder 6:
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
    show expression "img/BG01AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG01AA@2x.jpg" as bg0 with dissolve
    play music  "BGM10"
    play sound "SE08_18L"
#EFF_STAC 1,SUN_LE,EFF_SKIP
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
    "我鼓足干劲，拿着今天商讨所需的资料，向约好和结乃碰头的地方走去。"
    "忙了整整一夜，但现在却一点睡意都没有，反而神清气爽。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC03"),"True","img/YU_LCC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「早上好。」"
    voice "NYU05A_YU000"
    结乃 "「嗯，早上好……」"
    "是因为考虑广播的事，而没睡好么？"
    "明明是早上，结乃却没什么精神。"
    志雄 "「因为今天想打起干劲来商量，就不要去酪萨克了。」"
    "没有麻寻的干扰，效率应该会直线提升。"
    "当然，也考虑到要待上很长时间，选择快餐店反而会变得不方便。"
    志雄 "「有什么推荐的咖啡馆么？」"
    "身为学生的话，进入咖啡馆本身就是难度挺大的一件事。"
    "与我相比，结乃对这种店应该比较了解，所以问问她好了……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC01"),"True","img/YU_LCC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU001"
    结乃 "「那个……对不起，刚才在说什么？」"
    志雄 "「没有，算了，没什么。」"
    "果然是还没睡醒啊。"
    "结乃没听清我说话倒是很少见的。"
    "不管怎么说，还是先找个地方休息比较好。"
    志雄 "「这里……貌似离第一次去和神奈见面的咖啡馆很近呢。」"
    window hide
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB06"),"True","img/YU_LCB06A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    结乃 "「……！」"
#QUA2_CHR 0
#MESEX_A M_NOA,A_CH_YU,NYU05A_YU002,"【結乃】「……！」%K%P"
    "突然，结乃晃了一下，差点跌倒在地。"
    志雄 "「哦？站着就睡着了么？真的没事吗？」"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,YU_LXB05,3,F24
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB05"),"True","img/YU_LCB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NYU05A_YU003"
    结乃 "「没，没事。对不起，咖啡馆对吧。」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
#BG_PRI 3
    "结乃还有些没回过神，脸上的笑容充满疲惫。"
    "是因为被看到开小差的样子而害羞么，她的侧脸微有点红。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB04"),"True","img/YU_LCB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU004"
    结乃 "「比起那里，我有推荐的咖啡馆，要去吗？」"
    志雄 "「是么？嗯，哪里都行，亨大概会骑摩托车过来，所以稍微远点也没关系。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB01"),"True","img/YU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU005"
    结乃 "「没关系的，车站那边有很多家。」"
    window hide
    play sound "SE01_04L"
#SE_VOLC 0,96
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "结乃快速的迈出脚步。"
    "到底怎么了……？"
    "隐隐觉得她刚才眼神有些不对，是我多心了么？"
    志雄 "「喂，等我一下啊。」"
    window hide
    play sound "SE01_04L"
    "这种事还是闲下来再考虑吧，现在要赶紧去追已经和我拉开了距离的结乃。"
    "结乃的运动神经很发达，稍微一放松就会跟丢了。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1
#EFF_STPC 1,EFF_SKIP
    scene expression Solid("000") with fade
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG05AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG05AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC05"),"True","img/YU_LCC05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE05_15L"
#FADE_IN 1
    志雄 "「真是没办法，一到暑假，哪里都拥挤的不像话。」"
    voice "NYU05A_YU006"
    结乃 "「嗯……」"
    "从碰头的时候开始，结乃看上去就不太舒服，而这种状态随着时间的推移也越发的明显。"
    "当然，要去的咖啡馆全都客满，会变成这样也能够理解了。"
    "在火热的太阳下，为了寻找咖啡店而走到精疲力尽也真是无奈……我这么想着。"
    志雄 "（这么说来……）"
    "我想起了放在包里的东西。"
    志雄 "「那个，之前我有拿到酪萨克的优惠劵，截止日期刚好是今天。」"
    志雄 "「就算算上电车费，也是划得来的，怎么样？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC01"),"True","img/YU_LCC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU007"
    结乃 "「啊……这样吗，其实我也带着。」"
    "真是造化弄人"
    "完全找不到落脚地方的我们，只好妥协了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC03"),"True","img/YU_LCC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU008"
    结乃 "「早知道是这样的话，一开始就选定酪萨克不就好了……」"
    "话中带着刺人的尖刺。"
    "这样的状态，在暑假开始的时候也有过一次。"
    "眼前的她，和那时因为『同居未遂』而抱着忧郁心情的身影相重合。"
    "有想和我说却无法开口的事情……这种时候，结乃就会露出这样的表情。"
    志雄 "「那个，结乃。虽然不知道是什么事情困扰着你，方便的话可以和我说吗？」"
    "知道导致结乃这样的原因的话，就算是误会也能想办法化解。"
    "如果真是我做错了什么，我会反省并道歉。"
    "但如果一直保持着沉默的状态，那什么也解决不了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB03"),"True","img/YU_LCB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU009"
    结乃 "「没事的，请不要在意。」"
    "就算如此……"
    "结乃还是很明显地在刻意躲避着什么。"
    志雄 "「你就这么不信任我么……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB01"),"True","img/YU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU010"
    结乃 "「别乱想了，什么都没有，快点去酪萨克吧。」"
    "虽然知道笑容是勉强做出的……"
    "作为想要真诚守护她的我，心痛是肯定的吧。"
    window hide
    stop sound
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
    scene expression "img/BG35AA@2x.jpg" as bg0
#BG_SET_DEFC 0,BG35AA
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC01"),"True","img/YU_LCC01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (32/32.0)
    play music  "OBGM12"
#EFF_STAC 1,SUN_LE,EFF_SKIP
#FADE_IN 1
    志雄 "「什么嘛，是那件事啊。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC02"),"True","img/YU_LCC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU011"
    结乃 "「不是什么“那件事”！对我来说这是很重要的事情。」"
    "在去酪萨克的路上，我反复的设法询问，终于问出了结乃不高兴的理由。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC03"),"True","img/YU_LCC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU012"
    结乃 "「这个广播，明明是为了丰富我们两人的回忆而去制作的……」"
    "前些日子，神奈好像告诉了结乃我找她一起来参加广播制作的事。"
    "而结乃对此貌似非常在意。"
    志雄 "「当然是这样，不过没必要执著于只由我们两个人来完成吧……」"
    "已经请亨来帮忙了。"
    "箱崎同学也是，必要的话，应该会来帮忙的。"
    志雄 "「就因为是我和结乃回忆的结晶……所以想要让关系深刻的人来参加，难道这样错了么？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB03"),"True","img/YU_LCB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU013"
    结乃 "「因为学长太过温柔了。」"
    "本以为会遭到强烈的反驳，但结乃带着寂寞的笑脸，给出了意料之外的回答。"
    voice "NYU05A_YU014"
    结乃 "「对周围所有人都很重视，从来不带偏见的去接纳。」"
    voice "NYU05A_YU015"
    结乃 "「虽然明知道没有什么，但有些时候还是会感到不安。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC05"),"True","img/YU_LCC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU016"
    结乃 "「我明明……想要一直是志雄学长心中的唯一……」"
    志雄 "「结乃……」"
    "看着结乃那看上去快要哭出来的笑脸，我好想紧紧地抱住她。"
    "比起用语言传达……身体有时更能表明心迹。"
    stop music fadeout 132
    play sound "SE09_31"
    ＴＯＭＯＹＡ"「汪！ 汪！」"
    stop se
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "就在我的手即将碰到结乃肩膀的瞬间，突入其来的狗叫声打乱了节奏。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA04"),"True","img/MH_LAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    if not persistent.dictlist[58] and persistent.show_dict:
        $persistent.dictlist[58]=True
        show screen dict_pop(i=58)
    voice "NYU05A_MA000"
    麻寻 "「喂，ＴＯＭＯＹＡ！不老实点的话……」"
    志雄 "「麻、麻寻小姐！」"
    window hide
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAB04"),"True","img/MH_LAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM07"
    voice "NYU05A_MA001"
    麻寻 "「看吧，被发现了吧……」"
    "带着狗散步的麻寻，就站在离我们不远的地方。"
    "这么说……刚才我们的样子肯定都被她看在眼里了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA02"),"True","img/MH_LAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_MA002"
    麻寻 "「不要在意我，就当作我是空气好了，请吧请吧。」"
    志雄 "「什么也没有啊……我们不会做那种事情的，对吧，结乃？」"
    "我无奈地叹着气，向结乃征求同意。"
    voice "NYU05A_YU017"
    结乃 "「是，是这样的。」"
    "是因为害羞么，结乃像是要躲着麻寻一样藏在我身后。"
    "这也没有办法的吧，总之还是快点改变话题的好。"
    志雄 "「那个，今天休息么？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAB04"),"True","img/MH_LAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_MA003"
    麻寻 "「嗯，明明你们难得过来，对不起了哦。」"
    志雄 "（这样反而更好了。）"
    "看来今天能安心地在酪萨克谈话了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA01"),"True","img/MH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_MA004"
    麻寻 "「难得有时间，所以就带着朋友的狗出来散步了。」"
    志雄 "「朋友……是男朋友么？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA05"),"True","img/MH_LAA05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_MA005"
    麻寻 "「不，怎么会呢。」"
    "不用思考，否定就脱口而出。"
    "虽然是能够知道麻寻小秘密的宝贵机会，不过，看起来想套话也并不容易。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/NIMG11A@2x.jpg" as bg1 zorder 30 with dissolve
    志雄 "（嗯？ＴＯＭＯＹＡ，ＴＯＭＯＹＡ……）"
    "总感觉好像在哪听到过。"
    志雄 "（啊啊啊！那个！和稻穗并列，澄空学园传说中的黑名单里的一人的绰号！！）"
    "居然被取上和那个人一样的名字……"
    "光是这点，就感到面前的狗非常可悲。"
    志雄 "「好可爱，是吧，结乃？」"
    voice "NYU05A_YU018"
    结乃 "「嗯，是这样的呢……」"
    window hide
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA03"),"True","img/MH_LAA03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    hide bg1 with dissolve
    voice "NYU05A_MA006"
    麻寻 "「不用勉强哦，这家伙一脸呆样。」"
    "面对不能无法真心说出赞美的我们，麻寻并不介意，反而笑了起来。"
    voice "NYU05A_MA007"
    麻寻 "「但是，相处久了的话，就会感到离不开它了呢，真是个亲近人的孩子。」"
    志雄 "「看起来是这样呢……」"
    "从毫不客气的在我脚边打转这点来看，这狗不怎么认生。"
    "有了感情的话……就像自己的孩子一样，自然就觉得可爱了。"
    play sound "SE09_32"
    ＴＯＭＯＹＡ "「呜——」"
    stop se
    "不知是不是对我不感兴趣了，ＴＯＭＯＹＡ往躲在我身后的结乃那边走去。"
    voice "NYU05A_YU019"
    结乃 "「呃！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA06"),"True","img/MH_LAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "结乃的反应意外的激烈。"
    "她用力地抓住我的肩膀，闭上眼不去看ＴＯＭＯＹＡ。"
    志雄 "「难道说……结乃害怕狗么？」"
    "虽然我对狗的种类并不是很了解，不过害怕一只普通大小的家养狗我还是挺意外的。"
    "她给人的印象应该是那种喜欢小动物的吧。"
    voice "NYU05A_YU020"
    结乃 "「别胡说！我以前有养过猫的，没理由会害怕狗吧！」"
    "就算养过猫，也不能成为不怕狗的理由吧……"
    "不管怎么说，结乃确实对狗有着恐惧。"
    "我为了打消结乃的不安，我抱住她细小的肩膀。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'MH'",DynamicDisplayable(mouthanime,"MH_LAA01"),"True","img/MH_LAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「麻寻，你看……」"
    voice "NYU05A_MA008"
    麻寻 "「嗯，对不起呢。那么，我回去咯。」"
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
    "本想用狗来捉弄一下结乃，逗她开心的，谁知被麻寻一下子牵了回去。"
    "说不定她是在对刚才偷看被发现的事存有罪恶感。"
    志雄 "「已经没事了哦。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC03"),"True","img/YU_LCC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "BGM06"
    voice "NYU05A_YU021"
    结乃 "「呼……」"
    "已经几乎要虚脱的结乃，长出了一口气。"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,YU_LXB05,3,F24
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB05"),"True","img/YU_LCB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NYU05A_YU022"
    结乃 "「啊……」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
#BG_PRI 3
    "平静下来的结乃好像才发现我抱着她的肩膀，脸一下子又红了起来。"
    志雄 "「抱歉，让你感到不安了。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB03"),"True","img/YU_LCB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU023"
    结乃 "「是，是……我才是，没理由地乱吃醋。真对不起。」"
    "在我的臂弯里，紧张着的结乃慢慢放松下来。"
    "多亏了意外的情况，不用去在意本应害羞的行为和话语。"
    "我的心意，确确实实传达到结乃的心中。"
    志雄 "（也要好好感谢麻寻和ＴＯＭＯＹＡ呢。）"
    "知道了结乃害怕狗这件事，也看到了结乃可爱的另一面……"
    "第一次，从心底里感谢麻寻了。"
    window hide
    stop sound
    stop music fadeout 1
#FADE_OUT 1
#EFF_STPC 0,1,EFF_SKIP
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 1
#BG_SETWC 0,1,EXBG01A,BG36AA
    scene expression "img/EXBG01A@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    play music  "OBGM12"
#FADE_IN 1
    "稻穗去了温泉旅馆兼职，麻寻又休息。"
    "今天谁也不会来打扰我们，应该能够顺利进行广播的商讨吧。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZCC02"),"True","img/YU_ZCC02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    hide bg1 with dissolve
    志雄 "「不，不是那样的吧。」"
    voice "NYU05A_YU024"
    结乃 "「学长才是，完全没有明白呢。」"
    "但是，我们的很多意见出乎意料的相左，讨论几乎没有进展。"
    "好不容易借助ＴＯＭＯＹＡ消除的那份尴尬，又一次浮现在双方的脸上。"
    志雄 "「所以说，广播不就是和听众的互相交流么？」"
    "作为接触过很多Ｔ－ｗａｖｅ这类参与型广播的我，在这点上无法让步的。"
    "本想结乃也应该是这样想的，但是她的反驳却相当打击我。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZCC03"),"True","img/YU_ZCC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU025"
    结乃 "「从效果上来说，这点自然是最重要的，但是，要和听众接触需要一定的时间。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZCC02"),"True","img/YU_ZCC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU026"
    结乃 "「为了整体质量，节目必须以主持人为中心。话题要将地区的特色全部用上才对。」"
    "结乃有条不紊地说出意见。"
    "神奈也提过相同的看法，如果想要取得好的结果，就必须要做出一定的妥协。"
    "我也明白，为了达到自己的目标，取得优胜是必要的前置条件。"
    志雄 "「但是，这样的节目还有意思么？」"
    voice "NYU05A_YU027"
    结乃 "「毕竟是比赛，一定程度的妥协是必要的吧？」"
    "明知结乃的主张是正确的，但是，有些东西实在难以接受。"
    志雄 "「这次比赛，是为了制作出我们二人的回忆才去参加的吧。」"
    "正因如此，为了能做出可以成为回忆的节目……才想要将广播制作成类似Ｔ－ｗａｖｅ样式的。"
    "就算是不好的结果，两个人努力的结晶，也已经融于广播之中。"
    "我认为这才是比任何东西都重要的。"
    志雄 "「虽然结果是很重要，但是过于追求的话，不就错过了制作广播的真正乐趣么？」"
    "结乃和我相同的广播爱好。"
    "如果将此舍弃的话，就失去了参加这个活动的意义了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZCC04"),"True","img/YU_ZCC04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU028"
    结乃 "「没有那回事！说得好像我的节目完全没意思一样！」"
    志雄 "「没，并没有那样说吧。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZCB03"),"True","img/YU_ZCB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU029"
    结乃 "「而且，参与的话就要留下好结果这句话不是学长说的么！」"
    "……结果又回到了原点。"
    "看重过程的我，和看重结果的结乃。"
    "各执己见的我们，就像永远不相交的平行线。"
    window hide
#FADE_OUT 1
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZCC05"),"True","img/YU_ZCC05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    pause (32/32.0)
#FADE_IN 1
    志雄 "「……」"
    结乃 "「……」"
#MESEX_A M_NOA,A_CH_YU,NYU05A_YU030,"【結乃】「……」%K%P"
    "想说的话基本上都说完了。"
    "即使如此，我们都没有改变意见。不知何时，两人都开始沉默不语。"
    "如果要打破这个状况，必须要有第三者的介入……"
    "惟独今天，不会有随随便便就来插话的麻寻。"
    "明明一个开始就不希望出现的人，现在却如此渴望她的存在。"
    志雄 "（这样的话，只能寄希望于那家伙了。）"
    "我一边耐心的喝着可乐消磨时间，一边等待着救世主的出现。"
    stop music fadeout 132
    play sound "SE06_34"
    志雄 "「哈……」"
    "没有听错，熟悉的摩托车引擎声。"
    "这个声音听上去就像是援军吹起的号角一般。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZCB03"),"True","img/YU_ZCB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU031"
    结乃 "「是……亨学长吧？」"
    志雄 "「嗯，果然是骑摩托车过来啊。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZCB01"),"True","img/YU_ZCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU032"
    结乃 "「亨学长真的很喜欢摩托车呢，很不容易才得到家人的允许吧。」"
    志雄 "「不过呢，明明都是备考生了，还到处骑车兜风不上补习班。这时候一心只想玩再怎么说也不太好吧。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZCA02"),"True","img/YU_ZCA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU033B"
    结乃 "「ＴＷ２２５型摩托，不仅能将车胎换粗，而且还能做各种各样的改造，真是会挑呢。」"
    志雄 "「呃，了解的好详细……」"
    "虽然结乃只看到过几次，但不仅是车钟，连其特征都很了解……"
    "其实，那家伙的摩托车是什么车种我也是结乃说后才知道，真是作为朋友的失职啊。"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,YU_ZXB05,3,F24
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_ZCB05"),"True","img/YU_ZCB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NYU05A_YU034"
    结乃 "「有调查过的哦，因为亨学长老是向我炫耀啊。」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
#BG_PRI 3
    志雄 "「连结乃也……那家伙真的是没完没了呢。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_INIC 2
#CHR_ALPC 1
#CHR_ALPC 2
#CHR_POSC 1,(320-160)
#CHR_POSC 2,(320+160)
    show expression "img/BG07AA3@2x.jpg" as bg2 zorder 20
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh1 zorder (100+1):
        xcenter .25
        ypos 0.0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_MAB06"),"True","img/RI_MAB06A@2x.png") as lh2 zorder (100+2):
        xcenter .75
        ypos 0.0

#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
    
    with dissolve
    stop se
    stop sound
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 0
#CHR_ALPC 0
#CHR_ALPC 1
#CHR_ALPC 2
#BG_ALPC 2
#BG_UVC 2,160,60,480,336
#BG_BLUR 2
    hide bg1 with dissolve
    "关于摩托车，莉莉丝都已经听得厌烦了。"
    window hide
    hide lh2 with dissolve
#CHR_SET_BACK
#CHR_INIC 2
#CHR_POSC 2,(320-160)-320
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAA03"),"True","img/TO_MAA03A@2x.png") as lh1 zorder (100+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAA01"),"True","img/CH_MAA01A@2x.png") as lh2 zorder (100+2):
        xcenter .75
#ROUTINE_STA

#BG_BLUR 2


#ROUTINE_STP
#BG_UV_SAVEC 2
#CHR_POS_SAVEC 1
#CHR_POS_SAVEC 2
    pause (16/32.0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh1 zorder (100+1):
        ypos 0.0
    with dissolve
    pause (32/32.0)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CH'",DynamicDisplayable(mouthanime,"CH_MAC02"),"True","img/CH_MAC02A@2x.png") as lh2 zorder (100+2):
        ypos 0.0
    with dissolve
    pause (32/32.0)
    hide lh2 with dissolve
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB05"),"True","img/TO_MAB05A@2x.png") as lh1 zorder (100+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_MAB06"),"True","img/YU_MAB06A@2x.png") as lh2 zorder (100+2):
        xcenter .75
    hide bg3 with dissolve
#BG_SET_BACK 
#BG_INIC 3
#BG_ALPC 3
    "当身边没有能够炫耀的对象时……"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_MAB02"),"True","img/TO_MAB02A@2x.png") as lh1 zorder (100+1):
        ypos 0.0
    with dissolve
#BG_SET_BACK
#BG_SHOWC 3
#BG_SET_BACK 
#BG_INIC 2
#BG_UVC 2,0,0,640,448
    show expression "img/BG08AA@2x.jpg" as bg2 zorder 20
    with dissolve
#CHR_ALPC 0
#CHR_ALPC 2
#CHR_POSC 1,(320-160)
    hide bg3 with dissolve
    extend "就把目标变为朋友的女友么……"
#MESX "就把目标变为朋友的女友么……%K%P"
    window hide
#BG_INIC 1
#BG_PRI 1
#CHR_ERSWC 1,2
    hide bg2 with dissolve
    scene expression "img/EXBG01A@2x.jpg" as bg0 with dissolve
#BG_ALPC 0
#CHR_ALPC 0
    hide bg1 with dissolve
    show expression "img/BG36AA@2x.jpg" as bg_over zorder 2 with dissolve
    play sound "SE06_36"
    pause (32/32.0)
    play sound "SE00_32"
    pause (32/32.0)
    voice "NYU05A_XL000"
    店員Ｅ "「欢迎光临～」"
    voice "NYU05A_TO000"
    亨 "「啊，我和别人有约的……那个，啊，找到了。」"
    "亨看到我们后，单手拿着头盔，大步的走过来。"
    "在另一只手拿着的ＭＤ播放器里，应该放有他的作曲吧。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-160)
#CHR_POSC 1,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA01"),"True","img/YU_LCA01A@2x.png") as lh0 zorder (10+0):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA01"),"True","img/TO_LBA01A@2x.png") as lh1 zorder (10+1):
        xcenter .75
    with dissolve
    play music  "BGM09"
    voice "NYU05A_TO001"
    亨 "「不好意思，来晚了。」"
    志雄 "「哪有，突然叫你出来，是我们给你添麻烦可。」"
    voice "NYU05A_YU035"
    结乃 "「给你添麻烦了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB01"),"True","img/TO_LBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU05A_TO002"
    亨 "「没事，反正很闲，完全不要在意啦。」"
    "向店员点完东西后，亨向我使了个眼色。"
    "我点点头站起来，坐到结乃的身边。"
    "连座位这种小事都会去在意，没想到这家伙还挺细心的。"
    voice "NYU05A_TO003"
    亨 "「那么，怎么样，节目的内容决定了么？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC03"),"True","img/YU_LCC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「没，还没有。」"
    "桌子上打开着的笔记本上还是空空的。"
    "什么都没有决定。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA03"),"True","img/TO_LBA03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU05A_TO004"
    亨 "「不会吧，虽然本身就迟到的我不该这么说，但你们应该讨论了很久了吧。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC05"),"True","img/YU_LCC05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU036"
    结乃 "「对不起，有些问题上意见没能统一……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB04"),"True","img/TO_LBB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU05A_TO005"
    亨 "「哈……这还真是罕见的事呢。」"
    voice "NYU05A_TO006"
    亨 "「你们两人不管什么时候都给人一种很相配的感觉啊。」"
    "刚刚坐到位子上的亨，带着很惊讶的表情说道。"
    "的确，因为结乃和我的思考方向，兴趣都很接近，所以我们的关系才渐渐亲密起来的。"
    "不过现在看来也不完全是那么一回事了……大概这是我们第一次意见有了分歧吧。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBA01"),"True","img/TO_LBA01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU05A_TO007"
    亨 "「不过，偶尔出种事也算正常啦。要不，听下我给节目做的主题曲怎么样？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCA01"),"True","img/YU_LCA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    志雄 "「已经做好了？」"
    voice "NYU05A_TO008"
    亨 "「嗯，因为灵感爆棚，主旋律决定好后一会就完成了。」"
    "明明拜托他还没多久，效率真是高啊。"
    "真不愧是身为备考生还能公开宣布自己很悠闲的人。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB01"),"True","img/YU_LCB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU037"
    结乃 "「那么，能让我听一下吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB02"),"True","img/YU_LCB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU038"
    结乃 "「也有可能会从主题曲中得到启发呢。」"
    "结乃的兴趣也来了。"
    "紧张的气氛也彻底改变了，默默地在心中对亨表示感谢。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB02"),"True","img/TO_LBB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU05A_TO009"
    亨 "「哦，那么，我播了。」"
    "亨将MD播放器放在桌子上，将耳机递给我和结乃。"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,YU_LXB05,3,F24
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB05"),"True","img/YU_LCB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    stop music fadeout 132
#REEK_CHR 0
    voice "NYU05A_YU039"
    结乃 "「啊……」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
#BG_PRI 3
    window hide
#BG_SET_BACK 
#BG_INIC 2
#BG_ALPC 2
    show expression "img/EV_YU05A@2x.png" as bg2 zorder 200 with dissolve
#BG_INIC 1
#BG_PRI 1
#BG_ALPC 0
#BG_ALPC 2
#CHR_ALPC 0
#CHR_ALPC 1
    hide bg1 with dissolve
    "接过耳机的结乃脸微微红了起来。"
    "一定是想起之前的那件事了吧。"
    "第一次一起去ＫＡＮＡＴＡ的公开广播……"
    "我的收音机没电了，只好借用结乃的一只耳机听节目。"
    window hide
    show expression "img/EV_YU05B@2x.png" as bg2 zorder 200  with dissolve
    "这却导致我们被正在播音的ＫＡＮＡＴＡ误以为是恋人，还在广播里公开戏弄了一番。"
    "虽然当时在现场很是害羞，但现在的我们，已经是ＫＡＮＡＴＡ所说的那个关系了。"
    window hide
#BG_INIC 1
#BG_PRI 1
    hide bg2 with dissolve
#BG_ALPC 0
#CHR_ALPC 0
#CHR_ALPC 1
    voice "NYU05A_TO010"
    亨 "「这是我灵魂的作曲，用心灵去感受吧！」"
    "亨的声音，将怀念从前的我们拉回现实。"
    "亨特地摆好了姿势，打开开关。"
    window hide
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_POSC 2,(320-160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCB06"),"True","img/YU_LCB06A@2x.png") as lh2 zorder (10-2):
        ypos 0.0
        xcenter .25
    with dissolve
    play sound "SE07_06"
#CHR_ALP_AUTOC 2,128,0,1
#CHR_ALP_AUTOC 0,0,0,1
#CHR_ALP_SAVEC 2
#CHR_ALP_SAVEC 0
    pause 2
    stop sound
##BG_INIC 3
#    show expression "img/BG36AA@2x.jpg" as bg3 zorder 3 with dissolve
#EFF_STAC 0,DEATH_METAL,EFF_SKIP
##BG_ALPC 3
    志雄 "「哇！」"
    voice "NYU05A_YU040"
    结乃 "「这，这是什么啊！」"
    "从耳机里传出来的，完全是超乎想象的音乐。"
    "能力有限，我无法用已知的东西将这个声音表达出来。"
    "只是，我明白……能接受这个东西的人，绝非常人。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB01"),"True","img/TO_LBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU05A_TO011"
    亨 "「这是我特别制作的重金属音乐啊，不错吧，能接受吧？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC04"),"True","img/YU_LCC04A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
    with dissolve
    voice "NYU05A_YU041"
    结乃 "「已，已经够了！快点停下吧……拜托了……」"
    "比我承受了更多伤害的结乃，脸色发青的抬起手寻求帮助。"
    "这个，应该说是……能将人正常的精神无端分裂的音乐。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB02"),"True","img/TO_LBB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU05A_TO012"
    亨 "「在说些什么啊，好戏现在才开始呢！」"
    stop sound
#EFF_STPC 1,EFF_NORMAL
    "我抓住想要提高音量的亨的手，把名为音乐的噪音的元凶干脆利落地关上了。"
    voice "NYU05A_YU042"
    结乃 "「太感谢了，刚才好像看到了满是鲜花的田野……」"
    window hide


    hide lh2 with dissolve
    play sound "SE04_17"
#QUA2_ALL 
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 2
#CHR_ALPC 0
#CHR_ALPC 2
#CHR_SET_FRONT
    "连从耳朵里掉落下来的耳机都没去捡，直挺挺地倒在桌子上。"
    "如果再持续数秒的话，结乃的精神上会受到无法弥补的伤害也说不定。"
    voice "NYU05A_TO013"
    亨 "「怎么样，很棒吧，把这个作为开头曲的话一定是最棒的！」"
    志雄 "「谁会去用啊，那种东西！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0,(320-160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LCC02"),"True","img/YU_LCC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
        xcenter .25
    with dissolve
    voice "NYU05A_YU043"
    结乃 "「是，是啊，听众里出现死者要怎么办啊啊啊啊！」"
    "对着得意洋洋的亨，我和结乃一起吐糟着。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_LBB04"),"True","img/TO_LBB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NYU05A_TO014"
    亨 "「果，果然一个鼻孔出气啊，你们两个……」"
    志雄 "「那种噪音谁听了都会这样！」"
    voice "NYU05A_YU044"
    结乃 "「亨学长的乐团原来一直都是只做这样的音乐么！」"
    "仿佛刚才的隔阂完全没有发生过一般，现在我和结乃阵线异常的统一。"
    "虽然代价有些大，但我们之间险恶的气氛，被亨和重金属音乐一挥而去了。"
#label QJUMP
    window hide
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG15NA1@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG15NA1@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    play music  "OBGM17"
#FADE_IN 1
    "因为结乃被亨的重金属音乐完全击溃了。"
    "商议的问题只得再次搁浅。"
    志雄 "「结果到最后什么都没决定呢……」"
    "考虑到截止日期的话，问题已经达到相当严重的地步了。"
    "就算如此，比起在心里没底的情况下勉强决定来说，还是从头到尾重新考虑下好。"
    志雄 "「但是，明天再不快点决定内容的话……」"
    "话虽如此，就这样以平行线的状态保持下去的可能性也比较高。"
    志雄 "（怎么办才好呢……）"
    "不知何时，感觉好像偏离了原本的目的。"
    "对于结乃来说，或许会很执着于结果吧？"
    志雄 "（如果是神奈的话或许能问到点什么。）"
    "手刚放在电脑电源开关上，又不由得缩了回来。"
    "今天之所以会有如此险恶情况，就是因为我询问神奈要不要参加。"
    "为了只有两人的回忆。"
    "我十分理解结乃的心情。"
    "事到如此……关于比赛的事情还是不要再去拜托她比较好吧。"
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    menu:
        "即使这样还是要和神奈商量":
            $F7=0
        "结乃说的话的确也有道理":
            $F7=1
    if F7==0:
        jump L_NYU05A_SEL00_A
    if F7==1:
        jump L_NYU05A_SEL00_B
label L_NYU05A_SEL00_A:
    $F5+=1
    志雄 "「虽然有点对不住结乃……」"
    "但第三者的意见，一般来说能让事态得到好转。"
    "现在这个阶段，最理解结乃的只有神奈了。"
    "直到，我能够取代神奈的位置之前……受她照顾也是没办法的吧。"
#CHAT_STA
#BG_SET_BACK 
#BG_INIC 2
#BG_PRI 2
#BG_HIDEC 3
#BG_SET_BACK 
#BG_INIC 1
#BG_ALPC 1
    show expression "img/CHAT_5A_00@2x.png" as bg_chat zorder (10-1)
    show expression "img/NIMG14C@2x.jpg" as bg1
    with dissolve
#BG_COLC 0,128,128,128
    play sound "SE09_35"


#BG_ALP_SAVEC 0
#BG_ALP_SAVEC 1
#BG_ALPC 0
#BG_ALPC 1
    hide bg2 with dissolve
#CHAT_STR "〈神奈：〉%N已经准备好投稿的内容了哦。"
#WAIT_KEY 96
#CHAT_END
    "打开聊天软件，跳出的第一句话就是这个。"
    "连节目的内容都还没最终决定，神奈就准备要投稿了。"
    "应该还没等我联络就已经等不急了吧。"
#CHAT_STA
    show expression "img/CHAT_5A_01@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N啊，不，对不起，其实内容还没有决定好。"
#WAIT_KEY 96
    show expression "img/CHAT_5A_02@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N是么？快要到截止日期了哦。还在说这种话。真的没关系么？"
#WAIT_KEY 96
#CHAT_END
    "这到不是责备，神奈说话一贯如此。"
    "面对紧迫的事态，神奈那冷静自若的姿态，总能给我带来奇妙的安全感。"
    window hide
#FADE_OUT 1
#CHAT_STA
    show expression "img/CHAT_5A_03@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N但是啊，怎么说呢，结乃特别在意我找你商量这件事，因此也引发了一些主题上的分歧。"
#FADE_IN 1
    show expression "img/CHAT_5A_04@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N这样的话，找我来商量那不就是恶性循环了么？"
#WAIT_KEY 96
    show expression "img/CHAT_5A_05@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N虽然如此……"
#WAIT_KEY 96
#CHAT_END
    "面对结乃的抱怨我却还来找神奈，神奈作出了理所当然的判断。"
#CHAT_STA
    show expression "img/CHAT_5A_06@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N好吧，我也向结乃提了下志雄邀请我参加这件事。"
#WAIT_KEY 96
    show expression "img/CHAT_5A_07@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N我也有责任呢……"
#WAIT_KEY 96
    show expression "img/CHAT_5A_08@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N不，你并不是有意的，况且你本来就拒绝了嘛。"
#WAIT_KEY 96
    show expression "img/CHAT_5A_09@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N嗯……当然，是为了给你们两人的节目投稿，不过的确也要照顾下结乃的心情呢……"
#WAIT_KEY 96
#CHAT_END
    "一想到能如此考虑的神奈，就对自己那肤浅的想法感到憎恨。"
#CHAT_STA
    show expression "img/CHAT_5A_0A@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N平心而论，比起结乃的节目，还是志雄的点子比较有意思。"
#WAIT_KEY 96
#CHAT_END
    "经过好几次聊天后察觉到。"
    "从对于广播的兴趣这一点来说，比起结乃，神奈和我似乎更合的来些。"
    "那是因为，将我和广播联系到一起的初代『凯尔玛妹妹』就是神奈，会这样想也是当然的吧。"
#CHAT_STA
    show expression "img/CHAT_5A_0B@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N我想，结乃也应该明白是我的提案比较有意思。"
#WAIT_KEY 96
    show expression "img/CHAT_5A_0C@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N但是，她对于结果异常执着了呢……"
#WAIT_KEY 96
    show expression "img/CHAT_5A_0D@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N呃……"
#WAIT_KEY 96
#CHAT_END
    "明明屏幕上显示的只有文字，却能从电脑的另一边听到神奈重重地叹气声。"
#CHAT_STA
    show expression "img/CHAT_5A_0E@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N不对吗？"
#WAIT_KEY 96
    show expression "img/CHAT_5A_0F@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N就算是这样……结乃如此执着于结果也是有原因的吧？"
#WAIT_KEY 96
    show expression "img/CHAT_5A_10@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N她那么努力，也是为了志雄哦。不要太不在意对方的心情了。"
#WAIT_KEY 96
#CHAT_END
    "原以为能得到赞同的，但神奈的回复稍微令我有些意外。"
#CHAT_STA
    show expression "img/CHAT_5A_11@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N从结乃那里……听到了什么吗？"
#WAIT_KEY 96
    show expression "img/CHAT_5A_12@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N谁知道呢，就算听到了什么也不会告诉你哦，自己去领会吧。"
#WAIT_KEY 96
#CHAT_END
    "关键的地方，神奈总是一反常态的保持嘴紧。"
    "但是，知道了结乃是为了我才对结果如此执着这一点，就感到心里轻松了起来。"
#CHAT_STA
    show expression "img/CHAT_5A_13@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N谢谢了，我稍微也从结乃的方面考虑一下，重新规划吧。"
#WAIT_KEY 96
    show expression "img/CHAT_5A_14@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N嗯，就这样做好了，我会在在你们的背后为你们鼓劲的。"
#WAIT_KEY 96
    show expression "img/CHAT_5A_15@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N晚安，如果是志雄的话，我相信一定能做好。"
#WAIT_KEY 96
    show expression "img/CHAT_5A_16@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N嗯，晚安。"
#WAIT_KEY 96
    scene expression "img/NIMG14B@2x.jpg" as bg0 with dissolve
#CHAT_END
    "不会让神奈产生是她在防碍着我和结乃的错觉吧。"
    "仔细想想的话，我一直在被神奈鼓励着。"
    志雄 "「谢谢了呢。」"
    "看着已经离线的神奈的头像，我再一次道谢。"
    "就算不直接参加……神奈对于我们的广播来说依旧是不可缺少的存在。"
    jump L_NYU05A_SEL00_X
label L_NYU05A_SEL00_B:
    $F3+=1
    志雄 "「还是算了吧。」"
    "想要成为我心中的唯一。"
    "结乃是这样说的。"
    "就算她不说，对我而言，最重要的也只能是结乃。"
    "不能再让结乃因此感到不安了，这是我的责任。"
    志雄 "「再考虑下结乃的意见……有分歧的地方推倒重来一遍吧。」"
    "为自己喜欢的女孩去考虑，光是这点就让我感到很幸福。"
    "虽然我不能肯定这样做就会有个好结果……再认真考虑，找到平衡吧。"
    jump L_NYU05A_SEL00_X
label L_NYU05A_SEL00_X:
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
#label THREAD_CHR_ASE
#TH_CHR_ASE BG_3
#EOT
