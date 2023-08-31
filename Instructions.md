# P2: Concurrent Processing & Shared Resources
- Due Friday by 11:59pm 
- Points 20 
- Submitting a text entry box 
- Available until Oct 3 at 11:59pm

In this project, we'll look at what happens with concurrent processes are accessing a shared resource.  A shared resource could be a SQLite database, a queue (first-in, first-out, like a grocery store line), a deque ("deck") if working with sliding time windows (which we'll do later), an office printer, or more. 

## Tasks:

1. You'll review how one multiprocessing example when tasks are quick and sharing goes well (generally).
2. You'll change to longer-running concurrent tasks and explore what happens. 
3. You'll implement a scaffolded process that streams from a csv file. 
4. You'll write your own streaming process that reads from a unique data source 

## Every module:

1. run about.py to generate an about.txt.
2. Customize your README.md to reflect the focus, add your name and notes. 
3. Customize and comment your code as recommended by the Python Style GuideLinks to an external site..
4. Demonstrate your project and communication skills. 
---
### Notes on multiprocessing. In streaming, we often have multiple processes running concurrently (search this term as needed).
- In this example, we run all processes in a single terminal window using the multiprocessing package from the Python standard library.
- In later assignments, we'll start up different terminal windows for different applications. Learn both for maximum benefit.
- When running multiple terminals (later), you can use the integrated terminal in VS Code, or in Terminal (on a Mac), or in Anaconda Prompt (in Windows). Explore the options see what works best for you. 
---
### Module Repo - Read the code and comments carefully

https://github.com/denisecase/streaming-02-multiple-processesLinks to an external site.
### Additional resources:
- Module 0: Course Text
- Streaming and Sockets
- Module 0: FAQ
### General Approach (Same as usual - soon you'll create these without a starter repo)
1. Fork the repo into your GitHub account
2. Clone your new repo down to your local machine 
3. Execute the code 
4. Read the code and comments carefully
5. Modify the examples as requested
6. Document your results - don't forget this key step! 
7. Commit and push / sync your changes back up to GitHub
### Managing Your Fork
- See Managing Your Fork for more.
---
# Concurrent Multiprocessing

## Task 1. 
Explore the output from concurrent processes. Were activities performed in a in order? Does the order vary on multiple runs? What would happen if a process - or machine - dies? Is information lost? These considerations are important when deciding how to implement distributed analytics solutions. 

## Task 2. 
Increase the time and see how things go? What happens? 

# Stream Processing 

## Task 3. 
Stream processing is different because the data is unbound - it could be infinite. Think tweets being generated in real time, or sensor data, like GPS, temperature, stocks, or web analytics. These are examples of "data in motion".
- copy process_streaming_0.py from the Module 1 repo.
- copy the other file you need to make it work. Hint: read the code. Look for the name of another (data) file to read from.

This will simulate an infinite source of information, process it, and output a continuous steam of information. If all goes well - it will run for quite a while. Many processes run continuously until a failure occurs or the user stops the process by shutting it down, or interrupting it with Cnrl c or Control C (to close).  See the Module 0: FAQ for more help. 

## Task 4:
- Stream your own unique CSV data by modifying the example approach provided.
- Create a new file process_streaming_yourname.py
Stream from your CSV file into a new file named out9.txt.
- Use the examples provided as the basis for your implementation. 
- Generate one record every 1-3 seconds. Let it run long enough to write ten or more records to out9.txt.
    - For the output file, either open a file for writing and have your code write to the file - or you can manually copy and paste into the output file.
    -  Let us know which option you chose and why in your submission.
### Optional. 
After successfully completing your implementation of the example code on your own datafile, then you may copy your working code into another file (process_streaming_yourname99.py) and send the output to out99.txt (which should match out9.txt above). 

- What changes when you read from a different csv file? 
    - See Hint here: https://github.com/denisecase/streaming-01-getting-started/blob/main/process_streaming_0.py#L50

## Task 5:

Python offers two types of sockets in the standard socket library. 
- The UDP datagrams we used are the easiest - just chunk it up and send. 
- The TCP protocol is more widely used. To learn more about the TCP protocol, see the quiz this module and do a bit of searching.
- You want to (a) be aware of UDP vs TCP and (b) be able to read and understand a project using either. 

Learning libraries and packages are why companies ask for years of experience in a language. The language syntax takes only hours or days to learn, but becoming aware of all the free libraries available can take many years. Learning how to learn the ones you need is an important skill.

---
### Reflection (on your own)
Shared resources don't necessarily ensure that things are processed in the order they were created. If we forget to close a file, we can have it bound to one process, causing another processes to have to wait for access, and if these happens enough (processes waiting on each other and not being able to continue), we can get into deadlock where progress stalls completely.

How could deadlock be avoided?

Suggestion: 
Rather than remembering to close() a resource, always use the "with open() as f:" syntax so resources are automatically dropped when the code block finishes. 

---
## Part 3 - Self Review

Ensure you have a compliant submission. Confirm each item before you submit.

1. Your link is clickable.
2. Your link points to your forked repo as instructed.
3. You've pasted the learning objectives and assessed each on individually,
4. Your README.md is complete, correct, professional and meets requirements.
5. No files have <<<<<<<< or >>>>>>>>> (these are common when merging two versions - just clean them up.)
6. All correctly-named scripts are included in the correctly-named repo along with required, correctly-named, documentation files verifying the results.
7. You have read and used the code examples provided.

---
# Grading Rubric 
 44671-P2

## Criteria	
1. Complete, correct
Links visible and clickable, all requirements met, code is correct, well-organized, well presented.
    - 16 pts: Full Marks / Submission correct.
    - 14 pts: Mostly correct and complete
    - 12 pts: Several items missing or incorrect
    - 0 pts: No Marks / Missing or incorrect
2. On-time, professional submission
    - 4 pts: Completed expectations before the assigned due date.
    - 3 pts: Minimal additional time/revisions required. Completed expectations with minimal additional time, revisions, or other assistance.
    - 2 pts:
Significant additional time/revisions required. Completed expectations with significant additional time or revisions required.
    - 0 pts: No marks. Missing or incorrect
3. Bonus (10%) optional
    - 2 pts: Max 10% bonus
    - 1 pts: 5% bonus
    - 0 pts: No Marks
## Total Points: 22
