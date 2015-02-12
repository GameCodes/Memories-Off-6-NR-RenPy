# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):
    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
                background None
                area ((1136-952)/2,640-146,952,146)
                id "window"
                fixed:
                    add "img/bgMes@2x.png" align (0.5,1.0)
                    text what id "what" slow_cps True language "eastasian" size 28 color "fff" outlines [(0,"000",1,1)] pos(30,0) xsize 880
                    if current_route != 0:
                        add Routeicon(current_route) pos (0.95,-0.2)

    else:

        # The two window variant.
        #vbox:
            #style "say_two_window_vbox"

            if who:
                window:
                    background None
                    #style "say_who_window"
                    fixed:
                        add "img/bgChrName@2x.png" pos((1136-952)/2,640-146-55)
                        text who:
                            id "who"
                            xanchor 0.5
                            pos((1136-952)/2+236/2,640-146-55+5)
                            
                            language "eastasian"
                            size 28
                            color "fff"
                            outlines [(0,"000",1,1)]
                            bold False

            window:
                background None
                area ((1136-952)/2,640-146,952,146)
                id "window"
                fixed:
                    add "img/bgMes@2x.png" align (0.5,1.0)
                    text what id "what" slow_cps True language "eastasian" size 28 color "fff" outlines [(0,"000",1,1)] pos(30,0) xsize 880
                    if current_route != 0:
                        add Routeicon(current_route) pos (0.95,-0.2)
    if renpy.music.get_playing(channel="voice"):
        $renpy.music.set_volume(0.5,channel="music")
    else:
        $renpy.music.set_volume(1,channel="music")
    # Use the quick menu.
    key "rollback" action Show("text_history",transition=dissolve)
    key "rollforward" action NullAction()
    use quick_menu
    


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 12

            for caption, action, chosen in items:

                if action:
                    
                    button:
                        background None
                        maximum (811,61)
                        idle_child Fixed(Image("img/btnSelect_0@2x.png"),Text(caption,style = "menu_choice",color="fff",outlines=[(0,"000",1,1)]))
                        hover_child Fixed(Image("img/btnSelect_1@2x.png"),Text(caption,style = "menu_choice",color="fff",outlines=[(0,"000",1,1)]))
                        action action
                        #style "menu_choice_button"

                        

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu
label op:
    $_game_menu_screen=""
    $renpy.movie_cutscene("video/MOVIE_OP."+persistent.videof)
    $_game_menu_screen="rmenuin"
    return

transform taptostart:
    align (0.5,0.5)
    alpha 0
    "img/tap_to_start@2x.png"
    block:
        easein 1.0 alpha 1
        easein 1.0 alpha 0
        repeat

screen main_menu(isTapped=False,inMainMenu=False):
    tag menu
    
    default isTapped = False
    default inMainMenu = False
    default titlebg = ""
    if not persistent.allclear:
        if persistent.lastclear:
            $titlebg = "img/titlebg"+str(persistent.lastclear)+"-568h@2x.png"
        else:
            $titlebg = "img/titlebg0-568h@2x.png"
    else:
        $titlebg = "img/titlebg6-568h@2x.png"
    
    if not isTapped:
        on "show" action [Stop("sound"),Stop("se"),Queue("music","BGM01NL")]
        window:
            background "img/titlebg0-568h@2x.png"
        button:
            background None
            xfill True
            yfill True
            add taptostart
            action Show("main_menu",isTapped=True,transition=dissolve)
            activate_sound "SYSSE00"
        timer 10.0 action Start("op")
        add "img/5pb_btn1@2x.png" pos (10,10)
    else:
        if persistent.lastclear==0:
            pass
        elif persistent.lastclear==1 and not inMainMenu:
            timer 0.000001 action Play("music","BGM17")
        elif persistent.lastclear==2 and not inMainMenu:
            timer 0.000001 action Play("music","BGM18")
        elif persistent.lastclear==3 and not inMainMenu:
            timer 0.000001 action Play("music","BGM19")
        elif persistent.lastclear==4 and not inMainMenu:
            timer 0.000001 action Play("music","BGM20")
        elif persistent.lastclear==5 and not inMainMenu:
            timer 0.000001 action Play("music","BGM21")
        elif not inMainMenu:
            timer 0.000001 action Play("music","BGM22NL")
        $inMainMenu=True
        window:
            background titlebg
        imagebutton idle "img/btnT0_0@2x.png" hover "img/btnT0_1@2x.png" pos(0.629,0.3) action Start()
        imagebutton:
            insensitive At("img/btnT1_0@2x.png",Transform(alpha=0.5))
            idle "img/btnT1_0@2x.png"
            hover "img/btnT1_1@2x.png"
            pos(0.629,0.4)
            action If(persistent.lastclear,true=Show("main_menu_to_extra"),false=None)
        imagebutton idle "img/btnT2_0@2x.png" hover "img/btnT2_1@2x.png" pos(0.629,0.5) action Show("main_menu_to_load")
        imagebutton:
            insensitive At("img/btnT3_0@2x.png",Transform(alpha=0.5))
            idle "img/btnT3_0@2x.png"
            hover "img/btnT3_1@2x.png"
            pos(0.629,0.6)
            action If(persistent.lastclear,true=Show("main_menu_to_memories"),false=None)
        imagebutton idle "img/btnT4_0@2x.png" hover "img/btnT4_1@2x.png" pos(0.629,0.7) action Show("mopedia",transition=dissolve)
        imagebutton idle "img/btnT5_0@2x.png" hover "img/btnT5_1@2x.png" pos(0.629,0.8) action Show("preferences",transition=dissolve)
        imagebutton idle "img/5pb_btn1@2x.png" hover "img/5pb_btn2@2x.png" pos(10,10) action OpenURL("http://5pb.jp/games/smapho/")
        imagebutton idle "img/btnHelp0.png" hover "img/btnHelp1.png" align(0.0,1.0) action Show("help",transition=dissolve)
        key "game_menu" action Quit()
