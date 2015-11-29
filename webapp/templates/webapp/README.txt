INSTRUCTION AND SAMPLE INPUT FOR THIS WEBSITE

DESCRIPTION:
This is the web front end for MPCS53001 Final Project. It is build using Django.Source code: https://github.com/zhushigang/dbFront

Functions (8 in total):
1. On /webapp/index
Click the first link to view the available Champions that can be played in the game. 

2. On /webapp/championList
Click any Champion names to view the title of this champion

3. On /webapp/index
Click the second link to view the most played Champion

4. On /webapp/index
In the text box, type a Summoner's username to search for a specific summoner.
Example: "Adrian Ma". This will return a summoner info page. 

5. On /webapp/index (the summoner info page)
Click the first link to show the matches of this summoner

6. On /webapp/summoner
Click the second link to show the Team that contains this summoner

7. On /webapp/summoner
Click the third link to show the friend list of this summoner

8. After clicking the second link on /webapp/summoner, it will return a page /webapp/getTeamByMember/?id=xxxxxxx
Click the team name on this page will display the members of this team. 

The results returned by the functions aboves are all dynamically generated through sql executions and displayed using HTML templates. 
