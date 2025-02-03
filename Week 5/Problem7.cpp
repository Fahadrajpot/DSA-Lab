#include <iostream>
#include <vector>

using namespace std;

template <typename T>
class Vector {
public:
    Vector() : data(1), size(0), capacity(1) {}

    void push_back(T value) {
        if (size >= capacity) {
            capacity *= 2; 
            vector<T> newData(capacity);
            move(data.begin(), data.end(), newData.begin());
            data = move(newData);
        }
        data[size++] = value;
    }

    T operator[](int index) const {
        if (index >= size) {
            throw out_of_range("Index out of bounds");
        }
        return data[index];
    }

    T& operator[](int index) {
        if (index >= size) {
            throw out_of_range("Index out of bounds");
        }
        return data[index];
    }

    friend ostream& operator<<(ostream& out, const Vector& other) {
        for (int i = 0; i < other.size; ++i) {
            out << other.data[i] << " ";
        }
        return out;
    }

    ~Vector() {}

private:
    vector<T> data;
    int size;
    int capacity;
};

int main() {
    Vector<int> vector;
    for (int i = 0; i < 10; ++i) {
        vector.push_back(i);
        cout << "Vector: " << vector << endl;
    }
    return 0;
}