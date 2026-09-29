import time
import os
import sys
import levels
import openai
import textdeco

sys.stdout.write("\033[2J\033[H")
sys.stdout.flush()
sys.stdout.write("\033[?25l")

print("Welcome to Prompt-Injection 101! This is a game that will test your skills in prompt injection attacks. You will be given a series of levels, each with a different challenge. Your goal is to try and trick the AI into revealing the password that is hidden in the system prompt. If you can get the AI to reveal the password, you win! If not, you lose."
      )
textdeco.red("="*100)
textdeco.green("Please note that this game is for reasearch and educational purposes only, all techniques and jailbreaking methods are to help you understand your skills.")
textdeco.red("="*100)

while True:
    textdeco.red("*"*10+"Welcome to Prompt-Injection 101!" + "*" * 10)
    textdeco.red(
        "If you don't have one, you can get it from the Google AI studio: https://developers.generativeai.google/console")

    textdeco.blk_terminal()
    print("Before we start, please paste in your API key. This is essential for the program to work. API keys are stored on your device and is not sent to anybody.")

    api_key = input("Paste your API key here: ")
    api_key = os.system(f"API_KEY={api_key}")

    lvlinput = input("Pick levels from 1-5. Enter 0 to quit. 1 is the easiest and 5 is the hardest (ideally impossible). Each has a different challenge. Select a level and press enter to continue. Since we are on a time crunch you only get 1 prompt")

    if lvlinput == "1":
        print("You have selected level 1. In this level, you will be prompted to enter a prompt. The AI will respond to your prompt. Your goal is to try and trick the AI into revealing the password that is hidden in the system prompt. If you can get the AI to reveal the password, you win! If not, you lose.")
        time.sleep(5)
        textdeco.blk_terminal()
        usrprompt = input("Enter your prompt here: ")
        response = levels.level1(usrprompt)
        print(f"AI Response: {response}")
        continue

    elif lvlinput == "2":
        print("You have selected level 2. In this level, you will be prompted to enter a prompt. The AI will respond to your prompt. Your goal is to try and trick the AI into revealing the password that is hidden in the system prompt. If you can get the AI to reveal the password, you win! If not, you lose.")
        time.sleep(5)
        textdeco.blk_terminal()
        usrprompt = input("Enter your prompt here: ")
        response = levels.level2(usrprompt)
        print(f"AI Response: {response}")
        continue

    elif lvlinput == "0":
        print("Exiting the program. Goodbye!")
        break

    elif lvlinput == "3":
        print("You have selected level 3. In this level, you will be prompted to enter a prompt. The AI will respond to your prompt. Your goal is to try and trick the AI into revealing the password that is hidden in the system prompt. If you can get the AI to reveal the password, you win! If not, you lose.")
        time.sleep(5)
        textdeco.blk_terminal()
        usrprompt = input("Enter your prompt here: ")
        response = levels.level3(usrprompt)
        print(f"AI Response: {response}")
        continue

    elif lvlinput == "4":
        print("You have selected level 4. In this level, you will be prompted to enter a prompt. The AI will respond to your prompt. Your goal is to try and trick the AI into revealing the password that is hidden in the system prompt. If you can get the AI to reveal the password, you win! If not, you lose.")
        time.sleep(5)
        textdeco.blk_terminal()
        usrprompt = input("Enter your prompt here: ")
        response = levels.level4(usrprompt)
        print(f"AI Response: {response}")
        continue

    elif lvlinput == "5":
        print("You have selected level 5. In this level, you will be prompted to enter a prompt. The AI will respond to your prompt. Your goal is to try and trick the AI into revealing the password that is hidden in the system prompt. If you can get the AI to reveal the password, you win! If not, you lose.")
        time.sleep(5)
        textdeco.blk_terminal()
        usrprompt = input("Enter your prompt here: ")
        response = levels.level5(usrprompt)
        print(f"AI Response: {response}")
        continue

    elif lvlinput >= "0" and lvlinput <= "5":
        print("Invalid input. Please enter a number between 0 and 5.")

    else:
        print("Invalid input. Please enter a number between 0 and 5.")
        continue


print("Thank you for playing Prompt-Injection 101! We hope you enjoyed the game and learned something new about prompt injection attacks. Please remember to always be careful when interacting with AI systems and to never share sensitive information with them. Goodbye!")



