#include <iostream>
using namespace std;

// Linked List

class Node {
public:
    int data;
    Node* next;

    Node(int value) {
        data=value;
        next= NULL;
    }
};

class LinkList {
private:
    Node* head;
public:
    LinkList() {
        head = NULL;
    }

    ~LinkList() {
        while (head != NULL) {
            Node* temp = head;
            head = head->next;
            delete temp;
        }
    }

    bool is_empty() {
        return head == NULL;
    }

    Node* insert_node(int index, int x) {
        Node* new_node = new Node(x);
        if (index == 0) {
            new_node->next = head;
            head = new_node;
            return head;
        }

        Node* current = head;
        for (int i = 0; i < index - 1 && current != NULL; i++) {
            current = current->next;
        }

        if (current == NULL) {
            cout << "Index out of bounds" << endl;
            delete new_node;
            return NULL;
        }

        new_node->next = current->next;
        current->next = new_node;
        return new_node;
    }

    Node* insert_at_head(int x) {
        Node* new_node = new Node(x);
        new_node->next = head;
        head=new_node;
        return new_node;
    }

    Node* insert_at_end(int x) {
        Node* new_node = new Node(x);
        if (head == NULL) {
            head=new_node;
            return head;
        }

        Node* current = head;
        while (current->next != NULL) {
            current = current->next;
        }

        current->next = new_node;
        return head;
    }

    bool find_node(int x) {
        Node* current = head;
        while (current != NULL) {
            if (current->data == x) {
                return true;
            }
            current = current->next;
        }
        return false;
    }

    bool delete_node(int x) {
        if (head == NULL) {
            return false;
        }
        Node* current = head;
        Node* previous = NULL;

        bool found = false;
        while (current != NULL) {
            if (current->data == x) {
                if (previous == NULL) {
                    head = current->next;
                } else {
                    previous->next = current->next;
                }
                delete current;
                found = true;
                current = (previous == NULL) ? head : previous->next;
            } else {
                previous = current;
                current = current->next;
            }
        }
        return found;
    }

    bool delete_from_start() {
        if (head == NULL) return false;

        Node* temp = head;
        head = head->next;
        delete temp;
        return true;
    }

    bool delete_from_end() {
        if (head == NULL) return false;

        if (head->next == NULL) {
            delete head;
            head = NULL;
            return true;
        }

        Node* current = head;
        while (current->next->next != NULL) {
            current = current->next;
        }

        delete current->next;
        current->next = NULL;
        return true;
    }

    void display_list() {
        Node* current = head;
        if (current!= NULL){
            cout << current->data ;
            current = current->next;
            while (current != NULL) {
                cout << " , " << current->data ;
                current = current->next;
            }
        }
        cout << endl;
    }

    Node* reverse_list() {
        Node* prev = NULL;
        Node* current = head;
        Node* next = NULL;

        while (current != NULL) {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        head = prev;
        return head;
    }

    Node* sort_list(Node* list) {
        if (list == NULL || list->next == NULL) {
            return list;
        }

        Node* sorted = NULL;

        while (list != NULL) {
            Node* current = list;
            list = list->next;

            if (sorted == NULL || sorted->data >= current->data) {
                current->next = sorted;
                sorted = current;
            } else {
                Node* temp = sorted;
                while (temp->next != NULL && temp->next->data < current->data) {
                    temp = temp->next;
                }
                current->next = temp->next;
                temp->next = current;
            }
        }
        return sorted;
    }

    Node* remove_duplicates(Node* list) {
        Node* current = list;

        while (current != NULL && current->next != NULL) {
            if (current->data == current->next->data) {
                Node* temp = current->next;
                current->next = current->next->next;
                delete temp;
            } else {
                current = current->next;
            }
        }
        return list;
    }

    Node* merge_lists(Node* list1, Node* list2) {
        if (list1 == NULL) return list2;
        if (list2 == NULL) return list1;

        if (list1->data < list2->data) {
            list1->next = merge_lists(list1->next, list2);
            return list1;
        } else {
            list2->next = merge_lists(list1, list2->next);
            return list2;
        }
    }

    Node* interest_lists(Node* list1, Node* list2) {
        Node* result = NULL;
        Node* tail = NULL;

        while (list1 != NULL && list2 != NULL) {
            if (list1->data == list2->data) {
                if (result == NULL) {
                    result = new Node(list1->data);
                    tail = result;
                } else {
                    tail->next = new Node(list1->data);
                    tail = tail->next;
                }
                list1 = list1->next;
                list2 = list2->next;
            } else if (list1->data < list2->data) {
                list1 = list1->next;
            } else {
                list2 = list2->next;
            }
        }

        return result;
    }
};

int main(){
    LinkList list;
    list.insert_at_head(10);
    list.insert_at_end(20);
    list.insert_at_head(30);
    list.reverse_list();
    list.display_list();
    return 0;
}
// Doubly Linked List

class DoublyNode {
public:
    int data;
    DoublyNode* next;
    DoublyNode* prev;

    DoublyNode(int value) {
        data = value;
        next = NULL;
        prev = NULL;
    }
};
class DoublyLinkList {
private:
    DoublyNode* head;
public:
    DoublyLinkList() {
        head = NULL;
    }

    ~DoublyLinkList() {
        while (head != NULL) {
            DoublyNode* temp = head;
            head = head->next;
            delete temp;
        }
    }

