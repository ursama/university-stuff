#include <iostream>
#include <string>

using namespace std;

int main() { 
    // it will make the user input the words until they input one that starts with a small letter
    string word;

    do {
        cout << "Input a word that starts with a small letter: ";
        cin >> word;
    } while (word[0] >= 'z' || word[0] <= 'a');
    
    return 0;
}
