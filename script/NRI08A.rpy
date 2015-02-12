label NRI08A:
    $currentlabel = "NRI08A"
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $month = '07'
    $day = '28'
    $date = '5'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_BG NIMG15C,CAL_0728
    show expression "img/NIMG15C-568h@2x.jpg" as cal zorder 5
    show expression "img/07_28_FRIDAY@2x.png" as cal_date zorder 6:
        align (1.0,1.0)
    with dissolve
    pause 2
    hide cal
    hide cal_date
    with dissolve
#FADE_OUT 0
    scene expression Solid("000") with fade
    scene expression "img/NIMG01B@2x.png" as bg_over zorder 2
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
#FADE_IN 1
    play music  "BGM02"
#TITLE_DSP
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESLOG_TITLE
    voice "NRI08A_XB000"
    車内放送の声 "「特快列车～马上就要发车了。」"
    志雄 "「唔……」"
    "我的额头上浮出了一条皱纹。"
    "在我视线前方的，是两张车票——去龙境的特快列车车票。"
    "可为什么我却用看待敌人般的目光瞪着它呢……"
    voice "NRI08A_RI000"
    莉莉丝 "「还找不到位子吗？」"
    志雄 "「嗯……对不起……」"
    "我把视线移开车票垂下肩膀。"
    "从刚才起，我们就一直在找票上标注的位置，可总是找不到。"
    voice "NRI08A_RI001"
    莉莉丝 "「让我看一下。」"
    "莉莉丝把头凑过我的肩膀，仔细的看着票面。"
    "她的手触碰到我的肩膀，侧脸贴近我的胸膛……几乎都可以感受到她轻轻吞吐的气息。"
    "……我有些不好意思。"
    voice "NRI08A_RI002"
    莉莉丝 "「那个，位子的号码是……那个……诶？」"
    voice "NRI08A_RI003"
    莉莉丝 "「等等，志雄……」"
    志雄 "「怎、怎么了？」"
    "莉莉丝的目光忽然锐利了起来……"
    voice "NRI08A_RI004"
    莉莉丝 "「这个号的座位现在不就在我们眼前吗？」"
    志雄 "「……诶？」"
    "我仔细比较起座位上写的号码和车票上的号码……"
    "啊，是真的。"
    voice "NRI08A_RI005"
    莉莉丝 "「……真笨。」"
    "与其说是在责备我，不如说是无奈的感叹。"
    志雄 "「对不起，灯光有些昏暗……」"
    voice "NRI08A_RI006"
    莉莉丝 "「不过，找到就好了。那么，我们坐下吧。给。」"
    "莉莉丝突然把旅行用的包塞给我。"
    志雄 "「……？」"
    voice "NRI08A_RI007"
    莉莉丝 "「真是的。这种事总该懂吧。帮我把包放到架子上去啊。」"
    志雄 "「好、好的。莉莉丝没办法把它放上去是吧？」"
    voice "NRI08A_RI008"
    莉莉丝 "「你，你说什么！」"
    "与此同时，莉莉丝的脚瞬间就动了一下。扫堂腿吗！？扫堂腿要来了吗！？"
    志雄 "「……」"
    "我为了从容应对莉莉丝的扫堂腿，赶快摆好防御姿势。"
    "……不过，预料之中的扫堂腿却没有到来。"
    voice "NRI08A_RI009"
    莉莉丝 "「你真是失礼呢。」"
    志雄 "「……」"
    "我还以为这次的扫堂腿攻击力系数极高呢……最近莉莉丝的态度似乎变得有些过于温和了吧。"
    voice "NRI08A_RI010"
    莉莉丝 "「什么嘛，这似笑非笑的猥琐表情。好了啦，快点把包放上去！」"
    志雄 "「知道了。」"
    "我接过莉莉丝递过来的包，放到座位上方的架子上。"
    voice "NRI08A_RI011"
    莉莉丝 "「……谢谢。」"
    志雄 "「没什么，不客气。」"
    window hide
    play sound "SE06_30"
    voice "NRI08A_XB001"
    車内放送の声 "「车门就要关上了～请大家注意～」"
    stop se
    voice "NRI08A_XB002"
    車内放送の声 "「列车正在启动～」"
    stop music fadeout 1
    play sound "SE06_17L"
    "正当我站起来准备把行李放上去的时候，电车突然动了起来。我瞬间失去了平衡。"
    志雄 "「哇！？」"
    voice "NRI08A_RI012"
    莉莉丝 "「喂，喂！」"
    "……而且，倒向的正好是莉莉丝的方向……"
    window hide