transform main_menu_to_load_trans_out:
        Fixed(
            Image("img/btnT0_0@2x.png",pos=(0.63,0.3)),
            ConditionSwitch("persistent.lastclear","img/btnT1_0@2x.png","True",At("img/btnT1_0@2x.png",Transform(alpha=0.5)),pos=(0.63,0.4)),
            Image("img/btnT2_0@2x.png",pos=(0.63,0.5)),
            ConditionSwitch("persistent.lastclear","img/btnT3_0@2x.png","True",At("img/btnT3_0@2x.png",Transform(alpha=0.5)),pos=(0.63,0.6)),
            Image("img/btnT4_0@2x.png",pos=(0.63,0.7)),
            Image("img/btnT5_0@2x.png",pos=(0.63,0.8)),
            pos=(0,0),
            alpha=1.0
            )
        parallel:
            easein 0.5 xpos -0.3
        parallel:
            easein 0.5 alpha 0.0

transform main_menu_to_load_trans_in:
        Fixed(
            Image("img/btnC0_0@2x.png",pos=(0.93,0.45)),
            Image("img/btnC1_0@2x.png",pos=(0.93,0.55)),
            Image("img/btnC2_0@2x.png",pos=(0.93,0.8)),
            pos=(0,0)
            )
        alpha 0
        parallel:
            easein 0.5 xpos -0.3
        parallel:
            easein 0.5 alpha 1

screen main_menu_to_load:
    tag menu
    default titlebg = ""
    if not persistent.allclear:
        if persistent.lastclear:
            $titlebg = "img/titlebg"+str(persistent.lastclear)+"-568h@2x.png"
        else:
            $titlebg = "img/titlebg0-568h@2x.png"
    else:
        $titlebg = "img/titlebg6-568h@2x.png"
    window:
        background titlebg
    add main_menu_to_load_trans_in
    add main_menu_to_load_trans_out
    imagebutton idle "img/5pb_btn1@2x.png" hover "img/5pb_btn2@2x.png" pos(10,10) action OpenURL("http://5pb.jp/games/smapho/")
    timer 0.5 action Show("main_menu_load")

transform load_to_main_menu_trans_in:
        Fixed(
            Image("img/btnT0_0@2x.png",pos=(0.33,0.3)),
            ConditionSwitch("persistent.lastclear","img/btnT1_0@2x.png","True",At("img/btnT1_0@2x.png",Transform(alpha=0.5)),pos=(0.33,0.4)),
            Image("img/btnT2_0@2x.png",pos=(0.33,0.5)),
            ConditionSwitch("persistent.lastclear","img/btnT3_0@2x.png","True",At("img/btnT3_0@2x.png",Transform(alpha=0.5)),pos=(0.33,0.6)),
            Image("img/btnT4_0@2x.png",pos=(0.33,0.7)),
            Image("img/btnT5_0@2x.png",pos=(0.33,0.8)),
            pos=(0,0),
            )
        alpha 0.0
        parallel:
            easein 0.5 xpos 0.3
        parallel:
            easein 0.5 alpha 1.0

transform load_to_main_menu_trans_out:
        Fixed(
            Image("img/btnC0_0@2x.png",pos=(0.63,0.45)),
            Image("img/btnC1_0@2x.png",pos=(0.63,0.55)),
            Image("img/btnC2_0@2x.png",pos=(0.63,0.8)),
            pos=(0,0)
            )
        parallel:
            easein 0.5 xpos 0.3
        parallel:
            easein 0.5 alpha 0.0



screen load_to_main_menu:
    tag menu
    default titlebg = ""
    if not persistent.allclear:
        if persistent.lastclear:
            $titlebg = "img/titlebg"+str(persistent.lastclear)+"-568h@2x.png"
        else:
            $titlebg = "img/titlebg0-568h@2x.png"
    else:
        $titlebg = "img/titlebg6-568h@2x.png"
    window:
        background titlebg
    add load_to_main_menu_trans_in
    add load_to_main_menu_trans_out
    imagebutton idle "img/5pb_btn1@2x.png" hover "img/5pb_btn2@2x.png" pos(10,10) action OpenURL("http://5pb.jp/games/smapho/")
    timer 0.5 action Show("main_menu",isTapped=True,inMainMenu=True)
    
    
screen main_menu_load:
    tag menu
    default titlebg = ""
    if not persistent.allclear:
        if persistent.lastclear:
            $titlebg = "img/titlebg"+str(persistent.lastclear)+"-568h@2x.png"
        else:
            $titlebg = "img/titlebg0-568h@2x.png"
    else:
        $titlebg = "img/titlebg6-568h@2x.png"
    window:
        background titlebg
    imagebutton:
        idle "img/btnC0_0@2x.png"
        hover "img/btnC0_1@2x.png"
        action [FilePage("1"),Show("load",transition=dissolve,quick=False)]
        pos (0.631,0.45)
    imagebutton:
        idle "img/btnC1_0@2x.png"
        hover "img/btnC1_1@2x.png"
        action [FilePage("quick"),Show("load",transition=dissolve,quick=True)]
        pos (0.631,0.55)
    imagebutton:
        idle "img/btnC2_0@2x.png"
        hover "img/btnC2_1@2x.png"
        action Show("load_to_main_menu")
        pos (0.631,0.8)
    imagebutton idle "img/5pb_btn1@2x.png" hover "img/5pb_btn2@2x.png" pos(10,10) action OpenURL("http://5pb.jp/games/smapho/")


transform main_menu_to_memories_trans_out:
        Fixed(
            Image("img/btnT0_0@2x.png",pos=(0.63,0.3)),
            ConditionSwitch("persistent.lastclear","img/btnT1_0@2x.png","True",At("img/btnT1_0@2x.png",Transform(alpha=0.5)),pos=(0.63,0.4)),
            Image("img/btnT2_0@2x.png",pos=(0.63,0.5)),
            ConditionSwitch("persistent.lastclear","img/btnT3_0@2x.png","True",At("img/btnT3_0@2x.png",Transform(alpha=0.5)),pos=(0.63,0.6)),
            Image("img/btnT4_0@2x.png",pos=(0.63,0.7)),
            Image("img/btnT5_0@2x.png",pos=(0.63,0.8)),
            pos=(0,0),
            alpha=1.0
            )
        parallel:
            easein 0.5 xpos -0.3
        parallel:
            easein 0.5 alpha 0.0

