import os
import random
from datetime import datetime, timedelta


def cleanUpFiles():
    # Get all files that match the pattern "data_*.txt"
    for filename in os.listdir('.'):
        if filename.startswith('data_') and filename.endswith('.txt'):
            os.remove(filename)


def makeCommits(days: int):
    if days < 1:
        # Push all commits to the repository after all commits are made
        os.system('git push')
    else:
        # Set the base date for the commits
        base_date = datetime.now() - timedelta(days=days)

        # Generate a random number of commits between 0 and 22 (inclusive)
        num_commits = random.randint(0, 22)

        for i in range(num_commits):
            # Create a unique commit time for each commit
            commit_time = base_date + timedelta(minutes=i * 10)
            commit_date = commit_time.strftime('%Y-%m-%d %H:%M:%S')

            # Create a unique file for each commit to ensure unique changes
            filename = f'data_{days}_{i}.txt'
            with open(filename, 'w') as file:
                file.write(f'{commit_date} <- this is commit #{i + 1} for day {days}!\n')

            # Stage the new file
            os.system(f'git add {filename}')

            # Make the commit with the specific date and unique message
            os.system(f'git commit --date="{commit_date}" -m "Random commit #{i + 1} for day {days}!"')

        # Recursive call to handle the previous day
        makeCommits(days - 1)


# Start the process with X days
makeCommits(30)

# Clean up files after all commits are done
cleanUpFiles()
