from dataclasses import dataclass


@dataclass
class Country:
    name: str
    currency: str
    population: int
    vvp: float

    @staticmethod
    def travel(name="guests"):
        print(f"come again, {name}")

    @classmethod
    def loy_currency(cls, name, currency, population, vvp):
        return cls(name, currency.upper(), population, vvp)


def f(obj):
    return f"{type(obj).__name__}(name='{obj.name}', continent={obj.continent}, currency='{obj.currency}', population={obj.population}, vvp={obj.vvp}) "


CountryPlace = type("EurCountry",
                    (Country,),
                    {"continent": "undefined", "__str__": f})

belarus = Country("Belarus", "BYN", 9_255_500, 1.2)
belarus.travel("anna")
print(belarus)
greece = Country.loy_currency("Greece", "eur", 10_800_000, 8.5)
print(greece)

belarus2 = CountryPlace("Belarus", "BYN", 9_255_500, 1.2)
belarus2.continent = "Europe"
print(belarus2)
