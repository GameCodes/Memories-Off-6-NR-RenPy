label NYU04A:
    $currentlabel = "NYU04A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '26'
    $date = '3'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
    show expression "img/NIMG15H-568h@2x.jpg" as cal zorder 5
    show expression "img/07_26_WEDNESDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
#FADE_IN 0
#CAL_DSP_GRP 3,CAL_0726
#FADE_OUT 0
    scene expression Solid("000") with fade
    show expression "img/NIMG01B@2x.png" as bg_over zorder 2
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
    voice "NYU04A_YU000"
    结乃 "「因为是地方ＦＭ主办的比赛啊。」"
    voice "NYU04A_YU001"
    结乃 "「果然还是把本地的故事做到节目里比较好吧……」"
    window hide
#EFF_PRI 0
    show expression "img/BG05AA@2x.jpg" as bg1 with dissolve
#EFF_STPC 0,EFF_SKIP
#ROUTINE_STA
#EFF_PRI 0
#BG_SWPC 0
    hide bg1 with dissolve
#BG_PRIC 0
#BG_PRIC 1
#ROUTINE_STP
    play music  "BGM06"
    pause (32/32.0)
    scene expression "img/BG101AA@2x.jpg" as bg0
#FADE_OUT 1
    show expression "img/BG101AA@2x.jpg" as bg0 with dissolve
#FADE_IN 1
    "按照结乃的提议，我们在网上搜索着浜咲ＦＭ覆盖区域中的各种奇闻异事。"
    window hide
#FADE_OUT 1
    show expression "img/BG102AA@2x.jpg" as bg_over zorder 2 with dissolve
#FADE_IN 1
    pause (32/32.0)
#FADE_OUT 1
    show expression "img/BG104AA@2x.jpg" as bg_over zorder 2 with dissolve
#FADE_IN 1
    "直到现在，广播的进展还算顺利……"
    window hide
#FADE_OUT 1
    show expression "img/BG85AA@2x.jpg" as bg_over zorder 2 with dissolve
#FADE_IN 1
    志雄 "「真是的……完全没有料到这里居然这么陡。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB02"),"True","img/YU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU002"
    结乃 "「是呢，不过还是要加油哦，很多老年人都这么有精神的走着呢。」"
    "我已经满头大汗，虽然擦拭了很多次，额头上的汗珠仍然没有停下来的意思。"
    if not persistent.dictlist[24] and persistent.show_dict:
        $persistent.dictlist[24]=True
        show screen dict_pop(i=24)
    "虽然我们住的这个地区以海岸闻名，但是只要稍微向内陆推进一些，就会被群山包围。"
    if not persistent.dictlist[29] and persistent.show_dict:
        $persistent.dictlist[29]=True
        show screen dict_pop(i=29)
    "探访散布在这座山上的神社，就是今天的主要目的之一。"
    if not persistent.dictlist[30] and persistent.show_dict:
        $persistent.dictlist[30]=True
        show screen dict_pop(i=30)