#EFF_STPC 0,EFF_SKIP
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/EXBG03AA4@2x.png" as bg0 zorder 0 with dissolve
#BG_ZOOM_RATE 0,8
#CHR_INIC 1
#CHR_POSC 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBA04"),"True","img/RI_XBA04A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
    with dissolve
#EFF_STAC 0,QUAKE_H_02,EFF_SKIP
#BG_ALP_AUTOC 3,0,0
#BG_ALPC 3
    hide bg3 with dissolve
    志雄 "「唔！」"
    "我立刻用脚使劲往地上撑。同时，莉莉丝也伸出手来支撑我——"
    window hide
#EFF_STPC 0,EFF_NOSKIP
#EFF_STPC 1,EFF_NOSKIP
    志雄 "「……啊，好险。」"
    "莉莉丝用力地撑住我的身体。"
    志雄 "「真、真不好意思，我没想到它会突然启动。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_XBB01"),"True","img/RI_XBB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI013"
    莉莉丝 "「没事，没关系的。」"
    play music  "BGM10"
    "和刚才一样，莉莉丝又很自然地说了些完全出乎我意料的言辞。"
    "看着她的侧脸，像是在恶作剧般的微笑。"
    "能和莉莉丝两人这么自然地对话，总觉得心情很舒畅。"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#GRAPH_INI 
    pause (32/32.0)
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/EXBG03AB@2x.png" as bg0
    show expression "img/trainoutside0@2x.png" as train_bg zorder -5:
        align (0,0)
    show expression "img/trainoutside_tree0@2x.png" as train_tree1 zorder -2:
        ycenter .2
        block:
            xcenter .4
            linear 0.3 xcenter -.1
            repeat
    with dissolve
#EFF_STAC 0,TRAINWINDOW,EFF_NOSKIP
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,125
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBF01"),"True","img/RI_ZBF01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
#SE_VOLC 1,255
#FADE_IN 1
#DICT_SET_GRP_SHIKADEN
    $persistent.dictlist[22]=True
    $persistent.dictlist[56]=True
    $persistent.dictlist[19]=True
    $persistent.dictlist[26]=True
    $persistent.dictlist[32]=True
    voice "NRI08A_RI014"
    莉莉丝 "「哇，景色在往后退耶。同样是电车，和芦鹿电简直是天壤之别。」"
    "看着窗外的景色，莉莉丝兴奋得像个孩子。"
    志雄 "「……我们两个人去，真的好吗？」"
    "虽然富美子婆婆说了不要紧，可是，就我们两个去的话，对于对方来说，就相当于去了两个陌生人一样。"
    志雄 "「到达旅馆的时候，不会被吼道『你们是谁啊，给我回去』之类的话吧……」"
    voice "NRI08A_RI015"
    莉莉丝 "「婆婆都说没事了，你就放心吧。」"
    志雄 "「嗯，说的也是。」"
