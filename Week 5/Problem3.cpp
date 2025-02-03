#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    vector<int> vec = {5, 10, 56, 79,35, 62, 43, 65, 15, 20};
    int target;
    cout << "Enter the integer to search for: ";
    cin >> target;
    auto it = find(vec.begin(), vec.end(), target);
    if (it != vec.end()) {
        cout << "Integer found at index: " << distance(vec.begin(), it) << endl;
    } else {
        cout << "Integer not found in the vector." << endl;
    }
    return 0;
}
