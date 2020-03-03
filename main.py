import os


if __name__ == '__main__':
    jsondir = 'post'
    if not os.path.exists(jsondir):
        os.makedirs(jsondir)
        pass

    if not os.path.exists('out'):
        os.makedirs('out')
        pass

    filelist = os.listdir(jsondir)

    pic = "pic:"

    for i in filelist:
        pic += "\n  - title: " + i + "\n    file: " + i + "\n    des: " + i + "\n"

    filename = "out/picindex.yml"

    with open(filename, 'w') as f:
        f.write(pic)

