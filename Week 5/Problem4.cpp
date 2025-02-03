#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void reverse_vector(vector<int>& vec);
void sort_vector(vector<int>& vec);
void remove_duplicates(vector<int>& vec);
void print_vector(const vector<int>& vec);

int main() {
    vector<int> vec = {10, 20, 10, 30, 40, 30, 50, 60, 50, 70};

    cout << "Original vector: ";
    print_vector(vec);

    reverse_vector(vec);
    cout << "Reversed vector: ";
    print_vector(vec);

    sort_vector(vec);
    cout << "Sorted vector: ";
    print_vector(vec);

    remove_duplicates(vec);
    cout << "Vector after removing duplicates: ";
    print_vector(vec);

    return 0;
}
void reverse_vector(vector<int>& vec) {
    reverse(vec.begin(), vec.end());
}

void sort_vector(vector<int>& vec) {
    sort(vec.begin(), vec.end());
}

void remove_duplicates(vector<int>& vec) {
    auto it = unique(vec.begin(), vec.end());
    vec.erase(it, vec.end());
}

void print_vector(const vector<int>& vec) {
    for (int num : vec) {
        cout << num << " ";
    }
    cout << endl;
}