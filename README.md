# Ohbot for Python (Windows Version)

<a href="http://whoosh.co.uk/ohbothelp/images/eyes.gif" target="_blank"><img src="http://whoosh.co.uk/ohbothelp/images/eyes.gif" border="0" width = "30%"/></a>


Background
-----

These instructions allow you to program your Ohbot using Python on a Windows PC.

More information about Ohbot can be found on [ohbot.co.uk.](http://www.ohbot.co.uk)


Setup
--------

Install the latest version of Python from [here.](https://www.python.org/downloads/release/python-364/)


<a href="https://github.com/ohbot/ohbotWin-python/blob/master/images/image1-22.png" target="_blank"><img src="https://github.com/ohbot/ohbotWin-python/blob/master/images/image1-22.png" border="0" width = "80%"/></a>

We chose version 3.6 Windows x86-64 executable installer.

During the Install make sure that the pip option is selected

Once install is complete type “Command” into the Windows search box.  Right click on <b>Command Prompt </b> and select <b>Run as administrator.</b>

<br>

<a href="https://github.com/ohbot/ohbotWin-python/blob/master/images/image2-24.tif" target="_blank"><img src="https://github.com/ohbot/ohbotWin-python/blob/master/images/image2-24.tif" border="0" width = "35%"/></a>

<br>

This will open a command prompt window. 

Type the folloing:

``pip install ohbotWin``


Installing more voices (optional)
--------

The Ohbot Python library will default to using SAPI voices which are the voices that are available through Windows Control Panel:Speech Propeties.

You can change this to espeak or espeak-ng by calling ohbot.setSynthesiser (“espeak”) or ohbot.setSynthesizer (“espeak-ng”).

Install the espeak library from [here.](http://espeak.sourceforge.net/download.html)


Install espeak and then copy the espeak.exe file in Windows File Explorer from 

C:\Program Files (x86)\eSpeak\command_line

To 

C:\Program Files\Python36

To use the espeak-ng library install it from [here.](https://github.com/espeak-ng/espeak-ng#binaries)

Install espeak-ng and then copy the espeak-ng.exe and espeak-ng.dll files in Windows File Explorer from 

C:\Program Files\eSpeak NG

To 

C:\Program Files\Python36

That should be it for the setup.

Dependencies
----------

The ``pip install ohbotWin`` command will install the following libraries:


| Library    | Use         | Terminal command to install  |Link |
| ---------- |-------------| -----------------------------|-----|
| ohbotWin   | Interface with Ohbot          | ```pip install ohbotWin```  |[ohbot](https://github.com/ohbot/ohbotWin-python/) |
| serial    | Communicate with serial port| ```pip install pyserial```  |[pyserial](https://github.com/pyserial/pyserial/) |
| lxml    | Import settings file          | ```pip install lxml```  |[lxml](https://github.com/lxml/lxml) |
| comtypes    | Required for serial communication      | ```pip install comtypes```  |[lxml](https://github.com/lxml/lxml) |


To upgrade to the latest version of the library run the following in the console:
```pip install ohbotWin -- upgrade```



Ohbot library files (these will be installed with the `pip install ohbotWin` command above):

| File    | Use         |
| ---------- |------------|
| ohbot.py   | Ohbot package |
| MotorDefinionsv21.omd    | Motor settings file |

_Note: The text to speech module will generate an audio file, ‘ohbotspeech.wav’ and a text file ‘phonemes.txt’ inside your working folder._

---

Hardware
-----

Required:


* PC Running Windows.
* Ohbot
* USB Y Cable
* USB Power Socket Adaptor
* Speakers/headphones.


Setup:


Plug the middle of USB Y cable into the PC and the other large USB plug into the power adaptor. Then plug the mini USB into Ohbot.

---

Starting Python Programs
--------

Go to the Windows Menu and run IDLE from the Python folder:


<a href="https://github.com/ohbot/ohbotWin-python/blob/master/images/image3-26.tif" target="_blank"><img src="https://github.com/ohbot/ohbotWin-python/blob/master/images/image3-26.tif" border="0" width = "35%"/></a>


Select <b>New</b> from the <b>File menu.</b>

Go to the [hellworldohbot](https://github.com/ohbot/ohbotWin-python/blob/master/examples/helloworldohbot.py) example on Github


Copy the code and paste it into the new Python window.

Select <b>Run Module</b> from the <b>Run</b> menu.

Ohbot should speak and move.


Functions
-------

ohbot.init(portName)
----------

Called internally looking for a port with name containing "USB Serial Device" but if your port is different you can call it and override this port name. It returns True if the port is found and opened successfully, otherwise it returns false. This is likely with a versions of Windows in languages other than English. 

ohbot.move(m, pos, speed=3)
----------


| Name| Range| Description | Default |
| --- |------|-------------|---------|
| m   | 0-6 (int)  | Motor Number| - |
| pos | 0-10 (int)  | Desired Position| - |
| speed | 0-10 (int) | Motor Speed| 3 |


For Example:
```python
ohbot.move(1,7)
```
or
```python
ohbot.move(2,3,1) 
```
or you can use a constant from the library to specify the motor:
```python
ohbot.move(ohbot.EYETURN,3,1) 
```
Motor index reference:

| m | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| ----| --- | --- |  --- |  --- |  --- |  --- |  --- |
| constant | HEADNOD | HEADTURN | EYETURN | LIDBLINK | TOPLIP | BOTTOMLIP | EYETILT | 
  

ohbot.say(text, untilDone=True, lipSync=True, hdmiAudio=False, soundDelay=0)
----------

| Name| Range| Description | Default |
| --- |------|-------------|---------|
| text   | 'A string with no punctuation'  | Words to say| - |
| untilDone | bool  | Return when finished speaking| True |
| lipSync | bool | Move lips in time with speech| True |
| hdmiAudio | bool | Fixes missing start of phrase when HDMI audio output is being used| False |
| soundDelay | float | Set to positive if lip movement is lagging behind sound and negative if sound is lagging behind lip movement| 0 |



For Example:
```python
ohbot.say('Hello I am Ohbot')

ohbot.say('Goodbye',False,False)

ohbot.say('Goodbye',False,False,True)

ohbot.say('Goodbye',soundDelay = 0.3)
```
---

ohbot.wait(seconds)
----------

Seconds - float or int required wait time. ohbot.wait(1.5)

| Name| Range| Description  |
| --- |------|-------------|
| seconds   | float or int  | Length of wait in seconds|



For Example:
```python
ohbot.wait(2)

ohbot.wait(0.5)
```

*Note: It is important to use ohbot.wait() commands between motor sequential commands for the same motor.*

For Example:
```python
ohbot.move(1,7,2)

ohbot.wait(2)

ohbot.move(1,4,2)
```
---

ohbot.eyeColour(r, g, b, swapRandG=False)
----------

Set the colour of Ohbot’s eyes. 

| Name| Range| Description  | Default |
| ---      |------|-------------| ------- |
| r        | 0-10 (int)  | Red| - |
| g        | 0-10 (int)  | Green| - |
| b        | 0-10 (int)  | Blue| - |
| swapRandG| bool | swap r and g value for some older Ohbots | False |


For Example:
```python
ohbot.eyeColour(2,3,8)
```
or 
```python
ohbot.eyeColour(2,3,8,True)
```

---

ohbot.reset()
----------

Resets Ohbot’s motors back to rest positions and turns off Ohbot’s eyes. Useful to start programs with this. You may need an ohbot.wait() after this to give time for the motors to move. 

For Example:
```python
ohbot.reset()
ohbot.move(1,7,2)
ohbot.wait(1)
ohbot.move(1,1)
...
```
---

ohbot.close()
----------

Call to detach all Ohbot’s motors which stops them using power, you can call ohbot.attach(m) or ohbot.detach(m) for individual motors.

For Example:
```python
ohbot.move(1,7,2)
ohbot.wait(1)
ohbot.move(1,1)

ohbot.close()
```
---

ohbot.readSensor(sensorNumber)
----------

Seconds - float or int required wait time. ohbot.wait(1.5)

| Name| Range| Description  |
| --- |------|-------------|
| sensorNumber   | 0-6 (int) | the pin the sensor is connected to |

returns the value as a float 0 - 10.

For Example:
```python
reading = ohbot.readSensor(3)

ohbot.move(ohbot.HEADTURN, reading)

```
ohbot.setSynthesizer(synth)
----------

Use ohbot.setSynthesizer (“sapi”) to use SAPI speech<br>
Use ohbot.setSynthesizer (“espeak-ng”) to espeak-ng speech<br>
Use ohbot.setSynthesizer (“espeak”) to use espeak speech<br>

Note that the SAPI speech uses the voices available in Control Panel:Text to Speech.   It can’t use Cortana voices.

Use ohbot.setVoice() to set the voice depending on the synthesizer:

ohbot.setVoice(voice)
------


<b>Using SAPI</b>

Use any of the following arguments:

| Name| Description|
| --- |------|
| -a0 to -a100   | amplitude |
| -r-10 to r10   | rate |
| -v any part of the name of a SAPI voice (eg. -vHazel or -vZira) | voice |

e.g. ``-a82 -r12 -vzira``<br>

<b>Using ESPEAK</b>

http://espeak.sourceforge.net/commands.html<br>

| Name| Description|
| --- |------|
| -v followed by a letter code|look in program files\espeak\espeak-data\voices to see what's available|
| +m1 to +m7   | male voices |
| +f1 to +f4   | remale voices |
| +croak or +whisper   | tone |
| -a0 - -a200   | amplitude |
| -s80 - -s500   | speed |
| -p0 - -p99   | pitch |

e.g.'-ven+croak' for English croaky voice or '-vzh+m2 -s26' for fast Chinese male.<br>



<b>Using ESPEAK-NG</b>

supports some of the ESPEAK parameters but some are missing.



