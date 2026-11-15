---
id: learning.zephyr-docs.api-source-system-reference.page-11
title: eth_nxp_enet.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/eth__nxp__enet_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_eth\_nxp\_enet.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/eth__nxp__enet_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P109_zephyr__drivers__ethernet__eth_nxp_enet.h_文件参考.md)。

## 11.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="adevice_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright 2023 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_ETH_NXP_ENET_H__
#define ZEPHYR_INCLUDE_DRIVERS_ETH_NXP_ENET_H__

/*
 * This header is for NXP ENET driver development
 * and has definitions for internal implementations
 * not to be used by application
 */

#include <zephyr/device.h>
#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif


/*
 * Reasons for callback to a driver:
 *
 * Module reset: The ENET module was reset, perhaps because of power management
 * actions, and subdriver should reinitialize part of the module.
 * Interrupt: An interrupt of a type relevant to the subdriver occurred.
 * Interrupt enable: The driver's relevant interrupt was enabled in NVIC
 */
enum nxp_enet_callback_reason {
        NXP_ENET_MODULE_RESET,
        NXP_ENET_INTERRUPT,
        NXP_ENET_INTERRUPT_ENABLED,
};

enum nxp_enet_driver {
        NXP_ENET_MAC,
        NXP_ENET_MDIO,
        NXP_ENET_PTP_CLOCK,
};

struct nxp_enet_ptp_data {
        struct k_sem ptp_ts_sem;
        struct k_mutex *ptp_mutex; /* created in PTP driver */
        void *enet; /* enet_handle poiniter used by PTP driver */
};

#ifdef CONFIG_MDIO_NXP_ENET
extern void nxp_enet_mdio_callback(const struct device *mdio_dev,
                enum nxp_enet_callback_reason event,
                void *data);
#else
#define nxp_enet_mdio_callback(...)
#endif

#ifdef CONFIG_PTP_CLOCK_NXP_ENET
extern void nxp_enet_ptp_clock_callback(const struct device *dev,
                enum nxp_enet_callback_reason event,
                void *data);
#else
#define nxp_enet_ptp_clock_callback(...)
#endif

/*
 * Internal implementation, inter-driver communication function
 *
 * dev: target device to call back
 * dev_type: which driver to call back
 * event: reason/cause of callback
 * data: opaque data, will be interpreted based on reason and target driver
 */
extern void nxp_enet_driver_cb(const struct device *dev,
                                enum nxp_enet_driver dev_type,
                                enum nxp_enet_callback_reason event,
                                void *data);


#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_ETH_NXP_ENET_H__ */
```

## 11.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 16 行

本头文件用于 NXP ENET 驱动开发（Driver Development），定义内部实现（Internal Implementations）所需的内容，不供应用程序使用。

### 注释 3：原第 31 行

调用驱动回调（Driver Callback）的原因：

- 模块复位（Module Reset）：ENET 模块已复位，可能由电源管理（Power Management）操作引起；子驱动（Subdriver）应重新初始化模块的相关部分。
- 中断（Interrupt）：发生了与子驱动相关类型的中断。
- 中断启用（Interrupt Enable）：已在嵌套向量中断控制器（NVIC）中启用与驱动相关的中断。

### 注释 4：原第 53 行

在精确时间协议驱动（PTP Driver）中创建。

### 注释 5：原第 54 行

供精确时间协议驱动（PTP Driver）使用的 `enet_handle` 指针（Pointer）。

### 注释 6：原第 73 行

内部实现（Internal Implementation），用于驱动间通信（Inter-Driver Communication）。

- `dev`：要回调的目标设备（Target Device）。
- `dev_type`：要回调哪个驱动。
- `event`：回调的原因（Reason / Cause）。
- `data`：不透明数据（Opaque Data），根据回调原因和目标驱动解释。

### 注释 7：原第 93 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_ETH_NXP_ENET_H__`。

## 11.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P109_zephyr__drivers__ethernet__eth_nxp_enet.h_文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [device](../device_reference/P002_设备对象结构.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

---

[上一章](P010_dsa_core.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P012_fs_interface.h_源码浏览.md)
