import spintax


# Function to generate the super hero name
def GenerateSuperHeroName():
    SuperHeroName = spintax.spin(r"{The |}{Super|Scarlet|Commander|Hydro|Captain|Fantastic|Colossal|Nighthawk|Wild} {Mountain|Hawk|Flame|Claw|Machine|Watchman}")
    return SuperHeroName

# Only print name if it is run directly
if __name__ == "__main__":
    print(GenerateSuperHeroName())
