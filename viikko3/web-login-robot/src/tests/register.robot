*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset App And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Title Should Be  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  s
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Page Should Contain  Username must contain at least 3 characters from [a-z]

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kal123
    Set Password Confirmation  kal123
    Click Button  Register
    Page Should Contain  Password min lenght is 8 and it should contain characters from [a-z] and atleast one symbol

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle122
    Click Button  Register
    Page Should Contain  Password do not match with Password confirmation
    
*** Keywords ***

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Reset App And Go To Register Page
    Reset Application
    Go To Register Page