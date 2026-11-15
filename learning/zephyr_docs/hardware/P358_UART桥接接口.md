---
id: learning.zephyr-docs.hardware.uartutil-0
title: UART桥接接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__bridge_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第358章\_UART桥接接口

原文：[uart__bridge_8h](https://docs.zephyrproject.org/latest/doxygen/html/uart__bridge_8h.html)。读取日期：2026-10-13，`latest`。

## 358.1\_传播端口设置

`zephyr/drivers/uart/uart_bridge.h` 提供通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的桥接（Bridge）设置更新函数，原头文件包含 `zephyr/device.h`。

桥接把两个端口相连；该函数让其中一个端口的配置传递到另一个端口，而不是直接传输数据。

## 358.2\_更新硬件端口

函数声明为：

```c
void uart_bridge_settings_update(const struct device *dev,
                                  const struct device *bridge_dev);
```

若 `dev` 属于 `bridge_dev`，将 `dev` 的 UART 配置应用到该桥接中的另一个设备。这样可把通用串行总线（Universal Serial Bus，USB）通信设备类（Communication Device Class，CDC）的抽象控制模型（Abstract Control Model，ACM）端口设置传播到硬件 UART。

若 `dev` 不属于 `bridge_dev`，此函数不执行任何操作。函数无返回值，原页没有列出其他错误处理约定。

---

[上一章：MSPM0UART设备树常量](P357_MSPM0UART设备树常量.md) · [下一章：UART模拟控制接口](P359_UART模拟控制接口.md) · [返回大纲](大纲.md)
