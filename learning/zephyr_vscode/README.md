---
id: zephyr-vscode-index
title: VS Code Zephyr IDE 教程导航
kind: reference
status: maintained
domains: [zephyr, vscode, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# VS Code Zephyr IDE 教程

先读 [PPT](P001_VSCode_Zephyr_IDE接入已有工程_Windows.pptx) 或 [同名正文](P001_VSCode_Zephyr_IDE接入已有工程_Windows.md)。二者沿同一条路线讲解：Zephyr 自己提供哪些构建输入，Mylonics 的 IDE for Zephyr 怎样把这些输入变成可点击的工程和 Build，以及每一步保存到哪里。

资料目录为 `F:/git_storage/zephyr_hc32f4a0/learning/zephyr_vscode`。主线工作区为 `G:/zephyr_practice`，VS Code 打开其下 `zephyr-main`。已有 SDK、venv 和模块继续复用。插件按本机 `mylonics.zephyr-ide` **4.1.1** 的设置声明和实现核对；界面版本变化时按扩展 ID 和完整设置键定位。

| 当前要做的事 | 阅读位置 |
| --- | --- |
| 从头认识职责、找到入口、完成已有工程接入 | [主教程](P001_VSCode_Zephyr_IDE接入已有工程_Windows.md) |
| 在“设置”里找不到文章所说的按钮 | [入口与配置地图](RESET_WALKTHROUGH.md) |
| 已接入，但环境、Build 或代码跳转不对 | [按结果定位的行动指南](ACTION_GUIDE.md) |
| 查完整设置键、默认值、Build/Runner 字段 | [配置参考](CONFIGURATION_REFERENCE.md) |
| 复制命令或配置 | [命令索引](commands/README.md)；先区分主线示例和历史诊断副本 |
| 查哪些步骤有证据、哪些尚未实测 | [验证记录](VALIDATION.md) |

原生工程的准备顺序是 [P004 CMSIS 选择与下载](../P01_zephyr_make_project/P004_CMSIS选择与下载_Windows.md) → [P005 工程组织与驱动模型](../P01_zephyr_make_project/P005_Zephyr工程组织与驱动模型_Windows.md) → [P006 HC32 / DDL 与外部模块](../P01_zephyr_make_project/P006_HC32与外部源码模块接入_Windows.md)。先理解输入与驱动责任，再在本教程中对应到插件操作。

本教程只采用一组构建标识：应用 `samples/hello_world`、板 `mps2/an386`、Build 名 `ide-mps2`、输出 `build/learning-tools/zephyr-vscode/hello_world`。CMSIS 由已有 west 清单与模块发现接入；自有 HAL 放在 `G:/zephyr_practice/hal_xhsc-zephyr`，通过独立的模块接入示例说明。hello_world 的构建结果不代表 HC32 板级支持已经完成。

2026-10-10 已撤回旧版“72 张实机截图、完整 GUI 编译实测”的证据声明：旧截图多数内容重复，不能支持逐步操作结论。现行教程不再引用这批图片。具体核验与保留范围见 [验证记录](VALIDATION.md)。

本轮重新核对并保留7张真实入口截图，展示两类Settings、Workspace信息，以及**点CMake Args后先West参数、再CMake参数**的两步向导。[入口地图](RESET_WALKTHROUGH.md)配有连续操作说明；画面中的历史Build名和旧模块参数仅用于定位，不作为现行模板。图片来源和摘要见[图片记录](assets/README.md)。
