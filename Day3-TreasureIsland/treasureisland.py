print("""

    ___ __ 
   (_  ( . ) )__                  '.    \   :   /    .'
     '(___(_____)      __           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|/_/__      -----____   _  _____-----
_______________''.--o/___  \_______________(_)___________
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     ___|_||_____     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..:: .lcf/
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~
   ~                  ~    ~ ~                 ~


      """)
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
# Left or right
left_or_right = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()
if left_or_right[0] == "l":
     swim_or_wait = input("After some time, you've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
     # Swim or break
     if swim_or_wait[0] == "w":
          # Wich door to enter
          which_door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
          if which_door[0] == "r":
               print("You entered a room full of snakes. Game Over.")
          
          elif which_door[0] == "y":
               print("You found the treasure! You Win!")
          elif which_door[0] == "b":
               print("The room is booby trapped. Game Over.")
     else:
          print("You got attacked by by sharks. Game Over.")
else:
     print("You fell into a hole. Game Over.")
