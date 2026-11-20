# P011_Zephyr的CMake输入与依赖发现：当前命令索引

命令逐块取自[当前正文](../../../P011_Zephyr的CMake输入与依赖发现.md)。先读正文前提，只执行所选环境与路线，不批量执行本目录。

| 操作 | 终端 | 所属讲解 | 内容 |
| --- | --- | --- | --- |
| 001 | bash | [11.3.5_核对 AN386 的编译清单](../../../reference/AN386模块与编译清单实验.md#section-11-3-5) | [完整命令](001-bash.txt) |

## 配套完整操作

下列操作保留已验证实验的目录名，按当前正文前提选择；不能批量执行。与上面的逐块命令相比，它们包含创建文件或恢复必要环境的完整过程。

| 操作 | 说明 |
| --- | --- |
| [编译并反汇编一个函数（PowerShell）](complete/compile-probe-powershell.txt) | 在[实验小节](../../../P011_Zephyr的CMake输入与依赖发现.md#section-11-2-2)保存 probe.c 后执行。 |
| [编译并反汇编一个函数（UCRT64）](complete/compile-probe-ucrt64.txt) | GCC 生成 probe.o，再由 objdump 读取同一个对象。 |
| [trace-selected-sources.txt](complete/trace-selected-sources.txt) | Windows UCRT64；P008 的 first-ucrt-zip 已配置成功；只读生成结果。 |
