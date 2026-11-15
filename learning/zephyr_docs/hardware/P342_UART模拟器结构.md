---
id: learning.zephyr-docs.hardware.uartemul-1
title: UART模拟器结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuart__emul.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第342章\_UART模拟器结构

原文：[structuart__emul](https://docs.zephyrproject.org/latest/doxygen/html/structuart__emul.html)。读取日期：2026-10-13，`latest`。

## 342.1\_模拟设备链表节点

[`uart_emul`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__emul.html) 是通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）设备模拟器（Emulator）链表中的节点，声明来自 `zephyr/drivers/uart_emul.h`。它将链表节点、目标模拟器及设备接口关联起来。

## 342.2\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`node`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__emul.html#a5d363d3cd85e7fed7ce2f24f5a75243a) | [`sys_snode_t`](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493) | 控制器模拟器单向链表中的节点 |
| [`target`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__emul.html#ab0fa46fc3bae0c089555ca1045924e60) | `const struct emul *` | 目标模拟器；所有类型的模拟总线节点都必须提供 |
| [`api`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__emul.html#a6bf13a7090376d6f3419f5c6a6ca1608) | `const struct uart_emul_device_api *` | 此设备提供的应用程序编程接口（Application Programming Interface，API） |

---

[上一章：UART模拟接口](P341_UART模拟接口.md) · [下一章：UART模拟函数表](P343_UART模拟函数表.md) · [返回大纲](大纲.md)
