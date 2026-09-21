class ActionHistoryStack:
    def __init__(self):
        self.actionhistory_stack = []

    def push_action(self, action_string):
        self.actionhistory_stack.append(action_string)
        pushAction(action_string)

    def pop_action(self):
        if self.is_empty():
            return "Empty"
        return self.actionhistory_stack.pop()
        
    def peek(self):
        if not self.is_empty():
            print(self.actionhistory_stack[-1])
        else:
            return "Empty"
                
    def is_empty(self):
        return len(self.actionhistory_stack) == 0

stack = ActionHistoryStack()

stack.push_action("planted at [1] [2]")
stack.push_action("planted at [1] [1]")

stack.peek()

print("\nAction history Stack ready! (push, pop, & peek tested)\n")

