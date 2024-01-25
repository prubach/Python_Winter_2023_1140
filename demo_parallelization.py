from functools import partial
from multiprocessing import Pool

from knotprot_download import get_proteins, download_link, setup_download_dir, time_it


def run_seq(my_dir):
    i = 0
    prot_list = get_proteins()
    for p in prot_list:
        i += 1
        download_link(my_dir, p)
    print(f'structures downloaded: {i}')


def run_multiprocesssing(my_dir):
    prot_list = get_proteins()
    download = partial(download_link, my_dir)
    with Pool(8) as pool:
        pool.map(download, prot_list)


if __name__ == '__main__':
    setup_download_dir()
    time_it(run_seq, 'images')