#DICT_FLG 38
    "在此之前，我们已经去过了澄空、浜咲以及其他相关的地方，而现在，我们则回到了最开始也是最后的一站——芦鹿岛。"
    志雄 "「结乃不会感到累吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB06"),"True","img/YU_LBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU003"
    结乃 "「唉？这么一说是有点……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB02"),"True","img/YU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU004"
    结乃 "「不过把这当作爬山的话，不就不会那么无聊了，呃？夏天去山上玩可是必不可少的啊。」"
    志雄 "「原来如此，这样想会好些吧。」"
    "离开山道稍微远一点的地方就是海岸。"
    "能同时享受爬山和大海的风光，这么看，这个地方也算是块宝地。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU005"
    结乃 "「加上刚才的神社已经４个了呢，照这趋势，七福神都能碰上吧。」"
    志雄 "「不说的话还真没有注意，这里所有的神社都和七福神有关呢。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU006"
    结乃 "「是的，大黑大人，惠比寿大人，毗沙门天，布袋大人……还有谁来着？」"
    if not persistent.dictlist[40] and persistent.show_dict:
        $persistent.dictlist[40]=True
        show screen dict_pop(i=40)
    志雄 "「剩下的是福禄寿，寿老人和……弁财天么？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB06"),"True","img/YU_LBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU007"
    结乃 "「好厉害！能把七福神都说出来的人现在可不多见了。」"
    志雄 "「是么……」"
    "小学的时候曾经很用功的画过七福神的画像。"
    "如果在睡觉的时候把画像放在枕头下面就会有个好梦。"
    "那时竟然信以为真，在给加人和莉莉丝画的时候，就牢牢的记住了这七个名字。"
    "看来小时候的知识储备偶尔也会派上用场啊。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB02"),"True","img/YU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU008"
    结乃 "「真难得，如果能遇上所有的七福神就好了。」"
    志雄 "「如果全部灵验的话，一定会很幸福吧。」"
    "由神社来探访这个地区的故事……"
    "虽然觉得这和结乃当初的计划不太一致，但是只要能看到结乃欢快的笑容，这种小事也不必要去计较了。"
    志雄 "「哦，下一个神社要到了呢。」"
    "祭拜弁财天的神社就在眼前。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB03"),"True","img/YU_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "但是，结乃竟显得有些犹豫了起来。"
    voice "NYU04A_YU009"
    结乃 "「要不弁财天就算了吧。」"
    志雄 "「为什么？这不是最重要的神灵么！」"
    "怎么能避开掌管财运的神灵。"
    "如果在这许愿的话，说不定就能得到庇佑，轻松拿到优胜奖金，那广播计划也自然而然可以一路顺风。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA04"),"True","img/YU_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU010"
    结乃 "「虽然金钱的确是非常重要啦……但是，因为是个女神灵。」"
    志雄 "「啊……原来是这样啊。」"
    voice "NYU04A_YU011"
    结乃 "「是的，听说有因为神灵看不惯恋人而吃醋导致分手的事情发生……」"
    "能如此醋意大发的神灵必然是女性吧。"
    "有关这一类的话题似乎的确没怎么在男性神灵的传说里出现过。"
    志雄 "「吃醋么……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA03"),"True","img/YU_LBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU012"
    结乃 "「怎，怎么了？」"
    志雄 "「啊不，没什么。」"
    "我情不自禁的偷看了一眼身旁的结乃，撅起来的嘴吧真是惹人怜爱。"
    "在学生会和可爱的学妹说话的时候……"
    "和莉莉丝或者箱崎同学谈话时间比较长的时候，常常能看到结乃露出这种可爱的神色。"
    志雄 "（连神灵都会吃醋吗？这样不是和小女生没差了……）"
    "我没来由的乱想着。"
    志雄 "「真想看看是七福神的保佑会灵验呢，还是弁财天大人的嫉妒比较厉害。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC02"),"True","img/YU_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU013"
    结乃 "「就算没有发生不好的事情，但是要是和灵验的保佑互相抵消的话岂不是也很得不偿失。」"
    "结乃说的也对。"
    "但是……我知道的，这个神社为了能吸引恋人们来参拜，有特意做了补救的措施。"
    志雄 "「没关系的，过来吧。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC01"),"True","img/YU_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU014"
    结乃 "「唉？一定要这样吗？出了问题我可不管啊……」"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
    show expression "img/BG105AA@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    play sound "SE05_15L"
#FADE_IN 1
    "拉着结乃的手走进神社，那里有一棵高大的银杏树。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA04"),"True","img/YU_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU015"
    结乃 "「是……连理枝么？」"
    志雄 "「嗯。你看，这棵银杏，明明有两个树干，却只有一个树根呢。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB06"),"True","img/YU_LBB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU016"
    结乃 "「唉？真的，所以才被称作连理枝吧！」"
    "这就是活用自然景物特点的智慧啊！"
    "好像是为了呼应连理枝一样，树的周围供奉着无数个祈求良缘的绘马。"
    play music  "BGM13"
    志雄 "「这里的弁财天好像是兼职了红娘的工作呢。」"
    voice "NYU04A_YU017"
    结乃 "「哈，这我倒是真不知道呢……」"
    "……其实，这是昨天在网上看到的，不过这些细节还是不要告诉结乃了吧。"
    志雄 "「反正难得来一次，我们也去供奉绘马吧？」"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,YU_LXB05,3,F24
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB05"),"True","img/YU_LBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NYU04A_YU018"
    结乃 "「这样好么，绘马应该会一直保留在这里的吧？」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
#BG_PRI 3
    志雄 "「难道有什么不妥的吗？」"
    "许下过诺言，要在这个夏天和结乃留下很多的回忆。"
    "既然这样的话，以物品的形式留下的绘马……毋庸置疑是个最棒的选择。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB02"),"True","img/YU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU019"
    结乃 "「不，不会！就这么做吧！」"
    "刚说完，结乃就向出售绘马的巫女那里跑去。"
    志雄 "「用不着这么着急吧……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU020"
    结乃 "「当然！要在弁财天让学长改变心意以前做完！」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "转眼间，结乃就只剩下了一个浅浅的背影。"
    "看来，直到现在，在这种事情上还是不能给结乃足够的安全感啊。"
    志雄 "「比起结乃，弁财天大人的嫉妒心显然是小巫见大巫了吧。」"
    "无数个被供奉起来的绘马上，写着恋人们的名字。"
    "他们是抱着怎样的心情写上的呢？"
    "是刚刚相依的新人，还是情比金坚的伴侣，亦或是已经渐行渐远的故人。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU021"
    结乃 "「买来了哦！」"
    志雄 "「好的，那么，写上我们的名字吧。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA02"),"True","img/YU_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU022"
    结乃 "「嗯！」"
    "在这里，作为新加入的成员……"
    "弁财天大人会怎样迎接我们的到来呢？"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB02"),"True","img/YU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU023"
    结乃 "「春日——结乃——。写好了！」"
    志雄 "「把全名写上去吗，怎么感觉像是给学生会文件签字一样。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA03"),"True","img/YU_LBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU024"
    结乃 "「学长！气氛完全被你破坏了！」"
    志雄 "「对，对不起！」"
    "无意的一句话，却让结乃又鼓起了脸蛋。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC02"),"True","img/YU_LBC02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU025"
    结乃 "「既然当作了文件……联想到别的文件也好啊，比如说……结婚申请书……」"
    志雄 "「哈，你说什么？」"
