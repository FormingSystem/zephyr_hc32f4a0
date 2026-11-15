---
id: learning.zephyr-docs.hardware.virtqstruct-7
title: VirtIO驱动后端接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第580章\_VirtIO驱动后端接口

原文：[group__virtio__interface__backend](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html)。读取日期：2026-10-13，`latest`。

本组提供实现**虚拟输入输出（Virtual I/O，VIRTIO）**驱动所需的**应用程序编程接口（Application Programming Interface，API）**类型定义、**回调（Callback）**签名及其他辅助定义。

```c
#include <zephyr/drivers/virtio.h>
```

## 580.1\_驱动操作结构

`struct virtio_driver_api` 保存 VIRTIO 驱动实现的各项操作。详情见[驱动操作结构](P581_VirtIO驱动操作结构.md)。

## 580.2\_操作函数指针类型

以下每种类型都是对应操作的函数指针类型。参数说明及返回约定见[VirtIO设备接口](P571_VirtIO设备接口.md)中同名操作；原文逐项引用对应接口，未在本页另列一套参数规则。

**获取指定索引的虚拟队列。**类型为 [`virtio_api_get_virtqueue`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#gadfbb97d9ee309f732ae35823577d3dc0)，对应 [`virtio_get_virtqueue()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#ga4c1e58e5e34cb40f0a420a52767bff27)。

```c
typedef struct virtq * (*virtio_api_get_virtqueue)(const struct device *dev, uint16_t queue_idx);
```

**通知虚拟队列。**类型为 [`virtio_api_notify_virtqueue`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga594c0cad88de538feb224fca8c4296da)，对应 [`virtio_notify_virtqueue()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#gada51c40981fcdf232b571e1a11dc3cee)。

```c
typedef void (*virtio_api_notify_virtqueue)(const struct device *dev, uint16_t queue_idx);
```

**获取设备专属配置。**类型为 [`virtio_api_get_device_specific_config`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga5b9b5154ebe1572f7e694d27deab9d7f)，对应 [`virtio_get_device_specific_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#ga24987fd9a7603824baed470e4b0ef4d0)。

```c
typedef void * (*virtio_api_get_device_specific_config)(const struct device *dev);
```

**读取设备提供的特性位。**类型为 [`virtio_api_read_device_feature_bit`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga84f6ea683db6dec98aac75ec1cb2d10e)，对应 [`virtio_read_device_feature_bit()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#ga55be5a1c2dc457bb1d44b0c302bfb7a8)。

```c
typedef bool (*virtio_api_read_device_feature_bit)(const struct device *dev, int bit);
```

**设置驱动特性位。**类型为 [`virtio_api_write_driver_feature_bit`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga3dd5a50881ceeef712b3e667e7da33a9)，对应 [`virtio_write_driver_feature_bit()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#gab920f8dfee1139585f6af6b22c340912)。

```c
typedef int (*virtio_api_write_driver_feature_bit)(const struct device *dev, int bit, bool value);
```

**提交特性位。**类型为 [`virtio_api_commit_feature_bits`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga1f2e55fbde5585086748e4a1bde3fc06)，对应 [`virtio_commit_feature_bits()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#ga7d29735da898548661844356fef966e9)。

```c
typedef int (*virtio_api_commit_feature_bits)(const struct device *dev);
```

**初始化虚拟队列。**类型为 [`virtio_api_init_virtqueues`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga9d9191842a75511905fff779378cad5a)，对应 [`virtio_init_virtqueues()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#gaf8fde0107ed6da7eb621f334f478666e)。

```c
typedef int (*virtio_api_init_virtqueues)(const struct device *dev, uint16_t num_queues, virtio_enumerate_queues cb, void *opaque);
```

**完成设备初始化。**类型为 [`virtio_api_finalize_init`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#gab61586ac03a951bc0e4ecd217a316e98)，对应 [`virtio_finalize_init()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#ga3ce7e3833b19210d47e563995c39087d)。

```c
typedef void (*virtio_api_finalize_init)(const struct device *dev);
```


---

[上一章：VirtIO缓冲区结构](P579_VirtIO缓冲区结构.md) · [下一章：VirtIO驱动操作结构](P581_VirtIO驱动操作结构.md) · [返回大纲](大纲.md)
