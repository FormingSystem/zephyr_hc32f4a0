---
id: learning.zephyr-docs.hardware.emulstruct-4
title: eSPI仿真设备API结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__device__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第481章\_eSPI仿真设备API结构

原文：[structemul__espi__device__api](https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__device__api.html)。读取日期：2026-10-13，`latest`。

`struct emul_espi_device_api` 定义**增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）**设备仿真器的**应用程序编程接口（Application Programming Interface，API）**，位于 `zephyr/drivers/espi_emul.h`。

## 481.1\_处理函数与配置条件

设备仿真器通过以下处理函数设置或取得**虚拟线（Virtual Wire，VW）**状态，以及取得 **高级配置与电源接口（Advanced Configuration and Power Interface，ACPI）**共享内存地址。虚拟线是在 eSPI 上传送的信号状态，**共享内存（Shared Memory，SHM）**则是接口所暴露的共享区域。

| 类型与字段 | 官方说明译文 |
| --- | --- |
| `emul_espi_api_set_vw set_vw` | eSPI 虚拟线设置处理函数 |
| `emul_espi_api_get_vw get_vw` | eSPI 虚拟线读取处理函数 |
| `emul_espi_api_get_acpi_shm get_acpi_shm` | ACPI 共享内存地址读取处理函数 |

**注意：**只有启用 Kconfig 配置项 [`CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION) 时，[`get_acpi_shm`](https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__device__api.html#a9f74d3b4f647bfb756fdf92851a64f86) 才可用。该配置控制 eSPI 外设的 ACPI 共享内存区域支持。

---

[上一章：无总线仿真器桩结构](P480_无总线仿真器桩结构.md) · [下一章：eSPI仿真驱动API结构](P482_eSPI仿真驱动API结构.md) · [返回大纲](大纲.md)
