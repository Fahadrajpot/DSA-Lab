#include <iostream>
using namespace std;

class Queue {
private:
    int* queue;
    int capacity;
    int front;
    int rear;
    int size;

public:
    Queue(int capacity) {
        this->capacity = capacity;
        queue = new int[capacity];
        front = 0;
        rear = -1;
        size = 0;
    }

    void enqueue(int num) {
        if (size==capacity) {
            cout << "Queue is full." << num << "." << endl;
            return;
        }
        else{
            rear++;
            queue[rear] = num;
            size++;
            cout << num << " enqueued to the queue." << endl;
        }
    }

    int dequeue() {
        if (size==0) {
            cout << "Queue is empty." << endl;
            return ;
        }
        front ++;
        size--;
        return ;
    }

    int peek() {
        if (size==0) {
            cout << "Queue is empty." << endl;
            return 0;
        }
        return queue[front];
    }

    bool is_full() {
        return size == capacity;
    }

    bool is_empty() {
        return size == 0;
    }

};
