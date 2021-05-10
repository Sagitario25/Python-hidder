<!-- TABLE OF CONTENTS -->
 <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
 <ol>
   <li>
     <a href="#about-the-project">About The Project</a>
     <ul>
       <li><a href="#built-with">Built With</a></li>
     </ul>
   </li>
   <li>
     <a href="#getting-started">Getting Started</a>
     <ul>
       <li><a href="#prerequisites">Prerequisites</a></li>
       <li><a href="#installation">Installation</a></li>
     </ul>
   </li>
   <li><a href="#usage">Usage</a></li>
   <li><a href="#acknowledgements">Acknowledgements</a></li>
 </ol>



<!-- ABOUT THE PROJECT -->
## About The Project

>If you are doing some code that needs to run in the background for whatever reason and you are running on windows, I have good news. An other way to say this is that this code code activates stealth mode on windows for educative purposes.
>
>### Built With
>>
>>* [Python](https://www.python.org/)
>>* [win32process](https://pypi.org/project/pywin/)



<!-- GETTING STARTED -->
## Getting Started

>Clone the repository or download and extract the zip file.
>
>### Prerequisites
>
>>For the installation you have to be using windows with python installed. Tested on windows 10 and python 3.8, it should work in other versions. Not using Windows isn't an option, as win32process won't run other ways.
>
>
>### Installation
>
>> Download
>>>```
>>>git clone https://github.com/Sagitario25/Python-hidder
>>>cd Python-hidder
>>>```
>>>If you don't like this way you can also download the zip, extract it and navigate to it in CMD.
>>
>>Install requirements
>>>```pip install requirements.txt```
>>
>> Move
>>> Just move ```hidder.py``` to the main directory of the program where you want to use.



<!-- USAGE EXAMPLES -->
## Usage

>Really simple use actually. e.g.:
>>```
>>import hidder
>>hidder.hide ()
>>```
>And just like that your window is hidden, or what is the same, your program is running on the background.
>```hidder.hide``` can recive a boolean argument, it's false by deafault, true will make it to ignore the windows blocker, but it assured the code will fail a bit later.
>
>
>I just added another method, now you can just open this file of the folder of the desired and I will import ```main.py``` and call ```main ()``` inside it. You might need to recode part of your project, but the method other is still available, so there is no need to use this one.


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [W.Leto](https://stackoverflow.com/a/49451756/13758800) - I used his code for this
