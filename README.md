# Wikipedia Research Assistant 🔎

A Python-based research assistant that uses Wikipedia’s API to quickly retrieve information about unfamiliar topics and suggest related areas to explore.

The idea was simple: enter a topic, let the program search Wikipedia, get a short summary, and then see what related topics might be worth exploring next.

## What it does

- Searches Wikipedia for a topic
- Retrieves a short summary
- Shows related topics to explore
- Handles searches with no useful results
- Runs directly from the terminal

## Example

```text
🔎 Welcome to the Wikipedia Research Assistant!

Enter a topic to search (or type 'exit' to quit): Albert Einstein

📚 Summary of 'Albert Einstein':

Albert Einstein was a German-born theoretical physicist...
## How it works

The program uses Wikipedia's API to search for topics and retrieve article information. The results are then processed and displayed through a simple command-line interface.

The project currently uses Python and the `requests` library to communicate with the API.

## Running the project

Install the required package using:

pip install -r requirements.txt

Then run the program using:

python research_assistant.py

Enter a topic when prompted. Type `exit` when you want to stop the program.

## Why I built it

I wanted to build something that was actually useful to me while learning Python instead of only writing small programs to practice individual concepts.

This project gave me a chance to work with APIs, HTTP requests, user input, loops, functions, and error handling in one project.

## Things I'd like to improve

This is still a work in progress. Some things I'd like to experiment with are:

- Making searches faster
- Improving how the most relevant result is selected
- Handling more natural questions
- Making the terminal output cleaner
- Experimenting with other information sources
- Eventually giving it a proper interface

I'm keeping the project simple for now and plan to improve it as I learn more.