transform main_menu_to_memories_trans_in:
        Fixed(
            Image("img/btnM0_0@2x.png",pos=(0.93,0.3)),
            Image("img/btnM1_0@2x.png",pos=(0.93,0.4)),
            Image("img/btnM2_0@2x.png",pos=(0.93,0.5)),
            Image("img/btnM3_0@2x.png",pos=(0.93,0.6)),
            Image("img/btnM5_0@2x.png",pos=(0.93,0.8)),
            pos=(0,0)
            )
        alpha 0.0
        parallel:
            easein 0.5 xpos -0.3
        parallel:
            easein 0.5 alpha 1.0
screen main_menu_to_memories:
    tag menu
    default titlebg = ""
    if not persistent.allclear:
        if persistent.lastclear:
            $titlebg = "img/titlebg"+str(persistent.lastclear)+"-568h@2x.png"
        else:
            $titlebg = "img/titlebg0-568h@2x.png"
    else:
        $titlebg = "img/titlebg6-568h@2x.png"
    window:
        background titlebg
    imagebutton idle "img/5pb_btn1@2x.png" hover "img/5pb_btn2@2x.png" pos(10,10) action OpenURL("http://5pb.jp/games/smapho/")
    add main_menu_to_memories_trans_in
    add main_menu_to_memories_trans_out
    timer 0.5 action Show("main_menu_memories")

transform memories_to_main_menu_trans_in:
    Fixed(
            Image("img/btnT0_0@2x.png",pos=(0.33,0.3)),
            ConditionSwitch("persistent.lastclear","img/btnT1_0@2x.png","True",At("img/btnT1_0@2x.png",Transform(alpha=0.5)),pos=(0.33,0.4)),
            Image("img/btnT2_0@2x.png",pos=(0.33,0.5)),
            ConditionSwitch("persistent.lastclear","img/btnT3_0@2x.png","True",At("img/btnT3_0@2x.png",Transform(alpha=0.5)),pos=(0.33,0.6)),
            Image("img/btnT4_0@2x.png",pos=(0.33,0.7)),
            Image("img/btnT5_0@2x.png",pos=(0.33,0.8)),
            pos=(0,0),
            alpha=1.0
            )
    alpha 0
    parallel:
        easein 0.5 xpos 0.3
    parallel:
        easein 0.5 alpha 1.0

transform memories_to_main_menu_trans_out:
    Fixed(
        Image("img/btnM0_0@2x.png",pos=(0.63,0.3)),
        Image("img/btnM1_0@2x.png",pos=(0.63,0.4)),
        Image("img/btnM2_0@2x.png",pos=(0.63,0.5)),
        Image("img/btnM3_0@2x.png",pos=(0.63,0.6)),
        Image("img/btnM5_0@2x.png",pos=(0.63,0.8)),
        pos=(0,0)
        )
    parallel:
        easein 0.5 xpos 0.3
    parallel:
        easein 0.5 alpha 0.0
            
            
screen memories_to_main_menu:
    tag menu
    default titlebg = ""
    if not persistent.allclear:
        if persistent.lastclear:
            $titlebg = "img/titlebg"+str(persistent.lastclear)+"-568h@2x.png"
        else:
            $titlebg = "img/titlebg0-568h@2x.png"
    else:
        $titlebg = "img/titlebg6-568h@2x.png"
    window:
        background titlebg
    add memories_to_main_menu_trans_in
    add memories_to_main_menu_trans_out
    imagebutton idle "img/5pb_btn1@2x.png" hover "img/5pb_btn2@2x.png" pos(10,10) action OpenURL("http://5pb.jp/games/smapho/")
    timer 0.5 action Show("main_menu",isTapped=True,inMainMenu=True)


screen main_menu_memories(fromMusic=False):
    tag menu
    default titlebg = ""
    if not persistent.allclear:
        if persistent.lastclear:
            $titlebg = "img/titlebg"+str(persistent.lastclear)+"-568h@2x.png"
        else:
            $titlebg = "img/titlebg0-568h@2x.png"
    else:
        $titlebg = "img/titlebg6-568h@2x.png"
    if fromMusic:
        if persistent.lastclear==0:
            timer 0.000001 action Play("music","BGM01NL")
        elif persistent.lastclear==1:
            timer 0.000001 action Play("music","BGM17")
        elif persistent.lastclear==2:
            timer 0.000001 action Play("music","BGM18")
        elif persistent.lastclear==3:
            timer 0.000001 action Play("music","BGM19")
        elif persistent.lastclear==4:
            timer 0.000001 action Play("music","BGM20")
        elif persistent.lastclear==5:
            timer 0.000001 action Play("music","BGM21")
        else:
            timer 0.000001 action Play("music","BGM22NL")
    window:
        background titlebg
    imagebutton idle "img/btnM0_0@2x.png" hover "img/btnM0_1@2x.png" pos(0.631,0.3) action Show("clearlist",transition=dissolve)
    imagebutton idle "img/btnM1_0@2x.png" hover "img/btnM1_1@2x.png" pos(0.631,0.4) action Show("album",transition=dissolve)
    imagebutton idle "img/btnM2_0@2x.png" hover "img/btnM2_1@2x.png" pos(0.631,0.5) action Show("music",transition=dissolve)
    imagebutton idle "img/btnM3_0@2x.png" hover "img/btnM3_1@2x.png" pos(0.631,0.6) action Show("movie",transition=dissolve)
    imagebutton idle "img/btnM5_0@2x.png" hover "img/btnM5_1@2x.png" pos(0.631,0.8) action Show("memories_to_main_menu")
    imagebutton idle "img/5pb_btn1@2x.png" hover "img/5pb_btn2@2x.png" pos(10,10) action OpenURL("http://5pb.jp/games/smapho/")

screen main_menu_extra:
    tag menu
    default titlebg = ""
    if not persistent.allclear:
        if persistent.lastclear:
            $titlebg = "img/titlebg"+str(persistent.lastclear)+"-568h@2x.png"
        else:
            $titlebg = "img/titlebg0-568h@2x.png"
    else:
        $titlebg = "img/titlebg6-568h@2x.png"
    window:
        background titlebg
    imagebutton idle "img/btnE0_0@2x.png" hover "img/btnE0_1@2x.png" pos(0.631,0.5) action Start("EX04")
    imagebutton idle "img/btnE1_0@2x.png" hover "img/btnE1_1@2x.png" pos(0.631,0.8) action Show("extra_to_main_menu")
    imagebutton idle "img/5pb_btn1@2x.png" hover "img/5pb_btn2@2x.png" pos(10,10) action OpenURL("http://5pb.jp/games/smapho/")

