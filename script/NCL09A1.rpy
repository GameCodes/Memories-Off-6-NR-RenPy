label NCL09A1:
    $currentlabel = "NCL09A1"
    $chapter_title = persistent.scenenamelist[persistent.scenelabellist.index(currentlabel)]
    $persistent.scenelist[persistent.scenelabellist.index(currentlabel)] = True
    $month = '08'
    $day = '10'
    $date = '4'
    window hide
#FADE_OUT 0
    scene expression Solid("000") with fade
#FADE_IN 0
#CAL_DSP_GRP 2,CAL_0810
    show expression "img/NIMG15L-568h@2x.jpg" as cal zorder 5
    show expression "img/08_10_THURSDAY@2x.png" as cal_date zorder 6:
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
#BG_INIC 1
#BG_SETWC 0,1,BG15AA,NIMG01B
#BG_PRIC 1
#EFF_STAC 0,CLOUD_B,EFF_NOSKIP
    scene expression "img/BG15AA@2x.jpg" as bg0 with dissolve
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA02"),"True","img/CL_MAA02A@2x.png") as lh0 zorder (10-0):
        ypos 0.0
    with dissolve
    play sound "SE05_15L"
    pause (32/32.0)
#EFF_STAC 1,LENZ,EFF_SKIP
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
    志雄 "「好热啊……」"
    "我情不自禁地感叹道。"
    "我抬起手，擦了擦额头上的汗水，望向窗外。"
    "又是万里无云，碧空如洗。当然，太阳也灿烂地闪耀着。"
    "为了放松心情而打开的收音机里却播出了『今天是入夏以来气温最高的一天』这样令人恐慌的消息。"
    "我不禁无力地瘫坐在椅子上。"
    window hide
#EFF_STPC 0,EFF_NOSKIP
#EFF_STPC 1,EFF_NOSKIP
#SE_VOLC 1,(64/2)
    hide bg1 with dissolve
    play music "BGM04"
    voice "NCL09A_KU000"
    克罗艾 "「志雄真是的。休息还早了点儿哦。」"
    "与我一样汗如雨下的学姐，十分无奈地看着我说道。"
    "学姐的手里正拿着吸尘器。而我手里则抓着擦窗户用的抹布。"
    "是的。我和学姐，正在进行大扫除。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA03"),"True","img/CL_MAA03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU001"
    克罗艾 "「不快点做完扫除的话，一直都会这么热的哦？」"
    志雄 "「这个我知道了啦，可是通融一下，分担点工作到天凉的日子里……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA04"),"True","img/CL_MAA04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU002"
    克罗艾 "「俗话说，『言必信，行必果』不是吗？而且工作量如此巨大也是受累于志雄之前对扫除的『偷工减料』吧？」"
    志雄 "「那可不是偷懒啊，只是有些地方从我住进来开始就没动过的……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA02"),"True","img/CL_MAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU003"
    克罗艾 "「这就叫做偷懒了吧～」"
    "说到这里，学姐做出有些无奈的表情，又开动了吸尘器。"
    window hide
    play sound "SE06_18"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    志雄 "「是……」"
    "我微微地叹了口气，从椅子上站起来继续擦起窗户。"
    "为了给屋里通风，所有的窗户都打开了，空调自然也就关掉了。"
    "正因为如此，屋外的热气全部跑进屋里来了。"
    志雄 "「一时半会儿根本干不完啊……」"
    "为了重回科技所创造的天堂，我只好一心一意地回到了扫除工作中。"
    window hide
    stop se fadeout 1
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG33AA@2x.jpg" as bg0 zorder 0 with dissolve
    pause (32/32.0)
#FADE_IN 1
    "……１小时之后，整个房间的扫除终于完成了。"
    "我立刻关上所有的窗户，打开了空调。"
    "出风口送出的凉风，让早已汗流浃背的我立刻清爽了起来。"
    志雄 "「啊，活过来了～」"
    "情不自禁地发出这样的感叹。"
#CHR_INIC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB06"),"True","img/CL_LAB06A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    voice "NCL09A_KU004"
    克罗艾 "「志雄真是的，太夸张了吧？」"
    "面对这样的情境，克罗艾学姐无奈地笑着，递给我泡好的凉茶。"
    志雄 "「太感谢了！」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB02"),"True","img/CL_LAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU005"
    克罗艾 "「不用客气。如果对这次打扫心有余悸的话，往后，就要多注意好好搞卫生哦。」"
    志雄 "「说的是呢。今天真是留下了无比深刻的『夏之噩梦』……」"
    "说着，我一口气喝完了整杯凉茶。"
    window hide
    stop music fadeout 1
    play sound "SE02_00L"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB03"),"True","img/CL_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    "这时，放在屋里的手机响了起来。"
    志雄 "「谁会在这个时候打来……？」"
#SE_VOLC 0,255
    scene expression "img/BG15AA@2x.jpg" as bg_over zorder 2 with dissolve
    "我走进房间，迅速地拿起手机，确认了屏幕上的来电显示。"
    "……亨打来的么？"
    window hide
    play sound "SE02_03"
    志雄 "「喂，亨吗？」"
    window hide
    play music "BGM09"
    voice "NCL09A_TO000_K"
    亨 "「啊，喂，志雄……」"
    "电话里传来的，是许久不见的亨的声音。"
    志雄 "「怎么了呢，突然找我。」"
    voice "NCL09A_TO001_K"
    亨 "「啊，其实是有事情要和你商量啦……」"
    "亨在电话那头用极其认真的声音说着。那郑重的语气让我也不禁认真起来。"
    志雄 "「到底是什么事情要和我商量啊？」"
