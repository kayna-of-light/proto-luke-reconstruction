"""Verse-inclusion matrix across the published reconstructions of Marcion's gospel (finding aid for the
audit). Facts only (which verses each edition prints); no reconstructed text is copied.
Sources: Bilby's normalized datasets on Harvard Dataverse (Roth doi:10.7910/DVN/BYPOOR; Harnack 5TEA5A;
Klinghardt BVEOEX; Nicolotti JGL7LB; BeDuhn UQVGW6; Hahn and Zahn BYNHX6).
Writes docs/stylometry/results/reconstruction_matrix.csv."""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corpus import read_book, recon_present, roth_strata, RECON_FILES

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))


def main():
    keys = list(read_book('63-Lk').keys())
    roth = roth_strata(keys)
    names = list(RECON_FILES)
    sets = {n: recon_present(n) for n in names}
    path = os.path.join(REPO, 'docs', 'stylometry', 'results', 'reconstruction_matrix.csv')
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['ref', 'roth_class'] + names + ['n_editions_printing'])
        for k in keys:
            row = [int(k in sets[n]) for n in names]
            w.writerow([f'{k[0]}:{k[1]}', roth[k]] + row + [sum(row)])
    print(path)


if __name__ == '__main__':
    main()
