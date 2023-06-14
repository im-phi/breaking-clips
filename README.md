# breaking-clips

Clips your breaking files for you 

<!-- ## Description

An in-depth paragraph about your project and overview of use.

## Getting Started

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
``` -->

## Help

Sort your videos in order by name
Then you will record which video, start time, end time, and name of move/combo for your clip
Each line of input text must follow this format
```
"{videoIndex} - {startTime} {endTime} {moveName}"
	where : 
		videoIndex 	is an 	int
		startTime 	is in 	"mss" format
		endTime 	is in 	"mss" format
		moveName 	is a 	string

		videoIndex is required for one initial line. If the next line clips from the same video,
			videoIndex will be optional.
		
	    mss format may look more familiar converted to different formats e.g.
			mss		455
			m:ss	4:55
			mm:ss	04:55

			this means breaking-clips doesn't clip videos past 10min for now 
			(it's because I don't use it lol)

	Example Input :
		5 - 151 204 ***Braid
		515 603 **Pedestrian Step > Tippy Taps > Bingo Steps > 7Step > No Hands 6Step
		6 - 245 256 ***No Hands 6Step + Back Rolls
		653 728 **Pedestrian Step > Stompies(?) > Uncrossed Back Shuffle > misc fw
		7 - 206 227 misc fw > No Hands 6Step > Hand Swipes
		8 - 230 313 Floor Palms > Telewide

		Explanation: 
			5 - 151 204 ***Braid 
			- In my 5th video, this will take a clip from 1:51 to 2:04 
				and name the file "Braid"

			515 603 **Pedestrian Step > Tippy Taps > Bingo Steps > 7Step > No Hands 6Step
			- In my 5th video, this will take a clip from 5:15 to 6:03
				and name the file... that entire string after lol

```

<!-- ## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release -->