import os
import random

def makeCommits(days: int):
    # Clear the data.txt file before starting a new series of commits
    open('data.txt', 'w').close()

    if days < 1:
        os.system('git push')
    else:
        dates = f"{days} days ago"
        # Generate a random number of commits between 0 and 22
        num_commits = random.randint(0, 22)
        with open('data.txt', 'a') as file:
            for _ in range(num_commits):
                file.write(f'{dates} <- this was the commit for the day!!\n')
        
        # staging 
        os.system('git add data.txt')

        # commit 
        os.system('git commit --date="' + dates + '" -m "First commit for the day!"')

        return days * makeCommits(days - 1)

makeCommits(14)
