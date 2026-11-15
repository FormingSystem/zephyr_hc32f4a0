---
id: learning.zephyr-docs.hardware.virtqstruct-8
title: VirtIO驱动操作结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第581章\_VirtIO驱动操作结构

原文：[structvirtio__driver__api](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html)。读取日期：2026-10-13，`latest`。

`struct virtio_driver_api` 是每个**虚拟输入输出（Virtual I/O，VIRTIO）**驱动都需要定义的**驱动操作（Driver Operations）应用程序编程接口（Application Programming Interface，API）**结构。它保存驱动实现的操作函数指针，以及驱动专属的其他常量数据。

```c
#include <zephyr/drivers/virtio.h>
```

## 581.1\_必需与可选成员

原文用 **必需（Required，REQ）**标记驱动必须设置的成员，用**可选（Optional，OPT）**标记可选成员。本结构列出的八个成员全部为 **REQ**。

| 成员 | 类型 | 要求 | 操作 |
| --- | --- | --- | --- |
| [`get_virtqueue`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#a8c07c38516724e2c00a7abfb6307c03c) | [`virtio_api_get_virtqueue`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#gadfbb97d9ee309f732ae35823577d3dc0) | 必需（REQ） | 获取指定索引的虚拟队列 |
| [`notify_virtqueue`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#a7292ae9b4a4390f32e7ae2c96a816abb) | [`virtio_api_notify_virtqueue`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga594c0cad88de538feb224fca8c4296da) | 必需（REQ） | 通知虚拟队列 |
| [`get_device_specific_config`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#a86fb67f88b86915654408e198ee44f45) | [`virtio_api_get_device_specific_config`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga5b9b5154ebe1572f7e694d27deab9d7f) | 必需（REQ） | 获取设备专属配置 |
| [`read_device_feature_bit`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#a2c8afe3cb38f7ced72eb2bea856a6657) | [`virtio_api_read_device_feature_bit`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga84f6ea683db6dec98aac75ec1cb2d10e) | 必需（REQ） | 读取设备提供的特性位 |
| [`write_driver_feature_bit`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#ad7223786d876cd8c0fb42163e0b378ce) | [`virtio_api_write_driver_feature_bit`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga3dd5a50881ceeef712b3e667e7da33a9) | 必需（REQ） | 设置驱动特性位 |
| [`commit_feature_bits`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#a16c5f2cf9e65cc0839738f53a5f09954) | [`virtio_api_commit_feature_bits`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga1f2e55fbde5585086748e4a1bde3fc06) | 必需（REQ） | 提交特性位 |
| [`init_virtqueues`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#a133dd3f346c3f58ab6f253e3e1cbeea4) | [`virtio_api_init_virtqueues`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga9d9191842a75511905fff779378cad5a) | 必需（REQ） | 初始化虚拟队列 |
| [`finalize_init`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#ab70e364a741b0a30d74257c90fc7bc2d) | [`virtio_api_finalize_init`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#gab61586ac03a951bc0e4ecd217a316e98) | 必需（REQ） | 完成设备初始化 |

这些函数指针的完整类型定义见[驱动后端接口](P580_VirtIO驱动后端接口.md)，对应参数和返回值见[设备接口](P571_VirtIO设备接口.md)。

## 581.2\_相关定义

原文列出的相关宏为 [`DEVICE_DT_INST_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)、[`DEVICE_DT_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1) 和 [`DEVICE_API()`](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)，分别用于基于设备树实例定义设备、基于设备树节点定义设备，以及定义驱动 API 结构实例。

本结构的文档由 `zephyr/drivers/virtio.h` 生成。

---

[上一章：VirtIO驱动后端接口](P580_VirtIO驱动后端接口.md) · [下一章：NVMe控制器绑定](P582_NVMe控制器绑定.md) · [返回大纲](大纲.md)