#MUS_VOL 0
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NCL09A_TO002_K"
    亨 "「今天，做火锅吧～」"
    play sound "SE07_13"
#WIN_POS_BEZIER 80,30,130,50,160,140,50
    pause (64/32.0)
#MUS_VOL 128
#WIN_POS 0,0
    志雄 "「啊——！？火锅！？」"
    "用那样郑重的语气说出的这个词语，我不禁怀疑起自己的听觉了。"
    voice "NCL09A_TO003_K"
    亨 "「对，火锅。大家带上各种食材到你家，一起开火锅派对吧！」"
    "再一次确认了亨所说出的那个词，结果思维却更混乱了，这么热的天气里吃火锅？"
    志雄 "「你没病吧？难道天太热你脑子热成浆糊了？」"
    voice "NCL09A_TO004_K"
    亨 "「天气预报里说，今天是入夏以来最热的一天不是吗？」"
    "说起来，收音机里确实是这么说的。"
    志雄 "「啊，是啊。所以我才问你受到了什么刺想到这种活动啊！」"
    voice "NCL09A_TO005_K"
    亨 "「啊，别着急啊。这么热的天里，怎样都有些食欲不振吧？所以这种时候就要做一些提起食欲的东西才行吧。」"
    志雄 "「就好比三伏天里的丑日要吃鳗鱼那样？」"
    voice "NCL09A_TO006_K"
    亨 "「就是如此。不过你想，鳗鱼很贵吧？」"
    志雄 "「那倒是。」"
    voice "NCL09A_TO007_K"
    亨 "「吃鳗鱼显然不现实，吃别的又提不起食欲。那么既经济又能打牙祭的活动，就是火锅了。」"
    "亨说的倒是有些道理……"
    志雄 "「那么，又为什么定在了我家啊。」"
    voice "NCL09A_TO008_K"
    亨 "「暑假之后咱们也一直都没见过吧？想借此机会好好见见面嘛～」"
    "听了这话我稍微有些感动。"
    "说起来，除了学生会成员以及奏云祭的执行委员之外，这个夏天都没有和朋友们碰过面。和亨也有很久很久没见过了。"
    voice "NCL09A_TO009_K"
    亨 "「怎么样，是个好主意吧？」"
    志雄 "「嗯。这么说来倒是不错呢。」"
    "大家一起玩玩闹闹也不坏，对为了家里的事情正在烦恼的学姐来说，也有助于恢复活力。稍微热闹一下心情也会随之变好的吧。"
    "当然，毕竟举行地点在我家，还得和学姐商量一下。"
    志雄 "「那个，稍微等我一下好吧？」"
    voice "NCL09A_TO010_K"
    亨 "「诶？这倒是没什么啦……」"
#MUS_VOL 64
    "于是我按下了手机上的通话保持按键，去向在客厅休息的学姐征求意见。"
    show expression "img/BG33AA@2x.jpg" as bg_over zorder 2 with dissolve
    志雄 "「学姐，有点事想问你可以吗～？」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA01"),"True","img/CL_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU006"
    克罗艾 "「怎么了啊？」"
    志雄 "「亨他问要不要办个火锅派对呢。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA02"),"True","img/CL_MAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU007"
    克罗艾 "「火锅？这么热的天里？」"
    志雄 "「那家伙说正是因为天热的缘故。好久不见大家了想聚一下，所以想问问学姐的意见」"
    "对亨的提案做了少许的思考后，学姐莞尔一笑地点头了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB06"),"True","img/CL_MAB06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU008"
    克罗艾 "「嗯，有什么不行的呢，大家会很开心的吧」"
    志雄 "「那，学姐也参加喽？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU009"
    克罗艾 "「嗯，如果不会给你添麻烦的话。」"
    志雄 "「当然没问题。不过，食材要大家各自都带一些，所以，我们一会儿还得出去买点儿。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB02"),"True","img/CL_MAB02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    克罗艾 "「对呢……{w=3}{nw}"
#MESA A_CH_KU,NCL09A_KU010A,"【クロエ】「对呢……"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB04"),"True","img/CL_MAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU010B"
    extend "那个，可不可以……」"
    "说到这里，学姐用央求的目光试探着我的意见般地说道。"
    志雄 "「怎么了啊？」"
    voice "NCL09A_KU011"
    克罗艾 "「如果方便的话……可不可以把诺艾儿也带来呢？」"
    志雄 "「让诺艾儿也过来吗？」"
    voice "NCL09A_KU012"
    克罗艾 "「那孩子到日本来的时间还很短呢，不是吗？所以我想她一定会很喜欢这种派对的吧。」"
    志雄 "「那样的话，得先确认一下诺艾儿是不是能来才行哦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA07"),"True","img/CL_MAA07A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU013"
    克罗艾 "「谢谢你，志雄～」"
    志雄 "「总之我先告诉亨要多来两个人吧。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA01"),"True","img/CL_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU014"
    克罗艾 "「嗯，拜托你了。」"
    scene expression "img/BG15AA@2x.jpg" as bg_over zorder 2 with dissolve
    "我解除了手机的通话保持状态，继续和亨说道。"
