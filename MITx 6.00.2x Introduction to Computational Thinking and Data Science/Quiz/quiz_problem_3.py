# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 10:13:38 2017

@author: szahn
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    
    working_song_list = songs[:]
    used_disk_size = 0
    used_songs = []
    
    
    first_song = working_song_list.pop(0)
    if first_song[2] > max_size:
        return []
    else:
        used_songs.append(first_song)
        used_disk_size += first_song[2]
    
    while used_disk_size <= max_size:
        if not working_song_list:
            break
        x = min(working_song_list, key=lambda x: x[2])
        if used_disk_size + x[2] > max_size:
            break
        used_songs.append(working_song_list.pop(working_song_list.index(x)))
        used_disk_size += x[2]

    return [song[0] for song in used_songs]




test_songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
test_songs_2 = [('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)]