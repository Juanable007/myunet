

class ImageConfig:
    Id=-1
    Path=""
    SegPath=""
    Name=""
    GroupId=1
    Num=0
# 对于每个全局变量，都需要定义get_value和set_value接口
def set_Id(id):
  ImageConfig.Id = id
def get_Id():
  return ImageConfig.Id

# 对于每个全局变量，都需要定义get_value和set_value接口
def set_path(path):
  ImageConfig.Path = path
def get_path():
  return ImageConfig.Path

def set_segPath(path):
  ImageConfig.SegPath = path
def get_segPath():
  return ImageConfig.SegPath

# 对于每个全局变量，都需要定义get_value和set_value接口
def set_name(name):
  ImageConfig.Name = name
def get_name():
  return ImageConfig.Name


# 对于每个全局变量，都需要定义get_value和set_value接口
def set_groupId(groupId):
  ImageConfig.GroupId = groupId
def get_groupId():
  return ImageConfig.GroupId

# 对于每个全局变量，都需要定义get_value和set_value接口
def set_num(num):
  ImageConfig.Num = num
def get_num():
  return ImageConfig.Num