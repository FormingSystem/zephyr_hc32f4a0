---
id: zephyr-vscode-assets
title: Zephyr IDE 教程图片与图源
kind: reference
status: maintained
domains: [documentation]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 图片与图源

## 本轮实际核对的界面

`verified_20261010/`的7张JPG来自2026-10-10本机VS Code、Mylonics IDE for Zephyr 4.1.1。逐张检查了画面内容与所述入口，7个SHA-256各不相同，完整摘要记录在[sources.json](sources.json)。它们证明本轮实际查看的入口、字段与向导次序，不证明创建新工程、执行构建或操作硬件已成功。

| 图片 | 对应入口与阅读限制 |
| --- | --- |
| [01-native-settings.jpg](verified_20261010/01-native-settings.jpg) | 原生设置搜索`@ext:mylonics.zephyr-ide`，35项；图中为用户范围，按教程操作当前工程需切到工作区 |
| [02-open-settings-command.jpg](verified_20261010/02-open-settings-command.jpg) | 命令面板的Zephyr IDE: Open Settings；背后的旧JSON不是待复制示例 |
| [03-plugin-settings.jpg](verified_20261010/03-plugin-settings.jpg) | Directory Settings两条路径及每项Workspace选择 |
| [04-sidebar.jpg](verified_20261010/04-sidebar.jpg) | Project Details的CMake Args；历史Build名仅用于定位入口 |
| [05-workspace-information.jpg](verified_20261010/05-workspace-information.jpg) | Workspace Information的目录、venv与版本字段 |
| [06-build-args-west.jpg](verified_20261010/06-build-args-west.jpg) | 点击CMake Args后的第1步：West build arguments |
| [07-build-args-cmake.jpg](verified_20261010/07-build-args-cmake.jpg) | 按Enter后的第2步：CMake arguments；旧ZEPHYR_MODULES值不可当主线复制 |

参数向导查看后按Esc退出，没有保存输入或修改G盘配置。连续操作说明在[入口地图1.6](../RESET_WALKTHROUGH.md)，原生35项与插件自有31项的区别在[配置参考](../CONFIGURATION_REFERENCE.md)。

## 官方文档示意

下面三张图片于 2026-10-07 从 [Mylonics 插件仓库](https://github.com/mylonics/zephyr-ide) 的 develop 文档取得。它们用于历史外观参考，工程名、路径和按钮排列不构成本机 4.1.1 的逐屏操作证据。

| 本地图片 | 来源 |
| --- | --- |
| [main_build.png](main_build.png) | [Project/Build 示意](https://raw.githubusercontent.com/mylonics/zephyr-ide/develop/docs/media/main_build.png) |
| [workspace_setup.png](workspace_setup.png) | [工作区示意](https://raw.githubusercontent.com/mylonics/zephyr-ide/develop/docs/media/workspace_setup.png) |
| [sdk_install.png](sdk_install.png) | [SDK 示意](https://raw.githubusercontent.com/mylonics/zephyr-ide/develop/docs/media/sdk_install.png) |

摘要见 [sources.json](sources.json)。许可入口为 [上游 LICENSE](https://github.com/mylonics/zephyr-ide/blob/develop/LICENSE)。

## 失效的旧截图证据

`reset_demo/` 中保存的 91 张 JPG 经 2026-10-10 文件摘要核对，88 张具有完全相同的 SHA-256：`7b1914f04b1283ae58b6c0f9ee9c727005ba9ccdd6d428d1ae7a499ed1f70a0b`。其中名为 `36-build-success.jpg` 的图片内容不能证明构建成功。

这批文件保留供追溯，当前教程不再引用。不同文件名、文件存在或 Markdown 链接有效都不能证明画面内容正确；旧版“72 张实机操作截图”和相关 GUI 实测结论已撤回。目录中的 configuration-inventory.json 可作为旧设置清单快照，不能给截图内容或实际操作背书。当前设置以已安装插件定义重新核对。

## 封面与原生图解

`series-cover.png` 复用本系列芯片封面背景。PPT 中的关系表、代码和流程图保持可编辑；界面示意必须标明来源和版本。`diagram-*.mmd` 是历史 Mermaid 图源；使用前对照现行正文，避免从旧图重新引入已取消的接入路线。
