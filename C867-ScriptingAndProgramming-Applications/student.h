#pragma once
#include <array>
#include <string>
#include "degree.h"

using namespace std;

class Student
{
public:
	Student();
	Student(string studentID, string firstName, string lastName, string emailAddress, int age, int daysInCourse[], DegreeProgram degreeProgram);

	// Requirement D2a: Accessors (getters) for each instance variable
	string GetStudentID();
	string GetFirstName();
	string GetLastName();
	string GetEmailAddress();
	int GetAge();
	int* GetDaysInCourse();
	DegreeProgram GetDegreeProgram();

	// Requirement D2B: Mutators (setters) for each instance variable
	void SetStudentID(string newStudentID);
	void SetFirstName(string newFirstName);
	void SetLastName(string newLastName);
	void SetEmailAddress(string newEmailAddress);
	void SetAge(int newAge);
	void SetDaysInCourse(int* newDaysInCourse);
	void SetDegreeProgram(DegreeProgram newDegreeProgram);

	// Requirement D2e: function to print specific student data
	void Print();

private:
	//Requirement D1: Create student class with required variables
	string studentID;
	string firstName;
	string lastName;
	string emailAddress;
	int age;
	int daysInCourse[3] = { 0, 0, 0 };
	DegreeProgram degreeProgram;
};


