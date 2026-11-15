---
id: learning.zephyr-docs.api-file-bluetooth-uuid-reference.page-1
title: zephyr__bluetooth__uuid.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_bluetooth\_\_uuid.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙通用唯一标识符（UUID）的处理。

<a id="details"></a>

```c
#include <stddef.h>
#include <stdint.h>
#include <zephyr/sys/util.h>
#include <zephyr/bluetooth/byteorder.h>
```

查看此文件的源码。

蓝牙通用唯一标识符（UUID）的处理。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_bt_5Fuuid"></a>

```c
struct bt_uuid
```

相关声明：[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)。

这是一个暂定类型（Tentative Type），应仅以指针形式使用。

<a id="r_bt_5Fuuid_5F16"></a>

```c
struct bt_uuid_16
```

相关声明：[bt_uuid_16](../bluetooth_connection_model_reference/P133_bt_uuid_16_结构体.md)。

<a id="r_bt_5Fuuid_5F32"></a>

```c
struct bt_uuid_32
```

相关声明：[bt_uuid_32](../bluetooth_connection_model_reference/P134_bt_uuid_32_结构体.md)。

<a id="r_bt_5Fuuid_5F128"></a>

```c
struct bt_uuid_128
```

相关声明：[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)。

<a id="r_bt_5Fuuid_5Fany"></a>

```c
struct bt_uuid_any
```

相关声明：[bt_uuid_any](../bluetooth_connection_model_reference/P135_bt_uuid_any_结构体.md)。

可保存任意大小UUID的辅助类型（Helper Type）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_ga9d3506fd135b5cd8763446f572c161da"></a>

```c
#define BT_UUID_SIZE_16 2
```

相关声明：[BT_UUID_SIZE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9d3506fd135b5cd8763446f572c161da)。

16 位通用唯一标识符（UUID）的大小，单位为八位字节（Octets）。

<a id="r_gaf35f2e5054bfcc81985e90b8ef659fd9"></a>

```c
#define BT_UUID_SIZE_32 4
```

相关声明：[BT_UUID_SIZE_32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf35f2e5054bfcc81985e90b8ef659fd9)。

32 位通用唯一标识符（UUID）的大小，单位为八位字节（Octets）。

<a id="r_ga86fdce8e63c0f8208bea6b0f2584eb67"></a>

```c
#define BT_UUID_SIZE_128 16
```

相关声明：[BT_UUID_SIZE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga86fdce8e63c0f8208bea6b0f2584eb67)。

128 位通用唯一标识符（UUID）的大小，单位为八位字节（Octets）。

<a id="r_gab7c9f80628c5fb1b5d1c09d18a1baff7"></a>

```c
#define BT_UUID_INIT_16(value)
```

相关声明：[BT_UUID_INIT_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab7c9f80628c5fb1b5d1c09d18a1baff7)。

初始化 16 位 UUID（Initialize）。

<a id="r_ga207ff52ebf1eea1c487fff3d840a38f8"></a>

```c
#define BT_UUID_INIT_32(value)
```

相关声明：[BT_UUID_INIT_32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga207ff52ebf1eea1c487fff3d840a38f8)。

初始化 32 位 UUID（Initialize）。

<a id="r_ga1a840adf4bc06cf2cd5dbeb0c868374b"></a>

```c
#define BT_UUID_INIT_128(value...)
```

相关声明：[BT_UUID_INIT_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1a840adf4bc06cf2cd5dbeb0c868374b)。

初始化 128 位 UUID（Initialize）。

<a id="r_ga66ea8148e444e163a936ebd79a63eb55"></a>

```c
#define BT_UUID_DECLARE_16(value)
```

相关声明：[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)。

用于内联声明（Declare Inline）16 位 UUID 的辅助宏。

<a id="r_ga945448449c57b4800e25a363e7d4d1cc"></a>

```c
#define BT_UUID_DECLARE_32(value)
```

相关声明：[BT_UUID_DECLARE_32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga945448449c57b4800e25a363e7d4d1cc)。

用于内联声明（Declare Inline）32 位 UUID 的辅助宏。

<a id="r_gadece715e13e2a529aa55c298ff760bf0"></a>

```c
#define BT_UUID_DECLARE_128(value...)
```

相关声明：[BT_UUID_DECLARE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadece715e13e2a529aa55c298ff760bf0)。

用于内联声明（Declare Inline）128 位 UUID 的辅助宏。

<a id="r_ga7466cf356741d6348f332653a385fd01"></a>

```c
#define BT_UUID_16(__u)
```

相关声明：[BT_UUID_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7466cf356741d6348f332653a385fd01)。

从通用 UUID（Generic UUID）访问 16 位 UUID 的辅助宏。

<a id="r_gacc77f082e8dac620672676ed8d005504"></a>

```c
#define BT_UUID_32(__u)
```

相关声明：[BT_UUID_32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacc77f082e8dac620672676ed8d005504)。

从通用 UUID（Generic UUID）访问 32 位 UUID 的辅助宏。

<a id="r_ga931a0d5eb23537be31408c787fd8b48d"></a>

```c
#define BT_UUID_128(__u)
```

相关声明：[BT_UUID_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga931a0d5eb23537be31408c787fd8b48d)。

从通用 UUID（Generic UUID）访问 128 位 UUID 的辅助宏。

<a id="r_gac3973b66e992cbc0940752b77b378f43"></a>

```c
#define BT_UUID_128_ENCODE(w32, w1, w2, w3, w48)
```

相关声明：[BT_UUID_128_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3973b66e992cbc0940752b77b378f43)。

将 128 位 UUID 编码为小端格式（Little-endian）的数组值。

<a id="r_ga16e057af1bb2f1c11e74b50bfd490586"></a>

```c
#define BT_UUID_16_ENCODE(w16)
```

相关声明：[BT_UUID_16_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga16e057af1bb2f1c11e74b50bfd490586)。

将 16 位 UUID 编码为小端格式（Little-endian）的数组值。

<a id="r_gad5294c1c19c66b20321c88939a8849bf"></a>

```c
#define BT_UUID_32_ENCODE(w32)
```

相关声明：[BT_UUID_32_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad5294c1c19c66b20321c88939a8849bf)。

将 32 位 UUID 编码为小端格式（Little-endian）的数组值。

<a id="r_gaf9a36381128454102c558568dfd5d029"></a>

```c
#define BT_UUID_STR_LEN 37
```

相关声明：[BT_UUID_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf9a36381128454102c558568dfd5d029)。

蓝牙 UUID 用户字符串缓冲区（User String Buffer）的建议长度。

<a id="r_gaaf6715d89ba70a057949e636fb2368dd"></a>

```c
#define BT_UUID_GAP_VAL 0x1800
```

相关声明：[BT_UUID_GAP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaaf6715d89ba70a057949e636fb2368dd)。

通用访问（Generic Access）的 UUID 值。

<a id="r_gae8b61f07e6732ffb876318045b5803c4"></a>

```c
#define BT_UUID_GAP BT_UUID_DECLARE_16(BT_UUID_GAP_VAL)
```

相关声明：[BT_UUID_GAP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae8b61f07e6732ffb876318045b5803c4)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GAP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaaf6715d89ba70a057949e636fb2368dd)。

通用访问（Generic Access）。

<a id="r_gad893036bda14523c3e35ff66d23bacb2"></a>

```c
#define BT_UUID_GATT_VAL 0x1801
```

相关声明：[BT_UUID_GATT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad893036bda14523c3e35ff66d23bacb2)。

通用属性（Generic attribute）的 UUID 值。

<a id="r_ga18f210e4e60b9fdd80d9d68f007b0728"></a>

```c
#define BT_UUID_GATT BT_UUID_DECLARE_16(BT_UUID_GATT_VAL)
```

相关声明：[BT_UUID_GATT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga18f210e4e60b9fdd80d9d68f007b0728)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad893036bda14523c3e35ff66d23bacb2)。

通用属性（Generic Attribute）。

<a id="r_ga637aece6581426d8d5d7b9aeb546a67e"></a>

```c
#define BT_UUID_IAS_VAL 0x1802
```

相关声明：[BT_UUID_IAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga637aece6581426d8d5d7b9aeb546a67e)。

即时告警服务（Immediate Alert Service）的 UUID 值。

<a id="r_ga9d99491d2957912ab80e2636d6ac7416"></a>

```c
#define BT_UUID_IAS BT_UUID_DECLARE_16(BT_UUID_IAS_VAL)
```

相关声明：[BT_UUID_IAS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9d99491d2957912ab80e2636d6ac7416)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_IAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga637aece6581426d8d5d7b9aeb546a67e)。

即时告警服务（Immediate Alert Service）。

<a id="r_ga1b868ca21fa47aba88601f71eb8ad1d5"></a>

```c
#define BT_UUID_LLS_VAL 0x1803
```

相关声明：[BT_UUID_LLS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1b868ca21fa47aba88601f71eb8ad1d5)。

链路丢失服务（Link Loss Service）的 UUID 值。

<a id="r_ga6bdab3bba88af7187eb50b7817cc317e"></a>

```c
#define BT_UUID_LLS BT_UUID_DECLARE_16(BT_UUID_LLS_VAL)
```

相关声明：[BT_UUID_LLS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6bdab3bba88af7187eb50b7817cc317e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_LLS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1b868ca21fa47aba88601f71eb8ad1d5)。

链路丢失服务（Link Loss Service）。

<a id="r_gab8d79e7553b418eae94b9d790d9a422e"></a>

```c
#define BT_UUID_TPS_VAL 0x1804
```

相关声明：[BT_UUID_TPS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab8d79e7553b418eae94b9d790d9a422e)。

发送功率服务（Tx Power Service）的 UUID 值。

<a id="r_ga2e250a6880be716f98e668ab26dcdac3"></a>

```c
#define BT_UUID_TPS BT_UUID_DECLARE_16(BT_UUID_TPS_VAL)
```

相关声明：[BT_UUID_TPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2e250a6880be716f98e668ab26dcdac3)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TPS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab8d79e7553b418eae94b9d790d9a422e)。

发送功率服务（Tx Power Service）。

<a id="r_ga264f3b58d4e3bee6a7533acf0670206d"></a>

```c
#define BT_UUID_CTS_VAL 0x1805
```

相关声明：[BT_UUID_CTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga264f3b58d4e3bee6a7533acf0670206d)。

当前时间服务（Current Time Service）的 UUID 值。

<a id="r_ga8c2c089f4cc458c0f4a5a7506c21a6f9"></a>

```c
#define BT_UUID_CTS BT_UUID_DECLARE_16(BT_UUID_CTS_VAL)
```

相关声明：[BT_UUID_CTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8c2c089f4cc458c0f4a5a7506c21a6f9)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga264f3b58d4e3bee6a7533acf0670206d)。

当前时间服务（Current Time Service）。

<a id="r_ga13300d9d1074fd90a65233357dd9ad60"></a>

```c
#define BT_UUID_RTUS_VAL 0x1806
```

相关声明：[BT_UUID_RTUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga13300d9d1074fd90a65233357dd9ad60)。

参考时间更新服务（Reference Time Update Service）的 UUID 值。

<a id="r_ga52c98d18473e61c581f0cab4839defa8"></a>

```c
#define BT_UUID_RTUS BT_UUID_DECLARE_16(BT_UUID_RTUS_VAL)
```

相关声明：[BT_UUID_RTUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga52c98d18473e61c581f0cab4839defa8)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_RTUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga13300d9d1074fd90a65233357dd9ad60)。

参考时间更新服务（Reference Time Update Service）。

<a id="r_ga0396837f73209e12bc6d11c64a3a6d67"></a>

```c
#define BT_UUID_NDSTS_VAL 0x1807
```

相关声明：[BT_UUID_NDSTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0396837f73209e12bc6d11c64a3a6d67)。

下次夏令时变更服务（Next DST Change Service）的 UUID 值。

<a id="r_ga3a4f846cbf5dd4fccec26be00506a61c"></a>

```c
#define BT_UUID_NDSTS BT_UUID_DECLARE_16(BT_UUID_NDSTS_VAL)
```

相关声明：[BT_UUID_NDSTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3a4f846cbf5dd4fccec26be00506a61c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_NDSTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0396837f73209e12bc6d11c64a3a6d67)。

下次夏令时变更服务（Next DST Change Service）。

<a id="r_gab31578ab529cf755ec611c491a3676ac"></a>

```c
#define BT_UUID_GS_VAL 0x1808
```

相关声明：[BT_UUID_GS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab31578ab529cf755ec611c491a3676ac)。

葡萄糖服务（Glucose Service）的 UUID 值。

<a id="r_gac1f5583a48b80fab9d05546d87cb6de0"></a>

```c
#define BT_UUID_GS BT_UUID_DECLARE_16(BT_UUID_GS_VAL)
```

相关声明：[BT_UUID_GS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac1f5583a48b80fab9d05546d87cb6de0)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab31578ab529cf755ec611c491a3676ac)。

葡萄糖服务（Glucose Service）。

<a id="r_ga3caec4c6564711a2959ffadcf5598011"></a>

```c
#define BT_UUID_HTS_VAL 0x1809
```

相关声明：[BT_UUID_HTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3caec4c6564711a2959ffadcf5598011)。

健康温度计服务（Health Thermometer Service）的 UUID 值。

<a id="r_gabffa5a0a0a57cfd330a8bef348c2c2ee"></a>

```c
#define BT_UUID_HTS BT_UUID_DECLARE_16(BT_UUID_HTS_VAL)
```

相关声明：[BT_UUID_HTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabffa5a0a0a57cfd330a8bef348c2c2ee)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3caec4c6564711a2959ffadcf5598011)。

健康温度计服务（Health Thermometer Service）。

<a id="r_ga3eaf1d7bfeb9b9375e1e2b4ba7f23aed"></a>

```c
#define BT_UUID_DIS_VAL 0x180a
```

相关声明：[BT_UUID_DIS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3eaf1d7bfeb9b9375e1e2b4ba7f23aed)。

设备信息服务（Device Information Service）的 UUID 值。

<a id="r_ga03ea74768fa1e69dad54cffe9eeeee31"></a>

```c
#define BT_UUID_DIS BT_UUID_DECLARE_16(BT_UUID_DIS_VAL)
```

相关声明：[BT_UUID_DIS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga03ea74768fa1e69dad54cffe9eeeee31)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_DIS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3eaf1d7bfeb9b9375e1e2b4ba7f23aed)。

设备信息服务（Device Information Service）。

<a id="r_ga66870ecd34acfee828d55f63167b7e67"></a>

```c
#define BT_UUID_NAS_VAL 0x180b
```

相关声明：[BT_UUID_NAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66870ecd34acfee828d55f63167b7e67)。

网络可用性服务（Network Availability Service）的 UUID 值。

<a id="r_ga92af25a46ae1b534fa248fd0516278cb"></a>

```c
#define BT_UUID_NAS BT_UUID_DECLARE_16(BT_UUID_NAS_VAL)
```

相关声明：[BT_UUID_NAS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga92af25a46ae1b534fa248fd0516278cb)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_NAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66870ecd34acfee828d55f63167b7e67)。

网络可用性服务（Network Availability Service）。

<a id="r_ga110066c42ffc45bf86a9c90528aeb2e7"></a>

```c
#define BT_UUID_WDS_VAL 0x180c
```

相关声明：[BT_UUID_WDS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga110066c42ffc45bf86a9c90528aeb2e7)。

看门狗服务（Watchdog Service）的 UUID 值。

<a id="r_ga7c501f33b29907d48dd31ed70eeb67d4"></a>

```c
#define BT_UUID_WDS BT_UUID_DECLARE_16(BT_UUID_WDS_VAL)
```

相关声明：[BT_UUID_WDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7c501f33b29907d48dd31ed70eeb67d4)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_WDS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga110066c42ffc45bf86a9c90528aeb2e7)。

看门狗服务（Watchdog Service）。

<a id="r_ga912cb91295d110813a3db0144c95551d"></a>

```c
#define BT_UUID_HRS_VAL 0x180d
```

相关声明：[BT_UUID_HRS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga912cb91295d110813a3db0144c95551d)。

心率服务（Heart Rate Service）的 UUID 值。

<a id="r_ga17893ceaa9bc20640d4ecdeabe9beb28"></a>

```c
#define BT_UUID_HRS BT_UUID_DECLARE_16(BT_UUID_HRS_VAL)
```

相关声明：[BT_UUID_HRS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga17893ceaa9bc20640d4ecdeabe9beb28)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HRS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga912cb91295d110813a3db0144c95551d)。

心率服务（Heart Rate Service）。

<a id="r_gaea47ecf9bc957d813312a188a701db54"></a>

```c
#define BT_UUID_PAS_VAL 0x180e
```

相关声明：[BT_UUID_PAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaea47ecf9bc957d813312a188a701db54)。

电话告警服务（Phone Alert Service）的 UUID 值。

<a id="r_gadd5233cc3cb516f8b7fb192d6c64bcad"></a>

```c
#define BT_UUID_PAS BT_UUID_DECLARE_16(BT_UUID_PAS_VAL)
```

相关声明：[BT_UUID_PAS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadd5233cc3cb516f8b7fb192d6c64bcad)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_PAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaea47ecf9bc957d813312a188a701db54)。

电话告警服务（Phone Alert Service）。

<a id="r_ga2ff64c18d7f8dae8a328b52f486161c4"></a>

```c
#define BT_UUID_BAS_VAL 0x180f
```

相关声明：[BT_UUID_BAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2ff64c18d7f8dae8a328b52f486161c4)。

电池服务（Battery Service）的 UUID 值。

<a id="r_gabc55390a1144b556477df555e76848ab"></a>

```c
#define BT_UUID_BAS BT_UUID_DECLARE_16(BT_UUID_BAS_VAL)
```

相关声明：[BT_UUID_BAS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabc55390a1144b556477df555e76848ab)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2ff64c18d7f8dae8a328b52f486161c4)。

电池服务（Battery Service）。

<a id="r_ga2ff98d3bfd27cba7eb99c62dfb31a6fd"></a>

```c
#define BT_UUID_BPS_VAL 0x1810
```

相关声明：[BT_UUID_BPS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2ff98d3bfd27cba7eb99c62dfb31a6fd)。

血压服务（Blood Pressure Service）的 UUID 值。

<a id="r_ga97ed88c10cdc3f1c32c4e53d260eaa3e"></a>

```c
#define BT_UUID_BPS BT_UUID_DECLARE_16(BT_UUID_BPS_VAL)
```

相关声明：[BT_UUID_BPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga97ed88c10cdc3f1c32c4e53d260eaa3e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BPS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2ff98d3bfd27cba7eb99c62dfb31a6fd)。

血压服务（Blood Pressure Service）。

<a id="r_ga0c6ee900cba57e40f8b3681e1ea404c7"></a>

```c
#define BT_UUID_ANS_VAL 0x1811
```

相关声明：[BT_UUID_ANS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0c6ee900cba57e40f8b3681e1ea404c7)。

告警通知服务（Alert Notification Service）的 UUID 值。

<a id="r_ga7a208b147e3b35857c72ba8f8db22d62"></a>

```c
#define BT_UUID_ANS BT_UUID_DECLARE_16(BT_UUID_ANS_VAL)
```

相关声明：[BT_UUID_ANS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7a208b147e3b35857c72ba8f8db22d62)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_ANS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0c6ee900cba57e40f8b3681e1ea404c7)。

告警通知服务（Alert Notification Service）。

<a id="r_ga2bf2ec6082e31f397dec6634cda56bbb"></a>

```c
#define BT_UUID_HIDS_VAL 0x1812
```

相关声明：[BT_UUID_HIDS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2bf2ec6082e31f397dec6634cda56bbb)。

人机接口设备 HID 服务（HID Service）的 UUID 值。

<a id="r_ga74e91eef3e2dcbb4499a0f70f3b479d4"></a>

```c
#define BT_UUID_HIDS BT_UUID_DECLARE_16(BT_UUID_HIDS_VAL)
```

相关声明：[BT_UUID_HIDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga74e91eef3e2dcbb4499a0f70f3b479d4)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HIDS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2bf2ec6082e31f397dec6634cda56bbb)。

人机接口设备 HID 服务（HID Service）。

<a id="r_ga73e7ff27e935868fa86c9d38e186e405"></a>

```c
#define BT_UUID_SPS_VAL 0x1813
```

相关声明：[BT_UUID_SPS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga73e7ff27e935868fa86c9d38e186e405)。

扫描参数服务（Scan Parameters Service）的 UUID 值。

<a id="r_ga7599a7a3cdc6a32c60862618b6b70327"></a>

```c
#define BT_UUID_SPS BT_UUID_DECLARE_16(BT_UUID_SPS_VAL)
```

相关声明：[BT_UUID_SPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7599a7a3cdc6a32c60862618b6b70327)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_SPS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga73e7ff27e935868fa86c9d38e186e405)。

扫描参数服务（Scan Parameters Service）。

<a id="r_gad35b23e0814f0f74c3a33587f7922966"></a>

```c
#define BT_UUID_RSCS_VAL 0x1814
```

相关声明：[BT_UUID_RSCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad35b23e0814f0f74c3a33587f7922966)。

跑步速度与步频服务（Running Speed and Cadence Service）的 UUID 值。

<a id="r_ga40a6402510b5c71b0eca5b2f7a914085"></a>

```c
#define BT_UUID_RSCS BT_UUID_DECLARE_16(BT_UUID_RSCS_VAL)
```

相关声明：[BT_UUID_RSCS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga40a6402510b5c71b0eca5b2f7a914085)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_RSCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad35b23e0814f0f74c3a33587f7922966)。

跑步速度与步频服务（Running Speed and Cadence Service）。

<a id="r_ga4449d49abf6fed72da52b14a967aec4d"></a>

```c
#define BT_UUID_AIOS_VAL 0x1815
```

相关声明：[BT_UUID_AIOS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4449d49abf6fed72da52b14a967aec4d)。

自动化输入／输出服务（Automation IO Service）的 UUID 值。

<a id="r_gaaa73f77971aad79900e18fd58d12ea22"></a>

```c
#define BT_UUID_AIOS BT_UUID_DECLARE_16(BT_UUID_AIOS_VAL)
```

相关声明：[BT_UUID_AIOS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaaa73f77971aad79900e18fd58d12ea22)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_AIOS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4449d49abf6fed72da52b14a967aec4d)。

自动化输入／输出服务（Automation IO Service）。

<a id="r_ga4d31b6944d378bcda7c8f7bfc74c5692"></a>

```c
#define BT_UUID_CSC_VAL 0x1816
```

相关声明：[BT_UUID_CSC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4d31b6944d378bcda7c8f7bfc74c5692)。

骑行速度与踏频服务（Cycling Speed and Cadence Service）的 UUID 值。

<a id="r_ga6514fa0098d12c02aa34c18e1e5a6396"></a>

```c
#define BT_UUID_CSC BT_UUID_DECLARE_16(BT_UUID_CSC_VAL)
```

相关声明：[BT_UUID_CSC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6514fa0098d12c02aa34c18e1e5a6396)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CSC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4d31b6944d378bcda7c8f7bfc74c5692)。

骑行速度与踏频服务（Cycling Speed and Cadence Service）。

<a id="r_gab063c1e5d2773927ce54c1745c7134d4"></a>

```c
#define BT_UUID_CPS_VAL 0x1818
```

相关声明：[BT_UUID_CPS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab063c1e5d2773927ce54c1745c7134d4)。

骑行功率服务（Cycling Power Service）的 UUID 值。

<a id="r_gac3c2895467ba651b8ebad709fdd44f6d"></a>

```c
#define BT_UUID_CPS BT_UUID_DECLARE_16(BT_UUID_CPS_VAL)
```

相关声明：[BT_UUID_CPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3c2895467ba651b8ebad709fdd44f6d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CPS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab063c1e5d2773927ce54c1745c7134d4)。

骑行功率服务（Cycling Power Service）。

<a id="r_ga36161c4e68b691cfb6a9f691a8f693dd"></a>

```c
#define BT_UUID_LNS_VAL 0x1819
```

相关声明：[BT_UUID_LNS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga36161c4e68b691cfb6a9f691a8f693dd)。

位置与导航服务（Location and Navigation Service）的 UUID 值。

<a id="r_gac48ea20cb0503dd748862862157e9224"></a>

```c
#define BT_UUID_LNS BT_UUID_DECLARE_16(BT_UUID_LNS_VAL)
```

相关声明：[BT_UUID_LNS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac48ea20cb0503dd748862862157e9224)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_LNS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga36161c4e68b691cfb6a9f691a8f693dd)。

位置与导航服务（Location and Navigation Service）。

<a id="r_ga8e8d24d0bf0a49713bbfa93cc2bdb0da"></a>

```c
#define BT_UUID_ESS_VAL 0x181a
```

相关声明：[BT_UUID_ESS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8e8d24d0bf0a49713bbfa93cc2bdb0da)。

环境感知服务（Environmental Sensing Service）的 UUID 值。

<a id="r_ga96c5958372c4fdba211b4f74d342a5b3"></a>

```c
#define BT_UUID_ESS BT_UUID_DECLARE_16(BT_UUID_ESS_VAL)
```

相关声明：[BT_UUID_ESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga96c5958372c4fdba211b4f74d342a5b3)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_ESS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8e8d24d0bf0a49713bbfa93cc2bdb0da)。

环境感知服务（Environmental Sensing Service）。

<a id="r_ga69baa896cd558487733cd575a6193e0d"></a>

```c
#define BT_UUID_BCS_VAL 0x181b
```

相关声明：[BT_UUID_BCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga69baa896cd558487733cd575a6193e0d)。

身体成分服务（Body Composition Service）的 UUID 值。

<a id="r_ga08170da6b471e937f64de6943b6e24bb"></a>

```c
#define BT_UUID_BCS BT_UUID_DECLARE_16(BT_UUID_BCS_VAL)
```

相关声明：[BT_UUID_BCS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga08170da6b471e937f64de6943b6e24bb)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga69baa896cd558487733cd575a6193e0d)。

身体成分服务（Body Composition Service）。

<a id="r_ga035ee545fdd640745b3bcbd8b7e7b3b6"></a>

```c
#define BT_UUID_UDS_VAL 0x181c
```

相关声明：[BT_UUID_UDS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga035ee545fdd640745b3bcbd8b7e7b3b6)。

用户数据服务（User Data Service）的 UUID 值。

<a id="r_gac6edbd84e5f0b454e130f835a32f1a44"></a>

```c
#define BT_UUID_UDS BT_UUID_DECLARE_16(BT_UUID_UDS_VAL)
```

相关声明：[BT_UUID_UDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac6edbd84e5f0b454e130f835a32f1a44)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_UDS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga035ee545fdd640745b3bcbd8b7e7b3b6)。

用户数据服务（User Data Service）。

<a id="r_ga6b6566f914d2c92c9b1bb4efd6efee98"></a>

```c
#define BT_UUID_WSS_VAL 0x181d
```

相关声明：[BT_UUID_WSS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6b6566f914d2c92c9b1bb4efd6efee98)。

体重秤服务（Weight Scale Service）的 UUID 值。

<a id="r_gaa5c518578e2620aafad915a0291dfe8f"></a>

```c
#define BT_UUID_WSS BT_UUID_DECLARE_16(BT_UUID_WSS_VAL)
```

相关声明：[BT_UUID_WSS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa5c518578e2620aafad915a0291dfe8f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_WSS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6b6566f914d2c92c9b1bb4efd6efee98)。

体重秤服务（Weight Scale Service）。

<a id="r_ga399ffbd6e7d3e50010383f2d521d8089"></a>

```c
#define BT_UUID_BMS_VAL 0x181e
```

相关声明：[BT_UUID_BMS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga399ffbd6e7d3e50010383f2d521d8089)。

绑定管理服务（Bond Management Service）的 UUID 值。

<a id="r_ga0a91114bf5e53c894d10d1e432223714"></a>

```c
#define BT_UUID_BMS BT_UUID_DECLARE_16(BT_UUID_BMS_VAL)
```

相关声明：[BT_UUID_BMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0a91114bf5e53c894d10d1e432223714)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BMS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga399ffbd6e7d3e50010383f2d521d8089)。

绑定管理服务（Bond Management Service）。

<a id="r_ga9726266ed3399a646999e19f639457a7"></a>

```c
#define BT_UUID_CGMS_VAL 0x181f
```

相关声明：[BT_UUID_CGMS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9726266ed3399a646999e19f639457a7)。

连续葡萄糖监测服务（Continuous Glucose Monitoring Service）的 UUID 值。

<a id="r_ga04767d3a7461b3508bce584704d92c75"></a>

```c
#define BT_UUID_CGMS BT_UUID_DECLARE_16(BT_UUID_CGMS_VAL)
```

相关声明：[BT_UUID_CGMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga04767d3a7461b3508bce584704d92c75)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CGMS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9726266ed3399a646999e19f639457a7)。

连续葡萄糖监测服务（Continuous Glucose Monitoring Service）。

<a id="r_gad8cc687442abd5eea3e367d2b859e2e8"></a>

```c
#define BT_UUID_IPSS_VAL 0x1820
```

相关声明：[BT_UUID_IPSS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad8cc687442abd5eea3e367d2b859e2e8)。

IP 支持服务（IP Support Service）的 UUID 值。

<a id="r_ga32f10a8bfb452aee43c64eec3c2d5a0f"></a>

```c
#define BT_UUID_IPSS BT_UUID_DECLARE_16(BT_UUID_IPSS_VAL)
```

相关声明：[BT_UUID_IPSS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga32f10a8bfb452aee43c64eec3c2d5a0f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_IPSS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad8cc687442abd5eea3e367d2b859e2e8)。

IP 支持服务（IP Support Service）。

<a id="r_ga8fafd81c36f6b515d2709d5f4efd9d00"></a>

```c
#define BT_UUID_IPS_VAL 0x1821
```

相关声明：[BT_UUID_IPS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8fafd81c36f6b515d2709d5f4efd9d00)。

室内定位服务（Indoor Positioning Service）的 UUID 值。

<a id="r_ga8dac7b88922315a2af06ad70cdfcfd0c"></a>

```c
#define BT_UUID_IPS BT_UUID_DECLARE_16(BT_UUID_IPS_VAL)
```

相关声明：[BT_UUID_IPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8dac7b88922315a2af06ad70cdfcfd0c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_IPS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8fafd81c36f6b515d2709d5f4efd9d00)。

室内定位服务（Indoor Positioning Service）。

<a id="r_gabfb8333e3fb8e819f02601ace836687b"></a>

```c
#define BT_UUID_POS_VAL 0x1822
```

相关声明：[BT_UUID_POS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabfb8333e3fb8e819f02601ace836687b)。

脉搏血氧仪服务（Pulse Oximeter Service）的 UUID 值。

<a id="r_gaa713f38e63cfc998559c862f80f2380b"></a>

```c
#define BT_UUID_POS BT_UUID_DECLARE_16(BT_UUID_POS_VAL)
```

相关声明：[BT_UUID_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa713f38e63cfc998559c862f80f2380b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_POS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabfb8333e3fb8e819f02601ace836687b)。

脉搏血氧仪服务（Pulse Oximeter Service）。

<a id="r_ga5f66d3e11dcde95c3c4e7055734c9aef"></a>

```c
#define BT_UUID_HPS_VAL 0x1823
```

相关声明：[BT_UUID_HPS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5f66d3e11dcde95c3c4e7055734c9aef)。

HTTP 代理服务（HTTP Proxy Service）的 UUID 值。

<a id="r_gaade9071b49d238d13edf57e90655c41c"></a>

```c
#define BT_UUID_HPS BT_UUID_DECLARE_16(BT_UUID_HPS_VAL)
```

相关声明：[BT_UUID_HPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaade9071b49d238d13edf57e90655c41c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HPS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5f66d3e11dcde95c3c4e7055734c9aef)。

HTTP 代理服务（HTTP Proxy Service）。

<a id="r_gafafc31de7e0d06e831ef13f5ddb88685"></a>

```c
#define BT_UUID_TDS_VAL 0x1824
```

相关声明：[BT_UUID_TDS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafafc31de7e0d06e831ef13f5ddb88685)。

传输发现服务（Transport Discovery Service）的 UUID 值。

<a id="r_gaccdb682d8f53c8560bea355a5376d72d"></a>

```c
#define BT_UUID_TDS BT_UUID_DECLARE_16(BT_UUID_TDS_VAL)
```

相关声明：[BT_UUID_TDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaccdb682d8f53c8560bea355a5376d72d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TDS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafafc31de7e0d06e831ef13f5ddb88685)。

传输发现服务（Transport Discovery Service）。

<a id="r_ga0a7a74bbb0c8bbd97d5fd6807deeb4c3"></a>

```c
#define BT_UUID_OTS_VAL 0x1825
```

相关声明：[BT_UUID_OTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0a7a74bbb0c8bbd97d5fd6807deeb4c3)。

对象传输服务（Object Transfer Service）的 UUID 值。

<a id="r_ga4f18867b63edde824c1a57c0ee354282"></a>

```c
#define BT_UUID_OTS BT_UUID_DECLARE_16(BT_UUID_OTS_VAL)
```

相关声明：[BT_UUID_OTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4f18867b63edde824c1a57c0ee354282)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0a7a74bbb0c8bbd97d5fd6807deeb4c3)。

对象传输服务（Object Transfer Service）。

<a id="r_ga036c6c7b6589a7178851ff7004aa64db"></a>

```c
#define BT_UUID_FMS_VAL 0x1826
```

相关声明：[BT_UUID_FMS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga036c6c7b6589a7178851ff7004aa64db)。

健身器械服务（Fitness Machine Service）的 UUID 值。

<a id="r_ga8935f33e5d388c96e38a172a5831b573"></a>

```c
#define BT_UUID_FMS BT_UUID_DECLARE_16(BT_UUID_FMS_VAL)
```

相关声明：[BT_UUID_FMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8935f33e5d388c96e38a172a5831b573)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_FMS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga036c6c7b6589a7178851ff7004aa64db)。

健身器械服务（Fitness Machine Service）。

<a id="r_gaa0bf05b5c11a3b6f9f0f8e48298b4776"></a>

```c
#define BT_UUID_MESH_PROV_VAL 0x1827
```

相关声明：[BT_UUID_MESH_PROV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa0bf05b5c11a3b6f9f0f8e48298b4776)。

网状网络配网服务（Mesh Provisioning Service）的 UUID 值。

<a id="r_ga665cc5a42b1b074536ce949fe1853f7b"></a>

```c
#define BT_UUID_MESH_PROV BT_UUID_DECLARE_16(BT_UUID_MESH_PROV_VAL)
```

相关声明：[BT_UUID_MESH_PROV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga665cc5a42b1b074536ce949fe1853f7b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MESH_PROV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa0bf05b5c11a3b6f9f0f8e48298b4776)。

网状网络配网服务（Mesh Provisioning Service）。

<a id="r_gaa347d1cf40b3eba7052c3e7c80e32a02"></a>

```c
#define BT_UUID_MESH_PROXY_VAL 0x1828
```

相关声明：[BT_UUID_MESH_PROXY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa347d1cf40b3eba7052c3e7c80e32a02)。

网状网络代理服务（Mesh Proxy Service）的 UUID 值。

<a id="r_ga34de82083c412e280bb585db519d70a2"></a>

```c
#define BT_UUID_MESH_PROXY BT_UUID_DECLARE_16(BT_UUID_MESH_PROXY_VAL)
```

相关声明：[BT_UUID_MESH_PROXY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga34de82083c412e280bb585db519d70a2)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MESH_PROXY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa347d1cf40b3eba7052c3e7c80e32a02)。

网状网络代理服务（Mesh Proxy Service）。

<a id="r_ga02eaaf8d7ec7981336713d4cb1ea6b6a"></a>

```c
#define BT_UUID_MESH_PROXY_SOLICITATION_VAL 0x1859
```

相关声明：[BT_UUID_MESH_PROXY_SOLICITATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga02eaaf8d7ec7981336713d4cb1ea6b6a)。

代理请求（Proxy Solicitation）的 UUID 值。

<a id="r_ga76f45a959cf7d4bb5b874ba2e2f8c5ad"></a>

```c
#define BT_UUID_RCSRV_VAL 0x1829
```

相关声明：[BT_UUID_RCSRV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga76f45a959cf7d4bb5b874ba2e2f8c5ad)。

重连接配置服务（Reconnection Configuration Service）的 UUID 值。

<a id="r_gafc39274d32d212b7b244f24809d00e15"></a>

```c
#define BT_UUID_RCSRV BT_UUID_DECLARE_16(BT_UUID_RCSRV_VAL)
```

相关声明：[BT_UUID_RCSRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafc39274d32d212b7b244f24809d00e15)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_RCSRV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga76f45a959cf7d4bb5b874ba2e2f8c5ad)。

重连接配置服务（Reconnection Configuration Service）。

<a id="r_gac1069e0c1a650aa7659942f0533cb384"></a>

```c
#define BT_UUID_IDS_VAL 0x183a
```

相关声明：[BT_UUID_IDS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac1069e0c1a650aa7659942f0533cb384)。

胰岛素输注服务（Insulin Delivery Service）的 UUID 值。

<a id="r_gac3921b7c5c31423d7ac7ed4338ccf980"></a>

```c
#define BT_UUID_IDS BT_UUID_DECLARE_16(BT_UUID_IDS_VAL)
```

相关声明：[BT_UUID_IDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3921b7c5c31423d7ac7ed4338ccf980)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_IDS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac1069e0c1a650aa7659942f0533cb384)。

胰岛素输注服务（Insulin Delivery Service）。

<a id="r_gaa75f32c09a7f70c1b79fb7af1b50c0fe"></a>

```c
#define BT_UUID_BSS_VAL 0x183b
```

相关声明：[BT_UUID_BSS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa75f32c09a7f70c1b79fb7af1b50c0fe)。

二值传感器服务（Binary Sensor Service）的 UUID 值。

<a id="r_gacc9ac8d5418e857f70b7836629874296"></a>

```c
#define BT_UUID_BSS BT_UUID_DECLARE_16(BT_UUID_BSS_VAL)
```

相关声明：[BT_UUID_BSS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacc9ac8d5418e857f70b7836629874296)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BSS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa75f32c09a7f70c1b79fb7af1b50c0fe)。

二值传感器服务（Binary Sensor Service）。

<a id="r_gabd1855b6ede9f8dcfa46b211ad7a33b5"></a>

```c
#define BT_UUID_ECS_VAL 0x183c
```

相关声明：[BT_UUID_ECS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabd1855b6ede9f8dcfa46b211ad7a33b5)。

紧急配置服务（Emergency Configuration Service）的 UUID 值。

<a id="r_ga966e2b5ad06522d4a6e882755fc4dcbf"></a>

```c
#define BT_UUID_ECS BT_UUID_DECLARE_16(BT_UUID_ECS_VAL)
```

相关声明：[BT_UUID_ECS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga966e2b5ad06522d4a6e882755fc4dcbf)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_ECS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabd1855b6ede9f8dcfa46b211ad7a33b5)。

紧急配置服务（Emergency Configuration Service）。

<a id="r_ga72b1d17c97437e7ced4e1c7c3fb9d0cd"></a>

```c
#define BT_UUID_ACLS_VAL 0x183d
```

相关声明：[BT_UUID_ACLS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga72b1d17c97437e7ced4e1c7c3fb9d0cd)。

授权控制服务（Authorization Control Service）的 UUID 值。

<a id="r_ga022390a0b44e81e0925e29a87fd4d1e3"></a>

```c
#define BT_UUID_ACLS BT_UUID_DECLARE_16(BT_UUID_ACLS_VAL)
```

相关声明：[BT_UUID_ACLS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga022390a0b44e81e0925e29a87fd4d1e3)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_ACLS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga72b1d17c97437e7ced4e1c7c3fb9d0cd)。

授权控制服务（Authorization Control Service）。

<a id="r_gaf85d03a7c42d040559874e6d1a6296a6"></a>

```c
#define BT_UUID_PAMS_VAL 0x183e
```

相关声明：[BT_UUID_PAMS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf85d03a7c42d040559874e6d1a6296a6)。

身体活动监测服务（Physical Activity Monitor Service）的 UUID 值。

<a id="r_ga3c5590637fc3c90c4beed23bab9f5eb6"></a>

```c
#define BT_UUID_PAMS BT_UUID_DECLARE_16(BT_UUID_PAMS_VAL)
```

相关声明：[BT_UUID_PAMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3c5590637fc3c90c4beed23bab9f5eb6)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_PAMS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf85d03a7c42d040559874e6d1a6296a6)。

身体活动监测服务（Physical Activity Monitor Service）。

<a id="r_ga1d21d600546eef483a96bc5c2e50cb66"></a>

```c
#define BT_UUID_ETS_VAL 0x183f
```

相关声明：[BT_UUID_ETS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1d21d600546eef483a96bc5c2e50cb66)。

经过时间服务（Elapsed Time Service）的 UUID 值。

<a id="r_ga27126fff5520f8dde63e795ebd69eded"></a>

```c
#define BT_UUID_ETS BT_UUID_DECLARE_16(BT_UUID_ETS_VAL)
```

相关声明：[BT_UUID_ETS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga27126fff5520f8dde63e795ebd69eded)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_ETS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1d21d600546eef483a96bc5c2e50cb66)。

经过时间服务（Elapsed Time Service）。

<a id="r_ga67f3c417689d2a7af32e9bacaa274d44"></a>

```c
#define BT_UUID_AICS_VAL 0x1843
```

相关声明：[BT_UUID_AICS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga67f3c417689d2a7af32e9bacaa274d44)。

音频输入控制服务（Audio Input Control Service）的 UUID 值。

<a id="r_ga8e7ec38a733ebe33d9d1d525a7c2c051"></a>

```c
#define BT_UUID_AICS BT_UUID_DECLARE_16(BT_UUID_AICS_VAL)
```

相关声明：[BT_UUID_AICS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8e7ec38a733ebe33d9d1d525a7c2c051)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_AICS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga67f3c417689d2a7af32e9bacaa274d44)。

音频输入控制服务（Audio Input Control Service）。

<a id="r_ga9de8d92b55a644904d5b7257608cba45"></a>

```c
#define BT_UUID_VCS_VAL 0x1844
```

相关声明：[BT_UUID_VCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9de8d92b55a644904d5b7257608cba45)。

音量控制服务（Volume Control Service）的 UUID 值。

<a id="r_gaaf797d6506d5f47e730e5bbf6ff79f7c"></a>

```c
#define BT_UUID_VCS BT_UUID_DECLARE_16(BT_UUID_VCS_VAL)
```

相关声明：[BT_UUID_VCS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaaf797d6506d5f47e730e5bbf6ff79f7c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_VCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9de8d92b55a644904d5b7257608cba45)。

音量控制服务（Volume Control Service）。

<a id="r_ga78b30023b019279b2b9567d7c3ffeac2"></a>

```c
#define BT_UUID_VOCS_VAL 0x1845
```

相关声明：[BT_UUID_VOCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga78b30023b019279b2b9567d7c3ffeac2)。

音量偏移控制服务（Volume Offset Control Service）的 UUID 值。

<a id="r_ga2ab2f92985ca0f65fb066df57c2f1433"></a>

```c
#define BT_UUID_VOCS BT_UUID_DECLARE_16(BT_UUID_VOCS_VAL)
```

相关声明：[BT_UUID_VOCS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2ab2f92985ca0f65fb066df57c2f1433)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_VOCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga78b30023b019279b2b9567d7c3ffeac2)。

音量偏移控制服务（Volume Offset Control Service）。

<a id="r_ga5f2c25e1c3f14fb65f062dc34f56b3ed"></a>

```c
#define BT_UUID_CSIS_VAL 0x1846
```

相关声明：[BT_UUID_CSIS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5f2c25e1c3f14fb65f062dc34f56b3ed)。

协调集合标识服务（Coordinated Set Identification Service）的 UUID 值。

<a id="r_ga111f2eb8e186444804b8b3c39f0f00a3"></a>

```c
#define BT_UUID_CSIS BT_UUID_DECLARE_16(BT_UUID_CSIS_VAL)
```

相关声明：[BT_UUID_CSIS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga111f2eb8e186444804b8b3c39f0f00a3)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CSIS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5f2c25e1c3f14fb65f062dc34f56b3ed)。

协调集合标识服务（Coordinated Set Identification Service）。

<a id="r_gad8fc6ade8cafce1b9461de0a27389c88"></a>

```c
#define BT_UUID_DTS_VAL 0x1847
```

相关声明：[BT_UUID_DTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad8fc6ade8cafce1b9461de0a27389c88)。

设备时间服务（Device Time Service）的 UUID 值。

<a id="r_ga6417c327841fd7317515e394f5ac0089"></a>

```c
#define BT_UUID_DTS BT_UUID_DECLARE_16(BT_UUID_DTS_VAL)
```

相关声明：[BT_UUID_DTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6417c327841fd7317515e394f5ac0089)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_DTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad8fc6ade8cafce1b9461de0a27389c88)。

设备时间服务（Device Time Service）。

<a id="r_ga3cd2f717c107a3e8d65eb958155884fd"></a>

```c
#define BT_UUID_MCS_VAL 0x1848
```

相关声明：[BT_UUID_MCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3cd2f717c107a3e8d65eb958155884fd)。

媒体控制服务（Media Control Service）的 UUID 值。

<a id="r_ga7b84d0b301ce2f565de7eb89165af0cf"></a>

```c
#define BT_UUID_MCS BT_UUID_DECLARE_16(BT_UUID_MCS_VAL)
```

相关声明：[BT_UUID_MCS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7b84d0b301ce2f565de7eb89165af0cf)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3cd2f717c107a3e8d65eb958155884fd)。

媒体控制服务（Media Control Service）。

<a id="r_ga35e8dae5a05985c10e3cdd610161ebcc"></a>

```c
#define BT_UUID_GMCS_VAL 0x1849
```

相关声明：[BT_UUID_GMCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga35e8dae5a05985c10e3cdd610161ebcc)。

通用媒体控制服务（Generic Media Control Service）的 UUID 值。

<a id="r_ga4efbadd4ce5a6fb64a5d9832b4626d0f"></a>

```c
#define BT_UUID_GMCS BT_UUID_DECLARE_16(BT_UUID_GMCS_VAL)
```

相关声明：[BT_UUID_GMCS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4efbadd4ce5a6fb64a5d9832b4626d0f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GMCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga35e8dae5a05985c10e3cdd610161ebcc)。

通用媒体控制服务（Generic Media Control Service）。

<a id="r_ga9e7f780e9800abc6fa86fa034482df4b"></a>

```c
#define BT_UUID_CTES_VAL 0x184a
```

相关声明：[BT_UUID_CTES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9e7f780e9800abc6fa86fa034482df4b)。

恒定音调扩展服务（Constant Tone Extension Service）的 UUID 值。

<a id="r_gaf85f0bff2abbe069d8d64a3eda2a066d"></a>

```c
#define BT_UUID_CTES BT_UUID_DECLARE_16(BT_UUID_CTES_VAL)
```

相关声明：[BT_UUID_CTES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf85f0bff2abbe069d8d64a3eda2a066d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CTES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9e7f780e9800abc6fa86fa034482df4b)。

恒定音调扩展服务（Constant Tone Extension Service）。

<a id="r_gae25bb19fe3d92555a9c2c2de6fae5354"></a>

```c
#define BT_UUID_TBS_VAL 0x184b
```

相关声明：[BT_UUID_TBS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae25bb19fe3d92555a9c2c2de6fae5354)。

电话承载服务（Telephone Bearer Service）的 UUID 值。

<a id="r_ga70c7991e602fa8c87868cac63c838c21"></a>

```c
#define BT_UUID_TBS BT_UUID_DECLARE_16(BT_UUID_TBS_VAL)
```

相关声明：[BT_UUID_TBS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga70c7991e602fa8c87868cac63c838c21)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TBS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae25bb19fe3d92555a9c2c2de6fae5354)。

电话承载服务（Telephone Bearer Service）。

<a id="r_ga1e90e6d7a97ca28b842012f61b76a2cb"></a>

```c
#define BT_UUID_GTBS_VAL 0x184c
```

相关声明：[BT_UUID_GTBS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1e90e6d7a97ca28b842012f61b76a2cb)。

通用电话承载服务（Generic Telephone Bearer Service）的 UUID 值。

<a id="r_gabb0810fa80d5623a5af457a2fb02ca6e"></a>

```c
#define BT_UUID_GTBS BT_UUID_DECLARE_16(BT_UUID_GTBS_VAL)
```

相关声明：[BT_UUID_GTBS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabb0810fa80d5623a5af457a2fb02ca6e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GTBS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1e90e6d7a97ca28b842012f61b76a2cb)。

通用电话承载服务（Generic Telephone Bearer Service）。

<a id="r_gac18fe10ee79d240af7c494fab0304d90"></a>

```c
#define BT_UUID_MICS_VAL 0x184d
```

相关声明：[BT_UUID_MICS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac18fe10ee79d240af7c494fab0304d90)。

麦克风控制服务（Microphone Control Service）的 UUID 值。

<a id="r_ga411a51f52e6e63c905d86ce5b924e69c"></a>

```c
#define BT_UUID_MICS BT_UUID_DECLARE_16(BT_UUID_MICS_VAL)
```

相关声明：[BT_UUID_MICS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga411a51f52e6e63c905d86ce5b924e69c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MICS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac18fe10ee79d240af7c494fab0304d90)。

麦克风控制服务（Microphone Control Service）。

<a id="r_gaedc903cd915524adfa5d4d64fa38cf22"></a>

```c
#define BT_UUID_ASCS_VAL 0x184e
```

相关声明：[BT_UUID_ASCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaedc903cd915524adfa5d4d64fa38cf22)。

音频流控制服务（Audio Stream Control Service）的 UUID 值。

<a id="r_ga7d52614d936753738fb04f124c97fc09"></a>

```c
#define BT_UUID_ASCS BT_UUID_DECLARE_16(BT_UUID_ASCS_VAL)
```

相关声明：[BT_UUID_ASCS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7d52614d936753738fb04f124c97fc09)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_ASCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaedc903cd915524adfa5d4d64fa38cf22)。

音频流控制服务（Audio Stream Control Service）。

<a id="r_gaa671703a706fc97dcc9a4b1dd7f4fef3"></a>

```c
#define BT_UUID_BASS_VAL 0x184f
```

相关声明：[BT_UUID_BASS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa671703a706fc97dcc9a4b1dd7f4fef3)。

广播音频扫描服务（Broadcast Audio Scan Service）的 UUID 值。

<a id="r_ga7d0e06ae7e089098ac9d0c32087d5803"></a>

```c
#define BT_UUID_BASS BT_UUID_DECLARE_16(BT_UUID_BASS_VAL)
```

相关声明：[BT_UUID_BASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7d0e06ae7e089098ac9d0c32087d5803)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BASS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa671703a706fc97dcc9a4b1dd7f4fef3)。

广播音频扫描服务（Broadcast Audio Scan Service）。

<a id="r_ga69dafd580d116dec74b54c818d5c275b"></a>

```c
#define BT_UUID_PACS_VAL 0x1850
```

相关声明：[BT_UUID_PACS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga69dafd580d116dec74b54c818d5c275b)。

已发布音频能力服务（Published Audio Capabilities Service）的 UUID 值。

<a id="r_ga86720eb2ad6aa3f66a9bf2248cb95383"></a>

```c
#define BT_UUID_PACS BT_UUID_DECLARE_16(BT_UUID_PACS_VAL)
```

相关声明：[BT_UUID_PACS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga86720eb2ad6aa3f66a9bf2248cb95383)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_PACS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga69dafd580d116dec74b54c818d5c275b)。

已发布音频能力服务（Published Audio Capabilities Service）。

<a id="r_gaa1c0efca17e5b3de3c0fd254181a53db"></a>

```c
#define BT_UUID_BASIC_AUDIO_VAL 0x1851
```

相关声明：[BT_UUID_BASIC_AUDIO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa1c0efca17e5b3de3c0fd254181a53db)。

基本音频公告服务（Basic Audio Announcement Service）的 UUID 值。

<a id="r_ga842f48f68be48c3379161b595fca22a2"></a>

```c
#define BT_UUID_BASIC_AUDIO BT_UUID_DECLARE_16(BT_UUID_BASIC_AUDIO_VAL)
```

相关声明：[BT_UUID_BASIC_AUDIO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga842f48f68be48c3379161b595fca22a2)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BASIC_AUDIO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa1c0efca17e5b3de3c0fd254181a53db)。

基本音频公告服务（Basic Audio Announcement Service）。

<a id="r_ga0c67f9e1a5fef34fd1fddc539e20119b"></a>

```c
#define BT_UUID_BROADCAST_AUDIO_VAL 0x1852
```

相关声明：[BT_UUID_BROADCAST_AUDIO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0c67f9e1a5fef34fd1fddc539e20119b)。

广播音频公告服务（Broadcast Audio Announcement Service）的 UUID 值。

<a id="r_gafe9b1d539a9c77037e0c8433b702790e"></a>

```c
#define BT_UUID_BROADCAST_AUDIO BT_UUID_DECLARE_16(BT_UUID_BROADCAST_AUDIO_VAL)
```

相关声明：[BT_UUID_BROADCAST_AUDIO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafe9b1d539a9c77037e0c8433b702790e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BROADCAST_AUDIO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0c67f9e1a5fef34fd1fddc539e20119b)。

广播音频公告服务（Broadcast Audio Announcement Service）。

<a id="r_gab3f48a2a32b3a2061f3b108350c59ec4"></a>

```c
#define BT_UUID_CAS_VAL 0x1853
```

相关声明：[BT_UUID_CAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab3f48a2a32b3a2061f3b108350c59ec4)。

通用音频服务（Common Audio Service）的 UUID 值。

<a id="r_gab69a851e430a0232abb839b0d9fc54e5"></a>

```c
#define BT_UUID_CAS BT_UUID_DECLARE_16(BT_UUID_CAS_VAL)
```

相关声明：[BT_UUID_CAS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab69a851e430a0232abb839b0d9fc54e5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab3f48a2a32b3a2061f3b108350c59ec4)。

通用音频服务（Common Audio Service）。

<a id="r_ga8d937e82611aaa2da305795d00074c93"></a>

```c
#define BT_UUID_HAS_VAL 0x1854
```

相关声明：[BT_UUID_HAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8d937e82611aaa2da305795d00074c93)。

助听访问服务（Hearing Access Service）的 UUID 值。

<a id="r_gac5acaee5423acd4531768fbf8844676b"></a>

```c
#define BT_UUID_HAS BT_UUID_DECLARE_16(BT_UUID_HAS_VAL)
```

相关声明：[BT_UUID_HAS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac5acaee5423acd4531768fbf8844676b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8d937e82611aaa2da305795d00074c93)。

助听访问服务（Hearing Access Service）。

<a id="r_ga42f0d2bf3ce4a258a6f9d14a828cf422"></a>

```c
#define BT_UUID_TMAS_VAL 0x1855
```

相关声明：[BT_UUID_TMAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga42f0d2bf3ce4a258a6f9d14a828cf422)。

电话与媒体音频服务（Telephony and Media Audio Service）的 UUID 值。

<a id="r_ga84ea43f70dee139497be28d90db70104"></a>

```c
#define BT_UUID_TMAS BT_UUID_DECLARE_16(BT_UUID_TMAS_VAL)
```

相关声明：[BT_UUID_TMAS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga84ea43f70dee139497be28d90db70104)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TMAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga42f0d2bf3ce4a258a6f9d14a828cf422)。

电话与媒体音频服务（Telephony and Media Audio Service）。

<a id="r_ga06265a1d97c1b734340f9eb0055da913"></a>

```c
#define BT_UUID_PBA_VAL 0x1856
```

相关声明：[BT_UUID_PBA_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga06265a1d97c1b734340f9eb0055da913)。

公共广播公告服务（Public Broadcast Announcement Service）的 UUID 值。

<a id="r_ga98f4f946c1bca483a7e81cad162ee0b1"></a>

```c
#define BT_UUID_PBA BT_UUID_DECLARE_16(BT_UUID_PBA_VAL)
```

相关声明：[BT_UUID_PBA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga98f4f946c1bca483a7e81cad162ee0b1)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_PBA_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga06265a1d97c1b734340f9eb0055da913)。

公共广播公告服务（Public Broadcast Announcement Service）。

<a id="r_ga8244f6edaf3a347be1a3bf4e1d8fb4c3"></a>

```c
#define BT_UUID_GATT_PRIMARY_VAL 0x2800
```

相关声明：[BT_UUID_GATT_PRIMARY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8244f6edaf3a347be1a3bf4e1d8fb4c3)。

GATT 主服务（GATT Primary Service）的 UUID 值。

<a id="r_ga6e87ce1575494eb90358e074e8dbe276"></a>

```c
#define BT_UUID_GATT_PRIMARY BT_UUID_DECLARE_16(BT_UUID_GATT_PRIMARY_VAL)
```

相关声明：[BT_UUID_GATT_PRIMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6e87ce1575494eb90358e074e8dbe276)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_PRIMARY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8244f6edaf3a347be1a3bf4e1d8fb4c3)。

GATT 主服务（GATT Primary Service）。

<a id="r_ga764703eec266d58b0ea9e00d02f23d1d"></a>

```c
#define BT_UUID_GATT_SECONDARY_VAL 0x2801
```

相关声明：[BT_UUID_GATT_SECONDARY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga764703eec266d58b0ea9e00d02f23d1d)。

GATT 次服务（GATT Secondary Service）的 UUID 值。

<a id="r_gad084d3658e663b6b8e200be256c54cdb"></a>

```c
#define BT_UUID_GATT_SECONDARY BT_UUID_DECLARE_16(BT_UUID_GATT_SECONDARY_VAL)
```

相关声明：[BT_UUID_GATT_SECONDARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad084d3658e663b6b8e200be256c54cdb)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SECONDARY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga764703eec266d58b0ea9e00d02f23d1d)。

GATT 次服务（GATT Secondary Service）。

<a id="r_gaa493141bce2425fe40f809f151ace673"></a>

```c
#define BT_UUID_GATT_INCLUDE_VAL 0x2802
```

相关声明：[BT_UUID_GATT_INCLUDE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa493141bce2425fe40f809f151ace673)。

GATT 包含服务（GATT Include Service）的 UUID 值。

<a id="r_ga995596ff7374ebcb44d4706bc16234e4"></a>

```c
#define BT_UUID_GATT_INCLUDE BT_UUID_DECLARE_16(BT_UUID_GATT_INCLUDE_VAL)
```

相关声明：[BT_UUID_GATT_INCLUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga995596ff7374ebcb44d4706bc16234e4)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_INCLUDE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa493141bce2425fe40f809f151ace673)。

GATT 包含服务（GATT Include Service）。

<a id="r_gae8b1af5f3458ca8523db83a3d8ccc62c"></a>

```c
#define BT_UUID_GATT_CHRC_VAL 0x2803
```

相关声明：[BT_UUID_GATT_CHRC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae8b1af5f3458ca8523db83a3d8ccc62c)。

GATT 特征（GATT Characteristic）的 UUID 值。

<a id="r_gadcedbbe1c432c4ac737e54b318e01a0f"></a>

```c
#define BT_UUID_GATT_CHRC BT_UUID_DECLARE_16(BT_UUID_GATT_CHRC_VAL)
```

相关声明：[BT_UUID_GATT_CHRC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadcedbbe1c432c4ac737e54b318e01a0f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CHRC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae8b1af5f3458ca8523db83a3d8ccc62c)。

GATT 特征（GATT Characteristic）。

<a id="r_ga68b7ae19aad514e4a6731796c34c59da"></a>

```c
#define BT_UUID_GATT_CEP_VAL 0x2900
```

相关声明：[BT_UUID_GATT_CEP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga68b7ae19aad514e4a6731796c34c59da)。

GATT 特征扩展属性（GATT Characteristic Extended Properties）的 UUID 值。

<a id="r_ga6aa143b721d810f1536d7431a9bf7cc7"></a>

```c
#define BT_UUID_GATT_CEP BT_UUID_DECLARE_16(BT_UUID_GATT_CEP_VAL)
```

相关声明：[特征扩展属性 UUID（Characteristic Extended Properties UUID）：`BT_UUID_GATT_CEP`。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6aa143b721d810f1536d7431a9bf7cc7)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CEP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga68b7ae19aad514e4a6731796c34c59da)。

GATT 特征扩展属性（GATT Characteristic Extended Properties）。

<a id="r_ga2a168fa660bc6c3c3d5a85d99f2c9e60"></a>

```c
#define BT_UUID_GATT_CUD_VAL 0x2901
```

相关声明：[BT_UUID_GATT_CUD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2a168fa660bc6c3c3d5a85d99f2c9e60)。

GATT 特征用户描述（GATT Characteristic User Description）的 UUID 值。

<a id="r_gaaaf94f5d918a1b6715cf4816b03875a2"></a>

```c
#define BT_UUID_GATT_CUD BT_UUID_DECLARE_16(BT_UUID_GATT_CUD_VAL)
```

相关声明：[BT_UUID_GATT_CUD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaaaf94f5d918a1b6715cf4816b03875a2)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CUD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2a168fa660bc6c3c3d5a85d99f2c9e60)。

GATT 特征用户描述（GATT Characteristic User Description）。

<a id="r_gaa7807cb9ed1aa19f48c7dc4904f52dbb"></a>

```c
#define BT_UUID_GATT_CCC_VAL 0x2902
```

相关声明：[BT_UUID_GATT_CCC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa7807cb9ed1aa19f48c7dc4904f52dbb)。

GATT 客户端特征配置（GATT Client Characteristic Configuration）的 UUID 值。

<a id="r_ga03a2d3f0ce89508b794d5c87a4303057"></a>

```c
#define BT_UUID_GATT_CCC BT_UUID_DECLARE_16(BT_UUID_GATT_CCC_VAL)
```

相关声明：[客户端特征配置 UUID（Client Characteristic Configuration UUID）：`BT_UUID_GATT_CCC`。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga03a2d3f0ce89508b794d5c87a4303057)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CCC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa7807cb9ed1aa19f48c7dc4904f52dbb)。

GATT 客户端特征配置（GATT Client Characteristic Configuration）。

<a id="r_ga84cc4d600b5218baf5620b87cb8ddc55"></a>

```c
#define BT_UUID_GATT_SCC_VAL 0x2903
```

相关声明：[BT_UUID_GATT_SCC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga84cc4d600b5218baf5620b87cb8ddc55)。

GATT 服务器特征配置（GATT Server Characteristic Configuration）的 UUID 值。

<a id="r_ga82567cdce8c4411cd3daf26711ba9685"></a>

```c
#define BT_UUID_GATT_SCC BT_UUID_DECLARE_16(BT_UUID_GATT_SCC_VAL)
```

相关声明：[服务器特征配置 UUID（Server Characteristic Configuration UUID）：`BT_UUID_GATT_SCC`。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga82567cdce8c4411cd3daf26711ba9685)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SCC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga84cc4d600b5218baf5620b87cb8ddc55)。

GATT 服务器特征配置（GATT Server Characteristic Configuration）。

<a id="r_ga71924f95ca117ace35e64b0222bb5bf7"></a>

```c
#define BT_UUID_GATT_CPF_VAL 0x2904
```

相关声明：[BT_UUID_GATT_CPF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga71924f95ca117ace35e64b0222bb5bf7)。

GATT 特征表示格式（GATT Characteristic Presentation Format）的 UUID 值。

<a id="r_ga331a61702ffe9b15bac0de3d60414022"></a>

```c
#define BT_UUID_GATT_CPF BT_UUID_DECLARE_16(BT_UUID_GATT_CPF_VAL)
```

相关声明：[特征呈现格式 UUID（Characteristic Presentation Format UUID）：`BT_UUID_GATT_CPF`。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga331a61702ffe9b15bac0de3d60414022)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CPF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga71924f95ca117ace35e64b0222bb5bf7)。

GATT 特征表示格式（GATT Characteristic Presentation Format）。

<a id="r_ga88dbd0deac028cb0df1a6bd1874aec7f"></a>

```c
#define BT_UUID_GATT_CAF_VAL 0x2905
```

相关声明：[BT_UUID_GATT_CAF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga88dbd0deac028cb0df1a6bd1874aec7f)。

GATT 特征聚合格式（GATT Characteristic Aggregated Format）的 UUID 值。

<a id="r_gadc590b4039c9f47965e88e57b5589a93"></a>

```c
#define BT_UUID_GATT_CAF BT_UUID_DECLARE_16(BT_UUID_GATT_CAF_VAL)
```

相关声明：[BT_UUID_GATT_CAF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadc590b4039c9f47965e88e57b5589a93)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CAF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga88dbd0deac028cb0df1a6bd1874aec7f)。

GATT 特征聚合格式（GATT Characteristic Aggregated Format）。

<a id="r_ga6fa0e8a8f2727e4646461ca14247466f"></a>

```c
#define BT_UUID_VALID_RANGE_VAL 0x2906
```

相关声明：[BT_UUID_VALID_RANGE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6fa0e8a8f2727e4646461ca14247466f)。

有效范围描述符（Valid Range Descriptor）的 UUID 值。

<a id="r_gad53d373df905c4b11c39a3ae4284a6d1"></a>

```c
#define BT_UUID_VALID_RANGE BT_UUID_DECLARE_16(BT_UUID_VALID_RANGE_VAL)
```

相关声明：[BT_UUID_VALID_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad53d373df905c4b11c39a3ae4284a6d1)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_VALID_RANGE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6fa0e8a8f2727e4646461ca14247466f)。

有效范围描述符（Valid Range Descriptor）。

<a id="r_gaa8e06b1198ea23a01e892080df88e7f4"></a>

```c
#define BT_UUID_HIDS_EXT_REPORT_VAL 0x2907
```

相关声明：[BT_UUID_HIDS_EXT_REPORT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa8e06b1198ea23a01e892080df88e7f4)。

HID 外部报告描述符（HID External Report Descriptor）的 UUID 值。

<a id="r_gae945ad8eac1b444d92096c76239e106d"></a>

```c
#define BT_UUID_HIDS_EXT_REPORT BT_UUID_DECLARE_16(BT_UUID_HIDS_EXT_REPORT_VAL)
```

相关声明：[BT_UUID_HIDS_EXT_REPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae945ad8eac1b444d92096c76239e106d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HIDS_EXT_REPORT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa8e06b1198ea23a01e892080df88e7f4)。

HID 外部报告描述符（HID External Report Descriptor）。

<a id="r_ga4c1f2a0f52f101910f9294b10b5af484"></a>

```c
#define BT_UUID_HIDS_REPORT_REF_VAL 0x2908
```

相关声明：[BT_UUID_HIDS_REPORT_REF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4c1f2a0f52f101910f9294b10b5af484)。

HID 报告引用描述符（HID Report Reference Descriptor）的 UUID 值。

<a id="r_ga001e019b08f5f88a158ed0861c017609"></a>

```c
#define BT_UUID_HIDS_REPORT_REF BT_UUID_DECLARE_16(BT_UUID_HIDS_REPORT_REF_VAL)
```

相关声明：[BT_UUID_HIDS_REPORT_REF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga001e019b08f5f88a158ed0861c017609)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HIDS_REPORT_REF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4c1f2a0f52f101910f9294b10b5af484)。

HID 报告引用描述符（HID Report Reference Descriptor）。

<a id="r_ga882af0a9286c487c1f108346be9af304"></a>

```c
#define BT_UUID_VAL_TRIGGER_SETTING_VAL 0x290a
```

相关声明：[BT_UUID_VAL_TRIGGER_SETTING_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga882af0a9286c487c1f108346be9af304)。

数值触发设置描述符（Value Trigger Setting Descriptor）的 UUID 值。

<a id="r_ga2601c8bcfd2efae9b20e67f5c95de3f1"></a>

```c
#define BT_UUID_VAL_TRIGGER_SETTING BT_UUID_DECLARE_16(BT_UUID_VAL_TRIGGER_SETTING_VAL)
```

相关声明：[BT_UUID_VAL_TRIGGER_SETTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2601c8bcfd2efae9b20e67f5c95de3f1)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_VAL_TRIGGER_SETTING_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga882af0a9286c487c1f108346be9af304)。

数值触发设置描述符（Value Trigger Setting Descriptor）。

<a id="r_ga85eab7f3dbd2f517d36e750d3c020dec"></a>

```c
#define BT_UUID_ES_CONFIGURATION_VAL 0x290b
```

相关声明：[BT_UUID_ES_CONFIGURATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga85eab7f3dbd2f517d36e750d3c020dec)。

环境感知配置描述符（Environmental Sensing Configuration Descriptor）的 UUID 值。

<a id="r_gae2d7028c5102df6f53765a98b9b729ea"></a>

```c
#define BT_UUID_ES_CONFIGURATION BT_UUID_DECLARE_16(BT_UUID_ES_CONFIGURATION_VAL)
```

相关声明：[BT_UUID_ES_CONFIGURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae2d7028c5102df6f53765a98b9b729ea)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_ES_CONFIGURATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga85eab7f3dbd2f517d36e750d3c020dec)。

环境感知配置描述符（Environmental Sensing Configuration Descriptor）。

<a id="r_ga8758259d984c0391feeceb459591e2fb"></a>

```c
#define BT_UUID_ES_MEASUREMENT_VAL 0x290c
```

相关声明：[BT_UUID_ES_MEASUREMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8758259d984c0391feeceb459591e2fb)。

环境感知测量描述符（Environmental Sensing Measurement Descriptor）的 UUID 值。

<a id="r_ga5e738598773234b87a1db746badce304"></a>

```c
#define BT_UUID_ES_MEASUREMENT BT_UUID_DECLARE_16(BT_UUID_ES_MEASUREMENT_VAL)
```

相关声明：[BT_UUID_ES_MEASUREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5e738598773234b87a1db746badce304)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_ES_MEASUREMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8758259d984c0391feeceb459591e2fb)。

环境感知测量描述符（Environmental Sensing Measurement Descriptor）。

<a id="r_ga0da1b874a844e15cdf185c6e7cbc9d64"></a>

```c
#define BT_UUID_ES_TRIGGER_SETTING_VAL 0x290d
```

相关声明：[BT_UUID_ES_TRIGGER_SETTING_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0da1b874a844e15cdf185c6e7cbc9d64)。

环境感知触发设置描述符（Environmental Sensing Trigger Setting Descriptor）的 UUID 值。

<a id="r_gab9daf129a8625853989516032010f1a3"></a>

```c
#define BT_UUID_ES_TRIGGER_SETTING BT_UUID_DECLARE_16(BT_UUID_ES_TRIGGER_SETTING_VAL)
```

相关声明：[BT_UUID_ES_TRIGGER_SETTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab9daf129a8625853989516032010f1a3)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_ES_TRIGGER_SETTING_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0da1b874a844e15cdf185c6e7cbc9d64)。

环境感知触发设置描述符（Environmental Sensing Trigger Setting Descriptor）。

<a id="r_gacacc7a2120d918c46a45cde0b0a8e44b"></a>

```c
#define BT_UUID_TM_TRIGGER_SETTING_VAL 0x290e
```

相关声明：[BT_UUID_TM_TRIGGER_SETTING_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacacc7a2120d918c46a45cde0b0a8e44b)。

时间触发设置描述符（Time Trigger Setting Descriptor）的 UUID 值。

<a id="r_ga017b04e00401d50fc33cfd34d218492c"></a>

```c
#define BT_UUID_TM_TRIGGER_SETTING BT_UUID_DECLARE_16(BT_UUID_TM_TRIGGER_SETTING_VAL)
```

相关声明：[BT_UUID_TM_TRIGGER_SETTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga017b04e00401d50fc33cfd34d218492c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TM_TRIGGER_SETTING_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacacc7a2120d918c46a45cde0b0a8e44b)。

时间触发设置描述符（Time Trigger Setting Descriptor）。

<a id="r_gac7a400574b6c78638e41eeaf97b7e9f3"></a>

```c
#define BT_UUID_GAP_DEVICE_NAME_VAL 0x2a00
```

相关声明：[BT_UUID_GAP_DEVICE_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac7a400574b6c78638e41eeaf97b7e9f3)。

GAP 设备名称特征（GAP Characteristic Device Name）的 UUID 值。

<a id="r_ga2bda01c9df904c8d0260ca3c0e3924cb"></a>

```c
#define BT_UUID_GAP_DEVICE_NAME BT_UUID_DECLARE_16(BT_UUID_GAP_DEVICE_NAME_VAL)
```

相关声明：[BT_UUID_GAP_DEVICE_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2bda01c9df904c8d0260ca3c0e3924cb)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GAP_DEVICE_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac7a400574b6c78638e41eeaf97b7e9f3)。

GAP 设备名称特征（GAP Characteristic Device Name）。

<a id="r_ga8789efbc24ac67479a86c3dfa0379154"></a>

```c
#define BT_UUID_GAP_APPEARANCE_VAL 0x2a01
```

相关声明：[BT_UUID_GAP_APPEARANCE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8789efbc24ac67479a86c3dfa0379154)。

GAP 外观特征（GAP Characteristic Appearance）的 UUID 值。

<a id="r_ga4354d250e2cfca4fc868134bca4178b0"></a>

```c
#define BT_UUID_GAP_APPEARANCE BT_UUID_DECLARE_16(BT_UUID_GAP_APPEARANCE_VAL)
```

相关声明：[BT_UUID_GAP_APPEARANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4354d250e2cfca4fc868134bca4178b0)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GAP_APPEARANCE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8789efbc24ac67479a86c3dfa0379154)。

GAP 外观特征（GAP Characteristic Appearance）。

<a id="r_ga575ef013a228bb5bb728724c9334347f"></a>

```c
#define BT_UUID_GAP_PPF_VAL 0x2a02
```

相关声明：[BT_UUID_GAP_PPF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga575ef013a228bb5bb728724c9334347f)。

GAP 外围设备隐私标志特征（GAP Characteristic Peripheral Privacy Flag）的 UUID 值。

<a id="r_ga4bec5c6656a10756a38ac9a6805f9757"></a>

```c
#define BT_UUID_GAP_PPF BT_UUID_DECLARE_16(BT_UUID_GAP_PPF_VAL)
```

相关声明：[BT_UUID_GAP_PPF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4bec5c6656a10756a38ac9a6805f9757)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GAP_PPF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga575ef013a228bb5bb728724c9334347f)。

GAP 外围设备隐私标志特征（GAP Characteristic Peripheral Privacy Flag）。

<a id="r_ga739961cc85dd01779228f5054a3c3790"></a>

```c
#define BT_UUID_GAP_RA_VAL 0x2a03
```

相关声明：[BT_UUID_GAP_RA_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga739961cc85dd01779228f5054a3c3790)。

GAP 重连接地址特征（GAP Characteristic Reconnection Address）的 UUID 值。

<a id="r_ga569663025aceabcd964f9c423ab030b5"></a>

```c
#define BT_UUID_GAP_RA BT_UUID_DECLARE_16(BT_UUID_GAP_RA_VAL)
```

相关声明：[BT_UUID_GAP_RA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga569663025aceabcd964f9c423ab030b5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GAP_RA_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga739961cc85dd01779228f5054a3c3790)。

GAP 重连接地址特征（GAP Characteristic Reconnection Address）。

<a id="r_ga08be6df54da61393b3fe4efb7ab70b71"></a>

```c
#define BT_UUID_GAP_PPCP_VAL 0x2a04
```

相关声明：[BT_UUID_GAP_PPCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga08be6df54da61393b3fe4efb7ab70b71)。

GAP 外围设备首选连接参数特征（GAP Characteristic Peripheral Preferred Connection Parameters）的 UUID 值。

<a id="r_gad174f313309b1bbb1208c61769566c77"></a>

```c
#define BT_UUID_GAP_PPCP BT_UUID_DECLARE_16(BT_UUID_GAP_PPCP_VAL)
```

相关声明：[BT_UUID_GAP_PPCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad174f313309b1bbb1208c61769566c77)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GAP_PPCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga08be6df54da61393b3fe4efb7ab70b71)。

GAP 外围设备首选连接参数特征（GAP Characteristic Peripheral Preferred Connection Parameters）。

<a id="r_gaf7af098d1487b3e09ded21b4490c50e0"></a>

```c
#define BT_UUID_GATT_SC_VAL 0x2a05
```

相关声明：[BT_UUID_GATT_SC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf7af098d1487b3e09ded21b4490c50e0)。

GATT 服务已变更特征（GATT Characteristic Service Changed）的 UUID 值。

<a id="r_gad0609fd8c275c69cd0aabb7ba7c0f628"></a>

```c
#define BT_UUID_GATT_SC BT_UUID_DECLARE_16(BT_UUID_GATT_SC_VAL)
```

相关声明：[BT_UUID_GATT_SC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad0609fd8c275c69cd0aabb7ba7c0f628)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf7af098d1487b3e09ded21b4490c50e0)。

GATT 服务已变更特征（GATT Characteristic Service Changed）。

<a id="r_ga2df4fc4fb971330cb7462911b68f73fd"></a>

```c
#define BT_UUID_ALERT_LEVEL_VAL 0x2a06
```

相关声明：[BT_UUID_ALERT_LEVEL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2df4fc4fb971330cb7462911b68f73fd)。

GATT 告警级别特征（GATT Characteristic Alert Level）的 UUID 值。

<a id="r_ga400e07242af41e836dfc250dc41cb010"></a>

```c
#define BT_UUID_ALERT_LEVEL BT_UUID_DECLARE_16(BT_UUID_ALERT_LEVEL_VAL)
```

相关声明：[BT_UUID_ALERT_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga400e07242af41e836dfc250dc41cb010)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_ALERT_LEVEL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2df4fc4fb971330cb7462911b68f73fd)。

GATT 告警级别特征（GATT Characteristic Alert Level）。

<a id="r_ga07f1f99a8e237304f9415fade56432e4"></a>

```c
#define BT_UUID_TPS_TX_POWER_LEVEL_VAL 0x2a07
```

相关声明：[BT_UUID_TPS_TX_POWER_LEVEL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga07f1f99a8e237304f9415fade56432e4)。

TPS 发送功率级别特征（TPS Characteristic Tx Power Level）的 UUID 值。

<a id="r_gade253bd200b4d2ea9f0463c3911295f1"></a>

```c
#define BT_UUID_TPS_TX_POWER_LEVEL BT_UUID_DECLARE_16(BT_UUID_TPS_TX_POWER_LEVEL_VAL)
```

相关声明：[BT_UUID_TPS_TX_POWER_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gade253bd200b4d2ea9f0463c3911295f1)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TPS_TX_POWER_LEVEL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga07f1f99a8e237304f9415fade56432e4)。

TPS 发送功率级别特征（TPS Characteristic Tx Power Level）。

<a id="r_ga71d42d8e00aa0b388315aeeb68c29839"></a>

```c
#define BT_UUID_GATT_DT_VAL 0x2a08
```

相关声明：[BT_UUID_GATT_DT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga71d42d8e00aa0b388315aeeb68c29839)。

GATT 日期时间特征（GATT Characteristic Date Time）的 UUID 值。

<a id="r_ga09cd4c6c81b8393f19b765a01ec556a0"></a>

```c
#define BT_UUID_GATT_DT BT_UUID_DECLARE_16(BT_UUID_GATT_DT_VAL)
```

相关声明：[BT_UUID_GATT_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga09cd4c6c81b8393f19b765a01ec556a0)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_DT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga71d42d8e00aa0b388315aeeb68c29839)。

GATT 日期时间特征（GATT Characteristic Date Time）。

<a id="r_ga952c7341d02dd4bf3cea142b0b41e41c"></a>

```c
#define BT_UUID_GATT_DW_VAL 0x2a09
```

相关声明：[BT_UUID_GATT_DW_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga952c7341d02dd4bf3cea142b0b41e41c)。

GATT 星期特征（GATT Characteristic Day of Week）的 UUID 值。

<a id="r_ga442781cffe3da4bff3c8903d46ae07a0"></a>

```c
#define BT_UUID_GATT_DW BT_UUID_DECLARE_16(BT_UUID_GATT_DW_VAL)
```

相关声明：[BT_UUID_GATT_DW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga442781cffe3da4bff3c8903d46ae07a0)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_DW_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga952c7341d02dd4bf3cea142b0b41e41c)。

GATT 星期特征（GATT Characteristic Day of Week）。

<a id="r_ga02fd005f86fd9995d61f63c3e7735028"></a>

```c
#define BT_UUID_GATT_DDT_VAL 0x2a0a
```

相关声明：[BT_UUID_GATT_DDT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga02fd005f86fd9995d61f63c3e7735028)。

GATT 星期日期时间特征（GATT Characteristic Day Date Time）的 UUID 值。

<a id="r_gaee156d97abd11f1422677bbb08cd5193"></a>

```c
#define BT_UUID_GATT_DDT BT_UUID_DECLARE_16(BT_UUID_GATT_DDT_VAL)
```

相关声明：[BT_UUID_GATT_DDT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaee156d97abd11f1422677bbb08cd5193)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_DDT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga02fd005f86fd9995d61f63c3e7735028)。

GATT 星期日期时间特征（GATT Characteristic Day Date Time）。

<a id="r_ga195fc66b479dec1131ea5e7cf1350afb"></a>

```c
#define BT_UUID_GATT_ET256_VAL 0x2a0c
```

相关声明：[BT_UUID_GATT_ET256_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga195fc66b479dec1131ea5e7cf1350afb)。

GATT 精确时间 256 特征（GATT Characteristic Exact Time 256）的 UUID 值。

<a id="r_ga3d5472767d50ddeabcdc7e2961610b78"></a>

```c
#define BT_UUID_GATT_ET256 BT_UUID_DECLARE_16(BT_UUID_GATT_ET256_VAL)
```

相关声明：[BT_UUID_GATT_ET256](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3d5472767d50ddeabcdc7e2961610b78)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ET256_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga195fc66b479dec1131ea5e7cf1350afb)。

GATT 精确时间 256 特征（GATT Characteristic Exact Time 256）。

<a id="r_gad826c92cd28e6eef5651474b611ab093"></a>

```c
#define BT_UUID_GATT_DST_VAL 0x2a0d
```

相关声明：[BT_UUID_GATT_DST_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad826c92cd28e6eef5651474b611ab093)。

GATT 夏令时偏移特征（GATT Characteristic DST Offset）的 UUID 值。

<a id="r_ga4b08c7472ecfe66eb2290fd83772ea24"></a>

```c
#define BT_UUID_GATT_DST BT_UUID_DECLARE_16(BT_UUID_GATT_DST_VAL)
```

相关声明：[BT_UUID_GATT_DST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4b08c7472ecfe66eb2290fd83772ea24)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_DST_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad826c92cd28e6eef5651474b611ab093)。

GATT 夏令时偏移特征（GATT Characteristic DST Offset）。

<a id="r_ga4e7082162bcdc58b385989e955ebb7f9"></a>

```c
#define BT_UUID_GATT_TZ_VAL 0x2a0e
```

相关声明：[BT_UUID_GATT_TZ_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4e7082162bcdc58b385989e955ebb7f9)。

GATT 时区特征（GATT Characteristic Time Zone）的 UUID 值。

<a id="r_ga83e5e48b8bd8955dc559b95ec6e73a78"></a>

```c
#define BT_UUID_GATT_TZ BT_UUID_DECLARE_16(BT_UUID_GATT_TZ_VAL)
```

相关声明：[BT_UUID_GATT_TZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga83e5e48b8bd8955dc559b95ec6e73a78)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TZ_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4e7082162bcdc58b385989e955ebb7f9)。

GATT 时区特征（GATT Characteristic Time Zone）。

<a id="r_ga25c6a750b9548144da0e78cca3ad6a59"></a>

```c
#define BT_UUID_GATT_LTI_VAL 0x2a0f
```

相关声明：[BT_UUID_GATT_LTI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga25c6a750b9548144da0e78cca3ad6a59)。

GATT 本地时间信息特征（GATT Characteristic Local Time Information）的 UUID 值。

<a id="r_ga6524bc40fbada1e558635af6b52283b9"></a>

```c
#define BT_UUID_GATT_LTI BT_UUID_DECLARE_16(BT_UUID_GATT_LTI_VAL)
```

相关声明：[BT_UUID_GATT_LTI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6524bc40fbada1e558635af6b52283b9)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LTI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga25c6a750b9548144da0e78cca3ad6a59)。

GATT 本地时间信息特征（GATT Characteristic Local Time Information）。

<a id="r_ga1bf3703c269e658c0e0e4ef822f14299"></a>

```c
#define BT_UUID_GATT_TDST_VAL 0x2a11
```

相关声明：[BT_UUID_GATT_TDST_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1bf3703c269e658c0e0e4ef822f14299)。

GATT 含夏令时信息的时间特征（GATT Characteristic Time with DST）的 UUID 值。

<a id="r_gace914257c496dbe17adc0d2b3db8f4c7"></a>

```c
#define BT_UUID_GATT_TDST BT_UUID_DECLARE_16(BT_UUID_GATT_TDST_VAL)
```

相关声明：[BT_UUID_GATT_TDST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gace914257c496dbe17adc0d2b3db8f4c7)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TDST_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1bf3703c269e658c0e0e4ef822f14299)。

GATT 含夏令时信息的时间特征（GATT Characteristic Time with DST）。

<a id="r_gad304e85ca1a4b8f0f53d6068a37ae8d2"></a>

```c
#define BT_UUID_GATT_TA_VAL 0x2a12
```

相关声明：[BT_UUID_GATT_TA_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad304e85ca1a4b8f0f53d6068a37ae8d2)。

GATT 时间准确度特征（GATT Characteristic Time Accuracy）的 UUID 值。

<a id="r_ga75036cc3ceecebccfbfc153a0cc9920f"></a>

```c
#define BT_UUID_GATT_TA BT_UUID_DECLARE_16(BT_UUID_GATT_TA_VAL)
```

相关声明：[BT_UUID_GATT_TA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga75036cc3ceecebccfbfc153a0cc9920f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TA_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad304e85ca1a4b8f0f53d6068a37ae8d2)。

GATT 时间准确度特征（GATT Characteristic Time Accuracy）。

<a id="r_ga188a456a10d2a44c19a6825bb288294f"></a>

```c
#define BT_UUID_GATT_TS_VAL 0x2a13
```

相关声明：[BT_UUID_GATT_TS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga188a456a10d2a44c19a6825bb288294f)。

GATT 时间源特征（GATT Characteristic Time Source）的 UUID 值。

<a id="r_gaaaed25b2d73258322825ca9d2460c1a1"></a>

```c
#define BT_UUID_GATT_TS BT_UUID_DECLARE_16(BT_UUID_GATT_TS_VAL)
```

相关声明：[BT_UUID_GATT_TS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaaaed25b2d73258322825ca9d2460c1a1)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga188a456a10d2a44c19a6825bb288294f)。

GATT 时间源特征（GATT Characteristic Time Source）。

<a id="r_ga668e9e73668b1c00a3bac74080ad7bcc"></a>

```c
#define BT_UUID_GATT_RTI_VAL 0x2a14
```

相关声明：[BT_UUID_GATT_RTI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga668e9e73668b1c00a3bac74080ad7bcc)。

GATT 参考时间信息特征（GATT Characteristic Reference Time Information）的 UUID 值。

<a id="r_ga5b241e9ab9be83919aa99c24da34fa4b"></a>

```c
#define BT_UUID_GATT_RTI BT_UUID_DECLARE_16(BT_UUID_GATT_RTI_VAL)
```

相关声明：[BT_UUID_GATT_RTI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5b241e9ab9be83919aa99c24da34fa4b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_RTI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga668e9e73668b1c00a3bac74080ad7bcc)。

GATT 参考时间信息特征（GATT Characteristic Reference Time Information）。

<a id="r_ga89f6031ef8778c4eb281dcda1afe5688"></a>

```c
#define BT_UUID_GATT_TUCP_VAL 0x2a16
```

相关声明：[BT_UUID_GATT_TUCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga89f6031ef8778c4eb281dcda1afe5688)。

GATT 时间更新控制点特征（GATT Characteristic Time Update Control Point）的 UUID 值。

<a id="r_gaead8cf75f2bdecf9188272da2b3c5d41"></a>

```c
#define BT_UUID_GATT_TUCP BT_UUID_DECLARE_16(BT_UUID_GATT_TUCP_VAL)
```

相关声明：[BT_UUID_GATT_TUCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaead8cf75f2bdecf9188272da2b3c5d41)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TUCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga89f6031ef8778c4eb281dcda1afe5688)。

GATT 时间更新控制点特征（GATT Characteristic Time Update Control Point）。

<a id="r_ga0511dd52eadfa58395981b621b31c635"></a>

```c
#define BT_UUID_GATT_TUS_VAL 0x2a17
```

相关声明：[BT_UUID_GATT_TUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0511dd52eadfa58395981b621b31c635)。

GATT 时间更新状态特征（GATT Characteristic Time Update State）的 UUID 值。

<a id="r_gaeef7563b0eb39783afc3c86147262aee"></a>

```c
#define BT_UUID_GATT_TUS BT_UUID_DECLARE_16(BT_UUID_GATT_TUS_VAL)
```

相关声明：[BT_UUID_GATT_TUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaeef7563b0eb39783afc3c86147262aee)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0511dd52eadfa58395981b621b31c635)。

GATT 时间更新状态特征（GATT Characteristic Time Update State）。

<a id="r_gaa11e9838368e470262efc07f86d12fc7"></a>

```c
#define BT_UUID_GATT_GM_VAL 0x2a18
```

相关声明：[BT_UUID_GATT_GM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa11e9838368e470262efc07f86d12fc7)。

GATT 葡萄糖测量特征（GATT Characteristic Glucose Measurement）的 UUID 值。

<a id="r_ga804ab92719239778e8328157876fce61"></a>

```c
#define BT_UUID_GATT_GM BT_UUID_DECLARE_16(BT_UUID_GATT_GM_VAL)
```

相关声明：[BT_UUID_GATT_GM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga804ab92719239778e8328157876fce61)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_GM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa11e9838368e470262efc07f86d12fc7)。

GATT 葡萄糖测量特征（GATT Characteristic Glucose Measurement）。

<a id="r_ga1961ff80d56b5c06185601cfce941cf1"></a>

```c
#define BT_UUID_BAS_BATTERY_LEVEL_VAL 0x2a19
```

相关声明：[BT_UUID_BAS_BATTERY_LEVEL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1961ff80d56b5c06185601cfce941cf1)。

BAS 电池电量特征（BAS Characteristic Battery Level）的 UUID 值。

<a id="r_gae4f41b4e329c728767a8a99a3a89af7e"></a>

```c
#define BT_UUID_BAS_BATTERY_LEVEL BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_LEVEL_VAL)
```

相关声明：[BT_UUID_BAS_BATTERY_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae4f41b4e329c728767a8a99a3a89af7e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BAS_BATTERY_LEVEL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1961ff80d56b5c06185601cfce941cf1)。

BAS 电池电量特征（BAS Characteristic Battery Level）。

<a id="r_ga818b6cbee38384f23e1548d49c89e53e"></a>

```c
#define BT_UUID_BAS_BATTERY_POWER_STATE_VAL 0x2a1a
```

相关声明：[BT_UUID_BAS_BATTERY_POWER_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga818b6cbee38384f23e1548d49c89e53e)。

BAS 电池电源状态特征（BAS Characteristic Battery Power State）的 UUID 值。

<a id="r_ga17d4a2ee5c7587ef35013f47dacfb95d"></a>

```c
#define BT_UUID_BAS_BATTERY_POWER_STATE BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_POWER_STATE_VAL)
```

相关声明：[BT_UUID_BAS_BATTERY_POWER_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga17d4a2ee5c7587ef35013f47dacfb95d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BAS_BATTERY_POWER_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga818b6cbee38384f23e1548d49c89e53e)。

BAS 电池电源状态特征（BAS Characteristic Battery Power State）。

<a id="r_ga7dcdb33b95cc58489343c9591fc0b453"></a>

```c
#define BT_UUID_BAS_BATTERY_LEVEL_STATE_VAL 0x2a1b
```

相关声明：[BT_UUID_BAS_BATTERY_LEVEL_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7dcdb33b95cc58489343c9591fc0b453)。

BAS 电池电量状态特征（BAS Characteristic Battery Level State）的 UUID 值。

<a id="r_ga3022242a2bd7ccec5580d007182864dc"></a>

```c
#define BT_UUID_BAS_BATTERY_LEVEL_STATE BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_LEVEL_STATE_VAL)
```

相关声明：[BT_UUID_BAS_BATTERY_LEVEL_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3022242a2bd7ccec5580d007182864dc)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BAS_BATTERY_LEVEL_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7dcdb33b95cc58489343c9591fc0b453)。

BAS 电池电量状态特征（BAS Characteristic Battery Level State）。

<a id="r_ga612376c2ac9b3b21e1fe07aa2c931fad"></a>

```c
#define BT_UUID_HTS_MEASUREMENT_VAL 0x2a1c
```

相关声明：[BT_UUID_HTS_MEASUREMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga612376c2ac9b3b21e1fe07aa2c931fad)。

HTS 温度测量特征（HTS Characteristic Temperature Measurement）的 UUID 值。

<a id="r_gade726271d11b08b573aec3a1a6794c55"></a>

```c
#define BT_UUID_HTS_MEASUREMENT BT_UUID_DECLARE_16(BT_UUID_HTS_MEASUREMENT_VAL)
```

相关声明：[BT_UUID_HTS_MEASUREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gade726271d11b08b573aec3a1a6794c55)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HTS_MEASUREMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga612376c2ac9b3b21e1fe07aa2c931fad)。

HTS 温度测量特征值（HTS Characteristic Temperature Measurement Value）。

<a id="r_ga1e2c9c8bf1c27e0dd3fd37910a349d75"></a>

```c
#define BT_UUID_HTS_TEMP_TYP_VAL 0x2a1d
```

相关声明：[BT_UUID_HTS_TEMP_TYP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1e2c9c8bf1c27e0dd3fd37910a349d75)。

HTS 温度类型特征（HTS Characteristic Temperature Type）的 UUID 值。

<a id="r_ga7055bba7158854729f65f76841a32de6"></a>

```c
#define BT_UUID_HTS_TEMP_TYP BT_UUID_DECLARE_16(BT_UUID_HTS_TEMP_TYP_VAL)
```

相关声明：[BT_UUID_HTS_TEMP_TYP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7055bba7158854729f65f76841a32de6)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HTS_TEMP_TYP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1e2c9c8bf1c27e0dd3fd37910a349d75)。

HTS 温度类型特征（HTS Characteristic Temperature Type）。

<a id="r_ga4b13a008e37df4a0eb2b4b94bdb15126"></a>

```c
#define BT_UUID_HTS_TEMP_INT_VAL 0x2a1e
```

相关声明：[BT_UUID_HTS_TEMP_INT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4b13a008e37df4a0eb2b4b94bdb15126)。

HTS 中间温度特征（HTS Characteristic Intermediate Temperature）的 UUID 值。

<a id="r_ga98f9fe29431766e819b3ea014294431b"></a>

```c
#define BT_UUID_HTS_TEMP_INT BT_UUID_DECLARE_16(BT_UUID_HTS_TEMP_INT_VAL)
```

相关声明：[BT_UUID_HTS_TEMP_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga98f9fe29431766e819b3ea014294431b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HTS_TEMP_INT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4b13a008e37df4a0eb2b4b94bdb15126)。

HTS 中间温度特征（HTS Characteristic Intermediate Temperature）。

<a id="r_ga67a6e1c0f24628e0cd11a4311de5a6fa"></a>

```c
#define BT_UUID_HTS_TEMP_C_VAL 0x2a1f
```

相关声明：[BT_UUID_HTS_TEMP_C_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga67a6e1c0f24628e0cd11a4311de5a6fa)。

HTS 摄氏温度特征（HTS Characteristic Temperature Celsius）的 UUID 值。

<a id="r_ga51ef3d61ceffb85824b920fa7b04bd62"></a>

```c
#define BT_UUID_HTS_TEMP_C BT_UUID_DECLARE_16(BT_UUID_HTS_TEMP_C_VAL)
```

相关声明：[BT_UUID_HTS_TEMP_C](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga51ef3d61ceffb85824b920fa7b04bd62)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HTS_TEMP_C_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga67a6e1c0f24628e0cd11a4311de5a6fa)。

HTS 摄氏温度特征（HTS Characteristic Temperature Celsius）。

<a id="r_ga002d02e831aa0c3ca24b61b2527ac65b"></a>

```c
#define BT_UUID_HTS_TEMP_F_VAL 0x2a20
```

相关声明：[BT_UUID_HTS_TEMP_F_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga002d02e831aa0c3ca24b61b2527ac65b)。

HTS 华氏温度特征（HTS Characteristic Temperature Fahrenheit）的 UUID 值。

<a id="r_ga6835b7816c5dc5bb4453e0b82925bb99"></a>

```c
#define BT_UUID_HTS_TEMP_F BT_UUID_DECLARE_16(BT_UUID_HTS_TEMP_F_VAL)
```

相关声明：[BT_UUID_HTS_TEMP_F](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6835b7816c5dc5bb4453e0b82925bb99)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HTS_TEMP_F_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga002d02e831aa0c3ca24b61b2527ac65b)。

HTS 华氏温度特征（HTS Characteristic Temperature Fahrenheit）。

<a id="r_gac90751f69745ed65ff1739c1b86f3942"></a>

```c
#define BT_UUID_HTS_INTERVAL_VAL 0x2a21
```

相关声明：[BT_UUID_HTS_INTERVAL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac90751f69745ed65ff1739c1b86f3942)。

HTS 测量间隔特征（HTS Characteristic Measurement Interval）的 UUID 值。

<a id="r_ga993de0f6c8904f1d1f8527d8a4f31946"></a>

```c
#define BT_UUID_HTS_INTERVAL BT_UUID_DECLARE_16(BT_UUID_HTS_INTERVAL_VAL)
```

相关声明：[BT_UUID_HTS_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga993de0f6c8904f1d1f8527d8a4f31946)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HTS_INTERVAL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac90751f69745ed65ff1739c1b86f3942)。

HTS 测量间隔特征（HTS Characteristic Measurement Interval）。

<a id="r_gaa842693e29c174601e84feb43098b543"></a>

```c
#define BT_UUID_HIDS_BOOT_KB_IN_REPORT_VAL 0x2a22
```

相关声明：[BT_UUID_HIDS_BOOT_KB_IN_REPORT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa842693e29c174601e84feb43098b543)。

HID 引导键盘输入报告特征（HID Characteristic Boot Keyboard Input Report）的 UUID 值。

<a id="r_ga0ef3ddb08d602fcb513d348b1e1f2eb8"></a>

```c
#define BT_UUID_HIDS_BOOT_KB_IN_REPORT BT_UUID_DECLARE_16(BT_UUID_HIDS_BOOT_KB_IN_REPORT_VAL)
```

相关声明：[BT_UUID_HIDS_BOOT_KB_IN_REPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0ef3ddb08d602fcb513d348b1e1f2eb8)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HIDS_BOOT_KB_IN_REPORT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa842693e29c174601e84feb43098b543)。

HID 引导键盘输入报告特征（HID Characteristic Boot Keyboard Input Report）。

<a id="r_ga4fdfa6e582c6367aea30e9846653ebd3"></a>

```c
#define BT_UUID_DIS_SYSTEM_ID_VAL 0x2a23
```

相关声明：[BT_UUID_DIS_SYSTEM_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4fdfa6e582c6367aea30e9846653ebd3)。

DIS 系统标识符特征（DIS Characteristic System ID）的 UUID 值。

<a id="r_gaac15c93c66cb583c3819036a2bd5ba24"></a>

```c
#define BT_UUID_DIS_SYSTEM_ID BT_UUID_DECLARE_16(BT_UUID_DIS_SYSTEM_ID_VAL)
```

相关声明：[BT_UUID_DIS_SYSTEM_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaac15c93c66cb583c3819036a2bd5ba24)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_DIS_SYSTEM_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4fdfa6e582c6367aea30e9846653ebd3)。

DIS 系统标识符特征（DIS Characteristic System ID）。

<a id="r_ga32a4462aa866ff15bf33046efde8e796"></a>

```c
#define BT_UUID_DIS_MODEL_NUMBER_VAL 0x2a24
```

相关声明：[BT_UUID_DIS_MODEL_NUMBER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga32a4462aa866ff15bf33046efde8e796)。

DIS 型号字符串特征（DIS Characteristic Model Number String）的 UUID 值。

<a id="r_ga250d08b7b3de123c866143599975aa41"></a>

```c
#define BT_UUID_DIS_MODEL_NUMBER BT_UUID_DECLARE_16(BT_UUID_DIS_MODEL_NUMBER_VAL)
```

相关声明：[BT_UUID_DIS_MODEL_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga250d08b7b3de123c866143599975aa41)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_DIS_MODEL_NUMBER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga32a4462aa866ff15bf33046efde8e796)。

DIS 型号字符串特征（DIS Characteristic Model Number String）。

<a id="r_ga40c84dd8ce10d983596a4f6b9cfea82f"></a>

```c
#define BT_UUID_DIS_SERIAL_NUMBER_VAL 0x2a25
```

相关声明：[BT_UUID_DIS_SERIAL_NUMBER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga40c84dd8ce10d983596a4f6b9cfea82f)。

DIS 序列号字符串特征（DIS Characteristic Serial Number String）的 UUID 值。

<a id="r_ga072770347ecf34cb89d293c31f59642d"></a>

```c
#define BT_UUID_DIS_SERIAL_NUMBER BT_UUID_DECLARE_16(BT_UUID_DIS_SERIAL_NUMBER_VAL)
```

相关声明：[BT_UUID_DIS_SERIAL_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga072770347ecf34cb89d293c31f59642d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_DIS_SERIAL_NUMBER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga40c84dd8ce10d983596a4f6b9cfea82f)。

DIS 序列号字符串特征（DIS Characteristic Serial Number String）。

<a id="r_ga220481d4fb2b498fad4e82637a0d02da"></a>

```c
#define BT_UUID_DIS_FIRMWARE_REVISION_VAL 0x2a26
```

相关声明：[BT_UUID_DIS_FIRMWARE_REVISION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga220481d4fb2b498fad4e82637a0d02da)。

DIS 固件版本字符串特征（DIS Characteristic Firmware Revision String）的 UUID 值。

<a id="r_ga988bb4018b232cb4da64d522703ec5b3"></a>

```c
#define BT_UUID_DIS_FIRMWARE_REVISION BT_UUID_DECLARE_16(BT_UUID_DIS_FIRMWARE_REVISION_VAL)
```

相关声明：[BT_UUID_DIS_FIRMWARE_REVISION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga988bb4018b232cb4da64d522703ec5b3)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_DIS_FIRMWARE_REVISION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga220481d4fb2b498fad4e82637a0d02da)。

DIS 固件版本字符串特征（DIS Characteristic Firmware Revision String）。

<a id="r_ga3db6b3e905dd874c28a7b59c7a2a1b21"></a>

```c
#define BT_UUID_DIS_HARDWARE_REVISION_VAL 0x2a27
```

相关声明：[BT_UUID_DIS_HARDWARE_REVISION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3db6b3e905dd874c28a7b59c7a2a1b21)。

DIS 硬件版本字符串特征（DIS Characteristic Hardware Revision String）的 UUID 值。

<a id="r_ga3842092a747954d24ceef3a0951efac7"></a>

```c
#define BT_UUID_DIS_HARDWARE_REVISION BT_UUID_DECLARE_16(BT_UUID_DIS_HARDWARE_REVISION_VAL)
```

相关声明：[BT_UUID_DIS_HARDWARE_REVISION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3842092a747954d24ceef3a0951efac7)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_DIS_HARDWARE_REVISION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3db6b3e905dd874c28a7b59c7a2a1b21)。

DIS 硬件版本字符串特征（DIS Characteristic Hardware Revision String）。

<a id="r_gabef02eec1e667b2b35521a46b355d2e8"></a>

```c
#define BT_UUID_DIS_SOFTWARE_REVISION_VAL 0x2a28
```

相关声明：[BT_UUID_DIS_SOFTWARE_REVISION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabef02eec1e667b2b35521a46b355d2e8)。

DIS 软件版本字符串特征（DIS Characteristic Software Revision String）的 UUID 值。

<a id="r_ga8e9cc11f505e578851155659dc1ab262"></a>

```c
#define BT_UUID_DIS_SOFTWARE_REVISION BT_UUID_DECLARE_16(BT_UUID_DIS_SOFTWARE_REVISION_VAL)
```

相关声明：[BT_UUID_DIS_SOFTWARE_REVISION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8e9cc11f505e578851155659dc1ab262)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_DIS_SOFTWARE_REVISION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabef02eec1e667b2b35521a46b355d2e8)。

DIS 软件版本字符串特征（DIS Characteristic Software Revision String）。

<a id="r_gac726ebb1cbc1d7ed63df41c232ee4a42"></a>

```c
#define BT_UUID_DIS_MANUFACTURER_NAME_VAL 0x2a29
```

相关声明：[BT_UUID_DIS_MANUFACTURER_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac726ebb1cbc1d7ed63df41c232ee4a42)。

DIS 制造商名称字符串特征（DIS Characteristic Manufacturer Name String）的 UUID 值。

<a id="r_gaefd466120c6923d806cfc4b5beb9899d"></a>

```c
#define BT_UUID_DIS_MANUFACTURER_NAME BT_UUID_DECLARE_16(BT_UUID_DIS_MANUFACTURER_NAME_VAL)
```

相关声明：[BT_UUID_DIS_MANUFACTURER_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaefd466120c6923d806cfc4b5beb9899d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_DIS_MANUFACTURER_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac726ebb1cbc1d7ed63df41c232ee4a42)。

DIS 制造商名称字符串特征（DIS Characteristic Manufacturer Name String）。

<a id="r_gabf8a181cbe973c985c71aa6eb7d92fe1"></a>

```c
#define BT_UUID_GATT_IEEE_RCDL_VAL 0x2a2a
```

相关声明：[BT_UUID_GATT_IEEE_RCDL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabf8a181cbe973c985c71aa6eb7d92fe1)。

GATT IEEE 法规认证数据列表特征（GATT Characteristic IEEE Regulatory Certification Data List）的 UUID 值。

<a id="r_ga3d95539bee32ca38ea825aadf85840fb"></a>

```c
#define BT_UUID_GATT_IEEE_RCDL BT_UUID_DECLARE_16(BT_UUID_GATT_IEEE_RCDL_VAL)
```

相关声明：[BT_UUID_GATT_IEEE_RCDL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3d95539bee32ca38ea825aadf85840fb)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_IEEE_RCDL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabf8a181cbe973c985c71aa6eb7d92fe1)。

GATT IEEE 法规认证数据列表特征（GATT Characteristic IEEE Regulatory Certification Data List）。

<a id="r_gae8de32ab38c9e160dc1883c345063855"></a>

```c
#define BT_UUID_CTS_CURRENT_TIME_VAL 0x2a2b
```

相关声明：[BT_UUID_CTS_CURRENT_TIME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae8de32ab38c9e160dc1883c345063855)。

CTS 当前时间特征（CTS Characteristic Current Time）的 UUID 值。

<a id="r_gae0a920c076eb504b448f390c320ccfb8"></a>

```c
#define BT_UUID_CTS_CURRENT_TIME BT_UUID_DECLARE_16(BT_UUID_CTS_CURRENT_TIME_VAL)
```

相关声明：[BT_UUID_CTS_CURRENT_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae0a920c076eb504b448f390c320ccfb8)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CTS_CURRENT_TIME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae8de32ab38c9e160dc1883c345063855)。

CTS 当前时间特征（CTS Characteristic Current Time）。

<a id="r_ga6768ade4d8adf925fb52a27cee616e6e"></a>

```c
#define BT_UUID_MAGN_DECLINATION_VAL 0x2a2c
```

相关声明：[BT_UUID_MAGN_DECLINATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6768ade4d8adf925fb52a27cee616e6e)。

磁偏角特征（Magnetic Declination Characteristic）的 UUID 值。

<a id="r_ga7322a8412c7aaf9e6f06473d3fa5186d"></a>

```c
#define BT_UUID_MAGN_DECLINATION BT_UUID_DECLARE_16(BT_UUID_MAGN_DECLINATION_VAL)
```

相关声明：[BT_UUID_MAGN_DECLINATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7322a8412c7aaf9e6f06473d3fa5186d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MAGN_DECLINATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6768ade4d8adf925fb52a27cee616e6e)。

磁偏角特征（Magnetic Declination Characteristic）。

<a id="r_gabc9b96c541f0711bf5525269c4b3e5b0"></a>

```c
#define BT_UUID_GATT_LLAT_VAL 0x2a2d
```

相关声明：[BT_UUID_GATT_LLAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabc9b96c541f0711bf5525269c4b3e5b0)。

GATT 遗留纬度特征（GATT Characteristic Legacy Latitude）的 UUID 值。

<a id="r_gaa9187bacfb95b379734ccf89f7eef163"></a>

```c
#define BT_UUID_GATT_LLAT BT_UUID_DECLARE_16(BT_UUID_GATT_LLAT_VAL)
```

相关声明：[BT_UUID_GATT_LLAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa9187bacfb95b379734ccf89f7eef163)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LLAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabc9b96c541f0711bf5525269c4b3e5b0)。

GATT 遗留纬度特征（GATT Characteristic Legacy Latitude）。

<a id="r_ga5d369d45c15dad30ccf7c3066863401f"></a>

```c
#define BT_UUID_GATT_LLON_VAL 0x2a2e
```

相关声明：[BT_UUID_GATT_LLON_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5d369d45c15dad30ccf7c3066863401f)。

GATT 遗留经度特征（GATT Characteristic Legacy Longitude）的 UUID 值。

<a id="r_gae090952d14ae3db50edabbdfc4d8ae25"></a>

```c
#define BT_UUID_GATT_LLON BT_UUID_DECLARE_16(BT_UUID_GATT_LLON_VAL)
```

相关声明：[BT_UUID_GATT_LLON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae090952d14ae3db50edabbdfc4d8ae25)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LLON_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5d369d45c15dad30ccf7c3066863401f)。

GATT 遗留经度特征（GATT Characteristic Legacy Longitude）。

<a id="r_gaca1fdcec43844e0e6afeda46d7d60baf"></a>

```c
#define BT_UUID_GATT_POS_2D_VAL 0x2a2f
```

相关声明：[BT_UUID_GATT_POS_2D_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaca1fdcec43844e0e6afeda46d7d60baf)。

GATT 二维位置特征（GATT Characteristic Position 2D）的 UUID 值。

<a id="r_ga21220783e6c7079bc9bd2f712b882dc6"></a>

```c
#define BT_UUID_GATT_POS_2D BT_UUID_DECLARE_16(BT_UUID_GATT_POS_2D_VAL)
```

相关声明：[BT_UUID_GATT_POS_2D](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga21220783e6c7079bc9bd2f712b882dc6)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_POS_2D_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaca1fdcec43844e0e6afeda46d7d60baf)。

GATT 二维位置特征（GATT Characteristic Position 2D）。

<a id="r_ga66b1060fd8eaf94955211b87c9d940c2"></a>

```c
#define BT_UUID_GATT_POS_3D_VAL 0x2a30
```

相关声明：[BT_UUID_GATT_POS_3D_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66b1060fd8eaf94955211b87c9d940c2)。

GATT 三维位置特征（GATT Characteristic Position 3D）的 UUID 值。

<a id="r_ga56e0a35ad8138b961f68155fa2091ae1"></a>

```c
#define BT_UUID_GATT_POS_3D BT_UUID_DECLARE_16(BT_UUID_GATT_POS_3D_VAL)
```

相关声明：[BT_UUID_GATT_POS_3D](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga56e0a35ad8138b961f68155fa2091ae1)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_POS_3D_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66b1060fd8eaf94955211b87c9d940c2)。

GATT 三维位置特征（GATT Characteristic Position 3D）。

<a id="r_ga862122929d6e4717d21c84efc5869da2"></a>

```c
#define BT_UUID_GATT_SR_VAL 0x2a31
```

相关声明：[BT_UUID_GATT_SR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga862122929d6e4717d21c84efc5869da2)。

GATT 扫描刷新特征（GATT Characteristic Scan Refresh）的 UUID 值。

<a id="r_ga720d3e1f20d70cffe312f983224c2335"></a>

```c
#define BT_UUID_GATT_SR BT_UUID_DECLARE_16(BT_UUID_GATT_SR_VAL)
```

相关声明：[BT_UUID_GATT_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga720d3e1f20d70cffe312f983224c2335)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga862122929d6e4717d21c84efc5869da2)。

GATT 扫描刷新特征（GATT Characteristic Scan Refresh）。

<a id="r_ga79c18c840c919a2824d7bb84fa2217b5"></a>

```c
#define BT_UUID_HIDS_BOOT_KB_OUT_REPORT_VAL 0x2a32
```

相关声明：[BT_UUID_HIDS_BOOT_KB_OUT_REPORT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga79c18c840c919a2824d7bb84fa2217b5)。

HID 引导键盘输出报告特征（HID Boot Keyboard Output Report Characteristic）的 UUID 值。

<a id="r_ga67e34824d0d393dcbb401c91690bce00"></a>

```c
#define BT_UUID_HIDS_BOOT_KB_OUT_REPORT BT_UUID_DECLARE_16(BT_UUID_HIDS_BOOT_KB_OUT_REPORT_VAL)
```

相关声明：[BT_UUID_HIDS_BOOT_KB_OUT_REPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga67e34824d0d393dcbb401c91690bce00)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HIDS_BOOT_KB_OUT_REPORT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga79c18c840c919a2824d7bb84fa2217b5)。

HID 引导键盘输出报告特征（HID Boot Keyboard Output Report Characteristic）。

<a id="r_ga804ec93e78855249a4a0a692314f4bf9"></a>

```c
#define BT_UUID_HIDS_BOOT_MOUSE_IN_REPORT_VAL 0x2a33
```

相关声明：[BT_UUID_HIDS_BOOT_MOUSE_IN_REPORT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga804ec93e78855249a4a0a692314f4bf9)。

HID 引导鼠标输入报告特征（HID Boot Mouse Input Report Characteristic）的 UUID 值。

<a id="r_gae86aedfdbe15939df6384870e883bfa5"></a>

```c
#define BT_UUID_HIDS_BOOT_MOUSE_IN_REPORT BT_UUID_DECLARE_16(BT_UUID_HIDS_BOOT_MOUSE_IN_REPORT_VAL)
```

相关声明：[BT_UUID_HIDS_BOOT_MOUSE_IN_REPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae86aedfdbe15939df6384870e883bfa5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HIDS_BOOT_MOUSE_IN_REPORT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga804ec93e78855249a4a0a692314f4bf9)。

HID 引导鼠标输入报告特征（HID Boot Mouse Input Report Characteristic）。

<a id="r_ga95629cec83007634ec69516be8086d5a"></a>

```c
#define BT_UUID_GATT_GMC_VAL 0x2a34
```

相关声明：[BT_UUID_GATT_GMC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga95629cec83007634ec69516be8086d5a)。

GATT 葡萄糖测量上下文特征（GATT Characteristic Glucose Measurement Context）的 UUID 值。

<a id="r_ga1ca1906ee4fc482d5bb83664362c19ae"></a>

```c
#define BT_UUID_GATT_GMC BT_UUID_DECLARE_16(BT_UUID_GATT_GMC_VAL)
```

相关声明：[BT_UUID_GATT_GMC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1ca1906ee4fc482d5bb83664362c19ae)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_GMC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga95629cec83007634ec69516be8086d5a)。

GATT 葡萄糖测量上下文特征（GATT Characteristic Glucose Measurement Context）。

<a id="r_ga2342a077a10cbf649bb46f64e5fa24cb"></a>

```c
#define BT_UUID_GATT_BPM_VAL 0x2a35
```

相关声明：[BT_UUID_GATT_BPM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2342a077a10cbf649bb46f64e5fa24cb)。

GATT 血压测量特征（GATT Characteristic Blood Pressure Measurement）的 UUID 值。

<a id="r_ga53f7809544d80bc8b797dfb0d0761ae2"></a>

```c
#define BT_UUID_GATT_BPM BT_UUID_DECLARE_16(BT_UUID_GATT_BPM_VAL)
```

相关声明：[BT_UUID_GATT_BPM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga53f7809544d80bc8b797dfb0d0761ae2)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_BPM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2342a077a10cbf649bb46f64e5fa24cb)。

GATT 血压测量特征（GATT Characteristic Blood Pressure Measurement）。

<a id="r_gaf68e5c86b67a8065ca3a1dc8ed0bd9ea"></a>

```c
#define BT_UUID_GATT_ICP_VAL 0x2a36
```

相关声明：[BT_UUID_GATT_ICP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf68e5c86b67a8065ca3a1dc8ed0bd9ea)。

GATT 中间袖带压力特征（GATT Characteristic Intermediate Cuff Pressure）的 UUID 值。

<a id="r_ga33ffcb4cc70f133a29bbbe6c19d6e964"></a>

```c
#define BT_UUID_GATT_ICP BT_UUID_DECLARE_16(BT_UUID_GATT_ICP_VAL)
```

相关声明：[BT_UUID_GATT_ICP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga33ffcb4cc70f133a29bbbe6c19d6e964)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ICP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf68e5c86b67a8065ca3a1dc8ed0bd9ea)。

GATT 中间袖带压力特征（GATT Characteristic Intermediate Cuff Pressure）。

<a id="r_ga44d502836331e3ffda5718d719e77ff6"></a>

```c
#define BT_UUID_HRS_MEASUREMENT_VAL 0x2a37
```

相关声明：[BT_UUID_HRS_MEASUREMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga44d502836331e3ffda5718d719e77ff6)。

HRS 测量间隔特征（HRS Characteristic Measurement Interval）的 UUID 值。

<a id="r_ga270ace7cd256a5441986d33becbbed05"></a>

```c
#define BT_UUID_HRS_MEASUREMENT BT_UUID_DECLARE_16(BT_UUID_HRS_MEASUREMENT_VAL)
```

相关声明：[BT_UUID_HRS_MEASUREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga270ace7cd256a5441986d33becbbed05)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HRS_MEASUREMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga44d502836331e3ffda5718d719e77ff6)。

HRS 测量间隔特征（HRS Characteristic Measurement Interval）。

<a id="r_gafed38fc5d9727fb2b1d009975142ec44"></a>

```c
#define BT_UUID_HRS_BODY_SENSOR_VAL 0x2a38
```

相关声明：[BT_UUID_HRS_BODY_SENSOR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafed38fc5d9727fb2b1d009975142ec44)。

HRS 身体传感器位置特征（HRS Characteristic Body Sensor Location）。

<a id="r_ga6021612c89adac51569a14565f1f6dd2"></a>

```c
#define BT_UUID_HRS_BODY_SENSOR BT_UUID_DECLARE_16(BT_UUID_HRS_BODY_SENSOR_VAL)
```

相关声明：[BT_UUID_HRS_BODY_SENSOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6021612c89adac51569a14565f1f6dd2)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HRS_BODY_SENSOR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafed38fc5d9727fb2b1d009975142ec44)。

HRS 身体传感器位置特征（HRS Characteristic Body Sensor Location）。

<a id="r_ga83825772db7f9d5c4376a78d44d10a60"></a>

```c
#define BT_UUID_HRS_CONTROL_POINT_VAL 0x2a39
```

相关声明：[BT_UUID_HRS_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga83825772db7f9d5c4376a78d44d10a60)。

HRS 控制点特征（HRS Characteristic Control Point）的 UUID 值。

<a id="r_gacec1c535fc0d96bbad3083240b5a87a1"></a>

```c
#define BT_UUID_HRS_CONTROL_POINT BT_UUID_DECLARE_16(BT_UUID_HRS_CONTROL_POINT_VAL)
```

相关声明：[BT_UUID_HRS_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacec1c535fc0d96bbad3083240b5a87a1)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HRS_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga83825772db7f9d5c4376a78d44d10a60)。

HRS 控制点特征（HRS Characteristic Control Point）。

<a id="r_gadb260392b00da4d849c03718aaf7d323"></a>

```c
#define BT_UUID_GATT_REM_VAL 0x2a3a
```

相关声明：[BT_UUID_GATT_REM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadb260392b00da4d849c03718aaf7d323)。

GATT 可移除特征（GATT Characteristic Removable）的 UUID 值。

<a id="r_ga92564b1966ed0cacd36b13cdf44b9a04"></a>

```c
#define BT_UUID_GATT_REM BT_UUID_DECLARE_16(BT_UUID_GATT_REM_VAL)
```

相关声明：[BT_UUID_GATT_REM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga92564b1966ed0cacd36b13cdf44b9a04)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_REM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadb260392b00da4d849c03718aaf7d323)。

GATT 可移除特征（GATT Characteristic Removable）。

<a id="r_gade09ce0a6c46fc85ada2d38c3240b953"></a>

```c
#define BT_UUID_GATT_SRVREQ_VAL 0x2a3b
```

相关声明：[BT_UUID_GATT_SRVREQ_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gade09ce0a6c46fc85ada2d38c3240b953)。

GATT 需要服务特征（GATT Characteristic Service Required）的 UUID 值。

<a id="r_ga66b18ba52088ed23136ffe121d350fa2"></a>

```c
#define BT_UUID_GATT_SRVREQ BT_UUID_DECLARE_16(BT_UUID_GATT_SRVREQ_VAL)
```

相关声明：[BT_UUID_GATT_SRVREQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66b18ba52088ed23136ffe121d350fa2)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SRVREQ_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gade09ce0a6c46fc85ada2d38c3240b953)。

GATT 需要服务特征（GATT Characteristic Service Required）。

<a id="r_ga2253ec9a6d97865c7408ea4ab18a392e"></a>

```c
#define BT_UUID_GATT_SC_TEMP_C_VAL 0x2a3c
```

相关声明：[BT_UUID_GATT_SC_TEMP_C_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2253ec9a6d97865c7408ea4ab18a392e)。

GATT 科学用途摄氏温度特征（GATT Characteristic Scientific Temperature in Celsius）的 UUID 值。

<a id="r_ga2bb1b8f54f9cc4ef40650ad713181b49"></a>

```c
#define BT_UUID_GATT_SC_TEMP_C BT_UUID_DECLARE_16(BT_UUID_GATT_SC_TEMP_C_VAL)
```

相关声明：[BT_UUID_GATT_SC_TEMP_C](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2bb1b8f54f9cc4ef40650ad713181b49)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SC_TEMP_C_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2253ec9a6d97865c7408ea4ab18a392e)。

GATT 科学用途摄氏温度特征（GATT Characteristic Scientific Temperature in Celsius）。

<a id="r_ga3b3f44113ca4a89e10d3d84eb02dd847"></a>

```c
#define BT_UUID_GATT_STRING_VAL 0x2a3d
```

相关声明：[BT_UUID_GATT_STRING_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3b3f44113ca4a89e10d3d84eb02dd847)。

GATT 字符串特征（GATT Characteristic String）的 UUID 值。

<a id="r_ga4ca46824207979918b9a668cdf78e19a"></a>

```c
#define BT_UUID_GATT_STRING BT_UUID_DECLARE_16(BT_UUID_GATT_STRING_VAL)
```

相关声明：[BT_UUID_GATT_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4ca46824207979918b9a668cdf78e19a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_STRING_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3b3f44113ca4a89e10d3d84eb02dd847)。

GATT 字符串特征（GATT Characteristic String）。

<a id="r_gabd1aafbeaf157c4d515e5c2bae04823b"></a>

```c
#define BT_UUID_GATT_NETA_VAL 0x2a3e
```

相关声明：[BT_UUID_GATT_NETA_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabd1aafbeaf157c4d515e5c2bae04823b)。

GATT 网络可用性特征（GATT Characteristic Network Availability）的 UUID 值。

<a id="r_ga98caa54c91df23461cac4b5db6a86330"></a>

```c
#define BT_UUID_GATT_NETA BT_UUID_DECLARE_16(BT_UUID_GATT_NETA_VAL)
```

相关声明：[BT_UUID_GATT_NETA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga98caa54c91df23461cac4b5db6a86330)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_NETA_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabd1aafbeaf157c4d515e5c2bae04823b)。

GATT 网络可用性特征（GATT Characteristic Network Availability）。

<a id="r_ga11715889e92b0bf1942b3c4d84fa8aea"></a>

```c
#define BT_UUID_GATT_ALRTS_VAL 0x2a3f
```

相关声明：[BT_UUID_GATT_ALRTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga11715889e92b0bf1942b3c4d84fa8aea)。

GATT 告警状态特征（GATT Characteristic Alert Status）的 UUID 值。

<a id="r_ga0ef467a1b71b718216f08b21dca1e9b4"></a>

```c
#define BT_UUID_GATT_ALRTS BT_UUID_DECLARE_16(BT_UUID_GATT_ALRTS_VAL)
```

相关声明：[BT_UUID_GATT_ALRTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0ef467a1b71b718216f08b21dca1e9b4)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ALRTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga11715889e92b0bf1942b3c4d84fa8aea)。

GATT 告警状态特征（GATT Characteristic Alert Status）。

<a id="r_gaacbe74b5b9267f2398ea1bbde0300dc6"></a>

```c
#define BT_UUID_GATT_RCP_VAL 0x2a40
```

相关声明：[BT_UUID_GATT_RCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaacbe74b5b9267f2398ea1bbde0300dc6)。

GATT 铃声控制点特征（GATT Characteristic Ringer Control Point）的 UUID 值。

<a id="r_ga54702c100d46cb9dc358fd511dbc0b7d"></a>

```c
#define BT_UUID_GATT_RCP BT_UUID_DECLARE_16(BT_UUID_GATT_RCP_VAL)
```

相关声明：[BT_UUID_GATT_RCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga54702c100d46cb9dc358fd511dbc0b7d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_RCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaacbe74b5b9267f2398ea1bbde0300dc6)。

GATT 铃声控制点特征（GATT Characteristic Ringer Control Point）。

<a id="r_ga1479dc83c76a07d7000d3b53f8dee08d"></a>

```c
#define BT_UUID_GATT_RS_VAL 0x2a41
```

相关声明：[BT_UUID_GATT_RS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1479dc83c76a07d7000d3b53f8dee08d)。

GATT 铃声设置特征（GATT Characteristic Ringer Setting）的 UUID 值。

<a id="r_ga5c78797bbe75b3b66cbc0d6ff1b185fa"></a>

```c
#define BT_UUID_GATT_RS BT_UUID_DECLARE_16(BT_UUID_GATT_RS_VAL)
```

相关声明：[BT_UUID_GATT_RS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5c78797bbe75b3b66cbc0d6ff1b185fa)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_RS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1479dc83c76a07d7000d3b53f8dee08d)。

GATT 铃声设置特征（GATT Characteristic Ringer Setting）。

<a id="r_ga46356e3da57646e2a5bf2f6bc13e903f"></a>

```c
#define BT_UUID_GATT_ALRTCID_MASK_VAL 0x2a42
```

相关声明：[BT_UUID_GATT_ALRTCID_MASK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga46356e3da57646e2a5bf2f6bc13e903f)。

GATT 告警类别标识符位掩码特征（GATT Characteristic Alert Category ID Bit Mask）的 UUID 值。

<a id="r_ga7c905ac7003a24680ea6b2d3eeaee801"></a>

```c
#define BT_UUID_GATT_ALRTCID_MASK BT_UUID_DECLARE_16(BT_UUID_GATT_ALRTCID_MASK_VAL)
```

相关声明：[BT_UUID_GATT_ALRTCID_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7c905ac7003a24680ea6b2d3eeaee801)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ALRTCID_MASK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga46356e3da57646e2a5bf2f6bc13e903f)。

GATT 告警类别标识符位掩码特征（GATT Characteristic Alert Category ID Bit Mask）。

<a id="r_gab8423dbeb2c21e6c7bc90fcfe34c3a3a"></a>

```c
#define BT_UUID_GATT_ALRTCID_VAL 0x2a43
```

相关声明：[BT_UUID_GATT_ALRTCID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab8423dbeb2c21e6c7bc90fcfe34c3a3a)。

GATT 告警类别标识符特征（GATT Characteristic Alert Category ID）的 UUID 值。

<a id="r_ga207107524e82a8a34dc06263b434325f"></a>

```c
#define BT_UUID_GATT_ALRTCID BT_UUID_DECLARE_16(BT_UUID_GATT_ALRTCID_VAL)
```

相关声明：[BT_UUID_GATT_ALRTCID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga207107524e82a8a34dc06263b434325f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ALRTCID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab8423dbeb2c21e6c7bc90fcfe34c3a3a)。

GATT 告警类别标识符特征（GATT Characteristic Alert Category ID）。

<a id="r_ga0ef4d1008dcfafce23b10ff3e9f13407"></a>

```c
#define BT_UUID_GATT_ALRTNCP_VAL 0x2a44
```

相关声明：[BT_UUID_GATT_ALRTNCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0ef4d1008dcfafce23b10ff3e9f13407)。

GATT 告警通知控制点特征值（GATT Characteristic Alert Notification Control Point Value）。

<a id="r_ga0c0c2f7825242e43ad13c070d1a8c137"></a>

```c
#define BT_UUID_GATT_ALRTNCP BT_UUID_DECLARE_16(BT_UUID_GATT_ALRTNCP_VAL)
```

相关声明：[BT_UUID_GATT_ALRTNCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0c0c2f7825242e43ad13c070d1a8c137)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ALRTNCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0ef4d1008dcfafce23b10ff3e9f13407)。

GATT 告警通知控制点特征（GATT Characteristic Alert Notification Control Point）。

<a id="r_gacfacfd310975fb4fd6f25c33e658dfaa"></a>

```c
#define BT_UUID_GATT_UALRTS_VAL 0x2a45
```

相关声明：[BT_UUID_GATT_UALRTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacfacfd310975fb4fd6f25c33e658dfaa)。

GATT 未读告警状态特征（GATT Characteristic Unread Alert Status）的 UUID 值。

<a id="r_gacf608b24c1f0c1d10fdabd8594fe91d4"></a>

```c
#define BT_UUID_GATT_UALRTS BT_UUID_DECLARE_16(BT_UUID_GATT_UALRTS_VAL)
```

相关声明：[BT_UUID_GATT_UALRTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacf608b24c1f0c1d10fdabd8594fe91d4)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_UALRTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacfacfd310975fb4fd6f25c33e658dfaa)。

GATT 未读告警状态特征（GATT Characteristic Unread Alert Status）。

<a id="r_ga61f32ab52c24492cc2a1f0c9ee042987"></a>

```c
#define BT_UUID_GATT_NALRT_VAL 0x2a46
```

相关声明：[BT_UUID_GATT_NALRT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga61f32ab52c24492cc2a1f0c9ee042987)。

GATT 新告警特征（GATT Characteristic New Alert）的 UUID 值。

<a id="r_gac66637f6bdb5c4efb56739ac3a370032"></a>

```c
#define BT_UUID_GATT_NALRT BT_UUID_DECLARE_16(BT_UUID_GATT_NALRT_VAL)
```

相关声明：[BT_UUID_GATT_NALRT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac66637f6bdb5c4efb56739ac3a370032)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_NALRT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga61f32ab52c24492cc2a1f0c9ee042987)。

GATT 新告警特征（GATT Characteristic New Alert）。

<a id="r_ga2cc802e286be6c6d97835bc21eaa0433"></a>

```c
#define BT_UUID_GATT_SNALRTC_VAL 0x2a47
```

相关声明：[BT_UUID_GATT_SNALRTC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2cc802e286be6c6d97835bc21eaa0433)。

GATT 支持的新告警类别特征（GATT Characteristic Supported New Alert Category）的 UUID 值。

<a id="r_ga30a9d308743e751e56890d48f6ef606b"></a>

```c
#define BT_UUID_GATT_SNALRTC BT_UUID_DECLARE_16(BT_UUID_GATT_SNALRTC_VAL)
```

相关声明：[BT_UUID_GATT_SNALRTC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga30a9d308743e751e56890d48f6ef606b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SNALRTC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2cc802e286be6c6d97835bc21eaa0433)。

GATT 支持的新告警类别特征（GATT Characteristic Supported New Alert Category）。

<a id="r_ga64a81cfd5ce67cd6c1d27f0a7e7433bd"></a>

```c
#define BT_UUID_GATT_SUALRTC_VAL 0x2a48
```

相关声明：[BT_UUID_GATT_SUALRTC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga64a81cfd5ce67cd6c1d27f0a7e7433bd)。

GATT 支持的未读告警类别特征（GATT Characteristic Supported Unread Alert Category）的 UUID 值。

<a id="r_ga771c8d083004c4ef49e3334909f3d317"></a>

```c
#define BT_UUID_GATT_SUALRTC BT_UUID_DECLARE_16(BT_UUID_GATT_SUALRTC_VAL)
```

相关声明：[BT_UUID_GATT_SUALRTC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga771c8d083004c4ef49e3334909f3d317)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SUALRTC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga64a81cfd5ce67cd6c1d27f0a7e7433bd)。

GATT 支持的未读告警类别特征（GATT Characteristic Supported Unread Alert Category）。

<a id="r_gae5d786f2be340c5f126be0f500ade1f8"></a>

```c
#define BT_UUID_GATT_BPF_VAL 0x2a49
```

相关声明：[BT_UUID_GATT_BPF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae5d786f2be340c5f126be0f500ade1f8)。

GATT 血压功能特征（GATT Characteristic Blood Pressure Feature）的 UUID 值。

<a id="r_ga639e0f8fe154cca9773dd84e21ecc4d5"></a>

```c
#define BT_UUID_GATT_BPF BT_UUID_DECLARE_16(BT_UUID_GATT_BPF_VAL)
```

相关声明：[BT_UUID_GATT_BPF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga639e0f8fe154cca9773dd84e21ecc4d5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_BPF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae5d786f2be340c5f126be0f500ade1f8)。

GATT 血压功能特征（GATT Characteristic Blood Pressure Feature）。

<a id="r_ga929e50a821031cfb9c0faa3e2b0e9c4a"></a>

```c
#define BT_UUID_HIDS_INFO_VAL 0x2a4a
```

相关声明：[BT_UUID_HIDS_INFO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga929e50a821031cfb9c0faa3e2b0e9c4a)。

HID 信息特征（HID Information Characteristic）的 UUID 值。

<a id="r_ga28724b6efade76bfebeca2e8d7f9cdba"></a>

```c
#define BT_UUID_HIDS_INFO BT_UUID_DECLARE_16(BT_UUID_HIDS_INFO_VAL)
```

相关声明：[BT_UUID_HIDS_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga28724b6efade76bfebeca2e8d7f9cdba)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HIDS_INFO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga929e50a821031cfb9c0faa3e2b0e9c4a)。

HID 信息特征（HID Information Characteristic）。

<a id="r_ga8b3812488738cf6202586b9202403663"></a>

```c
#define BT_UUID_HIDS_REPORT_MAP_VAL 0x2a4b
```

相关声明：[BT_UUID_HIDS_REPORT_MAP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8b3812488738cf6202586b9202403663)。

HID 报告映射特征（HID Report Map Characteristic）的 UUID 值。

<a id="r_ga20a3521c85acd563064c5fc7ac022cda"></a>

```c
#define BT_UUID_HIDS_REPORT_MAP BT_UUID_DECLARE_16(BT_UUID_HIDS_REPORT_MAP_VAL)
```

相关声明：[BT_UUID_HIDS_REPORT_MAP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga20a3521c85acd563064c5fc7ac022cda)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HIDS_REPORT_MAP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8b3812488738cf6202586b9202403663)。

HID 报告映射特征（HID Report Map Characteristic）。

<a id="r_gabd625952d5706e851ff40b04e3d86547"></a>

```c
#define BT_UUID_HIDS_CTRL_POINT_VAL 0x2a4c
```

相关声明：[BT_UUID_HIDS_CTRL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabd625952d5706e851ff40b04e3d86547)。

HID 控制点特征（HID Control Point Characteristic）的 UUID 值。

<a id="r_ga8d867aac6ce50f6196c987438aa34c51"></a>

```c
#define BT_UUID_HIDS_CTRL_POINT BT_UUID_DECLARE_16(BT_UUID_HIDS_CTRL_POINT_VAL)
```

相关声明：[BT_UUID_HIDS_CTRL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8d867aac6ce50f6196c987438aa34c51)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HIDS_CTRL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabd625952d5706e851ff40b04e3d86547)。

HID 控制点特征（HID Control Point Characteristic）。

<a id="r_gad6eea2097a8432254fd82ce3798869d7"></a>

```c
#define BT_UUID_HIDS_REPORT_VAL 0x2a4d
```

相关声明：[BT_UUID_HIDS_REPORT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad6eea2097a8432254fd82ce3798869d7)。

HID 报告特征（HID Report Characteristic）的 UUID 值。

<a id="r_ga76e590c2499cc6d7540b0bbce20daec9"></a>

```c
#define BT_UUID_HIDS_REPORT BT_UUID_DECLARE_16(BT_UUID_HIDS_REPORT_VAL)
```

相关声明：[BT_UUID_HIDS_REPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga76e590c2499cc6d7540b0bbce20daec9)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HIDS_REPORT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad6eea2097a8432254fd82ce3798869d7)。

HID 报告特征（HID Report Characteristic）。

<a id="r_ga7de83d3e0472f4edb4821e75fc209aff"></a>

```c
#define BT_UUID_HIDS_PROTOCOL_MODE_VAL 0x2a4e
```

相关声明：[BT_UUID_HIDS_PROTOCOL_MODE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7de83d3e0472f4edb4821e75fc209aff)。

HID 协议模式特征（HID Protocol Mode Characteristic）的 UUID 值。

<a id="r_ga88f780ded3c66387af8825d7a3a1c8ba"></a>

```c
#define BT_UUID_HIDS_PROTOCOL_MODE BT_UUID_DECLARE_16(BT_UUID_HIDS_PROTOCOL_MODE_VAL)
```

相关声明：[BT_UUID_HIDS_PROTOCOL_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga88f780ded3c66387af8825d7a3a1c8ba)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HIDS_PROTOCOL_MODE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7de83d3e0472f4edb4821e75fc209aff)。

HID 协议模式特征（HID Protocol Mode Characteristic）。

<a id="r_gacc5bebeb6cd2fb4c1b0bc7a78a9c67a2"></a>

```c
#define BT_UUID_GATT_SIW_VAL 0x2a4f
```

相关声明：[BT_UUID_GATT_SIW_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacc5bebeb6cd2fb4c1b0bc7a78a9c67a2)。

GATT 扫描间隔窗口特征（GATT Characteristic Scan Interval Windows）的 UUID 值。

<a id="r_ga2bc786ce9acf331708f874261ab457d7"></a>

```c
#define BT_UUID_GATT_SIW BT_UUID_DECLARE_16(BT_UUID_GATT_SIW_VAL)
```

相关声明：[BT_UUID_GATT_SIW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2bc786ce9acf331708f874261ab457d7)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SIW_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacc5bebeb6cd2fb4c1b0bc7a78a9c67a2)。

GATT 扫描间隔窗口特征（GATT Characteristic Scan Interval Windows）。

<a id="r_gab01c14fa28140cae03cae611ee1d32a1"></a>

```c
#define BT_UUID_DIS_PNP_ID_VAL 0x2a50
```

相关声明：[BT_UUID_DIS_PNP_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab01c14fa28140cae03cae611ee1d32a1)。

DIS 即插即用标识符特征（DIS Characteristic PnP ID）的 UUID 值。

<a id="r_ga259ece0a5de917da4a497563197bcafe"></a>

```c
#define BT_UUID_DIS_PNP_ID BT_UUID_DECLARE_16(BT_UUID_DIS_PNP_ID_VAL)
```

相关声明：[BT_UUID_DIS_PNP_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga259ece0a5de917da4a497563197bcafe)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_DIS_PNP_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab01c14fa28140cae03cae611ee1d32a1)。

DIS 即插即用标识符特征（DIS Characteristic PnP ID）。

<a id="r_gaea2d0fd8564007e96dcdcab634896fd7"></a>

```c
#define BT_UUID_GATT_GF_VAL 0x2a51
```

相关声明：[BT_UUID_GATT_GF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaea2d0fd8564007e96dcdcab634896fd7)。

GATT 葡萄糖功能特征（GATT Characteristic Glucose Feature）的 UUID 值。

<a id="r_ga71ef8682466bc0418dfa848bf83af96c"></a>

```c
#define BT_UUID_GATT_GF BT_UUID_DECLARE_16(BT_UUID_GATT_GF_VAL)
```

相关声明：[BT_UUID_GATT_GF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga71ef8682466bc0418dfa848bf83af96c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_GF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaea2d0fd8564007e96dcdcab634896fd7)。

GATT 葡萄糖功能特征（GATT Characteristic Glucose Feature）。

<a id="r_ga413047b20718bddff95b45e1be0b5125"></a>

```c
#define BT_UUID_RECORD_ACCESS_CONTROL_POINT_VAL 0x2a52
```

相关声明：[BT_UUID_RECORD_ACCESS_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga413047b20718bddff95b45e1be0b5125)。

记录访问控制点特征值（Record Access Control Point Characteristic value）。

<a id="r_ga8eedb1ff835988f3969a1b38713a6636"></a>

```c
#define BT_UUID_RECORD_ACCESS_CONTROL_POINT BT_UUID_DECLARE_16(BT_UUID_RECORD_ACCESS_CONTROL_POINT_VAL)
```

相关声明：[BT_UUID_RECORD_ACCESS_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8eedb1ff835988f3969a1b38713a6636)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_RECORD_ACCESS_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga413047b20718bddff95b45e1be0b5125)。

记录访问控制点（Record Access Control Point）。

<a id="r_ga68f55222e780136b2c88ed9615c08f4e"></a>

```c
#define BT_UUID_RSC_MEASUREMENT_VAL 0x2a53
```

相关声明：[BT_UUID_RSC_MEASUREMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga68f55222e780136b2c88ed9615c08f4e)。

跑步速度与步频 RSC 测量特征（RSC Measurement Characteristic）的 UUID 值。

<a id="r_ga14a447a839d13bdc879da42399e39e63"></a>

```c
#define BT_UUID_RSC_MEASUREMENT BT_UUID_DECLARE_16(BT_UUID_RSC_MEASUREMENT_VAL)
```

相关声明：[BT_UUID_RSC_MEASUREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga14a447a839d13bdc879da42399e39e63)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_RSC_MEASUREMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga68f55222e780136b2c88ed9615c08f4e)。

跑步速度与步频 RSC 测量特征（RSC Measurement Characteristic）。

<a id="r_ga9f07e47cd086e3158f637dc2266f7acb"></a>

```c
#define BT_UUID_RSC_FEATURE_VAL 0x2a54
```

相关声明：[BT_UUID_RSC_FEATURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9f07e47cd086e3158f637dc2266f7acb)。

跑步速度与步频 RSC 功能特征（RSC Feature Characteristic）的 UUID 值。

<a id="r_ga4f64ed5b7c06c530320a9fa68794af3a"></a>

```c
#define BT_UUID_RSC_FEATURE BT_UUID_DECLARE_16(BT_UUID_RSC_FEATURE_VAL)
```

相关声明：[BT_UUID_RSC_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4f64ed5b7c06c530320a9fa68794af3a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_RSC_FEATURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9f07e47cd086e3158f637dc2266f7acb)。

跑步速度与步频 RSC 功能特征（RSC Feature Characteristic）。

<a id="r_gad4fd923bb1733c2e9dd993cafa8b5b01"></a>

```c
#define BT_UUID_SC_CONTROL_POINT_VAL 0x2a55
```

相关声明：[BT_UUID_SC_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad4fd923bb1733c2e9dd993cafa8b5b01)。

速度与步频 SC 控制点特征（SC Control Point Characteristic）的 UUID 值。

<a id="r_ga9d6efa914c5a83dcd39ec502e5ac4178"></a>

```c
#define BT_UUID_SC_CONTROL_POINT BT_UUID_DECLARE_16(BT_UUID_SC_CONTROL_POINT_VAL)
```

相关声明：[BT_UUID_SC_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9d6efa914c5a83dcd39ec502e5ac4178)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_SC_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad4fd923bb1733c2e9dd993cafa8b5b01)。

速度与步频 SC 控制点特征（SC Control Point Characteristic）。

<a id="r_gab1af32d2ba06891961e32b46917b39ab"></a>

```c
#define BT_UUID_GATT_DI_VAL 0x2a56
```

相关声明：[BT_UUID_GATT_DI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab1af32d2ba06891961e32b46917b39ab)。

GATT 数字输入特征（GATT Characteristic Digital Input）的 UUID 值。

<a id="r_ga8c4a4fd21416af1be4a0ff2760c48786"></a>

```c
#define BT_UUID_GATT_DI BT_UUID_DECLARE_16(BT_UUID_GATT_DI_VAL)
```

相关声明：[BT_UUID_GATT_DI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8c4a4fd21416af1be4a0ff2760c48786)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_DI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab1af32d2ba06891961e32b46917b39ab)。

GATT 数字输入特征（GATT Characteristic Digital Input）。

<a id="r_gad9c70984dc907efd40e3652603012ada"></a>

```c
#define BT_UUID_GATT_DO_VAL 0x2a57
```

相关声明：[BT_UUID_GATT_DO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad9c70984dc907efd40e3652603012ada)。

GATT 数字输出特征（GATT Characteristic Digital Output）的 UUID 值。

<a id="r_gab39f19f3e38e8954cac13c4ba6db2234"></a>

```c
#define BT_UUID_GATT_DO BT_UUID_DECLARE_16(BT_UUID_GATT_DO_VAL)
```

相关声明：[BT_UUID_GATT_DO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab39f19f3e38e8954cac13c4ba6db2234)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_DO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad9c70984dc907efd40e3652603012ada)。

GATT 数字输出特征（GATT Characteristic Digital Output）。

<a id="r_ga6b9158a8808fe72710023efac16f8d7e"></a>

```c
#define BT_UUID_GATT_AI_VAL 0x2a58
```

相关声明：[BT_UUID_GATT_AI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6b9158a8808fe72710023efac16f8d7e)。

GATT 模拟输入特征（GATT Characteristic Analog Input）的 UUID 值。

<a id="r_ga8f60411278ff93a3d590050ed4a87a70"></a>

```c
#define BT_UUID_GATT_AI BT_UUID_DECLARE_16(BT_UUID_GATT_AI_VAL)
```

相关声明：[BT_UUID_GATT_AI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8f60411278ff93a3d590050ed4a87a70)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_AI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6b9158a8808fe72710023efac16f8d7e)。

GATT 模拟输入特征（GATT Characteristic Analog Input）。

<a id="r_gae6b9567925c04cde856d656c091540fc"></a>

```c
#define BT_UUID_GATT_AO_VAL 0x2a59
```

相关声明：[BT_UUID_GATT_AO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae6b9567925c04cde856d656c091540fc)。

GATT 模拟输出特征（GATT Characteristic Analog Output）的 UUID 值。

<a id="r_ga3f04b6880bc88de907a3c5b5e1acc10b"></a>

```c
#define BT_UUID_GATT_AO BT_UUID_DECLARE_16(BT_UUID_GATT_AO_VAL)
```

相关声明：[BT_UUID_GATT_AO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3f04b6880bc88de907a3c5b5e1acc10b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_AO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae6b9567925c04cde856d656c091540fc)。

GATT 模拟输出特征（GATT Characteristic Analog Output）。

<a id="r_gadb16be338b14fbd82f7c33b6b92502e8"></a>

```c
#define BT_UUID_GATT_AGGR_VAL 0x2a5a
```

相关声明：[BT_UUID_GATT_AGGR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadb16be338b14fbd82f7c33b6b92502e8)。

GATT 聚合特征（GATT Characteristic Aggregate）的 UUID 值。

<a id="r_ga7bc66b120e8a90631fe557c9393a7b88"></a>

```c
#define BT_UUID_GATT_AGGR BT_UUID_DECLARE_16(BT_UUID_GATT_AGGR_VAL)
```

相关声明：[BT_UUID_GATT_AGGR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7bc66b120e8a90631fe557c9393a7b88)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_AGGR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadb16be338b14fbd82f7c33b6b92502e8)。

GATT 聚合特征（GATT Characteristic Aggregate）。

<a id="r_ga3465d2cfa3704021b137316d04d786b1"></a>

```c
#define BT_UUID_CSC_MEASUREMENT_VAL 0x2a5b
```

相关声明：[BT_UUID_CSC_MEASUREMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3465d2cfa3704021b137316d04d786b1)。

骑行速度与踏频 CSC 测量特征（CSC Measurement Characteristic）的 UUID 值。

<a id="r_gab3a6cac39fe5370fe4c23f43a165db2d"></a>

```c
#define BT_UUID_CSC_MEASUREMENT BT_UUID_DECLARE_16(BT_UUID_CSC_MEASUREMENT_VAL)
```

相关声明：[BT_UUID_CSC_MEASUREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab3a6cac39fe5370fe4c23f43a165db2d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CSC_MEASUREMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3465d2cfa3704021b137316d04d786b1)。

骑行速度与踏频 CSC 测量特征（CSC Measurement Characteristic）。

<a id="r_ga7f697ab76e21d37c62080fe0b5a0e591"></a>

```c
#define BT_UUID_CSC_FEATURE_VAL 0x2a5c
```

相关声明：[BT_UUID_CSC_FEATURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7f697ab76e21d37c62080fe0b5a0e591)。

骑行速度与踏频 CSC 功能特征（CSC Feature Characteristic）的 UUID 值。

<a id="r_gaa4d36cbd23dfb98f8baa5da37f7754ac"></a>

```c
#define BT_UUID_CSC_FEATURE BT_UUID_DECLARE_16(BT_UUID_CSC_FEATURE_VAL)
```

相关声明：[BT_UUID_CSC_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa4d36cbd23dfb98f8baa5da37f7754ac)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CSC_FEATURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7f697ab76e21d37c62080fe0b5a0e591)。

骑行速度与踏频 CSC 功能特征（CSC Feature Characteristic）。

<a id="r_gae9aec5938fb89ffe510f66af4b330e19"></a>

```c
#define BT_UUID_SENSOR_LOCATION_VAL 0x2a5d
```

相关声明：[BT_UUID_SENSOR_LOCATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae9aec5938fb89ffe510f66af4b330e19)。

传感器位置特征（Sensor Location Characteristic）的 UUID 值。

<a id="r_gad639330b00b9f8ffcd62c6c1ef7b75d0"></a>

```c
#define BT_UUID_SENSOR_LOCATION BT_UUID_DECLARE_16(BT_UUID_SENSOR_LOCATION_VAL)
```

相关声明：[BT_UUID_SENSOR_LOCATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad639330b00b9f8ffcd62c6c1ef7b75d0)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_SENSOR_LOCATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae9aec5938fb89ffe510f66af4b330e19)。

传感器位置特征（Sensor Location Characteristic）。

<a id="r_ga828a25d5bd3e087a17460a6a0d10c0a9"></a>

```c
#define BT_UUID_GATT_PLX_SCM_VAL 0x2a5e
```

相关声明：[BT_UUID_GATT_PLX_SCM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga828a25d5bd3e087a17460a6a0d10c0a9)。

GATT 脉搏血氧 PLX 单次测量特征（GATT Characteristic PLX Spot-Check Measurement）的 UUID 值。

<a id="r_ga0e691d0bdabf3b8df7c986b44eab4c85"></a>

```c
#define BT_UUID_GATT_PLX_SCM BT_UUID_DECLARE_16(BT_UUID_GATT_PLX_SCM_VAL)
```

相关声明：[BT_UUID_GATT_PLX_SCM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0e691d0bdabf3b8df7c986b44eab4c85)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_PLX_SCM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga828a25d5bd3e087a17460a6a0d10c0a9)。

GATT 脉搏血氧 PLX 单次测量特征（GATT Characteristic PLX Spot-Check Measurement）。

<a id="r_ga4eb8f3c1d2b33bac3b1e7e1d37cab6a3"></a>

```c
#define BT_UUID_GATT_PLX_CM_VAL 0x2a5f
```

相关声明：[BT_UUID_GATT_PLX_CM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4eb8f3c1d2b33bac3b1e7e1d37cab6a3)。

GATT 脉搏血氧 PLX 连续测量特征（GATT Characteristic PLX Continuous Measurement）的 UUID 值。

<a id="r_ga73cf57feba3e1388ad052ffad5832bc1"></a>

```c
#define BT_UUID_GATT_PLX_CM BT_UUID_DECLARE_16(BT_UUID_GATT_PLX_CM_VAL)
```

相关声明：[BT_UUID_GATT_PLX_CM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga73cf57feba3e1388ad052ffad5832bc1)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_PLX_CM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4eb8f3c1d2b33bac3b1e7e1d37cab6a3)。

GATT 脉搏血氧 PLX 连续测量特征（GATT Characteristic PLX Continuous Measurement）。

<a id="r_ga8b523306abec9cadcdc742c21d86d702"></a>

```c
#define BT_UUID_GATT_PLX_F_VAL 0x2a60
```

相关声明：[BT_UUID_GATT_PLX_F_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8b523306abec9cadcdc742c21d86d702)。

GATT 脉搏血氧 PLX 功能特征（GATT Characteristic PLX Features）的 UUID 值。

<a id="r_ga146ec7d39986333cd3583bbfc8ef27fd"></a>

```c
#define BT_UUID_GATT_PLX_F BT_UUID_DECLARE_16(BT_UUID_GATT_PLX_F_VAL)
```

相关声明：[BT_UUID_GATT_PLX_F](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga146ec7d39986333cd3583bbfc8ef27fd)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_PLX_F_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8b523306abec9cadcdc742c21d86d702)。

GATT 脉搏血氧 PLX 功能特征（GATT Characteristic PLX Features）。

<a id="r_gaef6e49a81b4c5a7a32e17ed228a0415a"></a>

```c
#define BT_UUID_GATT_POPE_VAL 0x2a61
```

相关声明：[BT_UUID_GATT_POPE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaef6e49a81b4c5a7a32e17ed228a0415a)。

GATT 脉搏血氧测量脉动事件特征（GATT Characteristic Pulse Oximetry Pulastile Event）的 UUID 值。 译注：原文将 Pulsatile 拼为 Pulastile，英文保留原样。

<a id="r_ga7fa4ae596a22b9fef9db13a830cb8739"></a>

```c
#define BT_UUID_GATT_POPE BT_UUID_DECLARE_16(BT_UUID_GATT_POPE_VAL)
```

相关声明：[BT_UUID_GATT_POPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7fa4ae596a22b9fef9db13a830cb8739)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_POPE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaef6e49a81b4c5a7a32e17ed228a0415a)。

GATT 脉搏血氧测量脉动事件特征（GATT Characteristic Pulse Oximetry Pulsatile Event）。

<a id="r_gac98748753db550fcd2bf338f4e11c246"></a>

```c
#define BT_UUID_GATT_POCP_VAL 0x2a62
```

相关声明：[BT_UUID_GATT_POCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac98748753db550fcd2bf338f4e11c246)。

GATT 脉搏血氧测量控制点特征（GATT Characteristic Pulse Oximetry Control Point）的 UUID 值。

<a id="r_ga2ae69ed734761275ae0e4eb09080207a"></a>

```c
#define BT_UUID_GATT_POCP BT_UUID_DECLARE_16(BT_UUID_GATT_POCP_VAL)
```

相关声明：[BT_UUID_GATT_POCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2ae69ed734761275ae0e4eb09080207a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_POCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac98748753db550fcd2bf338f4e11c246)。

GATT 脉搏血氧测量控制点特征（GATT Characteristic Pulse Oximetry Control Point）。

<a id="r_gabab0970b455fb1f0ea87fb3010782ed0"></a>

```c
#define BT_UUID_GATT_CPS_CPM_VAL 0x2a63
```

相关声明：[BT_UUID_GATT_CPS_CPM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabab0970b455fb1f0ea87fb3010782ed0)。

GATT 骑行功率测量特征（GATT Characteristic Cycling Power Measurement）的 UUID 值。

<a id="r_ga607c07b67d8af3554e36943cea63d1b5"></a>

```c
#define BT_UUID_GATT_CPS_CPM BT_UUID_DECLARE_16(BT_UUID_GATT_CPS_CPM_VAL)
```

相关声明：[BT_UUID_GATT_CPS_CPM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga607c07b67d8af3554e36943cea63d1b5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CPS_CPM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabab0970b455fb1f0ea87fb3010782ed0)。

GATT 骑行功率测量特征（GATT Characteristic Cycling Power Measurement）。

<a id="r_gac4bde8ba3ccd35dbd94018d40438b8fb"></a>

```c
#define BT_UUID_GATT_CPS_CPV_VAL 0x2a64
```

相关声明：[BT_UUID_GATT_CPS_CPV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac4bde8ba3ccd35dbd94018d40438b8fb)。

GATT 骑行功率向量特征（GATT Characteristic Cycling Power Vector）的 UUID 值。

<a id="r_ga99de832aed97db92213ffe90efd60fd7"></a>

```c
#define BT_UUID_GATT_CPS_CPV BT_UUID_DECLARE_16(BT_UUID_GATT_CPS_CPV_VAL)
```

相关声明：[BT_UUID_GATT_CPS_CPV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga99de832aed97db92213ffe90efd60fd7)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CPS_CPV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac4bde8ba3ccd35dbd94018d40438b8fb)。

GATT 骑行功率向量特征（GATT Characteristic Cycling Power Vector）。

<a id="r_ga97647d99503cc60a335d6b9bacc693e9"></a>

```c
#define BT_UUID_GATT_CPS_CPF_VAL 0x2a65
```

相关声明：[BT_UUID_GATT_CPS_CPF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga97647d99503cc60a335d6b9bacc693e9)。

GATT 骑行功率功能特征（GATT Characteristic Cycling Power Feature）的 UUID 值。

<a id="r_ga0b7fbbfa7d539676027d0345a3ce5d83"></a>

```c
#define BT_UUID_GATT_CPS_CPF BT_UUID_DECLARE_16(BT_UUID_GATT_CPS_CPF_VAL)
```

相关声明：[BT_UUID_GATT_CPS_CPF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0b7fbbfa7d539676027d0345a3ce5d83)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CPS_CPF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga97647d99503cc60a335d6b9bacc693e9)。

GATT 骑行功率功能特征（GATT Characteristic Cycling Power Feature）。

<a id="r_ga1efedae02d29eeca33b7e527506169e8"></a>

```c
#define BT_UUID_GATT_CPS_CPCP_VAL 0x2a66
```

相关声明：[BT_UUID_GATT_CPS_CPCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1efedae02d29eeca33b7e527506169e8)。

GATT 骑行功率控制点特征（GATT Characteristic Cycling Power Control Point）的 UUID 值。

<a id="r_gadc239b7879e9b3a082388331a50392c5"></a>

```c
#define BT_UUID_GATT_CPS_CPCP BT_UUID_DECLARE_16(BT_UUID_GATT_CPS_CPCP_VAL)
```

相关声明：[BT_UUID_GATT_CPS_CPCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadc239b7879e9b3a082388331a50392c5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CPS_CPCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1efedae02d29eeca33b7e527506169e8)。

GATT 骑行功率控制点特征（GATT Characteristic Cycling Power Control Point）。

<a id="r_gacc581ed161c7d5461b2d420b8b9a88f1"></a>

```c
#define BT_UUID_GATT_LOC_SPD_VAL 0x2a67
```

相关声明：[BT_UUID_GATT_LOC_SPD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacc581ed161c7d5461b2d420b8b9a88f1)。

GATT 位置与速度特征（GATT Characteristic Location and Speed）的 UUID 值。

<a id="r_gae3a4c256c950e72ecb5767b31033bcb8"></a>

```c
#define BT_UUID_GATT_LOC_SPD BT_UUID_DECLARE_16(BT_UUID_GATT_LOC_SPD_VAL)
```

相关声明：[BT_UUID_GATT_LOC_SPD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae3a4c256c950e72ecb5767b31033bcb8)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LOC_SPD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacc581ed161c7d5461b2d420b8b9a88f1)。

GATT 位置与速度特征（GATT Characteristic Location and Speed）。

<a id="r_ga28c8f061887f0e0b25dff4d716a65d92"></a>

```c
#define BT_UUID_GATT_NAV_VAL 0x2a68
```

相关声明：[BT_UUID_GATT_NAV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga28c8f061887f0e0b25dff4d716a65d92)。

GATT 导航特征（GATT Characteristic Navigation）的 UUID 值。

<a id="r_ga6e08e74465bf881a85136d99bec2dc3f"></a>

```c
#define BT_UUID_GATT_NAV BT_UUID_DECLARE_16(BT_UUID_GATT_NAV_VAL)
```

相关声明：[BT_UUID_GATT_NAV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6e08e74465bf881a85136d99bec2dc3f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_NAV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga28c8f061887f0e0b25dff4d716a65d92)。

GATT 导航特征（GATT Characteristic Navigation）。

<a id="r_ga26f80b9d40ff1a9e6718150c337a018c"></a>

```c
#define BT_UUID_GATT_PQ_VAL 0x2a69
```

相关声明：[BT_UUID_GATT_PQ_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga26f80b9d40ff1a9e6718150c337a018c)。

GATT 定位质量特征（GATT Characteristic Position Quality）的 UUID 值。

<a id="r_ga1da56c6bd8423c99aa143756415aebc5"></a>

```c
#define BT_UUID_GATT_PQ BT_UUID_DECLARE_16(BT_UUID_GATT_PQ_VAL)
```

相关声明：[BT_UUID_GATT_PQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1da56c6bd8423c99aa143756415aebc5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_PQ_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga26f80b9d40ff1a9e6718150c337a018c)。

GATT 定位质量特征（GATT Characteristic Position Quality）。

<a id="r_gab3d9abfecb080e73c7f7309cfaa2760e"></a>

```c
#define BT_UUID_GATT_LNF_VAL 0x2a6a
```

相关声明：[BT_UUID_GATT_LNF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab3d9abfecb080e73c7f7309cfaa2760e)。

GATT 位置与导航 LN 功能特征（GATT Characteristic LN Feature）的 UUID 值。

<a id="r_gaee45af0edec1f2d7528b03b3d65f37ea"></a>

```c
#define BT_UUID_GATT_LNF BT_UUID_DECLARE_16(BT_UUID_GATT_LNF_VAL)
```

相关声明：[BT_UUID_GATT_LNF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaee45af0edec1f2d7528b03b3d65f37ea)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LNF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab3d9abfecb080e73c7f7309cfaa2760e)。

GATT 位置与导航 LN 功能特征（GATT Characteristic LN Feature）。

<a id="r_ga2026b24e2189a4fc8292487b7ee94429"></a>

```c
#define BT_UUID_GATT_LNCP_VAL 0x2a6b
```

相关声明：[BT_UUID_GATT_LNCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2026b24e2189a4fc8292487b7ee94429)。

GATT 位置与导航 LN 控制点特征（GATT Characteristic LN Control Point）的 UUID 值。

<a id="r_ga732fde43bbaf6f4c25d824013882089d"></a>

```c
#define BT_UUID_GATT_LNCP BT_UUID_DECLARE_16(BT_UUID_GATT_LNCP_VAL)
```

相关声明：[BT_UUID_GATT_LNCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga732fde43bbaf6f4c25d824013882089d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LNCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2026b24e2189a4fc8292487b7ee94429)。

GATT 位置与导航 LN 控制点特征（GATT Characteristic LN Control Point）。

<a id="r_ga9ee48bd5d6b3ad89252c04861f6d8ff9"></a>

```c
#define BT_UUID_ELEVATION_VAL 0x2a6c
```

相关声明：[BT_UUID_ELEVATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9ee48bd5d6b3ad89252c04861f6d8ff9)。

高程特征（Elevation Characteristic）的 UUID 值。

<a id="r_ga6a556f695cf7c608b9667ecec3091e32"></a>

```c
#define BT_UUID_ELEVATION BT_UUID_DECLARE_16(BT_UUID_ELEVATION_VAL)
```

相关声明：[BT_UUID_ELEVATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6a556f695cf7c608b9667ecec3091e32)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_ELEVATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9ee48bd5d6b3ad89252c04861f6d8ff9)。

高程特征（Elevation Characteristic）。

<a id="r_ga9bb13b8b9d9212f8f7ef4559db81ab00"></a>

```c
#define BT_UUID_PRESSURE_VAL 0x2a6d
```

相关声明：[BT_UUID_PRESSURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9bb13b8b9d9212f8f7ef4559db81ab00)。

压力特征（Pressure Characteristic）的 UUID 值。

<a id="r_ga3c179c975cfd6f0797e1098d65d59654"></a>

```c
#define BT_UUID_PRESSURE BT_UUID_DECLARE_16(BT_UUID_PRESSURE_VAL)
```

相关声明：[BT_UUID_PRESSURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3c179c975cfd6f0797e1098d65d59654)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_PRESSURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9bb13b8b9d9212f8f7ef4559db81ab00)。

压力特征（Pressure Characteristic）。

<a id="r_ga9f420dc2ff26a723fe4cbdd467e64d47"></a>

```c
#define BT_UUID_TEMPERATURE_VAL 0x2a6e
```

相关声明：[BT_UUID_TEMPERATURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9f420dc2ff26a723fe4cbdd467e64d47)。

温度特征（Temperature Characteristic）的 UUID 值。

<a id="r_ga9ce10219c9d9b2f16b9bc101398a5093"></a>

```c
#define BT_UUID_TEMPERATURE BT_UUID_DECLARE_16(BT_UUID_TEMPERATURE_VAL)
```

相关声明：[BT_UUID_TEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9ce10219c9d9b2f16b9bc101398a5093)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TEMPERATURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9f420dc2ff26a723fe4cbdd467e64d47)。

温度特征（Temperature Characteristic）。

<a id="r_gaa1739f28a51d563d6c9b77c2f7cbf081"></a>

```c
#define BT_UUID_HUMIDITY_VAL 0x2a6f
```

相关声明：[BT_UUID_HUMIDITY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa1739f28a51d563d6c9b77c2f7cbf081)。

湿度特征（Humidity Characteristic）的 UUID 值。

<a id="r_gae6d2caca722e06366171b25659798478"></a>

```c
#define BT_UUID_HUMIDITY BT_UUID_DECLARE_16(BT_UUID_HUMIDITY_VAL)
```

相关声明：[BT_UUID_HUMIDITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae6d2caca722e06366171b25659798478)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HUMIDITY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa1739f28a51d563d6c9b77c2f7cbf081)。

湿度特征（Humidity Characteristic）。

<a id="r_gab89e34d55bd53f075dac53f0720241ba"></a>

```c
#define BT_UUID_TRUE_WIND_SPEED_VAL 0x2a70
```

相关声明：[BT_UUID_TRUE_WIND_SPEED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab89e34d55bd53f075dac53f0720241ba)。

真风速特征（True Wind Speed Characteristic）的 UUID 值。

<a id="r_ga1bf8b992dc79021b1a3f876b2898d25d"></a>

```c
#define BT_UUID_TRUE_WIND_SPEED BT_UUID_DECLARE_16(BT_UUID_TRUE_WIND_SPEED_VAL)
```

相关声明：[BT_UUID_TRUE_WIND_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1bf8b992dc79021b1a3f876b2898d25d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TRUE_WIND_SPEED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab89e34d55bd53f075dac53f0720241ba)。

真风速特征（True Wind Speed Characteristic）。

<a id="r_ga7d77a45acb17505099602df264b8bb96"></a>

```c
#define BT_UUID_TRUE_WIND_DIR_VAL 0x2a71
```

相关声明：[BT_UUID_TRUE_WIND_DIR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7d77a45acb17505099602df264b8bb96)。

真风向特征（True Wind Direction Characteristic）的 UUID 值。

<a id="r_ga0ba41218ce4954620dfe73f06089fc96"></a>

```c
#define BT_UUID_TRUE_WIND_DIR BT_UUID_DECLARE_16(BT_UUID_TRUE_WIND_DIR_VAL)
```

相关声明：[BT_UUID_TRUE_WIND_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0ba41218ce4954620dfe73f06089fc96)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TRUE_WIND_DIR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7d77a45acb17505099602df264b8bb96)。

真风向特征（True Wind Direction Characteristic）。

<a id="r_gad0cff10ce44864db5128c438e4be7c8d"></a>

```c
#define BT_UUID_APPARENT_WIND_SPEED_VAL 0x2a72
```

相关声明：[BT_UUID_APPARENT_WIND_SPEED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad0cff10ce44864db5128c438e4be7c8d)。

视风速特征（Apparent Wind Speed Characteristic）的 UUID 值。

<a id="r_gaf6a81b9581f029463314fb25dd100e95"></a>

```c
#define BT_UUID_APPARENT_WIND_SPEED BT_UUID_DECLARE_16(BT_UUID_APPARENT_WIND_SPEED_VAL)
```

相关声明：[BT_UUID_APPARENT_WIND_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf6a81b9581f029463314fb25dd100e95)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_APPARENT_WIND_SPEED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad0cff10ce44864db5128c438e4be7c8d)。

视风速特征（Apparent Wind Speed Characteristic）。

<a id="r_ga5eb592d6e55ca89ae5cd825edae6d508"></a>

```c
#define BT_UUID_APPARENT_WIND_DIR_VAL 0x2a73
```

相关声明：[BT_UUID_APPARENT_WIND_DIR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5eb592d6e55ca89ae5cd825edae6d508)。

视风向特征（Apparent Wind Direction Characteristic）的 UUID 值。

<a id="r_ga69adddc8dc981d2b5d02ab604826e42b"></a>

```c
#define BT_UUID_APPARENT_WIND_DIR BT_UUID_DECLARE_16(BT_UUID_APPARENT_WIND_DIR_VAL)
```

相关声明：[BT_UUID_APPARENT_WIND_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga69adddc8dc981d2b5d02ab604826e42b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_APPARENT_WIND_DIR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5eb592d6e55ca89ae5cd825edae6d508)。

视风向特征（Apparent Wind Direction Characteristic）。

<a id="r_ga52857a87ddb7c2df50dcb8436804c7e2"></a>

```c
#define BT_UUID_GUST_FACTOR_VAL 0x2a74
```

相关声明：[BT_UUID_GUST_FACTOR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga52857a87ddb7c2df50dcb8436804c7e2)。

阵风因子特征（Gust Factor Characteristic）的 UUID 值。

<a id="r_ga0b97427c4d526e544b0fc1b778756941"></a>

```c
#define BT_UUID_GUST_FACTOR BT_UUID_DECLARE_16(BT_UUID_GUST_FACTOR_VAL)
```

相关声明：[BT_UUID_GUST_FACTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0b97427c4d526e544b0fc1b778756941)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GUST_FACTOR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga52857a87ddb7c2df50dcb8436804c7e2)。

阵风因子特征（Gust Factor Characteristic）。

<a id="r_gaececeeeb1976c979aafafe3c892f8a59"></a>

```c
#define BT_UUID_POLLEN_CONCENTRATION_VAL 0x2a75
```

相关声明：[BT_UUID_POLLEN_CONCENTRATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaececeeeb1976c979aafafe3c892f8a59)。

花粉浓度特征（Pollen Concentration Characteristic）的 UUID 值。

<a id="r_gaa1a189a6d6b23f6983e38124e53aa8be"></a>

```c
#define BT_UUID_POLLEN_CONCENTRATION BT_UUID_DECLARE_16(BT_UUID_POLLEN_CONCENTRATION_VAL)
```

相关声明：[BT_UUID_POLLEN_CONCENTRATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa1a189a6d6b23f6983e38124e53aa8be)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_POLLEN_CONCENTRATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaececeeeb1976c979aafafe3c892f8a59)。

花粉浓度特征（Pollen Concentration Characteristic）。

<a id="r_gae30333c9b8a0b24f1fa6790872fc7a55"></a>

```c
#define BT_UUID_UV_INDEX_VAL 0x2a76
```

相关声明：[BT_UUID_UV_INDEX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae30333c9b8a0b24f1fa6790872fc7a55)。

紫外线指数特征（UV Index Characteristic）的 UUID 值。

<a id="r_gab47898ad86865b6fd514f577e3b7d6f6"></a>

```c
#define BT_UUID_UV_INDEX BT_UUID_DECLARE_16(BT_UUID_UV_INDEX_VAL)
```

相关声明：[BT_UUID_UV_INDEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab47898ad86865b6fd514f577e3b7d6f6)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_UV_INDEX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae30333c9b8a0b24f1fa6790872fc7a55)。

紫外线指数特征（UV Index Characteristic）。

<a id="r_gaa48c2c1a4c75a3b1071b0ef4ca480150"></a>

```c
#define BT_UUID_IRRADIANCE_VAL 0x2a77
```

相关声明：[BT_UUID_IRRADIANCE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa48c2c1a4c75a3b1071b0ef4ca480150)。

辐照度特征（Irradiance Characteristic）的 UUID 值。

<a id="r_ga1e5254104ebb5ccd9a1e3c0915891aad"></a>

```c
#define BT_UUID_IRRADIANCE BT_UUID_DECLARE_16(BT_UUID_IRRADIANCE_VAL)
```

相关声明：[BT_UUID_IRRADIANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1e5254104ebb5ccd9a1e3c0915891aad)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_IRRADIANCE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa48c2c1a4c75a3b1071b0ef4ca480150)。

辐照度特征（Irradiance Characteristic）。

<a id="r_ga4ed507e7f1ecd49186411efbe4fc26ee"></a>

```c
#define BT_UUID_RAINFALL_VAL 0x2a78
```

相关声明：[BT_UUID_RAINFALL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4ed507e7f1ecd49186411efbe4fc26ee)。

降雨量特征（Rainfall Characteristic）的 UUID 值。

<a id="r_ga71278019b98dac06d067227ce47320ba"></a>

```c
#define BT_UUID_RAINFALL BT_UUID_DECLARE_16(BT_UUID_RAINFALL_VAL)
```

相关声明：[BT_UUID_RAINFALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga71278019b98dac06d067227ce47320ba)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_RAINFALL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4ed507e7f1ecd49186411efbe4fc26ee)。

降雨量特征（Rainfall Characteristic）。

<a id="r_ga424993240c213443fc9e95fa9d4ea913"></a>

```c
#define BT_UUID_WIND_CHILL_VAL 0x2a79
```

相关声明：[BT_UUID_WIND_CHILL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga424993240c213443fc9e95fa9d4ea913)。

风寒特征（Wind Chill Characteristic）的 UUID 值。

<a id="r_ga2bd92aab9da9f594d8a061922c51a137"></a>

```c
#define BT_UUID_WIND_CHILL BT_UUID_DECLARE_16(BT_UUID_WIND_CHILL_VAL)
```

相关声明：[BT_UUID_WIND_CHILL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2bd92aab9da9f594d8a061922c51a137)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_WIND_CHILL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga424993240c213443fc9e95fa9d4ea913)。

风寒特征（Wind Chill Characteristic）。

<a id="r_ga3c0468464a353c37ff4994f49439d27b"></a>

```c
#define BT_UUID_HEAT_INDEX_VAL 0x2a7a
```

相关声明：[BT_UUID_HEAT_INDEX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3c0468464a353c37ff4994f49439d27b)。

酷热指数特征（Heat Index Characteristic）的 UUID 值。

<a id="r_ga56c812b5eb985ff21f91fb430d89deb3"></a>

```c
#define BT_UUID_HEAT_INDEX BT_UUID_DECLARE_16(BT_UUID_HEAT_INDEX_VAL)
```

相关声明：[BT_UUID_HEAT_INDEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga56c812b5eb985ff21f91fb430d89deb3)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HEAT_INDEX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3c0468464a353c37ff4994f49439d27b)。

酷热指数特征（Heat Index Characteristic）。

<a id="r_gacf36659263e0a99aece77af08f4ca816"></a>

```c
#define BT_UUID_DEW_POINT_VAL 0x2a7b
```

相关声明：[BT_UUID_DEW_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacf36659263e0a99aece77af08f4ca816)。

露点特征（Dew Point Characteristic）的 UUID 值。

<a id="r_gaf80bc7369817e44102e530371bdf7771"></a>

```c
#define BT_UUID_DEW_POINT BT_UUID_DECLARE_16(BT_UUID_DEW_POINT_VAL)
```

相关声明：[BT_UUID_DEW_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf80bc7369817e44102e530371bdf7771)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_DEW_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacf36659263e0a99aece77af08f4ca816)。

露点特征（Dew Point Characteristic）。

<a id="r_gabb35ed33581726b5eb3bd09abe3bf090"></a>

```c
#define BT_UUID_GATT_TREND_VAL 0x2a7c
```

相关声明：[BT_UUID_GATT_TREND_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabb35ed33581726b5eb3bd09abe3bf090)。

GATT 趋势特征（GATT Characteristic Trend）的 UUID 值。

<a id="r_ga8b36445adba800c187208c2822a4c0ef"></a>

```c
#define BT_UUID_GATT_TREND BT_UUID_DECLARE_16(BT_UUID_GATT_TREND_VAL)
```

相关声明：[BT_UUID_GATT_TREND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8b36445adba800c187208c2822a4c0ef)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TREND_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabb35ed33581726b5eb3bd09abe3bf090)。

GATT 趋势特征（GATT Characteristic Trend）。

<a id="r_gadaf24469185095c9a64d09f9494202bd"></a>

```c
#define BT_UUID_DESC_VALUE_CHANGED_VAL 0x2a7d
```

相关声明：[BT_UUID_DESC_VALUE_CHANGED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadaf24469185095c9a64d09f9494202bd)。

描述符值已变更特征（Descriptor Value Changed Characteristic）的 UUID 值。

<a id="r_ga12ad8a70a766261bd258c5ff96dda1d0"></a>

```c
#define BT_UUID_DESC_VALUE_CHANGED BT_UUID_DECLARE_16(BT_UUID_DESC_VALUE_CHANGED_VAL)
```

相关声明：[BT_UUID_DESC_VALUE_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga12ad8a70a766261bd258c5ff96dda1d0)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_DESC_VALUE_CHANGED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadaf24469185095c9a64d09f9494202bd)。

描述符值已变更特征（Descriptor Value Changed Characteristic）。

<a id="r_gad0a8a823d03c2cfd29b330422d909468"></a>

```c
#define BT_UUID_GATT_AEHRLL_VAL 0x2a7e
```

相关声明：[BT_UUID_GATT_AEHRLL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad0a8a823d03c2cfd29b330422d909468)。

GATT 有氧心率下限特征（GATT Characteristic Aerobic Heart Rate Low Limit）的 UUID 值。

<a id="r_ga185e4267f64937fae52a15297df555d0"></a>

```c
#define BT_UUID_GATT_AEHRLL BT_UUID_DECLARE_16(BT_UUID_GATT_AEHRLL_VAL)
```

相关声明：[BT_UUID_GATT_AEHRLL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga185e4267f64937fae52a15297df555d0)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_AEHRLL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad0a8a823d03c2cfd29b330422d909468)。

GATT 有氧心率下限特征（GATT Characteristic Aerobic Heart Rate Lower Limit）。

<a id="r_gafe43bdafe5d04b4b5ff205ee9c4efa59"></a>

```c
#define BT_UUID_GATT_AETHR_VAL 0x2a7f
```

相关声明：[BT_UUID_GATT_AETHR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafe43bdafe5d04b4b5ff205ee9c4efa59)。

GATT 有氧阈值特征（GATT Characteristic Aerobic Threshold）的 UUID 值。

<a id="r_ga81826c45c657d1b6e1ab391776e37d04"></a>

```c
#define BT_UUID_GATT_AETHR BT_UUID_DECLARE_16(BT_UUID_GATT_AETHR_VAL)
```

相关声明：[BT_UUID_GATT_AETHR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga81826c45c657d1b6e1ab391776e37d04)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_AETHR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafe43bdafe5d04b4b5ff205ee9c4efa59)。

GATT 有氧阈值特征（GATT Characteristic Aerobic Threshold）。

<a id="r_ga783cfd994944d68e137d4101943d3665"></a>

```c
#define BT_UUID_GATT_AGE_VAL 0x2a80
```

相关声明：[BT_UUID_GATT_AGE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga783cfd994944d68e137d4101943d3665)。

GATT 年龄特征（GATT Characteristic Age）的 UUID 值。

<a id="r_ga76fb417fd8e60358ae753d7139be227f"></a>

```c
#define BT_UUID_GATT_AGE BT_UUID_DECLARE_16(BT_UUID_GATT_AGE_VAL)
```

相关声明：[BT_UUID_GATT_AGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga76fb417fd8e60358ae753d7139be227f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_AGE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga783cfd994944d68e137d4101943d3665)。

GATT 年龄特征（GATT Characteristic Age）。

<a id="r_gac145e3d9d2b97eb18b059a0146bf4831"></a>

```c
#define BT_UUID_GATT_ANHRLL_VAL 0x2a81
```

相关声明：[BT_UUID_GATT_ANHRLL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac145e3d9d2b97eb18b059a0146bf4831)。

GATT 无氧心率下限特征（GATT Characteristic Anaerobic Heart Rate Lower Limit）的 UUID 值。

<a id="r_ga8150d2662f87da3a2175f57236905dbd"></a>

```c
#define BT_UUID_GATT_ANHRLL BT_UUID_DECLARE_16(BT_UUID_GATT_ANHRLL_VAL)
```

相关声明：[BT_UUID_GATT_ANHRLL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8150d2662f87da3a2175f57236905dbd)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ANHRLL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac145e3d9d2b97eb18b059a0146bf4831)。

GATT 无氧心率下限特征（GATT Characteristic Anaerobic Heart Rate Lower Limit）。

<a id="r_gaf160fd8971de7dcfd231474e928c20fd"></a>

```c
#define BT_UUID_GATT_ANHRUL_VAL 0x2a82
```

相关声明：[BT_UUID_GATT_ANHRUL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf160fd8971de7dcfd231474e928c20fd)。

GATT 无氧心率上限特征（GATT Characteristic Anaerobic Heart Rate Upper Limit）的 UUID 值。

<a id="r_gae8c042a675573ca1078b0eacc2041a86"></a>

```c
#define BT_UUID_GATT_ANHRUL BT_UUID_DECLARE_16(BT_UUID_GATT_ANHRUL_VAL)
```

相关声明：[BT_UUID_GATT_ANHRUL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae8c042a675573ca1078b0eacc2041a86)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ANHRUL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf160fd8971de7dcfd231474e928c20fd)。

GATT 无氧心率上限特征（GATT Characteristic Anaerobic Heart Rate Upper Limit）。

<a id="r_ga21eb08c2a91f869b792b5f71135c2586"></a>

```c
#define BT_UUID_GATT_ANTHR_VAL 0x2a83
```

相关声明：[BT_UUID_GATT_ANTHR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga21eb08c2a91f869b792b5f71135c2586)。

GATT 无氧阈值特征（GATT Characteristic Anaerobic Threshold）的 UUID 值。

<a id="r_ga843badc1d786e621ef26b38fa973421a"></a>

```c
#define BT_UUID_GATT_ANTHR BT_UUID_DECLARE_16(BT_UUID_GATT_ANTHR_VAL)
```

相关声明：[BT_UUID_GATT_ANTHR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga843badc1d786e621ef26b38fa973421a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ANTHR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga21eb08c2a91f869b792b5f71135c2586)。

GATT 无氧阈值特征（GATT Characteristic Anaerobic Threshold）。

<a id="r_ga4e2a18435fac380402c890284f4b9cb2"></a>

```c
#define BT_UUID_GATT_AEHRUL_VAL 0x2a84
```

相关声明：[BT_UUID_GATT_AEHRUL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4e2a18435fac380402c890284f4b9cb2)。

GATT 有氧心率上限特征（GATT Characteristic Aerobic Heart Rate Upper Limit）的 UUID 值。

<a id="r_ga7477670294c4af4a0f55426653d382f6"></a>

```c
#define BT_UUID_GATT_AEHRUL BT_UUID_DECLARE_16(BT_UUID_GATT_AEHRUL_VAL)
```

相关声明：[BT_UUID_GATT_AEHRUL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7477670294c4af4a0f55426653d382f6)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_AEHRUL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4e2a18435fac380402c890284f4b9cb2)。

GATT 有氧心率上限特征（GATT Characteristic Aerobic Heart Rate Upper Limit）。

<a id="r_gab72ef81ad3ad789c024749d05cf8a132"></a>

```c
#define BT_UUID_GATT_DATE_BIRTH_VAL 0x2a85
```

相关声明：[BT_UUID_GATT_DATE_BIRTH_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab72ef81ad3ad789c024749d05cf8a132)。

GATT 出生日期特征（GATT Characteristic Date of Birth）的 UUID 值。

<a id="r_ga20f4e7f27ff0beae7239be8e69ec6cae"></a>

```c
#define BT_UUID_GATT_DATE_BIRTH BT_UUID_DECLARE_16(BT_UUID_GATT_DATE_BIRTH_VAL)
```

相关声明：[BT_UUID_GATT_DATE_BIRTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga20f4e7f27ff0beae7239be8e69ec6cae)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_DATE_BIRTH_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab72ef81ad3ad789c024749d05cf8a132)。

GATT 出生日期特征（GATT Characteristic Date of Birth）。

<a id="r_ga896c861e50c844d821f571297f9c5e54"></a>

```c
#define BT_UUID_GATT_DATE_THRASS_VAL 0x2a86
```

相关声明：[BT_UUID_GATT_DATE_THRASS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga896c861e50c844d821f571297f9c5e54)。

GATT 阈值评估日期特征（GATT Characteristic Date of Threshold Assessment）的 UUID 值。

<a id="r_gaf8dbfb3be192a96f6da53a897e853b52"></a>

```c
#define BT_UUID_GATT_DATE_THRASS BT_UUID_DECLARE_16(BT_UUID_GATT_DATE_THRASS_VAL)
```

相关声明：[BT_UUID_GATT_DATE_THRASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf8dbfb3be192a96f6da53a897e853b52)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_DATE_THRASS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga896c861e50c844d821f571297f9c5e54)。

GATT 阈值评估日期特征（GATT Characteristic Date of Threshold Assessment）。

<a id="r_gaf5b2e7bd75c03612409d34874275502b"></a>

```c
#define BT_UUID_GATT_EMAIL_VAL 0x2a87
```

相关声明：[BT_UUID_GATT_EMAIL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf5b2e7bd75c03612409d34874275502b)。

GATT 电子邮件地址特征（GATT Characteristic Email Address）的 UUID 值。

<a id="r_gaf81242da24e4380fcf379cfc0a1bd2d6"></a>

```c
#define BT_UUID_GATT_EMAIL BT_UUID_DECLARE_16(BT_UUID_GATT_EMAIL_VAL)
```

相关声明：[BT_UUID_GATT_EMAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf81242da24e4380fcf379cfc0a1bd2d6)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_EMAIL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf5b2e7bd75c03612409d34874275502b)。

GATT 电子邮件地址特征（GATT Characteristic Email Address）。

<a id="r_ga1b56739dbd398eede2689af120d2ffab"></a>

```c
#define BT_UUID_GATT_FBHRLL_VAL 0x2a88
```

相关声明：[BT_UUID_GATT_FBHRLL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1b56739dbd398eede2689af120d2ffab)。

GATT 燃脂心率下限特征（GATT Characteristic Fat Burn Heart Rate Lower Limit）的 UUID 值。

<a id="r_gafe6b60c5aeb090729e901de822a21179"></a>

```c
#define BT_UUID_GATT_FBHRLL BT_UUID_DECLARE_16(BT_UUID_GATT_FBHRLL_VAL)
```

相关声明：[BT_UUID_GATT_FBHRLL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafe6b60c5aeb090729e901de822a21179)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_FBHRLL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1b56739dbd398eede2689af120d2ffab)。

GATT 燃脂心率下限特征（GATT Characteristic Fat Burn Heart Rate Lower Limit）。

<a id="r_gadaed267d894b3f6637ec65c3ebcaafbe"></a>

```c
#define BT_UUID_GATT_FBHRUL_VAL 0x2a89
```

相关声明：[BT_UUID_GATT_FBHRUL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadaed267d894b3f6637ec65c3ebcaafbe)。

GATT 燃脂心率上限特征（GATT Characteristic Fat Burn Heart Rate Upper Limit）的 UUID 值。

<a id="r_ga499864acace035767c673f7f992fb072"></a>

```c
#define BT_UUID_GATT_FBHRUL BT_UUID_DECLARE_16(BT_UUID_GATT_FBHRUL_VAL)
```

相关声明：[BT_UUID_GATT_FBHRUL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga499864acace035767c673f7f992fb072)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_FBHRUL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadaed267d894b3f6637ec65c3ebcaafbe)。

GATT 燃脂心率上限特征（GATT Characteristic Fat Burn Heart Rate Upper Limit）。

<a id="r_ga05a1552396ae29c2e0e6f23e1e6fe41b"></a>

```c
#define BT_UUID_GATT_FIRST_NAME_VAL 0x2a8a
```

相关声明：[BT_UUID_GATT_FIRST_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga05a1552396ae29c2e0e6f23e1e6fe41b)。

GATT 名特征（GATT Characteristic First Name）的 UUID 值。

<a id="r_ga5668fc0689a92ef812ed7ee1c4bdd2e4"></a>

```c
#define BT_UUID_GATT_FIRST_NAME BT_UUID_DECLARE_16(BT_UUID_GATT_FIRST_NAME_VAL)
```

相关声明：[BT_UUID_GATT_FIRST_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5668fc0689a92ef812ed7ee1c4bdd2e4)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_FIRST_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga05a1552396ae29c2e0e6f23e1e6fe41b)。

GATT 名特征（GATT Characteristic First Name）。

<a id="r_ga0bf726af2e7015a870cdd67e2e055b48"></a>

```c
#define BT_UUID_GATT_5ZHRL_VAL 0x2a8b
```

相关声明：[BT_UUID_GATT_5ZHRL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0bf726af2e7015a870cdd67e2e055b48)。

GATT 五区间心率界限特征（GATT Characteristic Five Zone Heart Rate Limits）的 UUID 值。

<a id="r_ga8c7ec19973ae92bb21e2c13bdc9762e2"></a>

```c
#define BT_UUID_GATT_5ZHRL BT_UUID_DECLARE_16(BT_UUID_GATT_5ZHRL_VAL)
```

相关声明：[BT_UUID_GATT_5ZHRL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8c7ec19973ae92bb21e2c13bdc9762e2)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_5ZHRL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0bf726af2e7015a870cdd67e2e055b48)。

GATT 五区间心率界限特征（GATT Characteristic Five Zone Heart Rate Limits）。

<a id="r_gac5142588ca57f7c8202dab97e19c47f0"></a>

```c
#define BT_UUID_GATT_GENDER_VAL 0x2a8c
```

相关声明：[BT_UUID_GATT_GENDER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac5142588ca57f7c8202dab97e19c47f0)。

GATT 性别特征（GATT Characteristic Gender）的 UUID 值。

<a id="r_ga5f51ed2cf6d32af22216a9fd2d444ed3"></a>

```c
#define BT_UUID_GATT_GENDER BT_UUID_DECLARE_16(BT_UUID_GATT_GENDER_VAL)
```

相关声明：[BT_UUID_GATT_GENDER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5f51ed2cf6d32af22216a9fd2d444ed3)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_GENDER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac5142588ca57f7c8202dab97e19c47f0)。

GATT 性别特征（GATT Characteristic Gender）。

<a id="r_ga8fe65597e6c89ad6fffc3f0c33169ebe"></a>

```c
#define BT_UUID_GATT_HR_MAX_VAL 0x2a8d
```

相关声明：[BT_UUID_GATT_HR_MAX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8fe65597e6c89ad6fffc3f0c33169ebe)。

GATT 最大心率特征（GATT Characteristic Heart Rate Max）的 UUID 值。

<a id="r_ga94b53abaa40569423e0a47428379f42e"></a>

```c
#define BT_UUID_GATT_HR_MAX BT_UUID_DECLARE_16(BT_UUID_GATT_HR_MAX_VAL)
```

相关声明：[BT_UUID_GATT_HR_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga94b53abaa40569423e0a47428379f42e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_HR_MAX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8fe65597e6c89ad6fffc3f0c33169ebe)。

GATT 最大心率特征（GATT Characteristic Heart Rate Max）。

<a id="r_gaa147b4c9f91f0d0675ffba0c715154ec"></a>

```c
#define BT_UUID_GATT_HEIGHT_VAL 0x2a8e
```

相关声明：[BT_UUID_GATT_HEIGHT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa147b4c9f91f0d0675ffba0c715154ec)。

GATT 身高特征（GATT Characteristic Height）的 UUID 值。

<a id="r_gab80f4d69799421d48ab61a1832a575a7"></a>

```c
#define BT_UUID_GATT_HEIGHT BT_UUID_DECLARE_16(BT_UUID_GATT_HEIGHT_VAL)
```

相关声明：[BT_UUID_GATT_HEIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab80f4d69799421d48ab61a1832a575a7)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_HEIGHT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa147b4c9f91f0d0675ffba0c715154ec)。

GATT 身高特征（GATT Characteristic Height）。

<a id="r_gaedb0d5b971613bd7245c3f632b7a8a13"></a>

```c
#define BT_UUID_GATT_HC_VAL 0x2a8f
```

相关声明：[BT_UUID_GATT_HC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaedb0d5b971613bd7245c3f632b7a8a13)。

GATT 臀围特征（GATT Characteristic Hip Circumference）的 UUID 值。

<a id="r_ga3c3e534e884b6b5215a43528a51ff4e3"></a>

```c
#define BT_UUID_GATT_HC BT_UUID_DECLARE_16(BT_UUID_GATT_HC_VAL)
```

相关声明：[BT_UUID_GATT_HC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3c3e534e884b6b5215a43528a51ff4e3)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_HC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaedb0d5b971613bd7245c3f632b7a8a13)。

GATT 臀围特征（GATT Characteristic Hip Circumference）。

<a id="r_ga242f34d1b3dbb26c0efa62e0d23888ea"></a>

```c
#define BT_UUID_GATT_LAST_NAME_VAL 0x2a90
```

相关声明：[BT_UUID_GATT_LAST_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga242f34d1b3dbb26c0efa62e0d23888ea)。

GATT 姓特征（GATT Characteristic Last Name）的 UUID 值。

<a id="r_gabaae49281851c5d6626ef483b90e3d53"></a>

```c
#define BT_UUID_GATT_LAST_NAME BT_UUID_DECLARE_16(BT_UUID_GATT_LAST_NAME_VAL)
```

相关声明：[BT_UUID_GATT_LAST_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabaae49281851c5d6626ef483b90e3d53)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LAST_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga242f34d1b3dbb26c0efa62e0d23888ea)。

GATT 姓特征（GATT Characteristic Last Name）。

<a id="r_ga98a0f14a9a0ac32e48280b1ce441a6fd"></a>

```c
#define BT_UUID_GATT_MRHR_VAL 0x2a91
```

相关声明：[BT_UUID_GATT_MRHR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga98a0f14a9a0ac32e48280b1ce441a6fd)。

GATT 最大建议心率特征（GATT Characteristic Maximum Recommended Heart Rate>）的 UUID 值。 译注：原文在 Rate 后多出一个右尖括号，此处保留原样。

<a id="r_gac855511d479c0c82971cadfff61a4178"></a>

```c
#define BT_UUID_GATT_MRHR BT_UUID_DECLARE_16(BT_UUID_GATT_MRHR_VAL)
```

相关声明：[BT_UUID_GATT_MRHR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac855511d479c0c82971cadfff61a4178)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_MRHR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga98a0f14a9a0ac32e48280b1ce441a6fd)。

GATT 最大建议心率特征（GATT Characteristic Maximum Recommended Heart Rate）。

<a id="r_gaed3bfd56abb70c0dff169c1d2813ec18"></a>

```c
#define BT_UUID_GATT_RHR_VAL 0x2a92
```

相关声明：[BT_UUID_GATT_RHR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaed3bfd56abb70c0dff169c1d2813ec18)。

GATT 静息心率特征（GATT Characteristic Resting Heart Rate）的 UUID 值。

<a id="r_ga4b425ea527897b54a0ed6871ce65b7de"></a>

```c
#define BT_UUID_GATT_RHR BT_UUID_DECLARE_16(BT_UUID_GATT_RHR_VAL)
```

相关声明：[BT_UUID_GATT_RHR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4b425ea527897b54a0ed6871ce65b7de)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_RHR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaed3bfd56abb70c0dff169c1d2813ec18)。

GATT 静息心率特征（GATT Characteristic Resting Heart Rate）。

<a id="r_ga5303fd51cf82df81f635cc1213b7e7c8"></a>

```c
#define BT_UUID_GATT_AEANTHR_VAL 0x2a93
```

相关声明：[BT_UUID_GATT_AEANTHR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5303fd51cf82df81f635cc1213b7e7c8)。

GATT 有氧与无氧阈值对应的运动类型特征（GATT Characteristic Sport Type for Aerobic and Anaerobic Thresholds）的 UUID 值。

<a id="r_gaf80845ed35ef1e841c4805d1a1b346af"></a>

```c
#define BT_UUID_GATT_AEANTHR BT_UUID_DECLARE_16(BT_UUID_GATT_AEANTHR_VAL)
```

相关声明：[BT_UUID_GATT_AEANTHR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf80845ed35ef1e841c4805d1a1b346af)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_AEANTHR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5303fd51cf82df81f635cc1213b7e7c8)。

GATT 有氧与无氧阈值对应的运动类型特征（GATT Characteristic Sport Type for Aerobic and Anaerobic Threshold）。

<a id="r_gafddfc45ece5b3f747190bd3de773ebbe"></a>

```c
#define BT_UUID_GATT_3ZHRL_VAL 0x2a94
```

相关声明：[BT_UUID_GATT_3ZHRL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafddfc45ece5b3f747190bd3de773ebbe)。

GATT 三区间心率界限特征（GATT Characteristic Three Zone Heart Rate Limits）的 UUID 值。

<a id="r_ga0b303fde7bf69dfb0284034338ae1999"></a>

```c
#define BT_UUID_GATT_3ZHRL BT_UUID_DECLARE_16(BT_UUID_GATT_3ZHRL_VAL)
```

相关声明：[BT_UUID_GATT_3ZHRL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0b303fde7bf69dfb0284034338ae1999)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_3ZHRL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafddfc45ece5b3f747190bd3de773ebbe)。

GATT 三区间心率界限特征（GATT Characteristic Three Zone Heart Rate Limits）。

<a id="r_gaa252d83bfa77990bc93d98bda035fd9c"></a>

```c
#define BT_UUID_GATT_2ZHRL_VAL 0x2a95
```

相关声明：[BT_UUID_GATT_2ZHRL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa252d83bfa77990bc93d98bda035fd9c)。

GATT 两区间心率界限特征（GATT Characteristic Two Zone Heart Rate Limits）的 UUID 值。

<a id="r_ga5389bd047e5b6769083a59114ed5603b"></a>

```c
#define BT_UUID_GATT_2ZHRL BT_UUID_DECLARE_16(BT_UUID_GATT_2ZHRL_VAL)
```

相关声明：[BT_UUID_GATT_2ZHRL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5389bd047e5b6769083a59114ed5603b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_2ZHRL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa252d83bfa77990bc93d98bda035fd9c)。

GATT 两区间心率界限特征（GATT Characteristic Two Zone Heart Rate Limits）。

<a id="r_ga2e3de0e6f3ca1dbad4d7dc559f5bc093"></a>

```c
#define BT_UUID_GATT_VO2_MAX_VAL 0x2a96
```

相关声明：[BT_UUID_GATT_VO2_MAX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2e3de0e6f3ca1dbad4d7dc559f5bc093)。

GATT 最大摄氧量特征（GATT Characteristic VO2 Max）的 UUID 值。

<a id="r_gaec914c8c808dc5accb82f7c707f8f9c1"></a>

```c
#define BT_UUID_GATT_VO2_MAX BT_UUID_DECLARE_16(BT_UUID_GATT_VO2_MAX_VAL)
```

相关声明：[BT_UUID_GATT_VO2_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaec914c8c808dc5accb82f7c707f8f9c1)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_VO2_MAX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2e3de0e6f3ca1dbad4d7dc559f5bc093)。

GATT 最大摄氧量特征（GATT Characteristic VO2 Max）。

<a id="r_ga6f843d3c3131abe778d3ec9ce1bcee7d"></a>

```c
#define BT_UUID_GATT_WC_VAL 0x2a97
```

相关声明：[BT_UUID_GATT_WC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6f843d3c3131abe778d3ec9ce1bcee7d)。

GATT 腰围特征（GATT Characteristic Waist Circumference）的 UUID 值。

<a id="r_ga06e0730f0abf36dea42a713b22a0082a"></a>

```c
#define BT_UUID_GATT_WC BT_UUID_DECLARE_16(BT_UUID_GATT_WC_VAL)
```

相关声明：[BT_UUID_GATT_WC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga06e0730f0abf36dea42a713b22a0082a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_WC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6f843d3c3131abe778d3ec9ce1bcee7d)。

GATT 腰围特征（GATT Characteristic Waist Circumference）。

<a id="r_gabd5f45139136449cac740e99e74a9894"></a>

```c
#define BT_UUID_GATT_WEIGHT_VAL 0x2a98
```

相关声明：[BT_UUID_GATT_WEIGHT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabd5f45139136449cac740e99e74a9894)。

GATT 体重特征（GATT Characteristic Weight）的 UUID 值。

<a id="r_ga637f0da0906948ee5b7e40cc602ed167"></a>

```c
#define BT_UUID_GATT_WEIGHT BT_UUID_DECLARE_16(BT_UUID_GATT_WEIGHT_VAL)
```

相关声明：[BT_UUID_GATT_WEIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga637f0da0906948ee5b7e40cc602ed167)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_WEIGHT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabd5f45139136449cac740e99e74a9894)。

GATT 体重特征（GATT Characteristic Weight）。

<a id="r_gaa88fbc8a584c60ad025447e72c5b0cb6"></a>

```c
#define BT_UUID_GATT_DBCHINC_VAL 0x2a99
```

相关声明：[BT_UUID_GATT_DBCHINC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa88fbc8a584c60ad025447e72c5b0cb6)。

GATT 数据库变更递增值特征（GATT Characteristic Database Change Increment）的 UUID 值。

<a id="r_gafa555b52c6f195f3d01905a3923db9f3"></a>

```c
#define BT_UUID_GATT_DBCHINC BT_UUID_DECLARE_16(BT_UUID_GATT_DBCHINC_VAL)
```

相关声明：[BT_UUID_GATT_DBCHINC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafa555b52c6f195f3d01905a3923db9f3)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_DBCHINC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa88fbc8a584c60ad025447e72c5b0cb6)。

GATT 数据库变更递增值特征（GATT Characteristic Database Change Increment）。

<a id="r_gadff9aa175bd9b12f9f882e24335aada5"></a>

```c
#define BT_UUID_GATT_USRIDX_VAL 0x2a9a
```

相关声明：[BT_UUID_GATT_USRIDX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadff9aa175bd9b12f9f882e24335aada5)。

GATT 用户索引特征（GATT Characteristic User Index）的 UUID 值。

<a id="r_ga34b014cdec1c5cf41a65e47234eb3f4e"></a>

```c
#define BT_UUID_GATT_USRIDX BT_UUID_DECLARE_16(BT_UUID_GATT_USRIDX_VAL)
```

相关声明：[BT_UUID_GATT_USRIDX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga34b014cdec1c5cf41a65e47234eb3f4e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_USRIDX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadff9aa175bd9b12f9f882e24335aada5)。

GATT 用户索引特征（GATT Characteristic User Index）。

<a id="r_ga4cb5bc721905c8baa78dc25d9738cbad"></a>

```c
#define BT_UUID_GATT_BCF_VAL 0x2a9b
```

相关声明：[BT_UUID_GATT_BCF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4cb5bc721905c8baa78dc25d9738cbad)。

GATT 身体成分功能特征（GATT Characteristic Body Composition Feature）的 UUID 值。

<a id="r_ga3d96fa7aafedab4d8b2e9910a8db1029"></a>

```c
#define BT_UUID_GATT_BCF BT_UUID_DECLARE_16(BT_UUID_GATT_BCF_VAL)
```

相关声明：[BT_UUID_GATT_BCF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3d96fa7aafedab4d8b2e9910a8db1029)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_BCF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4cb5bc721905c8baa78dc25d9738cbad)。

GATT 身体成分功能特征（GATT Characteristic Body Composition Feature）。

<a id="r_gafa981b32cb8b6babd737922ba8bf1430"></a>

```c
#define BT_UUID_GATT_BCM_VAL 0x2a9c
```

相关声明：[BT_UUID_GATT_BCM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafa981b32cb8b6babd737922ba8bf1430)。

GATT 身体成分测量特征（GATT Characteristic Body Composition Measurement）的 UUID 值。

<a id="r_ga9ade71ac5e947cc41d5ab6b747232a7d"></a>

```c
#define BT_UUID_GATT_BCM BT_UUID_DECLARE_16(BT_UUID_GATT_BCM_VAL)
```

相关声明：[BT_UUID_GATT_BCM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9ade71ac5e947cc41d5ab6b747232a7d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_BCM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafa981b32cb8b6babd737922ba8bf1430)。

GATT 身体成分测量特征（GATT Characteristic Body Composition Measurement）。

<a id="r_ga68a0df5e07c31bf5d532c9ef64c1568c"></a>

```c
#define BT_UUID_GATT_WM_VAL 0x2a9d
```

相关声明：[BT_UUID_GATT_WM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga68a0df5e07c31bf5d532c9ef64c1568c)。

GATT 体重测量特征（GATT Characteristic Weight Measurement）的 UUID 值。

<a id="r_gab9a5d321fb5d2854d7edbe66c4d8956c"></a>

```c
#define BT_UUID_GATT_WM BT_UUID_DECLARE_16(BT_UUID_GATT_WM_VAL)
```

相关声明：[BT_UUID_GATT_WM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab9a5d321fb5d2854d7edbe66c4d8956c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_WM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga68a0df5e07c31bf5d532c9ef64c1568c)。

GATT 体重测量特征（GATT Characteristic Weight Measurement）。

<a id="r_gae5fa58f25c54cbb228d816fb58eb5eed"></a>

```c
#define BT_UUID_GATT_WSF_VAL 0x2a9e
```

相关声明：[BT_UUID_GATT_WSF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae5fa58f25c54cbb228d816fb58eb5eed)。

GATT 体重秤功能特征（GATT Characteristic Weight Scale Feature）的 UUID 值。

<a id="r_ga7c084498045835ca6b9037758ccb437e"></a>

```c
#define BT_UUID_GATT_WSF BT_UUID_DECLARE_16(BT_UUID_GATT_WSF_VAL)
```

相关声明：[BT_UUID_GATT_WSF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7c084498045835ca6b9037758ccb437e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_WSF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae5fa58f25c54cbb228d816fb58eb5eed)。

GATT 体重秤功能特征（GATT Characteristic Weight Scale Feature）。

<a id="r_ga0e8380df1c605924bf794974b9a0c811"></a>

```c
#define BT_UUID_GATT_USRCP_VAL 0x2a9f
```

相关声明：[BT_UUID_GATT_USRCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0e8380df1c605924bf794974b9a0c811)。

GATT 用户控制点特征（GATT Characteristic User Control Point）的 UUID 值。

<a id="r_ga6cf64ee2a0564da8c5468842d4ccca72"></a>

```c
#define BT_UUID_GATT_USRCP BT_UUID_DECLARE_16(BT_UUID_GATT_USRCP_VAL)
```

相关声明：[BT_UUID_GATT_USRCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6cf64ee2a0564da8c5468842d4ccca72)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_USRCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0e8380df1c605924bf794974b9a0c811)。

GATT 用户控制点特征（GATT Characteristic User Control Point）。

<a id="r_ga12df5c55e64d68377b144bbe6afc9fa1"></a>

```c
#define BT_UUID_MAGN_FLUX_DENSITY_2D_VAL 0x2aa0
```

相关声明：[BT_UUID_MAGN_FLUX_DENSITY_2D_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga12df5c55e64d68377b144bbe6afc9fa1)。

二维磁通密度特征（Magnetic Flux Density - 2D Characteristic）的 UUID 值。

<a id="r_ga7c6fe7de55f9167f0deb7e5793683df5"></a>

```c
#define BT_UUID_MAGN_FLUX_DENSITY_2D BT_UUID_DECLARE_16(BT_UUID_MAGN_FLUX_DENSITY_2D_VAL)
```

相关声明：[BT_UUID_MAGN_FLUX_DENSITY_2D](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7c6fe7de55f9167f0deb7e5793683df5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MAGN_FLUX_DENSITY_2D_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga12df5c55e64d68377b144bbe6afc9fa1)。

二维磁通密度特征（Magnetic Flux Density - 2D Characteristic）。

<a id="r_ga6eab42e702b2fe2f74ee316b565b6a15"></a>

```c
#define BT_UUID_MAGN_FLUX_DENSITY_3D_VAL 0x2aa1
```

相关声明：[BT_UUID_MAGN_FLUX_DENSITY_3D_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6eab42e702b2fe2f74ee316b565b6a15)。

三维磁通密度特征（Magnetic Flux Density - 3D Characteristic）的 UUID 值。

<a id="r_ga40845b75cd4b7ec5a561123f58e33f70"></a>

```c
#define BT_UUID_MAGN_FLUX_DENSITY_3D BT_UUID_DECLARE_16(BT_UUID_MAGN_FLUX_DENSITY_3D_VAL)
```

相关声明：[BT_UUID_MAGN_FLUX_DENSITY_3D](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga40845b75cd4b7ec5a561123f58e33f70)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MAGN_FLUX_DENSITY_3D_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6eab42e702b2fe2f74ee316b565b6a15)。

三维磁通密度特征（Magnetic Flux Density - 3D Characteristic）。

<a id="r_ga1bf8e2d09646e1340f7195c90e7b53a5"></a>

```c
#define BT_UUID_GATT_LANG_VAL 0x2aa2
```

相关声明：[BT_UUID_GATT_LANG_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1bf8e2d09646e1340f7195c90e7b53a5)。

GATT 语言特征（GATT Characteristic Language）的 UUID 值。

<a id="r_ga8738fa7d86325f46ac3560b646afd96c"></a>

```c
#define BT_UUID_GATT_LANG BT_UUID_DECLARE_16(BT_UUID_GATT_LANG_VAL)
```

相关声明：[BT_UUID_GATT_LANG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8738fa7d86325f46ac3560b646afd96c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LANG_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1bf8e2d09646e1340f7195c90e7b53a5)。

GATT 语言特征（GATT Characteristic Language）。

<a id="r_ga820b05ac625c07d538697ddda5573b46"></a>

```c
#define BT_UUID_BAR_PRESSURE_TREND_VAL 0x2aa3
```

相关声明：[BT_UUID_BAR_PRESSURE_TREND_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga820b05ac625c07d538697ddda5573b46)。

大气压力趋势特征（Barometric Pressure Trend Characteristic）的 UUID 值。

<a id="r_ga1fcf3463c69e2974877bfa953c9cbe52"></a>

```c
#define BT_UUID_BAR_PRESSURE_TREND BT_UUID_DECLARE_16(BT_UUID_BAR_PRESSURE_TREND_VAL)
```

相关声明：[BT_UUID_BAR_PRESSURE_TREND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1fcf3463c69e2974877bfa953c9cbe52)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BAR_PRESSURE_TREND_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga820b05ac625c07d538697ddda5573b46)。

大气压力趋势特征（Barometric Pressure Trend Characteristic）。

<a id="r_gaa3b803e6b55d72d830f0ee01cfc1c1f4"></a>

```c
#define BT_UUID_BMS_CONTROL_POINT_VAL 0x2aa4
```

相关声明：[BT_UUID_BMS_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa3b803e6b55d72d830f0ee01cfc1c1f4)。

绑定管理控制点（Bond Management Control Point）的 UUID 值。

<a id="r_ga08c91b0e746cce311a0c96bf4347d300"></a>

```c
#define BT_UUID_BMS_CONTROL_POINT BT_UUID_DECLARE_16(BT_UUID_BMS_CONTROL_POINT_VAL)
```

相关声明：[BT_UUID_BMS_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga08c91b0e746cce311a0c96bf4347d300)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BMS_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa3b803e6b55d72d830f0ee01cfc1c1f4)。

绑定管理控制点（Bond Management Control Point）。

<a id="r_ga666cd38fd2225997e302c0517b7d7070"></a>

```c
#define BT_UUID_BMS_FEATURE_VAL 0x2aa5
```

相关声明：[BT_UUID_BMS_FEATURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga666cd38fd2225997e302c0517b7d7070)。

绑定管理功能（Bond Management Feature）的 UUID 值。

<a id="r_ga1d998f7915295eeec0895cfa9d500482"></a>

```c
#define BT_UUID_BMS_FEATURE BT_UUID_DECLARE_16(BT_UUID_BMS_FEATURE_VAL)
```

相关声明：[BT_UUID_BMS_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1d998f7915295eeec0895cfa9d500482)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BMS_FEATURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga666cd38fd2225997e302c0517b7d7070)。

绑定管理功能（Bond Management Feature）。

<a id="r_gad7e8753c103960268eafdf4b8fa5710e"></a>

```c
#define BT_UUID_CENTRAL_ADDR_RES_VAL 0x2aa6
```

相关声明：[BT_UUID_CENTRAL_ADDR_RES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad7e8753c103960268eafdf4b8fa5710e)。

中心设备地址解析特征（Central Address Resolution Characteristic）的 UUID 值。

<a id="r_gaf3c3da6a9485674f8865764a831e6011"></a>

```c
#define BT_UUID_CENTRAL_ADDR_RES BT_UUID_DECLARE_16(BT_UUID_CENTRAL_ADDR_RES_VAL)
```

相关声明：[BT_UUID_CENTRAL_ADDR_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf3c3da6a9485674f8865764a831e6011)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CENTRAL_ADDR_RES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad7e8753c103960268eafdf4b8fa5710e)。

中心设备地址解析特征（Central Address Resolution Characteristic）。

<a id="r_gacec2ac2f394b7d8af60163568581c9ac"></a>

```c
#define BT_UUID_CGM_MEASUREMENT_VAL 0x2aa7
```

相关声明：[BT_UUID_CGM_MEASUREMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacec2ac2f394b7d8af60163568581c9ac)。

连续葡萄糖监测 CGM 测量特征值（CGM Measurement Characteristic value）。

<a id="r_ga634603e1545a177d0ccfad140103f7e5"></a>

```c
#define BT_UUID_CGM_MEASUREMENT BT_UUID_DECLARE_16(BT_UUID_CGM_MEASUREMENT_VAL)
```

相关声明：[BT_UUID_CGM_MEASUREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga634603e1545a177d0ccfad140103f7e5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CGM_MEASUREMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacec2ac2f394b7d8af60163568581c9ac)。

连续葡萄糖监测 CGM 测量特征（CGM Measurement Characteristic）。

<a id="r_ga693fb44bd4fe9b2da9071b04170bed8a"></a>

```c
#define BT_UUID_CGM_FEATURE_VAL 0x2aa8
```

相关声明：[BT_UUID_CGM_FEATURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga693fb44bd4fe9b2da9071b04170bed8a)。

连续葡萄糖监测 CGM 功能特征值（CGM Feature Characteristic value）。

<a id="r_ga6be4b6b21e0c5f1dd06f45e309cc4097"></a>

```c
#define BT_UUID_CGM_FEATURE BT_UUID_DECLARE_16(BT_UUID_CGM_FEATURE_VAL)
```

相关声明：[BT_UUID_CGM_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6be4b6b21e0c5f1dd06f45e309cc4097)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CGM_FEATURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga693fb44bd4fe9b2da9071b04170bed8a)。

连续葡萄糖监测 CGM 功能特征（CGM Feature Characteristic）。

<a id="r_ga0c2ebf2de8e5f2a83ebc2f11a6a79441"></a>

```c
#define BT_UUID_CGM_STATUS_VAL 0x2aa9
```

相关声明：[BT_UUID_CGM_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0c2ebf2de8e5f2a83ebc2f11a6a79441)。

连续葡萄糖监测 CGM 状态特征值（CGM Status Characteristic value）。

<a id="r_ga040dec91474ceaf096c2864eb0f46bff"></a>

```c
#define BT_UUID_CGM_STATUS BT_UUID_DECLARE_16(BT_UUID_CGM_STATUS_VAL)
```

相关声明：[BT_UUID_CGM_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga040dec91474ceaf096c2864eb0f46bff)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CGM_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0c2ebf2de8e5f2a83ebc2f11a6a79441)。

连续葡萄糖监测 CGM 状态特征（CGM Status Characteristic）。

<a id="r_ga6f646767f25f2d94cb1190ad4acef86f"></a>

```c
#define BT_UUID_CGM_SESSION_START_TIME_VAL 0x2aaa
```

相关声明：[BT_UUID_CGM_SESSION_START_TIME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6f646767f25f2d94cb1190ad4acef86f)。

连续葡萄糖监测 CGM 会话开始时间特征值（CGM Session Start Time Characteristic value）。

<a id="r_ga0f17cfb12a8c4d628a26f7c83c8a7f4b"></a>

```c
#define BT_UUID_CGM_SESSION_START_TIME BT_UUID_DECLARE_16(BT_UUID_CGM_SESSION_START_TIME_VAL)
```

相关声明：[BT_UUID_CGM_SESSION_START_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0f17cfb12a8c4d628a26f7c83c8a7f4b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CGM_SESSION_START_TIME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6f646767f25f2d94cb1190ad4acef86f)。

连续葡萄糖监测 CGM 会话开始时间（CGM Session Start Time）。

<a id="r_ga98d88d1b785d3b71b9e3b95864efdbf7"></a>

```c
#define BT_UUID_CGM_SESSION_RUN_TIME_VAL 0x2aab
```

相关声明：[BT_UUID_CGM_SESSION_RUN_TIME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga98d88d1b785d3b71b9e3b95864efdbf7)。

连续葡萄糖监测 CGM 会话运行时间特征值（CGM Session Run Time Characteristic value）。

<a id="r_ga0f8565339251160fb439d06f5b29b4cf"></a>

```c
#define BT_UUID_CGM_SESSION_RUN_TIME BT_UUID_DECLARE_16(BT_UUID_CGM_SESSION_RUN_TIME_VAL)
```

相关声明：[BT_UUID_CGM_SESSION_RUN_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0f8565339251160fb439d06f5b29b4cf)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CGM_SESSION_RUN_TIME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga98d88d1b785d3b71b9e3b95864efdbf7)。

连续葡萄糖监测 CGM 会话运行时间（CGM Session Run Time）。

<a id="r_gaec1bbb364e33912fcc22e63c369e4c77"></a>

```c
#define BT_UUID_CGM_SPECIFIC_OPS_CONTROL_POINT_VAL 0x2aac
```

相关声明：[BT_UUID_CGM_SPECIFIC_OPS_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaec1bbb364e33912fcc22e63c369e4c77)。

连续葡萄糖监测 CGM 专用操作控制点特征值（CGM Specific Ops Control Point Characteristic value）。

<a id="r_ga820aab0acff43919e2710b3d5f93ef4b"></a>

```c
#define BT_UUID_CGM_SPECIFIC_OPS_CONTROL_POINT BT_UUID_DECLARE_16(BT_UUID_CGM_SPECIFIC_OPS_CONTROL_POINT_VAL)
```

相关声明：[BT_UUID_CGM_SPECIFIC_OPS_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga820aab0acff43919e2710b3d5f93ef4b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CGM_SPECIFIC_OPS_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaec1bbb364e33912fcc22e63c369e4c77)。

连续葡萄糖监测 CGM 专用操作控制点（CGM Specific Ops Control Point）。

<a id="r_gafe31f631bf3f9a232214dafa76b35ba6"></a>

```c
#define BT_UUID_GATT_IPC_VAL 0x2aad
```

相关声明：[BT_UUID_GATT_IPC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafe31f631bf3f9a232214dafa76b35ba6)。

GATT 室内定位配置特征（GATT Characteristic Indoor Positioning Configuration）的 UUID 值。

<a id="r_ga350bcb39fe9c71f12e5661e4157e95f2"></a>

```c
#define BT_UUID_GATT_IPC BT_UUID_DECLARE_16(BT_UUID_GATT_IPC_VAL)
```

相关声明：[BT_UUID_GATT_IPC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga350bcb39fe9c71f12e5661e4157e95f2)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_IPC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafe31f631bf3f9a232214dafa76b35ba6)。

GATT 室内定位配置特征（GATT Characteristic Indoor Positioning Configuration）。

<a id="r_gadda62951b9abf642684b266f1f073856"></a>

```c
#define BT_UUID_GATT_LAT_VAL 0x2aae
```

相关声明：[BT_UUID_GATT_LAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadda62951b9abf642684b266f1f073856)。

GATT 纬度特征（GATT Characteristic Latitude）的 UUID 值。

<a id="r_ga0dcbbd018fd83efcb84721146fa8c47d"></a>

```c
#define BT_UUID_GATT_LAT BT_UUID_DECLARE_16(BT_UUID_GATT_LAT_VAL)
```

相关声明：[BT_UUID_GATT_LAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0dcbbd018fd83efcb84721146fa8c47d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadda62951b9abf642684b266f1f073856)。

GATT 纬度特征（GATT Characteristic Latitude）。

<a id="r_ga89312e66f25972bced92a8ea1574037a"></a>

```c
#define BT_UUID_GATT_LON_VAL 0x2aaf
```

相关声明：[BT_UUID_GATT_LON_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga89312e66f25972bced92a8ea1574037a)。

GATT 经度特征（GATT Characteristic Longitude）的 UUID 值。

<a id="r_ga59aa1b51e5948c649d0d49d5d7fe45ed"></a>

```c
#define BT_UUID_GATT_LON BT_UUID_DECLARE_16(BT_UUID_GATT_LON_VAL)
```

相关声明：[BT_UUID_GATT_LON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga59aa1b51e5948c649d0d49d5d7fe45ed)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LON_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga89312e66f25972bced92a8ea1574037a)。

GATT 经度特征（GATT Characteristic Longitude）。

<a id="r_gab8183450fa0b94f92709a76f58ce041c"></a>

```c
#define BT_UUID_GATT_LNCOORD_VAL 0x2ab0
```

相关声明：[BT_UUID_GATT_LNCOORD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab8183450fa0b94f92709a76f58ce041c)。

GATT 本地北向坐标特征（GATT Characteristic Local North Coordinate）的 UUID 值。

<a id="r_gaf1294000d6653870589cd0d4e2d3f05f"></a>

```c
#define BT_UUID_GATT_LNCOORD BT_UUID_DECLARE_16(BT_UUID_GATT_LNCOORD_VAL)
```

相关声明：[BT_UUID_GATT_LNCOORD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf1294000d6653870589cd0d4e2d3f05f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LNCOORD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab8183450fa0b94f92709a76f58ce041c)。

GATT 本地北向坐标特征（GATT Characteristic Local North Coordinate）。

<a id="r_ga700e5b0a5be6ba38c882692da43e41f0"></a>

```c
#define BT_UUID_GATT_LECOORD_VAL 0x2ab1
```

相关声明：[BT_UUID_GATT_LECOORD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga700e5b0a5be6ba38c882692da43e41f0)。

GATT 本地东向坐标特征（GATT Characteristic Local East Coordinate）的 UUID 值。

<a id="r_gac7d73c69f971bad67095ee6ad03ed0f2"></a>

```c
#define BT_UUID_GATT_LECOORD BT_UUID_DECLARE_16(BT_UUID_GATT_LECOORD_VAL)
```

相关声明：[BT_UUID_GATT_LECOORD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac7d73c69f971bad67095ee6ad03ed0f2)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LECOORD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga700e5b0a5be6ba38c882692da43e41f0)。

GATT 本地东向坐标特征（GATT Characteristic Local East Coordinate）。

<a id="r_ga64e22e58c78f09f8614079bb8cd4092e"></a>

```c
#define BT_UUID_GATT_FN_VAL 0x2ab2
```

相关声明：[BT_UUID_GATT_FN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga64e22e58c78f09f8614079bb8cd4092e)。

GATT 楼层编号特征（GATT Characteristic Floor Number）的 UUID 值。

<a id="r_ga7fd58fd3410975a1a66f03bdcebabdc3"></a>

```c
#define BT_UUID_GATT_FN BT_UUID_DECLARE_16(BT_UUID_GATT_FN_VAL)
```

相关声明：[BT_UUID_GATT_FN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7fd58fd3410975a1a66f03bdcebabdc3)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_FN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga64e22e58c78f09f8614079bb8cd4092e)。

GATT 楼层编号特征（GATT Characteristic Floor Number）。

<a id="r_ga5b30f97c97ee5006390ab895f4bc438e"></a>

```c
#define BT_UUID_GATT_ALT_VAL 0x2ab3
```

相关声明：[BT_UUID_GATT_ALT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5b30f97c97ee5006390ab895f4bc438e)。

GATT 海拔高度特征（GATT Characteristic Altitude）的 UUID 值。

<a id="r_ga10bdfef928a7cd1da6bf3b3406121c99"></a>

```c
#define BT_UUID_GATT_ALT BT_UUID_DECLARE_16(BT_UUID_GATT_ALT_VAL)
```

相关声明：[BT_UUID_GATT_ALT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga10bdfef928a7cd1da6bf3b3406121c99)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ALT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5b30f97c97ee5006390ab895f4bc438e)。

GATT 海拔高度特征（GATT Characteristic Altitude）。

<a id="r_gaeff0f6c7ab86eb8b264d80d579ad4aa5"></a>

```c
#define BT_UUID_GATT_UNCERTAINTY_VAL 0x2ab4
```

相关声明：[BT_UUID_GATT_UNCERTAINTY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaeff0f6c7ab86eb8b264d80d579ad4aa5)。

GATT 不确定度特征（GATT Characteristic Uncertainty）的 UUID 值。

<a id="r_ga5fc1842a9886deb02cc28887b2e21155"></a>

```c
#define BT_UUID_GATT_UNCERTAINTY BT_UUID_DECLARE_16(BT_UUID_GATT_UNCERTAINTY_VAL)
```

相关声明：[BT_UUID_GATT_UNCERTAINTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5fc1842a9886deb02cc28887b2e21155)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_UNCERTAINTY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaeff0f6c7ab86eb8b264d80d579ad4aa5)。

GATT 不确定度特征（GATT Characteristic Uncertainty）。

<a id="r_gaa7c22c7d434e3a9b9e2f3f44bd75dad1"></a>

```c
#define BT_UUID_GATT_LOC_NAME_VAL 0x2ab5
```

相关声明：[BT_UUID_GATT_LOC_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa7c22c7d434e3a9b9e2f3f44bd75dad1)。

GATT 位置名称特征（GATT Characteristic Location Name）的 UUID 值。

<a id="r_gaa5418e610552e13acaa2c675564ae776"></a>

```c
#define BT_UUID_GATT_LOC_NAME BT_UUID_DECLARE_16(BT_UUID_GATT_LOC_NAME_VAL)
```

相关声明：[BT_UUID_GATT_LOC_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa5418e610552e13acaa2c675564ae776)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LOC_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa7c22c7d434e3a9b9e2f3f44bd75dad1)。

GATT 位置名称特征（GATT Characteristic Location Name）。

<a id="r_gafb86347f61b0e745bf3b970eb6cf71b0"></a>

```c
#define BT_UUID_URI_VAL 0x2ab6
```

相关声明：[BT_UUID_URI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafb86347f61b0e745bf3b970eb6cf71b0)。

统一资源标识符 URI（URI）的 UUID 值。

<a id="r_gaee04f3121fa14082ffabc4d705325449"></a>

```c
#define BT_UUID_URI BT_UUID_DECLARE_16(BT_UUID_URI_VAL)
```

相关声明：[BT_UUID_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaee04f3121fa14082ffabc4d705325449)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_URI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafb86347f61b0e745bf3b970eb6cf71b0)。

统一资源标识符（URI）。

<a id="r_gaf489c9885e90b49b0f072d365c6a7098"></a>

```c
#define BT_UUID_HTTP_HEADERS_VAL 0x2ab7
```

相关声明：[BT_UUID_HTTP_HEADERS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf489c9885e90b49b0f072d365c6a7098)。

HTTP 头部（HTTP Headers）的 UUID 值。

<a id="r_gad88c1b58957bbcc2df817628a6f756db"></a>

```c
#define BT_UUID_HTTP_HEADERS BT_UUID_DECLARE_16(BT_UUID_HTTP_HEADERS_VAL)
```

相关声明：[BT_UUID_HTTP_HEADERS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad88c1b58957bbcc2df817628a6f756db)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HTTP_HEADERS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf489c9885e90b49b0f072d365c6a7098)。

HTTP 头部（HTTP Headers）。

<a id="r_ga257e4213c8e4aa4e6b61dba44e36b268"></a>

```c
#define BT_UUID_HTTP_STATUS_CODE_VAL 0x2ab8
```

相关声明：[BT_UUID_HTTP_STATUS_CODE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga257e4213c8e4aa4e6b61dba44e36b268)。

HTTP 状态码（HTTP Status Code）的 UUID 值。

<a id="r_gaf2e15b1eabca8c810e7f61ee0d650450"></a>

```c
#define BT_UUID_HTTP_STATUS_CODE BT_UUID_DECLARE_16(BT_UUID_HTTP_STATUS_CODE_VAL)
```

相关声明：[BT_UUID_HTTP_STATUS_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf2e15b1eabca8c810e7f61ee0d650450)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HTTP_STATUS_CODE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga257e4213c8e4aa4e6b61dba44e36b268)。

HTTP 状态码（HTTP Status Code）。

<a id="r_ga84600520548f966e511355ee94edbcde"></a>

```c
#define BT_UUID_HTTP_ENTITY_BODY_VAL 0x2ab9
```

相关声明：[BT_UUID_HTTP_ENTITY_BODY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga84600520548f966e511355ee94edbcde)。

HTTP 实体正文（HTTP Entity Body）的 UUID 值。

<a id="r_ga2336a53590edbb9ba14c7aacfa36a592"></a>

```c
#define BT_UUID_HTTP_ENTITY_BODY BT_UUID_DECLARE_16(BT_UUID_HTTP_ENTITY_BODY_VAL)
```

相关声明：[BT_UUID_HTTP_ENTITY_BODY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2336a53590edbb9ba14c7aacfa36a592)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HTTP_ENTITY_BODY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga84600520548f966e511355ee94edbcde)。

HTTP 实体正文（HTTP Entity Body）。

<a id="r_ga37eb19663266e076c35cfa0c73dd0f4f"></a>

```c
#define BT_UUID_HTTP_CONTROL_POINT_VAL 0x2aba
```

相关声明：[BT_UUID_HTTP_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga37eb19663266e076c35cfa0c73dd0f4f)。

HTTP 控制点（HTTP Control Point）的 UUID 值。

<a id="r_ga996630b67869b95babf5f7b280f26c49"></a>

```c
#define BT_UUID_HTTP_CONTROL_POINT BT_UUID_DECLARE_16(BT_UUID_HTTP_CONTROL_POINT_VAL)
```

相关声明：[BT_UUID_HTTP_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga996630b67869b95babf5f7b280f26c49)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HTTP_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga37eb19663266e076c35cfa0c73dd0f4f)。

HTTP 控制点（HTTP Control Point）。

<a id="r_gacaa02070d2036c0cc76b16437e1cc62b"></a>

```c
#define BT_UUID_HTTPS_SECURITY_VAL 0x2abb
```

相关声明：[BT_UUID_HTTPS_SECURITY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacaa02070d2036c0cc76b16437e1cc62b)。

HTTPS 安全（HTTPS Security）的 UUID 值。

<a id="r_ga365519de0ab148b5820442eca52ad700"></a>

```c
#define BT_UUID_HTTPS_SECURITY BT_UUID_DECLARE_16(BT_UUID_HTTPS_SECURITY_VAL)
```

相关声明：[BT_UUID_HTTPS_SECURITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga365519de0ab148b5820442eca52ad700)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HTTPS_SECURITY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacaa02070d2036c0cc76b16437e1cc62b)。

HTTPS 安全（HTTPS Security）。

<a id="r_ga44d037f49e771f08da2381c981fb6ea6"></a>

```c
#define BT_UUID_GATT_TDS_CP_VAL 0x2abc
```

相关声明：[BT_UUID_GATT_TDS_CP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga44d037f49e771f08da2381c981fb6ea6)。

GATT 传输发现服务 TDS 控制点特征（GATT Characteristic TDS Control Point）的 UUID 值。

<a id="r_ga90f08ee842d221580b036d154417c122"></a>

```c
#define BT_UUID_GATT_TDS_CP BT_UUID_DECLARE_16(BT_UUID_GATT_TDS_CP_VAL)
```

相关声明：[BT_UUID_GATT_TDS_CP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga90f08ee842d221580b036d154417c122)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TDS_CP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga44d037f49e771f08da2381c981fb6ea6)。

GATT 传输发现服务 TDS 控制点特征（GATT Characteristic TDS Control Point）。

<a id="r_ga763bb4a64fa3ba2cd3680858d24dd200"></a>

```c
#define BT_UUID_OTS_FEATURE_VAL 0x2abd
```

相关声明：[BT_UUID_OTS_FEATURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga763bb4a64fa3ba2cd3680858d24dd200)。

对象传输服务 OTS 功能特征（OTS Feature Characteristic）的 UUID 值。

<a id="r_ga6bf7967b64150e3bc7f849fa19ddfe7c"></a>

```c
#define BT_UUID_OTS_FEATURE BT_UUID_DECLARE_16(BT_UUID_OTS_FEATURE_VAL)
```

相关声明：[BT_UUID_OTS_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6bf7967b64150e3bc7f849fa19ddfe7c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_FEATURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga763bb4a64fa3ba2cd3680858d24dd200)。

对象传输服务 OTS 功能特征（OTS Feature Characteristic）。

<a id="r_ga4768610413b66751e9e38eef00bc4516"></a>

```c
#define BT_UUID_OTS_NAME_VAL 0x2abe
```

相关声明：[BT_UUID_OTS_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4768610413b66751e9e38eef00bc4516)。

OTS 对象名称特征（OTS Object Name Characteristic）的 UUID 值。

<a id="r_gaa6b72769537df80ba5450b6a398b21ff"></a>

```c
#define BT_UUID_OTS_NAME BT_UUID_DECLARE_16(BT_UUID_OTS_NAME_VAL)
```

相关声明：[BT_UUID_OTS_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa6b72769537df80ba5450b6a398b21ff)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4768610413b66751e9e38eef00bc4516)。

OTS 对象名称特征（OTS Object Name Characteristic）。

<a id="r_ga1e313ee3c5d5047b8d629d99976c1e32"></a>

```c
#define BT_UUID_OTS_TYPE_VAL 0x2abf
```

相关声明：[BT_UUID_OTS_TYPE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1e313ee3c5d5047b8d629d99976c1e32)。

OTS 对象类型特征（OTS Object Type Characteristic）的 UUID 值。

<a id="r_ga94b169c80d3d351c85535d085366086b"></a>

```c
#define BT_UUID_OTS_TYPE BT_UUID_DECLARE_16(BT_UUID_OTS_TYPE_VAL)
```

相关声明：[BT_UUID_OTS_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga94b169c80d3d351c85535d085366086b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_TYPE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1e313ee3c5d5047b8d629d99976c1e32)。

OTS 对象类型特征（OTS Object Type Characteristic）。

<a id="r_ga6072d84794782c93b6c8cb5f30707d9d"></a>

```c
#define BT_UUID_OTS_SIZE_VAL 0x2ac0
```

相关声明：[BT_UUID_OTS_SIZE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6072d84794782c93b6c8cb5f30707d9d)。

OTS 对象大小特征（OTS Object Size Characteristic）的 UUID 值。

<a id="r_gae24957c8aad49fc0f98570b6b313098a"></a>

```c
#define BT_UUID_OTS_SIZE BT_UUID_DECLARE_16(BT_UUID_OTS_SIZE_VAL)
```

相关声明：[BT_UUID_OTS_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae24957c8aad49fc0f98570b6b313098a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_SIZE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6072d84794782c93b6c8cb5f30707d9d)。

OTS 对象大小特征（OTS Object Size Characteristic）。

<a id="r_gab0c3ef2ee627f77c46cc78ec1b6e5543"></a>

```c
#define BT_UUID_OTS_FIRST_CREATED_VAL 0x2ac1
```

相关声明：[BT_UUID_OTS_FIRST_CREATED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab0c3ef2ee627f77c46cc78ec1b6e5543)。

OTS 对象首次创建时间特征（OTS Object First-Created Characteristic）的 UUID 值。

<a id="r_gae5ac09c297a770ebbf7f2a344d24d153"></a>

```c
#define BT_UUID_OTS_FIRST_CREATED BT_UUID_DECLARE_16(BT_UUID_OTS_FIRST_CREATED_VAL)
```

相关声明：[BT_UUID_OTS_FIRST_CREATED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae5ac09c297a770ebbf7f2a344d24d153)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_FIRST_CREATED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab0c3ef2ee627f77c46cc78ec1b6e5543)。

OTS 对象首次创建时间特征（OTS Object First-Created Characteristic）。

<a id="r_gaa9016cda30f09bd61b38654d87198694"></a>

```c
#define BT_UUID_OTS_LAST_MODIFIED_VAL 0x2ac2
```

相关声明：[BT_UUID_OTS_LAST_MODIFIED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa9016cda30f09bd61b38654d87198694)。

OTS 对象最后修改时间特征的 UUI 值（OTS Object Last-Modified Characteristic UUI value）。 译注：原文写作 UUI，此处保留；对应条目为 UUID 常量。

<a id="r_ga06f1570cde6df5e932c72417fe59daef"></a>

```c
#define BT_UUID_OTS_LAST_MODIFIED BT_UUID_DECLARE_16(BT_UUID_OTS_LAST_MODIFIED_VAL)
```

相关声明：[BT_UUID_OTS_LAST_MODIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga06f1570cde6df5e932c72417fe59daef)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_LAST_MODIFIED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa9016cda30f09bd61b38654d87198694)。

OTS 对象最后修改时间特征（OTS Object Last-Modified Characteristic）。

<a id="r_gad32cdd62e0bead3599de3b3dd6e4e014"></a>

```c
#define BT_UUID_OTS_ID_VAL 0x2ac3
```

相关声明：[BT_UUID_OTS_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad32cdd62e0bead3599de3b3dd6e4e014)。

OTS 对象标识符特征（OTS Object ID Characteristic）的 UUID 值。

<a id="r_gaf301617baf5a039c202f0993d80061ce"></a>

```c
#define BT_UUID_OTS_ID BT_UUID_DECLARE_16(BT_UUID_OTS_ID_VAL)
```

相关声明：[BT_UUID_OTS_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf301617baf5a039c202f0993d80061ce)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad32cdd62e0bead3599de3b3dd6e4e014)。

OTS 对象标识符特征（OTS Object ID Characteristic）。

<a id="r_ga0360f97a4f18b56ae3dac4e9b0287602"></a>

```c
#define BT_UUID_OTS_PROPERTIES_VAL 0x2ac4
```

相关声明：[BT_UUID_OTS_PROPERTIES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0360f97a4f18b56ae3dac4e9b0287602)。

OTS 对象属性特征（OTS Object Properties Characteristic）的 UUID 值。

<a id="r_ga215d8088166c529ad1d0024a8f362e3e"></a>

```c
#define BT_UUID_OTS_PROPERTIES BT_UUID_DECLARE_16(BT_UUID_OTS_PROPERTIES_VAL)
```

相关声明：[BT_UUID_OTS_PROPERTIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga215d8088166c529ad1d0024a8f362e3e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_PROPERTIES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0360f97a4f18b56ae3dac4e9b0287602)。

OTS 对象属性特征（OTS Object Properties Characteristic）。

<a id="r_ga7ebe0c55c503cb82cf4d0ee3838f50fe"></a>

```c
#define BT_UUID_OTS_ACTION_CP_VAL 0x2ac5
```

相关声明：[BT_UUID_OTS_ACTION_CP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7ebe0c55c503cb82cf4d0ee3838f50fe)。

OTS 对象操作控制点特征（OTS Object Action Control Point Characteristic）的 UUID 值。

<a id="r_ga29c7bec908eeff922e1aaa3043278d2b"></a>

```c
#define BT_UUID_OTS_ACTION_CP BT_UUID_DECLARE_16(BT_UUID_OTS_ACTION_CP_VAL)
```

相关声明：[BT_UUID_OTS_ACTION_CP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga29c7bec908eeff922e1aaa3043278d2b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_ACTION_CP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7ebe0c55c503cb82cf4d0ee3838f50fe)。

OTS 对象操作控制点特征（OTS Object Action Control Point Characteristic）。

<a id="r_ga145f367de3db51b96ea6922017380aa3"></a>

```c
#define BT_UUID_OTS_LIST_CP_VAL 0x2ac6
```

相关声明：[BT_UUID_OTS_LIST_CP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga145f367de3db51b96ea6922017380aa3)。

OTS 对象列表控制点特征（OTS Object List Control Point Characteristic）的 UUID 值。

<a id="r_ga8acbfefbe1b7cbb5a7aba290d6e7effb"></a>

```c
#define BT_UUID_OTS_LIST_CP BT_UUID_DECLARE_16(BT_UUID_OTS_LIST_CP_VAL)
```

相关声明：[BT_UUID_OTS_LIST_CP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8acbfefbe1b7cbb5a7aba290d6e7effb)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_LIST_CP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga145f367de3db51b96ea6922017380aa3)。

OTS 对象列表控制点特征（OTS Object List Control Point Characteristic）。

<a id="r_ga675bd50dd63de1a13363b041eefc1634"></a>

```c
#define BT_UUID_OTS_LIST_FILTER_VAL 0x2ac7
```

相关声明：[BT_UUID_OTS_LIST_FILTER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga675bd50dd63de1a13363b041eefc1634)。

OTS 对象列表过滤器特征（OTS Object List Filter Characteristic）的 UUID 值。

<a id="r_gabca5bfb5f6fb4a92f29752cb686c7d88"></a>

```c
#define BT_UUID_OTS_LIST_FILTER BT_UUID_DECLARE_16(BT_UUID_OTS_LIST_FILTER_VAL)
```

相关声明：[BT_UUID_OTS_LIST_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabca5bfb5f6fb4a92f29752cb686c7d88)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_LIST_FILTER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga675bd50dd63de1a13363b041eefc1634)。

OTS 对象列表过滤器特征（OTS Object List Filter Characteristic）。

<a id="r_gaea820a540c02088355739bf6ec6e26ba"></a>

```c
#define BT_UUID_OTS_CHANGED_VAL 0x2ac8
```

相关声明：[BT_UUID_OTS_CHANGED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaea820a540c02088355739bf6ec6e26ba)。

OTS 对象已变更特征（OTS Object Changed Characteristic）的 UUID 值。

<a id="r_ga45dc6f040b210aac136b018c760ac37e"></a>

```c
#define BT_UUID_OTS_CHANGED BT_UUID_DECLARE_16(BT_UUID_OTS_CHANGED_VAL)
```

相关声明：[BT_UUID_OTS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga45dc6f040b210aac136b018c760ac37e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_CHANGED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaea820a540c02088355739bf6ec6e26ba)。

OTS 对象已变更特征（OTS Object Changed Characteristic）。

<a id="r_ga080af564ef60858fe3ddc0c487f06e97"></a>

```c
#define BT_UUID_GATT_RPAO_VAL 0x2ac9
```

相关声明：[BT_UUID_GATT_RPAO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga080af564ef60858fe3ddc0c487f06e97)。

GATT 仅使用可解析私有地址特征（GATT Characteristic Resolvable Private Address Only）的 UUID 值。

<a id="r_ga5db6e037e7020b467a5218f828b8a7ea"></a>

```c
#define BT_UUID_GATT_RPAO BT_UUID_DECLARE_16(BT_UUID_GATT_RPAO_VAL)
```

相关声明：[BT_UUID_GATT_RPAO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5db6e037e7020b467a5218f828b8a7ea)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_RPAO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga080af564ef60858fe3ddc0c487f06e97)。

GATT 仅使用可解析私有地址特征（GATT Characteristic Resolvable Private Address Only）。

<a id="r_ga74f28ba3693c541b909580c4fd262416"></a>

```c
#define BT_UUID_OTS_TYPE_UNSPECIFIED_VAL 0x2aca
```

相关声明：[BT_UUID_OTS_TYPE_UNSPECIFIED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga74f28ba3693c541b909580c4fd262416)。

OTS 未指定对象类型（OTS Unspecified Object Type）的 UUID 值。

<a id="r_gadc3afb0781f51b2550b077ee24ce9227"></a>

```c
#define BT_UUID_OTS_TYPE_UNSPECIFIED BT_UUID_DECLARE_16(BT_UUID_OTS_TYPE_UNSPECIFIED_VAL)
```

相关声明：[BT_UUID_OTS_TYPE_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadc3afb0781f51b2550b077ee24ce9227)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_TYPE_UNSPECIFIED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga74f28ba3693c541b909580c4fd262416)。

OTS 未指定对象类型（OTS Unspecified Object Type）。

<a id="r_ga2fee72d19822abcf76cedfbfd96d4cdc"></a>

```c
#define BT_UUID_OTS_DIRECTORY_LISTING_VAL 0x2acb
```

相关声明：[BT_UUID_OTS_DIRECTORY_LISTING_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2fee72d19822abcf76cedfbfd96d4cdc)。

OTS 目录列表（OTS Directory Listing）的 UUID 值。

<a id="r_ga8f306bef03ca5204c99befc1c6e71225"></a>

```c
#define BT_UUID_OTS_DIRECTORY_LISTING BT_UUID_DECLARE_16(BT_UUID_OTS_DIRECTORY_LISTING_VAL)
```

相关声明：[BT_UUID_OTS_DIRECTORY_LISTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8f306bef03ca5204c99befc1c6e71225)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_DIRECTORY_LISTING_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2fee72d19822abcf76cedfbfd96d4cdc)。

OTS 目录列表（OTS Directory Listing）。

<a id="r_ga556cd0fd7d3ff4f862dd3028f0206462"></a>

```c
#define BT_UUID_GATT_FMF_VAL 0x2acc
```

相关声明：[BT_UUID_GATT_FMF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga556cd0fd7d3ff4f862dd3028f0206462)。

GATT 健身器械功能特征（GATT Characteristic Fitness Machine Feature）的 UUID 值。

<a id="r_ga2aeb2e0aa454feb4438f9527c52780ed"></a>

```c
#define BT_UUID_GATT_FMF BT_UUID_DECLARE_16(BT_UUID_GATT_FMF_VAL)
```

相关声明：[BT_UUID_GATT_FMF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2aeb2e0aa454feb4438f9527c52780ed)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_FMF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga556cd0fd7d3ff4f862dd3028f0206462)。

GATT 健身器械功能特征（GATT Characteristic Fitness Machine Feature）。

<a id="r_gaedc6e4f493355fe2999e7f1f84bf5d00"></a>

```c
#define BT_UUID_GATT_TD_VAL 0x2acd
```

相关声明：[BT_UUID_GATT_TD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaedc6e4f493355fe2999e7f1f84bf5d00)。

GATT 跑步机数据特征（GATT Characteristic Treadmill Data）的 UUID 值。

<a id="r_gaa8a7f082cf9b4df21c07ded6a4913b35"></a>

```c
#define BT_UUID_GATT_TD BT_UUID_DECLARE_16(BT_UUID_GATT_TD_VAL)
```

相关声明：[BT_UUID_GATT_TD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa8a7f082cf9b4df21c07ded6a4913b35)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaedc6e4f493355fe2999e7f1f84bf5d00)。

GATT 跑步机数据特征（GATT Characteristic Treadmill Data）。

<a id="r_ga235dc61fb231d43a5aaab0b32f398a48"></a>

```c
#define BT_UUID_GATT_CTD_VAL 0x2ace
```

相关声明：[BT_UUID_GATT_CTD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga235dc61fb231d43a5aaab0b32f398a48)。

GATT 椭圆训练机数据特征（GATT Characteristic Cross Trainer Data）的 UUID 值。

<a id="r_ga47d30eeb1bb66bb84b8b315fbeb76eea"></a>

```c
#define BT_UUID_GATT_CTD BT_UUID_DECLARE_16(BT_UUID_GATT_CTD_VAL)
```

相关声明：[BT_UUID_GATT_CTD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga47d30eeb1bb66bb84b8b315fbeb76eea)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CTD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga235dc61fb231d43a5aaab0b32f398a48)。

GATT 椭圆训练机数据特征（GATT Characteristic Cross Trainer Data）。

<a id="r_ga84863f0507404fd9637319c384468808"></a>

```c
#define BT_UUID_GATT_STPCD_VAL 0x2acf
```

相关声明：[BT_UUID_GATT_STPCD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga84863f0507404fd9637319c384468808)。

GATT 踏步机数据特征（GATT Characteristic Step Climber Data）的 UUID 值。

<a id="r_ga4fd0ee59f5451669a389814d4390c6b5"></a>

```c
#define BT_UUID_GATT_STPCD BT_UUID_DECLARE_16(BT_UUID_GATT_STPCD_VAL)
```

相关声明：[BT_UUID_GATT_STPCD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4fd0ee59f5451669a389814d4390c6b5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_STPCD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga84863f0507404fd9637319c384468808)。

GATT 踏步机数据特征（GATT Characteristic Step Climber Data）。

<a id="r_ga222ab56024893f1019af55052f646aca"></a>

```c
#define BT_UUID_GATT_STRCD_VAL 0x2ad0
```

相关声明：[BT_UUID_GATT_STRCD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga222ab56024893f1019af55052f646aca)。

GATT 楼梯训练机数据特征（GATT Characteristic Stair Climber Data）的 UUID 值。

<a id="r_gae0b7d7316806ee18c4300b399faeb52e"></a>

```c
#define BT_UUID_GATT_STRCD BT_UUID_DECLARE_16(BT_UUID_GATT_STRCD_VAL)
```

相关声明：[BT_UUID_GATT_STRCD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae0b7d7316806ee18c4300b399faeb52e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_STRCD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga222ab56024893f1019af55052f646aca)。

GATT 楼梯训练机数据特征（GATT Characteristic Stair Climber Data）。

<a id="r_gaed2b696b1a2ecbe1e981437ee9e58389"></a>

```c
#define BT_UUID_GATT_RD_VAL 0x2ad1
```

相关声明：[BT_UUID_GATT_RD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaed2b696b1a2ecbe1e981437ee9e58389)。

GATT 划船机数据特征（GATT Characteristic Rower Data）的 UUID 值。

<a id="r_ga933043dfadcbebbbb2c10a828280c0a0"></a>

```c
#define BT_UUID_GATT_RD BT_UUID_DECLARE_16(BT_UUID_GATT_RD_VAL)
```

相关声明：[BT_UUID_GATT_RD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga933043dfadcbebbbb2c10a828280c0a0)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_RD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaed2b696b1a2ecbe1e981437ee9e58389)。

GATT 划船机数据特征（GATT Characteristic Rower Data）。

<a id="r_ga92198d40e1a682c0c7515ba306af2093"></a>

```c
#define BT_UUID_GATT_IBD_VAL 0x2ad2
```

相关声明：[BT_UUID_GATT_IBD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga92198d40e1a682c0c7515ba306af2093)。

GATT 室内自行车数据特征（GATT Characteristic Indoor Bike Data）的 UUID 值。

<a id="r_gaf6d86dfccb1bf3796b1dbd3c087b8127"></a>

```c
#define BT_UUID_GATT_IBD BT_UUID_DECLARE_16(BT_UUID_GATT_IBD_VAL)
```

相关声明：[BT_UUID_GATT_IBD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf6d86dfccb1bf3796b1dbd3c087b8127)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_IBD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga92198d40e1a682c0c7515ba306af2093)。

GATT 室内自行车数据特征（GATT Characteristic Indoor Bike Data）。

<a id="r_ga13e94c01279818ad0ce923051bf4fd1c"></a>

```c
#define BT_UUID_GATT_TRSTAT_VAL 0x2ad3
```

相关声明：[BT_UUID_GATT_TRSTAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga13e94c01279818ad0ce923051bf4fd1c)。

GATT 训练状态特征（GATT Characteristic Training Status）的 UUID 值。

<a id="r_ga5a7f9c7d6d0e93f2d35ff308b875f883"></a>

```c
#define BT_UUID_GATT_TRSTAT BT_UUID_DECLARE_16(BT_UUID_GATT_TRSTAT_VAL)
```

相关声明：[BT_UUID_GATT_TRSTAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5a7f9c7d6d0e93f2d35ff308b875f883)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TRSTAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga13e94c01279818ad0ce923051bf4fd1c)。

GATT 训练状态特征（GATT Characteristic Training Status）。

<a id="r_gadad6f8c3d4cf5f40c5f1f27d5ea38ac3"></a>

```c
#define BT_UUID_GATT_SSR_VAL 0x2ad4
```

相关声明：[BT_UUID_GATT_SSR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadad6f8c3d4cf5f40c5f1f27d5ea38ac3)。

GATT 支持的速度范围特征（GATT Characteristic Supported Speed Range）的 UUID 值。

<a id="r_gab6ef5e742460fba12f8b974fc4bf735d"></a>

```c
#define BT_UUID_GATT_SSR BT_UUID_DECLARE_16(BT_UUID_GATT_SSR_VAL)
```

相关声明：[BT_UUID_GATT_SSR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab6ef5e742460fba12f8b974fc4bf735d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SSR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadad6f8c3d4cf5f40c5f1f27d5ea38ac3)。

GATT 支持的速度范围特征（GATT Characteristic Supported Speed Range）。

<a id="r_ga6339f09bf4e825454fd8c517faf53194"></a>

```c
#define BT_UUID_GATT_SIR_VAL 0x2ad5
```

相关声明：[BT_UUID_GATT_SIR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6339f09bf4e825454fd8c517faf53194)。

GATT 支持的倾斜度范围特征（GATT Characteristic Supported Inclination Range）的 UUID 值。

<a id="r_gac69a06d1568114dec01f46df95a3c5ac"></a>

```c
#define BT_UUID_GATT_SIR BT_UUID_DECLARE_16(BT_UUID_GATT_SIR_VAL)
```

相关声明：[BT_UUID_GATT_SIR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac69a06d1568114dec01f46df95a3c5ac)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SIR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6339f09bf4e825454fd8c517faf53194)。

GATT 支持的倾斜度范围特征（GATT Characteristic Supported Inclination Range）。

<a id="r_gaf6fae4763a3aa3fe1f04b51b108ca642"></a>

```c
#define BT_UUID_GATT_SRLR_VAL 0x2ad6
```

相关声明：[BT_UUID_GATT_SRLR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf6fae4763a3aa3fe1f04b51b108ca642)。

GATT 支持的阻力级别范围特征（GATT Characteristic Supported Resistance Level Range）的 UUID 值。

<a id="r_ga4141c63e9e7924c8d9e27922ebda4b98"></a>

```c
#define BT_UUID_GATT_SRLR BT_UUID_DECLARE_16(BT_UUID_GATT_SRLR_VAL)
```

相关声明：[BT_UUID_GATT_SRLR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4141c63e9e7924c8d9e27922ebda4b98)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SRLR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf6fae4763a3aa3fe1f04b51b108ca642)。

GATT 支持的阻力级别范围特征（GATT Characteristic Supported Resistance Level Range）。

<a id="r_ga8516dbe4b6b630f380f9ab3a80bce179"></a>

```c
#define BT_UUID_GATT_SHRR_VAL 0x2ad7
```

相关声明：[BT_UUID_GATT_SHRR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8516dbe4b6b630f380f9ab3a80bce179)。

GATT 支持的心率范围特征（GATT Characteristic Supported Heart Rate Range）的 UUID 值。

<a id="r_gabe5693829c64f8cd98444c853e0f121c"></a>

```c
#define BT_UUID_GATT_SHRR BT_UUID_DECLARE_16(BT_UUID_GATT_SHRR_VAL)
```

相关声明：[BT_UUID_GATT_SHRR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabe5693829c64f8cd98444c853e0f121c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SHRR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8516dbe4b6b630f380f9ab3a80bce179)。

GATT 支持的心率范围特征（GATT Characteristic Supported Heart Rate Range）。

<a id="r_ga1f7f6e8197940264ff921e6dec5c2e81"></a>

```c
#define BT_UUID_GATT_SPR_VAL 0x2ad8
```

相关声明：[BT_UUID_GATT_SPR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1f7f6e8197940264ff921e6dec5c2e81)。

GATT 支持的功率范围特征（GATT Characteristic Supported Power Range）的 UUID 值。

<a id="r_gab82bacbce14b886d23f9368db97bb329"></a>

```c
#define BT_UUID_GATT_SPR BT_UUID_DECLARE_16(BT_UUID_GATT_SPR_VAL)
```

相关声明：[BT_UUID_GATT_SPR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab82bacbce14b886d23f9368db97bb329)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SPR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1f7f6e8197940264ff921e6dec5c2e81)。

GATT 支持的功率范围特征（GATT Characteristic Supported Power Range）。

<a id="r_gaf910e7d5ce12084045e9283b4c5b8b7e"></a>

```c
#define BT_UUID_GATT_FMCP_VAL 0x2ad9
```

相关声明：[BT_UUID_GATT_FMCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf910e7d5ce12084045e9283b4c5b8b7e)。

GATT 健身器械控制点特征（GATT Characteristic Fitness Machine Control Point）的 UUID 值。

<a id="r_ga26b12f1ef3313b7c28328ae22512b277"></a>

```c
#define BT_UUID_GATT_FMCP BT_UUID_DECLARE_16(BT_UUID_GATT_FMCP_VAL)
```

相关声明：[BT_UUID_GATT_FMCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga26b12f1ef3313b7c28328ae22512b277)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_FMCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf910e7d5ce12084045e9283b4c5b8b7e)。

GATT 健身器械控制点特征（GATT Characteristic Fitness Machine Control Point）。

<a id="r_gaea596e91c046949687c4331a4841dd07"></a>

```c
#define BT_UUID_GATT_FMS_VAL 0x2ada
```

相关声明：[BT_UUID_GATT_FMS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaea596e91c046949687c4331a4841dd07)。

GATT 健身器械状态特征（GATT Characteristic Fitness Machine Status）的 UUID 值。

<a id="r_ga9ff5045f804b6a2a8cd0b2ec8906e4b3"></a>

```c
#define BT_UUID_GATT_FMS BT_UUID_DECLARE_16(BT_UUID_GATT_FMS_VAL)
```

相关声明：[BT_UUID_GATT_FMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9ff5045f804b6a2a8cd0b2ec8906e4b3)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_FMS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaea596e91c046949687c4331a4841dd07)。

GATT 健身器械状态特征（GATT Characteristic Fitness Machine Status）。

<a id="r_ga2bde466cfcaeec5c542d5e74f51ddd05"></a>

```c
#define BT_UUID_MESH_PROV_DATA_IN_VAL 0x2adb
```

相关声明：[BT_UUID_MESH_PROV_DATA_IN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2bde466cfcaeec5c542d5e74f51ddd05)。

网状网络配网数据输入（Mesh Provisioning Data In）的 UUID 值。

<a id="r_gaae548e7ca5a9835bd4dcfdf853c43993"></a>

```c
#define BT_UUID_MESH_PROV_DATA_IN BT_UUID_DECLARE_16(BT_UUID_MESH_PROV_DATA_IN_VAL)
```

相关声明：[BT_UUID_MESH_PROV_DATA_IN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaae548e7ca5a9835bd4dcfdf853c43993)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MESH_PROV_DATA_IN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2bde466cfcaeec5c542d5e74f51ddd05)。

网状网络配网数据输入（Mesh Provisioning Data In）。

<a id="r_gafd6e15eb3ae65d5f480706e68aabad8e"></a>

```c
#define BT_UUID_MESH_PROV_DATA_OUT_VAL 0x2adc
```

相关声明：[BT_UUID_MESH_PROV_DATA_OUT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafd6e15eb3ae65d5f480706e68aabad8e)。

网状网络配网数据输出（Mesh Provisioning Data Out）的 UUID 值。

<a id="r_gaa003522c72e96e8b2c4b7b724aa2bf2e"></a>

```c
#define BT_UUID_MESH_PROV_DATA_OUT BT_UUID_DECLARE_16(BT_UUID_MESH_PROV_DATA_OUT_VAL)
```

相关声明：[BT_UUID_MESH_PROV_DATA_OUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa003522c72e96e8b2c4b7b724aa2bf2e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MESH_PROV_DATA_OUT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafd6e15eb3ae65d5f480706e68aabad8e)。

网状网络配网数据输出（Mesh Provisioning Data Out）。

<a id="r_ga55488739e50c8482da6f4ad0826f0cae"></a>

```c
#define BT_UUID_MESH_PROXY_DATA_IN_VAL 0x2add
```

相关声明：[BT_UUID_MESH_PROXY_DATA_IN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga55488739e50c8482da6f4ad0826f0cae)。

网状网络代理数据输入（Mesh Proxy Data In）的 UUID 值。

<a id="r_gaebcae07983c397b0771f424d2d890259"></a>

```c
#define BT_UUID_MESH_PROXY_DATA_IN BT_UUID_DECLARE_16(BT_UUID_MESH_PROXY_DATA_IN_VAL)
```

相关声明：[BT_UUID_MESH_PROXY_DATA_IN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaebcae07983c397b0771f424d2d890259)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MESH_PROXY_DATA_IN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga55488739e50c8482da6f4ad0826f0cae)。

网状网络代理数据输入（Mesh Proxy Data In）。

<a id="r_ga452dfb3d0f4b62ec327910b9c578ffb0"></a>

```c
#define BT_UUID_MESH_PROXY_DATA_OUT_VAL 0x2ade
```

相关声明：[BT_UUID_MESH_PROXY_DATA_OUT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga452dfb3d0f4b62ec327910b9c578ffb0)。

网状网络代理数据输出（Mesh Proxy Data Out）的 UUID 值。

<a id="r_gaf3fbcbebb0507aec45d94244729f85d8"></a>

```c
#define BT_UUID_MESH_PROXY_DATA_OUT BT_UUID_DECLARE_16(BT_UUID_MESH_PROXY_DATA_OUT_VAL)
```

相关声明：[BT_UUID_MESH_PROXY_DATA_OUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf3fbcbebb0507aec45d94244729f85d8)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MESH_PROXY_DATA_OUT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga452dfb3d0f4b62ec327910b9c578ffb0)。

网状网络代理数据输出（Mesh Proxy Data Out）。

<a id="r_gab01aec4c2f19b53d919c89b58fd92956"></a>

```c
#define BT_UUID_GATT_NNN_VAL 0x2adf
```

相关声明：[BT_UUID_GATT_NNN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab01aec4c2f19b53d919c89b58fd92956)。

GATT 需要新编号特征（GATT Characteristic New Number Needed）的 UUID 值。

<a id="r_ga355480e43c9fd2ee1e7fa72a05141c93"></a>

```c
#define BT_UUID_GATT_NNN BT_UUID_DECLARE_16(BT_UUID_GATT_NNN_VAL)
```

相关声明：[BT_UUID_GATT_NNN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga355480e43c9fd2ee1e7fa72a05141c93)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_NNN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab01aec4c2f19b53d919c89b58fd92956)。

GATT 需要新编号特征（GATT Characteristic New Number Needed）。

<a id="r_gaf2bc7408a53341478f1b41d54e888478"></a>

```c
#define BT_UUID_GATT_AC_VAL 0x2ae0
```

相关声明：[BT_UUID_GATT_AC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf2bc7408a53341478f1b41d54e888478)。

GATT 平均电流特征（GATT Characteristic Average Current）的 UUID 值。

<a id="r_gadbe14281482e776e87facb9835f522af"></a>

```c
#define BT_UUID_GATT_AC BT_UUID_DECLARE_16(BT_UUID_GATT_AC_VAL)
```

相关声明：[BT_UUID_GATT_AC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadbe14281482e776e87facb9835f522af)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_AC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf2bc7408a53341478f1b41d54e888478)。

GATT 平均电流特征（GATT Characteristic Average Current）。

<a id="r_ga2b5c1eef80844de1d49a70314db91b1d"></a>

```c
#define BT_UUID_GATT_AV_VAL 0x2ae1
```

相关声明：[BT_UUID_GATT_AV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2b5c1eef80844de1d49a70314db91b1d)。

GATT 平均电压特征（GATT Characteristic Average Voltage）的 UUID 值。

<a id="r_ga3c669e805ea7fc93cade56f2281b10dc"></a>

```c
#define BT_UUID_GATT_AV BT_UUID_DECLARE_16(BT_UUID_GATT_AV_VAL)
```

相关声明：[BT_UUID_GATT_AV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3c669e805ea7fc93cade56f2281b10dc)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_AV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2b5c1eef80844de1d49a70314db91b1d)。

GATT 平均电压特征（GATT Characteristic Average Voltage）。

<a id="r_ga0e1cbd1ae5c198c0f834802f9d354fb7"></a>

```c
#define BT_UUID_GATT_BOOLEAN_VAL 0x2ae2
```

相关声明：[BT_UUID_GATT_BOOLEAN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0e1cbd1ae5c198c0f834802f9d354fb7)。

GATT 布尔值特征（GATT Characteristic Boolean）的 UUID 值。

<a id="r_ga1801b550a1be17bf0bb8c07818749e4e"></a>

```c
#define BT_UUID_GATT_BOOLEAN BT_UUID_DECLARE_16(BT_UUID_GATT_BOOLEAN_VAL)
```

相关声明：[BT_UUID_GATT_BOOLEAN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1801b550a1be17bf0bb8c07818749e4e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_BOOLEAN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0e1cbd1ae5c198c0f834802f9d354fb7)。

GATT 布尔值特征（GATT Characteristic Boolean）。

<a id="r_ga2601e0757464729c789b58deeee15285"></a>

```c
#define BT_UUID_GATT_CRDFP_VAL 0x2ae3
```

相关声明：[BT_UUID_GATT_CRDFP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2601e0757464729c789b58deeee15285)。

GATT 相对普朗克轨迹的色度距离特征（GATT Characteristic Chromatic Distance From Planckian）的 UUID 值。

<a id="r_gac5bc300a9b31543dc3847990832d78c3"></a>

```c
#define BT_UUID_GATT_CRDFP BT_UUID_DECLARE_16(BT_UUID_GATT_CRDFP_VAL)
```

相关声明：[BT_UUID_GATT_CRDFP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac5bc300a9b31543dc3847990832d78c3)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CRDFP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2601e0757464729c789b58deeee15285)。

GATT 相对普朗克轨迹的色度距离特征（GATT Characteristic Chromatic Distance From Planckian）。

<a id="r_ga8fa1863d2ae7b22462be097308fb5c81"></a>

```c
#define BT_UUID_GATT_CRCOORDS_VAL 0x2ae4
```

相关声明：[BT_UUID_GATT_CRCOORDS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8fa1863d2ae7b22462be097308fb5c81)。

GATT 色度坐标特征（GATT Characteristic Chromaticity Coordinates）的 UUID 值。

<a id="r_gac43c1fdab4869d79c423399c864f6088"></a>

```c
#define BT_UUID_GATT_CRCOORDS BT_UUID_DECLARE_16(BT_UUID_GATT_CRCOORDS_VAL)
```

相关声明：[BT_UUID_GATT_CRCOORDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac43c1fdab4869d79c423399c864f6088)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CRCOORDS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8fa1863d2ae7b22462be097308fb5c81)。

GATT 色度坐标特征（GATT Characteristic Chromaticity Coordinates）。

<a id="r_gac6ef845c60c6d68ad0c3269690e97d51"></a>

```c
#define BT_UUID_GATT_CRCCT_VAL 0x2ae5
```

相关声明：[BT_UUID_GATT_CRCCT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac6ef845c60c6d68ad0c3269690e97d51)。

GATT 以相关色温 CCT 和 Duv 值表示的色度特征（GATT Characteristic Chromaticity In CCT And Duv Values）的 UUID 值。

<a id="r_ga52a4a6bcb91935822f7e21fecbb283bc"></a>

```c
#define BT_UUID_GATT_CRCCT BT_UUID_DECLARE_16(BT_UUID_GATT_CRCCT_VAL)
```

相关声明：[BT_UUID_GATT_CRCCT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga52a4a6bcb91935822f7e21fecbb283bc)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CRCCT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac6ef845c60c6d68ad0c3269690e97d51)。

GATT 以相关色温 CCT 和 Duv 值表示的色度特征（GATT Characteristic Chromaticity In CCT And Duv Values）。

<a id="r_ga5d65027929bf31cdbdacc167c3f28951"></a>

```c
#define BT_UUID_GATT_CRT_VAL 0x2ae6
```

相关声明：[BT_UUID_GATT_CRT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5d65027929bf31cdbdacc167c3f28951)。

GATT 色度容差特征（GATT Characteristic Chromaticity Tolerance）的 UUID 值。

<a id="r_ga94c83c03f6cb240374af1bc4ec1b5f32"></a>

```c
#define BT_UUID_GATT_CRT BT_UUID_DECLARE_16(BT_UUID_GATT_CRT_VAL)
```

相关声明：[BT_UUID_GATT_CRT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga94c83c03f6cb240374af1bc4ec1b5f32)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CRT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5d65027929bf31cdbdacc167c3f28951)。

GATT 色度容差特征（GATT Characteristic Chromaticity Tolerance）。

<a id="r_ga361d00b8be7dc6c3d319a138bf5be1b9"></a>

```c
#define BT_UUID_GATT_CIEIDX_VAL 0x2ae7
```

相关声明：[BT_UUID_GATT_CIEIDX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga361d00b8be7dc6c3d319a138bf5be1b9)。

GATT CIE 13.3-1995 显色指数特征（GATT Characteristic CIE 13.3-1995 Color Rendering Index）的 UUID 值。

<a id="r_ga706f4f40760275742a9834d4b94cd1ed"></a>

```c
#define BT_UUID_GATT_CIEIDX BT_UUID_DECLARE_16(BT_UUID_GATT_CIEIDX_VAL)
```

相关声明：[BT_UUID_GATT_CIEIDX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga706f4f40760275742a9834d4b94cd1ed)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CIEIDX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga361d00b8be7dc6c3d319a138bf5be1b9)。

GATT CIE 13.3-1995 显色指数特征（GATT Characteristic CIE 13.3-1995 Color Rendering Index）。

<a id="r_ga298d1f0c9a48695488c7b211a7de66a9"></a>

```c
#define BT_UUID_GATT_COEFFICIENT_VAL 0x2ae8
```

相关声明：[BT_UUID_GATT_COEFFICIENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga298d1f0c9a48695488c7b211a7de66a9)。

GATT 系数特征（GATT Characteristic Coefficient）的 UUID 值。

<a id="r_ga941228f8812bfda85e86a15185a1270d"></a>

```c
#define BT_UUID_GATT_COEFFICIENT BT_UUID_DECLARE_16(BT_UUID_GATT_COEFFICIENT_VAL)
```

相关声明：[BT_UUID_GATT_COEFFICIENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga941228f8812bfda85e86a15185a1270d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_COEFFICIENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga298d1f0c9a48695488c7b211a7de66a9)。

GATT 系数特征（GATT Characteristic Coefficient）。

<a id="r_ga5533c28dc6bcaad3f66678d0e90a4e88"></a>

```c
#define BT_UUID_GATT_CCTEMP_VAL 0x2ae9
```

相关声明：[BT_UUID_GATT_CCTEMP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5533c28dc6bcaad3f66678d0e90a4e88)。

GATT 相关色温特征（GATT Characteristic Correlated Color Temperature）的 UUID 值。

<a id="r_ga2562158387beea244d57757e9e87422e"></a>

```c
#define BT_UUID_GATT_CCTEMP BT_UUID_DECLARE_16(BT_UUID_GATT_CCTEMP_VAL)
```

相关声明：[BT_UUID_GATT_CCTEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2562158387beea244d57757e9e87422e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CCTEMP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5533c28dc6bcaad3f66678d0e90a4e88)。

GATT 相关色温特征（GATT Characteristic Correlated Color Temperature）。

<a id="r_ga2c292a6bf086b695dce4c8a6fcb2e331"></a>

```c
#define BT_UUID_GATT_COUNT16_VAL 0x2aea
```

相关声明：[BT_UUID_GATT_COUNT16_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2c292a6bf086b695dce4c8a6fcb2e331)。

GATT 16 位计数特征（GATT Characteristic Count 16）的 UUID 值。

<a id="r_ga770c5a643468816820bdcc5db2af8d69"></a>

```c
#define BT_UUID_GATT_COUNT16 BT_UUID_DECLARE_16(BT_UUID_GATT_COUNT16_VAL)
```

相关声明：[BT_UUID_GATT_COUNT16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga770c5a643468816820bdcc5db2af8d69)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_COUNT16_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2c292a6bf086b695dce4c8a6fcb2e331)。

GATT 16 位计数特征（GATT Characteristic Count 16）。

<a id="r_ga360c3c084ac6f8f4ae6c0f8ddb1f2cf3"></a>

```c
#define BT_UUID_GATT_COUNT24_VAL 0x2aeb
```

相关声明：[BT_UUID_GATT_COUNT24_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga360c3c084ac6f8f4ae6c0f8ddb1f2cf3)。

GATT 24 位计数特征（GATT Characteristic Count 24）的 UUID 值。

<a id="r_ga7191613ab08efa46949ecb67d3512180"></a>

```c
#define BT_UUID_GATT_COUNT24 BT_UUID_DECLARE_16(BT_UUID_GATT_COUNT24_VAL)
```

相关声明：[BT_UUID_GATT_COUNT24](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7191613ab08efa46949ecb67d3512180)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_COUNT24_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga360c3c084ac6f8f4ae6c0f8ddb1f2cf3)。

GATT 24 位计数特征（GATT Characteristic Count 24）。

<a id="r_ga77981b5aad0c0424a08c0bbc86c5ca71"></a>

```c
#define BT_UUID_GATT_CNTRCODE_VAL 0x2aec
```

相关声明：[BT_UUID_GATT_CNTRCODE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga77981b5aad0c0424a08c0bbc86c5ca71)。

GATT 国家代码特征（GATT Characteristic Country Code）的 UUID 值。

<a id="r_gaf83aeabd260ea7d027aafa69beb2b050"></a>

```c
#define BT_UUID_GATT_CNTRCODE BT_UUID_DECLARE_16(BT_UUID_GATT_CNTRCODE_VAL)
```

相关声明：[BT_UUID_GATT_CNTRCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf83aeabd260ea7d027aafa69beb2b050)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CNTRCODE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga77981b5aad0c0424a08c0bbc86c5ca71)。

GATT 国家代码特征（GATT Characteristic Country Code）。

<a id="r_gad551c08d84b220342831bbb1d358efd6"></a>

```c
#define BT_UUID_GATT_DATEUTC_VAL 0x2aed
```

相关声明：[BT_UUID_GATT_DATEUTC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad551c08d84b220342831bbb1d358efd6)。

GATT UTC 日期特征（GATT Characteristic Date UTC）的 UUID 值。

<a id="r_ga4151cbfefc334f33800be8fdc853ca34"></a>

```c
#define BT_UUID_GATT_DATEUTC BT_UUID_DECLARE_16(BT_UUID_GATT_DATEUTC_VAL)
```

相关声明：[BT_UUID_GATT_DATEUTC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4151cbfefc334f33800be8fdc853ca34)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_DATEUTC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad551c08d84b220342831bbb1d358efd6)。

GATT UTC 日期特征（GATT Characteristic Date UTC）。

<a id="r_ga5ae0a7207e95f6aa2d982877057453d2"></a>

```c
#define BT_UUID_GATT_EC_VAL 0x2aee
```

相关声明：[BT_UUID_GATT_EC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5ae0a7207e95f6aa2d982877057453d2)。

GATT 电流特征（GATT Characteristic Electric Current）的 UUID 值。

<a id="r_ga9c86c847e1f2bb2deb23dbf4382b003f"></a>

```c
#define BT_UUID_GATT_EC BT_UUID_DECLARE_16(BT_UUID_GATT_EC_VAL)
```

相关声明：[BT_UUID_GATT_EC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9c86c847e1f2bb2deb23dbf4382b003f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_EC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5ae0a7207e95f6aa2d982877057453d2)。

GATT 电流特征（GATT Characteristic Electric Current）。

<a id="r_ga67e672df782986945ab3103c4ddff412"></a>

```c
#define BT_UUID_GATT_ECR_VAL 0x2aef
```

相关声明：[BT_UUID_GATT_ECR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga67e672df782986945ab3103c4ddff412)。

GATT 电流范围特征（GATT Characteristic Electric Current Range）的 UUID 值。

<a id="r_gac2121117e06e8d90448733b7e2ac9b97"></a>

```c
#define BT_UUID_GATT_ECR BT_UUID_DECLARE_16(BT_UUID_GATT_ECR_VAL)
```

相关声明：[BT_UUID_GATT_ECR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac2121117e06e8d90448733b7e2ac9b97)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ECR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga67e672df782986945ab3103c4ddff412)。

GATT 电流范围特征（GATT Characteristic Electric Current Range）。

<a id="r_gafd1eeaf887046c9f2785089a81275153"></a>

```c
#define BT_UUID_GATT_ECSPEC_VAL 0x2af0
```

相关声明：[BT_UUID_GATT_ECSPEC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafd1eeaf887046c9f2785089a81275153)。

GATT 电流规格特征（GATT Characteristic Electric Current Specification）的 UUID 值。

<a id="r_gaabdf693ada22d60cb524b501b3203b59"></a>

```c
#define BT_UUID_GATT_ECSPEC BT_UUID_DECLARE_16(BT_UUID_GATT_ECSPEC_VAL)
```

相关声明：[BT_UUID_GATT_ECSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaabdf693ada22d60cb524b501b3203b59)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ECSPEC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafd1eeaf887046c9f2785089a81275153)。

GATT 电流规格特征（GATT Characteristic Electric Current Specification）。

<a id="r_ga198d44bb45cf18921841e1788aeaa774"></a>

```c
#define BT_UUID_GATT_ECSTAT_VAL 0x2af1
```

相关声明：[BT_UUID_GATT_ECSTAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga198d44bb45cf18921841e1788aeaa774)。

GATT 电流统计特征（GATT Characteristic Electric Current Statistics）的 UUID 值。

<a id="r_ga6a1b29e07ffd6240e138c2a0ab1d6525"></a>

```c
#define BT_UUID_GATT_ECSTAT BT_UUID_DECLARE_16(BT_UUID_GATT_ECSTAT_VAL)
```

相关声明：[BT_UUID_GATT_ECSTAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6a1b29e07ffd6240e138c2a0ab1d6525)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ECSTAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga198d44bb45cf18921841e1788aeaa774)。

GATT 电流统计特征（GATT Characteristic Electric Current Statistics）。

<a id="r_gad6a61da207a152987afcad67fe4633d2"></a>

```c
#define BT_UUID_GATT_ENERGY_VAL 0x2af2
```

相关声明：[BT_UUID_GATT_ENERGY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad6a61da207a152987afcad67fe4633d2)。

GATT 能量特征（GATT Characteristic Energy）的 UUID 值。

<a id="r_ga556811cb737ddccf121dda3d65f2d79f"></a>

```c
#define BT_UUID_GATT_ENERGY BT_UUID_DECLARE_16(BT_UUID_GATT_ENERGY_VAL)
```

相关声明：[BT_UUID_GATT_ENERGY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga556811cb737ddccf121dda3d65f2d79f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ENERGY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad6a61da207a152987afcad67fe4633d2)。

GATT 能量特征（GATT Characteristic Energy）。

<a id="r_gab14d5fbaaa0e06c51db1cd41fcc368de"></a>

```c
#define BT_UUID_GATT_EPOD_VAL 0x2af3
```

相关声明：[BT_UUID_GATT_EPOD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab14d5fbaaa0e06c51db1cd41fcc368de)。

GATT 一天内某时段的能量特征（GATT Characteristic Energy In A Period Of Day）的 UUID 值。

<a id="r_ga2c5e6339a8d25083ce8656f02298cc57"></a>

```c
#define BT_UUID_GATT_EPOD BT_UUID_DECLARE_16(BT_UUID_GATT_EPOD_VAL)
```

相关声明：[BT_UUID_GATT_EPOD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2c5e6339a8d25083ce8656f02298cc57)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_EPOD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab14d5fbaaa0e06c51db1cd41fcc368de)。

GATT 一天内某时段的能量特征（GATT Characteristic Energy In A Period Of Day）。

<a id="r_gafec2c62ae00f7efb506341edf08b0d9a"></a>

```c
#define BT_UUID_GATT_EVTSTAT_VAL 0x2af4
```

相关声明：[BT_UUID_GATT_EVTSTAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafec2c62ae00f7efb506341edf08b0d9a)。

GATT 事件统计特征（GATT Characteristic Event Statistics）的 UUID 值。

<a id="r_gaa8f949e568dce7f639aeb80415674e2a"></a>

```c
#define BT_UUID_GATT_EVTSTAT BT_UUID_DECLARE_16(BT_UUID_GATT_EVTSTAT_VAL)
```

相关声明：[BT_UUID_GATT_EVTSTAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa8f949e568dce7f639aeb80415674e2a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_EVTSTAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafec2c62ae00f7efb506341edf08b0d9a)。

GATT 事件统计特征（GATT Characteristic Event Statistics）。

<a id="r_ga5d80019b1543d04e7cc5c7dc0f969c8c"></a>

```c
#define BT_UUID_GATT_FSTR16_VAL 0x2af5
```

相关声明：[BT_UUID_GATT_FSTR16_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5d80019b1543d04e7cc5c7dc0f969c8c)。

GATT 定长字符串 16 特征（GATT Characteristic Fixed String 16）的 UUID 值。

<a id="r_ga8970252d984fd463369baab7445f7bf6"></a>

```c
#define BT_UUID_GATT_FSTR16 BT_UUID_DECLARE_16(BT_UUID_GATT_FSTR16_VAL)
```

相关声明：[BT_UUID_GATT_FSTR16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8970252d984fd463369baab7445f7bf6)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_FSTR16_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5d80019b1543d04e7cc5c7dc0f969c8c)。

GATT 定长字符串 16 特征（GATT Characteristic Fixed String 16）。

<a id="r_gafa6970b19301bfc1c5f3dc6392850bd8"></a>

```c
#define BT_UUID_GATT_FSTR24_VAL 0x2af6
```

相关声明：[BT_UUID_GATT_FSTR24_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafa6970b19301bfc1c5f3dc6392850bd8)。

GATT 定长字符串 24 特征（GATT Characteristic Fixed String 24）的 UUID 值。

<a id="r_ga421bb2147cbf541fed439273ee5f2119"></a>

```c
#define BT_UUID_GATT_FSTR24 BT_UUID_DECLARE_16(BT_UUID_GATT_FSTR24_VAL)
```

相关声明：[BT_UUID_GATT_FSTR24](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga421bb2147cbf541fed439273ee5f2119)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_FSTR24_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafa6970b19301bfc1c5f3dc6392850bd8)。

GATT 定长字符串 24 特征（GATT Characteristic Fixed String 24）。

<a id="r_ga2b90639839a47260c7f555eec0b8bcd0"></a>

```c
#define BT_UUID_GATT_FSTR36_VAL 0x2af7
```

相关声明：[BT_UUID_GATT_FSTR36_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2b90639839a47260c7f555eec0b8bcd0)。

GATT 定长字符串 36 特征（GATT Characteristic Fixed String 36）的 UUID 值。

<a id="r_ga0a03f71c8d0b616f3a496efe4b5c6561"></a>

```c
#define BT_UUID_GATT_FSTR36 BT_UUID_DECLARE_16(BT_UUID_GATT_FSTR36_VAL)
```

相关声明：[BT_UUID_GATT_FSTR36](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0a03f71c8d0b616f3a496efe4b5c6561)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_FSTR36_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2b90639839a47260c7f555eec0b8bcd0)。

GATT 定长字符串 36 特征（GATT Characteristic Fixed String 36）。

<a id="r_gabafdb729c08aae0debace870f6043930"></a>

```c
#define BT_UUID_GATT_FSTR8_VAL 0x2af8
```

相关声明：[BT_UUID_GATT_FSTR8_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabafdb729c08aae0debace870f6043930)。

GATT 定长字符串 8 特征（GATT Characteristic Fixed String 8）的 UUID 值。

<a id="r_ga7b2a21e708cc13937038a3b88c0ad58b"></a>

```c
#define BT_UUID_GATT_FSTR8 BT_UUID_DECLARE_16(BT_UUID_GATT_FSTR8_VAL)
```

相关声明：[BT_UUID_GATT_FSTR8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7b2a21e708cc13937038a3b88c0ad58b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_FSTR8_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabafdb729c08aae0debace870f6043930)。

GATT 定长字符串 8 特征（GATT Characteristic Fixed String 8）。

<a id="r_ga18a4861ba81ae7f0a9ff0f1de37a6a0b"></a>

```c
#define BT_UUID_GATT_GENLVL_VAL 0x2af9
```

相关声明：[BT_UUID_GATT_GENLVL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga18a4861ba81ae7f0a9ff0f1de37a6a0b)。

GATT 通用等级特征（GATT Characteristic Generic Level）的 UUID 值。

<a id="r_ga7250c5f01251cf185035c18cf5d087c6"></a>

```c
#define BT_UUID_GATT_GENLVL BT_UUID_DECLARE_16(BT_UUID_GATT_GENLVL_VAL)
```

相关声明：[BT_UUID_GATT_GENLVL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7250c5f01251cf185035c18cf5d087c6)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_GENLVL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga18a4861ba81ae7f0a9ff0f1de37a6a0b)。

GATT 通用等级特征（GATT Characteristic Generic Level）。

<a id="r_ga1419411a928165a5cc4a26f0a97358d7"></a>

```c
#define BT_UUID_GATT_GTIN_VAL 0x2afa
```

相关声明：[BT_UUID_GATT_GTIN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1419411a928165a5cc4a26f0a97358d7)。

GATT 全球贸易项目代码特征（GATT Characteristic Global Trade Item Number）的 UUID 值。

<a id="r_ga27ef69db6e19c23b4f735bfbe2c83b7a"></a>

```c
#define BT_UUID_GATT_GTIN BT_UUID_DECLARE_16(BT_UUID_GATT_GTIN_VAL)
```

相关声明：[BT_UUID_GATT_GTIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga27ef69db6e19c23b4f735bfbe2c83b7a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_GTIN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1419411a928165a5cc4a26f0a97358d7)。

GATT 全球贸易项目代码特征（GATT Characteristic Global Trade Item Number）。

<a id="r_gaf660977f7494cecb5bd2d1d4808b0531"></a>

```c
#define BT_UUID_GATT_ILLUM_VAL 0x2afb
```

相关声明：[BT_UUID_GATT_ILLUM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf660977f7494cecb5bd2d1d4808b0531)。

GATT 照度特征（GATT Characteristic Illuminance）的 UUID 值。

<a id="r_gacb727e39a14240931183e4cc608f3114"></a>

```c
#define BT_UUID_GATT_ILLUM BT_UUID_DECLARE_16(BT_UUID_GATT_ILLUM_VAL)
```

相关声明：[BT_UUID_GATT_ILLUM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacb727e39a14240931183e4cc608f3114)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ILLUM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf660977f7494cecb5bd2d1d4808b0531)。

GATT 照度特征（GATT Characteristic Illuminance）。

<a id="r_ga742681175c952de8840c70df64b1562b"></a>

```c
#define BT_UUID_GATT_LUMEFF_VAL 0x2afc
```

相关声明：[BT_UUID_GATT_LUMEFF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga742681175c952de8840c70df64b1562b)。

GATT 光效特征（GATT Characteristic Luminous Efficacy）的 UUID 值。

<a id="r_ga3441cb7f9449be2ba9cc5cd73505f894"></a>

```c
#define BT_UUID_GATT_LUMEFF BT_UUID_DECLARE_16(BT_UUID_GATT_LUMEFF_VAL)
```

相关声明：[BT_UUID_GATT_LUMEFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3441cb7f9449be2ba9cc5cd73505f894)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LUMEFF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga742681175c952de8840c70df64b1562b)。

GATT 光效特征（GATT Characteristic Luminous Efficacy）。

<a id="r_gade0213130552d2757d74cdc2abe12d65"></a>

```c
#define BT_UUID_GATT_LUMNRG_VAL 0x2afd
```

相关声明：[BT_UUID_GATT_LUMNRG_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gade0213130552d2757d74cdc2abe12d65)。

GATT 光能特征（GATT Characteristic Luminous Energy）的 UUID 值。

<a id="r_gaa9ad315787bedcd20206b8dc99af4081"></a>

```c
#define BT_UUID_GATT_LUMNRG BT_UUID_DECLARE_16(BT_UUID_GATT_LUMNRG_VAL)
```

相关声明：[BT_UUID_GATT_LUMNRG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa9ad315787bedcd20206b8dc99af4081)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LUMNRG_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gade0213130552d2757d74cdc2abe12d65)。

GATT 光能特征（GATT Characteristic Luminous Energy）。

<a id="r_ga3f2d4a042fb00481383b7b5e8837f24e"></a>

```c
#define BT_UUID_GATT_LUMEXP_VAL 0x2afe
```

相关声明：[BT_UUID_GATT_LUMEXP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3f2d4a042fb00481383b7b5e8837f24e)。

GATT 光曝光量特征（GATT Characteristic Luminous Exposure）的 UUID 值。

<a id="r_ga38d3dd48f55ebfde06d52310324088d4"></a>

```c
#define BT_UUID_GATT_LUMEXP BT_UUID_DECLARE_16(BT_UUID_GATT_LUMEXP_VAL)
```

相关声明：[BT_UUID_GATT_LUMEXP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga38d3dd48f55ebfde06d52310324088d4)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LUMEXP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3f2d4a042fb00481383b7b5e8837f24e)。

GATT 光曝光量特征（GATT Characteristic Luminous Exposure）。

<a id="r_ga26f37ccbd862af70e5fa7516e59da73e"></a>

```c
#define BT_UUID_GATT_LUMFLX_VAL 0x2aff
```

相关声明：[BT_UUID_GATT_LUMFLX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga26f37ccbd862af70e5fa7516e59da73e)。

GATT 光通量特征（GATT Characteristic Luminous Flux）的 UUID 值。

<a id="r_gae05c06b201217e919c8493d3245b2f52"></a>

```c
#define BT_UUID_GATT_LUMFLX BT_UUID_DECLARE_16(BT_UUID_GATT_LUMFLX_VAL)
```

相关声明：[BT_UUID_GATT_LUMFLX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae05c06b201217e919c8493d3245b2f52)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LUMFLX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga26f37ccbd862af70e5fa7516e59da73e)。

GATT 光通量特征（GATT Characteristic Luminous Flux）。

<a id="r_gab1080ef3dffbc5521c8f587766ac22d6"></a>

```c
#define BT_UUID_GATT_LUMFLXR_VAL 0x2b00
```

相关声明：[BT_UUID_GATT_LUMFLXR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab1080ef3dffbc5521c8f587766ac22d6)。

GATT 光通量范围特征（GATT Characteristic Luminous Flux Range）的 UUID 值。

<a id="r_ga93a7fa9b6c9bbd12ef5d9a7169405e59"></a>

```c
#define BT_UUID_GATT_LUMFLXR BT_UUID_DECLARE_16(BT_UUID_GATT_LUMFLXR_VAL)
```

相关声明：[BT_UUID_GATT_LUMFLXR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga93a7fa9b6c9bbd12ef5d9a7169405e59)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LUMFLXR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab1080ef3dffbc5521c8f587766ac22d6)。

GATT 光通量范围特征（GATT Characteristic Luminous Flux Range）。

<a id="r_ga00cfabe28348d7a86a54608b8f0ec3de"></a>

```c
#define BT_UUID_GATT_LUMINT_VAL 0x2b01
```

相关声明：[BT_UUID_GATT_LUMINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga00cfabe28348d7a86a54608b8f0ec3de)。

GATT 发光强度特征（GATT Characteristic Luminous Intensity）的 UUID 值。

<a id="r_gaefd8b48d82a4c403e735badb04e812b4"></a>

```c
#define BT_UUID_GATT_LUMINT BT_UUID_DECLARE_16(BT_UUID_GATT_LUMINT_VAL)
```

相关声明：[BT_UUID_GATT_LUMINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaefd8b48d82a4c403e735badb04e812b4)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LUMINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga00cfabe28348d7a86a54608b8f0ec3de)。

GATT 发光强度特征（GATT Characteristic Luminous Intensity）。

<a id="r_ga23f13789b3f3f19691dbfdc3a33a506e"></a>

```c
#define BT_UUID_GATT_MASSFLOW_VAL 0x2b02
```

相关声明：[BT_UUID_GATT_MASSFLOW_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga23f13789b3f3f19691dbfdc3a33a506e)。

GATT 质量流量特征（GATT Characteristic Mass Flow）的 UUID 值。

<a id="r_ga8670491866b6b62a3834c4f619612a7d"></a>

```c
#define BT_UUID_GATT_MASSFLOW BT_UUID_DECLARE_16(BT_UUID_GATT_MASSFLOW_VAL)
```

相关声明：[BT_UUID_GATT_MASSFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8670491866b6b62a3834c4f619612a7d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_MASSFLOW_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga23f13789b3f3f19691dbfdc3a33a506e)。

GATT 质量流量特征（GATT Characteristic Mass Flow）。

<a id="r_ga4b8ec7d1538e6655b065a488d8c523af"></a>

```c
#define BT_UUID_GATT_PERLGHT_VAL 0x2b03
```

相关声明：[BT_UUID_GATT_PERLGHT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4b8ec7d1538e6655b065a488d8c523af)。

GATT 感知明度特征（GATT Characteristic Perceived Lightness）的 UUID 值。

<a id="r_ga0f13aca1a13cc11b7e1adf7c1f7e75b1"></a>

```c
#define BT_UUID_GATT_PERLGHT BT_UUID_DECLARE_16(BT_UUID_GATT_PERLGHT_VAL)
```

相关声明：[BT_UUID_GATT_PERLGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0f13aca1a13cc11b7e1adf7c1f7e75b1)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_PERLGHT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4b8ec7d1538e6655b065a488d8c523af)。

GATT 感知明度特征（GATT Characteristic Perceived Lightness）。

<a id="r_ga4bc9aee30308246d28eb96152eb686b1"></a>

```c
#define BT_UUID_GATT_PER8_VAL 0x2b04
```

相关声明：[BT_UUID_GATT_PER8_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4bc9aee30308246d28eb96152eb686b1)。

GATT 8 位百分比特征（GATT Characteristic Percentage 8）的 UUID 值。

<a id="r_ga60ea8b576b1d3951be45cb928ce841b0"></a>

```c
#define BT_UUID_GATT_PER8 BT_UUID_DECLARE_16(BT_UUID_GATT_PER8_VAL)
```

相关声明：[BT_UUID_GATT_PER8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga60ea8b576b1d3951be45cb928ce841b0)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_PER8_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4bc9aee30308246d28eb96152eb686b1)。

GATT 8 位百分比特征（GATT Characteristic Percentage 8）。

<a id="r_gac70e24a9a91738c615e83e6238c96ed7"></a>

```c
#define BT_UUID_GATT_PWR_VAL 0x2b05
```

相关声明：[BT_UUID_GATT_PWR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac70e24a9a91738c615e83e6238c96ed7)。

GATT 功率特征（GATT Characteristic Power）的 UUID 值。

<a id="r_gaa374060d2715bfab9986c1eee2467ed5"></a>

```c
#define BT_UUID_GATT_PWR BT_UUID_DECLARE_16(BT_UUID_GATT_PWR_VAL)
```

相关声明：[BT_UUID_GATT_PWR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa374060d2715bfab9986c1eee2467ed5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_PWR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac70e24a9a91738c615e83e6238c96ed7)。

GATT 功率特征（GATT Characteristic Power）。

<a id="r_ga3db91205384fb559aa9f8865c15356d1"></a>

```c
#define BT_UUID_GATT_PWRSPEC_VAL 0x2b06
```

相关声明：[BT_UUID_GATT_PWRSPEC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3db91205384fb559aa9f8865c15356d1)。

GATT 功率规格特征（GATT Characteristic Power Specification）的 UUID 值。

<a id="r_gad69a1f73335555e9a7c164ebd2474371"></a>

```c
#define BT_UUID_GATT_PWRSPEC BT_UUID_DECLARE_16(BT_UUID_GATT_PWRSPEC_VAL)
```

相关声明：[BT_UUID_GATT_PWRSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad69a1f73335555e9a7c164ebd2474371)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_PWRSPEC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3db91205384fb559aa9f8865c15356d1)。

GATT 功率规格特征（GATT Characteristic Power Specification）。

<a id="r_gac5533a77612f300dd8f1cd8ccd2ee522"></a>

```c
#define BT_UUID_GATT_RRICR_VAL 0x2b07
```

相关声明：[BT_UUID_GATT_RRICR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac5533a77612f300dd8f1cd8ccd2ee522)。

GATT 电流范围内相对运行时间特征（GATT Characteristic Relative Runtime In A Current Range）的 UUID 值。

<a id="r_ga7c3534f8bd7b9c662e73cd9d46dc8c79"></a>

```c
#define BT_UUID_GATT_RRICR BT_UUID_DECLARE_16(BT_UUID_GATT_RRICR_VAL)
```

相关声明：[BT_UUID_GATT_RRICR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7c3534f8bd7b9c662e73cd9d46dc8c79)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_RRICR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac5533a77612f300dd8f1cd8ccd2ee522)。

GATT 电流范围内相对运行时间特征（GATT Characteristic Relative Runtime In A Current Range）。

<a id="r_ga41b95788eb3271a8fe87766fe903e8d9"></a>

```c
#define BT_UUID_GATT_RRIGLR_VAL 0x2b08
```

相关声明：[BT_UUID_GATT_RRIGLR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga41b95788eb3271a8fe87766fe903e8d9)。

GATT 通用等级范围内相对运行时间特征（GATT Characteristic Relative Runtime In A Generic Level Range）的 UUID 值。

<a id="r_ga2e1c29cac1ece5f3fad29c61ed2b0aa4"></a>

```c
#define BT_UUID_GATT_RRIGLR BT_UUID_DECLARE_16(BT_UUID_GATT_RRIGLR_VAL)
```

相关声明：[BT_UUID_GATT_RRIGLR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2e1c29cac1ece5f3fad29c61ed2b0aa4)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_RRIGLR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga41b95788eb3271a8fe87766fe903e8d9)。

GATT 通用等级范围内相对运行时间特征（GATT Characteristic Relative Runtime In A Generic Level Range）。

<a id="r_gac3bb5af173f013c8a49227b2920bc107"></a>

```c
#define BT_UUID_GATT_RVIVR_VAL 0x2b09
```

相关声明：[BT_UUID_GATT_RVIVR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3bb5af173f013c8a49227b2920bc107)。

GATT 电压范围内相对值特征（GATT Characteristic Relative Value In A Voltage Range）的 UUID 值。

<a id="r_gaac802734c88aac862fcab0599cb2e216"></a>

```c
#define BT_UUID_GATT_RVIVR BT_UUID_DECLARE_16(BT_UUID_GATT_RVIVR_VAL)
```

相关声明：[BT_UUID_GATT_RVIVR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaac802734c88aac862fcab0599cb2e216)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_RVIVR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3bb5af173f013c8a49227b2920bc107)。

GATT 电压范围内相对值特征（GATT Characteristic Relative Value In A Voltage Range）。

<a id="r_ga2866d911411268e5026ef729efa990e9"></a>

```c
#define BT_UUID_GATT_RVIIR_VAL 0x2b0a
```

相关声明：[BT_UUID_GATT_RVIIR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2866d911411268e5026ef729efa990e9)。

GATT 照度范围内相对值特征（GATT Characteristic Relative Value In A Illuminance Range）的 UUID 值。

<a id="r_ga165f79f1dcde1e7359a4c4602dc88c40"></a>

```c
#define BT_UUID_GATT_RVIIR BT_UUID_DECLARE_16(BT_UUID_GATT_RVIIR_VAL)
```

相关声明：[BT_UUID_GATT_RVIIR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga165f79f1dcde1e7359a4c4602dc88c40)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_RVIIR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2866d911411268e5026ef729efa990e9)。

GATT 照度范围内相对值特征（GATT Characteristic Relative Value In A Illuminance Range）。

<a id="r_gab73b24f9941a80fab6423ff85f68aae6"></a>

```c
#define BT_UUID_GATT_RVIPOD_VAL 0x2b0b
```

相关声明：[BT_UUID_GATT_RVIPOD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab73b24f9941a80fab6423ff85f68aae6)。

GATT 一天内某时段的相对值特征（GATT Characteristic Relative Value In A Period Of Day）的 UUID 值。

<a id="r_ga9e6b0e6585f2ceb62dd236a0ae3afc6a"></a>

```c
#define BT_UUID_GATT_RVIPOD BT_UUID_DECLARE_16(BT_UUID_GATT_RVIPOD_VAL)
```

相关声明：[BT_UUID_GATT_RVIPOD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9e6b0e6585f2ceb62dd236a0ae3afc6a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_RVIPOD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab73b24f9941a80fab6423ff85f68aae6)。

GATT 一天内某时段的相对值特征（GATT Characteristic Relative Value In A Period Of Day）。

<a id="r_gaac84e4bcae1a1b83af9124688e01912a"></a>

```c
#define BT_UUID_GATT_RVITR_VAL 0x2b0c
```

相关声明：[BT_UUID_GATT_RVITR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaac84e4bcae1a1b83af9124688e01912a)。

GATT 温度范围内相对值特征（GATT Characteristic Relative Value In A Temperature Range）的 UUID 值。

<a id="r_ga8c8e5e43e2bc8f7c26344fff4127e039"></a>

```c
#define BT_UUID_GATT_RVITR BT_UUID_DECLARE_16(BT_UUID_GATT_RVITR_VAL)
```

相关声明：[BT_UUID_GATT_RVITR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8c8e5e43e2bc8f7c26344fff4127e039)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_RVITR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaac84e4bcae1a1b83af9124688e01912a)。

GATT 温度范围内相对值特征（GATT Characteristic Relative Value In A Temperature Range）。

<a id="r_gaa7a119bfd7df636f0ed0bf515232e6bb"></a>

```c
#define BT_UUID_GATT_TEMP8_VAL 0x2b0d
```

相关声明：[BT_UUID_GATT_TEMP8_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa7a119bfd7df636f0ed0bf515232e6bb)。

GATT 8 位温度特征（GATT Characteristic Temperature 8）的 UUID 值。

<a id="r_ga146d14e283686a5712c90698fd6a64ad"></a>

```c
#define BT_UUID_GATT_TEMP8 BT_UUID_DECLARE_16(BT_UUID_GATT_TEMP8_VAL)
```

相关声明：[BT_UUID_GATT_TEMP8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga146d14e283686a5712c90698fd6a64ad)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TEMP8_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa7a119bfd7df636f0ed0bf515232e6bb)。

GATT 8 位温度特征（GATT Characteristic Temperature 8）。

<a id="r_ga616708b903a88a6bb9eabdae60813063"></a>

```c
#define BT_UUID_GATT_TEMP8_IPOD_VAL 0x2b0e
```

相关声明：[BT_UUID_GATT_TEMP8_IPOD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga616708b903a88a6bb9eabdae60813063)。

GATT 一天内某时段的 8 位温度特征（GATT Characteristic Temperature 8 In A Period Of Day）的 UUID 值。

<a id="r_ga3d28ebdcaa93ed4ccdee512f7ddd979a"></a>

```c
#define BT_UUID_GATT_TEMP8_IPOD BT_UUID_DECLARE_16(BT_UUID_GATT_TEMP8_IPOD_VAL)
```

相关声明：[BT_UUID_GATT_TEMP8_IPOD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3d28ebdcaa93ed4ccdee512f7ddd979a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TEMP8_IPOD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga616708b903a88a6bb9eabdae60813063)。

GATT 一天内某时段的 8 位温度特征（GATT Characteristic Temperature 8 In A Period Of Day）。

<a id="r_ga3d54ad101d044924da30aa81a6b64111"></a>

```c
#define BT_UUID_GATT_TEMP8_STAT_VAL 0x2b0f
```

相关声明：[BT_UUID_GATT_TEMP8_STAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3d54ad101d044924da30aa81a6b64111)。

GATT 8 位温度统计特征（GATT Characteristic Temperature 8 Statistics）的 UUID 值。

<a id="r_ga071d32c5e9dd24fc179f8cac531e499f"></a>

```c
#define BT_UUID_GATT_TEMP8_STAT BT_UUID_DECLARE_16(BT_UUID_GATT_TEMP8_STAT_VAL)
```

相关声明：[BT_UUID_GATT_TEMP8_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga071d32c5e9dd24fc179f8cac531e499f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TEMP8_STAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3d54ad101d044924da30aa81a6b64111)。

GATT 8 位温度统计特征（GATT Characteristic Temperature 8 Statistics）。

<a id="r_gadcdd9e4d2cfa09f6d766b513224ef7bf"></a>

```c
#define BT_UUID_GATT_TEMP_RNG_VAL 0x2b10
```

相关声明：[BT_UUID_GATT_TEMP_RNG_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadcdd9e4d2cfa09f6d766b513224ef7bf)。

GATT 温度范围特征（GATT Characteristic Temperature Range）的 UUID 值。

<a id="r_ga99e73003bde4dac095f198dd7045b297"></a>

```c
#define BT_UUID_GATT_TEMP_RNG BT_UUID_DECLARE_16(BT_UUID_GATT_TEMP_RNG_VAL)
```

相关声明：[BT_UUID_GATT_TEMP_RNG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga99e73003bde4dac095f198dd7045b297)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TEMP_RNG_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadcdd9e4d2cfa09f6d766b513224ef7bf)。

GATT 温度范围特征（GATT Characteristic Temperature Range）。

<a id="r_ga035eaed3f130c2222236fdc194f9b1a4"></a>

```c
#define BT_UUID_GATT_TEMP_STAT_VAL 0x2b11
```

相关声明：[BT_UUID_GATT_TEMP_STAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga035eaed3f130c2222236fdc194f9b1a4)。

GATT 温度统计特征（GATT Characteristic Temperature Statistics）的 UUID 值。

<a id="r_ga8ae19f54cd4aa1c7ab42c48f33080f52"></a>

```c
#define BT_UUID_GATT_TEMP_STAT BT_UUID_DECLARE_16(BT_UUID_GATT_TEMP_STAT_VAL)
```

相关声明：[BT_UUID_GATT_TEMP_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8ae19f54cd4aa1c7ab42c48f33080f52)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TEMP_STAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga035eaed3f130c2222236fdc194f9b1a4)。

GATT 温度统计特征（GATT Characteristic Temperature Statistics）。

<a id="r_gae5f1cda9dbc55f77cfbb4c00f4e359f0"></a>

```c
#define BT_UUID_GATT_TIM_DC8_VAL 0x2b12
```

相关声明：[BT_UUID_GATT_TIM_DC8_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae5f1cda9dbc55f77cfbb4c00f4e359f0)。

GATT 8 位十分之一小时时间特征（GATT Characteristic Time Decihour 8）的 UUID 值。

<a id="r_gae9feb929d7a7eb67dc1db02ce26cc82b"></a>

```c
#define BT_UUID_GATT_TIM_DC8 BT_UUID_DECLARE_16(BT_UUID_GATT_TIM_DC8_VAL)
```

相关声明：[BT_UUID_GATT_TIM_DC8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae9feb929d7a7eb67dc1db02ce26cc82b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TIM_DC8_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae5f1cda9dbc55f77cfbb4c00f4e359f0)。

GATT 8 位十分之一小时时间特征（GATT Characteristic Time Decihour 8）。

<a id="r_ga07a0510f652506225410b1865882d1ea"></a>

```c
#define BT_UUID_GATT_TIM_EXP8_VAL 0x2b13
```

相关声明：[BT_UUID_GATT_TIM_EXP8_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga07a0510f652506225410b1865882d1ea)。

GATT 8 位指数表示时间特征（GATT Characteristic Time Exponential 8）的 UUID 值。

<a id="r_ga5e4aee6898f1ab1f8065c113241c99bd"></a>

```c
#define BT_UUID_GATT_TIM_EXP8 BT_UUID_DECLARE_16(BT_UUID_GATT_TIM_EXP8_VAL)
```

相关声明：[BT_UUID_GATT_TIM_EXP8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5e4aee6898f1ab1f8065c113241c99bd)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TIM_EXP8_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga07a0510f652506225410b1865882d1ea)。

GATT 8 位指数表示时间特征（GATT Characteristic Time Exponential 8）。

<a id="r_ga272a11fc6d56e685243f6507708f8032"></a>

```c
#define BT_UUID_GATT_TIM_H24_VAL 0x2b14
```

相关声明：[BT_UUID_GATT_TIM_H24_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga272a11fc6d56e685243f6507708f8032)。

GATT 24 位小时时间特征（GATT Characteristic Time Hour 24）的 UUID 值。

<a id="r_gac209c86c368f2ed7c20bae2b90f36a0a"></a>

```c
#define BT_UUID_GATT_TIM_H24 BT_UUID_DECLARE_16(BT_UUID_GATT_TIM_H24_VAL)
```

相关声明：[BT_UUID_GATT_TIM_H24](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac209c86c368f2ed7c20bae2b90f36a0a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TIM_H24_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga272a11fc6d56e685243f6507708f8032)。

GATT 24 位小时时间特征（GATT Characteristic Time Hour 24）。

<a id="r_ga181a187356797362b4a7d9a7d22f7fdc"></a>

```c
#define BT_UUID_GATT_TIM_MS24_VAL 0x2b15
```

相关声明：[BT_UUID_GATT_TIM_MS24_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga181a187356797362b4a7d9a7d22f7fdc)。

GATT 24 位毫秒时间特征（GATT Characteristic Time Millisecond 24）的 UUID 值。

<a id="r_ga941191900854cfed39dae2b5dfba499b"></a>

```c
#define BT_UUID_GATT_TIM_MS24 BT_UUID_DECLARE_16(BT_UUID_GATT_TIM_MS24_VAL)
```

相关声明：[BT_UUID_GATT_TIM_MS24](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga941191900854cfed39dae2b5dfba499b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TIM_MS24_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga181a187356797362b4a7d9a7d22f7fdc)。

GATT 24 位毫秒时间特征（GATT Characteristic Time Millisecond 24）。

<a id="r_ga2ad71e9a1912c84f31072edcf3234093"></a>

```c
#define BT_UUID_GATT_TIM_S16_VAL 0x2b16
```

相关声明：[BT_UUID_GATT_TIM_S16_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2ad71e9a1912c84f31072edcf3234093)。

GATT 16 位秒时间特征（GATT Characteristic Time Second 16）的 UUID 值。

<a id="r_ga216c5c11e143571c5b40e7554c40ab91"></a>

```c
#define BT_UUID_GATT_TIM_S16 BT_UUID_DECLARE_16(BT_UUID_GATT_TIM_S16_VAL)
```

相关声明：[BT_UUID_GATT_TIM_S16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga216c5c11e143571c5b40e7554c40ab91)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TIM_S16_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2ad71e9a1912c84f31072edcf3234093)。

GATT 16 位秒时间特征（GATT Characteristic Time Second 16）。

<a id="r_gae7ad9e90132e56a59d3fb3cfaea55faa"></a>

```c
#define BT_UUID_GATT_TIM_S8_VAL 0x2b17
```

相关声明：[BT_UUID_GATT_TIM_S8_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae7ad9e90132e56a59d3fb3cfaea55faa)。

GATT 8 位秒时间特征（GATT Characteristic Time Second 8）的 UUID 值。

<a id="r_gacf36b122fdeb96d6da4b710506118668"></a>

```c
#define BT_UUID_GATT_TIM_S8 BT_UUID_DECLARE_16(BT_UUID_GATT_TIM_S8_VAL)
```

相关声明：[BT_UUID_GATT_TIM_S8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacf36b122fdeb96d6da4b710506118668)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TIM_S8_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae7ad9e90132e56a59d3fb3cfaea55faa)。

GATT 8 位秒时间特征（GATT Characteristic Time Second 8）。

<a id="r_gae727674510a76ca337ea57c4222791ab"></a>

```c
#define BT_UUID_GATT_V_VAL 0x2b18
```

相关声明：[BT_UUID_GATT_V_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae727674510a76ca337ea57c4222791ab)。

GATT 电压特征（GATT Characteristic Voltage）的 UUID 值。

<a id="r_ga1cedb6e5b998d0edf435dd4203fee96c"></a>

```c
#define BT_UUID_GATT_V BT_UUID_DECLARE_16(BT_UUID_GATT_V_VAL)
```

相关声明：[BT_UUID_GATT_V](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1cedb6e5b998d0edf435dd4203fee96c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_V_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae727674510a76ca337ea57c4222791ab)。

GATT 电压特征（GATT Characteristic Voltage）。

<a id="r_ga5bc426767e92938654f24f0158a16b53"></a>

```c
#define BT_UUID_GATT_V_SPEC_VAL 0x2b19
```

相关声明：[BT_UUID_GATT_V_SPEC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5bc426767e92938654f24f0158a16b53)。

GATT 电压规格特征（GATT Characteristic Voltage Specification）的 UUID 值。

<a id="r_ga23440a5aff26bf0a737d4a48b6ce301d"></a>

```c
#define BT_UUID_GATT_V_SPEC BT_UUID_DECLARE_16(BT_UUID_GATT_V_SPEC_VAL)
```

相关声明：[BT_UUID_GATT_V_SPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga23440a5aff26bf0a737d4a48b6ce301d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_V_SPEC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5bc426767e92938654f24f0158a16b53)。

GATT 电压规格特征（GATT Characteristic Voltage Specification）。

<a id="r_gac655949e3c565b8835b099a93a24498f"></a>

```c
#define BT_UUID_GATT_V_STAT_VAL 0x2b1a
```

相关声明：[BT_UUID_GATT_V_STAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac655949e3c565b8835b099a93a24498f)。

GATT 电压统计特征（GATT Characteristic Voltage Statistics）的 UUID 值。

<a id="r_gac1d74460417a592cbd4f5b6528c77e28"></a>

```c
#define BT_UUID_GATT_V_STAT BT_UUID_DECLARE_16(BT_UUID_GATT_V_STAT_VAL)
```

相关声明：[BT_UUID_GATT_V_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac1d74460417a592cbd4f5b6528c77e28)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_V_STAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac655949e3c565b8835b099a93a24498f)。

GATT 电压统计特征（GATT Characteristic Voltage Statistics）。

<a id="r_gae37019af7703f5b3abb99bcfbb1d5343"></a>

```c
#define BT_UUID_GATT_VOLF_VAL 0x2b1b
```

相关声明：[BT_UUID_GATT_VOLF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae37019af7703f5b3abb99bcfbb1d5343)。

GATT 体积流量特征（GATT Characteristic Volume Flow）的 UUID 值。

<a id="r_ga8ddcea2b365f55ac647562063ede0f3c"></a>

```c
#define BT_UUID_GATT_VOLF BT_UUID_DECLARE_16(BT_UUID_GATT_VOLF_VAL)
```

相关声明：[BT_UUID_GATT_VOLF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8ddcea2b365f55ac647562063ede0f3c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_VOLF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae37019af7703f5b3abb99bcfbb1d5343)。

GATT 体积流量特征（GATT Characteristic Volume Flow）。

<a id="r_gaf7b547b7f4c6908f601afc33d0d0ebb8"></a>

```c
#define BT_UUID_GATT_CRCOORD_VAL 0x2b1c
```

相关声明：[BT_UUID_GATT_CRCOORD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf7b547b7f4c6908f601afc33d0d0ebb8)。

GATT 色度坐标特征，使用单数 Coordinate 而非复数 Coordinates（GATT Characteristic Chromaticity Coordinate (not Coordinates)）的 UUID 值。

<a id="r_ga53a898269a7f5ab84e9853521f69bc69"></a>

```c
#define BT_UUID_GATT_CRCOORD BT_UUID_DECLARE_16(BT_UUID_GATT_CRCOORD_VAL)
```

相关声明：[BT_UUID_GATT_CRCOORD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga53a898269a7f5ab84e9853521f69bc69)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CRCOORD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf7b547b7f4c6908f601afc33d0d0ebb8)。

GATT 色度坐标特征，使用单数 Coordinate 而非复数 Coordinates（GATT Characteristic Chromaticity Coordinate (not Coordinates)）。

<a id="r_ga8b2d587922902479e47bd316443e0a56"></a>

```c
#define BT_UUID_GATT_RCF_VAL 0x2b1d
```

相关声明：[BT_UUID_GATT_RCF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8b2d587922902479e47bd316443e0a56)。

GATT 重连接配置 RC 功能特征（GATT Characteristic RC Feature）的 UUID 值。

<a id="r_gac6961922da80f8c628a35b8855cb788b"></a>

```c
#define BT_UUID_GATT_RCF BT_UUID_DECLARE_16(BT_UUID_GATT_RCF_VAL)
```

相关声明：[BT_UUID_GATT_RCF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac6961922da80f8c628a35b8855cb788b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_RCF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8b2d587922902479e47bd316443e0a56)。

GATT 重连接配置 RC 功能特征（GATT Characteristic RC Feature）。

<a id="r_ga47316949dd2eb5571e3b94240a4e6c90"></a>

```c
#define BT_UUID_GATT_RCSET_VAL 0x2b1e
```

相关声明：[BT_UUID_GATT_RCSET_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga47316949dd2eb5571e3b94240a4e6c90)。

GATT 重连接配置 RC 设置特征（GATT Characteristic RC Settings）的 UUID 值。

<a id="r_ga2af1f07e6e4484476740db5bb6b31b8f"></a>

```c
#define BT_UUID_GATT_RCSET BT_UUID_DECLARE_16(BT_UUID_GATT_RCSET_VAL)
```

相关声明：[BT_UUID_GATT_RCSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2af1f07e6e4484476740db5bb6b31b8f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_RCSET_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga47316949dd2eb5571e3b94240a4e6c90)。

GATT 重连接配置 RC 设置特征（GATT Characteristic RC Settings）。

<a id="r_gaabe52b93d5ac1e72c468be08fdea35ef"></a>

```c
#define BT_UUID_GATT_RCCP_VAL 0x2b1f
```

相关声明：[BT_UUID_GATT_RCCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaabe52b93d5ac1e72c468be08fdea35ef)。

GATT 重连接配置控制点特征（GATT Characteristic Reconnection Configuration Control Point）的 UUID 值。

<a id="r_ga48b7a42b204407553262ea68e53f65d7"></a>

```c
#define BT_UUID_GATT_RCCP BT_UUID_DECLARE_16(BT_UUID_GATT_RCCP_VAL)
```

相关声明：[BT_UUID_GATT_RCCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga48b7a42b204407553262ea68e53f65d7)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_RCCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaabe52b93d5ac1e72c468be08fdea35ef)。

GATT 重连接配置控制点特征（GATT Characteristic Reconnection Configuration Control Point）。

<a id="r_gadc4e7dcda6314aa68b4165199ddc4123"></a>

```c
#define BT_UUID_GATT_IDD_SC_VAL 0x2b20
```

相关声明：[BT_UUID_GATT_IDD_SC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadc4e7dcda6314aa68b4165199ddc4123)。

GATT 胰岛素输注设备 IDD 状态已变更特征（GATT Characteristic IDD Status Changed）的 UUID 值。

<a id="r_gab36f1fff60a7657844985841bb0350f8"></a>

```c
#define BT_UUID_GATT_IDD_SC BT_UUID_DECLARE_16(BT_UUID_GATT_IDD_SC_VAL)
```

相关声明：[BT_UUID_GATT_IDD_SC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab36f1fff60a7657844985841bb0350f8)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_IDD_SC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadc4e7dcda6314aa68b4165199ddc4123)。

GATT 胰岛素输注设备 IDD 状态已变更特征（GATT Characteristic IDD Status Changed）。

<a id="r_gafb1511371c0c19323989961689425d08"></a>

```c
#define BT_UUID_GATT_IDD_S_VAL 0x2b21
```

相关声明：[BT_UUID_GATT_IDD_S_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafb1511371c0c19323989961689425d08)。

GATT 胰岛素输注设备 IDD 状态特征（GATT Characteristic IDD Status）的 UUID 值。

<a id="r_ga560d7cef69190752eb8a5c4f6fed5989"></a>

```c
#define BT_UUID_GATT_IDD_S BT_UUID_DECLARE_16(BT_UUID_GATT_IDD_S_VAL)
```

相关声明：[BT_UUID_GATT_IDD_S](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga560d7cef69190752eb8a5c4f6fed5989)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_IDD_S_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafb1511371c0c19323989961689425d08)。

GATT 胰岛素输注设备 IDD 状态特征（GATT Characteristic IDD Status）。

<a id="r_ga2e854242941b30552241e1ee3669d669"></a>

```c
#define BT_UUID_GATT_IDD_AS_VAL 0x2b22
```

相关声明：[BT_UUID_GATT_IDD_AS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2e854242941b30552241e1ee3669d669)。

GATT 胰岛素输注设备 IDD 通报状态特征（GATT Characteristic IDD Annunciation Status）的 UUID 值。

<a id="r_ga980781b7142c177ed46b8caca9b8b518"></a>

```c
#define BT_UUID_GATT_IDD_AS BT_UUID_DECLARE_16(BT_UUID_GATT_IDD_AS_VAL)
```

相关声明：[BT_UUID_GATT_IDD_AS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga980781b7142c177ed46b8caca9b8b518)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_IDD_AS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2e854242941b30552241e1ee3669d669)。

GATT 胰岛素输注设备 IDD 通报状态特征（GATT Characteristic IDD Annunciation Status）。

<a id="r_ga7d20cc62ad420b71d299361430005d27"></a>

```c
#define BT_UUID_GATT_IDD_F_VAL 0x2b23
```

相关声明：[BT_UUID_GATT_IDD_F_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7d20cc62ad420b71d299361430005d27)。

GATT 胰岛素输注设备 IDD 功能特征（GATT Characteristic IDD Features）的 UUID 值。

<a id="r_ga369b0b1ddac085d2812a42f737bdd594"></a>

```c
#define BT_UUID_GATT_IDD_F BT_UUID_DECLARE_16(BT_UUID_GATT_IDD_F_VAL)
```

相关声明：[BT_UUID_GATT_IDD_F](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga369b0b1ddac085d2812a42f737bdd594)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_IDD_F_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7d20cc62ad420b71d299361430005d27)。

GATT 胰岛素输注设备 IDD 功能特征（GATT Characteristic IDD Features）。

<a id="r_ga1e817e253f29e03a98327e08c2048e6b"></a>

```c
#define BT_UUID_GATT_IDD_SRCP_VAL 0x2b24
```

相关声明：[BT_UUID_GATT_IDD_SRCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1e817e253f29e03a98327e08c2048e6b)。

GATT 胰岛素输注设备 IDD 状态读取控制点特征（GATT Characteristic IDD Status Reader Control Point）的 UUID 值。

<a id="r_ga13d829bfcacb036a2271cd09491c1578"></a>

```c
#define BT_UUID_GATT_IDD_SRCP BT_UUID_DECLARE_16(BT_UUID_GATT_IDD_SRCP_VAL)
```

相关声明：[BT_UUID_GATT_IDD_SRCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga13d829bfcacb036a2271cd09491c1578)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_IDD_SRCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1e817e253f29e03a98327e08c2048e6b)。

GATT 胰岛素输注设备 IDD 状态读取控制点特征（GATT Characteristic IDD Status Reader Control Point）。

<a id="r_ga1dc738c5c564bf05d3c2669a79db6e17"></a>

```c
#define BT_UUID_GATT_IDD_CCP_VAL 0x2b25
```

相关声明：[BT_UUID_GATT_IDD_CCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1dc738c5c564bf05d3c2669a79db6e17)。

GATT 胰岛素输注设备 IDD 命令控制点特征（GATT Characteristic IDD Command Control Point）的 UUID 值。

<a id="r_gaf2bc260638bc158b8bfd403bf43de2d9"></a>

```c
#define BT_UUID_GATT_IDD_CCP BT_UUID_DECLARE_16(BT_UUID_GATT_IDD_CCP_VAL)
```

相关声明：[BT_UUID_GATT_IDD_CCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf2bc260638bc158b8bfd403bf43de2d9)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_IDD_CCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1dc738c5c564bf05d3c2669a79db6e17)。

GATT 胰岛素输注设备 IDD 命令控制点特征（GATT Characteristic IDD Command Control Point）。

<a id="r_ga70d6ece9b4d331965c42f0606c0c7526"></a>

```c
#define BT_UUID_GATT_IDD_CD_VAL 0x2b26
```

相关声明：[BT_UUID_GATT_IDD_CD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga70d6ece9b4d331965c42f0606c0c7526)。

GATT 胰岛素输注设备 IDD 命令数据特征（GATT Characteristic IDD Command Data）的 UUID 值。

<a id="r_gac7dbb4cb283933558699d129928e37d5"></a>

```c
#define BT_UUID_GATT_IDD_CD BT_UUID_DECLARE_16(BT_UUID_GATT_IDD_CD_VAL)
```

相关声明：[BT_UUID_GATT_IDD_CD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac7dbb4cb283933558699d129928e37d5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_IDD_CD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga70d6ece9b4d331965c42f0606c0c7526)。

GATT 胰岛素输注设备 IDD 命令数据特征（GATT Characteristic IDD Command Data）。

<a id="r_gab9ef1f54711a8d7d5884c7b3a798f615"></a>

```c
#define BT_UUID_GATT_IDD_RACP_VAL 0x2b27
```

相关声明：[BT_UUID_GATT_IDD_RACP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab9ef1f54711a8d7d5884c7b3a798f615)。

GATT 胰岛素输注设备 IDD 记录访问控制点特征（GATT Characteristic IDD Record Access Control Point）的 UUID 值。

<a id="r_ga628c153b88ea0f504c234dc44248a237"></a>

```c
#define BT_UUID_GATT_IDD_RACP BT_UUID_DECLARE_16(BT_UUID_GATT_IDD_RACP_VAL)
```

相关声明：[BT_UUID_GATT_IDD_RACP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga628c153b88ea0f504c234dc44248a237)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_IDD_RACP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab9ef1f54711a8d7d5884c7b3a798f615)。

GATT 胰岛素输注设备 IDD 记录访问控制点特征（GATT Characteristic IDD Record Access Control Point）。

<a id="r_ga26f24abf219ce90fd002d995e3a19d30"></a>

```c
#define BT_UUID_GATT_IDD_HD_VAL 0x2b28
```

相关声明：[BT_UUID_GATT_IDD_HD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga26f24abf219ce90fd002d995e3a19d30)。

GATT 胰岛素输注设备 IDD 历史数据特征（GATT Characteristic IDD History Data）的 UUID 值。

<a id="r_ga88e2087b512092d91508f8e878a22f3a"></a>

```c
#define BT_UUID_GATT_IDD_HD BT_UUID_DECLARE_16(BT_UUID_GATT_IDD_HD_VAL)
```

相关声明：[BT_UUID_GATT_IDD_HD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga88e2087b512092d91508f8e878a22f3a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_IDD_HD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga26f24abf219ce90fd002d995e3a19d30)。

GATT 胰岛素输注设备 IDD 历史数据特征（GATT Characteristic IDD History Data）。

<a id="r_ga54537cebc8ce6e7d8d0f377a38765635"></a>

```c
#define BT_UUID_GATT_CLIENT_FEATURES_VAL 0x2b29
```

相关声明：[BT_UUID_GATT_CLIENT_FEATURES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga54537cebc8ce6e7d8d0f377a38765635)。

GATT 客户端支持的功能特征（GATT Characteristic Client Supported Features）的 UUID 值。

<a id="r_gae3faa1515f3aae0c71d4face04929dec"></a>

```c
#define BT_UUID_GATT_CLIENT_FEATURES BT_UUID_DECLARE_16(BT_UUID_GATT_CLIENT_FEATURES_VAL)
```

相关声明：[BT_UUID_GATT_CLIENT_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae3faa1515f3aae0c71d4face04929dec)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CLIENT_FEATURES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga54537cebc8ce6e7d8d0f377a38765635)。

GATT 客户端支持的功能特征（GATT Characteristic Client Supported Features）。

<a id="r_gacead7897f5fed798714a79df2764d95a"></a>

```c
#define BT_UUID_GATT_DB_HASH_VAL 0x2b2a
```

相关声明：[BT_UUID_GATT_DB_HASH_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacead7897f5fed798714a79df2764d95a)。

GATT 数据库哈希特征（GATT Characteristic Database Hash）的 UUID 值。

<a id="r_ga6b162958f4f406fd3e3d31a84393fe19"></a>

```c
#define BT_UUID_GATT_DB_HASH BT_UUID_DECLARE_16(BT_UUID_GATT_DB_HASH_VAL)
```

相关声明：[BT_UUID_GATT_DB_HASH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6b162958f4f406fd3e3d31a84393fe19)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_DB_HASH_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacead7897f5fed798714a79df2764d95a)。

GATT 数据库哈希特征（GATT Characteristic Database Hash）。

<a id="r_gaf609e6663173f4c4bb6ed18274f9931b"></a>

```c
#define BT_UUID_GATT_BSS_CP_VAL 0x2b2b
```

相关声明：[BT_UUID_GATT_BSS_CP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf609e6663173f4c4bb6ed18274f9931b)。

GATT 二值传感器服务 BSS 控制点特征（GATT Characteristic BSS Control Point）的 UUID 值。

<a id="r_gadeabab76545da0de52cc26d48e564730"></a>

```c
#define BT_UUID_GATT_BSS_CP BT_UUID_DECLARE_16(BT_UUID_GATT_BSS_CP_VAL)
```

相关声明：[BT_UUID_GATT_BSS_CP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadeabab76545da0de52cc26d48e564730)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_BSS_CP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf609e6663173f4c4bb6ed18274f9931b)。

GATT 二值传感器服务 BSS 控制点特征（GATT Characteristic BSS Control Point）。

<a id="r_ga73cbe100a043e8f08b87fcfed82107ad"></a>

```c
#define BT_UUID_GATT_BSS_R_VAL 0x2b2c
```

相关声明：[BT_UUID_GATT_BSS_R_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga73cbe100a043e8f08b87fcfed82107ad)。

GATT 二值传感器服务 BSS 响应特征（GATT Characteristic BSS Response）的 UUID 值。

<a id="r_gae9f0db1cbcc6dfeda9beb96e14350cf6"></a>

```c
#define BT_UUID_GATT_BSS_R BT_UUID_DECLARE_16(BT_UUID_GATT_BSS_R_VAL)
```

相关声明：[BT_UUID_GATT_BSS_R](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae9f0db1cbcc6dfeda9beb96e14350cf6)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_BSS_R_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga73cbe100a043e8f08b87fcfed82107ad)。

GATT 二值传感器服务 BSS 响应特征（GATT Characteristic BSS Response）。

<a id="r_ga77157df8db39286f6f6edf1dd71f4a5e"></a>

```c
#define BT_UUID_GATT_EMG_ID_VAL 0x2b2d
```

相关声明：[BT_UUID_GATT_EMG_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga77157df8db39286f6f6edf1dd71f4a5e)。

GATT 紧急标识符特征（GATT Characteristic Emergency ID）的 UUID 值。

<a id="r_ga6fdb1cd7bf1323b27645180ca39ca063"></a>

```c
#define BT_UUID_GATT_EMG_ID BT_UUID_DECLARE_16(BT_UUID_GATT_EMG_ID_VAL)
```

相关声明：[BT_UUID_GATT_EMG_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6fdb1cd7bf1323b27645180ca39ca063)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_EMG_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga77157df8db39286f6f6edf1dd71f4a5e)。

GATT 紧急标识符特征（GATT Characteristic Emergency ID）。

<a id="r_gabcea55cbf065daab8709e4d36941ad90"></a>

```c
#define BT_UUID_GATT_EMG_TXT_VAL 0x2b2e
```

相关声明：[BT_UUID_GATT_EMG_TXT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabcea55cbf065daab8709e4d36941ad90)。

GATT 紧急文本特征（GATT Characteristic Emergency Text）的 UUID 值。

<a id="r_ga1bc6805b2948d3f36af972f2ee34f93a"></a>

```c
#define BT_UUID_GATT_EMG_TXT BT_UUID_DECLARE_16(BT_UUID_GATT_EMG_TXT_VAL)
```

相关声明：[BT_UUID_GATT_EMG_TXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1bc6805b2948d3f36af972f2ee34f93a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_EMG_TXT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabcea55cbf065daab8709e4d36941ad90)。

GATT 紧急文本特征（GATT Characteristic Emergency Text）。

<a id="r_ga7d46292e64c3a8bc9a2ddd71418e56c8"></a>

```c
#define BT_UUID_GATT_ACS_S_VAL 0x2b2f
```

相关声明：[BT_UUID_GATT_ACS_S_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7d46292e64c3a8bc9a2ddd71418e56c8)。

GATT 授权控制服务 ACS 状态特征（GATT Characteristic ACS Status）的 UUID 值。

<a id="r_gad94f7adb29687b460fb7bb860023d890"></a>

```c
#define BT_UUID_GATT_ACS_S BT_UUID_DECLARE_16(BT_UUID_GATT_ACS_S_VAL)
```

相关声明：[BT_UUID_GATT_ACS_S](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad94f7adb29687b460fb7bb860023d890)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ACS_S_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7d46292e64c3a8bc9a2ddd71418e56c8)。

GATT 授权控制服务 ACS 状态特征（GATT Characteristic ACS Status）。

<a id="r_ga0b19f25f01532abb98b63438d55b7683"></a>

```c
#define BT_UUID_GATT_ACS_DI_VAL 0x2b30
```

相关声明：[BT_UUID_GATT_ACS_DI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0b19f25f01532abb98b63438d55b7683)。

GATT 授权控制服务 ACS 数据输入特征（GATT Characteristic ACS Data In）的 UUID 值。

<a id="r_gabd8886704d8fba31bbb1f9a8aeee9aa3"></a>

```c
#define BT_UUID_GATT_ACS_DI BT_UUID_DECLARE_16(BT_UUID_GATT_ACS_DI_VAL)
```

相关声明：[BT_UUID_GATT_ACS_DI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabd8886704d8fba31bbb1f9a8aeee9aa3)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ACS_DI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0b19f25f01532abb98b63438d55b7683)。

GATT 授权控制服务 ACS 数据输入特征（GATT Characteristic ACS Data In）。

<a id="r_ga08ffe10a9e5e1f716581d96dd49bebac"></a>

```c
#define BT_UUID_GATT_ACS_DON_VAL 0x2b31
```

相关声明：[BT_UUID_GATT_ACS_DON_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga08ffe10a9e5e1f716581d96dd49bebac)。

GATT 授权控制服务 ACS 数据输出通知特征（GATT Characteristic ACS Data Out Notify）的 UUID 值。

<a id="r_ga0933ee4e3740e4f6c28522113b84c5b0"></a>

```c
#define BT_UUID_GATT_ACS_DON BT_UUID_DECLARE_16(BT_UUID_GATT_ACS_DON_VAL)
```

相关声明：[BT_UUID_GATT_ACS_DON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0933ee4e3740e4f6c28522113b84c5b0)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ACS_DON_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga08ffe10a9e5e1f716581d96dd49bebac)。

GATT 授权控制服务 ACS 数据输出通知特征（GATT Characteristic ACS Data Out Notify）。

<a id="r_ga852f095873bee6c0dec742ea45817294"></a>

```c
#define BT_UUID_GATT_ACS_DOI_VAL 0x2b32
```

相关声明：[BT_UUID_GATT_ACS_DOI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga852f095873bee6c0dec742ea45817294)。

GATT 授权控制服务 ACS 数据输出指示特征（GATT Characteristic ACS Data Out Indicate）的 UUID 值。

<a id="r_ga4875b80953686217209dc8a90e705ff2"></a>

```c
#define BT_UUID_GATT_ACS_DOI BT_UUID_DECLARE_16(BT_UUID_GATT_ACS_DOI_VAL)
```

相关声明：[BT_UUID_GATT_ACS_DOI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4875b80953686217209dc8a90e705ff2)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ACS_DOI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga852f095873bee6c0dec742ea45817294)。

GATT 授权控制服务 ACS 数据输出指示特征（GATT Characteristic ACS Data Out Indicate）。

<a id="r_ga492e0766dd16dea9e63e80423c9210cb"></a>

```c
#define BT_UUID_GATT_ACS_CP_VAL 0x2b33
```

相关声明：[BT_UUID_GATT_ACS_CP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga492e0766dd16dea9e63e80423c9210cb)。

GATT 授权控制服务 ACS 控制点特征（GATT Characteristic ACS Control Point）的 UUID 值。

<a id="r_gabd2164db62c4f29d2bafc272178312e5"></a>

```c
#define BT_UUID_GATT_ACS_CP BT_UUID_DECLARE_16(BT_UUID_GATT_ACS_CP_VAL)
```

相关声明：[BT_UUID_GATT_ACS_CP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabd2164db62c4f29d2bafc272178312e5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ACS_CP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga492e0766dd16dea9e63e80423c9210cb)。

GATT 授权控制服务 ACS 控制点特征（GATT Characteristic ACS Control Point）。

<a id="r_ga3016f0dd266a98f7d88a3198f54caf7e"></a>

```c
#define BT_UUID_GATT_EBPM_VAL 0x2b34
```

相关声明：[BT_UUID_GATT_EBPM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3016f0dd266a98f7d88a3198f54caf7e)。

GATT 增强血压测量特征（GATT Characteristic Enhanced Blood Pressure Measurement）的 UUID 值。

<a id="r_gafe7d80c67c7c059c174c2ec8aa6cf92d"></a>

```c
#define BT_UUID_GATT_EBPM BT_UUID_DECLARE_16(BT_UUID_GATT_EBPM_VAL)
```

相关声明：[BT_UUID_GATT_EBPM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafe7d80c67c7c059c174c2ec8aa6cf92d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_EBPM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3016f0dd266a98f7d88a3198f54caf7e)。

GATT 增强血压测量特征（GATT Characteristic Enhanced Blood Pressure Measurement）。

<a id="r_gad61213ed875c9d0b6bd5a2e7154f80d7"></a>

```c
#define BT_UUID_GATT_EICP_VAL 0x2b35
```

相关声明：[BT_UUID_GATT_EICP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad61213ed875c9d0b6bd5a2e7154f80d7)。

GATT 增强中间袖带压力特征（GATT Characteristic Enhanced Intermediate Cuff Pressure）的 UUID 值。

<a id="r_gab5032246e17304cb99bb619e6a3d70f1"></a>

```c
#define BT_UUID_GATT_EICP BT_UUID_DECLARE_16(BT_UUID_GATT_EICP_VAL)
```

相关声明：[BT_UUID_GATT_EICP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab5032246e17304cb99bb619e6a3d70f1)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_EICP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad61213ed875c9d0b6bd5a2e7154f80d7)。

GATT 增强中间袖带压力特征（GATT Characteristic Enhanced Intermediate Cuff Pressure）。

<a id="r_ga5b59d10e5d4653ed774a05da55241368"></a>

```c
#define BT_UUID_GATT_BPR_VAL 0x2b36
```

相关声明：[BT_UUID_GATT_BPR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5b59d10e5d4653ed774a05da55241368)。

GATT 血压记录特征（GATT Characteristic Blood Pressure Record）的 UUID 值。

<a id="r_gafa84009c324ee2e0a36efd0bbb486d4b"></a>

```c
#define BT_UUID_GATT_BPR BT_UUID_DECLARE_16(BT_UUID_GATT_BPR_VAL)
```

相关声明：[BT_UUID_GATT_BPR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafa84009c324ee2e0a36efd0bbb486d4b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_BPR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5b59d10e5d4653ed774a05da55241368)。

GATT 血压记录特征（GATT Characteristic Blood Pressure Record）。

<a id="r_ga4ac04b637bed53a51dbf598bd54a827a"></a>

```c
#define BT_UUID_GATT_RU_VAL 0x2b37
```

相关声明：[BT_UUID_GATT_RU_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4ac04b637bed53a51dbf598bd54a827a)。

GATT 已注册用户特征（GATT Characteristic Registered User）的 UUID 值。

<a id="r_ga8a00648e37c023bf06be268960071d27"></a>

```c
#define BT_UUID_GATT_RU BT_UUID_DECLARE_16(BT_UUID_GATT_RU_VAL)
```

相关声明：[BT_UUID_GATT_RU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8a00648e37c023bf06be268960071d27)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_RU_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4ac04b637bed53a51dbf598bd54a827a)。

GATT 已注册用户特征（GATT Characteristic Registered User）。

<a id="r_gab89358d9db126f1eb9e1df6dc4639b82"></a>

```c
#define BT_UUID_GATT_BR_EDR_HD_VAL 0x2b38
```

相关声明：[BT_UUID_GATT_BR_EDR_HD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab89358d9db126f1eb9e1df6dc4639b82)。

GATT BR/EDR 切换数据特征（GATT Characteristic BR-EDR Handover Data）的 UUID 值。

<a id="r_ga279da4b9d9aaccd67846d3ff93e25516"></a>

```c
#define BT_UUID_GATT_BR_EDR_HD BT_UUID_DECLARE_16(BT_UUID_GATT_BR_EDR_HD_VAL)
```

相关声明：[BT_UUID_GATT_BR_EDR_HD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga279da4b9d9aaccd67846d3ff93e25516)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_BR_EDR_HD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab89358d9db126f1eb9e1df6dc4639b82)。

GATT BR/EDR 切换数据特征（GATT Characteristic BR-EDR Handover Data）。

<a id="r_gaf95bc5640e25a651bb62f474fbdbd0f0"></a>

```c
#define BT_UUID_GATT_BT_SIG_D_VAL 0x2b39
```

相关声明：[BT_UUID_GATT_BT_SIG_D_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf95bc5640e25a651bb62f474fbdbd0f0)。

GATT 蓝牙技术联盟 SIG 数据特征（GATT Characteristic Bluetooth SIG Data）的 UUID 值。

<a id="r_ga268e9d8096668ef890f5c17c76c882c5"></a>

```c
#define BT_UUID_GATT_BT_SIG_D BT_UUID_DECLARE_16(BT_UUID_GATT_BT_SIG_D_VAL)
```

相关声明：[BT_UUID_GATT_BT_SIG_D](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga268e9d8096668ef890f5c17c76c882c5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_BT_SIG_D_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf95bc5640e25a651bb62f474fbdbd0f0)。

GATT 蓝牙技术联盟 SIG 数据特征（GATT Characteristic Bluetooth SIG Data）。

<a id="r_ga8d23a276e657bccde1385066ce2cd709"></a>

```c
#define BT_UUID_GATT_SERVER_FEATURES_VAL 0x2b3a
```

相关声明：[BT_UUID_GATT_SERVER_FEATURES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8d23a276e657bccde1385066ce2cd709)。

GATT 服务器支持的功能特征（GATT Characteristic Server Supported Features）的 UUID 值。

<a id="r_ga261af6f050c6a16d174c80cfce48b13e"></a>

```c
#define BT_UUID_GATT_SERVER_FEATURES BT_UUID_DECLARE_16(BT_UUID_GATT_SERVER_FEATURES_VAL)
```

相关声明：[BT_UUID_GATT_SERVER_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga261af6f050c6a16d174c80cfce48b13e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SERVER_FEATURES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8d23a276e657bccde1385066ce2cd709)。

GATT 服务器支持的功能特征（GATT Characteristic Server Supported Features）。

<a id="r_gad94da8852116cc6651c2bb75b8420c95"></a>

```c
#define BT_UUID_GATT_PHY_AMF_VAL 0x2b3b
```

相关声明：[BT_UUID_GATT_PHY_AMF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad94da8852116cc6651c2bb75b8420c95)。

GATT 身体活动监测器功能特征（GATT Characteristic Physical Activity Monitor Features）的 UUID 值。

<a id="r_ga6d227d76b62bcec99cc8a8b6b8054474"></a>

```c
#define BT_UUID_GATT_PHY_AMF BT_UUID_DECLARE_16(BT_UUID_GATT_PHY_AMF_VAL)
```

相关声明：[BT_UUID_GATT_PHY_AMF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6d227d76b62bcec99cc8a8b6b8054474)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_PHY_AMF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad94da8852116cc6651c2bb75b8420c95)。

GATT 身体活动监测器功能特征（GATT Characteristic Physical Activity Monitor Features）。

<a id="r_ga8302d0d60c536b9862028633c8155a3a"></a>

```c
#define BT_UUID_GATT_GEN_AID_VAL 0x2b3c
```

相关声明：[BT_UUID_GATT_GEN_AID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8302d0d60c536b9862028633c8155a3a)。

GATT 一般活动瞬时数据特征（GATT Characteristic General Activity Instantaneous Data）的 UUID 值。

<a id="r_gacfbd8563c68df3aa15264fc81f0eabb8"></a>

```c
#define BT_UUID_GATT_GEN_AID BT_UUID_DECLARE_16(BT_UUID_GATT_GEN_AID_VAL)
```

相关声明：[BT_UUID_GATT_GEN_AID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacfbd8563c68df3aa15264fc81f0eabb8)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_GEN_AID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8302d0d60c536b9862028633c8155a3a)。

GATT 一般活动瞬时数据特征（GATT Characteristic General Activity Instantaneous Data）。

<a id="r_ga4865adb3aadcb01834444e7fda021162"></a>

```c
#define BT_UUID_GATT_GEN_ASD_VAL 0x2b3d
```

相关声明：[BT_UUID_GATT_GEN_ASD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4865adb3aadcb01834444e7fda021162)。

GATT 一般活动汇总数据特征（GATT Characteristic General Activity Summary Data）的 UUID 值。

<a id="r_ga3b068ab73e6c277692a535b81b6e9ae1"></a>

```c
#define BT_UUID_GATT_GEN_ASD BT_UUID_DECLARE_16(BT_UUID_GATT_GEN_ASD_VAL)
```

相关声明：[BT_UUID_GATT_GEN_ASD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3b068ab73e6c277692a535b81b6e9ae1)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_GEN_ASD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4865adb3aadcb01834444e7fda021162)。

GATT 一般活动汇总数据特征（GATT Characteristic General Activity Summary Data）。

<a id="r_gac82a202322d7ee65130150d09d82b76a"></a>

```c
#define BT_UUID_GATT_CR_AID_VAL 0x2b3e
```

相关声明：[BT_UUID_GATT_CR_AID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac82a202322d7ee65130150d09d82b76a)。

GATT 心肺活动瞬时数据特征（GATT Characteristic CardioRespiratory Activity Instantaneous Data）的 UUID 值。

<a id="r_ga35d88cb3312b6867d153780ee3a57be2"></a>

```c
#define BT_UUID_GATT_CR_AID BT_UUID_DECLARE_16(BT_UUID_GATT_CR_AID_VAL)
```

相关声明：[BT_UUID_GATT_CR_AID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga35d88cb3312b6867d153780ee3a57be2)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CR_AID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac82a202322d7ee65130150d09d82b76a)。

GATT 心肺活动瞬时数据特征（GATT Characteristic CardioRespiratory Activity Instantaneous Data）。

<a id="r_ga6606c6d6ac05bbdbbbd27af5c28b825a"></a>

```c
#define BT_UUID_GATT_CR_ASD_VAL 0x2b3f
```

相关声明：[BT_UUID_GATT_CR_ASD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6606c6d6ac05bbdbbbd27af5c28b825a)。

GATT 心肺活动汇总数据特征（GATT Characteristic CardioRespiratory Activity Summary Data）的 UUID 值。

<a id="r_gadac7397ba9891282ef425e05c8161938"></a>

```c
#define BT_UUID_GATT_CR_ASD BT_UUID_DECLARE_16(BT_UUID_GATT_CR_ASD_VAL)
```

相关声明：[BT_UUID_GATT_CR_ASD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadac7397ba9891282ef425e05c8161938)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CR_ASD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6606c6d6ac05bbdbbbd27af5c28b825a)。

GATT 心肺活动汇总数据特征（GATT Characteristic CardioRespiratory Activity Summary Data）。

<a id="r_ga2aed9d07c8f4d552a4d6a5c2b693e97e"></a>

```c
#define BT_UUID_GATT_SC_ASD_VAL 0x2b40
```

相关声明：[BT_UUID_GATT_SC_ASD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2aed9d07c8f4d552a4d6a5c2b693e97e)。

GATT 计步活动汇总数据特征（GATT Characteristic Step Counter Activity Summary Data）的 UUID 值。

<a id="r_ga9dd42f8966856001425c4bae4f6dc5a5"></a>

```c
#define BT_UUID_GATT_SC_ASD BT_UUID_DECLARE_16(BT_UUID_GATT_SC_ASD_VAL)
```

相关声明：[BT_UUID_GATT_SC_ASD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9dd42f8966856001425c4bae4f6dc5a5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SC_ASD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2aed9d07c8f4d552a4d6a5c2b693e97e)。

GATT 计步活动汇总数据特征（GATT Characteristic Step Counter Activity Summary Data）。

<a id="r_gabb73d22b90482201f9f20d6f89aa6671"></a>

```c
#define BT_UUID_GATT_SLP_AID_VAL 0x2b41
```

相关声明：[BT_UUID_GATT_SLP_AID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabb73d22b90482201f9f20d6f89aa6671)。

GATT 睡眠活动瞬时数据特征（GATT Characteristic Sleep Activity Instantaneous Data）的 UUID 值。

<a id="r_gaf0a5a409f91366422f145acbb45e4abd"></a>

```c
#define BT_UUID_GATT_SLP_AID BT_UUID_DECLARE_16(BT_UUID_GATT_SLP_AID_VAL)
```

相关声明：[BT_UUID_GATT_SLP_AID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf0a5a409f91366422f145acbb45e4abd)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SLP_AID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabb73d22b90482201f9f20d6f89aa6671)。

GATT 睡眠活动瞬时数据特征（GATT Characteristic Sleep Activity Instantaneous Data）。

<a id="r_gaa309ce83ee85407cc8068aaccec95b94"></a>

```c
#define BT_UUID_GATT_SLP_ASD_VAL 0x2b42
```

相关声明：[BT_UUID_GATT_SLP_ASD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa309ce83ee85407cc8068aaccec95b94)。

GATT 睡眠活动汇总数据特征（GATT Characteristic Sleep Activity Summary Data）的 UUID 值。

<a id="r_ga5232c5aac8c20f23aaadf1a023d91fcb"></a>

```c
#define BT_UUID_GATT_SLP_ASD BT_UUID_DECLARE_16(BT_UUID_GATT_SLP_ASD_VAL)
```

相关声明：[BT_UUID_GATT_SLP_ASD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5232c5aac8c20f23aaadf1a023d91fcb)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SLP_ASD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa309ce83ee85407cc8068aaccec95b94)。

GATT 睡眠活动汇总数据特征（GATT Characteristic Sleep Activity Summary Data）。

<a id="r_ga1c2a6903fe19f05e4515122ddd6e454f"></a>

```c
#define BT_UUID_GATT_PHY_AMCP_VAL 0x2b43
```

相关声明：[BT_UUID_GATT_PHY_AMCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1c2a6903fe19f05e4515122ddd6e454f)。

GATT 身体活动监测器控制点特征（GATT Characteristic Physical Activity Monitor Control Point）的 UUID 值。

<a id="r_ga59ef934ce5ccf5e4ed309319f75c1150"></a>

```c
#define BT_UUID_GATT_PHY_AMCP BT_UUID_DECLARE_16(BT_UUID_GATT_PHY_AMCP_VAL)
```

相关声明：[BT_UUID_GATT_PHY_AMCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga59ef934ce5ccf5e4ed309319f75c1150)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_PHY_AMCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1c2a6903fe19f05e4515122ddd6e454f)。

GATT 身体活动监测器控制点特征（GATT Characteristic Physical Activity Monitor Control Point）。

<a id="r_gad5ea6f8f92b3679cafed3ac61f5d9128"></a>

```c
#define BT_UUID_GATT_ACS_VAL 0x2b44
```

相关声明：[BT_UUID_GATT_ACS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad5ea6f8f92b3679cafed3ac61f5d9128)。

GATT 活动当前会话特征（GATT Characteristic Activity Current Session）的 UUID 值。

<a id="r_ga12e8344ffb0ae5d3ff088df56f22d440"></a>

```c
#define BT_UUID_GATT_ACS BT_UUID_DECLARE_16(BT_UUID_GATT_ACS_VAL)
```

相关声明：[BT_UUID_GATT_ACS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga12e8344ffb0ae5d3ff088df56f22d440)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ACS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad5ea6f8f92b3679cafed3ac61f5d9128)。

GATT 活动当前会话特征（GATT Characteristic Activity Current Session）。

<a id="r_ga16b2c15259a5c4d456a43df7be9080d6"></a>

```c
#define BT_UUID_GATT_PHY_ASDESC_VAL 0x2b45
```

相关声明：[BT_UUID_GATT_PHY_ASDESC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga16b2c15259a5c4d456a43df7be9080d6)。

GATT 身体活动会话描述符特征（GATT Characteristic Physical Activity Session Descriptor）的 UUID 值。

<a id="r_ga3906642c3830a0dff787b6218f502b74"></a>

```c
#define BT_UUID_GATT_PHY_ASDESC BT_UUID_DECLARE_16(BT_UUID_GATT_PHY_ASDESC_VAL)
```

相关声明：[BT_UUID_GATT_PHY_ASDESC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3906642c3830a0dff787b6218f502b74)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_PHY_ASDESC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga16b2c15259a5c4d456a43df7be9080d6)。

GATT 身体活动会话描述符特征（GATT Characteristic Physical Activity Session Descriptor）。

<a id="r_gae9e12c4297a520b3d626fbd7f4e9c49c"></a>

```c
#define BT_UUID_GATT_PREF_U_VAL 0x2b46
```

相关声明：[BT_UUID_GATT_PREF_U_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae9e12c4297a520b3d626fbd7f4e9c49c)。

GATT 首选单位特征（GATT Characteristic Preferred Units）的 UUID 值。

<a id="r_ga323afc65d2c3568d9a3267328e46879e"></a>

```c
#define BT_UUID_GATT_PREF_U BT_UUID_DECLARE_16(BT_UUID_GATT_PREF_U_VAL)
```

相关声明：[BT_UUID_GATT_PREF_U](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga323afc65d2c3568d9a3267328e46879e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_PREF_U_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae9e12c4297a520b3d626fbd7f4e9c49c)。

GATT 首选单位特征（GATT Characteristic Preferred Units）。

<a id="r_gab74738d5e1fde9be0ae137603d58266a"></a>

```c
#define BT_UUID_GATT_HRES_H_VAL 0x2b47
```

相关声明：[BT_UUID_GATT_HRES_H_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab74738d5e1fde9be0ae137603d58266a)。

GATT 高分辨率身高特征（GATT Characteristic High Resolution Height）的 UUID 值。

<a id="r_gaf095ec3ea1b24f184fce737db3b16855"></a>

```c
#define BT_UUID_GATT_HRES_H BT_UUID_DECLARE_16(BT_UUID_GATT_HRES_H_VAL)
```

相关声明：[BT_UUID_GATT_HRES_H](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf095ec3ea1b24f184fce737db3b16855)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_HRES_H_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab74738d5e1fde9be0ae137603d58266a)。

GATT 高分辨率身高特征（GATT Characteristic High Resolution Height）。

<a id="r_gae44137b7932e5493b66c037b93177f30"></a>

```c
#define BT_UUID_GATT_MID_NAME_VAL 0x2b48
```

相关声明：[BT_UUID_GATT_MID_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae44137b7932e5493b66c037b93177f30)。

GATT 中间名特征（GATT Characteristic Middle Name）的 UUID 值。

<a id="r_ga478706893a1e14f1af28928ea7ee3dde"></a>

```c
#define BT_UUID_GATT_MID_NAME BT_UUID_DECLARE_16(BT_UUID_GATT_MID_NAME_VAL)
```

相关声明：[BT_UUID_GATT_MID_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga478706893a1e14f1af28928ea7ee3dde)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_MID_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae44137b7932e5493b66c037b93177f30)。

GATT 中间名特征（GATT Characteristic Middle Name）。

<a id="r_ga8ebc62a93e6c323031cd64a4c89bc191"></a>

```c
#define BT_UUID_GATT_STRDLEN_VAL 0x2b49
```

相关声明：[BT_UUID_GATT_STRDLEN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8ebc62a93e6c323031cd64a4c89bc191)。

GATT 步幅特征（GATT Characteristic Stride Length）的 UUID 值。

<a id="r_ga1a05d2cef4e003d8a9f417cfb1915600"></a>

```c
#define BT_UUID_GATT_STRDLEN BT_UUID_DECLARE_16(BT_UUID_GATT_STRDLEN_VAL)
```

相关声明：[BT_UUID_GATT_STRDLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1a05d2cef4e003d8a9f417cfb1915600)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_STRDLEN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8ebc62a93e6c323031cd64a4c89bc191)。

GATT 步幅特征（GATT Characteristic Stride Length）。

<a id="r_gaa3a2515dfef7871cb4f2ddaa9b1838bf"></a>

```c
#define BT_UUID_GATT_HANDEDNESS_VAL 0x2b4a
```

相关声明：[BT_UUID_GATT_HANDEDNESS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa3a2515dfef7871cb4f2ddaa9b1838bf)。

GATT 惯用手特征（GATT Characteristic Handedness）的 UUID 值。

<a id="r_ga9e0dd2e887dacb08466f63951bdce22c"></a>

```c
#define BT_UUID_GATT_HANDEDNESS BT_UUID_DECLARE_16(BT_UUID_GATT_HANDEDNESS_VAL)
```

相关声明：[BT_UUID_GATT_HANDEDNESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9e0dd2e887dacb08466f63951bdce22c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_HANDEDNESS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa3a2515dfef7871cb4f2ddaa9b1838bf)。

GATT 惯用手特征（GATT Characteristic Handedness）。

<a id="r_ga7e3028631b4f17fc6127eb41343f6113"></a>

```c
#define BT_UUID_GATT_DEVICE_WP_VAL 0x2b4b
```

相关声明：[BT_UUID_GATT_DEVICE_WP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7e3028631b4f17fc6127eb41343f6113)。

GATT 设备佩戴位置特征（GATT Characteristic Device Wearing Position）的 UUID 值。

<a id="r_gaf26f9aa3d7566892cb4d851a212c7a26"></a>

```c
#define BT_UUID_GATT_DEVICE_WP BT_UUID_DECLARE_16(BT_UUID_GATT_DEVICE_WP_VAL)
```

相关声明：[BT_UUID_GATT_DEVICE_WP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf26f9aa3d7566892cb4d851a212c7a26)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_DEVICE_WP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7e3028631b4f17fc6127eb41343f6113)。

GATT 设备佩戴位置特征（GATT Characteristic Device Wearing Position）。

<a id="r_gaff4928b6e4a0e7329ab18beed9600f1a"></a>

```c
#define BT_UUID_GATT_4ZHRL_VAL 0x2b4c
```

相关声明：[BT_UUID_GATT_4ZHRL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaff4928b6e4a0e7329ab18beed9600f1a)。

GATT 四区间心率界限特征（GATT Characteristic Four Zone Heart Rate Limit）的 UUID 值。

<a id="r_ga1ead62ac6b72dfafdbe46f3c6a3202a1"></a>

```c
#define BT_UUID_GATT_4ZHRL BT_UUID_DECLARE_16(BT_UUID_GATT_4ZHRL_VAL)
```

相关声明：[BT_UUID_GATT_4ZHRL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1ead62ac6b72dfafdbe46f3c6a3202a1)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_4ZHRL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaff4928b6e4a0e7329ab18beed9600f1a)。

GATT 四区间心率界限特征（GATT Characteristic Four Zone Heart Rate Limit）。

<a id="r_ga7fcf423cf762d9c9b534c869581ef358"></a>

```c
#define BT_UUID_GATT_HIET_VAL 0x2b4d
```

相关声明：[BT_UUID_GATT_HIET_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7fcf423cf762d9c9b534c869581ef358)。

GATT 高强度运动阈值特征（GATT Characteristic High Intensity Exercise Threshold）的 UUID 值。

<a id="r_gaa0a5aa82b3eccfc14eef8ce4006899f8"></a>

```c
#define BT_UUID_GATT_HIET BT_UUID_DECLARE_16(BT_UUID_GATT_HIET_VAL)
```

相关声明：[BT_UUID_GATT_HIET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa0a5aa82b3eccfc14eef8ce4006899f8)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_HIET_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7fcf423cf762d9c9b534c869581ef358)。

GATT 高强度运动阈值特征（GATT Characteristic High Intensity Exercise Threshold）。

<a id="r_ga80d44e488176d215f9da4c531915b9f4"></a>

```c
#define BT_UUID_GATT_AG_VAL 0x2b4e
```

相关声明：[BT_UUID_GATT_AG_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga80d44e488176d215f9da4c531915b9f4)。

GATT 活动目标特征（GATT Characteristic Activity Goal）的 UUID 值。

<a id="r_ga8ab5d539f23fd30b6b44294d52cd148f"></a>

```c
#define BT_UUID_GATT_AG BT_UUID_DECLARE_16(BT_UUID_GATT_AG_VAL)
```

相关声明：[BT_UUID_GATT_AG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8ab5d539f23fd30b6b44294d52cd148f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_AG_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga80d44e488176d215f9da4c531915b9f4)。

GATT 活动目标特征（GATT Characteristic Activity Goal）。

<a id="r_ga9f129bc582093032197016897e86748f"></a>

```c
#define BT_UUID_GATT_SIN_VAL 0x2b4f
```

相关声明：[BT_UUID_GATT_SIN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9f129bc582093032197016897e86748f)。

GATT 久坐间隔通知特征（GATT Characteristic Sedentary Interval Notification）的 UUID 值。

<a id="r_gaac75b92f8daddb4aecd5b6e0b2a5d33b"></a>

```c
#define BT_UUID_GATT_SIN BT_UUID_DECLARE_16(BT_UUID_GATT_SIN_VAL)
```

相关声明：[BT_UUID_GATT_SIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaac75b92f8daddb4aecd5b6e0b2a5d33b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SIN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9f129bc582093032197016897e86748f)。

GATT 久坐间隔通知特征（GATT Characteristic Sedentary Interval Notification）。

<a id="r_ga462b52ed2ca39b836e0d7ea3d7a6a609"></a>

```c
#define BT_UUID_GATT_CI_VAL 0x2b50
```

相关声明：[BT_UUID_GATT_CI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga462b52ed2ca39b836e0d7ea3d7a6a609)。

GATT 热量摄入特征（GATT Characteristic Caloric Intake）的 UUID 值。

<a id="r_ga61d3e8f34e0f3d466d4a0b64258a6d13"></a>

```c
#define BT_UUID_GATT_CI BT_UUID_DECLARE_16(BT_UUID_GATT_CI_VAL)
```

相关声明：[BT_UUID_GATT_CI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga61d3e8f34e0f3d466d4a0b64258a6d13)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga462b52ed2ca39b836e0d7ea3d7a6a609)。

GATT 热量摄入特征（GATT Characteristic Caloric Intake）。

<a id="r_ga781de482737cfc42662f6e8b1114070f"></a>

```c
#define BT_UUID_GATT_TMAPR_VAL 0x2b51
```

相关声明：[BT_UUID_GATT_TMAPR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga781de482737cfc42662f6e8b1114070f)。

GATT 电话与媒体音频配置文件 TMAP 角色特征（GATT Characteristic TMAP Role）的 UUID 值。

<a id="r_ga66395bad8099540561670bd1e588e1e9"></a>

```c
#define BT_UUID_GATT_TMAPR BT_UUID_DECLARE_16(BT_UUID_GATT_TMAPR_VAL)
```

相关声明：[BT_UUID_GATT_TMAPR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66395bad8099540561670bd1e588e1e9)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TMAPR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga781de482737cfc42662f6e8b1114070f)。

GATT 电话与媒体音频配置文件 TMAP 角色特征（GATT Characteristic TMAP Role）。

<a id="r_ga95a4d3f8c62782325d2f2bb0df260a97"></a>

```c
#define BT_UUID_AICS_STATE_VAL 0x2b77
```

相关声明：[BT_UUID_AICS_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga95a4d3f8c62782325d2f2bb0df260a97)。

音频输入控制服务状态值（Audio Input Control Service State value）。

<a id="r_ga36fff8099e5a7d9c0cbd407b9b261742"></a>

```c
#define BT_UUID_AICS_STATE BT_UUID_DECLARE_16(BT_UUID_AICS_STATE_VAL)
```

相关声明：[BT_UUID_AICS_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga36fff8099e5a7d9c0cbd407b9b261742)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_AICS_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga95a4d3f8c62782325d2f2bb0df260a97)。

音频输入控制服务状态（Audio Input Control Service State）。

<a id="r_gaab9ed2f83db5e1ea5c2756b8045ca708"></a>

```c
#define BT_UUID_AICS_GAIN_SETTINGS_VAL 0x2b78
```

相关声明：[BT_UUID_AICS_GAIN_SETTINGS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaab9ed2f83db5e1ea5c2756b8045ca708)。

音频输入控制服务增益设置属性值（Audio Input Control Service Gain Settings Properties value）。

<a id="r_ga0b26573f473babc0d4b4d1f817a0e292"></a>

```c
#define BT_UUID_AICS_GAIN_SETTINGS BT_UUID_DECLARE_16(BT_UUID_AICS_GAIN_SETTINGS_VAL)
```

相关声明：[BT_UUID_AICS_GAIN_SETTINGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0b26573f473babc0d4b4d1f817a0e292)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_AICS_GAIN_SETTINGS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaab9ed2f83db5e1ea5c2756b8045ca708)。

音频输入控制服务增益设置属性（Audio Input Control Service Gain Settings Properties）。

<a id="r_ga60250c00a3361316b78e5fa6fef335d7"></a>

```c
#define BT_UUID_AICS_INPUT_TYPE_VAL 0x2b79
```

相关声明：[BT_UUID_AICS_INPUT_TYPE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga60250c00a3361316b78e5fa6fef335d7)。

音频输入控制服务输入类型值（Audio Input Control Service Input Type value）。

<a id="r_gaf9ba49297331bec61b2706ad43a88260"></a>

```c
#define BT_UUID_AICS_INPUT_TYPE BT_UUID_DECLARE_16(BT_UUID_AICS_INPUT_TYPE_VAL)
```

相关声明：[BT_UUID_AICS_INPUT_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf9ba49297331bec61b2706ad43a88260)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_AICS_INPUT_TYPE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga60250c00a3361316b78e5fa6fef335d7)。

音频输入控制服务输入类型（Audio Input Control Service Input Type）。

<a id="r_ga369eeaa589fbb61fffe8e3dabab5aebf"></a>

```c
#define BT_UUID_AICS_INPUT_STATUS_VAL 0x2b7a
```

相关声明：[BT_UUID_AICS_INPUT_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga369eeaa589fbb61fffe8e3dabab5aebf)。

音频输入控制服务输入状态值（Audio Input Control Service Input Status value）。

<a id="r_ga549930ceca2598871f140ec81778923b"></a>

```c
#define BT_UUID_AICS_INPUT_STATUS BT_UUID_DECLARE_16(BT_UUID_AICS_INPUT_STATUS_VAL)
```

相关声明：[BT_UUID_AICS_INPUT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga549930ceca2598871f140ec81778923b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_AICS_INPUT_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga369eeaa589fbb61fffe8e3dabab5aebf)。

音频输入控制服务输入状态（Audio Input Control Service Input Status）。

<a id="r_gacd6c279c902bb8dfa59e886f52161f9a"></a>

```c
#define BT_UUID_AICS_CONTROL_VAL 0x2b7b
```

相关声明：[BT_UUID_AICS_CONTROL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacd6c279c902bb8dfa59e886f52161f9a)。

音频输入控制服务控制点值（Audio Input Control Service Control Point value）。

<a id="r_gae507a2c877c174accb4eb1c18fd7bbc4"></a>

```c
#define BT_UUID_AICS_CONTROL BT_UUID_DECLARE_16(BT_UUID_AICS_CONTROL_VAL)
```

相关声明：[BT_UUID_AICS_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae507a2c877c174accb4eb1c18fd7bbc4)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_AICS_CONTROL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacd6c279c902bb8dfa59e886f52161f9a)。

音频输入控制服务控制点（Audio Input Control Service Control Point）。

<a id="r_ga0cb5c04f3f8c257d012d9907ba8cde38"></a>

```c
#define BT_UUID_AICS_DESCRIPTION_VAL 0x2b7c
```

相关声明：[BT_UUID_AICS_DESCRIPTION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0cb5c04f3f8c257d012d9907ba8cde38)。

音频输入控制服务输入描述值（Audio Input Control Service Input Description value）。

<a id="r_ga9de23aa540a7e07e4c932d60dd84f7c5"></a>

```c
#define BT_UUID_AICS_DESCRIPTION BT_UUID_DECLARE_16(BT_UUID_AICS_DESCRIPTION_VAL)
```

相关声明：[BT_UUID_AICS_DESCRIPTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9de23aa540a7e07e4c932d60dd84f7c5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_AICS_DESCRIPTION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0cb5c04f3f8c257d012d9907ba8cde38)。

音频输入控制服务输入描述（Audio Input Control Service Input Description）。

<a id="r_ga40235c24d4ab2f3c068e8833295bfb89"></a>

```c
#define BT_UUID_VCS_STATE_VAL 0x2b7d
```

相关声明：[BT_UUID_VCS_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga40235c24d4ab2f3c068e8833295bfb89)。

音量控制设置值（Volume Control Setting value）。

<a id="r_gac116f24a102a7b8e6aa80533cc096615"></a>

```c
#define BT_UUID_VCS_STATE BT_UUID_DECLARE_16(BT_UUID_VCS_STATE_VAL)
```

相关声明：[BT_UUID_VCS_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac116f24a102a7b8e6aa80533cc096615)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_VCS_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga40235c24d4ab2f3c068e8833295bfb89)。

音量控制设置（Volume Control Setting）。

<a id="r_ga303c174785d397db54c53572c421e6d3"></a>

```c
#define BT_UUID_VCS_CONTROL_VAL 0x2b7e
```

相关声明：[BT_UUID_VCS_CONTROL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga303c174785d397db54c53572c421e6d3)。

音量控制控制点值（Volume Control Control point value）。

<a id="r_ga24d297c008c9679dcb7078f68affe0a1"></a>

```c
#define BT_UUID_VCS_CONTROL BT_UUID_DECLARE_16(BT_UUID_VCS_CONTROL_VAL)
```

相关声明：[BT_UUID_VCS_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga24d297c008c9679dcb7078f68affe0a1)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_VCS_CONTROL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga303c174785d397db54c53572c421e6d3)。

音量控制控制点（Volume Control Control point）。

<a id="r_ga7f3385da26bf4cddfe12f48147457baf"></a>

```c
#define BT_UUID_VCS_FLAGS_VAL 0x2b7f
```

相关声明：[BT_UUID_VCS_FLAGS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7f3385da26bf4cddfe12f48147457baf)。

音量控制标志值（Volume Control Flags value）。

<a id="r_ga47ff83b277e87cf0629a633a67567e34"></a>

```c
#define BT_UUID_VCS_FLAGS BT_UUID_DECLARE_16(BT_UUID_VCS_FLAGS_VAL)
```

相关声明：[BT_UUID_VCS_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga47ff83b277e87cf0629a633a67567e34)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_VCS_FLAGS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7f3385da26bf4cddfe12f48147457baf)。

音量控制标志（Volume Control Flags）。

<a id="r_gae5535cd478c55390fa3c1199584e614d"></a>

```c
#define BT_UUID_VOCS_STATE_VAL 0x2b80
```

相关声明：[BT_UUID_VOCS_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae5535cd478c55390fa3c1199584e614d)。

音量偏移状态值（Volume Offset State value）。

<a id="r_ga1d198cbdb65d99eb877fa871f4ac5155"></a>

```c
#define BT_UUID_VOCS_STATE BT_UUID_DECLARE_16(BT_UUID_VOCS_STATE_VAL)
```

相关声明：[BT_UUID_VOCS_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1d198cbdb65d99eb877fa871f4ac5155)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_VOCS_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae5535cd478c55390fa3c1199584e614d)。

音量偏移状态（Volume Offset State）。

<a id="r_ga784c29647d14983b3d3f37f9188b6b6f"></a>

```c
#define BT_UUID_VOCS_LOCATION_VAL 0x2b81
```

相关声明：[BT_UUID_VOCS_LOCATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga784c29647d14983b3d3f37f9188b6b6f)。

音频位置值（Audio Location value）。

<a id="r_gad3493dcb58547b4108e8ded6e48e8a8c"></a>

```c
#define BT_UUID_VOCS_LOCATION BT_UUID_DECLARE_16(BT_UUID_VOCS_LOCATION_VAL)
```

相关声明：[BT_UUID_VOCS_LOCATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad3493dcb58547b4108e8ded6e48e8a8c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_VOCS_LOCATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga784c29647d14983b3d3f37f9188b6b6f)。

音频位置（Audio Location）。

<a id="r_gacc2e4a9ac1e93bf6ed1a7001c8038a52"></a>

```c
#define BT_UUID_VOCS_CONTROL_VAL 0x2b82
```

相关声明：[BT_UUID_VOCS_CONTROL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacc2e4a9ac1e93bf6ed1a7001c8038a52)。

音量偏移控制点值（Volume Offset Control Point value）。

<a id="r_gafb68257cf790e12dab2b888320617de7"></a>

```c
#define BT_UUID_VOCS_CONTROL BT_UUID_DECLARE_16(BT_UUID_VOCS_CONTROL_VAL)
```

相关声明：[BT_UUID_VOCS_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafb68257cf790e12dab2b888320617de7)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_VOCS_CONTROL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacc2e4a9ac1e93bf6ed1a7001c8038a52)。

音量偏移控制点（Volume Offset Control Point）。

<a id="r_ga46471ebc019b7c842c0b76efed504625"></a>

```c
#define BT_UUID_VOCS_DESCRIPTION_VAL 0x2b83
```

相关声明：[BT_UUID_VOCS_DESCRIPTION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga46471ebc019b7c842c0b76efed504625)。

音量偏移音频输出描述值（Volume Offset Audio Output Description value）。

<a id="r_gad4a8b4af9f5935b86d1541a2086609d3"></a>

```c
#define BT_UUID_VOCS_DESCRIPTION BT_UUID_DECLARE_16(BT_UUID_VOCS_DESCRIPTION_VAL)
```

相关声明：[BT_UUID_VOCS_DESCRIPTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad4a8b4af9f5935b86d1541a2086609d3)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_VOCS_DESCRIPTION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga46471ebc019b7c842c0b76efed504625)。

音量偏移音频输出描述（Volume Offset Audio Output Description）。

<a id="r_gadaf8b170c1f603f8a61515090558b96c"></a>

```c
#define BT_UUID_CSIS_SIRK_VAL 0x2b84
```

相关声明：[BT_UUID_CSIS_SIRK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadaf8b170c1f603f8a61515090558b96c)。

集合身份解析密钥值（Set Identity Resolving Key value）。

<a id="r_gac0a3863cf4a928bfaae397b14771622d"></a>

```c
#define BT_UUID_CSIS_SIRK BT_UUID_DECLARE_16(BT_UUID_CSIS_SIRK_VAL)
```

相关声明：[BT_UUID_CSIS_SIRK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac0a3863cf4a928bfaae397b14771622d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CSIS_SIRK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadaf8b170c1f603f8a61515090558b96c)。

集合身份解析密钥（Set Identity Resolving Key）。

<a id="r_ga7b5cf381c0806b01fc91c806588a3cfc"></a>

```c
#define BT_UUID_CSIS_SET_SIZE_VAL 0x2b85
```

相关声明：[BT_UUID_CSIS_SET_SIZE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7b5cf381c0806b01fc91c806588a3cfc)。

集合大小值（Set size value）。

<a id="r_ga8995e2ac9173ab613c35f56c5a353d69"></a>

```c
#define BT_UUID_CSIS_SET_SIZE BT_UUID_DECLARE_16(BT_UUID_CSIS_SET_SIZE_VAL)
```

相关声明：[BT_UUID_CSIS_SET_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8995e2ac9173ab613c35f56c5a353d69)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CSIS_SET_SIZE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7b5cf381c0806b01fc91c806588a3cfc)。

集合大小（Set size）。

<a id="r_ga7f296b9f8b09bc62e639b2e1076894dc"></a>

```c
#define BT_UUID_CSIS_SET_LOCK_VAL 0x2b86
```

相关声明：[BT_UUID_CSIS_SET_LOCK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7f296b9f8b09bc62e639b2e1076894dc)。

集合锁值（Set lock value）。

<a id="r_gaf6493077e90f87765c1c1efc044436f0"></a>

```c
#define BT_UUID_CSIS_SET_LOCK BT_UUID_DECLARE_16(BT_UUID_CSIS_SET_LOCK_VAL)
```

相关声明：[BT_UUID_CSIS_SET_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf6493077e90f87765c1c1efc044436f0)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CSIS_SET_LOCK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7f296b9f8b09bc62e639b2e1076894dc)。

集合锁（Set lock）。

<a id="r_ga21db384fb731b1903239a4ecc70138d4"></a>

```c
#define BT_UUID_CSIS_RANK_VAL 0x2b87
```

相关声明：[BT_UUID_CSIS_RANK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga21db384fb731b1903239a4ecc70138d4)。

序位值（Rank value）。

<a id="r_gaa356de4e79779132ed4eeda837b7db57"></a>

```c
#define BT_UUID_CSIS_RANK BT_UUID_DECLARE_16(BT_UUID_CSIS_RANK_VAL)
```

相关声明：[BT_UUID_CSIS_RANK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa356de4e79779132ed4eeda837b7db57)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CSIS_RANK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga21db384fb731b1903239a4ecc70138d4)。

序位（Rank）。

<a id="r_ga31e072f6706b28c309e518cd9449b883"></a>

```c
#define BT_UUID_GATT_EDKM_VAL 0x2b88
```

相关声明：[BT_UUID_GATT_EDKM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga31e072f6706b28c309e518cd9449b883)。

GATT 加密数据密钥材料特征（GATT Characteristic Encrypted Data Key Material）的 UUID 值。

<a id="r_ga9b0daac4f03e23c10fca1a40d07e1618"></a>

```c
#define BT_UUID_GATT_EDKM BT_UUID_DECLARE_16(BT_UUID_GATT_EDKM_VAL)
```

相关声明：[BT_UUID_GATT_EDKM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9b0daac4f03e23c10fca1a40d07e1618)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_EDKM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga31e072f6706b28c309e518cd9449b883)。

GATT 加密数据密钥材料特征（GATT Characteristic Encrypted Data Key Material）。

<a id="r_gac74ea8f9e2800086c286c5fa4185a00e"></a>

```c
#define BT_UUID_GATT_AE32_VAL 0x2b89
```

相关声明：[BT_UUID_GATT_AE32_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac74ea8f9e2800086c286c5fa4185a00e)。

GATT 32 位视在能量特征（GATT Characteristic Apparent Energy 32）的 UUID 值。

<a id="r_ga646adee056d3097eb180bdea1ad0fd33"></a>

```c
#define BT_UUID_GATT_AE32 BT_UUID_DECLARE_16(BT_UUID_GATT_AE32_VAL)
```

相关声明：[BT_UUID_GATT_AE32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga646adee056d3097eb180bdea1ad0fd33)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_AE32_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac74ea8f9e2800086c286c5fa4185a00e)。

GATT 32 位视在能量特征（GATT Characteristic Apparent Energy 32）。

<a id="r_gac3a8b96b59612b0e4ef704afae04e7e3"></a>

```c
#define BT_UUID_GATT_AP_VAL 0x2b8a
```

相关声明：[BT_UUID_GATT_AP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3a8b96b59612b0e4ef704afae04e7e3)。

GATT 视在功率特征（GATT Characteristic Apparent Power）的 UUID 值。

<a id="r_ga91eea2c307dfa99632b52d062c2a2645"></a>

```c
#define BT_UUID_GATT_AP BT_UUID_DECLARE_16(BT_UUID_GATT_AP_VAL)
```

相关声明：[BT_UUID_GATT_AP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga91eea2c307dfa99632b52d062c2a2645)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_AP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3a8b96b59612b0e4ef704afae04e7e3)。

GATT 视在功率特征（GATT Characteristic Apparent Power）。

<a id="r_gaa1edc406495ec9797e153daf1e6cca1f"></a>

```c
#define BT_UUID_GATT_CO2CONC_VAL 0x2b8c
```

相关声明：[BT_UUID_GATT_CO2CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa1edc406495ec9797e153daf1e6cca1f)。

GATT 二氧化碳浓度特征（GATT Characteristic CO2 Concentration）的 UUID 值。

<a id="r_gab4db18c78e70c6e781dcda022be13276"></a>

```c
#define BT_UUID_GATT_CO2CONC BT_UUID_DECLARE_16(BT_UUID_GATT_CO2CONC_VAL)
```

相关声明：[BT_UUID_GATT_CO2CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab4db18c78e70c6e781dcda022be13276)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CO2CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa1edc406495ec9797e153daf1e6cca1f)。

GATT 二氧化碳浓度特征（GATT Characteristic CO2 Concentration）。

<a id="r_ga7a568dfc0ac219b16bdd606953b88184"></a>

```c
#define BT_UUID_GATT_COS_VAL 0x2b8d
```

相关声明：[BT_UUID_GATT_COS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7a568dfc0ac219b16bdd606953b88184)。

GATT 角度余弦特征（GATT Characteristic Cosine of the Angle）的 UUID 值。

<a id="r_ga7d456cc3cdf5d6b25a35f6cca08da585"></a>

```c
#define BT_UUID_GATT_COS BT_UUID_DECLARE_16(BT_UUID_GATT_COS_VAL)
```

相关声明：[BT_UUID_GATT_COS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7d456cc3cdf5d6b25a35f6cca08da585)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_COS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7a568dfc0ac219b16bdd606953b88184)。

GATT 角度余弦特征（GATT Characteristic Cosine of the Angle）。

<a id="r_ga7da79c223cdfb3be45607e86f71a6caa"></a>

```c
#define BT_UUID_GATT_DEVTF_VAL 0x2b8e
```

相关声明：[BT_UUID_GATT_DEVTF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7da79c223cdfb3be45607e86f71a6caa)。

GATT 设备时间功能特征（GATT Characteristic Device Time Feature）的 UUID 值。

<a id="r_ga7e8485b07e0c359964be7b6f8e896546"></a>

```c
#define BT_UUID_GATT_DEVTF BT_UUID_DECLARE_16(BT_UUID_GATT_DEVTF_VAL)
```

相关声明：[BT_UUID_GATT_DEVTF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7e8485b07e0c359964be7b6f8e896546)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_DEVTF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7da79c223cdfb3be45607e86f71a6caa)。

GATT 设备时间功能特征（GATT Characteristic Device Time Feature）。

<a id="r_ga744f71f5b0c8d2cfe4faf6107f33633b"></a>

```c
#define BT_UUID_GATT_DEVTP_VAL 0x2b8f
```

相关声明：[BT_UUID_GATT_DEVTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga744f71f5b0c8d2cfe4faf6107f33633b)。

GATT 设备时间参数特征（GATT Characteristic Device Time Parameters）的 UUID 值。

<a id="r_ga0f22bf31cbe7a58944340b03ccf591c5"></a>

```c
#define BT_UUID_GATT_DEVTP BT_UUID_DECLARE_16(BT_UUID_GATT_DEVTP_VAL)
```

相关声明：[BT_UUID_GATT_DEVTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0f22bf31cbe7a58944340b03ccf591c5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_DEVTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga744f71f5b0c8d2cfe4faf6107f33633b)。

GATT 设备时间参数特征（GATT Characteristic Device Time Parameters）。

<a id="r_ga7d0ff38d80780d63e4b43a200be5c7d3"></a>

```c
#define BT_UUID_GATT_DEVT_VAL 0x2b90
```

相关声明：[BT_UUID_GATT_DEVT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7d0ff38d80780d63e4b43a200be5c7d3)。

GATT 设备时间特征（GATT Characteristic Device Time）的 UUID 值。

<a id="r_ga9eb6c84a8ab924deb9fbe5b331d2628a"></a>

```c
#define BT_UUID_GATT_DEVT BT_UUID_DECLARE_16(BT_UUID_GATT_DEVT_VAL)
```

相关声明：[BT_UUID_GATT_DEVT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9eb6c84a8ab924deb9fbe5b331d2628a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_DEVT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7d0ff38d80780d63e4b43a200be5c7d3)。

GATT 设备时间特征（GATT Characteristic Device Time）。

<a id="r_ga111396f18a4d565fabe50e4ab4bb6b01"></a>

```c
#define BT_UUID_GATT_DEVTCP_VAL 0x2b91
```

相关声明：[BT_UUID_GATT_DEVTCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga111396f18a4d565fabe50e4ab4bb6b01)。

GATT 设备时间控制点特征（GATT Characteristic Device Time Control Point）的 UUID 值。

<a id="r_ga18de8889aa0297fc80a6fc2846f83da2"></a>

```c
#define BT_UUID_GATT_DEVTCP BT_UUID_DECLARE_16(BT_UUID_GATT_DEVTCP_VAL)
```

相关声明：[BT_UUID_GATT_DEVTCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga18de8889aa0297fc80a6fc2846f83da2)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_DEVTCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga111396f18a4d565fabe50e4ab4bb6b01)。

GATT 设备时间控制点特征（GATT Characteristic Device Time Control Point）。

<a id="r_ga2aa7a226cd54e1e2435a045cd936c222"></a>

```c
#define BT_UUID_GATT_TCLD_VAL 0x2b92
```

相关声明：[BT_UUID_GATT_TCLD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2aa7a226cd54e1e2435a045cd936c222)。

GATT 时间变更日志数据特征（GATT Characteristic Time Change Log Data）的 UUID 值。

<a id="r_ga0e38fdb6334c4aa1b3fe8163cad290ea"></a>

```c
#define BT_UUID_GATT_TCLD BT_UUID_DECLARE_16(BT_UUID_GATT_TCLD_VAL)
```

相关声明：[BT_UUID_GATT_TCLD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0e38fdb6334c4aa1b3fe8163cad290ea)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TCLD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2aa7a226cd54e1e2435a045cd936c222)。

GATT 时间变更日志数据特征（GATT Characteristic Time Change Log Data）。

<a id="r_ga26421e4fde9e424af8318a2a06e55729"></a>

```c
#define BT_UUID_MCS_PLAYER_NAME_VAL 0x2b93
```

相关声明：[BT_UUID_MCS_PLAYER_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga26421e4fde9e424af8318a2a06e55729)。

媒体播放器名称值（Media player name value）。

<a id="r_ga25706c3572dd91b223dd7cbea6cc71e2"></a>

```c
#define BT_UUID_MCS_PLAYER_NAME BT_UUID_DECLARE_16(BT_UUID_MCS_PLAYER_NAME_VAL)
```

相关声明：[BT_UUID_MCS_PLAYER_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga25706c3572dd91b223dd7cbea6cc71e2)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_PLAYER_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga26421e4fde9e424af8318a2a06e55729)。

媒体播放器名称（Media player name）。

<a id="r_gadefa705eae4221748b18f5a088c768ca"></a>

```c
#define BT_UUID_MCS_ICON_OBJ_ID_VAL 0x2b94
```

相关声明：[BT_UUID_MCS_ICON_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadefa705eae4221748b18f5a088c768ca)。

媒体图标对象标识符值（Media Icon Object ID value）。

<a id="r_ga63ce9edebeebcac1e7344efdabc6519e"></a>

```c
#define BT_UUID_MCS_ICON_OBJ_ID BT_UUID_DECLARE_16(BT_UUID_MCS_ICON_OBJ_ID_VAL)
```

相关声明：[BT_UUID_MCS_ICON_OBJ_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga63ce9edebeebcac1e7344efdabc6519e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_ICON_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadefa705eae4221748b18f5a088c768ca)。

媒体图标对象标识符（Media Icon Object ID）。

<a id="r_gad80db7e88bc50944b71ca4c51f6674db"></a>

```c
#define BT_UUID_MCS_ICON_URL_VAL 0x2b95
```

相关声明：[BT_UUID_MCS_ICON_URL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad80db7e88bc50944b71ca4c51f6674db)。

媒体图标 URL 值（Media Icon URL value）。

<a id="r_ga1ff74274cc34b8ba88af2b455109eb98"></a>

```c
#define BT_UUID_MCS_ICON_URL BT_UUID_DECLARE_16(BT_UUID_MCS_ICON_URL_VAL)
```

相关声明：[BT_UUID_MCS_ICON_URL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1ff74274cc34b8ba88af2b455109eb98)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_ICON_URL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad80db7e88bc50944b71ca4c51f6674db)。

媒体图标 URL（Media Icon URL）。

<a id="r_ga71cb9b105eb4a581167e09fb293d7dd5"></a>

```c
#define BT_UUID_MCS_TRACK_CHANGED_VAL 0x2b96
```

相关声明：[BT_UUID_MCS_TRACK_CHANGED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga71cb9b105eb4a581167e09fb293d7dd5)。

曲目已变更值（Track Changed value）。

<a id="r_gae7e7b15660158399bd837f10c1380982"></a>

```c
#define BT_UUID_MCS_TRACK_CHANGED BT_UUID_DECLARE_16(BT_UUID_MCS_TRACK_CHANGED_VAL)
```

相关声明：[BT_UUID_MCS_TRACK_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae7e7b15660158399bd837f10c1380982)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_TRACK_CHANGED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga71cb9b105eb4a581167e09fb293d7dd5)。

曲目已变更（Track Changed）。

<a id="r_ga8082647831b1da4237b85346f1dca249"></a>

```c
#define BT_UUID_MCS_TRACK_TITLE_VAL 0x2b97
```

相关声明：[BT_UUID_MCS_TRACK_TITLE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8082647831b1da4237b85346f1dca249)。

曲目标题值（Track Title value）。

<a id="r_gafb41d75e4bf569b1efeba763fb93722f"></a>

```c
#define BT_UUID_MCS_TRACK_TITLE BT_UUID_DECLARE_16(BT_UUID_MCS_TRACK_TITLE_VAL)
```

相关声明：[BT_UUID_MCS_TRACK_TITLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafb41d75e4bf569b1efeba763fb93722f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_TRACK_TITLE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8082647831b1da4237b85346f1dca249)。

曲目标题（Track Title）。

<a id="r_ga7786188af799df504bcbba1aa007a3eb"></a>

```c
#define BT_UUID_MCS_TRACK_DURATION_VAL 0x2b98
```

相关声明：[BT_UUID_MCS_TRACK_DURATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7786188af799df504bcbba1aa007a3eb)。

曲目时长值（Track Duration value）。

<a id="r_ga76d4d2c92df6b9d82d60ee7fe835d29c"></a>

```c
#define BT_UUID_MCS_TRACK_DURATION BT_UUID_DECLARE_16(BT_UUID_MCS_TRACK_DURATION_VAL)
```

相关声明：[BT_UUID_MCS_TRACK_DURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga76d4d2c92df6b9d82d60ee7fe835d29c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_TRACK_DURATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7786188af799df504bcbba1aa007a3eb)。

曲目时长（Track Duration）。

<a id="r_ga6b74c773a708eccb84074cb7ef8c8fe2"></a>

```c
#define BT_UUID_MCS_TRACK_POSITION_VAL 0x2b99
```

相关声明：[BT_UUID_MCS_TRACK_POSITION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6b74c773a708eccb84074cb7ef8c8fe2)。

曲目位置值（Track Position value）。

<a id="r_gaa4665539c5027680a843d851bf1b8bfe"></a>

```c
#define BT_UUID_MCS_TRACK_POSITION BT_UUID_DECLARE_16(BT_UUID_MCS_TRACK_POSITION_VAL)
```

相关声明：[BT_UUID_MCS_TRACK_POSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa4665539c5027680a843d851bf1b8bfe)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_TRACK_POSITION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6b74c773a708eccb84074cb7ef8c8fe2)。

曲目位置（Track Position）。

<a id="r_gadfe7acf9dbc6ebd3fe21fe469f39e937"></a>

```c
#define BT_UUID_MCS_PLAYBACK_SPEED_VAL 0x2b9a
```

相关声明：[BT_UUID_MCS_PLAYBACK_SPEED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadfe7acf9dbc6ebd3fe21fe469f39e937)。

播放速度值（Playback Speed value）。

<a id="r_ga47629d64d3ed4587089fb8551c4c594c"></a>

```c
#define BT_UUID_MCS_PLAYBACK_SPEED BT_UUID_DECLARE_16(BT_UUID_MCS_PLAYBACK_SPEED_VAL)
```

相关声明：[BT_UUID_MCS_PLAYBACK_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga47629d64d3ed4587089fb8551c4c594c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_PLAYBACK_SPEED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadfe7acf9dbc6ebd3fe21fe469f39e937)。

播放速度（Playback Speed）。

<a id="r_gaf8ebb66a23e2bed1c7e5b08c79cfe579"></a>

```c
#define BT_UUID_MCS_SEEKING_SPEED_VAL 0x2b9b
```

相关声明：[BT_UUID_MCS_SEEKING_SPEED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf8ebb66a23e2bed1c7e5b08c79cfe579)。

搜索速度值（Seeking Speed value）。

<a id="r_gac1d6109a86c67555c4b632d6a0563d92"></a>

```c
#define BT_UUID_MCS_SEEKING_SPEED BT_UUID_DECLARE_16(BT_UUID_MCS_SEEKING_SPEED_VAL)
```

相关声明：[BT_UUID_MCS_SEEKING_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac1d6109a86c67555c4b632d6a0563d92)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_SEEKING_SPEED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf8ebb66a23e2bed1c7e5b08c79cfe579)。

搜索速度（Seeking Speed）。

<a id="r_gafa793d37f3d9c57d1f456a0a9c5dba36"></a>

```c
#define BT_UUID_MCS_TRACK_SEGMENTS_OBJ_ID_VAL 0x2b9c
```

相关声明：[BT_UUID_MCS_TRACK_SEGMENTS_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafa793d37f3d9c57d1f456a0a9c5dba36)。

曲目分段对象标识符值（Track Segments Object ID value）。

<a id="r_gaa1e0e61ba28da785308e5dafd72931fd"></a>

```c
#define BT_UUID_MCS_TRACK_SEGMENTS_OBJ_ID BT_UUID_DECLARE_16(BT_UUID_MCS_TRACK_SEGMENTS_OBJ_ID_VAL)
```

相关声明：[BT_UUID_MCS_TRACK_SEGMENTS_OBJ_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa1e0e61ba28da785308e5dafd72931fd)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_TRACK_SEGMENTS_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafa793d37f3d9c57d1f456a0a9c5dba36)。

曲目分段对象标识符（Track Segments Object ID）。

<a id="r_ga884f66865500c127def77f2764b7a322"></a>

```c
#define BT_UUID_MCS_CURRENT_TRACK_OBJ_ID_VAL 0x2b9d
```

相关声明：[BT_UUID_MCS_CURRENT_TRACK_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga884f66865500c127def77f2764b7a322)。

当前曲目对象标识符值（Current Track Object ID value）。

<a id="r_gad11916b1a6704ce9cc80a35ddd1b1023"></a>

```c
#define BT_UUID_MCS_CURRENT_TRACK_OBJ_ID BT_UUID_DECLARE_16(BT_UUID_MCS_CURRENT_TRACK_OBJ_ID_VAL)
```

相关声明：[BT_UUID_MCS_CURRENT_TRACK_OBJ_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad11916b1a6704ce9cc80a35ddd1b1023)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_CURRENT_TRACK_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga884f66865500c127def77f2764b7a322)。

当前曲目对象标识符（Current Track Object ID）。

<a id="r_ga791f147766bd7511fdeb98ed9f4e3e05"></a>

```c
#define BT_UUID_MCS_NEXT_TRACK_OBJ_ID_VAL 0x2b9e
```

相关声明：[BT_UUID_MCS_NEXT_TRACK_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga791f147766bd7511fdeb98ed9f4e3e05)。

下一曲目对象标识符值（Next Track Object ID value）。

<a id="r_gaba85414e514d71f1ada3cd32ab7b9857"></a>

```c
#define BT_UUID_MCS_NEXT_TRACK_OBJ_ID BT_UUID_DECLARE_16(BT_UUID_MCS_NEXT_TRACK_OBJ_ID_VAL)
```

相关声明：[BT_UUID_MCS_NEXT_TRACK_OBJ_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaba85414e514d71f1ada3cd32ab7b9857)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_NEXT_TRACK_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga791f147766bd7511fdeb98ed9f4e3e05)。

下一曲目对象标识符（Next Track Object ID）。

<a id="r_ga06410ca2d5575cb44f3f365c27960487"></a>

```c
#define BT_UUID_MCS_PARENT_GROUP_OBJ_ID_VAL 0x2b9f
```

相关声明：[BT_UUID_MCS_PARENT_GROUP_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga06410ca2d5575cb44f3f365c27960487)。

父组对象标识符值（Parent Group Object ID value）。

<a id="r_ga2dbb766bda1581f49ff331beefdad2c5"></a>

```c
#define BT_UUID_MCS_PARENT_GROUP_OBJ_ID BT_UUID_DECLARE_16(BT_UUID_MCS_PARENT_GROUP_OBJ_ID_VAL)
```

相关声明：[BT_UUID_MCS_PARENT_GROUP_OBJ_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2dbb766bda1581f49ff331beefdad2c5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_PARENT_GROUP_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga06410ca2d5575cb44f3f365c27960487)。

父组对象标识符（Parent Group Object ID）。

<a id="r_ga3873c1d5075d4cb3035509ce57595c28"></a>

```c
#define BT_UUID_MCS_CURRENT_GROUP_OBJ_ID_VAL 0x2ba0
```

相关声明：[BT_UUID_MCS_CURRENT_GROUP_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3873c1d5075d4cb3035509ce57595c28)。

组对象标识符值（Group Object ID value）。

<a id="r_ga303b89c5ba301bd2c18a3eb48f214ded"></a>

```c
#define BT_UUID_MCS_CURRENT_GROUP_OBJ_ID BT_UUID_DECLARE_16(BT_UUID_MCS_CURRENT_GROUP_OBJ_ID_VAL)
```

相关声明：[BT_UUID_MCS_CURRENT_GROUP_OBJ_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga303b89c5ba301bd2c18a3eb48f214ded)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_CURRENT_GROUP_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3873c1d5075d4cb3035509ce57595c28)。

组对象标识符（Group Object ID）。

<a id="r_ga0b17cfa67cdec5722cf51ebc9a616384"></a>

```c
#define BT_UUID_MCS_PLAYING_ORDER_VAL 0x2ba1
```

相关声明：[BT_UUID_MCS_PLAYING_ORDER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0b17cfa67cdec5722cf51ebc9a616384)。

播放顺序值（Playing Order value）。

<a id="r_ga7c676d7019e19189cffaf34aefe66c59"></a>

```c
#define BT_UUID_MCS_PLAYING_ORDER BT_UUID_DECLARE_16(BT_UUID_MCS_PLAYING_ORDER_VAL)
```

相关声明：[BT_UUID_MCS_PLAYING_ORDER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7c676d7019e19189cffaf34aefe66c59)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_PLAYING_ORDER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0b17cfa67cdec5722cf51ebc9a616384)。

播放顺序（Playing Order）。

<a id="r_ga103cd4f0ae88b27c32ab7854c331de59"></a>

```c
#define BT_UUID_MCS_PLAYING_ORDERS_VAL 0x2ba2
```

相关声明：[BT_UUID_MCS_PLAYING_ORDERS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga103cd4f0ae88b27c32ab7854c331de59)。

支持的播放顺序值（Playing Orders supported value）。

<a id="r_ga283a2f22a049a6c78221d1186d17e6f5"></a>

```c
#define BT_UUID_MCS_PLAYING_ORDERS BT_UUID_DECLARE_16(BT_UUID_MCS_PLAYING_ORDERS_VAL)
```

相关声明：[BT_UUID_MCS_PLAYING_ORDERS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga283a2f22a049a6c78221d1186d17e6f5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_PLAYING_ORDERS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga103cd4f0ae88b27c32ab7854c331de59)。

支持的播放顺序（Playing Orders supported）。

<a id="r_ga8f62ba6fe627eda5c188151a89d1299f"></a>

```c
#define BT_UUID_MCS_MEDIA_STATE_VAL 0x2ba3
```

相关声明：[BT_UUID_MCS_MEDIA_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8f62ba6fe627eda5c188151a89d1299f)。

媒体状态值（Media State value）。

<a id="r_gaadaf94fbf0d316505e27fc115998ffd2"></a>

```c
#define BT_UUID_MCS_MEDIA_STATE BT_UUID_DECLARE_16(BT_UUID_MCS_MEDIA_STATE_VAL)
```

相关声明：[BT_UUID_MCS_MEDIA_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaadaf94fbf0d316505e27fc115998ffd2)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_MEDIA_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8f62ba6fe627eda5c188151a89d1299f)。

媒体状态（Media State）。

<a id="r_ga3b276420dc39941339c3f3bcb3835d3c"></a>

```c
#define BT_UUID_MCS_MEDIA_CONTROL_POINT_VAL 0x2ba4
```

相关声明：[BT_UUID_MCS_MEDIA_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3b276420dc39941339c3f3bcb3835d3c)。

媒体控制点值（Media Control Point value）。

<a id="r_gae3dc24d21d36349c7af95fe90db6ec91"></a>

```c
#define BT_UUID_MCS_MEDIA_CONTROL_POINT BT_UUID_DECLARE_16(BT_UUID_MCS_MEDIA_CONTROL_POINT_VAL)
```

相关声明：[BT_UUID_MCS_MEDIA_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae3dc24d21d36349c7af95fe90db6ec91)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_MEDIA_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3b276420dc39941339c3f3bcb3835d3c)。

媒体控制点（Media Control Point）。

<a id="r_ga6eb18372f842f362bb45c93bbefd560b"></a>

```c
#define BT_UUID_MCS_MEDIA_CONTROL_OPCODES_VAL 0x2ba5
```

相关声明：[BT_UUID_MCS_MEDIA_CONTROL_OPCODES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6eb18372f842f362bb45c93bbefd560b)。

支持的媒体控制操作码值（Media control opcodes supported value）。

<a id="r_ga6ef3d74033d401d7d5fb092485faee16"></a>

```c
#define BT_UUID_MCS_MEDIA_CONTROL_OPCODES BT_UUID_DECLARE_16(BT_UUID_MCS_MEDIA_CONTROL_OPCODES_VAL)
```

相关声明：[BT_UUID_MCS_MEDIA_CONTROL_OPCODES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6ef3d74033d401d7d5fb092485faee16)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_MEDIA_CONTROL_OPCODES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6eb18372f842f362bb45c93bbefd560b)。

支持的媒体控制操作码（Media control opcodes supported）。

<a id="r_ga337509c52a77206589a8208cf6ac3ac0"></a>

```c
#define BT_UUID_MCS_SEARCH_RESULTS_OBJ_ID_VAL 0x2ba6
```

相关声明：[BT_UUID_MCS_SEARCH_RESULTS_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga337509c52a77206589a8208cf6ac3ac0)。

搜索结果对象标识符值（Search result object ID value）。

<a id="r_ga2ce71ff006f161cd899fb6b09a98c66f"></a>

```c
#define BT_UUID_MCS_SEARCH_RESULTS_OBJ_ID BT_UUID_DECLARE_16(BT_UUID_MCS_SEARCH_RESULTS_OBJ_ID_VAL)
```

相关声明：[BT_UUID_MCS_SEARCH_RESULTS_OBJ_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2ce71ff006f161cd899fb6b09a98c66f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_SEARCH_RESULTS_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga337509c52a77206589a8208cf6ac3ac0)。

搜索结果对象标识符（Search result object ID）。

<a id="r_gab89e74c66515dfcdffcb4967b3de4f0d"></a>

```c
#define BT_UUID_MCS_SEARCH_CONTROL_POINT_VAL 0x2ba7
```

相关声明：[BT_UUID_MCS_SEARCH_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab89e74c66515dfcdffcb4967b3de4f0d)。

搜索控制点值（Search control point value）。

<a id="r_gab7892abc4201dc18da2bd4a2efca1963"></a>

```c
#define BT_UUID_MCS_SEARCH_CONTROL_POINT BT_UUID_DECLARE_16(BT_UUID_MCS_SEARCH_CONTROL_POINT_VAL)
```

相关声明：[BT_UUID_MCS_SEARCH_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab7892abc4201dc18da2bd4a2efca1963)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCS_SEARCH_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab89e74c66515dfcdffcb4967b3de4f0d)。

搜索控制点（Search control point）。

<a id="r_ga8f238d8197b3293562809916eb667f27"></a>

```c
#define BT_UUID_GATT_E32_VAL 0x2ba8
```

相关声明：[BT_UUID_GATT_E32_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8f238d8197b3293562809916eb667f27)。

GATT 32 位能量特征（GATT Characteristic Energy 32）的 UUID 值。

<a id="r_ga6419bfcbe6cad1f568b9e212d704e7c7"></a>

```c
#define BT_UUID_GATT_E32 BT_UUID_DECLARE_16(BT_UUID_GATT_E32_VAL)
```

相关声明：[BT_UUID_GATT_E32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6419bfcbe6cad1f568b9e212d704e7c7)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_E32_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8f238d8197b3293562809916eb667f27)。

GATT 32 位能量特征（GATT Characteristic Energy 32）。

<a id="r_gaeb12a1e806156ec1b7f945dddce3fa24"></a>

```c
#define BT_UUID_OTS_TYPE_MPL_ICON_VAL 0x2ba9
```

相关声明：[BT_UUID_OTS_TYPE_MPL_ICON_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaeb12a1e806156ec1b7f945dddce3fa24)。

媒体播放器图标对象类型值（Media Player Icon Object Type value）。

<a id="r_ga3b425e5f019ba59d2d76a5d6e9cc16ee"></a>

```c
#define BT_UUID_OTS_TYPE_MPL_ICON BT_UUID_DECLARE_16(BT_UUID_OTS_TYPE_MPL_ICON_VAL)
```

相关声明：[BT_UUID_OTS_TYPE_MPL_ICON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3b425e5f019ba59d2d76a5d6e9cc16ee)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_TYPE_MPL_ICON_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaeb12a1e806156ec1b7f945dddce3fa24)。

媒体播放器图标对象类型（Media Player Icon Object Type）。

<a id="r_gaf05ecc673eae8b56ce6d5a98e5b22130"></a>

```c
#define BT_UUID_OTS_TYPE_TRACK_SEGMENT_VAL 0x2baa
```

相关声明：[BT_UUID_OTS_TYPE_TRACK_SEGMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf05ecc673eae8b56ce6d5a98e5b22130)。

曲目分段对象类型值（Track Segments Object Type value）。

<a id="r_ga5f3fdbd12cc804ed0ca811d4bafe1109"></a>

```c
#define BT_UUID_OTS_TYPE_TRACK_SEGMENT BT_UUID_DECLARE_16(BT_UUID_OTS_TYPE_TRACK_SEGMENT_VAL)
```

相关声明：[BT_UUID_OTS_TYPE_TRACK_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5f3fdbd12cc804ed0ca811d4bafe1109)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_TYPE_TRACK_SEGMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf05ecc673eae8b56ce6d5a98e5b22130)。

曲目分段对象类型（Track Segments Object Type）。

<a id="r_gaf4094e3381053890f6264d17ff129255"></a>

```c
#define BT_UUID_OTS_TYPE_TRACK_VAL 0x2bab
```

相关声明：[BT_UUID_OTS_TYPE_TRACK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf4094e3381053890f6264d17ff129255)。

曲目对象类型值（Track Object Type value）。

<a id="r_gafcf9774a2b6aa1081b6c1a03b31a0c07"></a>

```c
#define BT_UUID_OTS_TYPE_TRACK BT_UUID_DECLARE_16(BT_UUID_OTS_TYPE_TRACK_VAL)
```

相关声明：[BT_UUID_OTS_TYPE_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafcf9774a2b6aa1081b6c1a03b31a0c07)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_TYPE_TRACK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf4094e3381053890f6264d17ff129255)。

曲目对象类型（Track Object Type）。

<a id="r_gafc689c443c46385aefbca0e1db73f877"></a>

```c
#define BT_UUID_OTS_TYPE_GROUP_VAL 0x2bac
```

相关声明：[BT_UUID_OTS_TYPE_GROUP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafc689c443c46385aefbca0e1db73f877)。

组对象类型值（Group Object Type value）。

<a id="r_ga7a6fd4221135821cd15a3ba10f33532d"></a>

```c
#define BT_UUID_OTS_TYPE_GROUP BT_UUID_DECLARE_16(BT_UUID_OTS_TYPE_GROUP_VAL)
```

相关声明：[BT_UUID_OTS_TYPE_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7a6fd4221135821cd15a3ba10f33532d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OTS_TYPE_GROUP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafc689c443c46385aefbca0e1db73f877)。

组对象类型（Group Object Type）。

<a id="r_ga6577476ef4d85191e5d5533f6bb99b2d"></a>

```c
#define BT_UUID_GATT_CTEE_VAL 0x2bad
```

相关声明：[BT_UUID_GATT_CTEE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6577476ef4d85191e5d5533f6bb99b2d)。

GATT 恒定音调扩展启用特征（GATT Characteristic Constant Tone Extension Enable）的 UUID 值。

<a id="r_ga985a0ebcc0a61e2c4d9f2f61a7a1afb0"></a>

```c
#define BT_UUID_GATT_CTEE BT_UUID_DECLARE_16(BT_UUID_GATT_CTEE_VAL)
```

相关声明：[BT_UUID_GATT_CTEE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga985a0ebcc0a61e2c4d9f2f61a7a1afb0)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CTEE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6577476ef4d85191e5d5533f6bb99b2d)。

GATT 恒定音调扩展启用特征（GATT Characteristic Constant Tone Extension Enable）。

<a id="r_gaca4a23a27a2c06eb10da1a64c617cac1"></a>

```c
#define BT_UUID_GATT_ACTEML_VAL 0x2bae
```

相关声明：[BT_UUID_GATT_ACTEML_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaca4a23a27a2c06eb10da1a64c617cac1)。

GATT 广播恒定音调扩展最小长度特征（GATT Characteristic Advertising Constant Tone Extension Minimum Length）的 UUID 值。

<a id="r_ga51915bb0637c157a67ce4488e46905a6"></a>

```c
#define BT_UUID_GATT_ACTEML BT_UUID_DECLARE_16(BT_UUID_GATT_ACTEML_VAL)
```

相关声明：[BT_UUID_GATT_ACTEML](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga51915bb0637c157a67ce4488e46905a6)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ACTEML_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaca4a23a27a2c06eb10da1a64c617cac1)。

GATT 广播恒定音调扩展最小长度特征（GATT Characteristic Advertising Constant Tone Extension Minimum Length）。

<a id="r_gad3ddda1c88208094616608b178bb27ec"></a>

```c
#define BT_UUID_GATT_ACTEMTC_VAL 0x2baf
```

相关声明：[BT_UUID_GATT_ACTEMTC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad3ddda1c88208094616608b178bb27ec)。

GATT 广播恒定音调扩展最小发送次数特征（GATT Characteristic Advertising Constant Tone Extension Minimum Transmit Count）的 UUID 值。

<a id="r_ga47620598a9365d2fc8d70ada1144c9c1"></a>

```c
#define BT_UUID_GATT_ACTEMTC BT_UUID_DECLARE_16(BT_UUID_GATT_ACTEMTC_VAL)
```

相关声明：[BT_UUID_GATT_ACTEMTC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga47620598a9365d2fc8d70ada1144c9c1)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ACTEMTC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad3ddda1c88208094616608b178bb27ec)。

GATT 广播恒定音调扩展最小发送次数特征（GATT Characteristic Advertising Constant Tone Extension Minimum Transmit Count）。

<a id="r_ga165c63f8c91f61a9930b3c804f7051b7"></a>

```c
#define BT_UUID_GATT_ACTETD_VAL 0x2bb0
```

相关声明：[BT_UUID_GATT_ACTETD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga165c63f8c91f61a9930b3c804f7051b7)。

GATT 广播恒定音调扩展发送时长特征（GATT Characteristic Advertising Constant Tone Extension Transmit Duration）的 UUID 值。

<a id="r_ga5a15560d93177634882ff117b35deab4"></a>

```c
#define BT_UUID_GATT_ACTETD BT_UUID_DECLARE_16(BT_UUID_GATT_ACTETD_VAL)
```

相关声明：[BT_UUID_GATT_ACTETD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5a15560d93177634882ff117b35deab4)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ACTETD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga165c63f8c91f61a9930b3c804f7051b7)。

GATT 广播恒定音调扩展发送时长特征（GATT Characteristic Advertising Constant Tone Extension Transmit Duration）。

<a id="r_ga3be14ce89c7c291cdde2bf1f4ce85808"></a>

```c
#define BT_UUID_GATT_ACTEI_VAL 0x2bb1
```

相关声明：[BT_UUID_GATT_ACTEI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3be14ce89c7c291cdde2bf1f4ce85808)。

GATT 广播恒定音调扩展间隔特征（GATT Characteristic Advertising Constant Tone Extension Interval）的 UUID 值。

<a id="r_ga492d6a8c673f4df65d34abad342f4e75"></a>

```c
#define BT_UUID_GATT_ACTEI BT_UUID_DECLARE_16(BT_UUID_GATT_ACTEI_VAL)
```

相关声明：[BT_UUID_GATT_ACTEI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga492d6a8c673f4df65d34abad342f4e75)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ACTEI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3be14ce89c7c291cdde2bf1f4ce85808)。

GATT 广播恒定音调扩展间隔特征（GATT Characteristic Advertising Constant Tone Extension Interval）。

<a id="r_gac32badacbe9099b6f00d5c3d780cdbfe"></a>

```c
#define BT_UUID_GATT_ACTEP_VAL 0x2bb2
```

相关声明：[BT_UUID_GATT_ACTEP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac32badacbe9099b6f00d5c3d780cdbfe)。

GATT 广播恒定音调扩展物理层特征（GATT Characteristic Advertising Constant Tone Extension PHY）的 UUID 值。

<a id="r_gaff802fc0d7358acf3bd4bf3209d7aa15"></a>

```c
#define BT_UUID_GATT_ACTEP BT_UUID_DECLARE_16(BT_UUID_GATT_ACTEP_VAL)
```

相关声明：[BT_UUID_GATT_ACTEP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaff802fc0d7358acf3bd4bf3209d7aa15)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ACTEP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac32badacbe9099b6f00d5c3d780cdbfe)。

GATT 广播恒定音调扩展物理层特征（GATT Characteristic Advertising Constant Tone Extension PHY）。

<a id="r_gaca347be4dd1f019c5d7421d7c2c0dd29"></a>

```c
#define BT_UUID_TBS_PROVIDER_NAME_VAL 0x2bb3
```

相关声明：[BT_UUID_TBS_PROVIDER_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaca347be4dd1f019c5d7421d7c2c0dd29)。

承载提供者名称值（Bearer Provider Name value）。

<a id="r_gafaff1ecd49123fab18bce167342a0d3e"></a>

```c
#define BT_UUID_TBS_PROVIDER_NAME BT_UUID_DECLARE_16(BT_UUID_TBS_PROVIDER_NAME_VAL)
```

相关声明：[BT_UUID_TBS_PROVIDER_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafaff1ecd49123fab18bce167342a0d3e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TBS_PROVIDER_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaca347be4dd1f019c5d7421d7c2c0dd29)。

承载提供者名称（Bearer Provider Name）。

<a id="r_ga361ef37fd71a78544ffcbfd34ecbff6f"></a>

```c
#define BT_UUID_TBS_UCI_VAL 0x2bb4
```

相关声明：[BT_UUID_TBS_UCI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga361ef37fd71a78544ffcbfd34ecbff6f)。

承载统一呼叫标识符 UCI 值（Bearer UCI value）。

<a id="r_ga2d4349fc96395f603cada574841a90d2"></a>

```c
#define BT_UUID_TBS_UCI BT_UUID_DECLARE_16(BT_UUID_TBS_UCI_VAL)
```

相关声明：[BT_UUID_TBS_UCI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2d4349fc96395f603cada574841a90d2)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TBS_UCI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga361ef37fd71a78544ffcbfd34ecbff6f)。

承载统一呼叫标识符 UCI（Bearer UCI）。

<a id="r_ga066546cd6eb07098643b0fa331b813d3"></a>

```c
#define BT_UUID_TBS_TECHNOLOGY_VAL 0x2bb5
```

相关声明：[BT_UUID_TBS_TECHNOLOGY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga066546cd6eb07098643b0fa331b813d3)。

承载技术值（Bearer Technology value）。

<a id="r_ga37ec4aed5afafc2751ef3902f2ef7d73"></a>

```c
#define BT_UUID_TBS_TECHNOLOGY BT_UUID_DECLARE_16(BT_UUID_TBS_TECHNOLOGY_VAL)
```

相关声明：[BT_UUID_TBS_TECHNOLOGY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga37ec4aed5afafc2751ef3902f2ef7d73)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TBS_TECHNOLOGY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga066546cd6eb07098643b0fa331b813d3)。

承载技术（Bearer Technology）。

<a id="r_ga5e499b3bcb22b0ddd719aba4fed5c644"></a>

```c
#define BT_UUID_TBS_URI_LIST_VAL 0x2bb6
```

相关声明：[BT_UUID_TBS_URI_LIST_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5e499b3bcb22b0ddd719aba4fed5c644)。

承载支持的 URI 前缀列表值（Bearer URI Prefixes Supported List value）。

<a id="r_ga6c76f72b427694a1e1180b0d2a2adb38"></a>

```c
#define BT_UUID_TBS_URI_LIST BT_UUID_DECLARE_16(BT_UUID_TBS_URI_LIST_VAL)
```

相关声明：[BT_UUID_TBS_URI_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6c76f72b427694a1e1180b0d2a2adb38)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TBS_URI_LIST_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5e499b3bcb22b0ddd719aba4fed5c644)。

承载支持的 URI 前缀列表（Bearer URI Prefixes Supported List）。

<a id="r_ga44859b71e874ca148e708fde37882c4b"></a>

```c
#define BT_UUID_TBS_SIGNAL_STRENGTH_VAL 0x2bb7
```

相关声明：[BT_UUID_TBS_SIGNAL_STRENGTH_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga44859b71e874ca148e708fde37882c4b)。

承载信号强度值（Bearer Signal Strength value）。

<a id="r_gaf5ebde9e6e4121909d8a165dee7fda3a"></a>

```c
#define BT_UUID_TBS_SIGNAL_STRENGTH BT_UUID_DECLARE_16(BT_UUID_TBS_SIGNAL_STRENGTH_VAL)
```

相关声明：[BT_UUID_TBS_SIGNAL_STRENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf5ebde9e6e4121909d8a165dee7fda3a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TBS_SIGNAL_STRENGTH_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga44859b71e874ca148e708fde37882c4b)。

承载信号强度（Bearer Signal Strength）。

<a id="r_ga726edee9ad2a92f2a5687a3320f68f99"></a>

```c
#define BT_UUID_TBS_SIGNAL_INTERVAL_VAL 0x2bb8
```

相关声明：[BT_UUID_TBS_SIGNAL_INTERVAL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga726edee9ad2a92f2a5687a3320f68f99)。

承载信号强度报告间隔值（Bearer Signal Strength Reporting Interval value）。

<a id="r_ga189f78c9eb6829851ab0497a0e6e3f51"></a>

```c
#define BT_UUID_TBS_SIGNAL_INTERVAL BT_UUID_DECLARE_16(BT_UUID_TBS_SIGNAL_INTERVAL_VAL)
```

相关声明：[BT_UUID_TBS_SIGNAL_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga189f78c9eb6829851ab0497a0e6e3f51)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TBS_SIGNAL_INTERVAL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga726edee9ad2a92f2a5687a3320f68f99)。

承载信号强度报告间隔（Bearer Signal Strength Reporting Interval）。

<a id="r_ga1fcc7e36b3ca482eca7572c77fe3bba4"></a>

```c
#define BT_UUID_TBS_LIST_CURRENT_CALLS_VAL 0x2bb9
```

相关声明：[BT_UUID_TBS_LIST_CURRENT_CALLS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1fcc7e36b3ca482eca7572c77fe3bba4)。

承载当前呼叫列表值（Bearer List Current Calls value）。

<a id="r_gaa5aea84109af0027aae9829169ab7789"></a>

```c
#define BT_UUID_TBS_LIST_CURRENT_CALLS BT_UUID_DECLARE_16(BT_UUID_TBS_LIST_CURRENT_CALLS_VAL)
```

相关声明：[BT_UUID_TBS_LIST_CURRENT_CALLS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa5aea84109af0027aae9829169ab7789)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TBS_LIST_CURRENT_CALLS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1fcc7e36b3ca482eca7572c77fe3bba4)。

承载当前呼叫列表（Bearer List Current Calls）。

<a id="r_ga01899f1d2f5ec81669b5012ab1448e5b"></a>

```c
#define BT_UUID_CCID_VAL 0x2bba
```

相关声明：[BT_UUID_CCID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga01899f1d2f5ec81669b5012ab1448e5b)。

内容控制标识符值（Content Control ID value）。

<a id="r_gab76981ff7b5fe1949c606e901daa33d3"></a>

```c
#define BT_UUID_CCID BT_UUID_DECLARE_16(BT_UUID_CCID_VAL)
```

相关声明：[BT_UUID_CCID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab76981ff7b5fe1949c606e901daa33d3)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CCID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga01899f1d2f5ec81669b5012ab1448e5b)。

内容控制标识符（Content Control ID）。

<a id="r_ga250a14189efd3cc176ae159de0ab03ed"></a>

```c
#define BT_UUID_TBS_STATUS_FLAGS_VAL 0x2bbb
```

相关声明：[BT_UUID_TBS_STATUS_FLAGS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga250a14189efd3cc176ae159de0ab03ed)。

状态标志值（Status flags value）。

<a id="r_ga8f465ca9874ff4889614f13fa7057c87"></a>

```c
#define BT_UUID_TBS_STATUS_FLAGS BT_UUID_DECLARE_16(BT_UUID_TBS_STATUS_FLAGS_VAL)
```

相关声明：[BT_UUID_TBS_STATUS_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8f465ca9874ff4889614f13fa7057c87)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TBS_STATUS_FLAGS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga250a14189efd3cc176ae159de0ab03ed)。

状态标志（Status flags）。

<a id="r_ga89ec945699c44fbbb220fa6798efa986"></a>

```c
#define BT_UUID_TBS_INCOMING_URI_VAL 0x2bbc
```

相关声明：[BT_UUID_TBS_INCOMING_URI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga89ec945699c44fbbb220fa6798efa986)。

来电目标呼叫者标识符值（Incoming Call Target Caller ID value）。

<a id="r_gaa11ae7df9db3a1a3576a413db9d70539"></a>

```c
#define BT_UUID_TBS_INCOMING_URI BT_UUID_DECLARE_16(BT_UUID_TBS_INCOMING_URI_VAL)
```

相关声明：[BT_UUID_TBS_INCOMING_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa11ae7df9db3a1a3576a413db9d70539)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TBS_INCOMING_URI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga89ec945699c44fbbb220fa6798efa986)。

来电目标呼叫者标识符（Incoming Call Target Caller ID）。

<a id="r_ga07adb1e98dfdeaa84efeb28a53087286"></a>

```c
#define BT_UUID_TBS_CALL_STATE_VAL 0x2bbd
```

相关声明：[BT_UUID_TBS_CALL_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga07adb1e98dfdeaa84efeb28a53087286)。

呼叫状态值（Call State value）。

<a id="r_gaf3c8e758416d2d7d34adb4be895f1ed0"></a>

```c
#define BT_UUID_TBS_CALL_STATE BT_UUID_DECLARE_16(BT_UUID_TBS_CALL_STATE_VAL)
```

相关声明：[BT_UUID_TBS_CALL_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf3c8e758416d2d7d34adb4be895f1ed0)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TBS_CALL_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga07adb1e98dfdeaa84efeb28a53087286)。

呼叫状态（Call State）。

<a id="r_gadc6f999aa7d3ebc821405bac4ed4bf35"></a>

```c
#define BT_UUID_TBS_CALL_CONTROL_POINT_VAL 0x2bbe
```

相关声明：[BT_UUID_TBS_CALL_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadc6f999aa7d3ebc821405bac4ed4bf35)。

呼叫控制点值（Call Control Point value）。

<a id="r_ga9870653514120a07d85e4ea4f0a83f6e"></a>

```c
#define BT_UUID_TBS_CALL_CONTROL_POINT BT_UUID_DECLARE_16(BT_UUID_TBS_CALL_CONTROL_POINT_VAL)
```

相关声明：[BT_UUID_TBS_CALL_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9870653514120a07d85e4ea4f0a83f6e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TBS_CALL_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadc6f999aa7d3ebc821405bac4ed4bf35)。

呼叫控制点（Call Control Point）。

<a id="r_ga0e2f14bde4f81d44bdd4171e1bfae68e"></a>

```c
#define BT_UUID_TBS_OPTIONAL_OPCODES_VAL 0x2bbf
```

相关声明：[BT_UUID_TBS_OPTIONAL_OPCODES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0e2f14bde4f81d44bdd4171e1bfae68e)。

可选操作码值（Optional Opcodes value）。

<a id="r_ga9c794c63e6c216b9a4a7518207ea7268"></a>

```c
#define BT_UUID_TBS_OPTIONAL_OPCODES BT_UUID_DECLARE_16(BT_UUID_TBS_OPTIONAL_OPCODES_VAL)
```

相关声明：[BT_UUID_TBS_OPTIONAL_OPCODES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9c794c63e6c216b9a4a7518207ea7268)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TBS_OPTIONAL_OPCODES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0e2f14bde4f81d44bdd4171e1bfae68e)。

可选操作码（Optional Opcodes）。

<a id="r_gab146e7f4f8b965634967ea7845a7d875"></a>

```c
#define BT_UUID_TBS_TERMINATE_REASON_VAL 0x2bc0
```

相关声明：[BT_UUID_TBS_TERMINATE_REASON_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab146e7f4f8b965634967ea7845a7d875)。

电话承载服务终止原因 UUID 数值常量（BT_UUID_TBS_TERMINATE_REASON_VAL）。

<a id="r_ga5eb69cfa65d293421bd2f6797cf1bdd0"></a>

```c
#define BT_UUID_TBS_TERMINATE_REASON BT_UUID_DECLARE_16(BT_UUID_TBS_TERMINATE_REASON_VAL)
```

相关声明：[BT_UUID_TBS_TERMINATE_REASON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5eb69cfa65d293421bd2f6797cf1bdd0)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TBS_TERMINATE_REASON_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab146e7f4f8b965634967ea7845a7d875)。

电话承载服务终止原因 UUID 常量（BT_UUID_TBS_TERMINATE_REASON）。

<a id="r_gaee6b14bcbd32f18efc4d7f805455deb1"></a>

```c
#define BT_UUID_TBS_INCOMING_CALL_VAL 0x2bc1
```

相关声明：[BT_UUID_TBS_INCOMING_CALL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaee6b14bcbd32f18efc4d7f805455deb1)。

来电值（Incoming Call value）。

<a id="r_ga4ec4bdf60129003573b79f8ffe993f20"></a>

```c
#define BT_UUID_TBS_INCOMING_CALL BT_UUID_DECLARE_16(BT_UUID_TBS_INCOMING_CALL_VAL)
```

相关声明：[BT_UUID_TBS_INCOMING_CALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4ec4bdf60129003573b79f8ffe993f20)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TBS_INCOMING_CALL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaee6b14bcbd32f18efc4d7f805455deb1)。

来电（Incoming Call）。

<a id="r_ga598672b6e2aa0bc58c62ac9755aaf64c"></a>

```c
#define BT_UUID_TBS_FRIENDLY_NAME_VAL 0x2bc2
```

相关声明：[BT_UUID_TBS_FRIENDLY_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga598672b6e2aa0bc58c62ac9755aaf64c)。

来电友好名称值（Incoming Call Friendly name value）。

<a id="r_ga32682d7390ccb0aafd82b57255007749"></a>

```c
#define BT_UUID_TBS_FRIENDLY_NAME BT_UUID_DECLARE_16(BT_UUID_TBS_FRIENDLY_NAME_VAL)
```

相关声明：[BT_UUID_TBS_FRIENDLY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga32682d7390ccb0aafd82b57255007749)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TBS_FRIENDLY_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga598672b6e2aa0bc58c62ac9755aaf64c)。

来电友好名称（Incoming Call Friendly name）。

<a id="r_ga24667ed9a87ae7f1b529cfea8515b7f3"></a>

```c
#define BT_UUID_MICS_MUTE_VAL 0x2bc3
```

相关声明：[BT_UUID_MICS_MUTE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga24667ed9a87ae7f1b529cfea8515b7f3)。

麦克风控制服务静音值（Microphone Control Service Mute value）。

<a id="r_gada38c5574c186c19c71788d612bb7987"></a>

```c
#define BT_UUID_MICS_MUTE BT_UUID_DECLARE_16(BT_UUID_MICS_MUTE_VAL)
```

相关声明：[BT_UUID_MICS_MUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gada38c5574c186c19c71788d612bb7987)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MICS_MUTE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga24667ed9a87ae7f1b529cfea8515b7f3)。

麦克风控制服务静音（Microphone Control Service Mute）。

<a id="r_ga780a810da56da9b9dbba775305f70c69"></a>

```c
#define BT_UUID_ASCS_ASE_SNK_VAL 0x2bc4
```

相关声明：[BT_UUID_ASCS_ASE_SNK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga780a810da56da9b9dbba775305f70c69)。

音频流接收端点特征值（Audio Stream Endpoint Sink Characteristic value）。

<a id="r_ga6542839cbcda51b512d04f1039840964"></a>

```c
#define BT_UUID_ASCS_ASE_SNK BT_UUID_DECLARE_16(BT_UUID_ASCS_ASE_SNK_VAL)
```

相关声明：[BT_UUID_ASCS_ASE_SNK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6542839cbcda51b512d04f1039840964)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_ASCS_ASE_SNK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga780a810da56da9b9dbba775305f70c69)。

音频流接收端点特征（Audio Stream Endpoint Sink Characteristic）。

<a id="r_gace1bd537f3ecee4715efde2b68ebce70"></a>

```c
#define BT_UUID_ASCS_ASE_SRC_VAL 0x2bc5
```

相关声明：[BT_UUID_ASCS_ASE_SRC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gace1bd537f3ecee4715efde2b68ebce70)。

音频流发送端点特征值（Audio Stream Endpoint Source Characteristic value）。

<a id="r_gae520d2f81b0ee284d42e80854217c209"></a>

```c
#define BT_UUID_ASCS_ASE_SRC BT_UUID_DECLARE_16(BT_UUID_ASCS_ASE_SRC_VAL)
```

相关声明：[BT_UUID_ASCS_ASE_SRC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae520d2f81b0ee284d42e80854217c209)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_ASCS_ASE_SRC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gace1bd537f3ecee4715efde2b68ebce70)。

音频流发送端点特征（Audio Stream Endpoint Source Characteristic）。

<a id="r_ga6eeb6b573908fe77254894cf3efc5378"></a>

```c
#define BT_UUID_ASCS_ASE_CP_VAL 0x2bc6
```

相关声明：[BT_UUID_ASCS_ASE_CP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6eeb6b573908fe77254894cf3efc5378)。

音频流端点控制点特征值（Audio Stream Endpoint Control Point Characteristic value）。

<a id="r_ga79416b6f0e79ee43bf9b495ec94cca4b"></a>

```c
#define BT_UUID_ASCS_ASE_CP BT_UUID_DECLARE_16(BT_UUID_ASCS_ASE_CP_VAL)
```

相关声明：[BT_UUID_ASCS_ASE_CP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga79416b6f0e79ee43bf9b495ec94cca4b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_ASCS_ASE_CP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6eeb6b573908fe77254894cf3efc5378)。

音频流端点控制点特征（Audio Stream Endpoint Control Point Characteristic）。

<a id="r_gad66cb5c49c932d3546fb549c6febeaa0"></a>

```c
#define BT_UUID_BASS_CONTROL_POINT_VAL 0x2bc7
```

相关声明：[BT_UUID_BASS_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad66cb5c49c932d3546fb549c6febeaa0)。

广播音频扫描服务扫描状态值（Broadcast Audio Scan Service Scan State value）。

<a id="r_ga4d8a9467cf5fce4f6be36d160075984c"></a>

```c
#define BT_UUID_BASS_CONTROL_POINT BT_UUID_DECLARE_16(BT_UUID_BASS_CONTROL_POINT_VAL)
```

相关声明：[BT_UUID_BASS_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4d8a9467cf5fce4f6be36d160075984c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BASS_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad66cb5c49c932d3546fb549c6febeaa0)。

广播音频扫描服务扫描状态（Broadcast Audio Scan Service Scan State）。

<a id="r_ga6c69b13ecbcca8121e6bbe49b58eb799"></a>

```c
#define BT_UUID_BASS_RECV_STATE_VAL 0x2bc8
```

相关声明：[BT_UUID_BASS_RECV_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6c69b13ecbcca8121e6bbe49b58eb799)。

广播音频扫描服务接收状态值（Broadcast Audio Scan Service Receive State value）。

<a id="r_ga384b5b68bff445f353762e1e15d85aa4"></a>

```c
#define BT_UUID_BASS_RECV_STATE BT_UUID_DECLARE_16(BT_UUID_BASS_RECV_STATE_VAL)
```

相关声明：[BT_UUID_BASS_RECV_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga384b5b68bff445f353762e1e15d85aa4)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BASS_RECV_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6c69b13ecbcca8121e6bbe49b58eb799)。

广播音频扫描服务接收状态（Broadcast Audio Scan Service Receive State）。

<a id="r_gac27fec8eb7a757709f647cbaf5b9735f"></a>

```c
#define BT_UUID_PACS_SNK_VAL 0x2bc9
```

相关声明：[BT_UUID_PACS_SNK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac27fec8eb7a757709f647cbaf5b9735f)。

接收端已发布音频能力 PAC 特征值（Sink PAC Characteristic value）。

<a id="r_gaf103bb8e2866a7ab7df90f8b62d4edcd"></a>

```c
#define BT_UUID_PACS_SNK BT_UUID_DECLARE_16(BT_UUID_PACS_SNK_VAL)
```

相关声明：[BT_UUID_PACS_SNK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf103bb8e2866a7ab7df90f8b62d4edcd)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_PACS_SNK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac27fec8eb7a757709f647cbaf5b9735f)。

接收端已发布音频能力 PAC 特征（Sink PAC Characteristic）。

<a id="r_ga3df681f24778459df49c4f2e8cae6c4b"></a>

```c
#define BT_UUID_PACS_SNK_LOC_VAL 0x2bca
```

相关声明：[BT_UUID_PACS_SNK_LOC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3df681f24778459df49c4f2e8cae6c4b)。

接收端 PAC 位置特征值（Sink PAC Locations Characteristic value）。

<a id="r_gab54021bccf67751069b0cf5eaef8c61c"></a>

```c
#define BT_UUID_PACS_SNK_LOC BT_UUID_DECLARE_16(BT_UUID_PACS_SNK_LOC_VAL)
```

相关声明：[BT_UUID_PACS_SNK_LOC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab54021bccf67751069b0cf5eaef8c61c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_PACS_SNK_LOC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3df681f24778459df49c4f2e8cae6c4b)。

接收端 PAC 位置特征（Sink PAC Locations Characteristic）。

<a id="r_gaa7c87310bea3593a8097fa20ec4c2c88"></a>

```c
#define BT_UUID_PACS_SRC_VAL 0x2bcb
```

相关声明：[BT_UUID_PACS_SRC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa7c87310bea3593a8097fa20ec4c2c88)。

发送端已发布音频能力 PAC 特征值（Source PAC Characteristic value）。

<a id="r_ga958e64cfd0f6b21095b2de28f3b4a0ee"></a>

```c
#define BT_UUID_PACS_SRC BT_UUID_DECLARE_16(BT_UUID_PACS_SRC_VAL)
```

相关声明：[BT_UUID_PACS_SRC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga958e64cfd0f6b21095b2de28f3b4a0ee)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_PACS_SRC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa7c87310bea3593a8097fa20ec4c2c88)。

发送端已发布音频能力 PAC 特征（Source PAC Characteristic）。

<a id="r_ga13eee95752b5b248888ad0328c2c7f99"></a>

```c
#define BT_UUID_PACS_SRC_LOC_VAL 0x2bcc
```

相关声明：[BT_UUID_PACS_SRC_LOC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga13eee95752b5b248888ad0328c2c7f99)。

发送端 PAC 位置特征值（Source PAC Locations Characteristic value）。

<a id="r_ga0c89cb848378466beba18c389286cac7"></a>

```c
#define BT_UUID_PACS_SRC_LOC BT_UUID_DECLARE_16(BT_UUID_PACS_SRC_LOC_VAL)
```

相关声明：[BT_UUID_PACS_SRC_LOC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0c89cb848378466beba18c389286cac7)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_PACS_SRC_LOC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga13eee95752b5b248888ad0328c2c7f99)。

发送端 PAC 位置特征（Source PAC Locations Characteristic）。

<a id="r_ga64798749d367c63e3d9ed2d07a236e37"></a>

```c
#define BT_UUID_PACS_AVAILABLE_CONTEXT_VAL 0x2bcd
```

相关声明：[BT_UUID_PACS_AVAILABLE_CONTEXT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga64798749d367c63e3d9ed2d07a236e37)。

可用音频上下文特征值（Available Audio Contexts Characteristic value）。

<a id="r_ga0017f4e6621ba40e51062b8f7c77a634"></a>

```c
#define BT_UUID_PACS_AVAILABLE_CONTEXT BT_UUID_DECLARE_16(BT_UUID_PACS_AVAILABLE_CONTEXT_VAL)
```

相关声明：[BT_UUID_PACS_AVAILABLE_CONTEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0017f4e6621ba40e51062b8f7c77a634)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_PACS_AVAILABLE_CONTEXT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga64798749d367c63e3d9ed2d07a236e37)。

可用音频上下文特征（Available Audio Contexts Characteristic）。

<a id="r_ga63588c6624da5cba5b53e07c869c16ff"></a>

```c
#define BT_UUID_PACS_SUPPORTED_CONTEXT_VAL 0x2bce
```

相关声明：[BT_UUID_PACS_SUPPORTED_CONTEXT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga63588c6624da5cba5b53e07c869c16ff)。

支持的音频上下文特征值（Supported Audio Context Characteristic value）。

<a id="r_ga4f61367e2c6aeac35f2054759389306b"></a>

```c
#define BT_UUID_PACS_SUPPORTED_CONTEXT BT_UUID_DECLARE_16(BT_UUID_PACS_SUPPORTED_CONTEXT_VAL)
```

相关声明：[BT_UUID_PACS_SUPPORTED_CONTEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4f61367e2c6aeac35f2054759389306b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_PACS_SUPPORTED_CONTEXT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga63588c6624da5cba5b53e07c869c16ff)。

支持的音频上下文特征（Supported Audio Context Characteristic）。

<a id="r_ga68bf0922cd7486337b912f8cce89140d"></a>

```c
#define BT_UUID_GATT_NH4CONC_VAL 0x2bcf
```

相关声明：[BT_UUID_GATT_NH4CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga68bf0922cd7486337b912f8cce89140d)。

GATT 氨浓度特征（GATT Characteristic Ammonia Concentration）的 UUID 值。

<a id="r_ga7204a371be3fb10d382ea00bc76b5102"></a>

```c
#define BT_UUID_GATT_NH4CONC BT_UUID_DECLARE_16(BT_UUID_GATT_NH4CONC_VAL)
```

相关声明：[BT_UUID_GATT_NH4CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7204a371be3fb10d382ea00bc76b5102)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_NH4CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga68bf0922cd7486337b912f8cce89140d)。

GATT 氨浓度特征（GATT Characteristic Ammonia Concentration）。

<a id="r_ga397cccc077652fe327b7ceab3ccc1f4d"></a>

```c
#define BT_UUID_GATT_COCONC_VAL 0x2bd0
```

相关声明：[BT_UUID_GATT_COCONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga397cccc077652fe327b7ceab3ccc1f4d)。

GATT 一氧化碳浓度特征（GATT Characteristic Carbon Monoxide Concentration）的 UUID 值。

<a id="r_gab599f83b69654c1b3be91429d9f7bf32"></a>

```c
#define BT_UUID_GATT_COCONC BT_UUID_DECLARE_16(BT_UUID_GATT_COCONC_VAL)
```

相关声明：[BT_UUID_GATT_COCONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab599f83b69654c1b3be91429d9f7bf32)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_COCONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga397cccc077652fe327b7ceab3ccc1f4d)。

GATT 一氧化碳浓度特征（GATT Characteristic Carbon Monoxide Concentration）。

<a id="r_ga13ecd6003180e0ed73d7aa80542dddd6"></a>

```c
#define BT_UUID_GATT_CH4CONC_VAL 0x2bd1
```

相关声明：[BT_UUID_GATT_CH4CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga13ecd6003180e0ed73d7aa80542dddd6)。

GATT 甲烷浓度特征（GATT Characteristic Methane Concentration）的 UUID 值。

<a id="r_gad0496cbb8cf296852fe85b7694c1e3a8"></a>

```c
#define BT_UUID_GATT_CH4CONC BT_UUID_DECLARE_16(BT_UUID_GATT_CH4CONC_VAL)
```

相关声明：[BT_UUID_GATT_CH4CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad0496cbb8cf296852fe85b7694c1e3a8)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_CH4CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga13ecd6003180e0ed73d7aa80542dddd6)。

GATT 甲烷浓度特征（GATT Characteristic Methane Concentration）。

<a id="r_ga37fdb9197c3003175875337df66c0937"></a>

```c
#define BT_UUID_GATT_NO2CONC_VAL 0x2bd2
```

相关声明：[BT_UUID_GATT_NO2CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga37fdb9197c3003175875337df66c0937)。

GATT 二氧化氮浓度特征（GATT Characteristic Nitrogen Dioxide Concentration）的 UUID 值。

<a id="r_ga1a0f1553bbf70517af224fd32a5842f6"></a>

```c
#define BT_UUID_GATT_NO2CONC BT_UUID_DECLARE_16(BT_UUID_GATT_NO2CONC_VAL)
```

相关声明：[BT_UUID_GATT_NO2CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1a0f1553bbf70517af224fd32a5842f6)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_NO2CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga37fdb9197c3003175875337df66c0937)。

GATT 二氧化氮浓度特征（GATT Characteristic Nitrogen Dioxide Concentration）。

<a id="r_ga2023c3c8c4fdf714a66dc64984a9f198"></a>

```c
#define BT_UUID_GATT_NONCH4CONC_VAL 0x2bd3
```

相关声明：[BT_UUID_GATT_NONCH4CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2023c3c8c4fdf714a66dc64984a9f198)。

GATT 非甲烷挥发性有机化合物浓度特征（GATT Characteristic Non-Methane Volatile Organic Compounds Concentration）的 UUID 值。

<a id="r_ga6770e5f7e2f46c604ada573dd8b950e9"></a>

```c
#define BT_UUID_GATT_NONCH4CONC BT_UUID_DECLARE_16(BT_UUID_GATT_NONCH4CONC_VAL)
```

相关声明：[BT_UUID_GATT_NONCH4CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6770e5f7e2f46c604ada573dd8b950e9)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_NONCH4CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2023c3c8c4fdf714a66dc64984a9f198)。

GATT 非甲烷挥发性有机化合物浓度特征（GATT Characteristic Non-Methane Volatile Organic Compounds Concentration）。

<a id="r_ga4a022ea0079ebc09dedf5f472a8755ee"></a>

```c
#define BT_UUID_GATT_O3CONC_VAL 0x2bd4
```

相关声明：[BT_UUID_GATT_O3CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4a022ea0079ebc09dedf5f472a8755ee)。

GATT 臭氧浓度特征（GATT Characteristic Ozone Concentration）的 UUID 值。

<a id="r_ga23054b696f62c03afb73a0f5286dc2d5"></a>

```c
#define BT_UUID_GATT_O3CONC BT_UUID_DECLARE_16(BT_UUID_GATT_O3CONC_VAL)
```

相关声明：[BT_UUID_GATT_O3CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga23054b696f62c03afb73a0f5286dc2d5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_O3CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4a022ea0079ebc09dedf5f472a8755ee)。

GATT 臭氧浓度特征（GATT Characteristic Ozone Concentration）。

<a id="r_ga8dde1677ff60c1970c427e9b984e24d9"></a>

```c
#define BT_UUID_GATT_PM1CONC_VAL 0x2bd5
```

相关声明：[BT_UUID_GATT_PM1CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8dde1677ff60c1970c427e9b984e24d9)。

GATT PM1 颗粒物浓度特征（GATT Characteristic Particulate Matter - PM1 Concentration）的 UUID 值。

<a id="r_ga9c39a445bab4603148d4256bcce23a5b"></a>

```c
#define BT_UUID_GATT_PM1CONC BT_UUID_DECLARE_16(BT_UUID_GATT_PM1CONC_VAL)
```

相关声明：[BT_UUID_GATT_PM1CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9c39a445bab4603148d4256bcce23a5b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_PM1CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8dde1677ff60c1970c427e9b984e24d9)。

GATT PM1 颗粒物浓度特征（GATT Characteristic Particulate Matter - PM1 Concentration）。

<a id="r_ga055b7900ffda40c9ec4e1870abc1d855"></a>

```c
#define BT_UUID_GATT_PM25CONC_VAL 0x2bd6
```

相关声明：[BT_UUID_GATT_PM25CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga055b7900ffda40c9ec4e1870abc1d855)。

GATT PM2.5 颗粒物浓度特征（GATT Characteristic Particulate Matter - PM2.5 Concentration）的 UUID 值。

<a id="r_ga88d2f1f4afcb89267c713144f84f4f7f"></a>

```c
#define BT_UUID_GATT_PM25CONC BT_UUID_DECLARE_16(BT_UUID_GATT_PM25CONC_VAL)
```

相关声明：[BT_UUID_GATT_PM25CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga88d2f1f4afcb89267c713144f84f4f7f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_PM25CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga055b7900ffda40c9ec4e1870abc1d855)。

GATT PM2.5 颗粒物浓度特征（GATT Characteristic Particulate Matter - PM2.5 Concentration）。

<a id="r_gaebebc238d90e667f33d2c95690d67376"></a>

```c
#define BT_UUID_GATT_PM10CONC_VAL 0x2bd7
```

相关声明：[BT_UUID_GATT_PM10CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaebebc238d90e667f33d2c95690d67376)。

GATT PM10 颗粒物浓度特征（GATT Characteristic Particulate Matter - PM10 Concentration）的 UUID 值。

<a id="r_ga9668baee783462813c530f411da07890"></a>

```c
#define BT_UUID_GATT_PM10CONC BT_UUID_DECLARE_16(BT_UUID_GATT_PM10CONC_VAL)
```

相关声明：[BT_UUID_GATT_PM10CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9668baee783462813c530f411da07890)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_PM10CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaebebc238d90e667f33d2c95690d67376)。

GATT PM10 颗粒物浓度特征（GATT Characteristic Particulate Matter - PM10 Concentration）。

<a id="r_gaf7ee2d08cd80e1d4afc777457217508d"></a>

```c
#define BT_UUID_GATT_SO2CONC_VAL 0x2bd8
```

相关声明：[BT_UUID_GATT_SO2CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf7ee2d08cd80e1d4afc777457217508d)。

GATT 二氧化硫浓度特征（GATT Characteristic Sulfur Dioxide Concentration）的 UUID 值。

<a id="r_ga3c7b7be6268bb748f7406737eaa129e2"></a>

```c
#define BT_UUID_GATT_SO2CONC BT_UUID_DECLARE_16(BT_UUID_GATT_SO2CONC_VAL)
```

相关声明：[BT_UUID_GATT_SO2CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3c7b7be6268bb748f7406737eaa129e2)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SO2CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf7ee2d08cd80e1d4afc777457217508d)。

GATT 二氧化硫浓度特征（GATT Characteristic Sulfur Dioxide Concentration）。

<a id="r_gaba0853f84e9e33dd4d7d71ecebc31bb6"></a>

```c
#define BT_UUID_GATT_SF6CONC_VAL 0x2bd9
```

相关声明：[BT_UUID_GATT_SF6CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaba0853f84e9e33dd4d7d71ecebc31bb6)。

GATT 六氟化硫浓度特征（GATT Characteristic Sulfur Hexafluoride Concentration）的 UUID 值。

<a id="r_gaf17d7037cdaed65e208df3792f1fd2d3"></a>

```c
#define BT_UUID_GATT_SF6CONC BT_UUID_DECLARE_16(BT_UUID_GATT_SF6CONC_VAL)
```

相关声明：[BT_UUID_GATT_SF6CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf17d7037cdaed65e208df3792f1fd2d3)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SF6CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaba0853f84e9e33dd4d7d71ecebc31bb6)。

GATT 六氟化硫浓度特征（GATT Characteristic Sulfur Hexafluoride Concentration）。

<a id="r_gad4967e4904cd371940af8b135da21f47"></a>

```c
#define BT_UUID_HAS_HEARING_AID_FEATURES_VAL 0x2bda
```

相关声明：[BT_UUID_HAS_HEARING_AID_FEATURES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad4967e4904cd371940af8b135da21f47)。

助听器功能特征值（Hearing Aid Features Characteristic value）。

<a id="r_gaebd2bbb103e6928059f1a76eac55916b"></a>

```c
#define BT_UUID_HAS_HEARING_AID_FEATURES BT_UUID_DECLARE_16(BT_UUID_HAS_HEARING_AID_FEATURES_VAL)
```

相关声明：[BT_UUID_HAS_HEARING_AID_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaebd2bbb103e6928059f1a76eac55916b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HAS_HEARING_AID_FEATURES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad4967e4904cd371940af8b135da21f47)。

助听器功能特征（Hearing Aid Features Characteristic）。

<a id="r_ga6fdc731a19072629917ce6ebf28c7fee"></a>

```c
#define BT_UUID_HAS_PRESET_CONTROL_POINT_VAL 0x2bdb
```

相关声明：[BT_UUID_HAS_PRESET_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6fdc731a19072629917ce6ebf28c7fee)。

助听器预设控制点特征值（Hearing Aid Preset Control Point Characteristic value）。

<a id="r_ga7f3a8eea9e7ee68d8865809a061a0e96"></a>

```c
#define BT_UUID_HAS_PRESET_CONTROL_POINT BT_UUID_DECLARE_16(BT_UUID_HAS_PRESET_CONTROL_POINT_VAL)
```

相关声明：[BT_UUID_HAS_PRESET_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7f3a8eea9e7ee68d8865809a061a0e96)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HAS_PRESET_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6fdc731a19072629917ce6ebf28c7fee)。

助听器预设控制点特征（Hearing Aid Preset Control Point Characteristic）。

<a id="r_gae9b2bf949e992c7cd6f1aaaa49888189"></a>

```c
#define BT_UUID_HAS_ACTIVE_PRESET_INDEX_VAL 0x2bdc
```

相关声明：[BT_UUID_HAS_ACTIVE_PRESET_INDEX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae9b2bf949e992c7cd6f1aaaa49888189)。

活动预设索引特征值（Active Preset Index Characteristic value）。

<a id="r_ga9ef9b65a7c9a105798691a2cdffbaf7a"></a>

```c
#define BT_UUID_HAS_ACTIVE_PRESET_INDEX BT_UUID_DECLARE_16(BT_UUID_HAS_ACTIVE_PRESET_INDEX_VAL)
```

相关声明：[BT_UUID_HAS_ACTIVE_PRESET_INDEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9ef9b65a7c9a105798691a2cdffbaf7a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HAS_ACTIVE_PRESET_INDEX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae9b2bf949e992c7cd6f1aaaa49888189)。

活动预设索引特征（Active Preset Index Characteristic）。

<a id="r_gac18b9e325ef1db22774f8da35b888223"></a>

```c
#define BT_UUID_GATT_FSTR64_VAL 0x2bde
```

相关声明：[BT_UUID_GATT_FSTR64_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac18b9e325ef1db22774f8da35b888223)。

GATT 定长字符串 64 特征（GATT Characteristic Fixed String 64）的 UUID 值。

<a id="r_gac617c317945f2b6d45de15eca1190823"></a>

```c
#define BT_UUID_GATT_FSTR64 BT_UUID_DECLARE_16(BT_UUID_GATT_FSTR64_VAL)
```

相关声明：[BT_UUID_GATT_FSTR64](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac617c317945f2b6d45de15eca1190823)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_FSTR64_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac18b9e325ef1db22774f8da35b888223)。

GATT 定长字符串 64 特征（GATT Characteristic Fixed String 64）。

<a id="r_ga2a3928912a6eed082deac4893fb4f980"></a>

```c
#define BT_UUID_GATT_HITEMP_VAL 0x2bdf
```

相关声明：[BT_UUID_GATT_HITEMP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2a3928912a6eed082deac4893fb4f980)。

GATT 高温特征（GATT Characteristic High Temperature）的 UUID 值。

<a id="r_ga8d9bad6c04ea4cf096d0d010208e1d2a"></a>

```c
#define BT_UUID_GATT_HITEMP BT_UUID_DECLARE_16(BT_UUID_GATT_HITEMP_VAL)
```

相关声明：[BT_UUID_GATT_HITEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8d9bad6c04ea4cf096d0d010208e1d2a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_HITEMP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2a3928912a6eed082deac4893fb4f980)。

GATT 高温特征（GATT Characteristic High Temperature）。

<a id="r_ga2b707ca8b876eded6b3adf9bb7132479"></a>

```c
#define BT_UUID_GATT_HV_VAL 0x2be0
```

相关声明：[BT_UUID_GATT_HV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2b707ca8b876eded6b3adf9bb7132479)。

GATT 高电压特征（GATT Characteristic High Voltage）的 UUID 值。

<a id="r_ga1104d7e9d1571aacdb77693c64a15edc"></a>

```c
#define BT_UUID_GATT_HV BT_UUID_DECLARE_16(BT_UUID_GATT_HV_VAL)
```

相关声明：[BT_UUID_GATT_HV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1104d7e9d1571aacdb77693c64a15edc)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_HV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2b707ca8b876eded6b3adf9bb7132479)。

GATT 高电压特征（GATT Characteristic High Voltage）。

<a id="r_ga67e534b02154fd7ff94b5ed21616f5f2"></a>

```c
#define BT_UUID_GATT_LD_VAL 0x2be1
```

相关声明：[BT_UUID_GATT_LD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga67e534b02154fd7ff94b5ed21616f5f2)。

GATT 光分布特征（GATT Characteristic Light Distribution）的 UUID 值。

<a id="r_ga5f68a688a1347d84bd28aa3df7252be9"></a>

```c
#define BT_UUID_GATT_LD BT_UUID_DECLARE_16(BT_UUID_GATT_LD_VAL)
```

相关声明：[BT_UUID_GATT_LD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5f68a688a1347d84bd28aa3df7252be9)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga67e534b02154fd7ff94b5ed21616f5f2)。

GATT 光分布特征（GATT Characteristic Light Distribution）。

<a id="r_gaa127fa12de6d6a641183641853439708"></a>

```c
#define BT_UUID_GATT_LO_VAL 0x2be2
```

相关声明：[BT_UUID_GATT_LO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa127fa12de6d6a641183641853439708)。

GATT 光输出特征（GATT Characteristic Light Output）的 UUID 值。

<a id="r_gacc7b122d7a849291a5c9c877acfbd50a"></a>

```c
#define BT_UUID_GATT_LO BT_UUID_DECLARE_16(BT_UUID_GATT_LO_VAL)
```

相关声明：[BT_UUID_GATT_LO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacc7b122d7a849291a5c9c877acfbd50a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa127fa12de6d6a641183641853439708)。

GATT 光输出特征（GATT Characteristic Light Output）。

<a id="r_ga34f9f97b35397e713f655b888845d443"></a>

```c
#define BT_UUID_GATT_LST_VAL 0x2be3
```

相关声明：[BT_UUID_GATT_LST_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga34f9f97b35397e713f655b888845d443)。

GATT 光源类型特征（GATT Characteristic Light Source Type）的 UUID 值。

<a id="r_ga2794fa8a9e1030826b4d382cc59f835a"></a>

```c
#define BT_UUID_GATT_LST BT_UUID_DECLARE_16(BT_UUID_GATT_LST_VAL)
```

相关声明：[BT_UUID_GATT_LST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2794fa8a9e1030826b4d382cc59f835a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_LST_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga34f9f97b35397e713f655b888845d443)。

GATT 光源类型特征（GATT Characteristic Light Source Type）。

<a id="r_gab3b7b78bfb8b5dfd30a1751ce9ffaee7"></a>

```c
#define BT_UUID_GATT_NOISE_VAL 0x2be4
```

相关声明：[BT_UUID_GATT_NOISE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab3b7b78bfb8b5dfd30a1751ce9ffaee7)。

GATT 噪声特征（GATT Characteristic Noise）的 UUID 值。

<a id="r_gaeb4d264b70d6d6c87a34f0da320f8e7a"></a>

```c
#define BT_UUID_GATT_NOISE BT_UUID_DECLARE_16(BT_UUID_GATT_NOISE_VAL)
```

相关声明：[BT_UUID_GATT_NOISE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaeb4d264b70d6d6c87a34f0da320f8e7a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_NOISE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab3b7b78bfb8b5dfd30a1751ce9ffaee7)。

GATT 噪声特征（GATT Characteristic Noise）。

<a id="r_ga8cbc0843565303e78f564517c21feb0f"></a>

```c
#define BT_UUID_GATT_RRCCTP_VAL 0x2be5
```

相关声明：[BT_UUID_GATT_RRCCTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8cbc0843565303e78f564517c21feb0f)。

GATT 相关色温范围内相对运行时间特征（GATT Characteristic Relative Runtime in a Correlated Color Temperature Range）的 UUID 值。

<a id="r_ga0f5bffe28d45d35fa2dc6680bc52476d"></a>

```c
#define BT_UUID_GATT_RRCCTR BT_UUID_DECLARE_16(BT_UUID_GATT_RRCCTR_VAL)
```

相关声明：[BT_UUID_GATT_RRCCTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0f5bffe28d45d35fa2dc6680bc52476d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)。

GATT 相关色温范围内相对运行时间特征（GATT Characteristic Relative Runtime in a Correlated Color Temperature Range）。

<a id="r_ga9fd1550589d248be145b120c446181ee"></a>

```c
#define BT_UUID_GATT_TIM_S32_VAL 0x2be6
```

相关声明：[BT_UUID_GATT_TIM_S32_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9fd1550589d248be145b120c446181ee)。

GATT 32 位秒时间特征（GATT Characteristic Time Second 32）的 UUID 值。

<a id="r_gac76fc378354bcd1a8c706f7438a90ebb"></a>

```c
#define BT_UUID_GATT_TIM_S32 BT_UUID_DECLARE_16(BT_UUID_GATT_TIM_S32_VAL)
```

相关声明：[BT_UUID_GATT_TIM_S32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac76fc378354bcd1a8c706f7438a90ebb)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_TIM_S32_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9fd1550589d248be145b120c446181ee)。

GATT 32 位秒时间特征（GATT Characteristic Time Second 32）。

<a id="r_gabf10e337b78be1ab371fbef771109c53"></a>

```c
#define BT_UUID_GATT_VOCCONC_VAL 0x2be7
```

相关声明：[BT_UUID_GATT_VOCCONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabf10e337b78be1ab371fbef771109c53)。

GATT 挥发性有机化合物 VOC 浓度特征（GATT Characteristic VOC Concentration）的 UUID 值。

<a id="r_ga7181f9f1dfaae6cfe3fd8cedd8c20917"></a>

```c
#define BT_UUID_GATT_VOCCONC BT_UUID_DECLARE_16(BT_UUID_GATT_VOCCONC_VAL)
```

相关声明：[BT_UUID_GATT_VOCCONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7181f9f1dfaae6cfe3fd8cedd8c20917)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_VOCCONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabf10e337b78be1ab371fbef771109c53)。

GATT 挥发性有机化合物 VOC 浓度特征（GATT Characteristic VOC Concentration）。

<a id="r_ga4c57416ae5e84133339e3fab0ba31918"></a>

```c
#define BT_UUID_GATT_VF_VAL 0x2be8
```

相关声明：[BT_UUID_GATT_VF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4c57416ae5e84133339e3fab0ba31918)。

GATT 电压频率特征（GATT Characteristic Voltage Frequency）的 UUID 值。

<a id="r_gae8500640959d58da51aee03fa75c85ba"></a>

```c
#define BT_UUID_GATT_VF BT_UUID_DECLARE_16(BT_UUID_GATT_VF_VAL)
```

相关声明：[BT_UUID_GATT_VF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae8500640959d58da51aee03fa75c85ba)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_VF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4c57416ae5e84133339e3fab0ba31918)。

GATT 电压频率特征（GATT Characteristic Voltage Frequency）。

<a id="r_gaad27c84d46c85c4fc436e2d57249e562"></a>

```c
#define BT_UUID_BAS_BATTERY_CRIT_STATUS_VAL 0x2be9
```

相关声明：[BT_UUID_BAS_BATTERY_CRIT_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaad27c84d46c85c4fc436e2d57249e562)。

BAS 电池临界状态特征（BAS Characteristic Battery Critical Status）的 UUID 值。

<a id="r_ga678d5e47dee2070ce9208538c529460b"></a>

```c
#define BT_UUID_BAS_BATTERY_CRIT_STATUS BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_CRIT_STATUS_VAL)
```

相关声明：[BT_UUID_BAS_BATTERY_CRIT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga678d5e47dee2070ce9208538c529460b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BAS_BATTERY_CRIT_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaad27c84d46c85c4fc436e2d57249e562)。

BAS 电池临界状态特征（BAS Characteristic Battery Critical Status）。

<a id="r_ga0dd78641b14fa1affa283f3f53a5f194"></a>

```c
#define BT_UUID_BAS_BATTERY_HEALTH_STATUS_VAL 0x2bea
```

相关声明：[BT_UUID_BAS_BATTERY_HEALTH_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0dd78641b14fa1affa283f3f53a5f194)。

BAS 电池健康状态特征（BAS Characteristic Battery Health Status）的 UUID 值。

<a id="r_gaa442c41b04c72f1a7a983e0c6561b90d"></a>

```c
#define BT_UUID_BAS_BATTERY_HEALTH_STATUS BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_HEALTH_STATUS_VAL)
```

相关声明：[BT_UUID_BAS_BATTERY_HEALTH_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa442c41b04c72f1a7a983e0c6561b90d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BAS_BATTERY_HEALTH_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0dd78641b14fa1affa283f3f53a5f194)。

BAS 电池健康状态特征（BAS Characteristic Battery Health Status）。

<a id="r_ga3324d4b7047cab8fb2c033c4c92c5793"></a>

```c
#define BT_UUID_BAS_BATTERY_HEALTH_INF_VAL 0x2beb
```

相关声明：[BT_UUID_BAS_BATTERY_HEALTH_INF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3324d4b7047cab8fb2c033c4c92c5793)。

BAS 电池健康信息特征（BAS Characteristic Battery Health Information）的 UUID 值。

<a id="r_ga62ad5685a1fcbb18afd57c7ded6463a0"></a>

```c
#define BT_UUID_BAS_BATTERY_HEALTH_INF BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_HEALTH_INF_VAL)
```

相关声明：[BT_UUID_BAS_BATTERY_HEALTH_INF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga62ad5685a1fcbb18afd57c7ded6463a0)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BAS_BATTERY_HEALTH_INF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3324d4b7047cab8fb2c033c4c92c5793)。

BAS 电池健康信息特征（BAS Characteristic Battery Health Information）。

<a id="r_ga04f0ff51790e2c759b401f36a989f6b7"></a>

```c
#define BT_UUID_BAS_BATTERY_INF_VAL 0x2bec
```

相关声明：[BT_UUID_BAS_BATTERY_INF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga04f0ff51790e2c759b401f36a989f6b7)。

BAS 电池信息特征（BAS Characteristic Battery Information）的 UUID 值。

<a id="r_gad6dffe9e9e9684b2a943471e0a6c0918"></a>

```c
#define BT_UUID_BAS_BATTERY_INF BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_INF_VAL)
```

相关声明：[BT_UUID_BAS_BATTERY_INF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad6dffe9e9e9684b2a943471e0a6c0918)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BAS_BATTERY_INF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga04f0ff51790e2c759b401f36a989f6b7)。

BAS 电池信息特征（BAS Characteristic Battery Information）。

<a id="r_gaf14fdc69148ba65b5fb7fe9d42706787"></a>

```c
#define BT_UUID_BAS_BATTERY_LEVEL_STATUS_VAL 0x2bed
```

相关声明：[BT_UUID_BAS_BATTERY_LEVEL_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf14fdc69148ba65b5fb7fe9d42706787)。

BAS 电池电量状态特征（BAS Characteristic Battery Level Status）的 UUID 值。

<a id="r_ga54a26381c17065abbda1eb4c2a35c244"></a>

```c
#define BT_UUID_BAS_BATTERY_LEVEL_STATUS BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_LEVEL_STATUS_VAL)
```

相关声明：[BT_UUID_BAS_BATTERY_LEVEL_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga54a26381c17065abbda1eb4c2a35c244)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BAS_BATTERY_LEVEL_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf14fdc69148ba65b5fb7fe9d42706787)。

BAS 电池电量状态特征（BAS Characteristic Battery Level Status）。

<a id="r_ga8a1d978914a8cb9c3744b4b333e38f46"></a>

```c
#define BT_UUID_BAS_BATTERY_TIME_STATUS_VAL 0x2bee
```

相关声明：[BT_UUID_BAS_BATTERY_TIME_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8a1d978914a8cb9c3744b4b333e38f46)。

BAS 电池时间状态特征（BAS Characteristic Battery Time Status）的 UUID 值。

<a id="r_ga25e2b1b84d5b9dd46ae79ab26752a02f"></a>

```c
#define BT_UUID_BAS_BATTERY_TIME_STATUS BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_TIME_STATUS_VAL)
```

相关声明：[BT_UUID_BAS_BATTERY_TIME_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga25e2b1b84d5b9dd46ae79ab26752a02f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BAS_BATTERY_TIME_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8a1d978914a8cb9c3744b4b333e38f46)。

BAS 电池时间状态特征（BAS Characteristic Battery Time Status）。

<a id="r_gaff547b9ef568ae7ae70fdb18cbced21b"></a>

```c
#define BT_UUID_GATT_ESD_VAL 0x2bef
```

相关声明：[BT_UUID_GATT_ESD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaff547b9ef568ae7ae70fdb18cbced21b)。

GATT 预计维护日期特征（GATT Characteristic Estimated Service Date）的 UUID 值。

<a id="r_ga432ba40acfbe03c50b4a3ede80b972c1"></a>

```c
#define BT_UUID_GATT_ESD BT_UUID_DECLARE_16(BT_UUID_GATT_ESD_VAL)
```

相关声明：[BT_UUID_GATT_ESD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga432ba40acfbe03c50b4a3ede80b972c1)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_ESD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaff547b9ef568ae7ae70fdb18cbced21b)。

GATT 预计维护日期特征（GATT Characteristic Estimated Service Date）。

<a id="r_ga7af8620512a789611a3c6c96bcbd6c06"></a>

```c
#define BT_UUID_BAS_BATTERY_ENERGY_STATUS_VAL 0x2bf0
```

相关声明：[BT_UUID_BAS_BATTERY_ENERGY_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7af8620512a789611a3c6c96bcbd6c06)。

BAS 电池能量状态特征（BAS Characteristic Battery Energy Status）的 UUID 值。

<a id="r_gadc442a139fff871f63d5e11be37c8231"></a>

```c
#define BT_UUID_BAS_BATTERY_ENERGY_STATUS BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_ENERGY_STATUS_VAL)
```

相关声明：[BT_UUID_BAS_BATTERY_ENERGY_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadc442a139fff871f63d5e11be37c8231)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BAS_BATTERY_ENERGY_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7af8620512a789611a3c6c96bcbd6c06)。

BAS 电池能量状态特征（BAS Characteristic Battery Energy Status）。

<a id="r_gaeb700085e464d9ee63350ec3fd06d6c7"></a>

```c
#define BT_UUID_ETS_CURRENT_ELAPSED_TIME_VAL 0x2bf2
```

相关声明：[BT_UUID_ETS_CURRENT_ELAPSED_TIME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaeb700085e464d9ee63350ec3fd06d6c7)。

ETS 当前经过时间特征（ETS Characteristic Current Elapsed Time）的 UUID 值。

<a id="r_gaf27d2fbbf83f1193a8d400dcba6f4a2b"></a>

```c
#define BT_UUID_ETS_CURRENT_ELAPSED_TIME BT_UUID_DECLARE_16(BT_UUID_ETS_CURRENT_ELAPSED_TIME_VAL)
```

相关声明：[BT_UUID_ETS_CURRENT_ELAPSED_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf27d2fbbf83f1193a8d400dcba6f4a2b)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_ETS_CURRENT_ELAPSED_TIME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaeb700085e464d9ee63350ec3fd06d6c7)。

ETS 当前经过时间特征（ETS Characteristic Current Elapsed Time）。

<a id="r_ga87e7a8d4ea7c2f0b4345c3ddd83e2bcc"></a>

```c
#define BT_UUID_GATT_SL_VAL 0x2bf5
```

相关声明：[BT_UUID_GATT_SL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga87e7a8d4ea7c2f0b4345c3ddd83e2bcc)。

GATT 低功耗 LE GATT 安全级别特征（GATT Characteristic LE GATT Security Levels）的 UUID 值。

<a id="r_ga07c07b64d8d06b76b64c71109dd39bc4"></a>

```c
#define BT_UUID_GATT_SL BT_UUID_DECLARE_16(BT_UUID_GATT_SL_VAL)
```

相关声明：[BT_UUID_GATT_SL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga07c07b64d8d06b76b64c71109dd39bc4)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GATT_SL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga87e7a8d4ea7c2f0b4345c3ddd83e2bcc)。

GATT 低功耗 LE GATT 安全级别特征（GATT Characteristic LE GATT Security Levels）。

<a id="r_ga1904b4b736c5949b544cfd3cf270b9a1"></a>

```c
#define BT_UUID_UDI_FOR_MEDICAL_DEVICES_VAL 0x2bff
```

相关声明：[BT_UUID_UDI_FOR_MEDICAL_DEVICES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1904b4b736c5949b544cfd3cf270b9a1)。

GATT 医疗器械唯一器械标识 UDI 特征（GATT Characteristic UDI for Medical Devices）的 UUID 值。

<a id="r_ga1d0210d3557a3838a4b04bedf413e80c"></a>

```c
#define BT_UUID_UDI_FOR_MEDICAL_DEVICES BT_UUID_DECLARE_16(BT_UUID_UDI_FOR_MEDICAL_DEVICES_VAL)
```

相关声明：[BT_UUID_UDI_FOR_MEDICAL_DEVICES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1d0210d3557a3838a4b04bedf413e80c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_UDI_FOR_MEDICAL_DEVICES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1904b4b736c5949b544cfd3cf270b9a1)。

GATT 医疗器械唯一器械标识 UDI 特征（GATT Characteristic UDI for Medical Devices）。

<a id="r_ga791ebaadcc3fac61cda4001d1dadc044"></a>

```c
#define BT_UUID_GMAS_VAL 0x1858
```

相关声明：[BT_UUID_GMAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga791ebaadcc3fac61cda4001d1dadc044)。

游戏音频服务（Gaming Audio Service）的 UUID 值。

<a id="r_gae48cde28242dd2813cb9259a3db4cd0f"></a>

```c
#define BT_UUID_GMAS BT_UUID_DECLARE_16(BT_UUID_GMAS_VAL)
```

相关声明：[BT_UUID_GMAS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae48cde28242dd2813cb9259a3db4cd0f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GMAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga791ebaadcc3fac61cda4001d1dadc044)。

游戏音频服务（Gaming Audio Service）。

<a id="r_ga8a9ca3e7c352dcc5c6b4834f1c1b188c"></a>

```c
#define BT_UUID_GMAP_ROLE_VAL 0x2C00
```

相关声明：[BT_UUID_GMAP_ROLE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8a9ca3e7c352dcc5c6b4834f1c1b188c)。

游戏音频配置文件角色（Gaming Audio Profile Role）的 UUID 值。

<a id="r_gacb7897b761dc608e7814a2ad103e47a2"></a>

```c
#define BT_UUID_GMAP_ROLE BT_UUID_DECLARE_16(BT_UUID_GMAP_ROLE_VAL)
```

相关声明：[BT_UUID_GMAP_ROLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacb7897b761dc608e7814a2ad103e47a2)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GMAP_ROLE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8a9ca3e7c352dcc5c6b4834f1c1b188c)。

游戏音频配置文件角色（Gaming Audio Profile Role）。

<a id="r_ga9a79627722acfc4c93b2d251aefd8b83"></a>

```c
#define BT_UUID_GMAP_UGG_FEAT_VAL 0x2C01
```

相关声明：[BT_UUID_GMAP_UGG_FEAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9a79627722acfc4c93b2d251aefd8b83)。

游戏音频配置文件单播游戏网关功能（Gaming Audio Profile Unicast Game Gateway Features）的 UUID 值。

<a id="r_gafcdc548a86c976b07fa57bd0ccaee9c9"></a>

```c
#define BT_UUID_GMAP_UGG_FEAT BT_UUID_DECLARE_16(BT_UUID_GMAP_UGG_FEAT_VAL)
```

相关声明：[BT_UUID_GMAP_UGG_FEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafcdc548a86c976b07fa57bd0ccaee9c9)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GMAP_UGG_FEAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9a79627722acfc4c93b2d251aefd8b83)。

游戏音频配置文件单播游戏网关功能（Gaming Audio Profile Unicast Game Gateway Features）。

<a id="r_ga24f317039700e33d09f6244d74e4c024"></a>

```c
#define BT_UUID_GMAP_UGT_FEAT_VAL 0x2C02
```

相关声明：[BT_UUID_GMAP_UGT_FEAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga24f317039700e33d09f6244d74e4c024)。

游戏音频配置文件单播游戏终端功能（Gaming Audio Profile Unicast Game Terminal Features）的 UUID 值。

<a id="r_gaf3b064865efb4e566ea3d00b1de932e1"></a>

```c
#define BT_UUID_GMAP_UGT_FEAT BT_UUID_DECLARE_16(BT_UUID_GMAP_UGT_FEAT_VAL)
```

相关声明：[BT_UUID_GMAP_UGT_FEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf3b064865efb4e566ea3d00b1de932e1)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GMAP_UGT_FEAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga24f317039700e33d09f6244d74e4c024)。

游戏音频配置文件单播游戏终端功能（Gaming Audio Profile Unicast Game Terminal Features）。

<a id="r_ga5aa7be5ea8b74329c07f7de879e9ab2f"></a>

```c
#define BT_UUID_GMAP_BGS_FEAT_VAL 0x2C03
```

相关声明：[BT_UUID_GMAP_BGS_FEAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5aa7be5ea8b74329c07f7de879e9ab2f)。

游戏音频配置文件广播游戏发送端功能（Gaming Audio Profile Broadcast Game Sender Features）的 UUID 值。

<a id="r_ga0aa83932e08ed22c1d75464b77e23b0c"></a>

```c
#define BT_UUID_GMAP_BGS_FEAT BT_UUID_DECLARE_16(BT_UUID_GMAP_BGS_FEAT_VAL)
```

相关声明：[BT_UUID_GMAP_BGS_FEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0aa83932e08ed22c1d75464b77e23b0c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GMAP_BGS_FEAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5aa7be5ea8b74329c07f7de879e9ab2f)。

游戏音频配置文件广播游戏发送端功能（Gaming Audio Profile Broadcast Game Sender Features）。

<a id="r_ga5b7fcf7e18179190c3cd3ec2289ebcd5"></a>

```c
#define BT_UUID_GMAP_BGR_FEAT_VAL 0x2C04
```

相关声明：[BT_UUID_GMAP_BGR_FEAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5b7fcf7e18179190c3cd3ec2289ebcd5)。

游戏音频配置文件广播游戏接收端功能（Gaming Audio Profile Broadcast Game Receiver Features）的 UUID 值。

<a id="r_ga0d13271568a11aceb9a6d169cdb6474c"></a>

```c
#define BT_UUID_GMAP_BGR_FEAT BT_UUID_DECLARE_16(BT_UUID_GMAP_BGR_FEAT_VAL)
```

相关声明：[BT_UUID_GMAP_BGR_FEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0d13271568a11aceb9a6d169cdb6474c)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_GMAP_BGR_FEAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5b7fcf7e18179190c3cd3ec2289ebcd5)。

游戏音频配置文件广播游戏接收端功能（Gaming Audio Profile Broadcast Game Receiver Features）。

<a id="r_ga445fdadef349779dd2da0553b11baf35"></a>

```c
#define BT_UUID_HIDS_SCI_MODE_VAL 0x2C39
```

相关声明：[BT_UUID_HIDS_SCI_MODE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga445fdadef349779dd2da0553b11baf35)。

HID 更短连接间隔 SCI 模式（HID SCI (Shorter Connection Intervals) Mode）的 UUID 值。

<a id="r_gae3b45358af78c1eb24ffd1f719f7e495"></a>

```c
#define BT_UUID_HIDS_SCI_MODE BT_UUID_DECLARE_16(BT_UUID_HIDS_SCI_MODE_VAL)
```

相关声明：[BT_UUID_HIDS_SCI_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae3b45358af78c1eb24ffd1f719f7e495)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HIDS_SCI_MODE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga445fdadef349779dd2da0553b11baf35)。

HID 更短连接间隔 SCI 模式（HID SCI (Shorter Connection Intervals) Mode）。

<a id="r_ga66f968bf7d0e1fee8946dcdb73eaf6b5"></a>

```c
#define BT_UUID_HIDS_SCI_INFO_VAL 0x2C3A
```

相关声明：[BT_UUID_HIDS_SCI_INFO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66f968bf7d0e1fee8946dcdb73eaf6b5)。

HID 更短连接间隔 SCI 信息（HID SCI (Shorter Connection Intervals) Information）的 UUID 值。

<a id="r_ga377f64178319aa5f6d8c52233422fd50"></a>

```c
#define BT_UUID_HIDS_SCI_INFO BT_UUID_DECLARE_16(BT_UUID_HIDS_SCI_INFO_VAL)
```

相关声明：[BT_UUID_HIDS_SCI_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga377f64178319aa5f6d8c52233422fd50)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HIDS_SCI_INFO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66f968bf7d0e1fee8946dcdb73eaf6b5)。

HID 更短连接间隔 SCI 信息（HID SCI (Shorter Connection Intervals) Information）。

<a id="r_gaa82cf709aaa5986ada534ac4c24aa407"></a>

```c
#define BT_UUID_SDP_VAL 0x0001
```

相关声明：[BT_UUID_SDP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa82cf709aaa5986ada534ac4c24aa407)。

<a id="r_ga82f35da766ed6acfe18de8d119d19859"></a>

```c
#define BT_UUID_SDP BT_UUID_DECLARE_16(BT_UUID_SDP_VAL)
```

相关声明：[BT_UUID_SDP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga82f35da766ed6acfe18de8d119d19859)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_SDP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa82cf709aaa5986ada534ac4c24aa407)。

<a id="r_gab0d4e8012eef2d067b63e8e538d6317c"></a>

```c
#define BT_UUID_UDP_VAL 0x0002
```

相关声明：[BT_UUID_UDP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab0d4e8012eef2d067b63e8e538d6317c)。

<a id="r_ga51e5cf4018099907c64eabf219a193c8"></a>

```c
#define BT_UUID_UDP BT_UUID_DECLARE_16(BT_UUID_UDP_VAL)
```

相关声明：[BT_UUID_UDP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga51e5cf4018099907c64eabf219a193c8)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_UDP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab0d4e8012eef2d067b63e8e538d6317c)。

<a id="r_ga71dd44d6977cc000c00a6176f71053c9"></a>

```c
#define BT_UUID_RFCOMM_VAL 0x0003
```

相关声明：[BT_UUID_RFCOMM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga71dd44d6977cc000c00a6176f71053c9)。

<a id="r_gafce3f7dd2fbd02c3a549f46395253cde"></a>

```c
#define BT_UUID_RFCOMM BT_UUID_DECLARE_16(BT_UUID_RFCOMM_VAL)
```

相关声明：[BT_UUID_RFCOMM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafce3f7dd2fbd02c3a549f46395253cde)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_RFCOMM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga71dd44d6977cc000c00a6176f71053c9)。

<a id="r_gab4dac3d360e3428cc0b66e34bea75285"></a>

```c
#define BT_UUID_TCP_VAL 0x0004
```

相关声明：[BT_UUID_TCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab4dac3d360e3428cc0b66e34bea75285)。

<a id="r_ga419519758947e29b8ded5209b1c47743"></a>

```c
#define BT_UUID_TCP BT_UUID_DECLARE_16(BT_UUID_TCP_VAL)
```

相关声明：[BT_UUID_TCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga419519758947e29b8ded5209b1c47743)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab4dac3d360e3428cc0b66e34bea75285)。

<a id="r_gab7f9b345cb85f922840e6e21722c3373"></a>

```c
#define BT_UUID_TCS_BIN_VAL 0x0005
```

相关声明：[BT_UUID_TCS_BIN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab7f9b345cb85f922840e6e21722c3373)。

<a id="r_ga5c9bd29f560d84a30c0cb009ccfdc36a"></a>

```c
#define BT_UUID_TCS_BIN BT_UUID_DECLARE_16(BT_UUID_TCS_BIN_VAL)
```

相关声明：[BT_UUID_TCS_BIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5c9bd29f560d84a30c0cb009ccfdc36a)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TCS_BIN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab7f9b345cb85f922840e6e21722c3373)。

<a id="r_ga09236e2cc7267043f47445e7b233bc38"></a>

```c
#define BT_UUID_TCS_AT_VAL 0x0006
```

相关声明：[BT_UUID_TCS_AT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga09236e2cc7267043f47445e7b233bc38)。

<a id="r_ga7c31eb642d9cb8231de38f25c43ef23f"></a>

```c
#define BT_UUID_TCS_AT BT_UUID_DECLARE_16(BT_UUID_TCS_AT_VAL)
```

相关声明：[BT_UUID_TCS_AT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7c31eb642d9cb8231de38f25c43ef23f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_TCS_AT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga09236e2cc7267043f47445e7b233bc38)。

<a id="r_ga675b73753e13c6c6dbbc5f655b23e466"></a>

```c
#define BT_UUID_ATT_VAL 0x0007
```

相关声明：[BT_UUID_ATT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga675b73753e13c6c6dbbc5f655b23e466)。

<a id="r_gaa91cf6c6639156a4b5c67041d479d555"></a>

```c
#define BT_UUID_ATT BT_UUID_DECLARE_16(BT_UUID_ATT_VAL)
```

相关声明：[BT_UUID_ATT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa91cf6c6639156a4b5c67041d479d555)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_ATT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga675b73753e13c6c6dbbc5f655b23e466)。

<a id="r_gab63382153f97c79f7cdcdfa0a264d6e7"></a>

```c
#define BT_UUID_OBEX_VAL 0x0008
```

相关声明：[BT_UUID_OBEX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab63382153f97c79f7cdcdfa0a264d6e7)。

<a id="r_ga8f660c1d39057815d0420d2dce00639e"></a>

```c
#define BT_UUID_OBEX BT_UUID_DECLARE_16(BT_UUID_OBEX_VAL)
```

相关声明：[BT_UUID_OBEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8f660c1d39057815d0420d2dce00639e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_OBEX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab63382153f97c79f7cdcdfa0a264d6e7)。

<a id="r_ga5bd66bfdd6ee1f68dd2447aed448d860"></a>

```c
#define BT_UUID_IP_VAL 0x0009
```

相关声明：[BT_UUID_IP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5bd66bfdd6ee1f68dd2447aed448d860)。

<a id="r_gad0469b885ffe7be0ff1bef7feb2395d5"></a>

```c
#define BT_UUID_IP BT_UUID_DECLARE_16(BT_UUID_IP_VAL)
```

相关声明：[BT_UUID_IP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad0469b885ffe7be0ff1bef7feb2395d5)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_IP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5bd66bfdd6ee1f68dd2447aed448d860)。

<a id="r_gad8ecc3b05eb61d0a3da8daa38deb3887"></a>

```c
#define BT_UUID_FTP_VAL 0x000a
```

相关声明：[BT_UUID_FTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad8ecc3b05eb61d0a3da8daa38deb3887)。

<a id="r_gada757111154b60d3dbb375192ec48a0f"></a>

```c
#define BT_UUID_FTP BT_UUID_DECLARE_16(BT_UUID_FTP_VAL)
```

相关声明：[BT_UUID_FTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gada757111154b60d3dbb375192ec48a0f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_FTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad8ecc3b05eb61d0a3da8daa38deb3887)。

<a id="r_gafd11ab75ca80c343f894db89779419d4"></a>

```c
#define BT_UUID_HTTP_VAL 0x000c
```

相关声明：[BT_UUID_HTTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafd11ab75ca80c343f894db89779419d4)。

<a id="r_ga34afe0fe521f95f82f0c86e0de8c1d93"></a>

```c
#define BT_UUID_HTTP BT_UUID_DECLARE_16(BT_UUID_HTTP_VAL)
```

相关声明：[BT_UUID_HTTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga34afe0fe521f95f82f0c86e0de8c1d93)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HTTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafd11ab75ca80c343f894db89779419d4)。

<a id="r_gac095fdb1bc8d0a07737061b428e12071"></a>

```c
#define BT_UUID_WSP_VAL 0x000e
```

相关声明：[BT_UUID_WSP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac095fdb1bc8d0a07737061b428e12071)。

<a id="r_ga8f0f3c9e5ef2b6a313ed742a8f7ed0bd"></a>

```c
#define BT_UUID_WSP BT_UUID_DECLARE_16(BT_UUID_WSP_VAL)
```

相关声明：[BT_UUID_WSP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8f0f3c9e5ef2b6a313ed742a8f7ed0bd)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_WSP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac095fdb1bc8d0a07737061b428e12071)。

<a id="r_gacf6c5a3e20d50500cca56daf5802faf5"></a>

```c
#define BT_UUID_BNEP_VAL 0x000f
```

相关声明：[BT_UUID_BNEP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacf6c5a3e20d50500cca56daf5802faf5)。

<a id="r_ga9bd1756830328cacd40fc8bf80ee176d"></a>

```c
#define BT_UUID_BNEP BT_UUID_DECLARE_16(BT_UUID_BNEP_VAL)
```

相关声明：[BT_UUID_BNEP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9bd1756830328cacd40fc8bf80ee176d)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_BNEP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacf6c5a3e20d50500cca56daf5802faf5)。

<a id="r_ga0dac826a9f670d1eba071603723fd3f5"></a>

```c
#define BT_UUID_UPNP_VAL 0x0010
```

相关声明：[BT_UUID_UPNP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0dac826a9f670d1eba071603723fd3f5)。

<a id="r_ga3f7ade885937ba780b0074516c180c42"></a>

```c
#define BT_UUID_UPNP BT_UUID_DECLARE_16(BT_UUID_UPNP_VAL)
```

相关声明：[BT_UUID_UPNP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3f7ade885937ba780b0074516c180c42)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_UPNP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0dac826a9f670d1eba071603723fd3f5)。

<a id="r_gac30ff318ffebd4a6793a0267de6b84e9"></a>

```c
#define BT_UUID_HIDP_VAL 0x0011
```

相关声明：[BT_UUID_HIDP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac30ff318ffebd4a6793a0267de6b84e9)。

<a id="r_ga9cbd452d2c4fa9fae46cd39bb8133ea2"></a>

```c
#define BT_UUID_HIDP BT_UUID_DECLARE_16(BT_UUID_HIDP_VAL)
```

相关声明：[BT_UUID_HIDP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9cbd452d2c4fa9fae46cd39bb8133ea2)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HIDP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac30ff318ffebd4a6793a0267de6b84e9)。

<a id="r_gaccdbcd9b4ab68185c4ba213d2b83fcf2"></a>

```c
#define BT_UUID_HCRP_CTRL_VAL 0x0012
```

相关声明：[BT_UUID_HCRP_CTRL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaccdbcd9b4ab68185c4ba213d2b83fcf2)。

<a id="r_ga731221f8f6711a400aa0e7c39c8520ea"></a>

```c
#define BT_UUID_HCRP_CTRL BT_UUID_DECLARE_16(BT_UUID_HCRP_CTRL_VAL)
```

相关声明：[BT_UUID_HCRP_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga731221f8f6711a400aa0e7c39c8520ea)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HCRP_CTRL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaccdbcd9b4ab68185c4ba213d2b83fcf2)。

<a id="r_ga61619a474d5278d79bf66fcda77076f6"></a>

```c
#define BT_UUID_HCRP_DATA_VAL 0x0014
```

相关声明：[BT_UUID_HCRP_DATA_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga61619a474d5278d79bf66fcda77076f6)。

<a id="r_ga0bd9a371c57ecc22cfb40b31025cc69e"></a>

```c
#define BT_UUID_HCRP_DATA BT_UUID_DECLARE_16(BT_UUID_HCRP_DATA_VAL)
```

相关声明：[BT_UUID_HCRP_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0bd9a371c57ecc22cfb40b31025cc69e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HCRP_DATA_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga61619a474d5278d79bf66fcda77076f6)。

<a id="r_ga99a3d8dfd8f46ece85f3fa5be8c94a64"></a>

```c
#define BT_UUID_HCRP_NOTE_VAL 0x0016
```

相关声明：[BT_UUID_HCRP_NOTE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga99a3d8dfd8f46ece85f3fa5be8c94a64)。

<a id="r_ga85372fbf20b7d83fdf5e780487f14974"></a>

```c
#define BT_UUID_HCRP_NOTE BT_UUID_DECLARE_16(BT_UUID_HCRP_NOTE_VAL)
```

相关声明：[BT_UUID_HCRP_NOTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga85372fbf20b7d83fdf5e780487f14974)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_HCRP_NOTE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga99a3d8dfd8f46ece85f3fa5be8c94a64)。

<a id="r_ga07ce8ad97e49eb94eb08a75b8fa555ca"></a>

```c
#define BT_UUID_AVCTP_VAL 0x0017
```

相关声明：[BT_UUID_AVCTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga07ce8ad97e49eb94eb08a75b8fa555ca)。

<a id="r_ga1b172e9a094474f5d7fe6b1b46dbc93e"></a>

```c
#define BT_UUID_AVCTP BT_UUID_DECLARE_16(BT_UUID_AVCTP_VAL)
```

相关声明：[BT_UUID_AVCTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1b172e9a094474f5d7fe6b1b46dbc93e)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_AVCTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga07ce8ad97e49eb94eb08a75b8fa555ca)。

<a id="r_ga4d08c3f7d19718e9107414d111940b43"></a>

```c
#define BT_UUID_AVCTP_BROWSING_VAL 0x0018
```

相关声明：[BT_UUID_AVCTP_BROWSING_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4d08c3f7d19718e9107414d111940b43)。

<a id="r_gae3f1b0e418dc12a1ef4c2d2f4f35c485"></a>

```c
#define BT_UUID_AVCTP_BROWSING BT_UUID_DECLARE_16(BT_UUID_AVCTP_BROWSING_VAL)
```

相关声明：[BT_UUID_AVCTP_BROWSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae3f1b0e418dc12a1ef4c2d2f4f35c485)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_AVCTP_BROWSING_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4d08c3f7d19718e9107414d111940b43)。

<a id="r_ga2e2934e79054324cec077903c07108ad"></a>

```c
#define BT_UUID_AVDTP_VAL 0x0019
```

相关声明：[BT_UUID_AVDTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2e2934e79054324cec077903c07108ad)。

<a id="r_ga926c1d29d7655320c3b89558ec5b3d2f"></a>

```c
#define BT_UUID_AVDTP BT_UUID_DECLARE_16(BT_UUID_AVDTP_VAL)
```

相关声明：[BT_UUID_AVDTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga926c1d29d7655320c3b89558ec5b3d2f)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_AVDTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2e2934e79054324cec077903c07108ad)。

<a id="r_gae83a731e34ef81a8340f9c5919ad0c6f"></a>

```c
#define BT_UUID_CMTP_VAL 0x001b
```

相关声明：[BT_UUID_CMTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae83a731e34ef81a8340f9c5919ad0c6f)。

<a id="r_gaa70481ddcb90e8232b3397580c5927a0"></a>

```c
#define BT_UUID_CMTP BT_UUID_DECLARE_16(BT_UUID_CMTP_VAL)
```

相关声明：[BT_UUID_CMTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa70481ddcb90e8232b3397580c5927a0)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_CMTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae83a731e34ef81a8340f9c5919ad0c6f)。

<a id="r_ga477f7e4e7baffa502a0d8ded852ec2e7"></a>

```c
#define BT_UUID_UDI_VAL 0x001d
```

相关声明：[BT_UUID_UDI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga477f7e4e7baffa502a0d8ded852ec2e7)。

<a id="r_gaae2132eeff69adb594365a0af0419695"></a>

```c
#define BT_UUID_UDI BT_UUID_DECLARE_16(BT_UUID_UDI_VAL)
```

相关声明：[BT_UUID_UDI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaae2132eeff69adb594365a0af0419695)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_UDI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga477f7e4e7baffa502a0d8ded852ec2e7)。

<a id="r_ga9a893aa35fe599d26b6dcfd9bd0fcb2e"></a>

```c
#define BT_UUID_MCAP_CTRL_VAL 0x001e
```

相关声明：[BT_UUID_MCAP_CTRL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9a893aa35fe599d26b6dcfd9bd0fcb2e)。

<a id="r_ga1f576ec8576152a951d44a87b8406514"></a>

```c
#define BT_UUID_MCAP_CTRL BT_UUID_DECLARE_16(BT_UUID_MCAP_CTRL_VAL)
```

相关声明：[BT_UUID_MCAP_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1f576ec8576152a951d44a87b8406514)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCAP_CTRL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9a893aa35fe599d26b6dcfd9bd0fcb2e)。

<a id="r_gabc9726eea06d6f3cea2de134f62fb4f1"></a>

```c
#define BT_UUID_MCAP_DATA_VAL 0x001f
```

相关声明：[BT_UUID_MCAP_DATA_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabc9726eea06d6f3cea2de134f62fb4f1)。

<a id="r_gab5607157844471d48d2d1db3e295cee3"></a>

```c
#define BT_UUID_MCAP_DATA BT_UUID_DECLARE_16(BT_UUID_MCAP_DATA_VAL)
```

相关声明：[BT_UUID_MCAP_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab5607157844471d48d2d1db3e295cee3)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_MCAP_DATA_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabc9726eea06d6f3cea2de134f62fb4f1)。

<a id="r_ga64e0b2fde8593ae40dfc0d661240abb4"></a>

```c
#define BT_UUID_L2CAP_VAL 0x0100
```

相关声明：[BT_UUID_L2CAP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga64e0b2fde8593ae40dfc0d661240abb4)。

<a id="r_ga17007ef5a1e355f912af78f909a1d971"></a>

```c
#define BT_UUID_L2CAP BT_UUID_DECLARE_16(BT_UUID_L2CAP_VAL)
```

相关声明：[BT_UUID_L2CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga17007ef5a1e355f912af78f909a1d971)、[BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)、[BT_UUID_L2CAP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga64e0b2fde8593ae40dfc0d661240abb4)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.3\_枚举（Enumerations）

<a id="r_gabec48a57ba2d88c9e6006d9996a0fb43"></a>

```c
enum { BT_UUID_TYPE_16 , BT_UUID_TYPE_32 , BT_UUID_TYPE_128 }
```

相关声明：[BT_UUID_TYPE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ggabec48a57ba2d88c9e6006d9996a0fb43a8a5a0c5b6310aff10b182daec0e452ba)、[BT_UUID_TYPE_32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ggabec48a57ba2d88c9e6006d9996a0fb43a27382df27b8098bf6144021c1b23c4c8)、[BT_UUID_TYPE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ggabec48a57ba2d88c9e6006d9996a0fb43a786cbb74a1d74c77cb31ff3c4da45517)。

蓝牙 UUID 类型（Bluetooth UUID Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.4\_函数（Functions）

<a id="r_gafe17513c1f91cb3f3e61648b71620c6b"></a>

```c
int bt_uuid_cmp (const struct bt_uuid *u1, const struct bt_uuid *u2)
```

相关声明：[bt_uuid_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafe17513c1f91cb3f3e61648b71620c6b)、[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)。

比较蓝牙 UUID（Compare Bluetooth UUIDs）。

<a id="r_ga9e260584efcc111eb3ee02bf78f01881"></a>

```c
bool bt_uuid_create (struct bt_uuid *uuid, const uint8_t *data, uint8_t data_len)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_uuid_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9e260584efcc111eb3ee02bf78f01881)、[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从小端格式（Little-endian）的数据缓冲区创建 `bt_uuid`。

<a id="r_gab5ef78dd2263f08de16a0f1e764df657"></a>

```c
void bt_uuid_to_str (const struct bt_uuid *uuid, char *str, size_t len)
```

相关声明：[bt_uuid_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab5ef78dd2263f08de16a0f1e764df657)、[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)。

将蓝牙 UUID 转换为字符串（String）。

<a id="r_ga4dec477f7827ece43b91d42d75b1244b"></a>

```c
int bt_uuid_from_str (const char *str, struct bt_uuid_any *uuid)
```

相关声明：[bt_uuid_from_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4dec477f7827ece43b91d42d75b1244b)、[bt_uuid_any](../bluetooth_connection_model_reference/P135_bt_uuid_any_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)。

将 UUID 字符串转换为蓝牙 UUID（Bluetooth UUID）。

<a id="r_ga72cd2ea0cc6fedded3d1eb8f617f4c07"></a>

```c
int bt_uuid_compress (const struct bt_uuid *src, struct bt_uuid_any *dst)
```

相关声明：[bt_uuid_compress](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga72cd2ea0cc6fedded3d1eb8f617f4c07)、[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[bt_uuid_any](../bluetooth_connection_model_reference/P135_bt_uuid_any_结构体.md)。

如果 128 位 UUID 与蓝牙基础 UUID（Bluetooth Base UUID）匹配，则将其压缩为 16 位或 32 位。


## 1.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/bluetooth/byteorder.h](../byteorder_reference/P005_蓝牙字节序头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P020_uuid.h_源码浏览.md)
- [bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)
- [bt_uuid_16](../bluetooth_connection_model_reference/P133_bt_uuid_16_结构体.md)
- [bt_uuid_32](../bluetooth_connection_model_reference/P134_bt_uuid_32_结构体.md)
- [bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)
- [bt_uuid_any](../bluetooth_connection_model_reference/P135_bt_uuid_any_结构体.md)
- [BT_UUID_SIZE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9d3506fd135b5cd8763446f572c161da)
- [BT_UUID_SIZE_32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf35f2e5054bfcc81985e90b8ef659fd9)
- [BT_UUID_SIZE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga86fdce8e63c0f8208bea6b0f2584eb67)
- [BT_UUID_INIT_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab7c9f80628c5fb1b5d1c09d18a1baff7)
- [BT_UUID_INIT_32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga207ff52ebf1eea1c487fff3d840a38f8)
- [BT_UUID_INIT_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1a840adf4bc06cf2cd5dbeb0c868374b)
- [BT_UUID_DECLARE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66ea8148e444e163a936ebd79a63eb55)
- [BT_UUID_DECLARE_32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga945448449c57b4800e25a363e7d4d1cc)
- [BT_UUID_DECLARE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadece715e13e2a529aa55c298ff760bf0)
- [BT_UUID_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7466cf356741d6348f332653a385fd01)
- [BT_UUID_32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacc77f082e8dac620672676ed8d005504)
- [BT_UUID_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga931a0d5eb23537be31408c787fd8b48d)
- [BT_UUID_128_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3973b66e992cbc0940752b77b378f43)
- [BT_UUID_16_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga16e057af1bb2f1c11e74b50bfd490586)
- [BT_UUID_32_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad5294c1c19c66b20321c88939a8849bf)
- [BT_UUID_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf9a36381128454102c558568dfd5d029)
- [BT_UUID_GAP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaaf6715d89ba70a057949e636fb2368dd)
- [BT_UUID_GAP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae8b61f07e6732ffb876318045b5803c4)
- [BT_UUID_GATT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad893036bda14523c3e35ff66d23bacb2)
- [BT_UUID_GATT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga18f210e4e60b9fdd80d9d68f007b0728)
- [BT_UUID_IAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga637aece6581426d8d5d7b9aeb546a67e)
- [BT_UUID_IAS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9d99491d2957912ab80e2636d6ac7416)
- [BT_UUID_LLS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1b868ca21fa47aba88601f71eb8ad1d5)
- [BT_UUID_LLS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6bdab3bba88af7187eb50b7817cc317e)
- [BT_UUID_TPS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab8d79e7553b418eae94b9d790d9a422e)
- [BT_UUID_TPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2e250a6880be716f98e668ab26dcdac3)
- [BT_UUID_CTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga264f3b58d4e3bee6a7533acf0670206d)
- [BT_UUID_CTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8c2c089f4cc458c0f4a5a7506c21a6f9)
- [BT_UUID_RTUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga13300d9d1074fd90a65233357dd9ad60)
- [BT_UUID_RTUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga52c98d18473e61c581f0cab4839defa8)
- [BT_UUID_NDSTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0396837f73209e12bc6d11c64a3a6d67)
- [BT_UUID_NDSTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3a4f846cbf5dd4fccec26be00506a61c)
- [BT_UUID_GS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab31578ab529cf755ec611c491a3676ac)
- [BT_UUID_GS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac1f5583a48b80fab9d05546d87cb6de0)
- [BT_UUID_HTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3caec4c6564711a2959ffadcf5598011)
- [BT_UUID_HTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabffa5a0a0a57cfd330a8bef348c2c2ee)
- [BT_UUID_DIS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3eaf1d7bfeb9b9375e1e2b4ba7f23aed)
- [BT_UUID_DIS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga03ea74768fa1e69dad54cffe9eeeee31)
- [BT_UUID_NAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66870ecd34acfee828d55f63167b7e67)
- [BT_UUID_NAS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga92af25a46ae1b534fa248fd0516278cb)
- [BT_UUID_WDS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga110066c42ffc45bf86a9c90528aeb2e7)
- [BT_UUID_WDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7c501f33b29907d48dd31ed70eeb67d4)
- [BT_UUID_HRS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga912cb91295d110813a3db0144c95551d)
- [BT_UUID_HRS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga17893ceaa9bc20640d4ecdeabe9beb28)
- [BT_UUID_PAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaea47ecf9bc957d813312a188a701db54)
- [BT_UUID_PAS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadd5233cc3cb516f8b7fb192d6c64bcad)
- [BT_UUID_BAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2ff64c18d7f8dae8a328b52f486161c4)
- [BT_UUID_BAS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabc55390a1144b556477df555e76848ab)
- [BT_UUID_BPS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2ff98d3bfd27cba7eb99c62dfb31a6fd)
- [BT_UUID_BPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga97ed88c10cdc3f1c32c4e53d260eaa3e)
- [BT_UUID_ANS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0c6ee900cba57e40f8b3681e1ea404c7)
- [BT_UUID_ANS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7a208b147e3b35857c72ba8f8db22d62)
- [BT_UUID_HIDS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2bf2ec6082e31f397dec6634cda56bbb)
- [BT_UUID_HIDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga74e91eef3e2dcbb4499a0f70f3b479d4)
- [BT_UUID_SPS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga73e7ff27e935868fa86c9d38e186e405)
- [BT_UUID_SPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7599a7a3cdc6a32c60862618b6b70327)
- [BT_UUID_RSCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad35b23e0814f0f74c3a33587f7922966)
- [BT_UUID_RSCS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga40a6402510b5c71b0eca5b2f7a914085)
- [BT_UUID_AIOS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4449d49abf6fed72da52b14a967aec4d)
- [BT_UUID_AIOS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaaa73f77971aad79900e18fd58d12ea22)
- [BT_UUID_CSC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4d31b6944d378bcda7c8f7bfc74c5692)
- [BT_UUID_CSC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6514fa0098d12c02aa34c18e1e5a6396)
- [BT_UUID_CPS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab063c1e5d2773927ce54c1745c7134d4)
- [BT_UUID_CPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3c2895467ba651b8ebad709fdd44f6d)
- [BT_UUID_LNS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga36161c4e68b691cfb6a9f691a8f693dd)
- [BT_UUID_LNS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac48ea20cb0503dd748862862157e9224)
- [BT_UUID_ESS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8e8d24d0bf0a49713bbfa93cc2bdb0da)
- [BT_UUID_ESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga96c5958372c4fdba211b4f74d342a5b3)
- [BT_UUID_BCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga69baa896cd558487733cd575a6193e0d)
- [BT_UUID_BCS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga08170da6b471e937f64de6943b6e24bb)
- [BT_UUID_UDS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga035ee545fdd640745b3bcbd8b7e7b3b6)
- [BT_UUID_UDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac6edbd84e5f0b454e130f835a32f1a44)
- [BT_UUID_WSS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6b6566f914d2c92c9b1bb4efd6efee98)
- [BT_UUID_WSS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa5c518578e2620aafad915a0291dfe8f)
- [BT_UUID_BMS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga399ffbd6e7d3e50010383f2d521d8089)
- [BT_UUID_BMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0a91114bf5e53c894d10d1e432223714)
- [BT_UUID_CGMS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9726266ed3399a646999e19f639457a7)
- [BT_UUID_CGMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga04767d3a7461b3508bce584704d92c75)
- [BT_UUID_IPSS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad8cc687442abd5eea3e367d2b859e2e8)
- [BT_UUID_IPSS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga32f10a8bfb452aee43c64eec3c2d5a0f)
- [BT_UUID_IPS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8fafd81c36f6b515d2709d5f4efd9d00)
- [BT_UUID_IPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8dac7b88922315a2af06ad70cdfcfd0c)
- [BT_UUID_POS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabfb8333e3fb8e819f02601ace836687b)
- [BT_UUID_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa713f38e63cfc998559c862f80f2380b)
- [BT_UUID_HPS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5f66d3e11dcde95c3c4e7055734c9aef)
- [BT_UUID_HPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaade9071b49d238d13edf57e90655c41c)
- [BT_UUID_TDS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafafc31de7e0d06e831ef13f5ddb88685)
- [BT_UUID_TDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaccdb682d8f53c8560bea355a5376d72d)
- [BT_UUID_OTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0a7a74bbb0c8bbd97d5fd6807deeb4c3)
- [BT_UUID_OTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4f18867b63edde824c1a57c0ee354282)
- [BT_UUID_FMS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga036c6c7b6589a7178851ff7004aa64db)
- [BT_UUID_FMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8935f33e5d388c96e38a172a5831b573)
- [BT_UUID_MESH_PROV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa0bf05b5c11a3b6f9f0f8e48298b4776)
- [BT_UUID_MESH_PROV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga665cc5a42b1b074536ce949fe1853f7b)
- [BT_UUID_MESH_PROXY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa347d1cf40b3eba7052c3e7c80e32a02)
- [BT_UUID_MESH_PROXY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga34de82083c412e280bb585db519d70a2)
- [BT_UUID_MESH_PROXY_SOLICITATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga02eaaf8d7ec7981336713d4cb1ea6b6a)
- [BT_UUID_RCSRV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga76f45a959cf7d4bb5b874ba2e2f8c5ad)
- [BT_UUID_RCSRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafc39274d32d212b7b244f24809d00e15)
- [BT_UUID_IDS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac1069e0c1a650aa7659942f0533cb384)
- [BT_UUID_IDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3921b7c5c31423d7ac7ed4338ccf980)
- [BT_UUID_BSS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa75f32c09a7f70c1b79fb7af1b50c0fe)
- [BT_UUID_BSS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacc9ac8d5418e857f70b7836629874296)
- [BT_UUID_ECS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabd1855b6ede9f8dcfa46b211ad7a33b5)
- [BT_UUID_ECS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga966e2b5ad06522d4a6e882755fc4dcbf)
- [BT_UUID_ACLS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga72b1d17c97437e7ced4e1c7c3fb9d0cd)
- [BT_UUID_ACLS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga022390a0b44e81e0925e29a87fd4d1e3)
- [BT_UUID_PAMS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf85d03a7c42d040559874e6d1a6296a6)
- [BT_UUID_PAMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3c5590637fc3c90c4beed23bab9f5eb6)
- [BT_UUID_ETS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1d21d600546eef483a96bc5c2e50cb66)
- [BT_UUID_ETS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga27126fff5520f8dde63e795ebd69eded)
- [BT_UUID_AICS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga67f3c417689d2a7af32e9bacaa274d44)
- [BT_UUID_AICS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8e7ec38a733ebe33d9d1d525a7c2c051)
- [BT_UUID_VCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9de8d92b55a644904d5b7257608cba45)
- [BT_UUID_VCS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaaf797d6506d5f47e730e5bbf6ff79f7c)
- [BT_UUID_VOCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga78b30023b019279b2b9567d7c3ffeac2)
- [BT_UUID_VOCS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2ab2f92985ca0f65fb066df57c2f1433)
- [BT_UUID_CSIS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5f2c25e1c3f14fb65f062dc34f56b3ed)
- [BT_UUID_CSIS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga111f2eb8e186444804b8b3c39f0f00a3)
- [BT_UUID_DTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad8fc6ade8cafce1b9461de0a27389c88)
- [BT_UUID_DTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6417c327841fd7317515e394f5ac0089)
- [BT_UUID_MCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3cd2f717c107a3e8d65eb958155884fd)
- [BT_UUID_MCS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7b84d0b301ce2f565de7eb89165af0cf)
- [BT_UUID_GMCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga35e8dae5a05985c10e3cdd610161ebcc)
- [BT_UUID_GMCS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4efbadd4ce5a6fb64a5d9832b4626d0f)
- [BT_UUID_CTES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9e7f780e9800abc6fa86fa034482df4b)
- [BT_UUID_CTES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf85f0bff2abbe069d8d64a3eda2a066d)
- [BT_UUID_TBS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae25bb19fe3d92555a9c2c2de6fae5354)
- [BT_UUID_TBS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga70c7991e602fa8c87868cac63c838c21)
- [BT_UUID_GTBS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1e90e6d7a97ca28b842012f61b76a2cb)
- [BT_UUID_GTBS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabb0810fa80d5623a5af457a2fb02ca6e)
- [BT_UUID_MICS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac18fe10ee79d240af7c494fab0304d90)
- [BT_UUID_MICS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga411a51f52e6e63c905d86ce5b924e69c)
- [BT_UUID_ASCS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaedc903cd915524adfa5d4d64fa38cf22)
- [BT_UUID_ASCS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7d52614d936753738fb04f124c97fc09)
- [BT_UUID_BASS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa671703a706fc97dcc9a4b1dd7f4fef3)
- [BT_UUID_BASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7d0e06ae7e089098ac9d0c32087d5803)
- [BT_UUID_PACS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga69dafd580d116dec74b54c818d5c275b)
- [BT_UUID_PACS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga86720eb2ad6aa3f66a9bf2248cb95383)
- [BT_UUID_BASIC_AUDIO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa1c0efca17e5b3de3c0fd254181a53db)
- [BT_UUID_BASIC_AUDIO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga842f48f68be48c3379161b595fca22a2)
- [BT_UUID_BROADCAST_AUDIO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0c67f9e1a5fef34fd1fddc539e20119b)
- [BT_UUID_BROADCAST_AUDIO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafe9b1d539a9c77037e0c8433b702790e)
- [BT_UUID_CAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab3f48a2a32b3a2061f3b108350c59ec4)
- [BT_UUID_CAS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab69a851e430a0232abb839b0d9fc54e5)
- [BT_UUID_HAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8d937e82611aaa2da305795d00074c93)
- [BT_UUID_HAS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac5acaee5423acd4531768fbf8844676b)
- [BT_UUID_TMAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga42f0d2bf3ce4a258a6f9d14a828cf422)
- [BT_UUID_TMAS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga84ea43f70dee139497be28d90db70104)
- [BT_UUID_PBA_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga06265a1d97c1b734340f9eb0055da913)
- [BT_UUID_PBA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga98f4f946c1bca483a7e81cad162ee0b1)
- [BT_UUID_GATT_PRIMARY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8244f6edaf3a347be1a3bf4e1d8fb4c3)
- [BT_UUID_GATT_PRIMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6e87ce1575494eb90358e074e8dbe276)
- [BT_UUID_GATT_SECONDARY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga764703eec266d58b0ea9e00d02f23d1d)
- [BT_UUID_GATT_SECONDARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad084d3658e663b6b8e200be256c54cdb)
- [BT_UUID_GATT_INCLUDE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa493141bce2425fe40f809f151ace673)
- [BT_UUID_GATT_INCLUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga995596ff7374ebcb44d4706bc16234e4)
- [BT_UUID_GATT_CHRC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae8b1af5f3458ca8523db83a3d8ccc62c)
- [BT_UUID_GATT_CHRC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadcedbbe1c432c4ac737e54b318e01a0f)
- [BT_UUID_GATT_CEP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga68b7ae19aad514e4a6731796c34c59da)
- [特征扩展属性 UUID（Characteristic Extended Properties UUID）：`BT_UUID_GATT_CEP`。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6aa143b721d810f1536d7431a9bf7cc7)
- [BT_UUID_GATT_CUD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2a168fa660bc6c3c3d5a85d99f2c9e60)
- [BT_UUID_GATT_CUD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaaaf94f5d918a1b6715cf4816b03875a2)
- [BT_UUID_GATT_CCC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa7807cb9ed1aa19f48c7dc4904f52dbb)
- [客户端特征配置 UUID（Client Characteristic Configuration UUID）：`BT_UUID_GATT_CCC`。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga03a2d3f0ce89508b794d5c87a4303057)
- [BT_UUID_GATT_SCC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga84cc4d600b5218baf5620b87cb8ddc55)
- [服务器特征配置 UUID（Server Characteristic Configuration UUID）：`BT_UUID_GATT_SCC`。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga82567cdce8c4411cd3daf26711ba9685)
- [BT_UUID_GATT_CPF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga71924f95ca117ace35e64b0222bb5bf7)
- [特征呈现格式 UUID（Characteristic Presentation Format UUID）：`BT_UUID_GATT_CPF`。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga331a61702ffe9b15bac0de3d60414022)
- [BT_UUID_GATT_CAF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga88dbd0deac028cb0df1a6bd1874aec7f)
- [BT_UUID_GATT_CAF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadc590b4039c9f47965e88e57b5589a93)
- [BT_UUID_VALID_RANGE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6fa0e8a8f2727e4646461ca14247466f)
- [BT_UUID_VALID_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad53d373df905c4b11c39a3ae4284a6d1)
- [BT_UUID_HIDS_EXT_REPORT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa8e06b1198ea23a01e892080df88e7f4)
- [BT_UUID_HIDS_EXT_REPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae945ad8eac1b444d92096c76239e106d)
- [BT_UUID_HIDS_REPORT_REF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4c1f2a0f52f101910f9294b10b5af484)
- [BT_UUID_HIDS_REPORT_REF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga001e019b08f5f88a158ed0861c017609)
- [BT_UUID_VAL_TRIGGER_SETTING_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga882af0a9286c487c1f108346be9af304)
- [BT_UUID_VAL_TRIGGER_SETTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2601c8bcfd2efae9b20e67f5c95de3f1)
- [BT_UUID_ES_CONFIGURATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga85eab7f3dbd2f517d36e750d3c020dec)
- [BT_UUID_ES_CONFIGURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae2d7028c5102df6f53765a98b9b729ea)
- [BT_UUID_ES_MEASUREMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8758259d984c0391feeceb459591e2fb)
- [BT_UUID_ES_MEASUREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5e738598773234b87a1db746badce304)
- [BT_UUID_ES_TRIGGER_SETTING_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0da1b874a844e15cdf185c6e7cbc9d64)
- [BT_UUID_ES_TRIGGER_SETTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab9daf129a8625853989516032010f1a3)
- [BT_UUID_TM_TRIGGER_SETTING_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacacc7a2120d918c46a45cde0b0a8e44b)
- [BT_UUID_TM_TRIGGER_SETTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga017b04e00401d50fc33cfd34d218492c)
- [BT_UUID_GAP_DEVICE_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac7a400574b6c78638e41eeaf97b7e9f3)
- [BT_UUID_GAP_DEVICE_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2bda01c9df904c8d0260ca3c0e3924cb)
- [BT_UUID_GAP_APPEARANCE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8789efbc24ac67479a86c3dfa0379154)
- [BT_UUID_GAP_APPEARANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4354d250e2cfca4fc868134bca4178b0)
- [BT_UUID_GAP_PPF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga575ef013a228bb5bb728724c9334347f)
- [BT_UUID_GAP_PPF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4bec5c6656a10756a38ac9a6805f9757)
- [BT_UUID_GAP_RA_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga739961cc85dd01779228f5054a3c3790)
- [BT_UUID_GAP_RA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga569663025aceabcd964f9c423ab030b5)
- [BT_UUID_GAP_PPCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga08be6df54da61393b3fe4efb7ab70b71)
- [BT_UUID_GAP_PPCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad174f313309b1bbb1208c61769566c77)
- [BT_UUID_GATT_SC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf7af098d1487b3e09ded21b4490c50e0)
- [BT_UUID_GATT_SC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad0609fd8c275c69cd0aabb7ba7c0f628)
- [BT_UUID_ALERT_LEVEL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2df4fc4fb971330cb7462911b68f73fd)
- [BT_UUID_ALERT_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga400e07242af41e836dfc250dc41cb010)
- [BT_UUID_TPS_TX_POWER_LEVEL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga07f1f99a8e237304f9415fade56432e4)
- [BT_UUID_TPS_TX_POWER_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gade253bd200b4d2ea9f0463c3911295f1)
- [BT_UUID_GATT_DT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga71d42d8e00aa0b388315aeeb68c29839)
- [BT_UUID_GATT_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga09cd4c6c81b8393f19b765a01ec556a0)
- [BT_UUID_GATT_DW_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga952c7341d02dd4bf3cea142b0b41e41c)
- [BT_UUID_GATT_DW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga442781cffe3da4bff3c8903d46ae07a0)
- [BT_UUID_GATT_DDT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga02fd005f86fd9995d61f63c3e7735028)
- [BT_UUID_GATT_DDT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaee156d97abd11f1422677bbb08cd5193)
- [BT_UUID_GATT_ET256_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga195fc66b479dec1131ea5e7cf1350afb)
- [BT_UUID_GATT_ET256](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3d5472767d50ddeabcdc7e2961610b78)
- [BT_UUID_GATT_DST_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad826c92cd28e6eef5651474b611ab093)
- [BT_UUID_GATT_DST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4b08c7472ecfe66eb2290fd83772ea24)
- [BT_UUID_GATT_TZ_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4e7082162bcdc58b385989e955ebb7f9)
- [BT_UUID_GATT_TZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga83e5e48b8bd8955dc559b95ec6e73a78)
- [BT_UUID_GATT_LTI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga25c6a750b9548144da0e78cca3ad6a59)
- [BT_UUID_GATT_LTI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6524bc40fbada1e558635af6b52283b9)
- [BT_UUID_GATT_TDST_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1bf3703c269e658c0e0e4ef822f14299)
- [BT_UUID_GATT_TDST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gace914257c496dbe17adc0d2b3db8f4c7)
- [BT_UUID_GATT_TA_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad304e85ca1a4b8f0f53d6068a37ae8d2)
- [BT_UUID_GATT_TA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga75036cc3ceecebccfbfc153a0cc9920f)
- [BT_UUID_GATT_TS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga188a456a10d2a44c19a6825bb288294f)
- [BT_UUID_GATT_TS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaaaed25b2d73258322825ca9d2460c1a1)
- [BT_UUID_GATT_RTI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga668e9e73668b1c00a3bac74080ad7bcc)
- [BT_UUID_GATT_RTI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5b241e9ab9be83919aa99c24da34fa4b)
- [BT_UUID_GATT_TUCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga89f6031ef8778c4eb281dcda1afe5688)
- [BT_UUID_GATT_TUCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaead8cf75f2bdecf9188272da2b3c5d41)
- [BT_UUID_GATT_TUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0511dd52eadfa58395981b621b31c635)
- [BT_UUID_GATT_TUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaeef7563b0eb39783afc3c86147262aee)
- [BT_UUID_GATT_GM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa11e9838368e470262efc07f86d12fc7)
- [BT_UUID_GATT_GM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga804ab92719239778e8328157876fce61)
- [BT_UUID_BAS_BATTERY_LEVEL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1961ff80d56b5c06185601cfce941cf1)
- [BT_UUID_BAS_BATTERY_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae4f41b4e329c728767a8a99a3a89af7e)
- [BT_UUID_BAS_BATTERY_POWER_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga818b6cbee38384f23e1548d49c89e53e)
- [BT_UUID_BAS_BATTERY_POWER_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga17d4a2ee5c7587ef35013f47dacfb95d)
- [BT_UUID_BAS_BATTERY_LEVEL_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7dcdb33b95cc58489343c9591fc0b453)
- [BT_UUID_BAS_BATTERY_LEVEL_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3022242a2bd7ccec5580d007182864dc)
- [BT_UUID_HTS_MEASUREMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga612376c2ac9b3b21e1fe07aa2c931fad)
- [BT_UUID_HTS_MEASUREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gade726271d11b08b573aec3a1a6794c55)
- [BT_UUID_HTS_TEMP_TYP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1e2c9c8bf1c27e0dd3fd37910a349d75)
- [BT_UUID_HTS_TEMP_TYP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7055bba7158854729f65f76841a32de6)
- [BT_UUID_HTS_TEMP_INT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4b13a008e37df4a0eb2b4b94bdb15126)
- [BT_UUID_HTS_TEMP_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga98f9fe29431766e819b3ea014294431b)
- [BT_UUID_HTS_TEMP_C_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga67a6e1c0f24628e0cd11a4311de5a6fa)
- [BT_UUID_HTS_TEMP_C](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga51ef3d61ceffb85824b920fa7b04bd62)
- [BT_UUID_HTS_TEMP_F_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga002d02e831aa0c3ca24b61b2527ac65b)
- [BT_UUID_HTS_TEMP_F](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6835b7816c5dc5bb4453e0b82925bb99)
- [BT_UUID_HTS_INTERVAL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac90751f69745ed65ff1739c1b86f3942)
- [BT_UUID_HTS_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga993de0f6c8904f1d1f8527d8a4f31946)
- [BT_UUID_HIDS_BOOT_KB_IN_REPORT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa842693e29c174601e84feb43098b543)
- [BT_UUID_HIDS_BOOT_KB_IN_REPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0ef3ddb08d602fcb513d348b1e1f2eb8)
- [BT_UUID_DIS_SYSTEM_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4fdfa6e582c6367aea30e9846653ebd3)
- [BT_UUID_DIS_SYSTEM_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaac15c93c66cb583c3819036a2bd5ba24)
- [BT_UUID_DIS_MODEL_NUMBER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga32a4462aa866ff15bf33046efde8e796)
- [BT_UUID_DIS_MODEL_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga250d08b7b3de123c866143599975aa41)
- [BT_UUID_DIS_SERIAL_NUMBER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga40c84dd8ce10d983596a4f6b9cfea82f)
- [BT_UUID_DIS_SERIAL_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga072770347ecf34cb89d293c31f59642d)
- [BT_UUID_DIS_FIRMWARE_REVISION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga220481d4fb2b498fad4e82637a0d02da)
- [BT_UUID_DIS_FIRMWARE_REVISION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga988bb4018b232cb4da64d522703ec5b3)
- [BT_UUID_DIS_HARDWARE_REVISION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3db6b3e905dd874c28a7b59c7a2a1b21)
- [BT_UUID_DIS_HARDWARE_REVISION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3842092a747954d24ceef3a0951efac7)
- [BT_UUID_DIS_SOFTWARE_REVISION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabef02eec1e667b2b35521a46b355d2e8)
- [BT_UUID_DIS_SOFTWARE_REVISION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8e9cc11f505e578851155659dc1ab262)
- [BT_UUID_DIS_MANUFACTURER_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac726ebb1cbc1d7ed63df41c232ee4a42)
- [BT_UUID_DIS_MANUFACTURER_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaefd466120c6923d806cfc4b5beb9899d)
- [BT_UUID_GATT_IEEE_RCDL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabf8a181cbe973c985c71aa6eb7d92fe1)
- [BT_UUID_GATT_IEEE_RCDL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3d95539bee32ca38ea825aadf85840fb)
- [BT_UUID_CTS_CURRENT_TIME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae8de32ab38c9e160dc1883c345063855)
- [BT_UUID_CTS_CURRENT_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae0a920c076eb504b448f390c320ccfb8)
- [BT_UUID_MAGN_DECLINATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6768ade4d8adf925fb52a27cee616e6e)
- [BT_UUID_MAGN_DECLINATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7322a8412c7aaf9e6f06473d3fa5186d)
- [BT_UUID_GATT_LLAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabc9b96c541f0711bf5525269c4b3e5b0)
- [BT_UUID_GATT_LLAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa9187bacfb95b379734ccf89f7eef163)
- [BT_UUID_GATT_LLON_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5d369d45c15dad30ccf7c3066863401f)
- [BT_UUID_GATT_LLON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae090952d14ae3db50edabbdfc4d8ae25)
- [BT_UUID_GATT_POS_2D_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaca1fdcec43844e0e6afeda46d7d60baf)
- [BT_UUID_GATT_POS_2D](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga21220783e6c7079bc9bd2f712b882dc6)
- [BT_UUID_GATT_POS_3D_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66b1060fd8eaf94955211b87c9d940c2)
- [BT_UUID_GATT_POS_3D](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga56e0a35ad8138b961f68155fa2091ae1)
- [BT_UUID_GATT_SR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga862122929d6e4717d21c84efc5869da2)
- [BT_UUID_GATT_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga720d3e1f20d70cffe312f983224c2335)
- [BT_UUID_HIDS_BOOT_KB_OUT_REPORT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga79c18c840c919a2824d7bb84fa2217b5)
- [BT_UUID_HIDS_BOOT_KB_OUT_REPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga67e34824d0d393dcbb401c91690bce00)
- [BT_UUID_HIDS_BOOT_MOUSE_IN_REPORT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga804ec93e78855249a4a0a692314f4bf9)
- [BT_UUID_HIDS_BOOT_MOUSE_IN_REPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae86aedfdbe15939df6384870e883bfa5)
- [BT_UUID_GATT_GMC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga95629cec83007634ec69516be8086d5a)
- [BT_UUID_GATT_GMC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1ca1906ee4fc482d5bb83664362c19ae)
- [BT_UUID_GATT_BPM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2342a077a10cbf649bb46f64e5fa24cb)
- [BT_UUID_GATT_BPM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga53f7809544d80bc8b797dfb0d0761ae2)
- [BT_UUID_GATT_ICP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf68e5c86b67a8065ca3a1dc8ed0bd9ea)
- [BT_UUID_GATT_ICP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga33ffcb4cc70f133a29bbbe6c19d6e964)
- [BT_UUID_HRS_MEASUREMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga44d502836331e3ffda5718d719e77ff6)
- [BT_UUID_HRS_MEASUREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga270ace7cd256a5441986d33becbbed05)
- [BT_UUID_HRS_BODY_SENSOR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafed38fc5d9727fb2b1d009975142ec44)
- [BT_UUID_HRS_BODY_SENSOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6021612c89adac51569a14565f1f6dd2)
- [BT_UUID_HRS_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga83825772db7f9d5c4376a78d44d10a60)
- [BT_UUID_HRS_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacec1c535fc0d96bbad3083240b5a87a1)
- [BT_UUID_GATT_REM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadb260392b00da4d849c03718aaf7d323)
- [BT_UUID_GATT_REM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga92564b1966ed0cacd36b13cdf44b9a04)
- [BT_UUID_GATT_SRVREQ_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gade09ce0a6c46fc85ada2d38c3240b953)
- [BT_UUID_GATT_SRVREQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66b18ba52088ed23136ffe121d350fa2)
- [BT_UUID_GATT_SC_TEMP_C_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2253ec9a6d97865c7408ea4ab18a392e)
- [BT_UUID_GATT_SC_TEMP_C](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2bb1b8f54f9cc4ef40650ad713181b49)
- [BT_UUID_GATT_STRING_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3b3f44113ca4a89e10d3d84eb02dd847)
- [BT_UUID_GATT_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4ca46824207979918b9a668cdf78e19a)
- [BT_UUID_GATT_NETA_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabd1aafbeaf157c4d515e5c2bae04823b)
- [BT_UUID_GATT_NETA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga98caa54c91df23461cac4b5db6a86330)
- [BT_UUID_GATT_ALRTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga11715889e92b0bf1942b3c4d84fa8aea)
- [BT_UUID_GATT_ALRTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0ef467a1b71b718216f08b21dca1e9b4)
- [BT_UUID_GATT_RCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaacbe74b5b9267f2398ea1bbde0300dc6)
- [BT_UUID_GATT_RCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga54702c100d46cb9dc358fd511dbc0b7d)
- [BT_UUID_GATT_RS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1479dc83c76a07d7000d3b53f8dee08d)
- [BT_UUID_GATT_RS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5c78797bbe75b3b66cbc0d6ff1b185fa)
- [BT_UUID_GATT_ALRTCID_MASK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga46356e3da57646e2a5bf2f6bc13e903f)
- [BT_UUID_GATT_ALRTCID_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7c905ac7003a24680ea6b2d3eeaee801)
- [BT_UUID_GATT_ALRTCID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab8423dbeb2c21e6c7bc90fcfe34c3a3a)
- [BT_UUID_GATT_ALRTCID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga207107524e82a8a34dc06263b434325f)
- [BT_UUID_GATT_ALRTNCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0ef4d1008dcfafce23b10ff3e9f13407)
- [BT_UUID_GATT_ALRTNCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0c0c2f7825242e43ad13c070d1a8c137)
- [BT_UUID_GATT_UALRTS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacfacfd310975fb4fd6f25c33e658dfaa)
- [BT_UUID_GATT_UALRTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacf608b24c1f0c1d10fdabd8594fe91d4)
- [BT_UUID_GATT_NALRT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga61f32ab52c24492cc2a1f0c9ee042987)
- [BT_UUID_GATT_NALRT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac66637f6bdb5c4efb56739ac3a370032)
- [BT_UUID_GATT_SNALRTC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2cc802e286be6c6d97835bc21eaa0433)
- [BT_UUID_GATT_SNALRTC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga30a9d308743e751e56890d48f6ef606b)
- [BT_UUID_GATT_SUALRTC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga64a81cfd5ce67cd6c1d27f0a7e7433bd)
- [BT_UUID_GATT_SUALRTC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga771c8d083004c4ef49e3334909f3d317)
- [BT_UUID_GATT_BPF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae5d786f2be340c5f126be0f500ade1f8)
- [BT_UUID_GATT_BPF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga639e0f8fe154cca9773dd84e21ecc4d5)
- [BT_UUID_HIDS_INFO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga929e50a821031cfb9c0faa3e2b0e9c4a)
- [BT_UUID_HIDS_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga28724b6efade76bfebeca2e8d7f9cdba)
- [BT_UUID_HIDS_REPORT_MAP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8b3812488738cf6202586b9202403663)
- [BT_UUID_HIDS_REPORT_MAP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga20a3521c85acd563064c5fc7ac022cda)
- [BT_UUID_HIDS_CTRL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabd625952d5706e851ff40b04e3d86547)
- [BT_UUID_HIDS_CTRL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8d867aac6ce50f6196c987438aa34c51)
- [BT_UUID_HIDS_REPORT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad6eea2097a8432254fd82ce3798869d7)
- [BT_UUID_HIDS_REPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga76e590c2499cc6d7540b0bbce20daec9)
- [BT_UUID_HIDS_PROTOCOL_MODE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7de83d3e0472f4edb4821e75fc209aff)
- [BT_UUID_HIDS_PROTOCOL_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga88f780ded3c66387af8825d7a3a1c8ba)
- [BT_UUID_GATT_SIW_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacc5bebeb6cd2fb4c1b0bc7a78a9c67a2)
- [BT_UUID_GATT_SIW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2bc786ce9acf331708f874261ab457d7)
- [BT_UUID_DIS_PNP_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab01c14fa28140cae03cae611ee1d32a1)
- [BT_UUID_DIS_PNP_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga259ece0a5de917da4a497563197bcafe)
- [BT_UUID_GATT_GF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaea2d0fd8564007e96dcdcab634896fd7)
- [BT_UUID_GATT_GF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga71ef8682466bc0418dfa848bf83af96c)
- [BT_UUID_RECORD_ACCESS_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga413047b20718bddff95b45e1be0b5125)
- [BT_UUID_RECORD_ACCESS_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8eedb1ff835988f3969a1b38713a6636)
- [BT_UUID_RSC_MEASUREMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga68f55222e780136b2c88ed9615c08f4e)
- [BT_UUID_RSC_MEASUREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga14a447a839d13bdc879da42399e39e63)
- [BT_UUID_RSC_FEATURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9f07e47cd086e3158f637dc2266f7acb)
- [BT_UUID_RSC_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4f64ed5b7c06c530320a9fa68794af3a)
- [BT_UUID_SC_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad4fd923bb1733c2e9dd993cafa8b5b01)
- [BT_UUID_SC_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9d6efa914c5a83dcd39ec502e5ac4178)
- [BT_UUID_GATT_DI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab1af32d2ba06891961e32b46917b39ab)
- [BT_UUID_GATT_DI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8c4a4fd21416af1be4a0ff2760c48786)
- [BT_UUID_GATT_DO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad9c70984dc907efd40e3652603012ada)
- [BT_UUID_GATT_DO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab39f19f3e38e8954cac13c4ba6db2234)
- [BT_UUID_GATT_AI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6b9158a8808fe72710023efac16f8d7e)
- [BT_UUID_GATT_AI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8f60411278ff93a3d590050ed4a87a70)
- [BT_UUID_GATT_AO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae6b9567925c04cde856d656c091540fc)
- [BT_UUID_GATT_AO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3f04b6880bc88de907a3c5b5e1acc10b)
- [BT_UUID_GATT_AGGR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadb16be338b14fbd82f7c33b6b92502e8)
- [BT_UUID_GATT_AGGR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7bc66b120e8a90631fe557c9393a7b88)
- [BT_UUID_CSC_MEASUREMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3465d2cfa3704021b137316d04d786b1)
- [BT_UUID_CSC_MEASUREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab3a6cac39fe5370fe4c23f43a165db2d)
- [BT_UUID_CSC_FEATURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7f697ab76e21d37c62080fe0b5a0e591)
- [BT_UUID_CSC_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa4d36cbd23dfb98f8baa5da37f7754ac)
- [BT_UUID_SENSOR_LOCATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae9aec5938fb89ffe510f66af4b330e19)
- [BT_UUID_SENSOR_LOCATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad639330b00b9f8ffcd62c6c1ef7b75d0)
- [BT_UUID_GATT_PLX_SCM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga828a25d5bd3e087a17460a6a0d10c0a9)
- [BT_UUID_GATT_PLX_SCM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0e691d0bdabf3b8df7c986b44eab4c85)
- [BT_UUID_GATT_PLX_CM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4eb8f3c1d2b33bac3b1e7e1d37cab6a3)
- [BT_UUID_GATT_PLX_CM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga73cf57feba3e1388ad052ffad5832bc1)
- [BT_UUID_GATT_PLX_F_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8b523306abec9cadcdc742c21d86d702)
- [BT_UUID_GATT_PLX_F](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga146ec7d39986333cd3583bbfc8ef27fd)
- [BT_UUID_GATT_POPE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaef6e49a81b4c5a7a32e17ed228a0415a)
- [BT_UUID_GATT_POPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7fa4ae596a22b9fef9db13a830cb8739)
- [BT_UUID_GATT_POCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac98748753db550fcd2bf338f4e11c246)
- [BT_UUID_GATT_POCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2ae69ed734761275ae0e4eb09080207a)
- [BT_UUID_GATT_CPS_CPM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabab0970b455fb1f0ea87fb3010782ed0)
- [BT_UUID_GATT_CPS_CPM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga607c07b67d8af3554e36943cea63d1b5)
- [BT_UUID_GATT_CPS_CPV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac4bde8ba3ccd35dbd94018d40438b8fb)
- [BT_UUID_GATT_CPS_CPV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga99de832aed97db92213ffe90efd60fd7)
- [BT_UUID_GATT_CPS_CPF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga97647d99503cc60a335d6b9bacc693e9)
- [BT_UUID_GATT_CPS_CPF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0b7fbbfa7d539676027d0345a3ce5d83)
- [BT_UUID_GATT_CPS_CPCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1efedae02d29eeca33b7e527506169e8)
- [BT_UUID_GATT_CPS_CPCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadc239b7879e9b3a082388331a50392c5)
- [BT_UUID_GATT_LOC_SPD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacc581ed161c7d5461b2d420b8b9a88f1)
- [BT_UUID_GATT_LOC_SPD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae3a4c256c950e72ecb5767b31033bcb8)
- [BT_UUID_GATT_NAV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga28c8f061887f0e0b25dff4d716a65d92)
- [BT_UUID_GATT_NAV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6e08e74465bf881a85136d99bec2dc3f)
- [BT_UUID_GATT_PQ_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga26f80b9d40ff1a9e6718150c337a018c)
- [BT_UUID_GATT_PQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1da56c6bd8423c99aa143756415aebc5)
- [BT_UUID_GATT_LNF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab3d9abfecb080e73c7f7309cfaa2760e)
- [BT_UUID_GATT_LNF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaee45af0edec1f2d7528b03b3d65f37ea)
- [BT_UUID_GATT_LNCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2026b24e2189a4fc8292487b7ee94429)
- [BT_UUID_GATT_LNCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga732fde43bbaf6f4c25d824013882089d)
- [BT_UUID_ELEVATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9ee48bd5d6b3ad89252c04861f6d8ff9)
- [BT_UUID_ELEVATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6a556f695cf7c608b9667ecec3091e32)
- [BT_UUID_PRESSURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9bb13b8b9d9212f8f7ef4559db81ab00)
- [BT_UUID_PRESSURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3c179c975cfd6f0797e1098d65d59654)
- [BT_UUID_TEMPERATURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9f420dc2ff26a723fe4cbdd467e64d47)
- [BT_UUID_TEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9ce10219c9d9b2f16b9bc101398a5093)
- [BT_UUID_HUMIDITY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa1739f28a51d563d6c9b77c2f7cbf081)
- [BT_UUID_HUMIDITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae6d2caca722e06366171b25659798478)
- [BT_UUID_TRUE_WIND_SPEED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab89e34d55bd53f075dac53f0720241ba)
- [BT_UUID_TRUE_WIND_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1bf8b992dc79021b1a3f876b2898d25d)
- [BT_UUID_TRUE_WIND_DIR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7d77a45acb17505099602df264b8bb96)
- [BT_UUID_TRUE_WIND_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0ba41218ce4954620dfe73f06089fc96)
- [BT_UUID_APPARENT_WIND_SPEED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad0cff10ce44864db5128c438e4be7c8d)
- [BT_UUID_APPARENT_WIND_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf6a81b9581f029463314fb25dd100e95)
- [BT_UUID_APPARENT_WIND_DIR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5eb592d6e55ca89ae5cd825edae6d508)
- [BT_UUID_APPARENT_WIND_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga69adddc8dc981d2b5d02ab604826e42b)
- [BT_UUID_GUST_FACTOR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga52857a87ddb7c2df50dcb8436804c7e2)
- [BT_UUID_GUST_FACTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0b97427c4d526e544b0fc1b778756941)
- [BT_UUID_POLLEN_CONCENTRATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaececeeeb1976c979aafafe3c892f8a59)
- [BT_UUID_POLLEN_CONCENTRATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa1a189a6d6b23f6983e38124e53aa8be)
- [BT_UUID_UV_INDEX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae30333c9b8a0b24f1fa6790872fc7a55)
- [BT_UUID_UV_INDEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab47898ad86865b6fd514f577e3b7d6f6)
- [BT_UUID_IRRADIANCE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa48c2c1a4c75a3b1071b0ef4ca480150)
- [BT_UUID_IRRADIANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1e5254104ebb5ccd9a1e3c0915891aad)
- [BT_UUID_RAINFALL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4ed507e7f1ecd49186411efbe4fc26ee)
- [BT_UUID_RAINFALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga71278019b98dac06d067227ce47320ba)
- [BT_UUID_WIND_CHILL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga424993240c213443fc9e95fa9d4ea913)
- [BT_UUID_WIND_CHILL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2bd92aab9da9f594d8a061922c51a137)
- [BT_UUID_HEAT_INDEX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3c0468464a353c37ff4994f49439d27b)
- [BT_UUID_HEAT_INDEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga56c812b5eb985ff21f91fb430d89deb3)
- [BT_UUID_DEW_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacf36659263e0a99aece77af08f4ca816)
- [BT_UUID_DEW_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf80bc7369817e44102e530371bdf7771)
- [BT_UUID_GATT_TREND_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabb35ed33581726b5eb3bd09abe3bf090)
- [BT_UUID_GATT_TREND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8b36445adba800c187208c2822a4c0ef)
- [BT_UUID_DESC_VALUE_CHANGED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadaf24469185095c9a64d09f9494202bd)
- [BT_UUID_DESC_VALUE_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga12ad8a70a766261bd258c5ff96dda1d0)
- [BT_UUID_GATT_AEHRLL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad0a8a823d03c2cfd29b330422d909468)
- [BT_UUID_GATT_AEHRLL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga185e4267f64937fae52a15297df555d0)
- [BT_UUID_GATT_AETHR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafe43bdafe5d04b4b5ff205ee9c4efa59)
- [BT_UUID_GATT_AETHR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga81826c45c657d1b6e1ab391776e37d04)
- [BT_UUID_GATT_AGE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga783cfd994944d68e137d4101943d3665)
- [BT_UUID_GATT_AGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga76fb417fd8e60358ae753d7139be227f)
- [BT_UUID_GATT_ANHRLL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac145e3d9d2b97eb18b059a0146bf4831)
- [BT_UUID_GATT_ANHRLL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8150d2662f87da3a2175f57236905dbd)
- [BT_UUID_GATT_ANHRUL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf160fd8971de7dcfd231474e928c20fd)
- [BT_UUID_GATT_ANHRUL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae8c042a675573ca1078b0eacc2041a86)
- [BT_UUID_GATT_ANTHR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga21eb08c2a91f869b792b5f71135c2586)
- [BT_UUID_GATT_ANTHR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga843badc1d786e621ef26b38fa973421a)
- [BT_UUID_GATT_AEHRUL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4e2a18435fac380402c890284f4b9cb2)
- [BT_UUID_GATT_AEHRUL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7477670294c4af4a0f55426653d382f6)
- [BT_UUID_GATT_DATE_BIRTH_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab72ef81ad3ad789c024749d05cf8a132)
- [BT_UUID_GATT_DATE_BIRTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga20f4e7f27ff0beae7239be8e69ec6cae)
- [BT_UUID_GATT_DATE_THRASS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga896c861e50c844d821f571297f9c5e54)
- [BT_UUID_GATT_DATE_THRASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf8dbfb3be192a96f6da53a897e853b52)
- [BT_UUID_GATT_EMAIL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf5b2e7bd75c03612409d34874275502b)
- [BT_UUID_GATT_EMAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf81242da24e4380fcf379cfc0a1bd2d6)
- [BT_UUID_GATT_FBHRLL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1b56739dbd398eede2689af120d2ffab)
- [BT_UUID_GATT_FBHRLL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafe6b60c5aeb090729e901de822a21179)
- [BT_UUID_GATT_FBHRUL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadaed267d894b3f6637ec65c3ebcaafbe)
- [BT_UUID_GATT_FBHRUL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga499864acace035767c673f7f992fb072)
- [BT_UUID_GATT_FIRST_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga05a1552396ae29c2e0e6f23e1e6fe41b)
- [BT_UUID_GATT_FIRST_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5668fc0689a92ef812ed7ee1c4bdd2e4)
- [BT_UUID_GATT_5ZHRL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0bf726af2e7015a870cdd67e2e055b48)
- [BT_UUID_GATT_5ZHRL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8c7ec19973ae92bb21e2c13bdc9762e2)
- [BT_UUID_GATT_GENDER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac5142588ca57f7c8202dab97e19c47f0)
- [BT_UUID_GATT_GENDER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5f51ed2cf6d32af22216a9fd2d444ed3)
- [BT_UUID_GATT_HR_MAX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8fe65597e6c89ad6fffc3f0c33169ebe)
- [BT_UUID_GATT_HR_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga94b53abaa40569423e0a47428379f42e)
- [BT_UUID_GATT_HEIGHT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa147b4c9f91f0d0675ffba0c715154ec)
- [BT_UUID_GATT_HEIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab80f4d69799421d48ab61a1832a575a7)
- [BT_UUID_GATT_HC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaedb0d5b971613bd7245c3f632b7a8a13)
- [BT_UUID_GATT_HC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3c3e534e884b6b5215a43528a51ff4e3)
- [BT_UUID_GATT_LAST_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga242f34d1b3dbb26c0efa62e0d23888ea)
- [BT_UUID_GATT_LAST_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabaae49281851c5d6626ef483b90e3d53)
- [BT_UUID_GATT_MRHR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga98a0f14a9a0ac32e48280b1ce441a6fd)
- [BT_UUID_GATT_MRHR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac855511d479c0c82971cadfff61a4178)
- [BT_UUID_GATT_RHR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaed3bfd56abb70c0dff169c1d2813ec18)
- [BT_UUID_GATT_RHR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4b425ea527897b54a0ed6871ce65b7de)
- [BT_UUID_GATT_AEANTHR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5303fd51cf82df81f635cc1213b7e7c8)
- [BT_UUID_GATT_AEANTHR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf80845ed35ef1e841c4805d1a1b346af)
- [BT_UUID_GATT_3ZHRL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafddfc45ece5b3f747190bd3de773ebbe)
- [BT_UUID_GATT_3ZHRL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0b303fde7bf69dfb0284034338ae1999)
- [BT_UUID_GATT_2ZHRL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa252d83bfa77990bc93d98bda035fd9c)
- [BT_UUID_GATT_2ZHRL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5389bd047e5b6769083a59114ed5603b)
- [BT_UUID_GATT_VO2_MAX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2e3de0e6f3ca1dbad4d7dc559f5bc093)
- [BT_UUID_GATT_VO2_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaec914c8c808dc5accb82f7c707f8f9c1)
- [BT_UUID_GATT_WC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6f843d3c3131abe778d3ec9ce1bcee7d)
- [BT_UUID_GATT_WC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga06e0730f0abf36dea42a713b22a0082a)
- [BT_UUID_GATT_WEIGHT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabd5f45139136449cac740e99e74a9894)
- [BT_UUID_GATT_WEIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga637f0da0906948ee5b7e40cc602ed167)
- [BT_UUID_GATT_DBCHINC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa88fbc8a584c60ad025447e72c5b0cb6)
- [BT_UUID_GATT_DBCHINC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafa555b52c6f195f3d01905a3923db9f3)
- [BT_UUID_GATT_USRIDX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadff9aa175bd9b12f9f882e24335aada5)
- [BT_UUID_GATT_USRIDX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga34b014cdec1c5cf41a65e47234eb3f4e)
- [BT_UUID_GATT_BCF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4cb5bc721905c8baa78dc25d9738cbad)
- [BT_UUID_GATT_BCF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3d96fa7aafedab4d8b2e9910a8db1029)
- [BT_UUID_GATT_BCM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafa981b32cb8b6babd737922ba8bf1430)
- [BT_UUID_GATT_BCM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9ade71ac5e947cc41d5ab6b747232a7d)
- [BT_UUID_GATT_WM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga68a0df5e07c31bf5d532c9ef64c1568c)
- [BT_UUID_GATT_WM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab9a5d321fb5d2854d7edbe66c4d8956c)
- [BT_UUID_GATT_WSF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae5fa58f25c54cbb228d816fb58eb5eed)
- [BT_UUID_GATT_WSF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7c084498045835ca6b9037758ccb437e)
- [BT_UUID_GATT_USRCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0e8380df1c605924bf794974b9a0c811)
- [BT_UUID_GATT_USRCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6cf64ee2a0564da8c5468842d4ccca72)
- [BT_UUID_MAGN_FLUX_DENSITY_2D_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga12df5c55e64d68377b144bbe6afc9fa1)
- [BT_UUID_MAGN_FLUX_DENSITY_2D](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7c6fe7de55f9167f0deb7e5793683df5)
- [BT_UUID_MAGN_FLUX_DENSITY_3D_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6eab42e702b2fe2f74ee316b565b6a15)
- [BT_UUID_MAGN_FLUX_DENSITY_3D](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga40845b75cd4b7ec5a561123f58e33f70)
- [BT_UUID_GATT_LANG_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1bf8e2d09646e1340f7195c90e7b53a5)
- [BT_UUID_GATT_LANG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8738fa7d86325f46ac3560b646afd96c)
- [BT_UUID_BAR_PRESSURE_TREND_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga820b05ac625c07d538697ddda5573b46)
- [BT_UUID_BAR_PRESSURE_TREND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1fcf3463c69e2974877bfa953c9cbe52)
- [BT_UUID_BMS_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa3b803e6b55d72d830f0ee01cfc1c1f4)
- [BT_UUID_BMS_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga08c91b0e746cce311a0c96bf4347d300)
- [BT_UUID_BMS_FEATURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga666cd38fd2225997e302c0517b7d7070)
- [BT_UUID_BMS_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1d998f7915295eeec0895cfa9d500482)
- [BT_UUID_CENTRAL_ADDR_RES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad7e8753c103960268eafdf4b8fa5710e)
- [BT_UUID_CENTRAL_ADDR_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf3c3da6a9485674f8865764a831e6011)
- [BT_UUID_CGM_MEASUREMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacec2ac2f394b7d8af60163568581c9ac)
- [BT_UUID_CGM_MEASUREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga634603e1545a177d0ccfad140103f7e5)
- [BT_UUID_CGM_FEATURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga693fb44bd4fe9b2da9071b04170bed8a)
- [BT_UUID_CGM_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6be4b6b21e0c5f1dd06f45e309cc4097)
- [BT_UUID_CGM_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0c2ebf2de8e5f2a83ebc2f11a6a79441)
- [BT_UUID_CGM_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga040dec91474ceaf096c2864eb0f46bff)
- [BT_UUID_CGM_SESSION_START_TIME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6f646767f25f2d94cb1190ad4acef86f)
- [BT_UUID_CGM_SESSION_START_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0f17cfb12a8c4d628a26f7c83c8a7f4b)
- [BT_UUID_CGM_SESSION_RUN_TIME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga98d88d1b785d3b71b9e3b95864efdbf7)
- [BT_UUID_CGM_SESSION_RUN_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0f8565339251160fb439d06f5b29b4cf)
- [BT_UUID_CGM_SPECIFIC_OPS_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaec1bbb364e33912fcc22e63c369e4c77)
- [BT_UUID_CGM_SPECIFIC_OPS_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga820aab0acff43919e2710b3d5f93ef4b)
- [BT_UUID_GATT_IPC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafe31f631bf3f9a232214dafa76b35ba6)
- [BT_UUID_GATT_IPC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga350bcb39fe9c71f12e5661e4157e95f2)
- [BT_UUID_GATT_LAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadda62951b9abf642684b266f1f073856)
- [BT_UUID_GATT_LAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0dcbbd018fd83efcb84721146fa8c47d)
- [BT_UUID_GATT_LON_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga89312e66f25972bced92a8ea1574037a)
- [BT_UUID_GATT_LON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga59aa1b51e5948c649d0d49d5d7fe45ed)
- [BT_UUID_GATT_LNCOORD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab8183450fa0b94f92709a76f58ce041c)
- [BT_UUID_GATT_LNCOORD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf1294000d6653870589cd0d4e2d3f05f)
- [BT_UUID_GATT_LECOORD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga700e5b0a5be6ba38c882692da43e41f0)
- [BT_UUID_GATT_LECOORD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac7d73c69f971bad67095ee6ad03ed0f2)
- [BT_UUID_GATT_FN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga64e22e58c78f09f8614079bb8cd4092e)
- [BT_UUID_GATT_FN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7fd58fd3410975a1a66f03bdcebabdc3)
- [BT_UUID_GATT_ALT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5b30f97c97ee5006390ab895f4bc438e)
- [BT_UUID_GATT_ALT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga10bdfef928a7cd1da6bf3b3406121c99)
- [BT_UUID_GATT_UNCERTAINTY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaeff0f6c7ab86eb8b264d80d579ad4aa5)
- [BT_UUID_GATT_UNCERTAINTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5fc1842a9886deb02cc28887b2e21155)
- [BT_UUID_GATT_LOC_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa7c22c7d434e3a9b9e2f3f44bd75dad1)
- [BT_UUID_GATT_LOC_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa5418e610552e13acaa2c675564ae776)
- [BT_UUID_URI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafb86347f61b0e745bf3b970eb6cf71b0)
- [BT_UUID_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaee04f3121fa14082ffabc4d705325449)
- [BT_UUID_HTTP_HEADERS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf489c9885e90b49b0f072d365c6a7098)
- [BT_UUID_HTTP_HEADERS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad88c1b58957bbcc2df817628a6f756db)
- [BT_UUID_HTTP_STATUS_CODE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga257e4213c8e4aa4e6b61dba44e36b268)
- [BT_UUID_HTTP_STATUS_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf2e15b1eabca8c810e7f61ee0d650450)
- [BT_UUID_HTTP_ENTITY_BODY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga84600520548f966e511355ee94edbcde)
- [BT_UUID_HTTP_ENTITY_BODY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2336a53590edbb9ba14c7aacfa36a592)
- [BT_UUID_HTTP_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga37eb19663266e076c35cfa0c73dd0f4f)
- [BT_UUID_HTTP_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga996630b67869b95babf5f7b280f26c49)
- [BT_UUID_HTTPS_SECURITY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacaa02070d2036c0cc76b16437e1cc62b)
- [BT_UUID_HTTPS_SECURITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga365519de0ab148b5820442eca52ad700)
- [BT_UUID_GATT_TDS_CP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga44d037f49e771f08da2381c981fb6ea6)
- [BT_UUID_GATT_TDS_CP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga90f08ee842d221580b036d154417c122)
- [BT_UUID_OTS_FEATURE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga763bb4a64fa3ba2cd3680858d24dd200)
- [BT_UUID_OTS_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6bf7967b64150e3bc7f849fa19ddfe7c)
- [BT_UUID_OTS_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4768610413b66751e9e38eef00bc4516)
- [BT_UUID_OTS_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa6b72769537df80ba5450b6a398b21ff)
- [BT_UUID_OTS_TYPE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1e313ee3c5d5047b8d629d99976c1e32)
- [BT_UUID_OTS_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga94b169c80d3d351c85535d085366086b)
- [BT_UUID_OTS_SIZE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6072d84794782c93b6c8cb5f30707d9d)
- [BT_UUID_OTS_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae24957c8aad49fc0f98570b6b313098a)
- [BT_UUID_OTS_FIRST_CREATED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab0c3ef2ee627f77c46cc78ec1b6e5543)
- [BT_UUID_OTS_FIRST_CREATED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae5ac09c297a770ebbf7f2a344d24d153)
- [BT_UUID_OTS_LAST_MODIFIED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa9016cda30f09bd61b38654d87198694)
- [BT_UUID_OTS_LAST_MODIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga06f1570cde6df5e932c72417fe59daef)
- [BT_UUID_OTS_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad32cdd62e0bead3599de3b3dd6e4e014)
- [BT_UUID_OTS_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf301617baf5a039c202f0993d80061ce)
- [BT_UUID_OTS_PROPERTIES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0360f97a4f18b56ae3dac4e9b0287602)
- [BT_UUID_OTS_PROPERTIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga215d8088166c529ad1d0024a8f362e3e)
- [BT_UUID_OTS_ACTION_CP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7ebe0c55c503cb82cf4d0ee3838f50fe)
- [BT_UUID_OTS_ACTION_CP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga29c7bec908eeff922e1aaa3043278d2b)
- [BT_UUID_OTS_LIST_CP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga145f367de3db51b96ea6922017380aa3)
- [BT_UUID_OTS_LIST_CP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8acbfefbe1b7cbb5a7aba290d6e7effb)
- [BT_UUID_OTS_LIST_FILTER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga675bd50dd63de1a13363b041eefc1634)
- [BT_UUID_OTS_LIST_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabca5bfb5f6fb4a92f29752cb686c7d88)
- [BT_UUID_OTS_CHANGED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaea820a540c02088355739bf6ec6e26ba)
- [BT_UUID_OTS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga45dc6f040b210aac136b018c760ac37e)
- [BT_UUID_GATT_RPAO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga080af564ef60858fe3ddc0c487f06e97)
- [BT_UUID_GATT_RPAO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5db6e037e7020b467a5218f828b8a7ea)
- [BT_UUID_OTS_TYPE_UNSPECIFIED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga74f28ba3693c541b909580c4fd262416)
- [BT_UUID_OTS_TYPE_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadc3afb0781f51b2550b077ee24ce9227)
- [BT_UUID_OTS_DIRECTORY_LISTING_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2fee72d19822abcf76cedfbfd96d4cdc)
- [BT_UUID_OTS_DIRECTORY_LISTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8f306bef03ca5204c99befc1c6e71225)
- [BT_UUID_GATT_FMF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga556cd0fd7d3ff4f862dd3028f0206462)
- [BT_UUID_GATT_FMF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2aeb2e0aa454feb4438f9527c52780ed)
- [BT_UUID_GATT_TD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaedc6e4f493355fe2999e7f1f84bf5d00)
- [BT_UUID_GATT_TD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa8a7f082cf9b4df21c07ded6a4913b35)
- [BT_UUID_GATT_CTD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga235dc61fb231d43a5aaab0b32f398a48)
- [BT_UUID_GATT_CTD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga47d30eeb1bb66bb84b8b315fbeb76eea)
- [BT_UUID_GATT_STPCD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga84863f0507404fd9637319c384468808)
- [BT_UUID_GATT_STPCD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4fd0ee59f5451669a389814d4390c6b5)
- [BT_UUID_GATT_STRCD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga222ab56024893f1019af55052f646aca)
- [BT_UUID_GATT_STRCD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae0b7d7316806ee18c4300b399faeb52e)
- [BT_UUID_GATT_RD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaed2b696b1a2ecbe1e981437ee9e58389)
- [BT_UUID_GATT_RD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga933043dfadcbebbbb2c10a828280c0a0)
- [BT_UUID_GATT_IBD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga92198d40e1a682c0c7515ba306af2093)
- [BT_UUID_GATT_IBD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf6d86dfccb1bf3796b1dbd3c087b8127)
- [BT_UUID_GATT_TRSTAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga13e94c01279818ad0ce923051bf4fd1c)
- [BT_UUID_GATT_TRSTAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5a7f9c7d6d0e93f2d35ff308b875f883)
- [BT_UUID_GATT_SSR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadad6f8c3d4cf5f40c5f1f27d5ea38ac3)
- [BT_UUID_GATT_SSR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab6ef5e742460fba12f8b974fc4bf735d)
- [BT_UUID_GATT_SIR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6339f09bf4e825454fd8c517faf53194)
- [BT_UUID_GATT_SIR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac69a06d1568114dec01f46df95a3c5ac)
- [BT_UUID_GATT_SRLR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf6fae4763a3aa3fe1f04b51b108ca642)
- [BT_UUID_GATT_SRLR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4141c63e9e7924c8d9e27922ebda4b98)
- [BT_UUID_GATT_SHRR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8516dbe4b6b630f380f9ab3a80bce179)
- [BT_UUID_GATT_SHRR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabe5693829c64f8cd98444c853e0f121c)
- [BT_UUID_GATT_SPR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1f7f6e8197940264ff921e6dec5c2e81)
- [BT_UUID_GATT_SPR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab82bacbce14b886d23f9368db97bb329)
- [BT_UUID_GATT_FMCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf910e7d5ce12084045e9283b4c5b8b7e)
- [BT_UUID_GATT_FMCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga26b12f1ef3313b7c28328ae22512b277)
- [BT_UUID_GATT_FMS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaea596e91c046949687c4331a4841dd07)
- [BT_UUID_GATT_FMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9ff5045f804b6a2a8cd0b2ec8906e4b3)
- [BT_UUID_MESH_PROV_DATA_IN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2bde466cfcaeec5c542d5e74f51ddd05)
- [BT_UUID_MESH_PROV_DATA_IN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaae548e7ca5a9835bd4dcfdf853c43993)
- [BT_UUID_MESH_PROV_DATA_OUT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafd6e15eb3ae65d5f480706e68aabad8e)
- [BT_UUID_MESH_PROV_DATA_OUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa003522c72e96e8b2c4b7b724aa2bf2e)
- [BT_UUID_MESH_PROXY_DATA_IN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga55488739e50c8482da6f4ad0826f0cae)
- [BT_UUID_MESH_PROXY_DATA_IN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaebcae07983c397b0771f424d2d890259)
- [BT_UUID_MESH_PROXY_DATA_OUT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga452dfb3d0f4b62ec327910b9c578ffb0)
- [BT_UUID_MESH_PROXY_DATA_OUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf3fbcbebb0507aec45d94244729f85d8)
- [BT_UUID_GATT_NNN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab01aec4c2f19b53d919c89b58fd92956)
- [BT_UUID_GATT_NNN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga355480e43c9fd2ee1e7fa72a05141c93)
- [BT_UUID_GATT_AC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf2bc7408a53341478f1b41d54e888478)
- [BT_UUID_GATT_AC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadbe14281482e776e87facb9835f522af)
- [BT_UUID_GATT_AV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2b5c1eef80844de1d49a70314db91b1d)
- [BT_UUID_GATT_AV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3c669e805ea7fc93cade56f2281b10dc)
- [BT_UUID_GATT_BOOLEAN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0e1cbd1ae5c198c0f834802f9d354fb7)
- [BT_UUID_GATT_BOOLEAN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1801b550a1be17bf0bb8c07818749e4e)
- [BT_UUID_GATT_CRDFP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2601e0757464729c789b58deeee15285)
- [BT_UUID_GATT_CRDFP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac5bc300a9b31543dc3847990832d78c3)
- [BT_UUID_GATT_CRCOORDS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8fa1863d2ae7b22462be097308fb5c81)
- [BT_UUID_GATT_CRCOORDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac43c1fdab4869d79c423399c864f6088)
- [BT_UUID_GATT_CRCCT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac6ef845c60c6d68ad0c3269690e97d51)
- [BT_UUID_GATT_CRCCT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga52a4a6bcb91935822f7e21fecbb283bc)
- [BT_UUID_GATT_CRT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5d65027929bf31cdbdacc167c3f28951)
- [BT_UUID_GATT_CRT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga94c83c03f6cb240374af1bc4ec1b5f32)
- [BT_UUID_GATT_CIEIDX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga361d00b8be7dc6c3d319a138bf5be1b9)
- [BT_UUID_GATT_CIEIDX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga706f4f40760275742a9834d4b94cd1ed)
- [BT_UUID_GATT_COEFFICIENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga298d1f0c9a48695488c7b211a7de66a9)
- [BT_UUID_GATT_COEFFICIENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga941228f8812bfda85e86a15185a1270d)
- [BT_UUID_GATT_CCTEMP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5533c28dc6bcaad3f66678d0e90a4e88)
- [BT_UUID_GATT_CCTEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2562158387beea244d57757e9e87422e)
- [BT_UUID_GATT_COUNT16_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2c292a6bf086b695dce4c8a6fcb2e331)
- [BT_UUID_GATT_COUNT16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga770c5a643468816820bdcc5db2af8d69)
- [BT_UUID_GATT_COUNT24_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga360c3c084ac6f8f4ae6c0f8ddb1f2cf3)
- [BT_UUID_GATT_COUNT24](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7191613ab08efa46949ecb67d3512180)
- [BT_UUID_GATT_CNTRCODE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga77981b5aad0c0424a08c0bbc86c5ca71)
- [BT_UUID_GATT_CNTRCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf83aeabd260ea7d027aafa69beb2b050)
- [BT_UUID_GATT_DATEUTC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad551c08d84b220342831bbb1d358efd6)
- [BT_UUID_GATT_DATEUTC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4151cbfefc334f33800be8fdc853ca34)
- [BT_UUID_GATT_EC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5ae0a7207e95f6aa2d982877057453d2)
- [BT_UUID_GATT_EC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9c86c847e1f2bb2deb23dbf4382b003f)
- [BT_UUID_GATT_ECR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga67e672df782986945ab3103c4ddff412)
- [BT_UUID_GATT_ECR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac2121117e06e8d90448733b7e2ac9b97)
- [BT_UUID_GATT_ECSPEC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafd1eeaf887046c9f2785089a81275153)
- [BT_UUID_GATT_ECSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaabdf693ada22d60cb524b501b3203b59)
- [BT_UUID_GATT_ECSTAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga198d44bb45cf18921841e1788aeaa774)
- [BT_UUID_GATT_ECSTAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6a1b29e07ffd6240e138c2a0ab1d6525)
- [BT_UUID_GATT_ENERGY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad6a61da207a152987afcad67fe4633d2)
- [BT_UUID_GATT_ENERGY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga556811cb737ddccf121dda3d65f2d79f)
- [BT_UUID_GATT_EPOD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab14d5fbaaa0e06c51db1cd41fcc368de)
- [BT_UUID_GATT_EPOD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2c5e6339a8d25083ce8656f02298cc57)
- [BT_UUID_GATT_EVTSTAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafec2c62ae00f7efb506341edf08b0d9a)
- [BT_UUID_GATT_EVTSTAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa8f949e568dce7f639aeb80415674e2a)
- [BT_UUID_GATT_FSTR16_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5d80019b1543d04e7cc5c7dc0f969c8c)
- [BT_UUID_GATT_FSTR16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8970252d984fd463369baab7445f7bf6)
- [BT_UUID_GATT_FSTR24_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafa6970b19301bfc1c5f3dc6392850bd8)
- [BT_UUID_GATT_FSTR24](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga421bb2147cbf541fed439273ee5f2119)
- [BT_UUID_GATT_FSTR36_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2b90639839a47260c7f555eec0b8bcd0)
- [BT_UUID_GATT_FSTR36](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0a03f71c8d0b616f3a496efe4b5c6561)
- [BT_UUID_GATT_FSTR8_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabafdb729c08aae0debace870f6043930)
- [BT_UUID_GATT_FSTR8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7b2a21e708cc13937038a3b88c0ad58b)
- [BT_UUID_GATT_GENLVL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga18a4861ba81ae7f0a9ff0f1de37a6a0b)
- [BT_UUID_GATT_GENLVL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7250c5f01251cf185035c18cf5d087c6)
- [BT_UUID_GATT_GTIN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1419411a928165a5cc4a26f0a97358d7)
- [BT_UUID_GATT_GTIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga27ef69db6e19c23b4f735bfbe2c83b7a)
- [BT_UUID_GATT_ILLUM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf660977f7494cecb5bd2d1d4808b0531)
- [BT_UUID_GATT_ILLUM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacb727e39a14240931183e4cc608f3114)
- [BT_UUID_GATT_LUMEFF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga742681175c952de8840c70df64b1562b)
- [BT_UUID_GATT_LUMEFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3441cb7f9449be2ba9cc5cd73505f894)
- [BT_UUID_GATT_LUMNRG_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gade0213130552d2757d74cdc2abe12d65)
- [BT_UUID_GATT_LUMNRG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa9ad315787bedcd20206b8dc99af4081)
- [BT_UUID_GATT_LUMEXP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3f2d4a042fb00481383b7b5e8837f24e)
- [BT_UUID_GATT_LUMEXP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga38d3dd48f55ebfde06d52310324088d4)
- [BT_UUID_GATT_LUMFLX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga26f37ccbd862af70e5fa7516e59da73e)
- [BT_UUID_GATT_LUMFLX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae05c06b201217e919c8493d3245b2f52)
- [BT_UUID_GATT_LUMFLXR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab1080ef3dffbc5521c8f587766ac22d6)
- [BT_UUID_GATT_LUMFLXR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga93a7fa9b6c9bbd12ef5d9a7169405e59)
- [BT_UUID_GATT_LUMINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga00cfabe28348d7a86a54608b8f0ec3de)
- [BT_UUID_GATT_LUMINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaefd8b48d82a4c403e735badb04e812b4)
- [BT_UUID_GATT_MASSFLOW_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga23f13789b3f3f19691dbfdc3a33a506e)
- [BT_UUID_GATT_MASSFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8670491866b6b62a3834c4f619612a7d)
- [BT_UUID_GATT_PERLGHT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4b8ec7d1538e6655b065a488d8c523af)
- [BT_UUID_GATT_PERLGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0f13aca1a13cc11b7e1adf7c1f7e75b1)
- [BT_UUID_GATT_PER8_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4bc9aee30308246d28eb96152eb686b1)
- [BT_UUID_GATT_PER8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga60ea8b576b1d3951be45cb928ce841b0)
- [BT_UUID_GATT_PWR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac70e24a9a91738c615e83e6238c96ed7)
- [BT_UUID_GATT_PWR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa374060d2715bfab9986c1eee2467ed5)
- [BT_UUID_GATT_PWRSPEC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3db91205384fb559aa9f8865c15356d1)
- [BT_UUID_GATT_PWRSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad69a1f73335555e9a7c164ebd2474371)
- [BT_UUID_GATT_RRICR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac5533a77612f300dd8f1cd8ccd2ee522)
- [BT_UUID_GATT_RRICR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7c3534f8bd7b9c662e73cd9d46dc8c79)
- [BT_UUID_GATT_RRIGLR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga41b95788eb3271a8fe87766fe903e8d9)
- [BT_UUID_GATT_RRIGLR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2e1c29cac1ece5f3fad29c61ed2b0aa4)
- [BT_UUID_GATT_RVIVR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3bb5af173f013c8a49227b2920bc107)
- [BT_UUID_GATT_RVIVR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaac802734c88aac862fcab0599cb2e216)
- [BT_UUID_GATT_RVIIR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2866d911411268e5026ef729efa990e9)
- [BT_UUID_GATT_RVIIR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga165f79f1dcde1e7359a4c4602dc88c40)
- [BT_UUID_GATT_RVIPOD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab73b24f9941a80fab6423ff85f68aae6)
- [BT_UUID_GATT_RVIPOD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9e6b0e6585f2ceb62dd236a0ae3afc6a)
- [BT_UUID_GATT_RVITR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaac84e4bcae1a1b83af9124688e01912a)
- [BT_UUID_GATT_RVITR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8c8e5e43e2bc8f7c26344fff4127e039)
- [BT_UUID_GATT_TEMP8_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa7a119bfd7df636f0ed0bf515232e6bb)
- [BT_UUID_GATT_TEMP8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga146d14e283686a5712c90698fd6a64ad)
- [BT_UUID_GATT_TEMP8_IPOD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga616708b903a88a6bb9eabdae60813063)
- [BT_UUID_GATT_TEMP8_IPOD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3d28ebdcaa93ed4ccdee512f7ddd979a)
- [BT_UUID_GATT_TEMP8_STAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3d54ad101d044924da30aa81a6b64111)
- [BT_UUID_GATT_TEMP8_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga071d32c5e9dd24fc179f8cac531e499f)
- [BT_UUID_GATT_TEMP_RNG_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadcdd9e4d2cfa09f6d766b513224ef7bf)
- [BT_UUID_GATT_TEMP_RNG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga99e73003bde4dac095f198dd7045b297)
- [BT_UUID_GATT_TEMP_STAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga035eaed3f130c2222236fdc194f9b1a4)
- [BT_UUID_GATT_TEMP_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8ae19f54cd4aa1c7ab42c48f33080f52)
- [BT_UUID_GATT_TIM_DC8_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae5f1cda9dbc55f77cfbb4c00f4e359f0)
- [BT_UUID_GATT_TIM_DC8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae9feb929d7a7eb67dc1db02ce26cc82b)
- [BT_UUID_GATT_TIM_EXP8_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga07a0510f652506225410b1865882d1ea)
- [BT_UUID_GATT_TIM_EXP8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5e4aee6898f1ab1f8065c113241c99bd)
- [BT_UUID_GATT_TIM_H24_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga272a11fc6d56e685243f6507708f8032)
- [BT_UUID_GATT_TIM_H24](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac209c86c368f2ed7c20bae2b90f36a0a)
- [BT_UUID_GATT_TIM_MS24_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga181a187356797362b4a7d9a7d22f7fdc)
- [BT_UUID_GATT_TIM_MS24](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga941191900854cfed39dae2b5dfba499b)
- [BT_UUID_GATT_TIM_S16_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2ad71e9a1912c84f31072edcf3234093)
- [BT_UUID_GATT_TIM_S16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga216c5c11e143571c5b40e7554c40ab91)
- [BT_UUID_GATT_TIM_S8_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae7ad9e90132e56a59d3fb3cfaea55faa)
- [BT_UUID_GATT_TIM_S8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacf36b122fdeb96d6da4b710506118668)
- [BT_UUID_GATT_V_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae727674510a76ca337ea57c4222791ab)
- [BT_UUID_GATT_V](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1cedb6e5b998d0edf435dd4203fee96c)
- [BT_UUID_GATT_V_SPEC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5bc426767e92938654f24f0158a16b53)
- [BT_UUID_GATT_V_SPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga23440a5aff26bf0a737d4a48b6ce301d)
- [BT_UUID_GATT_V_STAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac655949e3c565b8835b099a93a24498f)
- [BT_UUID_GATT_V_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac1d74460417a592cbd4f5b6528c77e28)
- [BT_UUID_GATT_VOLF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae37019af7703f5b3abb99bcfbb1d5343)
- [BT_UUID_GATT_VOLF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8ddcea2b365f55ac647562063ede0f3c)
- [BT_UUID_GATT_CRCOORD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf7b547b7f4c6908f601afc33d0d0ebb8)
- [BT_UUID_GATT_CRCOORD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga53a898269a7f5ab84e9853521f69bc69)
- [BT_UUID_GATT_RCF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8b2d587922902479e47bd316443e0a56)
- [BT_UUID_GATT_RCF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac6961922da80f8c628a35b8855cb788b)
- [BT_UUID_GATT_RCSET_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga47316949dd2eb5571e3b94240a4e6c90)
- [BT_UUID_GATT_RCSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2af1f07e6e4484476740db5bb6b31b8f)
- [BT_UUID_GATT_RCCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaabe52b93d5ac1e72c468be08fdea35ef)
- [BT_UUID_GATT_RCCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga48b7a42b204407553262ea68e53f65d7)
- [BT_UUID_GATT_IDD_SC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadc4e7dcda6314aa68b4165199ddc4123)
- [BT_UUID_GATT_IDD_SC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab36f1fff60a7657844985841bb0350f8)
- [BT_UUID_GATT_IDD_S_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafb1511371c0c19323989961689425d08)
- [BT_UUID_GATT_IDD_S](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga560d7cef69190752eb8a5c4f6fed5989)
- [BT_UUID_GATT_IDD_AS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2e854242941b30552241e1ee3669d669)
- [BT_UUID_GATT_IDD_AS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga980781b7142c177ed46b8caca9b8b518)
- [BT_UUID_GATT_IDD_F_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7d20cc62ad420b71d299361430005d27)
- [BT_UUID_GATT_IDD_F](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga369b0b1ddac085d2812a42f737bdd594)
- [BT_UUID_GATT_IDD_SRCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1e817e253f29e03a98327e08c2048e6b)
- [BT_UUID_GATT_IDD_SRCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga13d829bfcacb036a2271cd09491c1578)
- [BT_UUID_GATT_IDD_CCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1dc738c5c564bf05d3c2669a79db6e17)
- [BT_UUID_GATT_IDD_CCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf2bc260638bc158b8bfd403bf43de2d9)
- [BT_UUID_GATT_IDD_CD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga70d6ece9b4d331965c42f0606c0c7526)
- [BT_UUID_GATT_IDD_CD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac7dbb4cb283933558699d129928e37d5)
- [BT_UUID_GATT_IDD_RACP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab9ef1f54711a8d7d5884c7b3a798f615)
- [BT_UUID_GATT_IDD_RACP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga628c153b88ea0f504c234dc44248a237)
- [BT_UUID_GATT_IDD_HD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga26f24abf219ce90fd002d995e3a19d30)
- [BT_UUID_GATT_IDD_HD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga88e2087b512092d91508f8e878a22f3a)
- [BT_UUID_GATT_CLIENT_FEATURES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga54537cebc8ce6e7d8d0f377a38765635)
- [BT_UUID_GATT_CLIENT_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae3faa1515f3aae0c71d4face04929dec)
- [BT_UUID_GATT_DB_HASH_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacead7897f5fed798714a79df2764d95a)
- [BT_UUID_GATT_DB_HASH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6b162958f4f406fd3e3d31a84393fe19)
- [BT_UUID_GATT_BSS_CP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf609e6663173f4c4bb6ed18274f9931b)
- [BT_UUID_GATT_BSS_CP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadeabab76545da0de52cc26d48e564730)
- [BT_UUID_GATT_BSS_R_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga73cbe100a043e8f08b87fcfed82107ad)
- [BT_UUID_GATT_BSS_R](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae9f0db1cbcc6dfeda9beb96e14350cf6)
- [BT_UUID_GATT_EMG_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga77157df8db39286f6f6edf1dd71f4a5e)
- [BT_UUID_GATT_EMG_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6fdb1cd7bf1323b27645180ca39ca063)
- [BT_UUID_GATT_EMG_TXT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabcea55cbf065daab8709e4d36941ad90)
- [BT_UUID_GATT_EMG_TXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1bc6805b2948d3f36af972f2ee34f93a)
- [BT_UUID_GATT_ACS_S_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7d46292e64c3a8bc9a2ddd71418e56c8)
- [BT_UUID_GATT_ACS_S](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad94f7adb29687b460fb7bb860023d890)
- [BT_UUID_GATT_ACS_DI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0b19f25f01532abb98b63438d55b7683)
- [BT_UUID_GATT_ACS_DI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabd8886704d8fba31bbb1f9a8aeee9aa3)
- [BT_UUID_GATT_ACS_DON_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga08ffe10a9e5e1f716581d96dd49bebac)
- [BT_UUID_GATT_ACS_DON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0933ee4e3740e4f6c28522113b84c5b0)
- [BT_UUID_GATT_ACS_DOI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga852f095873bee6c0dec742ea45817294)
- [BT_UUID_GATT_ACS_DOI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4875b80953686217209dc8a90e705ff2)
- [BT_UUID_GATT_ACS_CP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga492e0766dd16dea9e63e80423c9210cb)
- [BT_UUID_GATT_ACS_CP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabd2164db62c4f29d2bafc272178312e5)
- [BT_UUID_GATT_EBPM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3016f0dd266a98f7d88a3198f54caf7e)
- [BT_UUID_GATT_EBPM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafe7d80c67c7c059c174c2ec8aa6cf92d)
- [BT_UUID_GATT_EICP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad61213ed875c9d0b6bd5a2e7154f80d7)
- [BT_UUID_GATT_EICP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab5032246e17304cb99bb619e6a3d70f1)
- [BT_UUID_GATT_BPR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5b59d10e5d4653ed774a05da55241368)
- [BT_UUID_GATT_BPR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafa84009c324ee2e0a36efd0bbb486d4b)
- [BT_UUID_GATT_RU_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4ac04b637bed53a51dbf598bd54a827a)
- [BT_UUID_GATT_RU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8a00648e37c023bf06be268960071d27)
- [BT_UUID_GATT_BR_EDR_HD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab89358d9db126f1eb9e1df6dc4639b82)
- [BT_UUID_GATT_BR_EDR_HD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga279da4b9d9aaccd67846d3ff93e25516)
- [BT_UUID_GATT_BT_SIG_D_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf95bc5640e25a651bb62f474fbdbd0f0)
- [BT_UUID_GATT_BT_SIG_D](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga268e9d8096668ef890f5c17c76c882c5)
- [BT_UUID_GATT_SERVER_FEATURES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8d23a276e657bccde1385066ce2cd709)
- [BT_UUID_GATT_SERVER_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga261af6f050c6a16d174c80cfce48b13e)
- [BT_UUID_GATT_PHY_AMF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad94da8852116cc6651c2bb75b8420c95)
- [BT_UUID_GATT_PHY_AMF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6d227d76b62bcec99cc8a8b6b8054474)
- [BT_UUID_GATT_GEN_AID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8302d0d60c536b9862028633c8155a3a)
- [BT_UUID_GATT_GEN_AID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacfbd8563c68df3aa15264fc81f0eabb8)
- [BT_UUID_GATT_GEN_ASD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4865adb3aadcb01834444e7fda021162)
- [BT_UUID_GATT_GEN_ASD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3b068ab73e6c277692a535b81b6e9ae1)
- [BT_UUID_GATT_CR_AID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac82a202322d7ee65130150d09d82b76a)
- [BT_UUID_GATT_CR_AID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga35d88cb3312b6867d153780ee3a57be2)
- [BT_UUID_GATT_CR_ASD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6606c6d6ac05bbdbbbd27af5c28b825a)
- [BT_UUID_GATT_CR_ASD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadac7397ba9891282ef425e05c8161938)
- [BT_UUID_GATT_SC_ASD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2aed9d07c8f4d552a4d6a5c2b693e97e)
- [BT_UUID_GATT_SC_ASD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9dd42f8966856001425c4bae4f6dc5a5)
- [BT_UUID_GATT_SLP_AID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabb73d22b90482201f9f20d6f89aa6671)
- [BT_UUID_GATT_SLP_AID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf0a5a409f91366422f145acbb45e4abd)
- [BT_UUID_GATT_SLP_ASD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa309ce83ee85407cc8068aaccec95b94)
- [BT_UUID_GATT_SLP_ASD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5232c5aac8c20f23aaadf1a023d91fcb)
- [BT_UUID_GATT_PHY_AMCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1c2a6903fe19f05e4515122ddd6e454f)
- [BT_UUID_GATT_PHY_AMCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga59ef934ce5ccf5e4ed309319f75c1150)
- [BT_UUID_GATT_ACS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad5ea6f8f92b3679cafed3ac61f5d9128)
- [BT_UUID_GATT_ACS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga12e8344ffb0ae5d3ff088df56f22d440)
- [BT_UUID_GATT_PHY_ASDESC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga16b2c15259a5c4d456a43df7be9080d6)
- [BT_UUID_GATT_PHY_ASDESC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3906642c3830a0dff787b6218f502b74)
- [BT_UUID_GATT_PREF_U_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae9e12c4297a520b3d626fbd7f4e9c49c)
- [BT_UUID_GATT_PREF_U](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga323afc65d2c3568d9a3267328e46879e)
- [BT_UUID_GATT_HRES_H_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab74738d5e1fde9be0ae137603d58266a)
- [BT_UUID_GATT_HRES_H](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf095ec3ea1b24f184fce737db3b16855)
- [BT_UUID_GATT_MID_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae44137b7932e5493b66c037b93177f30)
- [BT_UUID_GATT_MID_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga478706893a1e14f1af28928ea7ee3dde)
- [BT_UUID_GATT_STRDLEN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8ebc62a93e6c323031cd64a4c89bc191)
- [BT_UUID_GATT_STRDLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1a05d2cef4e003d8a9f417cfb1915600)
- [BT_UUID_GATT_HANDEDNESS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa3a2515dfef7871cb4f2ddaa9b1838bf)
- [BT_UUID_GATT_HANDEDNESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9e0dd2e887dacb08466f63951bdce22c)
- [BT_UUID_GATT_DEVICE_WP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7e3028631b4f17fc6127eb41343f6113)
- [BT_UUID_GATT_DEVICE_WP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf26f9aa3d7566892cb4d851a212c7a26)
- [BT_UUID_GATT_4ZHRL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaff4928b6e4a0e7329ab18beed9600f1a)
- [BT_UUID_GATT_4ZHRL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1ead62ac6b72dfafdbe46f3c6a3202a1)
- [BT_UUID_GATT_HIET_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7fcf423cf762d9c9b534c869581ef358)
- [BT_UUID_GATT_HIET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa0a5aa82b3eccfc14eef8ce4006899f8)
- [BT_UUID_GATT_AG_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga80d44e488176d215f9da4c531915b9f4)
- [BT_UUID_GATT_AG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8ab5d539f23fd30b6b44294d52cd148f)
- [BT_UUID_GATT_SIN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9f129bc582093032197016897e86748f)
- [BT_UUID_GATT_SIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaac75b92f8daddb4aecd5b6e0b2a5d33b)
- [BT_UUID_GATT_CI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga462b52ed2ca39b836e0d7ea3d7a6a609)
- [BT_UUID_GATT_CI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga61d3e8f34e0f3d466d4a0b64258a6d13)
- [BT_UUID_GATT_TMAPR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga781de482737cfc42662f6e8b1114070f)
- [BT_UUID_GATT_TMAPR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66395bad8099540561670bd1e588e1e9)
- [BT_UUID_AICS_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga95a4d3f8c62782325d2f2bb0df260a97)
- [BT_UUID_AICS_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga36fff8099e5a7d9c0cbd407b9b261742)
- [BT_UUID_AICS_GAIN_SETTINGS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaab9ed2f83db5e1ea5c2756b8045ca708)
- [BT_UUID_AICS_GAIN_SETTINGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0b26573f473babc0d4b4d1f817a0e292)
- [BT_UUID_AICS_INPUT_TYPE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga60250c00a3361316b78e5fa6fef335d7)
- [BT_UUID_AICS_INPUT_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf9ba49297331bec61b2706ad43a88260)
- [BT_UUID_AICS_INPUT_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga369eeaa589fbb61fffe8e3dabab5aebf)
- [BT_UUID_AICS_INPUT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga549930ceca2598871f140ec81778923b)
- [BT_UUID_AICS_CONTROL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacd6c279c902bb8dfa59e886f52161f9a)
- [BT_UUID_AICS_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae507a2c877c174accb4eb1c18fd7bbc4)
- [BT_UUID_AICS_DESCRIPTION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0cb5c04f3f8c257d012d9907ba8cde38)
- [BT_UUID_AICS_DESCRIPTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9de23aa540a7e07e4c932d60dd84f7c5)
- [BT_UUID_VCS_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga40235c24d4ab2f3c068e8833295bfb89)
- [BT_UUID_VCS_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac116f24a102a7b8e6aa80533cc096615)
- [BT_UUID_VCS_CONTROL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga303c174785d397db54c53572c421e6d3)
- [BT_UUID_VCS_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga24d297c008c9679dcb7078f68affe0a1)
- [BT_UUID_VCS_FLAGS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7f3385da26bf4cddfe12f48147457baf)
- [BT_UUID_VCS_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga47ff83b277e87cf0629a633a67567e34)
- [BT_UUID_VOCS_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae5535cd478c55390fa3c1199584e614d)
- [BT_UUID_VOCS_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1d198cbdb65d99eb877fa871f4ac5155)
- [BT_UUID_VOCS_LOCATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga784c29647d14983b3d3f37f9188b6b6f)
- [BT_UUID_VOCS_LOCATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad3493dcb58547b4108e8ded6e48e8a8c)
- [BT_UUID_VOCS_CONTROL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacc2e4a9ac1e93bf6ed1a7001c8038a52)
- [BT_UUID_VOCS_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafb68257cf790e12dab2b888320617de7)
- [BT_UUID_VOCS_DESCRIPTION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga46471ebc019b7c842c0b76efed504625)
- [BT_UUID_VOCS_DESCRIPTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad4a8b4af9f5935b86d1541a2086609d3)
- [BT_UUID_CSIS_SIRK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadaf8b170c1f603f8a61515090558b96c)
- [BT_UUID_CSIS_SIRK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac0a3863cf4a928bfaae397b14771622d)
- [BT_UUID_CSIS_SET_SIZE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7b5cf381c0806b01fc91c806588a3cfc)
- [BT_UUID_CSIS_SET_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8995e2ac9173ab613c35f56c5a353d69)
- [BT_UUID_CSIS_SET_LOCK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7f296b9f8b09bc62e639b2e1076894dc)
- [BT_UUID_CSIS_SET_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf6493077e90f87765c1c1efc044436f0)
- [BT_UUID_CSIS_RANK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga21db384fb731b1903239a4ecc70138d4)
- [BT_UUID_CSIS_RANK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa356de4e79779132ed4eeda837b7db57)
- [BT_UUID_GATT_EDKM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga31e072f6706b28c309e518cd9449b883)
- [BT_UUID_GATT_EDKM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9b0daac4f03e23c10fca1a40d07e1618)
- [BT_UUID_GATT_AE32_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac74ea8f9e2800086c286c5fa4185a00e)
- [BT_UUID_GATT_AE32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga646adee056d3097eb180bdea1ad0fd33)
- [BT_UUID_GATT_AP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3a8b96b59612b0e4ef704afae04e7e3)
- [BT_UUID_GATT_AP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga91eea2c307dfa99632b52d062c2a2645)
- [BT_UUID_GATT_CO2CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa1edc406495ec9797e153daf1e6cca1f)
- [BT_UUID_GATT_CO2CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab4db18c78e70c6e781dcda022be13276)
- [BT_UUID_GATT_COS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7a568dfc0ac219b16bdd606953b88184)
- [BT_UUID_GATT_COS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7d456cc3cdf5d6b25a35f6cca08da585)
- [BT_UUID_GATT_DEVTF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7da79c223cdfb3be45607e86f71a6caa)
- [BT_UUID_GATT_DEVTF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7e8485b07e0c359964be7b6f8e896546)
- [BT_UUID_GATT_DEVTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga744f71f5b0c8d2cfe4faf6107f33633b)
- [BT_UUID_GATT_DEVTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0f22bf31cbe7a58944340b03ccf591c5)
- [BT_UUID_GATT_DEVT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7d0ff38d80780d63e4b43a200be5c7d3)
- [BT_UUID_GATT_DEVT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9eb6c84a8ab924deb9fbe5b331d2628a)
- [BT_UUID_GATT_DEVTCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga111396f18a4d565fabe50e4ab4bb6b01)
- [BT_UUID_GATT_DEVTCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga18de8889aa0297fc80a6fc2846f83da2)
- [BT_UUID_GATT_TCLD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2aa7a226cd54e1e2435a045cd936c222)
- [BT_UUID_GATT_TCLD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0e38fdb6334c4aa1b3fe8163cad290ea)
- [BT_UUID_MCS_PLAYER_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga26421e4fde9e424af8318a2a06e55729)
- [BT_UUID_MCS_PLAYER_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga25706c3572dd91b223dd7cbea6cc71e2)
- [BT_UUID_MCS_ICON_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadefa705eae4221748b18f5a088c768ca)
- [BT_UUID_MCS_ICON_OBJ_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga63ce9edebeebcac1e7344efdabc6519e)
- [BT_UUID_MCS_ICON_URL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad80db7e88bc50944b71ca4c51f6674db)
- [BT_UUID_MCS_ICON_URL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1ff74274cc34b8ba88af2b455109eb98)
- [BT_UUID_MCS_TRACK_CHANGED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga71cb9b105eb4a581167e09fb293d7dd5)
- [BT_UUID_MCS_TRACK_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae7e7b15660158399bd837f10c1380982)
- [BT_UUID_MCS_TRACK_TITLE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8082647831b1da4237b85346f1dca249)
- [BT_UUID_MCS_TRACK_TITLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafb41d75e4bf569b1efeba763fb93722f)
- [BT_UUID_MCS_TRACK_DURATION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7786188af799df504bcbba1aa007a3eb)
- [BT_UUID_MCS_TRACK_DURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga76d4d2c92df6b9d82d60ee7fe835d29c)
- [BT_UUID_MCS_TRACK_POSITION_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6b74c773a708eccb84074cb7ef8c8fe2)
- [BT_UUID_MCS_TRACK_POSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa4665539c5027680a843d851bf1b8bfe)
- [BT_UUID_MCS_PLAYBACK_SPEED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadfe7acf9dbc6ebd3fe21fe469f39e937)
- [BT_UUID_MCS_PLAYBACK_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga47629d64d3ed4587089fb8551c4c594c)
- [BT_UUID_MCS_SEEKING_SPEED_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf8ebb66a23e2bed1c7e5b08c79cfe579)
- [BT_UUID_MCS_SEEKING_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac1d6109a86c67555c4b632d6a0563d92)
- [BT_UUID_MCS_TRACK_SEGMENTS_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafa793d37f3d9c57d1f456a0a9c5dba36)
- [BT_UUID_MCS_TRACK_SEGMENTS_OBJ_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa1e0e61ba28da785308e5dafd72931fd)
- [BT_UUID_MCS_CURRENT_TRACK_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga884f66865500c127def77f2764b7a322)
- [BT_UUID_MCS_CURRENT_TRACK_OBJ_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad11916b1a6704ce9cc80a35ddd1b1023)
- [BT_UUID_MCS_NEXT_TRACK_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga791f147766bd7511fdeb98ed9f4e3e05)
- [BT_UUID_MCS_NEXT_TRACK_OBJ_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaba85414e514d71f1ada3cd32ab7b9857)
- [BT_UUID_MCS_PARENT_GROUP_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga06410ca2d5575cb44f3f365c27960487)
- [BT_UUID_MCS_PARENT_GROUP_OBJ_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2dbb766bda1581f49ff331beefdad2c5)
- [BT_UUID_MCS_CURRENT_GROUP_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3873c1d5075d4cb3035509ce57595c28)
- [BT_UUID_MCS_CURRENT_GROUP_OBJ_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga303b89c5ba301bd2c18a3eb48f214ded)
- [BT_UUID_MCS_PLAYING_ORDER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0b17cfa67cdec5722cf51ebc9a616384)
- [BT_UUID_MCS_PLAYING_ORDER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7c676d7019e19189cffaf34aefe66c59)
- [BT_UUID_MCS_PLAYING_ORDERS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga103cd4f0ae88b27c32ab7854c331de59)
- [BT_UUID_MCS_PLAYING_ORDERS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga283a2f22a049a6c78221d1186d17e6f5)
- [BT_UUID_MCS_MEDIA_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8f62ba6fe627eda5c188151a89d1299f)
- [BT_UUID_MCS_MEDIA_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaadaf94fbf0d316505e27fc115998ffd2)
- [BT_UUID_MCS_MEDIA_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3b276420dc39941339c3f3bcb3835d3c)
- [BT_UUID_MCS_MEDIA_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae3dc24d21d36349c7af95fe90db6ec91)
- [BT_UUID_MCS_MEDIA_CONTROL_OPCODES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6eb18372f842f362bb45c93bbefd560b)
- [BT_UUID_MCS_MEDIA_CONTROL_OPCODES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6ef3d74033d401d7d5fb092485faee16)
- [BT_UUID_MCS_SEARCH_RESULTS_OBJ_ID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga337509c52a77206589a8208cf6ac3ac0)
- [BT_UUID_MCS_SEARCH_RESULTS_OBJ_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2ce71ff006f161cd899fb6b09a98c66f)
- [BT_UUID_MCS_SEARCH_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab89e74c66515dfcdffcb4967b3de4f0d)
- [BT_UUID_MCS_SEARCH_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab7892abc4201dc18da2bd4a2efca1963)
- [BT_UUID_GATT_E32_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8f238d8197b3293562809916eb667f27)
- [BT_UUID_GATT_E32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6419bfcbe6cad1f568b9e212d704e7c7)
- [BT_UUID_OTS_TYPE_MPL_ICON_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaeb12a1e806156ec1b7f945dddce3fa24)
- [BT_UUID_OTS_TYPE_MPL_ICON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3b425e5f019ba59d2d76a5d6e9cc16ee)
- [BT_UUID_OTS_TYPE_TRACK_SEGMENT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf05ecc673eae8b56ce6d5a98e5b22130)
- [BT_UUID_OTS_TYPE_TRACK_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5f3fdbd12cc804ed0ca811d4bafe1109)
- [BT_UUID_OTS_TYPE_TRACK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf4094e3381053890f6264d17ff129255)
- [BT_UUID_OTS_TYPE_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafcf9774a2b6aa1081b6c1a03b31a0c07)
- [BT_UUID_OTS_TYPE_GROUP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafc689c443c46385aefbca0e1db73f877)
- [BT_UUID_OTS_TYPE_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7a6fd4221135821cd15a3ba10f33532d)
- [BT_UUID_GATT_CTEE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6577476ef4d85191e5d5533f6bb99b2d)
- [BT_UUID_GATT_CTEE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga985a0ebcc0a61e2c4d9f2f61a7a1afb0)
- [BT_UUID_GATT_ACTEML_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaca4a23a27a2c06eb10da1a64c617cac1)
- [BT_UUID_GATT_ACTEML](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga51915bb0637c157a67ce4488e46905a6)
- [BT_UUID_GATT_ACTEMTC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad3ddda1c88208094616608b178bb27ec)
- [BT_UUID_GATT_ACTEMTC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga47620598a9365d2fc8d70ada1144c9c1)
- [BT_UUID_GATT_ACTETD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga165c63f8c91f61a9930b3c804f7051b7)
- [BT_UUID_GATT_ACTETD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5a15560d93177634882ff117b35deab4)
- [BT_UUID_GATT_ACTEI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3be14ce89c7c291cdde2bf1f4ce85808)
- [BT_UUID_GATT_ACTEI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga492d6a8c673f4df65d34abad342f4e75)
- [BT_UUID_GATT_ACTEP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac32badacbe9099b6f00d5c3d780cdbfe)
- [BT_UUID_GATT_ACTEP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaff802fc0d7358acf3bd4bf3209d7aa15)
- [BT_UUID_TBS_PROVIDER_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaca347be4dd1f019c5d7421d7c2c0dd29)
- [BT_UUID_TBS_PROVIDER_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafaff1ecd49123fab18bce167342a0d3e)
- [BT_UUID_TBS_UCI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga361ef37fd71a78544ffcbfd34ecbff6f)
- [BT_UUID_TBS_UCI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2d4349fc96395f603cada574841a90d2)
- [BT_UUID_TBS_TECHNOLOGY_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga066546cd6eb07098643b0fa331b813d3)
- [BT_UUID_TBS_TECHNOLOGY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga37ec4aed5afafc2751ef3902f2ef7d73)
- [BT_UUID_TBS_URI_LIST_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5e499b3bcb22b0ddd719aba4fed5c644)
- [BT_UUID_TBS_URI_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6c76f72b427694a1e1180b0d2a2adb38)
- [BT_UUID_TBS_SIGNAL_STRENGTH_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga44859b71e874ca148e708fde37882c4b)
- [BT_UUID_TBS_SIGNAL_STRENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf5ebde9e6e4121909d8a165dee7fda3a)
- [BT_UUID_TBS_SIGNAL_INTERVAL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga726edee9ad2a92f2a5687a3320f68f99)
- [BT_UUID_TBS_SIGNAL_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga189f78c9eb6829851ab0497a0e6e3f51)
- [BT_UUID_TBS_LIST_CURRENT_CALLS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1fcc7e36b3ca482eca7572c77fe3bba4)
- [BT_UUID_TBS_LIST_CURRENT_CALLS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa5aea84109af0027aae9829169ab7789)
- [BT_UUID_CCID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga01899f1d2f5ec81669b5012ab1448e5b)
- [BT_UUID_CCID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab76981ff7b5fe1949c606e901daa33d3)
- [BT_UUID_TBS_STATUS_FLAGS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga250a14189efd3cc176ae159de0ab03ed)
- [BT_UUID_TBS_STATUS_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8f465ca9874ff4889614f13fa7057c87)
- [BT_UUID_TBS_INCOMING_URI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga89ec945699c44fbbb220fa6798efa986)
- [BT_UUID_TBS_INCOMING_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa11ae7df9db3a1a3576a413db9d70539)
- [BT_UUID_TBS_CALL_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga07adb1e98dfdeaa84efeb28a53087286)
- [BT_UUID_TBS_CALL_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf3c8e758416d2d7d34adb4be895f1ed0)
- [BT_UUID_TBS_CALL_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadc6f999aa7d3ebc821405bac4ed4bf35)
- [BT_UUID_TBS_CALL_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9870653514120a07d85e4ea4f0a83f6e)
- [BT_UUID_TBS_OPTIONAL_OPCODES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0e2f14bde4f81d44bdd4171e1bfae68e)
- [BT_UUID_TBS_OPTIONAL_OPCODES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9c794c63e6c216b9a4a7518207ea7268)
- [BT_UUID_TBS_TERMINATE_REASON_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab146e7f4f8b965634967ea7845a7d875)
- [BT_UUID_TBS_TERMINATE_REASON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5eb69cfa65d293421bd2f6797cf1bdd0)
- [BT_UUID_TBS_INCOMING_CALL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaee6b14bcbd32f18efc4d7f805455deb1)
- [BT_UUID_TBS_INCOMING_CALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4ec4bdf60129003573b79f8ffe993f20)
- [BT_UUID_TBS_FRIENDLY_NAME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga598672b6e2aa0bc58c62ac9755aaf64c)
- [BT_UUID_TBS_FRIENDLY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga32682d7390ccb0aafd82b57255007749)
- [BT_UUID_MICS_MUTE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga24667ed9a87ae7f1b529cfea8515b7f3)
- [BT_UUID_MICS_MUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gada38c5574c186c19c71788d612bb7987)
- [BT_UUID_ASCS_ASE_SNK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga780a810da56da9b9dbba775305f70c69)
- [BT_UUID_ASCS_ASE_SNK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6542839cbcda51b512d04f1039840964)
- [BT_UUID_ASCS_ASE_SRC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gace1bd537f3ecee4715efde2b68ebce70)
- [BT_UUID_ASCS_ASE_SRC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae520d2f81b0ee284d42e80854217c209)
- [BT_UUID_ASCS_ASE_CP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6eeb6b573908fe77254894cf3efc5378)
- [BT_UUID_ASCS_ASE_CP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga79416b6f0e79ee43bf9b495ec94cca4b)
- [BT_UUID_BASS_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad66cb5c49c932d3546fb549c6febeaa0)
- [BT_UUID_BASS_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4d8a9467cf5fce4f6be36d160075984c)
- [BT_UUID_BASS_RECV_STATE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6c69b13ecbcca8121e6bbe49b58eb799)
- [BT_UUID_BASS_RECV_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga384b5b68bff445f353762e1e15d85aa4)
- [BT_UUID_PACS_SNK_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac27fec8eb7a757709f647cbaf5b9735f)
- [BT_UUID_PACS_SNK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf103bb8e2866a7ab7df90f8b62d4edcd)
- [BT_UUID_PACS_SNK_LOC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3df681f24778459df49c4f2e8cae6c4b)
- [BT_UUID_PACS_SNK_LOC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab54021bccf67751069b0cf5eaef8c61c)
- [BT_UUID_PACS_SRC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa7c87310bea3593a8097fa20ec4c2c88)
- [BT_UUID_PACS_SRC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga958e64cfd0f6b21095b2de28f3b4a0ee)
- [BT_UUID_PACS_SRC_LOC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga13eee95752b5b248888ad0328c2c7f99)
- [BT_UUID_PACS_SRC_LOC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0c89cb848378466beba18c389286cac7)
- [BT_UUID_PACS_AVAILABLE_CONTEXT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga64798749d367c63e3d9ed2d07a236e37)
- [BT_UUID_PACS_AVAILABLE_CONTEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0017f4e6621ba40e51062b8f7c77a634)
- [BT_UUID_PACS_SUPPORTED_CONTEXT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga63588c6624da5cba5b53e07c869c16ff)
- [BT_UUID_PACS_SUPPORTED_CONTEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4f61367e2c6aeac35f2054759389306b)
- [BT_UUID_GATT_NH4CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga68bf0922cd7486337b912f8cce89140d)
- [BT_UUID_GATT_NH4CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7204a371be3fb10d382ea00bc76b5102)
- [BT_UUID_GATT_COCONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga397cccc077652fe327b7ceab3ccc1f4d)
- [BT_UUID_GATT_COCONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab599f83b69654c1b3be91429d9f7bf32)
- [BT_UUID_GATT_CH4CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga13ecd6003180e0ed73d7aa80542dddd6)
- [BT_UUID_GATT_CH4CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad0496cbb8cf296852fe85b7694c1e3a8)
- [BT_UUID_GATT_NO2CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga37fdb9197c3003175875337df66c0937)
- [BT_UUID_GATT_NO2CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1a0f1553bbf70517af224fd32a5842f6)
- [BT_UUID_GATT_NONCH4CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2023c3c8c4fdf714a66dc64984a9f198)
- [BT_UUID_GATT_NONCH4CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6770e5f7e2f46c604ada573dd8b950e9)
- [BT_UUID_GATT_O3CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4a022ea0079ebc09dedf5f472a8755ee)
- [BT_UUID_GATT_O3CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga23054b696f62c03afb73a0f5286dc2d5)
- [BT_UUID_GATT_PM1CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8dde1677ff60c1970c427e9b984e24d9)
- [BT_UUID_GATT_PM1CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9c39a445bab4603148d4256bcce23a5b)
- [BT_UUID_GATT_PM25CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga055b7900ffda40c9ec4e1870abc1d855)
- [BT_UUID_GATT_PM25CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga88d2f1f4afcb89267c713144f84f4f7f)
- [BT_UUID_GATT_PM10CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaebebc238d90e667f33d2c95690d67376)
- [BT_UUID_GATT_PM10CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9668baee783462813c530f411da07890)
- [BT_UUID_GATT_SO2CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf7ee2d08cd80e1d4afc777457217508d)
- [BT_UUID_GATT_SO2CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3c7b7be6268bb748f7406737eaa129e2)
- [BT_UUID_GATT_SF6CONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaba0853f84e9e33dd4d7d71ecebc31bb6)
- [BT_UUID_GATT_SF6CONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf17d7037cdaed65e208df3792f1fd2d3)
- [BT_UUID_HAS_HEARING_AID_FEATURES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad4967e4904cd371940af8b135da21f47)
- [BT_UUID_HAS_HEARING_AID_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaebd2bbb103e6928059f1a76eac55916b)
- [BT_UUID_HAS_PRESET_CONTROL_POINT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6fdc731a19072629917ce6ebf28c7fee)
- [BT_UUID_HAS_PRESET_CONTROL_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7f3a8eea9e7ee68d8865809a061a0e96)
- [BT_UUID_HAS_ACTIVE_PRESET_INDEX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae9b2bf949e992c7cd6f1aaaa49888189)
- [BT_UUID_HAS_ACTIVE_PRESET_INDEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9ef9b65a7c9a105798691a2cdffbaf7a)
- [BT_UUID_GATT_FSTR64_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac18b9e325ef1db22774f8da35b888223)
- [BT_UUID_GATT_FSTR64](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac617c317945f2b6d45de15eca1190823)
- [BT_UUID_GATT_HITEMP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2a3928912a6eed082deac4893fb4f980)
- [BT_UUID_GATT_HITEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8d9bad6c04ea4cf096d0d010208e1d2a)
- [BT_UUID_GATT_HV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2b707ca8b876eded6b3adf9bb7132479)
- [BT_UUID_GATT_HV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1104d7e9d1571aacdb77693c64a15edc)
- [BT_UUID_GATT_LD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga67e534b02154fd7ff94b5ed21616f5f2)
- [BT_UUID_GATT_LD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5f68a688a1347d84bd28aa3df7252be9)
- [BT_UUID_GATT_LO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa127fa12de6d6a641183641853439708)
- [BT_UUID_GATT_LO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacc7b122d7a849291a5c9c877acfbd50a)
- [BT_UUID_GATT_LST_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga34f9f97b35397e713f655b888845d443)
- [BT_UUID_GATT_LST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2794fa8a9e1030826b4d382cc59f835a)
- [BT_UUID_GATT_NOISE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab3b7b78bfb8b5dfd30a1751ce9ffaee7)
- [BT_UUID_GATT_NOISE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaeb4d264b70d6d6c87a34f0da320f8e7a)
- [BT_UUID_GATT_RRCCTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8cbc0843565303e78f564517c21feb0f)
- [BT_UUID_GATT_RRCCTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0f5bffe28d45d35fa2dc6680bc52476d)
- [BT_UUID_GATT_TIM_S32_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9fd1550589d248be145b120c446181ee)
- [BT_UUID_GATT_TIM_S32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac76fc378354bcd1a8c706f7438a90ebb)
- [BT_UUID_GATT_VOCCONC_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabf10e337b78be1ab371fbef771109c53)
- [BT_UUID_GATT_VOCCONC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7181f9f1dfaae6cfe3fd8cedd8c20917)
- [BT_UUID_GATT_VF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4c57416ae5e84133339e3fab0ba31918)
- [BT_UUID_GATT_VF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae8500640959d58da51aee03fa75c85ba)
- [BT_UUID_BAS_BATTERY_CRIT_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaad27c84d46c85c4fc436e2d57249e562)
- [BT_UUID_BAS_BATTERY_CRIT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga678d5e47dee2070ce9208538c529460b)
- [BT_UUID_BAS_BATTERY_HEALTH_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0dd78641b14fa1affa283f3f53a5f194)
- [BT_UUID_BAS_BATTERY_HEALTH_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa442c41b04c72f1a7a983e0c6561b90d)
- [BT_UUID_BAS_BATTERY_HEALTH_INF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3324d4b7047cab8fb2c033c4c92c5793)
- [BT_UUID_BAS_BATTERY_HEALTH_INF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga62ad5685a1fcbb18afd57c7ded6463a0)
- [BT_UUID_BAS_BATTERY_INF_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga04f0ff51790e2c759b401f36a989f6b7)
- [BT_UUID_BAS_BATTERY_INF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad6dffe9e9e9684b2a943471e0a6c0918)
- [BT_UUID_BAS_BATTERY_LEVEL_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf14fdc69148ba65b5fb7fe9d42706787)
- [BT_UUID_BAS_BATTERY_LEVEL_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga54a26381c17065abbda1eb4c2a35c244)
- [BT_UUID_BAS_BATTERY_TIME_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8a1d978914a8cb9c3744b4b333e38f46)
- [BT_UUID_BAS_BATTERY_TIME_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga25e2b1b84d5b9dd46ae79ab26752a02f)
- [BT_UUID_GATT_ESD_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaff547b9ef568ae7ae70fdb18cbced21b)
- [BT_UUID_GATT_ESD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga432ba40acfbe03c50b4a3ede80b972c1)
- [BT_UUID_BAS_BATTERY_ENERGY_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7af8620512a789611a3c6c96bcbd6c06)
- [BT_UUID_BAS_BATTERY_ENERGY_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadc442a139fff871f63d5e11be37c8231)
- [BT_UUID_ETS_CURRENT_ELAPSED_TIME_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaeb700085e464d9ee63350ec3fd06d6c7)
- [BT_UUID_ETS_CURRENT_ELAPSED_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf27d2fbbf83f1193a8d400dcba6f4a2b)
- [BT_UUID_GATT_SL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga87e7a8d4ea7c2f0b4345c3ddd83e2bcc)
- [BT_UUID_GATT_SL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga07c07b64d8d06b76b64c71109dd39bc4)
- [BT_UUID_UDI_FOR_MEDICAL_DEVICES_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1904b4b736c5949b544cfd3cf270b9a1)
- [BT_UUID_UDI_FOR_MEDICAL_DEVICES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1d0210d3557a3838a4b04bedf413e80c)
- [BT_UUID_GMAS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga791ebaadcc3fac61cda4001d1dadc044)
- [BT_UUID_GMAS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae48cde28242dd2813cb9259a3db4cd0f)
- [BT_UUID_GMAP_ROLE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8a9ca3e7c352dcc5c6b4834f1c1b188c)
- [BT_UUID_GMAP_ROLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacb7897b761dc608e7814a2ad103e47a2)
- [BT_UUID_GMAP_UGG_FEAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9a79627722acfc4c93b2d251aefd8b83)
- [BT_UUID_GMAP_UGG_FEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafcdc548a86c976b07fa57bd0ccaee9c9)
- [BT_UUID_GMAP_UGT_FEAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga24f317039700e33d09f6244d74e4c024)
- [BT_UUID_GMAP_UGT_FEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaf3b064865efb4e566ea3d00b1de932e1)
- [BT_UUID_GMAP_BGS_FEAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5aa7be5ea8b74329c07f7de879e9ab2f)
- [BT_UUID_GMAP_BGS_FEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0aa83932e08ed22c1d75464b77e23b0c)
- [BT_UUID_GMAP_BGR_FEAT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5b7fcf7e18179190c3cd3ec2289ebcd5)
- [BT_UUID_GMAP_BGR_FEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0d13271568a11aceb9a6d169cdb6474c)
- [BT_UUID_HIDS_SCI_MODE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga445fdadef349779dd2da0553b11baf35)
- [BT_UUID_HIDS_SCI_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae3b45358af78c1eb24ffd1f719f7e495)
- [BT_UUID_HIDS_SCI_INFO_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga66f968bf7d0e1fee8946dcdb73eaf6b5)
- [BT_UUID_HIDS_SCI_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga377f64178319aa5f6d8c52233422fd50)
- [BT_UUID_SDP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa82cf709aaa5986ada534ac4c24aa407)
- [BT_UUID_SDP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga82f35da766ed6acfe18de8d119d19859)
- [BT_UUID_UDP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab0d4e8012eef2d067b63e8e538d6317c)
- [BT_UUID_UDP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga51e5cf4018099907c64eabf219a193c8)
- [BT_UUID_RFCOMM_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga71dd44d6977cc000c00a6176f71053c9)
- [BT_UUID_RFCOMM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafce3f7dd2fbd02c3a549f46395253cde)
- [BT_UUID_TCP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab4dac3d360e3428cc0b66e34bea75285)
- [BT_UUID_TCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga419519758947e29b8ded5209b1c47743)
- [BT_UUID_TCS_BIN_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab7f9b345cb85f922840e6e21722c3373)
- [BT_UUID_TCS_BIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5c9bd29f560d84a30c0cb009ccfdc36a)
- [BT_UUID_TCS_AT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga09236e2cc7267043f47445e7b233bc38)
- [BT_UUID_TCS_AT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga7c31eb642d9cb8231de38f25c43ef23f)
- [BT_UUID_ATT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga675b73753e13c6c6dbbc5f655b23e466)
- [BT_UUID_ATT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa91cf6c6639156a4b5c67041d479d555)
- [BT_UUID_OBEX_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab63382153f97c79f7cdcdfa0a264d6e7)
- [BT_UUID_OBEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8f660c1d39057815d0420d2dce00639e)
- [BT_UUID_IP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga5bd66bfdd6ee1f68dd2447aed448d860)
- [BT_UUID_IP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad0469b885ffe7be0ff1bef7feb2395d5)
- [BT_UUID_FTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gad8ecc3b05eb61d0a3da8daa38deb3887)
- [BT_UUID_FTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gada757111154b60d3dbb375192ec48a0f)
- [BT_UUID_HTTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafd11ab75ca80c343f894db89779419d4)
- [BT_UUID_HTTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga34afe0fe521f95f82f0c86e0de8c1d93)
- [BT_UUID_WSP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac095fdb1bc8d0a07737061b428e12071)
- [BT_UUID_WSP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga8f0f3c9e5ef2b6a313ed742a8f7ed0bd)
- [BT_UUID_BNEP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gacf6c5a3e20d50500cca56daf5802faf5)
- [BT_UUID_BNEP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9bd1756830328cacd40fc8bf80ee176d)
- [BT_UUID_UPNP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0dac826a9f670d1eba071603723fd3f5)
- [BT_UUID_UPNP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga3f7ade885937ba780b0074516c180c42)
- [BT_UUID_HIDP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac30ff318ffebd4a6793a0267de6b84e9)
- [BT_UUID_HIDP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9cbd452d2c4fa9fae46cd39bb8133ea2)
- [BT_UUID_HCRP_CTRL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaccdbcd9b4ab68185c4ba213d2b83fcf2)
- [BT_UUID_HCRP_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga731221f8f6711a400aa0e7c39c8520ea)
- [BT_UUID_HCRP_DATA_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga61619a474d5278d79bf66fcda77076f6)
- [BT_UUID_HCRP_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga0bd9a371c57ecc22cfb40b31025cc69e)
- [BT_UUID_HCRP_NOTE_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga99a3d8dfd8f46ece85f3fa5be8c94a64)
- [BT_UUID_HCRP_NOTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga85372fbf20b7d83fdf5e780487f14974)
- [BT_UUID_AVCTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga07ce8ad97e49eb94eb08a75b8fa555ca)
- [BT_UUID_AVCTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1b172e9a094474f5d7fe6b1b46dbc93e)
- [BT_UUID_AVCTP_BROWSING_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4d08c3f7d19718e9107414d111940b43)
- [BT_UUID_AVCTP_BROWSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae3f1b0e418dc12a1ef4c2d2f4f35c485)
- [BT_UUID_AVDTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga2e2934e79054324cec077903c07108ad)
- [BT_UUID_AVDTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga926c1d29d7655320c3b89558ec5b3d2f)
- [BT_UUID_CMTP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gae83a731e34ef81a8340f9c5919ad0c6f)
- [BT_UUID_CMTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaa70481ddcb90e8232b3397580c5927a0)
- [BT_UUID_UDI_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga477f7e4e7baffa502a0d8ded852ec2e7)
- [BT_UUID_UDI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gaae2132eeff69adb594365a0af0419695)
- [BT_UUID_MCAP_CTRL_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9a893aa35fe599d26b6dcfd9bd0fcb2e)
- [BT_UUID_MCAP_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga1f576ec8576152a951d44a87b8406514)
- [BT_UUID_MCAP_DATA_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gabc9726eea06d6f3cea2de134f62fb4f1)
- [BT_UUID_MCAP_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab5607157844471d48d2d1db3e295cee3)
- [BT_UUID_L2CAP_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga64e0b2fde8593ae40dfc0d661240abb4)
- [BT_UUID_L2CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga17007ef5a1e355f912af78f909a1d971)
- [BT_UUID_TYPE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ggabec48a57ba2d88c9e6006d9996a0fb43a8a5a0c5b6310aff10b182daec0e452ba)
- [BT_UUID_TYPE_32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ggabec48a57ba2d88c9e6006d9996a0fb43a27382df27b8098bf6144021c1b23c4c8)
- [BT_UUID_TYPE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ggabec48a57ba2d88c9e6006d9996a0fb43a786cbb74a1d74c77cb31ff3c4da45517)
- [bt_uuid_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafe17513c1f91cb3f3e61648b71620c6b)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_uuid_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9e260584efcc111eb3ee02bf78f01881)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_uuid_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab5ef78dd2263f08de16a0f1e764df657)
- [bt_uuid_from_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4dec477f7827ece43b91d42d75b1244b)
- [bt_uuid_compress](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga72cd2ea0cc6fedded3d1eb8f617f4c07)

<a id="header-details"></a>

---

[返回大纲](大纲.md)
