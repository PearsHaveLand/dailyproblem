// An XOR linked list is a more memory efficient doubly linked list. Instead of
// each node holding next and prev fields, it holds a field named both, which is
// an XOR of the next node and the previous node. Implement an XOR linked list;
// it has an add(element) which adds the element to the end, and a get(index)
// which returns the node at index.

// If using a language that has no pointers (such as Python), you can assume you
// have access to get_pointer and dereference_pointer functions that converts
// between nodes and memory addresses.

using namespace std;
#include <iostream>

class xor_list {
    public:
    
    // Default constructor
    xor_list(){
        m_root = NULL;
        m_end = NULL;
    }

    ~xor_list(){
        node_t *curr_node = m_root; // Start at the root of the list
        unsigned long ul_prev_node = NULL;
        node_t *next_node = NULL;

        // Loop until the end of the list
        while (curr_node != NULL){

            // Save position of next node
            // addr(next node) = curr_node->m_both XOR addr(previous node)
            next_node = (node_t*)(curr_node->m_both ^ ul_prev_node);
            
            cout << "deleting node with value " << curr_node->m_data << endl;

            // Update address of previous node to that of current node
            ul_prev_node = (unsigned long)curr_node;

            // Delete current node and update to next node
            delete curr_node;
            curr_node = next_node;
        }
    }

    typedef struct node {
        int m_data;
        unsigned long m_both;
    } node_t;

    void add(int data){

        cout << "adding " << data << endl;

        // Create new node with the correct data
        node_t *new_node = new node_t;
        new_node->m_data = data;
        new_node->m_both = (unsigned long)m_end;

        cout << "new node created successfully" << endl;

        if (!m_root)
        {
            m_root = new_node;
            m_end = m_root;
        }
        else
        {
            // Update end node's m_both pointer with new node
            m_end->m_both = m_end->m_both ^ (unsigned long)new_node;
            m_end = new_node;
        }
        cout << "data " << data << " successfully added" << endl;
    }

    // Returns node at given index
    node_t get(int index){
        node_t retval;
        retval.m_data = m_root->m_data;
        retval.m_both = m_root->m_both;

        return retval;
    }

    private:
    node_t *m_root;
    node_t *m_end;
};

int main(){
    xor_list my_list;
    my_list.add(1);
    my_list.add(2);
    my_list.add(3);
    my_list.add(4);
    my_list.add(5);

    xor_list::node_t my_node;
    for (int i = 0; i < 5; i++){
        my_node = my_list.get(i);
        cout << my_node.m_data;
    }

    return 0;
}