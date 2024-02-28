#include <iostream>
#include <string>
#include <array>
#include "roster.h"


using namespace std;

Roster::Roster()
{
	for (int i = 0; i < 5; i++)
	{
		this->classRosterArray[i] = new Student;
	}
}

// Requirement F5 - destructor for Roster
Roster::~Roster()
{
	for (int i = 0; i < 5; i++)
	{
		delete classRosterArray[i];
		classRosterArray[i] = nullptr;
	}
}

// Requirement E3a: Sets instance variables from D1 and updates roster to next index
void Roster::add(string studentID, string firstName, string lastName, string emailAddress, int age, int daysInCourse1, int daysInCourse2, int daysInCourse3, DegreeProgram degreeProgram)
{
	int courseDurations[3] = { daysInCourse1, daysInCourse2, daysInCourse3 };
	classRosterArray[++startClassIndex] = new Student(studentID, firstName, lastName, emailAddress, age, courseDurations, degreeProgram);

}

string Roster::getStudentIDByIndex(int index)
{
	string studentID = classRosterArray[index]->GetStudentID();
	return studentID;
}

// Requirement E3b: Removes students from roster by student ID. Throws error message if student does not exist.
void Roster::remove(string studentID)
{
	bool studentExists = false;

	for (int i = 0; i < 5; i++)
	{
		if (classRosterArray[i] == nullptr)
		{
			continue;
		}
		else if (studentID == classRosterArray[i]->GetStudentID()) {
			classRosterArray[i] = nullptr;
			studentExists = true;
			break;
		}
	}
	if (!studentExists)
	{
		cout << "ERROR: The student with ID: " << studentID << " was not found." << endl;
	}
	if (studentExists)
	{
		cout << "The student with ID " << studentID << " has been removed." << endl;
	}
}

// Requirement E2a and E2b: Parse each set of data in studentData table and perform add to classRosterArray
void Roster::parse(string studentData)
{
	size_t rightIndex = studentData.find(",");
	string studentID = studentData.substr(0, rightIndex);

	size_t leftIndex = rightIndex + 1;
	rightIndex = studentData.find(",", leftIndex);
	string firstName = studentData.substr(leftIndex, rightIndex - leftIndex);

	leftIndex = rightIndex + 1;
	rightIndex = studentData.find(",", leftIndex);
	string lastName = studentData.substr(leftIndex, rightIndex - leftIndex);

	leftIndex = rightIndex + 1;
	rightIndex = studentData.find(",", leftIndex);
	string emailAddress = studentData.substr(leftIndex, rightIndex - leftIndex);

	leftIndex = rightIndex + 1;
	rightIndex = studentData.find(",", leftIndex);
	int age = stoi(studentData.substr(leftIndex, rightIndex - leftIndex));

	leftIndex = rightIndex + 1;
	rightIndex = studentData.find(",", leftIndex);
	int daysInCourse1 = stoi(studentData.substr(leftIndex, rightIndex - leftIndex));

	leftIndex = rightIndex + 1;
	rightIndex = studentData.find(",", leftIndex);
	int daysInCourse2 = stoi(studentData.substr(leftIndex, rightIndex - leftIndex));

	leftIndex = rightIndex + 1;
	rightIndex = studentData.find(",", leftIndex);
	int daysInCourse3 = stoi(studentData.substr(leftIndex, rightIndex - leftIndex));

	leftIndex = rightIndex + 1;
	rightIndex = studentData.find(",", leftIndex);
	string strDegreeProgram = studentData.substr(leftIndex, rightIndex - leftIndex);
	DegreeProgram degreeProgram = SECURITY;
	if (strDegreeProgram == "NETWORK")
	{
		degreeProgram = NETWORK;
	}
	else if (strDegreeProgram == "SOFTWARE")
	{
		degreeProgram = SOFTWARE;
	}

	add(studentID, firstName, lastName, emailAddress, age, daysInCourse1, daysInCourse2, daysInCourse3, degreeProgram);
}

// Requirement E3c: Print a complete tab-separated list of student data. Usues Print() function.
void Roster::printAll()
{
	cout << "Displaying Roster of All Students:" << endl;
	// Check if the pointer is null, if it is then skip to print non null pointers. 
	for (int i = 0; i < 5; i++)
	{
		if (classRosterArray[i] == nullptr)
		{
		}
		else
		{
			classRosterArray[i]->Print();
		}
	}
}

// Requirement E3d: Prints student's average number of days in the three courses provided
void Roster::printAverageDaysInCourse(string studentID)
{
	int sumOfCourseDays = 0;
	for (int i = 0; i < 5; i++)
	{
		if (studentID == classRosterArray[i]->GetStudentID())
		{
			sumOfCourseDays = classRosterArray[i]->GetDaysInCourse()[0] + classRosterArray[i]->GetDaysInCourse()[1] + classRosterArray[i]->GetDaysInCourse()[2];

			cout << "Student ID: " << studentID << ", average days in course is: " << sumOfCourseDays / 3 << endl;
		}
	}
}

// Requirement E3e: Verifies student emails and displays invalid email addresses
void Roster::printInvalidEmails()
{
	cout << "\nDisplaying Invalid Emails:\n";

	for (int i = 0; i < 5; i++)
	{
		string studentEmail = classRosterArray[i]->GetEmailAddress();

		if (studentEmail.find('@') == string::npos || studentEmail.find(' ') != string::npos || studentEmail.find('.') == string::npos)
		{
			cout << studentEmail << " - is invalid.\n";
		}
	}
	cout << endl;
}

void Roster::printByDegreeProgram(DegreeProgram degreeProgram)
{
	string strDegreeProgram;

	if (degreeProgram == SECURITY)
	{
		strDegreeProgram = "Security";
	}
	else if (degreeProgram == NETWORK)
	{
		strDegreeProgram = "Network";
	}
	else if (degreeProgram == SOFTWARE)
	{
		strDegreeProgram = "Software";
	}

	cout << "\nDisplaying students in degree program: " << strDegreeProgram << endl;

	for (int i = 0; i < 5; i++)
	{
		if (classRosterArray[i]->GetDegreeProgram() == degreeProgram)
		{
			classRosterArray[i]->Print();
		}
	}
}

