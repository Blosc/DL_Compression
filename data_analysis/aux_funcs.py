import pandas as pd
import numpy as np


def get_filtered_df(path, name, special_vals=None, nchunk=None, category=None):
    filename = name + '.csv.gz'
    df = pd.read_csv(path/filename, delimiter=',')
    codec_filter = np.repeat(name, df.__len__())
    df['codec_filter'] = codec_filter
    df.columns = df.columns.str.strip()
    if category is not None:
        categoria = np.repeat(category, df.__len__())
        df['categoria'] = categoria
    if special_vals is not None:
        df = df[df.special_vals.isin(special_vals)]
    if nchunk is not None:
        df = df[df.nchunk.isin(nchunk)]

    return df


def delete_special_vals(df, col_names: list):
    for var in col_names:
        df = df[getattr(df, var).isin([0])]

    return df
