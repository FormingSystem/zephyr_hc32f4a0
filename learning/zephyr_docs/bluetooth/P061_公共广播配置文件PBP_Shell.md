---
id: learning.zephyr-docs.bluetooth.page-61
title: 公共广播配置文件PBP_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/pbp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-public-broadcast-profile-shell"></a>

# 第61章\_蓝牙：公共广播配置文件 Shell（Bluetooth: Public Broadcast Profile Shell）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/pbp.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——操作上下文：代码块中的命令在启用了相应音频功能的目标固件 Zephyr Shell 中执行，接入与初始化见[蓝牙 Shell](P007_蓝牙Shell.md)。`uart:~$` 是提示符，后续日志是官方预期输出；不要把提示符、日志或 `<address>` 等占位符原样当作主机终端命令运行。各示例代表不同角色和操作分支，按实际连接与初始化状态选择，不连贯粘贴整章。命令缺失、初始化失败或发现未完成时，应先核对固件配置、控制器能力及当前版本帮助，再继续后续操作。

> 译注——版本与验证：原文“当前”“尚未实现”等表述均保留其快照语境。代码块完整保留原始命令、帮助和输出，本文没有执行固件构建、连接音频设备或验证互操作性。

本文说明如何运行公共广播配置文件（Public Broadcast Profile，PBP）的功能。PBP 没有关联的服务；它用于更快、更高效地发现采用常见编解码器配置传输音频的广播发送端。

<a id="using-the-pbp-shell"></a>

## 61.1 使用 PBP Shell（Using the PBP Shell）

蓝牙协议栈完成初始化（`bt init`）后，即可运行 PBP。调用 `pbp set_features`，设置公共广播公告（Public Broadcast Announcement）的功能位。

```text
pbp --help
pbp - Bluetooth PBP shell commands
Subcommands:
  set_features    :Set the Public Broadcast Announcement features
```

对应官方文档源码：[doc/services/connectivity/bluetooth/shell/audio/pbp.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/audio/pbp.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/shell/audio/pbp.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件或连接音频设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：媒体控制配置文件MCP_Shell](P060_媒体控制配置文件MCP_Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：电话承载服务TBS_Shell](P062_电话承载服务TBS_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P060_媒体控制配置文件MCP_Shell.md) · [返回大纲](大纲.md) · [下一章](P062_电话承载服务TBS_Shell.md)

</details>

<!-- reading-navigation:end -->
