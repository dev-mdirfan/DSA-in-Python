/*
Take Input the Full date and print the day of that date
0 - Saturday
*/

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int day, month, year;
    cout << "Enter the day: ";
    cin >> day;
    cout << "Enter the month: ";
    cin >> month;
    cout << "Enter the year: ";
    cin >> year;
    int code;
    code = (year + (year / 4) - (year / 100) + (year / 400)) % 7;
    int month_code;
    switch (month)
    {
    case 1:
        month_code = 0;
        break;
    case 2:
        month_code = 3;
        break;
    case 3:
        month_code = 3;
        break;
    case 4:
        month_code = 6;
        break;
    case 5:
        month_code = 1;
        break;
    case 6:
        month_code = 4;
        break;
    case 7:
        month_code = 6;
        break;
    case 8:
        month_code = 2;
        break;
    case 9:
        month_code = 5;
        break;
    case 10:
        month_code = 0;
        break;
    case 11:
        month_code = 3;
        break;
    case 12:
        month_code = 5;
        break;
    default:
        cout << "Invalid month" << endl;
    }
    int century_code;
    century_code = (year / 100) % 4;
    int day_code;
    day_code = (day + month_code + century_code + code) % 7;
    switch (day_code)
    {
    case 0:
        cout << "Saturday" << endl;
        break;
    case 1:
        cout << "Sunday" << endl;
        break;
    case 2:
        cout << "Monday" << endl;
        break;
    case 3:
        cout << "Tuesday" << endl;
        break;
    case 4:
        cout << "Wednesday" << endl;
        break;
    case 5:
        cout << "Thursday" << endl;
        break;
    case 6:
        cout << "Friday" << endl;
        break;
    default:
        cout << "Invalid day" << endl;
    }
    return 0;
}
