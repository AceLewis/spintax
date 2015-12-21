import spintax
# Don't use this it is not secure it is only an example
# Only 470,400 possible unique combinations

# Function to generate password
def GenerateSuperHeroName():
    SuperHeroName = spintax.parse(r"{The|One|A|}{Big|Large|Small|Tiny|Giant|Titanic|Massive}{Blue|Red|Green|Yellow|Purple|Violet|Rose|Black|White|Pink}{Dog|Cat|Pig|Cow|Chicken|Rabbit|Sheep|Duck|Goat|Elephant}{Is|IsNow|HasBeen|Was|WasJust|}{Happily|Gladly|Joyfully|}{Eating|Jumping|Running|Walking|Smiling|Playing|Laughing}")
    return SuperHeroName[0]

# Only print password if it is run directly
if __name__ == "__main__":
    print(GenerateSuperHeroName())

