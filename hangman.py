stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# a=1
# word_list = []
display = []
words = ''
end = False
lives = 6
points = 0
print('''
 .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--. 
/ .. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \
\ \/\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ \/ /
 \/ /`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\/ / 
 / /\                                                                                                                    / /\ 
/ /\ \   █████                                                                                                          / /\ \
\ \/ /  ░░███                                                                                                           \ \/ /
 \/ /    ░███████    ██████   ████████    ███████ █████████████    ██████   ████████                                     \/ / 
 / /\    ░███░░███  ░░░░░███ ░░███░░███  ███░░███░░███░░███░░███  ░░░░░███ ░░███░░███                                    / /\ 
/ /\ \   ░███ ░███   ███████  ░███ ░███ ░███ ░███ ░███ ░███ ░███   ███████  ░███ ░███                                   / /\ \
\ \/ /   ░███ ░███  ███░░███  ░███ ░███ ░███ ░███ ░███ ░███ ░███  ███░░███  ░███ ░███                                   \ \/ /
 \/ /    ████ █████░░████████ ████ █████░░███████ █████░███ █████░░████████ ████ █████                                   \/ / 
 / /\   ░░░░ ░░░░░  ░░░░░░░░ ░░░░ ░░░░░  ░░░░░███░░░░░ ░░░ ░░░░░  ░░░░░░░░ ░░░░ ░░░░░                                    / /\ 
/ /\ \                                   ███ ░███                                                                       / /\ \
\ \/ /                                  ░░██████                                                                        \ \/ /
 \/ /                                    ░░░░░░                                                                          \/ / 
 / /\      █████████                                                                                             █████   / /\ 
/ /\ \    ███░░░░░███                                                                                           ░░███   / /\ \
\ \/ /   ███     ░░░  █████ ████  ██████   █████   █████      ██████      █████ ███ █████  ██████  ████████   ███████   \ \/ /
 \/ /   ░███         ░░███ ░███  ███░░███ ███░░   ███░░      ░░░░░███    ░░███ ░███░░███  ███░░███░░███░░███ ███░░███    \/ / 
 / /\   ░███    █████ ░███ ░███ ░███████ ░░█████ ░░█████      ███████     ░███ ░███ ░███ ░███ ░███ ░███ ░░░ ░███ ░███    / /\ 
/ /\ \  ░░███  ░░███  ░███ ░███ ░███░░░   ░░░░███ ░░░░███    ███░░███     ░░███████████  ░███ ░███ ░███     ░███ ░███   / /\ \
\ \/ /   ░░█████████  ░░████████░░██████  ██████  ██████    ░░████████     ░░████░████   ░░██████  █████    ░░████████  \ \/ /
 \/ /     ░░░░░░░░░    ░░░░░░░░  ░░░░░░  ░░░░░░  ░░░░░░      ░░░░░░░░       ░░░░ ░░░░     ░░░░░░  ░░░░░      ░░░░░░░░    \/ / 
 / /\                                                                                                                    / /\ 
/ /\ \                                                                                                                  / /\ \
\ \/ /                                                                                                                  \ \/ /
 \/ /                              █████  ███           ███                                                              \/ / 
 / /\                             ░░███  ░░░           ░███                                                              / /\ 
/ /\ \    ██████  ████████      ███████  ████   ██████ ░███                                                             / /\ \
\ \/ /   ███░░███░░███░░███    ███░░███ ░░███  ███░░███░███                                                             \ \/ /
 \/ /   ░███ ░███ ░███ ░░░    ░███ ░███  ░███ ░███████ ░███                                                              \/ / 
 / /\   ░███ ░███ ░███        ░███ ░███  ░███ ░███░░░  ░░░                                                               / /\ 
/ /\ \  ░░██████  █████       ░░████████ █████░░██████  ███                                                             / /\ \
\ \/ /   ░░░░░░  ░░░░░         ░░░░░░░░ ░░░░░  ░░░░░░  ░░░                                                              \ \/ /
 \/ /                                                                                                                    \/ / 
 / /\.--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--./ /\ 
/ /\ \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \/\ \
\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /
 `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--' 
''')

print('\n Welcome to Hangman Game: Epic Word Guessing Adventure! 🎩✨')

print('''
1. You have 6 attempts to unravel the mystery word... Choose wisely! No deductions for correct guesses, lucky you!
2. Each correct guess earns you 5 points - cha-ching! 💰
3. For each wrong guess, 2 points vanish into the abyss of lost points... poof! 🌪️

Get ready to dive into the world of words and win those points like a boss! 🏆💬''')

