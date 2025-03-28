# import directories
import random
import statistics
import os


# sub-routine to find the next free file name
def find_free_filepath():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")  # Get Desktop Path
    results_folder = os.path.join(desktop_path, "Dudunsparce") # create the file path to save the results
    os.makedirs(results_folder, exist_ok=True) # if the folder doesn't exist, this creates it
    base_filename = "dudunsparce_hunt_results" # start of the file name
    file_extension = ".txt" # file extension

    counter = 1
    global file_path # needs to be global so it can be called upon in the main function
    file_path = os.path.join(results_folder, f"{base_filename}{file_extension}")  # Create File Path

    while os.path.exists(file_path): # the loop keeps going until it finds a free filepath
        file_path = os.path.join(results_folder, f"{base_filename}_{counter}{file_extension}")
        counter += 1 # if the filename exists, adds 1 to end and repeats


def main():
    # define my variables and lists
    hunts = 1
    shiny_encounters = []
    dudun_encounters = []

    while True:
        try:
            loops = int(input("How many hunts?: "))  # user inputs how many hunts to specify (with error handling)
            break
        except ValueError:
            print("Invalid input")
            print("----------")

    print("----------")

    for i in range(loops): # repeats the hunts the number of times specified
        # reset variables each hunt
        encounters = 0
        shinies = 0
        print(f"Hunt {hunts}/{loops}...")
        while True:
            encounters += 1
            a = random.randint(1, 603) # first check to see if we get a shiny
            if a == 1:
                shinies += 1
                b = random.randint(1, 100) # second check to see if it's 3 segment
                if b == 1:
                    print(f"Shinies Seen: {shinies}")
                    shiny_encounters.append(shinies) # add results to the created lists
                    dudun_encounters.append(encounters)
                    hunts += 1

                    with open(file_path, "a") as file: # save results to the txt file
                        file.write(f"---------- Results For Hunt {hunts-1}----------\n")
                        file.write(f"Encounters: {encounters}\n")
                        file.write(f"Shinies until 3-segment shiny: {shinies}\n")
                        file.write("\n")

                    break

    if dudun_encounters and shiny_encounters: # this if is a failsafe in case the lists are empty
        lowest_value = min(shiny_encounters) # find the least amount of encounters
        lowest_index = shiny_encounters.index(lowest_value)+1 # locate the hunt that had the least encounters
        highest_value = max(shiny_encounters) # find the highest encounters
        highest_index = shiny_encounters.index(highest_value)+1 # locate the hunt that had the highest encounters
        # print results into the console
        print("----------")
        print("Encounters: ", dudun_encounters)
        print("Shinies until 3-segment shiny: ", shiny_encounters)
        print("----------")
        print("Hunts: ", loops)
        print("Average Encounters: ", statistics.mean(dudun_encounters))
        print("Average Shinies until 3-segment shiny:", statistics.mean(shiny_encounters))
        print("Lowest Shinies until 3-segment shiny:", min(shiny_encounters), "( Hunt", lowest_index, ")")
        print("Highest Shinies until 3-segment shiny:", max(shiny_encounters), "( Hunt", highest_index, ")")

        with open(file_path, "r") as file:
            old_content = file.readlines() # save the file contents to a variable (needed to add data to the start)

        with open(file_path, "w") as file: # open the file in write mode
            pass # clear the file of contents
            # add the results to the file
            file.write(f"---------- Overall Results ----------\n")
            file.write(f"Hunts: {hunts-1}\n")
            file.write(f"Average Encounters: {statistics.mean(dudun_encounters)}\n")
            file.write(f"Average Shinies until 3-segment shiny: {statistics.mean(shiny_encounters)}\n")
            file.write(f"Lowest Shinies until 3-segment shiny: {min(shiny_encounters)} (Hunt {lowest_index})\n")
            file.write(f"Highest Shinies until 3-segment shiny: {max(shiny_encounters)} (Hunt {highest_index})\n")
            file.write("\n")
            file.writelines(old_content) # add the other data back into the file at the bottom
            file.write("\n---------------------------------------\n")
            file.write(f"All Encounters:\n {dudun_encounters}\n") # write the full data set at the bottom
            file.write(f"All Shiny Encounters:\n {shiny_encounters}")

    else:
        print("No hunt data found")

    replay() # run the sub-routine to replay the program


def replay():
    print("----------")
    while True:
        try:
            replay_question = int(input("1 - Replay 2 - Quit: ")) # ask if the users wants to reply (w/ error handling)
            if replay_question != 1 and replay_question != 2:
                print("Invalid Selection")
                print("----------")
            else:
                break
        except ValueError:
            print("Invalid input")
            print("----------")

    if replay_question == 1:
        print("----------")
        find_free_filepath()
        main()
    else:
        print("----------")
        print("Exiting...")


#run the program
find_free_filepath()
main()

