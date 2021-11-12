def get_new_md_content(old_content, new_content):
    result = ""
    result = old_content['md_links'] + '\n' + new_content['md_link'] + '\n' + old_content['md_solutions'] + '\n' + new_content['md_solution']
    return result


def read_data(file_name):
    file = open(f'{file_name}.txt')
    return file.read()


def write_data(file_name, data):
    file = open(f'{file_name}.txt', "w")
    file.write(data)


def get_new_md_solution(data):
    result = {}
    data_to_list_of_string = data.split('\n')
    result['md_link'] = '+ [' + data_to_list_of_string[0] + '](#' + data_to_list_of_string[1].split('/')[-2] + ')'
    result['md_solution'] = "## " + data_to_list_of_string[0] + "\n" + "\n"  + data_to_list_of_string[1] + "\n" + "\n```python\n" + '\n'.join(data_to_list_of_string[2:]) + "\n" + "\n" + "```"
    return result


def get_old_md_solutions(data):
    result = {}
    data_to_list_of_string = data.split('##')
    result['md_links'] = data_to_list_of_string[0]
    result['md_solutions'] = '##' + '##'.join(data_to_list_of_string[1:])
    return result


new_solution = read_data('new_solution')
new_content = get_new_md_solution(new_solution)
old_solutions = read_data('leetcode')
old_content = get_old_md_solutions(old_solutions)
result = get_new_md_content(old_content, new_content)
write_data('leetcode', result)