    bool is_empty() {
        return head == NULL;
    }

    DoublyNode* insert_node(int index, int x) {
        DoublyNode* new_node = new DoublyNode(x);
        if (index == 0) {
            if (head != NULL) {
                head->prev = new_node;
                new_node->next = head;
            }
            head = new_node;
            return head;
        }

        DoublyNode* current = head;
        for (int i = 0; i < index - 1 && current != NULL; i++) {
            current = current->next;
        }

        if (current == NULL) {
            cout << "Index out of bounds" << endl;
            delete new_node;
            return NULL;
        }

        new_node->next = current->next;
        if (current->next != NULL) {
            current->next->prev = new_node;
        }
        current->next = new_node;
        new_node->prev = current;

        return new_node;
    }

    DoublyNode* insert_at_head(int x) {
        DoublyNode* new_node = new DoublyNode(x);
        if (head != NULL) {
            head->prev = new_node;
            new_node->next = head;
        }
        head = new_node;
        return new_node;
    }

    DoublyNode* insert_at_end(int x) {
        DoublyNode* new_node = new DoublyNode(x);
        if (head == NULL) {
            head = new_node;
            return head;
        }

        DoublyNode* current = head;
        while (current->next != NULL) {
            current = current->next;
        }

        current->next = new_node;
        new_node->prev = current;
        return head;
    }

    bool find_node(int x) {
        DoublyNode* current = head;
        while (current != NULL) {
            if (current->data == x) {
                return true;
            }
            current = current->next;
        }
        return false;
    }

    bool delete_node(int x) {
        if (head == NULL) return false;

        DoublyNode* current = head;
        while (current != NULL && current->data != x) {
            current = current->next;
        }

        if (current == NULL) return false;

        if (current->prev != NULL) {
            current->prev->next = current->next;
        } else {
            head = current->next;
        }

        if (current->next != NULL) {
            current->next->prev = current->prev;
        }

        delete current;
        return true;
    }

    bool delete_from_start() {
        if (head == NULL) return false;

        DoublyNode* temp = head;
        head = head->next;

        if (head != NULL) {
            head->prev = NULL;
        }

        delete temp;
        return true;
    }

    bool delete_from_end() {
        if (head == NULL) return false;

        if (head->next == NULL) {
            delete head;
            head = NULL;
            return true;
        }

        DoublyNode* current = head;
        while (current->next != NULL) {
            current = current->next;
        }

        current->prev->next = NULL;
        delete current;
        return true;
    }

    void display_list() {
        DoublyNode* current = head;
        if (current!=NULL){
            cout << current->data ;
            current = current->next;
            while (current != NULL) {
                cout << " , " << current->data ;
                current = current->next;
                
        }
        cout<<endl;
        }
    }

    DoublyNode* reverse_list() {
        DoublyNode* temp = NULL;
        DoublyNode* current = head;

        while (current != NULL) {
            temp = current->prev;
            current->prev = current->next;
            current->next = temp;
            current = current->prev;
        }

        if (temp != NULL) {
            head = temp->prev;
        }
        return head;
    }

    DoublyNode* sort_list(DoublyNode* list) {
        if (list == NULL || list->next == NULL) {
            return list;
        }

        DoublyNode* sorted = NULL;

        while (list != NULL) {
            DoublyNode* current = list;
            list = list->next;

            if (sorted == NULL || sorted->data >= current->data) {
                current->next = sorted;
                if (sorted != NULL) {
                    sorted->prev = current;
                }
                sorted = current;
                sorted->prev = NULL;
            } else {
                DoublyNode* temp = sorted;
                while (temp->next != NULL && temp->next->data < current->data) {
                    temp = temp->next;
                }
                current->next = temp->next;
                if (temp->next != NULL) {
                    temp->next->prev = current;
                }
                temp->next = current;
                current->prev = temp;
            }
        }
        return sorted;
    }

    DoublyNode* remove_duplicates(DoublyNode* list) {
        DoublyNode* current = list;

        while (current != NULL && current->next != NULL) {
            if (current->data == current->next->data) {
                DoublyNode* temp = current->next;
                current->next = current->next->next;
                if (current->next != NULL) {
                    current->next->prev = current;
                }
                delete temp;
            } else {
                current = current->next;
            }
        }
        return list;
    }

    DoublyNode* merge_lists(DoublyNode* list1, DoublyNode* list2) {
        if (list1 == NULL) return list2;
        if (list2 == NULL) return list1;

        if (list1->data < list2->data) {
            list1->next = merge_lists(list1->next, list2);
            list1->next->prev = list1;
            return list1;
        } else {
            list2->next = merge_lists(list1, list2->next);
            list2->next->prev = list2;
            return list2;
        }
    }

    DoublyNode* interest_lists(DoublyNode* list1, DoublyNode* list2) {
        DoublyNode* result = NULL;
        DoublyNode* tail = NULL;

        while (list1 != NULL && list2 != NULL) {
            if (list1->data == list2->data) {
                if (result == NULL) {
                    result = new DoublyNode(list1->data);
                    tail = result;
                } else {
                    tail->next = new DoublyNode(list1->data);
                    tail->next->prev = tail;
                    tail = tail->next;
                }
                list1 = list1->next;
                list2 = list2->next;
            } else if (list1->data < list2->data) {
                list1 = list1->next;
            } else {
                list2 = list2->next;
            }
        }

        return result;
    }
};