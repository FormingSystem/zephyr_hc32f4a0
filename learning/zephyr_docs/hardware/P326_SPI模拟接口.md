---
id: learning.zephyr-docs.hardware.spiback-2
title: SPI模拟接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第326章\_SPI模拟接口

原文：[group__spi__emul__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html)。读取日期：2026-10-13，`latest`。

## 326.1\_模拟设备的总线入口

本组是串行外设接口（Serial Peripheral Interface，SPI）的模拟（Emulation）接口。公开声明位于 `zephyr/drivers/spi_emul.h`，该文件提供 SPI 模拟驱动的应用程序编程接口（Application Programming Interface，API）。[`spi_emul`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html) 描述控制器模拟器链表中的一个设备，[`spi_emul_api`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul__api.html) 定义模拟器函数表。

## 326.2\_模拟收发回调

[`spi_emul_io_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html#ga034da8d578cd4facdff61ce3afb19487) 将 SPI 消息传给模拟器，由模拟器把读回的数据写入接收缓冲区：

```c
typedef int (*spi_emul_io_t)(const struct emul *target,
                             const struct spi_config *config,
                             const struct spi_buf_set *tx_bufs,
                             const struct spi_buf_set *rx_bufs);
```

`target` 为设备模拟器（Emulator）实例，`config` 指向有效的 [`spi_config`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__config.html) 配置结构；实现可能使用指针比较检测相对前次操作的变化。`tx_bufs` 为待发送数据来源的缓冲区数组，无数据时为 `NULL`；`rx_bufs` 为读入数据写入的缓冲区数组，无接收数据时为 `NULL`。

成功返回 0；`-EIO` 表示一般输入输出（Input/Output，I/O）错误。

## 326.3\_获取配置与注册模拟设备

[`spi_emul_get_config`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html#ga8b872edd18ec2911618919cc68229362) 提供旁路访问入口，让模拟器读取宿主控制器配置：

```c
uint32_t spi_emul_get_config(const struct device *dev);
```

`dev` 是与模拟器关联的 SPI 设备。返回值为按位打包的 32 位数值，包含设备运行时配置。

[`spi_emul_register`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html#ga6c782e1c480a9bf4640c82360e562703) 在控制器上注册模拟设备：

```c
int spi_emul_register(const struct device *dev, struct spi_emul *emul);
```

`dev` 是将使用模拟器的设备，[`emul`](P477_仿真器实例结构.md) 是要使用的 SPI 模拟器。原文明确说明始终返回 0，表示成功。

---

[上一章：SPI驱动函数表](P325_SPI驱动函数表.md) · [下一章：SPI模拟器结构](P327_SPI模拟器结构.md) · [返回大纲](大纲.md)
