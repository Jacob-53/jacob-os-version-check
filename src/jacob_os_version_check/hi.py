art = """
===============================+***+============================================
======================+*####@%@%*++**#*=========================================
====================+#*+==##+==+*#+++++%#=======================================
===================*#+===##+#%##*++====++*##*===================================
==================+#+==+#%*=-::::::::::::::-=+#*================================
==================*#+##=**:::::::::::::::::::::-##==============================
==================*@*-::=#:::::::::::::::::::::::=#*============================
=================#%#=::::=-:::::::::::::::::::::::-*#===========================
================%+::::::::::::::::::::::::::::::::::*#==========================
==============+@-::::::::::::::::::::::::::::::::::::*#=========================
==============%=::::::::::::::::::::::::::::::::::::::%*========================
=============**:::::::::::::::::::::::::::::::::::::::-@========================
=============%+::::::::::::::::::::::::::::::::::::::::+%=======================
=============%=:::::::::::::::::::::::::::::::::::::::::#*======================
=============%=:::::::::::::::::::::::::::::::::::::::::-%+=====================
=============**-::::::::::::::::::::::::::::::::::::::::-##+====================
=============+%-::::::::::::::::::::::::::::::::::::::::::=#+===================
==============#+:::::::::::::::::-=+++++++=::::::-=+*****++**===================
==============+%:::::::::::::::=*+=:......-+*=:=*+-.......-*#+==================
===============#+::::::::::::=#=.............=%+............-#+=================
===============+%:::::::::::+*:................#:........  ..:%=================
================%+::+@*::::=*:..................%........   ..**================
============+#+=+%::*+#=:::+=... ...............*-....-*:   ..=#================
============+%%%=%=-*=-%-::+=... :%@=.    ......*-....*@=   ..**================
=============%*+@%*=*-:+#::=+:.. ..:..    .....:%.......... .=#=================
=============*#==%%**-::%=::*=....        .....%@#*+=----##:=#+=================
=============+%===#@*:::=#:::+*.........  ...-%-::::::::::=#*===================
==============#*==+#-::::::::::#%:.........=@+::::::::::::-**===================
==================#@**%%:::::::::-*@@@@@@%=::::::::::::::-*%+===================
================+%=*%#=::::::::::::::::::-----==+*##%%%@@%==##==================
================#*:+#--#:::::::::::--+%@%+=------------------+%=================
================*#-+=:::::::::::-+%#=-------------------------+%================
=================*#+===**:::::-*%=-----------------------------#*===============
===================+#%=::::::-#+-------------------------------+%===============
====================**-:::::-#+---------------------------------@===============
====================**-:::::+*=---------------------------------*#==============
====================#+:::::-*+----===---------------------------+%==============
===================+#=:::::-*+---=##=-----------------------=+*#*===============
===================**-:::::-*+---+****#####***********###%##*+==================
===================#+:::::::**=----------===============#*======================
==================+#=:::::::-#=---------------------=+#%+=======================
=============+#%%%%*:::::::::=%=-------------------+#*==========================
============**:=::#=::::::::::-%*----------------=*%+===========================
===========*+...+%*:::::::::::::=##=------------*%*=============================
==========+*:.....+#=:::::::::::::-=#%#*+===+#%%+===============================
=========+*-........:##-:::::::::::::::------=%@*===============================
=========*+............:#%=::::::::::::::::::*+..*@*============================
========*+.....         ...=##=-:::::::::::::*=.....+%+=========================
=======+@:.....         .......:*%*+---::::::*=.......#*========================
========+%*:...         ............:#%*-::::=%=...:*-:%++======================
========%-.+*-....      ............++.:%-::::-*#.:*=..-%++=====================
====+++#*:...-**-:....          ...=+....*+-::::=%*%-...+#+=====================
+*#*=-::-+*+-...:+*+-:.......   ..=+......=*=::::+*-*-...#*+====================
+...........-*+:....:=*+=:.......=*.........+*-:+*..-#-::-#+====================
...............**........-+*=-..=*...........:**#....=%+***+=======+============


"""


def hi():
    print(art)

def random_pic():
    from check_os_ver.hi import hi as r1
    from hj_check_os_version.hi import hi as r2
    from lucas_check_os_ver.hi import hi as r3
    from stundrg_check_os_ver.hi import hi as r4
    from cho_check_os_ver.hi import hi as r5
    from nunininu_check_os_ver.hi import hi as r6
    from seo_check_os_version.hi import hi as r7
    import random

    pool=[r1,r2,r3,r4,r5,r6,r7]
    whosnext = random.choice(pool)()
    return(whosnext)


