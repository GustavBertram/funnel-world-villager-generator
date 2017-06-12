import math
from lib.dice_tools import *

male_human_name = ['Abeodan','Ace','Acwel','Aelle','Agyfen','Aheawan','Alchfrith','Aldhelm','Alfred','Algar','Alger','Almund','Alwin','Andettan','Andsaca','Andswaru','Andwyrdan','Ane','Archerd','Archibald','Arlice','Astyrian','Avery','Baldlice','Bana','Banan','Bar','Bawdewyn','Beadurinc','Benoic','Benwick','Besyrwan','Betlic','Bronson','Caedwalla','Caflice','Camden','Chapman','Cynewulf','Cynn','Dalston','Deogol','Derian','Drefan','Dreogan','Eadig','Eadlyn','Eamon','Ecgfrith','Edmund','Edmund','Eldrid','Eorl','Farmon','Garrett','Geoff','Gildas','Gimm','Graeme','Grendel','Grimbold','Grimme','Halig','Ham','Landry','Lange','Lar','Leax','Leng','Leof','Lin','List','Lufian','Manton','Norville','Odi','Odin','Oswine','Peada','Perry','Pierce','Prasutagus','Ramm','Rand','Rinc','Ro','Rypan','Scrydan','Seward','Sihtric','Stearc','Stedman','Swift','Tamar','Tolan','Trace','Waelfwulf','Winter','Wissian','Worthington']
female_human_name = ['Acca','Aedre','Aefentid','Aefre','Aethelflaed','Aethelthryth','Alodia','Alodie','Andsware','Anlicnes','Annis','Ar','Ardith','Arianrod','Ashley','Audrey','Bearrocscir','Bernia','Bisgu','Bletsung','Bliss','Blythe','Bodicea','Brigantia','Brimlad','Bysen','Cartimandua','Cearo','Chelsea','Claennis','Clover','Cwen','Cyst','Daedbot','Daisy','Darel','Darelene','Darelle','Darline','Daryl','Dawn','Devona','Dohtor','Don','Eacnung','Eadgyth','Easter','Eda','Edith','Edlyn','Edmunda','Edrys','Eldrida','Elene','Elga','Ellenweorc','Ellette','Elswyth','Elva','Elvina','Engel','Eostre','Erlina','Esma','Estra','Etheswitha','Freya','Garmangabis','Hamia','Harimilla','Hilda','Ifield','Juliana','Kendra','Linette','Lora','Loretta','Lyn','Mae','Maida','Megan','Mercia','Moira','Nelda','Nerthus','Odelia','Ora','Orva','Osberga','Rheda','Rowena','Sibley','Silver','Sulis','Sunniva','Tate','Udele','Viradecthis','Wilda','Willa']
male_dwarf_name = ['Babbar','Borar','Dalor','Dragir','Gindor','Givli','Mavon','Ravan','Thodor','Thorli']
female_dwarf_name = ['Baergi','Belrin','Dagna','Dragrina','Giva','Glorna','Melviel','Tholga','Thorgana','Thorva']
male_elf_name = ['Analith','Celaith','Elromir','Fondel','Galoldur','Horfir','Legoriand','Tinilith','Thrund','Unaramir']
female_elf_name = ['Cadrielith','Deleviel','Eariothiel','Elronia','Galaniel','Legarawen','Milmalith','Sithrade','Tinoniel','Throrfiviel']
male_halfling_name = ['Adelard','Andwise','Calkin','Eldon','Falco','Griffo ','Halfred','Olo','Rosco','Seredoc']
female_halfling_name = ['Amaryllia','Carissa','Donamira','Lavinia','Marigold','Myrtle','Pearl','Ruby','Seraphina','Violet']

def choose_name(gender, race, ineligible=[]):
    name_type = {'Male':   {'Human': male_human_name,   
                            'Dwarf': male_dwarf_name,   
                            'Elf': male_elf_name,   
                            'Halfling': male_halfling_name},
                 'Female': {'Human': female_human_name, 
                            'Dwarf': female_dwarf_name, 
                            'Elf': female_elf_name, 
                            'Halfling': female_halfling_name}}

    return random.choice(list(set(name_type[gender][race])-set(ineligible)))

