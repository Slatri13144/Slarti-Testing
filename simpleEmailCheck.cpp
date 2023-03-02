#include <iostream>
#include <string>
using namespace std;

void validEmail(string email) {
	size_t atSign = email.find("@");
	size_t period = email.find(".");
	if (atSign != string::npos) {
		if (period != string::npos) {
			cout << "This is a valid email!" << endl;
			return;
		}
	}
			
	cout << "This is not a valid email!" << endl;
}

int main() {
	string userEmail;
	cout << "Please enter an email to check: " << endl;
	cin >> userEmail;
	validEmail(userEmail);
	return 0;
}