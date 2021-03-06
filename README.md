# **Colorado Election Analysis**

##**Overview of Project**

A Colorado Board of Elections employee, Tom, requested an election audit of the results for a U.S. congressional precinct.  

###*Purpose of Analysis*

There are three primary voting methods to determine the election results:

•	Mail-In Ballots: Hand counted at the central office

•	Punch Cards: Collected, fed into a machine for counting and then results are sent to the central office

•	Direct Recording Electronic (DRE): Computer counted with memory cards that are sent to the central office

I was tasked with generating an automated vote count report to certify the election results for the district.  Using Python to write algorithms that will assist with the confirmation and analysis of the election results, the initial report showed:

•	Total Number of Votes Cast

•	Total Votes for Each Candidate

•	The Percentage of Total Votes for Each Candidate

•	Winner of the Election Based on Popular Vote

After completing the initial audit, the commission requested additional data to finalize the election audit. The report was updated to also include:

•	Voter Turnout for Each County

•	Percentage of Total Votes for Each County 

•	County with the Highest Voter Turnout

*Note:* I will also use a Python Interpreter, Visual Studio Code, to speed up the analysis process because Python scripts will be long and need to be edited often.  Speed isn’t critical for this project, but VS Code will alert me if there are syntax errors and misspellings. It can also help with bracket-matching and code indentation.  Tom’s boss, Seth, recommended running files from the command line to be sure their output is correct. 

####**Resources**

Data Source: election_results.csv (provided by Tom)
Software: Python 3.7.6 and Visual Studio Code, 1.47

#####**Summary**

In the election analysis, I performed mathematical calculations as well as extracting non-mathematical data from the .csv file. After looking at the data set more closely, agreed with Seth and used repetition statements, such as loops, to retrieve data and complete the audit.  I also used a programming technique called Pseudo coding to make the audit easier to present to non-technical stakeholders. These items are marked by hashtags and in green font throughout the code. 

*Candidate Results*

•	Total Number of Votes Cast: 369,711

•	Total Votes for Each Candidate

  -	Charles Casper Stockham: 272,892

  -	Diana DeGette: 272,892

  -	Raymon Anthony Doane: 11,606

•	The Percentage of Total Votes for Each Candidate

  -	Charles Casper Stockham: 23%
  
  -	Diana DeGette: 73.8%
  
  -	Raymon Anthony Doane: 3.1%
  
•	**Winner of the Election Based on Popular Vote: Diana DeGette**

![Election Results](https://github.com/FeliciaGanthier/Election_Analysis/blob/master/Resources/Election%20Results.png)

*County Results*

•	Voter Turnout by County

-	Arapahoe: 24,802

-	Denver: 306,056

-	Jefferson: 38,856

•	Percentage of Total Votes by County

-	Arapahoe: 6.7%

-	Denver: 82.8%

-	Jefferson: 10.5%

•	**County with Highest Turnout: Denver**

![Complete Results](https://github.com/FeliciaGanthier/Election_Analysis/blob/master/Complete%20Results.png)




