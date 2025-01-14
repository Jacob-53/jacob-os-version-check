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
    from check_os_ver.hi import hi
    from hj_check_os_version.hi import hi
    from lucas_check_os_ver.hi import hi
    from stundrg_check_os_ver.hi import hi
    from cho_check_os_ver.hi import hi
    from nunininu_check_os_ver.hi import hi
    from seo_check_os_version.hi import hi
    import random
    import importlib

    pool={0:"check_os_ver",1:"hj_check_os_version",2:"jacob_os_version_check",3:"lucas_check_os_ver",4:"stundrg_check_os_ver",5:"cho_check_os_ver",6:"nunininu_check_os_ver",7:"seo_check_os_version"}
    whosnext = pool[random.randint(0,7)]
    module = importlib.import_module(whosnext)
    return module.hi()

    print(random_pic())

