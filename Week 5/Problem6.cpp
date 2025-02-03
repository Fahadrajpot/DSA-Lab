#include <iostream>
#include <vector>

using namespace std;

template <typename T>
class auto_growing_array {
public:
    auto_growing_array() : data(1), size(0), capacity(1) {}

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

    friend ostream& operator<<(ostream& out, const auto_growing_array& other) {
        for (int i = 0; i < other.size; ++i) {
            out << other.data[i] << " ";
        }
        return out;
    }

    ~auto_growing_array() {}

    void push_back(T value) {
        if (size >= capacity) {
            capacity++;
            vector<T> newData(capacity);
            copy(data.begin(), data.end(), newData.begin());
            data = move(newData);
        }
        data[size++] = value;
    }

private:
    vector<T> data;
    int size;
    int capacity;
};

int main() {
    auto_growing_array<int> array;

    for (int i = 0; i < 10; ++i) {
        array.push_back(i);
        cout << "Array: " << array << endl;
    }


    return 0;
}