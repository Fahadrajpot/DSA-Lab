#include <iostream>
#include <vector>
#include <time.h>

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
void CreateRandomFile ( string fn , int Size , int RN =100)
{
srand ( time (0) ) ;
std::ofstream Writer ( fn ) ;
for ( int i = 0; i < Size * 1024 * 1024; i ++)
{
Writer << rand () % RN << " " ;
}
}
main(){
    CreateRandomFile ( "vector" , 2 , 100)    
}
