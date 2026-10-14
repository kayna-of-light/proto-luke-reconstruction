# Proto-Luke read in correspondence: analysis of the whole text

**Status:** analysis only. Nothing in `data/` is changed, and nothing is reconstructed. The text is translated into its inner sense, read through as one story, and the places where that story does not run are flagged. Deciding any doubt is a later step and is not begun here.

**Text:** the printed text of PR #3 (`e5de666`, `data/proto_luke.json`), in its English, which translates the printed Greek.

## 1. The object: the text before Marcion

The witnesses attest the text read in Marcion's church. The object here is the text Marcion received. Four levels of certainty follow from that difference, and every reference in these files carries one of them.

| Mark | Level | What it covers | Status for the text before Marcion |
|---|---|---|---|
| `[4:31]` | **Certain** | Content attested for Marcion's text (`A+`) that canonical Luke also has | Both lines of transmission carry it. It stood in the text before either of them. Hard fact. |
| `[4:36 g]` | **Lower** | Grey verses: unattested inside an attested pericope (`U?`), present in canonical Luke | Canonical Luke has it; no witness speaks for Marcion's text. Neither confirmed nor excluded. |
| `[5:14 ◊]` | **Doubt** | Where Marcion's attested text differs from canonical Luke: wording (the "Marcionite readings printed" tables in `docs/audit/AUDIT_LOG.md`), order (Capernaum before Nazara; 4:27 inside 17:12–14), the opening junction 3:1 → 4:31, the two additions at 23:2 | Either form may be the earlier one. The PR #3 form is read as printed, and every reading that depends on it is marked. |
| *position* | **Unknown** | Everything not printed (`A−`, `U−`, `U?` outside attested pericopes) | Marcion's lacking a passage is not evidence that the earlier text lacked it. Unattested is not evidence either way. Nothing here is free to choose. Positions are listed at their places; their contents are not read. |

## 2. The method

The rules are those of the correspondential reading:
- **One soul.** Every person, place, time, object, number and act in the text is a state, power or movement of one soul. Nothing in the reading refers outside it.
- **The source and the three degrees.** The Father is Divine Love, the source. It goes forth through the soul and shapes it in three degrees:
  - **will**: what the soul loves;
  - **understanding**: what it sees and knows;
  - **outer form**: what it says, does and appears as.
- **The central figure.** "Jesus" is Divine Truth in outer form. The other names ("son of man", "holy one of God", "son of God", "the Anointed One", "Lord", "the Living One") describe its inner form. Who uses which name, and when, shows the inner form becoming recognised in the outer.
- **The key, not the conclusions.**
  - Use Swedenborg's key only: a thing signifies what does the same work inwardly, and the function is derived from the text or from nature.
  - Do not use his Christology, his expositions of particular verses, his science, or his schemes.
- **No prefilled structure.** Whatever structure appears comes out of the reading.

The steps are:
1. Translate, without judgement (`reading/`).
2. Read the translation through as one story (`story.md`).
3. Register the places where the inner story does not run (`register.md`).

The fourth step, deciding doubts, is in `decisions.md`, as proposals only.

## 3. Files

| File | Contents |
|---|---|
| `reading/ch01.md` … `reading/ch22.md` | Step 1. Each file contains three things: the inner sense of every printed verse of the chapter, with its certainty mark; the names given to the central figure; and the positions of unprinted passages. |
| `story.md` | Step 2. The movements the text repeats, the one-soul story in sequence, and the sequence of names. |
| `register.md` | Step 3. Gaps and breaks in the inner story. It also lists the gaps in the letter that were tested and found to hold inwardly, the tensions at doubtful wordings, and the places where the story leans on grey verses. |
| `decisions.md` | Step 4. Part A fixes the requirements, and was committed before any candidate was read. Part B tests the candidates against them. Part C summarises the proposals for the text before Marcion. These are proposals only; `data/` is unchanged. |

## 4. Correspondences relied on

Each correspondence is derived from what the element does in the text, or in nature where the text gives no definition. Elements whose function cannot be derived beyond a general sense are marked (?) and carry no weight in the register.

### Persons and powers

