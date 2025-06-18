### INSTRUCTIONS

0. These instructions are based on the instructions from CarbonCast's src/weather README. Refer to their link if you are running into issues (https://github.com/carbonfirst/CarbonCast/tree/v3.1/src/weather). These instructions worked for me on a Linux server, didn't work on my M1 laptop. Also, each downloaded file will be ~1GB file, so make sure you have space. 
1. Register on the GFS weather forecast archive (https://rda.ucar.edu/datasets/d084001/). I signed in using Globus with my UCSC account, but use whatever method works (https://rda.ucar.edu/datasets/d084001/).
2. Clone the rda-app-client repo (https://github.com/NCAR/rda-apps-clients) and follow their installation process and run their test programs. You want to use their python client, which will have an initial authentication process but should save your details in a file so you don't have to re-auth for every API call.
3. Copy all the python files in this repo into the rda-apps-client/src/python files. Also copy over the control_files/ folder into rda-apps-client/src folder. 
4. Choose a particular location with the spreadsheet below. NOTE: Each location has four files each, please submit all four together. Then write these files into the array in "upload_files.py". You will get emails that a file is ready to upload, NOTE that this file will only be available for 5 days. 
5. Please run the "download_files.py" code whenever you have a file ready to download. Everytime you run "download_files.py" please remove the older files so there aren't any overlaps. "download_files.py" will print a dictionary that pairs each (location, parameter) to a file name. Once you have downloaded all your files, add the files and the text file (rda_downloaded_files.txt) that explains what each file means in a zip and email it to me (manjosep@ucsc.edu).
6. Once you have downloaded all 8 files, run the "purge_files.py" file to clear all the requests and then choose another location to upload files for. 


Here is the spreadsheet where you can mark which locations you have submitted for. The limit for pending requests are 10, so I would recommend doing 2 locations at a time, so you will end up doing 8 requests since each location has 4 files. Login with your UCSC account and follow the spreadsheet format. 
https://docs.google.com/spreadsheets/d/1jh-Vf3s_ii-CQW6yw2f6fLUf8SjnH18ZSZ9Yj_fjiq0/edit?usp=sharing


If you have any questions, feel free to email me too. 