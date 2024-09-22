import os
import random
from datetime import datetime, timedelta


def makeCommits(days: int):
    # Clear the data.txt file before starting a new series of commits
    open('data.txt', 'w').close()

    if days < 1:
        # If no more days left, push all commits to the repository
        os.system('git push')
    else:
        # Set the base date for the commits
        base_date = datetime.now() - timedelta(days=days)

        # Generate a random number of commits between 0 and 22 (inclusive)
        num_commits = random.randint(0, 22)

        if num_commits > 0:
            with open('data.txt', 'a') as file:
                for i in range(num_commits):
                    file.write(f'{base_date} <- this was the commit #{i + 1} for the day!!\n')

            # Stage the file to prepare for the commit
            os.system('git add data.txt')

            for i in range(num_commits):
                # Create a unique commit time for each commit
                commit_time = base_date + timedelta(minutes=i * 10)
                commit_date = commit_time.strftime('%Y-%m-%d %H:%M:%S')

                # Make the commit with the specific date and unique message
                os.system(f'git commit --date="{commit_date}" -m "Random commit #{i + 1}!"')

        # Recursive call to handle the previous day
        makeCommits(days - 1)


# Start the process with 23 days
makeCommits(15)
