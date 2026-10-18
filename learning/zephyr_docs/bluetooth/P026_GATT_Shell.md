---
id: learning.zephyr-docs.bluetooth.page-26
title: GATT_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/host/gatt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-gatt-shell"></a>

# 第26章\_GATT\_Shell

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/host/gatt.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——使用前提：以下命令在启用了对应蓝牙功能的目标固件Zephyr Shell中执行，初始化与接入方式见[蓝牙Shell](P007_蓝牙Shell.md)。代码中的 `uart:~$` 是提示符，其后输出是原文预期结果；输入命令时不复制提示符和日志。若命令不可用或初始化失败，应先检查目标配置、控制器能力及当前版本帮助，再继续连接或传输步骤。本批仅翻译与核对文档，未连接设备或执行这些命令。

下例假设两台设备已建立连接。通用属性配置文件（Generic Attribute Profile，GATT）Shell用于发现、订阅、通知及交换MTU等操作。

客户端（Client）用 `gatt discover` 发现服务，应打印GATT服务端（Server）提供的全部服务。

服务端用 `gatt register` 注册预定义测试服务。完成后，客户端重新运行发现命令，应看到新加入的服务。

然后可在客户端订阅这些服务。订阅测试服务的示例如下：

```text
uart:~$ gatt subscribe 26 25
Subscribed
```

> 译注——句柄顺序与进制：[官方cmd_subscribe实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/host/shell/gatt.c)把第一个参数按十六进制解析为客户端特征配置（Client Characteristic Configuration，CCC）句柄，第二个解析为特征值句柄。因此此处是CCC句柄0x26、值句柄0x25；应以实际发现结果替换，不能把26／25固定套到任意服务。Subscribed表示订阅已建立。

服务端随后可用 `gatt notify` 向客户端发送通知（Notification）。

GATT命令还可发起最大传输单元（Maximum Transmission Unit，MTU）交换，命令为 `gatt exchange-mtu`。如果要改变Shell支持的最大MTU，应修改Shell配置文件中的Kconfig选项；详见[MTU更新示例](../bluetooth_samples/P011_MTU更新.md#bluetooth_mtu_update)。


对应官方文档源码：[doc/services/connectivity/bluetooth/shell/host/gatt.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/host/gatt.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/bluetooth/shell/host/gatt.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：GAP_Shell](P025_GAP_Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：L2CAP_Shell](P027_L2CAP_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P025_GAP_Shell.md) · [返回大纲](大纲.md) · [下一章](P027_L2CAP_Shell.md)

</details>

<!-- reading-navigation:end -->
