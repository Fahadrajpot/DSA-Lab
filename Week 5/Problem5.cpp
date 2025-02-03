#include <iostream>
#include <vector>

using namespace std;

void add_row(vector<vector<int>>& matrix, const vector<int>& row);
void add_column(vector<vector<int>>& matrix, const vector<int>& column);
void display_matrix(const vector<vector<int>>& matrix);
vector<vector<int>> transpose_matrix(const vector<vector<int>> matrix);

int main() {
    vector<vector<int>> matrix = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    cout << "Original matrix:" << endl;
    display_matrix(matrix);

    vector<int> new_row = {10, 11, 12};
    add_row(matrix, new_row);
    cout << "Matrix after adding a row:" << endl;
    display_matrix(matrix);

    vector<int> new_column = {13, 14, 15, 16};
    add_column(matrix, new_column);
    cout << "Matrix after adding a column:" << endl;
    display_matrix(matrix);

    vector<vector<int>> transposed = transpose_matrix(matrix);
    cout << "Transposed matrix:" << endl;
    display_matrix(transposed);

    return 0;
}
void add_row(vector<vector<int>>& matrix, const vector<int>& row) {
    matrix.push_back(row);
}

void add_column(vector<vector<int>>& matrix, const vector<int>& column) {
    if (matrix.empty()) {
        for (int val : column) {
            matrix.push_back({val});
        }
    } else {
        for (size_t i = 0; i < matrix.size(); ++i) {
            if (i < column.size()) {
                matrix[i].push_back(column[i]);
            } else {
                matrix[i].push_back(0);
            }
        }
    }
}

void display_matrix(const vector<vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
}

vector<vector<int>> transpose_matrix(const vector<vector<int>> matrix) {
    if (matrix.empty()) return {};

    size_t rows = matrix.size();
    size_t cols = matrix[0].size();
    vector<vector<int>> transposed(cols, vector<int>(rows));

    for (size_t i = 0; i < rows; ++i) {
        for (size_t j = 0; j < cols; ++j) {
            transposed[j][i] = matrix[i][j];
        }
    }
    return transposed;
}