#MUS_VOL 128
    志雄 "「喂，还在吗？」"
    voice "NCL09A_TO011_K"
    亨 "「哦，于是，怎么样了？」"
    志雄 "「火锅派对，我参加了。然后，我再叫两个人一起可以吗？」"
    voice "NCL09A_TO012_K"
    亨 "「啊，这倒没什么关系啦。火锅还是人越多越好吧～」"
    志雄 "「那么，你都叫谁了呢？」"
    voice "NCL09A_TO013_K"
    亨 "「我叫了莉莉丝还有智纱」"
    志雄 "「……这样啊。其实你只是是想见莉莉丝而已吧？」"
    voice "NCL09A_TO014_K"
    亨 "「当然了！」"
    "居然直接承认了。想到刚才还为他看似真挚的话语而感动，浑身起满了鸡皮疙瘩。"
    voice "NCL09A_TO015_K"
    亨 "「那个，莉莉丝好像说还要叫上铃呢。」"
    voice "NCL09A_TO016_K"
    亨 "「那，你都叫谁了呢？」"
    志雄 "「学姐和她家人。」"
    voice "NCL09A_TO017_K"
    亨 "「什么！？已经和学姐一家这么亲近了吗……真行呢，志雄！」"
    志雄 "「没有啦……」"
    "对学姐一家来说，我还远远谈不上亲近吧……"
    志雄 "「那一会儿再联系吧。」"
    voice "NCL09A_TO018_K"
    亨 "「恩。」"
    window hide
    stop music fadeout 1
    play sound "SE02_08"
    志雄 "「唉，真是没办法呢……」"
    play sound "SE02_03"
    "挂断了通话，我才想起大扫除时刚刚收拾起来的大锅和燃气灶……不禁无奈的叹了口气。"
    "对了，还要去接诺艾儿呢……"
    志雄 "「不对……」"
    "比起这些，眼下更应该让克罗艾学姐打个电话比较好吧。"
    "那样的话学姐的母亲也能放心，说不定是个能消除两人的隔阂的好机会。"
    show expression "img/BG33AA@2x.jpg" as bg_over zorder 2 with dissolve
    志雄 "「接下来，给学姐家打个电话吧。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320+160)
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA01"),"True","img/CL_MAA01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU015"
    克罗艾 "「嗯，拜托了……」"
    志雄 "「不是该学姐来打吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA02"),"True","img/CL_MAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU016"
    克罗艾 "「诶？可是……」"
    志雄 "「我想，还是学姐以姐姐的身份叫出诺艾儿更合适吧。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA06"),"True","img/CL_MAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU017"
    克罗艾 "「也对呢……」"
    "学姐有些紧张地拿起了电话听筒，手指在数字按键上犹豫了一会儿，又回头看向我。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA02"),"True","img/CL_MAA02A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU018"
    克罗艾 "「那个，志雄。有件事想求你……」"
    志雄 "「什么事啊？」"
    voice "NCL09A_KU019"
    克罗艾 "「打电话的时候，能留在我身边吗？」"
    志雄 "「这点事情当然没问题，学姐就放心打吧～」"
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
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA07"),"True","img/CL_LAA07A@2x.png") as lh0 zorder 100:
        ypos 0.0
    with dissolve
    "我知道，她需要来自身外的力量去推她一把，而这就是我的职责。我走到学姐身边，握住她那只犹豫不决的手，十指相扣。"
    voice "NCL09A_KU020"
    克罗艾 "「嗯……那我打了。」"
    window hide
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAA06"),"True","img/CL_LAA06A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    play sound "SE02_10"
    pause (16/32.0)
    play sound "SE02_10"
    pause (12/32.0)
    play sound "SE02_10"
    "克罗艾学姐再次拿起了电话听筒，这次，她拨了自己家的号码。"
    window hide
    play sound "SE02_06L"
    "在几声通话音之后，学姐母亲的声音传了出来。"
    play sound "SE02_08"
#FADE_OUT_STA 256
    voice "NCL09A_KU021"
    克罗艾 "「喂，是我……嗯，嗯。那个……」"
    window hide
#FADE_WAT 1
    pause (64/32.0)
#FADE_IN 1
    play music "OBGM08"
    voice "NCL09A_KU022"
    克罗艾 "「那就这样……嗯……我知道了……」"
    play sound "SE02_07"
    "打完电话的学姐，放下听筒长出了一口气。"
    志雄 "「怎么样？」"
    voice "NCL09A_KU023"
    克罗艾 "「嗯。因为是很难得的机会，所以很认真地拜托了妈妈。接下来只要去接诺艾儿就行了。」"
    志雄 "「那顺道去买要准备的东西的吧。」"
    voice "NCL09A_KU024"
    克罗艾 "「嗯，好……」"
    志雄 "「然后，还得准备好做火锅用的大锅才行。」"
    voice "NCL09A_KU025"
    克罗艾 "「嗯……」"
    "学姐心不在焉地回答道。"
    志雄 "「学姐？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB03"),"True","img/CL_LAB03A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU026"
    克罗艾 "「……呃，什么？」"
    志雄 "「发生了什么吗？在那里发愣。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB04"),"True","img/CL_LAB04A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU027"
    克罗艾 "「没、没什么啦。」"
    志雄 "「不会吧，有什么在意的事情吗？」"
    "学姐躲避着我的视线打算逃避，不过很快就放弃般地叹了口气。"
    voice "NCL09A_KU028"
    克罗艾 "「嗯，不是那样的。只是……我从家跑出来，结果也没有说些什么……」"
    "学姐的声音里充满了无力感。"
    "学姐，果然是在想这些事情……"
    志雄 "「学姐……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC01"),"True","img/CL_LAC01A@2x.png") as lh0 zorder (10+0):
        ypos 0.0
    with dissolve
    voice "NCL09A_KU029"
    克罗艾 "「只是，这样而已。好了，去接诺艾儿吧。」"
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "学姐提高声调说完，便径直走向门口。"
    "无论怎么看都是强装出来的明快……"
    show expression "img/OIBG012A@2x.png" as bg_over zorder 2 with dissolve
    志雄 "「学姐，请等一下！」"
    "要是学姐多少能回复些精神就好了……来不及考虑更多，我赶忙跟在她身后走了出去。"
    window hide
    stop music fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop music fadeout 1
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG81AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG81AA@2x.jpg" as bg0 with dissolve
    play sound "SE05_15L"
    pause (32/32.0)
