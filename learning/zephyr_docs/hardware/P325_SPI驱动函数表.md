---
id: learning.zephyr-docs.hardware.spiback-1
title: SPI驱动函数表
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structspi__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第325章\_SPI驱动函数表

原文：[structspi__driver__api](https://docs.zephyrproject.org/latest/doxygen/html/structspi__driver__api.html)。读取日期：2026-10-13，`latest`。

## 325.1\_驱动操作表的职责

[`spi_driver_api`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__driver__api.html) 是所有串行外设接口（Serial Peripheral Interface，SPI）驱动都需要定义的操作结构，声明来自 `zephyr/drivers/spi.h`。它保存驱动实现的操作函数指针，以及其他驱动专用常量数据。

标为必需（Required，REQ）的成员必须由驱动设置；标为可选（Optional，OPT）的成员可以不实现。应用程序编程接口（Application Programming Interface，API）通过这张表访问具体驱动。

## 325.2\_必需与可选操作

| 字段 | 类型 | 要求与功能 |
| --- | --- | --- |
| <a id="abeb852d35e4772dcec716cf63ef307bb"></a>[`transceive`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__driver__api.html#abeb852d35e4772dcec716cf63ef307bb) | [`spi_api_io`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface__backend.html#ga3fc669f866b03cfdad98754de69cda13) | REQ：读写指定数量的数据 |
| <a id="af067daa58e79b9067a59fedcfd61034b"></a>[`transceive_async`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__driver__api.html#af067daa58e79b9067a59fedcfd61034b) | [`spi_api_io_async`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface__backend.html#ga03be7f33032ac479153616bbe26848e7) | OPT：异步读写指定数量的数据；仅在启用 Kconfig 配置项 [`CONFIG_SPI_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_ASYNC) 时存在 |
| <a id="af88a1a6b823d5742b099170eb3b2e38a"></a>[`iodev_submit`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__driver__api.html#af88a1a6b823d5742b099170eb3b2e38a) | [`spi_api_iodev_submit`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface__backend.html#gae274c0d704e8fd8993631fc1b91bfcb1) | OPT：向 SPI 设备提交请求；仅在启用 Kconfig 配置项 [`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO) 时存在 |
| <a id="ae15944912ece9f736fd935184e8a184d"></a>[`release`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__driver__api.html#ae15944912ece9f736fd935184e8a184d) | [`spi_api_release`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface__backend.html#gac651ff7cd3dde7abe2525e20ef2e9e7d) | REQ：释放当前配置锁定的 SPI 设备和/或片选（Chip Select，CS） |

异步（Asynchronous）传输启动后通过通知报告完成；实时输入输出（Real-Time Input/Output，RTIO）使用提交请求的方式安排操作。上表给出的配置条件是对应字段的可用条件，不能忽略条件后假定所有构建都有同样布局。

原页相关入口为设备定义宏 `DEVICE_DT_INST_DEFINE`、`DEVICE_DT_DEFINE` 及接口定义宏 `DEVICE_API`。

---

[上一章：SPI驱动后端接口](P324_SPI驱动后端接口.md) · [下一章：SPI模拟接口](P326_SPI模拟接口.md) · [返回大纲](大纲.md)
