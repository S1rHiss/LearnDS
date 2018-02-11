from textblob import TextBlob
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "In the beginning God created the heavens and the earth. And the earth was waste and void; and darkness was upon the face of the deep: and the Spirit of God moved upon the face of the waters.   And God said, Let there be light: and there was light.   And God saw the light, that it was good: and God divided the light from the darkness.   And God called the light Day, and the darkness he called Night. And there was evening and there was morning, one day.   And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters.   And God made the firmament, and divided the waters which were under the firmament from the waters which were above the firmament: and it was so.   And God called the firmament Heaven. And there was evening and there was morning, a second day.   And God said, Let the waters under the heavens be gathered together unto one place, and let the dry land appear: and it was so.   And God called the dry land Earth; and the gathering together of the waters called he Seas: and God saw that it was good.   And God said, Let the earth put forth grass, herbs yielding seed, and fruit-trees bearing fruit after their kind, wherein is the seed thereof, upon the earth: and it was so.   And the earth brought forth grass, herbs yielding seed after their kind, and trees bearing fruit, wherein is the seed thereof, after their kind: and God saw that it was good.   And there was evening and there was morning, a third day.   And God said, Let there be lights in the firmament of heaven to divide the day from the night; and let them be for signs, and for seasons, and for days and years:   and let them be for lights in the firmament of heaven to give light upon the earth: and it was so.   And God made the two great lights; the greater light to rule the day, and the lesser light to rule the night: he made the stars also.   And God set them in the firmament of heaven to give light upon the earth,   and to rule over the day and over the night, and to divide the light from the darkness: and God saw that it was good.   And there was evening and there was morning, a fourth day.   And God said, Let the waters swarm with swarms of living creatures, and let birds fly above the earth in the open firmament of heaven.   And God created the great sea-monsters, and every living creature that moveth, wherewith the waters swarmed, after their kind, and every winged bird after its kind: and God saw that it was good.   And God blessed them, saying, Be fruitful, and multiply, and fill the waters in the seas, and let birds multiply on the earth.   And there was evening and there was morning, a fifth day.   And God said, Let the earth bring forth living creatures after their kind, cattle, and creeping things, and beasts of the earth after their kind: and it was so.   And God made the beasts of the earth after their kind, and the cattle after their kind, and everything that creepeth upon the ground after its kind: and God saw that it was good.   And God said, Let us make man in our image, after our likeness: and let them have dominion over the fish of the sea, and over the birds of the heavens, and over the cattle, and over all the earth, and over every creeping thing that creepeth upon the earth.   And God created man in his own image, in the image of God created he him; male and female created he them.   And God blessed them: and God said unto them, Be fruitful, and multiply, and replenish the earth, and subdue it; and have dominion over the fish of the sea, and over the birds of the heavens, and over every living thing that moveth upon the earth.   And God said, Behold, I have given you every herb yielding seed, which is upon the face of all the earth, and every tree, in which is the fruit of a tree yielding seed; to you it shall be for food:   and to every beast of the earth, and to every bird of the heavens, and to everything that creepeth upon the earth, wherein there is life, I have given every green herb for food: and it was so.   And God saw everything that he had made, and, behold, it was very good. And there was evening and there was morning, the sixth day.  Top of page.  Genesis    And the heavens and the earth were finished, and all the host of them.   And on the seventh day God finished his work which he had made; and he rested on the seventh day from all his work which he had made.   And God blessed the seventh day, and hallowed it; because that in it he rested from all his work which God had created and made.   These are the generations of the heavens and of the earth when they were created, in the day that Jehovah God made earth and heaven.   And no plant of the field was yet in the earth, and no herb of the field had yet sprung up; for Jehovah God had not caused it to rain upon the earth: and there was not a man to till the ground;   but there went up a mist from the earth, and watered the whole face of the ground.   And Jehovah God formed man of the dust of the ground, and breathed into his nostrils the breath of life; and man became a living soul.   And Jehovah God planted a garden eastward, in Eden; and there he put the man whom he had formed.   And out of the ground made Jehovah God to grow every tree that is pleasant to the sight, and good for food; the tree of life also in the midst of the garden, and the tree of the knowledge of good and evil.   And a river went out of Eden to water the garden; and from thence it was parted, and became four heads.   The name of the first is Pishon: that is it which compasseth the whole land of Havilah, where there is gold;   and the gold of that land is good: there is bdellium and the onyx stone.   And the name of the second river is Gihon: the same is it that compasseth the whole land of Cush.   And the name of the third river is Hiddekel: that is it which goeth in front of Assyria. And the fourth river is the Euphrates.   And Jehovah God took the man, and put him into the garden of Eden to dress it and to keep it.   And Jehovah God commanded the man, saying, Of every tree of the garden thou mayest freely eat:   but of the tree of the knowledge of good and evil, thou shalt not eat of it: for in the day that thou eatest thereof thou shalt surely die.   And Jehovah God said, It is not good that the man should be alone; I will make him a help meet for him.   And out of the ground Jehovah God formed every beast of the field, and every bird of the heavens; and brought them unto the man to see what he would call them: and whatsoever the man called every living creature, that was the name thereof."

bibleBlob = TextBlob(text)

print(bibleBlob.tags)
print(bibleBlob.words)
print(bibleBlob.sentiment.polarity)