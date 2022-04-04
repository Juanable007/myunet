

class User:
    user=""
# 对于每个全局变量，都需要定义get_value和set_value接口
def set_Id(user):
  User.user = user
def get_Id():
  return User.user