#EXT_POS_AUTOC 0,0,132,,320,,50
    "富美子婆婆的确不会什么都不考虑就让我们去的。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBG02"),"True","img/RI_ZBG02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI016"
    莉莉丝 "「比起这个……那个……」"
    志雄 "「……？」"
    voice "NRI08A_RI017"
    莉莉丝 "「怎么说呢……这种话……」"
    志雄 "「我知道了，厕所的话就在旁边的车厢里。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBI04"),"True","img/RI_ZBI04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI018"
    莉莉丝 "「不、不是啦！真是的！」"
    志雄 "「都这时候了你还在顾虑什么啊。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBI05"),"True","img/RI_ZBI05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI019"
    莉莉丝 "「不和你说了，真是……」"
    志雄 "「……？啊，说起来……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBF04"),"True","img/RI_ZBF04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI020"
    莉莉丝 "「什么？」"
    "正望着窗外的莉莉丝把视线转移到我身上。"
    志雄 "「莉莉丝有什么诸如『有了这个就好了』之类的东西吗？」"
    "总之，先想想莉莉丝的生日礼物该怎么办吧。"
    voice "NRI08A_RI021"
    莉莉丝 "「有了这个就好了？什么啊？」"
    志雄 "「那个，稍微做个小的调查」"
    莉莉丝 "「我想想……{w=4}{nw}"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBI01"),"True","img/RI_ZBI01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI022B"
    extend "啊啊，早上起来时有那种能瞬间移动到学校的瞬间移动装置就好了。」"
    志雄 "「那只是因为莉莉丝早上起不来的关系吧……能像普通人一样起来的话，根本不需要这种装置吧。而且，你想穿着睡衣去学校吗？」"
    voice "NRI08A_RI023A"
    莉莉丝 "「其他还有……{w=4}{nw}"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBH02"),"True","img/RI_ZBH02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI023B"
    extend "嗯，吃下去就能变聪明的面包之类的。」"
    志雄 "「那个……能不能不要提那种把人类的欲望显露无疑的东西，有没有更加……微小一点、普通一点的想要的东西？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBH05"),"True","img/RI_ZBH05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI024"
    莉莉丝 "「更加微小的东西……比如说糖果吗？」"
    志雄 "「那个……那个也太微小了吧。」"
    "生日礼物送糖果总不太好吧。送这种东西的话，之后不知道会被她怎么说了。"
    志雄 "「嗯，那之外的东西还有吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBF01"),"True","img/RI_ZBF01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI025"
    莉莉丝 "「我不是那种对东西很执着的人。啊，洋装之类的或许也不错。」"
    "洋装吗……要考虑尺寸的话，还是很有难度的。"
    "而且，以我的品味选择的衣服是不是适合她穿，也还是个大问题。"
    "果然，要问出合适的答案真不容易呢。不过反正也不是当天就回来的旅行，慢慢问就好了。"
    志雄 "「说起来，你带学习用具了吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBF03"),"True","img/RI_ZBF03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI026"
    莉莉丝 "「诶？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBH06"),"True","img/RI_ZBH06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI027"
    莉莉丝 "「啊，那个啊～啊哈哈……」"
    "莉莉丝想蒙混过关似得笑着。还真是意料之中啊……"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBI01"),"True","img/RI_ZBI01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI028"
    莉莉丝 "「这样不也挺好吗？难得的旅行，应该更放松地去享受嘛！」"
    志雄 "「最近我真的开始担心你和亨了……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBI04"),"True","img/RI_ZBI04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI029"
    莉莉丝 "「烦、烦死了。总会有办法的，总会有的！」"
    志雄 "「是啦是啦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBF05"),"True","img/RI_ZBF05A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI030"
    莉莉丝 "「什、什么啊，这种口气！？」"
    voice "NRI08A_RI031"
    莉莉丝 "「再说，你自己的方向不也没决定吗？」"
    志雄 "「唔……」"
    "这下换我哑口无言了……毕竟她说的也是事实。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBI01"),"True","img/RI_ZBI01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI032"
    莉莉丝 "「哈哈～」"
    志雄 "「不要露出这种炫耀胜利般的微笑好不好……」"
    "……像这种你来我往，互相交锋的交流，对我们来说已经是家常便饭了。"
    window hide
#FADE_OUT 1
#CHR_ALPC 0
#FADE_IN 0
    "在成为恋人之前，还有之后都没什么变化。也许对我们来说，着就是最好的关系了吧。"
    window hide
#EFF_STPC 0,EFF_NOSKIP
#BG_SET_BACK
#CHR_SET_BACK
#BG_INIC 1
#BG_PRI 1
#BG_INIC 2
#CHR_INIC 1
#BG_ALPC 0
#BG_ALPC 2
    show expression "img/BG50AA@2x.jpg" as bg2 zorder 200 with dissolve
#CHR_POSC 1
#CHR_COLC 1,128,136,136
    hide lh11
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'TO'",DynamicDisplayable(mouthanime,"TO_XBA01"),"True","img/TO_XBA01A@2x.png") as lh11 zorder (1000-11):
        ypos 0.0
    with dissolve
    hide bg1 with dissolve
#MUS_VOL 0
#SE_VOLC 1,0
    voice "NRI05A_TO035_K"
    亨 "「所以，这不是一个很好的机会吗？　处在不同的环境下的话，人也会变得稍微大胆些的。」"
    "虽然亨这么说，可我们这样不也很好吗……"
    window hide