#CHR_GET_POSC 0,F24,F25
#RSUB F24
#BG_LAY 3,YU_LXB05,3,F24
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB05"),"True","img/YU_LBB05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
#REEK_CHR 0
    voice "NYU04A_YU026"
    结乃 "「什，什么都没有！快点供奉起来吧！」"
#REMOVE_REEK_CHR 0
    hide bg3 with dissolve
#BG_PRI 3
    志雄 "「啊。不用这么着急啦，我不会改变心意的啦。」"
    "在我们无数的回忆里……又添上了重重的一笔。。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG85AA@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC02"),"True","img/YU_LBC02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play music  "BGM06"
    play sound "SE05_15L"
#FADE_IN 1
    voice "NYU04A_YU027"
    结乃 "「真是难以置信啊！学长！」"
    "说道祭拜弁财天的话，洗钱当然是必不可少的。"
    "在连理枝下回避了弁财天大人嫉妒的我们，阔步走向洗钱的地方。"
    志雄 "「嗯，所以说。洗的钱越多，效果越明显吗？」"
    "我想都不想，就把钱包里最大面值的纸钞放了水中。"
    "顺便提一下，那张纸币是我今天的全部财产。"
    voice "NYU04A_YU028"
    结乃 "「那可是洗钱，一般都是用硬币洗的吧！」"
    志雄 "「那这样不是挺好的，可以为广播营造多一点话题。」"
    "不过，这个真的合适作为话题么？这种粗心大意的事，一路上我似乎并没有少做。"
    voice "NYU04A_YU029"
    结乃 "但是，我们今天的路程好像并不是到这里为止吧……」"
    "结乃叹着气，无奈的看着我。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC03"),"True","img/YU_LBC03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU030"
    结乃 "「学长想用这张湿透了纸币……去付账么？」"
    志雄 "「呃……」"
    "完全没有考虑到这一点。"
    "除去这张纸币，我包里还有的硬币数量为……零！"
    "前几个神社捐钱的时候习惯的捐一些小面额硬币，不知不觉竟花光了所有的零钱。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA03"),"True","img/YU_LBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU031"
    结乃 "「事先说明……我可不会借你钱的哦。」"
    志雄 "「结，结乃～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA04"),"True","img/YU_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU032"
    结乃 "「自作自受！」"
    "对于将要收到这张纸币的商户，我真的感到非常的抱歉。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG86AA@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB06"),"True","img/YU_LBB06A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE05_19L"
#FADE_IN 1
    voice "NYU04A_YU033"
    结乃 "「哇啊啊！好厉害啊！」"
    志雄 "「终于到山顶了么……」"
    "结束了七福神的祈福后，我们重新修正目标为山顶。"
    "在我刚开始感觉吃力的时候，结乃还拉着我的手努力向上爬。"
    "到最后，我们两个到了只能互相搀扶才能勉强前进的夸张境地。也因此，依偎在一起的身体直到爬到山顶前都没有分开。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU034"
    结乃 "「真的是一览无余呢～」"
    志雄 "「嗯，付出的辛苦总算没有白费。」"
    "这座山的高度，对于职业登山者可能并不值一提。"
    "但是对于我们而言……能爬上这样的山，真的够之后骄傲好一阵子的了。"
    "而作为直接回报，山顶的优美景色真的是没话说。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU035"
    结乃 "「澄空学园是在那个方向吧？」"
    志雄 "「嗯，不过那么远，即使在山上也很难看见吧。」"
    voice "NYU04A_YU036"
    结乃 "「说的也是～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB02"),"True","img/YU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU037"
    结乃 "「但是真的好震撼啊！这样广阔的视野，地球果然是圆的吧。」"
    "不光是我们住的地方。站在这里放眼望去，目所能及的远方，天穹和地平线练成一条线。这便是这世界最真实的模样吧。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU038"
    结乃 "「搬来已经快一年了……可没有去过的地方还有很多。」"
    志雄 "「才一年可完全不够哦。我都住在这里十八年了，不知道的地方还有很多呢。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU039"
    结乃 "「是这样么，要是能将这些地方全都逛一遍就好了。」"
    志雄 "「嗯……」"
    "不知道在这个夏天能够逛多少个地方呢？"
    "就算全都逛过一遍，过不久，这些地方也会改变，换上一副新的模样。这么想来，真是怎么逛也逛不完的。"
    voice "NYU04A_YU040"
    结乃 "「对了，学长有去过那里么？」"
    志雄 "「呃，这还真没去过，虽然经常路过，但并没有怎么在意。」"
    voice "NYU04A_YU041"
    结乃 "「我也是呢……」"
    "结乃所说的，是芦鹿岛的瞭望台。"
    "电车从旁边经过的时候就能看见它，虽然没有去过，但却感觉成了日常生活里不可缺少的一个布景。"
    "这样说来，的确应该去瞭望台的里面看看呢。"
    志雄 "「机会难得……一起去补上这课吧。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB02"),"True","img/YU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU042"
    结乃 "「好的！那里也是一个适合欣赏美景的好地方呢。」"
    "以高度来说，这里的确拥有优势，但是那里却更能心平气和的去欣赏些东西。"
    "人真是奇妙，站的越高，就越是心跳不已。"
    志雄 "「好的！那么，比比看谁先到么？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA02"),"True","img/YU_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU043"
    结乃 "「可以啊～输掉的一方要负责门票钱哦！」"
    志雄 "「求之不得。」"
    "真是千载难逢的机会。"
    "如果我胜利的话，就不用使用那张湿透的纸币来丢人了。"
    "这场战斗绝对不能输啊。"
    志雄 "「那么，预备——」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB02"),"True","img/YU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU044"
    结乃 "「嘿！」"
    window hide
    play sound "SE01_02L"
