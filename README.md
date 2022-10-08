# yt-video-list-getter

I made this to help search within the members only videos of a  youtube channel, since youtube currently provides no way to search within them.

### How I get the list
Open Membership tab (must be logged in to an authorised account)
Open Network tab in Inspector and filter by "browse"
Refresh page and scroll all the way down or as far as you want to include
Make sure entire timeline is selected
Right click on one of the browse? files and select "Save all as HAR with content"
Save file and change extension from .har to .txt
Put into correct folder and change name to "concat-list1"/change file path in .py file
Create output5.csv file
Run .py script
Open spreadsheet & find and replace "\\\" with nothing (use "\\\\\" to find)
