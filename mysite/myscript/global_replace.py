import sys
import os

class REPLACE:
     
    #查找并替换
    def findAndReplace(self,file_path,find_string,rep_string):
        try:
            global sucessCount
            #encoding='iso-8859-1', 其他编码试过了，都会报错
            f=open(file_path,'r+',encoding='iso-8859-1')
    
            all_lines=f.readlines()
    
            f.seek(0)
            f.truncate()
    
            for line in all_lines:
                line=line.replace(find_string, rep_string)
                f.write(line)
    
        finally:
            f.close()
    
    #循环遍历文件夹中的文件，
    def listFiles(self,dirPath):
        fileList=[]
        #os.walk() ，返回一个三元组 
        for root,dirs,files in os.walk(dirPath):
            for fileObj in files:
                #判断文件后缀名是否是 .h 或者 .cpp
                extension = os.path.splitext(fileObj)[-1]
                extension = extension.lower()
    
                #if extension=='.h' or extension=='.cpp' or extension=='.txt'  :
                if extension=='.html' or extension=='.js'  :
                    fileList.append(os.path.join(root,fileObj))
    
        return fileList
    
    def printFileList(self,filepathname):
        for file_path in filepathname:
            print(file_path)
    
    def handle(self):
    
        if len(sys.argv)!=3:
            print("参数个数有误！\n参考命令：$ python main.py old_string new_string ");
            exit(1)
    
        #获取要替换的old string 和new string
        find_string=sys.argv[1]
        rep_string=sys.argv[2]
    
        #获取当前路径上一级目录
        current_path = os.path.abspath(os.path.dirname(os.getcwd())) 
        #获取文件名列表
        print("current_path=",current_path)
        fileNameList = self.listFiles(current_path)
        #print("fileNamelist=",fileNameList)

        for file_path in fileNameList:
            self.findAndReplace(file_path,find_string,rep_string)


if __name__=='__main__':
    instance = REPLACE()
    instance.handle()
