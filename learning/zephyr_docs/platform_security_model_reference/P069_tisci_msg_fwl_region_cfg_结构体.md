---
id: learning.zephyr-docs.platform-security-model-reference.page-69
title: tisci_msg_fwl_region_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtisci__msg__fwl__region__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_tisci\_msg\_fwl\_region\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtisci__msg__fwl__region__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

防火墙设置（Firewall Settings）的请求和响应。

```c
#include <zephyr/drivers/firmware/tisci/tisci.h>
```

<a id="details"></a>

防火墙设置（Firewall settings）的请求和响应。

参数（Parameters）：

- `fwl_id`：目标防火墙的 ID。
- `region`：要设置配置信息的区域号或通道号。简单防火墙不使用此字段，必须将其初始化为零。对于基于区域的防火墙，该字段表示目标区域，索引从 0 开始；对于基于通道的防火墙，该字段表示目标通道，索引从 0 开始。
- `n_permission_regs`：要设置的权限寄存器数量。
- `control`：要写入防火墙 `CONTROL` 寄存器的内容。
- `permissions`：要写入防火墙 `PERMISSION` 寄存器的内容。
- `start_address`：要写入防火墙 `START_ADDRESS` 寄存器的内容。
- `end_address`：要写入防火墙 `END_ADDRESS` 寄存器的内容。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/tisci/tisci.h`

## 69.1\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/tisci/tisci.h](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h_source.html)

<a id="header-details"></a>

---

[上一章](P068_tisci_msg_fwl_region_结构体.md) · [返回大纲](大纲.md) · [下一章](P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md)
