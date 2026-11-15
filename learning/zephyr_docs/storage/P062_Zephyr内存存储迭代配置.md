---
id: learning.zephyr-docs.storage.zmsapi-5
title: Zephyr内存存储迭代配置
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第62章\_Zephyr内存存储迭代配置

原文：[structzms__iter__config](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html)。读取日期：2026-10-13，`latest`。

## 62.1\_配置用途与默认行为

`struct zms_iter_config` 是**Zephyr 内存存储（Zephyr Memory Storage，ZMS）**传给 [`zms_iter_init_with_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga2c839e3cceb3fd4931a2ffc26726ca34) 的**迭代器配置（Iterator Configuration）**，声明于 `zephyr/kvss/zms.h`。

保持 [`use_mask`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#aaa2fad64dd01813dfee027dac55fd43e)、[`use_range`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#a4a23feb82c0e0456839bcea5d6296e23) 和 [`use_predicate`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#a829f0fa76965955a302be4ccc0206150) 均为禁用，即采用默认行为：接受整个 [`zms_id_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga0509b3dce3030a56ecff866d693944f9) 类型范围内的所有标识符。

## 62.2\_过滤字段

**掩码过滤（Mask-based Filtering）**使用位掩码；**范围过滤（Range-based Filtering）**使用包含两端点的区间；**谓词过滤（Predicate Filtering）**调用布尔判定回调。

| 字段 | 类型 | 中文说明 |
| --- | --- | --- |
| [`mask_id`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#ae97b3ae143582a23288a914e011b42e1) | [`zms_id_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga0509b3dce3030a56ecff866d693944f9) | [`use_mask`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#aaa2fad64dd01813dfee027dac55fd43e) 为 `true` 时使用的掩码 |
| [`min_id`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#a966d6318cf92a10c0d0df092badc8d9a) | [`zms_id_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga0509b3dce3030a56ecff866d693944f9) | [`use_range`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#a4a23feb82c0e0456839bcea5d6296e23) 为 `true` 时接受的最小标识符 |
| [`max_id`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#adb97ffe9fa5dda172aaf4cde2be82a8a) | [`zms_id_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga0509b3dce3030a56ecff866d693944f9) | [`use_range`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#a4a23feb82c0e0456839bcea5d6296e23) 为 `true` 时接受的最大标识符 |
| [`use_mask`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#aaa2fad64dd01813dfee027dac55fd43e) | [`bool`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b) | 启用掩码过滤 |
| [`use_range`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#a4a23feb82c0e0456839bcea5d6296e23) | [`bool`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b) | 启用包含上下界的范围过滤 |
| [`use_predicate`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#a829f0fa76965955a302be4ccc0206150) | [`bool`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b) | 启用回调过滤 |
| [`predicate_func`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#a65b7fbc563c7222f0ae9549b84932ae8) | [`zms_iter_predicate_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga73c4c209bc4fbb8125781088b15eef64) | [`use_predicate`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#a829f0fa76965955a302be4ccc0206150) 为 `true` 时使用的谓词回调 |

---

[上一章：Zephyr内存存储迭代器结构](P061_Zephyr内存存储迭代器结构.md) · [下一章：设置子系统接口](P063_设置子系统接口.md) · [返回大纲](大纲.md)
