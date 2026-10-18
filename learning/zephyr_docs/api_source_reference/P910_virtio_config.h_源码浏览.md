---
id: learning.zephyr-docs.api-source-reference.page-910
title: virtio_config.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第910章\_virtio\_config.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../hardware/P594_VirtIO规范常量.md)。

## 910.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00088"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00215"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00224"></a>
<a id="l00225"></a>

```c
/*
 * Copyright (c) 2025 Antmicro <www.antmicro.com>
 * Copyright (c) 2025 TOKITA Hiroshi
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_DRIVERS_VIRTIO_VIRTIO_CONFIG_H_
#define ZEPHYR_DRIVERS_VIRTIO_VIRTIO_CONFIG_H_


#define DEVICE_STATUS_ACKNOWLEDGE 0
#define DEVICE_STATUS_DRIVER      1
#define DEVICE_STATUS_DRIVER_OK   2
#define DEVICE_STATUS_FEATURES_OK 3
#define DEVICE_STATUS_NEEDS_RESET 6
#define DEVICE_STATUS_FAILED      7



#define VIRTIO_RING_F_INDIRECT_DESC 28
#define VIRTIO_RING_F_EVENT_IDX     29
#define VIRTIO_F_VERSION_1          32
#define VIRTIO_F_ACCESS_PLATFORM    33



#define VIRTQ_AVAIL_F_NO_INTERRUPT 1

#define VIRTQ_USED_F_NO_NOTIFY 1



#define DEV_TYPE_FEAT_RANGE_0_BEGIN 0
#define DEV_TYPE_FEAT_RANGE_0_END   23
#define DEV_TYPE_FEAT_RANGE_1_BEGIN 50
#define DEV_TYPE_FEAT_RANGE_1_END   127



#define VIRTIO_QUEUE_INTERRUPT                1
#define VIRTIO_DEVICE_CONFIGURATION_INTERRUPT 2



#define VIRTIO_MMIO_MAGIC_VALUE         0x000
#define VIRTIO_MMIO_VERSION             0x004
#define VIRTIO_MMIO_DEVICE_ID           0x008
#define VIRTIO_MMIO_VENDOR_ID           0x00c
#define VIRTIO_MMIO_DEVICE_FEATURES     0x010
#define VIRTIO_MMIO_DEVICE_FEATURES_SEL 0x014
#define VIRTIO_MMIO_DRIVER_FEATURES     0x020
#define VIRTIO_MMIO_DRIVER_FEATURES_SEL 0x024
#define VIRTIO_MMIO_QUEUE_SEL           0x030
#define VIRTIO_MMIO_QUEUE_SIZE_MAX      0x034
#define VIRTIO_MMIO_QUEUE_SIZE          0x038
#define VIRTIO_MMIO_QUEUE_READY         0x044
#define VIRTIO_MMIO_QUEUE_NOTIFY        0x050
#define VIRTIO_MMIO_INTERRUPT_STATUS    0x060
#define VIRTIO_MMIO_INTERRUPT_ACK       0x064
#define VIRTIO_MMIO_STATUS              0x070
#define VIRTIO_MMIO_QUEUE_DESC_LOW      0x080
#define VIRTIO_MMIO_QUEUE_DESC_HIGH     0x084
#define VIRTIO_MMIO_QUEUE_AVAIL_LOW     0x090
#define VIRTIO_MMIO_QUEUE_AVAIL_HIGH    0x094
#define VIRTIO_MMIO_QUEUE_USED_LOW      0x0a0
#define VIRTIO_MMIO_QUEUE_USED_HIGH     0x0a4
#define VIRTIO_MMIO_SHM_SEL             0x0ac
#define VIRTIO_MMIO_SHM_LEN_LOW         0x0b0
#define VIRTIO_MMIO_SHM_LEN_HIGH        0x0b4
#define VIRTIO_MMIO_SHM_BASE_LOW        0x0b8
#define VIRTIO_MMIO_SHM_BASE_HIGH       0x0bc
#define VIRTIO_MMIO_QUEUE_RESET         0x0c0
#define VIRTIO_MMIO_CONFIG_GENERATION   0x0fc
#define VIRTIO_MMIO_CONFIG              0x100


#endif /* ZEPHYR_DRIVERS_VIRTIO_VIRTIO_CONFIG_H_ */
```

## 910.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Antmicro <www.antmicro.com>。

版权（Copyright）：© 2025 TOKITA Hiroshi。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 225 行

头文件保护宏（Header guard）标记：`ZEPHYR_DRIVERS_VIRTIO_VIRTIO_CONFIG_H_`。

## 910.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../hardware/P594_VirtIO规范常量.md)

---

[上一章](P909_virtio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P911_virtiofs.h_源码浏览.md)
