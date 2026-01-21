# CS-4700-project1

The following outlines my implementation of project 1: socket basics, a Wordle guessing game working with TCP and TLS.

# Guessing Algorithm
I use a simple constraint-based approach using the provided word list (project1-words.txt):
1. Load all valid 5-letter words into a candidate list.
2. Always guess the first remaining candidate.
3. After each retry, take the most recent guess + marks and filter candidates:
    - For each candidate secret word, locally simulate Wordle scoring (including duplicate-letter rules).
    - Keep the candidate only if the simulated marks match the server’s marks exactly.
4. Repeat until receiving a bye message, then print only the flag.

This strategy is intentionally simple but converges well under the 500-guess limit.

# Testing
make
./client proj1.4700.network <username>
./client -s proj1.4700.network <username>

# Approach and Experience
My approach was to first focus on establishing a correct and reliable connection to the server before worrying about the guessing logic. This project was interesting because it operated at a lower level than what I’m used to — instead of working with higher-level client/server APIs, I had to work directly with TCP sockets, raw bytes, and buffering to correctly parse newline-terminated JSON messages. Handling partial reads and building a receive buffer required some additional documentation review, but it helped clarify how data actually moves through the networking stack.

Once the networking and protocol handling were in place, I implemented a simple and reliable guessing strategy. Using the provided word list, the client maintains a list of possible candidate words and repeatedly filters it based on the server’s feedback by simulating Wordle’s scoring rules. To keep the solution straightforward, the client always guesses the first remaining candidate. I also added basic error handling