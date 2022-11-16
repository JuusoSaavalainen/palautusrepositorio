*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  user  testpassw1valid
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  dummyuser  testpassw1valid
    Output Should Contain  Username is taken/already in use

Register With Too Short Username And Valid Password
    Input Credentials  s  testpassw1valid
    Output Should Contain  Username must contain at least 3 characters from [a-z]

Register With Valid Username And Too Short Password
    Input Credentials  dummyuseri  pwrd
    Output Should Contain  Password min lenght is 8 and it should contain characters from [a-z] and atleast one symbol

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  dummyuseri  testtesttest 
    Output Should Contain  Password min lenght is 8 and it should contain characters from [a-z] and atleast one symbol

*** Keywords ***
Input New Command And Create User
    Input New Command 
    Create User  dummyuser  dummypassw1