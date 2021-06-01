# Instructions
To install this project on your local machine and get it running in its own virtual environment, please follow the steps below:

1. Create a new project folder to run this application

2. You can get the files into your project folder a number of ways:

    a. Clone the GitHub repository - just click the green "Code" button on the page for the command. You can do this via HTTPS or GitHub CLI.

    b. Alternatively, you can download the ZIP file to your local machine, unzip and then copy the files over to the project folder you created in ***Step 1***.

3. This code is set to launch with Google Chrome so we will need to download the version of the [Chrome WebDriver](https://chromedriver.chromium.org/downloads) that is compatible with your version of Google Chrome.

4. To check your version of Chrome:
    - Click the 3 vertical dots on the right of the profile icon - next to the address/url bar.
    - Scroll down to where it says "Help" and then select "About Google Chrome"
    - Once you see the version of Chrome, [click here](https://chromedriver.chromium.org/downloads) to download the corresponding version of webDriver.
    - When you see the version that matches your browser, click on it to see the ZIP files. 
    - Download the one that matches your operating system, unzip it and add it to the root of this project folder along with the other files.

5. Make sure you have `Python3`, `pip`, and `pipenv` installed

    a. Depending on your OS, open a Command/PowerShell or Terminal window on your computer and run the command `python --version`. You should get an output like `Python 3.x.x` or `Python 2.x.x`.

    b. If you do not have Python3 installed, please [follow these instructions](https://docs.python-guide.org/starting/installation/)

    c. By the time you've completed the previous step, you should now have a version of `Python 3` and `pip` installed on your local machine.

    d. Next we'll install `pipenv`. You should be able to just execute the following command `pip install --user pipenv`. However, if that doesn't work, please refer to [this guide](https://docs.python-guide.org/dev/virtualenvs/#virtualenvironments-ref). Once you're able to install pipenv successfully, we're ready to begin.

    e. If you're installing on Windows 10, you might run into a warning asking you to add some of the `pipenv` executables to PATH. Check out this [helpful guide](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/) to learn how to add to the PATH.

## Using pipenv in your project

- From this point forward, we will have no further use for the `pip` command.

- Always run the `pipenv` commands from the root of your project directory. If you run it from anywhere else, it will setup a new environment there.

- To find the location of your virtual environment, run `pipenv --venv`.

- To install packages you only need in dev use `pipenv install <package_name> --dev`

- To uninstall a package use `pipenv uninstall <package_name>`

- Should your environment ever get messy and you need to refresh, use `pipenv --rm` to destroy the current and follow the steps below to create a new one. 

## Create the virtual environment

Ordinarily, you should be able to install your virtual environment and packges in one command `pipenv install --ignore-pipfile`. However, if your version of Python differs from what's in the Pipfile, you may run into issues. So I'll break it down step by step below.

### Take Note!
 You may come across a warning message that says your version of Python may be different from the package requirement. To avoid this, delete the Pipfile from the root directory of your project before running the `pipenv --three` command. 

1. From the root directory of your project, create a virtual environment by running `pipenv --three`. This creates a virtual environment with your version of Python 3. It also creates a **Pipfile** in your project directory that holds the requirements.

2. There are a couple of packages required here and that's **selenium** and **pytest**. So run the command `pipenv install selenium pytest`. It will install the packages and their dependencies in the environment and add it to the **Pipfile**. 

3. When the command is complete, you should see a success message followed by the location of the environment, and the command on how to activate it.

4. Activate the virtual environment by running `pipenv shell`.

## To run the code

1. Before we run the code, we need to make an edit to `main.py`. We need to set the path of the webDriver executable on line 23. Earlier we downloaded it and added it to the root of this project folder so now we change the value of the`executable_path` parameter. See options below. Remember to include either single or double quotes. 
    - Windows OS: `./chromedriver.exe`
    - Linux or MacOS: `./chromedriver`


2. Run the application with `pipenv run pytest main.py -v`

3. When execution completes, you can shutdown the virtual environment with:

    a. `exit` - this only temporarily closes the subshell. Should you wish to return, just run the `pipenv shell` command again to re-launch.

    b. `pipenv --rm` this will destroy the virtual environment altogether.

