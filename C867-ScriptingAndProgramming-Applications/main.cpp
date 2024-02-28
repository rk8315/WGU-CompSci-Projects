#include <iostream>
#include <string>
#include <array>

#include "roster.h"
#include "student.h"

using namespace std;

int main()
{
    // Requirement A: Modified studentData table to include personal information as last item
    const string studentData[5] =
    { "A1,John,Smith,John1989@gm ail.com,20,30,35,40,SECURITY",
      "A2,Suzan,Erickson,Erickson_1990@gmailcom,19,50,30,40,NETWORK",
      "A3,Jack,Napoli,The_lawyer99yahoo.com,19,20,40,33,SOFTWARE",
      "A4,Erin,Black,Erin.black@comcast.net,22,50,58,40,SECURITY",
      "A5,Robert,Kearns,rkear24@wgu.edu,32,7,10,15,SOFTWARE"
    };
    
    // Requirement F1: Print program introduction
    cout << "C867 - Scripting and Programming - Applications\nLanguage: C++\nStudentID: 011818662\nName: Robert Kearns\n" << endl;

    // Requirement F2: Create an instance of Roster
    Roster classRoster[5];

    // Requirement F3: Add each student from studentData to classRoster
    for (int i = 0; i < 5; i++)
    {
        classRoster->parse(studentData[i]);
    }

    // Requirement F4: converted pseudo code to complete rest of main() function
    classRoster->printAll();
    classRoster->printInvalidEmails();
    cout << "Displaying Average Days in a Course:\n";
    for (int i = 0; i < 5; i++)
    {
        classRoster->printAverageDaysInCourse(classRoster->getStudentIDByIndex(i));
    }
    classRoster->printByDegreeProgram(SOFTWARE);  
    cout << "\nPerforming Remove Function:\n";
    classRoster->remove("A3");
    classRoster->printAll();
    classRoster->remove("A3");
    
    cout << "\nDONE.\n";
}