| Element | What it does (text) | In the soul (degree) |
|---|---|---|
| Jesus | comes, teaches, heals, is rejected, gives itself, lives | Divine Truth in outer form |
| son of man, holy one of God, son of God, son of the Most High, the son, the Anointed One, the Living One | names spoken when the text speaks of what this truth is | the inner form of the same truth, at the degree of recognition the speaker has |
| the Father, the Most High | merciful, kind to the ungrateful (6:35–36); knows what is needed (12:30); gives the kingdom (12:32) and the holy spirit (11:13); sends (9:48; 10:16) | Divine Love, the source |
| holy spirit | given by the Father to those who ask (11:13); teaches what to say (12:12); truth rejoices in it (10:21) | the living working of the source within the soul |
| kingdom of God | belongs to the poor (6:20); comes near (10:9); is "within you" (17:21); grows hidden (13:18–21) | the soul ruled from within by the source |
| Caesar, Pilate, the governor | count the years (3:1); take tribute, bear the image on the coin (20:24–25); judge from outside (23) | rule over the soul from outside, by the outer degree |
| Herod and the tetrarchs | each rules a part (3:1); Herod is perplexed (9:7), wants a sign (23:8) | the outer degree divided among partial rulers |
| daimons, unclean spirits | live in a man and speak through him as "we" (4:34); bind (13:16); are cast out | foreign occupants: what is not the soul's own and has taken up residence in it |
| Satan, Beelzebul | ruler of the daimons (11:15–18); binds (13:16) | the rule of what is foreign in the soul |
| Simon / Peter | first to leave everything (5:11); names "the Anointed One of God" (9:20); "that your faith may not fail" (22:32 g) | the soul's faith: its power to acknowledge |
| James and John | partners with Simon (5:10); with him on the mountain (9:28); want fire on the unreceptive village (9:54) | powers nearest to faith (?) individual function not derivable |
| disciples | learn, follow, eat with truth | the soul's learning and following powers |
| the twelve, emissaries, the seventy | chosen and sent with power over daimons and sickness (9:1–2; 10:1, 19) | the soul's powers sent out to every part of it |
| Judas Iscariot | one of the twelve who hands truth over for money (22:3–5, 47–48) | a power among the chosen that hands truth over for the soul's own gain |
| crowds, the people | press to hear, are amazed, are feared by the rulers (20:19), cry "crucify" (23:18, 21 g) | the soul's multitude of everyday thoughts and affections |
| Pharisees | keep fasts and tithes (18:12), clean the outside (11:39), love the best seats (11:43), justify themselves (16:15), grumble at sinners received | self-righteous keeping of the outward rule |
| scribes, lawyers, teachers of the law | interpret what is written; load burdens (11:46); take away the key of knowledge (11:52) | the soul's learned interpreting of its rule |
| chief priests, elders, council | govern worship and judgement at the centre; seek to kill (22:2 g; 20:19) | the soul's governing centre: the authority over its worship and judgement |
| Sadducees | deny the resurrection (20:27) | the part that denies any life beyond the present state |
| tax collectors | collect for the outer rule; despised; receive truth | parts in the service of the outer rule, which are open to truth |
| sinners | are called to repentance (5:32); are sought (15) | parts gone astray |
| John | messenger who prepares the way (7:27); wilderness (7:24); fasting and prayers (5:33; 11:1); "the law and the prophets were until John" (16:16) | the preparing state under the law: the soul turning in a desolate state before truth itself is present |
| Moses | "as Moses commanded" (5:14); "Moses wrote" (20:28); "Moses and the prophets" (16:29) | the law: the order the soul has received |
| Elijah, the prophets | named with Moses (9:30; 16:29); killed by the fathers (6:23; 11:47) | the prophetic voice that calls the soul back to its order |
| Abraham | "father Abraham" (16:24); the poor carried to his bosom (16:22); daughter and son of Abraham (13:16; 19:9) | the origin to which the soul's faithful parts belong (?) beyond that |
| David | ate the bread of the presence when hungry (6:3–4); calls the Anointed One "Lord" (20:42–44) | the soul's past kingship |
| angels | messengers of the source; joy before them (15:10); carry the poor (16:22) | the source's messengers within the soul |
| centurion, soldiers | officers of the foreign army; "under authority" (7:8 g) | parts in the service of the outer rule, with authority of their own |
| Samaritans, the foreigner | between Galilee and Judea (17:11); "this foreigner" (17:18) | parts outside the soul's inherited worship |
| women | named by function in each passage: anointing (7:38), providing (8:3), bleeding (8:43), bent (13:11), grinding (17:35 g), bringing spices and the news (23:55–24:10) | read passage by passage, never as a class |
| children, little ones | received without claim (18:16); "the least is the greatest" (9:48) | the soul's states that receive without claiming |
| the poor / the rich | the poor have nothing, the rich have much and store it (6:20–24; 12:16–21; 16:19–31; 18:22–23) | states that claim nothing as their own / states that hold much as their own |
| mother, brothers, father, home town | natural kin and origin (4:23; 8:20; 9:59–61; 12:53) | the soul's natural origin and inheritance |
| the sick, blind, lame, lepers, paralysed, mute, deaf, dead | cannot see, walk, move, speak, hear, live; leprosy makes unclean and separates | functions of the soul closed, unable, corrupted or without life |

### Places

