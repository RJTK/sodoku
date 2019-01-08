I was for some reason inspired to write a Sodoku solver.  My solver uses BFS with some breadth limiting, constraint propogation, random exploration order, random restarts, and some seemingly-reasonable heuristics.  It seems to be able to solve the hardest puzzles in a book I have lying around in at most a couple seconds.

There are some puzzles that are designed to be extremely difficult, which take quite a bit longer.  For example, here is "AI Escargot", which is claimed by http://aisudoku.com/ to be the most difficult Sudoku in existence.

In [891]: print(s)
||=|=|=||=|=|=||=|=|=||
||1| | || | |7|| |9| ||
|| |3| || |2| || | |8||
|| | |9||6| | ||5| | ||
||=|=|=||=|=|=||=|=|=||
|| | |5||3| | ||9| | ||
|| |1| || |8| || | |2||
||6| | || | |4|| | | ||
||=|=|=||=|=|=||=|=|=||
||3| | || | | || |1| ||
|| |4|1|| | | || | |7||
|| | |7|| | | ||3| | ||
||=|=|=||=|=|=||=|=|=||

In [892]: print(solve(s))
||=|=|=||=|=|=||=|=|=||
||1|6|2||8|5|7||4|9|3||
||5|3|4||1|2|9||6|7|8||
||7|8|9||6|4|3||5|2|1||
||=|=|=||=|=|=||=|=|=||
||4|7|5||3|1|2||9|8|6||
||9|1|3||5|8|6||7|4|2||
||6|2|8||7|9|4||1|3|5||
||=|=|=||=|=|=||=|=|=||
||3|5|6||4|7|8||2|1|9||
||2|4|1||9|3|5||8|6|7||
||8|9|7||2|6|1||3|5|4||
||=|=|=||=|=|=||=|=|=||

For my solver however, a puzzle on Wikipedia having 17 clues (the minimum possible) turned out to take the longest:

In [962]: print(s)
||=|=|=||=|=|=||=|=|=||
|| | | || | | || | | ||
|| | | || | |3|| |8|5||
|| | |1|| |2| || | | ||
||=|=|=||=|=|=||=|=|=||
|| | | ||5| |7|| | | ||
|| | |4|| | | ||1| | ||
|| |9| || | | || | | ||
||=|=|=||=|=|=||=|=|=||
||5| | || | | || |7|3||
|| | |2|| |1| || | | ||
|| | | || |4| || | |9||
||=|=|=||=|=|=||=|=|=||


In [963]: print(solve(s))
||=|=|=||=|=|=||=|=|=||
||9|8|7||6|5|4||3|2|1||
||2|4|6||1|7|3||9|8|5||
||3|5|1||9|2|8||7|4|6||
||=|=|=||=|=|=||=|=|=||
||1|2|8||5|3|7||6|9|4||
||6|3|4||8|9|2||1|5|7||
||7|9|5||4|6|1||8|3|2||
||=|=|=||=|=|=||=|=|=||
||5|1|9||2|8|6||4|7|3||
||4|7|2||3|1|9||5|6|8||
||8|6|3||7|4|5||2|1|9||
||=|=|=||=|=|=||=|=|=||
