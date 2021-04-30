from numpy.random import shuffle

def generate_pattern_mismatch(standards, deviant, num_events=50):
    """
    Generates a randomized sequence of standard and deviant sound events. Each
    sound event (standard or deviant) has the same frequency of presentation.
    
    :param standards: list of (volume, frequency) attributes for each standard sound events.
                      May alternatively contain paths to sound files.
    :param deviant: (volume, frequency) attributes for the deviant sound event.
                    May alternatively contain path to sound file.
    :param num_events: number of events to generate for each unique sound event.
    :returns: sequence of sound events for a pattern mismatch trial
    """
    sequence = []
    for count, std in enumerate(standards):
        if isinstance(std, str):
            sequence += [{
                'filename': std,
                'vol': None, 
                'freq': None, 
                'label': 'standard ' + str(count)}
            ] * num_events
        else:
            std_vol, std_freq = std
            sequence += [{
                'filename': None,
                'vol': std_vol, 
                'freq': std_freq, 
                'label': 'standard ' + str(count)}
            ] * num_events
            
    if isinstance(deviant, str):
        sequence += [{
            'filename': deviant, 
            'vol': None, 
            'freq': None, 
            'label': 'deviant'}
        ] * num_events
    else:
        dev_vol, dev_freq = deviant
        sequence += [{
            'filename': None,
            'vol': dev_vol, 
            'freq': dev_freq, 
            'label': 'deviant'}
        ] * num_events
    
    shuffle(sequence)
    return sequence