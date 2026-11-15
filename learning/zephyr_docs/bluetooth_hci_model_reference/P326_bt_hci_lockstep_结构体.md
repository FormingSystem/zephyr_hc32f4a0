---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-326
title: bt_hci_lockstep_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__lockstep.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第326章\_bt\_hci\_lockstep\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__lockstep.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

锁步辅助对象（Lockstep Helper）。

```c
#include <zephyr/drivers/bluetooth/hci_lockstep.h>
```

<a id="details"></a>

锁步辅助对象（Lockstep Helper）。使用前应调用 `bt_hci_lockstep_init()` 初始化。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 326.1\_数据成员（Data Fields）

<a id="r_a6af9d44ebb27dab6971b99c39ba9b747"></a>

```c
k_timeout_t timeout
```

相关声明：[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[timeout](#a6af9d44ebb27dab6971b99c39ba9b747)。

命令超时（Command Timeout）。

## 326.2\_详细说明（Detailed Documentation）

<a id="a6af9d44ebb27dab6971b99c39ba9b747"></a>

### `timeout`

```c
k_timeout_t bt_hci_lockstep::timeout
```

命令超时（Command Timeout）。

`bt_hci_lockstep_cmd_send_sync()` 等待控制器允许发送命令、然后等待其响应的总时间。`bt_hci_lockstep_init()` 将其设为 10 秒，与蓝牙主机自身的命令超时一致；驱动可以随后修改该值。

本结构体文档由以下文件生成：

- `zephyr/drivers/bluetooth/hci_lockstep.h`

## 326.3\_原页交叉引用（Cross References）

- [zephyr/drivers/bluetooth/hci_lockstep.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__lockstep_8h_source.html)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [bt_hci_lockstep_init()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#ga02ea7a0ad2bbb7d8ee9845122e34f8ab)
- [bt_hci_lockstep_cmd_send_sync()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#gaa53d7b9aa5a7d6c5f11ea442c37f75d8)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P325_bt_hci_le_read_min_supported_conn_interval_group_结构体.md) · [返回大纲](大纲.md) · [下一章](P327_bt_hci_mesh_pattern_结构体.md)
