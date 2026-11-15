---
id: learning.zephyr-docs.hardware.mipibackend-2
title: MIPI显示串行后端
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第253章\_MIPI显示串行后端

原文：[group__mipi__dsi__interface__backend](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface__backend.html)。读取日期：2026-10-13，`latest`。

## 253.1\_用途

本组提供实现 MIPI **显示串行接口（Display Serial Interface，DSI）**驱动所需的 **应用程序编程接口（Application Programming Interface，API）**类型、回调签名（Callback Signature）及辅助内容，声明来自 `zephyr/drivers/mipi_dsi.h`。

驱动操作由[函数表](P254_MIPI显示串行函数表.md)提供，参数语义见[公共接口](P246_MIPI显示串行接口.md)。

## 253.2\_回调类型

以下为函数指针类型定义（Function Pointer Typedef）。

**类型 [`mipi_dsi_api_attach_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface__backend.html#ga9abb63e5c7cdb7597376a237a420c2b5)：将新设备连接到 DSI 总线。** 参数说明见函数 [`mipi_dsi_attach()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga18689fac223fddc10b23b6bc6712944e)。

```c
typedef int(* mipi_dsi_api_attach_t) (const struct device *dev, uint8_t channel, const struct mipi_dsi_device *mdev);
```

**类型 [`mipi_dsi_api_transfer_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface__backend.html#ga9ebc67e63c629c75ff61fa220a2787a0)：向总线上连接的设备传输数据或从其接收数据。** 参数说明见函数 [`mipi_dsi_transfer()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gace5bb52f483634baa185f46ac61efb71)。

```c
typedef ssize_t(* mipi_dsi_api_transfer_t) (const struct device *dev, uint8_t channel, struct mipi_dsi_msg *msg);
```

**类型 [`mipi_dsi_api_detach_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface__backend.html#gaf5e12800d2a80e8a78da16cb5a71b008)：将设备从 DSI 总线分离。** 参数说明见函数 [`mipi_dsi_detach()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gace728ac82d30e15868298facd6df0228)。

```c
typedef int(* mipi_dsi_api_detach_t) (const struct device *dev, uint8_t channel, const struct mipi_dsi_device *mdev);
```


---

[上一章：MIPI显示总线函数表](P252_MIPI显示总线函数表.md) · [下一章：MIPI显示串行函数表](P254_MIPI显示串行函数表.md) · [返回大纲](大纲.md)
