init -5 python:
    class Add(Action):
        def __init__(self,displayable,transform,i=1):
            self.displayable = displayable
            self.transform = transform
            self.i = i
        def __call__(self):
            renpy.hide("temp1")
            renpy.hide("temp2")
            renpy.hide("temp3")
            renpy.show("temp"+str(self.i),what=self.displayable,at_list=[self.transform],layer="screens",zorder=100)

transform center:
    xcenter 0.5
    yalign 0.0

init python:
    def stopallvoc(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            renpy.music.stop(channel="voice")
            persistent.speaking = ""
    def rrs_speaking(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            renpy.music.stop(channel="voice")
            persistent.speaking = "RI"
    def chi_speaking(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            renpy.music.stop(channel="voice")
            persistent.speaking = "CH"
    def cle_speaking(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            renpy.music.stop(channel="voice")
            persistent.speaking = "CL"
    def rin_speaking(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            renpy.music.stop(channel="voice")
            persistent.speaking = "SU"
    def yun_speaking(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            renpy.music.stop(channel="voice")
            persistent.speaking = "YU"
    
    def hen_speaking(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            renpy.music.stop(channel="voice")
            persistent.speaking = "TO"
    
    def shi_speaking(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            renpy.music.stop(channel="voice")
            persistent.speaking = "SN"
    
    def zx_speaking(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            renpy.music.stop(channel="voice")
            persistent.speaking = "SI"
    
    
    def sn_speaking(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            renpy.music.stop(channel="voice")
            persistent.speaking = "KA"
    
    def xw_speaking(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            renpy.music.stop(channel="voice")
            persistent.speaking = "SF"
    
    def xl_speaking(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            renpy.music.stop(channel="voice")
            persistent.speaking = "KR"
    def fmk_speaking(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            renpy.music.stop(channel="voice")
            persistent.speaking = "FU"
    def erz_speaking(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            renpy.music.stop(channel="voice")
            persistent.speaking = "YS"
    def xiz_speaking(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            renpy.music.stop(channel="voice")
            persistent.speaking = "YZ"
    def max_speaking(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            renpy.music.stop(channel="voice")
            persistent.speaking = "MH"
    def ner_speaking(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            renpy.music.stop(channel="voice")
            persistent.speaking = "NO"
    def els_speaking(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            renpy.music.stop(channel="voice")
            persistent.speaking = ""
    def mouthanime(st,at,lh):
        return At(Null(),m(lh)),None

init:
    transform m(lh):
        pause 0.4
        "img/"+lh+"B@2x.png"
        pause 0.4
        "img/"+lh+"C@2x.png"
        pause 0.1
        "img/"+lh+"A@2x.png"
        repeat
    #define adv = Character(name="",ctc="cursor")
    define narrator = Character(name="",ctc="cursor",callback = stopallvoc)
    define 莉莉丝 = Character("莉莉丝",ctc="cursor",show_two_window=True,voice_tag="RRS",callback=rrs_speaking)
    define りりす？ = Character("？？？",ctc="cursor",show_two_window=True,voice_tag="RRS",callback=rrs_speaking)
    define りりす・亨 = Character("莉莉丝·亨",ctc="cursor",show_two_window=True,voice_tag="RRS",callback=rrs_speaking)
    define 莉莉丝・志雄 = Character("莉莉丝·志雄",ctc="cursor",show_two_window=True,voice_tag="RRS",callback=rrs_speaking)
    define 智纱 = Character("智纱",ctc="cursor",show_two_window=True,voice_tag="CHI",callback=chi_speaking)
    define 智纱？ = Character("？？？",ctc="cursor",show_two_window=True,voice_tag="CHI",callback=chi_speaking)
    define 克罗艾 = Character("克罗艾",ctc="cursor",show_two_window=True,voice_tag="CLE",callback=cle_speaking)
    define クロエ・志雄 = Character("克罗艾、志雄",ctc="cursor",show_two_window=True,voice_tag="CLE",callback=cle_speaking)
    define 铃 = Character("铃",ctc="cursor",show_two_window=True,voice_tag="RIN",callback=rin_speaking)
    define 铃？ = Character("？？？",ctc="cursor",show_two_window=True,voice_tag="RIN",callback=rin_speaking)
    define 鈴・志雄 = Character("铃・志雄",ctc="cursor",show_two_window=True,voice_tag="RIN",callback=rin_speaking)
    define 结乃 =Character("结乃",ctc="cursor",show_two_window=True,voice_tag="YUN",callback=yun_speaking)
    define 結乃・志雄 = Character("结乃・志雄",ctc="cursor",show_two_window=True,voice_tag="YUN",callback=yun_speaking)
    define 结乃？ =Character("？？？",ctc="cursor",show_two_window=True,voice_tag="YUN",callback=yun_speaking)
    define 亨 = Character("亨",ctc="cursor",show_two_window=True,voice_tag="HEN",callback=hen_speaking)
    define 亨？ = Character("？？？",ctc="cursor",show_two_window=True,voice_tag="HEN",callback=hen_speaking)
    define 信 = Character("信",ctc="cursor",show_two_window=True,voice_tag="SHI",callback=shi_speaking)
    define 信？ = Character("？？？",ctc="cursor",show_two_window=True,voice_tag="SHI",callback=shi_speaking)
    define 志雄= Character("志雄",ctc="cursor",show_two_window=True,voice_tag="ZX",callback=zx_speaking)
    define 神奈= Character("神奈",ctc="cursor",show_two_window=True,voice_tag="SN",callback=sn_speaking)
    define 神奈？ = Character("？？？",ctc="cursor",show_two_window=True,voice_tag="SN",callback=sn_speaking)
    define 雄吾 = Character("雄吾",ctc="cursor",show_two_window=True,voice_tag="XW",callback=xw_speaking)
    define 雄吾？ = Character("？？？",ctc="cursor",show_two_window=True,voice_tag="XW",callback=xw_speaking)
    define 香里 = Character("香里",ctc="cursor",show_two_window=True,voice_tag="XL",callback=xl_speaking)
    define 香里？ = Character("？？？",ctc="cursor",show_two_window=True,voice_tag="XL",callback=xl_speaking)
    define 富美子 = Character("富美子",ctc="cursor",show_two_window=True,voice_tag="FMK",callback=fmk_speaking)
    define 爱丽丝 = Character("爱丽丝",ctc="cursor",show_two_window=True,voice_tag="ERZ",callback=erz_speaking)
    define 幸蔵 = Character("幸藏",ctc="cursor",show_two_window=True,voice_tag="XIZ",callback=xiz_speaking)
    define 麻寻 = Character("麻寻",ctc="cursor",show_two_window=True,voice_tag="MAX",callback=max_speaking)
    define 诺艾儿= Character("诺艾儿",ctc="cursor",show_two_window=True,voice_tag="NER",callback=ner_speaking)
    define ノエル？ = Character("？？？",ctc="cursor",show_two_window=True,voice_tag="NER",callback=ner_speaking)
    define エリーズ？= Character("？？？",ctc="cursor",show_two_window=True,voice_tag="ERZ",callback=erz_speaking)
    define 男Ａ = Character("男Ａ",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 男Ｂ = Character("男Ｂ",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 学生会干事 = Character("学生会干事",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 男子生徒Ａ = Character("男学生Ａ",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 女子生徒Ａ = Character("女学生Ａ",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 女子生徒１ = Character("女学生",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 生徒会一同 = Character("学生会员（全体）",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define バイカー = Character("摩托车手",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 仲居のおじさん = Character("男服务员",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 仲居のおばさん = Character("女服务员",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 仲居 = Character("女服务员",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 犬２ = Character("声音",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 犬  = Character("小狗",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 野良猫 = Character("野猫",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 店員 = Character("店员",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 店員Ｂ = Character("店员Ｂ",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 店員Ｃ = Character("店员Ｃ",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 店員Ｅ = Character("店员Ｅ",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 店員Ｄ = Character("店员Ｄ",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 店員Ｆ = Character("店员Ｆ",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 女孩 = Character("女孩",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 電話 = Character("电话",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 友人Ａ = Character("友人Ａ",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 老师 = Character("老师",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 友人Ｂ = Character("友人Ｂ",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define クロエ？ = Character("？？？",ctc="cursor",show_two_window=True,voice_tag="CLE",callback=cle_speaking)
    define 幸蔵２ = Character("克罗艾父亲",ctc="cursor",show_two_window=True,voice_tag="XIZ",callback=xiz_speaking)
    define エリーズ２ = Character("克罗艾母亲",ctc="cursor",show_two_window=True,voice_tag="ERZ",callback=erz_speaking)
    define 麻尋？ = Character("？？？",ctc="cursor",show_two_window=True,voice_tag="MAX",callback=max_speaking)
    define 麻尋２ = Character("店员",ctc="cursor",show_two_window=True,voice_tag="MAX",callback=max_speaking)
    define 麻尋３ = Character("仙堂",ctc="cursor",show_two_window=True,voice_tag="MAX",callback=max_speaking)
    define カップル男性 = Character("情侣·男",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define カップル女性 = Character("情侣·女",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 車内放送の声 = Character("车内广播",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 車内販売の売り子 =  Character("车内售货员",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 女性客 =  Character("女乘客",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 乗客 = Character("乘客",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 揚聲器 = Character("扬声器",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define アナウンス = Character("播音员",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define ＴＯＭＯＹＡ = Character("ＴＯＭＯＹＡ",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 工作人員 = Character("工作人员",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define ラジオ = Character("收音机",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 射的屋の店主 = Character("射箭店店主",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 輪投げ屋の店主 = Character("套圈店店主",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 通行人 =  Character("路人",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    define 客 =  Character("客人",ctc="cursor",show_two_window=True,voice_tag="ELS",callback=els_speaking)
    image cursor:
        "img/icoMsg@2x.png"
        transform_anchor True
        anchor(0.5,0.5)
        block:
            rotate 0.0
            linear 1.0 rotate 359
            repeat
    python:
        
        if persistent.lastclear == None:
            persistent.lastclear=0
        if persistent.autosave_choice == None:
            persistent.autosave_choice = True
        if persistent.autosave_scene == None:
            persistent.autosave_scene = True
        if persistent.show_dict == None:
            persistent.show_dict = True
        if persistent.total_playtime == None:
            persistent.total_playtime = 0
        if persistent.clearlist == None:
            persistent.clearlist = [False]*9
        if persistent.scenelist == None:
            persistent.scenelist = [False]*91
        if persistent.albumlist == None:
            persistent.albumlist = [False]*189
        if persistent.dictlist == None:
            persistent.dictlist = [False]*69
        if persistent.endnamelist == None:
            persistent.endnamelist =[
            "莉莉丝 Ａ结局",
            "莉莉丝 Ｂ结局",
            "智纱 Ａ结局",
            "智纱 Ｂ结局",
            "克罗艾 结局",
            "铃 Ａ结局",
            "铃 Ｂ结局",
            "结乃 结局",
            "神奈 结局",
           ]
        if persistent.albumthumb == None:
            persistent.albumthumb = [
                                        "EVN_RI01A",
                                        "EVN_RI02A",
                                        "EVN_RI03",
                                        "EVN_RI04A",
                                        "EVN_RI05A",
                                        "EVN_RI06A",
                                        "EVN_RI07A",
                                        "EVN_RI08A",
                                        "EVN_RI09A",
                                        "EVN_RI10A",
                                        "EVN_RI11A",
                                        "EVN_RI12A",
                                        "EVN_CH01A",
                                        "EVN_CH02A",
                                        "EVN_CH03A",
                                        "EVN_CH04A2",
                                        "EVN_CH05A",
                                        "EVN_CH06A",
                                        "EVN_CH07A",
                                        "EVN_CH08AA",
                                        "EVN_CH09A",
                                        "EVN_CH10A",
                                        "EVN_CH11A",
                                        "EVN_CH12A",
                                        "EVN_CL01A",
                                        "EVN_CL02A",
                                        "EVN_CL03A",
                                        "EVN_CL04A",
                                        "EVN_CL05A",
                                        "EVN_CL06A",
                                        "EVN_CL07A",
                                        "EVN_CL08A",
                                        "EVN_CL09A",
                                        "EVN_CL10A",
                                        "EVN_CL11A",
                                        "EVN_CL12A",
                                        "EVN_SU01A",
                                        "EVN_SU02A",
                                        "EVN_SU03A",
                                        "EVN_SU04A",
                                        "EVN_SU05A",
                                        "EVN_SU06A",
                                        "EVN_SU07A",
                                        "EVN_SU08A",
                                        "EVN_SU09A",
                                        "EVN_SU10A",
                                        "EVN_SU11A",
                                        "EVN_SU12A",
                                        "EVN_YU01A",
                                        "EVN_YU02A",
                                        "EVN_YU03A",
                                        "EVN_YU04A",
                                        "EVN_YU05A",
                                        "EVN_YU06A",
                                        "EVN_YU07AA",
                                        "EVN_YU08A",
                                        "EVN_YU09A",
                                        "EVN_YU10A",
                                        "EVN_YU11A",
                                        "EVN_YU12A",
                                        "EVN_YU13A",
                                        "EVN_SP01A",
                                        "EVN_SP02A",
                                        "EVN_SP03A",
                                        "EVN_SP04A",
                                        "EVN_SP05A",
                                        "EVN_SP06A",
                                        "EVN_SP07A",
                                        "EVN_SP08A",
                                        "EVN_SP09A",
                                        ]
        if persistent.albuminfo == None:
            persistent.albuminfo = ["EVN_RI01A",
                                    "EVN_RI01B",
                                    "EVN_RI01C",
                                    "EVN_RI01D",
                                    "EVN_RI01E",
                                    "EVN_RI02A",
                                    "EVN_RI02B",
                                    "EVN_RI02C",
                                    "EVN_RI02D",
                                    "EVN_RI03",
                                    "EVN_RI04A",
                                    "EVN_RI05A",
                                    "EVN_RI05B",
                                    "EVN_RI06A",
                                    "EVN_RI06B",
                                    "EVN_RI07A",
                                    "EVN_RI07B",
                                    "EVN_RI08A",
                                    "EVN_RI08B",
                                    "EVN_RI09A",
                                    "EVN_RI10A",
                                    "EVN_RI10B",
                                    "EVN_RI10C",
                                    "EVN_RI10D",
                                    "EVN_RI11A",
                                    "EVN_RI12A",
                                    "EVN_RI12B",
                                    "EVN_CH01A",
                                    "EVN_CH01B",
                                    "EVN_CH01C",
                                    "EVN_CH02A",
                                    "EVN_CH03A",
                                    "EVN_CH03B",
                                    "EVN_CH04A2",
                                    "EVN_CH04B2",
                                    "EVN_CH04C2",
                                    "EVN_CH04A",
                                    "EVN_CH04B",
                                    "EVN_CH04C",
                                    "EVN_CH04D",
                                    "EVN_CH04E",
                                    "EVN_CH04F2",
                                    "EVN_CH04G2",
                                    "EVN_CH04H2",
                                    "EVN_CH04F",
                                    "EVN_CH04G",
                                    "EVN_CH04H",
                                    "EVN_CH04I",
                                    "EVN_CH04J",
                                    "EVN_CH05A",
                                    "EVN_CH05B",
                                    "EVN_CH06A",
                                    "EVN_CH06B",
                                    "EVN_CH06C",
                                    "EVN_CH06D",
                                    "EVN_CH06E",
                                    "EVN_CH06F",
                                    "EVN_CH07A",
                                    "EVN_CH07B",
                                    "EVN_CH08AA",
                                    "EVN_CH08BA",
                                    "EVN_CH09A",
                                    "EVN_CH09B",
                                    "EVN_CH09C",
                                    "EVN_CH09D",
                                    "EVN_CH09E",
                                    "EVN_CH09F",
                                    "EVN_CH10A",
                                    "EVN_CH10B",
                                    "EVN_CH10C",
                                    "EVN_CH10D",
                                    "EVN_CH11A",
                                    "EVN_CH11B",
                                    "EVN_CH12A",
                                    "EVN_CH12C",
                                    "EVN_CH12B",
                                    "EVN_CH12D",
                                    "EVN_CL01A",
                                    "EVN_CL01B",
                                    "EVN_CL01C",
                                    "EVN_CL01D",
                                    "EVN_CL01E",
                                    "EVN_CL01F",
                                    "EVN_CL02A",
                                    "EVN_CL03A",
                                    "EVN_CL04A",
                                    "EVN_CL04B",
                                    "EVN_CL04C",
                                    "EVN_CL04D",
                                    "EVN_CL05A",
                                    "EVN_CL05B",
                                    "EVN_CL05C",
                                    "EVN_CL06A",
                                    "EVN_CL06B",
                                    "EVN_CL06C",
                                    "EVN_CL07A",
                                    "EVN_CL07B",
                                    "EVN_CL08A",
                                    "EVN_CL09A",
                                    "EVN_CL10A",
                                    "EVN_CL11A",
                                    "EVN_CL11B",
                                    "EVN_CL12A",
                                    "EVN_CL12B",
                                    "EVN_CL12C",
                                    "EVN_CL12D",
                                    "EVN_SU01A",
                                    "EVN_SU01B",
                                    "EVN_SU01C",
                                    "EVN_SU01D",
                                    "EVN_SU02A",
                                    "EVN_SU02B",
                                    "EVN_SU02E",
                                    "EVN_SU02F",
                                    "EVN_SU02G",
                                    "EVN_SU02H",
                                    "EVN_SU02I",
                                    "EVN_SU02J",
                                    "EVN_SU02K",
                                    "EVN_SU02L",
                                    "EVN_SU03A",
                                    "EVN_SU04A",
                                    "EVN_SU04B",
                                    "EVN_SU04C",
                                    "EVN_SU04D",
                                    "EVN_SU04E",
                                    "EVN_SU05A",
                                    "EVN_SU05B",
                                    "EVN_SU05C",
                                    "EVN_SU06A",
                                    "EVN_SU06B",
                                    "EVN_SU06C",
                                    "EVN_SU06D",
                                    "EVN_SU07A",
                                    "EVN_SU07B",
                                    "EVN_SU08A",
                                    "EVN_SU08B",
                                    "EVN_SU09A",
                                    "EVN_SU09B",
                                    "EVN_SU09C",
                                    "EVN_SU09D",
                                    "EVN_SU10A",
                                    "EVN_SU10B",
                                    "EVN_SU10C",
                                    "EVN_SU10D",
                                    "EVN_SU11A",
                                    "EVN_SU11B",
                                    "EVN_SU12A",
                                    "EVN_YU01A",
                                    "EVN_YU01B",
                                    "EVN_YU01C",
                                    "EVN_YU01D",
                                    "EVN_YU02A",
                                    "EVN_YU02B",
                                    "EVN_YU02C",
                                    "EVN_YU03A",
                                    "EVN_YU03B",
                                    "EVN_YU03C",
                                    "EVN_YU04A",
                                    "EVN_YU04B",
                                    "EVN_YU05A",
                                    "EVN_YU06A",
                                    "EVN_YU06B",
                                    "EVN_YU06C",
                                    "EVN_YU07AA",
                                    "EVN_YU07BA",
                                    "EVN_YU07CA",
                                    "EVN_YU08A",
                                    "EVN_YU08B",
                                    "EVN_YU09A",
                                    "EVN_YU10A",
                                    "EVN_YU10B",
                                    "EVN_YU10C",
                                    "EVN_YU11A",
                                    "EVN_YU11B",
                                    "EVN_YU12A",
                                    "EVN_YU12B",
                                    "EVN_YU13A",
                                    "EVN_YU13B",
                                    "EVN_SP01A",
                                    "EVN_SP02A",
                                    "EVN_SP02B",
                                    "EVN_SP03A",
                                    "EVN_SP04A",
                                    "EVN_SP05A",
                                    "EVN_SP06A",
                                    "EVN_SP07A",
                                    "EVN_SP08A",
                                    "EVN_SP09A",
                                    ]
        if persistent.musicinfo == None:
           persistent.musicinfo = [
                                    ["SONG01","SONG01","Next Relation","2:04","歌：Zwei#作詞：橋詰亮子 作曲／編曲：大島こうすけ",],
                                    ["BGM01","BGM01NL","Second Chapter","2:26","作曲／編曲：阿保　剛",],
                                    ["BGM02","BGM02NL","Ririsu -NR version-","2:34","作曲／編曲：阿保　剛",],
                                    ["BGM03","BGM03NL","Chisa -NR version-","2:49","作曲／編曲：阿保　剛",],
                                    ["BGM04","BGM04NL","Chloe -NR version-","2:14","作曲／編曲：阿保　剛",],
                                    ["BGM05","BGM05NL","Rein -NR version-","2:41","作曲／編曲：阿保　剛",],
                                    ["BGM06","BGM06NL","Yuno -NR version-","2:17","作曲／編曲：阿保　剛",],
                                    ["BGM07","BGM07NL","Mahiro -NR version-","2:01","作曲／編曲：阿保　剛",],
                                    ["BGM08","BGM08NL","Noelle","1:56","作曲／編曲：阿保　剛",],
                                    ["BGM09","BGM09NL","Toru","2:13","作曲／編曲：阿保　剛",],
                                    ["BGM10","BGM10NL","Serene sky","2:25","作曲／編曲：阿保　剛",],
                                    ["BGM11","BGM11NL","Ryuzakai","2:10","作曲／編曲：阿保　剛",],
                                    ["BGM12","BGM12NL","In the nature","2:08","作曲／編曲：阿保　剛",],
                                    ["BGM13","BGM13NL","Common heart","3:00","作曲／編曲：阿保　剛",],
                                    ["BGM14","BGM14NL","Monologue","2:37","作曲／編曲：阿保　剛",],
                                    ["BGM15","BGM15NL","An epilogue -memories off-","4:15","作曲／編曲：阿保　剛",],
                                    ["BGM22","BGM22NL","Way started now","2:06","作曲／編曲：阿保　剛",],
                                    ["BGM16","BGM16NL","In the nature -tranquillo-","2:30","作曲／編曲：阿保　剛",],
                                    ["OBGM01","OBGM01NL","Irreplaceable memories","2:21","作曲／編曲：阿保　剛",],
                                    ["OBGM02","OBGM02NL","Shio -His story-","2:01","作曲／編曲：阿保　剛",],
                                    ["OBGM04","OBGM04NL","Ririsu-Ⅱ -Fabrication-","1:52","作曲／編曲：阿保　剛",],
                                    ["OBGM05","OBGM05NL","Chisa-Ⅰ -Straight love-","3:17","作曲／編曲：阿保　剛",],
                                    ["OBGM06","OBGM06NL","Chisa-Ⅱ -Answer to me-","2:19","作曲／編曲：阿保　剛",],
                                    ["OBGM08","OBGM08NL","Chole-Ⅱ -Perplexity-","2:00","作曲／編曲：阿保　剛",],
                                    ["OBGM09","OBGM09NL","Rein-Ⅰ -Like winds-","3:18","作曲／編曲：阿保　剛",],
                                    ["OBGM10","OBGM10NL","Rein-Ⅱ -Mind journey-","1:58","作曲／編曲：阿保　剛",],
                                    ["OBGM11","OBGM11NL","Yuno-Ⅰ -Sympathy-","2:31","作曲／編曲：阿保　剛",],
                                    ["OBGM12","OBGM12NL","Yuno-Ⅱ -Dear friend-","2:37","作曲／編曲：阿保　剛",],
                                    ["OBGM25","OBGM25NL","Namasute， returns","3:09","作曲／編曲：阿保　剛",],
                                    ["OBGM13","OBGM13NL","Dangerous","3:19","作曲／編曲：阿保　剛",],
                                    ["OBGM14","OBGM14NL","Rising pulse","2:12","作曲／編曲：阿保　剛",],
                                    ["OBGM15","OBGM15NL","SUMISORA","2:07","作曲／編曲：阿保　剛",],
                                    ["OBGM16","OBGM16NL","Tremble","2:08","作曲／編曲：阿保　剛",],
                                    ["OBGM17","OBGM17NL","Every day -Nothing-","3:09","作曲／編曲：阿保　剛",],
                                    ["OBGM18","OBGM18NL","Cheerful step -Bustling time-","3:14","作曲／編曲：阿保　剛",],
                                    ["OBGM19","OBGM19NL","That time -Recollection-","2:59","作曲／編曲：阿保　剛",],
                                    ["OBGM20","OBGM20NL","Promise? -Sadness in confession-","2:04","作曲／編曲：阿保　剛",],
                                    ["OBGM26","OBGM26NL","Beautiful dreamer","3:02","作曲／編曲：阿保　剛",],
                                    ["OBGM27","OBGM27NL","Tremble -Piano-","2:15","作曲／編曲：阿保　剛",],
                                    ["OBGM28","OBGM28NL","Image","2:54","作曲／編曲：阿保　剛",],
                                    ["OBGM29","OBGM29NL","Image -Piano-","1:31","作曲／編曲：阿保　剛",],
                                    ["OBGM23","OBGM23NL","Lost thing is... -Bygone days-","4:05","作曲／編曲：阿保　剛",],
                                    ["OBGM22","OBGM22NL","Hello again -Memories Off-","4:03","作曲／編曲：阿保　剛",],
                                    ["BGM17","BGM17NL","Candy Love -monologue-","0:52","作曲／編曲：阿保　剛",],
                                    ["BGM18","BGM18NL","Mind Loop -monologue-","0:49","作曲／編曲：阿保　剛",],
                                    ["BGM19","BGM19NL","Blue Moon -monologue-","0:57","作曲／編曲：阿保　剛",],
                                    ["BGM20","BGM20NL","ハルカ　カナタ　-monologue-","0:34","作曲／編曲：阿保　剛",],
                                    ["BGM21","BGM21NL","Rainbow Highway -monologue-","0:48","作曲／編曲：阿保　剛",],
                                    ["SONG02","SONG02","ずっと一緒に　もっと遠くまで","2:26","作詞：彩音　作曲/編曲：水野大輔",],
                                    ]
        if persistent.dictinfo == None:
            persistent.dictinfo = [
                                    ["塚本志雄","0","Ｚ）－つかもとしお","人物","DICIMG_SI1","年龄：１７岁\n身高：１７０公分\n生日：１０月８日\n喜好：广播节目、ＫＡＮＡＴＡ\n\n澄空学园３年级生。学生会会长。在澄空站前的公寓居住，同时也是公寓的管理人。\n小学三年级的时候母亲去世了，之后和父亲两个人一起生活。在初中入学之后，发现父亲有了其他的女人。在和父亲大吵了一通之后将父亲赶出了家。不过，现在两人已经和解了。\n对广播投稿有着浓厚的兴趣，经常给『Ｔーｗａｖｅ』投稿。\n是艺人『ＫＡＮＡＴＡ』的忠实粉丝。\n\n口头禅是『真没办法啊』。\n"],
                                    ["远峰莉莉丝","1","Ｙ）－とおみねりりす","人物","DICIMG_RI1","年龄：１７岁\n身高：１５２公分\n生日：８月１０日\n喜好：外婆、棒棒糖\n\n澄空学园３年级生。志雄的青梅竹马，现在在同一个班级。与外婆一起生活，同时在外婆经营的小料理店『富美』帮忙，母亲现住在别处。\n小的时候是个非常文静的孩子，不过不知从什么时候起就变得旁若无人的样子。不过，不讲道理的任性基本都是只针对志雄的。\n偶然会露出女孩子可爱的一面。说话基本都是直抒胸臆，虽然稍微有些粗暴，但因外婆严厉地家教，从来不说脏话。\n和智纱是非常要好的挚友。少女作家『铃代黎音』的超级崇拜者。因为常年被亨追求，对亨的暴力倾向也在逐步加深。\n"],
                                    ["箱崎智纱","2","Ｘ）－はこさきちさ","人物","DICIMG_CH1","年龄：１７岁\n身高：１５９公分\n生日：１２月２３日\n喜好：所有动物、甜品\n厌恶：水域\n\n澄空学园３年级生。广播台成员。与志雄、亨、莉莉丝不在同一班级。\n从一进入高中就和莉莉丝成为挚友。升上３年级之后才迟迟地加入了广播台。\n有着要做什么决定的时候总会问一起的人『这样做可以吗？』的习惯。非常依赖别人。属于优等生类型。\n\n智纱篇中，一直考虑着要为志雄做些什么，并因此而积极行动着。\n"],
                                    ["嘉神川克罗艾","3","Ｊ）－かがみがわくろえ","人物","DICIMG_CL1","年龄：１９岁\n身高：１６７公分\n生日：７月２日\n喜好：缝纫、骑马\n厌恶：胡萝卜、青椒\n\n青峰学院大学经济学部１年级生。澄空学园前学生会长。\n日法混血儿（母亲是法国人）。\n平时十分关心周围的人，在关键时刻的判断力和行动力都非常强。而相反的，一些非日常性的事件发生在自己身上的话，就无法正常面对，判断力和行动力都会极度地失常。\n遇上已经决定的或者想着『应该如此』却又突然变得不可能了的事情，自己就无法应对了。\n有一种独特的美感，讨厌品格不好的人。\n家族世代经营着本地的大型食品制造贩售公司『嘉神食品株式会社』。虽然是社长的千金，但并没有什么大小姐的脾气，有着非常顾家的一面。\n顺便一提她并不擅长法语。\n"],
                                    ["春日结乃","4","Ｃ）－かすがゆうの","人物","DICIMG_YU1","年龄：１６岁\n身高：１５７公分\n生日：２月２８日\n喜好：喜好：ＫＡＮＡＴＡ、广播投稿\n厌恶：未知\n\n澄空学园２年级生。学生会的干事，放送部成员。\n去年的９月转学来到澄空学园。外表看上去是个活泼的女孩儿，不过，多少还是有些认生的。本性十分开朗，朋友很多，不过基本都是宽泛的浅交，能够称为挚友的人几乎没有。\n升上２年级的时候开始在学生会和广播台里活跃着。非常痴迷广播投稿，现在的昵称为『淳淳的牛奶』。\n与弱不禁风的外表相反，十分有力气，非常擅长体育运动。\n\n与秋津神奈既是挚友，同时也是广播投稿的竞争对手（以投稿为舞台的时候就完全地对志雄置之不理了）。\n"],
                                    ["铃代黎音","5","Ｌ）－すずしろれいん","人物","DICIMG_SU1","知名少女小说作家。稻穗铃的笔名。\n"],
                                    ["稻穗铃","6","Ｄ）－いなほすず","人物","DICIMG_SU1","年龄：２５岁\n生日：１月３日\n身高：１７２公分\n喜好：酒、摩托\n嫌}厌恶：做事不痛快的人、没有条理的事情、编辑\n\n澄空学园的毕业生。稻穗信的亲姐姐。\n作为少女向的小说家『铃代黎音』活跃中。最近将要在月刊杂志上开始短期连载。\n喜欢摩托，非常帅气漂亮的姐姐，秉承了江户人爽朗的的气质。喜欢喝酒，不过一喝就醉。醉了之后会显露非常女孩子气的一面。非常的忠实可靠，很纯情。非常坚持原则，并为此而不断吃亏。害怕被人一直盯着。\n对弟弟信相当粗暴。有对中意的男性使用绞杀技的倾向。\n\n铃篇里，与志雄愈走愈近，但是似乎因为『年龄有差距做不成情侣』这样的观念，一直没有什么进展。\n"],
                                    ["佐贺亨","7","Ｚ）－さがとおる","人物","DICIMG_TO1","年龄：１８岁\n生日：６月２９日\n身高：１７１公分\n喜好：所有音乐、莉莉丝\n厌恶：学习\n\n澄空学园３年级生。志雄的好友兼同班同学。\n从上高中起就一直和志雄同班。与信不同的是，并不擅长言辞，是用行动来表现的类型。\n父母是老师，对澄空的各种传说知道得非常详尽。\n取得了摩托车的驾照，也如愿以偿地购买了摩托车，并给爱车起名『猫大人』，不过，由于从父母那里借了钱，所以这个夏天被迫每天到补习班学习。\n"],
                                    ["稻穗信","8","Ｄ）－いなほしん","人物","DICIMG_SN1","年龄：２２岁\n生日：１月４日\n身高：１７５公分\n喜好：交谈、旅行、日本元素\n厌恶：被说教、学习\n\n澄空学园的毕业生。自称自由人的自由职业者，养了一只名为ＴＯＭＯＹＡ的杂种犬。\n在家庭餐厅酪萨克打工，并晋升为主管，因此逃也逃不掉了，过着一如既往的生活。\n在姐姐铃面前十分地抬不起头。\n"],
                                    ["远峰富美子","9","Ｙ）－とおみねふみこ","人物","DICIMG_FU1","年龄：７４岁\n身高：１４５公分\n\n莉莉丝的外婆。小料理店『富美』的女主人，常被老主顾称为妈妈。\n还依然非常朝气，虽然这么说，但随着年龄的增长，身体状况还是日渐严峻起来。\n对手机以及各种视频音频器械掌握得十分熟练，编写短信的速度完全不像是个老年人。\n"],
                                    ["塚本雄吾","10","Ｚ）－つかもとゆうご","人物","DICIMG_SF1","年龄：４２岁\n身高：１７２公分\n\n志雄的父亲。乍一看并没有什么不正经的印象，不过那只是在儿子（志雄）面前的面目而已。\n喝醉酒的时候会情绪失常。\n现在并没有和志雄一起生活，而是和香里（莉莉丝的母亲）一起住在蓝之丘的公寓。\n顺便一提，志雄的名字是从父母两人的名字里各取一个汉字组成的。\n"],
                                    ["塚本志织","11","Ｚ）－つかもとしおり","人物","DICIMG00","志雄的母亲。已去世。在志雄还是小孩子的时候，一向体弱的她为了救助在海中溺水的智纱（误认为是莉莉丝）之后，身体逐渐恶化，最后去世。和莉莉丝的母亲『香里』是高中时代的好友。\n顺便一提，志雄的名字是从父母两人的名字里各取一个汉字组成的。\n"],
                                    ["塚本香里","12","Ｚ）－つかもとかおり","人物","DICIMG_KR1","年龄：３９岁\n身高：１６０公分\n原姓：远峰\n\n莉莉丝的母亲。在莉莉丝还很小的时候丈夫就去世了。\n目前住在位于蓝之丘的高级公寓中。因为这件事，女儿莉莉丝曾经十分反感，跑回外婆家和外婆一起的生活。不过，现在两人已经和解了。\n"],
                                    ["嘉神川幸藏","13","Ｊ）－かがみがわこうぞう","人物","DICIMG_YZ1","年龄：４１岁\n身高：１７５公分\n\n克罗艾的父亲，嘉神食品株式会社的社长。忠诚老实且认真的人。\n常年过度地操劳，身体状况恶化而反复于入院出院之间。依然坚持经营着资金周转困难的公司，倾尽所有心思。\n与妻子爱丽丝分居中，但似乎并没有忽略过她。\n"],
                                    ["嘉神川爱丽丝","14","Ｊ）－かがみがわえりーず","人物","DICIMG_YS1","年龄：４１岁\n身高：１７２公分\n\n克罗艾的母亲。法国人。\n１２年前，幸藏的公司经营困难之后，夫妇关系便产生了不谐之音，之后离家出走，返回法国的父母家中。因幸藏病倒的事情为契机，再度返回了日本。\n语气很柔和，稍显妖艳。从不会怒吼或者歇斯底里。\n"],
                                    ["嘉神川诺艾儿","15","Ｊ）－かがみがわのえる","人物","DICIMG_NO1","年龄：１１岁\n身高：１４２公分\n喜好：胡萝卜、青椒、巧克力\n厌恶：硬的东西、辣的东西\n\n克罗艾的亲妹妹。\n日语是从母亲那里学来的，发音非常标准，不过还不知道（无法理解）的单词也很多。好奇心十分旺盛，领会能力非常强。\n与同龄的孩子相比，总是做一些稍显幼稚的行动和言行，不过精神上则更有大人的感觉。\n喜欢看日本的电视节目。\n"],
                                    ["ＫＡＮＡＴＡ","16","Ｋ）－かなた","人物","DICIMG00","浜咲出身的演员，从模特出道。本名叫黑须彼方。\n广播节目「Ｔーｗａｖｅ」的音乐解说播音员，因轻松、平易近人的谈话风格而非常有人气。\n"],
                                    ["仙堂麻寻","17","Ｘ）－せんどうまひろ","人物","DICIMG_MH1","年龄：２１岁\n身高：１６０公分\n喜好：自行车、橙色\n厌恶：黑暗狭窄的地方\n\n在罗萨克打工的自由职业者。千羽谷大学的电影同好团体「ＣＵＭ研」的成员，并不是千羽谷大学的学生。\n是个相当马虎的冒失鬼，忘记的东西非常多。\n信的好友，在他外出期间，帮助他照看他的狗ＴＯＭＯＹＡ。\n"],
                                    ["秋津神奈","18","Ｑ）－あきつかんな","人物","DICIMG_KA1","年龄：１６岁\n身高：１６０公分\n喜好：广播节目\n\n结乃的好友，初中的时候搬到了海外，不过现在回到了日本，与结乃保持着联系。家离澄空相当远，仅仅是过来一趟就相当于小型旅行的程度。\n广播节目『Ｔーｗａｖｅ』常年的投稿者，笔名是『凯尔玛妹妹』。在结乃篇中似乎对志雄十分有意。\n曾经让矿石收音机成功接收ＦＭ的信号，非常擅长电子方面的技术。\n"],
                                    ["鸭浦","19","Ｙ）－かもうら","地点","DICIMG00","位于芦鹿电东端的城镇。\n有一个名为『Ｍａｒｉｎｅ　Ｌａｎｄ』的游乐园，非常热闹。\n"],
                                    ["绫园台","20","Ｌ）－あやぞのだい","地点","DICIMG21","绫园学院高校、大型购物中心等位于这里。\n距离千羽谷的喧闹地带稍远的住宅区，套房公寓很多。由于房租比千羽谷地区更加便宜，有很多在千羽谷大学上学的学生都在这里租房独立生活。是个绿化程度很高的，非常安静的地方。\n"],
                                    ["千羽谷","21","Ｑ）－ちはや","地点","DICIMG22","汇集本地年轻人的地方。有着西有藤川、东有千羽谷的说法，因为有嘉神川夹在中间，东边的人大多在千羽谷游玩。\n这里有着千羽谷大学以及千羽谷医院等大型设施。\n也有芦鹿岛线本线的连接车站。\n顺便一提，稻穗信在这条街道的『日暮庄』居住。\n"],
                                    ["北的射","22","Ｂ）－きたまとい","地点","DICIMG23","芦鹿电沿线的一站。\n有很多住宅的城镇，是一个没有什么特别建筑的安逸清静的地方。\n"],
                                    ["的射","23","Ｄ）－まとい","地点","DICIMG00","芦鹿岛沿线的一站。\n是一条没有什么特别设施的娴静的住宅街。\n"],
                                    ["澄空","24","Ｃ）－すみそら","地点","DICIMG25","既是古老的住宅区，也是开发中的站前地区，公园等公共设施一应俱全。衣食住都很自由很舒适的城镇。大型购物时，选择乘坐芦鹿电几站到千羽谷去的人非常多。\n车站前的商店街非常热闹，不过深入其中的话就有很多古旧的店铺鳞次栉比地排列着，充斥着宁静的气氛。对附近澄空学园的学生来说，这里是顺道购物吃饭的绝好地点。\n另外，这个地区的一大特征是有许多坡道。此外，车站的南侧是海。\n"],
                                    ["中目町","25","Ｚ）－なかめちょう","地点","DICIMG00","规模上略小的城镇，从车站稍微步行一段路之后，至今仍可以看见武家屋敷等等那些过去美好时代残留至今的古迹。车站的规模是芦鹿岛中最小的一个。近些年正逐渐着手开发中，车站的扩建工程早已提上日程。不过，直到目前，这个计划仍尚在搁浅之中。\n"],
                                    ["蓝之丘","26","Ｌ）－あいがおか","地点","DICIMG27","绿意盎然，作为居民区而渐渐发展起来的新兴住宅区。这里也有芦鹿电的车站。\n蓝之丘第二中学位于此地。\n"],
                                    ["登波离","27","Ｄ）－とわり","地点","DICIMG00","位于登波离桥稍微上游一些的车站，在嘉神川靠樱峰的这一侧。站名是用假名的登波离（とわり）写的，并不是距离登波离桥最近的车站。\n"],
                                    ["樱峰","28","Ｙ）－さくらみね","地点","DICIMG29","让人联想到昭和初期的古旧街道，海风拍打着风化的看板，可以感受到历史的气息。\n车站周围只有一条非常小的商店街，勉强来说，也是有便利店的。街道南边面向着美丽的大海，一到夏天会有很多前来游泳的游客。沿着海岸附近的公路上有一家家庭餐厅『酪萨克』。\n这里是到登波离桥距离最短的一站。顺便一提，浜咲也是樱峰市的一部分。\n"],
                                    ["浜咲","29","Ｂ）－はまさき","地点","DICIMG30","属于樱峰市的一部分。车站北侧是座稍高的山丘，登上坡道的话就可以看见浜咲学园。\n离海很近，来此进行海水浴的游客非常多。\n"],
                                    ["芦鹿岛","30","Ｌ）－あしかじま","地点","DICIMG31","最近的站点是『芦鹿岛（あしかじま）站』。站名不是用汉字而是平假名写的。\n名字里虽然有个岛字，但实际上连着陆地。芦鹿岛作为著名的观光圣地，在山顶设有瞭望台。从那里可以眺望相当辽阔的地域。有着圣恋之丘，结缘之树等很多情侣常去的地点。\n每年夏天都会举办大规模的烟花大会。\n"],
                                    ["林钟寺","31","Ｌ）－りんしょうじ","地点","DICIMG00","数百年前，当时的豪族『黑川武利』建立的名为林钟寺的寺庙所在的城镇。有一所名为林钟寺女子学院的高中位于此处。\n"],
                                    ["藤川","32","Ｔ）－ふじかわ","地点","DICIMG33","与千羽谷相邻的繁华地区。这里有芦鹿电与别的线路换乘的车站，是芦鹿电中最大的一个车站。有几家大型的百货公司，名副其实的都会。是生活在嘉神川西侧的人常去的地点。\n"],
                                    ["嘉神川","33","Ｊ）－かがみがわ","地点","DICIMG34","流经千羽谷、澄空、樱峰附近的大河川。被认定为一级河川。\n克罗艾家的姓就是由此河川而来的。从很早以前就是名士家庭吧。\n"],
                                    ["登波离桥","34","Ｄ）－とわりばし","地点","DICIMG35","横跨嘉神川的大桥。传说在这里告白的情侣一定会分手。顺便一提，距离这里最近的车站是樱峰。距离登波离则是稍微有些远。\n"],
                                    ["酪萨克","35","Ｌ）－るさっく","地点","DICIMG36","位于樱峰的全国连锁式家庭餐厅，凭借料理的味道与品质获得了相当高的人气。藤川和千羽谷也有分店，樱峰店是信和麻寻打工的地方。\n"],
                                    ["Marine Land","36","Ｍ）－まりんらんど","地点","DICIMG37","位于鸭浦的游乐园。是这个地区非常普遍的约会地点。这里的吉祥物是一只名为多鲁比（ドルぴぃ）的海豚。\n"],
                                    ["富美","37","Ｆ）－ふみこ","地点","DICIMG38","莉莉丝的外婆『富美子』所经营的小料理店。莉莉丝在这里给外婆帮忙就如同每日的必修课一样。常客们的光顾使得这里非常热闹，最近信和铃也经常在这里露面。\n１楼的里面和２楼是作为居住的房间。\n"],
                                    ["澄空公园","38","Ｃ）－すみそらこうえん","地点","DICIMG39","位于澄空站附近的公园，别名是喷水池公园。智纱向志雄告白的公园。\n"],
                                    ["千羽谷大学","39","Ｑ）－ちはやだいがく","地点","DICIMG40","位于千羽谷的大学。有法学、艺术、文学、经济等多个学院。占地面积广大，具有各式各样的设施。\n"],
                                    ["澄空弁财天","40","Ｃ）－すみそらべんざいてん","地点","DICIMG41","芦鹿电观光旅游必去的景点。距离澄空站徒步20分钟左右，很有历史的神社。\n正如它的名字所示的，这里是供奉七福神之一的『弁天大人』的神社，传说用这里的水冲洗钱币，会受益颇多。为此，岩屋中放置着笸箩和舀子，供参拜者自由使用来清洗钱币。\n另外，据说如果洗过的钱能尽快用掉的话则将更有效，大概全部用在芦鹿电观光上会很吉利吧？\n这个神社名字里的『澄空』，是因自古这里的地名就是澄空而得名的。\n"],
                                    ["芦鹿岛水族馆","41","Ｌ）－あしかじますいぞくかん","地点","DICIMG42","芦鹿岛附近的水族馆，海豚表演相当的有人气。这里也是最知名的约会地点。\n"],
                                    ["澄空学园","42","Ｃ）－すみそらがくえん","地点","DICIMG43","澄位于澄空的私立高中。志雄他们所就读的学校，校风相当自由。\n需要注意的是在小卖部贩售的面包是除此之外哪里都买不到的稀有品。\n是一所升学率不错的学校，不过学生之间学习成绩的差距也很明显。\n"],
                                    ["浜咲学园","43","Ｂ）－はまさきがくえん","地点","DICIMG44","位于浜咲的私立高中。校风比较自由的升学率很高的学校，社团活动十分丰富。这几年这里名人辈出，在现在的初中生里相当的有人气。\nＫＡＮＡＴＡ也是出身于这里的（未毕业）。\n"],
                                    ["绫园学园","44","Ｌ）－あやぞのがくいん","地点","DICIMG00","位于绫园台的私立高中。着重学生的独立自主性，就算成就有些落后，但只要有一技之长，在升学上就没有大碍。\n红色的制服是他们的标志性装扮。\n"],
                                    ["千羽谷第一高中","45","Ｑ）－ちはやだいいちこうこう","地点","DICIMG00","位于千羽谷的私立女子高中。通称「千羽谷一高（いっこう）」。雅致的制服，广受女学生们的好评。\n麻寻的母校。\n"],
                                    ["SunGrace澄空","46","Ｓ）－さんぐれいすすみそら","地点","DICIMG47","志雄代替父亲作为管理人管理的高级公寓。大家都称之为『塚本公寓』或者『塚本大楼』。\n"],
                                    ["下龙境","47","Ｘ）－しもりゅうざかい","地点","DICIMG48","在上龙境相反方向的、隐匿不为人知的美丽的地方。给人感觉十分亲切，尚在开发中，正在逐渐成长为新的观光地。因此，新的旅馆等等设施一个接一个在该地的蓝图上筹划着。"],
                                    ["龙境","48","Ｌ）－りゅうざかい","地点","DICIMG00","也被称为龙境温泉乡。被山分割为西北部的上龙境（かみりゅうざかい）和东南部的下龙境（しもりゅうざかい），上龙境作为观光胜地而出名，经常在旅游杂志以及网页上出现。\n当地好像流传着关于龙神的传说。\n"],
                                    ["宝树庵","49","Ｂ）－ほうきあん","地点","DICIMG50","莉莉丝外婆的熟人所经营的旅馆。房间是用各种各样的花名来命名的。\n"],
                                    ["门亚湖","50","Ｍ）－とあこ","地点","DICIMG51","位于上龙境与下龙境之间的湖泊。此处整理出了一片所谓的沙滩，在水里也能游泳，十分美丽。\n也有可以骑摩托艇的区域。\n"],
                                    ["泉龙神社","51","Ｑ）－せんりゅうじんじゃ","地点","DICIMG52","供奉祭祀着镇守龙境温泉乡的龙神，小神社之一。作为可住人的建筑，位于这附近高度最高的地方。\n"],
                                    ["斯特拉斯堡","52","Ｓ）－すとらすぶーる","地点","DICIMG00","『Ｓｔｒａｓｂｏｕｒｇ』\n坐落在法国东北部莱茵河畔西岸的城市。作为沿河港口是交通的枢纽之地。\n克罗艾的母亲爱丽丝的娘家（阿梅勒家）在此。\n"],
                                    ["奏云祭","53","Ｚ）－そううんさい","庆典","DICIMG54","澄空学园的文化祭的名字。自由校风的缘故，是非常热闹的文化祭。当然，文化祭执行委员和学生会的成员也因此背负着巨大的使命。\n"],
                                    ["纸灯祭","54","Ｚ）－ぼんぼりまつり","庆典","DICIMG55","澄空附近的神社举行的祭典。在纸灯（提灯）上画上各种图案来表现当时社会的情景状况。\n"],
                                    ["泉龙神社夏日祭典","55","Ｑ）－せんりゅうじんじゃなつまつり","庆典","DICIMG56","泉龙神社在８月末举行的夏日祭奠。进入暑假之后，本地的孩子们每天都期待的祭典。最引人注目的是小镇上的居民们和孩子们建立起来的帐篷。因为区域内并不是很宽广，摊位也不会大量地摆出来。\n此外，到了盂兰盆会的时候，盂兰盆舞也会在神社内举行。\n"],
                                    ["芦鹿电","56","Ｌ）－しかでん","其他","DICIMG57","指的是芦鹿岛电铁芦鹿岛线，是这一地区举足轻重的交通机构。稍显老旧的车身也吸引了很多爱好者。\n路线上的车站由西开始依次是：藤川、林钟寺、芦鹿岛、浜咲、樱峰、登波离、蓝之丘、中目町、澄空、的射、北的射、千羽谷、绫园台…………鸭浦这个顺序\n。千羽谷、鸭浦方向是上行线，浜咲、藤川方向是下行线。\n"],
                                    ["孤挺花","57","Ｇ）－あまりりす","其他","DICIMG00","５月份到６月份左右盛开的植物。花的颜色是红色或者白色。花语是『健谈』、『傲气』、『娇羞』等等。\n莉莉丝的名字（りりす）就是由此花而来的。\n"],
                                    ["ＴＯＭＯＹＡ","58","Ｔ）－ともや","其他","DICIMG59","信饲养的杂种犬。信在高中退学之后从海边捡回来成为了信的伙伴。\n"],
                                    ["嘉神食品","59","Ｊ）－かがみしょくひん","其他","DICIMG00","嘉神食品株式会社。克罗艾的父亲——嘉神川幸藏所经营的食品公司。当前的业绩并不十分理想。\n自古就是在这一地区经商的老店铺了。\n"],
                                    ["浜咲ＦＭ","60","Ｂ）－はまさきえふえむ","其他","DICIMG00","在浜咲地区进行播放的区域性ＦＭ广播电台。虽然规模不大但收听率却很高，到了本地的人都知晓的程度。\n夏天会组织举行广播节目大赛。\n"],
                                    ["ＦＭ藤川","61","Ｆ）－えふえむふじかわ","其他","DICIMG00","以藤川为中心进行放送的ＦＭ广播电台。在首都圈内也能收听到。\n通称是ＳＥＡＳＩＤＥ—ＦＭ。\n电台呼号是ＪＯＦＰＢ。\n"],
                                    ["猫大人","62","Ｍ）－ねこどの","其他","DICIMG00","亨经过打工好不容易购置的摩托的爱称。虽然是一口气勉强买下的，不过因为是订做的而乐在其中。\n顺便一提，原著中该车的名字为Ａｎｇｅｌｉｎａ（あんじぇりーな），此处换名是为了方便阅读（原名过长）。\n"],
                                    ["蘑菇宝宝","63","Ｍ）－むっしゅまっしゅるーむ","其他","DICIMG64","莉莉丝和智纱喜欢的蘑菇形象的角色。除了穆秀先生（ムッシュさん）以外，还有可鲁贝洛君（ケルベロくん）等等形形色色的角色存在。\n"],
                                    ["矿石收音机","64","Ｋ）－こうせきらじお","其他","DICIMG65","利用方铅矿以及黄铁矿等矿石的整流作用所制作出来的ＡＭ广播收音机，不需要使用电池。\n若用锗二极管代替上述金属的话，可以获得更加稳定的性能。\n另外，无法接受ＦＭ波段的信号。\n"],
                                    ["Ｔ－ｗａｖｅ","65","Ｔ）－てぃーうぇーぶ","其他","DICIMG00","ＦＭ藤川放送的，ＫＡＮＡＴＡ担任主播的节目。\n志雄和结乃、神奈都经常向这里投稿。\n"],
                                    ["免责＆警告信息","66","★）－特别信息","Message","DICIMG67","此版本汉化为民间自制汉化，由『百度贴吧——秋之回忆吧』吧友『秋可可丶』立项。\n大多数工作，包括软件破解、美工修图、脚本制作、组织勘校等也由其担纲完成。\n本汉化作品严禁商业用途，仅供个人基于技术学习性质的测试和研究，如喜欢该作品，请支持正版。\n游戏版权归属原制作公司所有，一切汉化资源，未经汉化立项者以及原始拥有者同意，不得私自挪用。\n如转载本汉化作品，请保留随帖汉化成员名单以及感谢列表内容，并注明出处。须知尊重是相互的，也是起码的。\n"],
                                    ["特别鸣谢","67","★）－特别信息","Message","DICIMG00","游戏的汉化过程中得到了很多有心人的帮忙，在这里对你们表示感谢与敬意！\n\n脚本重新制作中，文本大多参照了ＰＳＰ版『秋之回忆６·下一篇章』ＫＩＤＳＦＣ特创组的脚本，在此，对ＫＩＤＳＦＣ特创组的前辈们表达最崇高的敬意！\n\n感谢游友『淳淳的牛奶』带作者走进『秋之回忆』的世界。\n\n感谢吧友『青衿』前辈在『命运石之门』上的汉化先例，激发了作者的企划。\n\n感谢吧友『百影虱子』前辈在软件破解上提供的突破性帮助。\n\n感谢扑家汉化组中『七夜沉默』、『小肥婆』、『masaki』三位前辈提供的ＵＩ翻译指导。\n\n最后，着重感谢ＰＳＰ版『秋之回忆６·下一篇章』汉化立项者『星野浩』前辈，作者是在与他交谈中，将这项汉化工作由『兴趣』上升至『责任』的，汉化工作也多受益于他的教导。\n\n同时也感谢在汉化过程中，对各个测试版本提出修改建议的吧友们：\n\n感谢吧友『shianran123』、『SuperGragon』在『结乃＆神奈ＬＩＮＥ』中的指导\n\n感谢吧友『×××』在『克罗艾ＬＩＮＥ』中的指导\n\n感谢吧友『×××』在『莉莉丝ＬＩＮＥ』中的指导\n\n感谢吧友『×××』在『智纱ＬＩＮＥ』中的指导\n\n感谢吧友『×××』在『铃ＬＩＮＥ』中的指导\n\n在此对以上前辈表达崇高的敬意。\n"],
                                    ["『秋之回忆』吧","68","★）－特别信息","Message","DICIMG71","『百度贴吧——秋之回忆吧』是『秋之回忆』系列作品及ＫＩＤ游戏爱好者最大聚集地。\n想获得更多最新的游戏资讯与资源、找到更多的同道中的朋友、分享你独特的游戏见解，请访问【http://tieba.baidu.com/秋之回忆】，我们在这里等着你！\n"],
                                    ]
            def deletter(a):
                i = 0
                if a == "Ａ":
                    i+=1
                    return i
                elif a == "Ｂ":
                    i+=2
                    return i
                elif a == "Ｃ":
                    i+=3
                    return i
                elif a == "Ｄ":
                    i+=4
                    return i
                elif a == "Ｅ":
                    i+=5
                    return i
                elif a == "Ｆ":
                    i+=6
                    return i
                elif a == "Ｇ":
                    i+=7
                    return i
                elif a == "Ｈ":
                    i+=8
                    return i
                elif a == "Ｉ":
                    i+=9
                    return i
                elif a == "Ｊ":
                    i+=10
                    return i
                elif a == "Ｋ":
                    i+=11
                    return i
                elif a == "Ｌ":
                    i+=12
                    return i
                elif a == "Ｍ":
                    i+=13
                    return i
                elif a == "Ｎ":
                    i+=14
                    return i
                elif a == "Ｏ":
                    i+=15
                    return i
                elif a == "Ｐ":
                    i+=16
                    return i
                elif a == "Ｑ":
                    i+=17
                    return i
                elif a == "Ｒ":
                    i+=18
                    return i
                elif a == "Ｓ":
                    i+=19
                    return i
                elif a == "Ｔ":
                    i+=20
                    return i
                elif a == "Ｕ":
                    i+=21
                    return i
                elif a == "Ｖ":
                    i+=22
                    return i
                elif a == "Ｗ":
                    i+=23
                    return i
                elif a == "Ｘ":
                    i+=24
                    return i
                elif a == "Ｙ":
                    i+=25
                    return i
                elif a == "Ｚ":
                    i+=26
                    return i
                elif a == "★":
                    i+=27
                    return i
                
        if persistent.auto_slot == None:
            persistent.auto_slot = 1
        if persistent.scenenamelist==None:
           persistent.scenenamelist =  ["序章",
                                        "一成不变的日常",
                                        "看不见的前路",
                                        "后辈的嘲弄",
                                        "膨胀的期待",
                                        "秘密购物",
                                        "花样苹果",
                                        "一如既往",
                                        "无所适从",
                                        "距离感",
                                        "邪恶妖精",
                                        "意料之外",
                                        "夜的第一章",
                                        "珍爱的笑容",
                                        "憧憬的关系",
                                        "孤挺花—甜美的莉莉丝",
                                        "坚实的后背",
                                        "不能失去之物",
                                        "描出思念的形状",
                                        "丢失的音容",
                                        "勤劳的妻子",
                                        "傻瓜情侣",
                                        "睡眠不足",
                                        "旅行见闻",
                                        "少女的秘密",
                                        "婚后难题",
                                        "两把钥匙",
                                        "不应在的人",
                                        "转机将近",
                                        "我可没有慌张",
                                        "渐行渐近",
                                        "苹果糖分享装",
                                        "心跳的步伐",
                                        "无法消除的距离",
                                        "夏日伊始",
                                        "偶然与必然",
                                        "不许偷看",
                                        "要点些什么",
                                        "违和感",
                                        "重逢与新的邂逅",
                                        "居所",
                                        "突然的再次造访",
                                        "志愿调研",
                                        "女神降临",
                                        "天使袭来",
                                        "巧克力灾难",
                                        "真诚的心意",
                                        "真切地道出",
                                        "传达心声",
                                        "吐露真情",
                                        "重新开始与尾声",
                                        "心灵的婚礼",
                                        "发动引擎",
                                        "热身圈",
                                        "整装待发",
                                        "裁判",
                                        "赛前练习",
                                        "暖胎圈",
                                        "全速前进",
                                        "快速弯道",
                                        "快速圈",
                                        "并列竞速",
                                        "冲刺直道",
                                        "减速弯道",
                                        "急转弯",
                                        "超车点",
                                        "黄旗",
                                        "短暂的休整",
                                        "弯内顶点",
                                        "超越极限",
                                        "最后冲刺",
                                        "心际相遇·黄金时代",
                                        "重新开始",
                                        "往昔的一年",
                                        "散学式",
                                        "创作承载回忆的广播",
                                        "取材？取材！",
                                        "取材？取材！２",
                                        "意见向左",
                                        "交错的约会",
                                        "无法打通的电话",
                                        "将思念抵押",
                                        "收录与纷争",
                                        "让思念乘风破浪",
                                        "评委特别奖",
                                        "因为担心",
                                        "和我一起做吗",
                                        "再会",
                                        "将思念乘风破浪",
                                        "女配角奖",
                                        "警告剧场",
                                        ]
        if persistent.scenelabellist==None:
           persistent.scenelabellist = ["A00A",
                                        "NRI01A",
                                        "NRI02A",
                                        "NRI03A",
                                        "NRI04A",
                                        "NRI05A",
                                        "NRI06A",
                                        "NRI07A",
                                        "NRI08A",
                                        "NRI09A",
                                        "NRI10A",
                                        "NRI11A",
                                        "NRI12A",
                                        "NRI13A",
                                        "NRI14A",
                                        "NRI15A",
                                        "NRI16A",
                                        "NRI17A",
                                        "NRI18A",
                                        "NRIXXA",
                                        "NCH01A",
                                        "NCH02A",
                                        "NCH03A",
                                        "NCH04A",
                                        "NCH05A",
                                        "NCH06A1A",
                                        "NCH06A1B",
                                        "NCH06A1C",
                                        "NCH06A1D",
                                        "NCH06A2",
                                        "NCH07A",
                                        "NCH08A",
                                        "NCH11A",
                                        "NCH09A",
                                        "NCL01A1",
                                        "NCL01A2",
                                        "NCL02A",
                                        "NCL03A",
                                        "NCL04A1",
                                        "NCL04A2",
                                        "NCL04B",
                                        "NCL05A",
                                        "NCL06A",
                                        "NCL07A",
                                        "NCL08A",
                                        "NCL09A1",
                                        "NCL10A",
                                        "NCL11A",
                                        "NCL12A",
                                        "NCL13A",
                                        "NCL14A",
                                        "NCL15A",
                                        "NSU01A",
                                        "NSU02A",
                                        "NSU03A",
                                        "NSU04A",
                                        "NSU05A",
                                        "NSU06A",
                                        "NSU07A",
                                        "NSU08A",
                                        "NSU09A",
                                        "NSU10A",
                                        "NSU11A",
                                        "NSU12A",
                                        "NSU13A",
                                        "NSU14A",
                                        "NSU15A",
                                        "NSU16A",
                                        "NSU17A",
                                        "NSU18A",
                                        "NSU19A",
                                        "NSU20A",
                                        "NSU21A",
                                        "NYU01A",
                                        "NYU01B",
                                        "NYU02A",
                                        "NYU03A",
                                        "NYU04A",
                                        "NYU05A",
                                        "NYU06A",
                                        "NYU07A",
                                        "NYU08A",
                                        "NYU09A",
                                        "NYU10A",
                                        "NYU11A",
                                        "NYU12A",
                                        "NYU13A",
                                        "NYU14A",
                                        "NYU15A",
                                        "NYU16A",
                                        "EX04",
                                        ]
        persistent.speaking = ""
        persistent.android = True # 安卓用
        if persistent.android:
            persistent.videof="mp4"
        else:
            persistent.videof="ogv"
        style.default.font = "default.ttf"
        #自定义了下读取文件方式。偷懒用。
        renpy.music.register_channel("music", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix='bgm/', file_suffix='.ogg', buffer_queue=True)
        renpy.music.register_channel("voice", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
        renpy.music.register_channel("se", mixer="sfx", loop=False, stop_on_mute=True, tight=True, file_prefix='bgm/', file_suffix='.ogg', buffer_queue=True)
        renpy.music.register_channel("sound", mixer="sfx", loop=False, stop_on_mute=True, tight=True, file_prefix='bgm/', file_suffix='.ogg', buffer_queue=True)
        style.default.size = 20
        style.default.color = "#000000" #Makes text black
        config.has_autosave = True
        config.image_cache_size = 16
        #config.default_text_cps = 10
        global in_game,chapter_title,run_time,route_icon,current_route
        in_game=False
        current_route = 0
        begintime=0
        current_icon = " "
        chapter_title= "序章"
        _game_menu_screen="rmenuin"
        def Routeicon(current_route):
            if current_route == 0:
                return " "
            else:
                return "img/meswinicon"+str(current_route)+"@2x.png"
    #----------------------------------------------------------------------------------------------------------------------------------
    #persistent,debug区（记得删除！）
    #$persistent.lastclear = 3
    #$persistent.clearlist = [True]*9
    #$persistent.dictlist=[True]*69
    #$persistent.albumlist = [True]*189
    
    $Preference("skip","all")()
#----------------------------------------------------------------------------------------------------------------------------------
    #temp_flag定义区


