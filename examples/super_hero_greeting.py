import spintax
import super_hero_name_generator

# Generate Super hero name
SuperHeroName = super_hero_name_generator.GenerateSuperHeroName()

# Generate greeting
SuperHeroText = r"""
{Hello|Hi|Hey}{,|} I{'| a}m \{0\}{,|!|!!!}
I {{come|am} {here|on this earth}|{came|travelled} {here|to this place}} to {protect|save} {humanity|the world|humans|civilization} {and {destroy|kill|eradicate|remove}|by {destroy|kill|eradicat|remov}ing} all {evil|badness|hate}.
"""
# As the { and } were escaped this allowed us to use .format() to insert the name
print(spintax.spin(SuperHeroText).format(SuperHeroName))