transform main_menu_to_extra_trans_out:
    Fixed(
            Image("img/btnT0_0@2x.png",pos=(0.63,0.3)),
            ConditionSwitch("persistent.lastclear","img/btnT1_0@2x.png","True",At("img/btnT1_0@2x.png",Transform(alpha=0.5)),pos=(0.63,0.4)),
            Image("img/btnT2_0@2x.png",pos=(0.63,0.5)),
            ConditionSwitch("persistent.lastclear","img/btnT3_0@2x.png","True",At("img/btnT3_0@2x.png",Transform(alpha=0.5)),pos=(0.63,0.6)),
            Image("img/btnT4_0@2x.png",pos=(0.63,0.7)),
            Image("img/btnT5_0@2x.png",pos=(0.63,0.8)),
            pos=(0,0),
            alpha=1.0
            )
    parallel:
            easein 0.5 xpos -0.3
    parallel:
            easein 0.5 alpha 0.0
    
transform main_menu_to_extra_in:
    Fixed(
            Image("img/btnE0_0@2x.png",pos=(0.93,0.5)),
            Image("img/btnE1_0@2x.png",pos=(0.93,0.8)),
            pos=(0,0)
            )
    alpha 0.0
    parallel:
            easein 0.5 xpos -0.3
    parallel:
            easein 0.5 alpha 1.0

screen main_menu_to_extra:
    tag menu
    default titlebg = ""
    if not persistent.allclear:
        if persistent.lastclear:
            $titlebg = "img/titlebg"+str(persistent.lastclear)+"-568h@2x.png"
        else:
            $titlebg = "img/titlebg0-568h@2x.png"
    else:
        $titlebg = "img/titlebg6-568h@2x.png"
    window:
        background titlebg
    imagebutton idle "img/5pb_btn1@2x.png" hover "img/5pb_btn2@2x.png" pos(10,10) action OpenURL("http://5pb.jp/games/smapho/")
    add main_menu_to_extra_trans_out
    add main_menu_to_extra_in
    timer 0.5 action Show("main_menu_extra")

transform extra_to_main_menu_trans_in:
    Fixed(
            Image("img/btnT0_0@2x.png",pos=(0.33,0.3)),
            ConditionSwitch("persistent.lastclear","img/btnT1_0@2x.png","True",At("img/btnT1_0@2x.png",Transform(alpha=0.5)),pos=(0.33,0.4)),
            Image("img/btnT2_0@2x.png",pos=(0.33,0.5)),
            ConditionSwitch("persistent.lastclear","img/btnT3_0@2x.png","True",At("img/btnT3_0@2x.png",Transform(alpha=0.5)),pos=(0.33,0.6)),
            Image("img/btnT4_0@2x.png",pos=(0.33,0.7)),
            Image("img/btnT5_0@2x.png",pos=(0.33,0.8)),
            pos=(0,0),
            alpha=1.0
            )
    alpha 0
    parallel:
        easein 0.5 xpos 0.3
    parallel:
        easein 0.5 alpha 1.0

transform extra_to_main_menu_trans_out:
    Fixed(
        Image("img/btnE0_0@2x.png",pos=(0.63,0.5)),
        Image("img/btnE1_0@2x.png",pos=(0.63,0.8)),
        pos=(0,0)
        )
    parallel:
        easein 0.5 xpos 0.3
    parallel:
        easein 0.5 alpha 0.0

screen extra_to_main_menu:
    tag menu
    default titlebg = ""
    if not persistent.allclear:
        if persistent.lastclear:
            $titlebg = "img/titlebg"+str(persistent.lastclear)+"-568h@2x.png"
        else:
            $titlebg = "img/titlebg0-568h@2x.png"
    else:
        $titlebg = "img/titlebg6-568h@2x.png"
    window:
        background titlebg
    imagebutton idle "img/5pb_btn1@2x.png" hover "img/5pb_btn2@2x.png" pos(10,10) action OpenURL("http://5pb.jp/games/smapho/")
    add extra_to_main_menu_trans_out
    add extra_to_main_menu_trans_in
    timer 0.5 action Show("main_menu",isTapped=True,inMainMenu=True)

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen in_game_hide_menu:
    tag menu
    timer 0.5 action Return()

