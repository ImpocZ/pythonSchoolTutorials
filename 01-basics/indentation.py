'''
Odsazování v Pythonu (indentation)

Většina programovacích jazyků jako C, C++, Java nebo JavaScript používá k vymezení bloků kódu složené závorky (braces).
V Pythonu se používá odsazování. Blok kódu (např. tělo funkce, cyklu atd.) tedy začíná s odsazením a končí prvním
neodsazeným řádkem.
Počet mezer v odsazení je libovolný, ale musí být konzistentní aspoň v rámci jednoho bloku.
K odsazení musí být použita minimálně jedna mezera.
Obvykle se k odsazování používá tubulátor, který bývá nejčastěji nastaven na 4 mezery.
'''

# Odsazení bloku kódu uvnitř cyklu a podmínky
for i in range(1, 10):
    print(i)
    if i % 2 == 0:
        print('even')
    else:
        print('odd')


'''
Dokumentační řetězce v Pythonu (docstrings)

Víceřádkový řetězec následující hned po záhlaví funkce v Pythonu je nazýván docstring (documentation string neboli 
dokumentační řetězec) a obsahuje stručné vysvětlení toho, co funkce provádí.
Přestože je to nepovinný doplněk programového kódu, je považován za "good programming practice", tedy jednu z dobrých
zásad, které by měl programátor v Pythonu dodržovat.
Docstrings se zapisují mezi trojnásobné uvozovky (tedy podobně jako komentáře).
Tyto dokumentační řetězce jsou přístupné prostřednictvím "magického" __doc__ atributu funkce.    
'''

# Odsazení bloku kódu uvnitř funkce a použití docstring
def greet(name):
    """
    This function greets to the person
    passed in as a parameter
    """
    print("Ahoj, " + name + "!")

# Vypíše docstring spojený s funkcí greet
print(greet.__doc__)
# Vyvolá funkci greet s parametrem 'Hilda'
greet('Hilda')

"""
Cvičení 2:

Vytvořte libovolně pojmenovanou vlastní funkci s minimálně jedním parametrem, v níž využijete cyklus for, 
aspoň jednu podmínku if a funkci print(). Dodržte správné odsazování kódu a opatřete funkci stručnou dokumentací.
Do konzole vypište nejprve docstring vaší funkce a potom zavolejte funkci samotnou.   
"""

# Zkusim vytvorit velice amaterskou a primitivni funkci na prvocisla, asi tam udelam input, at muze uzivatel nastavit range od ceho zacne a u ceho konci
# .. proste nemam zadny jiny napad

def find_prime_number(start_range, end_range):
    """
    This function will attempt to find any prime numbers.
    It shall start from the inputted range and continue its way to the end.
    If it find any prime number, it shall print it out.
    By the way, a prime number is a number, that is only divisible by itself and 1.
    Number one is not a prime number!
    """
    
    for i in range(start_range, end_range + 1):
        not_prime = False
        if i < 2: continue
        for j in range(2, i):
            if i % j == 0:
                not_prime = True
                break
        if not not_prime: print(f"{i} is a prime number") 

def call_the_function():
    first_num = input("Please enter the starting range to find the prime number: ")
    second_num = input("Please enter the end of the range: ")
    print(find_prime_number.__doc__)
    find_prime_number(int(first_num), int(second_num))
call_the_function()