neutral_physical_traits = ['Big feet', 'Big hands', 'Bloodshot eyes', 'Blue-eyed', 'Bony', 'Booming voice', 'Broad brow', 'Broad shoulders', 'Buck teeth', 'Bushy eyebrows', 'Cleft chin', 'Crooked teeth', 'Curly hair', 'Dark eyes', 'Dark skin', 'Dimples', 'Dirty', 'Fair-haired', 'Fat', 'Freckled', 'Full lips', 'Furrowed brow', 'Glowering', 'Gnarled fingers', 'Greasy-looking', 'Hawk-nosed', 'High cheekbones', 'Hunchback', 'Husky voice', 'Lanky', 'Large ears', 'Large eyes', 'Large nose', 'Lazy eye', 'Limp', 'Long arms', 'Long fingers', 'Long legs', 'Long torso', 'Matted hair', 'Missing teeth', 'Nasal voice', 'Nearsighted', 'One ear', 'One eye', 'One hand', 'Pale skin', 'Peg leg', 'Persistent cough', 'Piercing(s)', 'Plump', 'Pop-eyed', 'Quiet voice', 'Rosy cheeks', 'Rotten teeth', 'Ruddy', 'Scar(s)', 'Scowly', 'Sharp chin', 'Sharp fingernails', 'Short', 'Short hair', 'Skinny', 'Small ears', 'Small eyes', 'Small feet', 'Small hands', 'Small nose', 'Smiley', 'Spade-like hands', 'Stocky', 'Stubby fingers', 'Tall', 'Tattoo(s)', 'Thick neck', 'Unibrow', 'Wavy hair', 'Weathered', 'Well-built', 'Well-groomed', 'Wheezy', 'Whiny voice', 'Wild hair']
male_physical_traits = ['Bald', 'Balding', 'Barrel-chested', 'Broad chest', 'Hairless', 'Hirsute', 'Lambchop sideburns', 'Long beard', 'Long mustache', 'Nose ring', 'Pot-bellied', 'Square jaw'] + neutral_physical_traits
female_physical_traits = ['Big bosom', 'Braided hair', 'Broad hips', 'Long hair', 'Petite', 'Swan-like neck'] + neutral_physical_traits
all_physical_traits = list(set(male_physical_traits) | set(female_physical_traits) | set(neutral_physical_traits))

def choose_physical_trait(gender, race):
    if (race == 'Dwarf' and gender == 'Female'):
        physical_type = all_physical_traits # Female dwarves have facial hair too
    elif (race == 'Elf' and gender == 'Male'):
        physical_type = neutral_physical_traits # Elven males don't have facial hair
    elif (gender == 'Male'):
        physical_type = male_physical_traits
    else:
        physical_type = female_physical_traits

    return random.choice(physical_type)

personality_traits = ['Absentminded','Aggressive','Aloof','Ambitious','Arrogant','Callous','Calm','Cantankerous','Cautious','Cheerful','Coarse','Competitive','Conceited','Confident','Conscientious','Courageous','Courteous','Covetous','Cowardly','Crazy','Crude','Curious','Cynical','Daring','Deceitful','Decisive','Dignified','Disciplined','Drunkard','Earnest','Earthy','Efficient','Egocentric','Enthusiastic','Fatalistic','Fiery','Foolish','Forgiving','Forthright','Friendly','Frugal','Generous','Gentle','Good-natured','Gracious','Greedy','Gullible','Helpful','Honorable','Humble','Honorable','Humble','Impulsive','Kind','Lazy','Libidinous','Loyal','Melancholic','Methodical','Modest','Moralistic','Morbid','Mystical','Naive','Neat','Nihilistic','Obedient','Obsessive','Opportunistic','Optimistic','Outspoken','Paranoid','Peaceful','Pedantic','Plodding','Power-hungry','Protective','Proud','Quiet','Realistic','Religious','Romantic','Sadistic','Sanctimonious','Sarcastic','Secretive','Selfless','Serious','Shrewd','Solitary','Steadfast','Stoic','Stone-cold','Stubborn','Superstitious','Suspicious','Thorough','Timid','Treacherous','Trusting']

