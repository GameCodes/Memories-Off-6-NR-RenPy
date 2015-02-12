label splashscreen:
    show expression At("img/LaunchImage-700-568h@2x.png",Transform(rotate=270.0,align=(0.5,0.5))) as presplash
    pause 1
    if persistent.resumable:
        $persistent.resumable=False
        call screen yesno_prompt("发现中断存档。从该存档继续游戏吗？", FileLoad(100,page="auto",confirm=False),Return())
    hide presplash
    $persistent.resumable=False
    show expression "img/Z_mageslogo@2x.png" as splash with dissolve
    pause 1
    show expression "img/Z_5pblogo@2x.png" as splash with dissolve
    pause 1
    show expression "img/Z_mtrix@2x.png"  as splash with dissolve
    pause 1
    return
    
label after_load:
    $begintime=renpy.get_game_runtime()
    return
label quit:
    $persistent.total_playtime += renpy.get_game_runtime()-begintime
    if in_game:
        $runtime=renpy.get_game_runtime()
        $runtime_h=int(runtime/3600)
        $runtime = runtime % 3600
        $runtime_m=int(runtime/60)
        $runtime = runtime % 60
        $runtime_s = int(runtime /1)
        python:
            global save_name
            save_name = chapter_title+"-"+Routeicon(current_route)+"-"+str(runtime_h)+"-"+str(runtime_m)+"-"+str(runtime_s)
            renpy.save("auto-100",extra_info=save_name)
            persistent.resumable=True
    return

transform motor_eff_movein:
    block:
        xanchor 1.0
        xpos 0.0
        linear 1 xpos 2.0
        repeat
transform motor_eff_moveout:
    block:
        xanchor 0.0
        xpos 0.0
        linear 0.5 xpos 1.0
        xpos -1.0
        linear 0.5 xpos 0.0
        repeat


# The game starts here.
label start:
    $in_game=True
    $auto_slot = 1
    $current_route = 0
    python:
        F0=0
        F2=0
        F4=0
        F1=0
        F3=0
        F5=0
        F96=0
        F71=0
        F72=0
        F73=0
        F74=0
        F83=0
        F84=0
        F103=0
        F108=0
        F105=0
    call A00A
    call op
    if F16==1:
        $current_route = 1
        jump L_ROUTE_RRS
    if F16==2:
        $current_route = 2
        jump L_ROUTE_CHS
    if F16==3:
        $current_route = 3
        jump L_ROUTE_CLE
    if F16==5:
        $current_route = 5
        jump L_ROUTE_SUZ
    if F16==4:
        $current_route = 4
        jump L_ROUTE_YUN
label L_ROUTE_RRS:
    call NRI01A
    call NRI02A
    call NRI03A
    call NRI04A
    call NRI05A
    call NRI06A
    call NRI07A
    call NRI08A
    call NRI09A
    call NRI10A
    call NRI11A
    call NRI12A
    call NRI13A
    call NRI14A
    call NRI15A
    call NRI16A
    call NRI17A
    if F108:
        jump L_RRS_BAD
    jump L_RRS_GOOD
label L_RRS_GOOD:
    call NRI18A
    $persistent.clearlist[0]=True
    $persistent.lastclear = 1
    call ed_ririsu
    jump ALL_CLEAR_CHECK
label L_RRS_BAD:
    call NRIXXA
    $persistent.clearlist[1]=True
    call ending
    jump ALL_CLEAR_CHECK
label L_ROUTE_CHS:
    call NCH01A
    call NCH02A
    call NCH03A
    call NCH04A
    call NCH05A
    call NCH06A1A
    call NCH06A1B
    if F14=="NCH06A1C":
        jump L_NCH06A1C
    else:
        jump L_NCH06A1D
label L_NCH06A1C:
    call NCH06A1C
    jump L_NCH06A2
label L_NCH06A1D:
    call NCH06A1D
    jump L_NCH06A2
label L_NCH06A2:
    call NCH06A2
    call NCH06A3
    call NCH07A
    if F108:
        jump L_CHS_BAD
    jump L_CHS_GOOD
label L_CHS_GOOD:
    call NCH08A
    call NCH11A
    $persistent.clearlist[2]=True
    $persistent.lastclear = 2
    call ed_chisa
    jump ALL_CLEAR_CHECK
