# brain-doesnt-lie
My repository for a research project titled : Estimating User Engagement Statistics for Online Videos Using EEG Signals. The project is based on Brain Computing Interfaces and captures EEG signals through a non-invasive BCI device Emotiv Insight using Cortex API. Scroll Down for Project description. I also wrote an ACM Late Breaking Works paper (not published) in the CHI2020 Extended Abstract Format.

The study on user engagement for online videos is interesting
as the number of online videos is growing exponentially.
There are multiple videos available for a single topic with
varying presentation and thus have different levels of user
engagement. This paper primarily focuses on the study to
identify patterns in user engagement while watching some
videos gathered from online resources. The aim is to identify
the segments of recorded video that cause a change
in engagement of the user watching the video using a passive
brain computer interface. This study allows us to get
insights on where the dip or rise in user engagement occurs
while watching a video. The insights gathered may
further help the creators/producers of the media to better
assess the content and modify them accordingly to make
them more engaging.

The project folder contains three subfolders-
1)	datasets – It contains raw data of all 6 participants collected through user study.
2)	Python Files – Contains python scripts for data collection and data analysis.
3)	graphs – It is an empty folder where graphs (results) will be created when python script data_analysis.py will be run.

Python files and their description – 
1)	data_collection_ alpha_calibration.py –  To collect alpha calibration or relaxation values for all the participants.
2)	data_collection_video1.py – To collect EEG data for all participants while they watched video 1.
3)	data_collection_video2.py – To collect EEG data for all participants while they watched video 2.
4)	data_collection_video3.py – To collect EEG data for all participants while they watched video 3.
5)	data_analysis.py – To load the datasets, process it, calculate engagement and plot graphs. 


To run the python scripts,  file path needs to be changed. It has been indicated in the form of comments in the code.


The Videos used in this project were TED videos chosen from the playlist which can be found at : https://www.youtube.com/playlist?list=PLOGi5-fAu8bHMsH_8DihgDF9g7GVeFGwW

For My project,
Video 1 was - How the Hyperlink changed everything
Video 2 was - How the Buttons changed fashion
Video 3 was - The hidden way Stairs change our lives
