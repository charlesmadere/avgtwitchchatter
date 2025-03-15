import markovify
import sys

# Get the channel name passed as a command-line argument
bot_name = sys.argv[1] if len(sys.argv) > 1 else None

if not bot_name:
    print("No channel name provided.")


chat_log_file = "./" + bot_name + "/chat_log.txt"
###
# check if contains banned term
###

def contains_banned_term(text, filename="banned_terms.txt"):

    filename=bot_name + "/banned_terms.txt"

    if text is None:
        return False
    try:
        with open(filename, "r", encoding="utf-8") as file:
            banned_terms = {line.strip().lower() for line in file if line.strip()}
        
        text_words = set(text.lower().split())
        return any(term in text_words for term in banned_terms)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Get raw text as string.
with open(chat_log_file, "r", encoding='utf-8') as f:
	text = f.read()

#Build the model
text_model = markovify.NewlineText(text,state_size=3)

#Print five randomly-generated sentences

for i in range(20):

    #make sure term does not have banned term in it
    while True:
        string1 = text_model.make_sentence(test_output=False)
        if not contains_banned_term(string1):
            break

    #if only one word, print it
    if len(string1.split()) == 1:
        if string1 is not None :
            print(string1)
            break

    #if more than one word, regenerate it to be at least 10% unique, but no banned terms
    while True:
        string1 = text_model.make_sentence(max_overlap_ratio=0.9)
        if not contains_banned_term(string1):
            break

    if string1 is not None :
        print(string1)
        break

#print three randomly-generated sentences of no more than 280 characters
#for i in range(3):
#	print(text_model.make_short_sentence(280))