#FADE_IN 1
    "在这夏日里最猛烈阳光的炙烤下，我和学姐不停地擦着额头的汗珠。终于，抵达了目的地。"
    window hide
#SE_VOLC 1,(64/2)
#CHR_SET_BACK
#CHR_INIC 1
#CHR_INIC 2
#CHR_POSC 1,(320-160)
#CHR_POSC 2,(320+160)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA01"),"True","img/CL_MAA01A@2x.png") as lh1 zorder (10+1):
        xcenter .25
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh2 zorder (10+2):
        xcenter .75
    voice "NCL09A_KU030"
    克罗艾 "「那么，诺艾儿就交给我吧。」"
    voice "NCL09A_EL000B"
    爱丽丝 "「嗯，拜托了哦。」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_ALPC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA09"),"True","img/NO_MBA09A@2x.png") as lh0 zorder (10-0):
        ypos .2
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR0 128
#MOV_CHR1 ,(320-192)
#MOV_CHR2 ,(320+192)
#MOV_CHR_GO 1
    play music "BGM08"
    voice "NCL09A_NO000"
    诺艾儿 "「呐，火锅派对是什么啊？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCL09A_KU031"
    克罗艾 "「那个呢，是把食物都放进锅里一起煮，然后大家一起来吃的料理派对哦～」"
    "面对诺艾儿天真无邪的提问，学姐耐心的回答道。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB02"),"True","img/NO_MBB02A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO001"
    诺艾儿 "「好开心！」"
    "听完说明，她便欢呼了起来。诺艾儿今天也依然朝气十足。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB06"),"True","img/CL_MAB06A@2x.png") as lh1 zorder (10+1):
        xcenter .35
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA02"),"True","img/YS_MAA02A@2x.png") as lh2 zorder (10+2):
        xcenter .65
    voice "NCL09A_EL001"
    爱丽丝 "「诺艾儿，不要给克罗艾姐姐和志雄哥哥添麻烦哦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA02"),"True","img/NO_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO002"
    诺艾儿 "「好～的～」"
    window hide
    hide lh0 with dissolve
    "刚说完，诺艾儿就顺着道路跑了出去，学姐和母亲慌忙一起喊道。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA03"),"True","img/CL_MAA03A@2x.png") as lh1 zorder (10+1):
        xcenter .35
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA06"),"True","img/YS_MAA06A@2x.png") as lh2 zorder (10+2):
        xcenter .65
    voice "NCL09A_EL002"
    爱丽丝 "「喂，说了不要单独跑开了吧！」"
    voice "NCL09A_KU032"
    克罗艾 "「诺艾儿，那样很危险所以不可以自己在马路上跑哦！」"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA04"),"True","img/NO_MBA04A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO003"
    诺艾儿 "「妈妈和姐姐担心过头了啦～」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAA02"),"True","img/CL_MAA02A@2x.png") as lh1 zorder (10+1):
        xcenter .35
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA03"),"True","img/YS_MAA03A@2x.png") as lh2 zorder (10+2):
        xcenter .65
    voice "NCL09A_EL003"
    爱丽丝 "「可真是的……」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA01"),"True","img/YS_MAA01A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_EL004"
    爱丽丝 "「真是感谢二位呢。这孩子呢，一听说你们要带她出去就高兴得不得了。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA01"),"True","img/NO_MBA01A@2x.png") as lh0 zorder (10+0):
        ypos .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB01"),"True","img/CL_MAB01A@2x.png") as lh1 zorder (10+1):
        xcenter .35
    志雄 "「哪里，火锅还是大家一起吃才开心嘛。」"
    "大概是被诺艾儿的天真浪漫影响了，我也很愉快地露出了笑容。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC01"),"True","img/CL_MAC01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .35
    with dissolve
    voice "NCL09A_KU033"
    克罗艾 "「那妈妈，我们走了哦。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA02"),"True","img/NO_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO004"
    诺艾儿 "「那，我出去了～」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'YS'",DynamicDisplayable(mouthanime,"YS_MAA02"),"True","img/YS_MAA02A@2x.png") as lh2 zorder (10+2):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_EL005"
    爱丽丝 "「好，大家要多注意安全。」"
    志雄 "「嗯，那我们出发了。」"
    window hide
