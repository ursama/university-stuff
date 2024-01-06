#include <iostream>
#include <string>

using namespace std;

int main() {
    string word = "initial";
    const int D = 3;
    int shorter_words = 0;

    while (word[0] != '?' || word[word.length() - 1] != '?') {
        cout << "Enter a word that starts and end with the '?' sign: ";
        cin >> word;
        if (word.length() < D && (word[0] != '?' || word[word.length() - 1] != '?')) shorter_words++;
    };

    cout << "Number of words shorter than " << D << ": " << shorter_words;

    return 0;
}