import os

print('\ngetting_system_value.py {}\n'.format('-'*20))

# ==================================
#   fine special value
#       - os.environ['value_name'] return string
#       - return "Error" if don't have value
#       - you should write "try - catch"
# ==================================
# s = os.environ['XDG_RUNTIME_DIR']
# print('\t1. An environment value >> {}\n'.format(s))

# ==================================
#   fine special value
#       - os.getenv('value_name') return string
#       - return None if don't have value
# ==================================
s = os.getenv('user_id')
print('\t2. An environment value >> {}\n'.format(s))

# ==================================================
#   fine all value
#       - os.environ.keys() return <class 'collections.abc.KeysView'>
#       - If you want sort them, you have to cast list from class
# ==================================================
# ls = list(os.environ.keys())
# ls.sort()
#
# print('\t3. All environment value')
# for item in ls:
#     print('\t\t{}={}'.format(item, os.environ[item]))