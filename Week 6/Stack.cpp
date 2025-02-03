#include <iostream>
using namespace std;

class Stack {
private:
    int* stack;
    int top;
    int capacity;

public:
    Stack(int capacity) {
        this->capacity = capacity;
        stack = new int[capacity];
        top = -1;
    }

    void push(int num) {
        if (top >= capacity - 1) {
            cout << "Stack is full." << endl;
        } else {
            top++;
            stack[top] = num;
            cout << num << " pushed to the stack." << endl;
        }
    }

    void pop() {
        if (top == -1) {
            cout << "Stack is empty." << endl;
            return ;
        } else {
            top--;
            return ;
        }
    }

    int top() {
        if (top == -1) {
            cout << "Stack is empty." << endl;
            return 0;
        } else {
            return stack[top];
        }
    }
};
