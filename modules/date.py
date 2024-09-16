import time 
from datetime import datetime

# Converti les mois en chiffre en lettres
def chiffre_intoMonth(month):
        match month:
            case 1:
                return 'janvier'
            case 2:
                return 'février'
            case 3:
                return 'mars'
            case 4:
                return 'avril'
            case 5:
                return 'mai'
            case 6:
                return 'juin'
            case 7:
                return 'juillet'
            case 8:
                return 'août'
            case 9:
                return 'septembre'
            case 10:
                return 'octobre'
            case 11:
                return 'novembre'
            case 12:
                return 'décembre'
            case _:
                return 'invalid month'

# Calcule le décallage des jours et traduits en lettres
def anglais_intoJourFrancais(jour, decalage):
    if decalage == 0:
        match jour:
            case "Monday":
                return 'lun'
            case 'Tuesday':
                return 'mar'
            case 'Wednesday':
                return 'mer'
            case 'Thursday':
                return 'jeu'
            case 'Friday':
                return 'ven'
            case 'Saturday':
                return 'sam'
            case 'Sunday':
                return 'dim'
            case _:
                return 'invalid jour'
    elif decalage == 1:
        match jour:
            case "Monday":
                return 'mar'
            case 'Tuesday':
                return 'mer'
            case 'Wednesday':
                return 'jeu'
            case 'Thursday':
                return 'ven'
            case 'Friday':
                return 'sam'
            case 'Saturday':
                return 'dim'
            case 'Sunday':
                return 'lun'
            case _:
                return 'invalid jour'
    elif decalage == 2:
        match jour:
            case "Monday":
                return 'mer'
            case 'Tuesday':
                return 'jeu'
            case 'Wednesday':
                return 'ven'
            case 'Thursday':
                return 'sam'
            case 'Friday':
                return 'dim'
            case 'Saturday':
                return 'lun'
            case 'Sunday':
                return 'mar'
            case _:
                return 'invalid jour'
    elif decalage == 3:
        match jour:
            case "Monday":
                return 'jeu'
            case 'Tuesday':
                return 'ven'
            case 'Wednesday':
                return 'sam'
            case 'Thursday':
                return 'dim'
            case 'Friday':
                return 'lun'
            case 'Saturday':
                return 'mar'
            case 'Sunday':
                return 'mer'
            case _:
                return 'invalid jour'
    elif decalage == 4:
        match jour:
            case "Monday":
                return 'ven'
            case 'Tuesday':
                return 'sam'
            case 'Wednesday':
                return 'dim'
            case 'Thursday':
                return 'lun'
            case 'Friday':
                return 'mar'
            case 'Saturday':
                return 'mer'
            case 'Sunday':
                return 'jeu'
            case _:
                return 'invalid jour'
    elif decalage == 5:
        match jour:
            case "Monday":
                return 'sam'
            case 'Tuesday':
                return 'dim'
            case 'Wednesday':
                return 'lun'
            case 'Thursday':
                return 'mar'
            case 'Friday':
                return 'mer'
            case 'Saturday':
                return 'jeu'
            case 'Sunday':
                return 'ven'
            case _:
                return 'invalid jour'
    elif decalage == 6:
        match jour:
            case "Monday":
                return 'dim'
            case 'Tuesday':
                return 'lun'
            case 'Wednesday':
                return 'mar'
            case 'Thursday':
                return 'mer'
            case 'Friday':
                return 'jeu'
            case 'Saturday':
                return 'ven'
            case 'Sunday':
                return 'sam'
            case _:
                return 'invalid jour'

def testChiffreJour(chiffre, decalage):
    today = datetime.today()
    month = today.month

    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month == 2:
        if (today.year % 4 == 0 and today.year % 100 != 0) or (today.year % 400 == 0):
            max_days = 29
        else:
            max_days = 28
    else:
        max_days = 30

    if chiffre + decalage > max_days:
        return chiffre + decalage - max_days
    else:
        return chiffre + decalage

def testMoisNumero(chiffre, decalage):
    today = datetime.today()
    month = today.month

    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month == 2:
        if (today.year % 4 == 0 and today.year % 100 != 0) or (today.year % 400 == 0):
            max_days = 29
        else:
            max_days = 28
    else:
        max_days = 30

    if chiffre + decalage > max_days:
        next_month = month + 1 if month < 12 else 1
        return chiffre_intoMonth(next_month)
    else:
        return chiffre_intoMonth(month)