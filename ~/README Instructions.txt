Instructions

Problem Outline

The directors of Leaf inc are suspicious that someone employed by their company is leaking information and code to a competitor, Berry Ltd. ‘CodeAgent7’ has been hired to Leaf Inc.’s legal team to forensically collect all of their internal email data and analyse it for possible information relating to the case. The management team has identified 5 possible employees who may be involved. We have collected the mailboxes of these employees and have extracted the textual content of these emails. The aim of this project is to help identify which documents may be relevant to Leaf Inc.’s case by identifying the key people, companies, and dates from the data.

Coding Tasks

Please read all instructions before beginning the asks.

Write a program that takes folders of text files named after Control Numbers, representing the extracted text of emails, and CSV file as input, and outputs the following information:

For each email, output:
	
	+ a list of all the email domain involved in that e-mail
	+ the word count of that email
	+ the Primary Date field (1)

For each email, work out whether it contains
	+ phone numbers (2)
	+ more that one email in a thread
	+ URL’s
	+ any of the following potentially relevant keywords/phrases:
		- “not to be discussed”
		-“unfortunately”
		-“don’t tell”
		-“secretly”

	+ any of the following potentially irrelevant keywords/phrases:
		-“wedding”
		-“cat”
		-“photographer”
		-“internship”

Output a list of 50 potentially relevant Control Numbers, that the lawyers should look at first. 


NB. 
(1) The Primary Date field is created by coalescing the Date Sent, Date Received, Date Last Modified, and Date Created fields, in that order. i.e. If the Date Sent field is not null, the Primary Date field is the Date Sent Field. If Date Sent is null, and Date Received is populated, the Primary Date field is set to the Date Received value, and so on. 

(2) Phone numbers will be in the format ‘(xxx) xxx xxxx’, ‘xxx-xxxx-xxxx’, or ‘xxx xxxx’