#SE_VOLC 1,128
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "与学姐的母亲告别后，我们一起出发，前去选购食材。"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    show expression "img/BG04AA@2x.jpg" as bg0 zorder 0 with dissolve
    scene expression "img/BG04AA@2x.jpg" as bg0 with dissolve
#SE_VOLC 1,(64/2)
#FADE_IN 1
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA02"),"True","img/NO_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO005"
    诺艾儿 "「火锅火锅，真开心～」"
    window hide
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+160)
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC04"),"True","img/CL_MAC04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_KU034"
    克罗艾 "「好啦，诺艾儿。那样很危险啦……」"
    "显然，诺艾儿对火锅派对满怀期待，一路上蹦蹦跳跳的。克罗艾学姐无奈地牵住了她的手。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA09"),"True","img/NO_MBA09A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO006"
    诺艾儿 "「为什么要牵着手呢？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC01"),"True","img/CL_MAC01A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .75
    with dissolve
    voice "NCL09A_KU035"
    克罗艾 "「因为，在马路上蹦蹦跳跳的话很危险的啊。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB02"),"True","img/NO_LBB02A@2x.png") as lh0 zorder (10-0):
        ypos 0.2
    with dissolve
    voice "NCL09A_NO007"
    诺艾儿 "「那，大哥哥也来！」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB03"),"True","img/CL_MAB03A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .75
    with dissolve
    志雄 "「诶？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB01"),"True","img/NO_LBB01A@2x.png") as lh0 zorder (10+0):
        ypos .2
    with dissolve
    voice "NCL09A_NO008"
    诺艾儿 "「大哥哥也来把手牵起来吧？」"
    志雄 "「好，来吧。」"
    "我伸出手去，牵住了诺艾儿的另一只小手。"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA02"),"True","img/NO_LBA02A@2x.png") as lh0 zorder (10+0):
        ypos .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB06"),"True","img/CL_MAB06A@2x.png") as lh1 zorder (10-1):
        xcenter .75
    voice "NCL09A_NO009"
    诺艾儿 "「嘿嘿嘿～」"
    window hide
#SE_VOLC 1,0
#FADE_OUT 1
    scene expression Solid("000") with fade
#BG_SET_BACK 
#BG_INIC 0
    scene expression "img/BG05AA@2x.jpg" as bg0 with dissolve
#SE_VOLC 1,128
#FADE_IN 1
    "快要到商店街了，诺艾儿还是乐此不疲的跳着。"
    window hide
#SE_VOLC 1,(64/2)
    hide bg1 with dissolve
#BG_SWPC 0
#BG_PRI 1
#BG_PRI 0
#BG_GET_NOC 1,F34
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-224),(448/8)
#CHR_POSC 1,(320+224)
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA01"),"True","img/NO_LBA01A@2x.png") as lh0 zorder (10+0):
        xcenter .15
        ypos 0.2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC01"),"True","img/CL_LAC01A@2x.png") as lh1 zorder (10-1):
        xcenter .85
        ypos 0.0

    hide bg1 with dissolve
#BG_BLUR 0
    voice "NCL09A_KU036"
    克罗艾 "「差不多，可以放开手走了吧……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA03"),"True","img/NO_LBA03A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .15
    with dissolve
    voice "NCL09A_NO010"
    诺艾儿 "「诶？不要嘛～」"
    "诺艾儿发出了不情愿的叫声。"
    志雄 "「好不容易牵着手走到这里，就再牵一会儿吧……」"
    "不知不觉就说出了这样的话。虽然稍微有些早，不过能这样像一家人一样一起出门也真是很高兴。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB05"),"True","img/CL_LAB05A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .85
    with dissolve
    voice "NCL09A_KU037"
    克罗艾 "「志雄……」"
    "听了我的主意，和我一起把诺艾儿夹在中间的学姐有些无奈地说道。"
    "诶？我是不是做错了什么？"
    "学姐叹了叹气，提醒我和诺艾儿。"
    voice "NCL09A_KU038"
    克罗艾 "「你们俩个啊，这样子会给别人添麻烦的不是吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA09"),"True","img/NO_LBA09A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .15
    with dissolve
    志雄 "「啊……」"
    "这样说起来，三个人一横行地并排走着，会影响到别的行人的。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB04"),"True","img/CL_LAB04A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .85
    with dissolve
    voice "NCL09A_KU039"
    克罗艾 "「再保持这个样子的话，会让别人困扰的，诺艾儿也很危险不是吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA04"),"True","img/NO_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .15
    with dissolve
    voice "NCL09A_NO011"
    诺艾儿 "「好～的……」"
    "诺艾儿一副不情愿的表情放开了我的手。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB06"),"True","img/CL_LAB06A@2x.png") as lh1 zorder (10-1):
        ypos 0.0
        xcenter .85
    with dissolve
    voice "NCL09A_KU040"
    克罗艾 "「很好。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB03"),"True","img/NO_LBB03A@2x.png") as lh0 zorder (10+0):
        ypos .2xcenter .15
    with dissolve
    "听了学姐的话，诺艾儿微微点了点头，眼神里充满了遗憾。"
    "真是有点可怜啊。"
    "虽然学姐说的是对的，不过我也很理解诺艾儿的心情。"
    "对了，我有办法了……"
    志雄 "「诺艾儿有什么喜欢吃的点心吗？」"
    voice "NCL09A_NO012"
    诺艾儿 "「巧克力……」"
    志雄 "「好，那作为诺艾儿这么听话的奖励，给你买巧克力哦。」"
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB08"),"True","img/NO_LBB08A@2x.png") as lh0 zorder (10+0):
        xcenter .15
        ypos .2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB05"),"True","img/CL_LAB05A@2x.png") as lh1 zorder (10+1):
        xcenter .85
    voice "NCL09A_NO013"
    诺艾儿 "「诶，真的吗！？」"
    志雄 "「可以吧，学姐？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB04"),"True","img/CL_LAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .85
    with dissolve
    voice "NCL09A_KU041"
    克罗艾 "「真是的。没办法呢，志雄太温柔了……」"
    "出乎意料的回应，这下我有点不知所措了。"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB02"),"True","img/NO_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .15
    with dissolve
    voice "NCL09A_NO014"
    诺艾儿 "「太好了！」"
    window hide
    play sound "SE01_02L"
    hide lh0 with dissolve
    "伴随着诺艾儿的欢呼声，我们走进了商店街。"
    window hide
