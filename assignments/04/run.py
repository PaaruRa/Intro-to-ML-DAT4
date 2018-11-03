import danphe as dp


def main():
    s = dp.Series([23, 25, 24], name='Age')

    print(s) # Should pretty-print the object with name and values
    print(s[0]) # Should give 23

    print(s.mean()) # Should give 24

    df = dp.DataFrame({'Age': [30, 26, 25]})
    print(df['Age'].mean()) # Should give 27


if __name__ == '__main__':
    main()