def choose_personality_trait():
    return random.choice(personality_traits)

def choose_race_occupation_gear():
    return random.choice([
    ('Human', 'Alewife',       ['rolling pin (close, awkward, 1 wt)', 'cask of ale (2 rations, 2 wt)']), #Brewer
    ('Human', 'Apiarist',      ['staff (close, reach, 1 wt)', d(1,4)+' clay jars of honey (1 wt ea.)']),
    ('Human', 'Apothecary',    ['sickle (close, messy, 1 wt)', 'mortar & pestle (0 wt)']),
    ('Human', 'Baker',         ['baking paddle (reach, awkward, 1 wt)', 'sack of flour (2 wt)']),
    ('Human', 'Bard',          ['knife (hand, 0 wt)', 'instrument: '+choose('voice','flute (0 wt)','lute (1 wt)','horn (1 wt)')]),
    ('Human', 'Basketmaker',   ['knife (hand, 0 wt)', 'sturdy basket (1 wt)']),
    ('Human', 'Beggar',        ['begging bowl (0 wt)', d(1,4)+' coins']),
    ('Human', 'Blacksmith',    ['hammer (close, 1 wt)', 'burlap sack (0 wt)', d(1,4)+' iron ingots (1 wt ea.)']),
    ('Human', 'Boatwright',    ['handaxe (close, 1 wt)', d(2,4)+' planks of wood (1 wt each)']),
    ('Human', 'Bowyer',        ['shortbow (near, far, 1 wt)', 'arrows (1 ammo, 1 wt)', d(1,4)+' sets of staves & sinews (1 wt ea.)']),
    ('Human', 'Bricklayer',    ['trowel (close, awkward, 1 wt)', 'hod (1 wt)', d(2,4)+' bricks (1 wt each)']),
    ('Human', 'Burglar',       ['prybar (close, awkward, 1 wt)', 'burlap sack (0 wt)']),
    ('Human', 'Butcher',       ['cleaver (hand, messy, 1 wt)', 'side of salted beef (4 rations, 2 wt)']),
    ('Human', 'Carpenter',     ['handaxe (close, 1 wt)', 'hand saw (1 wt)']),
    ('Human', 'Cartwright',    ['handaxe (close, 1 wt)', 'pushcart']),
    ('Human', 'Catchpole',     ['club (close, 2 wt)', 'shoulder bag (0 wt)', d(2,6)+' coins']), #Tax Collector
    ('Human', 'Chandler',      ['staff (close, 2-handed, 1 wt)', d(2,4)+' candles (0 wt)']),
    ('Human', 'Chapman',       ['staff (close, 2-handed, 1 wt)', 'rucksack (0 wt)', 'trade item: ' + choose('worthless baubles (0 wt)','smoked fish (2 rations, 1 wt)','adventuring gear (2 uses, 1 wt)','jewelry (25 coins, 0 wt)')]), #Peddler
    ('Human', 'Cheesemaker',   ['staff (close, 2-handed, 1 wt)', 'burlap sack (0 wt)', 'wheel of cheese (4 rations, 2 wt)']),
    ('Human', 'Cobbler',       ['tack hammer (hand, 0 wt)', d(1,4)+' pairs of shoes or boots (1 wt ea.)']),
    ('Human', 'Constable',     ['shortsword (close, 1 wt)', 'set of iron cuffs with key (1 wt)']),
    ('Human', 'Courier',       ['knife (hand, 0 wt)', 'leather satchel (0 wt)', 'important letter (0 wt)']),
    ('Human', 'Crier',         ['knife (hand, 0 wt)', 'plumed hat (worn, 0 wt)']),
    ('Human', 'Crofter',       ['pitchfork (close, reach, 1 wt)', 'bushel of '+choose('turnips','potatoes','onions','oats')+' (4 rations, 2 wt)']), #24 #Farmer
    ('Human', 'Crofter',       ['pitchfork (close, reach, 1 wt)', 'bushel of '+choose('turnips','potatoes','onions','oats')+' (4 rations, 2 wt)']), #25
    ('Human', 'Crofter',       ['pitchfork (close, reach, 1 wt)', 'bushel of '+choose('turnips','potatoes','onions','oats')+' (4 rations, 2 wt)']), #26
    ('Human', 'Crofter',       ['pitchfork (close, reach, 1 wt)', 'bushel of '+choose('turnips','potatoes','onions','oats')+' (4 rations, 2 wt)']), #27
    ('Human', 'Ditch digger',  ['shovel (close, awkward, 2 wt)']),
    ('Human', 'Dung carter',   ['shovel (close, awkward, 2 wt)', 'pushcart full of dung']),
    ('Dwarf', 'Miner',         ['pick (close, +1 damage, 2 wt)', 'adventuring gear ('+d(1,4)+' uses, 1 wt)']),
    ('Dwarf', 'Smith',         ['hammer (close, 1 wt)', 'burlap sack (0 wt)', d(1,4)+' iron ingots (1 wt ea.)']),
    ('Dwarf', 'Mason',         ['hammer (close, 1 wt)', 'chisel (hand, awkward, 1 wt)']),
    ('Dwarf', 'Trapper',       ['knife (hand, 0 wt)', 'burlap sack (0 wt)', d(1,4)+' mole traps (1 wt ea.)']),
    ('Elf',   'Hunter',        ['shortbow (near, far, 1 wt)', 'arrows ('+d(1,4)+' ammo, 1 wt)']),
    ('Elf',   'Troubador',     ['knife (hand, 0 wt)', 'elven lyre (1 wt)']),
    ('Elf',   'Wanderer',      ['staff (close, reach, 1 wt)', 'hooded cloak (worn, 0 wt)']),
    ('Elf',   'Weaver',        ['knife (hand, 0 wt)', 'bolt of silk (2 wt)']),
    ('Human', 'Executioner',   ['executioner\'s axe (close, 2-handed, messy, +1 damage, 2 wt)', 'black hood (worn, 0 wt)']),
    ('Human', 'Falconer',      ['knife (hand, 0 wt)', 'leather gauntlet (0 wt)', 'falcon']),
    ('Human', 'Ferry pilot',   ['club (close, 2 wt)', '10\' pole']),
    ('Human', 'Fisherperson',  ['knife (hand, 0 wt)', 'fishing net (reach, thrown)']), #41
    ('Human', 'Fisherperson',  ['knife (hand, 0 wt)', 'fishing net (reach, thrown)']), #42
    ('Human', 'Fisherperson',  ['knife (hand, 0 wt)', 'fishing net (reach, thrown)']), #43
    ('Human', 'Fletcher',      ['shortbow (near, far, 1 wt)', 'arrows ('+d(1,4)+' ammo, 1 wt)']),
    ('Human', 'Footpad',       ['sap (hand, stun damage, 0 wt)', 'burlap sack (0 wt)']), #Robber
    ('Human', 'Forager',       ['sickle (hand, messy, 1 wt)', 'burlap sack (0 wt)', 'mushrooms ('+d(1,4)+' rations, 1 wt)']),
    ('Human', 'Forester',      ['shortbow (near, far, 1 wt)', 'arrows ('+d(1,4)+' ammo, 1 wt)']),
    ('Human', 'Goatherd',      ['crook (reach, awkward, 1 wt)', d(1,4)+' goats']), #48
    ('Human', 'Goatherd',      ['crook (reach, awkward, 1 wt)', d(1,4)+' goats']), #49
    ('Human', 'Goatherd',      ['crook (reach, awkward, 1 wt)', d(1,4)+' goats']), #50
    ('Human', 'Gravedigger',   ['shovel (close, awkward, 2 wt)']),
    ('Halfling', 'Brewer',     ['staff (close, 2-handed, 1 wt)', 'cask of beer (2 rations, 2 wt)']),
    ('Halfling', 'Cook',       ['cleaver (hand, +1 damage, 1 wt)', 'meat pies ('+d(1,4)+' rations, 1 wt)']),
    ('Halfling', 'Crofter',    ['pitchfork (close, reach, 1 wt)', 'bushel of '+choose('turnips (4 rations','potatoes (4 rations','onions (4 rations','pipeweed (')+', 2wt)']),
    ('Halfling', 'Gardener',   ['spade (hand, awkward, 0 wt)', 'wheelbarrow']),
    ('Human', 'Healer',        ['staff (close, 2-handed, 1 wt)', 'shoulder bag (0 wt)', 'bandages ('+d(1,4)+' uses, slow, 0 wt)']),
    ('Human', 'Hedge wizard',  ['staff (close, 2-handed, 1 wt)', 'belt pouch (0 wt)', 'cantrip: '+choose('Light','Unseen Servant','Prestidigitation')]),
    ('Human', 'Herald',        ['shortsword (close, 1 wt)', 'trumpet (1 wt)']),
    ('Human', 'Herbalist',     ['staff (close, 2-handed, 1 wt)', 'pouch (0 wt)', 'poultices & herbs ('+d(1,4)+' uses, slow, 0 wt)']),
    ('Human', 'Hunter',        ['shortbow (near, far, 1 wt)', 'arrows ('+d(1,4)+' ammo, 1 wt)']), #60
    ('Human', 'Hunter',        ['shortbow (near, far, 1 wt)', 'arrows ('+d(1,4)+' ammo, 1 wt)']), #61
    ('Human', 'Hunter',        ['shortbow (near, far, 1 wt)', 'arrows ('+d(1,4)+' ammo, 1 wt)']), #62
    ('Human', 'Innkeeper',     ['club (close, 2 wt)', 'provisions ('+d(2,4)+' rations, 2 wt)']),
    ('Human', 'Lantern maker', ['hammer (close, 1 wt)', 'lantern (0 wt)', 'flask of oil (0 wt)', 'flint & steel (0 wt)']),
    ('Human', 'Laundress',     ['canvas sack (0 wt)', 'cake of soap (0 wt)']),
    ('Human', 'Miller',        ['club (close, 2 wt)', 'sack of flour (2 wt)']),
    ('Human', 'Miner',         ['pick (close, +1 damage, 2 wt)', 'lantern (0 wt)', 'flask of oil (0 wt)', 'flint & steel (0 wt)']),
    ('Human', 'Monk',          ['staff (close, 2-handed, 1 wt)', 'holy symbol (0 wt)']),
    ('Human', 'Netmaker',      ['knife (hand, 0 wt)', 'fishing net (reach, thrown)', '50\' of rope (2 wt)']),
    ('Human', 'Noble',         ['longsword (close, +1 damage, 1 wt)', 'signet ring (10 coins, 0 wt)']),
    ('Human', 'Oxherd',        ['whip (reach, 1 wt)', 'ox']),
    ('Human', 'Peddler',       ['knife (hand, 0 wt)', 'rucksack (worn, 0 wt)', 'trade item: '+choose('pots & pans (2 wt)', d(2,4)+' knives (hand, 0 wt)', 'adventuring gear ('+d(1,4)+' uses, 2 wt)', d(1,4)+' healing potions (heal 1d8, 0 wt)')]),
    ('Human', 'Pilgrim',       ['staff (close, 2-handed, 1 wt)', 'holy symbol (0 wt)']),
    ('Human', 'Potter',        ['club (close, 2 wt)', 'burlap sack (0 wt)', '5 lbs. of clay (2 wt)']),
    ('Human', 'Prostitute',    ['knife (hand, 0 wt)', 'flask of perfume (0 wt)']),
    ('Human', 'Rat catcher',   ['club (close, 2 wt)', 'burlap sack (0 wt)', d(2,4)+' dead rats (1 wt)']),
    ('Human', 'Ropemaker',     ['club (close, 2 wt)', '100\' of rope (2 wt)']),
    ('Human', 'Scout',         ['knife (hand, 0 wt)', 'cloak (worn, 0 wt)']),
    ('Human', 'Scribe',        [d(2,4)+' pieces of parchment (0 wt)', 'quill & bottle of ink (0 wt)']),
    ('Human', 'Shepherd',      ['crook (reach, awkward, 1 wt)', d(1,4)+' sheep']), #80
    ('Human', 'Shepherd',      ['crook (reach, awkward, 1 wt)', d(1,4)+' sheep']), #81
    ('Human', 'Shepherd',      ['crook (reach, awkward, 1 wt)', d(1,4)+' sheep']), #82
    ('Human', 'Soothsayer',    ['Nothing']),
    ('Human', 'Swineherd',     ['crook (reach, awkward, 1 wt)', d(1,4)+' swine']), #84
    ('Human', 'Swineherd',     ['crook (reach, awkward, 1 wt)', d(1,4)+' swine']), #85
    ('Human', 'Swineherd',     ['crook (reach, awkward, 1 wt)', d(1,4)+' swine']), #86
    ('Human', 'Tanner',        ['knife (hand, 0 wt)', d(2,4)+' animal hides (2 wt)']),
    ('Human', 'Thatcher',      ['handaxe (close, 1 wt)', d(1,4)+' sheaves of straw (1 wt ea.)']),
    ('Human', 'Tinker',        ['tinker\'s tools (0 wt)']),
    ('Human', 'Trapper',       ['knife (hand, 0 wt)', choose(d(2,4)+' rat traps (0 wt)', d(1,4)+' rabbit traps (2 wt)', 'snare trap (1 wt)', 'bear trap (2 wt)')]), #90
    ('Human', 'Trapper',       ['knife (hand, 0 wt)', choose(d(2,4)+' rat traps (0 wt)', d(1,4)+' rabbit traps (2 wt)', 'snare trap (1 wt)', 'bear trap (2 wt)')]), #91
    ('Human', 'Trapper',       ['knife (hand, 0 wt)', choose(d(2,4)+' rat traps (0 wt)', d(1,4)+' rabbit traps (2 wt)', 'snare trap (1 wt)', 'bear trap (2 wt)')]), #92
    ('Human', 'Undertaker',    ['holy symbol (0 wt)', 'coffin (4 wt)']),
    ('Human', 'Watchman',      ['spear (reach, thrown, near, 1 wt)', 'helmet (worn, 0 wt)', 'lantern (0 wt)', 'flask of oil (0 wt)', 'flint & steel (0 wt)', 'horn (0 wt)']), #94
    ('Human', 'Watchman',      ['spear (reach, thrown, near, 1 wt)', 'helmet (worn, 0 wt)', 'lantern (0 wt)', 'flask of oil (0 wt)', 'flint & steel (0 wt)', 'horn (0 wt)']), #95
    ('Human', 'Watchman',      ['spear (reach, thrown, near, 1 wt)', 'helmet (worn, 0 wt)', 'lantern (0 wt)', 'flask of oil (0 wt)', 'flint & steel (0 wt)', 'horn (0 wt)']), #96
    ('Human', 'Weaver',        [d(1,4)+' bolts of fabric (1 wt ea.)']),
    ('Human', 'Woodsman',      ['handaxe (close, 1 wt)', d(2,4)+' sticks of firewood (1 wt ea.)']), #98
    ('Human', 'Woodsman',      ['handaxe (close, 1 wt)', d(2,4)+' sticks of firewood (1 wt ea.)']), #99
    ('Human', 'Woodsman',      ['handaxe (close, 1 wt)', d(2,4)+' sticks of firewood (1 wt ea.)']), #100
    ])