#SE_VOLC 0
#CHR_SET_BACK
#CHR_INIC 2
#CHR_PRIC ID_ALL
#CHR_ALPC 2
#CHR_POSC 2,(320-96)
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_SBA02"),"True","img/NO_SBA02A@2x.png") as lh2 zorder (10-2):
        ypos .2
        xcenter .35
    with dissolve
#MOV_CHR_INIT 48
#MOV_CHR2 128
#MOV_FOCUS_BG 0
#MOV_CHR_GO 1
#CHR_PRIC ID_ALL
    voice "NCL09A_NO015"
    诺艾儿 "「喂！你们俩个，快点啦快点！」"
    window hide
#SE_VOLC 0,128
    hide lh2 with dissolve
    stop se fadeout 1
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC05"),"True","img/CL_LAC05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
    with dissolve
#BG_SET_BACK 
#REEK_CHR 1
#THREAD_STA 1,THREAD_CHR_ASE_BG3
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NCL09A_KU042"
    克罗艾 "「喂，诺艾儿！不看前面乱跑的话很危险的！」"
#THREAD_STP 1
#REMOVE_REEK_CHR 1
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "学姐慌忙地追赶在诺艾儿后面。"
    志雄 "「真是没办法啊……」"
    "刚一撒开手就被扔下的我，只好叹了口气，赶忙追了上去。"
    window hide
    stop sound fadeout 1
#FADE_OUT 1
    scene expression Solid("000") with fade
    stop se
    stop sound
#BG_SET_BACK 
#BG_INIC 0
#BG_INIC 1
#BG_PRIC 0
#BG_SETWC 0,1,NIMG01C,BG03EA
#BG_ALPC 1
#BG_PRIC 1
    show expression "img/NIMG01C@2x.png" as bg_over zorder 2
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
    with dissolve
    pause 2
    scene expression "img/BG03EA@2x.jpg" as bg0 with dissolve
    play sound "SE05_13L"
    pause (32/32.0)
#EFF_PRI 0
#EFF_STAC 0,CLOUD_C,EFF_SKIP
#FADE_IN 1
    志雄 "「真重啊……」"
    "对于我情不自禁地哀鸣，走在前面的学姐回过头露出一幅恶作剧一般的神情。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_PRIC 0
#CHR_PRIC 1
#CHR_ALPC 0
#CHR_ALPC 1
#CHR_POSC 0,(320-96)
#CHR_POSC 1,(320+96)
#CHR_COLC 0,128,120,112,128
#CHR_COLC 1,128,120,112,128
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA01"),"True","img/NO_MBA01A@2x.png") as lh0 zorder (10+0):
        xcenter .35
        ypos 0.2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC01"),"True","img/CL_MAC01A@2x.png") as lh1 zorder (10+1):
        xcenter .65
        ypos 0.0

#SE_VOLC 1,(64/2)
#ROUTINE_STA
#CHR_ALP_AUTOC 0,128,1,F24
#CHR_ALP_AUTOC 1,128,1,F24
#BG_ALP_AUTOC 1,128,1,F24
#ROUTINE_STP
#EFF_STPC 0,EFF_SKIP
#ROUTINE_STA
#EFF_PRI 0
#CHR_PRIC 1
#CHR_PRIC 0
#BG_SWPC 0
#BG_PRIC 0
#BG_PRIC 1
    hide bg1 with dissolve
