# UMD Class Sign up Automating

This is a spam bot using `Selenium` Browser Automation. It is always a struggle for UMD students to navigate the Registration website on the day that they have to sign up for classes. This has it so that they just input classes and section numbers that they want into the arrays and the bot will take care of the rest. The only other time that a user will have to interact with the bot is when the bot asks which term the user is trying to sign up for. There will always be at least one option for which term to sign up for, and to make it easier for the user, the user just enters a number corresponding to the index of the term in the array. This requires some dependances to run. 

## MacOS Installation
- `pip install selenium`
- `sudo mv -f chromedriver /usr/local/bin/chromedriver` 

- This installs the selenium package and the driver to use it on google chrome. Visit [here](https://www.selenium.dev/downloads/) to decide which package best serves your needs. 

# Windows Installation
- Install python [here](https://www.python.org/downloads/windows/)
- Open the command prompt for python and run `pip.exe install selenium` in the console.
- User the same link above to install the package and driver that suits your needs.


Still a work in progess, I happily welcome Pull Requests with ways this can be made better!