#SE_VOLC 0,96
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "结乃没等我喊完就松开了手向前奔去。"
    "这完全是抢跑啊。"
    志雄 "「喂！这是耍赖啊！」"
    voice "NYU04A_YU045"
    结乃 "「你说什么，我听不到啊～」"
    "辛辛苦苦爬上来的坡道，结乃一溜烟地冲了下去。"
    window hide
    play sound "SE01_02L"
    "为了不跟丢那个背影……我拼命地追赶着。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG87EA@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC03"),"True","img/YU_LBC03A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE05_19L"
#FADE_IN 1
    voice "NYU04A_YU046"
    结乃 "「呼…呼…我赢了呢。」"
    志雄 "「可恶……结乃……你是属兔子的么？」"
    "前往瞭望台的赛跑，结乃一直保持着领先。"
    "一直到终点，我都只能看着她的背影。"
    "虽然知道结乃的运动细胞异常发达……但是，真没想到，我居然连赛跑也会输。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBC01"),"True","img/YU_LBC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU047"
    结乃 "「呼呼……仔细，想想的话……这不就是，让人羡慕的场面么。」"
    志雄 "「哪，哪里会是啊……」"
    "搞得满头大汗，弯着腰大口喘气，到底有哪一点称得上让人羡慕呢。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU048"
    结乃 "「逃跑着的女人喊着『来抓我看看啊』，这种常识都不知道么。」"
    志雄 "「又是～啊…哈……哦…呼呼……那个？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB02"),"True","img/YU_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU049"
    结乃 "「是的，虽然完……完全……感觉不到那种感……感觉……」"
    志雄 "「就是……那个一般是在沙滩上吧。」"
    "浪费了好多时间才调整好呼吸，终于能好好欣赏一下周围的风景了。"
    "天空被夕阳染红，观光客人们也陆陆续续的从山上走了下来。"
    "剩下在我们身边的，都是些……手牵着手散步的男女。"
    "在周围人看来，我们也是这些情侣中的一员吧。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU050"
    结乃 "「这里离海滩很近呢……这么难得的机会，早知道就带着泳衣来了。」"
    志雄 "「游泳的话，以后还有机会的。」"
    "关于游泳，倒是有值得推荐的地方。"
    志雄 "「广播比赛的决赛在海滩上设立的特别工作室举行，到时候去那里游泳就好了。」"
    志雄 "「如果顺利进入决赛的话，在出场前想游多久都没关系的哦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA02"),"True","img/YU_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU051"
    结乃 "「我知道了，那么到时候必须要将泳衣藏好了。」"
    志雄 "「哦……」"
    "还真是期待看到穿着泳装的结乃的样子。"
    "这下，要在广播比赛取得优胜的理由又多了一个。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG88EA@2x.jpg" as bg0 zorder 0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
