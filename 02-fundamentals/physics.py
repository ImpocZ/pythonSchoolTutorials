'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.80665 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SUN_GRAVITY = 274 # The surface gravity of the Sun.
SPEED_OF_LIGHT = 299_792_458  #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu
SPEED_OF_THE_FASTEST_JET = 3_292.8 # The speed of NASA X-43 

GRAVITIES = {
    "earth": EARTH_GRAVITY,
    "moon": MOON_GRAVITY,
    "sun": SUN_GRAVITY
}

SPEEDS = {
    "light": SPEED_OF_LIGHT,
    "sound": SPEED_OF_SOUND,
    "jet": SPEED_OF_THE_FASTEST_JET
}

def time_to_travel(distance, speed_type):
    """
    Via this function, we shall calculate how long it would take to travel the distance
    specified by the speed we choose.

    distance is in meters
    speed_type shall depend on the users preference on whether it shall be light, sound or jet.
    
    Sound only travels in an atmosphere, so there is no calculation for Moon or Sun..
    """
    return distance / SPEEDS[speed_type]

def fall_distance(time, gravity_type):
    """
    Via this function, we shall calculate how far would a perfect physical point fall in a specified time and gravity type.
    equation is s = 0.5 *g *t **2

    distance is in meters
    gravity_type will depend on user choice again, earth, moon or sun.
    """
    return 0.5 * GRAVITIES[gravity_type] * (time ** 2)

def fall_time(distance, gravity_type):
    """
    Via this function we shall calculate the time it took to fall the specified distance in a specified environment with a gravity.

    time will be in seconds.
    gravity_type will depend on user choice again, earth, moon or sun.
    """
    return ((2 * distance) / GRAVITIES[gravity_type]) ** 0.5

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''