#SE_VOLC 1,255
#MUS_VOL 128
#CHR_PRIC 1
#BG_PRI 2
#BG_INIC 1
#BG_PRI 1
    hide bg2
    hide lh11
    with dissolve
#BG_COLC 0,128,128,128
#BG_ALPC 0
    scene expression "img/EXBG03AB@2x.png" as bg0 zorder 0
    show expression "img/trainoutside0@2x.png" as train_bg zorder -5:
        align (0,0)
    show expression "img/trainoutside_tree0@2x.png" as train_tree1 zorder -2:
        ycenter .2
        block:
            xcenter .4
            linear 0.3 xcenter -.1
            repeat
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBI01"),"True","img/RI_ZBI01A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    hide bg1 with dissolve
    voice "NRI08A_XC000"
    車内販売の売り子 "「要买饮料和食品吗？」"
    "说着，售物员的推车朝这边靠近过来。"
    志雄 "「莉莉丝，想喝点什么吗？」"
    voice "NRI08A_RI033"
    莉莉丝 "「嗯～说的也是，我也有些渴了。有没有茶之类的东西？」"
    志雄 "「那么……不好意思！给我一瓶绿茶。」"
    voice "NRI08A_XC001"
    車内販売の売り子 "「给。１５０元。」"
    play sound "SE03_03"
    "我把钱给她然后接过瓶子。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA04"),"True","img/RI_ZBA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI034"
    莉莉丝 "「你的呢？」"
    志雄 "「我没关系，我不渴。」"
    voice "NRI08A_RI035"
    莉莉丝 "「是吗？」"
    play sound "SE03_03"
    "莉莉丝给了我１５０元，接过茶瓶，打开盖子。"
    voice "EV99_ET000"
    女性客 "「给我一个装三明治的袋子～」"
    "一旁的乘客从贩卖员那儿买了一份三明治。看样子和我们一样，是面对面的一对情侣。"
    "手推车经过后，女乘客手拿着三明治送到对面男人的口中。"
    voice "EV99_ET001"
    女性客 "「给，把嘴张开～」"
    "男人很幸福地咬了一口。"
    "哦，没想到在大庭广众之下还真有人做这种事。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBB02"),"True","img/RI_ZBB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    莉莉丝 "「…………」"
    志雄 "「怎么了？」"
    "莉莉丝满脸通红，目不转睛地看着一旁的座位。"
    "接着，她又把视线转移到了手上的瓶子，喃喃自语。"
    voice "NRI08A_RI037"
    莉莉丝 "「……唔……可是……唔唔……」"
    志雄 "「怎、怎么了？肚子疼吗？」"
    voice "NRI08A_RI038"
    莉莉丝 "「不，不是啦……我是在想……」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBC06"),"True","img/RI_ZBC06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "莉莉丝转向一侧，然后把瓶子塞到我身前。"
    stop music fadeout 1
    voice "NRI08A_RI039"
    莉莉丝 "「……这个，要、要喝吗？」"
    志雄 "「哎……」"
    "……这难道是想对刚才那种状况的再现吗？不过，如果加上有间接接吻这点，我们这边应该更耀眼一些吧。"
    志雄 "「……我，我不用了。」"
    window hide
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA02"),"True","img/RI_ZBA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play music  "OBGM18"
    voice "NRI08A_RI040"
    莉莉丝 "「什、什么嘛。我的茶就不能喝吗？」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD04"),"True","img/RI_ZBD04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI041"
    莉莉丝 "「难得我允许你喝我的茶，快点喝！」"
    志雄 "「等、等一下！」"
    "你是被醉酒后的老爸附体了吗？"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD02"),"True","img/RI_ZBD02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI042"
    莉莉丝 "「好了！快点喝啦！」"
    "莉莉丝扭扭捏捏地把瓶子往我这边塞。"
    志雄 "「唔，等一下啦！」"
    "我有些粗暴地握住莉莉丝的手，把瓶子推了回去。"
    stop music fadeout 18
    play sound "SE03_11"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA03"),"True","img/RI_ZBA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI042A"
    莉莉丝・志雄 "「啊……」"
    "我和莉莉丝异口同声地叫道，同时，瓶子从莉莉丝的手中掉了下去。"
    志雄 "「危险……！」"
    "我迅速地伸出手……好的，抓住了！"
    "可是——"
    志雄 "「哦哦！？」"
    window hide
