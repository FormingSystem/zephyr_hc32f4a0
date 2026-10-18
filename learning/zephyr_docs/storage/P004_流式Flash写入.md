---
id: learning.zephyr-docs.storage.stream-flash
title: 流式Flash写入
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/services/storage/stream/stream_flash.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第4章\_流式Flash写入

原文：[Stream Flash](https://docs.zephyrproject.org/latest/services/storage/stream/stream_flash.html)。读取日期：2026-10-12，`latest`。

**流式闪存写入（Stream Flash）**模块接收数据流中连续的片段，例如无线数据包内容，将它们汇集到调用者提供的缓冲区。缓冲区装满或数据流结束时，再写入原始 Flash 分区。模块还支持将读回缓冲区交给调用者，用于验证已持久化的数据流内容。

**设备固件升级（Device Firmware Upgrade，DFU）**过程中接收新固件镜像，是典型用途。

## 4.1\_使用缓冲写入的原因

某些设备受硬件限制，Flash 写入无法与无线接收、发送等操作并行；此外，减少写入操作次数也有助于改善应用观察到的响应时间。因此，可采用缓冲写入，而不是每到达一个数据片段就立即写 Flash。

## 4.2\_持久化写入进度

固件升级等流式写入可能持续很久。保存写入进度后，意外中断恢复时就可以从原来的位置继续。

Stream Flash 提供通过[设置子系统](P005_设置子系统.md)加载、保存、清除持久化进度的 **应用程序编程接口（Application Programming Interface，API）**，使用 Kconfig 配置项 `CONFIG_STREAM_FLASH_PROGRESS` 启用。

## 4.3\_API参考

接口见 [Stream to flash](../stream_flash_reference/P004_流式Flash公共接口.md)。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Flash循环缓冲区](P003_Flash循环缓冲区.md) · [本模块主线目录](../reading/storage.md) · [全部主线](../reading/README.md) · [下一篇：设置子系统](P005_设置子系统.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：Flash循环缓冲区](P003_Flash循环缓冲区.md) · [下一章：设置子系统](P005_设置子系统.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
