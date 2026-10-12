---
id: zephyr-vscode-commands
title: Zephyr IDE 可复制操作索引
kind: reference
status: maintained
domains: [zephyr, vscode, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 可复制操作

以 [现行主教程](../P001_VSCode_Zephyr_IDE接入已有工程_Windows.md) 为操作顺序。TXT 是注明终端的命令，JSON 是配置内容。先核对当前磁盘路径，再合并已有文件；不要把多个 JSON 对象顺次覆盖到同一个设置文件。

主线应用为 `samples/hello_world`、板为 `mps2/an386`、Build 名为 `ide-mps2`、输出为 `build/learning-tools/zephyr-vscode/hello_world`。相对路径从 VS Code 打开的 `G:/zephyr_practice/zephyr-main` 计算。SDK 实际解压目录必须先核对，不能把历史扁平目录假定为仍有效。

| 文件 | 使用位置 |
| --- | --- |
| [01-check-environment.txt](01-check-environment.txt) | 环境只读检查 |
| [02-launch-vscode.txt](02-launch-vscode.txt) | 可选终端继承诊断；日常从桌面打开 VS Code 不要求执行 |
| [03-settings.json](03-settings.json) | 合并本地 venv、SDK 查找路径等工作区设置 |
| [04-zephyr-ide.example.json](04-zephyr-ide.example.json) | Project/Build 结构参考；保留已有其他项目 |
| [05-build-cli.txt](05-build-cli.txt) | 对照插件 Build 的命令行输入；写入独立输出 |
| [06-cpp-settings.json](06-cpp-settings.json) | Microsoft C/C++ 读取本次构建数据库 |
| [07-create-app.txt](07-create-app.txt) | 目标不存在时，从官方应用复制自己的练习 |
| [08-settings-existing.json](08-settings-existing.json) | 设置合并参考；与03不是依次执行的安装步骤 |
| [09-settings-after-build.json](09-settings-after-build.json) | 编译成功后数据库路径参考 |

以下文件保留为历史诊断材料，**不属于当前主线，也不是 GUI 验证证据**：

| 历史文件 | 使用限制 |
| --- | --- |
| [10-local-cmsis-project.json](10-local-cmsis-project.json) | ide-local-cmsis 的完整显式模块列表诊断；ZEPHYR_MODULES 替换自动发现，不能当任意板的通用配置 |
| [12_gui_verified_settings.json](12_gui_verified_settings.json) | 旧设置副本；文件名 gui_verified 不再代表 GUI 已验证，勿整份覆盖当前设置 |
| [13_gui_verified_project.json](13_gui_verified_project.json) | 旧项目副本；不同 Build 名、显式模块和额外引号均不作为当前通用模板 |

补充材料按主教程的具体分支使用，不要求首次接入时全部执行：

| 文件 | 使用位置及影响 |
| --- | --- |
| [11-local-cmsis-build.txt](11-local-cmsis-build.txt) | 不用west时直接运行原生CMake；显式只列CMSIS，输出hello_world-native，与主线分开 |
| [14-west-projects.txt](14-west-projects.txt) | 只读查看当前west清单项目和版本 |
| [15-init-local-west.txt](15-init-local-west.txt) | 确认没有现成.west时，初始化本地west工作区；不是已有工程的刷新操作 |
| [16-update-cmsis.txt](16-update-cmsis.txt) | 核对原生Git及工作区后，定向更新cmsis_6；会同步仓库 |
| [17-hc32-extra-modules.json](17-hc32-extra-modules.json) | 已具备完整HC32板/SoC适配的应用追加HAL模块；不能单独让mps2变成HC32 |
| [18-sdk-cmake-args.json](18-sdk-cmake-args.json) | 需要固定本次SDK时使用的CMake参数片段 |
| [19-verify-build.txt](19-verify-build.txt) | 只读核对主线Build的产物、缓存和编译数据库 |
| [20-read-app-target.txt](20-read-app-target.txt) | 只读应用 CMake/prj.conf/main.c 与 MPS2 板输入 |
| [21-hc32-build-fragment.json](21-hc32-build-fragment.json) | 材料齐全后把 ide-hc32 成员合并到已有 hello_world 的 buildConfigs，不覆盖全文件 |
| [22-check-hc32-inputs.txt](22-check-hc32-inputs.txt) | HC32 输入只读检查与显式板/SoC 根查询，缺项即停止 |

旧12/13保留便于已有链接追溯。GUI 验证声明的撤回依据见 [验证记录](../VALIDATION.md)。当前新增 HAL 的方式使用 `EXTRA_ZEPHYR_MODULES`，完整操作以主教程为准。