def create_bond(bonder, bonded, villagers):
    if len(villagers) == 0:
        villagers = ['me']
    return random.choice([
        bonded+' has much to teach me about '+choose('love','anger','food','coin','raising children','survival'),
        bonded+' insulted me by '+choose('spitting on me','calling me names','insulting my mother','ignoring me'),
        bonded+' misunderstands me when I say that '+choose('I hate them','I like them','they stink','they are the best among us'),
        bonded+' owes me '+choose('their life','a favor','a kiss','a drink',d(1,4)+' coins','a child'),
        'I am bound to '+bonded+' because '+choose('they are kin','I owe them my life','I have no other friends','I am their property'),
        'I blame '+bonded+' for '+choose('losing that thing','getting me in trouble','my loss of faith','someone\'s death'),
        'I lied to '+bonded+' about '+choose('my feelings','where I hid that thing','my faith','my family'),
        'I saved '+bonded+' from '+choose('drowning','drink','a life of crime','bodily harm'),
        'I respect '+bonded+' for '+choose('listening to me','telling it like it is','their sacrifice','their discipline'),
        'I stole that thing from '+bonded+' because I needed to '+choose('satisfy an urge','feed my family','sell it for profit','practice'),
        bonded+' and I seek knowledge about '+choose('the wider world','beasts and monsters','the ways of the wild','arcane forces'),
        'I trust '+bonded+' because '+choose('we have sworn an oath','they are kin','they are wise','I have no choice'),
        'I will convince '+bonded+' of the value of '+choose('my faith','honor;','power','coin','friendship','knowledge'),
        'I will protect '+bonded+' from '+choose('the truth','dark magic','themself','the others'),
        'I have much to teach '+bonded+' about '+choose('the gods','good','love','teamwork','the wild','the social order'),
        bonded+' must forget about '+choose('their lost loved one','their mistakes','my mistakes','our past together'),
        bonded+' is destined for greatness, because '+choose('the gods have told me so','they have that special glow','I say so','the rest of us are chumps'),
        'I will learn '+bonded+'\'s secret about '+choose('what they stole','where they\'re really from',random.choice(villagers),'me'),
        'I do not trust '+bonded+' because '+choose('they smell','they think they\'re better','they\'re stupid','they\'re just plain evil'),
        'I will soothe '+bonded+'\'s concerns about '+choose(random.choice(villagers),'their missing loved one','coin','our fate')
    ])


