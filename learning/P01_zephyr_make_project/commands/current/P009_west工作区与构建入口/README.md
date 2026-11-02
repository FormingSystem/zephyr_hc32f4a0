# P009_west工作区与构建入口：当前命令索引

命令逐块取自[当前正文](../../../P009_west工作区与构建入口.md)。先读正文前提，只执行所选环境与路线，不批量执行本目录。

| 操作 | 终端 | 所属讲解 | 内容 |
| --- | --- | --- | --- |
| 001 | bash | 8.1_先把 west 程序与 Zephyr 分开 | [完整命令](001-bash.txt) |
| 002 | bash | 8.2_工作区怎样找到正确的清单 | [完整命令](002-bash.txt) |
| 003 | bash | 8.2_工作区怎样找到正确的清单 | [完整命令](003-bash.txt) |
| 004 | bash | 8.2_工作区怎样找到正确的清单 | [完整命令](004-bash.txt) |
| 005 | bash | 8.3_清单怎样决定下载什么 | [完整命令](005-bash.txt) |
| 006 | bash | 8.3_清单怎样决定下载什么 | [完整命令](006-bash.txt) |
| 007 | bash | 8.4_Zephyr 怎样把 build 命令交给 west | [完整命令](007-bash.txt) |
| 008 | bash | 8.5.1_先只配置，观察 west 传给 CMake 的参数 | [完整命令](008-bash.txt) |
| 009 | bash | 8.5.2_构建，以及与直接 CMake 共用目录 | [完整命令](009-bash.txt) |
| 010 | bash | 8.5.2_构建，以及与直接 CMake 共用目录 | [完整命令](010-bash.txt) |
| 011 | bash | 8.6_常用方式要分清参数交给谁 | [完整命令](011-bash.txt) |

## 配套完整操作

以下与正文完整操作逐块同步，保留既有实验目录名。按当前前提选择，不批量执行。

| 操作 | 说明 |
| --- | --- |
| [step-01.txt](complete/step-01.txt) | Windows UCRT64；进入 P003 的源码根，复用 P004 创建的环境。 |
| [step-02.txt](complete/step-02.txt) | Windows UCRT64；源码根；P004 环境已经存在。 |
| [step-03.txt](complete/step-03.txt) | Windows UCRT64；仅“尚无工作区”分支。已有工作区跳过整块。 |
| [step-04.txt](complete/step-04.txt) | Windows UCRT64；9.2 已确认工作区根为 /g/zephyr_practice。 |
| [step-05.txt](complete/step-05.txt) | Windows UCRT64；源码根；9.2 已确认正确工作区。 |
| [step-06.txt](complete/step-06.txt) | Windows UCRT64；源码根；工作区正确，模块本地修改已保存，项目地址允许访问。 |
| [step-07.txt](complete/step-07.txt) | Windows UCRT64；源码根；工作区检查已通过。 |
| [step-08.txt](complete/step-08.txt) | Windows UCRT64；P008 已确认工具、SDK、cmsis 和 cmsis_6；有效工作区已就绪。 |
| [step-09.txt](complete/step-09.txt) | Windows UCRT64；源码根；上一块 west-demo 已配置、生成成功。 |
| [step-10.txt](complete/step-10.txt) | Windows UCRT64；源码根；west-demo 已成功配置，工具位置没有改变。 |
| [step-11.txt](complete/step-11.txt) | Windows UCRT64；源码根；west-demo 已配置成功。 |
