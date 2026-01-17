from operator import itemgetter
import requests
import matplotlib.pyplot as plt
import textwrap

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        "title": response_dict["title"],
        "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
        "comments": response_dict.get("descendants", 0),  # Use get() to handle missing descendants
    }
    submission_dicts.append(submission_dict)

# Sort submissions by number of comments in descending order
submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

# Prepare data for plotting
titles = [dict["title"] for dict in submission_dicts]
comments = [dict["comments"] for dict in submission_dicts]
links = [dict["hn_link"] for dict in submission_dicts]

# Create bar chart
plt.figure(figsize=(12, 8))
bars = plt.bar(range(len(titles)), comments, color='skyblue')

# Customize the plot
plt.title('Most Active Discussions on Hacker News', fontsize=14, pad=20)
plt.xlabel('Submissions', fontsize=12)
plt.ylabel('Number of Comments', fontsize=12)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Wrap titles to prevent overlap and add as labels
for i, bar in enumerate(bars):
    wrapped_title = '\n'.join(textwrap.wrap(titles[i], 20))  # Wrap title to 20 characters
    plt.text(bar.get_x() + bar.get_width()/2, -10, wrapped_title, 
             ha='center', va='top', fontsize=10, wrap=True, rotation=0)
    # Note: Links are included in the data but not directly clickable in matplotlib image output

# Adjust layout to prevent label cutoff
plt.tight_layout()
plt.subplots_adjust(bottom=0.3)  # Add space for wrapped labels

# Save the plot
plt.savefig('hn_active_discussions.png')