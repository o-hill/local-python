'''

    Use a single source of truth for training progress.

    Also enables a web server to present real-time training progress.

'''

import numpy as np
import pandas as pd
import threading
import os


# Change this to set up where the CSV files will be located on the disk.
SAVE_LOC = '/Users/oliverhill/.network_progress'


class Writer:

    def __init__(self,
            name: str = f'{np.random.randint(5000)}_network',
            cols: list = ['loss']) -> None:
        '''Initialize the writer.'''

        self.full_path = os.path.join(SAVE_LOC, f'{name}.csv')

        # If there is already data present, assume we are appending to the existing data.
        if os.path.exists(self.full_path):
            data = pd.read_csv(self.full_path)

            for col in cols:
                if col not in list(data.columns.values):
                    raise RuntimeError('Given columns does not match data currently available. Delete file or try again.')

        else:
            data = pd.DataFrame(columns=cols)


    def write(self, new_data: list) -> None:
        '''Write heterogeneous data to the dataframe and save it.'''

        # Write the data.
        data.loc[data.size] = new_data

        # Save the data in a thread.
        threading.Thread(target=data.to_csv, args=[self.full_path]).start()


    def loss(self) -> float:
        '''Return the average loss from the last 10 iterations.'''
        return data['loss'].iloc[-10:].mean()

















