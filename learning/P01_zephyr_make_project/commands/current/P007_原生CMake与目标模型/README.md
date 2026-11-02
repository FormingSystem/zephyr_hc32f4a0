# P007_原生CMake与目标模型：当前命令索引

命令逐块取自[当前正文](../../../P007_原生CMake与目标模型.md)。先读正文前提，只执行所选环境与路线，不批量执行本目录。

| 操作 | 终端 | 所属讲解 | 内容 |
| --- | --- | --- | --- |
| 001 | bash | 6.2.1_工具、目录和文件来源 | [完整命令](001-bash.txt) |
| 002 | bash | 6.2.1_工具、目录和文件来源 | [完整命令](002-bash.txt) |
| 003 | bash | 6.2.1_工具、目录和文件来源 | [完整命令](003-bash.txt) |
| 004 | bash | 6.2.3_先配置和生成，再编译和运行 | [完整命令](004-bash.txt) |
| 005 | bash | 6.2.3_先配置和生成，再编译和运行 | [完整命令](005-bash.txt) |
| 006 | bash | 6.5_变量、缓存与目标属性各管什么 | [完整命令](006-bash.txt) |

## 配套完整操作

下列操作保留已验证实验的目录名，按当前正文前提选择；不能批量执行。与上面的逐块命令相比，它们包含创建文件或恢复必要环境的完整过程。

| 操作 | 说明 |
| --- | --- |
| [step-01.txt](complete/step-01.txt) | Windows UCRT64；源码根；只检查，不安装或编译。 |
| [step-02.txt](complete/step-02.txt) | Windows UCRT64；任意目录；仅上一块确认缺少主机 GCC 时执行。 |
| [step-03.txt](complete/step-03.txt) | Windows UCRT64；源码根；前提：已确认主机 CMake、Ninja、GCC 可用。 |
| [step-04.txt](complete/step-04.txt) | Windows UCRT64；源码根；前提：8.2.1 的两个练习文件已经创建。 |
| [step-05.txt](complete/step-05.txt) | Windows UCRT64；源码根；前提：上一块 configure/generate 正常结束。 |
| [step-06.txt](complete/step-06.txt) | Windows UCRT64；源码根；仅已手动加入上一段 option/if 后执行。 |
