#pragma once
#include <array>
#include <string>
#include "student.h"

using namespace std;

class Roster
{
public:
	Roster();
	~Roster();
	void add(string studentID, string firstName, string lastName, 
			string emailAddress, int age, int daysInCourse1, 
			int daysInCourse2, int daysInCourse3, DegreeProgram degreeProgram);
	string getStudentIDByIndex(int index);
	void remove(string studentID);
	void parse(string studentData);
	void printAll();
	void printAverageDaysInCourse(string studentID);
	void printInvalidEmails();
	void printByDegreeProgram(DegreeProgram degreeProgram);
	const static int classRosterSize = 5;
	Student* classRosterArray[classRosterSize];
	int startClassIndex = -1;

private:
	

};

