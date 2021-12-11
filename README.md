<b> Questions </b>

*1.Please explain Big-O notation in simple terms.*

I spent some time grasping this concept as I only heard-of this, but never really had good knowledge about it.
Big O notation is a mathematics concept that is used to determine how fast or slow an algorithmic function will perform.
based on the maximum input. The growth order is denoted from O(1) which is the fastest of the Big O time complexities to
O(2**n) which is the slowest.

----
*2. What are the most important things to look for when reviewing another team member's code?*

I think alot of it depends on experience of the team members and backgrounds they come from, but for the most part 
1. Check for syntax and logic errors which might immediately break the code.
2. Check for python coding standards naming, spacing etc
3. Hard to always do this but getting a general idea what the code is doing.
4. Look for measures to catch Exceptions and errors
5. Check for code efficiency and scope for simplification
----

*3.Describe a recent interaction with someone who was non-technical.
    What did you need to communicate and how did you do it?*

I recently had a talk with an Anim supervisor in order to explain an extra step of validation we were adding to fix
characters in the scene. Usually Animators update the character rigs in the scene before working on them. Recently this
was failing due to some broken rigs with missing sub-components being passed on. I communicated over a voice informing
why updating characters in the scene was failing, what were our options available to fix scenes with broken characters
and in the end what we decided to go with. I explained to them that a validation (extra_step) will be introduced if the
fix(tool) will pop up instead of the sceneUpdater if broken-rigs are found. I gave them a viusal tutorial along with
written steps and limitation of the tool.