"""This module is a script that processes AWS songs to find bpm / beats, etc
"""

def calculate_song_beats(song_fp):
    """Call the functions you wrote in bpmndbeats.py to calculate the song's
    beats
    """
    return []  # empty list of beats


def calculate_song_bpm(song_fp):
    """Call the functions you wrote in bpmndbeats.py to find the song's bpm and
    then return that value.
    """
    return 0.0


def create_song_info_json(song_bpm, beats_list):
    """This is complete -- it just creates the json object you want to write
    """
    return {
        'bpm': song_bpm,
        'beats_list': beats_list
    }


def download_song_to_memory():
    """Use AWS boto API to download the song into the program's memory as a
    File object
    """
    return None  # returning nothing for now


def get_all_song_keys():
    """Connect to AWS and find all songs in a storage location (in AWS, this is
    called a bucket). Get all the song storage location names and return them
    in a list.
    :return: example -
      [
        'songhaow-test-123/fb752f5e-e8f1-4b8a-b114-4fd3d1c937d7',
        'songhaow-test-123/some-other-hash-key',
        ...
      ]
    """
    return []


def write_json_info_to_s3(json_info, song_key):
    """Writes the json_info to AWS S3 under the same name as the song except
    with a .info postfix. Example:
        If the song S3 key is songhaow-test-123/song1, your info file would be
        songhaow-test-123/song1.info
    """
    pass  # pass means do nothing


def process_songs():
    """This is the main function for looping through all the songs you find in
    AWS S3 bucket, downloading, processing, and then uploading meta info.

    We wnat to keep logic simple so it is easy to read what is going on. So we
    break everything into small component functions. This also makes writing
    the functions easier because each function does a small simple task.
    """
    all_song_keys = get_all_song_keys()
    for song_key in all_song_keys:
        song_fp = download_song_to_memory(song_key)
        song_bpm = calculate_song_bpm(song_fp)
        beats_list = calculate_song_beats(song_fp)
        info_json = create_song_info_json(song_bpm, beats_list)
        write_json_info_to_s3(json_info, song_key)

        
if __name__ == '__main__':
    process_songs()
