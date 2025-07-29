import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()
print(f"{Fore.GREEN}Welcome to Sentiment Spy!{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mystery_Agent_501"  # safe filename format

conversation_history = []

def show_help():
    print(f"""
{Fore.CYAN}Available Commands:{Style.RESET_ALL}
  {Fore.YELLOW}help{Style.RESET_ALL}     - Show this help message
  {Fore.YELLOW}reset{Style.RESET_ALL}    - Clear conversation history
  {Fore.YELLOW}history{Style.RESET_ALL}  - Show all analyzed sentences with sentiment
  {Fore.YELLOW}exit{Style.RESET_ALL}     - Quit the program
""")

print(f"\n{Fore.CYAN}Hello, agent {user_name}!{Style.RESET_ALL}")
print("Type a sentence and I will analyze your sentiment.")
show_help()

while True:
    user_input = input("> ").strip()

    if not user_input:
        print(f"\n{Fore.RED}Please enter a sentence.{Style.RESET_ALL}")
        continue

    command = user_input.lower()

    if command == "exit":
        file_name = f"{user_name}_sentiment_analysis.txt"
        break

    elif command == "reset":
        conversation_history = []
        print(f"\n{Fore.CYAN}Conversation history has been reset.{Style.RESET_ALL}")
        continue

    elif command == "history":
        if not conversation_history:
            print(f"\n{Fore.YELLOW}No conversation history to display.{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.CYAN}Conversation history:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"
                print(f"{color}{idx}. {text} (Polarity: {polarity:.2f}, Sentiment: {sentiment_type} {emoji}){Style.RESET_ALL}")
        continue

    elif command == "help":
        show_help()
        continue

    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    conversation_history.append((user_input, polarity, sentiment_type))

    print(f"{color}Sentiment: {sentiment_type} {emoji} (Polarity: {polarity:.2f}){Style.RESET_ALL}")