screen file_picker(quick=False):
    $runtime=renpy.get_game_runtime()
    $runtime_h=int(runtime/3600)
    $runtime = runtime % 3600
    $runtime_m=int(runtime/60)
    $runtime = runtime % 60
    $runtime_s = int(runtime /1)
    python:
        global save_name
        save_name = chapter_title+"-"+Routeicon(current_route)+"-"+str(runtime_h)+"-"+str(runtime_m)+"-"+str(runtime_s)
    if quick==True:
        timer 0.0000001 action FilePage("quick")
    if not quick:
        hbox:
            style_group "file_picker_nav"
            align (0.45,.97)

            textbutton _("Previous"):
                text_size 28
                action FilePagePrevious()

            textbutton _("Auto"):
                text_size 28
                action FilePage("auto")

            for i in range(1, 11):
                textbutton str(i):
                    text_size 28
                    action FilePage(i)
            textbutton _("Next"):
                text_size 28
                action FilePageNext(max=10)
    imagebutton idle "img/btnBack_0@2x.png" hover "img/btnBack_1@2x.png" action If(in_game or _in_replay,false=Show("main_menu_load",transition=dissolve),true=Show("in_game_hide_menu",transition=dissolve)) align (0.98,0.98)
    key 'game_menu'action If(in_game or _in_replay,false=Show("main_menu_load",transition=dissolve),true=[Show("in_game_hide_menu",transition=dissolve)])
    grid 2 3:
        transpose True
        area (166,107,800,480)
        for i in range(1,7):
            button:
                action [SetField(persistent,"total_playtime",persistent.total_playtime+renpy.get_game_runtime()-begintime),SetVariable("begintime",renpy.get_game_runtime()),FileAction(i)]
                background None
                xfill True
                if quick==True:
                    add "img/cellQLoad0@2x.png"
                else:
                    add "img/cellLoad0@2x.png"

               # Add the screenshot.
                add FileScreenshot(i,empty="img/saveload_screenshot_default@2x.png") pos(39,13)
                $ file_name = FileSlotName(i, 6)
                $ file_time = FileTime(i, empty="")
                $ save_name_now = FileSaveName(i)
                default c=""
                default icon=""
                default h=0
                default m=0
                default s=0
                python:
                    if len(save_name_now)>=5:
                        c , icon , h , m , s = save_name_now.split("-")
                if FileNewest(file_name):
                    add "img/icoNew@2x.png" pos(39,75)
                if FileLoadable(i):
                    if file_name[0]!= 'q' and file_name[0]!= 'a':
                        text "%02d" % int(file_name) xpos 6 ypos 0.32 size 25 color "0044aa" outlines [(0,"fff",1,1)]
                        text c pos(180,13) size 25 color "fff"
                        if len(icon)==22:
                            add icon pos(180,30)
                        text "游戏时间" xanchor 0.0 pos(180,75) size 16 color "fff"
                        text "%02d:%02d:%02d" % (int(h),int(m),int(s)) xanchor 1.0 pos(340,75)  size 16 color "fff"
                        text FileTime(i,format="%Y/%m/%d") xanchor 0.0 pos(180,95) size 16 color "fff"
                        text FileTime(i,format="%H:%M") xanchor 1.0 pos(340,95) size 16 color "fff"
                    else:
                        $file_name = file_name[1:]
                        text "%02d" % int(file_name) xpos 6 ypos 0.32 size 25 color "0044aa"
                        if file_time!="":
                            text c pos(180,13) size 25 color "fff"
                            if len(icon)==22:
                                add icon pos(180,30)
                            text "游戏时间" xanchor 0.0 pos(180,75) size 16 color "fff"
                            text "%02d:%02d:%02d" % (int(h),int(m),int(s)) xanchor 1.0 pos(340,75)  size 16 color "fff"
                            text FileTime(i,format="%Y/%m/%d") xanchor 0.0 pos(180,95) size 16 color "fff"
                            text FileTime(i,format="%H:%M") xanchor 1.0 pos(340,95) size 16 color "fff"
                else:
                    if file_name[0]!= 'q' and file_name[0]!= 'a':
                        text "%02d" % int(file_name) xpos 6 ypos 0.32 size 25 color "0044aa" outlines [(0,"fff",1,1)]
                        text "No Data" xanchor 0.0 pos(230,50) size 25 color "fff"
                    else:
                        $file_name = file_name[1:]
                        text "%02d" % int(file_name) xpos 6 ypos 0.32 size 25 color "0044aa"
                        text "No Data" xanchor 0.0 pos(230,50) size 25 color "fff"
                key "save_delete" action FileDelete(i)
#    frame:
#        style "file_picker_frame"
#
#        has vbox
#
#        # The buttons at the top allow the user to pick a
#        # page of files.
#        hbox:
#            style_group "file_picker_nav"
#
#            textbutton _("Previous"):
#                action FilePagePrevious()
#
#            textbutton _("Auto"):
#                action FilePage("auto")
#
#            textbutton _("Quick"):
#                action FilePage("quick")
#
#            for i in range(1, 9):
#                textbutton str(i):
#                    action FilePage(i)
#
#            textbutton _("Next"):
#                action FilePageNext()
#
#        $ columns = 2
#        $ rows = 5
#
#        # Display a grid of file slots.
#        grid columns rows:
#            transpose True
#            xfill True
#            style_group "file_picker"
#
#            # Display ten file slots, numbered 1 - 10.
#            for i in range(1, columns * rows + 1):
#
#                # Each file slot is a button.
#                button:
#                    action FileAction(i)
#                    xfill True
#
#                    has hbox
#
#                    # Add the screenshot.
#                    add FileScreenshot(i)
#
#                    $ file_name = FileSlotName(i, columns * rows)
#                    $ file_time = FileTime(i, empty=_("Empty Slot."))
#                    $ save_name = FileSaveName(i)
#
#                    text "[file_name]. [file_time!t]\n[save_name!t]"
#
#                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu
    window:
        background "img/bgSave-568h@2x.jpg"
    use file_picker

screen load(quick=False):

   # This ensures that any other menu screen is replaced.
    tag menu
    if quick == False:
        window:
            background "img/bgLoad-568h@2x.jpg"
    else:
        window:
            background "img/bgQLoad-568h@2x.jpg"
   #use navigation
    use file_picker(quick=quick)

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
#

