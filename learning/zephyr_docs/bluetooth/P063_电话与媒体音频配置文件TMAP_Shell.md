---
id: learning.zephyr-docs.bluetooth.page-63
title: 电话与媒体音频配置文件TMAP_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/tmap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-telephone-and-media-audio-profile-shell"></a>

# 第63章\_蓝牙：电话与媒体音频配置文件 Shell（Bluetooth: Telephone and Media Audio Profile Shell）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/tmap.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——操作上下文：代码块中的命令在启用了相应音频功能的目标固件 Zephyr Shell 中执行，接入与初始化见[蓝牙 Shell](P007_蓝牙Shell.md)。`uart:~$` 是提示符，后续日志是官方预期输出；不要把提示符、日志或 `<address>` 等占位符原样当作主机终端命令运行。各示例代表不同角色和操作分支，按实际连接与初始化状态选择，不连贯粘贴整章。命令缺失、初始化失败或发现未完成时，应先核对固件配置、控制器能力及当前版本帮助，再继续后续操作。

> 译注——版本与验证：原文“当前”“尚未实现”等表述均保留其快照语境。代码块完整保留原始命令、帮助和输出，本文没有执行固件构建、连接音频设备或验证互操作性。

本文说明如何运行电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）功能。与大多数较低层配置文件不同，TMAP 在所有参与设备上都存在，并具有电话与媒体音频服务（Telephone and Media Audio Service，TMAS）。因此，发起方与接受方，或中心设备与外围设备，都应发现远端设备的 TMAS，确定其支持的 TMAP 角色。

<a id="using-the-tmap-shell"></a>

## 63.1 使用 TMAP Shell（Using the TMAP Shell）

蓝牙协议栈完成初始化（`bt init`）后，可以调用 `tmap init` 注册 TMAS。

```text
tmap --help
tmap - Bluetooth TMAP shell commands
Subcommands:
  init          :Initialize and register the TMAS
  discover      :Discover TMAS on remote device
```

对应官方文档源码：[doc/services/connectivity/bluetooth/shell/audio/tmap.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/audio/tmap.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/shell/audio/tmap.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件或连接音频设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：电话承载服务TBS_Shell](P062_电话承载服务TBS_Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Linux上的AutoPTS](P064_Linux上的AutoPTS.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P062_电话承载服务TBS_Shell.md) · [返回大纲](大纲.md) · [下一章](P064_Linux上的AutoPTS.md)

</details>

<!-- reading-navigation:end -->
