import pandas as pd

# Đọc file excel vào DataFrame
data_frame = pd.read_excel('dataExcel/final.xlsx')
# Khởi tạo một list rỗng để lưu giá trị cho cột mới
values_for_new_column = []
i = 1
ski = ['python', 'java'
    , 'c', 'c++', 'javaScript', 'sql', 'html5', 'css', 'mysql', 'reactjs', 'php','nosql'
       ,'golang', 'spring','nodejs', "scala", 'go','typescript', 'rust', 'postgresql'
       , 'mongodb','es6', 'nextjs', 'laravel', 'html', 'vuejs',   'redis', 'ruby'
       , 'phalcon', 'zend', 'yii2', 'codeigniter', 'js', 'db2', 'django', 'python-dijango'
       , 'redux', 'phpunitest', 'rdbms', 'kotlin',  'tensorflow', 'react', 'vue.js', 'node.js']
exp = ['years']
too = [  'aws',  'rabbitmq', 'truffle', 'remix', 'ganache'
, 'jenkins', 'activemq', 'ubuntu', 'centos','gcp', 'git',  'heroku'
       , 'cvs', 'svn', 'linux', 'gcp', 'axure', 'gitlab'
]
oth =['microservice','maven','kafka','docker', 'kubernetes','security', 'restful', 'ci/cd', 'tdd/bdd', 'ui/ux', 'testing', 'algorithms', 'seo'
      , 'cloudops', 'shell', 'aop', 'jpa', 'querydsl', 'pytorch','batch','keras', 'j2ee', 'oop']
lan =['toeic', 'english', 'japanese']
edu = ['bachelor', 'master degree']
job = ['devops']
add = ['noi', 'chi', 'minh', 'nang']
add2 = ['ha', 'ho', 'da', 'hanoi']
for value in data_frame['Word']:
    value = value.lower()
    if value in ski:
        values_for_new_column.append("B-ski")
    elif value in exp:
        values_for_new_column.append("I-exp")
    elif value in oth:
        values_for_new_column.append("B-oth")
    elif value in edu:
        values_for_new_column.append("B-edu")
    elif value in too:
        values_for_new_column.append("B-too")
    elif value in lan:
        values_for_new_column.append("B-lan")
    elif value in add:
        values_for_new_column.append("I-add")
    elif value in add2:
        values_for_new_column.append("B-add")
    else:
        values_for_new_column.append("O")
# Thêm cột mới với tên là 'Ten_cot_moi' và giá trị được lưu trong list 'values_for_new_column'
data_frame['TAG'] = values_for_new_column

# Lưu DataFrame đã được thêm cột mới vào file Excel
data_frame.to_excel('dataExcel/final22.xlsx', index=False)