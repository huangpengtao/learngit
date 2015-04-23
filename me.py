'''
Created on Apr 23, 2015

@author: ff
'''
class TestCase2(object):
    def __init__(self):
        print 'ok'
    def bubble_sort(self,sort_list):
        iter_len = len(sort_list)
        if iter_len < 2:
            return sort_list
        for i in range(iter_len-1):
            for j in range(iter_len-i-1):
                if sort_list[j] > sort_list[j+1]:
                    sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
        return sort_list
if __name__ == '__main__':
    bubble_test=TestCase2()
    sort_list=[33,3,42,1,45,6]
    ret=bubble_test.bubble_sort(sort_list)
    print ret
