# python3
class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        # self.phonebook = [[] for x in range()]
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    # print(queries)
    result = []
    phonebook = [0] * 10000001
    # Keep list of all existing (i.e. not deleted yet) contacts.
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            phonebook[cur_query.number] = cur_query.name

        elif cur_query.type == 'del':
            phonebook[cur_query.number] = 0

        else:
            if phonebook[cur_query.number] != 0:
                result.append(phonebook[cur_query.number])
            else:
                result.append('not found')

    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