#CHR_COLC 0,128,120,112
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play music  "BGM14"
#FADE_IN 1
    voice "NYU04A_YU052"
    结乃 "「风一下就停了呢。」"
    志雄 "「嗯，这就是所谓的“傍晚的海上风平浪静”吧。」"
    "接连不断地从大海吹向陆地的风不知不觉的小了许多。"
    志雄 "「再过一会儿的话，风向就要变了……」"
    voice "NYU04A_YU053"
    结乃 "「不管是哪边的风，这里都会很清晰的感受到吧。」"
    "瞭望台正好处在陆地与大海的交界处。"
    "在这个连一丝微风都被无限放大的空间里，用脸颊去守望着大海，和背后的街道。"
    "现在……并肩而立的我们，站在瞭望台的顶端。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA02"),"True","img/YU_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU054"
    结乃 "「就算太阳落山了，也看得很清楚呢。」"
    "街道上建筑物因为影子的湮没而渐渐褪去光彩，但是大海却毫不倦怠。"
    "远在天边的，闪着柔和光芒的水平线，仿佛触手可及。"
    志雄 "「真是漂亮啊……太阳落山只有一瞬，真是可惜。」"
    voice "NYU04A_YU055"
    结乃 "「虽然离秋天还早，但是太阳还是很早的就翘班了啊。」"
    "沿着瞭望台的扶手向下看去，海面因为夕阳的照射而闪着金黄色的光辉。"
    "黄金海……水面上反射出的光芒并不刺眼，反而带着特有的暖意。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU056"
    结乃 "「虽说夕阳短暂，但是这美的瞬间却已经深深地印刻在我的脑海里了。」"
    voice "NYU04A_YU057"
    结乃 "「这是夕阳和学长的回忆。」"
    "我默默地看着身边凝视远方的结乃。"
    "被夕阳染红的侧脸，明明已经看了很多次，但是一点都没有厌倦。"
    "太阳完全落下去了，结乃侧脸上的光辉也逐渐褪去，就好像要随同这太阳一起消逝在海底。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    志雄 "「结乃……」"
    voice "NYU04A_YU058"
    结乃 "「学长？」"
    "我从后面抱住了结乃。"
    "我知道这样的忧虑有些太过矫情，但我真的害怕失去。"
    "我的臂膀，牢牢的裹住了结乃，如此纤细的身躯。"
    志雄 "「稍微……这样待一会，好吗？」"
    voice "NYU04A_YU059"
    结乃 "「嗯……别说是一会儿了，能这样一辈子也行哦。」"
    "只要这样做的话，结乃就不会远去。"
    "高中生活马上就要结束了，在一起的时间也会越来越少……"
    "但只要回想起另一颗，在我胸前跳动的心，温暖便会涌出，唤起那些铭刻在身体里每一寸的记忆。"
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop sound
    stop music fadeout 1
##BG_SET_BACK
##BG_INIC 2
##BG_INIC 3
##BG_INIC 4
##BG_ALPC 2
##BG_ALPC 3
##BG_ALPC 4
##BG_PRI 2
##BG_PRI 3
##BG_PRI 4
#    show expression "img/BG37N1B@2x.jpg" as bg4 zorder 4 with dissolve
##BG_SETWC 2,3,BG37N1P,BG37N1P
##BG_ALPC 2
##BG_ALPC 3
##BG_ALPC 4
#BG_SET_BACK
#BG_INIC 0
#BG_PRI 0
    scene expression "img/BG37NA@2x.png" as bg0  zorder 0
    show expression "img/trainoutside_N@2x.png" as train_bg zorder -5
    show expression "img/trainoutside_tree1_N@2x.png" as train_tree1 zorder -2:
        ycenter .5
        block:
            xcenter .4
            linear 0.5 xcenter -.1
            repeat
    show expression "img/trainoutside_tree1_N@2x.png" as train_tree1 zorder -2:
        ycenter .5
        block:
            xcenter .6
            linear 0.5 xcenter 1.1
            repeat
    show expression "img/trainoutside_tree0_N@2x.png" as train_tree2 zorder -2:
        ycenter .5
        block:
            xcenter .4
            linear 0.7 xcenter -.1
            repeat
    show expression "img/trainoutside_house1_N@2x.png" as train_house1 zorder -3:
        ycenter .47
        block:
            xcenter .4
            linear 0.7 xcenter -.1
            repeat
    show expression "img/trainoutside_house1_N@2x.png" as train_house1 zorder -3:
        ycenter .47
        block:
            xcenter .7
            linear 0.7 xcenter 1.1
            repeat
    show expression "img/trainoutside_house2_N@2x.png" as train_house2 zorder -3:
        ycenter .5
        alpha 0
        pause .5
        alpha 1
        block:
            xcenter .4
            linear 0.7 xcenter -.1
            repeat
    with dissolve
    show expression "img/trainoutside_house1_N@2x.png" as train_house3 zorder -3:
        ycenter .47
        alpha 0
        pause .9
        alpha 1
        block:
            xcenter .4
            linear 0.7 xcenter -.1
            repeat
    with dissolve
#BG_ZOOM_RATE 0,8
#BG_PRI 0
#EFF_STAC 0,TRAINWINDOW2,EFF_NOSKIP
    stop se
    stop sound
