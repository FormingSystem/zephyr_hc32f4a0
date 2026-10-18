---
id: learning.zephyr-docs.hardware.spiback-3
title: SPI模拟器结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第327章\_SPI模拟器结构

原文：[structspi__emul](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html)。读取日期：2026-10-13，`latest`。

## 327.1\_控制器模拟器链表节点

[`spi_emul`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html) 表示串行外设接口（Serial Peripheral Interface，SPI）设备模拟器（Emulator）链表中的一个节点，声明来自 `zephyr/drivers/spi_emul.h`。它关联目标模拟器、片选与模拟器应用程序编程接口（Application Programming Interface，API）。

## 327.2\_字段与替身回退

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`node`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html#a4c49c2c9966eec74a9d010d22176bdd1) | [`sys_snode_t`](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493) | 控制器模拟器单向链表中的节点 |
| [`target`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html#a371b2447cf16752c191cc5a0aff26a57) | `const struct emul *` | 目标模拟器，所有总线模拟器都必须提供 |
| [`api`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html#a96649e8ea8360ad07ebbd721f999b0e7) | `const struct spi_emul_api *` | 此设备提供的实际 API |
| [`mock_api`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html#a4d174e7170a21e2f53c49e0da096a93e) | `struct spi_emul_api *` | 模拟替身（Mock）API；非 `NULL` 时优先于实际 API |
| [`chipsel`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html#a81450c3d7701c20da8d945e390e7cd33) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 模拟设备的 SPI 片选（Chip Select，CS）编号 |

设置 `mock_api` 后，如果它返回 `-ENOSYS`，会回退到默认的 `api`。因此，替身可以优先处理操作，也可以通过该返回值把操作交回默认实现。

---

[上一章：SPI模拟接口](P326_SPI模拟接口.md) · [下一章：SPI模拟函数表](P328_SPI模拟函数表.md) · [返回大纲](大纲.md)
