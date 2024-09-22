import os
import random


def makeCommits(days: int):
    # Clear the data.txt file before starting a new series of commits
    open('data.txt', 'w').close()

    if days < 1:
        # If no more days left, push all commits to the repository
        os.system('git push')
    else:
        dates = f"{days} days ago"
        # Generate a random number of commits between 0 and 22 (inclusive)
        num_commits = random.randint(0, 22)

        if num_commits > 0:
            # If there are commits to make, write dummy data into the file
            with open('data.txt', 'a') as file:
                for _ in range(num_commits):
                    file.write(f'{dates} <- this was the commit for the day!!\n')

            # Stage the file to prepare for the commit
            os.system('git add data.txt')

            # Make the specified number of commits with the same date
            for _ in range(num_commits):
                os.system(f'git commit --date="{dates}" -m "Random commit!"')

        # Recursive call to handle the previous day
        makeCommits(days - 1)


# Start the process with 23 days
makeCommits(15)