#EFF_STAC 1,QUAKE_TRAIN,EFF_NOSKIP
    pause (64/32.0)
    play sound "SE06_10L"
#FADE_IN 1
    pause (64/32.0)
    play sound "RAILWAY_000"
    pause (16/32.0)
##EFF_STAC 3,,EFF_NOSKIP
##EFF_STAC 1,,EFF_NOSKIP
    pause
    scene expression Solid("000") with fade
    stop sound fadeout 1
    show expression "img/BG01NA@2x.jpg" as bg_over zorder 2
    with dissolve
    play sound "SE05_17L"
    play music  "BGM13"
    "巡游的最后，我们到了这座已经融入夜幕的神社。"
    "虽然打着取材的名义乱逛了一天，但今天收获的快乐明显是丰厚的。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_COLC 5,128,128,128,256
#CHR_POSC 0
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBB01"),"True","img/YU_LBB01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    志雄 "「怎么样？重新逛逛的话发现这里还是不错的吧？」"
    "我从小生活在这里，对这里的每一条街都有着深厚的感情。"
    "能够带着结乃，与她分享这个小镇的点滴，我感到无比的幸福。"
    voice "NYU04A_YU060"
    结乃 "「是的，真觉得搬过来真是赚大了。」"
    "结乃去年搬来的时候，已经是秋天了。"
    "所以，现在是结乃在这里度过的第一个夏天，想介绍的地方数都数不过来。"
    "不仅芦鹿岛的烟花大会是第一次参加，这里夏季的很多东西，结乃都是第一次遇见。"
    志雄 "「啊……今天这里有特别的活动呢。」"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA01"),"True","img/YU_LBA01A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU061"
    结乃 "「神社么……虽然来过好几次，但是晚上还是第一次呢。」"
    志雄 "「平时女孩子当然不能一个人到这么暗的地方来哦。」"
    "但是，今天另当别论。"
    "不远处神社里散发出朦胧的光，即使还没有到，也能感到从里面溢出的安谧气氛。"
    hide lh10
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YU'",DynamicDisplayable(mouthanime,"YU_LBA02"),"True","img/YU_LBA02A@2x.png") as lh10 zorder (10+10):
        ypos 0.0
    with dissolve
    voice "NYU04A_YU062"
    结乃 "「真漂亮啊……感觉像是另外一个世界一样。」"
    志雄 "「哈，神社不就是脱离尘世的地方么。」"
    "除了新年和特别活动日，这里基本上没什么人。"
    "说这里是现代留下来的精神圣地也没什么错吧。"
    "但是就算这样……今天的神社真是状态爆棚，分外的美丽。"
    志雄 "「走吧，过去就知道那光究竟是什么了。」"
    voice "NYU04A_YU063"
    结乃 "「好的，那向导的工作就拜托你了。」"
    "为了不在人群中走散，我牵着结乃的手。"
    "对于还没有习惯这个动作的我们，这样的理由似乎显得格外重要。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU03A")]=True
    scene expression "img/EVN_YU03A@2x.jpg" as bg_over zorder 2 with dissolve
    voice "NYU04A_YU064"
    结乃 "「原来光芒是这么来的。」"
    志雄 "「很意外吧？」"
    "神社的石阶两旁并排挂着一盏盏灯笼，一直延伸到神社的院子里。"
    if not persistent.dictlist[54] and persistent.show_dict:
        $persistent.dictlist[54]=True
        show screen dict_pop(i=54)
    voice "NYU04A_YU065"
    结乃 "「是纸灯祭么，这些灯笼就是纸灯吧？」"
    志雄 "「嗯，这种灯也不错呢。」"
    voice "NYU04A_YU066"
    结乃 "「嗯，怎么说呢……给人一种神秘感。」"
    "和路灯比起来虚幻了不少，微弱到仿佛随时都会消失的光芒，倔强的从灯笼里投射出来。"
    "这些淡淡的光芒，仿佛灵巧的工匠，为这里的一切，镀上高贵古典的金黄。"
    voice "NYU04A_YU067"
    结乃 "「有各种各样的图案呢！」"
    "我们慢慢地走在石阶上，欣赏着路两边的灯笼。"
    "灯笼上描画出的古老图像，给人一种分外安详的奇妙感觉。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU03C")]=True
    scene expression "img/EVN_YU03C@2x.jpg" as bg0 with dissolve
    voice "NYU04A_YU068"
    结乃 "「真是非常温暖的光呢，看到这么古老的灯笼，感觉连心灵都被治愈了。」"
    志雄 "「我能理解。」"
    "在这种温柔光芒下生活的故人，一定都是处事不惊的智者吧。"
    "如今喧嚣的世界，真是连这种宁静都抛诸脑后了。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU03A")]=True
    scene expression "img/EVN_YU03A@2x.jpg" as bg0 with dissolve
    voice "NYU04A_YU069"
    结乃 "「身在这里，连现实都开始模糊了呢。」"
    志雄 "「考试和学生会的事也是哦。」"
    voice "NYU04A_YU070"
    结乃 "「……离开神社后，还请你一定要一五一十的想起来啊。」"
    "连玩笑也不放过的结乃，和以前一样，一本正经的说道。"
    "但至少，她也赞同，此刻应当把那些俗事放一放。"
    "对于身在此处的我来说，只要能喝结乃一起走着，就心满意足了。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU03B")]=True
    scene expression "img/EVN_YU03B@2x.jpg" as bg0 with dissolve
    voice "NYU04A_YU071"
    结乃 "「噗！」"
    志雄 "「怎么了？」"
    "看着灯笼的结乃忽然很夸张的捂着嘴笑了起来。"
    voice "NYU04A_YU072"
    结乃 "「那个，这个……总感觉画风忽然变了好多呢……」"
    志雄 "「啊，最近这些东西的确有不少。」"
    "结乃视线所指向的灯笼，旁边拥挤着很多人。"
    "虽然带着摄像机来祭拜的人很多，但是正在拍摄那个灯笼的人，无一例外都是手持高性能器材的家伙。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU03A")]=True
    scene expression "img/EVN_YU03A@2x.jpg" as bg0 with dissolve
    voice "NYU04A_YU073"
    结乃 "「是游戏角色吧？」"
    "这些灯笼或多或少也是由企业赞助制作的，有关于产品的宣传灯笼出现也是常情。"
    "如果是游戏公司的话，把自己的公司角色插画画上去也并不是什么不可以的事情。"
    voice "NYU04A_YU074"
    结乃 "「『秋之回忆６·下一篇章』，好评发售中……志雄学长有玩过么？」"
    志雄 "「那是怎么样的游戏呢，不知道啊。」"
    "这种灯笼是很好的宣传手段，从围在它身边的那群人就可以看出。"
    "与时俱进的集会……就是这样吧。"
    window hide
    $persistent.albumlist[persistent.albuminfo.index("EVN_YU03C")]=True
    scene expression "img/EVN_YU03C@2x.jpg" as bg0 with dissolve
    voice "NYU04A_YU075"
    结乃 "「啊……Ｔ－ｗａｖｅ也有宣传呢，去看看吧！」"
    志雄 "「嗯。」"
    "梦幻般的空间，一瞬间粉碎的干干净净。"
    "但是，嗯……"
    voice "NYU04A_YU076"
    结乃 "「哇啊，ＫＡＮＡＴＡ小姐的签名啊，快看这个！」"
    "结乃开心就好了。"
    "虽然又偏离了最初的计划，但是我们在纸灯祭里度过了一个相当愉快的夜晚。"