label L_CHS_BAD:
    call NCH09A
    call NCH10A
    $persistent.clearlist[3]=True
    call ending
    jump ALL_CLEAR_CHECK
label L_ROUTE_CLE:
    call NCL01A1
    call NCL01A2
    call NCL02A
    call NCL03A
    call NCL04A1
    call NCL04A2
    call NCL04B
    call NCL05A
    call NCL06A
    call NCL07A
    call NCL08A
    call NCL09A1
    call NCL09A2
    call NCL10A
    call NCL11A
    call NCL12A
    call NCL13A
    call NCL14A
    call NCL15A
    python:
        persistent.albumlist[persistent.albuminfo.index("EVN_CL02A")]=True
        persistent.albumlist[persistent.albuminfo.index("EVN_CL06A")]=True
        persistent.albumlist[persistent.albuminfo.index("EVN_CL06B")]=True
        persistent.albumlist[persistent.albuminfo.index("EVN_CL06C")]=True
    $persistent.clearlist[4]=True
    $persistent.lastclear = 3
    call ed_chloe
    jump ALL_CLEAR_CHECK
label L_ROUTE_YUN:
    call NYU01A
    call NYU01B
    call NYU02A
    call NYU03A
    call NYU04A
    call NYU05A
    call NYU06A
    if F16==4:
        jump L_YUN_GOOD
    if F16==6:
        jump L_ROUTE_KAN
label L_YUN_GOOD:
    call NYU07A
    call NYU08A
    call NYU09A
    call NYU10A
    call NYU11A
    $persistent.clearlist[7]=True
    $persistent.lastclear = 4
    call ed_yuno
    jump ALL_CLEAR_CHECK
label L_ROUTE_KAN:
    call NYU12A
    call NYU13A
    call NYU14A
    call NYU15A
    call NYU16A
    $persistent.clearlist[8]=True
    call ending
    jump ALL_CLEAR_CHECK
label L_ROUTE_SUZ:
    call NSU01A
    call NSU02A
    call NSU03A
    call NSU04A
    call NSU05A
    call NSU06A
    call NSU07A
    call NSU08A
    call NSU09A
    call NSU10A
    call NSU11A
    call NSU12A
    call NSU13A
    call NSU14A
    call NSU15A
    call NSU16A
    call NSU17A
    if F108!=0:
        jump L_SUZ_GOOD
    jump L_SUZ_BAD
label L_SUZ_GOOD:
    call NSU18A
    call NSU19A
    call NSU20A
    $persistent.clearlist[5]=True
    $persistent.lastclear = 5
    python:
        persistent.albumlist[persistent.albuminfo.index("EVN_SU02A")]=True
        persistent.albumlist[persistent.albuminfo.index("EVN_SU02B")]=True
        persistent.albumlist[persistent.albuminfo.index("EVN_SU02E")]=True
        persistent.albumlist[persistent.albuminfo.index("EVN_SU02F")]=True
        persistent.albumlist[persistent.albuminfo.index("EVN_SU02G")]=True
        persistent.albumlist[persistent.albuminfo.index("EVN_SU02H")]=True
        persistent.albumlist[persistent.albuminfo.index("EVN_SU02I")]=True
        persistent.albumlist[persistent.albuminfo.index("EVN_SU02J")]=True
        persistent.albumlist[persistent.albuminfo.index("EVN_SU02K")]=True
        persistent.albumlist[persistent.albuminfo.index("EVN_SU02L")]=True
    call ed_rin
    jump ALL_CLEAR_CHECK
label L_SUZ_BAD:
    call NSU21A
    $persistent.clearlist[6]=True
    call ending
    jump ALL_CLEAR_CHECK
    return
label ALL_CLEAR_CHECK:
    $persistent.total_playtime += renpy.get_game_runtime()
    $persistent.dictlist[66]=True
    $persistent.dictlist[67]=True
    $persistent.dictlist[68]=True
    python:
        i = 0
        for e in persistent.clearlist:
            if e:
                i += 1
        if i>=9:
            persistent.allclear = True
            for j in range(-9,0):
                persistent.albumlist[j]=True
            persistent.dictlist = [True]*69
            persistent.albumlist = [True]*189
    return