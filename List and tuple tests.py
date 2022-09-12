import pytest


class Test:
    @pytest.mark.parametrize('element',
                             ['string', [str(i) for i in range(5)], False, None])
    def test_list_inclusivity(self, element):
        '''Тест проверяет возможность вставки в лист элементов различных типов'''

        test_list = [i for i in range(10)]
        test_list_size = len(test_list)
        test_list.append(element)

        assert len(test_list) == test_list_size + 1, 'Impossible to add element to the list'

    def test_list_subtraction(self):
        '''Тест проверяет возможность вычитания списков'''

        test_list1 = [0, 1, 2]
        test_list2 = [3, 1, 0]

        try:
            assert test_list1 - test_list2, 'Impossible to substract one list from another'
        except TypeError:
            pass

    def test_list_reversibility(self):
        '''Тест проверяет возможность разворота списка'''

        test_list = [i for i in range(10)]
        reversed_test_list = [i for i in range(9, -1, -1)]
        test_list.reverse()

        assert test_list == reversed_test_list, 'List is impossible to reverse'

    @pytest.mark.parametrize('tuple_to_concatinate',
                             [(0, 1, 2), (0, 1, 2, 3), (0, 1, 2, 3, 4)])
    def test_tuple_concatination(self, tuple_to_concatinate):
        '''Тест проверяет возможность конкатенации кортежей одинаковой и различной длины'''

        test_tuple = (10, 9 , 8, 7)
        test_tuple_size = len(test_tuple)
        test_tuple += tuple_to_concatinate

        assert len(test_tuple) == (test_tuple_size + len(tuple_to_concatinate)), \
            "Impossible to concatinate tuples"

    def test_possibility_to_use_tuple_as_dictionary_key(self):
        '''Тест проверяет возможность использования кортежа в качестве ключа словаря'''

        test_tuple = ('Mark', 'Bob')
        test_int = 2
        test_dictionary = {test_tuple : test_int}

        assert test_dictionary.get(test_tuple) == test_int, \
            'Impossible to use tuple as dictionary key'

    def test_item_assignement_in_tuple(self):
        '''Тест проверяет возможность изменения элемента кортежа'''

        test_tuple = (0, 1, 2)

        try:
            test_tuple[0] = 10
            assert test_tuple[0] == 10, "Tuple doesn't support item assignnement"
        except TypeError:
            pass



