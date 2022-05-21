# ResistanceCalculator
<h3>Read this to use the tool correctly</h3>

Sometimes, you need a really specific resistor for your electronic circuit.
To get this resistance value, you connect two or more resistors in parallel or in series.
This way, you can get many different resistance values with very few different resistors.

My program does exactly the same thing, but much faster than you.

Before starting, you need to change the script to specify, which resistors you have laying around.
Currently, my own resistors are configured:

![image](https://user-images.githubusercontent.com/105979507/169655758-a41156b8-4018-40f6-aca1-76ab3312b5dd.png)

Now, run the script:

![image](https://user-images.githubusercontent.com/105979507/169655854-02258e9e-96cb-4ccc-b39a-7f192a1fcc89.png)

Type in the exact resistance you are looking for.
You may also use M or K for easier input. Those letters are directly replaced with 000000 or 000.
Good input:
- 12500
- 5,3
- 3M (= 3'000'000)
- 1K (= 1'000)

Bad inputs (they are valid, but most likely not intended): 
- 3K3 (= 30'003)
- 3,3K (= 3,3000 = 3,3)

The program will start testing out different resistor networks to find a fitting one for your solution.
It will show the theoretical resistance and what resistors it took to create it.
"+" means connect in series and "||" means connect in parallel.

![image](https://user-images.githubusercontent.com/105979507/169656241-6b601199-f535-4de7-8e59-8f764d30c682.png)


<h2>Important for 3 or more resistors:</h2>

![image](https://user-images.githubusercontent.com/105979507/169656346-a7693561-2357-4cb5-9bac-9956c649010e.png)

There are two ways to interpret the shown result:

![image](https://user-images.githubusercontent.com/105979507/169656980-c4e7aa57-ab2c-4777-9df4-0df08480de12.png)

The left one is correct, the right one is not.

Always read the result "from left to right":
E.g.: 2K + 1K || 5K + 2K = (((2K + 1K) || 5K) + 2K)

![image](https://user-images.githubusercontent.com/105979507/169657135-ef0b4cca-44a3-4337-8406-cca57989d4b1.png)



This tool is far from perfect (performance-wise). I believe there are many improvements to make, it suits its purpose really well in my opinion.
I wrote it because I needed 10 really specific resistances for a project.

Feel free to suggest improvements.



