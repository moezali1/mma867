# MMA867 Predictive Modeling Labs

## Cloning the Repository and Installing Dependencies

1. **Install Anaconda:**

   - **Windows:**
     1. Download the Anaconda installer from the [Official Anaconda website](https://www.anaconda.com/products/distribution#download-section).
     2. Run the installer and follow the instructions.

   - **macOS:**
     1. Download the Anaconda installer for macOS from the [Official Anaconda website](https://www.anaconda.com/products/distribution#download-section).
     2. Open the downloaded .pkg file and follow the installation instructions.

   - **Linux:**
     1. Download the Anaconda installer for Linux from the [Official Anaconda website](https://www.anaconda.com/products/distribution#download-section).
     2. Open Terminal and navigate to the directory where the installer was downloaded.
     3. Run the installer using the command:
        ```
        bash Anaconda3-<version>-Linux-x86_64.sh
        ```
     4. Follow the instructions in the Terminal.

2. **Install Visual Studio Code (VS Code) [Optional]:**

   - Download and install Visual Studio Code from the [Official VS Code website](https://code.visualstudio.com/).

3. **Install Git (Windows Users Only):**

   - Download and install Git from the [Official Git website](https://git-scm.com/download/win).
   - Follow the installation instructions.

4. **Configure Git and Authenticate:**

   - After installing Git, open Git Bash or Command Prompt and configure your Git username and email. These details will be associated with your commits:
     ```
     git config --global user.name "Your Name"
     git config --global user.email "your.email@example.com"
     ```
   - To authenticate to GitHub, you can use a personal access token. Follow these steps:
     1. Generate a personal access token on GitHub by following the instructions [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).
     2. Use the token to authenticate when prompted during a Git operation like `git clone` or `git push`.

5. **Setup Conda Environment and Jupyter Kernel: [Optional]**

   - Open Terminal or Anaconda Prompt and create a new conda environment named `mma867` with the following command:
     ```
     conda create --name mma867 python=3.11
     ```
   - Activate the conda environment:
     ```
     conda activate mma867
     ```
   - Install Jupyter Notebook in the conda environment:
     ```
     conda install jupyter
     ```
   - Create a Jupyter kernel with the same name as the conda environment:
     ```
     python -m ipykernel install --user --name mma867 --display-name "mma867"
     ```
        *Last 2 steps are not needed if you are using VS Code.*

1. **Clone the Repository:**

   - Use the following command to clone the repository to your local machine:
     ```
     git clone https://github.com/moezali1/mma867.git
     ```
   - This command downloads the repository and its contents into a new folder named `mma867` in the current directory.

2. **Navigate to the Repository Folder:**

   - Change your current directory to the newly cloned repository by running:
     ```
     cd mma867
     ```

3. **Install Required Libraries:**

   - Now, install all the required libraries isted in the `requirements.txt` file using pip. Make sure you have Python and pip installed on your system. Run the following command:
     ```
     pip install -r requirements.txt
     ```
   - This command reads the `requirements.txt` file in the current directory and installs all the libraries listed there.

## Data
For labs where data file is needed, the data is stored as a csv file and is stored in the respective folder. For example data needed for Session 1 is in Session 1 folder.
