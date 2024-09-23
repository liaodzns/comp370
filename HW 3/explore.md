- How big is the dataset?

Using `wc` there are: 
    36,860 lines of data 
    705,400 words
    4,896,994 characters

- What’s the structure of the data? (i.e., what are the field and what are values in them)

Title, writer, dialog, pony

As the title and author stay the same, each line for each episode is separated by the current pony speaking at the moment -> which updates the dialog for the line in data

- How many episodes does it cover?

There are 197 episodes 

- During the exploration phase, find at least one aspect of the dataset that is unexpected – meaning that it seems like it could create issues for later analysis.

In terms of uniformity, there are some dialog entries that contain a space before the dialog text, while others don't. This could be a issue when parsing.

When splitting entries based on commas, there are titles that contain commas too. 
On that same note, when splitting entries by quotations, there are dialog entries that contain quotations inside as well.


2036/36859 fluttershy - 0.0552

2746/36859 pinkie pie - 0.0745

2978/36859 rainbow dash 0.0807

2532/36859 rarity - 0.0687

4562/36859 twilight sparkle - 0.1238