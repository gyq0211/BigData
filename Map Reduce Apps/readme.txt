Write a Hadoop program to generate a word co-occurrence matrix between two given documents as outlined in Chapter 3 of Lin and Dyer's book, while removing punctuation and capitalization. The pairs algorithm is enough and if you emit 'a|b' as the key from your mapper, you can use the default aggregate reducer [3 points]. For initial testing, you can use the following two sentences to validate your results:

How much wood would a woodchuck chuck if a woodchuck could chuck wood?
He would chuck, he would, as much as he could, and chuck as much as a woodchuck would If a woodchuck could chuck wood.
These sentences were deliberately chosen to be small enough (and similar enough) such that you can  manually examine the results and confirm that they make sense.

You may run your code in Hadoop or on a machine using the pipeline construct, sort of like...

echo {sentence1, sentence2} | mapper | sort | reducer > {co-occurrence.matrix}
