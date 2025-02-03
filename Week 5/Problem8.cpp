#include <iostream>
#include <vector>

using namespace std;

template <typename T>
class array_list {
public:
    array_list() : data(2), size(0), capacity(2) {}

    void push_back(T value) {
        if (size >= capacity) {
            capacity = static_cast<int>(capacity * 1.5); 
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

    friend ostream& operator<<(ostream& out, const array_list& other) {
        for (int i = 0; i < other.size; ++i) {
            out << other.data[i] << " ";
        }
        return out;
    }

    ~array_list() {}

private:
    vector<T> data;
    int size;
    int capacity;
};

int main() {
    array_list<int> array_list;

    for (int i = 0; i < 10; ++i) {
        array_list.push_back(i);
        cout << "ArrayList: " << array_list << endl;
    }
    return 0;
}