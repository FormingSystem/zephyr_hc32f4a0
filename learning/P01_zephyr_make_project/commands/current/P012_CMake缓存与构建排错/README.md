# P012_CMake缓存与构建排错：当前命令索引

命令逐块取自[当前正文](../../../P012_CMake缓存与构建排错.md)。先读正文前提，只执行所选环境与路线，不批量执行本目录。

| 操作 | 终端 | 所属讲解 | 内容 |
| --- | --- | --- | --- |
| 001 | bash | 11.1.1.2_只看缓存时，不要意外重新配置 | [完整命令](001-bash.txt) |
| 002 | bash | 11.1.1.3_修改一项，然后故意不再传它 | [完整命令](002-bash.txt) |
| 003 | bash | 11.1.1.3_修改一项，然后故意不再传它 | [完整命令](003-bash.txt) |
| 004 | bash | 11.1.1.4_恢复默认与项目脚本覆盖 | [完整命令](004-bash.txt) |
| 005 | bash | 11.1.1.5_清理、重新配置与重建的边界 | [完整命令](005-bash.txt) |
| 006 | bash | 11.1.1.6_预设保存输入，缓存保存一次配置的结果 | [完整命令](006-bash.txt) |
| 007 | bash | 11.2.4_在本章构建目录完成自查与排错 | [完整命令](007-bash.txt) |
| 008 | bash | 11.2.4_在本章构建目录完成自查与排错 | [完整命令](008-bash.txt) |
| 009 | bash | 11.4.1_下载阶段的 407 先看代理，而不是改包版本 | [完整命令](009-bash.txt) |
| 010 | bash | 11.4.1_下载阶段的 407 先看代理，而不是改包版本 | [完整命令](010-bash.txt) |
| 011 | bash | 11.4.2_Python 找不到已有 YAML，先看它收到了哪种路径 | [完整命令](011-bash.txt) |
| 012 | bash | 11.4.3_源码包路径被拼接时，核对 CMake 的来源 | [完整命令](012-bash.txt) |
| 013 | bash | 11.4.5_DTC、Ccache 和 Git 警告分别判断 | [完整命令](013-bash.txt) |
| 014 | bash | 11.4.5_DTC、Ccache 和 Git 警告分别判断 | [完整命令](014-bash.txt) |

## 配套完整操作

下列操作保留已验证实验的目录名，按当前正文前提选择；不能批量执行。与上面的逐块命令相比，它们包含创建文件或恢复必要环境的完整过程。

| 操作 | 说明 |
| --- | --- |
| [11.1.1-01.txt](complete/11.1.1-01.txt) | Windows UCRT64；源码根；前提：8.5 的 first-ucrt-zip 配置成功。 |
| [11.1.1-02.txt](complete/11.1.1-02.txt) | Windows UCRT64；源码根；前提：first-ucrt-zip 已配置成功。 |
| [11.1.1-03.txt](complete/11.1.1-03.txt) | Windows UCRT64；源码根；前提：12.1.1.3 已把日志缓存项设为 VERBOSE。 |
| [11.1.1-04.txt](complete/11.1.1-04.txt) | Windows UCRT64；源码根；前提：12.1.1.3 已设置日志缓存项。 |
| [11.1.1-05.txt](complete/11.1.1-05.txt) | Windows UCRT64；源码根；前提：first-ucrt-zip 已成功构建。 |
| [11.1.1-06.txt](complete/11.1.1-06.txt) | Windows UCRT64；源码根；已按本节创建或合并 learning-mps2 预设。 |
| [11.2.4-01.txt](complete/11.2.4-01.txt) | Windows UCRT64；源码根；前提：8.5 的 first-ucrt-zip 已成功配置。 |
| [11.2.4-02.txt](complete/11.2.4-02.txt) | Windows UCRT64；源码根；前提：first-ucrt-zip 配置、生成成功。 |
| [step-01.txt](complete/step-01.txt) | Windows UCRT64；源码根；前提：8.5 的 first-ucrt-zip 配置成功。 |
| [step-02.txt](complete/step-02.txt) | Windows UCRT64；源码根；前提：first-ucrt-zip 已配置成功。 |
| [step-03.txt](complete/step-03.txt) | Windows UCRT64；源码根；前提：12.1.1.3 已把日志缓存项设为 VERBOSE。 |
| [step-04.txt](complete/step-04.txt) | Windows UCRT64；源码根；前提：12.1.1.3 已设置日志缓存项。 |
| [step-05.txt](complete/step-05.txt) | Windows UCRT64；源码根；前提：first-ucrt-zip 已成功构建。 |
| [step-06.txt](complete/step-06.txt) | Windows UCRT64；源码根；已按本节创建或合并 learning-mps2 预设。 |
| [step-07.txt](complete/step-07.txt) | Windows UCRT64；源码根；前提：8.5 的 first-ucrt-zip 已成功配置。 |
| [step-08.txt](complete/step-08.txt) | Windows UCRT64；源码根；前提：first-ucrt-zip 配置、生成成功。 |
