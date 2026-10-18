---
id: learning.zephyr-docs.hardware.virtiohdr-0
title: VirtIO公共头文件
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/virtio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第593章\_VirtIO公共头文件

原文：[virtio_8h](https://docs.zephyrproject.org/latest/doxygen/html/virtio_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/virtio.h` 是**虚拟输入输出（Virtual I/O，VIRTIO）**驱动**应用程序编程接口（Application Programming Interface，API）**的主头文件。

```c
#include <zephyr/device.h>
#include "virtio/virtqueue.h"
```

## 593.1\_驱动结构与类型定义

`struct virtio_driver_api` 表示 Virtio 驱动操作，其成员见[驱动操作结构](P581_VirtIO驱动操作结构.md)。本头文件声明以下回调和函数指针类型：

```c
typedef uint16_t(* virtio_enumerate_queues) (uint16_t queue_idx, uint16_t max_queue_size, void *opaque);
typedef struct virtq *(* virtio_api_get_virtqueue) (const struct device *dev, uint16_t queue_idx);
typedef void(* virtio_api_notify_virtqueue) (const struct device *dev, uint16_t queue_idx);
typedef void *(* virtio_api_get_device_specific_config) (const struct device *dev);
typedef bool(* virtio_api_read_device_feature_bit) (const struct device *dev, int bit);
typedef int(* virtio_api_write_driver_feature_bit) (const struct device *dev, int bit, bool value);
typedef int(* virtio_api_commit_feature_bits) (const struct device *dev);
typedef int(* virtio_api_init_virtqueues) (const struct device *dev, uint16_t num_queues, virtio_enumerate_queues cb, void *opaque);
typedef void(* virtio_api_finalize_init) (const struct device *dev);
```

| 类型 | 含义 |
| --- | --- |
| [`virtio_enumerate_queues`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#gac66779305009c3896eff113f680c29c4) | 枚举虚拟队列时使用的回调 |
| [`virtio_api_get_virtqueue`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#gadfbb97d9ee309f732ae35823577d3dc0) | 获取指定索引的虚拟队列的函数指针类型 |
| [`virtio_api_notify_virtqueue`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga594c0cad88de538feb224fca8c4296da) | 通知虚拟队列的函数指针类型 |
| [`virtio_api_get_device_specific_config`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga5b9b5154ebe1572f7e694d27deab9d7f) | 获取设备专属配置的函数指针类型 |
| [`virtio_api_read_device_feature_bit`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga84f6ea683db6dec98aac75ec1cb2d10e) | 读取设备提供的特性位的函数指针类型 |
| [`virtio_api_write_driver_feature_bit`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga3dd5a50881ceeef712b3e667e7da33a9) | 设置驱动特性位的函数指针类型 |
| [`virtio_api_commit_feature_bits`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga1f2e55fbde5585086748e4a1bde3fc06) | 提交特性位的函数指针类型 |
| [`virtio_api_init_virtqueues`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga9d9191842a75511905fff779378cad5a) | 初始化虚拟队列的函数指针类型 |
| [`virtio_api_finalize_init`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#gab61586ac03a951bc0e4ecd217a316e98) | 完成设备初始化的函数指针类型 |

枚举回调参数详见[设备接口](P571_VirtIO设备接口.md)，其他类型详见[驱动后端接口](P580_VirtIO驱动后端接口.md)。

## 593.2\_设备函数

```c
static struct virtq * virtio_get_virtqueue (const struct device *dev, uint16_t queue_idx);
static void virtio_notify_virtqueue (const struct device *dev, uint16_t queue_idx);
static void * virtio_get_device_specific_config (const struct device *dev);
static bool virtio_read_device_feature_bit (const struct device *dev, int bit);
static int virtio_write_driver_feature_bit (const struct device *dev, int bit, bool value);
static int virtio_commit_feature_bits (const struct device *dev);
static int virtio_init_virtqueues (const struct device *dev, uint16_t num_queues, virtio_enumerate_queues cb, void *opaque);
static void virtio_finalize_init (const struct device *dev);
```

| 函数 | 含义 |
| --- | --- |
| [`virtio_get_virtqueue()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#ga4c1e58e5e34cb40f0a420a52767bff27) | 获取指定索引的虚拟队列 |
| [`virtio_notify_virtqueue()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#gada51c40981fcdf232b571e1a11dc3cee) | 通知虚拟队列 |
| [`virtio_get_device_specific_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#ga24987fd9a7603824baed470e4b0ef4d0) | 获取设备专属配置 |
| [`virtio_read_device_feature_bit()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#ga55be5a1c2dc457bb1d44b0c302bfb7a8) | 读取设备提供的特性位 |
| [`virtio_write_driver_feature_bit()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#gab920f8dfee1139585f6af6b22c340912) | 设置驱动特性位 |
| [`virtio_commit_feature_bits()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#ga7d29735da898548661844356fef966e9) | 提交特性位 |
| [`virtio_init_virtqueues()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#gaf8fde0107ed6da7eb621f334f478666e) | 初始化虚拟队列 |
| [`virtio_finalize_init()`](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#ga3ce7e3833b19210d47e563995c39087d) | 完成设备初始化 |

完整参数、返回值及通知时序约束见[设备接口](P571_VirtIO设备接口.md)。

---

[上一章：VirtIO_SPI控制器绑定](P592_VirtIO_SPI控制器绑定.md) · [下一章：VirtIO规范常量](P594_VirtIO规范常量.md) · [返回大纲](大纲.md)
