Silly Story
===========

We can begin by writing a simple story and then looking for words to replace. This is a slightly edited section from the Simple English Wikipedia entry on ice cream:

  Ice cream is a frozen dessert made from cream, with added flavours and sweeteners. This mixture is quickly frozen while it is stirred, so that large ice crystals do not form. Some ice cream is made with carrageenan, extracted from seaweed, so that it is not sticky. There are many different flavours of ice cream, such as chocolate and vanilla. Ice cream often has things added to it for flavour, like chocolate chips, nuts, or fruit

You can use this passage for your game if you like, or come up with your own version. Now that we have the basic text, we can replace some of the words, such as nouns and verbs. Here’s an example.

  Ice cream is a frozen dessert made from **plural noun** ,with added flavours and sweeteners. This mixture is quickly frozen while it is **verb ending in ed** ,so that large **plural noun** do not form. Some ice cream is made with **noun** ,extracted from seaweed, so that it is not sticky. There are many different flavours of ice cream, such as **food** and **food** . Ice cream often has things added to it for flavour, like **noun**, **noun** , or **noun**.

Now let’s look at how you could use Python to create a Mad Libs–style game. The algorithm is fairly simple:

#. Ask for the user to input some words, such as plural nouns and foods
#. Assign these inputs to variables
#. Insert these variable values into the strings to complete the paragraph.

Step 1 and 2
++++++++++++
In Python, asking the user for input and assigning the value to a variable can be accomplished in a single line::

  answer = input('What is the meaning of life? ')

Step 3
++++++
You can then use this variable in a print statement using simple string concatenation::

  print('The meaning of life is ' + answer + '.')

So, to make the Mad Libs game, you can begin by asking the user for a load of words, and finish by inserting them into some strings that will be printed.

Here is the code for a complete Python program, and below that is a Trinket version for you to test out::
  
  noun_1 = input("Give me a plural noun ")
  verb = input("Give me a verb ending in ed ")
  noun_2 = input("Give me another plural noun ")
  noun_3 = input("Give me a noun ")
  adjective = input("Give me an adjective ")
  food_1 = input("Give me a type of food ")
  food_2 = input("Give me another type of food ")
  noun_4 = input("Give me a noun ")
  noun_5 = input("and another one ")
  noun_6 = input("Give me one last noun ")

  print("Ice cream is a frozen dessert made from " + noun_1 + ", with added flavours and sweeteners")
  print("This mixture is quickly frozen while it is " + verb + ", so that large " + noun_2 + " do not form.")
  print("Some ice cream is made with " + noun_3 + " extracted from seaweed, so that it is not " + adjective)
  print("There are many different flavours of ice cream, such as " + food_1 + " and " + food_2)
  print("Ice cream often has things added to it for flavour, like " + noun_4 + ", " + noun_5 + " or " + noun_6)

Prova a riprodurre questo programma in Scratch!
