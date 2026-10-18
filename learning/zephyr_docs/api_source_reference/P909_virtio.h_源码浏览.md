---
id: learning.zephyr-docs.api-source-reference.page-909
title: virtio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/virtio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第909章\_virtio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/virtio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../hardware/P593_VirtIO公共头文件.md)。

## 909.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00030"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00047"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="foldopen00129"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="foldopen00144"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="foldopen00155"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="foldopen00167"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="foldopen00180"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="foldopen00191"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="foldopen00205"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="foldopen00216"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__virtio__interface__backend_html_ga1f2e55fbde5585086748e4a1bde3fc06"></a>
<a id="agroup__virtio__interface__backend_html_ga3dd5a50881ceeef712b3e667e7da33a9"></a>
<a id="agroup__virtio__interface__backend_html_ga594c0cad88de538feb224fca8c4296da"></a>
<a id="agroup__virtio__interface__backend_html_ga5b9b5154ebe1572f7e694d27deab9d7f"></a>
<a id="agroup__virtio__interface__backend_html_ga84f6ea683db6dec98aac75ec1cb2d10e"></a>
<a id="agroup__virtio__interface__backend_html_ga9d9191842a75511905fff779378cad5a"></a>
<a id="agroup__virtio__interface__backend_html_gab61586ac03a951bc0e4ecd217a316e98"></a>
<a id="agroup__virtio__interface__backend_html_gadfbb97d9ee309f732ae35823577d3dc0"></a>
<a id="agroup__virtio__interface_html_ga24987fd9a7603824baed470e4b0ef4d0"></a>
<a id="agroup__virtio__interface_html_ga3ce7e3833b19210d47e563995c39087d"></a>
<a id="agroup__virtio__interface_html_ga4c1e58e5e34cb40f0a420a52767bff27"></a>
<a id="agroup__virtio__interface_html_ga55be5a1c2dc457bb1d44b0c302bfb7a8"></a>
<a id="agroup__virtio__interface_html_ga7d29735da898548661844356fef966e9"></a>
<a id="agroup__virtio__interface_html_gab920f8dfee1139585f6af6b22c340912"></a>
<a id="agroup__virtio__interface_html_gac66779305009c3896eff113f680c29c4"></a>
<a id="agroup__virtio__interface_html_gada51c40981fcdf232b571e1a11dc3cee"></a>
<a id="agroup__virtio__interface_html_gaf8fde0107ed6da7eb621f334f478666e"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructvirtio__driver__api_html"></a>
<a id="astructvirtio__driver__api_html_a133dd3f346c3f58ab6f253e3e1cbeea4"></a>
<a id="astructvirtio__driver__api_html_a16c5f2cf9e65cc0839738f53a5f09954"></a>
<a id="astructvirtio__driver__api_html_a2c8afe3cb38f7ced72eb2bea856a6657"></a>
<a id="astructvirtio__driver__api_html_a7292ae9b4a4390f32e7ae2c96a816abb"></a>
<a id="astructvirtio__driver__api_html_a86fb67f88b86915654408e198ee44f45"></a>
<a id="astructvirtio__driver__api_html_a8c07c38516724e2c00a7abfb6307c03c"></a>
<a id="astructvirtio__driver__api_html_ab70e364a741b0a30d74257c90fc7bc2d"></a>
<a id="astructvirtio__driver__api_html_ad7223786d876cd8c0fb42163e0b378ce"></a>
<a id="astructvirtq_html"></a>
<a id="avirtqueue_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Antmicro <www.antmicro.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_VIRTIO_VIRTIO_H_
#define ZEPHYR_VIRTIO_VIRTIO_H_
#include <zephyr/device.h>
#include "virtio/virtqueue.h"

