# https://www.yotpo.com/sms-analyzer/

import emoji
from better_profanity import profanity
from spellchecker import SpellChecker

spell = SpellChecker()
#sms = "{SiteName}: Hi {FirstName}👋, you left {SiteName} without your purchase! Grab it now at 10% off, before items sell out: {AbandonedCheckoutUrl}. Reply STOP to opt-out"

def find_all(s, c):
    idx = s.find(c)
    while idx != -1:
        yield idx
        idx = s.find(c, idx + 1)

def word_count(sms):
    if len( sms.split() ) in range(20,30):
        return 1 
    return 0

def character_count(sms):
    print(len(sms))
    if (len(sms)>150) & (len(sms)<255):
        return 1 
    return 0

def link(sms):
    if ("url" in sms.lower()) or ("link" in sms.lower()):
        return 1 
    return 0

def active_language(sms):
    for char in sms.lower().split():
        if char in ("is", "was", "were", "are", "by"):
            return 0
    return 1

def promotion(sms):
    if ("%" in sms.lower()):
        return 1 
    return 0

def sense_of_urgency(sms):
    if ("now" in sms.lower().split()) or ("today" in sms.lower().split()):
        return 1 
    return 0

def personalization(sms):
    if (("{" in sms.lower()) & ("}" in sms.lower())):
        return 1 
    return 0

def emojis_count(sms):
    emojies = ''.join(c for c in sms if c in emoji.UNICODE_EMOJI['en'])
    if len(emojies) > 0 : return 1
    return 0

def spell_check(sms):
    misspelled = spell.unknown("".join(u for u in sms if u not in ("?", ".", ",", ";", ":", "!", "%")).replace('-', ' ').split())
    for word in misspelled :
        if "{" not in word:
            return 0
    return 1

def capitalization_style(sms):
    print(sms[0])
    if sms[0].upper() != sms[0]:
        return 0
    count = 0
    tot = 0
    for position in find_all(sms,"."):
        tot += 1
        if sms[position+2] == sms[position+2].upper():
            count += 1
    if count == tot :
        return 1
    return 0

def bad_words(sms):
    censored = profanity.censor(sms)
    if (censored.lower() == sms.lower()):
        return 1
    return 0

def rules_and_requlations(sms):
    for char in sms.lower().split():
        if char in ("if", "before", "after", "then"):
            return 1
    return 0

def opt_out(sms):
    if (("opt" in sms.lower()) & ("out" in sms.lower())):
        return 1 
    return 0

def checker_logic(sms):
    total = word_count(sms) + character_count(sms) + link(sms) + active_language(sms) + promotion(sms) + sense_of_urgency(sms) + personalization(sms) + emojis_count(sms) + spell_check(sms) + capitalization_style(sms) + bad_words(sms) + rules_and_requlations(sms) + opt_out(sms)
    
    result = {"Score": 100*total/13, "details": {"word_count": word_count(sms), "character_count":character_count(sms), "link":link(sms),"promotion":promotion(sms), "active_language":active_language(sms), "sense_of_urgency":sense_of_urgency(sms), "personalization":personalization(sms),"emojis_count":emojis_count(sms),"spell_check":spell_check(sms),"capitalization_style":capitalization_style(sms), "bad_words":bad_words(sms),"rules_and_requlations":rules_and_requlations(sms),"opt_out":opt_out(sms)}}
    
    return result