#BG_SET_BACK 
#BG_INIC 3
    #scene expression "img/BG_SPEC1@2x.jpg" as bg3 zorder 3 with dissolve
    play sound "SE03_07"
#EFF_STAC 0,QUAKE_WITH_ZOOM,EFF_NOSKIP
#VIB_DOUKI
#FADE_OUT 0
#BG_INIC 0
    
    hide lh0 with dissolve
    hide bg3 with dissolve
    pause (32/32.0)
#VIB_STP 5
#GRAPH_INI 
#BG_SET_BACK 
#FADE_IN 0
    "我没办法控制住自己的重心，倒在了莉莉丝的位子上——"
    voice "NRI08A_RI043"
    莉莉丝 "「干、干什么啊——！？」"
    window hide
#FADE_OUT 0
#SE_VOLC 1,0
#BG_SET_BACK 
#BG_INIC 1
    $persistent.albumlist[persistent.albuminfo.index("EVN_RI03")]=True
    show expression "img/EVN_RI03@2x.jpg" as bg1 zorder 1 with dissolve
#FADE_IN 1
    play music  "OBGM19"
    voice "NRI08A_RI044"
    莉莉丝 "「啊……」"
    "这下我整个人倒在了莉莉丝的怀中，宛然一种被她拥抱着的感觉。"
    "眼前就是莉莉丝的脸。"
    "娇小，华丽，柔软的身体……苗条的腰部。"
    "花般的发香——"
    voice "NRI08A_RI045"
    莉莉丝 "「…………你想抱到什么时候啊？」"
    志雄 "「对，对不起！」"
    window hide
#FADE_OUT 1
#BG_SET_BACK 
#BG_INIC 0
#BG_PRI 0
    scene expression "img/EXBG03AB@2x.png" as bg0 zorder 0 with dissolve
    show expression "img/trainoutside0@2x.png" as train_bg zorder -5:
        align (0,0)
    show expression "img/trainoutside_tree0@2x.png" as train_tree1 zorder -2:
        ycenter .2
        block:
            xcenter .4
            linear 0.3 xcenter -.1
            repeat
    with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_PRIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBA05"),"True","img/RI_ZBA05A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    stop music fadeout 18
#SE_VOLC 1,255
#EFF_STAC 0,TRAINWINDOW,EFF_NOSKIP
#FADE_IN 1
    voice "NRI08A_RI046"
    莉莉丝 "「你这个笨蛋！」"
    play sound "SE04_08"
#THREAD_STA 1,THREAD_QUA_WIN
#VIB_DOKA 
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
    志雄 "「好疼！」"
#MESA A_CH_SI,"【志雄】「好疼！」"
#THREAD_WAT 1
#WIN_POS 0,0
#VIB_STP 5
#MESX "%K%P"
    window hide
    play music  "BGM02"
    voice "NRI08A_RI047"
    莉莉丝 "「……一不留心就这副德行！」"
    voice "NRI08A_RI048"
    莉莉丝 "「志雄的内心中也沉睡着野兽呢……我得赶快发邮件通知婆婆。」"
    志雄 "「不要啊！而且，从根本上来说，也是你做这种莫名其妙的事才导致的吧——」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'RI'",DynamicDisplayable(mouthanime,"RI_ZBD02"),"True","img/RI_ZBD02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NRI08A_RI049"
    莉莉丝 "「不要把别人当做借口！」"
    play sound "SE04_07"
    志雄 "「呃！」"
#THREAD_STA 1,THREAD_QUA_WIN
#VIB_DOKA 
    if persistent.autosave_scene:
         python:
            renpy.take_screenshot()
            renpy.save("auto-"+str(persistent.auto_slot))
            persistent.auto_slot+=1
            if persistent.auto_slot>6:
                persistent.auto_slot = 1
#MESA A_CH_SI,"【志雄】「呃！」"
#THREAD_WAT 1
#WIN_POS 0,0
#VIB_STP 5
#MESX "%K%P"
    "今天直到刚才为止还没有被踢过，还以为莉莉丝成熟些了，没想到……看来莉莉丝就是莉莉丝。"
    "……不过，这种争执在我们看来也是习以为常了。"
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
#label THREAD_QUA_WIN
#TH_QUAKE_WIN 4
#EOT
#label THREAD_QUA2_WIN
#TH_QUA2_WIN
#EOT