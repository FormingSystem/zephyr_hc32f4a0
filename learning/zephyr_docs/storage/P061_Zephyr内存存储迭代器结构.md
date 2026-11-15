---
id: learning.zephyr-docs.storage.zmsapi-4
title: Zephyr内存存储迭代器结构
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第61章\_Zephyr内存存储迭代器结构

原文：[structzms__iter](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html)。读取日期：2026-10-13，`latest`。

## 61.1\_不透明迭代状态

`struct zms_iter` 是**Zephyr 内存存储（Zephyr Memory Storage，ZMS）**供 [`zms_iter_next()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gaba4e19c06a27a5287e9f8507a4fa11c3) 与 [`zms_iter_next_all()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gaa37ba625bd4835acf772b0cdb38a3348) 使用的**不透明迭代器状态（Opaque Iterator State）**，声明于 `zephyr/kvss/zms.h`。

**使用前必须通过 [`zms_iter_init()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga7ca762e1b37186a2a2bf1dce5333272d) 或 [`zms_iter_init_with_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga2c839e3cceb3fd4931a2ffc26726ca34) 初始化，不要直接访问字段。** 下表对应官方结构参考，用于理解状态含义。

## 61.2\_字段参考

**分配表条目（Allocation Table Entry，ATE）**按环组织。**谓词（Predicate）**是用于筛选标识符的回调判定。

| 字段 | 类型 | 中文说明 |
| --- | --- | --- |
| [`walk_addr`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#ac7192fda17eabc58698615936691b89d) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | ATE 环中当前遍历地址 |
| [`end_addr`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#a998147073d23464bf69077e47269f0de) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 初始化迭代器时取得的 `ate_wra` 快照（Snapshot） |
| [`mask_id`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#a8a55a1e4aad54e9afed4da41813a2bd2) | [`zms_id_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga0509b3dce3030a56ecff866d693944f9) | 用于筛选返回条目的标识符掩码（ID Mask） |
| [`min_id`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#aac50c79d889b0954df0cbb781747ef8d) | [`zms_id_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga0509b3dce3030a56ecff866d693944f9) | 接受的最小标识符，包含该值 |
| [`max_id`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#a1d2a58a6567d7143466372367e5cf73a) | [`zms_id_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga0509b3dce3030a56ecff866d693944f9) | 接受的最大标识符，包含该值 |
| [`predicate_func`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#a14cf09843ce4046d541d4a5f7990685e) | [`zms_iter_predicate_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga73c4c209bc4fbb8125781088b15eef64) | 用于筛选标识符的可选回调 |
| [`exhausted`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#afaabf24d2be5a633c3370d9949abaacd) | [`bool`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b) | 完成整个环的遍历后为 `true` |
| [`previous_sector_num`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#a2bbec3cf7aede64963a2bd2c5f03805a) | `int` | 上一个遇到的 ATE 所在扇区；缓存该值，避免每一步都重新读取循环计数 |
| [`current_cycle`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#a958cec07dd78062c93c9db7f2ccb2370) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | `previous_sector_num` 指定扇区的循环计数（Cycle Count） |

---

[上一章：Zephyr内存存储实例结构](P060_Zephyr内存存储实例结构.md) · [下一章：Zephyr内存存储迭代配置](P062_Zephyr内存存储迭代配置.md) · [返回大纲](大纲.md)
