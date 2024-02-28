#include <iostream>
#include <array>
#include <string>
#include "student.h"

using namespace std;

// Requirement D2d: Constructor(s) using all input parameters in studentData table
Student::Student()
{
	this->studentID = "";
	this->firstName = "";
	this->lastName = "";
	this->emailAddress = "";
	this->age = 0;
	for (int i = 0; i < 3; i++)
	{
		this->daysInCourse[i] = 0;
	}
	this->degreeProgram = SOFTWARE;
}
Student::Student(string studentID, string firstName, string lastName, string emailAddress, int age, int daysInCourse[], DegreeProgram degreeProgram)
{
	this->studentID = studentID;
	this->firstName = firstName;
	this->lastName = lastName;
	this->emailAddress = emailAddress;
	this->age = age;
	for (int i = 0; i < 3; i++)
	{
		this->daysInCourse[i] = daysInCourse[i];
	}
	this->degreeProgram = degreeProgram;
}

string Student::GetStudentID()
{
	return studentID;
}

string Student::GetFirstName()
{
	return firstName;
}

string Student::GetLastName()
{
	return lastName;
}

string Student::GetEmailAddress()
{
	return emailAddress;
}

int Student::GetAge()
{
	return age;
}

int* Student::GetDaysInCourse()
{
	return daysInCourse;
}

DegreeProgram Student::GetDegreeProgram()
{
	return degreeProgram;
}

void Student::SetStudentID(string newStudentID)
{
	studentID = newStudentID;
}

void Student::SetFirstName(string newFirstName)
{
	firstName = newFirstName;
}

void Student::SetLastName(string newLastName)
{
	lastName = newLastName;
}

void Student::SetEmailAddress(string newEmailAddress)
{
	emailAddress = newEmailAddress;
}

void Student::SetAge(int newAge)
{
	age = newAge;
}

void Student::SetDaysInCourse(int* newDaysInCourse)
{
	for (int i = 0; i < 3; i++)
	{
		daysInCourse[i] = newDaysInCourse[i];
	}
}

void Student::SetDegreeProgram(DegreeProgram newDegreeProgram)
{
	degreeProgram = newDegreeProgram;
}

// Requirement D2e: print function to print specific student data
void Student::Print()
{
	string strDegreeProgram;

	if (this->GetDegreeProgram()  == SECURITY)
	{
		strDegreeProgram = "Security";
	}
	else if (this->GetDegreeProgram() == NETWORK)
	{
		strDegreeProgram = "Network";
	}
	else if (this->GetDegreeProgram() == SOFTWARE)
	{
		strDegreeProgram = "Software";
	}
	
	cout << this->GetStudentID() << "\tFirst Name: " << this->GetFirstName() << "\tLast Name: " << this->GetLastName() << "\tAge: " << this->GetAge() << "\t\tdaysInCourse: " << "{";
	for (int i = 0; i < 3; i++)
	{
		if (i == 2)
		{
			cout << this->GetDaysInCourse()[i];
		}
		else 
		{
			cout << this->GetDaysInCourse()[i] << ", ";
		}
	}
	cout << "}\tDegree Program: " << strDegreeProgram << endl;
}
