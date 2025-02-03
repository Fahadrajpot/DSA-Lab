#include <iostream>
#include <vector>
#include <string>
#include <conio.h>

using namespace std;


int main() {
    vector<string> vec;
    char option=0;
    string input;
    while (option != '3') {
        system("cls");
        cout << "Choose an operation:"<< endl;
        cout << "1. Add a string"<<endl;
        cout << "2. Remove a string"<<endl;
        cout << "3. Exit"<<endl;
        cin >> option;
        if (option == '1') {
            cout << "Enter a string to add: ";
            cin.ignore();
            getline(cin, input);
            vec.push_back(input);
            cout << "Size: " << vec.size() << ", Capacity: " << vec.capacity() << endl;
        } else if (option == '2') {
            if (!vec.empty()) {
                vec.pop_back();
                cout << "Last string removed."<< endl;
            } else {
                cout << "Vector is empty, nothing to remove."<<endl;
            }
            cout << "Size: " << vec.size() << ", Capacity: " << vec.capacity() << endl;
        }else if(option=='3'){
            break;
        
        } else {
            cout << "Invalid option. Please try again."<<endl;
        }
        getch();
    }

    return 0;
}
