'''
Jay Johnson - Lesson02 - Assignment02 - Generators and Closures

Ed Sheeran song lister with generators and closures
--
Write a generator to find and print all of your favorite artist’s
tracks from the data set. Your favorite artist isn’t represented
in that set? In that case, find Ed Sheeran’s tracks.

Find Ed Sheeran’s tracks - DONE

----
Closures
Using the same data set, write a closure to capture
high energy tracks. We will define high energy tracks
as anything over 8.0. Submit your code and the tracks it finds,
artist name, track name and energy value.

8.0 or higher energy finder - DONE

'''
import pandas as pd
music = pd.read_csv("featuresdf.csv")

#print(name.name)
full_list = len(music.name)
#print(full_list)

# generator to find and print all of your favorite artist’s
# tracks from the data set.
def ed_sheeran_gen(start, stop):
    music = pd.read_csv("featuresdf.csv")
    i = start
    while i < stop:
        new_song= music.name[i]
        #print(new_song)
        #print(music.artists[i])
        if music.artists[i] == 'Ed Sheeran':
            yield music.name[i]#new_song
        i += 1

def counter():
    music = pd.read_csv("featuresdf.csv")
    count = 0
    def increment():
        nonlocal count
        if music.energy[count] >= 0.8:
            print(music.name[count])
            print(music.artists[count])
            print(music.energy[count])
        count += 1
        return count
    return increment

# write a closure to capture high energy tracks.
# we will define high energy tracksas anything over 8.0.
if __name__ == '__main__':

    print("Ed Sheeran finder\n")

    ed_gen = ed_sheeran_gen(0,full_list)

    for ed_gen_x in ed_gen:
        print(ed_gen_x)

    print("\nEnergy finder\n")

    my_counter = counter()

    for j in range(0,full_list):
        my_counter()
