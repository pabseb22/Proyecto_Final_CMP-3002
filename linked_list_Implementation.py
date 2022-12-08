#Linked List Implementation
import ctypes

class Node:
    """
    Implementation of a node
    """
    def __init__(self, val=None):
        self.val = val
        self.next_node = None
        
    def set_next_node(self, node):
        self.next_node = node

class Singly_linked_list:
    """
    Implementation of a singly linked list
    """
    def __init__(self, name, head_node=None):
        self.head_node = head_node
        self.name = name

    def set_head_node(self, new_node):
        self.head_node = new_node  

    def get_head_node(self):
        return self.head_node
    
        
    def list_traversed(self):
        respuesta = ''
        node = self.head_node
        if node:
            respuesta += str(node.val)
            #print(node.val, end = '')
        while node:
            if node != self.head_node:
                respuesta += ' -> '
                respuesta += str(node.val)
                #print(' -> {}'.format(node.val), end = '')
            node = node.next_node
            
        return respuesta
    
    def search_1(self,name,newname):#metodo para reemplazar nombre Playlist
        
        current=self.head_node

        while current!=None:
            if current.val.name==name:
                current.val.name=newname
                return True
            current=current.next_node
        if current==None:
            return None
    

    def list_traversed_1(self):#traverse para imprimir nombres de canciones
        respuesta = '--> '
        node = self.head_node
        if node:
            respuesta += str(node.val.name)
            #print(node.val, end = '')
        while node:
            if node != self.head_node:
                respuesta += ' \n--> '
                respuesta += str(node.val.name)
                #print(' -> {}'.format(node.val), end = '')
            node = node.next_node
            
        return respuesta
            
    def insert_head(self, new_node):
        # insert to the head
        # A -> B -> null
        # R -> A -> B -> null 
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
        
    def insert_tail(self, new_node):
        # insert to the tail
        # A -> B -> null
        # A -> B -> R -> null 
        node = self.head_node
        prev = None
        while node:
            prev = node
            node = node.next_node
        prev.set_next_node(new_node)
        
    def delete_head(self):
        if self.head_node.next_node:
            self.head_node = self.head_node.next_node
        else:
            self.head_node = None
    
    def delete_tail(self):
        if self.head_node.next_node:
            prev = self.head_node
            node = prev.next_node
        
            while node.next_node:
                prev = node
                node = node.next_node

        
            prev.next_node = None
        else:
            self.head_node = None
            
    
    def delete_node(self, value):
        prev = self.head_node
        node = prev.next_node
        
        if node:
        
            if prev.val == value:
                self.head_node = self.head_node.next_node
                prev.next_node = None
            
            else:
            
                while node.val != value:
                        prev = node
                        node = node.next_node
                        
                        if node == None:
                            break
                    
                if node:
                    prev.set_next_node(node.next_node)
                    node.next_node = None
                    
                else:
                    print("Valor no se encuentra")
        else:
            self.head_node = None
    def delete_node_1(self, value):#metodo eliminar playlist
        prev = self.head_node
        node = prev.next_node
        
        if node:
        
            if prev.val.name == value:
                
                self.head_node = self.head_node.next_node
                prev.next_node = None
                return True
            
            else:
            
                while node.val.name != value:
                        
                        prev = node
                        node = node.next_node
                        
                        if node == None:
                            
                            break
                    
                if node:
                    
                    prev.set_next_node(node.next_node)
                    node.next_node = None
                    return True
                    
                else:
                    print("Valor no se encuentra")
                    return False
        else:
            self.head_node = None
            
                
    def reverse_list(lista):
            prev = None
            # We start with the head node
            node = lista.head_node

            
            while node:
                next_node = node.next_node
                node.next_node = prev
                prev = node
                node = next_node

            lista.head_node = prev

# Main Function Startup
def start_Project():
    global playlists
    playlists = Singly_linked_list("playlists")

    global play_queue
    play_queue = Singly_linked_list("play_queue")

def create_Playlist(name):
    node_1 = Node(Singly_linked_list(name))
    playlists.insert_head(node_1)

def rename_Playlist(name, newname):
    if(playlists.search_1(name,newname)):
        print("Succesful")
    else:
        print("Failed")

def show_Playlists():
    if playlists.get_head_node():
        print(playlists.list_traversed_1())
    else:
        print("No playlists")


def delete_Playlist(name):
    if(playlists.delete_node_1(name)):
        print("Succesful")
    else:
        print("Failed")


start_Project()
create_Playlist("SALSA")
create_Playlist("CUMBIA")

show_Playlists()

rename_Playlist("CUMBIA","REGGAE")

show_Playlists()

delete_Playlist("SALSA")

show_Playlists()

