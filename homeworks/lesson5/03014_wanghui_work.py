import nuke
def H_render():
    a = [1,2,3]
    for i in a:
        source = nuke.toNode('Read1')
        name = source['file'].getValue().split("/")[-1]
        node = nuke.createNode('Write')
        file_path = r'E:\nuke_python_class\Class5\ '[:-1]+name
        format = '.mov'
        number = "_"+str(i)
        new_path = file_path.replace("\\","/")[:-4]+number+format
        node['file'].setValue(new_path)
        node.setInput(0,source)
    nuke.execute ("Write1",start=1,end=10)
    nuke.execute ("Write2",start=30,end=40)
    nuke.execute ("Write3",start=80,end=100)