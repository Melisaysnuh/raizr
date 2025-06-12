from wiktionaryparser import WiktionaryParser
import spacy
from pyglottolog import Glottolog
glottolog = Glottolog('../glottolog', cache=True)
langs = glottolog.languoids()






parser = WiktionaryParser()


def get_word(word):
    fetch_word = parser.fetch(word)
    etymology = fetch_word[0]['etymology']
    return etymology

# English pipelines include a rule-based lemmatizer
nlp = spacy.load("en_core_web_sm")

# step 1. fetch
# and parse etymology
#todo step 2. split etymology by origins and comparisons using
# todo step 3. split each etymology into sequences
# logic to create word object
def parse_ety(word, languages):
    raw_ety = get_word(word)
    print(f"raw etymology is...{raw_ety}")
    sentence_list = [s.strip() for s in raw_ety.split(',') if s.strip()]

    #breaking each piece of the etymology down here
    i = 1
    for s in sentence_list:
        print(f"sentence {i} is {s}")
        i = i + 1

    for sent in sentence_list:
        parsed = nlp(sent)
        print(f"parsed is {parsed}")
        entities = parsed.ents
        if not entities:
            print("⚠️  No entities found.\n")
            continue
        query = entities[0].text
        matches = []
        for l in languages:
            if query.lower() in l.name.lower():
                matches.append(l);
        for m in matches:
            print(f"lang is {m}. /n {m.name} /n {m.latitude } /n {m.longitude} {m.endangerment} /n {m.family} /n {m.parent}")







parse_ety("hell", langs)

    # *EXAMPLE - ORANGE
    #Inherited from
    #Middle middle ADJ JJ amod Xxxxx True False
    #English English PROPN NNP compound Xxxxx True False
    # Middle English doc.ents
    # orenge, orange,
    # from Old French pome orenge (“fruit orange”),
   # Old Old PROPN NNP compound Xxx True False
    # French French PROPN NNP amod Xxxxx True False
    # influenced by the place name Orange (which is from Gaulish and unrelated to the word for the fruit and color) and by Old Occitan auranja and calqued from Old Italian melarancio, melarancia, compound of mela (“apple”) and un'arancia (“an orange”),
    # from Arabic نَارَنْج (nāranj), from Early Classical Persian نَارَنْگْ (nārang),
    # from Sanskrit नारङ्ग (nāraṅga, “orange tree”), ultimately from Dravidian.
    # Compare Tamil நாரங்காய் (nāraṅkāy), compound of நாரம் (nāram, “water”) and காய் (kāy, “fruit”);
    # also Telugu నారంగము, నారింజ (nāraṅgamu, nāriñja), Malayalam നാരങ്ങ (nāraṅṅa), Kannada ನಾರಂಗಿ (nāraṅgi)).

    #Originally borrowed as the surname (derived from the place name) in the 13th century, before the sense of the fruit was imported in the late 14th century and the color in 1510. In the color sense, largely displaced ġeolurēad, whence yellow-red.

    #* EXAMPLE - PHLEGM
    #From Middle English flewme, fleume, fleme,
    # from Old French fleume, Middle French flemme (French flegme),
    # and their source, Latin phlegma, from Ancient Greek φλέγμα (phlégma, “flame; inflammation; clammy humor in the body”),
    # from φλέγειν (phlégein, “to burn”).
    # Compare phlox, flagrant, flame, bleak (adjective), fulminate.
    # Spelling later altered to resemble the word's Latin and Greek roots.The regularly developed form /fliːm/ has been displaced by a pronunciation /flɛm/ of uncertain provenance.
    # It may be inherited, though some kind of learned or spelling pronunciation or influence from phlegmatic is also conceivable.