screen preferences:
    tag menu
    window:
        background "img/optionbg-568h@2x.jpg"
    side "c r":
        pos (122,83)
        spacing 50
        viewport:
            id "vp"
            child_size (860,1050)
            area (0,0,860,430)
            draggable True
            mousewheel True
            add "img/settings@2x.png"
            bar pos (460,9) value Preference("text speed") xsize 350 ysize 36 thumb "img/ice_big@2x.png" style None left_bar None right_bar None
            bar pos (460,89) value Preference("auto-forward time") xsize 350 ysize 36 thumb "img/ice_big@2x.png" style None left_bar None right_bar None bar_invert True
            bar pos (460,489) value MixerValue("voice") xsize 350 ysize 36 thumb "img/ice_big@2x.png" style None left_bar None right_bar None
            bar pos (460,569) value MixerValue("music") xsize 350 ysize 36 thumb "img/ice_big@2x.png" style None left_bar None right_bar None
            bar pos (460,649) value MixerValue("sound") xsize 350 ysize 36 thumb "img/ice_big@2x.png" style None left_bar None right_bar None
            imagebutton idle "img/checkYes0@2x.png" hover "img/checkYes1@2x.png" selected_idle "img/checkYes1@2x.png" action Preference("automatic move", "enable") pos (400,159)
            imagebutton idle "img/checkNo0@2x.png" hover "img/checkNo1@2x.png" selected_idle "img/checkNo1@2x.png" action Preference("automatic move", "disable") pos (700,159)
            imagebutton idle "img/checkYes0@2x.png" hover "img/checkYes1@2x.png" selected_idle "img/checkYes1@2x.png" action Preference("voice sustain", "enable") pos (400,239)
            imagebutton idle "img/checkNo0@2x.png" hover "img/checkNo1@2x.png" selected_idle "img/checkNo1@2x.png" action Preference("voice sustain", "disable") pos (700,239)
            imagebutton idle "img/checkEachSelection0@2x.png" hover "img/checkEachSelection1@2x.png" selected_idle "img/checkEachSelection1@2x.png" selected_hover "img/checkEachSelection0@2x.png" action SetField(persistent,"autosave_choice",True) pos (400,319)
            imagebutton idle "img/checkEachScene0@2x.png" hover "img/checkEachScene1@2x.png" selected_idle "img/checkEachScene1@2x.png" selected_hover "img/checkEachScene0@2x.png" action SetField(persistent,"autosave_scene",True) pos (700,319)
            imagebutton idle "img/checkYes0@2x.png" hover "img/checkYes1@2x.png" selected_idle "img/checkYes1@2x.png" action SetField(persistent,"show_dict",True) pos (400,399)
            imagebutton idle "img/checkNo0@2x.png" hover "img/checkNo1@2x.png" selected_idle "img/checkNo1@2x.png" action SetField(persistent,"show_dict",False) pos (700,399)
            imagebutton idle "img/chr1_0@2x.png" hover "img/chr1_1@2x.png" selected_hover "img/chr1_1@2x.png" selected_idle "img/chr1_2@2x.png" action ToggleVoiceMute("RRS") pos (400,720)
            imagebutton idle "img/chr2_0@2x.png" hover "img/chr2_1@2x.png" selected_hover "img/chr2_1@2x.png" selected_idle "img/chr2_2@2x.png" action ToggleVoiceMute("CHI") pos (515,720)
            imagebutton idle "img/chr3_0@2x.png" hover "img/chr3_1@2x.png" selected_hover "img/chr3_1@2x.png" selected_idle "img/chr3_2@2x.png" action ToggleVoiceMute("KLE") pos (630,720)
            imagebutton idle "img/chr4_0@2x.png" hover "img/chr4_1@2x.png" selected_hover "img/chr4_1@2x.png" selected_idle "img/chr4_2@2x.png" action ToggleVoiceMute("RIN") pos (745,720)
            imagebutton idle "img/chr5_0@2x.png" hover "img/chr5_1@2x.png" selected_hover "img/chr5_1@2x.png" selected_idle "img/chr5_2@2x.png" action ToggleVoiceMute("YUN") pos (400,785)
            imagebutton idle "img/chr6_0@2x.png" hover "img/chr6_1@2x.png" selected_hover "img/chr6_1@2x.png" selected_idle "img/chr6_2@2x.png" action ToggleVoiceMute("HEN") pos (515,785)
            imagebutton idle "img/chr7_0@2x.png" hover "img/chr7_1@2x.png" selected_hover "img/chr7_1@2x.png" selected_idle "img/chr7_2@2x.png" action ToggleVoiceMute("SHI") pos (630,785)
            imagebutton idle "img/chr8_0@2x.png" hover "img/chr8_1@2x.png" selected_hover "img/chr8_1@2x.png" selected_idle "img/chr8_2@2x.png" action ToggleVoiceMute("ZX") pos (745,785)
            imagebutton idle "img/chr9_0@2x.png" hover "img/chr9_1@2x.png" selected_hover "img/chr9_1@2x.png" selected_idle "img/chr9_2@2x.png" action ToggleVoiceMute("SN") pos (400,850)
            imagebutton idle "img/chr10_0@2x.png" hover "img/chr10_1@2x.png" selected_hover "img/chr10_1@2x.png" selected_idle "img/chr10_2@2x.png" action ToggleVoiceMute("XW") pos (515,850)
            imagebutton idle "img/chr11_0@2x.png" hover "img/chr11_1@2x.png" selected_hover "img/chr11_1@2x.png" selected_idle "img/chr11_2@2x.png" action ToggleVoiceMute("XL") pos (630,850)
            imagebutton idle "img/chr12_0@2x.png" hover "img/chr12_1@2x.png" selected_hover "img/chr12_1@2x.png" selected_idle "img/chr12_2@2x.png" action ToggleVoiceMute("FMK") pos (745,850)
            imagebutton idle "img/chr13_0@2x.png" hover "img/chr13_1@2x.png" selected_hover "img/chr13_1@2x.png" selected_idle "img/chr13_2@2x.png" action ToggleVoiceMute("ERZ") pos (400,915)
            imagebutton idle "img/chr14_0@2x.png" hover "img/chr14_1@2x.png" selected_hover "img/chr14_1@2x.png" selected_idle "img/chr14_2@2x.png" action ToggleVoiceMute("XIZ") pos (515,915)
            imagebutton idle "img/chr15_0@2x.png" hover "img/chr15_1@2x.png" selected_hover "img/chr15_1@2x.png" selected_idle "img/chr15_2@2x.png" action ToggleVoiceMute("MAX") pos (630,915)
            imagebutton idle "img/chr16_0@2x.png" hover "img/chr16_1@2x.png" selected_hover "img/chr16_1@2x.png" selected_idle "img/chr16_2@2x.png" action ToggleVoiceMute("NER") pos (745,915)
            imagebutton idle "img/chr17_0@2x.png" hover "img/chr17_1@2x.png" selected_hover "img/chr17_1@2x.png" selected_idle "img/chr17_2@2x.png" action ToggleVoiceMute("ELS") pos (400,980)
        vbar value YScrollValue("vp")
        
    
        
    imagebutton idle "img/btnBack_0@2x.png" hover "img/btnBack_1@2x.png" action If(in_game or _in_replay,false=Show("main_menu",transition=dissolve,isTapped=True,inMainMenu=True),true=[Show("in_game_hide_menu",transition=dissolve)]) align (0.98,0.98)
    imagebutton:
        align (0.8,0.98)
        idle "img/default_normal@2x.png"
        hover "img/default_tapping@2x.png"
        action [
    Preference("automatic move", "enable"),
    Preference("voice sustain", "disable"),
    SetField(persistent,"autosave_choice",True),
    SetField(persistent,"autosave_scene",True),
    SetVoiceMute("RRS",False),
    SetVoiceMute("CHI",False),
    SetVoiceMute("KLE",False),
    SetVoiceMute("RIN",False),
    SetVoiceMute("YUN",False),
    SetVoiceMute("HEN",False),
    SetVoiceMute("SHI",False),
    SetVoiceMute("ZX",False),
    SetVoiceMute("SN",False),
    SetVoiceMute("XW",False),
    SetVoiceMute("XL",False),
    SetVoiceMute("FMK",False),
    SetVoiceMute("ERZ",False),
    SetVoiceMute("XIZ",False),
    SetVoiceMute("MAX",False),
    SetVoiceMute("NER",False),
    SetVoiceMute("ELS",False),
    ]
    key 'game_menu'action If(in_game or _in_replay,false=Show("main_menu",transition=dissolve,isTapped=True,inMainMenu=True),true=[Show("in_game_hide_menu",transition=dissolve)])
    
    #screen preferences():
