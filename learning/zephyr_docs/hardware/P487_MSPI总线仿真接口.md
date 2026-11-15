---
id: learning.zephyr-docs.hardware.emulbus-2
title: MSPI总线仿真接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__emul__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第487章\_MSPI总线仿真接口

原文：[group__mspi__emul__interface](P487_MSPI总线仿真接口.md)。读取日期：2026-10-13，`latest`。

本页介绍**多线串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）**仿真驱动的公共**应用程序编程接口（Application Programming Interface，API）**。所有类型及函数均由 `zephyr/drivers/mspi_emul.h` 声明。

## 487.1\_设备与控制器对象

[`emul_mspi_device_api`](P483_MSPI仿真设备API结构.md) 定义 MSPI 设备仿真器 API；[`mspi_emul`](P489_MSPI仿真器链表节点.md) 是 MSPI 设备仿真器链表中的节点；[`emul_mspi_driver_api`](P484_MSPI仿真驱动API结构.md) 定义 MSPI 控制器仿真器 API。

下面的函数指针类型分别负责将收发请求交给设备仿真器、按设备索引查找仿真器，以及在控制器侧触发事件。`-EIO` 表示通用**输入/输出错误（Input/Output Error）**。

## 487.2\_收发回送接口

没有实际硬件连接时，[`emul_mspi_dev_api_transceive`](P487_MSPI总线仿真接口.md) 将 MSPI **收发（Transceive）**请求回送给设备仿真器，即使用**回环（Loopback）**路径处理请求。

```c
typedef int (*emul_mspi_dev_api_transceive)(
    const struct emul *target,
    const struct mspi_xfer_packet *packets,
    uint32_t num_packet, bool async, uint32_t timeout);
```

| 参数 | 官方说明译文 |
| --- | --- |
| `target` | 设备仿真器实例 |
| `packets` | 指向包含命令、地址、数据等内容的缓冲区 |
| `num_packet` | `packets` 中的数据包数量 |
| `async` | 标明这是否为异步请求（Asynchronous Request） |
| `timeout` | 该请求允许的最长时间 |

成功返回 `0`；通用输入/输出错误返回 `-EIO`。

> 译注：参数声明明确使用 `const struct mspi_xfer_packet *`，因此 `packets` 是传输数据包结构的指针。原页没有给出 `timeout` 的时间单位或特殊值，不能自行补成毫秒等单位。

## 487.3\_按设备索引查找

[`mspi_emul_find_emul`](P487_MSPI总线仿真接口.md) 查找 MSPI 总线上存在的仿真器。原文说明，目前它只用于查找主机设备的仿真器，在包含**串行外设接口闪存（Serial Peripheral Interface Flash，SPI Flash）**芯片的系统中也可能有用。

```c
typedef struct mspi_emul *(*mspi_emul_find_emul)(const struct device *dev,
                                                uint16_t dev_idx);
```

`dev` 是 MSPI 仿真控制器设备；`dev_idx` 是来自**设备树（Devicetree）**的设备索引（Device Index）。返回可使用的 [`mspi_emul`](P489_MSPI仿真器链表节点.md) 指针；找不到时返回空指针 `NULL`。

## 487.4\_控制器事件与注册

[`mspi_emul_trigger_event`](P487_MSPI总线仿真接口.md) 在 MSPI 控制器侧的仿真器上触发事件，从而调用相应的**回调（Callback）**函数。

```c
typedef int (*mspi_emul_trigger_event)(const struct device *dev,
                                       enum mspi_bus_event evt_type);
```

`dev` 是 MSPI 仿真控制器设备，`evt_type` 是待触发的事件类型，参见 [`mspi_bus_event`](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga4cd05950729893e08ef0d4a12e2242d5) 枚举。成功返回 `0`；通用输入/输出错误返回 `-EIO`。

[`mspi_emul_register()`](P487_MSPI总线仿真接口.md) 将被仿真的设备注册到控制器。

```c
int mspi_emul_register(const struct device *dev, struct mspi_emul *emul);
```

参数 `dev` 为 MSPI 仿真控制器设备，[`emul`](P477_仿真器实例结构.md) 为待注册的 MSPI 设备仿真器。原页明确说明：**总是返回 `0`，表示成功**。

---

[上一章：eSPI总线仿真接口](P486_eSPI总线仿真接口.md) · [下一章：eSPI仿真器链表节点](P488_eSPI仿真器链表节点.md) · [返回大纲](大纲.md)
