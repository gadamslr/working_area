compSciKeyWords = { 'Operator' : 'Something that tells python what to do with numbers, for example: an addition',
                    'Integer' : 'A whole number, for example: 0 or 1 or 25',
                    'Float' : 'A value with a decimal point, like 1.5 or 9.0',
                    'Value' : 'A value can be anything, like a number of string',
                    'Expression' : 'An expression is made up of values and operators, like 2 + 2',
                    'SyntaxError' : 'Python does not understand a part of the code',
                    'Variable' : 'A value stored as something, for example: Wall = 4, wall is the variable and 4 is the value',
                    'Assignment' : 'The act of storing a value inside a variable',
                    'Statement' : 'Instructions that do not evaluate to any value',
                    'String' : 'One or multiple amounts of any keyboard characters',
                    'Comment' : 'An instruction that starts with #, it is not part of the actual code',
                    'Function' : 'A function is multiple instructions that execute when the function is called'}

                    
                    
var = 1
while var == 1 :

    searchWord = input("Please enter a word to search for in the dictionary:")

    try:
         print("{0} definition: {1}".format(searchWord, compSciKeyWords[searchWord]))
    except KeyError:
        print("Word not found, please try again!!")
