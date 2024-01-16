# langchain_hub
一个简单的基于langchain的项目架构
##### 初衷
做开发多年，平时都忙于团队项目，还没参与过一些开源项目，受一位UP主的启发，加入「我票人人，人人票我」的行列！欢迎大家也票我一下，给点肯定可鼓励，谢谢！⭐️⭐️⭐️⭐️⭐️

当前的版本还有些粗糙，仅支持chatglm3-6b模型的部署，要求cuda。
后续有空闲时间的话会增加一些其他的模块和支持chatglm3-6b-int4等量化模型，也欢迎各位小伙伴能参与进来！也希望这项目对大伙有所帮助！！！

##### 环境部署
1.使用miniconda创建环境(xxx为自定义的名称)
> conda create --name xxx python=3.10

2.安装依赖库
> pip install -r requirements.txt

3.如果产生依赖库之间兼容性，可根据终端出现的提升来安装对应的版本，
torch的gpu版本可到官网选择完系统之后执行pip命令安装即可

4.如果系统存储资源有限，可将miniconda迁移至其他目录下，具体操作方式可自行搜索；使用pip cache purge 命令清除之前使用pip命令安装过的缓存文件。

##### 运行
客户端、服务器端、大模型端通过http访问
大模型端可开启多个模型（每个模型配置不同的端口），供团队一起访问，节省GPU资源，后续如果产生并发问题，可使用一些机制来管控。

1.启动大模型
终端启动大模型服务
> sh start_llm.sh

启动后，cuda环境可通过nvidia-smi查看显存的使用情况

2.启动服务器
> sh start_server.sh

3.关闭cli客户端和服务器端
> sh shutdown.sh

4.关闭大模型端

查看start_model.py的进程
> ps x

关闭进程
kill ****

5.注意
上面的启动服务器的脚本是连同cli客户端一起启动的
如仅需启动服务器，将python client/start_chat.py注释即可
