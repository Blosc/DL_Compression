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


def get_df_by_category(paths, name, category, nrep=None):
    df_res = pd.DataFrame()
    for i in range(len(paths)):
        df = get_filtered_df(paths[i], name, category=category)
        df_res = pd.concat([df_res, df], axis=0)
    df_res.rename(columns={'cratio': 'cratio' + category, 'speed': 'speed' + category,
                           'special_vals': 'special_vals' + category},
                  inplace=True)
    df_res = df_res.drop(['nchunk', 'category', 'codec_filter', 'categoria'], axis=1)
    df_res = df_res.reset_index(drop=True)

    return df_res


def delete_special_vals(df, col_names: list):
    for var in col_names:
        df = df[getattr(df, var).isin([0])]

    return df