hangman_words = [
'mystery', 'puzzle', 'jigsaw', 'riddle', 'enigma', 'clue', 'cipher', 'code', 'key', 'secret', 'paradox', 'quiz', 'conundrum', 'brainteaser', 'cryptogram', 'anagram', 'dilemma', 'perplexity', 'bewilderment', 'problem', 'challenge', 'confusion', 'maze', 'labyrinth', 'tangle', 'intrigue', 'whodunit', 'suspense', 'detective', 'investigation', 'thriller', 'espionage', 'adventure', 'quest', 'expedition', 'journey', 'voyage', 'odyssey', 'pilgrimage', 'trek', 'exploration', 'discovery', 'escape', 'fantasy', 'fiction', 'novel', 'tale', 'story', 'narrative', 'legend', 'myth', 'fable', 'saga', 'epic', 'chronicle', 'record', 'history', 'past', 'heritage', 'tradition', 'culture', 'civilization', 'society', 'community', 'population', 'humanity', 'mankind', 'species', 'race', 'lineage', 'ancestry', 'genealogy', 'evolution', 'origin', 'birth', 'creation', 'genesis', 'inauguration', 'commencement', 'beginning', 'start', 'dawn', 'sunrise', 'morning', 'daybreak', 'outset', 'onset', 'launch', 'initiation', 'foundation', 'establishment', 'institution', 'formation', 'development', 'growth', 'alchemy', 'artifact', 'beacon', 'cavern', 'decipher', 'eclipse', 'flora', 'glimmer', 'harbor', 'illusion', 'jubilee', 'kaleidoscope', 'lantern', 'mirage', 'nexus', 'oasis', 'paragon', 'quartz', 'relic', 'spectrum', 'talisman', 'utopia', 'vortex', 'wanderlust', 'xenon', 'yonder', 'zenith', 'abyss', 'barrage', 'cascade', 'delta', 'effigy', 'fjord', 'grotto', 'horizon', 'inertia', 'juncture', 'knoll', 'latitude', 'monolith', 'nebula', 'obelisk', 'pinnacle', 'quarry', 'rift', 'summit', 'terrain', 'undulate', 'vista', 'watershed', 'xeric', 'yearn', 'zephyr', 'archipelago', 'bungalow', 'canopy', 'dune', 'estuary', 'fresco', 'glacier', 'hinterland', 'isthmus', 'jovial', 'knack', 'lagoon', 'meadow', 'nomad', 'outcrop', 'prairie', 'quiver', 'ravine', 'savanna', 'tundra', 'uplift', 'volcano', 'wetland', 'xylem', 'yacht', 'zealot', 'accolade', 'bravado', 'crescendo', 'dynamo', 'echo', 'fandango', 'gusto', 'halo', 'impromptu', 'jargon', 'kudos', 'limbo', 'memento', 'nostalgia', 'opera', 'patio', 'quarto', 'rhapsody', 'sonata', 'tempo', 'unison', 'vibrato', 'waltz', 'xylophone', 'yodel', 'zest', 'abundance', 'bliss', 'charisma', 'delight', 'euphoria', 'felicity', 'grace', 'harmony', 'inspire', 'joviality', 'kindness', 'luminous', 'mirth', 'nirvana', 'optimism', 'paradise', 'quintessence', 'radiance', 'serenity', 'tranquility', 'utopia', 'vitality', 'whimsy', 'xanadu', 'youthful', 'zeal', 'affinity', 'benevolence', 'contentment', 'devotion', 'elation', 'fervor', 'gentility', 'honesty', 'integrity', 'joy', 'kinship', 'liberty', 'magnanimity', 'nobility', 'opulence', 'prosperity', 'quality', 'reverence', 'splendor', 'trust', 'unity', 'venerable', 'wisdom', 'exuberance', 'yonder', 'zestful', 'amity', 'bountiful', 'courage', 'dignity', 'earnest', 'fortitude', 'gratitude', 'humility', 'idealism', 'jubilation', 'karma', 'love', 'mercy', 'novelty', 'oracle', 'purity', 'quest', 'righteous', 'sacred', 'truth', 'unison', 'valor', 'wonder', 'exalt', 'yearning', 'zen', 'aspiration', 'blessing', 'clarity', 'divine', 'enlightenment', 'faith', 'glory', 'honor', 'innocence', 'juncture', 'kindred', 'legacy', 'miracle', 'newness', 'overture', 'promise', 'renaissance', 'sanctity', 'treasure', 'unveil', 'victory', 'wonderment', 'exquisite', 'yield', 'zenith', 'ascend', 'bloom', 'chivalry', 'dedication', 'eternity', 'fidelity', 'genesis', 'accolade', 'barricade', 'catalyst', 'dynamo', 'effervescent', 'flamboyant', 'gargantuan', 'haphazard', 'iconoclast', 'juxtapose', 'kaleidoscope', 'labyrinthine', 'maestro', 'neophyte', 'oscillate', 'palindrome', 'quintessential', 'rambunctious', 'symbiosis', 'turbulence', 'ubiquitous', 'vanguard', 'whirlwind', 'xenophile', 'yokel', 'zodiac', 'anecdote', 'buffoonery', 'capricious', 'debonair', 'eclectic', 'fiasco', 'gusto', 'hiatus', 'impromptu', 'juggernaut', 'knickknack', 'loquacious', 'maverick', 'narcissist', 'oblivion', 'panache', 'quagmire', 'raconteur', 'scintillating', 'trepidation', 'unorthodox', 'vivacious', 'wistful', 'xenogenesis', 'yin', 'zeppelin', 'aphorism', 'boisterous', 'cacophony', 'dichotomy', 'ephemeral', 'facetious', 'grandiose', 'heterogeneous', 'idiosyncrasy', 'jovial', 'kinetic', 'lucid', 'metamorphosis', 'nostalgia', 'omnipotent', 'paradox', 'quixotic', 'reminisce', 'serendipity', 'theoretical', 'unilateral', 'vortex', 'wanderlust', 'xeric', 'youthful', 'zephyr', 'altruism', 'boondoggle', 'cryptic', 'diatribe', 'eloquent', 'frivolous', 'gregarious', 'hermetic', 'innuendo', 'jubilant', 'kismet', 'liminal', 'monolith', 'nuance', 'ornate', 'philanthropy', 'quandary', 'resilient', 'stoic', 'tactile', 'undulate', 'verbose', 'wizened', 'xenon', 'yearn', 'zenith', 'ambrosia', 'bucolic', 'catharsis', 'dogma', 'exodus', 'fervent', 'aberration', 'benevolent', 'confluence', 'dexterous', 'ethereal', 'fortitude', 'gregarious', 'heuristic', 'idyllic', 'jovial', 'kinetic', 'lucid', 'mellifluous', 'nebulous', 'opulent', 'pandemonium', 'quixotic', 'redolent', 'surreptitious', 'taciturn', 'ubiquitous', 'verisimilitude', 'wanderlust', 'xenodochial', 'youthful', 'zealous', 'ameliorate', 'bucolic', 'cogent', 'deft', 'elucidate', 'fervent', 'grandeur', 'halcyon', 'immutable', 'juxtaposition', 'kismet', 'laconic', 'magnanimous', 'nescience', 'obfuscate', 'platitude', 'quell', 'reverberate', 'salubrious', 'tenacious', 'unfettered', 'venerate', 'winsome', 'xenophile', 'yoke', 'zephyr', 'alacrity', 'boon', 'convivial', 'diligent', 'empathy', 'fastidious', 'gallant', 'harbinger', 'incandescent', 'jubilant', 'knell', 'lithe', 'munificent', 'nocturnal', 'ostentatious', 'progeny', 'quaint', 'resplendent', 'stalwart', 'threnody', 'uncanny', 'vivify', 'whimsical', 'xenogenesis', 'yearn', 'zest', 'ardor', 'beguile', 'clandestine', 'dauntless', 'efficacious', 'florid', 'gossamer', 'hermitage', 'impervious', 'jocund', 'knack', 'languid', 'meticulous', 'nonchalant', 'ornamental', 'philanthropic', 'quiescent', 'rhapsodic', 'sanguine', 'temerity', 'unabashed', 'verdant', 'wistful', 'xeric', 'yare', 'zenith', 'ascertain', 'brevity', 'capitulate', 'decorum', 'effulgent', 'fruition'
]

# This code is valuable when, player wants to add there own sets of words to guess.
# b = int(input("How many words you want in your dictionary to guess later? "))

# while a<=b:
#     addition = input(f'What is word {a}, you want to be in your dictionary? ')
#     word_list.append(addition)
#     a += 1

chosen_word=random.choice(hangman_words)

for j in chosen_word:
    words += j
    words = words.lower()

for _ in words:
    display += '_'

print(display)

while end == False:
    guess = input('What is your guess? ').lower()
    if guess in display:
        print(f"You've already guessed '{guess}' letter.")
    for i in range(len(words)):
        letter = words[i]
        if guess == letter:
            display[i] = letter
            points += 5
            print(f'Points collected so far: {points}')

    if guess not in words:
        print(f"You've guessed a '{guess}' letter, that's not in the word. You lose a life and points too.")
        lives -= 1
        points -= 2
        if points < 0:
            points = 0
        if lives == 0:
            end = True
            print('You lose...')
    print(display, '\n', stages[lives])
    print('\n', f'Lives you got left... {lives}', '\n', f'Points you got so far... {points}')

    if '_' not in display:
        end = True
        print('\nYou WIN!')

print(f'Your total point pool is: {points}')
print(f"The word was: {chosen_word}")