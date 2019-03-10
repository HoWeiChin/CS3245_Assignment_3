This is the README file for A0000000X-A0155657U's submission

== Python Version ==

I'm (We're) using Python Version <3.6.6> for
this assignment.

== General Notes about this assignment ==

Give an overview of your program, describe the important algorithms/steps 
in your program, and discuss your experiments in general.  A few paragraphs 
are usually sufficient.

index.py:
1.load training data in a sorted manner.
2.for each line of a document, do:
	1.skip over number tokens.
	2.skip over punctuation tokens.
	3.skip over stopword tokens.
	4.take in only word tokens, remove any punctuation in word tokens. 
	  for eg: don't becomes dont
		  dec/mar becomes decmar


== Files included with this submission ==

List the files in your submission here and provide a short 1 line
description of each file.  Make sure your submission's files are named
and formatted correctly.

1.Codes:
index.py

2.Outputs:
dictionary.txt
postings.txt
postings_humanreadble.txt [to show the posting lists as a list in string form, instead of a binary data]


== Statement of individual work ==

Please initial one of the following statements.

[tick] We, A0000000X-A0155657U, certify that I have followed the CS 3245 Information
Retrieval class guidelines for homework assignments.  In particular, I
expressly vow that I have followed the Facebook rule in discussing
with others in doing the assignment and did not take notes (digital or
printed) from the discussions.  

[ ] I, A0000000X, did not follow the class rules regarding homework
assignment, because of the following reason:

<Please fill in>

I suggest that I should be graded as follows:

<Please fill in>

== References ==

<Please list any websites and/or people you consulted with for this
assignment and state their role>

Wikipedia-for Shunting Yard
Google-for Python syntax

