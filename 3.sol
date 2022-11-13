//SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;
contract StudentData {
    event Log(string func, address sender, uint value, bytes data);
    struct Student {
        uint id;
        uint marks;
        string name;
    }
    Student[] students;
    uint nextId = 0;
    function Create(uint marks,string memory name) public {
        students.push(Student(nextId,marks,name));
        nextId++;
    }
    function Read(uint id) view public returns(uint uid, uint marks, string memory name) {
        for(uint i=0; i<students.length; i++) {
            if(students[i].id == id) {
                return(students[i].id, students[i].marks, students[i].name);
            }
        }
    }
    function Update(uint id, uint marks, string memory name) public {
        for(uint i=0; i<students.length; i++) {
            if(students[i].id == id) {
                students[i].name =name;
                students[i].marks =marks;
            }
        }
    }
    function Delete(uint id) public {
        delete students[id];
    }
    fallback() external payable{
        emit Log("fallback",msg.sender,msg.value, msg.data);
    }

    receive() external payable{
        
    }

}