#ifdef __cplusplus
extern "C" {
#endif


typedef uint16_t (*virtio_enumerate_queues)(
        uint16_t queue_idx, uint16_t max_queue_size, void *opaque
);


typedef struct virtq *(*virtio_api_get_virtqueue)(const struct device *dev, uint16_t queue_idx);

typedef void (*virtio_api_notify_virtqueue)(const struct device *dev, uint16_t queue_idx);

typedef void *(*virtio_api_get_device_specific_config)(const struct device *dev);

typedef bool (*virtio_api_read_device_feature_bit)(const struct device *dev, int bit);

typedef int (*virtio_api_write_driver_feature_bit)(const struct device *dev, int bit, bool value);

typedef int (*virtio_api_commit_feature_bits)(const struct device *dev);

typedef int (*virtio_api_init_virtqueues)(
        const struct device *dev, uint16_t num_queues, virtio_enumerate_queues cb, void *opaque
);

typedef void (*virtio_api_finalize_init)(const struct device *dev);

__subsystem struct virtio_driver_api {
        virtio_api_get_virtqueue get_virtqueue;
        virtio_api_notify_virtqueue notify_virtqueue;
        virtio_api_get_device_specific_config get_device_specific_config;
        virtio_api_read_device_feature_bit read_device_feature_bit;
        virtio_api_write_driver_feature_bit write_driver_feature_bit;
        virtio_api_commit_feature_bits commit_feature_bits;
        virtio_api_init_virtqueues init_virtqueues;
        virtio_api_finalize_init finalize_init;
};


static inline struct virtq *virtio_get_virtqueue(const struct device *dev, uint16_t queue_idx)
{
        return DEVICE_API_GET(virtio, dev)->get_virtqueue(dev, queue_idx);
}

static inline void virtio_notify_virtqueue(const struct device *dev, uint16_t queue_idx)
{
        DEVICE_API_GET(virtio, dev)->notify_virtqueue(dev, queue_idx);
}

static inline void *virtio_get_device_specific_config(const struct device *dev)
{
        return DEVICE_API_GET(virtio, dev)->get_device_specific_config(dev);
}

static inline bool virtio_read_device_feature_bit(const struct device *dev, int bit)
{
        return DEVICE_API_GET(virtio, dev)->read_device_feature_bit(dev, bit);
}

static inline int virtio_write_driver_feature_bit(const struct device *dev, int bit, bool value)
{
        return DEVICE_API_GET(virtio, dev)->write_driver_feature_bit(dev, bit, value);
}

static inline int virtio_commit_feature_bits(const struct device *dev)
{
        return DEVICE_API_GET(virtio, dev)->commit_feature_bits(dev);
}

static inline int virtio_init_virtqueues(
        const struct device *dev, uint16_t num_queues, virtio_enumerate_queues cb, void *opaque)
{
        return DEVICE_API_GET(virtio, dev)->init_virtqueues(dev, num_queues, cb, opaque);
}

static inline void virtio_finalize_init(const struct device *dev)
{
        DEVICE_API_GET(virtio, dev)->finalize_init(dev);
}


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_VIRTIO_VIRTIO_H_ */
```

## 909.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Antmicro <www.antmicro.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 229 行

头文件保护宏（Header guard）标记：`ZEPHYR_VIRTIO_VIRTIO_H_`。

## 909.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../hardware/P593_VirtIO公共头文件.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [virtio/virtqueue.h](../hardware/P595_VirtIO队列头文件.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [virtio_enumerate_queues](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#gac66779305009c3896eff113f680c29c4)
- [virtq](../hardware/P578_VirtIO队列结构.md)
- [device](../device_reference/P002_设备对象结构.md)
- [virtio_api_notify_virtqueue](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga594c0cad88de538feb224fca8c4296da)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [virtio_api_read_device_feature_bit](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga84f6ea683db6dec98aac75ec1cb2d10e)
- [virtio_api_write_driver_feature_bit](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga3dd5a50881ceeef712b3e667e7da33a9)
- [virtio_api_commit_feature_bits](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga1f2e55fbde5585086748e4a1bde3fc06)
- [virtio_api_init_virtqueues](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga9d9191842a75511905fff779378cad5a)
- [virtio_api_finalize_init](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#gab61586ac03a951bc0e4ecd217a316e98)
- [virtio_driver_api](../hardware/P581_VirtIO驱动操作结构.md)
- [virtio_api_get_virtqueue](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#gadfbb97d9ee309f732ae35823577d3dc0)
- [get_virtqueue](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#a8c07c38516724e2c00a7abfb6307c03c)
- [notify_virtqueue](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#a7292ae9b4a4390f32e7ae2c96a816abb)
- [virtio_api_get_device_specific_config](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface__backend.html#ga5b9b5154ebe1572f7e694d27deab9d7f)
- [get_device_specific_config](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#a86fb67f88b86915654408e198ee44f45)
- [read_device_feature_bit](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#a2c8afe3cb38f7ced72eb2bea856a6657)
- [write_driver_feature_bit](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#ad7223786d876cd8c0fb42163e0b378ce)
- [commit_feature_bits](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#a16c5f2cf9e65cc0839738f53a5f09954)
- [init_virtqueues](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#a133dd3f346c3f58ab6f253e3e1cbeea4)
- [finalize_init](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#ab70e364a741b0a30d74257c90fc7bc2d)
- [virtio_get_virtqueue](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#ga4c1e58e5e34cb40f0a420a52767bff27)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [virtio_notify_virtqueue](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#gada51c40981fcdf232b571e1a11dc3cee)
- [virtio_get_device_specific_config](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#ga24987fd9a7603824baed470e4b0ef4d0)
- [virtio_read_device_feature_bit](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#ga55be5a1c2dc457bb1d44b0c302bfb7a8)
- [virtio_write_driver_feature_bit](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#gab920f8dfee1139585f6af6b22c340912)
- [virtio_commit_feature_bits](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#ga7d29735da898548661844356fef966e9)
- [virtio_init_virtqueues](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#gaf8fde0107ed6da7eb621f334f478666e)
- [virtio_finalize_init](https://docs.zephyrproject.org/latest/doxygen/html/group__virtio__interface.html#ga3ce7e3833b19210d47e563995c39087d)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [virtio_driver_api::init_virtqueues](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#a133dd3f346c3f58ab6f253e3e1cbeea4)
- [virtio_driver_api::commit_feature_bits](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#a16c5f2cf9e65cc0839738f53a5f09954)
- [virtio_driver_api::read_device_feature_bit](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#a2c8afe3cb38f7ced72eb2bea856a6657)
- [virtio_driver_api::notify_virtqueue](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#a7292ae9b4a4390f32e7ae2c96a816abb)
- [virtio_driver_api::get_device_specific_config](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#a86fb67f88b86915654408e198ee44f45)
- [virtio_driver_api::get_virtqueue](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#a8c07c38516724e2c00a7abfb6307c03c)
- [virtio_driver_api::finalize_init](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#ab70e364a741b0a30d74257c90fc7bc2d)
- [virtio_driver_api::write_driver_feature_bit](https://docs.zephyrproject.org/latest/doxygen/html/structvirtio__driver__api.html#ad7223786d876cd8c0fb42163e0b378ce)
- [virtqueue.h](../hardware/P595_VirtIO队列头文件.md)

---

[上一章](P908_video.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P910_virtio_config.h_源码浏览.md)
