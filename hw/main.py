from wine import Wine
from beer import Beer
from market import Market

"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""

wineCollection = [
    Wine('Chardonnay', '11.10.1999'),
    Wine('Merlot', '01.01.1998'),
    Wine('White zinfandel', '10.12.2009'),
    Wine('Pinot grigio', '27.05.1789'),
    Wine('Pinot noir', '31.12.2023')
]

beerCollection = [
    Beer('Sorbet Malina', '07.01.2024'),
    Beer('Pumpkin Mead', '07.01.2024'),
    Beer('IPA Every Day', '07.01.2024'),
    Beer('Christmas Ale', '24.12.2023'),
    Beer('Berry Porter', '01.12.2023')
]

partyMarket = Market(wineCollection, beerCollection)

print('Test 1: has_drink_with_title()')
print('\t',
      partyMarket.has_drink_with_title('Pinot noir'),
      partyMarket.has_drink_with_title('Christmas Ale'),
      partyMarket.has_drink_with_title('PiPinot'),
      '\n'
      )

print('Test 2: get_drinks_sorted_by_title()')
sortedPartyMarket = partyMarket.get_drinks_sorted_by_title()
for i in range(len(sortedPartyMarket)):
    print('\t', sortedPartyMarket[i])
print()

print('Test 3: get_drinks_by_production_date()')
periodPartyMarket = partyMarket.get_drinks_by_production_date('10.10.2000', '10.12.2023')
for i in range(len(periodPartyMarket)):
    print('\t', periodPartyMarket[i])
