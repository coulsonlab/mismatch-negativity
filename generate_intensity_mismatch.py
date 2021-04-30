from numpy.random import shuffle

def generate_intensity_mismatch(standards, deviant, num_events=50):
    """
    Generates a randomized sequence of standard and deviant sound events. Each
    sound event (standard or deviant) has the same frequency of presentation.
    """
    sequence = []
    for count, (std_vol, std_freq) in enumerate(standards):
        sequence += [{'vol': std_vol, 'freq': std_freq, 'label': 'standard ' + str(count)}] * num_events
    dev_vol, dev_freq = deviant
    sequence += [{'vol': dev_vol, 'freq': dev_freq, 'label': 'deviant'}] * num_events
    shuffle(sequence)
    return sequence