#
#    tag menu
#
#    # Include the navigation.
#    use navigation
#
#    # Put the navigation columns in a three-wide grid.
#    grid 3 1:
#        style_group "prefs"
#        xfill True
#
#        # The left column.
#        vbox:
#            frame:
#                style_group "pref"
#                has vbox
#
#                label _("Display")
#                textbutton _("Window") action Preference("display", "window")
#                textbutton _("Fullscreen") action Preference("display", "fullscreen")
#
#            frame:
#                style_group "pref"
#                has vbox
#
#                label _("Transitions")
#                textbutton _("All") action Preference("transitions", "all")
#                textbutton _("None") action Preference("transitions", "none")
#
#            frame:
#                style_group "pref"
#                has vbox
#
#                label _("Text Speed")
#                bar value Preference("text speed")
#
#            frame:
#                style_group "pref"
#                has vbox
#
#                textbutton _("Joystick...") action Preference("joystick")
#
#
#        vbox:
#            frame:
#                style_group "pref"
#                has vbox
#
#                label _("Skip")
#                textbutton _("Seen Messages") action Preference("skip", "seen")
#                textbutton _("All Messages") action Preference("skip", "all")
#
#            frame:
#                style_group "pref"
#                has vbox
#
#                textbutton _("Begin Skipping") action Skip()
#
#            frame:
#                style_group "pref"
#                has vbox
#
#                label _("After Choices")
#                textbutton _("Stop Skipping") action Preference("after choices", "stop")
#                textbutton _("Keep Skipping") action Preference("after choices", "skip")
#
#            frame:
#                style_group "pref"
#                has vbox
#
#                label _("Auto-Forward Time")
#                bar value Preference("auto-forward time")
#
#                if config.has_voice:
#                    textbutton _("Wait for Voice") action Preference("wait for voice", "le")
#
#        vbox:
#            frame:
#                style_group "pref"
#                has vbox
#
#                label _("Music Volume")
#                bar value Preference("music volume")
#
#            frame:
#                style_group "pref"
#                has vbox
#
#                label _("Sound Volume")
#                bar value Preference("sound volume")
#
#                if config.sample_sound:
#                    textbutton _("Test"):
#                        action Play("sound", config.sample_sound)
#                        style "soundtest_button"
#
#            if config.has_voice:
#                frame:
#                    style_group "pref"
#                    has vbox
#
#                    label _("Voice Volume")
#                    bar value Preference("voice volume")
#
#                    textbutton _("Voice Sustain") action Preference("voice sustain", "le")
#                    if config.sample_voice:
#                        textbutton _("Test"):
#                            action Play("voice", config.sample_voice)
#                            style "soundtest_button"
#
#init -2:
#    style pref_frame:
#        xfill True
#        xmargin 5
#        top_margin 5
#
#    style pref_vbox:
#        xfill True
#
#    style pref_button:
#        size_group "pref"
#        xalign 1.0
#
#    style pref_slider:
#        xmaximum 192
#        xalign 1.0
#
#    style soundtest_button:
#        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True
    if not in_game or _in_replay:
        window:
            #add Solid("000000")
            background At("img/LaunchImage-700-568h@2x.png",Transform(rotate=270.0,align=(0.5,0.5)))
            #style "gm_root"

        frame:
            #style_group "yesno"
            
            #xfill True
            #xmargin .05
            #ypos .1
            #yanchor 0
            #ypadding .05
            align (.5,.1)
            background None
            maximum(720,212)
            if message == layout.LOADING:
                add "img/checkLoad@2x.png" align (.5,.5)
            elif message == layout.OVERWRITE_SAVE:
                add "img/checkResave@2x.png" align (.5,.5)
            elif message == layout.MAIN_MENU:
                add "img/checkTitle@2x.png" align (.5,.5)
            else:
                add "img/bgMessageView@2x.png" align (.5,.5)
                text _(message) align (0.5,0.3) size 30 color "fff"
            
            hbox:
                align (.5,.9)
                spacing 100
                imagebutton idle "img/btnCheckBox0_0@2x.png" hover "img/btnCheckBox0_1@2x.png" action yes_action
                imagebutton idle "img/btnCheckBox1_0@2x.png" hover "img/btnCheckBox1_1@2x.png" action no_action
    else:
        #window:
            #background At("img/LaunchImage-700-568h@2x.png",Transform(rotate=270.0,align=(0.5,0.5)))
            #style "gm_root"

        frame:
            #style_group "yesno"
            
            #xfill True
            #xmargin .05
            #ypos .1
            #yanchor 0
            #ypadding .05
            align (.5,.5)
            background None
            maximum(720,212)
            if message == layout.LOADING:
                add "img/checkLoad@2x.png" align (.5,.5)
            elif message == layout.OVERWRITE_SAVE:
                add "img/checkResave@2x.png" align (.5,.5)
            elif message == layout.MAIN_MENU:
                add "img/checkTitle@2x.png" align (.5,.5)
            else:
                add "img/bgMessageView@2x.png" align (.5,.5)
                text _(message) align (0.5,0.3) size 30 color "fff"
            
            hbox:
                align (.5,.9)
                spacing 100
                imagebutton idle "img/btnCheckBox0_0@2x.png" hover "img/btnCheckBox0_1@2x.png" action yes_action
                imagebutton idle "img/btnCheckBox1_0@2x.png" hover "img/btnCheckBox1_1@2x.png" action no_action
                
#            has vbox:
#                xalign .5
#                yalign .5
#                spacing 30
#
#            label _(message):
#                xalign 0.5
#
#            hbox:
#                xalign 0.5
#                spacing 100
#
#                textbutton _("Yes") action yes_action
#                textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        #textbutton _("Back") action Rollback()
        #textbutton _("Save") action ShowMenu('save')
        #textbutton _("Q.Save") action QuickSave()
        #textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action [Preference("auto-forward", "disable"),Skip(),SelectedIf(None)] text_size 25
        #textbutton "强制快进" action [Preference("skip", "all"),Preference("auto-forward", "disable"),Skip(),SelectedIf(None)] text_size 25
        textbutton _("Auto") action [Preference("auto-forward", "enable"),Show("autologo")] text_size 25
        #textbutton _("Prefs") action ShowMenu('preferences')