#ROUTINE_STP
    voice "NCL09A_KU043"
    克罗艾 "「志雄可真不给力哦～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA02"),"True","img/NO_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .35
    with dissolve
    voice "NCL09A_NO016"
    诺艾儿 "「不给力哦～」"
    "诺艾儿天真地重复着学姐的戏言。"
    "东西买完了，我们踏上了回家的路程。"
    "克罗艾学姐和诺艾儿，在我前面牵着手信步徐行。"
    志雄 "「不是我说，这么多东西也确实太重了吧……」"
    "我拎起两手满满的购物袋向学姐示意。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAC04"),"True","img/CL_MAC04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_KU044"
    克罗艾 "「啊哈，那志雄想让女生来拎东西是吗？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB04"),"True","img/NO_MBB04A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .35
    with dissolve
    voice "NCL09A_NO017"
    诺艾儿 "「是吗～？」"
    "学姐的手里什么都没拿。而诺艾儿则是紧紧抱着装有巧克力的袋子。"
    "说到底也是我自己自愿要拎东西的。"
    "学姐和好奇心旺盛的诺艾儿两人把能逛的地方都逛了个遍。"
    "而且，无论如何我也做不到让女生拎这些重物……"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB02"),"True","img/CL_MAB02A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_KU045"
    克罗艾 "「那非要说的话，请问需不需要帮忙呢？」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBB01"),"True","img/NO_MBB01A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .35
    with dissolve
    志雄 "「请别小看我了！」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB06"),"True","img/CL_MAB06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    "既然说了这话，事到如今就只能乖乖地拎着东西了。"
    voice "NCL09A_KU046"
    克罗艾 "「那就别发牢骚努力拎着吧～」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA02"),"True","img/NO_MBA02A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .35
    with dissolve
    voice "NCL09A_NO018"
    诺艾儿 "「拎着吧～」"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "转过身去两人继续迈开了前行的步伐。在她们身后，是一边拎着沉重的东西一边追赶她们的我的身影。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
    show expression "img/BG04EA@2x.jpg" as bg0 zorder 0 with dissolve
    hide bg1 with dissolve
    pause (32/32.0)
#CHR_SET_BACK
#CHR_INIC 1
#CHR_POSC 1,(320+96)
#CHR_COLC 1,128,120,112,128
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_MAB03"),"True","img/CL_MAB03A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_KU047"
    克罗艾 "「啊！」"
    "走了一阵之后，克罗艾学姐突然停住了脚步。"
    window hide
#CHR_SET_BACK
#CHR_INIC 0
#CHR_POSC 0,(320-96)
#CHR_COLC 0,128,120,112,128
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_MBA09"),"True","img/NO_MBA09A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .35
    with dissolve
    voice "NCL09A_NO019"
    诺艾儿 "「怎么了……？」"
    "由于学姐突然停住脚步，一下子撞上了学姐的诺艾儿，不解地望着学姐的脸。"
    "从后面追上来的我也很在意地向学姐问道。"
    window hide
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    hide bg1 with dissolve
#BG_SWPC 0
#BG_PRI 1
#BG_PRI 0
#BG_GET_NOC 1,F34
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    #show expression "img/F34@2x.jpg" as bg0 zorder 0 with dissolve
#BG_BLUR 0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-96)
#CHR_POSC 1,(320+96)
#CHR_COLC 0,128,120,112,128
#CHR_COLC 1,128,120,112,128
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA09"),"True","img/NO_LBA09A@2x.png") as lh0 zorder (10+0):
        xcenter .35
        ypos 0.2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB03"),"True","img/CL_LAB03A@2x.png") as lh1 zorder (10+1):
        xcenter .65
        ypos 0.0

    hide bg1 with dissolve
#BG_GET_NOC 0,F34
#BG_SET_BACK 
#BG_INIC 3
#BG_ALPC 3
#BG_UVC 3,(640/2)+(640/16),(448/16),((640/8)*3),((448/8)*3)
    #show expression "img/F34@2x.jpg" as bg3 zorder 3 with dissolve
#CHR_SET_BACK
#CHR_INIC 2
#CHR_ALPC 2
#CHR_COLC 2,128,120,112,128
#CHR_SCLC 2,384,384
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XAC05"),"True","img/CL_XAC05A@2x.png") as lh1 zorder (10-2):
        ypos 0.0
        xcenter .65
    with dissolve
    志雄 "「怎么了啊？学姐？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB05"),"True","img/CL_LAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_KU048"
    克罗艾 "「刚想起来，家里的酱油已经没有了……」"
    志雄 "「啊？酱油一点都没有了吗？」"
    "面对我的提问，学姐脸上泛起了愁容。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB04"),"True","img/CL_LAB04A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_KU049"
    克罗艾 "「昨天做饭的时候用光了，本来想今天去买来着……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA04"),"True","img/NO_LBA04A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .35
    with dissolve
    voice "NCL09A_NO020"
    诺艾儿 "「酱、油？没有的话就吃不了火锅了吗？」"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB05"),"True","img/CL_LAB05A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_KU050"
    克罗艾 "「是啊。得赶紧去买呢」"
    "这里离家就两步路了。这么热的天里，还得走回商店街再去买酱油，显然是得不偿失的。"
    "所以，我向学姐提出了一个提案。"
    志雄 "「这样的话，就拜托其他的人买一下带来好了。」"
    window hide
#ROUTINE_STA
#CHR_PRIC 2
#CHR_POSC 2,(32)
#BG_ALP_AUTOC 3,128,1,F24
#BG_UV_AUTOC 3,(640/2),0,(640/2),(448/2),1,F24
#CHR_ALP_AUTOC 2,128,1,F24
#CHR_SCL_AUTOC 2,180,180,1,F24
#ROUTINE_STP
#BG_ALP_SAVEC 3
#BG_UV_SAVEC 3
#CHR_ALP_SAVEC 2
#CHR_SCL_SAVEC 2
#CHR_POS_SAVEC 2
#CHR_ERSWC 0,1
#BG_SET_BACK 
#REEK_CHR 2
#THREAD_STA 1,THREAD_CHR_ASE_BG1
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NCL09A_KU051"
    克罗艾 "「那可不行哦。酱油用完了这种事，多丢人……」"
