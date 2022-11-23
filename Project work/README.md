# Pitch estimation of a speech sequence

- This code uses Autocorelation of clipped-frames to estimate the pitch of the frame.
The fundamental frequency of a spoken signal is called pitch. More suitable definition of pitch is "Pitch is a perceptual property of sounds that allows their ordering on a frequency-related scale, or more commonly, pitch is the quality that makes it possible to judge sounds as *higher* and *lower* in the sense associated with musical melodies Pitch is a major auditory attribute of musical tones, along with duration, loudness, and timbre." . The goal of this project is to use auto-correlation to identify the pitch of a voiced speech frame. A discrete audio-sequence is divided into several overlapping frames, which then performs auto-correlation on each frame. The pitch estimation is derived from them. We first divide the audio signal into voiced and unvoiced samples based on its zero-crossing rate, and then apply our algorithm to it.

- This code works on an audio file in arctic dataset, which contains **Speech signal** in **Channel 1** and **EGG signal** of the same audio sequence in **Channel 2**
## Prerequisit packages
Run the following code in commandline to install prerequisits 
```
python3 pip install numpy scipy librosa matplotlib 
```
## Using the code
- Download the [Arctic data](https://github.com/imraunav/Programming-practicum-CS571/tree/main/Project%20work/arctic-20221111T144309Z-001/arctic)
- To change the audio file in action, change the **'path'** variable and the **'audioSelection'** variable in the script.
- Use the 'project_script.py' to see the simulation.

- Voiced-frames have been chosen using *Zero crossing rate* of a frame in the EGG signal. For a voiced-frame, the *ZCR* is very high, compared to unvoiced-frame. 
The code plots the **actual pitches** derived from the **EGG data** and the **estimated pitches** from the **Audio data** for each voiced-frame.

## Imperfection in the implementaion
- Fine tuning the threshold on the clipping of audio frame can improve removal of low energy noise.
- Tuning the threshold on zero-crossing rate to decide voiced frames can improve the positive voiced frames detection rate.
- Can be looked into a better peak-picking algorithm to remove false peak detection.