class Villager:
    def __init__(self, chosen_names):
        self.gender = choose('Male','Female')

        self.stats = (rollstat('STR'),
                      rollstat('DEX'),
                      rollstat('CON'),
                      rollstat('INT'),
                      rollstat('WIS'),
                      rollstat('CHA'),
                      rollstat('LCK'))

        self.hp = math.ceil(self.stats[2][1] / 4) # CON
        self.load = self.stats[0][2] + 4 #STR
        self.damage = '1d4'
        self.race, self.occupation, self.gear = choose_race_occupation_gear()

        if (self.occupation in ['Alewife','Prostitute']):
            self.gender = 'Female'
        elif (self.occupation in ['Executioner']):
            self.gender = 'Male'

        self.name = choose_name(self.gender, self.race, chosen_names) 
        self.physical_trait = choose_physical_trait(self.gender, self.race)
        self.personality_trait = choose_personality_trait()
        self.bonds = []

        chosen_names.append(self.name)
        
    def someone_else(self, people):
        other_people = list(set(people)-set([self.name]))
        if len(other_people) > 0:
            return random.choice(other_people)
        else:
            return None

    def create_player_bond(self, player_names, all_names):
        bonded = self.someone_else(player_names)
        if bonded != None:
            everyone_else = list( set(all_names) - set([self.name, bonded]))
            self.bonds.append(create_bond(self.name, bonded, everyone_else))


    def create_villager_bond(self, all_names):
        bonded = self.someone_else(all_names)
        everyone_else = list(set(all_names)-set([self.name, bonded]))
        if len(everyone_else) > 0:
            self.bonds.append(create_bond(self.name, bonded, everyone_else))

    def print(self):
        if (self.race == 'Human'):
            print(self.name, '('+self.personality_trait, self.gender, self.occupation+',', self.physical_trait+')')
        else:
            print(self.name, '('+self.personality_trait, self.gender, self.race, self.occupation+',', self.physical_trait+')')

        for stat in self.stats:
            print(stat[0]+':',str(stat[1])+'('+str(stat[2])+')')

        print(' HP:', self.hp)
        print('Load:', self.load)

        print('Gear:')
        for item in self.gear:
            print(' *',item)

        if len(self.bonds) > 0:
            print('BONDS:')
            for bond in self.bonds:
                print(' *', bond)

        print()





