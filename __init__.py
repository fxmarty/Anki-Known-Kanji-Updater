# -*- coding: utf-8 -*-

import sys
from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
import os
import re # pour kanji

# Update voc. cards, adding "y" in a defined field to note that the kanji for
# this card have already been studied.
def updateVocCards():
    kanji = r'[㐀-䶵一-鿋豈-頻]'
    
    # Get configuration
    vocabulary_card_type_name = gc('card_type_name')
    vocabulary_deck_name = gc('vocabulary_deck_name')
    kanji_deck_name = gc('kanji_deck_name')
    vocabulary_field_name = gc('vocabulary_field_name')
    kanji_field_name_in_kanji_deck = gc('kanji_field_name_in_kanji_deck')
    kanji_known_boolean_field_name = gc('kanji_known_boolean_field_name')
    
    for cid in mw.col.findNotes("deck:" + vocabulary_deck_name): 
        note = mw.col.getNote(cid)
        
        if note._model['name'] == card_type_name:
            for (name, value) in note.items():
                if (name == vocabulary_field_name):
                    listeKanjis = re.findall(kanji,value)
                    if len(listeKanjis) == 0: # If no kanji in the voc, pass
                        pass
                    else:
                        dejaVuTot = True
                        for k in listeKanjis:
                            dejaVu = False
                            for cidbis in mw.col.findNotes("deck:" + kanji_deck_name):
                                noteKanji = mw.col.getNote(cidbis)
                                
                                if dejaVu == True:
                                    break
                                
                                for (namebis, valuebis) in noteKanji.items():
                                    if (namebis == kanji_field_name_in_kanji_deck):
                                        if k == valuebis:
                                            dejaVu = True
                                            break
                            dejaVuTot = dejaVuTot and dejaVu
                        
                        if dejaVuTot == True:
                            for (namenew, valuenew) in note.items():
                                if (namenew == kanji_known_boolean_field_name):
                                    note[namenew] = "y"
        note.flush()
    showInfo("Done!")

def gc(arg, fail=False):
    return mw.addonManager.getConfig(__name__).get(arg, fail)

# create a new menu item
action = QAction("Update Japanese vocabulary cards according to known kanji", mw)
# set it to call updateVocCards when it's clicked
action.triggered.connect(updateVocCards)
# and add it to the tools menu
mw.form.menuTools.addAction(action)

