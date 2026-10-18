---
id: learning.zephyr-docs.hardware.uartemul-0
title: UART模拟接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__uart__emul__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第341章\_UART模拟接口

原文：[group__uart__emul__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__emul__interface.html)。读取日期：2026-10-13，`latest`。

## 341.1\_模拟驱动入口

本组提供通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的模拟（Emulation）接口，公开声明来自 `zephyr/drivers/uart_emul.h`。[`uart_emul`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__emul.html) 是 UART 设备模拟器链表节点，[`uart_emul_device_api`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__emul__device__api.html) 定义模拟器的应用程序编程接口（Application Programming Interface，API）。

## 341.2\_发送数据就绪回调

模拟回调（Callback）类型 [`uart_emul_device_tx_data_ready_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__emul__interface.html#gab4b5940f6e0c55c594a9ccddae04c8ae) 的签名为：

```c
typedef void (*uart_emul_device_tx_data_ready_t)(const struct device *dev,
                                                size_t size,
                                                const struct emul *target);
```

`dev` 是 UART 设备实例，`size` 是发送（Transmit，TX）缓冲区中可用的字节数，`target` 指向模拟上下文（Emulation Context）。回调没有返回值。

## 341.3\_注册模拟设备

[`uart_emul_register`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__emul__interface.html#gaa457b7ca5ac20a588a6fce562221e824) 在控制器上注册一个模拟设备：

```c
int uart_emul_register(const struct device *dev, struct uart_emul *emul);
```

`dev` 是将使用模拟器的设备，[`emul`](P477_仿真器实例结构.md) 是待使用的 UART 模拟器。返回 0 表示成功；原页没有列出其他返回码。

---

[上一章：UART事件数据联合体](P340_UART事件数据联合体.md) · [下一章：UART模拟器结构](P342_UART模拟器结构.md) · [返回大纲](大纲.md)
