# P013_自定义源码模块与配置开关：当前命令索引

命令逐块取自[当前正文](../../../P013_自定义源码模块与配置开关.md)。先读正文前提，只执行所选环境与路线，不批量执行本目录。

| 操作 | 终端 | 所属讲解 | 内容 |
| --- | --- | --- | --- |
| 001 | bash | 12.1.7_将组件根交给本次配置 | [完整命令](001-bash.txt) |
| 002 | bash | 12.1.10_关闭功能，验证被发现与被编译的区别 | [完整命令](002-bash.txt) |

## 配套完整操作

下列操作保留已验证实验的目录名，按当前正文前提选择；不能批量执行。与上面的逐块命令相比，它们包含创建文件或恢复必要环境的完整过程。

| 操作 | 说明 |
| --- | --- |
| [build-component-manual-modules.txt](complete/build-component-manual-modules.txt) | P013 13.1.11：显式提供完整模块列表的 CMake 分支 |
| [build-component-off.txt](complete/build-component-off.txt) | P013 13.1.10：保留开启版，独立构建关闭组件的应用 |
| [build-component-on.txt](complete/build-component-on.txt) | P013 13.1.7：构建启用 app_greeting 的应用 |
| [check-component-off.txt](complete/check-component-off.txt) | P013 13.1.10：检查组件仍被发现而源文件已关闭 |
| [check-component-on.txt](complete/check-component-on.txt) | P013 13.1.9：检查组件开启时的发现、配置、源码和 ELF |
| [create-component-application.txt](complete/create-component-application.txt) | P013 13.1.5：创建调用组件的独立应用，已有目标不覆盖 |
| [create-greeting-component.txt](complete/create-greeting-component.txt) | P013 13.1.1：创建普通组件，已有目标不覆盖 |