#THREAD_STP 1
#REMOVE_REEK_CHR 0
    志雄 "「呃？这种事情不至于……」"
    hide lh2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_XAC03"),"True","img/CL_XAC03A@2x.png") as lh1 zorder (10+2):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_KU052"
    克罗艾 "「大家会觉得我是个不合格的女朋友吧……」"
    志雄 "「……？」"
    window hide
#BG_GET_NOC 3,F34
#BG_SET_BACK 
#BG_INIC 0
#BG_UVC 0,0,512,640,448
    #show expression "img/F34@2x.jpg" as bg0 zorder 0 with dissolve
#BG_BLUR 0
#CHR_SET_BACK
#CHR_INIC 0
#CHR_INIC 1
#CHR_POSC 0,(320-96),(448/8)
#CHR_POSC 1,(320+96)
#CHR_COLC 0,128,120,112,128
#CHR_COLC 1,128,120,112,128
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA09"),"True","img/NO_LBA09A@2x.png") as lh0 zorder (10+0):
        xcenter .35
        ypos 0.2
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC05"),"True","img/CL_LAC05A@2x.png") as lh1 zorder (10+1):
        xcenter .65
        ypos 0.0

#BG_ALP_AUTOC 3,0,1,F24,48
#CHR_ALP_AUTOC 2,0,1,F24,48
#BG_ALP_SAVEC 3
#CHR_ALP_SAVEC 2
    hide bg3 with dissolve
#BG_ALPC 3,128
    hide lh2 with dissolve
#CHR_ALPC 2,128
#BG_SET_BACK 
#REEK_CHR 1
#THREAD_STA 1,THREAD_CHR_ASE_BG3
    if persistent.autosave_choice:
        python:
                 renpy.take_screenshot()
                 renpy.save("auto-"+str(persistent.auto_slot))
                 persistent.auto_slot+=1
                 if persistent.auto_slot>6:
                     persistent.auto_slot = 1
    voice "NCL09A_KU053"
    克罗艾 "「总、总之，我要去买酱油啦！」"
#THREAD_STP 1
#REMOVE_REEK_CHR 1
    "结果，学姐还是决定跑回去买酱油。"
    志雄 "「那把东西放回家，咱们再回商店街吧。」"
    "没办法呢，看来再跑一趟是避免不了了。干脆让她们俩在家等着我一个人跑去买回来好了……"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAC01"),"True","img/CL_LAC01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_KU054"
    克罗艾 "「我一个人去就行啦。志雄和诺艾儿一起拿东西回去吧。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBA01"),"True","img/NO_LBA01A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .35
    with dissolve
    志雄 "「诶？可是……」"
    voice "NCL09A_KU055"
    克罗艾 "「比起大家一起回家再回头去买，这样不是更快吗？」"
    志雄 "「这倒也是……」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB02"),"True","img/NO_LBB02A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .35
    with dissolve
    voice "NCL09A_NO021"
    诺艾儿 "「诺艾儿也一起去！」"
    "诺艾儿说着就和学姐牵起了手。学姐的脸上也露出了笑容。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB06"),"True","img/CL_LAB06A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_KU056"
    克罗艾 "「那，咱们一起吧。志雄，就麻烦你先回去准备火锅咯？」"
    "学姐满脸笑容地对我说了这些话。"
    志雄 "「我知道了」"
    "无法拒绝。"
    "面对那样的笑容，无论如何也无法拒绝的吧。"
    hide lh1
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'CL'",DynamicDisplayable(mouthanime,"CL_LAB01"),"True","img/CL_LAB01A@2x.png") as lh1 zorder (10+1):
        ypos 0.0
        xcenter .65
    with dissolve
    voice "NCL09A_KU057"
    克罗艾 "「那，准备的事情就拜托了呢。」"
    hide lh0
    show expression ConditionSwitch("renpy.music.get_playing(channel='voice') and persistent.speaking == 'NO'",DynamicDisplayable(mouthanime,"NO_LBB07"),"True","img/NO_LBB07A@2x.png") as lh0 zorder (10+0):
        ypos .2
        xcenter .35
    with dissolve
    voice "NCL09A_NO022"
    诺艾儿 "「拜托了呢～！」"
    window hide
    stop music fadeout 1
    hide lh0
    hide lh1
    hide lh2
    hide lh3
    hide lh4
    hide lh10
    hide lh11
    with dissolve
    "学姐和诺艾儿两人牵着手，径直向商店街的方向走去。"
    window hide
#BG_SET_BACK 
#BG_INIC 1
#BG_PRIC 1
#EFF_PRI 0
    show expression "img/NIMG01C@2x.png" as bg1 zorder 1
    show expression "img/NIMG01C@2x.png" as bg_over zorder 2
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
    with dissolve
#EFF_STAC 0,CLOUD_C,EFF_SKIP
#BG_ALP_AUTOC 0,0,1,F24
#EFF_PRI 0
#BG_PRIC 1
    志雄 "（我也抓紧时间去准备吧！）"
    "于是我径直向家走去，一个人布置起来的话，真有些力不从心呢……"
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
    return
#label THREAD_QUA_WIN
#TH_QUAKE_WIN 4
#EOT
#label THREAD_CHR_ASE_BG3
#TH_CHR_ASE BG_3
#EOT
#label THREAD_CHR_ASE_BG1
#TH_CHR_ASE BG_1
#EOT