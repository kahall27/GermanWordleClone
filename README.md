# German Wordle Clone
<h2> About this Project </h2>
This project is written in Python and uses the [pygame library](https://www.pygame.org/news) to create a user interface for the game. Additionally, I downloaded the raw text file from the [german-wordlist repository](https://github.com/enz/german-wordlist) for a list of German word that I then parsed to create a new text file of only five leader words. 
<h2>How to Play</h2>
The game follows the simple pattern of the popular word game, Wordle. The goal is to guess a five letter word.
<ol>
<li>A player guesses any five letter word.</li>
<li>The letters are highlighted in different colors to signify success or failure in guessing.
<ul>
<li>Any word that <strong>is not</strong> a valid German five letter word will appear red and not be accepted. The player must guess again.</li>
<li>If it is valid, any letter in the goal word that is in the <strong>correct</strong> place will be green.</li>
<li> If valid, any letter that is in the goal word but in the <strong>incorrect</strong> place will be yellow.</li>
<li>If it is not in the goal word at all, no color will change</li>
</ul>
</li>
<li>The player continues to guess until they find the correct word, or they have guessed six valid five letter German words. 
</ol>