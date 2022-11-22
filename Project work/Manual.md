# Pitch estimation of a speech sequence

This code uses Autocorelation of clipped-frames to estimate the pitch of the frame.
The fundamental frequency of a spoken signal is called pitch.More suitable definition of pitch is "Pitch is a perceptual property of sounds that allows their ordering on a frequency-related scale, or more commonly, pitch is the quality that makes it possible to judge sounds as *higher* and *lower* in the sense associated with musical melodies Pitch is a major auditory attribute of musical tones, along with duration, loudness, and timbre." . The goal of this project is to use the auto-correlation function to identify the pitch of spoken discrete speech. An discrete wave is divided into several overlapping frames by the method, which then performs auto-correlation on each frame. The pitch estimation is derived from them. We first divide the audio signal into voiced and unvoiced samples based on its energy content, and then apply our algorithm to it.

This code works on an audio file in arctic dataset, which contains **Speech signal** in **Channel 1** and **EGG signal** of the same audio sequence in **Channel 2**.

To change the audio file in action, change the path and the audiofile selection in the script.

Voiced-frames have been chosen using *Zero crossing rate* of a frame in the EGG signal. For a voiced-frame, the *ZCR* is very high, compared to unvoiced-frame. 
The code plots the **actual pitches** derived from the **EGG data** and the **estimated pitches** from the **Audio data** for each voiced-frame.