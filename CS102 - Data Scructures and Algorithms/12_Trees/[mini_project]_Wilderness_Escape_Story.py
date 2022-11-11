class TreeNode:
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []
  
  def add_child(self, node):
    self.choices.append(node)  

  def traverse(self):
      story_node = self
      print(story_node.story_piece)
      while len(story_node.choices) > 0:
        choice = input( "Enter 1 or 2 to continue the story")
        if choice not in ['1', '2']:
          print("Invalid choice. Try again.")
        else:
          chosen_index = int(choice)
          chosen_index -= 1
          chosen_child = story_node.choices[chosen_index]
          print(chosen_child.story_piece)
          story_node = chosen_child
    




story_root = TreeNode(
  """
  You are in a forest clearing. There is a path to the left.
  A bear emerges from the trees and roars!
  Do you:
  1) Roar back!
  2) Run to the left...
  """
)

user_choice = input("What is your name? ")
print(user_choice)
######
# VARIABLES FOR TREE
######
choice_a = TreeNode(
"""
The bear is startled and runs away.
Do you:
1) Shout 'Sorry bear!'
2) Yell 
'Horray!'
"""
)

choice_b = TreeNode(
  """
  You come across a clearing full of flowers.
  The bear follows you and asks 'what gives'?
  Do you:
  1) Gasp 'A talking bear!'
  2) Explain the the bear scared you.
  """
)

story_root.add_child(choice_a)
story_root.add_child(choice_b)

choice_a_1 = TreeNode(
 """ 
 The bear returns and tells you it's been a rough week. After making peace with a talking bear, he shows you the way out of the forest.

 YOU HAVE ESCAPED THE WILDERNESS.
 """ 
)

choice_a_2 = TreeNode(
  """
  The bear returns and tells you that bullying is not okay before leaving you alone in the wilderness.

  YOU REMAIN LOST.
  """
)

choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)

choice_b_1 = TreeNode(
  """
  The bear is amused. After smelling the flowers, it turns around and leaves you alone.

  YOU REMAIN LOST.
  """
)

choice_b_2 = TreeNode(
  """ 
  THe bear understands and apologieses for startling you. Your new friend shows you a path leading out of the forest.

  YOU HAVE ESCAPED THE WILDERNESS.
  """
)

choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

######
# TESTING AREA
######


print(story_root.story_piece)
story_root.traverse()######
# TREENODE CLASS
######
print("Once upon a time...")

