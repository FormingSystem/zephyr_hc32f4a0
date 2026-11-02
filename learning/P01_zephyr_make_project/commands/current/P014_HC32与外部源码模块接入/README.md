# P014_HC32与外部源码模块接入：当前命令索引

命令逐块取自[当前正文](../../../P014_HC32与外部源码模块接入.md)。先读正文前提，只执行所选环境与路线，不批量执行本目录。

| 操作 | 终端 | 所属讲解 | 内容 |
| --- | --- | --- | --- |
| 001 | bash | 13.3_获取并核验持续使用的 HAL 源码 | [完整命令](001-bash.txt) |
| 002 | bash | 13.3_获取并核验持续使用的 HAL 源码 | [完整命令](002-bash.txt) |
| 003 | bash | 13.3_获取并核验持续使用的 HAL 源码 | [完整命令](003-bash.txt) |
| 004 | bash | 13.3_获取并核验持续使用的 HAL 源码 | [完整命令](004-bash.txt) |
| 005 | bash | 13.3.1_已有目录优先的获取分支 | [完整命令](005-bash.txt) |
| 006 | bash | 13.5.5_先验证默认发现，再按目标检查额外模块 | [完整命令](006-bash.txt) |
| 007 | bash | 13.5.5_先验证默认发现，再按目标检查额外模块 | [完整命令](007-bash.txt) |
| 008 | bash | 13.6.1_复制适配模块并接入硬件搜索根 | [完整命令](008-bash.txt) |
| 009 | bash | 13.6.4_为这块板选择 hello_world 并配置构建 | [完整命令](009-bash.txt) |
| 010 | bash | 13.6.4_为这块板选择 hello_world 并配置构建 | [完整命令](010-bash.txt) |
| 011 | bash | 13.6.4_为这块板选择 hello_world 并配置构建 | [完整命令](011-bash.txt) |

## 配套完整操作

下列操作保留已验证实验的目录名，按当前正文前提选择；不能批量执行。与上面的逐块命令相比，它们包含创建文件或恢复必要环境的完整过程。

| 操作 | 说明 |
| --- | --- |
| [build-hc32-cmake.txt](complete/build-hc32-cmake.txt) | P014 14.6.4：相同 HC32 输入的直接 CMake 构建 |
| [build-hc32-manual-modules.txt](complete/build-hc32-manual-modules.txt) | P014 14.6.4：HC32 显式 CMSIS、HAL 与适配模块列表 |
| [build-hc32-west.txt](complete/build-hc32-west.txt) | P014 14.6.4：HC32 全部前提就绪后用 west 构建 |
| [check-hal-files.txt](complete/check-hal-files.txt) | P014 14.3：选择已有 HAL 根并核对模块入口及器件文件 |
| [copy-hc32-port.txt](complete/copy-hc32-port.txt) | P014 14.6.1：复制教材适配为工作副本，不覆盖现有目录 |
| [discover-default-modules.txt](complete/discover-default-modules.txt) | P014 14.5.5：读取默认 west 项目的模块发现结果 |
| [discover-extra-hal.txt](complete/discover-extra-hal.txt) | P014 14.5.5：在已核验 HAL 后检查额外模块发现 |
| [download-hal-fixed.txt](complete/download-hal-fixed.txt) | P014 14.3：没有可复用 HAL 时下载固定修订 |
| [fetch-hal-if-missing.txt](complete/fetch-hal-if-missing.txt) | P014 14.3.1：检查两个常用目录后才下载 HAL 的分支 |
| [query-hal-project.txt](complete/query-hal-project.txt) | P014 14.3：只读确认当前清单是否声明 hal_xhsc |
| [verify-hal-revision.txt](complete/verify-hal-revision.txt) | P014 14.3：选择实际 HAL 根并核对 Git 或原归档版本依据 |