| Element | What it does (text) | In the soul (degree) |
|---|---|---|
| Galilee | where truth "began" (23:5); towns, lake, fishermen | the outer degree |
| Judea, Jerusalem, temple | the centre: council, chief priests, temple, sacrifice | the centre, where the soul's worship and governance sit (will) |
| Samaria | between Galilee and Judea (17:11) | the region between the outer degree and the centre, foreign to the inherited worship |
| region of the Gerasenes | "opposite Galilee", across the water (8:26 g); pigs | a region foreign to the soul's order, reached by crossing |
| Nazara, home town | "where he had been brought up" (4:16) | the soul's inherited formation |
| Capernaum | a town of Galilee where truth first teaches (4:31) | a settled structure of the outer degree |
| town, village | settled common habitation | a settled structure of thinking |
| house | where one lives | the state of life one dwells in |
| assembly (synagogue) | where the community gathers and reads what it was taught | where the soul keeps and repeats its learned teaching (understanding) |
| mountain | high ground where truth prays (6:12; 9:28) | elevation of the soul toward the source |
| deserted place, wilderness | no settled habitation (4:42; 5:16 g) | a state empty of the soul's structures |
| lake, sea, water | holds fish; storm and roaring (8:23; 21:25) | (?) the soul's mass of knowing in the outer degree |
| boat | carries over water; truth teaches from it (5:3 g) | (?) a structure of the understanding that carries the soul over its knowing |
| roads, streets, hedgerows | outside the house, outside the town (14:21–23) | the soul's outermost, unordered parts |
| tomb | where the dead lie (8:27; 23:53) | a state where life is absent |

### Times

| Element | What it does | In the soul |
|---|---|---|
| sabbath | work stops | the soul's own activity at rest: receptivity |
| evening, night | light fades, is absent | a state closing; darkness |
| day, morning, dawn, first day of the week | light returns; something begins | a new state opening |
| "the fifteenth year of Tiberius" | time counted from the emperor | the soul's states counted by the outer rule |

### Objects and acts

| Element | What it does | In the soul |
|---|---|---|
| bread, grain, food, eating | sustains life | good that sustains the will; taking it in |
| wine | alive, fermenting, gladdening (5:37–38) | truth that is alive and active |
| wineskins, garment | hold or clothe | the forms that hold truth; the outer form a soul shows |
| fish, nets, catching | living things drawn out of the water | (?) living things gathered out of the soul's knowing |
| lamp, light | lights a house for those who come in (8:16; 11:33) | what makes the soul's state visible to itself |
| leaven | spreads hidden through the whole (12:1; 13:21) | what spreads hidden through the soul: hypocrisy or the kingdom |
| seed, soil | grows according to the ground (8:5–8) | what is received, and the soul's ground that receives it |
| tree, fruit | each tree known by its fruit (6:43–44) | what the soul is, and what comes forth from it |
| heart / mouth | "the mouth speaks out of the abundance of the heart" (6:45) | will / outer form, stated by the text itself |
| inside / outside of the cup | "did not the one who made the outside make the inside also?" (11:40) | inner / outer degree, stated by the text itself |
| hand, right hand | grips, acts | the power to act |
| feet | touch the ground | the outermost, the contact with the natural degree |
| eyes, seeing | see | understanding |
| ears, hearing | hear | receiving what is said |
| money, mammon, possessions | owned, stored, served (16:13) | what the soul holds as its own |
| fire | burns, kindles, consumes (9:54; 12:49) | (?) a kindling that divides; the specific function depends on the passage |
| cloud | covers and overshadows; a voice comes out of it (9:34–35) | a state in which the soul's sight is covered and in which it hears |
| body, bones, hands and feet (24:39) | the outer form with its structure | the outer form of truth, real and structured |
| blood | flows out and life goes with it (8:43–44); "poured out for you" (22:20) | the life of the soul |
| bread taken, blessed, broken, given (9:16; 22:19; 24:30) | the act of feeding | good given out from the source through truth |

### Numbers

Numbers are read only for what the text shows. Twelve recurs where something is complete: the twelve chosen, the twelve years of the bleeding and of the dying daughter, the twelve baskets. Few against many occurs in five loaves and five thousand. One against many occurs in one sheep against ninety-nine and one coin against ten. Every other specific value (seven, eighteen, seventy, sixty stadia, the sixth and ninth hour) is marked (?).

## 5. Conventions in the translation

- **The certainty mark comes with every verse reference** (§1).
- **Fixed terms.** "Truth" stands for Jesus, and "faith" for Peter. "The following powers" are the disciples. "The governing centre" covers the chief priests, elders and council. "The self-righteous keeping" is the Pharisees, and "the interpreting" the scribes and lawyers. "The outer rule" covers Caesar, Pilate and Herod. The table in §4 gives the derivation of each.
- **Degrees.** The degree is named where the function shows it.
- **No judgements in the translation files.** Breaks, gaps and doubts are in `register.md` only.
