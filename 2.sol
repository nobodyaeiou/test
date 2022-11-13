//SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;
contract BankAccount{
    address public owner;   //0x77efCF344B14983049bB222c47313E7387171400
    uint256 public balance; //0x74460327D8ECa83Dc2AB78F3Fd4d206B52cC435F balance fn 
    constructor(){
        owner = msg.sender;     
    }
    receive() payable external{
        balance += msg.value;
        // deposit fn
    }
    function withdraw(uint256 amount, address payable destAddress) public {
        require(msg.sender == owner, "Only owner can withdraw");
        require(amount<= balance, "Insufficent funds");

        destAddress.transfer(amount); // transfer is inbuilt function
        balance -= amount;

        // withdraw fn
    }
}
