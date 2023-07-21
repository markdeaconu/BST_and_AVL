class bst():
    '''
    The bst class simply keeps track of the head of the binary search tree, and helps initiate many recursive functions 
    stored from within the node class.
    '''
    def __init__(self, head):
        self.head = head
        self.total_height = 0
    def insert(self, newval):
        self.head.insert_helper(newval)
    def delete(self, delval):
        if self.head.value == delval:
            new_head = self.head.left
            bottom_left = new_head
            temp_right = self.head.right 
            while bottom_left.left != None:
                bottom_left = bottom_left.left
                    
            bottom_left.right = temp_right
            self.head = new_head


        else:    
            self.head.delete_helper(delval)
    
    def update_height(self, height_added):
        self.total_height += height_added

    def get_height(self):
        self.total_height = 0
        self.head.height_helper(1, self)
        final_height = self.total_height
        self.total_height = 0 
        return(final_height)
    
    def save(self):
        return(str(self.head.save_helper()))
    def restore(self, save_string):
        list_conversion = eval(save_string)
        self.head = node(list_conversion[0])
        self.restore_helper(self.head, list_conversion)

    def restore_helper(self, top, data_list):

        '''
        Reversed the process of the save function. Converts the given string into a nested list, and builds a full bst out 
        of the list data
        '''
        if data_list[0]!= None:
            top.value = data_list[0]
            if data_list[1]!=None:
                top.left = node(data_list[1][1])
                self.restore_helper(top.left, data_list[1])
            if data_list[2]!= None:
                top.right = node(data_list[2][1])

                self.restore_helper(top.right, data_list[2])



            


        


class node():

    '''
    Nodes to be stored in a binary search tree. Each has a value, as well as pointers to it's left and right subchildren.
    '''
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def height_helper(self, height, bst):
        '''
        Recursively traverses through the bst and adds it's own height to the height attribute of the bst 
        '''
        bst.update_height(height)
        if self.left != None:
            self.left.height_helper(height+1, bst)
        if self.right!= None:
            self.right.height_helper(height+1, bst)


    def insert_helper(self, newval):
        '''
        Traverses recursively down the tree, taking left and right turns depending on the values
        of those specific nodes in relation to the desired inserted value. This is done until a suitible place is found,
        and the newly created node is connected as a child of one of the previously existing ones.
        '''
        if newval>=self.value:
            try:
                if newval < self.right.value or self.right == None:
                    temp_right = self.right
                    self.right = node(newval, None, temp_right)
                else:
                    return(self.right.insert_helper(newval))

            except:
                temp_right = self.right
                self.right = node(newval, None, temp_right)

                
        if newval < self.value:
            try:

                if newval >= self.left.value or self.left == None:
                    temp_left = self.left
                    self.left = node(newval, temp_left, None)
                else:
                    return(self.left.insert_helper(newval))
            except:
                temp_left = self.left
                self.left = node(newval, temp_left, None)
            
    def delete_helper(self, delval):
        '''
        Recursively traverses through the bst, when the given value is found, the function effectively deletes it by
        connecting one of the children of the node to it's parent, and then connects it's other child to the bottom left of the first
        on the right hand side.
        '''
        if self.left != None: 
            if self.left.value == delval:
                if self.left.left == None and self.left.right == None:
                    self.left = None
                else:
                    temp_left = self.left.left
                    temp_right = self.left.right
                    self.left = temp_left
                    bottom_left = self.left
                    while bottom_left.left != None:
                        bottom_left = bottom_left.left
                    
                    bottom_left.right = temp_right
                
                return None
            
            self.left.delete_helper(delval)
        if self.right!= None:
            if self.right.value == delval:
                if self.right.left == None and self.right.right == None:
                    self.right = None
                else:
                    temp_left = self.right.left
                    temp_right = self.right.right
                    self.left = temp_left
                    bottom_left = self.left
                    while bottom_left.left != None:
                        bottom_left = bottom_left.left
                    
                    bottom_left.right = temp_right
                
                return None

            self.right.delete_helper(delval)
        return None
    
    def save_helper(self):
        '''
        Effectively stores the information of the bst into a nested list, this is then wrapped into a string.
        '''
        final_list = [self.value]

        if self.left != None:
            final_list.append(self.left.save_helper())
        else:
            final_list.append(None)
        if self.right != None:
            final_list.append(self.right.save_helper())
        else:
            final_list.append(None)

        return([final_list][0])
