import pickle

def main(csv_path, pkl_path, headers=['x', 'y', 'z']):
    # read a csv file
    with open(csv_path, 'r') as fobj_csv:
        records = [dict(zip(headers, line.strip().split(','))) for line in fobj_csv]
    # save this as a pickle object
    with open(pkl_path, 'wb') as fobj_pkl:
        pickle.dump(records, fobj_pkl)

if __name__ == '__main__':
    main('data.csv', 'data.pkl')