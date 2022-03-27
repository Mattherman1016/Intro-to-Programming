## chess Board Markdown
- I started by looking at all of the examples that were given in class for different programs.
- I couldn't find anything that resembled what i wanted so im gonna use my knowledge of stuff we learned already.
- I know that i have to define the variable at first and then print the variable.
- var chess = "# # # #"
- then i printed it to make sure console.log(chess);
- It printed!
- now i have to try to make 8 lines of this
- i have to make another variable about the size in the same environment
- var size = 8
- Trying var chess + var size
- syntax error: unexpected token +
- Tried in ()
- Syntax Error unexpected token (
- tried using a for statement pertaining to the X axes
- for (var x = 0) - trying to say for variable x, dont change anything
- Syntax error Unexpected token ')'
- Tried with == instead
- another syntax Error
- I am really at a loss as to what i am supposed to do.
- Biting the bullet and looking it up.

https://teamtreehouse.com/community/create-a-chess-board-with-hashtags

var size = 8;

var board = "";

for (var y = 0; y < size; y++) {
  for (var x = 0; x < size; x++) {
    if ((x + y) % 2 == 0)
      board += " ";
    else
      board += "#";
  }
  board += "\n";
}
console.log(board);

- At least even if i cant do it, i can try to understand why the solution is this.
- Starts with defining the size. I was right with that!
- Then defines the next variable as board. This is what is to be printed at the end. The "" was used when printing out the pyramid.
- Defines the X and Y variables - which for the record i knew had to be done. I just wasnt sure how.
- I dont understand y and x ++. What did that do?
- I forgot what % was and i looked it up - it is the remainder operator which obtains a remainder between two Numbers
- im honestly very confused. Ive been at this for almost an hour now and i just wanna cry