#label QJUMP
    window hide
    stop sound fadeout 1
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG15NA1@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG15NA1@2x.jpg" as bg0 with dissolve
    pause (32/32.0)
    play music  "OBGM17"
#FADE_IN 1
    志雄 "「呼……最近回家的时间都比较晚呢……」"
    "刚刚被摩托车带着到处跑，这次又玩到深夜……"
    "就备考生的身份而言，这真是大罪过了。"
    "但是，因此收获了一个充实的暑假，也不会留有太多遗憾了。"
    志雄 "「但是，最关键的问题还没有进展呢……」"
    "在明天去补习班前，要和结乃把广播内容确定下来。"
    "因为亨也参加这次商讨，可以的话，希望广播能有一些建设性的进展。"
    志雄 "「『必须做好』，是这样的心情吧。」"
    "至少也要做到和Ｔ－ｗａｖｅ一样，做一个让听众和主持人连成一片的广播。"
    "只是，因为这次是投稿的形式，所以要达到那种效果并不容易。"
    "考虑到广播时间有限，能做到听众和主持人有所共鸣，应该是最好的结果了。"
    志雄 "「这效果……无论如何也要达到。」"
    "我绞尽脑汁，也没有得到什么发散性的想法。"
    志雄 "「找神奈商量一下吧……」"
    "如果是神奈的话，说不定会有很多有价值的提议。"
    "虽然她说只想要给我们的节目投稿，但这样下去，恐怕连接受投稿的广播节目也无法诞生了。"
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    menu:
        "找神奈商量":
            $F7=0
        "不商量":
            $F7=1
    if F7==0:
        jump L_NYU04A_SEL00_A
    if F7==1:
        jump L_NYU04A_SEL00_B
label L_NYU04A_SEL00_A:
    $F5+=1
    window hide
#FADE_OUT 1
    pause (32/32.0)
    show expression "img/NIMG14C@2x.jpg" as bg0 zorder 0
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/CHAT_4A_00__@2x.png" as bg_chat zorder 1
    with dissolve
    pause
