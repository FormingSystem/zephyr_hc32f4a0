---
id: learning.zephyr-docs.storage.zmsapi-3
title: Zephyr内存存储实例结构
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第60章\_Zephyr内存存储实例结构

原文：[structzms__fs](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html)。读取日期：2026-10-13，`latest`。

## 60.1\_实例与存储布局

`struct zms_fs` 是**Zephyr 内存存储（Zephyr Memory Storage，ZMS）**实例结构，声明于 `zephyr/kvss/zms.h`。它维护闪存位置、**扇区（Sector）**布局、**分配表条目（Allocation Table Entry，ATE）**写地址以及挂载状态。

| 字段 | 类型 | 中文说明 |
| --- | --- | --- |
| [`offset`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#af2dfcc5d0e8eabc5f116e2964668b05f) | [`off_t`](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f) | 文件系统在闪存中的偏移 |
| [`ate_wra`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a6c28786531454a050f81981d32ca3640) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | ATE 写入地址；高 4 字节对应扇区，低 4 字节为扇区内偏移 |
| [`data_wra`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a25f2b002e4189ee29432198991061b7a) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 数据写入地址 |
| [`sector_size`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#aae1ffd5eebd0bfb4c898719c221a239f) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 扇区大小；若设备具备擦除能力，必须是擦除块大小（Erase Block Size）的整数倍 |
| [`sector_count`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#ad8960c2cee8e03446aca96697c0c9e4a) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 文件系统的扇区数量 |
| [`mount_flags`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a41063275f2211115abf00c4dbceb45cc) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 来自 `enum zms_mount_flags` 的挂载行为标志 |
| [`sector_cycle`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#ab3b4551a3007e4b36bfd8a2fc209b543) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 由 [`ate_wra`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a6c28786531454a050f81981d32ca3640) 指向的活动扇区的当前循环计数（Cycle Counter） |

## 60.2\_运行状态与设备字段

**互斥锁（Mutex）**保护闪存写入。以下字段保存其初始化状态和设备相关数据：

| 字段 | 类型 | 中文说明 |
| --- | --- | --- |
| [`ready`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#af46a398f15fbb933d46c0b16283dae16) | [`bool`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b) | 文件系统是否已经初始化 |
| [`lock_initialized`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a352dad2283b804c1318748bd05efaf75) | [`bool`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b) | [`zms_lock`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#af524e7a105749a3dbff41a229c20443b) 是否已经初始化 |
| [`zms_lock`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#af524e7a105749a3dbff41a229c20443b) | `struct k_mutex` | 用于锁定闪存写操作的互斥锁 |
| [`flash_device`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a2628eaff292518933e037b871179b8ea) | `const struct device *` | 闪存设备运行时结构（Runtime Structure） |
| [`flash_parameters`](../flash_reference/P004_Flash存储参数结构.md) | `const struct flash_parameters *` | 闪存参数结构 |
| [`ate_size`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a939f1c9100dc9d2efdc163aea61e38a3) | `size_t` | 一个 ATE 的大小 |

---

[上一章：Zephyr内存存储接口](P059_Zephyr内存存储接口.md) · [下一章：Zephyr内存存储迭代器结构](P061_Zephyr内存存储迭代器结构.md) · [返回大纲](大纲.md)
