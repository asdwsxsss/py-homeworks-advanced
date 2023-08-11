import unittest

def pairs():
    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    if len(boys) == len(girls):
        print('Идеальные пары:')
    boys.sort()
    girls.sort()
    names = zip(boys, girls)
    for a in names:
        return(f'{a[0]} и {a[1]}')
    else:
        return('Кто-то может остаться без пары')
    

class TestNames(unittest.TestCase):
    def test_list(self):
        a = 'Alex и Emma'
        b = 'Gena и Masha'
        my_list = pairs()
        self.assertIn(a, my_list)
        self.assertNotIn(b, my_list)


if __name__ == '__main__':
    unittest.main()