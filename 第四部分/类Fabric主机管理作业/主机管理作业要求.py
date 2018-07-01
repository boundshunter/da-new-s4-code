1、host group 1
2、host group 2
def Group(group_name):

1
>>
    h1
    h2
    h3

1.exec cmd
2.send file

1
>>
   cmd ：输入命令（df)
   本组内host全部执行，要并行
   
        ---------h1---------
        df 结果
		
		---------h2---------
		df 结果
		

1.exec cmd
2.send file
>>2

   put /tmp/xxx.py    /tmp/abc.py
   


1、主机分组
2、登录后显示主机分组，选择分组后查看ip列表
3、可批量执行命令、发送文件，结果实时返回（并行）
4、主机用户名和密码可以不同

4的实现
配置文件分组
group1
      h1      10.0.0.100           root     dongao.com123
	  h2       10.0.2.30           sujunfeng   123456
	  h3..........
group2
      h1       10.0.1.100           root     dongao@(*&IT
	  h2       10.0.2.40            dba      dbauser
	  
	  
	
	
	