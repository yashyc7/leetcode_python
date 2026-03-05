/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
    private:
   void InsertAtTail(Node*&head,Node*&tail,int data)
{
    Node*temp=new Node(data);
    if(head==NULL)
    {
        head=temp;
        tail=temp;
        return ; 
    }
    else
    {
        tail->next=temp;
        tail=temp;
    }
}
public:
    Node* copyRandomList(Node* head) {
     Node*clonehead=NULL;
        Node*clonetail=NULL;
        Node*temp=head;
        while(temp!=NULL)
        {
            InsertAtTail(clonehead,clonetail,temp->val);
            temp=temp->next;
        } //clone LInked list is created Using the next pointer 
        
        unordered_map<Node*,Node*>OldToNew;
        Node*original=head;
        Node*clone=clonehead;
        while(original!=NULL && clone!=NULL)
        {
            OldToNew[original]=clone;
            original=original->next;
            clone=clone->next;
        }
        
        original=head;
        clone=clonehead;
        while(original!=NULL)
        {
            clone->random=OldToNew[original->random];
            original=original->next;
            clone=clone->next;
        }
        return clonehead;
        
    }
};