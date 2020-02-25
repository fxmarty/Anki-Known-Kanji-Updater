# Anki Known Kanji Updater

An add-on for Anki to facilitate the study of Japanese vocabulary cards, displaying furigana for the unknown kanji, but hiding them for the known ones

## Why this add-on

Many people learning Japanese use Anki software to learn new vocabulary, classically with "both ways" notes:

- Front: Native language, Back: Japanese
- Front: Japanese, Back: Native language

This add-on is useful to improve the "Japanese to native language" cards.

Say you are learning kanji too and know some of them. You would want to see the furigana if you don't know the kanji of the vocabulary word already, but display the vocabulary word only in kanji if you know the individual kanji already. This add-on address this problem.

## Requirements

This add-on is built for the following configuration for studying Japanese with Anki:

- One Kanji deck to learn Kanji, basically with one field countaining only one kanji to learn and an other field with the meaning.
- One vocabulary deck with vocabulary cards with furigana, e.g. generated with the [Furigana Creator](https://github.com/fxmarty/Anki-Furigana-Creator) add-on.

This add-on will work ONLY with this configuration.

## Getting Started

Clone the repository and add it to your Anki 2.1 addons folder for fast use.

In your vocabulary card type, add a field for writing if the kanji in the vocabulary word is known or not. You could call this field "kanjiKnown" for example, but this is changeable in the configuration. This field will be written in if the kanjis in the vocabulary word are known.

Whether you know already a kanji or not will be determined according to its presence or absence in the kanji deck.

Update the configuration as follow:

- vocabulary_card_type_name = The note type name of your vocabulary notes.
- vocabulary_deck_name = The name of your vocabulary deck.
- kanji_deck_name = The name of your kanji name.
- vocabulary_field_name = The name of the vocabulary field in Japanese.
- kanji_field_name_in_kanji_deck = The name of the kanji field in your kanji deck.
- kanji_known_boolean_field_name = The name of the previously created field to indicate if a kanji is known or not.

Now, you need to update your "Japanese to native language" card with [conditional replacement](https://apps.ankiweb.net/docs/manual.html#conditional-replacement) to display the furigana only when the "knownKanji" field is non-emplty.

For example, my front side for "Japanese to native language" card looks like this:

```
 {{^knownKanji}}{{furigana:Kana}}{{/knownKanji}}
 {{#knownKanji}}{{kanji:Kana}}{{/knownKanji}}
```

Now, you can launch this add-on from the "Tools" menu to update the "knownKanji" field whenever you want, depending on the kanji you added to your kanji deck!

## License

This project is licensed under the GNU GPL v3.0 License - see the [LICENSE.md](LICENSE.md) file for details.
