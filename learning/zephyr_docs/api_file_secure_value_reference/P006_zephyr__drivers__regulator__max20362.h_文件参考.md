---
id: learning.zephyr-docs.api-file-secure-value-reference.page-6
title: zephyr__drivers__regulator__max20362.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2regulator_2max20362_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_drivers\_\_regulator\_\_max20362.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2regulator_2max20362_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MAX20362电源管理集成电路（PMIC）稳压器驱动的公共API。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

MAX20362电源管理集成电路（PMIC）稳压器驱动的公共API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="define-members-0"></a>

### MAX20362 INT／INT_MASK 寄存器位（Register Bits，0x14／0x18）

<a id="r_ga5b1b5c774d6aebaa378d1909d31ab13f"></a>

```c
#define MAX20362_INT_CAPOVLO_MASK BIT(7)
```

相关声明：[MAX20362_INT_CAPOVLO_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga5b1b5c774d6aebaa378d1909d31ab13f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

电容过压锁定（Cap Over-voltage Lockout）。

<a id="r_gaa66b7d738c596808bf76d282f66bfcaa"></a>

```c
#define MAX20362_INT_CAPUVLO_MASK BIT(6)
```

相关声明：[MAX20362_INT_CAPUVLO_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#gaa66b7d738c596808bf76d282f66bfcaa)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

电容欠压锁定（Cap Under-voltage Lockout）。

<a id="r_ga3132a45880cdb27745b9c2563cc96b70"></a>

```c
#define MAX20362_INT_BBSTON_MASK BIT(5)
```

相关声明：[MAX20362_INT_BBSTON_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga3132a45880cdb27745b9c2563cc96b70)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

降压－升压转换（Buck-boost）开启。

<a id="r_ga0984f89a16a9472de6ea258217782b57"></a>

```c
#define MAX20362_INT_BBSTOFF_MASK BIT(4)
```

相关声明：[MAX20362_INT_BBSTOFF_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga0984f89a16a9472de6ea258217782b57)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

降压－升压转换（Buck-boost）关闭。

<a id="r_ga3403d0d0cf4a17fec8d60a5faf04a5c4"></a>

```c
#define MAX20362_INT_BBINUVLO_MASK BIT(3)
```

相关声明：[MAX20362_INT_BBINUVLO_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga3403d0d0cf4a17fec8d60a5faf04a5c4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

降压－升压输入欠压锁定（Buck-boost Input UVLO）。

<a id="r_ga179e119da832e746b3a39c325f87f60b"></a>

```c
#define MAX20362_INT_UVLO_MASK BIT(2)
```

相关声明：[MAX20362_INT_UVLO_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga179e119da832e746b3a39c325f87f60b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

欠压锁定（Undervoltage Lockout）。

<a id="r_gab5bbfb375183b969e2b31839d7db7889"></a>

```c
#define MAX20362_INT_BSTFLT_MASK BIT(1)
```

相关声明：[MAX20362_INT_BSTFLT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#gab5bbfb375183b969e2b31839d7db7889)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

升压故障（Boost Fault）。

<a id="r_ga653b9d31b1ab26d43a0b74a541ff8047"></a>

```c
#define MAX20362_INT_THMFLT_MASK BIT(0)
```

相关声明：[MAX20362_INT_THMFLT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga653b9d31b1ab26d43a0b74a541ff8047)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

热故障（Thermal Fault）。

<a id="define-members-1"></a>

### MAX20362 LDO_INT／LDO_INT_MASK 寄存器位（Register Bits，0x17／0x1B）

<a id="r_ga8b1b64a14e2f10ef953a08b7a4dbfc1c"></a>

```c
#define MAX20362_LDOINT_DIV_MASK BIT(3)
```

相关声明：[MAX20362_LDOINT_DIV_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga8b1b64a14e2f10ef953a08b7a4dbfc1c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

分压器故障（Divider Fault）。

<a id="r_ga78af4eaf13610d2f7def724266e0217c"></a>

```c
#define MAX20362_LDOINT_SHR_MASK BIT(2)
```

相关声明：[MAX20362_LDOINT_SHR_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga78af4eaf13610d2f7def724266e0217c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

短路（Short Circuit）。

<a id="r_gaa2d65dc3d622a810ba33f099a3eaf750"></a>

```c
#define MAX20362_LDOINT_THM_MASK BIT(1)
```

相关声明：[MAX20362_LDOINT_THM_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#gaa2d65dc3d622a810ba33f099a3eaf750)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

热故障（Thermal Fault）。

<a id="r_gab7e94d5d83218f6a28d37b7b96e74f2c"></a>

```c
#define MAX20362_LDOINT_CLP_MASK BIT(0)
```

相关声明：[MAX20362_LDOINT_CLP_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#gab7e94d5d83218f6a28d37b7b96e74f2c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

限流／限幅故障（Current Limit/Clipping Fault）。

<a id="define-members-2"></a>

### MAX20362 INGEN_INT／INGEN_INT_MASK 寄存器位（Register Bits，0x16／0x1A）

<a id="r_ga4184d5fb84788ab19f6639920ee2d243"></a>

```c
#define MAX20362_INGENINT_OUTTMO_MASK BIT(4)
```

相关声明：[MAX20362_INGENINT_OUTTMO_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga4184d5fb84788ab19f6639920ee2d243)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

输出超时（Output Timeout）。

<a id="r_ga886c3bd5f8f04c496566d5ae4d830f7b"></a>

```c
#define MAX20362_INGENINT_DRPMIN_MASK BIT(3)
```

相关声明：[MAX20362_INGENINT_DRPMIN_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga886c3bd5f8f04c496566d5ae4d830f7b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

压降下限（Droop Min）。

<a id="r_ga860a173430349a49c5b731d18fd6f331"></a>

```c
#define MAX20362_INGENINT_TNKTMO_MASK BIT(2)
```

相关声明：[MAX20362_INGENINT_TNKTMO_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga860a173430349a49c5b731d18fd6f331)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

储能单元超时（Tank Timeout）。

<a id="r_gaef0d64dbe97e1baa80b63d5f66edeee2"></a>

```c
#define MAX20362_INGENINT_SIMOPIN_MASK BIT(1)
```

相关声明：[MAX20362_INGENINT_SIMOPIN_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#gaef0d64dbe97e1baa80b63d5f66edeee2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

SIMO 引脚（Pin）。

<a id="r_ga54a06997b332c094d2c8451b299883a7"></a>

```c
#define MAX20362_INGENINT_DRPMAX_MASK BIT(0)
```

相关声明：[MAX20362_INGENINT_DRPMAX_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga54a06997b332c094d2c8451b299883a7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

压降上限（Droop Max）。

<a id="define-members-3"></a>

### MAX20362 中断掩码便捷值（Interrupt Mask Convenience Values）

<a id="r_gad9eabba2abf5c8deaae6270c7305bd7a"></a>

```c
#define MAX20362_INT_MASK_ALL 0xFF
```

相关声明：[MAX20362_INT_MASK_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#gad9eabba2abf5c8deaae6270c7305bd7a)。

屏蔽全部 INT 位（Mask All INT Bits）。

<a id="r_ga937da6e8b96d82a75a695d9708392d39"></a>

```c
#define MAX20362_LDO_INT_MASK_ALL 0x0F
```

相关声明：[MAX20362_LDO_INT_MASK_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga937da6e8b96d82a75a695d9708392d39)。

屏蔽全部 `LDO_INT` 位，即 `DIV | SHR | THM | CLP`。

<a id="r_gaa1465b71561aaea295636066fb6bf846"></a>

```c
#define MAX20362_INGEN_INT_MASK_ALL 0x1F
```

相关声明：[MAX20362_INGEN_INT_MASK_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#gaa1465b71561aaea295636066fb6bf846)。

屏蔽全部 `INGEN_INT` 位，即 `OUTTMO | DRPMIN | TNKTMO | SIMOPIN | DRPMAX`。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.2\_函数（Functions）

<a id="r_ga43205673ced0b689fd05cdf74e779b15"></a>

```c
int regulator_max20362_set_int_mask (const struct device *dev, uint8_t mask)
```

相关声明：[regulator_max20362_set_int_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga43205673ced0b689fd05cdf74e779b15)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 MAX20362 设备的主中断掩码（Main Interrupt Mask），即 `INT_MASK` 寄存器。

<a id="r_ga1520e58ba2864383a43508722d352b8b"></a>

```c
int regulator_max20362_set_ingen_int_mask (const struct device *dev, uint8_t mask)
```

相关声明：[regulator_max20362_set_ingen_int_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga1520e58ba2864383a43508722d352b8b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 MAX20362 设备的 Ingenuity 中断掩码（Interrupt Mask），即 `INGEN_INT_MASK` 寄存器。

<a id="r_ga702d38f23b63cefe61178245ce6491df"></a>

```c
int regulator_max20362_set_ldo_int_mask (const struct device *dev, uint8_t mask)
```

相关声明：[regulator_max20362_set_ldo_int_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga702d38f23b63cefe61178245ce6491df)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 MAX20362 设备的低压差稳压器（LDO）中断掩码，即 `LDO_INT_MASK` 寄存器。


## 6.3\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P171_max20362.h_源码浏览.md)
- [MAX20362_INT_CAPOVLO_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga5b1b5c774d6aebaa378d1909d31ab13f)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [MAX20362_INT_CAPUVLO_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#gaa66b7d738c596808bf76d282f66bfcaa)
- [MAX20362_INT_BBSTON_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga3132a45880cdb27745b9c2563cc96b70)
- [MAX20362_INT_BBSTOFF_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga0984f89a16a9472de6ea258217782b57)
- [MAX20362_INT_BBINUVLO_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga3403d0d0cf4a17fec8d60a5faf04a5c4)
- [MAX20362_INT_UVLO_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga179e119da832e746b3a39c325f87f60b)
- [MAX20362_INT_BSTFLT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#gab5bbfb375183b969e2b31839d7db7889)
- [MAX20362_INT_THMFLT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga653b9d31b1ab26d43a0b74a541ff8047)
- [MAX20362_LDOINT_DIV_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga8b1b64a14e2f10ef953a08b7a4dbfc1c)
- [MAX20362_LDOINT_SHR_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga78af4eaf13610d2f7def724266e0217c)
- [MAX20362_LDOINT_THM_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#gaa2d65dc3d622a810ba33f099a3eaf750)
- [MAX20362_LDOINT_CLP_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#gab7e94d5d83218f6a28d37b7b96e74f2c)
- [MAX20362_INGENINT_OUTTMO_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga4184d5fb84788ab19f6639920ee2d243)
- [MAX20362_INGENINT_DRPMIN_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga886c3bd5f8f04c496566d5ae4d830f7b)
- [MAX20362_INGENINT_TNKTMO_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga860a173430349a49c5b731d18fd6f331)
- [MAX20362_INGENINT_SIMOPIN_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#gaef0d64dbe97e1baa80b63d5f66edeee2)
- [MAX20362_INGENINT_DRPMAX_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga54a06997b332c094d2c8451b299883a7)
- [MAX20362_INT_MASK_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#gad9eabba2abf5c8deaae6270c7305bd7a)
- [MAX20362_LDO_INT_MASK_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga937da6e8b96d82a75a695d9708392d39)
- [MAX20362_INGEN_INT_MASK_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#gaa1465b71561aaea295636066fb6bf846)
- [regulator_max20362_set_int_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga43205673ced0b689fd05cdf74e779b15)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [regulator_max20362_set_ingen_int_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga1520e58ba2864383a43508722d352b8b)
- [regulator_max20362_set_ldo_int_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__max20362.html#ga702d38f23b63cefe61178245ce6491df)

<a id="header-details"></a>

---

[上一章](P005_zephyr__xen__dom0__domctl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__sensor__adxl355.h_文件参考.md)