#FADE_IN 1
#CHAT_STA
#CHAT_STR "〈志雄：〉%N那么，我来做这件事，可以吧？"
#WAIT_KEY 96
    show expression "img/CHAT_4A_00_@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N嗯，结乃来做也可以，不过感觉志雄更能胜任哦。"
#WAIT_KEY 96
    show expression "img/CHAT_4A_00@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N总之，方法是有很多的，感觉得要自己摸索哦。"
#WAIT_KEY 96
    show expression "img/CHAT_4A_01@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N原来如此……真是受教了。"
#WAIT_KEY 96
#CHAT_END
    "烦恼过后，我将电脑打开，向神奈发出了信息。"
#CHAT_STA
    show expression "img/CHAT_4A_02@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N不好好振作起来的话，想得奖是不可能的！"
#WAIT_KEY 96
    show expression "img/CHAT_4A_03@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N是啊，现在可得好好努力了！"
#WAIT_KEY 96
#CHAT_END
    "神奈将我那些不合实际的想法整理起来，又给出了几条建议。"
    "这样的话，在后天和结乃的会议上，就能提出成型的想法了。"
#CHAT_STA
    show expression "img/CHAT_4A_04@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N好厉害呢，明明不在现场，却能准确地知道我和结乃在想什么。"
#WAIT_KEY 96
#CHAT_END
    "神奈在推断状况和气氛这方面真是厉害。"
    "这样说来，这说不定是神级广播投稿者必备的重要素质。"
#CHAT_STA
    show expression "img/CHAT_4A_05@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N那是当然的哦～"
#WAIT_KEY 96
    show expression "img/CHAT_4A_06@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N怎么可能不知道自己喜欢的人的想法呢。"
#WAIT_KEY 96
#CHAT_END
    志雄 "「唉？」"
    "神奈的话语，让我敲打键盘的手指停了下来。"
    志雄 "（喜欢的人是……）"
    "如果是指结乃的话，我并不会惊讶。"
    "因为两个人是好朋友，互相了解和看重彼此，这从去年奏云祭就能看出来了。"
    "但是，现在在讨论的是我和结乃两个人的事……"
    志雄 "（别乱想了……一定是指很亲近的朋友这一类的吧。）"
#CHAT_STA
    show expression "img/CHAT_4A_07@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N再说，志雄和结乃都不是很复杂的性格，很容易就猜到了哦。"
#WAIT_KEY 96
#CHAT_END
    志雄 "「唔……」"
    "结果很快就被神奈自己揭晓了。"
    "刚才那一瞬的心跳，真的是我想太多了。"
#CHAT_STA
    show expression "img/CHAT_4A_08@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N就是因为两个人都这样纯粹，所以才会喜欢呢。"
#WAIT_KEY 96
    show expression "img/CHAT_4A_09@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N谢谢，我现在应该这样说吧？"
#WAIT_KEY 96
    show expression "img/CHAT_4A_0A@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N你喜欢的话怎么说都可以哦。"
#WAIT_KEY 96
#CHAT_END
    "虽然在聊天软件里看不到对方的面容也听不到声音，但眼前却浮现出神奈对着电脑微笑的样子。"
    "最近感觉自己和神奈在网上聊的非常尽兴。"
    "和结乃一样，我也有着只能和神奈诉说的事情。"
#CHAT_STA
    show expression "img/CHAT_4A_0B@2x.png" as bg_chat
    with dissolve
    play sound "SE09_35"
    pause
#CHAT_STR "〈神奈：〉%N对了，如果结乃反对刚才的建议，我也准备了应对的说辞哦。"
#WAIT_KEY 96
    show expression "img/CHAT_4A_0C@2x.png" as bg_chat
    with dissolve
    play sound "SE06_24"
    pause
#CHAT_STR "〈志雄：〉%N哇，真是周到啊。"
#WAIT_KEY 96
#CHAT_END
    scene expression "img/NIMG14B@2x.jpg" as bg0 with dissolve
    "过去，连接结乃和神奈的工作由我承担着。"
    "如今，我和结乃的关系由神奈链接着。"
    志雄 "（真是缘分呢。）"
    "现在才感觉到，神奈在我心中，正一点点地扩张开来。"
    jump L_NYU04A_SEL00_X
label L_NYU04A_SEL00_B:
    $F3+=1
    志雄 "「也不要能一直请别人帮忙啊。」"
    "我将启动着的聊天软件切换到离线模式。"
    "已经很受神奈照顾了。"
    "如果再请求她提出意见的话，说不准我们会对『两个人所做的节目』这个意识淡漠下去。"
    志雄 "「也想给结乃看到我可靠的样子呢。」"
    "打开备忘录，我把我能想到的，明天要讨论的必要事项一一记录下来。"
    "结乃应该也正做着同样的事情吧？"
    "虽然不在一起，但只要心中惦记着对方，做着同样的事情，就能感到结乃正坐在我身边一样。"
    jump L_NYU04A_SEL00_X
label L_NYU04A_SEL00_X:
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