screen autologo:
    add "img/auto@2x.png" pos(12,7)
    button:
        background None
        action [Preference("auto-forward", "disable"),Hide("autologo")]

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"
        


transform rmenu_in_trans:
    Fixed(
        Image("img/bgMenu@2x.png",align=(1.0,0.5)),
        Image("img/btnMenu0_0@2x.png",align=(0.98,0.2)),
        Image("img/btnMenu1_0@2x.png",align=(0.98,0.3)),
        Image("img/btnMenu2_0@2x.png",align=(0.98,0.4)),
        Image("img/btnMenu3_0@2x.png",align=(0.98,0.5)),
        Image("img/btnMenu4_0@2x.png",align=(0.98,0.6)),
        Image("img/btnMenu5_0@2x.png",align=(0.98,0.7)),
        ConditionSwitch("_in_replay","img/btnMenu6_0@2x.png","True","img/btnMenu7_0@2x.png",align=(0.98,0.8)),
        )
    xpos 0.5
    easein 0.5 xpos 0.0

screen rmenuin:
    tag menu
    add rmenu_in_trans
    timer 0.5 action Show("rmenu")

screen rmenu:
    tag menu
    #on "show" action stopvoc
    key 'game_menu' action Show("rmenuhide")
    add "img/bgMenu@2x.png" align (1.0,0.5)
    imagebutton idle "img/btnMenu0_0@2x.png" hover "img/btnMenu0_1@2x.png" action [QuickSave(),Show("rmenuhide")] align (0.98,0.2)
    imagebutton idle "img/btnMenu1_0@2x.png" hover "img/btnMenu1_1@2x.png" action Show("load",quick=True,transition=dissolve) align (0.98,0.3)
    imagebutton idle "img/btnMenu2_0@2x.png" hover "img/btnMenu2_1@2x.png" action Show("save",transition=dissolve) align (0.98,0.4)
    imagebutton idle "img/btnMenu3_0@2x.png" hover "img/btnMenu3_1@2x.png" action Show("load",transition=dissolve) align (0.98,0.5)
    imagebutton idle "img/btnMenu4_0@2x.png" hover "img/btnMenu4_1@2x.png" action Show("preferences",transition=dissolve) align (0.98,0.6)
    imagebutton idle "img/btnMenu5_0@2x.png" hover "img/btnMenu5_1@2x.png" action Show("mopedia",transition=dissolve) align (0.98,0.7)
    if _in_replay:
        imagebutton idle "img/btnMenu6_0@2x.png" hover "img/btnMenu6_1@2x.png" action MainMenu() align (0.98,0.8)
    else:
        imagebutton idle "img/btnMenu7_0@2x.png" hover "img/btnMenu7_1@2x.png" action MainMenu() align (0.98,0.8)

transform rmenu_out_trans:
    Fixed(
        Image("img/bgMenu@2x.png",align=(1.0,0.5)),
        Image("img/btnMenu0_0@2x.png",align=(0.98,0.2)),
        Image("img/btnMenu1_0@2x.png",align=(0.98,0.3)),
        Image("img/btnMenu2_0@2x.png",align=(0.98,0.4)),
        Image("img/btnMenu3_0@2x.png",align=(0.98,0.5)),
        Image("img/btnMenu4_0@2x.png",align=(0.98,0.6)),
        Image("img/btnMenu5_0@2x.png",align=(0.98,0.7)),
        ConditionSwitch("_in_replay","img/btnMenu6_0@2x.png","True","img/btnMenu7_0@2x.png",align=(0.98,0.8)),
        )
    xpos 0.0
    easein 0.5 xpos 0.5

screen rmenuhide:
    tag menu
    add rmenu_out_trans
    timer 0.2 action Return()

transform tipsin:
    xcenter .5
    yanchor 1.0
    
    easein 1 ypos 81
transform tipstextin:
    yanchor 1.0
    ypos -30
    xpos 70
    easein 1 ypos 51
transform tipstextout(i):
    yanchor 1.0
    pos(70,51)
    Text('"{color=#f00}'+persistent.dictinfo[i][0]+'{/color}"'+'词条已登陆。')
    easeout 1 ypos -30

screen dict_pop(i=0):
    tag pop
    if not persistent.show_dict: 
        timer 0.00000001 action Hide("dict_pop")
    else:
        text '"{color=#f00}'+persistent.dictinfo[i][0]+'{/color}"'+'词条已登陆。' at tipstextin
        timer 3 action [Show("tipshide"),Add(Null(),tipstextout(i),i=3)]

screen tipshide:
    tag pop
    timer 0.000001 action Hide("tipshide")
    
    
screen help:
    tag menu
    window:
        background "img/bgHelp-568h@2x.jpg"
    key "game_menu" action Show("main_menu",isTapped=True,inMainMenu=True,transition=dissolve)
    imagebutton idle "img/btnBack_0@2x.png" hover "img/btnBack_1@2x.png" action Show("main_menu",isTapped=True,inMainMenu=True,transition=dissolve) align (0.98,0.98)
    viewport:
        pos (0.22,0.18)
        maximum (675,360)
        draggable True
        mousewheel True
        $t = "本作品由bakery面包工坊的百影虱子完成。\n感谢Ren'Py引擎的制作者Pytom提供的引擎，百度贴吧吧友『秋可可丶』提供的汉化脚本和修改后的图片，chen_xin_ming大大的音频解包脚本，以及KIDS FANS CHANNEL特别创作组组长冰天火焰的文本授权。\n该移植游戏禁止用于商业目的，由此造成的一切后果由违约者自行承担。\n\n面包工坊微博：\n\n百度秋之回忆贴吧："
        text t color "fff" size 24 outlines [(0,"000",1,1)]
        textbutton "点此进入" action OpenURL("http://www.weibo.com/u/5186767799") pos (.35,.52)
        textbutton "点此进入" action OpenURL("http://tieba.baidu.com/f?kw=%E7%A7%8B%E4%B9%8B%E5%9B%9E%E5%BF%86&fr=index&fp=0&ie=utf-8") pos (.35,.65)